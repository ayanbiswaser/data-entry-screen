from ._anvil_designer import userTemplate
from anvil import *
import anvil.server


class user(userTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.sidepanel_1.link_9.foreground = 'white'
