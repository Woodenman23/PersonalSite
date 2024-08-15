import wikipedia
from rich import print


def wiki_search(search_term: str) -> str | None:
    search_term = format_as_title(search_term)
    print(search_term)
    searches = wikipedia.search(search_term)
    if search_term in searches:
        return wikipedia.summary(search_term, auto_suggest=False)
    else:
        print(f"{search_term} not found. choose a similar term to find out about: ")
        for term in searches:
            print(term)
        return None


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
