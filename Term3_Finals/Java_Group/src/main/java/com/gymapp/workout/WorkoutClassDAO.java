package com.gymapp.workout;

import com.gymapp.model.WorkoutClass;
import com.gymapp.config.DatabaseConnect;
import com.gymapp.util.AppLogger;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class WorkoutClassDAO {

    // Add class
    public void addWorkoutClass(WorkoutClass workoutClass) {
        String sql = """
            INSERT INTO classes (class_name, description, schedule, trainer_id)
            VALUES (?, ?, ?, ?)
            """;

        try (Connection connection = DatabaseConnect.getConnection();
             PreparedStatement preparedStatement = connection.prepareStatement(sql)) {

            preparedStatement.setString(1, workoutClass.getClassName());
            preparedStatement.setString(2, workoutClass.getDescription());
            preparedStatement.setTimestamp(3, Timestamp.valueOf(workoutClass.getSchedule())
            );
            preparedStatement.setInt(4, workoutClass.getTrainerId());

            preparedStatement.executeUpdate();

        } catch (SQLException error) {
            AppLogger.logErrorTrace("Error adding workout class: " + error.getMessage(), error);
        }
    }

    // Update class
    public void updateWorkoutClass(WorkoutClass workoutClass) {
        String sql = """
            UPDATE classes
            SET class_name = ?, description = ?, schedule = ?, trainer_id = ?
            WHERE class_id = ?
            """;

        try (Connection connection = DatabaseConnect.getConnection();
             PreparedStatement preparedStatement = connection.prepareStatement(sql)) {

            preparedStatement.setString(1, workoutClass.getClassName());
            preparedStatement.setString(2, workoutClass.getDescription());
            preparedStatement.setTimestamp(
                3, Timestamp.valueOf(workoutClass.getSchedule())
            );
            preparedStatement.setInt(4, workoutClass.getTrainerId());
            preparedStatement.setInt(5, workoutClass.getClassId());

            preparedStatement.executeUpdate();

        } catch (SQLException error) {
            AppLogger.logErrorTrace("Error updating workout class: " + error.getMessage(), error);
        }
    }

    // Delete class
    public void deleteWorkoutClass(int classId) {
        String sql = "DELETE FROM classes WHERE class_id = ?";

        try (Connection connection = DatabaseConnect.getConnection();
             PreparedStatement preparedStatement = connection.prepareStatement(sql)) {

            preparedStatement.setInt(1, classId);
            preparedStatement.executeUpdate();

        } catch (SQLException error) {
            AppLogger.logErrorTrace("Error deleting workout class: " + error.getMessage(), error);
        }
    }

    // Read all classes
    public List<WorkoutClass> getAllWorkoutClasses() {
        List<WorkoutClass> workoutClasses = new ArrayList<>();
        String sql = "SELECT * FROM classes";

        try (Connection connection = DatabaseConnect.getConnection();
             PreparedStatement preparedStatement = connection.prepareStatement(sql);
             ResultSet resultSet = preparedStatement.executeQuery()) {

            while (resultSet.next()) {
                WorkoutClass workoutClass = new WorkoutClass(
                    resultSet.getInt("class_id"),
                    resultSet.getString("class_name"),
                    resultSet.getString("description"),
                    resultSet.getTimestamp("schedule").toLocalDateTime(),
                    resultSet.getInt("trainer_id")
                );
                workoutClasses.add(workoutClass);
            }

        } catch (SQLException error) {
            AppLogger.logErrorTrace("Error reading all workout classes: " + error.getMessage(), error);
        }

        return workoutClasses;
    }

    // Read classes by trainer ID
    public List<WorkoutClass> getWorkoutClassesByTrainerId(int trainerId) {
        List<WorkoutClass> workoutClasses = new ArrayList<>();
        String sql = "SELECT * FROM classes WHERE trainer_id = ?";

        try (Connection connection = DatabaseConnect.getConnection();
             PreparedStatement preparedStatement = connection.prepareStatement(sql)) {

            preparedStatement.setInt(1, trainerId);

            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                while (resultSet.next()) {
                    WorkoutClass workoutClass = new WorkoutClass(
                        resultSet.getInt("class_id"),
                        resultSet.getString("class_name"),
                        resultSet.getString("description"),
                        resultSet.getTimestamp("schedule").toLocalDateTime(),
                        resultSet.getInt("trainer_id")
                    );

                    workoutClasses.add(workoutClass);
                }
            }

        } catch (SQLException error) {
            AppLogger.logErrorTrace("Error reading workout classes by trainer ID: " + error.getMessage(), error);
        }

        return workoutClasses;
    }

    // Read available classes for specific member
    public List<WorkoutClass> getRegisteredWorkoutClassesByMemberId(int memberId) {
        List<WorkoutClass> workoutClasses = new ArrayList<>();
        String sql = "SELECT c.* FROM classes c JOIN enrollments r ON c.class_id = r.class_id WHERE r.member_id = ?";

        try (Connection connection = DatabaseConnect.getConnection();
             PreparedStatement preparedStatement = connection.prepareStatement(sql)) {

            preparedStatement.setInt(1, memberId);

            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                while (resultSet.next()) {
                    WorkoutClass workoutClass = new WorkoutClass(
                        resultSet.getInt("class_id"),
                        resultSet.getString("class_name"),
                        resultSet.getString("description"),
                        resultSet.getTimestamp("schedule").toLocalDateTime(),
                        resultSet.getInt("trainer_id")
                    );
                    workoutClasses.add(workoutClass);
                }
            }

        } catch (SQLException error) {
            AppLogger.logErrorTrace("Error reading workout classes for member ID: " + error.getMessage(), error);
        }

        return workoutClasses;
    }
}
