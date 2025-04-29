import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server
# routes.py
from routing.router import Route

class HomeType(Route):
    path = "/"
    form = "auth"

class AdminLogin(Route):
    path = "/login"
    form = "auth"
class CreateUser(Route):
    path = "/create-user"
    form = "createUser"


class TransactionTypeRoute(Route):
    path = "/transactionType"
    form = "transactionType"

class TransactionGroupRoute(Route):
    path = "/transactionGroup"
    form = "transactionGroup"
  
class GlMappingRoute(Route):
    path = "/glMapping"
    form = "glMapping"

class UserRoute(Route):
    path = "/user"
    form = "user"
  
class GroupRoute(Route):
    path = "/group"
    form = "group"

class ReportsRoute(Route):
    path = "/reports"
    form = "reports"

