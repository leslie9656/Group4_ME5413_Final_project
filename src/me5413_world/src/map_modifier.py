#!/usr/bin/env python3

import rospy
from nav_msgs.msg import OccupancyGrid

def map_callback(msg):
    # Get the map dimensions and resolution
    width = msg.info.width
    height = msg.info.height
    resolution = msg.info.resolution

    # Get the origin of the map in real-world coordinates
    origin_x = msg.info.origin.position.x
    origin_y = msg.info.origin.position.y

    # Set the whole area obstacle
    # # Compute the indices of the cells within the range [-1:1,2,4.5]
    # x_min = int(((-0.7 - origin_x) / resolution))
    # x_max = int(((4.9 - origin_x) / resolution))
    # y_min = int(((0.8 - origin_y) / resolution))
    # y_max = int(((4.3 - origin_y) / resolution))

    # # Set the value of the cells within the range to be obstacles
    # data_list = list(msg.data)
    # for y in range(y_min, y_max):
    #     for x in range(x_min, x_max):
    #         index = y * width + x
    #         data_list[index] = 100

    # Set the invisible obstacle
    x_obstacles = int(((4.9 - origin_x) / resolution))
    y_obstacles = int(((0.9 - origin_y) / resolution))
    data_list = list(msg.data)
    interval = int(0.35 / resolution)
    x_start = int(((1 - origin_x) / resolution))
    x_end = int(((2.6 - origin_x) / resolution))
    for x in range(x_start, x_end, interval):
        index = y_obstacles * width + x
        data_list[index] = 100
    y_start = int(((1.5 - origin_y) / resolution))
    y_end = int(((4.1 - origin_y) / resolution))
    for y in range(y_start, y_end, interval):
        index = y * width + x_obstacles
        data_list[index] = 100

    # Create a new OccupancyGrid message with the modified data
    modified_msg = OccupancyGrid()
    modified_msg.header = msg.header
    modified_msg.info = msg.info
    modified_msg.data = tuple(data_list)

    # Publish the modified map
    pub.publish(modified_msg)

rospy.init_node('map_modifier')

# Subscribe to the map topic
rospy.Subscriber('/map', OccupancyGrid, map_callback)

# Advertise the modified map topic
pub = rospy.Publisher('/modified_map', OccupancyGrid, queue_size=10)

rospy.spin()