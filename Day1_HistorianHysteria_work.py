"""original prompt: https://adventofcode.com/2024/day/1"""

working_list_1 = []
working_list_2 = []

with open(r"Day1_puzzleinput_list1", 'r') as file_object_1:
    working_list_1.extend([line.strip() for line in file_object_1.readlines()])
print(working_list_1[0])

with open(r"Day1_puzzleinput_list2", 'r') as file_object_2:
    working_list_2.extend([line.strip() for line in file_object_2.readlines()])
print(working_list_2[0])

list.sort(working_list_1)
list.sort(working_list_2)
print(working_list_1[0])
print(working_list_2[0])

working_list_3 = []

for x, y in zip(working_list_1, working_list_2):
    if int(y) - int(x) >=0:
        working_list_3.append(int(y) - int(x))
    else:
        working_list_3.append(-1*(int(y) - int(x)))
print(working_list_3[0])

with open(r"Day1_puzzleoutput1", 'w+') as file_object_3:
    for item in working_list_3:
        file_object_3.write(str(item) + '\n')

final_puzzle_answer = sum(working_list_3)
print(final_puzzle_answer)

""" Day 1, Part 1 is complete and verified correct on the Advent of Code website to unlock Part 2. Part 2's work starts below."""

set_1 = set(working_list_1)
set_2 = set(working_list_2)
intersection_1 = set_1.intersection(set_2)
print(intersection_1)
with open(r"Day1_puzzleoutput2", 'w+') as file_object_4:
    for item in intersection_1:
        file_object_4.write(str(item) + '\n')

dictionary_1 = { item:0 for item in intersection_1}

for item in working_list_2:
    if item in dictionary_1:
        dictionary_1[item] += 1

print(dictionary_1)

working_list_4 = []
for key, value in dictionary_1.items():
    similarity_score = int(key) * value
    working_list_4.append(similarity_score)

print(working_list_4)
final_puzzle_answer_2 = sum(working_list_4)
print(final_puzzle_answer_2)
