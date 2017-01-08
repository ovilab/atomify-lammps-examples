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

diffusion={"objectId": "diffusion", "inputScript": "simple_diffusion.in", "tags": ["diffusion", "lj"], "folder": "examples/diffusion/diffusion", "name": "Diffusion", "description": "This example shows how you can measure the diffusion coefficient using the mean square displacement. The white atoms have mass 1 while the red atoms have mass 4. This results in the red atoms having diffusion coefficient half the value of the white ones."}
singlewater={"objectId": "singlewater", "inputScript": "singlewater.in", "tags": ["water", "manybody", "vashishta"], "folder": "examples/water/singlewater", "name": "Single water molecule", "description": "A single water molecule using the vashishta potential."}
watervapor={"objectId": "watervapor", "inputScript": "vapor.in", "tags": ["water", "manybody", "vashishta"], "folder": "examples/water/vapor", "name": "Water vapor", "description": "Low density water gas using the vashishta potential."}
betacristobalite={"objectId": "betacristobalite", "inputScript": "betacristobalite.in", "tags": ["silica", "crystal", "manybody", "vashishta"], "folder": "examples/silica/betacristobalite", "name": "Silica beta cristobalite", "description": "Beta cristobalite crystal using the vashishta potential."}
zeolite_zsm5={"objectId": "zeolite_zsm5", "inputScript": "zeolite_zsm5.in", "tags": ["silica", "zeolite", "manybody", "vashishta"], "folder": "examples/silica/zeolite_zsm5", "name": "Zeolite ZSM-5", "description": "Zeolite ZSM-5 using the vashishta potential."}
zeolite_ssz13={"objectId": "zeolite_ssz13", "inputScript": "ssz13_generate.in", "tags": ["silica", "zeolite", "manybody", "vashishta"], "folder": "examples/silica/zeolite_ssz13", "name": "Zeolite SSZ-13", "description": "Zeolite SSZ-13 using the vashishta potential."}
generate_nanoporous={"objectId": "generate_nanoporous", "inputScript": "generate_nanoporous.in", "tags": ["silica", "manybody", "vashishta"], "folder": "examples/silica/generate_nanoporous", "name": "Nanoporous silica", "description": "Generate a nanoporous silica structure from betacristobalite using the vashishta potential."}
gcmcAr={"objectId": "gcmcAr", "inputScript": "gcmcAr.in", "tags": ["gcmc", "zeolite", "lj", "argon"], "folder": "examples/gcmc/gcmcAr", "name": "Zeolite+Argon GCMC", "description": "Insert argon into a nanopore of nanoporous zeolite system using GCMC."}
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
abstract_translocation={"objectId": "abstract_translocation", "inputScript": "run.in.npt", "tags": ["moltemplate", "molecule", "solvation", "polymer"], "folder": "examples/moltemplate/abstract_translocation", "name": "Polymer through hole", "description": "This example contains a (crude and somewhat simple) example of the translocation of a (rather short) polymer through a hole in a wall, surrounded by an explicit LJ solvent."}
alkane_chain_single={"objectId": "alkane_chain_single", "inputScript": "run.in.nvt", "tags": ["moltemplate", "molecule", "alkane", "polymer", "hydrocarbon"], "folder": "examples/moltemplate/alkane_chain_single", "name": "Alkane chain", "description": "This example is a simple simulation of a long alkane chain, in a vacuum at room temperature using the OPLSAA force field."}
benzene={"objectId": "benzene", "inputScript": "run.in.npt", "tags": ["moltemplate", "molecule", "benzene", "hydrocarbon"], "folder": "examples/moltemplate/benzene", "name": "Benzene", "description": "This example shows how to build a box of benzene molecules using the AMBER/GAFF force-field."}
chromosome={"objectId": "benzene", "inputScript": "run.in.stage1", "tags": ["moltemplate", "molecule"], "folder": "examples/moltemplate/chromosome_metaphase_Naumova2013", "name": "Metaphase chromatin", "description": "This is an implementation of the \"two-stage\" model used by Maxim Imakaev in the Naumova et Al 2013 Science paper on metaphase chromatin."}
ethylene_benzene={"objectId": "ethylene_benzene", "inputScript": "run.in.npt", "tags": ["moltemplate", "molecule", "hydrocarbon", "benzene"], "folder": "examples/moltemplate/ethylene+benzene", "name": "Ethylene and benzene", "description": "This example shows how to simulate a mixture of ethylene and benzene using the AMBER/GAFF force field."}
frustrated={"objectId": "frustrated", "inputScript": "run_short_sim.in.nvt", "tags": ["moltemplate", "molecule", "protein", "polymer"], "folder": "examples/moltemplate/frustrated", "name": "Protein folding", "description": "During this short simulation the protein evolves from an unfolded initial conformation to a misfolded conformation. It can take a very long time."}
ice_crystal={"objectId": "ice_crystal", "inputScript": "run.in.npt", "tags": ["moltemplate", "molecule", "water", "ice"], "folder": "examples/moltemplate/ice_crystal", "name": "Ice crystal", "description": "A simulation of an ice crystal using SPCE water and the shake algorithm."}
methane={"objectId": "methane", "inputScript": "run.in.npt", "tags": ["moltemplate", "molecule", "methane", "hydrocarbon"], "folder": "examples/moltemplate/methane", "name": "Methane", "description": "This example demonstrates how to build a simulation containing a box of methane."}
nanotube_water={"objectId": "nanotube_water", "inputScript": "run.in.npt", "tags": ["moltemplate", "water", "carbon"], "folder": "examples/moltemplate/nanotube+water", "name": "Water in nanotube", "description": "This is a small version of a carbon-nanotube, water capillary system."}
water_methane={"objectId": "water_methane", "inputScript": "run.in.npt", "tags": ["moltemplate", "water", "SPCE", "methane", "hydrocarbon"], "folder": "examples/moltemplate/waterSPCE+methane", "name": "Methane in water", "description": "This example contains a mixture of SPCE water and methane. The methane molecules use OPLSAA force-field."}
water_nacl={"objectId": "water_nacl", "inputScript": "run.in.npt", "tags": ["moltemplate", "water", "SPCE", "nacl"], "folder": "examples/moltemplate/waterSPCE+Na+Cl", "name": "Salt water", "description": "This example contains a mixture of SPCE water and salt (NaCl)."}
water_isobutane={"objectId": "water_isobutane", "inputScript": "run.in.npt", "tags": ["moltemplate", "water", "TIP3P", "hydrocarbon"], "folder": "examples/moltemplate/waterTIP3P+isobutane", "name": "TIP3P water and isobutane", "description": "The simulation consists of a mixture of isobutane and water. Over time (less than 1 ns), the two molecules phase-separate."}

examples = [
    diffusion,
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
    shear_void,
    abstract_translocation,
    alkane_chain_single,
    benzene,
    chromosome,
    ethylene_benzene,
    frustrated,
    ice_crystal,
    methane,
    nanotube_water,
    water_methane,
    water_nacl,
    water_isobutane
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
