package Problem4;

/**
 * Represents a Circle, a special case of Ellipse.
 */
public class Circle extends Ellipse {
    // Constructor takes the radius as both axes
    public Circle(String name, double radius) {
        super(name, radius, radius);
    }

    @Override
    public void scale(double factor) {
        a *= factor;
        b *= factor;
    }
}
