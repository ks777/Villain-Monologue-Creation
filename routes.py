#<input type = '<type>' name = '<name>' />
#need cover page to link to program
#need page for input
#need page to use input and output answer
#need page to give incorrect answer

from flask import Flask, url_for, request, render_template
from app import app
import weaponcreation

#initial page/server-side interaction
@app.route('/')
def commence():
    createLink = "<a href = '" + url_for('create') + "'>Proceed to the Demonstrator Fabricator Generator!</a>"
    return """<html>
                <head>
                    <title>Welcome to the Villianous Sentence Creation Station!</title>
                </head>
                <body>
                    """ + createLink + """
                </body>
              </html>"""

#second page
@app.route('/GeneratePhrase', methods = ['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('CreateQuestion.html')
    elif request.method == 'POST':
        answer = request.form['title']
        finish = weaponcreation.creation_generation(answer)
        return render_template('CreatedQuestion.html', finish = finish)
    else:
        return "<h2>This is what you see when we create a page!</h2>"

    
