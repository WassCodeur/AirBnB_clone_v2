#!/usr/bin/python3
from fabric.api import *

env.hosts = ['54.165.47.201', '54.175.138.0']


def do_deploy(archive_path):
    """
    function that distrube an archive to my servers

    parameters:
    (str) archive_path

    return:
    True if everything is okay
    False if something went wrong
    """
    try:
        put(archive_path, '/tmp/')
        run("tar -xvzf /tmp/{}\
                -c /data/web_static/releases/".format(archive_path))
        run("rm  /tmp/{}".format(archive_path))
        run("ln -sf /data/web_statis/releases/ /data/web_static/current")
        return True
    except ValueError:
        return False
