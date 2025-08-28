from playwright.sync_api import Page

class HomePage:
    
    def __init__(self, page :Page):
        self.page = page
        self.upgradeButton = page.get_by_role("button", name="Upgrade")
        self.performanceLink = page.get_by_role("link", name="Performance")
        self.dashboard_link = page.get_by_role("link", name="Dashboard")

    def is_upgrade_button_Visible(self):
        return self.upgradeButton.is_visible
      
    def clickPerformance(self):
        self.performanceLink.click
    
    def clickDashboard(self):
        self.dashboard_link.click