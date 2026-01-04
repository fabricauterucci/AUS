package com.fileshare;

import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

public class FileTransferService {
    private static final int TRANSFER_PORT = 0; // Puerto dinamico
    private static final String DOWNLOAD_DIR = "Downloads";

    private boolean running;
    private boolean waitingMode;
    private boolean fileReceived;
    private ServerSocket serverSocket;

    public int getPort() {
        return serverSocket != null ? serverSocket.getLocalPort() : -1;
    }

    public void setWaitingMode(boolean waiting) {
        this.waitingMode = waiting;
        this.fileReceived = false;
    }

    public boolean isFileReceived() {
        return fileReceived;
    }

    public void startServer() {
        new Thread(() -> {
            try {
                serverSocket = new ServerSocket(TRANSFER_PORT);
                running = true;
                System.out.println("El servidor de transferencia de archivos se ha iniciado en el puerto: " + serverSocket.getLocalPort());

                File downloadDir = new File(DOWNLOAD_DIR);
                if (!downloadDir.exists()) {
                    downloadDir.mkdirs();
                }

                while (running) {
                    Socket clientSocket = serverSocket.accept();
                    new Thread(() -> handleIncomingFile(clientSocket)).start();
                }
            } catch (IOException e) {
                if (running)
                    e.printStackTrace();
            }
        }).start();
    }

    public void stop() {
        running = false;
        try {
            if (serverSocket != null)
                serverSocket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void sendFile(String peerIp, int peerPort, File file) {
        try (Socket socket = new Socket(peerIp, peerPort);
                DataOutputStream dos = new DataOutputStream(socket.getOutputStream());
                DataInputStream dis = new DataInputStream(socket.getInputStream());
                FileInputStream fis = new FileInputStream(file)) {

            System.out.println("Enviando archivo: " + file.getName() + " hacía " + peerIp);

            // Protocolo: Nombre del archivo (UTF), Tamaño (Long), Contenido
            dos.writeUTF(file.getName());
            dos.writeLong(file.length());
            dos.flush();

            // Espera respuesta: "ACCEPTED" o "REJECTED"
            String response = dis.readUTF();
            
            if (response.equals("REJECTED")) {
                System.out.println("\n El archivo fue rechazado por el receptor.");
                return;
            }

            byte[] buffer = new byte[4096];
            int bytesRead;
            long totalSent = 0;

            while ((bytesRead = fis.read(buffer)) != -1) {
                dos.write(buffer, 0, bytesRead);
                totalSent += bytesRead;
            }

            System.out.println(" Archivo enviado exitosamente: " + file.getName());

        } catch (IOException e) {
            System.err.println(" Error al enviar el archivo: " + e.getMessage());
        }
    }

    private void handleIncomingFile(Socket socket) {
        try (DataInputStream dis = new DataInputStream(socket.getInputStream());
             DataOutputStream dos = new DataOutputStream(socket.getOutputStream())) {
            String fileName = dis.readUTF();
            long fileSize = dis.readLong();

            // Solo va a aceptar el archivo si está en modo de espera
            if (!waitingMode) {
                System.out.println("\n Archivo rechazado: " + fileName + " (No está en modo de recepción)");
                dos.writeUTF("REJECTED");
                dos.flush();
                // Consume los bytes del archivo para no dejar el socket en mal estado
                byte[] buffer = new byte[4096];
                long totalReceived = 0;
                int bytesRead;
                while (totalReceived < fileSize && (bytesRead = dis.read(buffer)) != -1) {
                    totalReceived += bytesRead;
                }
                return;
            }

            // Enviar aceptación
            dos.writeUTF("ACCEPTED");
            dos.flush();

            File file = new File(DOWNLOAD_DIR, fileName);
            System.out.println("\n Recibiendo archivo: " + fileName + " (" + fileSize + " bytes)");

            try (FileOutputStream fos = new FileOutputStream(file)) {
                byte[] buffer = new byte[4096];
                int bytesRead;
                long totalReceived = 0;

                while (totalReceived < fileSize && (bytesRead = dis.read(buffer)) != -1) {
                    fos.write(buffer, 0, bytesRead);
                    totalReceived += bytesRead;
                }
            }

            System.out.println(" Archivo recibido y guardado: " + file.getAbsolutePath());
            fileReceived = true;
            waitingMode = false;
            System.out.println("\n Presione enter para volver al menú");

        } catch (IOException e) {
            System.err.println(" Error al recibir el archivo: " + e.getMessage());
        } finally {
            try {
                socket.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
