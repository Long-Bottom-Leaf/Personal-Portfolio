package Problem4;

/**
 * Demonstrates Shape hierarchy and Scalable interface.
 */
public class Demo {
    // Main method
    public static void main(String[] args) {
        // Create an array of Shape objects
        Shape[] shapes = new Shape[4];
        shapes[0] = new Circle("Circle", 5);
        shapes[1] = new Ellipse("Ellipse", 8, 4);
        shapes[2] = new Triangle("Triangle", 3, 4, 5);
        shapes[3] = new EquilateralTriangle("Equilateral Triangle", 6);

        // Display shapes before scaling
        System.out.println("\n ----- Before Scaling -----");
        for (Shape s : shapes) {
            System.out.println(s);
        }

        // Scale all shapes by a factor of 2
        System.out.println("Scaling all shapes by factor 2...\n");
        scaleAll(shapes, 2.0); // static method

        // Display shapes after scaling
        System.out.println("----- After Scaling -----");
        for (Shape s : shapes) {
            System.out.println(s);
        }
    }

    // Static method to scale all scalable objects
    public static void scaleAll(Scalable[] arr, double factor) {
        for (Scalable s : arr) {
            s.scale(factor);
        }
    }
}
