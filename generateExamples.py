#!/usr/bin/python
import json
import os
from os import listdir
from os.path import isfile, join

def findFiles(simulation):
    ignoreList = [".DS_Store", "log.lammps"]
    simulation["files"] = []
    simulation["thumbnails"] = []
    for f in listdir(simulation["folder"]):
        if isfile(join(simulation["folder"], f)):
            if f in ignoreList: continue
            if f.lower().endswith(('.png', '.jpg', '.jpeg')):
                simulation["thumbnails"].append(f)
            simulation["files"].append(f)

singlewater={"objectId": "singlewater", "inputScript": "singlewater.in", "tags": ["water", "manybody", "vashishta"], "folder": "examples/water/singlewater", "name": "Single water molecule", "description": "A single water molecule using the vashishta potential."}
watervapor={"objectId": "watervapor", "inputScript": "watervapor.in", "tags": ["water", "manybody", "vashishta"], "folder": "examples/water/vapor", "name": "Water vapor", "description": "Low density water gas using the vashishta potential."}
betacristobalite={"objectId": "betacristobalite", "inputScript": "betacristobalite.in", "tags": ["silica", "crystal", "manybody", "vashishta"], "folder": "examples/silica/betacristobalite", "name": "Silica beta cristobalite", "description": "Beta cristobalite crystal using the vashishta potential."}
zeolite_zsm5={"objectId": "zeolite_zsm5", "inputScript": "zeolite_zsm5.in", "tags": ["silica", "zeolite", "manybody", "vashishta"], "folder": "examples/silica/zeolite_zsm5", "name": "Zeolite ZSM-5", "description": "Zeolite ZSM-5 using the vashishta potential."}
generate_nanoporous={"objectId": "generate_nanoporous", "inputScript": "generate_nanoporous.in", "tags": ["silica", "manybody", "vashishta"], "folder": "examples/silica/generate_nanoporous", "name": "Nanoporous silica", "description": "Generate a nanoporous silica structure from betacristobalite using the vashishta potential."}
crack={"objectId": "crack", "inputScript": "crack.in", "tags": ["lammps", "lj", "crack", "2d"], "folder": "examples/lammps/crack", "name": "Crack 2D", "description": "Crack propagation in a 2d solid."}
flow_couette={"objectId": "flow_couette", "inputScript": "flow_couette.in", "tags": ["lammps", "lj", "flow", "2d"], "folder": "examples/lammps/flow_couette", "name": "Couette flow 2D", "description": "Couette flow in a 2d channel."}
flow_poiseuille={"objectId": "flow_poiseuille", "inputScript": "flow_pois.in", "tags": ["lammps", "lj", "flow", "2d"], "folder": "examples/lammps/flow_pois", "name": "Poiseuille flow 2D", "description": "Poiseuille flow in a 2d channel."}
friction={"objectId": "friction", "inputScript": "friction.in", "tags": ["lammps", "lj", "friction", "2d"], "folder": "examples/lammps/friction", "name": "Friction 2D", "description": "Frictional contact of spherical asperities between 2d surfaces."}
cmap={"objectId": "cmap", "inputScript": "in.cmap", "tags": ["lammps", "charmm", "molecule"], "folder": "examples/lammps/cmap", "name": "CMAP 5-body", "description": "CMAP 5-body contributions to CHARMM force field."}
deposit_atom={"objectId": "deposit_atom", "inputScript": "in.deposit.atom", "tags": ["lammps", "lj", "deposit"], "folder": "examples/lammps/deposit_atom", "name": "Deposit atoms", "description": "Deposition of atoms onto a 3d substrate."}
deposit_molecule={"objectId": "deposit_molecule", "inputScript": "in.deposit.molecule", "tags": ["lammps", "lj", "deposit", "molecule"], "folder": "examples/lammps/deposit_molecule", "name": "Deposit molecules", "description": "Deposition of molecules onto a 3d substrate."}
micelle={"objectId": "micelle", "inputScript": "in.micelle", "tags": ["lammps", "soft"], "folder": "examples/lammps/micelle", "name": "Micelle", "description": "Self-assembly of small lipid-like molecules into 2d bilayers."}
obstacle={"objectId": "obstacle", "inputScript": "in.obstacle", "tags": ["lammps", "lj", "2d"], "folder": "examples/lammps/obstacle", "name": "2d obstacle", "description": "Flow around two voids in a 2d channel."}
peptide={"objectId": "peptide", "inputScript": "in.peptide", "tags": ["lammps", "molecule", "water", "solvation"], "folder": "examples/lammps/peptide", "name": "Peptide solvation", "description": "Dynamics of a small solvated peptide chain (5-mer)."}
pour_2d={"objectId": "pour_2d", "inputScript": "in.pour.2d", "tags": ["lammps", "granular", "2d"], "folder": "examples/lammps/pour_2d", "name": "2d pour.", "description": "Dynamics of a small solvated peptide chain (5-mer)."}
pour_2d_molecule={"objectId": "pour_2d_molecule", "inputScript": "in.pour.2d.molecule", "tags": ["lammps", "granular", "2d", "molecule"], "folder": "examples/lammps/pour_2d_molecule", "name": "2d molecule pour", "description": "Pouring of granular molecules into a 2d box, then chute flow."}
pour_3d={"objectId": "pour_3d", "inputScript": "in.pour", "tags": ["lammps", "granular"], "folder": "examples/lammps/pour_3d", "name": "3d pour", "description": "Pouring of granular particles into a 3d box, then chute flow."}
shear={"objectId": "shear", "inputScript": "in.shear", "tags": ["lammps", "shear"], "folder": "examples/lammps/shear", "name": "Shear", "description": "sideways shear applied to 2d solid."}
shear_void={"objectId": "shear_void", "inputScript": "in.shear.void", "tags": ["lammps", "shear"], "folder": "examples/lammps/shear_void", "name": "Shear with void", "description": "Sideways shear applied to 2d solid with a void."}
# moltemplate
abstract_translocation={"objectId": "abstract_translocation", "inputScript": "run.in.npt", "tags": ["moltemplate", "molecule", "solvation", "polymer"], "folder": "examples/lammps/abstract_translocation", "name": "Polymer through hole", "description": "This example contains a (crude and somewhat simple) example of the translocation of a (rather short) polymer through a hole in a wall, surrounded by an explicit LJ solvent."}


examples = [
    singlewater,
    watervapor,
    betacristobalite,
    zeolite_zsm5,
    generate_nanoporous,
    crack,
    flow_couette,
    flow_poiseuille,
    friction,
    cmap,
    deposit_atom,
    deposit_molecule,
    micelle,
    obstacle,
    peptide,
    pour_2d,
    pour_2d_molecule,
    pour_3d,
    shear,
    shear_void
]

examplesDictList = []
fileList = []

for example in examples:
    findFiles(example)
    examplesDictList.append(example)
    for file in example["files"]:
        fileList.append(os.path.join(example["folder"], file))

stringified=json.dumps(examplesDictList)
print stringified

with open('examples/examples.json', 'w') as outfile:
    json.dump({"results": examplesDictList}, outfile)

with open('examples.qrc', 'w') as outfile:
    outfile.write("<RCC>\n    <qresource prefix=\"/\">\n")
    for file in fileList:
        outfile.write("        <file>%s</file>\n" % file)
    outfile.write("        <file>examples/examples.json</file>\n")
    outfile.write("    </qresource>\n</RCC>")
