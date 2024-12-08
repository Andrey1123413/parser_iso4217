import requests 
from bs4 import BeautifulSoup 
import pandas as pd 

def get_currency_data(url):
    """Функция для получения данных о валютах с веб-страницы."""
    # Запрос к странице
    response = requests.get(url)
    response.raise_for_status()  # Проверка на успешный запрос

