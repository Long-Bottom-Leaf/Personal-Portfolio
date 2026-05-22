package Term3.Java.QAP2.Problem2;       // may need to edit or delete this line to run

public class MyRectangle {
    private MyPoint topLeft;
    private MyPoint bottomRight;

    // default rectangle constructor
    public MyRectangle() {
        this.topLeft = new MyPoint(0, 0);
        this.bottomRight = new MyPoint(1, 1);
    }

    // default constructor with 2 points
    public MyRectangle(MyPoint topLeft, MyPoint bottomRight) {
        this.topLeft = topLeft;
        this.bottomRight = bottomRight;
    }

    // accessors
    public MyPoint getTopLeft() {
        return topLeft;
    }

    public MyPoint getBottomRight() {
        return bottomRight;
    }

    // mutators
    public void setTopLeft(MyPoint topLeft) {
        this.topLeft = topLeft;
    }

    public void setBottomRight(MyPoint bottomRight) {
        this.bottomRight = bottomRight;
    }

    // width
    public double getWidth() {
        return Math.abs(bottomRight.getX() - topLeft.getX());
    }

    // height
    public double getHeight() {
        return Math.abs(bottomRight.getY() - topLeft.getY());
    }

    // area
    public double getArea() {
        return getWidth() * getHeight();
    }

    // perimeter
    public double getPerimeter() {
        return 2 * (getWidth() + getHeight());
    }

    // toString
    @Override
    public String toString() {
        return "MyRectangle [topLeft=" + topLeft + ", bottomRight=" + bottomRight + "]";
    }
}

