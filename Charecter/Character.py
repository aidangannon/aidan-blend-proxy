from bpy.types import Armature
from bpy.types import Object as BlendObj


class Character:
    """defines an project's character

    attributes: file, obj, rig
    """

    def __init__(self):
        self.__file: str
        self.__obj: Armature
        self.__rig: BlendObj

    # region blender api calls

    @staticmethod
    def loadFromFile() -> 'Character':
        """loads blender object from file"""
        raise NotImplementedError('not implemented')

    # endregion

    # region setters

    def __setFile(self, file: str) -> 'Character':
        self.__file = file
        return self

    def __setObj(self, obj: BlendObj) -> 'Character':
        self.__obj = obj
        return self

    def __setRig(self, rig: Armature) -> 'Character':
        self.__rig = rig
        return self

    # endregion

    # region getters

    def getFile(self) -> str:
        return self.__file

    def getObj(self) -> BlendObj:
        return self.__obj

    def getRig(self) -> Armature:
        return self.__rig

    # endregion
