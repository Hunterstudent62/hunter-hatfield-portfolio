/*
 * Tutor Directory
 * Originally created by Hunter Hatfield for USF COP 3514 Program Design.
 * Project 10 refactored an earlier linked-list assignment into multiple files.
 */

#include <stdio.h>

#include "tutor.h"

int main(void)
{
    char code;
    struct tutor *tutor_list = NULL;

    printf("Tutor Directory\n");
    printf("Operations: a = add, s = search, d = delete, p = print, q = quit\n\n");

    for (;;) {
        printf("Enter operation code: ");

        if (scanf(" %c", &code) != 1) {
            clear_list(tutor_list);
            return 0;
        }

        while (getchar() != '\n') {
            ;
        }

        switch (code) {
            case 'a':
                tutor_list = add_to_list(tutor_list);
                break;
            case 's':
                search_list(tutor_list);
                break;
            case 'd':
                tutor_list = delete_from_list(tutor_list);
                break;
            case 'p':
                print_list(tutor_list);
                break;
            case 'q':
                clear_list(tutor_list);
                return 0;
            default:
                printf("Illegal code.\n");
        }

        printf("\n");
    }
}
