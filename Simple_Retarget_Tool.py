# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


bl_info = {
    "name": "Simple Retarget Tool",
    "description": "Simply retarget bone animation",
    "author": "Fahad Hasan Pathik CGVIRUS",
    "version": (1, 0),
    "blender": (2, 90, 3),
    "category": "Rigging",
    "wiki_url": "https://github.com/cgvirus/Simple-Retarget-Tool-Blender"
    }



import bpy
from bpy.types import Menu


#Create muscle Constraints


def retarget_bone(context):

    actposebone = bpy.context.active_pose_bone
    
    bpy.ops.object.mode_set(mode='POSE')
    bpy.context.object.pose.use_mirror_x = False
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.context.object.data.use_mirror_x = False
    bpy.context.active_bone.roll = bpy.context.selected_bones[1].roll
    bpy.ops.object.mode_set(mode='POSE')
    bpy.ops.pose.constraint_add_with_targets(type='COPY_LOCATION')
    actposebone.constraints[-1].name = 'CopyLoc SMPTarget'
    actposebone.constraints["CopyLoc SMPTarget"].target_space = 'LOCAL'
    actposebone.constraints["CopyLoc SMPTarget"].owner_space = 'LOCAL'
    actposebone.constraints["CopyLoc SMPTarget"].use_offset= True

    bpy.ops.pose.constraint_add_with_targets(type='COPY_ROTATION')
    actposebone.constraints[-1].name = 'CopyRot SMPTarget'
    actposebone.constraints["CopyRot SMPTarget"].target_space = 'LOCAL'
    actposebone.constraints["CopyRot SMPTarget"].owner_space = 'LOCAL'
    actposebone.constraints["CopyRot SMPTarget"].mix_mode = 'BEFORE'




#Create Root Constraints

def retarget_root(context):

    actposebone = bpy.context.active_pose_bone

    bpy.ops.pose.rot_clear()
    bpy.ops.pose.loc_clear()



    bpy.ops.object.mode_set(mode='POSE')
    bpy.context.object.pose.use_mirror_x = False
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.context.object.data.use_mirror_x = False
    bpy.context.active_bone.roll = bpy.context.selected_bones[1].roll
    bpy.ops.object.mode_set(mode='POSE')
    bpy.ops.pose.constraint_add_with_targets(type='COPY_LOCATION')
    actposebone.constraints[-1].name = 'CopyLoc SMPTarget'
    actposebone.constraints["CopyLoc SMPTarget"].target_space = 'WORLD'
    actposebone.constraints["CopyLoc SMPTarget"].owner_space = 'WORLD'
    actposebone.constraints["CopyLoc SMPTarget"].use_offset= True

    bpy.ops.pose.constraint_add_with_targets(type='COPY_ROTATION')
    actposebone.constraints[-1].name = 'CopyRot SMPTarget'
    actposebone.constraints["CopyRot SMPTarget"].target_space = 'WORLD'
    actposebone.constraints["CopyRot SMPTarget"].owner_space = 'WORLD'
    actposebone.constraints["CopyRot SMPTarget"].mix_mode = 'BEFORE'

    bpy.ops.pose.rot_clear()
    bpy.ops.pose.loc_clear()

    bpy.ops.pose.visual_transform_apply()
    actposebone.location[0] = actposebone.location[0] * (-1) 
    actposebone.location[1] = actposebone.location[1] * (-1) 
    actposebone.location[2] = actposebone.location[2] * (-1) 
    actposebone.rotation_quaternion[0] = actposebone.rotation_quaternion[0] * (-1) 
    actposebone.rotation_quaternion[1] = actposebone.rotation_quaternion[1] * (1) 
    actposebone.rotation_quaternion[2] = actposebone.rotation_quaternion[2] * (-1) 
    actposebone.rotation_quaternion[3] = actposebone.rotation_quaternion[3] * (-1)
    bpy.context.scene.frame_current = 1



class RetargetRoot(bpy.types.Operator):
    """Retarget Root Bone"""
    bl_idname = "simpleretarget.retarget_root"
    bl_label = "Retarget Root"


    def execute(self, context):

        try:
            retarget_root(context)
            return {'FINISHED'}
        except:
            return {'CANCELLED'}


class RetargetBones(bpy.types.Operator):
    """Retarget Muscle Bone"""
    bl_idname = "simpleretarget.retarget_bone"
    bl_label = "Retarget Bone"


    def execute(self, context):

        try:
            retarget_bone(context)
            return {'FINISHED'}
        except:
            return {'CANCELLED'}


class ClearConstrain(bpy.types.Operator):
    """Clear pose constraints"""
    bl_idname = "simpleretarget.clear_constraint"
    bl_label = "Retarget Bone"


    def execute(self, context):

        try:
            bpy.ops.constraint.delete(constraint="CopyLoc SMPTarget", owner='BONE')
            bpy.ops.constraint.delete(constraint="CopyRot SMPTarget", owner='BONE')
            bpy.ops.pose.rot_clear()
            bpy.ops.pose.loc_clear()
            return {'FINISHED'}
        except:
            return {'CANCELLED'}            

#UI

class SimpleRetarget(Menu):
    bl_label = "Simple Retarget"
    bl_idname = "VIEW3D_MT_simpleretarget"


    
    def draw(self, context):
        layout = self.layout

        layout.operator("simpleretarget.retarget_root", text="retarget root")
        layout.operator("simpleretarget.retarget_bone", text="retarget muscle bone")
        layout.operator("simpleretarget.clear_constraint", text="clear pose constraint")



def draw_item(self, context):
    layout = self.layout
    layout.menu(SimpleRetarget.bl_idname)


classes = (
    RetargetRoot,
    RetargetBones,
    ClearConstrain,
    SimpleRetarget
)


def register():

    from bpy.utils import register_class
    
    for c in classes:
        bpy.utils.register_class(c)

    # lets add ourselves to the editor maenu
    bpy.types.VIEW3D_MT_pose.append(draw_item)

def unregister():
    
    from bpy.utils import unregister_class
    
    # remove operator and preferences
    for c in reversed(classes):
        bpy.utils.unregister_class(c)

    # lets add ourselves to the editor maenu
    bpy.types.VIEW3D_MT_pose.remove(draw_item)


if __name__ == "__main__":
    register()