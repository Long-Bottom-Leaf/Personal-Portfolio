package com.gymapp.util;

import java.util.logging.Logger;

public class LoggerTest {
    public static void main(String[] args) {
        Logger logger = AppLogger.getLogger();
        logger.info("Test log entry");
        logger.warning("Test warning");
        logger.severe("Test error");
    }
}