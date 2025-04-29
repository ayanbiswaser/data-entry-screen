# import anvil.server
# import anvil.google.auth, anvil.google.drive
# from anvil.google.drive import app_files
import anvil.users
# import anvil.tables as tables
# import anvil.tables.query as q
# from anvil.tables import app_tables




def Auth(authorization=False, roles=[]):
    authenticate = False
    authorized = False
    user = anvil.users.get_user()

    if user:
        authenticate = True
        if authorization:
            user_role = user.get('role', None)
            if user_role in roles:
                authorized = True

    return authenticate, authorized, user
