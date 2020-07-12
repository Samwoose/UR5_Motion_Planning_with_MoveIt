#! /usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()    
group = moveit_commander.MoveGroupCommander("manipulator")
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory)

'''
#set the target pose manually with group variable values.
group_variable_values = group.get_current_joint_values()
group_joints = group.get_joints()

print(group_joints)

group_variable_values[1] = -1.5
group.set_joint_value_target(group_variable_values)
'''

#Motion planning and executing with pre-defined poses
#pose 1.allZeros, pose 2.bentPose, pose 3.standing

#Pose 2
group.set_named_target("bentPose")

plan1 = group.plan()
group.go(wait=True)

#Pose 3
group.set_named_target("standing")

plan2 = group.plan()
group.go(wait=True)

#Pose 2
group.set_named_target("bentPose")

plan3 = group.plan()
group.go(wait=True)

#Pose 1
group.set_named_target("allZeros")

plan2 = group.plan()
group.go(wait=True)



rospy.sleep(5)

moveit_commander.roscpp_shutdown()
