"""Utilities"""

import sys
import os

def win32_longpath(path):
    '''Helper function to add the long path prefix for Windows

    So that shutil.copytree won't fail while working with paths with 255+ chars.
    '''
    if sys.platform == 'win32':
        # The use of os.path.normpath here is necessary since "the "\\?\" prefix to a path string
        # tells the Windows APIs to disable all string parsing and to send the string that follows
        # it straight to the file system".
        # (See https://docs.microsoft.com/pt-br/windows/desktop/FileIO/naming-a-file)
        return '\\\\?\\' + os.path.normpath(path)
    else:
        return path
