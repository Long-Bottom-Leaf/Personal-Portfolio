package Campus_Map;

public class MyCircle {
    // instance variables
    private MyPoint center;
    private double radius;

    // default constructor
    public MyCircle() {
        this.center = new MyPoint(0, 0);
        this.radius = 1;
    }

    public MyCircle(MyPoint center, double radius) {
        this.center = center;
        this.radius = radius;
    }

    // accessors
    public MyPoint getCenter() {
        return center;
    }

    public double getRadius() {
        return radius;
    }

    // mutators
    public void setCenter(MyPoint center) {
        this.center = center;
    }

    public void setRadius(double radius) {
        this.radius = radius;
    }

    // area
    public double getArea() {
        return Math.PI * radius * radius;
    }

    @Override
    public String toString() {
        return "MyCircle [center=" + center + ", radius=" + radius + "]";
    }
}

