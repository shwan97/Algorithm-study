def solution(record):
    id_to_nickname = {}
    result = []
    answer = []

    for log in record:
        chunks = log.split()
        if chunks[0] == "Enter":
            id = chunks[1]
            nickname = chunks[2]

            # 닉네임 변경
            id_to_nickname[id] = nickname

            # Enter log
            result.append([id, 0])
        elif chunks[0] == "Leave":
            # Leave log
            result.append([chunks[1], 1])
        else:  # "Change"
            id = chunks[1]
            nickname = chunks[2]

            # 닉네임 변경
            id_to_nickname[id] = nickname

    for elem in result:
        # print(id_to_nickname.get(elem[0]))
        statement = id_to_nickname.get(elem[0]) + "님이 " + ("들어왔습니다." if elem[1] == 0 else "나갔습니다.")
        answer.append(statement)

    return answer