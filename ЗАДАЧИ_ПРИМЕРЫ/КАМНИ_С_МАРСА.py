"""Сортирует список, сравнивет элементы списка, выводит подходящие по размеру элементы
quantity_orders и delivered_samples, необязательные, в задании нужны были, можно len()
"""

def quantity_orders(quantity_orders: int, 
                    orders_sample_weight: list[int], 
                    delivered_samples: int, 
                    weight_delivery_samples: list[int]
                    ):
    """_summary_

    Args:
        quantity_orders (int): количество заказов от музеев и лабораторий
        orders_sample_weight (list[int]): минимальный вес образца
        delivered_samples (int): количество образцов, доставленных с Марса
        weight_delivery_samples (list[int]): вес каждого из доставленных образцов

    Returns:
        int:  количество заказчиков, требования которых удовлетворены.
    """


    orders_sample_weight.sort()
    weight_delivery_samples.sort()
    orders: int = 0
    samples: int = 0

    while orders < quantity_orders and samples < delivered_samples:
        if weight_delivery_samples[samples] >= orders_sample_weight[orders]:
            orders += 1
        samples += 1

    return orders


if __name__ == '__main__':
    assert quantity_orders(
        10,
        [8, 5, 5, 8, 6, 9, 8, 2, 4, 7],
        8,
        [9, 8, 1, 1, 1, 5, 10, 8]
    ) == 5

    assert quantity_orders(
        10,
        [5, 10, 1, 5, 4, 4, 10, 1, 5, 10],
        9,
        [4, 4, 8, 5, 9, 6, 1, 7, 4]
    ) == 7 

    assert quantity_orders(
        1,
        [4],
        8,
        [1, 4, 7, 10, 2, 2, 7, 8]
    ) == 1

    assert quantity_orders(
        10,
        [8, 5, 5, 8, 6, 9, 8, 2, 4, 7],
        8,
        [9, 8, 1, 1, 1, 5, 10, 8]
    ) == 5
    