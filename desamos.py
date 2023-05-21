#!/usr/bin/python3

from fabric.api import *
from fabric import Collection  # Import Collection from fabric module
from datetime import datetime
import os

env.hosts = ['localhost']

def do_pack():
    """
    This function allows creating an archive of our web_static.

    Parameters: no parameters

    Return:
    - Archive path if everything is okay.
    - None if something went wrong.
    """
    try:
        current = datetime.now().strftime('%Y%m%d%H%M%S')
        archive = "versions/web_static_{}.tgz".format(current)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(archive))
        size = os.path.getsize(archive)
        print("web_static packed: {} -> {}Bytes".format(archive, size))
        return archive
    except ValueError:
        return None

ns = Collection()  # Create an instance of Collection

# Add your tasks to the Collection
ns.add_task(do_pack)

