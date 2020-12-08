class task:
    """Individual Object of the task"""
    def __init__(self,title,description,priority):
        self.title=title
        self.description=description
        self.priority=priority

    def getTitle(self):
        return self.title
    
    def getDescription(self):
        return self.description

    def getPriority(self):
        return self.priority