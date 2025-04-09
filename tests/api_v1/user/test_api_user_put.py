from requests import get, put

# Вывод всех работ до редактирования
print(get('http://localhost:8080/api/users').json())

# Стандартное редактирование, все данные верны
print(put('http://localhost:8080/api/users/4',
          json={'name': 'Sany', 'age': 3, 'modified_date': '2028-03-29 15:27:16'}).json())

# Не существующий id
print(put('http://localhost:8080/api/users/454',
          json={'name': 'Sany', 'age': 3, 'modified_date': '2028-03-29 15:27:16'}).json())

# Id не является числом
print(put('http://localhost:8080/api/users/a',
          json={'name': 'Sany', 'age': 3, 'modified_date': '2028-03-29 15:27:16'}).json())

# Есть ключи которых нет в данной таблице
print(put('http://localhost:8080/api/users/5',
          json={'name': 'Sany', 'age': 3, 'modified_date': '2028-03-29 15:27:16', 'no_key': 999}).json())

# Запрос, когда никакие данные не передаются
print(put('http://localhost:8080/api/users/1', json={}).json())

# вывод всех работ после редактирования
print(get('http://localhost:8080/api/users').json())
