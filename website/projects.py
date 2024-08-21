from website import PROJECT_ROOT


class Project:
    def __init__(self, name: str) -> None:
        self.name = name
        self.title = name.replace("_", " ").title()
        self.text = (
            PROJECT_ROOT / "website/static/projects/text" / f"{name}.md"
        ).read_text()
        self.image_name = f"{name}.png"
        self.image_path = f"/static/images/projects/{self.image_name}"
        self.github_url = f"https://github.com/Woodenman23/{name}"
