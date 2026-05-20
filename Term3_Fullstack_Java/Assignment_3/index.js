// ==============================
// Imports
// ==============================

    const express = require("express");
    const path = require("path");
    const session = require("express-session");
    const bcrypt = require("bcrypt");
    const { error } = require("console");

    const app = express();
    const PORT = 3000;

    const saltRounds = 10;

// ==============================
// Config
// ==============================

    app.use(express.urlencoded({ extended: true }));
    app.use(express.static(path.join(__dirname, "public")));

    app.use(
        session({
            secret: "A8mxN0HkYEg2jLz55FfFTmS9QwKa30p1aD",
            resave: false,
            saveUninitialized: true,
        })
    );

    app.set("view engine", "ejs");
    app.set("views", path.join(__dirname, "views"));

// ==============================
// In-Memory Data Stores
// ==============================

    const USERS = [
        {
            id: 1,
            username: "AdminUser",
            email: "admin@example.com",
            password: 'adminPassword', // will be hashed on startup
            role: "admin",
            hasRSVPed: false,
            rsvpTime: null
        },
        {
            id: 2,
            username: "Regular-User",
            email: "user@example.com",
            password: "userPassword",
            role: "user",
            hasRSVPed: false,
            rsvpTime: null
        },
    ];

    const RSVPS = [];

// ==============================
// Hash Existing User Passwords
// ==============================

    async function hashExistingUserPasswords() {
        for (let user of USERS) {
            if (!user.password.startsWith("$2b$")) {
                user.password = await bcrypt.hash(user.password, saltRounds);
            }
        }
    }

// ==============================
// Redirect Based on Role
// ==============================

    function redirectBasedOnRole(request, response) {
        const user = request.session.user;
        if (!user) return response.redirect("/");

        if (user.role === "admin") {
            return response.redirect("/adminLanding");

        } else {
            return response.redirect("/userLanding");
        }
    }

// ==============================
// Login Routes
// ==============================

    app.get("/login", (request, response) => {
        response.render("login", { error: null });
    });

    app.post("/login", async (request, response) => {
        const { email, password } = request.body;
        const errorMessage = "Invalid credentials!";

        // validate input
        if (!email || !password) return response.render("login", { error: errorMessage });

        const user = USERS.find(user => user.email.toLowerCase() === email.trim().toLowerCase());
        if (!user) return response.render("login", { error: errorMessage });

        try {
            const validPassword = await bcrypt.compare(password, user.password);
            if (!validPassword) return response.render("login", { error: errorMessage });

        } catch (error) {
            console.error("Error comparing passwords:", error);
            return response.render("login", { error: "An error occurred, please try again." });
        }

        // login successful
        request.session.user = {
            id: user.id,
            username: user.username,
            email: user.email,
            role: user.role,
            hasRSVPed: user.hasRSVPed
        };

        redirectBasedOnRole(request, response);
    });


// ==============================
// Signup Routes
// ==============================

    app.get("/signup", (request, response) => {
        response.render("signup", { error: null });
    });

    app.post("/signup", async (request, response) => {
        let { username, email, password } = request.body;

        if (!username || !email || !password) {
            return response.render("signup", { error: "All fields are required!" });
        }

        // normalize
        username = username.trim().toLowerCase();
        email = email.trim().toLowerCase();
        password = password.trim().toLowerCase();

        // username validation
        const usernameRegex = /^[a-zA-Z0-9_-]{3,20}$/;
        if (!usernameRegex.test(username)) {
            return response.render("signup", {
                error: "Username must be 3-20 characters (letters, numbers, dashes, underscores!)."
            });
        }

        // email validation
        if (!email.includes("@") || !email.includes(".")) {
            return response.render("signup", { error: "Please enter a valid email!" });
        }

        // password validation
        const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
        if (!passwordRegex.test(password)) {
            return response.render("signup", {
                error: "Password must be at least 8 characters long and include at least one uppercase letter, one lowercase letter, one number, and one special character."
            });
        };

        // unique username + email check
        const existingUser = USERS.find(
            user => user.email.toLowerCase() === email || user.username.toLowerCase() === username
        );

        if (existingUser) {
            return response.render("signup", { error: "Username or email already in use!" });
        }

        const hashedPassword = await bcrypt.hash(password, saltRounds);

        const newUser = {
            id: USERS.length + 1,
            username,
            email,
            password: hashedPassword,
            role: "user",
            hasRSVPed: false,
            rsvpTime: null
        };

        USERS.push(newUser);

        request.session.user = {
            id: newUser.id,
            username: newUser.username,
            email: newUser.email,
            role: newUser.role,
            hasRSVPed: newUser.hasRSVPed
        };

        redirectBasedOnRole(request, response);
    });


// ==============================
// Home Route
// ==============================

    app.get("/", (request, response) => {
        if (request.session.user) return redirectBasedOnRole(request, response);
        response.render("index");
    });

// ==============================
// Admin Landing Page
// ==============================

    app.get("/adminLanding", (request, response) => {
        const sessionUser = request.session.user;
        if (!sessionUser || sessionUser.role !== "admin") return response.redirect("/");

        response.render("adminLanding", { users: USERS, user: request.session.user });
    });

// ==============================
// User Landing Page
// ==============================

    app.get("/userLanding", (request, response) => {
        const sessionUser = request.session.user;
        if (!sessionUser || sessionUser.role !== "user") return response.redirect("/");

        const user = USERS.find(user => user.id === sessionUser.id);

        response.render("userLanding", { user, rsvps: RSVPS  });
    });

// ==============================
// RSVP POST Route
// ==============================

    app.post("/userLanding/rsvp", (request, response) => {
        const sessionUser = request.session.user;
        if (!sessionUser || sessionUser.role !== "user") return response.redirect("/login");

        const user = USERS.find(u => u.id === sessionUser.id);

        if (!user) return response.redirect("/login");
        if (user.hasRSVPed) return response.send("You have already RSVP'd!");

        user.hasRSVPed = true;
        user.rsvpTime = new Date(); // store as Date object
        RSVPS.push({ userId: user.id, rsvpTime: user.rsvpTime });

        // update session
        request.session.user.hasRSVPed = true;

        response.redirect("/userLanding");
    });

// ==============================
// Logout Route
// ==============================

    app.get("/logout", (request, response) => {
        request.session.destroy(error => {
            if (error) return response.send("Error logging out");

            response.redirect("/");
        });
    });

// ==============================
// Start Server
// ==============================

    hashExistingUserPasswords().then(() => {
        app.listen(PORT, () => {
            console.log(`Server is running on http://localhost:${PORT}`);
        });
    });
