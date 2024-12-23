import wikipedia
from rich import print

from website import PROJECT_ROOT


def wiki_summary(search_term: str) -> str:
    search_term = format_as_title(search_term)
    searches = wikipedia.search(search_term)
    if search_term in searches:
        return wikipedia.summary(search_term, auto_suggest=False)
    else:
        response = f"{search_term} not found. choose a similar term to find out about: "
        response.join(searches)
        return response


def format_as_title(search_term: str) -> str:
    title_words = []
    searched_words = search_term.split()
    for word in searched_words:
        if word == searched_words[0] or (
            not word.startswith("(")
            and word.lower() not in ["of", "and", "if", "on", "a"]
        ):
            word = word.capitalize()
        else:
            word = word.lower()
        title_words.append(word)

    return " ".join(title_words)


def get_flag_url(country: str) -> str:
    country = country.replace(" ", "_")
    url_path = PROJECT_ROOT / "website/static/countries/flag_urls" / f"{country}.txt"
    if url_path.exists():
        return url_path.read_text()
    country = country.capitalize()
    urls = [
        image
        for image in (wikipedia.page(country, auto_suggest=False).images)
        if f"Flag_of_{country}" in image
    ]
    url_path.write_text(urls[0])
    return urls[0]
