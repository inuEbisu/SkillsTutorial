# A tiny multi-file C project for teaching GNU Make basics

# Compiler and flags
CC := gcc
CFLAGS := -Wall -Wextra -std=c11 -O2

# Target executable name
TARGET := multi

# Source files in this project (multi-file!)
SRCS := main.c greet.c calc.c

# Derive object files from sources: foo.c -> foo.o
OBJS := $(SRCS:.c=.o)

.PHONY: all clean run

# Default goal builds the executable
all: $(TARGET)

# Link step: combine all object files into the final binary
$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $@ $^

# Compile step: pattern rule for .c -> .o
# $< is the first prerequisite (the .c file), $@ is the target (the .o file)
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# Header dependencies: if a header changes, rebuild the affected .o
main.o: greet.h calc.h
greet.o: greet.h
calc.o: calc.h

# Convenience: run the program after building
run: $(TARGET)
	./$(TARGET)

# Clean up build artifacts
clean:
	rm -f $(OBJS) $(TARGET)
