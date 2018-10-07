def organizingContainers(container):
    global n

    color_sum = [0] * n
    container_sum = []

    for row in container:
        container_sum.append(sum(row))
        for i in range(n):
            color_sum[i] += row[i]

    if (sorted(container_sum) == sorted(color_sum)):
        return "Possible"
    else:
        return "Impossible"


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        print(result)
