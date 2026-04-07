FROM osrf/ros:jazzy-desktop

SHELL ["/bin/bash", "-c"]

# Instalar
RUN apt update && apt upgrade -y && \
    apt install -y python3-colcon-common-extensions nano python3-matplotlib

# Workspace
RUN source /opt/ros/jazzy/setup.bash && \
    mkdir -p /ros2_ws/src && \
    cd /ros2_ws/src && \
    ros2 pkg create --build-type ament_python sensor_program --license MIT

# Guardar informacion del plotter
RUN mkdir -p /ros2_ws/data

# Configurar el setup.py con 3 nodos
RUN cat > /ros2_ws/src/sensor_program/setup.py << 'EOF'
from setuptools import find_packages, setup

package_name = 'sensor_program'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='user@example.com',
    description='Sensor program',
    license='MIT',
    entry_points={
        'console_scripts': [
            'sensor_node = sensor_program.sensor_node:main',
            'reader_node = sensor_program.reader_node:main',
            'plotter_node = sensor_program.plotter_node:main',
        ],
    },
)
EOF

# Sources
RUN echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc && \
    echo "source /ros2_ws/install/setup.bash" >> ~/.bashrc

WORKDIR /ros2_ws

ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["bash"]
