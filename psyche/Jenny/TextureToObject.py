import bpy

# First, select the object you want to apply the texture to
obj = bpy.context.object

# Then, create a new material to put on the object
material = bpy.data.materials.new(name = "NewMaterial")
# Enable the nodes
material.use_nodes = True

# Assign the certain material to the specific object
if obj.data.materials:
    # If the object already has a material on it, replace the original material
    obj.data.materials[0] = material
else:
    # If there are no materials on the object, append the new one
    obj.data.materials.append(material)

# Get the node tree for the specific material
material_nodes = material.node_tree.nodes

# Add an image texture node 
tex_image = material_nodes.new('ShaderNodeTexTimage')

# Load the image you would like and assign it to the image texture node
# Great free options for texture images - Poly Haven, CC0 Textures, Texture Haven, AmbientCG, Textures.com
# Your specific image path would go below
image_path = "C:\Users\jenny\Downloads\brown_mud_4k.blend\textures\brown_mud_disp_4k"
image = bpy.data.images.load(image_path)
tex_image.image = image

# You then need to connect the texture to the shader

# Find the Principled BSDF node
principled_bsdf = material_nodes.get('Principled BSDF')

# Connect the color output of the image texture to the base color of the shader
material.node_tree.links.new(principled_bsdf.inputs['Base Color'], tex_image.outputs['Color'])

# We then need to adjust the UV mapping if we would like, this is optional
# Add a texture coordinate node
tex_coord = material_nodes.new('ShaderNodeTexCoord')

# Add a mapping node
mapping = material_nodes.new('ShaderNodeMapping')

# Connect the texture coordinate node to the mapping code
material.node_tree.links.new(mapping.inputs['Vector'], tex_coord.outputs['UV'])

# Connect the mapping node to the image texture
material.node_tree.links.new(tex_image.inputs['Vector'], mapping.outputs['Vector'])
