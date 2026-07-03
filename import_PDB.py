import bpy
import random

# Path to your .PDB file
pdb_file="C:/Users/AJ269416.INTRA/Downloads/fBOX.pdb"

# Initiate object collections to store atoms
collection = bpy.data.collections.new("Atoms")
bpy.context.scene.collection.children.link(collection)

# Read .PDB and extract atoms spatial data
with open(pdb_file, "r") as f:
    lines = f.readlines()

for line in lines:
    if line.startswith("ATOM"):
        atom_name = line[12:16].strip()
        x = float(line[30:38].strip())
        y = float(line[38:46].strip())
        z = float(line[46:54].strip())
        scale = random.uniform(1.2, 1.5) # Ypiu can change here the random size of the atoms to get a globular effect
        new_sphere = bpy.data.objects.new(f"Atom_{atom_name}", atom_mesh)
        new_sphere.location = (x, y, z)
        new_sphere.scale = (scale, scale, scale)
        collection.objects.link(new_sphere)
