def divide(s, num):
    chunks = [s[idx:idx + num] for idx in range(0, len(s), num)]

    return chunks


def compress(chunks):
    compressed = ""
    cnt = 1
    length = len(chunks)
    tmp = ""

    for idx in range(length - 1):
        if chunks[idx] == chunks[idx + 1]:
            cnt += 1
        else:
            compressed += str(cnt) + chunks[idx] if cnt > 1 else chunks[idx]
            cnt = 1
            tmp = chunks[idx + 1]

        if idx == length - 2:
            if cnt > 1:
                compressed += str(cnt) + chunks[idx]
            else:
                compressed += chunks[idx + 1]

    return compressed


def solution(s):
    minimum = 1001

    if len(s) == 1:
        return 1

    for num in range(1, int(len(s) / 2) + 1):
        chunks = divide(s, num)
        compressed_string = compress(chunks)
        #print(compressed_string)
        minimum = min(minimum, len(compressed_string))

    return minimum


if __name__ == "__main__":
    print(solution("aabbaccc"))
