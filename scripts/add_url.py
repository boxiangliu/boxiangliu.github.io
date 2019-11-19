#!/usr/bin/env python
# Add URLs for a list of publications given in BibTex format.
import os
import sys
import bibtexparser
import scholarly
import argparse

parser = argparse.ArgumentParser(description='Add URLs for a list of "\
	"publications provided in BibTex format.')
parser.add_argument('--bib', type=str, help='The BibTex file.')
args = parser.parse_args()

bib_bak = args.bib + ".bak"
os.rename(args.bib, bib_bak)

with open(bib_bak, "r") as f:
	bib = bibtexparser.load(f)

try:
	n = 0
	for entry in bib.entries:
		title = entry["title"]
		if "url" not in entry or "abstract" not in entry:
			print("Searching for {}".format(title), flush=True)
			query = list(scholarly.search_pubs_query(title))[0]
			entry["url"] = query.bib["url"]
			entry["abstract"] = query.bib["abstract"]
			n += 1
		else:
			print("{} already has an URL and an abstract.".\
				format(title), flush=True)

	print("Added URLs for {} articles".format(n))

	with open(args.bib, "w") as f:
		bibtexparser.dump(bib, f)

	os.remove(bib_bak)

except:
	os.rename(bib_bak, args.bib)