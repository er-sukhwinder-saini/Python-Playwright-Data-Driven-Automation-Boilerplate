import pytest
from playwright.sync_api import sync_playwright

# fixture is used for reusable code that setup something
# before your test execution begins and clean it up
# when test execution completes

@pytest.fixture(scope='session')
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()
    


@pytest.fixture(scope="function")
def context(browser, request):
    """
    Create a fresh context per test with tracing enabled.
    Saves a unique trace file per test.
    """
    context = browser.new_context()

    # Start tracing
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield context   # test runs here

    # Create a unique filename: trace_<testname>.zip
    test_name = request.node.name  # pytest gives you the test function name
    trace_file = f"trace_{test_name}.zip"

    context.tracing.stop(path=r"E:\Web_Automation_Projects\PlayWright_Python\traces\trace_test.zip") 
    context.close()
