#!/usr/bin/env python3
import os
import sys
import ctypes
from ctypes import *

# Add the lib directory to the path
lib_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib")
if os.path.exists(lib_dir):
    sys.path.insert(0, lib_dir)

try:
    # Try to import pyray if available
    import pyray as rl
    print("Using pyray module")
except ImportError:
    # If pyray is not available, use ctypes to load raylib directly
    print("Pyray not found, using ctypes to load raylib directly")
    
    # Find the raylib shared library
    raylib_paths = [
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib", "libraylib.so"),
        "/usr/local/lib/libraylib.so",
        "./libraylib.so"
    ]
    
    raylib = None
    for path in raylib_paths:
        if os.path.exists(path):
            print(f"Loading raylib from: {path}")
            raylib = CDLL(path)
            break
    
    if raylib is None:
        print("Error: Could not find raylib library. Make sure to run build.sh first.")
        sys.exit(1)
    
    # Define raylib function prototypes
    raylib.InitWindow.argtypes = [c_int, c_int, c_char_p]
    raylib.InitWindow.restype = None
    
    raylib.WindowShouldClose.argtypes = []
    raylib.WindowShouldClose.restype = c_bool
    
    raylib.BeginDrawing.argtypes = []
    raylib.BeginDrawing.restype = None
    
    raylib.EndDrawing.argtypes = []
    raylib.EndDrawing.restype = None
    
    raylib.ClearBackground.argtypes = [c_uint]
    raylib.ClearBackground.restype = None
    
    raylib.DrawText.argtypes = [c_char_p, c_int, c_int, c_int, c_uint]
    raylib.DrawText.restype = None
    
    raylib.CloseWindow.argtypes = []
    raylib.CloseWindow.restype = None
    
    # Create color constants
    class Color(Structure):
        _fields_ = [
            ("r", c_ubyte),
            ("g", c_ubyte),
            ("b", c_ubyte),
            ("a", c_ubyte),
        ]
    
    YELLOW = Color(255, 255, 0, 255)
    RED = Color(255, 0, 0, 255)
    
    # Create wrapper functions for easier use
    class rl:
        @staticmethod
        def init_window(width, height, title):
            raylib.InitWindow(width, height, title.encode('utf-8'))
        
        @staticmethod
        def window_should_close():
            return raylib.WindowShouldClose()
        
        @staticmethod
        def begin_drawing():
            raylib.BeginDrawing()
        
        @staticmethod
        def end_drawing():
            raylib.EndDrawing()
        
        @staticmethod
        def clear_background(color):
            # Convert Color structure to uint
            color_value = (color.r << 24) | (color.g << 16) | (color.b << 8) | color.a
            raylib.ClearBackground(color_value)
        
        @staticmethod
        def draw_text(text, x, y, font_size, color):
            # Convert Color structure to uint
            color_value = (color.r << 24) | (color.g << 16) | (color.b << 8) | color.a
            raylib.DrawText(text.encode('utf-8'), x, y, font_size, color_value)
        
        @staticmethod
        def close_window():
            raylib.CloseWindow()
        
        # Define colors
        YELLOW = YELLOW
        RED = RED

def main():
    # Initialize window
    screen_width = 800
    screen_height = 450
    rl.init_window(screen_width, screen_height, "Raylib Hello World")
    
    # Main game loop
    while not rl.window_should_close():
        # Draw
        rl.begin_drawing()
        rl.clear_background(rl.YELLOW)  # Yellow background
        
        # Calculate text position to center it
        text = "Hello, C3X!"
        font_size = 100
        text_width = len(text) * font_size * 0.5  # Approximate width
        text_x = screen_width/2 - text_width/2
        text_y = screen_height/2 - font_size/2
        
        rl.draw_text(text, int(text_x), int(text_y), font_size, rl.RED)  # Red text
        rl.end_drawing()
    
    # Close window
    rl.close_window()

if __name__ == "__main__":
    main()
