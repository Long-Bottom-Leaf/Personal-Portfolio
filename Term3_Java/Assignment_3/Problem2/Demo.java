package Problem2;

/**
 * The Demo class tests the Point and MovablePoint classes
 * by creating and manipulating objects to show movement.
 * 
 * author 
 */
public class Demo {
    public static void main(String[] args) {
        // Create a Point object
        Point p1 = new Point(2.5f, 3.5f);
        System.out.println("\n Point: " + p1);

        // Create a MovablePoint object
        MovablePoint mp1 = new MovablePoint(2.5f, 3.5f, 1.2f, 2.3f);
        System.out.println("\n Before move: " + mp1);

        // Move the point and display the new position
        mp1.move();
        System.out.println("\n After move: " + mp1);
    }
}
