from flask import Flask, render_template, request  #NEW IMPORT -- request
from forms import PrereqForm                    # NEW IMPORT LINE


app = Flask(__name__)    #This is creating a new Flask object

app.secret_key = 'WebDesign'

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def prereq_form():
  form = PrereqForm()
 
  if request.method == 'POST':
    return 'Form posted.'
 
  elif request.method == 'GET':
    return render_template('index.html', form=form)




@app.errorhandler(404)
def pageNotFound(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def pageNotFound(e):
    return render_template('500.html'), 500



if __name__ == '__main__':
    app.run(debug=True)     #debug=True is optional
