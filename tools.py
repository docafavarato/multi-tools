class multitools:
    class lists:
        def ascending(_list: list):
            ascending_list = list()
            for i in range(len(_list)):
                ascending_list.append(min(_list))
                _list.remove(min(_list))
            return ascending_list
        
        def descending(_list: list):
            descending_list = list()
            for i in range(len(_list)):
                descending_list.append(max(_list))
                _list.remove(max(_list))
            return descending_list
        
        def min(_list: list):
            return min(_list)
        
        def max(_list: list):
            return max(_list)
        
        def sum(_list: list):
            total = 0
            for item in _list:
                try:
                    total += item
                except TypeError:
                    pass
            return total

        def subtraction(_list: list):
            total = 0
            for item in _list:
                try:
                    total -= item
                except TypeError:
                    pass
            return total

        def product(_list: list):
            total = 1
            for item in _list:
                try:
                    total *= int(item)
                except TypeError:
                    pass
                except ValueError:
                    pass
            return total
        
        def intersection(_list: list, _list_: list) -> list:
            intersection_list = list()
            for item in _list:
                if item in _list_:
                    intersection_list.append(item)
            return intersection_list
        
        def inverse(_list: list):
            inversed_list = list()
            for i in range(len(_list)):
                inversed_list.append(_list[-1])
                _list.pop(-1)
            return inversed_list
