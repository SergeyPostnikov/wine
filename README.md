# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Установка
- выполните команды
```
git clone https://github.com/SergeyPostnikov/wine.git
cd wine
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
```
- создайте файл данных [wine.xlsx](https://github.com/SergeyPostnikov/wine/files/9786233/wine.xlsx)
или иной .xlsx файл с следующей структурой в директории проекта![struct](https://user-images.githubusercontent.com/60840361/195845091-0dadba16-fe4c-4f6e-b331-0ee6dd55f8e2.jpg)
- опционально можно конфигурировать расположение файла через .env - PATH_TO_STORAGE или command line interface скрипта main.py
причём настройки из переменных окружения будут иметь приоритет над парамеиром из cli.
## Запуск
выполните командy
```
python main.py
```
Перейдите на сайт по адресу [http://127.0.0.1:5000](http://127.0.0.1:5000/index.html).



