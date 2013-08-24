from BeautifulSoup import BeautifulSoup
import logging
import mechanize

logger = logging.getLogger(__name__)

class SchwabBrowser:
	LOGIN_URL = "https://www.schwab.com/"
	LOGIN_FORM_NAME = "SignonForm"
	LOGIN_USER_ID_FIELD = "SignonAccountNumber"
	LOGIN_PASSWORD_FIELD = "SignonPassword"

	def __init__(self, user_id, password):
		"""Create browser"""
		self.user_id, self.password = user_id, password
		self.mech_br = mechanize.Browser()
		self.mech_br.set_handle_robots(False)
		self.mech_br.set_handle_refresh(False)
		self.mech_br.addheaders = [('User-agent', 'Firefox')]

	def get_login_response(self):
		self.mech_br.open(self.LOGIN_URL)
		self.mech_br.select_form(name=self.LOGIN_FORM_NAME)
		self.mech_br[self.LOGIN_USER_ID_FIELD] = self.user_id
		self.mech_br[self.LOGIN_PASSWORD_FIELD] = self.password
		return self.mech_br.submit()

	def get_balance(self):
		"Return account balance as float."
		login_response = self.get_login_response()
		soup = BeautifulSoup(login_response.read())
		table = soup.find("table", {"id": "tblCharlesSchwabBank"})
		balance = float(table('tr')[1]('td')[2].span.text[1:])  # 2nd row, 3rd cell
		return balance

	def logout(self):
		raise NotImplementedError