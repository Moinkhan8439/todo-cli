from os import system
import os.path
from tasks import task
from datetime import datetime

class Todo:
    date=""
    state=""
    file_name=""
    quote=""
    tasks={}

    def __init__(self):
        system('clear')
        self.state="dashboard"
        self.file=""
        self.date=datetime.today().strftime("%d-%m-%Y")

    def getQuote(self):
        """Returns quote from the utility module"""
        return self.quote

    def setState(self,state):
        self.state=state

    def getFile(self):
        return self.file_name

    def setQuote(self,quote):
        """Set quote taken from the utility module"""
        self.quote=quote

    def setFile(self,name):
        self.file_name=name

    def createTask(self,title,description,priority,date):
        if(self.tasks.get(date)==[]):
            self.tasks[date]=[]
        t=task(title=title,description=description,priority=priority)
        self.tasks[date].append(t)

    def setDate(self,date):
        self.date=date

    def getDate(self):
        return self.date
