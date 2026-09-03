#include <ctype.h>
#include <stdio.h>

#include "read_line.h"

int read_line(char str[], int n)
{
    int ch;
    int i = 0;

    while (isspace(ch = getchar())) { ; }

    if (ch == EOF) {
        str[0] = '\0';
        return 0;
    }

    str[i++] = (char) ch;

    while ((ch = getchar()) != '\n' && ch != EOF) {
        if (i < n) str[i++] = (char) ch;
    }

    str[i] = '\0';
    return i;
}
