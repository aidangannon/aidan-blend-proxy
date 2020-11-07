from bpy.types import Object as BlendObj


class Asset:
    """defines an project's assets

    attributes: file, obj
    """

    def __init__(self):
        self.__file: str
        self.__obj: BlendObj

    # region blender api calls

    @staticmethod
    def loadFromFile(file: str) -> 'Asset':
        """loads blender object from file"""
        raise NotImplementedError('not implemented')

    # endregion

    # region setters

    def __setFile(self, file: str) -> 'Asset':
        self.__file = file
        return self

    def __setObj(self, obj: BlendObj) -> 'Asset':
        self.__obj = obj
        return self

    # endregion

    # region getters

    def getFile(self) -> str:
        return self.__file

    def getObj(self) -> BlendObj:
        return self.__obj

    # endregion
