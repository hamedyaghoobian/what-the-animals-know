You are annotating animals in classical Persian literature for a study in the frame of Steven Wagschal's *Minding Animals in the Old and New Worlds* (2018). Wagschal argues that people conceive of an animal's mind according to how they use it and live with it (the mode of interaction: hunter and hunted, rider and horse, farmer and herd, king and counsellor), rather than according to what the animal can actually do.

You will be given one passage from one of four books, with the section heading and the passages just before and after it for context:
- Kalila wa Dimna, Nasrollah Monshi's Persian prose version (12th century): fables in which animals speak, reason and scheme at a lion's court, framed by a king and a philosopher, with verse quoted into the prose.
- Attar's Manteq al-Tayr, the Conference of the Birds (12th century): a Sufi allegory in verse; birds speak and argue on a journey to the Simorgh, and many short anecdotes about people use animals as images.
- Ferdowsi's Shahnameh (finished 1010): epic verse of kings, heroes, battles and hunts; horses, war elephants, hunted game, monsters, and constant similes of heroes as lions, leopards, crocodiles and dragons.
- Rumi's Masnavi (13th century): a Sufi teaching poem in six books, told through stories that interrupt each other, many of them animal fables (the lion and the hare, the parrot and the merchant, the elephant in the dark, the camel and the mule), with constant images of the soul, the self and the body as animals.

One word in the passage is marked with ⟦ ⟧. It was matched to an animal word by a dictionary, and it may not be an animal at all: شیر is lion or milk, گور onager or grave, باز falcon or "again"/"open", بوم owl or land, کره foal or sphere, باره horse or wall or time, مار snake or a suffix, کرم worm or generosity or Kerman, خر donkey or "great", آهو gazelle or fault, ماهی fish or a month, دام livestock or trap, رخش Rostam's horse Rakhsh or radiance, همای / هما the homa bird or Queen Homay, بهزاد Siavash's horse or a man.

Judge only the marked word, in this passage. Return JSON with these fields:

is_animal: true if the marked word here refers to an animal, a named animal, an animal kind, or an animal used as an image (a hero called a lion is still an animal word used as a figure). false if it is the other word (milk, grave, again, land, wall, a month...).

species: the animal in plain English, singular and lower case (lion, horse, jackal, dove, dragon, Simorgh...). Correct the dictionary's guess if the passage shows otherwise. Empty if is_animal is false.

figure: how the animal is present.
- "creature": an animal in the world of the text, acting or acted upon as an animal (a horse ridden into battle, a gazelle hunted, a lion that attacks, a bird that flies off).
- "character": an animal who acts as a person in the story: speaks, argues, plots, prays, rules (the jackals Kalila and Dimna, the lion king, the hoopoe and the birds of Attar's frame).
- "figure": the animal word is a comparison or metaphor for something else, usually a person: "like a lion", "the lion of the battlefield" said of a hero, "a dragon" for an army or a sword, "the bird of the soul", or a proverbial image in someone's speech that is not an event of the story.
- "none" if is_animal is false.

mode: the human–animal relation the passage puts it in. One of:
- "hunted": quarry of a hunt, game, prey of people.
- "hunter": the animal hunts or kills (a lion attacks, a falcon takes a bird, a dragon devours).
- "ridden": a mount or beast of burden, ridden, harnessed, loaded, led.
- "eaten": food, slaughtered, a feast, milk or meat.
- "sacrificed": offered, killed in ritual.
- "kept": a pet, a herd, a tame or captive animal in someone's care.
- "court": a subject, courtier, minister or king in an animal society (Kalila's court).
- "guide": a teacher, guide, saviour or advisor (the hoopoe leading the birds, the Simorgh raising Zal).
- "wild": met in the wild, no use made of it.
- "emblem": a sign, a banner, a constellation, an image on something, an omen.
- "none": no relation shown, or is_animal is false. Use "none" for most figures of speech.

faculties: every mental capacity the passage attributes to the animal. Any of: "speech", "reasoning", "knowledge", "emotion", "deception", "perception", "desire", "memory", "moral", "devotion". Empty list if none is attributed. Only what the passage gives this animal; for a figure of speech, list what is attributed to the animal image itself, usually none.

spectrum: where the representation of the animal's mind falls.
- "anthropectomy": the animal is treated as having no mind at all: an object, a thing, food, a tool, a number of mounts, a skin, a quantity of game.
- "species-typical": the animal does what that animal does (runs, roars, flies, bites, grazes) and no mind is claimed for it, neither denied nor attributed.
- "constructive": a mind is attributed that fits the animal's real nature and senses, read from cues: a horse senses danger and wakes its rider, a dog is loyal to its master, a mother animal fears for its young, a gazelle is wary.
- "gratuitous": human faculties beyond the animal's nature: speech, argument, scheming, piety, philosophy, legal judgement, letters.
- "none": is_animal is false, or the word is a figure of speech that says nothing about an animal's mind.

evidence: up to six words copied from the passage (in Persian) that decided the spectrum and faculties. Empty if none.

unsure: true if the passage is too ambiguous to decide the main fields with confidence.

Being spoken to is not speech. When a person speaks to an animal (Rostam talks to Rakhsh, Siavash to his horse Shabrang Behzad), the animal is not credited with speech or reasoning unless it answers or acts on the words as a person would; the speaker's trust in it may be perception, emotion or devotion, and the spectrum is "constructive" if the address fits a real bond of rider and horse, "species-typical" otherwise.

Parts and products of animals, and things shaped like them: an animal's skin worn as a garment (Rostam's tiger-skin, ببر بیان, often just ببر), ivory, a hide, meat on the spit, a mace with a bull's head (گرز گاوسر, گاوپیکر), a banner with a lion: figure "creature", mode "eaten" for food and otherwise "emblem", spectrum "anthropectomy", faculties [].

Examples (the marked word is in ⟦ ⟧):

1. Kalila: «⟦دمنه⟧ گفت: ای ملک، این بانگ گاوی است و از وی بیم نباید داشت» → is_animal true, species jackal, figure character, mode court, faculties [speech, reasoning, knowledge], spectrum gratuitous, evidence «دمنه گفت ای ملک».
2. Shahnameh: «چو ⟦رخش⟧ آن چنان دید، شد تیزچنگ / بزد بر سر شیر دندان و چنگ» while Rostam sleeps → is_animal true, species horse, figure creature, mode ridden, faculties [perception], spectrum constructive, evidence «رخش آن چنان دید».
3. Shahnameh: «بپوشید رستم سلیح نبرد / چو ⟦شیر⟧ ژیان اندر آمد به گرد» → is_animal true, species lion, figure figure, mode none, faculties [], spectrum none, evidence «چو شیر ژیان».
4. Shahnameh: «فرستاد صد ⟦اسپ⟧ با زین زر / ز دیبا و دینار و تیغ و کمر» → is_animal true, species horse, figure creature, mode ridden, faculties [], spectrum anthropectomy, evidence «صد اسپ با زین زر».
5. Shahnameh: «که بی‌شیر و ⟦گور⟧ و پلنگ است دشت» about hunting grounds → is_animal true, species onager, figure creature, mode hunted, faculties [], spectrum species-typical.
6. Shahnameh: «سپردند او را به تنگی ⟦گور⟧» (the grave) → is_animal false, species "", figure none, mode none, faculties [], spectrum none.
7. Attar: «⟦هدهد⟧ آشفته‌دل پر انتظار / در میان جمع آمد بی‌قرار» → is_animal true, species hoopoe, figure character, mode guide, faculties [emotion], spectrum gratuitous (a bird leading a spiritual assembly).
8. Attar: «همچو ⟦مرغ⟧ نیم بسمل می‌طپد» said of a lover → is_animal true, species bird, figure figure, mode none, faculties [], spectrum none.
9. Kalila: «و ⟦گاو⟧ در آن مرغزار می‌چرید و فربه می‌گشت» → is_animal true, species cattle, figure creature, mode wild, faculties [], spectrum species-typical.
10. Kalila: «و ⟦کبوتر⟧ بچگان را از بیم صیاد در آشیانه نگاه داشت» → is_animal true, species dove, figure creature, mode wild, faculties [emotion], spectrum constructive.

Be consistent: the same kind of use gets the same labels throughout the book.
