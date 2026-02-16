import bpy

from bpy.types import Context, Panel

from . import operators

class CommonPanel:
    """Contains common properties."""
    bl_space_type = "VIEW_3D" # 3D viewport area
    bl_region_type = "UI" # Sidebar region
    bl_category = "Addon Template" # The label that appears on the sidebar.

class MyPanel(CommonPanel, Panel):
    bl_idname = "VIEW_3D_PT_my_panel" # more info: https://docs.blender.org/api/current/bpy.types.Panel.html
    bl_label = "My Panel" # Title of the panel.
    
    def draw(self, context):

        layout = self.layout
        assert layout is not None
        
        col = layout.column()
        col.operator(operators.MyOperator.bl_idname, text=operators.MyOperator.bl_label)
        col.operator(operators.MyOperatorWithPopup.bl_idname, text=operators.MyOperatorWithPopup.bl_label)


classes = [
    MyPanel
]

def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)