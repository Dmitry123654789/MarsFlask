from requests import delete, get

# Вывод всех работ до редактирования
print(get('http://localhost:8080/api/v2/users').json())

# Стандартное удаление
print(delete('http://localhost:8080/api/v2/users/4').json())

# Аргумент не передан
print(delete('http://localhost:8080/api/v2/users/').json())

# Работы с таким id не существует
print(delete('http://localhost:8080/api/v2/users/999').json())

# Неверный тип аргумента
print(delete('http://localhost:8080/api/v2/users/q').json())

# вывод всех работ после редактирования
print(get('http://localhost:8080/api/v2/users').json())
