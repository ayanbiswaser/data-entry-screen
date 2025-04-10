from ._anvil_designer import transactionTypeTemplate
from anvil import *
import anvil.server


class transactionType(transactionTypeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.sidepanel_1.link_5.foreground = 'white'

