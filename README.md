A simple Python application

deployed to app engine

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
Deploy:
        gcloud app deploy
Wed Apr  2 08:14:14 AM MDT 2025
