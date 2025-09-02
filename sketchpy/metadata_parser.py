def load_file(filename: str):
    result = {}
    with open(filename, "r") as f:
        for line in f:
            imostr, cc, name, lat, lon = line.strip().split("\t")
            imo = int(imostr)
            result[imo] = [name, cc, lat, lon]
            
    return result