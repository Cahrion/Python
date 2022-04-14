# Question


class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def checkAnswer(self, answer):
     return self.answer == answer

# print(q1.checkAnswer("java"))
# print(q2.checkAnswer("python"))

# Quiz



class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0
    def getQuestion(self):
        return self.questions[self.questionIndex]
    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Soru {self.questionIndex+1}:{question.text}")
        a = 0
        for q in question.choices:
            a +=1
            print(f"{a} - {q}")

        answer = input("Cevap: ")
        self.guess(answer)
        self.loadQuest()

    def guess(self, answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score +=1
        self.questionIndex +=1
    def loadQuest(self):
        if len(self.questions) == self.questionIndex:
            self.showscore()
        else:
            self.displayProgress()
            self.displayQuestion()
    def showscore(self):
        print("Oyun bitti.")
        print(f"Skorunuz: {self.score}")

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber == totalQuestion:
            pass
        else:
            print(f" Question {questionNumber} of {totalQuestion} ".center(100,'*'))





q1 = Question(" en iyi programlama dili hangisidir? ", ['C#','python',"javascript","java",], "python")
q2 = Question(" en popüler programlama dili hangisidir? ", ['python',"javascript",'C#', "java"], "python")
q3 = Question(" en çok kazandıran programlama dili hangisidir? ", ['C#','python',"javascript","java"], "python")
q4 = Question(" en sevilen programlama dili hangisidir? ", ['C#','python',"javascript","java"], "python")
q5 = Question(" en kolay programlama dili hangisidir? ", ['C#','python',"javascript","java"], "python")


questions = [q1,q2,q3,q4,q5] # Soruları artırabilir ve burdan ek olarak koyarsan mantık aynı çalışır.

quiz = Quiz(questions)

quiz.loadQuest()