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
    load_cards(self)



    
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