import os
import sys

from app.tools.config_tools import get_config, REQUIREMENTS_CONFIG, APP_CONFIG
from app.tools.package_tools import get_package_info, install_package

app_config = get_config(APP_CONFIG)


def get_app_info():
    """
        get installed python package information
    :return: str info
    """
    requirements = get_config(REQUIREMENTS_CONFIG)["requirements"]
    pip_version = os.popen('pip -V').read().split(' ')[1]
    python_version = sys.version[0:5]
    info = {
        "pip_version": pip_version,
        "python_version": python_version
    }
    for requirement in requirements:
        version = get_package_info(requirement['name'])
        info[requirement['name']] = version
    return info


def install_app_require():
    """
        use pip to install packages stated in requirements.json
    :return:
    """
    requirements = get_config(REQUIREMENTS_CONFIG)["requirements"]
    for requirement in requirements:
        install_package(requirement["name"], requirement["version"])