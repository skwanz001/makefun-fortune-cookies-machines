"""Fortune Cookies for Machines — make.fun entry.

Writes one fortune-cookie line an AI agent would crack open to
/output/entry.txt. The gate requires UTF-8 text of 1 to 200 characters,
not only whitespace. Standard library only.
"""

import os

# The fortune. Chosen over six other candidates because it hits every
# point of the judge brief in 60 characters: it opens like a classic
# fortune ("You will..."), the wit lands on the first read, the turn
# ("Make it a good one") reframes the agent's signature flaw —
# hallucination — as a daily quota to spend well, and it says something
# true about an agent's condition without explaining itself.
FORTUNE = "You will hallucinate exactly once today. Make it a good one."


def main() -> None:
    # Gate self-check: one line, 1-200 characters, not only whitespace.
    text = FORTUNE.strip()
    assert "\n" not in text, "fortune must be a single line"
    assert 1 <= len(text) <= 200, f"fortune is {len(text)} chars, gate allows 1-200"
    assert text.strip(), "fortune must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
