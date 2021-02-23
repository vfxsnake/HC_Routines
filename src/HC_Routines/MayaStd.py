import MayaUtils

class MayaStd(object):
    def __init__(self):
        
        import maya.standalone
        maya.standalone.initialize()
        maya.standalone.initialize(name='python')
        
if __name__ == "__main__":
    print "maya"

