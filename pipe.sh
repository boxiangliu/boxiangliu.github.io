# Use this command to convert a BibTex file from Google Scholar
# to Markdown files for the publications page.
python scripts/add_url.py --bib files/publications.bib
python scripts/bib2md.py --bib files/publications.bib \
	--out_dir _publications/

# To generate markdown files for publications:
# Don't run  
jupyter notebook: markdown_generator/PubsFromBib.ipynb