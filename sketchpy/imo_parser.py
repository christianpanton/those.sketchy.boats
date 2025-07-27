"""
Parser for the homebrew '.imo' format. 

The file represents IMO number of vessels that need to be tagged, for a particular purpose.

Each file consists of a header prefixed with '#' followed by one IMO number per line.

Each IMO number can have a comment, that follows immedately after the first whitespace character.

The header is used as description for the tag.

The tag name is derived from the filename.
"""

from re import split
from glob import glob
from pathlib import Path

def validate_imo(imo):
    digits = list(map(int, list(str(imo))))
    chkdigit = digits.pop()
    while len(digits) < 6:
        digits.insert(0, 0)
    weights = [7, 6, 5, 4, 3, 2]
    calcchk = sum(map(lambda x: x[0]*x[1], zip(digits, weights))) % 10
    if chkdigit != calcchk:
        return False
    return True

def load_file(filename: str):    
    header = None
    imos = []
    imoc = {}
    
    path = Path(filename)  
    tagname = "{}:{}".format(path.parent.name, path.stem)
    
    header_complete = False

    with open(filename, "r") as f:
        
        for linenumber, line in enumerate(f):
            line = line.strip()
            linenumber += 1
            
            if line.startswith("#"):
                if header_complete:
                    raise Exception("Received comment after start of content at line {}".format(linenumber))
                
                line = line.lstrip("#").strip()
                if header is None:
                    header = line
                else:
                    header += "\n\n" + line
            else:
                header_complete = True
                line_split = split(r"\s", line, 1)
                
                imo = int(line_split[0])
                
                if validate_imo(imo):
                    imos.append(imo)
                else:
                    print("Ignore IMO, did not validate", imo)
                                
                if len(line_split) > 1:
                    if imo in imoc.keys():
                        imoc[imo] += "\n\n" + line_split[1].strip()
                    else:
                        imoc[imo] = line_split[1].strip()
                    
                
            
    return (tagname, header, imos, imoc)

def load_tree(base):
    for filename in glob(base):
        try:
            yield load_file(filename)
        except Exception as e:
            print("Error parsing .imo file: {}, error was: {}".format(filename, e))
            raise Exception("Parsing aborted due to errors")
            