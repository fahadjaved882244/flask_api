from selenium import webdriver
import unittest

class TestUserRegistration(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get('http://localhost:8000/register')

    def test_registration(self):
        username_input = self.browser.find_element_by_name('username')
        password_input = self.browser.find_element_by_name('password')
        email_input = self.browser.find_element_by_name('email')

        username_input.send_keys('newuser')
        password_input.send_keys('password123')
        email_input.send_keys('user@example.com')

        submit_button = self.browser.find_element_by_id('submit')
        submit_button.click()

        # Assert redirection to a new page, profile page, or confirmation message
        self.assertIn('Thank you for registering', self.browser.page_source)

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()
