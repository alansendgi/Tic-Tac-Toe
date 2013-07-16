"""
This is a functional test script copied from 
http://www.tdd-django-tutorial.com/tutorial/1/
"""
from django.test import LiveServerTestCase
from selenium import webdriver

class AdminTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_login_via_admin_site(self):
        # Gertrude opens her web browser, and goes to the admin page
        self.browser.get(self.live_server_url + '/admin/')

        # She sees the familiar 'Django administration' heading
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django administration', body.text)

        # TODO: this needs work
        self.fail('finish this test')
