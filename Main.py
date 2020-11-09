# Where things run

# region add main file for module imports

# backlog: clean up
# for blender's Python interpreter
import os
import sys

sys.path.append(os.getcwd())

# endregion

from Asset.Asset import Asset
from Conf import BlendSettings

asset: Asset = Asset.loadFromFile(f"{BlendSettings['BlendFiles']['Path']}Worm", 'Worm')
