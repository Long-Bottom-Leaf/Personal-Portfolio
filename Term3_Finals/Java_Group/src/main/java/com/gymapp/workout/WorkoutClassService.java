package com.gymapp.workout;

import com.gymapp.model.User;
import com.gymapp.model.WorkoutClass;
import com.gymapp.util.AppLogger;

import java.time.LocalDateTime;
import java.util.List;

public class WorkoutClassService {

    private final WorkoutClassDAO workoutClassDAO = new WorkoutClassDAO();

    // CREATE (Trainer only)
    public void createWorkoutClass(User currentUser, String className, String description, LocalDateTime schedule) {
        enforceRole(currentUser, "TRAINER", "create workout class");

        if (className == null || className.isBlank()) {
            throw new IllegalArgumentException("Class name is required");
        }

        WorkoutClass workoutClass = new WorkoutClass(
            0,
            className,
            description,
            schedule,
            currentUser.getRoleSpecificId()
        );

        workoutClassDAO.addWorkoutClass(workoutClass);

        AppLogger.logInfo("Workout class created by trainer ID: " + currentUser.getRoleSpecificId());
    }


    // UPDATE (Trainer only)
    public void updateWorkoutClass(User currentUser, int classId, String className, String description, LocalDateTime schedule) {
        enforceRole(currentUser, "TRAINER", "update workout class");

        WorkoutClass workoutClass = new WorkoutClass(
            classId,
            className,
            description,
            schedule,
            currentUser.getRoleSpecificId()
        );

        workoutClassDAO.updateWorkoutClass(workoutClass);

        AppLogger.logInfo("Workout class updated by trainer ID: " + currentUser.getRoleSpecificId());
    }

    // DELETE (Trainer only)
    public void deleteWorkoutClass(User currentUser, int classId) {
        enforceRole(currentUser, "TRAINER", "delete workout class");

        workoutClassDAO.deleteWorkoutClass(classId);

        AppLogger.logInfo("Workout class deleted by trainer ID: " + currentUser.getRoleSpecificId());
    }


    // READ (Trainer only)
    public List<WorkoutClass> getTrainerWorkoutClasses(User currentUser) {
        enforceRole(currentUser, "TRAINER", "view trainer classes");

        return workoutClassDAO.getWorkoutClassesByTrainerId(currentUser.getRoleSpecificId());
    }


    // READ (Admin only)
    public List<WorkoutClass> getAllWorkoutClasses(User currentUser) {
        enforceRole(currentUser, "ADMIN", "view all workout classes");

        return workoutClassDAO.getAllWorkoutClasses();
    }

    // READ (Member only)
    public List<WorkoutClass> getMemberWorkoutClasses(User currentUser) {
        enforceRole(currentUser, "MEMBER", "view enrolled workout classes");

        return workoutClassDAO.getRegisteredWorkoutClassesByMemberId(
            currentUser.getRoleSpecificId()
        );
    }

    // Role Enforcement
    private void enforceRole(User user, String requiredRole, String action) {
        if (!requiredRole.equals(user.getRole())) {
            AppLogger.logWarning("Unauthorized " + action + " attempt by user: " + user.getUsername() + " (role=" + user.getRole() + ")");
            throw new SecurityException("Access denied");
        }
    }
}