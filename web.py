from bs4 import BeautifulSoup
import requests as request

user_skill = input('Enter skill that you are looking for: ')
print(f'Filtering skills {user_skill}')

html_text = request.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')

jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

for job in jobs:
    job_published_date = job.find('span', class_='sim-posted').span.text

    if 'few' in job_published_date:
        company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
        skills = job.find('span', class_='srp-skills').text.replace(' ', '')
        more_info = job.header.h2.a['href']
        if user_skill in skills:
            print(f"Company Name: {company_name.strip()}")
            print(f"Required skills: {skills.strip()}")
            print(f"More info: {more_info}")
            print('----------------------------------------------------------------')

