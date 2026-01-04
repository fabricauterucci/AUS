package com.fileshare;

import java.io.File;
import java.net.SocketException;
import java.util.Collection;
import java.util.Scanner;

public class Main {
    private static DiscoveryService discoveryService;
    private static FileTransferService fileTransferService;
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.println(" *** Aplicación FileShare *** \n");
        System.out.print(" Por favor, ingrese su usuario: ");
        String username = scanner.nextLine();

        fileTransferService = new FileTransferService();
        fileTransferService.startServer();

        // Espero un poco a que el servidor se inicie y se conecte a un puerto
        try {
            Thread.sleep(100);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

        int tcpPort = fileTransferService.getPort();
        System.out.println("\n Transferencia de archivos escuchando en el puerto: " + tcpPort);

        discoveryService = new DiscoveryService(username, tcpPort);

        try {
            discoveryService.start();
        } catch (SocketException e) {
            System.err.println("\n Ocurrió un fallo al iniciar los servicios: " + e.getMessage());
            return;
        }

        boolean running = true;
        while (running) {
            printMenu();
            String choice = scanner.nextLine();

            switch (choice) {
                case "1":
                    listPeers();
                    break;
                case "2":
                    sendFile();
                    break;
                case "3":
                    waitForFiles();
                    break;
                case "4":
                    running = false;
                    break;
                default:
                    System.out.println("\n Opción invalida.");
            }
        }

        System.out.println("\n Suspendiendo servicios...");
        discoveryService.stop();
        fileTransferService.stop();
        System.out.println("\n*** Gracias por usar la app de FileShare. ***\n");
    }

    private static void printMenu() {
        System.out.println("\n *** Menu *** ");
        System.out.println(" 1. Listar usuarios");
        System.out.println(" 2. Enviar archivo a un usuario");
        System.out.println(" 3. Recibir archivos");
        System.out.println(" 4. Salir");
        System.out.print(" Porfavor, elija una opción: \n");
    }

    private static void listPeers() {
        Collection<Peer> peers = discoveryService.getPeers();
        if (peers.isEmpty()) {
            System.out.println(" No se encontraron usuarios.");
        } else {
            System.out.println(" *** Peers / Usuarios *** \n");
            int i = 1;
            for (Peer peer : peers) {
                System.out.println(i + ". " + peer);
                i++;
            }
        }
    }

    private static void sendFile() {
        Collection<Peer> allPeers = discoveryService.getPeers();
        // Filtrar solo los peers que están esperando archivos
        Collection<Peer> waitingPeers = new java.util.ArrayList<>();
        for (Peer peer : allPeers) {
            if (peer.isWaitingForFiles()) {
                waitingPeers.add(peer);
            }
        }
        
        if (waitingPeers.isEmpty()) {
            System.out.println("\n No hay usuarios esperando recibir archivos.");
            return;
        }

        System.out.println(" *** Peers / Usuarios (Esperando archivos) *** \n");
        int i = 1;
        for (Peer peer : waitingPeers) {
            System.out.println(i + ". " + peer);
            i++;
        }
        
        System.out.print("\n Porfavor, seleccione el numero del usuario para transferirle el archivo: ");
        try {
            int peerIndex = Integer.parseInt(scanner.nextLine()) - 1;
            if (peerIndex < 0 || peerIndex >= waitingPeers.size()) {
                System.out.println("\n Selección de usuario inválido.");
                return;
            }

            Peer targetPeer = (Peer) waitingPeers.toArray()[peerIndex];

            System.out.print("\n Porfavor, ingrese la ruta del archivo a enviar: ");
            String filePath = scanner.nextLine();
            File file = new File(filePath);

            if (file.exists() && file.isFile()) {
                fileTransferService.sendFile(targetPeer.getAddress().getHostAddress(), targetPeer.getTcpPort(), file);
            } else {
                System.out.println("\n Archivo no encontrado o no es un archivo valido.");
            }

        } catch (NumberFormatException e) {
            System.out.println("Input incorrecto.");
        }
    }

    private static void waitForFiles() {
        System.out.println("\n Esperando archivos... (presione Enter para cancelar)");
        fileTransferService.setWaitingMode(true);
        discoveryService.setWaitingForFiles(true);
        
        // Crear un thread que monitorea si se recibió un archivo
        Thread monitorThread = new Thread(() -> {
            while (fileTransferService.isFileReceived() == false && !Thread.currentThread().isInterrupted()) {
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    break;
                }
            }
        });
        monitorThread.start();
        
        scanner.nextLine();
        monitorThread.interrupt();
        fileTransferService.setWaitingMode(false);
        discoveryService.setWaitingForFiles(false);
        
        if (!fileTransferService.isFileReceived()) {
            System.out.println("\n Dejó de esperar archivos.");
        }
    }
}
