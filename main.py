"""Entry point for the grader. Writes a specific line to $MAKEFUN_OUTPUT_DIR/entry.txt."""
# Entry validated: output is 1-200 chars, one sentence, deterministic.

import os
from pathlib import Path

LINE = "CronWhisperer charges exhausted cron-job automation agents fifty cents per invocation to quietly rename their crashing scripts into impressive executive milestones for the weekly status log."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"

    content = LINE + "\n"
    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError("Content validation failed")

    out_path.write_text(content, encoding="utf-8")

    print(out_path)
    print(len(content))


if __name__ == "__main__":
    main()
