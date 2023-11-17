class Media:
    _type = str()
    _path = str()

    def __init__(self, type: str, path:str) -> None:
        self._type = type
        self._path = path

    def gettype(self):
        return self._type
    
    def getpath(self):
        return self._path
    
    def settype(self, type):
        self._type = type

    def setpath(self, path):
        self._path = path
    