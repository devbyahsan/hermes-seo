#!/usr/bin/env python3
"""
Hermes schema-validator hook.

After a file is edited or written, this handler scans for JSON-LD
structured data and reports any schema violations the agent might have
introduced. It is a Hermes port of the claude-seo validate-schema.py hook.

Usage:
    hermes-seo run hooks/validate-schema.py <file_path>

Exit codes:
    0 = no schema issues found
    1 = schema issues found
    2 = error
"""

import json
import sys
from pathlib import Path

# Core schema.org types that are valid for general use.
VALID_TYPES = {
    "Article", "BlogPosting", "NewsArticle", "WebPage", "Organization",
    "SiteNavigationElement", "WebSite", "Product", "ImageObject",
    "VideoObject", "BreadcrumbList", "FAQPage", "QAPage", "LocalBusiness",
    "Restaurant", "CafeOrCoffeeShop", "MedicalBusiness", "MedicalClinic",
    "FurnitureStore", "HomeAndConstructionBusiness", "Store",
}

# Schema types known to be deprecated or problematic for SEO.
DEPRECATED_TYPES = {
    "HowTo",        # Google deprecated HowTo rich results (Sept 2023)
    "VideoGameSection",
    "MusicRecordingSection",
    "PainPoint",
}

# Fields that trigger warnings when present.
WARN_FIELDS = {
    "sameAs",       # Only a warning if excessive
}


def load_json(path: Path) -> dict | list | None:
    """Load and parse a JSON file. Returns None on failure."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, UnicodeDecodeError, OSError) as e:
        print(f"  [warn] Could not parse {path}: {e}", file=sys.stderr)
        return None


def validate_jsonld(data) -> list:
    """Validate JSON-LD structured data. Returns list of issue strings."""
    issues = []
    errors = []

    # Handle array of @graph objects, or single object
    items = data if isinstance(data, list) else [data]

    for idx, item in enumerate(items):
        if not isinstance(item, dict):
            continue

        # Check @type
        item_type = item.get("@type")
        if isinstance(item_type, list):
            item_type = item_type[0]  # Take first type in list

        if not item_type:
            errors.append(f"Item {idx}: missing @type")
            continue

        # Check deprecation
        for t in (item_type if isinstance(item_type, list) else [item_type]):
            if t in DEPRECATED_TYPES:
                errors.append(f"Item {idx}: deprecated type '{t}'")

        # Check required @context
        if "@context" not in item:
            errors.append(f"Item {idx}: missing @context")

    return errors, issues


def main():
    if len(sys.argv) < 2:
        print("Usage: validate-schema.py <file_path>", file=sys.stderr)
        return 2

    file_path = Path(sys.argv[1])

    if not file_path.exists():
        print(f"  [info] File not found: {file_path}", file=sys.stderr)
        return 0

    # Only process supported file types
    if file_path.suffix.lower() not in (".json", ".jsonld", ".html", ".htm"):
        return 0

    data = load_json(file_path)
    if data is None:
        return 2

    errors, issues = validate_jsonld(data)

    for err in errors:
        print(f"  [error] {file_path}: {err}", file=sys.stderr)

    for issue in issues:
        print(f"  [warn] {file_path}: {issue}", file=sys.stderr)

    # Return exit code based on findings
    if errors:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
