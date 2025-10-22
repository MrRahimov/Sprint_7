# Sprint_7 API tests (Yandex Scooter)

## Запуск
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest -q

## Allure
pytest --alluredir=allure-results
allure generate allure-results -o allure-report --clean
