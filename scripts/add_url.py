#!/usr/bin/env python
# Find the URL of a list of publications given in BibTex format.

import sys
import bibtexparser
import scholarly

stdin = sys.stdin.read()
bib = bibtexparser.loads(stdin)

for entry in bib.entries[:2]:
	title = entry["title"]
	print("Searching URL for {}".format(title), flush=True)
	query = list(scholarly.search_pubs_query(title))[0]
	entry["url"] = query.bib["url"]

bib_str = bibtexparser.dumps(bib)
sys.stdout.write(bib_str)