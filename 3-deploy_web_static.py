#!/usr/bin/python3
from fabric.api import *
from datetime import datetime
import os
do_pack = __import__('1-pack_web_static').do_pack

env.hosts = ['54.165.47.201', '54.175.138.0']


def do_deploy():
    """
    function to deploy

    parameters:
    none

    return :
    True if everything is okay else return False
    """
    archive_path = do_pack()
    if os.path.exists(archive_path):
        return (do_deploy(archive_pat))
    else:
        return False


def do_deploy(archive_path):
    """
    function that distrube my archive to my servers

    parameters:
    (str) archive_path

    returns:
    (bool) True if everything is okay else False
    """
    try:
        archive_path_a = archive_path.split("versions/")
        path_without_dir = "".join(archive_path_a)
        archive_path_ext = path_without_dir.split(".tgz")
        dir_name = "".join(archive_path_ext)
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}".format(dir_name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}\
                ".format(path_without_dir, dir_name))
        run("rm -rf /tmp/{}".format(path_without_dir))
        run("mv /data/web_static/releases/{}/web_static/*\
                /data/web_static/releases/{}".format(dir_name, dir_name))
        run("rm -rf /data/web_static/releases/{}/web_static\
                ".format(dir_name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/\
                /data/web_static/current".format(dir_name))
        print("New version deployed!")
        return True
    except Exception:
        return False
