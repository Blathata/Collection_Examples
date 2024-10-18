import os
LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def solution(node, idx):
    if not idx:
        node = node.next_item
    else:
        exec('node' + '.next_item' * idx + '=' + 'node' + '.next_item'*(idx+1))
    return node



def test():
    node3 = Node("Задача 4: Обследовать грунт в радиусе 3 м", None)
    node2 = Node("Задача 3: Измерить температуру атмосферы", node3)
    node1 = Node("Задача 2: Пробурить скважину глубиной 0.5 м", node2)
    node0 = Node("Задача 1: Фотосъёмка 360°", node1)

    new_head = solution(node0, 1)
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None


if __name__ == '__main__':
    test()