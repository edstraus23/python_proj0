#!/usr/bin/python

# 6/21/2022 - Added flag to only show first occurence of title in topic

import sys, getopt, os, csv, re
from lxml import etree
from io import StringIO, BytesIO
import xml.etree.ElementTree as ET
import codecs
import map_mods
#farr=[]

def main(argv):
   """This main method calls all of the subroutines from the maps_mod module. 

        :param str argv: -h | -m <map> -i <inputdir> -o <outputdir>; Use -h option to see available arguments.

    """
   map_name = ''
   inputdir = ''
   outputdir = ''
   

   try:
      opts, args = getopt.getopt(argv,"hm:i:o:",["mfile=","ifile=","ofile="])
   except getopt.GetoptError:
      print('create_map.py -m <map> -i <inputdir> -o <outputdir>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('create_map.py -m <map> -i <inputdir> -o <outputdir>')
         sys.exit()
      elif opt in ("-m", "--map"):
         map_name = arg
      elif opt in ("-i", "--idir"):
         inputdir = arg
      elif opt in ("-o", "--odir"):
         outputdir = arg
   print('Map name is "', map_name, '"')
   print('Input directory is "', inputdir, '"')
   print('Output directory is "', outputdir, '"')
   #replace_files(inputdir,outputdir)
   farr=map_mods.create_array(inputdir)
   farr.sort()
   map_mods.create_mapfile(map_name,inputdir,outputdir,farr)
   map_mods.create_topics(map_name,inputdir,outputdir,farr)

if __name__ == "__main__":
   main(sys.argv[1:])

