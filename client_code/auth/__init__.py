from ._anvil_designer import authTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import plotly.graph_objects as go
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class auth(authTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.find_user()
    



  def find_user(self):
    user = anvil.users.get_user()
    if user is not None:
      self.login.visible=False
      self.signup.visible=False
      self.logout.visible=True

    else:
      self.login.visible=True
      self.signup.visible=True
      self.logout.visible=False
  def signup_click(self, **event_args):
    anvil.users.signup_with_form()
    self.find_user()

  def login_click(self, **event_args):
    anvil.users.login_with_form()
    self.find_user()

  def logout_click(self, **event_args):
    anvil.users.logout()
    self.find_user()

    
    

