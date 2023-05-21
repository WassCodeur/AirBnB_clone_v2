import fabric as fab
from datetime import datetime
import os




def pack():
    """
    This function allow to create an archive of our web_static.

    Parameters: no parameters

    Return:
    archive path if the everything is okay.

    None if something went wronget
    """
    try:

        current = datetime.now().strftime('%Y%m%d%H%M%S')
        archive = "versions/web_static_{}.tgz".format(current)
        fab.local("mkdir -p versions")
        fab.local("tar -cvzf {} web_static".format(archive))
        size = os.path.getsize(archive)
        print("web_static packed: {} -> {}Bytes".format(archive, size))
        return archive
    except ValueError:
        return None
