#!/usr/bin/env python3
# https://wiki.libsdl.org/SDL_CreateWindow

# Example program:
# Using SDL2 to create an application window

import sys
from sdl2 import *

def run():

    SDL_Init(SDL_INIT_VIDEO)              # Initialize SDL2

    # Create an application window with the following settings:
    window = SDL_CreateWindow(
        bytes("An SDL2 window", 'utf-8'),  # window title
        SDL_WINDOWPOS_UNDEFINED,           # initial x position
        SDL_WINDOWPOS_UNDEFINED,           # initial y position
        640,                               # width, in pixels
        480,                               # height, in pixels
        SDL_WINDOW_OPENGL                  # flags - see below
    )

    # Check that the window was successfully created
    if window == None:
        # In the case that the window could not be made...
        print("Could not create window: %s", SDL_GetError().decode('utf-8'))
        return 1

    # The window is open: could enter program loop here (see SDL_PollEvent())

    SDL_Delay(3000)  # Pause execution for 3000 milliseconds, for example

    # Close and destroy the window
    SDL_DestroyWindow(window)

    # Clean up
    SDL_Quit()
    return 0

if __name__ == "__main__":
    sys.exit(run())
