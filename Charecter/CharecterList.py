from Charecter.Character import Character


class CharacterList:
    """defines an project's asset"""

    def __init__(self):
        self.__chars: list

    # region list methods

    def add(self, char: Character):
        """adds asset to list"""

        assets: list = self.getChars()
        assets.append(char)
        self.__setChars(assets)

    # TODO: linear search
    def getByIndex(self, index: int) -> Character:
        """gets asset by index"""

        # cycles through assets
        # returns asset matching index
        for char in self.getChars():
            if self.getChars().index(char) == index:
                return char
        raise IndexError('could not find charecter')

    # endregion

    # region setters

    def __setChars(self, chars: list) -> 'CharacterList':
        self.__chars = chars
        return self

    # endregion

    # region getters

    def getChars(self) -> list:
        return self.__chars

    # endregion
