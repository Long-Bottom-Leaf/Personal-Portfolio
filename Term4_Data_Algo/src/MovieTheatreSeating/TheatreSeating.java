package MovieTheatreSeating;

import java.util.ArrayList;

public class TheatreSeating {
    // Constants
        private String[][] seats;
        private ArrayList<Reservation> reservations;

        private final int ROWS = 5;
        private final int SEATS_PER_ROW = 10;

    // Seat status constants
        private final String OPEN = "Open";
        private final String RESERVED = "Reserved";

    // Theater constructor
        public TheatreSeating() {
            seats = new String[ROWS][SEATS_PER_ROW];
            reservations = new ArrayList<>();
            initializeSeats();
        }

    // Initialize seats
        public void initializeSeats() {
            for (int i = 0; i < ROWS; i++) {
                for (int j = 0; j < SEATS_PER_ROW; j++) {
                    seats[i][j] = OPEN;
                }
            }
        }

    // Display seating plan
        public void displaySeating() {
            System.out.println("\nSeating Chart:");
            System.out.print(" ");

            for (int i = 1; i <= SEATS_PER_ROW; i++) {
                System.out.print(i + " ");
            }

            System.out.println();

            for (int i = 0; i < ROWS; i++) {
                System.out.print((char)('A' + i) + "  ");

                for (int j = 0; j < SEATS_PER_ROW; j++) {
                    System.out.print(seats[i][j] + " ");
                }

                System.out.println();
            }
        }

    // Reserve seat
        public void reserveSeat(String name, int row, int seat) {

            // Allow human numbering to translate to computer numbering
                row--;
                seat--;

            // Selection error check
                if (row < 0 || row >= ROWS || seat < 0 || seat >= SEATS_PER_ROW) {
                    System.out.println("Invalid seat selection.");
                    return;
                }

            // Reserve seat or already taken
                if (seats[row][seat].equals(OPEN)) {
                    seats[row][seat] = RESERVED;

                    reservations.add(new Reservation(name, row, seat));
                    System.out.println("Seat reserved successfully!");

                } else {
                    System.out.println("Seat is already taken.");
                    suggestSeat();
                }
        }

    // Suggest seat
        private void suggestSeat() {
            for (int i = 0; i < ROWS; i++) {
                for (int j = 0; j < SEATS_PER_ROW; j++) {
                    if (seats[i][j].equals(OPEN)) {
                        // ('A' + i) allows a readable format, iterates through he rows A-E (5 rows)
                        System.out.println("Suggested seat: Row " + (char)('A' + i) + " Seat " + (j + 1));
                        return;
                    }
                }
            }

            System.out.println("No seats available.");
        }

    // Cancel Reservation
        public void cancelReservation(String name) {
            for (int i = 0; i < reservations.size(); i++) {
                Reservation reservation = reservations.get(i);

                if (reservation.getCustomerName().equalsIgnoreCase(name)) {
                    seats[reservation.getRow()][reservation.getSeat()] = "O";
                    reservations.remove(i);
                    System.out.println("Reservation cancelled.");
                    return;
                }
            }

            System.out.println("Reservation not found.");
        }
}
