from website import PROJECT_ROOT, IMAGES_PATH
from website.wiki_search import wiki_summary, get_flag_url


class Country:
    def __init__(self, name: str) -> None:
        self.name = name
        self.title = (self.name.replace("_", " ")).title()
        self.urls = {
            "travel_advice": f"https://www.gov.uk/foreign-travel-advice/{name}",
            "lonely_planet": f"https://www.lonelyplanet.com/{name}",
            "hostel_world": f"https://www.hostelworld.com/st/hostels/{name}",
            "flag": get_flag_url(name),
            "redit": f"https://www.reddit.com/r/{name}",
        }
        self.visited = (IMAGES_PATH / name).exists()

    def get_text(self) -> str:
        text_path = PROJECT_ROOT / "website/static/countries/text" / f"{self.name}.txt"
        if text_path.exists():
            return text_path.read_text()
        else:
            text = wiki_summary(self.name)
            text_path.write_text(text)
            return text

    def get_images(self):
        files = (IMAGES_PATH / self.name).glob("*")
        return [
            file.name
            for file in files
            if file.is_file() and file.name.lower().endswith((".jpg", ".png"))
        ]
