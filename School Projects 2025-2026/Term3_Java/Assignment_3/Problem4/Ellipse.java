package Problem4;

/**
 * Represents an Ellipse shape with major and minor axes.
 */
public class Ellipse extends Shape {
    // major and minor axes
    protected double a; // major axis
    protected double b; // minor axis

    // Constructor
    public Ellipse(String name, double axis1, double axis2) {
        super(name);
        if (axis1 >= axis2) {
            this.a = axis1;
            this.b = axis2;

        } else {
            this.a = axis2;
            this.b = axis1;
        }
    }

    @Override
    public double getArea() {
        return Math.PI * a * b;
    }

    @Override
    public double getPerimeter() {
        return Math.PI * Math.sqrt(2 * (a * a + b * b) - ((a - b) * (a - b)) / 2);
    }

    @Override
    public void scale(double factor) {
        a *= factor;
        b *= factor;
    }
}

