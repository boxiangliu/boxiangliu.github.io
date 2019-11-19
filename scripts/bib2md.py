from pybtex.database.input import bibtex
import pybtex.database.input.bibtex 
from time import strptime
import string
import html
import os
import re
import argparse

parser = argparse.ArgumentParser(description='Generate Markdown files "\
	"given a BibTex file.')
parser.add_argument('--bib', type=str, help='The BibTex file.')
parser.add_argument('--out_dir', type=str, help='The BibTex file.')
args = parser.parse_args()

file = args.bib
out_dir = args.out_dir

html_escape_table = {
	"&": "&amp;",
	'"': "&quot;",
	"'": "&apos;"
	}

def html_escape(text):
	"""Produce entities within text."""
	return "".join(html_escape_table.get(c,c) for c in text)


def get_date(fields):
	#reset default date
	pub_year = "1900"
	pub_month = "01"
	pub_day = "01"
	
	pub_year = f'{fields["year"]}'

	#todo: this hack for month and day needs some cleanup
	if "month" in fields.keys(): 
		if(len(fields["month"])<3):
			pub_month = "0"+fields["month"]
			pub_month = pub_month[-2:]
		elif(fields["month"] not in range(12)):
			tmnth = strptime(fields["month"][:3],'%b').tm_mon   
			pub_month = "{:02d}".format(tmnth) 
		else:
			pub_month = str(fields["month"])
	if "day" in fields.keys(): 
		pub_day = str(fields["day"])

		
	pub_date = pub_year+"-"+pub_month+"-"+pub_day

	return pub_date, pub_year

def get_citation(fields, persons, _type, pub_year):

	#Build Citation from text
	citation = ""

	#citation authors - todo - add highlighting for primary author?
	for author in persons["author"]:
		if author.last_names[0] == "others":
			citation = citation[:-2] + " et al."
		else:
			citation += " "+author.first_names[0]+" "+\
				author.last_names[0]+", "

	#citation title
	citation += "\"" + html_escape(fields["title"].replace("{", "").\
		replace("}","").replace("\\","")) + ".\""

	#add venue logic depending on citation type

	if _type == "article":
		venue = fields["journal"]
	elif _type == "inproceedings" or _type == "incollection":
		venue = fields["booktitle"]

	citation += " " + html_escape(venue.replace("{", "").\
		replace("}","").replace("\\",""))
	citation += ", " + pub_year + "."

	return citation, venue


def get_markdown(fields, html_filename, md_filename, pub_date, venue, citation):

	## YAML variables
	md = "---\ntitle: \"" + html_escape(fields["title"].\
		replace("{", "").replace("}","").replace("\\","")) +"\""
	
	md += "\ncollection: publications"

	md += "\npermalink: /publications/" + html_filename

	md += "\ndate: " + str(pub_date) 

	md += "\nvenue: '" + html_escape(venue) + "'"
	
	if "url" in fields.keys():
		if len(str(fields["url"])) > 5:
			md += "\npaperurl: '" + fields["url"] + "'"

	md += "\ncitation: '" + html_escape(citation) + "'"
	md += "\nexcerpt_separator: <!--more-->"
	md += "\n---"
	md += "\n<!--more-->"
	
	## Markdown description for individual page
	if "abstract" in fields.keys():
		md += "\n" + html_escape(fields["abstract"]) + "\n"

	if "url" in fields.keys():
		md += "\n[Access paper here](" + fields["url"] + "){:target=\"_blank\"}\n" 
	else:
		md += "\nUse [Google Scholar](https://scholar.google.com/scholar?q="+html.escape(clean_title.replace("-","+"))+"){:target=\"_blank\"} for full citation"

	md_filename = os.path.basename(md_filename)

	return md

parser = bibtex.Parser()
bibdata = parser.parse_file(file)

#loop through the individual references in a given bibtex file
for bib_id in bibdata.entries.keys():
	
	fields = bibdata.entries[bib_id].fields
	persons = bibdata.entries[bib_id].persons
	_type = bibdata.entries[bib_id].type

	try:
		pub_date, pub_year = get_date(fields)
		
		#strip out {} as needed (some bibtex entries that maintain formatting)
		clean_title = fields["title"].replace("{", "").\
			replace("}","").replace("\\","").replace(" ","-")    

		url_slug = re.sub("\\[.*\\]|[^a-zA-Z0-9_-]", "", clean_title)
		url_slug = url_slug.replace("--","-")

		md_filename = (str(pub_date) + "-" + url_slug + ".md").\
			replace("--","-")
		html_filename = (str(pub_date) + "-" + url_slug).\
			replace("--","-")

		#Build Citation from text
		citation, venue = get_citation(fields, persons, _type, pub_year)
		
		# Get MarkDown:
		md = get_markdown(fields, html_filename, md_filename, \
			pub_date, venue, citation)

		with open(os.path.join(out_dir,md_filename), 'w') as f:
			f.write(md)
		print(f'SUCESSFULLY PARSED {bib_id}: \"', fields["title"][:60],"..."*(len(fields['title'])>60),"\"")
	
	# field may not exist for a reference
	except KeyError as e:
		print(f'WARNING Missing Expected Field {e} from entry {bib_id}: \"', fields["title"][:30],"..."*(len(fields['title'])>30),"\"")
		continue