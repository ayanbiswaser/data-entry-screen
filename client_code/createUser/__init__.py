from ._anvil_designer import createUserTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server
from anvil import Notification, Label



class createUser(createUserTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def create_user_submit_click(self, **event_args):
    email = self.text_box_1.text
    password = self.text_box_2.text
    try:
        # user = anvil.users.signup_with_email(email, password)
        # user['role'] = 'user'
      res=anvil.server.call('set_user_role',email,password) 
      if res['success'] is True:
        Notification(
          "User account created successfully",
          title="Success",
          style="success"
         ).show()
      else:
         Notification(
          res['message'],
          title="Failed",
          style="danger"
         ).show()
    except  Exception as e:
        Notification(
          "Internal Error",
          title="Failed",
          style="danger"
         ).show()
        print(e)
