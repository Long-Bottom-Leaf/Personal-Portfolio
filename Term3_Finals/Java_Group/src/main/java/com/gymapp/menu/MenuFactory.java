package com.gymapp.menu;

import com.gymapp.model.User;
import com.gymapp.model.Admin;
import com.gymapp.model.Member;
import com.gymapp.model.Trainer;

public class MenuFactory {

    public static Menu createMenu(User user) {

        if (user instanceof Trainer trainer) {
            return new TrainerMenu(trainer);
        }

        if (user instanceof Admin admin) {
            return new AdminMenu(admin);
        }

        if (user instanceof Member member) {
            return new MemberMenu(member);
        }

        throw new IllegalArgumentException("Unknown user type");
    }
}
