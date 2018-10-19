#!/bin/python


def commonChild(s1, s2):
    c = []
    start = 0
    m_end = len(s1) - 1
    n_end = len(s2) - 1
    count = 0
    # trim off the matching items at the beginning
    while start <= m_end and start <= n_end and s1[start] == s2[start]:
        start = start + 1
        count += 1
    # trim off the matching items at the end
    while start <= m_end and start <= n_end and s1[m_end] == s2[n_end]:
        m_end -= 1
        n_end -= 1
        count += 1
    for _ in range(2):
        c.append([0] * (n_end + 2))
    for i in range(start, m_end + 1):
        c[1] = [0] * (n_end + 2)
        for j in range(start, n_end + 1):
            if s1[i] == s2[j]:
                c[1][j + 1] = c[0][j] + 1
            else:
                c[1][j + 1] = max(c[0][j + 1], c[1][j])
        c[0] = c[1]
    return c[1][n_end + 1] + count


if __name__ == '__main__':
    s1 = raw_input()
    s2 = raw_input()
    result = commonChild(s1, s2)
    print(str(result))
