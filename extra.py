d = {"name": "neeaj", "class": "bca", "per": 45}


def name(d):
    if d["name"] != "neeraj":
        return "not match"
    if d["class"] == "bca":
        return "bca"
    if d["per"] == 50:
        return "Not match"


a = name(d)
print(a)
