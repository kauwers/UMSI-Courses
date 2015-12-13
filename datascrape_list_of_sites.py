import requests
from bs4 import BeautifulSoup

headers = {"user-agent": "Course prerequisite scraper, contact at email.com"}

def get_course_name(web_address):
    data = requests.get(web_address, headers=headers)
    soup = BeautifulSoup(data.text, "lxml")
    page_id = soup(id="page-title")[0].text
    return page_id.encode("utf-8")

def check_for_prereq(web_address):
    data = requests.get(web_address, headers=headers)
    soup = BeautifulSoup(data.text, "lxml")
    prereq_present = 0
    prereq_search = soup(string="SI 500")
    for i in prereq_search:
        prereq_present = prereq_present +1
    if prereq_present > 0:
        courses_found = get_course_name("https://www.si.umich.edu/programs/courses/620")
        print(courses_found)

prereq_found = check_for_prereq("https://www.si.umich.edu/programs/courses/620")


