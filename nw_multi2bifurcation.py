#!/usr/bin/env python
# Script by JK
# Fixes FastTree multifurcation

# Usage
import argparse
parser = argparse.ArgumentParser(
        prog='nw_multi2bifurcation.py',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='Resolves multifurcation / polytomy in Newick trees eg. from FastTree\nNote that this is not a true solution, but allows the tree to be imported into software that requires a strictly bifurcating tree eg. ClonalFrameML')
parser.add_argument('nwtree', metavar='nwtree', nargs=1, help='Newick tree file')
parser.add_argument('--nosupport', action='store_true', help='Remove internal node support values from tree eg. for ClonalFrameML')
args = parser.parse_args()

# Load tree from file
from ete2 import Tree
t = Tree(args.nwtree[0])
t.resolve_polytomy(recursive=True)
tn = str(t.write())

# Remove support values from tree
if args.nosupport:
	import re
	tn = re.sub(r'\)[0-9\.]+:', r'):', tn)

print(tn)
