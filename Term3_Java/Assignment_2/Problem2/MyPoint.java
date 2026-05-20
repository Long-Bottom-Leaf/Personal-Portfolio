package Term3.Java.QAP2.Problem2;       // may need to edit or delete this line to run

public class MyPoint {
    // instance variables
    private int x;
    private int y;

    // default constructor to format a point
    public MyPoint() {
        this.x = 0;
        this.y = 0;
    }

    // constructor to accept input for a point
    public MyPoint(int x, int y) {
        this.x = x;
        this.y = y;
    }

    // point accessors and mutators
    public int getX() {
        return x;
    }
    
    public int getY() {
        return y;
    }

    public void setX(int x) {
        this.x = x;
    }

    public void setY(int y) {
        this.y = y;
    }

    // set both points at one time
    public void setXY(int x, int y) {
        this.x = x;
        this.y = y;
    }

    // return both points, array is best to plot a point
    public int[] getXY() {
        return new int[] {x, y};
    }

    // Calculate distance between points
    public double distance(MyPoint another) {
        int xDiff = this.x - another.x;
        int yDiff = this.y - another.y;
        return Math.sqrt(xDiff * xDiff + yDiff * yDiff);
    }

    // to string method for points
    @Override
    public String toString() {
        return "(" + x + "," + y + ")";
    }
}
