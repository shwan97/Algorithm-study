def solution(n, wires):
    number_of_descendant = [0 for _ in range(n+1)]
    adjacent_list = [[] for _ in range(n+1)]
    visited = [False for _ in range(n+1)]

    # 인접리스트 생성
    for wire in wires:
        adjacent_list[wire[0]].append(wire[1])
        adjacent_list[wire[1]].append(wire[0])

    # 1번 노드를 root로 가정하고, DFS로 모든 노드를 탐색하여 각 노드의 자손노드의 개수를 구하기
    number_of_descendant[1] = dfs(1, adjacent_list, number_of_descendant, visited)

    # 자손노드의 개수에 자기 자신을 포함. 이 리스트의 idx번째 원소는 idx번 노드를 root로 하는
    # 서브트리의 모든 노드의 개수를 의미한다.
    number_of_node_in_subtree = list(map(lambda x:x+1, number_of_descendant[2:]))
    absolute = list(map(lambda x: abs((n-2*x)), number_of_node_in_subtree))
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

if __name__ == '__main__':
    n = 9
    wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
    print(solution(n, wires))