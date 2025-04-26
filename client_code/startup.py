import anvil.server
# In the startup Module
from routing.router import launch
from . import routes

launch()