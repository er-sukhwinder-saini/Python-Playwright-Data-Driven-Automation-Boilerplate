from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page:Page):
        self.page = page
        self.userNameInput= page.get_by_role("textbox", name="Username")
        self.userPassword=page.get_by_role("textbox", name="Password")
        self.loginButton=page.get_by_role("button", name="Login")
        
    def enterUserName(self, userName: str):
        self.userNameInput.fill(userName)
        
    def enterPassword(self, password: str):
        self.userPassword.fill(password)
    
    def clickLogin(self):
         self.loginButton.click()