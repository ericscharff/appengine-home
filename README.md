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
Thu May  8 07:47:50 PM MDT 2025
