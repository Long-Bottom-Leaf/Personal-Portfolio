package Term3.Java.QAP2.Problem2;

import java.util.ArrayList;

// I will be honest, I was rushing to get this done, and had to rely on AI more than usual to get everything structured and typed out
// I fully understand everything that is created but used AI far more than any other time to create code

public class CampusMap {
    // initialize variables
    private ArrayList<MyRectangle> buildings;
    private ArrayList<MyLine> walkways;
    private ArrayList<MyCircle> fountains;

    // default constructor and create arrays for the variables
    public CampusMap() {
        buildings = new ArrayList<>();
        walkways = new ArrayList<>();
        fountains = new ArrayList<>();
    }

    // add a building
    public void addBuilding(MyRectangle building) {
        buildings.add(building);
    }

    // add a fountain
    public void addFountain(MyCircle fountain) {
        fountains.add(fountain);
    }

    // add walkways that connect two buildings
    public void addWalkway(MyRectangle from, MyRectangle to) {
        if (!buildings.contains(from) || !buildings.contains(to)) {
            System.out.println("Error: Both buildings must exist in the campus map.");
            return;
        }

        // calculate center of buildings
        MyPoint centerFrom = new MyPoint(
            (from.getTopLeft().getX() + from.getBottomRight().getX()) / 2,
            (from.getTopLeft().getY() + from.getBottomRight().getY()) / 2
        );

        MyPoint centerTo = new MyPoint(
            (to.getTopLeft().getX() + to.getBottomRight().getX()) / 2,
            (to.getTopLeft().getY() + to.getBottomRight().getY()) / 2
        );

        MyLine walkway = new MyLine(centerFrom, centerTo);
        walkways.add(walkway);
    }

    // walkway length
    public double calculateTotalWalkwayLength() {
        double total = 0;
        for (MyLine line : walkways) {
            total += line.getLength();
        }
        return total;
    }

    // fountain area
    public double calculateTotalFountainArea() {
        double total = 0;
        for (MyCircle circle : fountains) {
            total += circle.getArea();
        }
        return total;
    }

    // check if walkways exist
    public boolean isWalkwayFromTo(MyRectangle fromBuilding, MyRectangle toBuilding) {
        MyPoint centerFrom = new MyPoint(
            (fromBuilding.getTopLeft().getX() + fromBuilding.getBottomRight().getX()) / 2,
            (fromBuilding.getTopLeft().getY() + fromBuilding.getBottomRight().getY()) / 2

        );
        MyPoint centerTo = new MyPoint(
            (toBuilding.getTopLeft().getX() + toBuilding.getBottomRight().getX()) / 2,
            (toBuilding.getTopLeft().getY() + toBuilding.getBottomRight().getY()) / 2

        );

        for (MyLine line : walkways) {
            if ((line.getBegin().getX() == centerFrom.getX() && line.getBegin().getY() == centerFrom.getY() &&
                 line.getEnd().getX() == centerTo.getX() && line.getEnd().getY() == centerTo.getY()) ||
                (line.getBegin().getX() == centerTo.getX() && line.getBegin().getY() == centerTo.getY() &&
                 line.getEnd().getX() == centerFrom.getX() && line.getEnd().getY() == centerFrom.getY())) {
                return true;
            }
        }
        return false;
    }

    // display map summary
    public void displaySummary() {
        System.out.println("\n");
        System.out.println("Buildings: ");
        for (MyRectangle b : buildings) System.out.println(b);

        System.out.println("\n");
        System.out.println("Fountains: ");
        for (MyCircle f : fountains) System.out.println(f);

        System.out.println("\n");
        System.out.println("\nWalkways: ");
        for (MyLine w : walkways) System.out.println(w);

        System.out.println("\n");
        System.out.println("Total walkway length: " + calculateTotalWalkwayLength());
        System.out.println("Total fountain area: " + calculateTotalFountainArea());
    }
}
