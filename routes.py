#<input type = '<type>' name = '<name>' />
#need cover page to link to program
#need page for input
#need page to use input and output answer
#need page to give incorrect answer

from flask import Flask, url_for, request, render_template
from app import app

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
        return render_template('createdquestion.html')
    else:
        return "<h2>This is what you see when we create a page!</h2>"

#last page
@app.route('/finale/<title>')
def finale(title):
    if request.method == 'GET':
        return render_template('AnswerQuestion.html')
    elif request.method == 'POST':
        return 'This is the last page'      
    else:
        return '<h2>Invalid Request<h2>'
    
