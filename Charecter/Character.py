from bpy.types import Collection as BlendCollection


class Character:
    """defines an project's character

    attributes: file, obj, rig
    """

    def __init__(self):
        self.__file: str
        self.__rig: BlendCollection

    # region blender api calls

    @staticmethod
    def loadFromFile(file: str, collectionName: str) -> 'Character':
        """loads blender object from file"""
        raise NotImplementedError('not implemented')

    # endregion

    # region setters

    def __setFile(self, file: str) -> 'Character':
        self.__file = file
        return self

    def __setRig(self, rig: BlendCollection) -> 'Character':
        self.__rig = rig
        return self

    # endregion

    # region getters

    def getFile(self) -> str:
        return self.__file

    def getRig(self) -> BlendCollection:
        return self.__rig

    # endregion
