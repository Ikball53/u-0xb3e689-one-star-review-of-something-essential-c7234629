from pathlib import Path

# One-star review: deadpan grievance about sleep, sting lands in the final words.
review_text = "Sleep takes eight hours every night and the best part is always the part I don't remember."

destination = Path("/output/entry.txt")
destination.parent.mkdir(parents=True, exist_ok=True)
destination.write_text(review_text + "\n", encoding="utf-8")
