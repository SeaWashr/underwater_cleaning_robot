#启动 Gazebo 服务器

"""Launch gz_server in a component container."""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, TextSubstitution
from ros_gz_sim.actions import GzServer


def generate_launch_description():

    # 声明 launch 参数
    declare_world_sdf_file_cmd = DeclareLaunchArgument(
        'world_sdf_file', default_value=TextSubstitution(text=''),
        description='Path to the SDF world file')
    declare_world_sdf_string_cmd = DeclareLaunchArgument(
        'world_sdf_string', default_value=TextSubstitution(text=''),
        description='SDF world string')
    declare_container_name_cmd = DeclareLaunchArgument(
        'container_name', default_value='ros_gz_container',
        description='Name of container that nodes will load in if use composition',)
    declare_create_own_container_cmd = DeclareLaunchArgument(
        'create_own_container', default_value='False',
        description='Whether we should start our own ROS container when using composition.',)
    declare_use_composition_cmd = DeclareLaunchArgument(
        'use_composition', default_value='False',
        description='Use composed bringup if True')

    gz_server_action = GzServer(
        world_sdf_file=LaunchConfiguration('world_sdf_file'),
        world_sdf_string=LaunchConfiguration('world_sdf_string'),
        container_name=LaunchConfiguration('container_name'),
        create_own_container=LaunchConfiguration('create_own_container'),
        use_composition=LaunchConfiguration('use_composition'),
    )

    # Create the launch description and populate
    ld = LaunchDescription()

    # Declare the launch options
    ld.add_action(declare_world_sdf_file_cmd)
    ld.add_action(declare_world_sdf_string_cmd)
    ld.add_action(declare_container_name_cmd)
    ld.add_action(declare_create_own_container_cmd)
    ld.add_action(declare_use_composition_cmd)
    # Add the gz_server action
    ld.add_action(gz_server_action)

    return ld