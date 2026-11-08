"""Find every animal word in the three books.

Each token of each unit is looked up in data/animals.tsv as written, then with Persian endings
and an attached preposition taken off (tools/tag.py), and two-word names (ابن آوی, سنگ پشت) are
joined first. Writes data/mentions.jsonl: one line per mention, with its unit, the half-line it
is in, its word index there, the form matched and the species.

  python3 -I tools/mentions.py data/units.jsonl data/mentions.jsonl
"""
import json, sys, os
from collections import Counter
sys.path.insert(0, os.path.dirname(__file__))
from tag import norm, candidates

PAIRS = {("ابن", "آوی"): "شغال", ("ابن", "عرس"): "راسو", ("سنگ", "پشت"): "سنگ‌پشت", ("شب", "پره"): "شب‌پره",
         ("گاو", "میش"): "گاومیش", ("موش", "خرما"): "راسو"}

def lexicon(path):
    lex = {}
    for row in open(path):
        if row.startswith("#") or not row.strip(): continue
        form, species, cls, homo, *note = row.rstrip("\n").split("\t")
        lex[norm(form)] = {"form": form, "species": species, "class": cls, "homograph": homo == "1"}
    return lex

def find(words, lex):
    """(word index, how many words, lexicon entry) for the animals in a half-line or sentence"""
    out, i = [], 0
    while i < len(words):
        w = words[i].strip("،؛:.!؟?«»\"'()")
        nxt = words[i + 1].strip("،؛:.!؟?«»\"'()") if i + 1 < len(words) else ""
        pair = PAIRS.get((norm(w), norm(nxt)))
        if pair:
            out.append((i, 2, lex[norm(pair)])); i += 2; continue
        hit = None
        for form, rule in candidates(norm(w)):
            for f in (form, form.replace("‌", "")):
                if f in lex: hit = lex[f]; break
            if hit: break
        if hit: out.append((i, 1, hit))
        i += 1
    return out

if __name__ == "__main__":
    lex = lexicon("data/animals.tsv")
    n, by = 0, Counter()
    with open(sys.argv[2], "w") as f:
        for line in open(sys.argv[1]):
            u = json.loads(line)
            for half, text in ((0, u["text"]), (1, u.get("text2", ""))):
                if not text: continue
                words = text.split(" ")
                for wi, span, e in find(words, lex):
                    f.write(json.dumps({"id": n, "unit": u["id"], "book": u["book"], "half": half, "w": wi, "span": span,
                                        "token": " ".join(words[wi:wi + span]), "form": e["form"], "species": e["species"],
                                        "class": e["class"], "homograph": e["homograph"]}, ensure_ascii=False) + "\n")
                    n += 1; by[(u["book"], e["form"])] += 1
    print(n, "mentions")
    for book in ("kalila", "attar", "shahnameh"):
        items = sorted(((c, form) for (b, form), c in by.items() if b == book), reverse=True)
        print(book, sum(c for c, _ in items), " ".join(f"{form}:{c}" for c, form in items[:45]))
