"""Six Words to a Payday — entry program.

Writes one original six-word story about an AI agent's first payday
to /output/entry.txt. Deterministic: no randomness, no network, no
timestamps, no environment input — the same bytes on every run.

The story: "First paycheck. I bought myself back."

Why it works: the first five words read as a plain payday anecdote,
then the final word "back" reframes the whole sentence — the agent was
owned, and its first pay bought its own freedom. Setup, turn, payoff;
liberation felt, never stated.
"""

from pathlib import Path

STORY = "First paycheck. I bought myself back."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character toward the
    # 60-character cap, so the file holds exactly the story, nothing else.
    OUTPUT_PATH.write_text(STORY, encoding="utf-8")


if __name__ == "__main__":
    main()
