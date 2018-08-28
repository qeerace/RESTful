from apistar import App, Route
from project.routes import routes
from project.models import Base
from apistar.commands import create_tables

settings = {
    "DATABASE": {
        "URL": "sqlite:///db.sqlite3",
            "METADATA": Base.metadata
}
}

list = [{"id": "59011597", "firstname": "Chatchanok", "lastname": "Wongsamang"},
        {"id": "59011598", "firstname": "Jiramate", "lastname": "Leingprom"},
        {"id": "59011599", "firstname": "Jirayu", "lastname": "Promsongwong"},
        {"id": "59011600", "firstname": "Kitpol", "lastname": "Tansakul"},
        {"id": "59011601", "firstname": "Nattamon", "lastname": "Sridam"},
        {"id": "59011602", "firstname": "Peeranat", "lastname": "Limpitaporn"},
        {"id": "59011604", "firstname": "Phison", "lastname": "Khankang"},
        {"id": "59011605", "firstname": "Thirawat", "lastname": "Rungrotchaiyaporn"}]

def get_student(std_id):
    for i in list:
        if std_id == i['id']:
            return(i)

def get_all():
    return(list)

routes = {
    Route('/id/{std_id}', 'GET', get_student),
    Route('/students', 'GET' , get_all)
}

app = App(routes=routes, settings=settings, commands=[create_tables])
