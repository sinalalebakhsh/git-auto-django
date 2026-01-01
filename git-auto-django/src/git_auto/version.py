DEFAULT_VERSION = "1.1.3"

def load_version(path=".git_auto_version"):
    try:
        with open(path) as f:
            return f.read().strip()
    except:
        return DEFAULT_VERSION

def save_version(version, path=".git_auto_version"):
    with open(path, "w") as f:
        f.write(version)



