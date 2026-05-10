"""
    Test Harness for the pull wikipedia script.


"""



import pytest
import wikipediaapi

from src.pullWikipedia import pullArticle




@pytest.fixture
def wiki():
    return wikipediaapi.Wikipedia(user_agent="VinylSage-Testing/0.1")




def test_fetch_expected_pull(wiki):
    album = {"title": "Aja", "artist": "Steely Dan", "wiki_title": "Aja (album)"}
    result = pullArticle(wiki, album)

    assert result is not None
    assert result["title"] == "Aja"
    assert result["artist"] == "Steely Dan"
    assert "full_text" in result
    assert "url" in result
    




def test_fetch_missing_page(wiki):

    album = {"title": "FakeAlbumahaah", "artist": "Ninajfa", "wiki_title": "thispagedoesnotexistblu7787030"}
    result = pullArticle(wiki, album)

    assert result is None




def test_fetch_uses_wiki_title(wiki):

     album = {"title": "Aja", "artist": "Steely Dan", "wiki_title": "Aja (album)"}
     result = pullArticle(wiki, album)


     assert result["title"] == "Aja"
     assert "Steely Dan" in result["full_text"]



