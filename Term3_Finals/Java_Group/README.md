# 🏋️ Gym Management System - User Documentation

## 1. Overview

The **Gym Management System** is a comprehensive application designed to streamline gym operations for administrators, trainers, and members. It provides a **centralized platform** to:

- Manage memberships and expenses 💳  
- Schedule and manage workout classes 🏋️‍♂️  
- Enroll members in classes ✅  
- Track trainer schedules and class attendance 📅  
- Access gym merchandise for purchase 🛒  

The system stores all data securely in a PostgreSQL database and allows users to interact via an intuitive **menu-based console interface**.

---

## 2. Application Components

The system is organized using a **service → DAO → model** architecture:

1. **Models** – Represent real-world entities (data).  
2. **DAOs (Data Access Objects)** – Handle all database operations.  
3. **Services** – Contain business logic like enrollments, membership management, and class scheduling.  
4. **Menus** – Console interface that interacts with users and calls services.

### 2.1 Main Classes

| Component | Purpose |
|-----------|---------|
| **User** | Base class for all users (username, password, role, contact info) |
| **Member** | Extends `User`, tracks membership status, start/end dates, total expenses |
| **Trainer** | Extends `User`, tracks specialty, experience, and class management |
| **WorkoutClass** | Represents gym classes with name, description, schedule, and trainer |
| **ClassEnrollment** | Tracks member enrollment in classes |
| **Merchandise** | Represents gym store items (name, price, quantity, description) |

### 2.2 DAOs

| DAO | Purpose |
|-----|---------|
| **UserDAO** | Retrieve and update users in the database |
| **MemberDAO** | Manage member data and membership info |
| **TrainerDAO** | Manage trainer data |
| **WorkoutClassDAO** | Add, update, delete, and retrieve classes |
| **ClassEnrollmentDAO** | Handle enrollments: add, check, list |
| **MerchandiseDAO** | Manage gym merchandise data |

### 2.3 Services

| Service | Purpose |
|---------|---------|
| **UserService** | Handles login and authentication |
| **MemberService** | Handles membership purchases and expense tracking |
| **WorkoutClassService** | Handles class creation, updates, deletion, retrieval |
| **ClassEnrollmentService** | Handles member enrollment in classes |
| **MerchandiseService** | Handles listing and purchasing merchandise |

### 2.4 Menus

| Menu | Purpose |
|------|---------|
| **BaseMenu** | Abstract menu with shared functionality |
| **MemberMenu** | Members: view classes, enroll, manage membership, shop |
| **TrainerMenu** | Trainers: create/update/delete classes, view schedules |
| **AdminMenu** | Admins: manage users, view all classes, track revenues |
| **MerchandiseMenu** | Browse, purchase, and manage store items |

---

## 3. Class Interaction

1. **Menus → Services:** Menus collect input and call appropriate service methods.  
2. **Services → DAOs:** Services enforce business rules and request database access via DAOs.  
3. **DAOs → Database:** DAOs execute SQL queries and return results as model objects.  
4. **Return Flow:** Results propagate back to the menus and display to the user.  

### 3.1 Class Diagram

User
├── Admin
├── Trainer
│   └── manages → WorkoutClass
└── Member
    └── purchases → Membership
    └── enrolls in → ClassEnrollment
                        └── enrolled in → WorkoutClass

WorkoutClass
└── created by → Trainer

ClassEnrollment
└── links → Member ↔ WorkoutClass

Merchandise
└── can be purchased by → Member

---

## 4. Getting Started

### 4.1 System Requirements

- Java JDK 17+  
- PostgreSQL database  
- Database schema created using provided SQL scripts  

### 4.2 Launching the Application

1. Open terminal or command prompt.  
2. Navigate to the project folder.  
3. Compile the project:
   ```bash
   javac -d out src/**/*.java

### 4.3 Run the program

- java -cp out com.gymapp.Main

### 4.4 Log in

Log in with your username and password

## 5. User Interactions

### 5.1 Members 🧑‍🤝‍🧑

Menu Options:

1. View available classes
2. Enroll in a class
3. View my classes
4. Purchase Membership / View Expenses
5. Store
6. Logout

- View available classes: See class names, schedules, descriptions, and trainers.

- Enroll in a class: Enter a class ID; duplicates are prevented.

- View my classes: List all classes you are enrolled in.

- Purchase Membership / View Expenses: Buy memberships or view total spent.

- Store: Browse and purchase merchandise.

- Logout: Safely exit the system.

### 5.2 Trainers 🏋️‍♂️

Menu Options:

1. Create workout class
2. Update workout class
3. Delete workout class
4. View my classes
5. Logout

- Create/Update/Delete classes: Manage classes by providing class ID, name, description, schedule.

- View my classes: Check all classes assigned to you.

- Logout: Exit safely.

### 5.3 Admins 🛠️

Menu Options:

1. View all users
2. View all classes
3. Manage memberships
4. Track revenues
5. Manage trainers
6. Manage members
7. Logout

- Manage users, memberships, and classes: Add, update, remove, or monitor data.

- Track revenues: Check income from memberships and merchandise.

- Logout: Exit safely.

### 5.4

Menu Options:

// add when done

- Browse items: See available merchandise, price, and quantity.

- Purchase items: Enter item ID and quantity.

- Admin functionality: Add new items, update prices, restock inventory.

## 6. Tips for Users

Always log out to protect your account 🔒

Enroll in a class only once; duplicates are prevented

Trainers: double-check class IDs when updating or deleting 📝

Admins: regularly monitor revenue and membership status

## 7. Troubleshooting

Login issues: Confirm username/password; ensure database is running

Enrollment errors: Verify class exists and you’re not already enrolled

Membership purchases: Check that membership is active and payment is processed

System crashes: Restart application; contact admin if issue persists