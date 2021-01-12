class CafeOrderChecker:
    def is_first_come_first_served(self, take_out_orders, dine_in_orders, served_orders):
        if (len(take_out_orders) + len(dine_in_orders)) != len(served_orders):
            return False

        for order in served_orders:
            if take_out_orders and order == take_out_orders[0]:
                take_out_orders.pop(0)
            elif dine_in_orders and order == dine_in_orders[0]:
                dine_in_orders.pop(0)
            else:
                return False
        return True

    def is_first_come_first_served2(self, take_out_orders, dine_in_orders, served_orders):
        T=len(take_out_orders)
        D=len(dine_in_orders)

        if (T + D) != len(served_orders):
            return False

        t=0
        d=0
        for order in served_orders:
            if t<T and order == take_out_orders[t]:
                t+=1
            elif d<D and order == dine_in_orders[d]:
                d+=1
            else:
                return False
        return True


if __name__ == '__main__':
    init = CafeOrderChecker()
    print(init.is_first_come_first_served2([17, 8, 24], [12, 19, 2], [17, 8, 12, 19, 24, 2]))  # True
    print(init.is_first_come_first_served2([1, 3, 5], [2, 4, 6], [1, 2, 4, 6, 5, 3]))  # False
