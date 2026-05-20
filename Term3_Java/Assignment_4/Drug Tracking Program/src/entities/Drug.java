package entities;

public class Drug {
    // Drug properties
    private int drugId;
    private String drugName;
    private double drugCost;
    private String dosage;

    // Constructor
    public Drug(int drugId, String drugName, double drugCost, String dosage) {
        this.drugId = drugId;
        this.drugName = drugName;
        this.drugCost = drugCost;
        this.dosage = dosage;
    };

    // Output
    @Override
    public String toString() {
        return drugId + ", " + drugName + ", " + drugCost + ", " + dosage;
    };

    public static Drug fromString(String line) {
        String[] parts = line.split(", ");
        
        return new Drug(
            Integer.parseInt(parts[0].trim()),
            parts[1].trim(),
            Double.parseDouble(parts[2].trim()),
            parts[3].trim()
        );
    };
}
