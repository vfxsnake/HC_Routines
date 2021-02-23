class MayaStd(object):
    def __init__(self):
        
        import maya.standalone
        maya.standalone.initialize()
        maya.standalone.initialize(name='python')
        
        import pymel.core as pm
        import maya.mel as mel

    def OpenFile(self):
        print "Open file"
        
if __name__ == "__main__":
    StartMaya = MayaStd()
    StartMaya.OpenFile()