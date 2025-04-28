from ._anvil_designer import RowTemplate4Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server
from anvil import Notification, Label




class RowTemplate4(RowTemplate4Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.link_1.text=self.item['map']
    self.is_open=False

#     self.drop_down_1.items = [
#     {"text": "Select Org", "value": None},  # optional placeholder
#     {"text": "Org A", "value": "org_a"},
#     {"text": "Org B", "value": "org_b"},
# ]

    rows = [
    {
      "dropdown_1_items": ["A1", "A2", "A3"],
      "dropdown_2_items": ["B1", "B2"],
      "dropdown_3_items": ["C1", "C2", "C3", "C4"],
      "selected_1": "A2",
      "selected_2": "B1",
      "selected_3": "C3"
    },
    {
      "dropdown_1_items": ["A9", "A10"],
      "dropdown_2_items": ["B5", "B6"],
      "dropdown_3_items": ["C9"],
      "selected_1": "A10",
      "selected_2": "B6",
      "selected_3": "C9"
    }
  ]

    self.repeating_panel_1.items = rows

    self.data_grid_1.columns = [
      {"id": "mapping", "title": "MAPPING", "data_key": "mapping"},
      {"id": "debit_account", "title": "DEBIT ACCOUNT", "data_key": "debit_account"},
      {"id": "credit_account", "title": "CREDIT ACCOUNT", "data_key": "credit_account"},
      {"id": "cta", "title": "Action", "data_key": "cta"},
    ]

    # Any code you write here will run before the form opens.


  def edit_button_click(self, **event_args):

    Notification(
    "Edit successful",
    title="Success",
    style="success"
    ).show()

  def delete_button_click(self, **event_args):

    Notification(
    "Delete successful",
    title="Success",
    style="success"
    ).show()

  def link_1_click(self, **event_args):
    self.flow_panel_4.visible=not self.flow_panel_4.visible
    self.is_open=not self.is_open
    if self.is_open is True:
      self.link_1.icon='fa:angle-up'
    else:
      self.link_1.icon='fa:angle-down'

    
    
    
