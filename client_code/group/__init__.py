from ._anvil_designer import groupTemplate
from anvil import *
import anvil.server

class group(groupTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.sidepanel_1.link_10.foreground = 'white'
