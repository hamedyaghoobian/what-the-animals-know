# What the Animals Know

Readings, Otherwise, No. 4. *Kalila wa Dimna* (Nasrollah Monshi), Attar's *Conference of the Birds*
and Ferdowsi's *Shahnameh* with every word taken out but the animals, each lit by how much mind the
text gives it, in the terms of Steven Wagschal, *Minding Animals in the Old and New Worlds: A
Cognitive Historical Analysis* (Toronto, 2018). With an atlas that counts it all.

## The pipeline

- `tools/fetch.py`: downloads a book from the Ganjoor API (`python3 -I tools/fetch.py /monshi/kelile-demni data/kalila-ganjoor.json`). The Conference of the Birds and the Shahnameh are read from the dumps of Nos. 2 and 3 (`../attar-conference-of-birds`, `../ferdowsi-shahnameh`).
- `tools/corpus.py`: one list of units, `data/units.jsonl`: couplets for verse, sentences for prose.
- `data/animals.tsv`: the animal words looked for, 181 forms, made by hand, with homographs marked.
- `tools/mentions.py`: every animal word in the units, through Persian endings and attached prepositions (`tools/tag.py`), into `data/mentions.jsonl` (10,457).
- `data/scheme.md`: the instructions every judgement was made under: Wagschal's spectrum (anthropectomy, species-typical, constructive, gratuitous), creature / character / figure of speech, the mode of interaction, the faculties.
- `tools/annotate.py`: sends each mention with its passage and neighbours to the Claude API (Message Batches, structured JSON output, the scheme cached) and writes `data/annotations.jsonl`. All 10,457 were judged by Claude Sonnet 5.5 at medium effort; the 92 judgements outside Kalila that credited speech were made again after a rule was added (an animal spoken to does not speak).
- `data/corrections.json`: judgements changed by hand, with the reason. `data/species-merge.json`: one name per species.
- `data/hand-check.tsv`: 60 judgements drawn at random and read against their passages: 54 agree, 2 wrong (corrected), 4 arguable.
- `tools/shape.py`: sets every line in Amiri with HarfBuzz (Kalila's prose broken into lines), places each animal, and writes `site/data/`.
- `tools/atlas.py`: writes `site/atlas/data.json` for the atlas.
- `tools/naardoon.py`: one drawing per species from [NaarDoon](https://library.eranshahr.com), Eranshahr's open library of Iranian visual elements (`data/naardoon-catalogue.json` lists its 224 animal and mythical-creature elements), cut into a silhouette in `site/data/naardoon/` with `credits.json`: 35 species, each credited to the hand that traced it and the museum that keeps the object.
- `site/`: the piece (`index.html`) and the atlas (`atlas/`), dressed in the site's faceplate. They link the site's `/assets/main.css`, `/assets/js/faceplate.js` and `../piece.js`, so they are meant to be served from the website (`readings-otherwise/what-the-animals-know/`).

```
uv venv .venv && uv pip install --python .venv/bin/python anthropic uharfbuzz fonttools brotli
python3 -I tools/corpus.py data/units.jsonl
python3 -I tools/mentions.py data/units.jsonl data/mentions.jsonl
.venv/bin/python tools/annotate.py dry 50 claude-sonnet-5-5     # read a sample first
.venv/bin/python tools/annotate.py submit claude-sonnet-5-5     # then a batch; ANTHROPIC_API_KEY in .env
.venv/bin/python tools/annotate.py collect <batch id>
.venv/bin/python -I tools/shape.py
python3 -I tools/atlas.py
```

## What it found

| | animals | figures of speech | human mind | read from the animal | what its kind does | no mind |
|---|---|---|---|---|---|---|
| Kalila wa Dimna | 1,228 | 16% | 78% | 2% | 12% | 6% |
| Conference of the Birds | 455 | 51% | 47% | 5% | 23% | 18% |
| Shahnameh | 5,571 | 36% | 1% | 3% | 35% | 61% |

(The spectrum shares are of the animals that are not figures of speech.) Of 1,438 horses, 67% are
given no mind and 3% a mind read from the horse; of the 41 horses given any mind, 19 are named
(Rakhsh, Shabrang Behzad, Shabdiz). The lion is a figure of speech in 730 of its 1,092 appearances.

## Licences

The three texts are in the public domain; the text and headings are Ganjoor's. The judgements
in `data/annotations.jsonl` were produced with the Claude API. Amiri is by Khaled Hosny, under the
SIL Open Font License 1.1 (`fonts/OFL.txt`); `site/data/hand.woff2` is a subset of it. The drawings
in `site/data/naardoon/` are from NaarDoon, which offers them to download and build with freely; each
is the work of the contributor named in `credits.json`, traced from an object whose own rights rest with
its museum. Wagschal's book is cited, not included.
