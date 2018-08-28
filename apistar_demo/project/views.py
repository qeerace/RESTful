#def welcome(name=None):
#    if name is None:
#        return {'message': 'Welcome to API Star!'}
#    return {'message': 'Welcome to API Star, %s!' % name}

from apistar.backends import SQLAlchemy
from .models import Poll, Choice

def create_poll(db: SQLAlchemy, question: str):
    session = db.session_class()
    poll = Poll(question=question)
    session.add(poll)
    session.commit()
    return {'question': question}

def create_choices(db: SQLAlchemy, poll_id: int, choice_text: str):
    session = db.session_class()
    poll = session.query(Poll).get(poll_id)
    choice = Choice(poll=poll.id, choice_text=choice_text, votes=0)
    session.add(choice)
    session.commit()
    return {'choice_text': choice_text}










