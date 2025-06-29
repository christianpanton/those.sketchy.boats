import json

from sketchpy import builder

build = builder.build()

with open("dist/boats.json", "w") as gen:
    json.dump(build, gen)