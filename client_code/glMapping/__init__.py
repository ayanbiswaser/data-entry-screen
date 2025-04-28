from ._anvil_designer import glMappingTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server
from time import sleep


class glMapping(glMappingTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.text_box_1.height = "100px"
    self.text_box_1.border = "2px solid #ccc"

    



    data = [
        {"map":"1", "tran_type":"123","sub_type_id": "Retail", "priority": "RET", "is_active": True},
        {"map":"2", "tran_type":"124","sub_type_id": "Wholesale", "priority": "WHO", "is_active": False}
    ]
    self.group_grid.columns = [
      {"id": "map", "title": "MAP", "data_key": "map"},
      {"id": "tran_type", "title": "TRAN TYPE", "data_key": "tran_type"},
      {"id": "sub_type_id", "title": "SUB TYPE ID", "data_key": "sub_type_id"},
      {"id": "priority", "title": "PRIORITY", "data_key": "priority"},
      {"id": "is_active", "title": "Active", "data_key": "is_active"},
      {"id": "cta", "title": "Action", "data_key": "cta"},
    ]
    self.gl_mapping_repeating_panel.items=data
    # Any code you write here will run before the form opens.

  def create_group_button_click(self, **event_args):
    print("new map added")

  def search_click(self, **event_args):
    self.loading_indicator = anvil.server.loading_indicator()
    self.loading_indicator.start()
    sleep(5)
    self.loading_indicator.stop()
    

