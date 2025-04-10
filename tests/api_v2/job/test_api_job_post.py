from datetime import datetime

from requests import get, post

# Правильный запрос
print(post('http://localhost:8080/api/v2/jobs',
           json={'job': 'работа не закончена',
                 'work_size': 15,
                 'collaborators': '1, 2',
                 'is_finished': False,
                 'team_leader': 1,
                 'creator': 1,
                 'start_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                 'end_date': '2028-02-12 00:00:00',
                 'hazard_category_id': 1,
                 'heh': 'heh'
                 }).json())


# Запрос в которром не хватает данных
print(post('http://localhost:8080/api/v2/jobs',
           json={'job': 'Плохая работа'
                 }).json())

# Запрос, когда передается неизвестный параметр
print(post('http://localhost:8080/api/v2/jobs',
           json={'job': 'работа закончена',
                 'work_size': 15,
                 'collaborators': '1, 2',
                 'is_finished': False,
                 'team_leader': 1,
                 'creator': 1,
                 'start_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                 'end_date': '2026-10-20 23:20:05',
                 'hazard_category_id': '1',
                 'none_param': 99
                 }).json())

# Запрос, когда никакие данные не передаются
print(post('http://localhost:8080/api/v2/jobs', json={}).json())

print(get('http://localhost:8080/api/v2/jobs').json())
