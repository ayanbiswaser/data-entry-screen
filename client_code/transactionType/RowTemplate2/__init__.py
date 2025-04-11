from ._anvil_designer import RowTemplate2Template
from anvil import *
import anvil.server


class RowTemplate2(RowTemplate2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def edit_button_click(self, **event_args):
    print(self.item)
    open_form('transactionTypeForm',form_type="edit", form_header = "Edit Transaction", data=self.item)
    # Any code you write here will run before the form opens.
