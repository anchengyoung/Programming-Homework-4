import csv

def CreateQuestionKeys(num_questions):
    return ['Q' + str(i + 1) for i in range(num_questions)]

exam_responses = {}
key = []

with open('exam_results.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)
    for row in csv_reader:
        student_id = row[0]
        student_answers = row[1:]
        num_questions = len(student_answers)
        answers = dict(zip(CreateQuestionKeys(num_questions), student_answers))
        exam_responses[student_id] = answers
        key.append(student_id)

unique = []
duplicate = []

for id in key:
    if id in unique:
        duplicate.append(id)
    else:
        unique.append(id)

print("Duplicated: %s" %duplicate)
