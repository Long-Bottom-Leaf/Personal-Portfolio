package Problem3;

/**
 * Abstract superclass for all geometric shapes.
 */
public abstract class Shape {
    protected String name;

    public Shape(String name) {
        this.name = name;
    }

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
