from datetime import datetime

from .department import Department
from .hazard_category import HazardCategory
from .jobs import Jobs
from .users import User
from . import db_session


def set_users():
    user1 = User()
    user1.surname = "Scott"
    user1.name = "Ridley"
    user1.age = 21
    user1.position = "captain"
    user1.speciality = "research engineer"
    user1.address = "module_1"
    user1.email = "scott_chief@mars.org"
    user1.city_from = "Krasnodar"
    user1.hashed_password = "cap"
    user1.set_password(user1.hashed_password)
    user2 = User()

    user2.surname = "Александровый"
    user2.name = "Александр"
    user2.age = 45
    user2.position = "stzer"
    user2.speciality = "проектировщик сайтов"
    user2.address = "module_2"
    user2.email = "stzer@mars.org"
    user2.city_from = "Wellington"
    user2.hashed_password = "stzer"
    user2.set_password(user2.hashed_password)
    user3 = User()

    user3.surname = "Поддубный"
    user3.name = "Дмитрий"
    user3.age = 555
    user3.position = "prezident"
    user3.speciality = "no work"
    user3.address = "module_3"
    user3.email = "best_prezident@mars.org"
    user3.city_from = "Moscow"
    user3.hashed_password = "prezident"
    user3.set_password(user3.hashed_password)

    user4 = User()
    user4.surname = "None"
    user4.name = "None"
    user4.age = 999
    user4.position = "none"
    user4.speciality = "none"
    user4.address = "module_4"
    user4.email = "none@mars.org"
    user4.city_from = "Krasnodar"
    user4.hashed_password = "none"
    user4.set_password(user4.hashed_password)

    session = db_session.create_session()
    session.add(user1)
    session.add(user2)
    session.add(user3)
    session.add(user4)
    session.commit()


def set_hazard():
    hazard1 = HazardCategory()
    hazard1.category = "Сложные работы"

    hazard2 = HazardCategory()
    hazard2.category = "Легкие работы"

    hazard3 = HazardCategory()
    hazard3.category = "Ненужные работы"

    session = db_session.create_session()
    session.add(hazard1)
    session.add(hazard2)
    session.add(hazard3)
    session.commit()


def set_jobs():
    job = Jobs()
    job.team_leader = 2
    job.job = 'Deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.hazard_category_id = 3
    job.creator = 2
    job.start_date = datetime.now()
    job.is_finished = False

    job2 = Jobs()
    job2.team_leader = 1
    job2.job = 'Exploration of mineral resources'
    job2.work_size = 95
    job2.collaborators = '3'
    job2.hazard_category_id = 1
    job2.creator = 1
    job2.start_date = datetime.now()
    job2.is_finished = False

    job3 = Jobs()
    job3.team_leader = 2
    job3.job = 'Development of a management system'
    job3.work_size = 25
    job3.collaborators = '1'
    job3.hazard_category_id = 2
    job3.creator = 3
    job3.start_date = datetime.now()
    job3.is_finished = False

    session = db_session.create_session()
    session.add(job)
    session.add(job2)
    session.add(job3)
    session.commit()


def set_departments():
    department1 = Department()
    department1.title = 'Department of geological exploration'
    department1.members = '3, 4, 8'
    department1.email = 'geo@mars.org'
    department1.chief = 2

    department2 = Department()
    department2.title = 'Department of construction'
    department2.members = '4, 5, 6'
    department2.email = 'terra@mars.org'
    department2.chief = 1

    department3 = Department()
    department3.title = 'Department of biological research'
    department3.members = '7, 10, 11'
    department3.email = 'bio@mars.org'
    department3.chief = 3

    session = db_session.create_session()
    session.add(department1)
    session.add(department2)
    session.add(department3)
    session.commit()
