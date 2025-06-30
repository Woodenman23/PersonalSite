# Skills Configuration
# Maps skill names to their official documentation/website URLs

# Systems & Infrastructure Skills
SYSTEMS_INFRASTRUCTURE_SKILLS = {
    # Cloud & Infrastructure
    "AWS": "https://aws.amazon.com/",
    "GCP": "https://cloud.google.com/",
    "Docker": "https://www.docker.com/",
    "Kubernetes": "https://kubernetes.io/",
    "Terraform": "https://www.terraform.io/",
    "Ansible": "https://www.ansible.com/",
    
    # CI/CD & DevOps Tools
    "CI/CD": "https://about.gitlab.com/topics/ci-cd/",
    "GitLab": "https://gitlab.com/",
    "Jenkins": "https://www.jenkins.io/",
    "Zuul": "https://zuul-ci.org/",
    "Gerrit": "https://www.gerritcodereview.com/",
    "Apache": "https://httpd.apache.org/",
    "Nginx": "https://nginx.org/",
    
    # Operating Systems & Infrastructure
    "Linux": "https://www.linux.org/",
    "Windows": "https://www.microsoft.com/en-us/windows/",
    "Networking/Security": "https://www.cisco.com/c/en/us/solutions/enterprise-networks/",
    
    # AI & Machine Learning
    "LLM Prompt Engineering": "https://platform.openai.com/docs/guides/prompt-engineering",
    "LangChain": "https://python.langchain.com/",
    "OpenAI API": "https://platform.openai.com/docs/api-reference",
    "PyTorch": "https://pytorch.org/",
    "Torchvision": "https://pytorch.org/vision/stable/index.html"
}

# Languages, APIs & Tooling Skills
LANGUAGES_APIS_TOOLING_SKILLS = {
    # Programming Languages
    "Python": "https://www.python.org/",
    "Go": "https://golang.org/",
    "Bash/Shell Scripting": "https://www.gnu.org/software/bash/",
    "JavaScript": "https://developer.mozilla.org/en-US/docs/Web/JavaScript",
    
    # AI & APIs
    "Whisper": "https://openai.com/research/whisper",
    
    # Web Frameworks & APIs
    "Flask": "https://flask.palletsprojects.com/",
    "FastAPI": "https://fastapi.tiangolo.com/",
    "ElevenLabs": "https://elevenlabs.io/",
    
    # Version Control & Databases
    "Git": "https://git-scm.com/",
    "SQL/PostgreSQL": "https://www.postgresql.org/",
    "Oracle DB": "https://www.oracle.com/database/",
    
    # Frontend & Styling
    "HTML/CSS": "https://developer.mozilla.org/en-US/docs/Web/HTML",
    "Bootstrap/SCSS": "https://getbootstrap.com/",
    "Jinja2": "https://jinja.palletsprojects.com/",
    
    # Development Tools
    "CLI Tools": "https://github.com/topics/cli",
    "Claude Code": "https://docs.anthropic.com/en/docs/claude-code",
    "WindSurf": "https://codeium.com/windsurf"
}

def get_skills_with_links(skills_dict):
    return [
        {
            'name': skill_name, 
            'link': skill_url
        } 
        for skill_name, skill_url in skills_dict.items()
    ]