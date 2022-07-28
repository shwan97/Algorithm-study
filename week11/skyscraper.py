# 기울기 계산
def find_slope(x1, x2, y1, y2):
    return (y1 - y2)/(x1 - x2)

num = int(input())
heights = list(map(int, input().split()))
heights.insert(0, 1)

#print(num)
#print(heights)

# i번째 빌딩이 j번째 빌딩을 볼 수 있는 경우 -> (i,j) = 1, (j,i) = 1
visible = [[0 for _ in range(num + 1)] for _ in range(num + 1)]

for cur in range(1, num + 1):
    for idx in range(1, num + 1):
        if cur != idx:
            low = min(idx, cur)
            high = max(idx, cur)
            slope = find_slope(low, high, heights[low], heights[high])

            # 두 빌딩 사이에 선분을 긋고 중간에 있는 빌딩을 지나거나 접하는지 확인
            # 즉, 각 빌딩의 x좌표에서의 선분의 y좌표와 빌딩의 높이를 비교
            for tmp in range(low + 1, high+1):
                if tmp == high:
                    visible[low][high] = 1
                    visible[high][low] = 1
                pos = slope * (tmp - low) + heights[low]
                if heights[tmp] >= pos:
                    break

answer = max(list(map(sum, visible)))
print(answer)


