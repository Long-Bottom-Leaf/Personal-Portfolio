package Problem4;

/**
 * Abstract superclass for all geometric shapes.
 */
public abstract class Shape implements Scalable {
    // Name of the shape
    protected String name;

    // Constructor
    public Shape(String name) {
        this.name = name;
    }

    // Getter for name
    public String getName() {
        return name;
    }

    // Abstract methods for area and perimeter
    public abstract double getArea();
    public abstract double getPerimeter();

    // Unified print for all shapes
    @Override
    public String toString() {
        return String.format("%shape: Area = %.2f, Perimeter = %.2f", name, getArea(), getPerimeter());
    }
}
