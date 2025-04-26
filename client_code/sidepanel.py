from ._anvil_designer import sidepanelTemplate
from anvil import *
import anvil.server
from routing.router import navigate


class sidepanel(sidepanelTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

#configuration toggle menu

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
  
  #Security toggle menu
  def link_2_click(self, **event_args):
    self.flow_panel_3.visible=False
    self.flow_panel_10.visible = True
    self.flow_panel_1.visible = True
    self.flow_panel_9.visible = True
    
  def link_8_click(self, **event_args):
    self.flow_panel_3.visible = True
    self.flow_panel_10.visible = False
    self.flow_panel_1.visible = False
    self.flow_panel_9.visible = False

  #navigations
  def link_5_click(self, **event_args):
    navigate(path='transactionType')
  def link_4_click(self, **event_args):
    navigate(path='transactionGroup')
  def link_6_click(self, **event_args):
    navigate(path='glMapping')
  def link_9_click(self, **event_args):
    navigate(path="user")
  def link_10_click(self, **event_args):
    navigate(path='group')
  def link_3_click(self, **event_args):
    navigate(path='reports')
