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

for student_id in exam_responses.keys():
    student_answers = exam_responses[student_id]
    graded_exam = GradeExam(student_answers, true_answers)
    print("Now grading Student %s" % student_id)
    print("Incorrect:")
    wrong = GradeExam(student_answers, true_answers)['incorrect']
    for x in wrong:
        print x
    pct_correct = ComputeCorrect(graded_exam)
    print("Student %s received a %.1f%%" % (student_id, pct_correct))
    print("")
