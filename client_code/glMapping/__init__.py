from ._anvil_designer import glMappingTemplate
from anvil import *
import anvil.server


class glMapping(glMappingTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    org_data = [
        {"sl_no":"1", "org_id":"123","group_name": "Retail", "group_short_name": "RET", "is_active": True},
        {"sl_no":"2", "org_id":"124","group_name": "Wholesale", "group_short_name": "WHO", "is_active": False}
    ]
    self.group_grid.columns = [
      {"id": "sl_no", "title": "Sl no", "data_key": "sl_no"},
      {"id": "org_id", "title": "Org id", "data_key": "org_id"},
      {"id": "group_name", "title": "Group name", "data_key": "group_name"},
      {"id": "group_short_name", "title": "Group short name", "data_key": "group_short_name"},
      {"id": "is_active", "title": "Active", "data_key": "is_active"},
      {"id": "cta", "title": "Action", "data_key": "cta"},
    ]
    self.group_repeating_panel.items=org_data
    # Any code you write here will run before the form opens.
