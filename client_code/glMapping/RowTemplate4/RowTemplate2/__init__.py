from ._anvil_designer import RowTemplate2Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server


class RowTemplate2(RowTemplate2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.drop_down_1.items = self.item['dropdown_1_items']
    self.drop_down_2.items = self.item['dropdown_2_items']
    self.drop_down_3.items = self.item['dropdown_3_items']

    self.drop_down_1.selected_value = self.item['selected_1']
    self.drop_down_2.selected_value = self.item['selected_2']
    self.drop_down_3.selected_value = self.item['selected_3']

    # Any code you write here will run before the form opens.
