import datetime
import json
import random
from os import path

from flask import Flask, request, render_template, redirect

from data import db_session
from data.jobs import Jobs
from data.users import User
from forms.login_form import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def name():
    return render_template('name.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/promotion')
def promotion():
    render_template('promotion.html')


@app.route('/image_mars')
def image_mars():
    return render_template('image_mars.html')


@app.route('/promotion_image')
def promotion_image():
    frazs = ["Человечество вырастает из детства.", "Человечеству мала одна планета.",
             "Мы сделаем обитаемыми безжизненные пока планеты.", "И начнем с Марса!", "Присоединяйся!"]
    return render_template('promotion_image.html', fraz_0=frazs[0], fraz_1=frazs[1], fraz_2=frazs[2], fraz_3=frazs[3],
                           fraz_4=frazs[4])


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return render_template('astronaut_selection_get.html')
    elif request.method == 'POST':
        return render_template('astronaut_selection_post.html')


@app.route('/choice/<planet_name>')
def choice_planet(planet_name):
    planet = ['', ''] if planet_name.lower() == 'марс' else ['не', 'возможно']
    frazs = ["На ней много необходимых ресурсов;", f"На ней {planet[1]} есть вода и атмосфера;",
             f"На ней {planet[1]} есть магнитное поле;", "Наконец, она просто красива!"]
    return render_template('choice_planet.html', planet_name=planet_name.capitalize(), planet=planet[0],
                           frazs_0=frazs[0], frazs_1=frazs[1], frazs_2=frazs[2], frazs_3=frazs[3])


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def result(nickname, level, rating):
    return render_template('results.html', nickname=nickname, level=level, rating=rating)


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    formats = ['.jpg', '.jpeg', '.png']
    if request.method == 'POST':
        if request.files['file'].filename and '.' + request.files['file'].filename.split('.')[-1] in formats:
            with open(f'static/img/load_photo.png', 'wb') as file:
                file.write(request.files['file'].read())

    return render_template('load_photo.html')


@app.route('/carousel')
def carousel():
    return render_template('carousel.html')


@app.route('/<title>')
@app.route('/index/<title>')
def index_tite(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def prof(prof):
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<spisk>')
def list_prof(spisk):
    profs = ['инженер - исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач', 'инженер по терраформированию',
             'климатолог', 'специалист по радиационной защите', 'астрогеолог', 'гляциолог', 'инженер жизнеобеспечения',
             'метеоролог', 'оператор марсохода', 'киберинженер', 'штурман', 'пилот дронов']
    return render_template('list_prof.html', professions=profs, list=spisk)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    dict_answer = {
        'title': 'Анкета',
        'surname': 'Watny',
        'name': 'Mark',
        'education': 'выше среднего',
        'profession': 'штурман марсохода',
        'sex': 'male',
        'motivation': 'Всегда мечтал застрять на Марсе!',
        'ready': True
    }
    return render_template('auto_answer.html', **dict_answer)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login_form.html', title='Авторизация', form=form)


@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/distribution')
def distribution():
    names = ['Ридли Скотт', 'Энди Уир', 'Марк Уотни', 'Венката Капур', 'Тедди Сандерс', 'Шон Бин']
    return render_template('distribution.html', names=names)


@app.route('/table/<sex>/<age>')
def table(sex, age):
    if age.isdigit():
        age = int(age)
    else:
        age = 0
    return render_template('table.html', sex=sex, age=age)


@app.route('/galery', methods=['POST', 'GET'])
def galery():
    formats = ['.jpg', '.jpeg', '.png']
    i = 0
    while path.exists(f'static/img/load_photo_galery{i}.png'):
        i += 1
    if request.method == 'POST':
        if request.files['file'].filename and '.' + request.files['file'].filename.split('.')[-1] in formats:
            request.files['file'].save(f'static/img/load_photo_galery{i}.png')
        else:
            i -= 1
    return render_template('galery.html', list_name=[f'img/load_photo_galery{x}.png' for x in range(1, i + 1)],
                           formats=', '.join(formats))


@app.route('/member')
def member():
    number_member = random.randint(0, 2)
    with open('templates/member.json', 'r', encoding='utf-8') as file:
        data = json.load(file)['crew_members'][number_member]
    return render_template('member.html', data=data)


def set_users():
    user1 = User()
    user1.surname = "Scott"
    user1.name = "Ridley"
    user1.age = 21
    user1.position = "captain"
    user1.speciality = "research engineer"
    user1.address = "module_1"
    user1.email = "scott_chief@mars.org"
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
    user4.hashed_password = "none"
    user4.set_password(user4.hashed_password)

    session = db_session.create_session()
    session.add(user1)
    session.add(user2)
    session.add(user3)
    session.add(user4)
    session.commit()


def set_jobs():
    job = Jobs()
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.start_date = datetime.datetime.now()
    job.is_finished = False

    session = db_session.create_session()
    session.add(job)
    session.commit()


def main():
    # db_session.global_init('db/mars.db')
    # set_users()
    # set_jobs()
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
