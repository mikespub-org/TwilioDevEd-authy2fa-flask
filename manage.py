#!/usr/bin/env python3
#
# See https://stackoverflow.com/questions/67538056/flask-script-from-flask-compat-import-text-type-modulenotfounderror-no-module
# Fix line 15 in venv/lib/python3.8/site-packages/flask_script/__init__.py
#
#from flask_script import Manager, Shell
from flask_migrate import Migrate

import os

from twofa import create_app, db
from twofa.models import User

app = create_app(os.getenv("FLASK_CONFIG") or "default")
migrate = Migrate(app, db)

#manager = Manager(app)

@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User)


#manager.add_command("shell", Shell(make_context=make_shell_context))

@app.cli.command()
#@manager.command
def test():
    """Run the unit tests."""
    import sys, unittest

    tests = unittest.TestLoader().discover("tests")
    result = unittest.TextTestRunner(verbosity=2).run(tests)

    if not result.wasSuccessful():
        sys.exit(1)


if __name__ == "__main__":
    print("Usage:\n./manage.py runserver --host 0.0.0.0 --port 8080\n")
    #app.run()
    #manager.run()
