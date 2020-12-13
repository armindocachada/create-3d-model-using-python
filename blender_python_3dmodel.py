import bpy
import numpy as np

from PIL import Image
grey_img = Image.open("~/projects/Blender Python 3D Model/IMG_20180724_191936.jpg").convert('L')

max_size=(500,500)
max_height=30
min_height=0

grey_img.thumbnail(max_size)
imageNp = np.array(grey_img)
maxPix=imageNp.max()
minPix=imageNp.min()

(W,H)=grey_img.size

print(f"W,H={W},{H}")
vertices=[]
edges=[]
faces=[]

DX=1
DY=1

for Y in range(0, H, DY):
    for X in range(0,W,DX):
        pixelIntensity = imageNp[Y][X]
        Z = (pixelIntensity * max_height) / maxPix
        vertices.append((X,Y,Z))
        
        
for X in range(0, W-1, DX):
    for Y in range(0, H-1, DY):
        face_v1= X+Y*W
        face_v2=X + 1 + Y* W
        face_v3=X + 1 + (Y+1) * W
        
        faces.append((face_v1,face_v2,face_v3))
        
        face_v1= X+Y*W
        face_v2=X  + (Y+1)* W
        face_v3=X + 1 + (Y+1) * W
        
        faces.append((face_v1,face_v2,face_v3))
        
new_mesh=bpy.data.meshes.new("new_mesh")
new_mesh.from_pydata(vertices,edges,faces)
new_mesh.update()
# make objec from the mesh
new_object = bpy.data.objects.new("new_object",new_mesh)
view_layer=bpy.context.view_layer
view_layer.active_layer_collection.collection.objects.link(new_object)
