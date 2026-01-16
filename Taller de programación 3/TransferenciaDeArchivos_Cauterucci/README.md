# FileShare P2P

FileShare es una aplicación de escritorio moderna desarrollada en **Java** que permite el intercambio de archivos entre dispositivos dentro de una misma red local (LAN) de forma rápida y segura, sin necesidad de servidores externos o servicios en la nube.

Inspirada en el flujo de trabajo de herramientas como *LocalSend*, ofrece una interfaz intuitiva y automatización en el descubrimiento de pares.

## Características

- **Descubrimiento Automático:** Encuentra otros dispositivos en la red local mediante el uso de Sockets UDP (Broadcast).
- **Transferencia de Alta Velocidad:** Envío de archivos directamente de punto a punto (P2P) usando Sockets TCP.
- **Interfaz Moderna:** UI desarrollada con JavaFX y el tema profesional **AtlantaFX** (PrimerDark).
- **Feedback en tiempo real:** Barra de progreso y notificaciones visuales sobre el estado de los envíos y recepciones.
- **Seguridad Local:** Los datos nunca salen de tu red privada.

## Tecnologías utilizadas

* **Lenguaje:** [Java 17+](https://www.oracle.com/java/technologies/downloads/)
* **GUI:** [JavaFX 21](https://openjfx.io/)
* **Gestión de Dependencias:** [Maven](https://maven.apache.org/)
* **Estilos:** [AtlantaFX](https://github.com/mkpaz/atlantafx)
* **Networking:** Java Sockets (TCP para archivos, UDP para descubrimiento).

##  Instalación y Ejecución

### Requisitos previos
1.  Tener instalado **JDK 17** o superior.
2.  Tener instalado **Maven**.

### Pasos para ejecutar
1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/tu-usuario/fileshare-app.git](https://github.com/tu-usuario/fileshare-app.git)
    cd fileshare-app
    ```

2.  **Compilar el proyecto:**
    ```bash
    mvn clean compile
    ```

3.  **Lanzar la aplicación:**
    ```bash
    mvn javafx:run
    ```

## Funcionamiento

Registro: Al iniciar, eliges un nombre de usuario.

Modo Recibir: Al entrar en la pestaña "Recibir", tu dispositivo comienza a emitir una señal UDP anunciando que estás listo para aceptar archivos.

Modo Enviar: En la pestaña "Enviar", verás una lista de usuarios disponibles. Solo arrastra un archivo sobre la tarjeta del usuario y el envío comenzará mediante un Socket TCP dedicado.

Almacenamiento: Todos los archivos recibidos se guardan automáticamente en la carpeta /Downloads dentro del directorio del proyecto.

## Estructura del Proyecto

La estructura sigue el estándar de Maven:

    src/main/java/com/fileshare/
         MainApp.java            # Punto de entrada y UI
        DiscoveryService.java    # Lógica de detección UDP
        FileTransferService.java # Servidor/Cliente TCP para archivos
        Peer.java                # Modelo de datos de usuario remoto
    pom.xml                      # Configuración de dependencias
    README.md

