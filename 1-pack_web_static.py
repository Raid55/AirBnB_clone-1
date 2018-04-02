#!/usr/bin/python3
""" creates a zip file """
from datetime import datetime
from fabric.api import local


def do_pack():
    try:
        time_stamp = datetime.now().strftime('%Y%m%d%H%M%S')
        file_name_n_path = "versions/web_static_{}.tgz".format(time_stamp)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name_n_path))
        return(file_name_n_path)
    except:
        return None
