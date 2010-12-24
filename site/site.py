# -*- coding: utf-8 -*-
import os
import sys

from flask import Flask
from flask import render_template, redirect
from flaskext.markdown import Markdown
from flaskext.versioned import Versioned

from render import FileRenderer

app = Flask(__name__)
md = Markdown(app)
ver = Versioned(app)

PROJECTS = [
    {
        'name': u'Sektionscafé Baljan',
        'desc': u'new system using RFID and new web site, 10K lines of code',
        'url': u'http://baljan.org/',
    },
    {
        'name': u'Flask-Versioned',
        'desc': u'Flask app for static file versioning',
        'url': u'http://packages.python.org/Flask-Versioned/',
    },
    {
        'name': u'Spotify Plugin for Pidgin',
        'desc': u'showing the currently playing song',
        'url': u'http://github.com/pilt/spotify',
    },
    {
        'name': u'pycolordelta',
        'desc': u'python lib for generating palettes and computing color distances',
        'url': u'http://github.com/pilt/pycolordelta',
    },
]

EXPERIENCE = [
    {
        'name': u'Agama Technologies',
        'url': u'http://agama.tv/',
    },
    {
        'name': u'ESDK konsult AB',
        'url': u'http://esdg.se/',
    },
]

@app.route('/version-<version>/<path:static_file>')
def versioned_static(version, static_file):
    return redirect(static_file)

@app.route("/")
def index():
    rend = FileRenderer(app)

    sections = {}
    for section, items in [
            ('main', [
                ('expertise', '.md'),
                ('projects', '.md'),
                ('work-exp', '.md'),
            ]),
            ('alt', [
                ('hire', '.md'),
                ('contact', '.md'),
            ]),
            ('footer', [
                ('footer', '.md'),
            ]),
        ]:
        sections[section] = []
        for id, ext in items:
            sections[section].append({
                'id': id,
                'body': rend.by_extension(os.path.join('body', id + ext)),
            })

    return render_template(
        'index.html', 
        sections=sections,
    )

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
