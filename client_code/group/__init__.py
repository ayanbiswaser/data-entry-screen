from ._anvil_designer import groupTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server
from anvil import Notification, Label


class group(groupTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    

    self.email_list=[]
    

    self.drop_down_data=['email1@example.com', 'email2@example.com', 'email3@example.com']
    self.drop_down_1.items=self.drop_down_data
    
    
    self.data_grid_1.columns = [
      {"id": "modules", "title": "MODULES", "data_key": "modules"},
      {"id": "allow_access", "title": "ALLOW ACCESS", "data_key": "allow_access"},
      {"id": "no_access", "title": "NO ACCESS", "data_key": "no_access"},
    ]
    # self.data_grid_2.columns = [
    #   {"id": "project_name", "title": "PROJECT NAME", "data_key": "project_name"},
    #   {"id": "allow_access", "title": "ALLOW ACCESS", "data_key": "allow_access"},
    #   {"id": "no_access", "title": "NO ACCESS", "data_key": "no_access"},
    # ]
    data_1 = [
      {"modules":"1", "allow_access":True,"no_access": False},
      {"modules":"2", "allow_access":False,"no_access": False}
    ]
    # data_2 = [
    #   {"project_name":"10", "allow_access":True,"no_access": False},
    #   {"project_name":"20", "allow_access":False,"no_access": False}
    # ]
    self.repeating_panel_1.items=data_1
    # self.repeating_panel_2.items=data_2
    
    load_cards(self)

  
  def button_2_click(self, **event_args):
    email=self.drop_down_1.selected_value
    if email is not None:
      self.email_list.append(email)
      show_user_list(self)
      self.drop_down_data.remove(email)
      self.drop_down_1.items=self.drop_down_data

        

      
    


  
def show_user_list(self):
  self.user_container.clear()
  
  for item in self.email_list:
    #group card
    card_panel = FlowPanel()
    card_panel.role = "group-email-card"
    
    # Create the cross icon button
    cross_button = Button(icon="fa:times")
    cross_button.role='filled'
    cross_button.tag=item
    # Optional: apply a role for styling

    # Create components for the card
    title_label = Label(text=item, bold=True)
    
    # Add components to the card panel
    card_panel.add_component(title_label, width='250px')
    card_panel.add_component(cross_button, width="20%")

    def btn_click(self, item, **event_args):
      self.drop_down_data.append(item)
      self.email_list.remove(item)
      self.drop_down_1.items=self.drop_down_data
      show_user_list(self)

    # cross_button.set_event_handler("click", btn_click)
    cross_button.set_event_handler("click", lambda sender, **event_args: btn_click(self,sender.tag))
    
    self.user_container.add_component(card_panel)

    
def load_cards(self):
  card_data = [
    {"title": "Card 1", "description": "Description for Card 1"},
    {"title": "Card 2", "description": "Description for Card 2"},
    {"title": "Card 3", "description": "Description for Card 3"},
  ]

  for item in card_data:
    # Create a Link component to make the card clickable
    card_link = Link()
    card_link.role = "group-card"  # Optional: apply a role for styling

    # Create components for the card
    title_label = Label(text=item["title"], bold=True)
    description_label = Label(text=item["description"])

    # Add components to the Link
    card_link.add_component(title_label)
    card_link.add_component(description_label)

    # Define the click event handler with a default argument to capture the current item
    def card_click(sender, item=item, **event_args):
      Notification(f"You clicked on: {item['title']}", timeout=3).show()
      self.side_panel.visible=True

      # Set the click event handler for the Link
    card_link.set_event_handler("click", card_click)

    # Add the Link to the container
    self.cards_container.add_component(card_link)