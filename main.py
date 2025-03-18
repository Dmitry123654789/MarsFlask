import datetime
import json
import random
from os import path

from flask import Flask, url_for, request, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

from data import db_session
from data.jobs import Jobs
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    username = StringField('id астранавта', validators=[DataRequired()])
    password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    username_captain = StringField('id капитана', validators=[DataRequired()])
    password_captain = PasswordField('Пароль капитана', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Доступ')


@app.route('/')
def name():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Миссия Колонизация Марса</h1>
                  </body>
                </html>
                """


@app.route('/index')
def index():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>И на Марсе будут яблони цвести!</h1>
                  </body>
                </html>"""


@app.route('/promotion')
def promotion():
    frazs = ["Человечество вырастает из детства.", "Человечеству мала одна планета.",
             "Мы сделаем обитаемыми безжизненные пока планеты.", "И начнем с Марса!", "Присоединяйся!"]
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    {" ".join(map(lambda x: f'<h3>{x}</h3>', frazs))}
                  </body>
                </html>"""


@app.route('/image_mars')
def image_mars():
    img = url_for('static', filename='img/mars.png')
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{}" alt="здесь должна была быть картинка, но не нашлась" height=300>
                    <a><br>Вот она какая, красивая планета.</a>
                  </body>
                </html>""".format(img)


@app.route('/promotion_image')
def promotion_image():
    img = url_for('static', filename='img/mars.png')
    style = url_for('static', filename='css/style.css')
    frazs = ["Человечество вырастает из детства.", "Человечеству мала одна планета.",
             "Мы сделаем обитаемыми безжизненные пока планеты.", "И начнем с Марса!", "Присоединяйся!"]
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                    <link href="{}" rel="stylesheet">
                  </head>
                  <body>
                    <h1 class="text-head-img">Жди нас, Марс!</h1>
                    <img src="{}" alt="здесь должна была быть картинка, но не нашлась" height=300>
                    <div class="alert alert-dark" role="alert">
                      {}
                    </div>
                    <div class="alert alert-success" role="alert">
                      {}
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      {}!
                    </div>
                    <div class="alert alert-warning" role="alert">
                      {}
                    </div>
                    <div class="alert alert-danger" role="alert">
                      {}
                    </div>
                  </body>
                </html>""".format(style, img, *frazs)


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                          <div class="center-text">
                            <h1>Анкета предендента</h1>
                            <h3>на участие в миссии</h3>
                          </div>
                            <div>
                                <form class="login-form" method="post">
                                    <input type="text" class="form-control" id="last-name" aria-describedby="emailHelp" placeholder="Введите фамилию" name="last_name">
                                    <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="educationSelect" class="set-pading">Какое у вас образование?</label>
                                        <select class="form-control" id="educationSelect" name="education">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                          <option>Без образования</option>
                                        </select>
                                    </div>
                                    
                                    <div class="set-pading">
                                        <a>Какие у Вас есть професии<br></a>
                                    </div>
                
                                    <div class="form-profes form-check">
                                        <div>
                                            <input type="checkbox" class="form-check-input" id="engineerRules">
                                            <label class="form-check-label" for="engineerRules">Инженер-исследователь</label>
                                        </div>
                                        <div>
                                            <input type="checkbox" class="form-check-input" id="builderRules">
                                            <label class="form-check-label" for="builderRules">Инженер-строитель</label>
                                        </div>
                                        <div>
                                            <input type="checkbox" class="form-check-input" id="pilotRules">
                                            <label class="form-check-label" for="pilotRules">Пилот</label>
                                        </div>
                                        <div>
                                            <input type="checkbox" class="form-check-input" id="meteoRules">
                                            <label class="form-check-label" for="meteoRules">Метеоролог</label>
                                        </div>
                                        <div>
                                            <input type="checkbox" class="form-check-input" id="lifeRules">
                                            <label class="form-check-label" for="lifeRules">Инженер по жизниобеспечению</label>
                                        </div>
                                        <div>
                                            <input type="checkbox" class="form-check-input" id="radioRules">
                                            <label class="form-check-label" for="radioRules">Инженер по рдиоцмонной защите</label>
                                        </div>
                                        <div>
                                            <input type="checkbox" class="form-check-input" id="vracRules">
                                            <label class="form-check-label" for="vracRules">Врач</label>
                                        </div>
                                        <div>
                                            <input type="checkbox" class="form-check-input" id="biologRules">
                                            <label class="form-check-label" for="biologRules">Экзобиолог</label>
                                        </div>
                                    </div>
                                    
                                    <div class="form-group">
                                        <label for="form-check" class="set-pading">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    
                                    <div class="form-group">
                                        <label for="about" class="set-pading">Почему вы хотите принять участие в миссии</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    
                                   <div class="set-pading">
                                      <a>Приложите фотографию<br></a>
                                      <label for="files" class="btn-get-file">Выберите файл</label>
                                      <input id="files" style="display:none;" type="file">
                                      <label for="files">Файл не выбран</label>
                                    </div>

                                    <div class="form-group form-check set-pading">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Мисия выполнена?</title>
                  </head>
                  <body>
                    <h1>Форма отправлена</h1>
                  </body>
                </html>
                """


@app.route('/choice/<planet_name>')
def choice_planet(planet_name):
    style = url_for('static', filename='css/style.css')
    planet = ['', ''] if planet_name.lower() == 'марс' else ['не', 'возможно']
    frazs = ["На ней много необходимых ресурсов;", f"На ней {planet[1]} есть вода и атмосфера;",
             f"На ней {planet[1]} есть магнитное поле;", "Наконец, она просто красива!"]
    return """<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                        <link href="{}" rel="stylesheet">
                      </head>
                      <body>
                        <h1 class="text-head-img">Мое предложение: {}</h1>
                        <h5>Эта планета {} близка к Земле;</h5>
                        <div class="alert alert-success" role="alert">
                          {}
                        </div>
                        <div class="alert alert-secondary" role="alert">
                          {}!
                        </div>
                        <div class="alert alert-warning" role="alert">
                          {}
                        </div>
                        <div class="alert alert-danger" role="alert">
                          {}
                        </div>
                      </body>
                    </html>""".format(style, planet_name.capitalize(), planet[0], *frazs)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def result(nickname, level, rating):
    return """<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                      </head>
                      <body>
                        <h1 class="text-head-img">Результаты отбора</h1>
                        <h5>Претендента на участие в миссии {}:</h5>
                        <div class="alert alert-success" role="alert">
                          <a>Поздравляем! Ваш рейтинг после {} этапа отбора</a>
                        </div>
                        
                        <div>
                            <a>Составляет {}!</a>
                        </div>
                        
                        <div class="alert alert-warning" role="alert">
                          <a>Желаем удачи</a>
                        </div>
                      </body>
                    </html>""".format(nickname, level, rating)


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    formats = ['.jpg', '.jpeg', '.png']
    if request.method == 'POST':
        if request.files['file'].filename and '.' + request.files['file'].filename.split('.')[-1] in formats:
            with open(f'static/img/load_photo.png', 'wb') as file:
                file.write(request.files['file'].read())

    style = url_for('static', filename='css/style.css')
    img = url_for('static', filename='img/load_photo.png')
    return '''<!doctype html>
                        <html lang="en">
                            <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{}" />
                                <title>Отбор астронавтов</title>
                            </head>
                            <body>
                                <div class="center-text">
                                    <h1>Загрузка фотографии</h1>
                                    <h3>для участия в миссии</h3>
                                </div>
                                <div>
                                    <form class="login-form" method="post" enctype="multipart/form-data">
                                        <div class="set-pading-photo-form">
                                            <a>Приложите фотографию<br></a>
                                            <label for="files" class="btn-get-file">Выберите файл</label>
                                            <input id="files" name="file" style="display:none;" onchange="this.form.submit()" type="file" accept="{}">
                                            <img src="{}" alt="Файл не выбран" class="img-load">
                                        </div>
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </form>
                                </div>
                            </body>
                        </html>'''.format(style, ', '.join(formats), img)


@app.route('/carousel')
def carousel():
    style = url_for('static', filename='css/style.css')
    frazs = '\n'.join([
        f'<div class="carousel-item"><img src="static/img/mars_peiz{x + 1}.png" class="d-block w-100" alt="Здесь должно быть фото("></div>'
        for x in range(1, 5)])
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Яндекс!</title>
                    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{}" />
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js" integrity="sha384-0pUGZvbkm6XF6gxjEnlmuGrJXVbNuzT9qBBavbLwCsOGabYfZo0T0to5eqruptLy" crossorigin="anonymous"></script>
                  </head>
                  <body>
                    <div class="center-text">
                        <h1>Пейзажи Марса</h1>
                    </div>
                    <div id="carouselExampleDark" class="carousel slide" width=100 style="width: 30%; margin: auto;">
                      <div class="carousel-inner">
                        <div class="carousel-item active">
                          <img src="static/img/mars_peiz1.png" class="d-block w-100" alt="здесь должна была быть картинка, но не нашлась">
                        </div>
                        {}
                      </div>
                      <button class="carousel-control-prev vissibal-button" type="button" data-bs-target="#carouselExampleDark" data-bs-slide="prev">
                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Previous</span>
                      </button>
                      <button class="carousel-control-next vissibal-button" type="button" data-bs-target="#carouselExampleDark" data-bs-slide="next">
                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Next</span>
                      </button>
                    </div>
                </body>
                </html>""".format(style, frazs)


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
    db_session.global_init("db/mars.db")
    set_users()
    set_jobs()
    # app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
