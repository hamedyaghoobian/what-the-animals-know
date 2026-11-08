"""One drawing per animal from NaarDoon, the open library of Iranian visual elements at
library.eranshahr.com, cut into a small silhouette for the page.

Each NaarDoon element is a contributor's tracing of a museum object. data/naardoon-catalogue.json
lists the animal and mythical-creature elements (title, who traced it, its source, its files);
PICKS below chooses one per species. The image is downloaded, reduced to 192 px high, and kept as
its own shape (the alpha), which the page fills with a single ink. Writes site/data/naardoon/
<species>.png and site/data/naardoon/credits.json.

  .venv/bin/python -I tools/naardoon.py
"""
import io, json, os, re, time, urllib.request
from PIL import Image

# species on the page: the NaarDoon element's title (an exact match, else the first that starts so).
# Left out because their drawing does not read alone as the animal: owl, dove, peacock.
PICKS = {
    "horse": "Brown Horse", "lion": "Lion", "elephant": "Elephant", "dragon": "Red Eyed Dragon",
    "leopard": "Sasanian Leopard", "bird": "Flying Bird", "wolf": "A Wolf Running", "onager": "Persian Zebra",
    "Simorgh": "Sasanian Simurgh,Simorgh", "crow": "Crow", "dog": "Sasanian Dog", "fish": "Sassanian Fish",
    "cattle": "Zebu Cow", "sheep": "Sheep", "falcon": "Falcon", "gazelle": "Two Gazelle Running",
    "eagle": "Eagle Or Hawk", "fox": "Fox", "tiger": "Tiger Dish", "boar": "Sassanian Boar",
    "pheasant": "Sasanian Bird,Pheasant", "fowl": "Rooster", "hoopoe": "Hoopoe",
    "cat": "Wild Cat", "hare": "Rabbit",
    "deer": "Deer Jumping", "duck": "Duck", "partridge": "Two Partridges", "parrot": "Green Parrot",
    "crane": "Crane Facing Left", "heron": "Herons", "goat": "Sassanian Goat", "wild sheep": "Sassanian Wild Sheep",
    "donkey": "Sasanian Donkey Head", "bear": "Brown Bear",
}
HIGH = 192

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "readings-otherwise (a page that credits NaarDoon)"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read()

if __name__ == "__main__":
    cat = json.load(open("data/naardoon-catalogue.json"))
    os.makedirs("site/data/naardoon", exist_ok=True)
    credits = {}
    for species, title in PICKS.items():
        el = next((x for x in cat if x["title"] == title), None) or next((x for x in cat if x["title"].startswith(title)), None)
        if not el:
            print("no element for", species, title); continue
        out = f"site/data/naardoon/{species.replace(' ', '-')}.png"
        if not os.path.exists(out):
            im = Image.open(io.BytesIO(get(el["png"]))).convert("RGBA")
            box = im.getchannel("A").getbbox()                      # the drawing itself, without its margin
            if box: im = im.crop(box)
            im = im.resize((max(1, round(im.width * HIGH / im.height)), HIGH), Image.LANCZOS)
            Image.merge("RGBA", (*Image.new("RGB", im.size, (0, 0, 0)).split(), im.getchannel("A"))).save(out, optimize=True)
            time.sleep(.6)
        museum = re.sub(r"^https?://(www\.)?([^/]+)/.*$", r"\2", el["source"]) if el["source"].startswith("http") else el["source"]
        credits[species] = {"file": os.path.basename(out), "title": el["title"], "by": el["by"], "collection": el["collection"],
                            "source": el["source"], "museum": museum}
        print(f"{species:10s} {el['title'][:34]:34s} {el['by']:22s} {museum}")
    json.dump(credits, open("site/data/naardoon/credits.json", "w"), ensure_ascii=False, indent=1)
    print(len(credits), "drawings,", sum(os.path.getsize(f"site/data/naardoon/{c['file']}") for c in credits.values()) // 1024, "KB")
