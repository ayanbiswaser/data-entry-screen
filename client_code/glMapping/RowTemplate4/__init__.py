from ._anvil_designer import RowTemplate4Template
from anvil import *
import anvil.server
from anvil import Notification, Label




class RowTemplate4(RowTemplate4Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  def edit_button_click(self, **event_args):
    print(self.item)

    Notification(
    "Edit successful",
    title="Success",
    style="success"
    ).show()
