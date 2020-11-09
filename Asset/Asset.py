from bpy.types import Object as BlendObj
from bpy.types import Collection
from bpy.types import BlendData
import bpy


class Asset:
    """defines an project's assets

    attributes: file, obj
    """

    # init variables and set default values
    def __init__(self):
        """set default values"""

        self.__file: str
        self.__refObj: BlendObj

    # region blender api calls

    @staticmethod
    def loadFromFile(file: str, collectionName: str) -> 'Asset':
        """loads blender object from file"""

        # reads collections from blend file
        # closes all resources as needed
        with bpy.data.libraries.load(f'{file}.blend', link=True) as (data_from, data_to):
            # load the collection with the collection name specified
            data_to.collections = [collectionName]

        # todo: avoid hardcode
        collectionToAdd: Collection = data_to.collections[0]

        # creates a new empty, adds collection as it's instance collection
        # the empty contains a reference to all the collection's data
        refObj: BlendObj = bpy.data.objects.new(name=f"{collectionName}_Ref", object_data=None)
        refObj.instance_type = 'COLLECTION'
        refObj.instance_collection = collectionToAdd

        # load into root of scene
        # backlog: store and load into scene later
        bpy.context.scene.collection.objects.link(refObj)

        # init and return asset
        return Asset()\
            .__setFile(file=file)\
            .__setObj(refObj=refObj)

    # endregion

    # region setters

    def __setFile(self, file: str) -> 'Asset':
        self.__file = file
        return self

    def __setObj(self, refObj: BlendObj) -> 'Asset':
        self.__refObj = refObj
        return self

    # endregion

    # region getters

    def getFile(self) -> str:
        return self.__file

    def getObj(self) -> BlendObj:
        return self.__refObj

    # endregion
