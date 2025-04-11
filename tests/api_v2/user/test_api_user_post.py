from datetime import datetime

from requests import get, post

# Правильный запрос
print(post('http://localhost:8080/api/v2/users',
           json={'surname': 'test',
                 'name': 'test',
                 'age': 99,
                 'position': 'test',
                 'speciality': 'test',
                 'address': 'test',
                 'city_from': 'test',
                 'email': 'testt@test.test',
                 'modified_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                 }).json())


# Запрос в которром не хватает данных
print(post('http://localhost:8080/api/v2/users',
           json={'city_from': 'Плохая работа'
                 }).json())

# Запрос, когда передаются неизвестные параметры
print(post('http://localhost:8080/api/v2/users',
           json={'job': 'работа закончена',
                 'work_size': 15,
                 'collaborators': '1, 2',
                 'is_finished': False,
                 'team_leader': 1,
                 'creator': 1,
                 'start_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                 'end_date': '2026-10-20 23:20:05',
                 'none_param': 99
                 }).json())

# Запрос, когда никакие данные не передаются
print(post('http://localhost:8080/api/v2/users', json={}).json())

print(get('http://localhost:8080/api/v2/users').json())
