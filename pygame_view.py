from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable
import inspect
import pygame


@dataclass
class ViewConfig:
    """Configuration for the bar visualization."""

    width: int = 1000
    height: int = 600
    fps: int = 20
    margin: int = 40
    background_color: tuple[int, int, int] = (20, 25, 35)
    bar_color: tuple[int, int, int] = (100, 200, 240)
    swap1_bar_color: tuple[int, int, int] = (255, 233, 70)
    swap2_bar_color: tuple[int, int, int] = (255, 89, 70)
    axis_color: tuple[int, int, int] = (180, 190, 220)


_CONFIG = ViewConfig()
_SCREEN: pygame.Surface | None = None
_CLOCK: pygame.time.Clock | None = None
_IS_OPEN = False
_IS_PAUSED = False


def init_window(config: ViewConfig | None = None) -> None:
    """Initialize pygame once.

    Args:
        config: None or a ViewConfig class with app parameters

    Stub-friendly behavior:
    - Creates a window and clock.
    - Stores them in module-level state for repeated updates.
    - Does not start a separate loop yet (can be called by bubble_sort function).
    """

    global _CONFIG, _SCREEN, _CLOCK, _IS_OPEN

    if _IS_OPEN:
        return

    if config is not None:
        _CONFIG = config

    pygame.init()
    _SCREEN = pygame.display.set_mode((_CONFIG.width, _CONFIG.height))
    pygame.display.set_caption("Sorting Visualizer (Pygame)")
    _CLOCK = pygame.time.Clock()
    _IS_OPEN = True


def _handle_events() -> None:
    """Process window events so OS does not mark the app as frozen."""

    global _IS_OPEN, _IS_PAUSED
    sorting_finished = inspect.stack()[1].function == "wait_until_closed"

    for event in pygame.event.get():
        if event.type == pygame.QUIT and sorting_finished:
            _IS_OPEN = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                _IS_PAUSED = not _IS_PAUSED
            if event.key in (pygame.K_ESCAPE, pygame.K_q) and sorting_finished:
                _IS_OPEN = False


def _bar_rects(values: list[int]) -> list[pygame.Rect]:
    """Compute bar rectangles from values.

    X axis = index in the list.
    Y axis = value height.

    Args:
        values: list of numbers to make rect objects for

    Returns:
        list of Pygame Rect objects
    """

    if not values:
        return []

    usable_width = _CONFIG.width - 2 * _CONFIG.margin
    usable_height = _CONFIG.height - 2 * _CONFIG.margin
    max_value = max(values) or 1
    bar_width = max(1, usable_width // len(values))

    rects: list[pygame.Rect] = []
    baseline_y = _CONFIG.height - _CONFIG.margin

    for i, value in enumerate(values):
        bar_height = int((value / max_value) * usable_height)
        x = _CONFIG.margin + i * bar_width
        y = baseline_y - bar_height
        rects.append(pygame.Rect(x, y, max(1, bar_width - 1), bar_height))

    return rects


def _draw_axes() -> None:
    """Draw simple axes."""

    if _SCREEN is None:
        return

    # Y axis
    pygame.draw.line(
        _SCREEN,
        _CONFIG.axis_color,
        (_CONFIG.margin, _CONFIG.margin),
        (_CONFIG.margin, _CONFIG.height - _CONFIG.margin),
        2,
    )
    # X axis
    pygame.draw.line(
        _SCREEN,
        _CONFIG.axis_color,
        (_CONFIG.margin, _CONFIG.height - _CONFIG.margin),
        (_CONFIG.width - _CONFIG.margin, _CONFIG.height - _CONFIG.margin),
        2,
    )


def _draw_bars(
    values: list[int],
    highlighted: list[int],
    custom_x_positions: dict[int, float] | None = None,
) -> None:
    """Draw bars, optionally with custom x positions for animation.

    Args:
        values: array of bar heights
        highlighted: indices to highlight
        custom_x_positions: dict mapping index -> custom x position (for animation)
    """
    if _SCREEN is None:
        return

    all_rects = _bar_rects(values)

    for i, rect in enumerate(all_rects):
        # If this index has a custom x-position, use it
        if custom_x_positions and i in custom_x_positions:
            rect.x = custom_x_positions[i]

        if i in highlighted:
            color = (
                _CONFIG.swap1_bar_color
                if i == highlighted[0]
                else _CONFIG.swap2_bar_color
            )
        else:
            color = _CONFIG.bar_color
        pygame.draw.rect(_SCREEN, color, rect)


def _animate_swap(
    values: list[int],
    idx1: int,
    idx2: int,
    steps: int = 8,
) -> None:
    """Very small swap animation stub.

    This is intentionally simple: it just redraws a few frames with both bars
    highlighted before/after the actual data swap in your sorting code.

    Args:
        arr: array to display
        idx2: first swapped index
        idx1: second swapped index
        steps: defines amount of animation frames
    """

    if _SCREEN is None or _CLOCK is None:
        return

    highlighted = [idx1, idx2]

    # Calculate coordinates for bar swapping animation
    normal_rects = _bar_rects(values)
    x1_start = normal_rects[idx2].x
    x2_start = normal_rects[idx1].x
    x1_end = normal_rects[idx1].x
    x2_end = normal_rects[idx2].x

    for k in range(steps):
        _handle_events()
        if not _IS_OPEN:
            return

        while _IS_PAUSED and _IS_OPEN:
            _handle_events()
            _CLOCK.tick(_CONFIG.fps)

        if not _IS_OPEN:
            return

        t = k / steps
        x1_current = x1_start + (x1_end - x1_start) * t
        x2_current = x2_start + (x2_end - x2_start) * t

        custom_x = {idx1: x1_current, idx2: x2_current}

        _SCREEN.fill(_CONFIG.background_color)
        _draw_axes()
        _draw_bars(values, highlighted, custom_x)
        pygame.display.flip()
        _CLOCK.tick(_CONFIG.fps)


def display_pygame(
    arr: Iterable[int], idx1: int | None = None, idx2: int | None = None
) -> None:
    """Render one visualization frame.

    Call this repeatedly from your sorting algorithm.
    Suggested usage pattern:
    1) call once each compare/swap step
    2) call with idx1/idx2 when those elements are active
    3) after a real swap in data, call again to show the new order

    Args:
        arr: array to display
        idx2: first swapped index
        idx1: second swapped index
    """

    if not _IS_OPEN:
        init_window()

    if not _IS_OPEN or _SCREEN is None or _CLOCK is None:
        return

    values = arr.copy()

    _handle_events()
    if not _IS_OPEN:
        return

    while _IS_PAUSED and _IS_OPEN:
        _handle_events()

        _SCREEN.fill(_CONFIG.background_color)
        _draw_axes()
        _draw_bars(values, [i for i in (idx1, idx2) if i is not None])
        pygame.display.flip()
        _CLOCK.tick(_CONFIG.fps)

    if not _IS_OPEN:
        return

    if idx1 is not None and idx2 is not None:
        _animate_swap(values, idx1, idx2)

    highlighted = [i for i in (idx1, idx2) if i is not None]

    _SCREEN.fill(_CONFIG.background_color)
    _draw_axes()
    _draw_bars(values, highlighted)
    pygame.display.flip()
    _CLOCK.tick(_CONFIG.fps)


def wait_until_closed(arr: Iterable[int] | None = None) -> None:
    """Keep the UI open until user closes it with ESC/Q/window close.

    Args:
        arr: optional final array snapshot to keep rendered while waiting
    """

    if not _IS_OPEN:
        return

    if _SCREEN is None or _CLOCK is None:
        return

    values = list(arr) if arr is not None else []

    while _IS_OPEN:
        _handle_events()
        if not _IS_OPEN:
            break

        _SCREEN.fill(_CONFIG.background_color)
        _draw_axes()
        if values:
            _draw_bars(values, [])
        pygame.display.flip()
        _CLOCK.tick(_CONFIG.fps)

    close_window()


def close_window() -> None:
    """Gracefully close pygame resources."""

    global _IS_OPEN, _IS_PAUSED

    if _IS_OPEN:
        pygame.quit()
        _IS_OPEN = False
        _IS_PAUSED = False
