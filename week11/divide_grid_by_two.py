number_of_descendant = []
adjacent_list = []
visited = []


def solution(n, wires):
    global number_of_descendant
    global adjacent_list
    global visited

    number_of_descendant = [0 for _ in range(n + 1)]
    adjacent_list = [[] for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]

    # 인접리스트 생성
    for wire in wires:
        adjacent_list[wire[0]].append(wire[1])
        adjacent_list[wire[1]].append(wire[0])

    # root는 1번노드로 가정하고, DFS로 각 노드의 자손 노드의 개수를 찾는다
    number_of_descendant[1] = find_the_number_of_descendant(1, adjacent_list, number_of_descendant, visited)

    # 자손 노드의 개수에 1을 더하여 각 서브트리의 크기를 구한다.
    # 서브트리의 크기 = 자기 자신을 root로 하는 서브트리의 모든 노드의 개수
    size_of_subtrees = list(map(lambda x: x + 1, number_of_descendant[2:]))
    diff = list(map(lambda x: abs((n - 2 * x)), size_of_subtrees))
    answer = min(diff)

    return answer


# num번 노드의 자손노드의 개수를 찾는 함수
def find_the_number_of_descendant(num):
    global number_of_descendant
    global adjacent_list
    global visited

    visited[num] = True

    # 1번노드 이거나 leaf 노드가 아닌 경우
    if len(adjacent_list[num]) > 1 or num == 1:
        total = 0
        for idx in adjacent_list[num]:
            if not visited[idx]:
                number_of_descendant[idx] = find_the_number_of_descendant(idx)
                total += number_of_descendant[idx]
        number_of_descendant[num] = len(adjacent_list[num]) - 1 + total
        return number_of_descendant[num]
    # 1번 노드가 아니고 leaf노드인 경우
    else:
        return 0
