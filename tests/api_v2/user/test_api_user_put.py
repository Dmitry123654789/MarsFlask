from datetime import datetime

from requests import get, put

# Вывод всех работ до редактирования
print(get('http://localhost:8080/api/v2/users').json())

# Стандартное редактирование, все данные верны
print(put('http://localhost:8080/api/v2/users/4',
          json={'surname': 'test2',
                'name': 'test',
                'age': 999,
                'position': 'test',
                'speciality': 'test',
                'address': 'test',
                'city_from': 'test',
                'email': 'test@test.test',
                'modified_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                }).json())

# Не существующий id
print(put('http://localhost:8080/api/v2/users/454',
          json={'name': 'Sany', 'age': 4, 'modified_date': '2028-03-29 15:27:16'}).json())

# Id не является числом
print(put('http://localhost:8080/api/v2/users/a',
          json={'name': 'Sany', 'age': 5, 'modified_date': '2028-03-29 15:27:16'}).json())

# Есть ключи которых нет в данной таблице
print(put('http://localhost:8080/api/v2/users/5',
          json={'name': 'Sany', 'age': 3, 'modified_date': '2028-03-29 15:27:16', 'no_key': 999}).json())

# Запрос, когда никакие данные не передаются
print(put('http://localhost:8080/api/v2/users/1', json={}).json())

# вывод всех работ после редактирования
print(get('http://localhost:8080/api/v2/users').json())
