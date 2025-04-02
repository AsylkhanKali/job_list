# app.py
from flask import Flask, render_template, request
from jobspy import scrape_jobs

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    search_term = request.form.get('search_term', '')
    jobs = scrape_jobs(
        site_names=["indeed", "linkedin", "zip_recruiter", "glassdoor"],
        search_term=search_term,
        location="United States",
        results_wanted=20
    )
    return render_template('results.html', jobs=jobs.to_dict('records'), search_term=search_term)

if __name__ == '__main__':
    app.run(port=7777)
