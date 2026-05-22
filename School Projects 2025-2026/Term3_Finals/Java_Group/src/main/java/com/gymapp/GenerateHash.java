package com.gymapp;

import org.mindrot.jbcrypt.BCrypt;

public class GenerateHash {
    public static void main(String[] args) {
        String password = "password1";
        String hash = BCrypt.hashpw(password, BCrypt.gensalt(12));

        System.out.println("Password: " + password);
        System.out.println("Hash: " + hash);
        System.out.println("Length: " + hash.length());
    }
}
