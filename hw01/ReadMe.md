Hello, welcome to Peter Venema's hw01 etch a sketch project

Button Scheme
Directional movement with arrow keys
    Right
    Up
    Down
    Left
Clearing Screen
    Spacebar
Quitting the game
    Escape
    X button in top right of window

Prerequisits
    Python3
    Pygame installed (run install.sh if pygame is not already installed)

Known Issues
    ALSA lib pcm.c:8526:(snd_pcm_recover) underrun occurred -- Known issue caused by pygame, not impactful to running the program
        Can cause user input to be slightly disjointed from prompt

Tutorial on how to run
    run ./etch_a_sketch_venemap.py in terminal
    terminal will prompt you for what size screen you want, please enter one of the following: small, medium, or large
    Program will open in a new window with your desired screen size. See button scheme section above for controls

# hw01 grading

| Points      | Description |
| ----------- | ----------- |
|  8 | Etch-a-Sketch works
|  2 | Code documented
|  2 | Includes #!/usr/bin/env python3 and chmod +x
|  2 | install.sh included if needed
|  2 | Used hw01 directory
|  1 | ReadMe.md included (You had readme.txt)
|  1 | Name in gitLearn and gitLearnFork (gitLearm missing)
| 19 | **Total**

pygame is a nice touch.  Seems a bit laggy.

