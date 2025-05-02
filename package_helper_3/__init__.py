from importlib.metadata import metadata

infos = metadata(__name__)
__version__ = infos["Version"]

# Parse authors from Author-email (may contain multiple entries)
author_email = infos.get("Author-email")
authors = []

if author_email:
    # Split entries by commas (handles multiple authors)
    entries = [e.strip() for e in author_email.split(",")]
    for entry in entries:
        # Split each entry into name and email
        if "<" in entry and ">" in entry:
            name, email = entry.split("<", 1)
            email = email.strip(">").strip()
            authors.append({"name": name.strip(), "email": email})
        else:
            authors.append({"name": entry, "email": None})

# Expose as needed (e.g., first author)
__author__ = authors[0]["name"] if authors else "Unknown"
__email__ = authors[0]["email"] if authors else None
