import heapq
from mylib import StopWatch
from collections import defaultdict


class Node:
    def __init__(self):
        self.prev = []
        self.next = []


def recover(lines):
    nodes = defaultdict(Node)
    for line in lines:
        a, b, c = line.strip()
        nodes[a].next.append(b)
        nodes[b].next.append(c)
        nodes[b].prev.append(a)
        nodes[c].prev.append(b)

    head = [ch for ch in nodes if not nodes[ch].prev]
    heapq.heapify(head)

    res = ''
    while head:
        ch = heapq.heappop(head)
        res += ch
        for c in nodes[ch].next:
            p = nodes[c].prev
            p.remove(ch)
            if len(p) == 0:
                heapq.heappush(head, c)
    if len(res) < len(nodes):
        return 'SMTH WRONG'
    return res


def main():
    # n = int(input().strip())
    # lines = []
    # for _ in range(n):
    #     lines.append(input())
    with open('p079_keylog.txt') as f:
        lines = f.readlines()
    with StopWatch():
        print(recover(lines))


if __name__ == '__main__':
    main()
