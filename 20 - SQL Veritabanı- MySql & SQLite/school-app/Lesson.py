class Lesson:
    def __init__(self,id,Name):
        if id is None:
            self.id = 0
        else:
            self.id = id
        
        self.name = Name

    @staticmethod
    def CreateLesson(obj):
        list= []

        if isinstance(obj, tuple):
            list.append(Lesson(obj[0],obj[1]))
        else:
            for i in obj:
               list.append(Lesson(i[0],i[1]))
        return list