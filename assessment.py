"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
    1) Encapsulation: Everything about the object(attributes, methods) are kept 
        together within the Class.
    2) Abstraction: Hides the details that we don't need, outside user doesn't 
        need to know information about a method defined inside the class. 
    3) Polymorphism: We can make interchangeable types of one thing. Several 
        subclasses can inherit attributes and methods from a subclass, as well 
        as override said attributes and methods.
2. What is a class?
    A class is a blueprint from which we can create instances of the class 
    type, which take on its given attributes and methods. 
3. What is an instance attribute?
    An instance attribute is an attribute unique to the instance of the class, 
    given by whomever creates the instance.
4. What is a method?
    A method is a function defined in the class, that any 
    instance of that class can call. 
5. What is an instance in object orientation?
    An instance is the object instantiated from the class, which takes on 
    the attributes and methods of the class.
6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
    A class attribute is given by the class, and inherited by the instance. 
    An instance attribute is defined in the instance. For example, 
    all Hackbright students(class) are women(class attribute), 
    but only I(instance) am from New Jersey(instance attribute).

"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
    """A student taking an exam or quiz."""

    def __init__(self, first_name, last_name, address):
        """When a Student object is instantiated, a first_name, last_name
        and address are assigned as attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question(object):
    """A question on an exam or quiz."""

    def __init__(self, question, correct_answer):
        """When a Question object is instantiated, 
        a question and correct_answer are assigned as attributes."""
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        """Prompts the student to answer the question.

        Returns True if the answer is correct, False if incorrect.
        """

        user_answer = raw_input("%s > " % self.question)
        return user_answer == self.correct_answer

class Exam(object):
    """An exam taken by a student."""

    def __init__(self, name):
        """When an Exam object is instantiated, it is assigned the attributes
        name and list of questions."""
        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        """Adds question object to list of questions.

        The question objects include the attributes question and correct_answer.
        """
        new_question = Question(question, correct_answer)
        self.questions.append(new_question)

    def administer(self):
        """Administers the exam.

        For every question object in the list of questions, the ask_and_evaluate
        method from the Question Class is run, and if the output is True, the
        score is incremented by 1 point. The total score is then returned.
        """
        score = 0

        i = 0
        for i in range(len(self.questions)):            
            if self.questions[i].ask_and_evaluate():
                score += 1
            i += 1

        return score

class Quiz(Exam):
    """The Quiz Class is a subclass of the Exam Class."""

    def __init__(self, name):
        """When a Quiz object is instantiated, it is assigned the same attributes
        as an Exam: name and list of questions.
        """
        super(Quiz, self).__init__(name)

    def add_question(self, question, correct_answer):
        """Adds question object to list of questions. 

        The same add_question method is used from the superclass Exam.
        """
        super(Quiz, self).add_question(question, correct_answer)

    def administer(self):
        """Administers the quiz.

        Similar to the Exam administer method, except the total score is 
        not returned. Instead, a percentage is calculated. If the precentage
        is over 50%, administer() returns True and the student passes. 
        Otherwise, administer() returns False and the student Fails.
        """
        score = 0

        i = 0
        for i in range(len(self.questions)):            
            if self.questions[i].ask_and_evaluate():
                score += 1
            i += 1

        return score/i > 0.5

def take_test(exam, student):
    """Function that returns the student score.

    Takes exam and student objects as arguments, runs the administer() method
    from the Exam Class or Quiz subclass, and returns the resulting score.
    Note that exam is the name of the instance, and could be an instance of
    a Quiz as well.
    """

    student.score = exam.administer()
    return student.score

def example():
    """Function that tests the Classes, methods and functions in this 
    assessment.py for an Exam example"""

    exam = Exam("Midterm")
    
    exam.add_question("Who makes the dopest chains?", "Markov")
    exam.add_question("What is Ada's last name?", "Lovelace")
    exam.add_question("How about Grace's?", "Hopper")

    student = Student("Nicole", "Negri", "SF")

    take_test(exam, student)

def quiz_example():
    """Function that tests the Classes, methods and functions in this 
    assessment.py for a Quiz example"""

    quiz = Quiz("Pop Quiz")
    
    quiz.add_question("How many houses in our cohort?", "Four")
    quiz.add_question("Which is the best house?", "Gryffindor")

    student = Student("Nicole", "Negri", "SF")

    take_test(quiz, student)

example()
quiz_example()
