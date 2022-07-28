def solution(answers):
    answers_of_students = [[1, 2, 3, 4, 5],
                           [2, 1, 2, 3, 2, 4, 2, 5],
                           [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    len = [5, 8, 10]
    num_of_right_answers = [0 for _ in range(3)]

    for idx, answer in enumerate(answers):
        for stud_num in range(3):
            if answer == answers_of_students[stud_num][idx % len[stud_num]]:
                num_of_right_answers[stud_num] += 1

    maximum = max(num_of_right_answers)
    answer = []

    for idx in range(3):
        if num_of_right_answers[idx] == maximum:
            answer.append(idx)

    return answer

