import re
from playwright.sync_api import Page, expect
from pages.Home_Page import HomePage
from pages.Login_Page import LoginPage


def test_login(page: Page, context) ->None:
   
    login_page=LoginPage(page)
    home_Page=HomePage(page)

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")    

    login_page.enterUserName('Admin')
    login_page.enterPassword('admin123')
    login_page.clickLogin
    home_Page.upgradeButton
    home_Page.clickDashboard
    home_Page.clickPerformance
