# where things run

# region add main file for module imports

# backlog: clean up
# for blender's Python interpreter
import os
import sys

sys.path.append(os.getcwd())

# endregion

# region imports

from App.BuisnessLogic.Asset.Asset import Asset
from App.BuisnessLogic.Charecter.Character import Character
from App.BuisnessLogic.Scene.Scene import Scene
from Conf import BlendSettings

# endregion

# todo: add subprocess wrapper
# todo: add custom files
pathToBlends: str = BlendSettings['BlendFiles']['Path']

asset: Asset = Asset.loadFromFile(f"{pathToBlends}Cup", 'Cup')
character: Character = Character.loadFromFile(f"{pathToBlends}Worm", 'Worm')

scene: Scene = Scene.setUp().addAsset(asset).addChar(character)
