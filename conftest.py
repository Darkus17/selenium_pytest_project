import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    """Добавляем опцию командной строки для выбора языка."""
    parser.addoption(
        '--language',
        action='store',
        default='en',
        help='Choose language: es, fr, ru, en, etc.'
    )


@pytest.fixture(scope="function")
def browser(request):
    """Фикстура для инициализации браузера с выбранным языком."""
    # Получаем значение языка из командной строки
    user_language = request.config.getoption("language")
    
    # Настраиваем опции Chrome
    options = Options()
    
    # Устанавливаем язык браузера
    options.add_experimental_option('prefs', {
        'intl.accept_languages': user_language,
    })
    
    # Инициализируем браузер с настройками
    print(f"\nStart browser with language: {user_language}")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)  # Неявное ожидание элементов
    
    # Передаем браузер в тест
    yield browser
    
    # Закрываем браузер после теста
    print("\nQuit browser...")
    browser.quit()


@pytest.fixture
def language(request):
    """Фикстура для получения языка теста."""
    return request.config.getoption("language")