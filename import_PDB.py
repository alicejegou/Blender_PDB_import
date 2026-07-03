import bpy
import random

# Path to your .PDB file
pdb_file="C:/Users/AJ269416.INTRA/Downloads/bZIP3.pdb"

# Init collections
collection = bpy.data.collections.new("Proteine")
bpy.context.scene.collection.children.link(collection)

# Creating spheres meshes for atoms 
bpy.ops.mesh.primitive_uv_sphere_add(radius=1.0)  # Change as you want atoms base radius
sphere_template = bpy.context.active_object
sphere_template.name = "Atom_Template"
sphere_template.hide_viewport = True
sphere_template.hide_render = True

atom_mesh = sphere_template.data

# Init collections
collection = bpy.data.collections.new("Atoms")
bpy.context.scene.collection.children.link(collection)

# Parse .PDB file to extract atoms disposition 
with open(pdb_file, "r") as f:
    lines = f.readlines()

for line in lines:
    if line.startswith("ATOM"):
        atom_name = line[12:16].strip()
        x = float(line[30:38].strip())
        y = float(line[38:46].strip())
        z = float(line[46:54].strip())
        scale = random.uniform(1.2, 1.5) # You can canpley with individual atoms scales to create a globular effect
        new_sphere = bpy.data.objects.new(f"Atom_{atom_name}", atom_mesh)
        new_sphere.location = (x, y, z)
        new_sphere.scale = (scale, scale, scale)
        collection.objects.link(new_sphere)
