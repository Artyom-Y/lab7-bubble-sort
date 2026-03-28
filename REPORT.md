# Project Report: AI-Assisted Development

## 1. Initial Approach
* **Understanding:** Briefly describe your strategy for tackling the requirements.

First, I do a little brainstorm, think of what I can do/what I don't understand. 
Then I write code within my capabilities and ask AI for help/explanation when I run
into problems I can't solve.
* **Assumptions:** What did you assume about the project before starting?

That it would be more complex and that I would end up with something unreadable.

## 2. Prompting & AI Interaction
* **Successes:** What types of prompts or context worked best for you?

Prompts in agent mode when I asked AI to be minimal with changes. It provided me with concise
solutions and nice explanations.
* **Failures:** Describe specific instances where CoPilot failed (hallucinations, over-engineering, or logical errors).

1. When I asked it to write tests with pytest, it imported pytest, but wrote code using basic python.
I later used Ask mode to rewrite tests using pytests features (which significally reduced app's size)
2. AI set STYLE_NONE constant, but in argparse function it set "color" mode to default, so this constant was useless.
I changed this default to STYLE_NONE, so that if we don't provide arguments, the app doesn't provide output.
3. AI suggest me the way to animate swapping, which involved changing values of list. The thing is,
in the very code AI made, bars' position is based on index, not their value. So I pointed it out and
AI gave me a better solution (although it suggested I write another draw_bars function. Instead, I
changed the current one to work with optional parameters)
4. AI made a close_window() function, but it was never used
5. After I asked for closing windows on button press feature, it followed it very directly.
The window would close, but in a moment it would open again, because main.py called it. This meant
that closing the window mid-execution would just skip steps, instead of haulting execution. I added a check
in handle_events function: if it was called from wait_until_closed, then we close the window. Otherwise we don't,
because the array is still being sorted.
* **Analysis:** Why do you think these failures happened, and how did they impact your progress?
They weren't failures, more like inconsistencies. It was fun to find/fix them and it didn't take
too long. For me it just goes to prove that writing code without human intent is impossible. 
There must be someone overseeing it.

## 3. Key Learnings
* **Technical Skills:** What CS concepts or tools did you discover or master during this project?

1. Callback vs generator (yield)
2. ANSI escape code
3. CLI parameters for python scripts
4. Python function attributes vs global variables
5. Pygame basics
* **AI Workflow:** How will you change your use of AI tools in your next project?

Keeping those AI hiccups in mind, I might be more precise with my prompts in the next lab.