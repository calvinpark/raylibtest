#!/usr/bin/env python3
"""
Raylib Countdown Timer for C3X
A fullscreen countdown application with interactive buttons
"""

import os
import sys
import time

# Add payload directory to Python path to find bundled modules
current_dir = os.path.dirname(os.path.abspath(__file__))
payload_dir = os.path.join(current_dir, "payload")
sys.path.insert(0, payload_dir)

# Import pyray from our bundled module
from pyray import *

# Initialize window
screen_width = 2160  # Default C3X resolution width
screen_height = 1080  # Default C3X resolution height
set_config_flags(FLAG_FULLSCREEN_MODE)
init_window(screen_width, screen_height, "C3X Countdown Timer")
set_target_fps(60)

# Countdown timer variables
countdown_seconds = 5
last_update_time = time.time()

# Button definitions
add_button_rect = Rectangle(screen_width - 300, 100, 200, 80)
sub_button_rect = Rectangle(100, 100, 200, 80)

# Main game loop
while not window_should_close():
    # Update
    current_time = time.time()
    if current_time - last_update_time >= 1.0:
        countdown_seconds -= 1
        last_update_time = current_time
    
    # Check for auto-close at zero
    if countdown_seconds <= 0:
        break
    
    # Check button interactions
    mouse_pos = get_mouse_position()
    
    # Add time button
    if (check_collision_point_rec(mouse_pos, add_button_rect) and 
        is_mouse_button_pressed(MOUSE_LEFT_BUTTON)):
        countdown_seconds += 5
    
    # Subtract time button
    if (check_collision_point_rec(mouse_pos, sub_button_rect) and 
        is_mouse_button_pressed(MOUSE_LEFT_BUTTON)):
        countdown_seconds = max(1, countdown_seconds - 5)  # Prevent going below 1
    
    # Draw
    begin_drawing()
    clear_background(YELLOW)
    
    # Draw countdown timer
    countdown_text = str(countdown_seconds)
    text_width = len(countdown_text) * 60  # Approximate width based on font size
    draw_text(countdown_text, 
              int(screen_width/2 - text_width/2), 
              int(screen_height/2 - 100), 
              200, RED)
    
    # Draw add time button
    draw_rectangle_rec(add_button_rect, GREEN)
    draw_rectangle_lines_ex(add_button_rect, 2, BLACK)
    draw_text("+5 sec", 
              int(add_button_rect.x + 20), 
              int(add_button_rect.y + 20), 
              40, BLACK)
    
    # Draw subtract time button
    draw_rectangle_rec(sub_button_rect, RED)
    draw_rectangle_lines_ex(sub_button_rect, 2, BLACK)
    draw_text("-5 sec", 
              int(sub_button_rect.x + 20), 
              int(sub_button_rect.y + 20), 
              40, BLACK)
    
    end_drawing()

# Close window and OpenGL context
close_window()
