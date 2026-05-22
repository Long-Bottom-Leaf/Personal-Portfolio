package AnimalShelter;

public abstract class Animal {
    private int order;
    private String name;

    public Animal(String name) {
        this.name = name;
    }

    public void setOrder(int order) {
        this.order = order;
    }

    public int getOrder() {
        return order;
    }

    public String getName() {
        return name;
    }

    // compare animal arrival times
    public boolean isOlder(Animal animal) {
        return this.order < animal.getOrder();
    }

    @Override
    public String toString() {
        return name + " (order " + order + ")";
    }
}
