import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import requests
from requests.auth import HTTPBasicAuth

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


@anvil.server.callable
def call_airflow():
  dag_id='simple_5min_python_operator_dag'
  airflow_host = "https://fast-pants-smell.loca.lt"  # Replace with your Airflow host if different
  username = "admin"
  password = "yRAVywkQ39zan4bM"
  endpoint = f"{airflow_host}/api/v1/dags/{dag_id}/dagRuns"
  headers = {
    'Content-Type': 'application/json'
  }
  data = {}
  try:
    response = requests.post(
      endpoint,
      auth=HTTPBasicAuth(username, password),
      headers=headers,
      json=data
    )
    response.raise_for_status()  # Raise an exception for HTTP errors
    print(response.json())
    # return response.json()
  except requests.exceptions.RequestException as e:
    print({'error from air':str(e)})
    # return {"error": str(e)}
  