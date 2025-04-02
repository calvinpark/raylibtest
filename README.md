# Raylib for C3X - Usage Instructions

This package contains everything needed to compile and run raylib on C3X devices with proper Wayland support.

## Contents

- `raylib/` - Source code for raylib with C3X-specific modifications
- `Makefile` - Build system for compiling and running raylib
- `run.py` - Hello world application using the compiled raylib
- `lib/` - Directory where compiled libraries are installed
- `include/` - Directory where header files are installed

## Quick Start

1. Transfer this entire folder to your C3X device
2. Run the build command:
   ```
   make build
   ```
3. Run the hello world application:
   ```
   make run
   ```

## Available Make Commands

- `make build` - Compile raylib for C3X
- `make run` - Run the hello world application
- `make clean` - Remove all generated files
- `make help` - Display help information about available commands
- `make deps-info` - Display information about required dependencies

## What to Expect

- The build process will compile raylib specifically for the C3X device using the PLATFORM_COMMA configuration
- The compilation uses Wayland and EGL as required by C3X
- The hello world application will display "Hello, C3X!" in red text on a yellow background
- The compilation only needs to be done once per device/AGNOS version

## Dependencies

The necessary dependencies for compilation should already be available on your C3X device:
- build-essential
- libegl-dev
- libgles-dev
- libwayland-dev
- libxkbcommon-dev

These are the standard dependencies used by the AGNOS system for graphics support.

## Important Note About Wayland Environment

This implementation requires a working Wayland display server, which is present on C3X devices but not in most development environments. If you try to run the hello world application in a non-C3X environment, you will likely see an error like:

```
WARNING: COMMA: Failed to create a Wayland display. Failed with: No such file or directory
FATAL: COMMA: Failed to initialize Wayland
```

This is expected behavior in environments without Wayland and does not indicate a problem with the implementation. The application will work correctly on actual C3X devices with the proper Wayland environment.

## Using Raylib in Your Own Projects

After compilation, you can use raylib in your own projects:

1. Include the header files:
   ```c
   #include "raylib.h"
   ```

2. Link against the compiled libraries:
   ```
   gcc -o myapp myapp.c -I./include -L./lib -lraylib -lwayland-client -lwayland-cursor -lwayland-egl -lEGL -lGLESv2 -lm -lpthread -lrt -ldl
   ```

3. For Python projects, you can use the ctypes approach as shown in run.py

## Troubleshooting

If you encounter issues:

1. Verify that the compiled libraries exist in the lib directory
2. Check for any error messages during compilation or execution
3. If compilation fails, check that the required dependencies are available using `make deps-info`
4. Remember that the application will only run properly on a C3X device with Wayland

## Notes

- This implementation uses the existing raylib Makefile with PLATFORM_COMMA target
- The raylib source includes the custom platform implementation for C3X (rcore_comma.c)
- The hello world application will try to use pyray if available, or fall back to loading raylib directly
- The implementation specifically targets Wayland/EGL as used by C3X, not X11
