package com.fileshare;

import java.net.InetAddress;
import java.util.Objects;

public class Peer {
    private InetAddress address; //dirección IP del dispositivo
    private String name;
    private int tcpPort; //el puerto TCP donde ese peer/usuario está escuchando para transferir archivos
    private long lastSeen; //indica cuándo fue la última vez que se detectó activo
    private boolean waitingForFiles; //indica si está esperando recibir archivos 

    
    /*Cuando se crea un peer/usuario, guarda su IP, nombre y puerto. 
     * Ademas marco el momento actual como última vez visto.
     */
    public Peer(InetAddress address, String name, int tcpPort, boolean waitingForFiles) {
        this.address = address;
        this.name = name;
        this.tcpPort = tcpPort;
        this.lastSeen = System.currentTimeMillis();
        this.waitingForFiles = waitingForFiles;
    }

    public InetAddress getAddress() {
        return address;
    }

    public String getName() {
        return name;
    }

    public int getTcpPort() {
        return tcpPort;
    }

    public long getLastSeen() {
        return lastSeen;
    }

    public boolean isWaitingForFiles() {
        return waitingForFiles;
    }

    public void setWaitingForFiles(boolean waitingForFiles) {
        this.waitingForFiles = waitingForFiles;
    }

    /*
     * Marca de tiempo cuando se vuelve a detectar el peer en la red.
	 *	Actualiza cuando se enviauna señal de emision y el usuario/peer responde 
     */
    public void updateLastSeen() {
        this.lastSeen = System.currentTimeMillis();
    }

    
    /*
     * Se considera que dos peers son iguales si tienen la misma dirección IP, sin importar el nombre o puerto
     *  Para: guardarlos en un HashSet sin duplicados, buscar ó actualizar peers
     */
    @Override
    public boolean equals(Object o) {
        if (this == o)
            return true;
        if (o == null || getClass() != o.getClass())
            return false;
        Peer peer = (Peer) o;
        return Objects.equals(address, peer.address);
    }

    @Override
    public int hashCode() {
        return Objects.hash(address);
    }

    @Override
    public String toString() {
        return name + " (" + address.getHostAddress() + ":" + tcpPort + ")";
    }
}
