from Asset.Asset import Asset


class AssetList:
    """defines an project's asset"""

    def __init__(self):
        self.__assets: list

    # region list methods

    def add(self, asset: Asset):
        """adds asset to list"""

        assets: list = self.getAssets()
        assets.append(asset)
        self.__setAssets(assets)

    # TODO: linear search
    def getByIndex(self, index: int) -> Asset:
        """gets asset by index"""

        # cycles through assets
        # returns asset matching index
        for asset in self.getAssets():
            if self.getAssets().index(asset) == index:
                return asset

    # endregion

    # region setters

    def __setAssets(self, assets: list) -> 'AssetList':
        self.__assets = assets
        return self

    # endregion

    # region getters

    def getAssets(self) -> list:
        return self.__assets

    # endregion
