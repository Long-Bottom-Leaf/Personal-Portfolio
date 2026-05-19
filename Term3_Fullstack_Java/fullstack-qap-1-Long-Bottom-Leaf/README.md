# Secure Password Generator (Node.js)

## 📌 Overview
This project is a **command-line password generator** built with Node.js.  
It allows you to generate secure, random passwords using a variety of customizable options such as length and character sets (lowercase, uppercase, numbers, and symbols).  

The program uses Node's built-in `crypto` module to ensure **cryptographically secure randomness**.

---

## How to use!

## 1. Clone and install

    ```bash
    git clone <git clone https://github.com/Keyin-S3-SD14/fullstack-qap-1-Long-Bottom-Leaf.git>
    cd <fullstack-qap-1-Long-Bottom-Leaf>
    npm install
    ```

### 2. Run the Generator

    ```bash
    node src/passwordGenerator.js [options]
    ```

### 3. Select from these options

    Options:

    ---help                 Show help message
    ---length               Set password length
    ---lowercase            Include lowercase letters
    ---uppercase            Include uppercase letters
    ---numbers              Include numbers
    ---symbols              Include symbols

### 4. Some Examples

    # Default (8 characters, uppercase only)
    node src/passwordGenerator.js

    # 12 characters, lowercase + numbers
    node src/passwordGenerator.js --length 12 --lowercase --numbers

    # 20 characters, all character sets
    node src/passwordGenerator.js --length 20 --lowercase --uppercase --numbers --symbols

    # Show help
    node src/passwordGenerator.js --help

### 5. Running Tests

    ```bash
    npm run test
    ```