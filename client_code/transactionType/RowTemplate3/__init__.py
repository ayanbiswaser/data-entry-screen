from ._anvil_designer import RowTemplate3Template
from anvil import *
import anvil.server


class RowTemplate3(RowTemplate3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  # def button_2_click(self, **event_args):
  #   self.flow_panel_1.visible= not self.flow_panel_1.visible 
  #   self.button_2.text='Close'
  #   self.label_1.text=self.item['tran_subtypes']

  def button_1_click(self, **event_args):
    open_form('transactionTypeForm',form_type="edit", form_header = "Edit Transaction Type", data=self.item)

    
    

