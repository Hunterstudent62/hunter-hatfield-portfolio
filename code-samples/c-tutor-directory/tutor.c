/*
 * Tutor Directory
 * Originally created by Hunter Hatfield for USF COP 3514 Program Design.
 * Cleaned and lightly refactored for portfolio use.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "read_line.h"
#include "tutor.h"

static int read_preferences(int preferences[3])
{
    int elementary;
    int middle;
    int high;

    if (scanf("%d %d %d", &elementary, &middle, &high) != 3) {
        while (getchar() != '\n') { ; }
        return 0;
    }

    while (getchar() != '\n') { ; }

    if ((elementary != 0 && elementary != 1) ||
        (middle != 0 && middle != 1) ||
        (high != 0 && high != 1)) {
        return 0;
    }

    preferences[0] = elementary;
    preferences[1] = middle;
    preferences[2] = high;
    return 1;
}

struct tutor *add_to_list(struct tutor *list)
{
    struct tutor *cur;
    struct tutor *new_node;
    struct tutor *prev;
    char first[NAME_LEN + 1];
    char last[NAME_LEN + 1];
    char email[EMAIL_LEN + 1];
    int preferences[3];

    printf("Enter last name: ");
    read_line(last, NAME_LEN);
    printf("Enter first name: ");
    read_line(first, NAME_LEN);
    printf("Enter email address: ");
    read_line(email, EMAIL_LEN);
    printf("Enter preferences (elementary middle high, using 0 or 1): ");

    if (!read_preferences(preferences)) {
        printf("Invalid preferences. Enter three values using only 0 or 1.\n");
        return list;
    }

    for (cur = list; cur != NULL; cur = cur->next) {
        if (strcmp(cur->last, last) == 0 && strcmp(cur->email, email) == 0) {
            printf("Tutor already exists.\n");
            return list;
        }
    }

    new_node = malloc(sizeof *new_node);
    if (new_node == NULL) {
        printf("Unable to allocate memory for a new tutor.\n");
        return list;
    }

    strcpy(new_node->first, first);
    strcpy(new_node->last, last);
    strcpy(new_node->email, email);
    for (int i = 0; i < 3; i++) {
        new_node->preferences[i] = preferences[i];
    }
    new_node->next = NULL;

    prev = NULL;
    cur = list;

    while (cur != NULL) {
        int last_cmp = strcmp(last, cur->last);

        if (last_cmp < 0) break;

        if (last_cmp == 0) {
            int first_cmp = strcmp(first, cur->first);
            if (first_cmp < 0) break;
            if (first_cmp == 0) {
                while (cur != NULL &&
                       strcmp(last, cur->last) == 0 &&
                       strcmp(first, cur->first) == 0) {
                    prev = cur;
                    cur = cur->next;
                }
                break;
            }
        }

        prev = cur;
        cur = cur->next;
    }

    if (prev == NULL) {
        new_node->next = cur;
        return new_node;
    }

    prev->next = new_node;
    new_node->next = cur;
    return list;
}

void search_list(const struct tutor *list)
{
    char level[LEVEL_LEN + 1];
    int pref_index;
    int found = 0;
    const struct tutor *cur = list;

    printf("Enter level (elementary, middle, or high): ");
    read_line(level, LEVEL_LEN);

    if (strcmp(level, "elementary") == 0) pref_index = 0;
    else if (strcmp(level, "middle") == 0) pref_index = 1;
    else if (strcmp(level, "high") == 0) pref_index = 2;
    else {
        printf("Invalid level.\n");
        return;
    }

    while (cur != NULL) {
        if (cur->preferences[pref_index] == 1) {
            printf("%s, %s - %s\n", cur->last, cur->first, cur->email);
            found = 1;
        }
        cur = cur->next;
    }

    if (!found) printf("No matching tutors found.\n");
}

void print_list(const struct tutor *list)
{
    const struct tutor *cur = list;

    if (cur == NULL) {
        printf("Tutor list is empty.\n");
        return;
    }

    printf("%-12s %-12s %-30s %6s %6s %6s\n",
           "Last", "First", "Email", "Elem", "Middle", "High");
    printf("-------------------------------------------------------------------------------------\n");

    while (cur != NULL) {
        printf("%-12s %-12s %-30s %6d %6d %6d\n",
               cur->last, cur->first, cur->email,
               cur->preferences[0], cur->preferences[1], cur->preferences[2]);
        cur = cur->next;
    }
}

void clear_list(struct tutor *list)
{
    while (list != NULL) {
        struct tutor *next = list->next;
        free(list);
        list = next;
    }
}

struct tutor *delete_from_list(struct tutor *list)
{
    char first[NAME_LEN + 1];
    char last[NAME_LEN + 1];
    char email[EMAIL_LEN + 1];
    struct tutor *cur = list;
    struct tutor *prev = NULL;

    printf("Enter last name: ");
    read_line(last, NAME_LEN);
    printf("Enter first name: ");
    read_line(first, NAME_LEN);
    printf("Enter email address: ");
    read_line(email, EMAIL_LEN);

    while (cur != NULL) {
        if (strcmp(cur->last, last) == 0 &&
            strcmp(cur->first, first) == 0 &&
            strcmp(cur->email, email) == 0) {
            if (prev == NULL) list = cur->next;
            else prev->next = cur->next;

            free(cur);
            printf("Tutor deleted.\n");
            return list;
        }

        prev = cur;
        cur = cur->next;
    }

    printf("Tutor does not exist.\n");
    return list;
}
