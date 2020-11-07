import bpy

# region type aliases

BlendObj = bpy.types.Object

# endregion


class Asset:
    """defines an project's asset"""

    def __init__(self, file: str, obj: BlendObj):
        self.__file: str = file
        self.__obj: BlendObj = obj

    # region blender api calls

    @staticmethod
    def loadFromFile() -> 'Asset':
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
