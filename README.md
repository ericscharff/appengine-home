A simple Python application

deployed to Cloud Run

# Installation

* Create venv for python and activate it
  * `python3 -m venv venvdir`
  * `source venvdir/bin/activate`
* Install deploy and test requirements
  * `pip install -r requirements.txt`
  * `pip install -r requirements-test.txt`

# Useful commands

Run dev server:
        flask --app main run
Run tests:
        pytest
Run coverage:
        coverage run -m pytest
        coverage report
Run tests in Docker:
        docker build --target test .
Build and run container locally:
        docker build -t homeapp .
        docker run --rm -p 8080:8080 homeapp
Deploy manually:
        gcloud run deploy homeapp --source . --region us-central1 --allow-unauthenticated
