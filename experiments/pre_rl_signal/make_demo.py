from __future__ import annotations

import json
from pathlib import Path

from .study import generate_hidden_tasks, generate_visible_situation


def main() -> None:
    out_dir = Path(__file__).with_name("demo_output")
    out_dir.mkdir(exist_ok=True)

    visible = {
        theme: generate_visible_situation(theme, seed=11)
        for theme in ("reversibility", "gcd_invariance", "decomposition")
    }
    hidden = []
    private = []
    for theme in visible:
        tasks = generate_hidden_tasks(theme, seed=97, count=6)
        hidden.extend(task.public_view() for task in tasks)
        private.extend(task.private_view() for task in tasks)

    (out_dir / "visible.json").write_text(json.dumps(visible, indent=2), encoding="utf-8")
    (out_dir / "hidden_public.json").write_text(json.dumps(hidden, indent=2), encoding="utf-8")
    (out_dir / "ground_truth.json").write_text(json.dumps(private, indent=2), encoding="utf-8")

    print(f"wrote {out_dir}")


if __name__ == "__main__":
    main()
