#!/bin/bash
# This script will help you set up and run the raylib hello world application on C3X

# Check if we're running on C3X
if [ ! -f "/VERSION" ] && [ ! -d "/data/tmp" ]; then
  echo "Warning: This doesn't appear to be a C3X device. Some features may not work correctly."
fi

# Display instructions
echo "===== Raylib for C3X Setup ====="
echo "This script will guide you through the process of setting up and running the raylib hello world application."
echo ""

# Check if raylib is already compiled
if [ -f "lib/libraylib.so" ]; then
  echo "Raylib is already compiled. Do you want to recompile it? (y/n)"
  read -r response
  if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]; then
    echo "Recompiling raylib..."
    ./build.sh
  else
    echo "Skipping compilation."
  fi
else
  echo "Raylib needs to be compiled. This will take a few minutes but only happens once."
  echo "Starting compilation..."
  ./build.sh
fi

# Check if compilation was successful
if [ ! -f "lib/libraylib.so" ]; then
  echo "Error: Compilation failed. Please check the output above for errors."
  exit 1
fi

# Run the hello world application
echo ""
echo "Running hello world application..."
./run.py

echo ""
echo "If you see a yellow window with red 'Hello, C3X!' text, the setup was successful!"
echo "You can now use raylib for your own applications on C3X."
