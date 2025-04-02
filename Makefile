# Raylib Countdown Application Makefile

# Default target
all: run

# Run the countdown application
run:
	./run.py

# Clean generated files (none in this minimal version)
clean:
	@echo "Nothing to clean in this minimal version"

.PHONY: all run clean
