# Use this command to convert a BibTex file from Google Scholar
# to Markdown files for the publications page.
cat files/publications.bib | \
python add_url.py | \
python bib2md.py 