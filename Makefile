# Makefile for raylib-sourced project for C3X

# Directories
LIB_DIR = lib
INCLUDE_DIR = include
RAYLIB_SRC_DIR = raylib/src

# Default target
all: build

# Clean target - removes all generated files
clean:
	@echo "Cleaning generated files..."
	@rm -rf $(LIB_DIR)/* $(INCLUDE_DIR)/*
	@cd $(RAYLIB_SRC_DIR) && make clean
	@echo "Clean complete!"

# Build target - compiles raylib for C3X
build:
	@echo "Starting raylib compilation for C3X..."
	
	# Create directories if they don't exist
	@mkdir -p $(LIB_DIR) $(INCLUDE_DIR)
	
	# Compile raylib for PLATFORM_COMMA
	@echo "Compiling raylib..."
	@cd $(RAYLIB_SRC_DIR) && make clean && make PLATFORM=PLATFORM_COMMA RAYLIB_LIBTYPE=SHARED
	
	# Create static library
	@echo "Creating static library..."
	@cd $(RAYLIB_SRC_DIR) && ar rcs ../../$(LIB_DIR)/libraylib.a rcore.o rshapes.o rtextures.o rtext.o rmodels.o utils.o raudio.o
	
	# Create shared library with explicit Wayland libraries
	@echo "Creating shared library..."
	@cd $(RAYLIB_SRC_DIR) && gcc -shared -o ../../$(LIB_DIR)/libraylib.so rcore.o rshapes.o rtextures.o rtext.o rmodels.o utils.o raudio.o \
		-lwayland-client -lwayland-cursor -lwayland-egl -lEGL -lGLESv2 -lm -lpthread -lrt -ldl
	
	# Copy header files
	@echo "Copying header files..."
	@cp $(RAYLIB_SRC_DIR)/raylib.h $(RAYLIB_SRC_DIR)/raymath.h $(RAYLIB_SRC_DIR)/rlgl.h $(INCLUDE_DIR)/
	
	@echo "Raylib compilation complete!"
	@echo "Libraries installed in ./$(LIB_DIR)"
	@echo "Headers installed in ./$(INCLUDE_DIR)"

# Run target - runs the hello world application
run:
	@echo "Running hello world application..."
	@chmod +x run.py
	@./run.py

# Help target
help:
	@echo "Available targets:"
	@echo "  all    - Same as 'build'"
	@echo "  clean  - Remove all generated files"
	@echo "  build  - Compile raylib for C3X"
	@echo "  run    - Run the hello world application"
	@echo "  help   - Display this help message"

# Dependencies information (no automatic installation)
deps-info:
	@echo "Required dependencies for raylib on C3X:"
	@echo "  - build-essential"
	@echo "  - libegl-dev"
	@echo "  - libgles-dev"
	@echo "  - libwayland-dev"
	@echo "  - libxkbcommon-dev"
	@echo ""
	@echo "These should already be available on your C3X device."
	@echo "If compilation fails, please ensure these dependencies are installed."

.PHONY: all clean build run help deps-info
