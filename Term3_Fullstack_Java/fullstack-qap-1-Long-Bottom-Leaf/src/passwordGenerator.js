import crypto from "crypto";

// character sets
const LOWERCASE = "abcdefghijklmnopqrstuvwxyz";
const UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const NUMBERS = "0123456789";
const SYMBOLS = "!@#$%^&*()-_=+[]{}|;:,.<>?/`~";

// help function
function printHelp() {
    console.log(`How to run: node src/passwordGenerator.js [options]
    Options:
        --help           Show this help message
        --length <num>   Specify password length (default: 8)
        --lowercase      Include lowercase letters
        --uppercase      Include uppercase letters (default)
        --numbers        Include numbers
        --symbols        Include symbols`);
}

// Generate password
export function generatePassword(length, useLowercase, useUppercase, useNumbers, useSymbols) {      // 'use' initiates the flags as a boolean
    const characterSets = [];               // initiate an empty array to hold selected character sets
    if (useLowercase) characterSets.push(LOWERCASE);
    if (useUppercase) characterSets.push(UPPERCASE);
    if (useNumbers) characterSets.push(NUMBERS);
    if (useSymbols) characterSets.push(SYMBOLS);

    if (characterSets.length === 0) {       // check at least one set was selected
        throw new Error("At least one character type must be selected.");
    }

    const allCharacters = characterSets.join("");   // combine selected sets into one string
    const passwordLength = length;                  // use the specified length, while later ensuring the default of 8 if none is specified

    let password = "";                    // initiate empty string to hold the generated password
    for (let i = 0; i < passwordLength; i++) {
        const charIdx = crypto.randomInt(0, allCharacters.length);
        password += allCharacters[charIdx];
    }

    return password;
}

// Create a default configuration and parse command lines
function parseArgs(argv) {
    const config = {
        length: 8,
        useLowercase: false,
        useUppercase: true,
        useSymbols: false,
        useNumbers: false,
        help: false,
    };

    for (let i = 2; i < argv.length; i++) {     // start at index 2 to skip 'node' and script name in terminal, accepting other inputs
        switch (argv[i]) {                      // switch case to validate the inputs/flags and apply to the config object
            case "--help":
                config.help = true;
            break;

            case "--length":
                if (i + 1 >= argv.length) throw new Error("Missing value for --length");
                const length = parseInt(argv[++i], 10);

                if (isNaN(length) || length <= 0) throw new Error("Invalid length value");
                config.length = length;
            break;

            case "--lowercase":
                config.useLowercase = true;
            break;

            case "--uppercase":
                config.useUppercase = true;
            break;

            case "--numbers":
                config.useNumbers = true;
            break;

            case "--symbols":
                config.useSymbols = true;
            break;

            default:
                throw new Error(`Unknown flag: ${argv[i]}`);
        }
    }

    return config;
}

// Entry point for the program to actually run
function main() {
    try {
        const config = parseArgs(process.argv);

        if (config.help) {
                printHelp();
                return;
        }

        const password = generatePassword(
            config.length,
            config.useLowercase,
            config.useUppercase,
            config.useNumbers,
            config.useSymbols
        );

        console.log(password);
    } catch (err) {
        console.error("Error:", err.message);
        process.exit(1);
    }
}

main();
