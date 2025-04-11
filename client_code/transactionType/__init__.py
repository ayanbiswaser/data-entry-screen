from ._anvil_designer import transactionTypeTemplate
from anvil import *
import anvil.server


class transactionType(transactionTypeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
     self.init_components(**properties)
     self.sidepanel_1.link_5.foreground = 'white'
     org_data = [
  {
    'created_at': '25-01-2025',
    'org_id':'001',
    'tran_name': 'Purchase',
    'tran_short_name': 'PUR',
    'tran_group_name': 'Sales',
    'is_active': True,
    'tran_subtypes': [
      {'tran_subtype_id': 101, 'name': 'Local'},
      {'tran_subtype_id': 102, 'name': 'International'},
    ]
  }
]
     self.data_grid_1.columns = [
       {"id": "created_at", "title": "created At", "data_key": "created_at"},
       {"id": "org_id", "title": "Org id", "data_key": "org_id"},
       {"id": "tran_name", "title": "Transaction Name", "data_key": "tran_name"},
       {"id": "tran_short_name", "title": "Transaction Short Name", "data_key": "tran_short_name"},
       {"id": "tran_group_name", "title": "Transaction Group Name", "data_key": "tran_group_name"},
       {"id": "is_active", "title": "Active", "data_key": "is_active"},
       {"id": "cta", "title": "Action", "data_key": "cta"},
       {"id": "view", "title": "Transaction Subtype", "data_key": "view"}
     ]
     self.repeating_panel_1.items=org_data

  def create_group_button_click(self, **event_args):
    open_form('transactionTypeForm',form_type="create", form_header = "Create Transaction")


