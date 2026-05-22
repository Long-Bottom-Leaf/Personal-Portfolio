package Problem4;

/**
 * Represents a general Triangle with three sides.
 */
public class Triangle extends Shape {
    // sides of the triangle
    protected double side1, side2, side3;

    // Constructor
    public Triangle(String name, double side1, double side2, double side3) {
        super(name);
        if ((side1 + side2 > side3) &&
            (side2 + side3 > side1) &&
            (side3 + side1 > side2)) {
            this.side1 = side1;
            this.side2 = side2;
            this.side3 = side3;

        } else {
            System.out.println("\n Error: Invalid triangle sides.");
            System.exit(1);
        }
    }

    @Override
    public double getPerimeter() {
        return side1 + side2 + side3;
    }

    @Override
    public double getArea() {
        double s = getPerimeter() / 2.0;
        return Math.sqrt(s * (s - side1) * (s - side2) * (s - side3));
    }

    @Override
    public void scale(double factor) {
        side1 *= factor;
        side2 *= factor;
        side3 *= factor;
    }
}
