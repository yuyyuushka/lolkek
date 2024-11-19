import requests


# Задание 1

response = requests.get('https://catfact.ninja/fact?max_length=140')

if response.status_code == 200:
    print("Запрос успешно выполнен")
    print("Данные:", response.json()['fact'])
else:
    print("Ошибка при выполнении запроса:", response.status_code)


print('\nЗадание 2')
# Задание 2

def post_request(url, data):
    response = requests.post(url, json=data)
    return response

url = 'http://localhost:8000/api/data'
data = {
    "title": "foo",
}
response = post_request(url, data)

if response.status_code == 201:
    print("Данные успешно отправлены")
else:
    print("Ошибка при отправке данных:", response.status_code)

print('\nЗадание 3')
# Задание 3

def analyze(url):
    response = requests.get(url)
    print("Заголовки запроса:")
    for key, value in response.request.headers.items():
        print(f"{key}: {value}")

    print("\nЗаголовки ответа:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")

    print("\nТип содержимого:", response.headers.get('Content-Type'))
    print("Код ответа:", response.status_code)

analyze(url)

print('\nЗадание 4')
import requests

# Задание 4

def send_request(method, url, data=None, retries=3):
    for attempt in range(retries):
        try:
            if method == "GET":
                response = requests.get(url)
            elif method == "POST":
                response = requests.post(url, json=data)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as err:
            print(f"Ошибка: {err}")
            if attempt < retries - 1:
                print("Повторная попытка...")
            else:
                print("Превышено количество попыток")
                raise

local_url = "http://localhost:8000/api/data"

response = send_request("GET", local_url)
print("Ответ на GET-запрос:", response.json())

print('\nЗадание 5')
# Задание 5

def send_get_request_with_params(url, params):
    response = requests.get(url, params=params)
    return response

params = {
    "userId": 1
}
response = send_get_request_with_params(local_url, params)
print("Ответ на GET-запрос с параметрами:", response.json())

def send_post_request_with_data(url, data):
    response = requests.post(url, json=data)
    return response

data = {
    "title": "foo"
}
response = send_post_request_with_data(local_url, data)
print("Ответ на POST-запрос:", response.json())



