import bpy
from bpy.types import Operator

# more details about operators: https://docs.blender.org/api/current/bpy.types.Operator.html

class MyOperator(Operator):
    bl_idname = "addon.my_operator"
    bl_label = "Test Operator"

    def execute(self, context):

        bpy.ops.mesh.primitive_cube_add(size=4)
        cube_obj = bpy.context.active_object

        if cube_obj is not None:
            cube_obj.location.z = 5

        return {"FINISHED"}

# operator with configurable properties in a popup on the lower-left corner 
# of the screen.
class MyOperatorWithPopup(Operator):
    bl_idname = "addon.my_operator_popup"
    bl_label = "Test Operator Popup"
    bl_options = {'REGISTER', 'UNDO'}

    z_offset: bpy.props.FloatProperty(name="Z Offset", default=5)
    cube_size: bpy.props.FloatProperty(name="Cube Size", default=4)

    def execute(self, context):

        bpy.ops.mesh.primitive_cube_add(size=self.cube_size)
        cube_obj = bpy.context.active_object

        if cube_obj is not None:
            cube_obj.location.z = self.z_offset

        return {"FINISHED"}

classes = [
    MyOperator,
    MyOperatorWithPopup
]

def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)
