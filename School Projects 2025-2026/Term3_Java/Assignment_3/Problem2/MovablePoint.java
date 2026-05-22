package Problem2;

/**
 * The MovablePoint class extends Point and adds speed attributes
 * for movement along the x and y axes.
 * It provides methods to move the point and return the new position.
 * 
 * @author Stephen
 */

public class MovablePoint extends Point {
    // Instance variables
    private float xSpeed;
    private float ySpeed;

    /**
     * Default constructor initializes coordinates and speeds to (0, 0)
     */
    public MovablePoint() {
        super();
    }

    /**
     * Constructs a MovablePoint with speed components.
     * 
     * @param xSpeed speed along the x-axis
     * @param ySpeed speed along the y-axis
     */
    public MovablePoint(float xSpeed, float ySpeed) {
        super();    // Call to Point's default constructor
        this.xSpeed = xSpeed;
        this.ySpeed = ySpeed;
    }

    /**
     * Constructs a MovablePoint with coordinates and speed components
     * @param x the x-coordinate
     * @param y the y-coordinate
     * @param xSpeed speed along the x-axis
     * @param ySpeed speed along the y-axis
     */
    public MovablePoint(float x, float y, float xSpeed, float ySpeed) {
        super(x, y);
        this.xSpeed = xSpeed;
        this.ySpeed = ySpeed;
    }

    /**
     * @return the xSpeed
     */
    public float getXSpeed() {
        return xSpeed;
    }

    /**
     * @return the ySpeed
     */
    public float getYSpeed() {
        return ySpeed;
    }

    /**
     * @param xSpeed sets the xSpeed
     */
    public void setXSpeed(float xSpeed) {
        this.xSpeed = xSpeed;
    }

    /**
     * @param ySpeed sets the ySpeed
     */
    public void setYSpeed(float ySpeed) {
        this.ySpeed = ySpeed;
    }

    /**
     * Sets both speed components.
     * 
     * @param xSpeed speed along the x-axis
     * @param ySpeed speed along the y-axis
     */
    public void setSpeed(float xSpeed, float ySpeed) {
        this.xSpeed = xSpeed;
        this.ySpeed = ySpeed;
    }

    /**
     * @return the speeds as an array [xSpeed, ySpeed]
     */
    public float[] getSpeed() {
        return new float[] { xSpeed, ySpeed };
    }

    /**
     * Moves the point by adding the speed values to the coordinates.
     * Uses setters/getters from the superclass.
     * 
     * @return this MovablePoint object after moving
     */
    public MovablePoint move() {
        setX(getX() + xSpeed);
        setY(getY() + ySpeed);
        return this;
    }

    /**
     * Returns a string representation of the MovablePoint.
     * 
     * @return formatted string "(x, y), speed=(xSpeed, ySpeed)"
     */
    @Override
    public String toString() {
        return String.format("(%s,%s), speed=(%s,%s)", getX(), getY(), xSpeed, ySpeed);
    }
}
