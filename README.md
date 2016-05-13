# nw_multi2bifurcation
Resolves multifurcation / polytomy in Newick trees eg. from FastTree
Note that this is not a true solution, but allows the tree to imported into software that requires a strictly bifurcating tree eg. ClonalFrameML

##Author

Jason Kwong (@kwongjc)

##Usage

```
$ nw_multi2bifurcation.py -h
usage: nw_multi2bifurcation.py [-h] [--nosupport] [--out outfile] nwtree

Resolves multifurcation / polytomy in Newick trees eg. from FastTree
Note that this is not a true solution, but allows the tree to imported into software that requires a strictly bifurcating tree eg. ClonalFrameML

positional arguments:
  nwtree         Newick tree file

optional arguments:
  -h, --help     show this help message and exit
  --nosupport    Remove internal node support values from tree eg. for
                 ClonalFrameML
  --out outfile  Output file name
```

##Bugs

Please submit via the [GitHub issues page](https://github.com/kwongj/nw_multi2bifurcation/issues).  

##Software Licence

[GPLv3](https://github.com/kwongj/nw_multi2bifurcation/blob/master/LICENCE)
