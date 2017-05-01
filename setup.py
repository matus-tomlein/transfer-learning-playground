from setuptools import setup, find_packages

setup(
    name='tflscripts',
    version='0.0.1',
    url='https://github.com/matus-tomlein/transfer-learning-playground',
    download_url='',
    author='Matus Tomlein',
    author_email='matus.tomlein@gmail.com',
    description='Scripts for a transfer learning experiment.',
    packages=['tflscripts'],
    data_files=[('tflscripts', ['tflscripts/configuration.json'])],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    license='MIT',
    install_requires=[],
)
