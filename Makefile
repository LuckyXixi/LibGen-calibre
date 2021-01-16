all:
	@zip -r Libgen-calibre.zip __init__.py \
	constants.py \
	LICENSE.md \
	libgen_plugin.py \
	plugin-import-name-store_libgen.txt \
	pylibgen.py \
	requests.py 
	@echo "generated Libgen-calibre.zip"
