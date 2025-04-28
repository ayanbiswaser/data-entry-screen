from ._anvil_designer import Form2Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server


class Form2(Form2Template):
  def __init__(self,form_type=None, form_header=None, data=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.form_type = form_type
    self.label_5.text=form_header
    if form_type=='edit':
      org=[(data['org_id'])]
      self.drop_down_1.items=org
      self.drop_down_1.enabled=False
      self.text_box_1.text=data['group_name']
      self.text_box_2.text=data['group_short_name']
      self.check_box_1.checked=data['is_active']
    else:
      self.delete_button.visible= False
    # Any code you write here will run before the form opens.

  def cancel_button_click(self, **event_args):
    open_form('transactionGroup')
  def link_1_click(self, **event_args):
    self.flow_panel_2.visible = False
    self.flow_panel_8.visible = True
    self.flow_panel_4.visible = True
    self.flow_panel_6.visible = True
    self.flow_panel_7.visible = True

  def link_7_click(self, **event_args):
    self.flow_panel_8.visible=False
    self.flow_panel_2.visible = True
    self.flow_panel_4.visible = False
    self.flow_panel_6.visible = False
    self.flow_panel_7.visible = False

  def delete_button_click(self, **event_args):
     self.save_button.visible=False
     self.cancel_button.visible=False
     org_id = self.drop_down_1.selected_value
     group_name = self.text_box_1.text
    
     try:
      anvil.server.call('delete_transaction_group',org_id,group_name)      
      self.label_6.visible=False
     except Exception as e:
      self.label_6.visible=True
      self.label_6.text=str(e)

  def save_button_click(self, **event_args):
      # org_id = self.drop_down_1.selected_value
      org_id = "VIT"
      group_name = self.text_box_1.text
      group_short_name = self.text_box_2.text
      is_active = self.check_box_1.checked
      print(self.form_type)
      if self.form_type == 'edit':
        edit_saved = anvil.server.call('save_edit_transaction_group',org_id,group_name,group_short_name,is_active)
        if edit_saved["success"] is False: 
          self.label_6.text = edit_saved["message"]
          self.label_6.visible=True
        else:
          self.label_6.text = edit_saved["message"]
          self.label_6.visible=True
          self.button_4.visible = True
      else:
        edit_saved = anvil.server.call('save_create_transaction_group',org_id,group_name,group_short_name,is_active)
        if edit_saved["success"] is False: 
          self.label_6.text = edit_saved["message"]
          self.label_6.visible=True
        else:
          self.label_6.text = edit_saved["message"]
          self.label_6.visible=True
          self.button_4.visible = True
  def button_4_click(self, **event_args):
    open_form('transactionGroup')

