# Poultry Production Tracker

A Java console application originally created by **Hunter Hatfield** for HCC's COP 2800 Java Programming course as P7, *Counting Your Chickens*. It has been lightly cleaned and expanded for portfolio use while retaining the original array-based design.

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

The cleanup intentionally preserves the original coursework's core architecture rather than rewriting it as a new application. Changes include clearer variable names, modern date/time handling, safer input parsing, helper methods, formatted summaries, per-week averages, and a highest-producer summary.
