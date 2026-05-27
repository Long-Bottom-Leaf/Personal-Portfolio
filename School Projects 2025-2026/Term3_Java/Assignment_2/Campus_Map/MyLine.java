package Assignment_2.Campus_Map;

public class MyLine {
    // instance variables
    private MyPoint begin;
    private MyPoint end;

    // default constructor for 2 points using coordinates
    public MyLine(int x1, int y1, int x2, int y2) {
        this.begin = new MyPoint(x1, y1);
        this.end = new MyPoint(x2, y2);
    }

    // constructor using MyPoint objects
    public MyLine(MyPoint begin, MyPoint end) {
        this.begin = begin;
        this.end = end;
    }

    // Accessors
    public MyPoint getBegin() {
        return begin;
    }

    public MyPoint getEnd() {
        return end;
    }

    // Mutators
    public void setBegin(MyPoint begin) {
        this.begin = begin;
    }

    public void setEnd(MyPoint end) {
        this.end = end;
    }

    // specific coordinate accessors
    public int getBeginX() {
        return begin.getX();
    }

    public int getBeginY() {
        return begin.getY();
    }

    public int getEndX() {
        return end.getX();
    }

    public int getEndY() {
        return end.getY();
    }

    // specific coordinate mutators
    public void setBeginX(int x) {
        begin.setX(x);
    }

    public void setBeginY(int y) {
        begin.setY(y);
    }

    public void setEndX(int x) {
        end.setX(x);
    }

    public void setEndY(int y) {
        end.setY(y);
    }

    // both coordinate accessors
    public int[] getBeginXY() {
        return begin.getXY();
    }

    public int[] getEndXY() {
        return end.getXY();
    }

    // both coordinate mutators
    public void setBeginXY(int x, int y) {
        begin.setXY(x, y);
    }

    public void setEndXY(int x, int y) {
        end.setXY(x, y);
    }

    // calculate line length
    public double getLength() {
        return begin.distance(end);
    }

    // calculate gradient
    public double getGradient() {
        int xDiff = end.getX() - begin.getX();
        int yDiff = end.getY() - begin.getY();

        return Math.atan2(yDiff, xDiff);
    }

    // toString method for display
    @Override
    public String toString() {
        return "MyLine [begin = " + begin + ", end = " + end + "]";
    }
}
