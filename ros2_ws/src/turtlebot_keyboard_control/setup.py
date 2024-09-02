from setuptools import setup

package_name = 'turtlebot_keyboard_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Srushtei',
    maintainer_email='srushtei.hn@gmail.com',
    description='Package for controlling TurtleBot3 using keyboard',
    license='Your License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'keyboard_control = turtlebot_keyboard_control.keyboard_control:main',
        ],
    },
)

