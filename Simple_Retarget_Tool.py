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




    bpy.ops.pose.constraint_add_with_targets(type='TRANSFORM')
    actposebone.constraints[-1].name = 'TranformLoc SMPTarget'
    actposebone.constraints["TranformLoc SMPTarget"].target_space = 'LOCAL'
    actposebone.constraints["TranformLoc SMPTarget"].owner_space = 'LOCAL'
    actposebone.constraints["TranformLoc SMPTarget"].from_rotation_mode = 'AUTO'
    actposebone.constraints["TranformLoc SMPTarget"].map_from = 'LOCATION'
    actposebone.constraints["TranformLoc SMPTarget"].map_to = 'LOCATION'
    actposebone.constraints["TranformLoc SMPTarget"].to_min_x = actposebone.location[0]
    actposebone.constraints["TranformLoc SMPTarget"].to_min_y = actposebone.location[1]
    actposebone.constraints["TranformLoc SMPTarget"].to_min_z = actposebone.location[2]
    actposebone.constraints["TranformLoc SMPTarget"].mix_mode = 'ADD'
    bpy.ops.constraint.move_up(constraint='TranformLoc SMPTarget', owner='BONE')
    bpy.ops.constraint.move_up(constraint='TranformLoc SMPTarget', owner='BONE')

    actposebone.rotation_mode = 'XYZ'
    bpy.ops.pose.constraint_add_with_targets(type='TRANSFORM')
    actposebone.constraints[-1].name = 'TranformRot SMPTarget'
    actposebone.constraints["TranformRot SMPTarget"].target_space = 'LOCAL'
    actposebone.constraints["TranformRot SMPTarget"].owner_space = 'LOCAL'
    actposebone.constraints["TranformRot SMPTarget"].map_from = 'ROTATION'
    actposebone.constraints["TranformRot SMPTarget"].from_rotation_mode = 'AUTO'
    actposebone.constraints["TranformRot SMPTarget"].map_to = 'ROTATION'
    actposebone.constraints["TranformRot SMPTarget"].to_euler_order = 'XYZ'
    actposebone.constraints["TranformRot SMPTarget"].to_min_x_rot = actposebone.rotation_euler[0]
    actposebone.constraints["TranformRot SMPTarget"].to_min_y_rot = actposebone.rotation_euler[1]
    actposebone.constraints["TranformRot SMPTarget"].to_min_z_rot = actposebone.rotation_euler[2]
    actposebone.constraints["TranformRot SMPTarget"].mix_mode_rot = 'BEFORE'
    bpy.ops.constraint.move_up(constraint='TranformRot SMPTarget', owner='BONE')
    bpy.ops.constraint.move_up(constraint='TranformRot SMPTarget', owner='BONE')
    bpy.ops.constraint.move_up(constraint='TranformRot SMPTarget', owner='BONE')




    actposebone.rotation_mode = 'QUATERNION'

    bpy.ops.pose.rot_clear()
    bpy.ops.pose.loc_clear()


# Set Rest Pose with Object

def set_rest_pose_object(context):
    rig = bpy.context.active_object

    for obj in bpy.data.objects:
        if (obj.type == 'MESH' and
            rig in [m.object for m in obj.modifiers if m.type == 'ARMATURE']
            ):
                
                objectToSelect = bpy.data.objects[obj.name]
                objectToSelect.select_set(True)    
                bpy.context.view_layer.objects.active = objectToSelect
                for mod in bpy.context.object.modifiers:
                    if mod.type == 'ARMATURE':
                        bpy.ops.object.modifier_copy(modifier=mod.name)
                        bpy.ops.object.modifier_apply(modifier=mod.name)
                        bpy.context.object.modifiers.active.name = mod.name
                        bpy.ops.object.select_all(action='DESELECT')
                        
    bpy.context.view_layer.objects.active = rig
    bpy.ops.pose.armature_apply(selected=False)



def clear_constrain(context):

    bones = bpy.context.selected_pose_bones

    for bone in bones:

        for a in bone.constraints:
            if 'CopyLoc SMPTarget' in a.name:
                bone.constraints.remove(a)

        for b in bone.constraints:
            if 'CopyRot SMPTarget' in b.name:
                bone.constraints.remove(b)

        for c in bone.constraints:
            if 'TranformRot SMPTarget' in c.name:
                bone.constraints.remove(c)

        for d in bone.constraints:
            if 'TranformLoc SMPTarget' in d.name:
                bone.constraints.remove(d)

    bpy.ops.pose.rot_clear()
    bpy.ops.pose.loc_clear()     




class RetargetRoot(bpy.types.Operator):
    """Retarget root bone"""
    bl_idname = "simpleretarget.retarget_root"
    bl_label = "Retarget Root"


    def execute(self, context):

        try:
            retarget_root(context)
            return {'FINISHED'}
        except:
            return {'CANCELLED'}


class RetargetBones(bpy.types.Operator):
    """Retarget muscle bone"""
    bl_idname = "simpleretarget.retarget_bone"
    bl_label = "Retarget Bone"


    def execute(self, context):

        try:
            retarget_bone(context)
            return {'FINISHED'}
        except:
            return {'CANCELLED'}

class SetRestPoseObject(bpy.types.Operator):
    """Set current pose as rest pose (with object pose)"""
    bl_idname = "simpleretarget.set_rest_pose_with_object"
    bl_label = "Set Rest Pose with Object"


    def execute(self, context):

        try:
            set_rest_pose_object(context)
            return {'FINISHED'}
        except:
            return {'CANCELLED'}



class ClearConstrain(bpy.types.Operator):
    """Clear pose constraints"""
    bl_idname = "simpleretarget.clear_constraint"
    bl_label = "Retarget Bone"


    def execute(self, context):

        try:
            clear_constrain(context)
            return {'FINISHED'}
        except:
            return {'CANCELLED'}            

#UI

class SimpleRetargetUI(Menu):
    bl_label = "Simple Retarget"
    bl_idname = "VIEW3D_MT_simpleretarget"


    
    def draw(self, context):
        layout = self.layout

        layout.operator("simpleretarget.set_rest_pose_with_object", text="set rest pose with objects")
        layout.operator("simpleretarget.retarget_root", text="retarget root")
        layout.operator("simpleretarget.retarget_bone", text="retarget muscle bone")
        layout.operator("simpleretarget.clear_constraint", text="clear pose constraint")



def draw_item(self, context):
    layout = self.layout
    layout.menu(SimpleRetargetUI.bl_idname)


classes = (
    RetargetRoot,
    RetargetBones,
    ClearConstrain,
    SetRestPoseObject,
    SimpleRetargetUI
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