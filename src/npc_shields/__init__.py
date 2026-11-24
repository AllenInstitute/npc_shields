from npc_shields.insertions import *
from npc_shields.shields import *

try:
    from npc_shields.widgets import *
except ImportError:  # ipywidgets is optional: pip install npc_shields[widgets]
    pass
