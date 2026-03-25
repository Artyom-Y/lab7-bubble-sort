# Bubble Sort Visualizer

Small learning project that demonstrates in-place bubble sort with optional
visualization callbacks.

## Overview

- Sorting algorithm: bubble sort (in-place)
- Display styles:
	- none: no visualization
	- color: console output with swapped values highlighted
	- bar: console output as bars
	- ui: pygame window with animated swaps
- CLI parsing with argparse for array input, style, and delay

## Installation

1. Create and activate a virtual environment (optional but recommended).
2. Install dependencies from requirements.txt:

	 pip install -r requirements.txt

## Usage

Run (from virtual environment if you have it installed):

python main.py [options]

CLI parameters:

- -a, --array: comma-separated integers to sort
	- Example: --array 5,2,9,1,3
- -s, --style: visualization style
	- Choices: color, bar, ui, none
	- Default: none
- -d, --delay: delay in seconds between display updates (for "bar" and "color" styles)
	- Example: --delay 0.2

Examples:

- python main.py --style none
- python main.py --array 9,4,7,1 --style color --delay 0.3
- python main.py --array 3,2,1 --style bar --delay 0.5
- python main.py --array 5,2,5,6,3,56,17,8 --style ui

## UI Controls

When running with --style ui:

- SPACE: pause/resume animation
- ESC or Q: close the window after an array is sorted. Because UI has no control over the caller function (bubble_sort),
trying to close UI mid-sorting was pointless, as bubble_sort opens it on each iterations. So I made quitting UI possible only
after an array has finished sorting. You can kill the program by just closing the terminal.

After sorting completes, the UI stays open and keeps rendering the final
state until you close it.

## Notes About Negative Values

Use "--array=..." syntax without whitespace after equality sign if your
array starts with a negative value.

Negative values work fine with "color" style. In "bar" style the absolute
value is used to draw bars. In "UI" mode negative values are represented as a
blank space.