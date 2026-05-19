import { generatePassword } from "../src/passwordGenerator.js";

describe("generatePassword", () => {

    // Test password length
        test("Generates password of the correct length -- more than default (8)", () => {
            const password = generatePassword(12, true, true, true, true);
            expect(password).toHaveLength(12);
        });

        test("Generates password of the correct length -- less than default (8)", () => {
            const password = generatePassword(6, true, true, true, true);
            expect(password).toHaveLength(6);
        });

        test("Generate password of default length (8) when no length specified", () => {
            const password = generatePassword(undefined, true, true, true, true);
            expect(password).toHaveLength(8);
        });

    // Test 1 character set inclusion
        test("Includes only lowercase letters when only lowercase is selected", () => {
            const password = generatePassword(10, true, false, false, false);
            expect(password).toMatch(/^[a-z]+$/);
        });

        test("Includes only uppercase letters when only uppercase is selected", () => {
            const password = generatePassword(10, false, true, false, false);
            expect(password).toMatch(/^[A-Z]+$/);
        });

        test("Includes only numbers when only numbers are selected", () => {
            const password = generatePassword(10, false, false, true, false);
            expect(password).toMatch(/^[0-9]+$/);
        });

        test("Includes only symbols when only symbols are selected", () => {
            const password = generatePassword(10, false, false, false, true);
            expect(password).toMatch(/^[!@#$%^&*()\-_=+\[\]{}|;:,.<>?/`~]+$/);
        });

    // Test multiple character set inclusion
        test("Includes only lowercase AND uppercase letters when selected", () => {
            const password = generatePassword(10, true, true, false, false);
            expect(password).toMatch(/^[a-zA-Z]+$/);
        });

        test("Includes only uppercase letters AND numbers when selected", () => {
            const password = generatePassword(10, false, true, true, false);
            expect(password).toMatch(/^[A-Z0-9]+$/);
        });

        test("Includes only numbers AND symbols when selected", () => {
            const password = generatePassword(10, false, false, true, true);
            expect(password).toMatch(/^[0-9!@#$%^&*()\-_=+\[\]{}|;:,.<>?/`~]+$/);
        });

        test("Includes only lowercase letters AND symbols when selected", () => {
            const password = generatePassword(10, true, false, false, true);
            expect(password).toMatch(/^[a-z!@#$%^&*()\-_=+\[\]{}|;:,.<>?/`~]+$/);
        });

    // Test not selecting any character sets
        test("Throws error if no character sets are selected", () => {
            expect(() => generatePassword(10, false, false, false, false)).toThrow("At least one character type must be selected.");
        });

    // test to make sure randomness is working, however this is a chance it may fail if the same password is generated twice
        test("Generates different passwords each time (randomness)", () => {
            const pass1 = generatePassword(15, true, true, true, true);
            const pass2 = generatePassword(15, true, true, true, true);

            expect(pass1).not.toBe(pass2);
        });
});
