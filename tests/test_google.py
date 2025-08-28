import re
from playwright.sync_api import expect, Page

def test_google_search(page, context):
  
    page.wait_for_timeout(3000)
    page.goto('http://www.google.com/ncr')
    try:
        page.get_by_role('button', name = 'Accept all').click(timeout= 5000)
    except : 
        print('No pop up to accept')

        page.get_by_role('combobox', name = 'Search').fill('Python')
        page.wait_for_timeout(3000)
        page.keyboard.press('Enter')
        page.wait_for_timeout(3000)
        expect(page).to_have_title(re.compile('Playwright11', re.IGNORECASE))

