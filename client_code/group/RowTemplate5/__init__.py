from ._anvil_designer import RowTemplate5Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RowTemplate5(RowTemplate5Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.radio_button_1.group_name=self.item['modules']
    self.radio_button_2.group_name=self.item['modules']

    if self.item['allow_access']:
      self.radio_button_1.selected = True
    else:
      self.radio_button_2.selected = True


    # Any code you write here will run before the form opens.
