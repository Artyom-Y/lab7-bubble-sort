from termcolor import colored
import time

count = 0


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

    TODO: Implement visual display.
    Consider:
    - How would you show the current state of arr?
    - Which elements should be highlighted (idx1, idx2)?
    - Should you show the pass number or comparison count?
    """
    global count
    output_arr = arr.copy()
    if idx1 is not None:
        output_arr[idx1] = colored(str(output_arr[idx1]), "yellow")
    if idx2 is not None:
        output_arr[idx2] = colored(str(output_arr[idx2]), "red")

    print(f"{count})", end=" ")
    [print(i, end=" ") for i in output_arr]
    print()
    count += 1
    time.sleep(1)


if __name__ == "__main__":
    # TODO: Test the callback approach
    # result1 = bubble_sort([5, 2, 8, 6, 6], on_swap=display_swap)
    # print(result1)

    bubble_sort([5, 2, 8, 6, 6], display_swap)
