import anvil.server
# routes.py
from routing.router import Route

class HomeType(Route):
    path = "/"
    form = "home"

class AdminLogin(Route):
    path = "/login"
    form = "login"


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

