import random
import csv

num_students = 150
num_questions = 26
mc_options = ['A','B','C','D']

def SimulateExam(num_questions, mc_options):
    answers = {}
    for question_number in range(num_questions):
        key = 'Q' + str(question_number + 1)
        answers[key] = random.choice(mc_options)
    return answers

exam_results = {}
for student in range(num_students):
    exam_results[student] = SimulateExam(num_questions, mc_options)

questions = ['Q' + str(i + 1) for i in range(num_questions)]
header = ['student'] + questions

with open('exam_results.csv', mode='wb') as exam_file:
    exam_writer = csv.writer(exam_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    exam_writer.writerow(header)
    for student in range(num_students):
        responses = exam_results[student]
        row_to_write = [student] + [responses[q] for q in questions]
        exam_writer.writerow(row_to_write)

#print(exam_results)
#print("Right exam_results length: " + str(len(exam_results.keys()) == num_students))
