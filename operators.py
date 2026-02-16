import bpy
from bpy.types import Operator

class MyOperator(Operator):
    bl_idname = "addon.my_operator"
    bl_label = "Test Operator"

    def execute(self, context):

        bpy.ops.mesh.primitive_cube_add(size=4)
        cube_obj = bpy.context.active_object

        if cube_obj is not None:
            cube_obj.location.z = 5

        return {"FINISHED"}
    
classes = [
    MyOperator
]

def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)
