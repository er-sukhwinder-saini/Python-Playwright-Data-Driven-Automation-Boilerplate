import re
from playwright.sync_api import Page, expect

def test_example(page: Page, context) -> None:

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Username").press("Tab")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("listitem").filter(has_text="Rockey user").locator("i").click()
    page.get_by_role("menuitem", name="Logout").click()
    expect(page.get_by_role("textbox", name="Password")).to_be_visible()
    expect(page.locator("#app")).to_contain_text("Password : admin1234")
    expect(page.locator("#app")).to_match_aria_snapshot("- paragraph: \"Username : Admin\"\n- paragraph: \"Password : admin123\"")
