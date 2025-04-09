from requests import delete, get

# Вывод всех работ до редактирования
print(get('http://localhost:8080/api/jobs').json())

# Стандартное удаление
print(delete('http://localhost:8080/api/jobs/5').json())

# Аргумент не передан
print(delete('http://localhost:8080/api/jobs/').json())

# Работы с таким id не существует
print(delete('http://localhost:8080/api/jobs/999').json())

# Неверный тип аргумента
print(delete('http://localhost:8080/api/jobs/q').json())

# вывод всех работ после редактирования
print(get('http://localhost:8080/api/jobs').json())
