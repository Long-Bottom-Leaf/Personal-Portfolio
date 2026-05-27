package Term3_Java.Assignment_2.Campus_Map;

public class TestCampusMap {
    public static void main(String[] args) {
        CampusMap campus = new CampusMap();

        // initialize test buildings
            MyRectangle scienceHall = new MyRectangle(new MyPoint(200, 700), new MyPoint(400, 900));
            MyRectangle library = new MyRectangle(new MyPoint(600, 700), new MyPoint(900, 950));
            MyRectangle lecture1 = new MyRectangle(new MyPoint(100, 500), new MyPoint(200, 600));
            MyRectangle lecture2 = new MyRectangle(new MyPoint(220, 500), new MyPoint(320, 600));
            MyRectangle lecture3 = new MyRectangle(new MyPoint(340, 500), new MyPoint(440, 600));

            // test adding buildings with names
            campus.addBuilding(scienceHall);
            campus.addBuilding(library);
            campus.addBuilding(lecture1);
            campus.addBuilding(lecture2);
            campus.addBuilding(lecture3);

        // test adding fountains
            MyCircle fountain = new MyCircle(new MyPoint(500, 500), 50);
            campus.addFountain(fountain);

        // Walkways connecting buildings
            campus.addWalkway(scienceHall, library);
            campus.addWalkway(scienceHall, lecture1);
            campus.addWalkway(scienceHall, lecture2);
            campus.addWalkway(scienceHall, lecture3);
            campus.addWalkway(library, lecture1);

        // test campus display
            campus.displaySummary();

        // Test walkway existence
            System.out.println("\n");
            System.out.println("Walkway from Science Hall to Library exists? " + campus.isWalkwayFromTo(scienceHall, library));
            System.out.println("Walkway from Library to Lecture 3 exists? " + campus.isWalkwayFromTo(library, lecture3));
    }
}
