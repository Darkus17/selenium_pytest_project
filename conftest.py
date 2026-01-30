import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: en, ru, fr, etc.")
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        
        print(f"\nStart chrome browser with language: {user_language}")
        # Selenium Manager автоматически найдет и скачает нужный драйвер
        browser = webdriver.Chrome(options=options)
    
    elif browser_name == "firefox":
        from selenium.webdriver.firefox.options import Options as FirefoxOptions
        from selenium.webdriver.firefox.service import Service as FirefoxService
        
        options = FirefoxOptions()
        options.set_preference("intl.accept_languages", user_language)
        
        print(f"\nStart firefox browser with language: {user_language}")
        browser = webdriver.Firefox(options=options)
    
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    
    browser.implicitly_wait(5)
    yield browser
    
    print("\nQuit browser...")
    browser.quit()