# 
# basic run through the PDB with lines, sticks, and ribbons
#
      
from glob import glob

import threading
import time
from pymol import cmd
import sys, os, os.path
import traceback

ent_dir = "pdb"


def load():
   cmd.set("valence")
   r = 0
   list = glob("pdb/*/*")
#   while list[0]!="pdb/f8/pdb1f8u":
#      list.pop(0)
   for file in list:
      try:
         cmd.delete('pdb')
         cmd.load(file,'pdb')
         cmd.set_title('pdb',1,os.path.split(file)[-1])
         cmd.rewind()
         cmd.orient('pdb')
         cmd.refresh()
         cmd.show_as("ribbon")
         cmd.refresh()
         cmd.show_as("sticks")
         cmd.refresh()
         sys.__stderr__.write(".")
         sys.__stderr__.flush()
         n = cmd.count_states()
         if n>1:
            cmd.rewind()
            sys.__stderr__.write(file+"\n")
            sys.__stderr__.flush()
            for a in range(1,n+1):
               cmd.forward()
               cmd.refresh()
      except:
         traceback.print_exc()
cmd.feedback('disable','symmetry objectmolecule executive','everything')
load()


