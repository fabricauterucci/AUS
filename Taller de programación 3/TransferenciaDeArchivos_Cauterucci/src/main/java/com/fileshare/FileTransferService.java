package com.fileshare;

import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import javafx.beans.property.BooleanProperty;
import javafx.beans.property.SimpleBooleanProperty;
import javafx.application.Platform;

public class FileTransferService {
    private static final int TRANSFER_PORT = 0; 
    private static final String DOWNLOAD_DIR = "Downloads";

    private boolean running;
    private boolean waitingMode;
    private final BooleanProperty fileReceived = new SimpleBooleanProperty(false);
    private ServerSocket serverSocket;

    public int getPort() {
        return serverSocket != null ? serverSocket.getLocalPort() : -1;
    }

    public void setWaitingMode(boolean waiting) {
        this.waitingMode = waiting;
        this.fileReceived.set(false);
    }

    public BooleanProperty fileReceivedProperty() {
        return fileReceived;
    }

    // --- EL MÉTODO QUE FALTABA ---
    public boolean sendFile(String host, int port, File file) {
        try (Socket socket = new Socket(host, port);
             DataOutputStream dos = new DataOutputStream(socket.getOutputStream());
             DataInputStream dis = new DataInputStream(socket.getInputStream());
             FileInputStream fis = new FileInputStream(file)) {

            // 1. Enviar metadatos
            dos.writeUTF(file.getName());
            dos.writeLong(file.length());
            dos.flush();

            // 2. Esperar confirmación
            String response = dis.readUTF(); 
            if (!"ACCEPTED".equals(response)) return false;

            // 3. Enviar bytes
            byte[] buffer = new byte[4096];
            int bytesRead;
            while ((bytesRead = fis.read(buffer)) != -1) {
                dos.write(buffer, 0, bytesRead);
            }
            dos.flush();
            return true;

        } catch (IOException e) {
            e.printStackTrace();
            return false;
        }
    }

    public void startServer() {
        new Thread(() -> {
            try {
                serverSocket = new ServerSocket(TRANSFER_PORT);
                running = true;
                File downloadDir = new File(DOWNLOAD_DIR);
                if (!downloadDir.exists()) downloadDir.mkdirs();

                while (running) {
                    Socket clientSocket = serverSocket.accept();
                    new Thread(() -> handleIncomingFile(clientSocket)).start();
                }
            } catch (IOException e) {
                if (running) e.printStackTrace();
            }
        }).start();
    }

    private void handleIncomingFile(Socket socket) {
        try (DataInputStream dis = new DataInputStream(socket.getInputStream());
             DataOutputStream dos = new DataOutputStream(socket.getOutputStream())) {

            String fileName = dis.readUTF();
            long fileSize = dis.readLong();

            if (!waitingMode) {
                dos.writeUTF("REJECTED");
                return;
            }

            dos.writeUTF("ACCEPTED");
            dos.flush();

            File file = new File(DOWNLOAD_DIR, fileName);
            try (FileOutputStream fos = new FileOutputStream(file)) {
                byte[] buffer = new byte[4096];
                int bytesRead;
                long totalReceived = 0;
                while (totalReceived < fileSize && (bytesRead = dis.read(buffer)) != -1) {
                    fos.write(buffer, 0, bytesRead);
                    totalReceived += bytesRead;
                }
            }

            // Notificamos a la UI que llegó algo
            Platform.runLater(() -> {
                fileReceived.set(false);
                fileReceived.set(true);
            });

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void stop() {
        running = false;
        try { if (serverSocket != null) serverSocket.close(); } catch (IOException e) { }
    }
}