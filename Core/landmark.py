class Landmark:
    _name = str()
    _position = 0, 0

    
    def __init__(self, position: tuple=None, name: str='') -> None:
         self._position = position
         self._name = name

    def getposition(self) -> tuple:
        return self._position
    
    def getname(self) -> str:
        return self._name
    
    def setposition(self, position: tuple) -> None:
        self._position = position

    def setname(self, name) -> None:
        self._name = name
