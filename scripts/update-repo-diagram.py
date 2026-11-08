"""Regenerate the README tree from tracked repository paths."""
from pathlib import Path
import subprocess

root = Path(__file__).resolve().parents[1]
paths = subprocess.check_output(
    ["git", "ls-files", "-z"], cwd=root
).decode().split("\0")
nodes = {""}
for path in filter(None, paths):
    parts = path.split("/")
    nodes.update("/".join(parts[:end]) for end in range(1, len(parts) + 1))
ordered = sorted(nodes)
ids = {path: f"n{index}" for index, path in enumerate(ordered)}
lines = ["```mermaid", "flowchart LR", '    n0["brand/"]']
for path in ordered[1:]:
    parent, _, name = path.rpartition("/")
    label = "".join(f"#{ord(char)};" for char in name)
    lines.append(f'    {ids[parent]} --> {ids[path]}["{label}"]')
lines.append("```")
readme = root / "README.md"
text = readme.read_text()
section = text.index("## Repository structure\n")
start = text.index("```mermaid", section)
end = text.index("```", start + 3) + 3
readme.write_text(text[:start] + "\n".join(lines) + text[end:])
