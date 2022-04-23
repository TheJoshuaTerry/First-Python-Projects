zybooks_grade = (91 + 91 + 91 + 91 + 91 + 91 + 91 + 91) / 8.0
outside_assignments = (85.5 + 85.5 + 85.5 + 85.5 + 85.5) / 5.0
tests = (94.5 + 94.5) / 2.0
overall_grade = (zybooks_grade * 0.5) + (outside_assignments * 0.3) + (tests * 0.2)

print('Intro to Programming Grade for Ted Ward')
print('Zybooks:',(zybooks_grade),'%')
print('Outside Assignments:', (outside_assignments),'%')
print('Tests:', (tests),'%')
print('Overall Grade:', (overall_grade), '%')