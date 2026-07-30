#!/bin/bash

# Wait for the desktop to finish loading
sleep 5

# Tell GUI programs which display to use
export DISPLAY=:0

# Go to your project
cd "/home/laylarules109/code/Desk-companion"

# Launch the program
python3 main.py
