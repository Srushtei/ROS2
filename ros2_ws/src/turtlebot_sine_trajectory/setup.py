from setuptools import setup
import os
from glob import glob

package_name = 'turtlebot_sine_trajectory'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='srushtei',
    maintainer_email='srushtei.hn@gmail.com',
    description='ROS2 package to make TurtleBot follow a sinusoidal trajectory.',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sine_trajectory = turtlebot_sine_trajectory.scripts.sine_trajectory:main'
        ],
    },
    package_data={
        '': ['scripts/*.py'],  # Include the scripts
    },
)

