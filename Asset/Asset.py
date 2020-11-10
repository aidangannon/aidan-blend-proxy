from bpy.types import Object as BlendObj
from bpy.types import Collection
import bpy


class Asset:
    """
    holds reference to blender asset
    """

    # region blender api calls

    @staticmethod
    def loadFromFile(file: str, collectionName: str) -> 'Asset':
        """
        loads blender object from file
        and inits asset
        """

        # reads collections from blend file
        # closes all resources as needed
        # load the collection with the collection name specified
        with bpy.data.libraries.load(f'{file}.blend', link=True) as (data_from, data_to):
            data_to.collections = [collectionName]

        # todo: avoid hardcode
        collectionToAdd: Collection = data_to.collections[0]

        # creates a new empty
        # creates linked copy of collection
        # links collection transform to empty
        refObj: BlendObj = bpy.data.objects.new(name=f"{collectionName}_Ref", object_data=None)
        refObj.instance_type = 'COLLECTION'
        refObj.instance_collection = collectionToAdd

        # load into root of scene
        # backlog: store and load into scene later
        bpy.context.scene.collection.objects.link(refObj)

        # init and return asset
        return Asset().__setFile(file=file).__setObj(refObj=refObj)

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
