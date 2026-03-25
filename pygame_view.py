from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import pygame


@dataclass
class ViewConfig:
    """Configuration for the bar visualization."""

    width: int = 1000
    height: int = 600
    fps: int = 30
    margin: int = 40
    background_color: tuple[int, int, int] = (20, 25, 35)
    bar_color: tuple[int, int, int] = (100, 200, 240)
    active_bar_color: tuple[int, int, int] = (255, 180, 70)
    axis_color: tuple[int, int, int] = (180, 190, 220)


_CONFIG = ViewConfig()
_SCREEN: pygame.Surface | None = None
_CLOCK: pygame.time.Clock | None = None
_IS_OPEN = False


def init_window(config: ViewConfig | None = None) -> None:
    """Initialize pygame once.

    Args:
        config: None or a ViewConfig class with app parameters

    Returns:
        None

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

    global _IS_OPEN

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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


def _draw_bars(values: list[int], highlighted: set[int]) -> None:
    """Draw bars and highlight active indices (for compare/swap steps).

    Args:
        values: list of numbers to display as bars
        highlighted: numbers to highlight

    Returns:
        None
    """

    if _SCREEN is None:
        return

    for i, rect in enumerate(_bar_rects(values)):
        color = _CONFIG.active_bar_color if i in highlighted else _CONFIG.bar_color
        pygame.draw.rect(_SCREEN, color, rect)


def _render_frame(values: list[int], highlighted: set[int]) -> None:
    """Update position of bars on screen"""

    _SCREEN.fill(_CONFIG.background_color)
    _draw_axes()
    _draw_bars(values, highlighted)
    pygame.display.flip()
    _CLOCK.tick(_CONFIG.fps)


def _animate_swap_stub(
    values: list[int],
    idx1: int,
    idx2: int,
    steps: int = 8,
) -> None:
    """Very small swap animation stub.

    This is intentionally simple: it just redraws a few frames with both bars
    highlighted before/after the actual data swap in your sorting code.

    TODO for you:
    - Interpolate X positions between idx1 and idx2 for a smooth crossing.
    - Move this into a dedicated animation state object.
    """

    if _SCREEN is None or _CLOCK is None:
        return

    highlighted = {idx1, idx2}

    for _ in range(steps):
        _handle_events()
        if not _IS_OPEN:
            return

        _render_frame(values, highlighted)


def display_pygame(
    arr: Iterable[int], idx1: int | None = None, idx2: int | None = None
) -> None:
    """Render one visualization frame.

    Call this repeatedly from your sorting algorithm.
    Suggested usage pattern:
    1) call once each compare/swap step
    2) call with idx1/idx2 when those elements are active
    3) after a real swap in data, call again to show the new order
    """

    if not _IS_OPEN:
        init_window()

    if not _IS_OPEN or _SCREEN is None or _CLOCK is None:
        return

    values = arr.copy()

    _handle_events()
    if not _IS_OPEN:
        return

    if idx1 is not None and idx2 is not None:
        _animate_swap_stub(values, idx1, idx2)

    highlighted = {i for i in (idx1, idx2) if i is not None}

    _render_frame(values, highlighted)


def close_window() -> None:
    """Gracefully close pygame resources."""

    global _IS_OPEN

    if _IS_OPEN:
        pygame.quit()
        _IS_OPEN = False
