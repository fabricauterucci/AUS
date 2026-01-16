package com.fileshare;

import atlantafx.base.theme.PrimerDark;
import javafx.animation.KeyFrame;
import javafx.animation.Timeline;
import javafx.application.Application;
import javafx.application.Platform;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.concurrent.Task;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.input.TransferMode;
import javafx.scene.layout.*;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import javafx.scene.text.FontWeight;
import javafx.stage.Modality;
import javafx.stage.Stage;
import javafx.stage.StageStyle;
import javafx.util.Duration;

import java.io.File;

public class MainApp extends Application {

    private DiscoveryService discoveryService;
    private FileTransferService fileTransferService;

    private final ObservableList<Peer> peers = FXCollections.observableArrayList();
    
    private BorderPane root = new BorderPane();
    private StackPane contentArea = new StackPane();
    private VBox sendView;
    private VBox receiveView;
    
    // Colores estilo "LocalSend" (Slate Dark)
    private final String BG_COLOR = "-fx-background-color: #0f172a;";
    private final String SIDEBAR_COLOR = "-fx-background-color: #1e293b;";
    private final String CARD_COLOR = "-fx-background-color: #334155; -fx-background-radius: 12; -fx-effect: dropshadow(three-pass-box, rgba(0,0,0,0.3), 10, 0, 0, 5);";
    private final String CARD_HOVER_COLOR = "-fx-background-color: #475569; -fx-background-radius: 12; -fx-cursor: hand;";
    private final String ACCENT_COLOR = "#3b82f6"; // Azul brillante

    @Override
    public void start(Stage stage) throws Exception {
        // Tema moderno base
        Application.setUserAgentStylesheet(new PrimerDark().getUserAgentStylesheet());

        String username = promptUsername();
        if (username == null || username.isBlank()) return;

        // Iniciar servicios
        fileTransferService = new FileTransferService();
        fileTransferService.startServer();
        // Breve pausa para asegurar que el puerto se asigne
        Thread.sleep(100); 
        
        discoveryService = new DiscoveryService(username, fileTransferService.getPort());
        discoveryService.start();

        // Construir UI
        root.setStyle(BG_COLOR);
        root.setLeft(buildSidebar());
        root.setCenter(contentArea);

        sendView = buildSendView();
        receiveView = buildReceiveView();

        contentArea.getChildren().addAll(sendView, receiveView);
        contentArea.setPadding(new Insets(20));
        
        // Estado inicial
        showSend();
        startPeerPolling();

        stage.setTitle("FileShare - " + username);
        stage.setScene(new Scene(root, 950, 650));
        stage.show();
    }

    // ================= Sidebar =================

    private VBox buildSidebar() {
        VBox sidebar = new VBox(15);
        sidebar.setPadding(new Insets(30, 20, 20, 20));
        sidebar.setStyle(SIDEBAR_COLOR);
        sidebar.setPrefWidth(220);

        Label title = new Label("FileShare");
        title.setFont(Font.font("Segoe UI", FontWeight.BOLD, 24));
        title.setTextFill(Color.WHITE);
        
        Separator sep = new Separator();
        sep.setOpacity(0.3);

        Button btnSend = createNavButton("📤  Enviar", true);
        Button btnReceive = createNavButton("📥  Recibir", false);

        btnSend.setOnAction(e -> {
            showSend();
            updateNavStyles(btnSend, btnReceive);
        });
        
        btnReceive.setOnAction(e -> {
            showReceive();
            updateNavStyles(btnReceive, btnSend);
        });

        // Footer con info
        Region spacer = new Region();
        VBox.setVgrow(spacer, Priority.ALWAYS);
        Label version = new Label("v1.0.0");
        version.setStyle("-fx-text-fill: gray; -fx-font-size: 10px;");

        sidebar.getChildren().addAll(title, sep, btnSend, btnReceive, spacer, version);
        
        // Activar estilo inicial
        updateNavStyles(btnSend, btnReceive);
        
        return sidebar;
    }

    private Button createNavButton(String text, boolean isActive) {
        Button btn = new Button(text);
        btn.setMaxWidth(Double.MAX_VALUE);
        btn.setAlignment(Pos.CENTER_LEFT);
        btn.setPadding(new Insets(12, 15, 12, 15));
        btn.setFont(Font.font("Segoe UI", 16));
        return btn;
    }

    private void updateNavStyles(Button active, Button inactive) {
        active.setStyle("-fx-background-color: " + ACCENT_COLOR + "; -fx-text-fill: white; -fx-background-radius: 8;");
        inactive.setStyle("-fx-background-color: transparent; -fx-text-fill: #94a3b8;");
    }

    // ================= Send View =================

    private VBox buildSendView() {
        VBox layout = new VBox(20);
        
        Label header = new Label("Dispositivos Cercanos");
        header.setFont(Font.font("Segoe UI", FontWeight.BOLD, 22));
        header.setTextFill(Color.WHITE);

        Label subHeader = new Label("Arrastra un archivo sobre un usuario para enviarlo.");
        subHeader.setTextFill(Color.web("#94a3b8"));

        TilePane grid = new TilePane();
        grid.setHgap(20);
        grid.setVgap(20);
        grid.setPrefColumns(3);

        // Listener para actualizar la lista de usuarios
        peers.addListener((javafx.collections.ListChangeListener<Peer>) c -> {
            grid.getChildren().clear();
            boolean found = false;
            for (Peer p : peers) {
                if (p.isWaitingForFiles()) {
                    grid.getChildren().add(createPeerCard(p));
                    found = true;
                }
            }
            if (!found) {
                Label placeholder = new Label("No hay nadie esperando archivos...");
                placeholder.setTextFill(Color.GRAY);
                grid.getChildren().add(placeholder);
            }
        });

        layout.getChildren().addAll(header, subHeader, grid);
        return layout;
    }

    private VBox createPeerCard(Peer peer) {
        VBox card = new VBox(10);
        card.setPadding(new Insets(20));
        card.setPrefSize(200, 140);
        card.setStyle(CARD_COLOR);
        
        // Efecto Hover
        card.setOnMouseEntered(e -> card.setStyle(CARD_HOVER_COLOR));
        card.setOnMouseExited(e -> card.setStyle(CARD_COLOR));

        Label icon = new Label("👤");
        icon.setStyle("-fx-font-size: 30px;");
        
        Label name = new Label(peer.getName());
        name.setStyle("-fx-font-size: 16px; -fx-font-weight: bold; -fx-text-fill: white;");
        
        Label ip = new Label(peer.getAddress().getHostAddress());
        ip.setStyle("-fx-text-fill: #94a3b8; -fx-font-size: 12px;");

        card.getChildren().addAll(icon, name, ip);

        // Drag & Drop
        card.setOnDragOver(e -> {
            if (e.getDragboard().hasFiles()) {
                e.acceptTransferModes(TransferMode.COPY);
                card.setStyle("-fx-background-color: " + ACCENT_COLOR + "; -fx-background-radius: 12;");
            }
            e.consume();
        });

        card.setOnDragExited(e -> card.setStyle(CARD_COLOR));

        card.setOnDragDropped(e -> {
            File file = e.getDragboard().getFiles().get(0);
            e.setDropCompleted(true);
            
            // Iniciar envío con UI de progreso
            startSendingTask(peer, file);
            
            e.consume();
        });

        return card;
    }

    // ================= Send Progress Dialog =================
    
 // En MainApp.java

    private void startSendingTask(Peer peer, File file) {
        // 1. Cambiamos Task<Void> a Task<Boolean>
        Task<Boolean> sendTask = new Task<>() {
            @Override
            protected Boolean call() throws Exception {
                // Ahora capturamos el resultado del envío
                return fileTransferService.sendFile(
                    peer.getAddress().getHostAddress(),
                    peer.getTcpPort(),
                    file
                );
            }
        };

        // ... (Configuración del diálogo igual que antes) ...
        Stage dialog = new Stage();
        dialog.initModality(Modality.APPLICATION_MODAL);
        dialog.initStyle(StageStyle.UTILITY);
        dialog.setTitle("Enviando archivo...");

        VBox dialogRoot = new VBox(20);
        dialogRoot.setAlignment(Pos.CENTER);
        dialogRoot.setPadding(new Insets(30));
        dialogRoot.setStyle("-fx-background-color: #0f172a;");
        
        // ... (Labels y ProgressBar iguales que antes) ...
        Label statusLabel = new Label("Conectando con " + peer.getName() + "...");
        statusLabel.setStyle("-fx-text-fill: white;");
        ProgressBar pb = new ProgressBar();
        pb.setProgress(ProgressBar.INDETERMINATE_PROGRESS);

        dialogRoot.getChildren().addAll(statusLabel, pb);
        dialog.setScene(new Scene(dialogRoot));

        // 2. Lógica al terminar la tarea
        sendTask.setOnSucceeded(e -> {
            dialog.close();
            boolean success = sendTask.getValue(); // <--- Leemos el resultado (true/false)

            if (success) {
                Alert alert = new Alert(Alert.AlertType.INFORMATION);
                alert.setHeaderText("¡Éxito!");
                alert.setContentText("Archivo enviado correctamente.");
                alert.show();
            } else {
                // AQUI mostramos el error si fue rechazado
                Alert alert = new Alert(Alert.AlertType.ERROR);
                alert.setHeaderText("Envío fallido");
                alert.setContentText("El usuario rechazó el archivo o hubo un error de conexión.");
                alert.show();
            }
        });

        sendTask.setOnFailed(e -> {
            dialog.close();
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setHeaderText("Error Crítico");
            alert.setContentText("Ocurrió un error inesperado en la aplicación.");
            alert.show();
        });

        new Thread(sendTask).start();
        dialog.show();
    }

    // ================= Receive View =================

    private VBox buildReceiveView() {
        VBox box = new VBox(20);
        box.setAlignment(Pos.CENTER);
        box.setPadding(new Insets(40));

        Label icon = new Label("📡");
        icon.setStyle("-fx-font-size: 60px;");

        Label title = new Label("Modo Recepción Activo");
        title.setFont(Font.font("Segoe UI", FontWeight.BOLD, 24));
        title.setTextFill(Color.WHITE);
        
        Label subtitle = new Label("Eres visible para otros dispositivos como: " + discoveryService.getName());
        subtitle.setTextFill(Color.web("#94a3b8"));

        ProgressBar bar = new ProgressBar();
        bar.setPrefWidth(300);
        bar.setProgress(0); // Se quedará en 0 hasta que implementemos el reporte de progreso en recepción

        Label status = new Label("Esperando conexión...");
        status.setStyle("-fx-text-fill: gray;");

        box.getChildren().addAll(icon, title, subtitle, bar, status);

        fileTransferService.fileReceivedProperty().addListener((obs, oldVal, newVal) -> {
            if (newVal) {
                Platform.runLater(() -> {
                    // Mostrar una alerta o notificación de éxito
                    Alert alert = new Alert(Alert.AlertType.INFORMATION);
                    alert.setTitle("Archivo Recibido");
                    alert.setHeaderText(null);
                    alert.setContentText("¡Has recibido un nuevo archivo en la carpeta Downloads!");
                    alert.show();
                });
            }
        });
        return box;
    }

    // ================= Helpers =================

    private void showSend() {
        sendView.setVisible(true);
        receiveView.setVisible(false);
        fileTransferService.setWaitingMode(false);
        discoveryService.setWaitingForFiles(false);
    }

    private void showReceive() {
        sendView.setVisible(false);
        receiveView.setVisible(true);
        fileTransferService.setWaitingMode(true);
        discoveryService.setWaitingForFiles(true);
    }

    private void startPeerPolling() {
        Timeline t = new Timeline(
            new KeyFrame(Duration.seconds(2), e -> {
                Platform.runLater(() -> 
                    peers.setAll(discoveryService.getPeers())
                );
            })
        );
        t.setCycleCount(Timeline.INDEFINITE);
        t.play();
    }

    private String promptUsername() {
        TextInputDialog d = new TextInputDialog("Usuario-" + (int)(Math.random()*1000));
        d.setTitle("Bienvenido");
        d.setHeaderText("Configuración inicial");
        d.setContentText("Elige un nombre para que te reconozcan:");
        d.setGraphic(null);
        return d.showAndWait().orElse(null);
    }

    @Override
    public void stop() {
        if (discoveryService != null) discoveryService.stop();
        if (fileTransferService != null) fileTransferService.stop();
    }
}