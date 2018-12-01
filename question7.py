import csv
import random

random.seed(42)

def CreateQuestionKeys(num_questions):
    return ['Q' + str(i + 1) for i in range(num_questions)]

exam_responses = {}

with open('exam_samples.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)
    for row in csv_reader:
        student_id = row[0]
        student_answers = row[1:]
        num_questions = len(student_answers)
        answers = dict(zip(CreateQuestionKeys(num_questions), student_answers))
        exam_responses[student_id] = answers

num_questions = len(exam_responses[exam_responses.keys()[0]])
question_keys = CreateQuestionKeys(num_questions)
answers = [random.choice(['A','B','C','D']) for i in range(num_questions)]

true_answers = dict(zip(question_keys, answers))

def GradeExam(student_answers, true_answers):
    correct = []
    incorrect = []
    for question in true_answers.keys():
        if student_answers[question] == true_answers[question]:
            correct.append(question)
        else:
            incorrect.append(question)
    return {'correct':correct, 'incorrect':incorrect}

def ComputeCorrect(graded_exam):
    number_correct = len(graded_exam['correct'])
    number_total = num_questions
    return (100.0 * number_correct) / number_total

all_scores = []

for student_id in exam_responses.keys():
    student_answers = exam_responses[student_id]
    graded_exam = GradeExam(student_answers, true_answers)
    scores = ComputeCorrect(graded_exam)
    all_scores.append(scores)

def AvgScore(scores):
    total = 0
    for x in scores:
        total = total + x
    return (1.0 * total) / len(scores)

def MinScore(scores):
    small = scores[0]
    for x in scores:
        if x < small:
            small = x
    return small

def MaxScore(scores):
    large = scores[0]
    for x in scores:
        if x > large:
            large = x
    return large

def Variance(scores):
    square = 0
    for x in scores:
        square = square + (x - AvgScore(scores))**2
    return square / len(scores)

print("The Mean Score is: %s" %(AvgScore(all_scores)))
print("The Minimum Score is: %s" %(MinScore(all_scores)))
print("The Maximum Score is: %s" %(MaxScore(all_scores)))
print("The Variance is: %s" %(Variance(all_scores)))
