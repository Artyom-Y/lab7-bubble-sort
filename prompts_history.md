# Prompts History

Automatically captured prompt log. Entries are appended in chronological order (oldest first).

### 23-03-2026 14:12
- **Prompt**: read #file:copilot-instructions.md and #file:journal-logger.agent.md

### 23-03-2026 14:36
- **Prompt**: Can you review my implementation and make some suggestions? I'm preparing to make a bubble sort visualization app

### 23-03-2026 14:41
- **Prompt**: Can you set yp testing for this app, using basic pytest features and create 5 tests?

### 23-03-2026 14:51
- **Prompt**: I would like to visualize the sorting as it is happening. First, I would like to explore a terminal based approach. What do you suggest? I think a simple solution would be to switch from return statements to yield, but then we would have to rewrite the tests, so it would be difficult

### 23-03-2026 15:03
- **Prompt**: I'm interested in the in-place redraw option. Help me implement this. Create the stubs and todos in main.py. Also, is it possible to create a wrapper function for bubble_sort, to turn it into a generator? We wouldn't change bubble_sort. Instead, if we want to get values one-by-one, we would call the wrapper function. If it's possible, create some stubs for it too (remain in Socratic mode)

### 24-03-2026 15:05
- **Prompt**: Can you help me create stubs for parsing CLI agruments? I want just two: -s and -d. They stand for style (which on_swap callback will bubble_sort use?) and delay (should we wait in display_swap before printing?) I think we should use argparse for simplicity. Maybe we should declare a user_input() function. Then the question would be where to declare style and delay constants: inside or outside of if __name__ == "__main__" ? Try to be minimalistic

### 24-03-2026 15:44
- **Prompt**: Can you explain why did you add #sym:STYLE_NONE, if we never use it? Also, could you give me a very basic overview of pygame? I want to create another .py file with pygame for better visualization. Afterwards, we can import it into main.py and add a new "-s" parameter to represent it

