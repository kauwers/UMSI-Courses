from flask import Flask, render_template, request  #NEW IMPORT -- request
from forms import PrereqForm
import requests
from bs4 import BeautifulSoup 					# NEW IMPORT LINE


app = Flask(__name__)    #This is creating a new Flask object

app.secret_key = 'WebDesign'

headers = {"user-agent": "Course prerequisite scraper, contact at email.com"} #For BS Scraper

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def prereq_form():
  form = PrereqForm()
  
  if request.method == 'POST':
    PreReqChosen = form.prereq.data
    courses_found = {}
    page_id = {}

    def get_course_name(web_address):
      data = requests.get(web_address, headers=headers)
      soup = BeautifulSoup(data.text, "lxml")
      page_id = soup(id="page-title")[0].text

    def check_for_prereq(web_address):
      data = requests.get(web_address, headers=headers)
      soup = BeautifulSoup(data.text, "lxml")
      prereq_present = 0
      prereq_search = soup(string=PreReqChosen)
      for i in prereq_search:
        prereq_present = prereq_present +1
      if prereq_present > 0:
        courses_found = get_course_name("https://www.si.umich.edu/programs/courses/620")
    prereq_found = check_for_prereq("https://www.si.umich.edu/programs/courses/620")    
    render_template('index.html', form=form, message=page_id)
    

  elif request.method == 'GET':
    return render_template('index.html', form=form)




@app.errorhandler(404)
def pageNotFound(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def pageNotFound(e):
    return render_template('500.html'), 500



if __name__ == '__main__':
    app.run(debug=True)		#debug=True is optional
