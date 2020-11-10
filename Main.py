# Where things run

# region add main file for module imports

# backlog: clean up
# for blender's Python interpreter
import os
import sys

sys.path.append(os.getcwd())

# endregion

from Asset.Asset import Asset
from Charecter.Character import Character
from Scene.Scene import Scene
from Conf import BlendSettings
import bpy

asset: Asset = Asset.loadFromFile(f"{BlendSettings['BlendFiles']['Path']}Cup", 'Cup')
character: Character = Character.loadFromFile(f"{BlendSettings['BlendFiles']['Path']}Worm", 'Worm')

scene: Scene = Scene.setUp().addAsset(asset).addChar(character)
