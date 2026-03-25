from termcolor import colored
from random import randint
from pygame_view import display_pygame, wait_until_closed
import time
import argparse
import os


count = 0

DISPLAY_DELAY = 1

STYLE_COLOR = "color"
STYLE_BAR = "bar"
STYLE_UI = "ui"
STYLE_NONE = "none"
DEFAULT_STYLE = STYLE_NONE


def cls():
    """Simple utility function from stack overflow to clear the console on any OS"""
    os.system("cls" if os.name == "nt" else "clear")


def parse_input_array(arr):
    """Function for parsing CLI array input"""
    parsed = []
    for el in arr.split(","):
        el = el.strip()
        if len(el) == 0:
            continue  # ignore empties
        parsed.append(int(el))

    if len(parsed) == 0:
        raise ValueError("Input array format incorrect :/")

    return parsed


def user_input() -> argparse.Namespace:
    """Parse minimal CLI arguments for sort display style and delay."""
    parser = argparse.ArgumentParser(description="Bubble sort visualization options")
    parser.add_argument(
        "-a",
        "--array",
        type=str,
        default=",".join([str(randint(1, 10)) for _ in range(5)]),
        help="Array to sort (separate each value by one comma)",
    )
    parser.add_argument(
        "-s",
        "--style",
        choices=STYLE_CALLBACKS,
        default=DEFAULT_STYLE,
        help="Display style (which callback bubble_sort should use)",
    )
    parser.add_argument(
        "-d",
        "--delay",
        type=float,
        default=1.0,
        help="Delay (seconds) before each display print",
    )
    return parser.parse_args()


def bubble_sort(arr: list, on_swap=None) -> list:
    """
    Sort array in-place using bubble sort.

    Args:
        arr: List to sort
        on_swap: Optional callback function(arr, idx1, idx2) called after each swap

    Returns:
        Sorted list (same object as input)
    """
    global count
    count = 0
    end = len(arr)

    if end in [0, 1]:
        return arr

    if on_swap:
        on_swap(arr)  # output initial list

    while end > 1:
        for i in range(0, end - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                # If on_swap callback exists, call it here
                if on_swap:
                    on_swap(arr, i, i + 1)
        end -= 1
    return arr


def display_swap(arr: list, idx1=None, idx2=None) -> None:
    """
    Display array after a swap with swapped numbers highlighted

    Args:
        arr: List to display
        idx1: first swapped number
        idx2: second swapped number

    Returns:
        None

    """
    global count

    if DISPLAY_DELAY > 0 and count != 0:
        time.sleep(DISPLAY_DELAY)

    output_arr = arr.copy()
    if idx1 is not None:
        output_arr[idx1] = colored(str(output_arr[idx1]), "yellow")
    if idx2 is not None:
        output_arr[idx2] = colored(str(output_arr[idx2]), "red")

    print(f"{count})", end=" ")
    [print(i, end=" ") for i in output_arr]
    print()
    count += 1


def display_swap_bars(arr: list, idx1=None, idx2=None) -> None:
    """
    Display array after a swap with bars representing numbers and
    clean CLI after each output. For simplicity, the bars represent
    absolute values of array's elements.


    Args:
        arr: List to display
        idx1: first swapped number
        idx2: second swapped number

    Returns:
        None

    """

    if DISPLAY_DELAY > 0:
        time.sleep(DISPLAY_DELAY)

    cls()

    output_arr = []
    for i in range(len(arr)):
        output_arr.append(f"({arr[i]}) " + "#" * abs(arr[i]))
        if i == idx1:
            output_arr[i] = colored(output_arr[i], "yellow")
        if i == idx2:
            output_arr[i] = colored(output_arr[i], "red")

    for bar in output_arr:
        print(bar)


# i had to put it after function definitions
STYLE_CALLBACKS = {
    STYLE_COLOR: display_swap,
    STYLE_BAR: display_swap_bars,
    STYLE_UI: display_pygame,
    STYLE_NONE: None,
}

if __name__ == "__main__":
    args = user_input()

    DISPLAY_DELAY = max(0.0, args.delay)
    array = parse_input_array(args.array)
    selected_callback = STYLE_CALLBACKS[args.style]
    bubble_sort(array, selected_callback)

    if args.style == STYLE_UI:
        wait_until_closed(array)
