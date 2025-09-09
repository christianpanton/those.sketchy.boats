from collections import defaultdict

from . import imo_parser
from . import metadata_parser

class SketchyBoat(object): 
    def __init__(self):
        self.tags = {}
        self.name = None
        self.flag = None
        self.imo = None
        self.mmsi = None
        self.lat = None
        self.lon = None
        
    def set_name(self, name):
        self.name = name
        
    def set_imo(self, imo):
        self.imo = imo
        
    def set_mmsi(self, mmsi):
        self.mmsi = mmsi
        
    def set_flag(self, flag):
        self.flag = flag
    
    def set_latlon(self, lat, lon):
        self.lat = lat
        self.lon = lon
    
    def set_tag(self, tag, comment=None):
        self.tags[tag] = comment
        
    def __repr__(self):
        return "{} {} {} {}".format(self.imo, self.flag, self.name, ", ".join(self.tags.keys()))
    
    def json(self):
        tags = []
        
        for tag in self.tags.keys():
            
            if self.tags[tag]:
                tags.append({
                    "tag": tag,
                    "comment": self.tags[tag]
                })
            else:
                tags.append({
                    "tag": tag,
                })
                        
        return {
            "imo": self.imo,
            "mmsi": self.mmsi,
            "name": self.name,
            "lat": self.lat,
            "lon": self.lon,
            "flag": self.flag,
            "tags": tags
        }

def build():
    
    build_result = defaultdict(SketchyBoat)
    ship_metadata = metadata_parser.load_file("src/metadata.tsv")
    headers = {}
    boats = []
    
    missing_metadata = set()
    
    for tag, header, imos, imoc in imo_parser.load_tree("src/*/*.imo"):
        headers[tag] = header
               
        for imo in imos:
            build_result[imo].set_imo(imo)
            
            if imo in ship_metadata: 
                build_result[imo].set_name(ship_metadata[imo][0])
                
                if ship_metadata[imo][2] != "NULL":
                    build_result[imo].set_mmsi(ship_metadata[imo][1])
    
                build_result[imo].set_flag(ship_metadata[imo][2])
                
                if ship_metadata[imo][3] != "NULL" and ship_metadata[imo][4] != "NULL":
                     build_result[imo].set_latlon(int(ship_metadata[imo][3]), int(ship_metadata[imo][4]))
                    
            else:
                missing_metadata.add(imo) 

            if imo in imoc:
                build_result[imo].set_tag(tag, imoc[imo])
            else:
                build_result[imo].set_tag(tag)
        
    for imo in sorted(build_result.keys()):
        boats.append(build_result[imo].json())

    for imo in sorted(missing_metadata):
        print(len(build_result[imo].tags), imo, "Missing metadata")
        
    return {
        "boats": boats,
        "tags": headers
    }