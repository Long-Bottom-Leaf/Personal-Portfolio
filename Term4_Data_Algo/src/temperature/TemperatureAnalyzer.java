package temperature;

import java.util.Arrays;
import java.util.ArrayList;
import java.util.Scanner;

public class TemperatureAnalyzer {

    public static void main(String[] args) {

        /* The initial inputs will be an array, while the array for the days that are above the average will
        * be an array list. */

        // Gather number of temp inputs
            Scanner input = new Scanner(System.in);
            System.out.println("===============================================================");
            System.out.println("This is the temperature analysis program!");
            System.out.println("Please enter the number of temperatures you'd like to analyze: ");

            int count = 0;
            count = input.nextInt();

        // Create temperature array
            double[] temperatures = new double[count];

        // Get temps for each day
            for (int i = 0; i < count; i++) {
                System.out.println("Enter temperature for day " + (i + 1) + ": ");
                temperatures[i] = input.nextDouble();
            }

        // Calculate sum of temperatures
            double sum = 0;
            for (double temp : temperatures) {
                sum += temp;
            }

            System.out.println("The total temperature is: " + sum);

        // Calculate temperature average
            double average = sum / count;

            System.out.println("The average temperate is: " + average);

        // Days above average
            ArrayList<Double> aboveAverageList = new ArrayList<>();
            for (double temp : temperatures) {
                if (temp > average) {
                    aboveAverageList.add(temp);
                }
            }

            // temps above average
            if (aboveAverageList.isEmpty()) {
                System.out.println("No temperatures are above the average temperature!");

            } else if (aboveAverageList.size() == 1) {
                System.out.println("The temperature that is above the average temperature is: " + aboveAverageList);
                System.out.println("Days above average: " + aboveAverageList.size());

            } else {
                System.out.println("The temperatures that are above the average temperature are: " + aboveAverageList);
                System.out.println("Days above average: " + aboveAverageList.size());
            }

        input.close();
    }
}