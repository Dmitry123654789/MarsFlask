from datetime import datetime

from requests import get, put

# Вывод всех работ до редактирования
print(get('http://localhost:8080/api/jobs').json())

# Стандартное редактирование, все данные верны
print(put('http://localhost:8080/api/jobs/4',
          json={'job': 'работа закончена',
                'work_size': 15221,
                'collaborators': '2, 3',
                'is_finished': True,
                'team_leader': 2,
                'creator': 2,
                'start_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'end_date': '2328-32-12 30:00:00',
                'hazard_category_id': '2',
                }).json())

# Не существующий id
print(put('http://localhost:8080/api/jobs/454',
          json={'work_size': 1, 'team_leader': 3, 'start_date': '2028-03-29 15:27:16'}).json())

# Id не является числом
print(put('http://localhost:8080/api/jobs/a',
          json={'work_size': 1, 'creator': 3, 'start_date': '2028-03-29 15:27:16'}).json())

# Есть ключи которых нет в данной таблице
print(put('http://localhost:8080/api/jobs/5',
          json={'is_finished': 1, 'team_leader': 3, 'start_date': '2028-03-29 15:27:16', 'no_key': 999}).json())

# Запрос, когда никакие данные не передаются
print(put('http://localhost:8080/api/jobs/1', json={}).json())

# вывод всех работ после редактирования
print(get('http://localhost:8080/api/jobs').json())
