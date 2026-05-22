package Problem3;


/**
 * Represents a Circle, a special case of Ellipse where a = b = radius.
 */
public class Circle extends Ellipse {

    public Circle(String name, double radius) {
        super(name, radius, radius);
    }
}
