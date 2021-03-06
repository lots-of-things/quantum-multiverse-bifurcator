#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#

from flask import Flask, render_template, request
import urllib.request

app = Flask(__name__)

app_data = {
    "name":         "Quantum Multiverse Bifurcator",
    "description":  "Flip a Quantum Coin, Make Decisions, Bifurcate the Multiverse",
    "author":       "Will Stedden",
    "html_title":   "Quantum Multiverse Bifurcator",
    "project_name": "Quantum Multiverse Bifurcator",
}


@app.route('/',methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            page = urllib.request.urlopen('http://150.203.48.55/RawBin.php', timeout=5)
            data = page.read().decode('utf-8')
            bit = data.split('"rng"')[1].split('<td>\n')[1].split('</td>')[0][0]
        except:
            with open('random_unseen.txt', 'r') as file:
                data = file.read()
            bit = data[0]
            with open('random_unseen.txt', 'w') as file:
                file.write(data[1:])

        result = request.form
        msg = []
        if bit=='0':
            msg.append(result['thingA'])
            msg.append(result['thingB'])
        else:
            msg.append(result['thingB'])
            msg.append(result['thingA'])
        return render_template("index.html",app_data=app_data, msg = msg)
    else:
        return render_template('index.html', app_data=app_data)

@app.route('/explain')
def explain():
    return render_template('explain.html', app_data=app_data)

def _write_random_to_file(iterations=10):
    data = ''
    for i in range(iterations):
        page = urllib.request.urlopen('http://150.203.48.55/RawBin.php', timeout=5)
        data = data+page.read().decode('utf-8').split('"rng"')[1].split('<td>\n')[1].split('</td>')[0]
    with open('random_unseen.txt', 'w') as file:
        file.write(data)

# ------- DEVELOPMENT CONFIG -------
if __name__ == '__main__':
    app.run(debug=True)