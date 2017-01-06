#!/usr/bin/python
import json
import os
from simulation import Simulation

singlewater = Simulation(name="singlewater", inputScript="singlewater.in", tags = ["water", "manybody", "vashishta"], folder="examples/water/singlewater", title="Single water molecule", description = "A single water molecule using the vashishta potential.")
watervapor = Simulation(name="watervapor", inputScript="watervapor.in", tags = ["water", "manybody", "vashishta"], folder="examples/water/vapor", title="Water vapor", description = "Low density water gas using the vashishta potential.")
betacristobalite = Simulation(name="betacristobalite", inputScript="betacristobalite.in", tags = ["silica", "crystal", "manybody", "vashishta"], folder="examples/silica/betacristobalite", title="Silica beta cristobalite", description = "Beta cristobalite crystal using the vashishta potential.")
zeolite_zsm5 = Simulation(name="zeolite_zsm5", inputScript="zeolite_zsm5.in", tags = ["silica", "zeolite", "manybody", "vashishta"], folder="examples/silica/zeolite_zsm5", title="Zeolite ZSM-5", description = "Zeolite ZSM-5 using the vashishta potential.")
generate_nanoporous = Simulation(name="generate_nanoporous", inputScript="generate_nanoporous.in", tags = ["silica", "manybody", "vashishta"], folder="examples/silica/generate_nanoporous", title="Nanoporous silica", description = "Generate a nanoporous silica structure from betacristobalite using the vashishta potential.")
crack = Simulation(name="crack", inputScript="crack.in", tags = ["lammps", "lj", "crack", "2d"], folder="examples/lammps/crack", title="Crack 2D", description = "Crack propagation in a 2d solid.")
flow_couette = Simulation(name="flow_couette", inputScript="flow_couette.in", tags = ["lammps", "lj", "flow", "2d"], folder="examples/lammps/flow_couette", title="Couette flow 2D", description = "Couette flow in a 2d channel.")
flow_poiseuille = Simulation(name="flow_poiseuille", inputScript="flow_pois.in", tags = ["lammps", "lj", "flow", "2d"], folder="examples/lammps/flow_pois", title="Poiseuille flow 2D", description = "Poiseuille flow in a 2d channel.")
friction = Simulation(name="friction", inputScript="friction.in", tags = ["lammps", "lj", "friction", "2d"], folder="examples/lammps/friction", title="Friction 2D", description = "Frictional contact of spherical asperities between 2d surfaces.")
cmap = Simulation(name="cmap", inputScript="in.cmap", tags = ["lammps", "charmm", "molecule"], folder="examples/lammps/cmap", title="CMAP 5-body", description = "CMAP 5-body contributions to CHARMM force field.")
deposit_atom = Simulation(name="deposit_atom", inputScript="in.deposit.atom", tags = ["lammps", "lj", "deposit"], folder="examples/lammps/deposit_atom", title="Deposit atoms", description = "Deposition of atoms onto a 3d substrate.")
deposit_molecule = Simulation(name="deposit_molecule", inputScript="in.deposit.molecule", tags = ["lammps", "lj", "deposit", "molecule"], folder="examples/lammps/deposit_molecule", title="Deposit molecules", description = "Deposition of molecules onto a 3d substrate.")
micelle = Simulation(name="micelle", inputScript="in.micelle", tags = ["lammps", "soft"], folder="examples/lammps/micelle", title="Micelle", description = "Self-assembly of small lipid-like molecules into 2d bilayers.")
obstacle = Simulation(name="obstacle", inputScript="in.obstacle", tags = ["lammps", "lj", "2d"], folder="examples/lammps/obstacle", title="2d obstacle", description = "Flow around two voids in a 2d channel.")
peptide = Simulation(name="peptide", inputScript="in.peptide", tags = ["lammps", "molecule", "water"], folder="examples/lammps/peptide", title="Peptide solvation", description = "Dynamics of a small solvated peptide chain (5-mer).")
pour_2d = Simulation(name="pour_2d", inputScript="in.pour.2d", tags = ["lammps", "granular", "2d"], folder="examples/lammps/pour_2d", title="2d pour.", description = "Dynamics of a small solvated peptide chain (5-mer).")
pour_2d_molecule = Simulation(name="pour_2d_molecule", inputScript="in.pour.2d.molecule", tags = ["lammps", "granular", "2d", "molecule"], folder="examples/lammps/pour_2d_molecule", title = "2d molecule pour", description="Pouring of granular molecules into a 2d box, then chute flow.")
pour_3d = Simulation(name="pour_3d", inputScript="in.pour", tags = ["lammps", "granular"], folder="examples/lammps/pour_3d", title = "3d pour", description="Pouring of granular particles into a 3d box, then chute flow.")
shear = Simulation(name="shear", inputScript="in.shear", tags = ["lammps", "shear"], folder="examples/lammps/shear", title="Shear", description="sideways shear applied to 2d solid.")
shear_void = Simulation(name="shear_void", inputScript="in.shear.void", tags = ["lammps", "shear"], folder="examples/lammps/shear_void", title="Shear with void", description="Sideways shear applied to 2d solid with a void.")

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
