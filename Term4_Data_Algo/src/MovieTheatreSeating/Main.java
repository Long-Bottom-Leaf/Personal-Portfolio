package MovieTheatreSeating;

import java.util.Scanner;

public class Main {
    // Main program
    public static void main(String[] args) {
        TheatreSeating theatreSeating = new TheatreSeating();
        Scanner input = new Scanner(System.in);

        int choice;

        do {
            // Menu
                System.out.println("Seat Reservation System!");
                System.out.println("==========================");
                System.out.println("\n1. View Seating");
                System.out.println("2. Reserve Seat");
                System.out.println("3. Cancel Reservation");
                System.out.println("4. Exit");
                System.out.print("Choose option: ");

                choice = input.nextInt();
                input.nextLine();

            // Menu choices
                switch (choice) {

                    case 1:
                        theatreSeating.displaySeating();
                        break;

                    case 2:
                        System.out.print("Enter name: ");
                        String name = input.nextLine();

                        System.out.print("Enter row (A-E): ");
                        char rowChar = input.next().toUpperCase().charAt(0);

                        System.out.print("Enter seat number (1-10): ");
                        int seat = input.nextInt();

                        int row = rowChar - 'A' + 1;
                        theatreSeating.reserveSeat(name, row, seat);
                        break;

                    case 3:
                        System.out.print("Enter name to cancel: ");

                        String cancelName = input.nextLine();
                        theatreSeating.cancelReservation(cancelName);
                        break;

                    case 4:
                        System.out.println("Goodbye!");
                        break;
            }

        } while (choice != 4);

        input.close();
    }
}
