<img src="[https://github.com/sinalalebakhsh/acron/blob/main/backend/products/gallery/2026/11/acron__Gemini_Generated_Image_.jpg](https://github.com/sinalalebakhsh/git-auto-django/blob/main/src/Gemini_Generated_Image_3x3vo93x3vo93x3v.jpg)" alt="git-auto-django" width="400"/>

# git-auto-django 🚀

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Git](https://img.shields.io/badge/Git-Automation-orange)
![License](https://img.shields.io/badge/License-MIT-green)

push-py is a simple and practical Python tool designed to automate Git push workflows.  
This project aims to simplify repetitive Git-related tasks for developers.  
push-py helps users stage changes, commit updates, and push code with minimal effort.  
The tool is written entirely in Python and focuses on clarity and usability.  
It is suitable for both beginners and experienced developers who work with Git daily.  
Automatic Git commit & push tool for Django projects.
auto push to github tool for django projects.


---

## 🎯 Features

- Automates `git add`, `git commit`, and `git push`
- Reduces repetitive Git commands
- Simple and readable Python code
- Customizable commit messages
- Beginner-friendly structure
- Easy to extend for advanced workflows

* **Auto commit & push**
* **Semantic versioning**
* **Internet connection detection**
* **Log rotation**
* **Safe git verification**
* **maybe need to run before**

---

## 📦 Requirements

Before using push-py, make sure you have:

- Python **3.x**
- Git installed and configured
- An initialized Git repository
- Valid GitHub authentication (SSH or HTTPS)

Check versions:

```bash
python --version
git --version

⚙️ Installation

Clone the repository:

git clone https://github.com/sinalalebakhsh/push-py.git

Navigate to the project directory:

cd push-py

No external dependencies are required.
▶️ Usage

Basic usage example:

python push.py

Example Python logic used inside the script:

import os

commit_message = "Update project files"
os.system("git add .")
os.system(f'git commit -m "{commit_message}"')
os.system("git push")

You can modify the commit message or add more Git commands as needed.
This allows full control over your Git workflow.
📁 Project Structure

push-py/
│
├── push.py          # Main automation script
├── README.md        # Project documentation
└── LICENSE          # License information

🧠 Learning Purpose

push-py is also designed as an educational project.
It demonstrates how Python can interact with system commands.
Users can learn how to automate developer workflows using Python.
The code is intentionally kept simple and readable.
🤝 Contributing

Contributions are welcome!
You can:

    Report bugs via Issues

    Suggest improvements

    Submit Pull Requests

Please keep the code clean and well-documented.
📜 License

This project is licensed under the MIT License.
You are free to use, modify, and distribute this project.
⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub.
Thank you for using push-py and supporting open-source development!


#### Structure

```
git-auto-django/
├── git_auto/
│   ├── __init__.py
│   ├── main.py         
│   └── version.py       ← مدیریت نسخه
├── pyproject.toml
├── README.md
├── LICENSE
└── .gitignore
```
---

