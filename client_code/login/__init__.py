from ._anvil_designer import loginTemplate
from anvil import *
import anvil.server


class login(loginTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    

    # Any code you write here will run before the form opens.

    # def signup_with_form():
    #  d = SignupDialog()
   
    #  while True:
    #    if not alert(d, title="Sign Up", buttons=[("Sign Up", True, 'primary'), ("Cancel", False)]):
    #      return
       
    #    if d.password_box.text != d.password_repeat_box.text:
    #      d.signup_err_lbl.text = 'Passwords do not match. Try again.'
    #      d.signup_err_lbl.visible = True
    #      continue
       
    #    err = anvil.server.call('_do_signup', d.email_box.text, d.name_box.text, d.password_box.text)
    #    if err is not None:
    #      d.signup_err_lbl.text = err
    #      d.signup_err_lbl.visible = True
    #    else:
    #      alert(f"We have sent a confirmation email to {d.email_box.text}.\n\nCheck your email, and click on the link.")
    #      return