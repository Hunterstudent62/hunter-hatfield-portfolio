# Tutor Directory in C

A command-line tutor directory originally created by **Hunter Hatfield** for USF's COP 3514 Program Design course and lightly cleaned/refactored for portfolio use.

The assignment evolved across several projects. This version reflects the Project 10 goal of splitting the application into multiple C source and header files while retaining a dynamically allocated linked-list data model.

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

The portfolio pass intentionally stayed close to the original coursework. Changes were limited to fixing header/include issues, resolving compiler warnings, improving input validation/output, and clarifying comments and naming. The linked-list design and core assignment logic remain the original implementation.
