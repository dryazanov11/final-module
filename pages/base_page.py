from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class BasePage():
	def __init__(self, browser, url, timeout=10):
		self.browser = browser
		self.url = url
	def open(self):
		self.browser.get(self.url)
	def is_element_present(self, find_element_by_css_selector, login_link_invalid):
		try:
			self.browser.find_element(find_element_by_css_selector, login_link_invalid)
		except (NoSuchElementException):
			return False
		return True