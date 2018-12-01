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

def DetailedReport(graded_exam):
    questions = CreateQuestionKeys(num_questions)
    for question in questions:
        if question in graded_exam['correct']:
            print(question)
        else:
            print(question + ' Wrong!')

for student_id in exam_responses.keys():
    student_answers = exam_responses[student_id]
    graded_exam = GradeExam(student_answers, true_answers)
    print("Student %s" % student_id)
    DetailedReport(graded_exam)
    pct_correct = ComputeCorrect(graded_exam)
    print("\t Student %s received a %.1f%%" % (student_id, pct_correct))
    if pct_correct < 50:
        print("\t Enjoy summer school!")
