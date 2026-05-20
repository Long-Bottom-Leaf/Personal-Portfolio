package Problem3;

/**
 * Represents an Ellipse shape with major and minor axes.
 */
public class Ellipse extends Shape {
    protected double a;     // major axis
    protected double b;     // minor axis

    public Ellipse(String name, double axis1, double axis2) {
        super(name);

        // assign largest to a, smallest to b for consistency
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
        // given formula: P = Pi * sqrt(2(a² + b²) - (a - b)² / 2)
        return Math.PI * Math.sqrt(2 * (a * a + b * b) - ((a - b) * (a - b)) / 2);
    }
}
