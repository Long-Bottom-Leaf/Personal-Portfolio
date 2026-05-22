package com.gymapp.util;

// Import necessary classes -- more secure and robust than java.io.*
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.logging.FileHandler;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.logging.SimpleFormatter;

public class AppLogger {
    // Logger instance
    private static final Logger logger = Logger.getLogger(AppLogger.class.getName());
    // Log file path
    private static final String LOG_FILE_PATH = "logs/app.log";

    // Static block to configure the logger
    static {
        try {
            // Ensure the logs directory exists
            Path logPath = Paths.get("logs");
            if (!Files.exists(logPath)) {
                Files.createDirectories(logPath);
            }

            // Create a FileHandler to write logs to a file
            FileHandler fileHandler = new FileHandler(LOG_FILE_PATH, true);

            // Set a simple formatter for the log messages
            fileHandler.setFormatter(new SimpleFormatter());

            // File handler to logger
            logger.addHandler(fileHandler);
            logger.setLevel(Level.ALL);

            // Log a startup message
            logger.info("Application Logger initialized.");

        } catch (IOException error) {
            System.err.println("Failed to create log directory: " + error.getMessage());
        }
    }

    // Private constructor prevents instantiation
    private AppLogger() {}

    public static Logger getLogger() {
        return logger;
    }

    // Log an info message
    public static void logInfo(String message) {
        logger.info(message);
    }

    // Log a warning message
    public static void logWarning(String message) {
        logger.warning(message);
    }

    // Log an error message
    public static void logError(String message) {
        logger.severe(message);
    }

    // Log an error with stack trace
    public static void logErrorTrace(String message, Throwable throwable) {
        logger.log(Level.SEVERE, message, throwable);
    }
}
