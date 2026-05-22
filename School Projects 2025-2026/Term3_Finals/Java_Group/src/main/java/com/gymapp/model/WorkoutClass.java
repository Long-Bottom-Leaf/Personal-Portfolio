package com.gymapp.model;

import java.time.LocalDateTime;

public class WorkoutClass {

    private int classId;
    private String className;
    private String description;
    private LocalDateTime schedule;
    private int trainerId;

    public WorkoutClass() {}

    public WorkoutClass(int classId, String className, String description,
                        LocalDateTime schedule, int trainerId) {
        this.classId = classId;
        this.className = className;
        this.description = description;
        this.schedule = schedule;
        this.trainerId = trainerId;
    }

    // Accessors
    public int getClassId() {
        return classId;
    }

    public String getClassName() {
        return className;
    }

    public String getDescription() {
        return description;
    }

    public LocalDateTime getSchedule() {
        return schedule;
    }

    public int getTrainerId() {
        return trainerId;
    }
    
    // Mutators
    public void setClassId(int classId) {
        this.classId = classId;
    }

    public void setClassName(String className) {
        this.className = className;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public void setSchedule(LocalDateTime schedule) {
        this.schedule = schedule;
    }

    public void setTrainerId(int trainerId) {
        this.trainerId = trainerId;
    }

    // toString method
    @Override
    public String toString() {
        return "Workout Class -- Class ID: " + classId + ", Class Name: " + className +
               ", Description: " + description + ", Schedule: " + schedule +
               ", Trainer ID: " + trainerId;
    }
}