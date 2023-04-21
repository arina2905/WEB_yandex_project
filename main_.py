# -*- coding: utf8 -*-
from flask import Flask, redirect, render_template
from data import db_session
from data.user import User
from flask_login import LoginManager, login_user, login_required, logout_user
from data.forms import LoginForm
from data.forms import RegForm
from data.crosswords import Crosswords

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

cross = Crosswords()
cross.open_file()
cross.new_table()
cross.question_show()

login_manager = LoginManager()
login_manager.init_app(app)

db_session.global_init('db/users.db')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/index")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/reg', methods=['GET', 'POST'])
def reg():
    form = RegForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('registration.html', form=form,
                                   message='Пользователь с такой почтой уже существует!')
        user = User()
        user.name = form.name.data
        user.surname = form.surname.data
        user.age = form.age.data
        user.email = form.email.data
        user.password = form.password.data
        user.submit = form.submit.data
        #    db_sess.execute(user)
        db_sess.add(user)
        db_sess.commit()
    return render_template('registration.html', title='Регистрация', form=form)


def main():
    con = db_session.create_session()


@login_manager.user_loader(id)
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/index")
def index():
    return render_template('index.html', title='Crossword', crosswords=cross.tab)


@app.route('/')
def greeting():
    return render_template('greeting.html')


@app.route('/question')
def question():
    return render_template('enter_word.html', quest=cross.dictionary_words[str('1')][0],
                           checki=cross.dictionary_words[str('1')][1])


if __name__ == '__main__':
    app.run(port=8080, debug=True)
    main()
