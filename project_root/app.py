from flask import Flask, request, redirect, url_for, render_template, jsonify
import os
from datetime import datetime

app = Flask(__name__)

# Mock database for events
events = []

@app.route('/')
def index():
    return render_template('index.html', greeting="Bem-vindo", username="Usuário")

@app.route('/get-events')
def get_events():
    return jsonify(events)

@app.route('/event-registration', methods=['GET', 'POST'])
def event_registration():
    if request.method == 'POST':
        title = request.form['title']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        description = request.form.get('description', '')

        new_event = {
            'title': title,
            'start_date': start_date,
            'end_date': end_date,
            'description': description
        }
        events.append(new_event)
        return redirect(url_for('event_registration'))

    return render_template('event_registration.html', events=events)

@app.route('/add_event', methods=['POST'])
def add_event():
    title = request.form['title']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    description = request.form.get('description', '')

    new_event = {
        'title': title,
        'start_date': start_date,
        'end_date': end_date,
        'description': description
    }
    events.append(new_event)
    return redirect(url_for('event_registration'))

if __name__ == '__main__':
    app.run(debug=True)
