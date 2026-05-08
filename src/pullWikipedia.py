"""
    Pull the wikipedia articles for the 15 anchor albums in albums.py
    Save the data in JSON format.

"""



import json
import wikipediaapi

from pathlib import Path


USER = "VinylSage/0.1 (https://github.com/FFHighwind02/VinylSage)"
OUTPUT_DIR = Path(__file__).parent.parent / "data" / "raw" / "wikipedia"
LIMIT_RATE = 1.0





def pullArticle(wiki: wikipediaapi.Wikipedia, album: dict) -> dict | None:
    """
    Pull function that fetches a single page from wikipedia that pertains to an album.
    Returns the formatted data of the pulled page.
    """



    title = album.get("wiki_title", album["title"])
    page = wiki.page(title)

    if not page.exists():
        print(f"Error: {title} not found")
        return None


    return {
            "title": album["title"],
            "artist": album["artist"],
            "wiki_title": page.title,
            "url": page.fullurl,
            "summary": page.summary,
            "full_text": page.text,
            "source": "wikipedia",
            }









