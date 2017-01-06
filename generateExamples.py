#!/usr/bin/python
import json
import os
from simulation import Simulation

singlewater = Simulation(name="singlewater", inputScript="singlewater.in", tags = ["water", "manybody", "vashishta"], folder="examples/water/singlewater", title="Single water molecule", description = "A single water molecule using the vashishta potential.")
watervapor = Simulation(name="watervapor", inputScript="watervapor.in", tags = ["water", "manybody", "vashishta"], folder="examples/water/vapor", title="Water vapor", description = "Low density water gas using the vashishta potential.")
betacristobalite = Simulation(name="betacristobalite", inputScript="betacristobalite.in", tags = ["silica", "crystal", "manybody", "vashishta"], folder="examples/silica/betacristobalite", title="Silica beta cristobalite", description = "Beta cristobalite crystal using the vashishta potential.")
zeolite_zsm5 = Simulation(name="zeolite_zsm5", inputScript="zeolite_zsm5.in", tags = ["silica", "zeolite", "manybody", "vashishta"], folder="examples/silica/zeolite_zsm5", title="Zeolite ZSM-5", description = "Zeolite ZSM-5 using the vashishta potential.")
generate_nanoporous = Simulation(name="generate_nanoporous", inputScript="generate_nanoporous.in", tags = ["silica", "manybody", "vashishta"], folder="examples/silica/generate_nanoporous", title="Nanoporous silica", description = "Generate a nanoporous silica structure from betacristobalite using the vashishta potential.")

examples = [
    singlewater,
    watervapor,
    betacristobalite,
    zeolite_zsm5,
    generate_nanoporous
]

examplesDictList = []
fileList = []

for example in examples:
    print "Working with ", example.name
    print "Folder: ", example.folder
    print "Files: ", example.files
    examplesDictList.append(example.__dict__)
    for file in example.files:
        fileList.append(os.path.join(example.folder, file))

stringified = json.dumps(examplesDictList)
print stringified

with open('examples/examples.json', 'w') as outfile:
    json.dump({"results": examplesDictList}, outfile)

with open('examples.qrc', 'w') as outfile:
    outfile.write("<RCC>\n    <qresource prefix=\"/\">\n")
    for file in fileList:
        outfile.write("        <file>%s</file>\n" % file)
    outfile.write("        <file>examples/examples.json</file>\n")
    outfile.write("    </qresource>\n</RCC>")
