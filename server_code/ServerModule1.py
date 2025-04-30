import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

@anvil.server.callable
def set_user_role(email, password):
  try:
    user=anvil.users.signup_with_email(email, password)
    user['role'] = 'user'
    return {'success':True}
  except anvil.users.PasswordNotAcceptable:
    return {'success':False, "message": "The password provided is not acceptable."}
  except anvil.users.UserExists:
    return {'success':False, "message": "A user with this email already exists."}
  except Exception as e:
    return {'success':False, 'message':e}


@anvil.server.callable
def admin_login(email, password):
  try:
    user=anvil.users.login_with_email(email, password)
    return {'success':True}
  except anvil.users.PasswordNotAcceptable:
    return {'success':False, "message": "The password provided is not acceptable."}
  except anvil.users.UserExists:
    return {'success':False, "message": "A user with this email already exists."}
  except Exception as e:
    return {'success':False, 'message':e}