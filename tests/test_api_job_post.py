from datetime import datetime

from requests import get, post

# Правильный запрос, когда работа не закончена
print(post('http://localhost:8080/api/jobs',
           json={'job': 'работа не закончена',
                 'work_size': 15,
                 'collaborators': '1, 2',
                 'is_finished': False,
                 'team_leader': 1,
                 'creator': 1,
                 'start_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                 }).json())

# Правильный запрос, когда работа закончена
print(post('http://localhost:8080/api/jobs',
           json={'job': 'работа закончена',
                 'work_size': 15,
                 'collaborators': '1, 2',
                 'is_finished': True,
                 'team_leader': 1,
                 'creator': 1,
                 'start_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                 'end_date': '2026-10-20 23:20:05'
                 }).json())

# Запрос в которром не хватает данных
print(post('http://localhost:8080/api/jobs',
           json={'job': 'Плохая работа'
                 }).json())

# Запрос, когда работа не закончена, но указана дата ее оканчания
print(post('http://localhost:8080/api/jobs',
           json={'job': 'работа закончена',
                 'work_size': 15,
                 'collaborators': '1, 2',
                 'is_finished': False,
                 'team_leader': 1,
                 'creator': 1,
                 'start_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                 'end_date': '2026-10-20 23:20:05'
                 }).json())

# Запрос, когда никакие данные не передаются
print(post('http://localhost:8080/api/jobs', json={}).json())

print(get('http://localhost:8080/api/jobs').json())
