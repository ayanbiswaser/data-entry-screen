from ._anvil_designer import transactionTypeTemplate
from anvil import *
import anvil.server


class transactionType(transactionTypeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
     self.init_components(**properties)
     self.sidepanel_1.link_5.foreground = 'white'
     data = [
        {"created_at":"1", "org_id":"123","tran_name": "Retail", "tran_short_name": "RET", "tran_group_name":"TG001", "is_active": True},
        {"created_at":"2", "org_id":"124","tran_name": "Wholesale", "tran_short_name": "WHO", "tran_group_name":"TG002", "is_active": False}
    ]

     self.data_grid_1.columns = [
       {"id": "created_at", "title": "created At", "data_key": "created_at"},
       {"id": "org_id", "title": "Org id", "data_key": "org_id"},
       {"id": "tran_name", "title": "Transaction Name", "data_key": "tran_name"},
       {"id": "tran_short_name", "title": "Transaction Short Name", "data_key": "tran_short_name"},
       {"id": "tran_group_name", "title": "Transaction Group Name", "data_key": "tran_group_name"},
       {"id": "is_active", "title": "Active", "data_key": "is_active"},
       {"id": "cta", "title": "Action", "data_key": "cta"},
     ]
     self.repeating_panel_1.items=data

  def create_type_button_click(self, **event_args):
    open_form('transactionTypeForm',form_type="create", form_header = "Create Transaction Type")


