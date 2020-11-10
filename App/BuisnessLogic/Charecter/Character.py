from bpy.types import Collection as BlendCollection
from bpy.types import Object as BlendObj
import bpy


class Character:
    """
    holds reference to blender character
    """

    # region blender api calls

    @staticmethod
    def loadFromFile(file: str, collectionName: str) -> 'Character':
        """
        loads blender object from file
        and inits character
        """

        # reads collections from blend file
        # closes all resources as needed
        # load the collection with the collection name specified
        with bpy.data.libraries.load(f'{file}.blend', link=True) as (data_from, data_to):
            data_to.collections = [collectionName]

        # todo: avoid hardcode
        collectionToAdd: BlendCollection = data_to.collections[0]

        # creates a new empty
        # creates linked copy of collection
        # links collection transform to empty
        refObj: BlendObj = bpy.data.objects.new(name=f"{collectionName}_Ref", object_data=None)
        refObj.instance_type = 'COLLECTION'
        refObj.instance_collection = collectionToAdd

        # load into root of scene
        # backlog: store and load into scene later
        bpy.context.scene.collection.objects.link(refObj)

        # select ref object and add library override
        bpy.context.view_layer.objects.active = refObj
        bpy.ops.object.make_override_library()

        # get collection with override and init character
        for collection in bpy.context.blend_data.collections:
            if collection.name_full == collectionName:
                return Character().__setFile(file).__setRig(collection)

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
