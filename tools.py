class multitools:
    class lists:
        def ascending(_list: list):
            '''Returns the list in ascending order'''
            ascending_list = list()
            for i in range(len(_list)):
                ascending_list.append(min(_list))
                _list.remove(min(_list))
            return ascending_list
        
        def descending(_list: list):
            '''Returns the list in descending order'''
            descending_list = list()
            for i in range(len(_list)):
                descending_list.append(max(_list))
                _list.remove(max(_list))
            return descending_list
        
        def min(_list: list):
            '''Returns the lowest numeric item from the list'''
            return min(_list)
        
        def max(_list: list):
            '''Returns the highest numeric item from the list'''
            return max(_list)
        
        def sum(_list: list):
            '''Returns the sum of all the numeric items from the list'''
            total = 0
            for item in _list:
                try:
                    total += item
                except TypeError:
                    pass
            return total

        def subtraction(_list: list):
            '''Returns the subtraction of all the numeric items from the list'''
            total = 0
            for item in _list:
                try:
                    total -= item
                except TypeError:
                    pass
            return total

        def product(_list: list):
            '''Returns the product of all the numeric items from the list'''
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
            '''Returns the intersected items from two different lists'''
            intersection_list = list()
            for item in _list:
                if item in _list_:
                    intersection_list.append(item)
            return intersection_list
        
        def inverse(_list: list):
            '''Returns the inversed list'''
            inversed_list = list()
            for i in range(len(_list)):
                inversed_list.append(_list[-1])
                _list.pop(-1)
            return inversed_list
        
        def evenodd(_list: list, mode: int = 0):
            '''Returns even or odd values from the list (0 = Even, 1 = Odd)'''
            match mode:
                case 0:
                    even_list = list()
                    for item in _list:
                        try:
                            if item % 2 == 0:
                                even_list.append(item)
                        except TypeError:
                            pass
                    return even_list
                case 1:
                    odd_list = list()
                    for item in _list:
                        try:
                            if item % 2 != 0:
                                odd_list.append(item)
                        except TypeError:
                            pass
                    return odd_list

    class encryptor:
        def encrypt(data):
            '''Returns a dictionary containing the encrypted data and the key'''
            import random
            random_chars = ['1', '2', '3', '4', '5', '6', '7',
                            '8', '9', '0', 'a', 'b', 'c', 'd',
                            'e', 'f', 'g', 'h', 'i', 'j', 'k',
                            'l', 'm', 'n', 'o', 'p', 'q', 'r',
                            's', 's', 't', 'u', 'v', 'w', 'x',
                            'y', 'z', '!', '@', '#', '$', '%',
                            '¨', '&', '*', '(', ')', '_', '-',
                            '+', '=', '{', '}', '[', '],', '^']
            key = {}
            encrypted = ''
            for letter in data:
                rand = random.choice(random_chars)
                encrypted += rand
                key[letter] = rand
            
            return {encrypted: key}