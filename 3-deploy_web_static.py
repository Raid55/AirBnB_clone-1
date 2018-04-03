#!/usr/bin/python3
""" creates a zip file """
from datetime import datetime
from fabric.api import env, run, put, local
import os


env.hosts = ['34.227.229.159', '34.229.125.244']

def do_pack():
    try:
        time_stamp = datetime.now().strftime('%Y%m%d%H%M%S')
        file_name_n_path = "versions/web_static_{}.tgz".format(time_stamp)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name_n_path))
        return(file_name_n_path)
    except:
        return None

def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False
    try:
        archive = archive_path.split('/')[1]
        put(archive_path, '/tmp/')
        run("mkdir -p /data/web_static/releases/{}".format(archive[:-4]))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(archive, archive[:-4]))
        run("rm /tmp/{}".format(archive))
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/"
            .format(archive[:-4], archive[:-4]))
        run("rm -rf /data/web_static/releases/{}/web_static".format(archive[:-4]))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(archive[:-4]))
    except:
        return False

def deploy():
    ret = do_pack()
    if ret:
        return do_deploy(ret)
    else:
        return False
