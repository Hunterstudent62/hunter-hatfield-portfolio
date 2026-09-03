import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;

public class PoultryProductionTracker {

    private static final int MAX_CHICKENS = 10;

    public static void main(String[] args) {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("M/d/yyyy 'at' HH:mm:ss");
        System.out.println("Poultry Production Tracker");
        System.out.println("Hunter Hatfield | " + LocalDateTime.now().format(formatter));
        System.out.println();

        try (Scanner input = new Scanner(System.in)) {
            int chickenCount = readIntInRange(input, "Enter number of chickens (1-10): ", 1, MAX_CHICKENS);
            int weekCount = readIntAtLeast(input, "Enter number of weeks to track: ", 1);

            String[] names = new String[chickenCount];
            String[] colors = new String[chickenCount];

            for (int chicken = 0; chicken < chickenCount; chicken++) {
                System.out.print("Enter the name of chicken " + (chicken + 1) + ": ");
                names[chicken] = readNonEmptyLine(input);

                System.out.print("Enter the color/breed description for " + names[chicken] + ": ");
                colors[chicken] = readNonEmptyLine(input);
            }

            int[][] eggProduction = new int[weekCount][chickenCount];
            int[] totals = new int[chickenCount];

            for (int chicken = 0; chicken < chickenCount; chicken++) {
                for (int week = 0; week < weekCount; week++) {
                    String prompt = "Enter egg production for " + names[chicken]
                            + " during week " + (week + 1) + ": ";
                    int eggs = readIntAtLeast(input, prompt, 0);
                    eggProduction[week][chicken] = eggs;
                    totals[chicken] += eggs;
                }
            }

            printSummary(names, colors, totals, weekCount);
        }
    }

    private static int readIntInRange(Scanner input, String prompt, int minimum, int maximum) {
        while (true) {
            int value = readInteger(input, prompt);
            if (value >= minimum && value <= maximum) return value;
            System.out.printf("Please enter a value from %d to %d.%n", minimum, maximum);
        }
    }

    private static int readIntAtLeast(Scanner input, String prompt, int minimum) {
        while (true) {
            int value = readInteger(input, prompt);
            if (value >= minimum) return value;
            System.out.printf("Please enter a value of at least %d.%n", minimum);
        }
    }

    private static int readInteger(Scanner input, String prompt) {
        while (true) {
            System.out.print(prompt);
            String line = input.nextLine().trim();
            try {
                return Integer.parseInt(line);
            } catch (NumberFormatException exception) {
                System.out.println("Please enter a whole number.");
            }
        }
    }

    private static String readNonEmptyLine(Scanner input) {
        while (true) {
            String value = input.nextLine().trim();
            if (!value.isEmpty()) return value;
            System.out.print("Value cannot be blank. Please try again: ");
        }
    }

    private static void printSummary(String[] names, String[] colors, int[] totals, int weekCount) {
        System.out.println("\nProduction Summary");
        System.out.println("---------------------------------------------------------------");
        System.out.printf("%-18s %-18s %10s %12s%n", "Chicken", "Color/Breed", "Total Eggs", "Avg./Week");
        System.out.println("---------------------------------------------------------------");

        int highestIndex = 0;

        for (int chicken = 0; chicken < names.length; chicken++) {
            double average = (double) totals[chicken] / weekCount;
            System.out.printf("%-18s %-18s %10d %12.2f%n",
                    names[chicken], colors[chicken], totals[chicken], average);

            if (totals[chicken] > totals[highestIndex]) highestIndex = chicken;
        }

        System.out.println("---------------------------------------------------------------");
        System.out.printf("Highest producer: %s with %d eggs over %d week%s.%n",
                names[highestIndex], totals[highestIndex], weekCount,
                weekCount == 1 ? "" : "s");
    }
}
