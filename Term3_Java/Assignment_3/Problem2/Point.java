package Problem2;


/**
 * The Point class represents a point in 2D space with x and y coordinates.
 * It provides getter and setter methods for manipulating these coordinates.
 * This class is the superclass of MovablePoint.
 * 
 * @author Stephen
 */

public class Point {
    // Instance variables
    private float x;
    private float y;

    /** Default constructor initializes coordinates to (0, 0). */
    public Point() {}

    /**
     * Constructs a Point with the specified coordinates.
     * 
     * @param x the x-coordinate
     * @param y the y-coordinate
     */
    public Point(float x, float y) {
        this.x = x;
        this.y = y;
    }

    /**
     * @return the x-coordinate
     */
    public float getX() {
        return x;
    }

    /**
     * @return the y-coordinate
     */
    public float getY() {
        return y;
    }

    /**
     * @param x sets the x-coordinate
     */
    public void setX(float x) {
        this.x = x;
    }

    /**
     * @param y sets the y-coordinate
     */
    public void setY(float y) {
        this.y = y;
    }

    /**
     * Sets both coordinates.
     * 
     * @param x the x-coordinate
     * @param y the y-coordinate
     */
    public void setXY(float x, float y) {
        this.x = x;
        this.y = y;
    }

    /**
     * @return an array of floats containing [x, y]
     */
    public float[] getXY() {
        return new float[]{x, y};
    }

    /**
     * Returns a string representation of the Point.
     * 
     * @return formatted as "(x,y)"
     */
    @Override
    public String toString() {
        return "(" + x + "," + y + ")";
    }
}
