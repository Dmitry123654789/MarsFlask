from requests import get

# Получение всех пользователей
print(get('http://localhost:8080/api/v2/users').json())

# Получение одного пользователя
print(get('http://localhost:8080/api/v2/users/1').json())

# Несуществующий id
print(get('http://localhost:8080/api/v2/users/999').json())

# Неверный формат id
print(get('http://localhost:8080/api/v2/users/q').json())