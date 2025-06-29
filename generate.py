import json
import os

from sketchpy import builder

build = builder.build()

os.makedirs("dist", exist_ok=True)

with open("dist/boats.json", "w") as gen:
    json.dump(build, gen)
