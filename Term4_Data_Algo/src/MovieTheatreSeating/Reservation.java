package MovieTheatreSeating;

public class Reservation {
    // Instance variables
        private String customerName;
        private int row;
        private int seat;

    // Constructor
        public Reservation(String customerName, int row, int seat) {
            this.customerName = customerName;
            this.row = row;
            this.seat = seat;
        }

    // Getters
        public String getCustomerName() {
            return customerName;
        }

        public int getRow() {
            return row;
        }

        public int getSeat() {
            return seat;
        }
}
