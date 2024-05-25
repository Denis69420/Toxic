import os
from flask import Flask, render_template, request, redirect, url_for
from models import ServerConfig, Session
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
session = Session()

languages = {
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    
}

def get_guild_config(guild_id):
    config = session.query(ServerConfig).filter_by(guild_id=str(guild_id)).first()
    if not config:
        config = ServerConfig(guild_id=str(guild_id))
        session.add(config)
        session.commit()
    return config

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/config/<guild_id>')
def config(guild_id):
    config = get_guild_config(guild_id)
    return render_template('config.html', config=config, languages=languages)

@app.route('/update/<guild_id>', methods=['POST'])
def update(guild_id):
    config = get_guild_config(guild_id)
    config.prefix = request.form['prefix']
    config.welcome_message = request.form['welcome_message']
    config.language = request.form['language']
    session.commit()
    return redirect(url_for('config', guild_id=guild_id))

if __name__ == '__main__':
    app.run(debug=True)
