class CustomList(list):
    """Класс пользовательского списка"""

    def __add__(self, compared_list) -> list:
        """метод для сложения списков"""
        maxlist = self if len(self) >= len(compared_list) else compared_list
        minlist = self if len(self) < len(compared_list) else compared_list
        result = CustomList(maxlist)
        for i in range(len(minlist)):
            result[i] += minlist[i]
        return result

    def __sub__(self, compared_list) -> list:
        """метод для вычитания списков"""
        maxlist = self if len(self) >= len(compared_list) else compared_list
        minlist = self if len(self) < len(compared_list) else compared_list
        result = CustomList(maxlist)
        for i in range(len(minlist)):
            result[i] -= minlist[i]
        return result

    def __lt__(self, compared_list) -> bool:
        """метод для операции (<) сравнения  двух списков """
        return sum(self) < sum(compared_list)

    def __le__(self, compared_list) -> bool:
        """метод для операции (<=) сравнения  двух списков """
        return sum(self) <= sum(compared_list)

    def __eq__(self, compared_list) -> bool:
        """метод для операции (==) сравнения  двух списков """
        return sum(self) == sum(compared_list)

    def __ne__(self, compared_list) -> bool:
        """метод для операции (!=) сравнения  двух списков """
        return sum(self) != sum(compared_list)

    def __gt__(self, compared_list) -> bool:
        """метод для операции (>) сравнения  двух списков """
        return sum(self) > sum(compared_list)

    def __ge__(self, compared_list) -> bool:
        """метод для операции (>=) сравнения  двух списков """
        return sum(self) >= sum(compared_list)

    def __radd__(self, compared_list) -> list:
        """метод для сложения списков в случае если первый список не является CustomList"""
        return self.__add__(compared_list)

    def __rsub__(self, compared_list) -> list:
        """метод для вычитания списков в случае если первый список не является CustomList"""
        return self.__sub__(compared_list)

