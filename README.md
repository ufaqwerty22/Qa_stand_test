### Описание

*Это мой пет-проект по тестированию для сайта qa-stand-login.inzhenerka.tech/login*  
  
### Затронутые виды тестирования
- Function testing
- API testing

### Запуск тестов
Клонирование репозитория в IDE
```
https://github.com/ufaqwerty22/Qa_stand_test.git
```
Установка зависимостей
```
pip install -r requirements.txt
```
Запуск тестов
```
pytest
```

<!-- - Клонируете репо в вашу IDE
- Прописать в консоль - **pip install -r requirements.txt**
- Для запуска всех тестов прописать в консоль - **pytest -v ./tests/** -->

### Основные библиотеки
- Requests
- Dotenv
- Pytest
- Playwright

### Решенные проблемы
*Зависимость API тестов*  
API Тесты работают изолированно друг от друга при помощи conftest.py. При каждом вызове функции создается пользователь и после выполнения функции он удаляется. Это позволяет тестам не зависеть от результатов других тестов.

*Импорт компонентов*  
Компоненты, находящиеся на несколько уровней выше текущего модуля можно импортировать без ошибок, используя`__init__.py` и `pythonpath = .`

### Структура проекта
```
Qa_stand_test/
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   └── logina_page.py
│
├── components/
│   ├── base_component.py
│   ├── info_component.py
│   └── login_component.py
│
├── controls/
│   ├── base_control.py
│   ├── button_control.py
│   ├── input_control.py
│   └── link_control.py
│   
├── tests/
│   ├── API/
│   │   ├── .env
│   │   ├── conftest.py
│   │   └── test_api_auth.py
│   │
│   └── Functional/
│       ├── .env
│       ├── conftest.py
│       └── test_login_page.py
│
├── .gitignore
├── README.md
├── pytest.ini
└── requirements.txt
```
