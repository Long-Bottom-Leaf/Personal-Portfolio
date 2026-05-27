public class TestMyLine {
    public static void main(String[] args) {
        // initialize test points
            MyPoint p1 = new MyPoint(1, 2);
            MyPoint p2 = new MyPoint(3, 4);

        // initialize line objects
            MyLine line1 = new MyLine(p1, p2);
            MyLine line2 = new MyLine(2, 4, 6, 8);

        // test display
            System.out.println("\n");
            System.out.println("Line 1: " + line1);
            System.out.println("Line 2: " + line2);

        // test accessors
            System.out.println("\n");
            System.out.println("Line 1 Begin Point: " + line1.getBegin());
            System.out.println("Line 1 End Point: " + line1.getEnd());
            System.out.println("Line 2 Begin X: " + line2.getBeginX());
            System.out.println("Line 2 End Y: " + line2.getEndY());

        // test mutators
            line2.setBeginXY(2, 3);
            line2.setEndXY(8, 7);

            System.out.println("\n");
            System.out.println("After updating Line 2 coordinates:");
            System.out.println("Line 2: " + line2);

        // test length and gradient methods
            System.out.println("\n");
            System.out.println("Line 1 Length: " + line1.getLength());
            System.out.println("Line 1 Gradient (radians): " + line1.getGradient());

            System.out.println("\n");
            System.out.println("Line 2 Length: " + line2.getLength());
            System.out.println("Line 2 Gradient (radians): " + line2.getGradient());

        // test accessing both points
            int[] beginXY = line1.getBeginXY();
            int[] endXY = line1.getEndXY();

            System.out.println("\n");
            System.out.println("Line 1 BeginXY: (" + beginXY[0] + "," + beginXY[1] + ")");
            System.out.println("Line 1 EndXY: (" + endXY[0] + "," + endXY[1] + ")");
    }
}
