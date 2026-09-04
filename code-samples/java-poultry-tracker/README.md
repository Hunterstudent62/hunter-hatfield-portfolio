# Poultry Production Tracker

I originally made this Java console program for HCC's COP 2800 Java Programming course as P7, *Counting Your Chickens*. The program tracks egg production for 1-10 chickens over however many weeks the user enters, using a two-dimensional array to store the weekly totals.

## Features

- Track 1-10 individual chickens
- Record chicken names and color/breed descriptions
- Track egg production across any positive number of weeks
- Store production data in a two-dimensional array
- Calculate total and average production per chicken
- Identify the highest-producing chicken
- Validate numeric and blank input
- Display a formatted production summary

## Java concepts demonstrated

- Arrays and two-dimensional arrays
- Loops and control flow
- Console input with `Scanner`
- Input validation
- Helper methods / decomposition
- Numeric calculations and formatted output
- Modern Java date/time API

## Build and run

```bash
javac PoultryProductionTracker.java
java PoultryProductionTracker
```

## Portfolio cleanup

For the portfolio version, I kept the same array-based program rather than turning it into a different project. I cleaned up variable names and input parsing, switched the date handling to Java's modern date/time API, broke some logic into helper methods, and improved the final summary with weekly averages and the highest-producing chicken.
