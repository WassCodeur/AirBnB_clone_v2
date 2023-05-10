#!/usr/bin/python3
from fabric.api import *
from datetime import datetime
import os

env.hosts = ['54.165.47.201', '54.175.138.0']


def do_pack():
    """
    function that generate archive of my web_static content folder.

    Parameters:
    None

    return:
    the generated archive path if everything is okay
    None if something went wrong
    """
    try:
        current = datetime.now().strftime('%Y%m%d%H%M%S')
        archive_path = "versions/web_static_{}.tgz".format(current)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(archive_path))
        size = os.path.getsize(archive_path)
        print("web_static packed: {} -> {}Bytes".format(archive_path, size))
        return archive_path
    except Exception:
        return None


def do_deploy(archive_path):
    """
    function that distrube my archive to my servers

    parameters:
    (str) archive_path

    returns:
    (bool) True if everything is okay
    (bool) False if something went wrong
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


def do_deploy():
    """
    fonction that deploy web_static
    call:
    do_pack
    do_deploy(archive_path)

    parameters:
    None

    return:
    False if no archive has been created
    do_deploy value
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    else:
        return do_deploy(archive_path)
