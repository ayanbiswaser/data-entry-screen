from ._anvil_designer import adminLoginTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import Notification, Label
from ..utill import Auth
from routing.router import navigate



class adminLogin(adminLoginTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.image_1.remove_from_parent()
    self.link_2.add_component(self.image_1)

    if Auth():
      navigate(path='/group')
      
    


    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
     email=self.email.text
     password=self.password.text
     print(email)
     try:
        user = anvil.users.login_with_email(email, password)
        if user:
          Notification(
           f"{user['email']} you are login",
           title="Success",
           style="success"
           ).show()
        else:
          Notification(
           "Sign-up canceled.",
           title="Failed",
           style="danger"
           ).show()
     except Exception as e:
        Notification(
           f"{e}",
           title="Failed",
           style="danger"
           ).show()

  def link_2_click(self, **event_args):
   try:
        user = anvil.users.login_with_google()
        if user:
          Notification(
           f"{user['email']} you are login",
           title="Success",
           style="success"
           ).show()
        else:
          Notification(
           "Sign-up canceled.",
           title="Failed",
           style="danger"
           ).show()
   except Exception as e:
        Notification(
           e,
           title="Failed",
           style="danger"
           ).show()


