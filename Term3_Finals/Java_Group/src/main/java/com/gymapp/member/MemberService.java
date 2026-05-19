package com.gymapp.member;

import com.gymapp.model.User;
import com.gymapp.util.AppLogger;

import java.time.LocalDate;

public class MemberService {

    private final MemberDAO memberDAO = new MemberDAO();

    private static final double MEMBERSHIP_COST = 50.00;
    private static final int MEMBERSHIP_DURATION_MONTHS = 1;

    // Purchase membership
    public void purchaseMembership(User user) {
        enforceRole(user, "MEMBER", "purchase membership");

        LocalDate start = LocalDate.now();
        LocalDate end = start.plusMonths(MEMBERSHIP_DURATION_MONTHS);

        memberDAO.updateMembership(
            user.getRoleSpecificId(),
            "ACTIVE",
            start,
            end,
            MEMBERSHIP_COST
        );

        AppLogger.logInfo("Member purchased membership: " + user.getUsername());
    }

    // View total spent
    public double viewTotalExpenses(User user) {
        enforceRole(user, "MEMBER", "view membership expenses");
        return memberDAO.getTotalRevenue(
            user.getRoleSpecificId()
        );
    }

    private void enforceRole(User user, String role, String action) {
        if (!role.equals(user.getRole())) {
            AppLogger.logWarning(
                "Unauthorized " + action + " attempt by " + user.getUsername()
            );
            throw new SecurityException("Access denied");
        }
    }
}
