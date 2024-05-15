from DBHandler import *
class Task:
    def __init__(self,title,desc,date,time):
          self.title = title
          self.desc = desc
          self.date = date
          self.time = time
    def __str__(self):
        return (self.title+":"+self.desc+":"+self.date+":"+self.time)

    def insertTask(self):
        print(self.__str__())

    def getTask(self):
        print(self.__str__())
'''if __name__ == '__main__':
    t = Task("Lecture Notes","Take down lecture notes for JAVA","16-07-2023","10:00:00 PM")
    db = DBHandler()
    db.insertTask(t)
    #print(t)'''