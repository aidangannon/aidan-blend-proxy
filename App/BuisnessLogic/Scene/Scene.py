from bpy.types import Collection
from App.Asset.AssetList import AssetList
from App.Asset.Asset import Asset
from App.Charecter.CharecterList import CharacterList
from App.Charecter.Character import Character
import bpy


class Scene:
    """
    holds reference to blender scene
    """

    # region blender api calls

    # backlog: remove hard coding
    @staticmethod
    def setUp() -> 'Scene':
        """
        creates assets, characters collection
        inits scene
        """

        # creates collections for assets and scenes
        charColl = bpy.data.collections.new(name="Characters")
        assetsColl = bpy.data.collections.new(name="Assets")
        bpy.context.scene.collection.children.link(charColl)
        bpy.context.scene.collection.children.link(assetsColl)

        # inits scene
        return Scene()\
            .__setCharCollection(charColl)\
            .__setAssetCollection(assetsColl)\
            .__setChars(CharacterList())\
            .__setAssets(AssetList())

    def addChar(self, char: Character) -> 'Scene':
        """
        adds char to chars, and adds char to char collection
        unlinks char from scene
        """

        self.__setChars(self.getChars().add(char))
        self.getCharCollection().children.link(char.getRig())
        bpy.context.scene.collection.children.unlink(char.getRig())
        return self

    def addAsset(self, asset: Asset) -> 'Scene':
        """
        adds asset to assets, and adds asset to asset collection
        unlinks asset from scene
        """

        self.__setAssets(self.getAssets().add(asset))
        self.getAssetCollection().objects.link(asset.getObj())
        bpy.context.scene.collection.objects.unlink(asset.getObj())
        return self

    # endregion

    # region setters

    def __setChars(self, chars: CharacterList) -> 'Scene':
        self.__chars = chars
        return self

    def __setAssets(self, assets: AssetList) -> 'Scene':
        self.__assets = assets
        return self

    def __setCharCollection(self, charCollection: Collection) -> 'Scene':
        self.__charCollection = charCollection
        return self

    def __setAssetCollection(self, assetCollection: Collection) -> 'Scene':
        self.__assetCollection = assetCollection
        return self

    # endregion

    # region getters

    def getChars(self) -> CharacterList:
        return self.__chars

    def getAssets(self) -> AssetList:
        return self.__assets

    def getCharCollection(self) -> Collection:
        return self.__charCollection

    def getAssetCollection(self) -> Collection:
        return self.__assetCollection

    # endregion
