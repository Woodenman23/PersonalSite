from flask import url_for

skill_urls = {
    "python": "https://www.python.org/",
    "ansible": "https://www.ansible.com/",
    "git": "https://git-scm.com/",
    "linux": "https://www.linux.com/what-is-linux/",
    "apache": "https://httpd.apache.org/",
    "docker": "https://www.docker.com/",
    "aws": "https://aws.amazon.com/",
    "jenkins": "https://www.jenkins.io/",
}


class Skill:
    def __init__(self, name: str) -> None:
        self.name = name
        self.title = name.replace("_", " ").title()
        self.url = skill_urls[name]
        self.image_path = f"/static/images/skills/{name}.png"


class Image:
    def __init__(self, name: str, catagory: str) -> None:
        self.name = name
        self.path = self.get_path(name, catagory)
        self.title = name.replace("_", " ").title()

    def get_path(self, name: str, catagory: str) -> str:
        return url_for("static", filename=f"images/{catagory}/{name}")
