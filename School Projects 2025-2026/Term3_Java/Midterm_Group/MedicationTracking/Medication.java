package MedicationTracking;

import java.util.concurrent.atomic.AtomicInteger;
import java.time.LocalDate;

/**
 * Represents a medication in the pharmacy system.
 * Each medication includes details such as name, dose, stock quantity, and expiry date.
 */
public class Medication {
    private static final AtomicInteger ID_GEN = new AtomicInteger(0);
    private final int id;
    private String name;
    private String dose;
    private int quantityInStock;
    private LocalDate expirationDate;

    /**
     * Constructs a new Medication with the given attributes.
     *
     * @param name            the name of the medication
     * @param dose            the dosage information
     * @param quantityInStock the number of units available in stock
     * @param expirationDate  the date when the medication expires
     */
    public Medication(String name, String dose, int quantityInStock, LocalDate expirationDate) {
        this.id = ID_GEN.getAndIncrement();
        this.name = name;
        this.dose = dose;
        this.quantityInStock = quantityInStock;
        
        // Assign random past expiry if none is provided
        if (expirationDate == null) {
            int randomDaysAgo = (int) (Math.random() * 1000); // up to ~3 years ago
            this.expirationDate = LocalDate.now().minusDays(randomDaysAgo);
        } else {
            this.expirationDate = expirationDate;
        }
    }

    /** @return the unique medication ID */
    public int getId() {
        return id;
    }

    /** @return the medication name */
    public String getName() {
        return name;
    }

    /** @return the dosage information */
    public String getDose() {
        return dose;
    }

    /** @return the number of units currently in stock */
    public int getQuantityInStock() {
        return quantityInStock;
    }

    /** @return the expiration date of the medication */
    public LocalDate getExpirationDate() {
        return expirationDate;
    }

    /**
     * Updates the quantity of this medication in stock.
     *
     * @param quantityInStock the new quantity value
     */
    public void setQuantityInStock(int quantityInStock) {
        this.quantityInStock = quantityInStock;
    }

    public void setNewExp(LocalDate expirationDate) {
        this.expirationDate = expirationDate;
    }

    public void setDose(String dose) {
        this.dose = dose;
    }

    @Override
    public String toString() {
        return String.format("ID: %d Name: %s Dose: %s Stock: %d Expiry: %s", id, name, dose, quantityInStock, expirationDate);
    }
}
