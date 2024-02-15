#!/usr/bin/python3

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

import os


def generate_launch_description():
    share_dir = get_package_share_directory("bluesea2")
    parameter_file = LaunchConfiguration("params_file_bluesea2")

    params_declare = DeclareLaunchArgument(
        "params_file_bluesea2",
        default_value=os.path.join(share_dir, "params", "LDS-50C-2.yaml"),
        description="FPath to the ROS2 parameters file to use.",
    )

    driver_node = Node(
        name="bluesea_node",
        namespace="/",
        package="bluesea2",
        executable="bluesea_node",
        output="screen",
        # emulate_tty=True,
        parameters=[parameter_file],
        respawn=True,
        respawn_delay=5.0,
    )

    # Lidar 2D filter Params
    lidar2d_filter_params_file = None
    try:
        lidar2d_filter_params_file = os.path.join(
            get_package_share_directory("navigation"),
            "config",
            "lidar_filter_0deg.yaml",
        )
    except Exception as e:
        print(f"Collision monitor failed reading params file. Got: {e}")

    # tf2_node = Node(
    #     package="tf2_ros",
    #     executable="static_transform_publisher",
    #     name="static_tf_pub_laser",
    #     arguments=[
    #         "-0.12",
    #         "0",
    #         "0.546",
    #         "3.1416",
    #         "0",
    #         "0",
    #         "1",
    #         "chassis",
    #         "laser_link",
    #     ],
    # )

    return LaunchDescription(
        [
            params_declare,
            driver_node,
            # tf2_node,
            Node(
                executable="scan_to_scan_filter_chain",
                package="laser_filters",
                exec_name="scan_filter",
                parameters=[lidar2d_filter_params_file],
                output="screen",
                respawn=True,
                respawn_delay=5.0,
            ),
        ]
    )
