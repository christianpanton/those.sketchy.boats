def load_file(filename: str):
    result = {}
    with open(filename, "r") as f:
        for line in f:
            imostr, mmsi, cc, name, lat, lon = line.strip().split("\t")
            imo = int(imostr)
            result[imo] = [name, mmsi, cc, lat, lon]
            
    return result