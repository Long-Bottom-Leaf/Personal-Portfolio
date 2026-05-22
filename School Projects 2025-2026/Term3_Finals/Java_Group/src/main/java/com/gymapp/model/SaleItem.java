package com.gymapp.model;

public class SaleItem {

    private int merchandiseId;
    private String itemName;
    private String description;
    private double price;
    private int quantity;

    public SaleItem() {}

    public SaleItem(int merchandiseId, String itemName,
                    String description, double price, int quantity) {
        this.merchandiseId = merchandiseId;
        this.itemName = itemName;
        this.description = description;
        this.price = price;
        this.quantity = quantity;
    }

    // Accessors
    public int getMerchandiseId() {
        return merchandiseId;
    }

    public String getItemName() {
        return itemName;
    }

    public String getDescription() {
        return description;
    }

    public double getPrice() {
        return price;
    }

    public int getQuantity() {
        return quantity;
    }

    // Mutators
    public void setMerchandiseId(int merchandiseId) {
        this.merchandiseId = merchandiseId;
    }

    public void setItemName(String itemName) {
        this.itemName = itemName;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    // toString method
    @Override
    public String toString() {
        return "Sale Item -- Merchandise ID: " + merchandiseId +
               ", Item Name: " + itemName +
               ", Description: " + description +
               ", Price: " + price +
               ", Quantity: " + quantity;
    }
}