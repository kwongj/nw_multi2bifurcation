# nw_multi2bifurcation
Resolves multifurcation / polytomy in Newick trees eg. from FastTree  
Note that this is not a true solution, but allows the tree to be imported into software that requires a strictly bifurcating tree eg. ClonalFrameML.

##Author

Jason Kwong (@kwongjc)

##Dependencies
* Python
* ete2

##Usage

```
$ nw_multi2bifurcation.py -h
usage: nw_multi2bifurcation.py [-h] [--nosupport] nwtree

Resolves multifurcation / polytomy in Newick trees eg. from FastTree
Note that this is not a true solution, but allows the tree to be imported into software that requires a strictly bifurcating tree eg. ClonalFrameML

positional arguments:
  nwtree       Newick tree file

optional arguments:
  -h, --help   show this help message and exit
  --nosupport  Remove internal node support values from tree eg. for
               ClonalFrameML
```

Prints new tree to ```stdout```.

##Bugs

Please submit via the [GitHub issues page](https://github.com/kwongj/nw_multi2bifurcation/issues).  

##Software Licence

[GPLv3](https://github.com/kwongj/nw_multi2bifurcation/blob/master/LICENCE)

##References

[ETE Toolkit](http://etetoolkit.org/docs/latest/reference/reference_tree.html)
