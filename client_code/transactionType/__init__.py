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
    'sl_no': 1,
    'tran_name': 'Purchase',
    'tran_short_name': 'PUR',
    'tran_group_name': 'Sales',
    'is_active': True,
    # 'tran_subtypes': [
    #   {'tran_subtype_id': 101, 'name': 'Local'},
    #   {'tran_subtype_id': 102, 'name': 'International'},
    # ]
  }
]

     self.group_grid.columns = [
       {"id": "sl_no", "title": "Sl no", "data_key": "sl_no"},
       {"id": "tran_name", "title": "Transaction Name", "data_key": "tran_name"},
       {"id": "tran_short_name", "title": "Transaction Short Name", "data_key": "tran_short_name"},
       {"id": "tran_group_name", "title": "Transaction Short Name", "data_key": "tran_group_name"},
       {"id": "is_active", "title": "Active", "data_key": "is_active"},
       {"id": "cta", "title": "Action", "data_key": "cta"},
     ]
     self.group_repeating_panel.items=org_data


