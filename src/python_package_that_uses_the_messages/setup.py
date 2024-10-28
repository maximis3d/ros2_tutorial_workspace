from setuptools import setup

package_name = 'python_package_that_uses_the_messages'

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
    maintainer='Max',
    maintainer_email="todo",
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'amazing_quote_publisher_node = python_package_that_uses_the_messages.amazing_quote_publisher_node:main',
            'amazing_quote_subscriber_node = python_package_that_uses_the_messages.amazing_quote_subscriber_node:main'
        ],
    },
)