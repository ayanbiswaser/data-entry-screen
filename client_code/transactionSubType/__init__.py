from ._anvil_designer import transactionSubTypeTemplate
from anvil import *
import anvil.server


class transactionSubType(transactionSubTypeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.sidepanel_1.link_6.foreground = 'white'
