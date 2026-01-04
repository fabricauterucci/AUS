package com.fileshare;

import java.io.IOException;
import java.net.*;
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;

public class DiscoveryService {
    private static final int DISCOVERY_PORT = 8888;
    private static final String BROADCAST_MESSAGE = "HOLA_FILESHARE";
    private static final int BROADCAST_INTERVAL_MS = 2000;
    private static final int PEER_TIMEOUT_MS = 5000;

    private DatagramSocket socket;
    private boolean running;
    private final Map<String, Peer> peers = new ConcurrentHashMap<>();
    private final String myName;
    private final int myTcpPort;
    private boolean waitingForFiles;

    public DiscoveryService(String myName, int myTcpPort) {
        this.myName = myName;
        this.myTcpPort = myTcpPort;
        this.waitingForFiles = false;
    }

    public void setWaitingForFiles(boolean waiting) {
        this.waitingForFiles = waiting;
    }

    public void start() throws SocketException {
        // Uso SO_REUSEADDR para permitir múltiples instancias en la misma pc
        socket = new DatagramSocket(null);
        socket.setReuseAddress(true);
        socket.bind(new InetSocketAddress(DISCOVERY_PORT));
        socket.setBroadcast(true);
        running = true;

        // Hilo listener 
        new Thread(this::listen).start();

        // Hilo Broadcaster ó Emisor de señal
        new Thread(this::broadcastLoop).start();

        // Hilo de limpieza
        new Thread(this::cleanupLoop).start();

        System.out.println("\n El servicio Discovery inició en el puerto: " + DISCOVERY_PORT);
    }

    public void stop() {
        running = false;
        if (socket != null && !socket.isClosed()) {
            socket.close();
        }
    }

    public Collection<Peer> getPeers() {
        return new ArrayList<>(peers.values());
    }

    private void listen() {
        byte[] buffer = new byte[1024];
        while (running) {
            try {
                DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
                socket.receive(packet);

                String message = new String(packet.getData(), 0, packet.getLength());
                InetAddress address = packet.getAddress();

                // Ignorar emisiones propias
                if (isOwnAddress(address)) {
                    // Si es nuestra propia IP, podría ser un proceso diferente.
                }

                if (message.startsWith(BROADCAST_MESSAGE)) {
                    // El formato es : HOLA_FILESHARE:<Name>:<TcpPort>:<WaitingForFiles>
                    String[] parts = message.split(":");
                    if (parts.length >= 3) {
                        String peerName = parts[1];
                        int peerTcpPort = Integer.parseInt(parts[2]);
                        boolean peerWaiting = parts.length >= 4 && parts[3].equals("1");

                        // Don't add ourselves
                        if (peerName.equals(myName) && peerTcpPort == myTcpPort)
                            continue;

                        String key = address.getHostAddress() + ":" + peerTcpPort;
                        peers.compute(key, (k, v) -> {
                            if (v == null) {
                                System.out.println("Nuevo usuario encontrado: " + peerName + " (" + address.getHostAddress() + ":"
                                        + peerTcpPort + ")");
                                return new Peer(address, peerName, peerTcpPort, peerWaiting);
                            } else {
                                v.updateLastSeen();
                                v.setWaitingForFiles(peerWaiting);
                                return v;
                            }
                        });
                    }
                }
            } catch (IOException | NumberFormatException e) {
                if (running)
                    e.printStackTrace();
            }
        }
    }

    private void broadcastLoop() {
        while (running) {
            try {
                String msg = BROADCAST_MESSAGE + ":" + myName + ":" + myTcpPort + ":" + (waitingForFiles ? "1" : "0");
                byte[] data = msg.getBytes();
                DatagramPacket packet = new DatagramPacket(data, data.length,
                        InetAddress.getByName("255.255.255.255"), DISCOVERY_PORT);
                socket.send(packet);
                Thread.sleep(BROADCAST_INTERVAL_MS);
            } catch (Exception e) {
                if (running)
                    e.printStackTrace();
            }
        }
    }

    private void cleanupLoop() {
        while (running) {
            try {
                long now = System.currentTimeMillis();
                peers.entrySet().removeIf(entry -> (now - entry.getValue().getLastSeen()) > PEER_TIMEOUT_MS);
                Thread.sleep(PEER_TIMEOUT_MS);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }
    }

    private boolean isOwnAddress(InetAddress addr) {
        try {
            return NetworkInterface.getByInetAddress(addr) != null;
        } catch (SocketException e) {
            return false;
        }
    }
}
