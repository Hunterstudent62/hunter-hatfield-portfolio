# Tutor Directory in C

I originally built this command-line tutor directory for USF's COP 3514 Program Design course. The assignment was expanded over several projects, and by Project 10 I had split the program into multiple C source and header files while keeping the tutor records in a dynamically allocated linked list.

## Features

- Add tutors with name, email, and grade-level preferences
- Keep tutors sorted alphabetically by last name and first name
- Detect duplicate records using the assignment's last-name + email rule
- Search tutors by elementary, middle, or high-school preference
- Delete records from any position in the linked list
- Print the complete directory
- Free all dynamically allocated nodes before exit
- Basic validation for tutoring-preference input and search levels

## C concepts demonstrated

- Structures
- Pointers and linked lists
- Dynamic memory allocation (`malloc` / `free`)
- String comparison and copying
- Multi-file program organization
- Header files and include guards
- Input handling and validation

## Build

```bash
make
./tutor_directory
```

Or compile directly:

```bash
gcc -std=c11 -Wall -Wextra -Wpedantic project10_tutors.c tutor.c read_line.c -o tutor_directory
```

## Portfolio cleanup

For the portfolio, I kept the original assignment structure and logic instead of rewriting the project from scratch. I mainly fixed header/include problems, cleared compiler warnings, tightened some input validation and output, and cleaned up comments and names so the code is easier to read.
