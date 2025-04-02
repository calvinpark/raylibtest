# Raylib Countdown Application Makefile

# Default target
all: build

# Help message
help:
	@echo "Available targets:"
	@echo "  help   - Display this help message"
	@echo "  build  - Build raylib (required before running)"
	@echo "  run    - Run the countdown application"
	@echo "  clean  - Remove all generated files"
	@echo "  deps-info - Show information about dependencies"

# Build raylib
build:
	@echo "Starting raylib compilation for C3X..."
	@# Create directories if they don't exist
	mkdir -p lib include build
	
	@# Compile raylib
	@echo "Compiling raylib..."
	cd build && cmake ../payload/raylib -DPLATFORM=PLATFORM_DESKTOP -DGRAPHICS=GRAPHICS_API_OPENGL_ES2 -DSUPPORT_SCREEN_CAPTURE=OFF -DSUPPORT_GIF_RECORDING=OFF -DBUILD_EXAMPLES=OFF || echo "CMake configuration failed, but continuing..."
	cd build && make -j$(shell nproc) || echo "Make failed, but continuing with bundled libraries..."
	
	@# Copy libraries and headers if compilation succeeded
	if [ -f build/raylib/libraylib.so ]; then \
		cp build/raylib/libraylib.so lib/; \
		cp build/raylib/libraylib.a lib/; \
		cp payload/raylib/raylib.h include/; \
		cp payload/raylib/raymath.h include/; \
		cp payload/raylib/rlgl.h include/; \
		echo "Raylib compiled successfully"; \
	else \
		echo "Using bundled raylib libraries"; \
	fi
	
	@echo "Build completed"

# Run the countdown application
run:
	@echo "Running countdown application..."
	./run.py

# Clean generated files
clean:
	@echo "Cleaning generated files..."
	rm -rf lib/* include/* build/*
	@echo "Clean completed"

# Show dependency information
deps-info:
	@echo "Dependencies required for building raylib:"
	@echo "  - cmake"
	@echo "  - build-essential"
	@echo "  - libegl-dev"
	@echo "  - libgles-dev"
	@echo "  - libwayland-dev"
	@echo "  - libxkbcommon-dev"
	@echo ""
	@echo "These dependencies should already be available on C3X devices."

.PHONY: all help build run clean deps-info
