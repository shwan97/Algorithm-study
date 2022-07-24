def solution(n, wires):
    number_of_descendant = [0 for _ in range(n+1)]
    adjacent_list = [[] for _ in range(n+1)]
    visited = [False for _ in range(n+1)]

    # 인접리스트 생성
    for wire in wires:
        adjacent_list[wire[0]].append(wire[1])
        adjacent_list[wire[1]].append(wire[0])

    # root는 1번노드로 가정하고, DFS로 각 노드의 자손 노드의 개수를 찾는다
    number_of_descendant[1] = dfs(1, adjacent_list, number_of_descendant, visited)

    # 자손 노드의 개수에 1을 더하여 각 노드의 크기를 계산한다.
    # 노드의 크기 = 자기 자신을 root로 하는 서브트리의 모든 노드의 개수
    subtree = list(map(lambda x:x+1, number_of_descendant[2:]))
    absolute = list(map(lambda x: abs((n-2*x)), subtree))
    answer = min(absolute)

    return answer

def dfs(num, adjacent_list, number_of_descendent, visited):
    visited[num] = True
    if len(adjacent_list[num]) > 1 or num == 1:
        total = 0
        for idx in adjacent_list[num]:
            if not visited[idx]:
                number_of_descendent[idx] = dfs(idx, adjacent_list, number_of_descendent, visited)
                total += number_of_descendent[idx]
        number_of_descendent[num] = len(adjacent_list[num]) - 1 + total
        return number_of_descendent[num]
    else:
        return 0