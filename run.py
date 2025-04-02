#!/usr/bin/env python3
"""
Raylib Countdown Timer for C3X
A fullscreen countdown application with interactive buttons
"""

import os
import sys
import time
import ctypes
from ctypes import *

# Define common structures needed regardless of import method
class Rectangle(Structure):
    _fields_ = [
        ("x", c_float),
        ("y", c_float),
        ("width", c_float),
        ("height", c_float),
    ]

class Vector2(Structure):
    _fields_ = [
        ("x", c_float),
        ("y", c_float),
    ]

class Color(Structure):
    _fields_ = [
        ("r", c_ubyte),
        ("g", c_ubyte),
        ("b", c_ubyte),
        ("a", c_ubyte),
    ]

# Try to use pyray if available, otherwise use ctypes to load raylib directly
try:
    import pyray as rl
    print("Using pyray")
    
    # Create color constants to match our ctypes implementation
    YELLOW = rl.Color(255, 255, 0, 255)
    RED = rl.Color(255, 0, 0, 255)
    GREEN = rl.Color(0, 255, 0, 255)
    BLUE = rl.Color(0, 0, 255, 255)
    BLACK = rl.Color(0, 0, 0, 255)
    WHITE = rl.Color(255, 255, 255, 255)
    
    # Add these to rl namespace for consistent access
    rl.YELLOW = YELLOW
    rl.RED = RED
    rl.GREEN = GREEN
    rl.BLUE = BLUE
    rl.BLACK = BLACK
    rl.WHITE = WHITE
    
except ImportError:
    print("Pyray not found, using ctypes to load raylib directly")
    
    # Find the raylib shared library
    if os.path.exists("./lib/libraylib.so"):
        path = os.path.abspath("./lib/libraylib.so")
    else:
        path = os.path.abspath("libraylib.so")
    
    print(f"Loading raylib from: {path}")
    
    # Load the library
    raylib = CDLL(path)
    
    # Define raylib function prototypes
    raylib.InitWindow.argtypes = [c_int, c_int, c_char_p]
    raylib.CloseWindow.argtypes = []
    raylib.WindowShouldClose.restype = c_bool
    raylib.BeginDrawing.argtypes = []
    raylib.EndDrawing.argtypes = []
    raylib.ClearBackground.argtypes = [Color]
    raylib.DrawText.argtypes = [c_char_p, c_int, c_int, c_int, Color]
    raylib.DrawRectangleRec.argtypes = [Rectangle, Color]
    raylib.DrawRectangleLinesEx.argtypes = [Rectangle, c_int, Color]
    raylib.CheckCollisionPointRec.argtypes = [Vector2, Rectangle]
    raylib.CheckCollisionPointRec.restype = c_bool
    raylib.GetMousePosition.restype = Vector2
    raylib.IsMouseButtonPressed.argtypes = [c_int]
    raylib.IsMouseButtonPressed.restype = c_bool
    raylib.GetScreenWidth.restype = c_int
    raylib.GetScreenHeight.restype = c_int
    raylib.SetTargetFPS.argtypes = [c_int]
    raylib.GetFrameTime.restype = c_float
    raylib.GetMonitorWidth.argtypes = [c_int]
    raylib.GetMonitorWidth.restype = c_int
    raylib.GetMonitorHeight.argtypes = [c_int]
    raylib.GetMonitorHeight.restype = c_int
    raylib.SetConfigFlags.argtypes = [c_uint]
    
    # Define raylib constants
    MOUSE_LEFT_BUTTON = 0
    FLAG_FULLSCREEN_MODE = 2
    
    # Define colors
    YELLOW = Color(255, 255, 0, 255)
    RED = Color(255, 0, 0, 255)
    GREEN = Color(0, 255, 0, 255)
    BLUE = Color(0, 0, 255, 255)
    BLACK = Color(0, 0, 0, 255)
    WHITE = Color(255, 255, 255, 255)
    
    # Create wrapper functions to match pyray interface
    def init_window(width, height, title):
        raylib.SetConfigFlags(FLAG_FULLSCREEN_MODE)
        return raylib.InitWindow(width, height, title.encode('utf-8'))
    
    def close_window():
        return raylib.CloseWindow()
    
    def window_should_close():
        return raylib.WindowShouldClose()
    
    def begin_drawing():
        return raylib.BeginDrawing()
    
    def end_drawing():
        return raylib.EndDrawing()
    
    def clear_background(color):
        return raylib.ClearBackground(color)
    
    def draw_text(text, x, y, font_size, color):
        return raylib.DrawText(text.encode('utf-8'), x, y, font_size, color)
    
    def draw_rectangle_rec(rec, color):
        return raylib.DrawRectangleRec(rec, color)
    
    def draw_rectangle_lines_ex(rec, line_thick, color):
        return raylib.DrawRectangleLinesEx(rec, line_thick, color)
    
    def check_collision_point_rec(point, rec):
        return raylib.CheckCollisionPointRec(point, rec)
    
    def get_mouse_position():
        return raylib.GetMousePosition()
    
    def is_mouse_button_pressed(button):
        return raylib.IsMouseButtonPressed(button)
    
    def get_screen_width():
        return raylib.GetScreenWidth()
    
    def get_screen_height():
        return raylib.GetScreenHeight()
    
    def set_target_fps(fps):
        return raylib.SetTargetFPS(fps)
    
    def get_frame_time():
        return raylib.GetFrameTime()
    
    def get_monitor_width(monitor):
        return raylib.GetMonitorWidth(monitor)
    
    def get_monitor_height(monitor):
        return raylib.GetMonitorHeight(monitor)
    
    # Replace rl namespace with our wrapper functions
    class rl:
        init_window = init_window
        close_window = close_window
        window_should_close = window_should_close
        begin_drawing = begin_drawing
        end_drawing = end_drawing
        clear_background = clear_background
        draw_text = draw_text
        draw_rectangle_rec = draw_rectangle_rec
        draw_rectangle_lines_ex = draw_rectangle_lines_ex
        check_collision_point_rec = check_collision_point_rec
        get_mouse_position = get_mouse_position
        is_mouse_button_pressed = is_mouse_button_pressed
        get_screen_width = get_screen_width
        get_screen_height = get_screen_height
        set_target_fps = set_target_fps
        get_frame_time = get_frame_time
        get_monitor_width = get_monitor_width
        get_monitor_height = get_monitor_height
        MOUSE_LEFT_BUTTON = MOUSE_LEFT_BUTTON
        YELLOW = YELLOW
        RED = RED
        GREEN = GREEN
        BLUE = BLUE
        BLACK = BLACK
        WHITE = WHITE

# Initialize window
screen_width = 2160  # Default C3X resolution width
screen_height = 1080  # Default C3X resolution height
rl.init_window(screen_width, screen_height, "C3X Countdown Timer")
rl.set_target_fps(60)

# Countdown timer variables
countdown_seconds = 5
last_update_time = time.time()

# Button definitions
add_button_rect = Rectangle(screen_width - 300, 100, 200, 80)
sub_button_rect = Rectangle(100, 100, 200, 80)

# Main game loop
while not rl.window_should_close():
    # Update
    current_time = time.time()
    if current_time - last_update_time >= 1.0:
        countdown_seconds -= 1
        last_update_time = current_time
    
    # Check for auto-close at zero
    if countdown_seconds <= 0:
        break
    
    # Check button interactions
    mouse_pos = rl.get_mouse_position()
    
    # Add time button
    if (rl.check_collision_point_rec(mouse_pos, add_button_rect) and 
        rl.is_mouse_button_pressed(rl.MOUSE_LEFT_BUTTON)):
        countdown_seconds += 5
    
    # Subtract time button
    if (rl.check_collision_point_rec(mouse_pos, sub_button_rect) and 
        rl.is_mouse_button_pressed(rl.MOUSE_LEFT_BUTTON)):
        countdown_seconds = max(1, countdown_seconds - 5)  # Prevent going below 1
    
    # Draw
    rl.begin_drawing()
    rl.clear_background(rl.YELLOW)
    
    # Draw countdown timer
    countdown_text = str(countdown_seconds)
    text_width = len(countdown_text) * 60  # Approximate width based on font size
    rl.draw_text(countdown_text, 
                 int(screen_width/2 - text_width/2), 
                 int(screen_height/2 - 100), 
                 200, rl.RED)
    
    # Draw add time button
    rl.draw_rectangle_rec(add_button_rect, rl.GREEN)
    rl.draw_rectangle_lines_ex(add_button_rect, 2, rl.BLACK)
    rl.draw_text("+5 sec", 
                 int(add_button_rect.x + 20), 
                 int(add_button_rect.y + 20), 
                 40, rl.BLACK)
    
    # Draw subtract time button
    rl.draw_rectangle_rec(sub_button_rect, rl.RED)
    rl.draw_rectangle_lines_ex(sub_button_rect, 2, rl.BLACK)
    rl.draw_text("-5 sec", 
                 int(sub_button_rect.x + 20), 
                 int(sub_button_rect.y + 20), 
                 40, rl.BLACK)
    
    rl.end_drawing()

# Close window and OpenGL context
rl.close_window()
