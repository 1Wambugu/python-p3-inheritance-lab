#!/usr/bin/env python
# lib/teacher.py
from user import User  # Import the User class
import random

class Teacher(User):
    knowledge = [
        "str is a data type in Python",
        "programming is hard, but it's worth it",
        "JavaScript async web request",
        "Python function call definition",
        "object-oriented teacher instance",
        "programming computers hacking learning terminal",
        "pipenv install pipenv shell",
        "pytest -x flag to fail fast",
    ]

    def teach(self):
        import random
        index = random.randint(0, len(self.knowledge) - 1)
        return self.knowledge[index]
