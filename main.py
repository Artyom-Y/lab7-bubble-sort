from termcolor import colored
from random import randint
import time
import argparse


count = 0

DISPLAY_DELAY = 0.0

STYLE_COLOR = "color"
STYLE_NONE = "none"
DEFAULT_STYLE = STYLE_NONE


def bubble_sort(arr: list, on_swap=None) -> list:
    """
    Sort array in-place using bubble sort.

    Args:
        arr: List to sort
        on_swap: Optional callback function(arr, idx1, idx2) called after each swap

    Returns:
        Sorted list (same object as input)
    """
    end = len(arr)
    count = 0
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
    Display array after a swap.


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


STYLE_CALLBACKS = {
    STYLE_COLOR: display_swap,
    STYLE_NONE: None,
}


def user_input() -> argparse.Namespace:
    """Parse minimal CLI arguments for sort display style and delay."""
    parser = argparse.ArgumentParser(description="Bubble sort visualization options")
    parser.add_argument(
        "-a",
        "-array",
        type=str,
        default=",".join([str(randint(-10, 10)) for _ in range(5)]),
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
        default=0.0,
        help="Delay (seconds) before each display print",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = user_input()

    DISPLAY_DELAY = max(0.0, args.delay)
    array = [int(number) for number in args.a.split(",")]
    selected_callback = STYLE_CALLBACKS[args.style]
    bubble_sort(array, selected_callback)
