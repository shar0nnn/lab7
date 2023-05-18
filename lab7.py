import requests


def main():
    # Отримати дані від користувача
    date = input("Введіть дату конвертації (у форматі YYYY-MM-DD): ")
    currency_code = input("Введіть код валюти для конвертації (наприклад, USD): ")

    # URL API для отримання даних конвертації
    url = f"https://api.exchangerate-api.com/v4/latest/{currency_code}"

    # Виконати запит до API та отримати результат
    response = requests.get(url)
    data = response.json()

    # Отримати назву валюти та конвертовану суму
    currency_name = data['base']
    converted_amount = data['rates']['UAH']

    # Вивести дані в консоль
    print(f"Назва валюти: {currency_name}")
    print(f"Дата конвертації: {date}")
    print(f"Конвертована сума: {converted_amount} UAH")


if __name__ == "__main__":
    main()
