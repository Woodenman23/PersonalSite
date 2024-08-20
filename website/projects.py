from website import PROJECT_ROOT


class Project:
    def __init__(self, name: str) -> None:
        self.name = name
        self.title = name.replace("_", " ").title()
        self.text = (
            PROJECT_ROOT / "website/static/projects/text" / f"{name}.txt"
        ).read_text()
        self.image_path = f"/static/images/projects/{name}.png"
        self.github_url = "https://github.com/Woodenman23/virtual-assistant"
