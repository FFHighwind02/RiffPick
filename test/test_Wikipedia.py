"""
Test harness to confirm proper setup of the Wikipedia API



"""


import wikipediaapi
import pytest


@pytest.fixture
def wiki():
    
    return wikipediaapi.Wikipedia(user_agent='VinylSage (https://github.com/FFHighwind02/VinylSage)', language='en')



def test_fetch_page(wiki):
    
    testPage = wiki.page("The Wall")    # Pink Floyd's 'The Wall'
    assert testPage.exists()
    assert len(testPage.text) > 1000    # Ensure the pull is a real album article not unfinished stub data
    assert "Another Brick" in testPage.text



def test_nonexistant_page(wiki):

    testPage = wiki.page("Led Zeppelin XVIIIIIIIII8")
    assert not testPage.exists()

