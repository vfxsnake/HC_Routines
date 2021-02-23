import maya.standalone

import maya.cmds as cmds

class MayaStd(object):
    def __init__(self):
        maya.standalone.initialize(name='python')

if __name__ == "__main__":
    StartMaya = MayaStd()