public class TestMyRectangle {
    public static void main(String[] args) {

        // initialize constants
            MyPoint p1 = new MyPoint(1, 5);
            MyPoint p2 = new MyPoint(6, 2);

        // initialize default rectangle
            MyRectangle rect1 = new MyRectangle(p1, p2);

        // test accessors
            System.out.println("\n");
            System.out.println("Rectangle: " + rect1);
            System.out.println("Width: " + rect1.getWidth());
            System.out.println("Height: " + rect1.getHeight());
            System.out.println("Area: " + rect1.getArea());
            System.out.println("Perimeter: " + rect1.getPerimeter());

        // test mutators
            System.out.println("\n");
            rect1.setTopLeft(new MyPoint(0, 6));
            rect1.setBottomRight(new MyPoint(4, 1));

        // test outputs after changing points
            System.out.println("\n");
            System.out.println("\nAfter updating points:");
            System.out.println("Rectangle: " + rect1);
            System.out.println("Width: " + rect1.getWidth());
            System.out.println("Height: " + rect1.getHeight());
            System.out.println("Area: " + rect1.getArea());
            System.out.println("Perimeter: " + rect1.getPerimeter());
    }
}