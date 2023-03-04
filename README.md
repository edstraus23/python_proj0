# Python Script for Creating a DITA Topic Map and Topics (python_proj0)

This Python script creates a DITA topic map and topics based on the contents of the xml input files. The following command line shows the help output:

```
$ python3 create_map.py -h

create_map.py -m <map> -i <inputdir> -o <outputdir>
```
Use a command line similar to the following to run the script:

```
$ python3 create_map.py -m media.ditamap -i ../tables -o ../media_out
Map name is " media.map "
Input directory is " ../tables "
Output directory is " ../media_out "

Creating media.map

Creating topic for movies.dita
Creating topic for tv_shows.dita
```
## Output

The script ouputs three files:
- media.ditamap
- movies.dita
- tv_shows.dita

## DITA OT Tool Kit

To generate a PDF file, you can copy the three files above to into your DITA OT directory and run the following commnd:

```
bin/dita --input=docsrc/samples/media.ditamap --format=pdf -Dnumbers-before-title=yes
```

This will generate a PDF file, but you can use other formats like "HTML". I like to use section numbering; hence, the "-Dnumbers-before-title=yes". But, you can leave this option out. For DITA OT documentation, see [DITA Open Toolkit](https://www.dita-ot.org/dev/).

## Documenting Code with Sphinx

One of the main objectives of this project was to show how to automatically document the Python code by using Sphinx. Open the index.html file in the docs/\_build/html folder to see the defintions for the functions of the create_map.py script. For a quick start guide to  document the Python code by using Sphinx, see [Documenting Python code with Sphinx](https://towardsdatascience.com/documenting-python-code-with-sphinx-554e1d6c4f6d).
