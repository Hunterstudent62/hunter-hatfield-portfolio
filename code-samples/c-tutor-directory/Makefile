CC = gcc
CFLAGS = -std=c11 -Wall -Wextra -Wpedantic
TARGET = tutor_directory
SOURCES = project10_tutors.c tutor.c read_line.c

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) $(SOURCES) -o $(TARGET)

clean:
	rm -f $(TARGET)
