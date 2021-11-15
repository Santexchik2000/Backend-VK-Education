import unittest
from custom_list import CustomList


class TestCustomList(unittest.TestCase):
    """Класс для тестирование класса CustomList"""

    def test_add_two_custom_eq_len(self):
        """
        Тест работы метода __add__, для двух кастомных списков
        равной длины
        """
        list_1 = CustomList([1, 2, 3, 4, 5])
        list_2 = CustomList([1, 2, 3, 4, 5])
        result = CustomList([2, 4, 6, 8, 10])
        c = list_1 + list_2
        self.assertIsInstance(c, CustomList)
        self.assertListEqual(c, result)

    def test_add_two_custon_not_eq_len(self):
        """
        Тест работы метода __add__, для двух кастомных списков не равной длины
        """
        list_1 = CustomList([1, 2, 3, 4, 5])
        list_2 = CustomList([1, 2, 3, 4, 5, 6])
        result = CustomList([2, 4, 6, 8, 10, 6])
        c = list_1 + list_2
        self.assertIsInstance(c, CustomList)
        self.assertListEqual(c, result)

    def test_add_one_custom_and_reg_list_eq_len(self):
        """
        Тест работы метода __add__, для одного кастомного и одного обычного списка
        равной длины
        """
        list_1 = CustomList([1, 2, 3, 4, 5])
        list_2 = [1, 2, 3, 4, 5]
        result = CustomList([2, 4, 6, 8, 10])
        c = list_1 + list_2
        self.assertIsInstance(c, CustomList)
        self.assertListEqual(c, result)

    def test_add_one_custom_and_reg_list_not_eq_len(self):
        """
        Тест работы метода __add__, для одного кастомного и одного обычного списка
        не равной длины
        """
        list_1 = CustomList([1, 2, 3, 4, 5])
        list_2 = [1, 2, 3, 4, 5, 6]
        result = CustomList([2, 4, 6, 8, 10, 6])
        c = list_1 + list_2
        self.assertIsInstance(c, CustomList)
        self.assertListEqual(c, result)

    def test_radd_two_custom_eq_len(self):
        """
        Тест работы метода __radd__ для двух кастомных списков равной длины
        """
        list_1 = CustomList([1, 2, 3, 4, 5])
        list_2 = CustomList([1, 2, 3, 4, 5])
        result = CustomList([2, 4, 6, 8, 10])
        c = list_1 + list_2
        self.assertIsInstance(c, CustomList)
        self.assertListEqual(c, result)

    def test_radd_two_custom_not_eq_len(self):
        """
        Тест работы метода __radd__, для двух кастомных списков не равной длины
        """
        list_1 = CustomList([1, 2, 3, 4, 5])
        list_2 = CustomList([1, 2, 3, 4, 5, 6])
        result = CustomList([2, 4, 6, 8, 10, 6])
        c = list_1 + list_2
        self.assertIsInstance(c, CustomList)
        self.assertListEqual(c, result)

    def test_radd_one_custom_and_reg_list_eq_len(self):
        """
        Тест работы метода __radd__, для одного кастомного и одного обычного списка
        равной длины
        """
        list_1 = CustomList([1, 2, 3, 4, 5])
        list_2 = [1, 2, 3, 4, 5]
        result = CustomList([2, 4, 6, 8, 10])
        c = list_1 + list_2
        self.assertIsInstance(c, CustomList)
        self.assertListEqual(c, result)

    def test_radd_one_custom_and_req_list_not_eq_len(self):
        """
        Тест работы метода __radd__, для одного кастомного и одного обычного списка
        не равной длины
        """
        list_1 = CustomList([1, 2, 3, 4, 5])
        list_2 = [1, 2, 3, 4, 5, 6]
        result = CustomList([2, 4, 6, 8, 10, 6])
        c = list_1 + list_2
        self.assertIsInstance(c, CustomList)
        self.assertListEqual(c, result)

    def test_radd_one_reg_and_custom_list_eq_len(self):
        """
        Тест работы метода __radd__, для одного обычного и одного кастомного списка
        равной длины
        """
        list_1 = [1, 2, 3, 4, 5]
        list_2 = CustomList([1, 2, 3, 4, 5])
        result = CustomList([2, 4, 6, 8, 10])
        c = list_1 + list_2
        self.assertIsInstance(c, CustomList)
        self.assertListEqual(c, result)

    def test_radd_one_reg_and_custom_list_not_eq_len(self):
        """
        Тест работы метода __radd__, для одного обычного и одного кастомного списка
        не равной длины
        """
        list_1 = [1, 2, 3, 4, 5, 6]
        list_2 = CustomList([1, 2, 3, 4, 5])
        result = CustomList([2, 4, 6, 8, 10, 6])
        c = list_1 + list_2
        self.assertIsInstance(c, CustomList)
        self.assertListEqual(c, result)

    def test_sub_two_custom_eq_len(self):
        """
        Тест работы метода __sub__, для двух кастомных списков
        равной длины
        """
        list_1 = CustomList([1, 2, 3, 4, 5])
        list_2 = CustomList([1, 2, 3, 4, 5])
        result = CustomList([0, 0, 0, 0, 0])
        c = list_1 - list_2
        self.assertIsInstance(c, CustomList)
        self.assertListEqual(c, result)

    def test_sub_two_custom_not_eq_len(self):
        """
        Тест работы метода __sub__, для двух кастомных списков не равной длины
        """
        list_1 = CustomList([1, 2, 3, 4, 5])
        list_2 = CustomList([1, 2, 3, 4, 5, 6])
        result = CustomList([0, 0, 0, 0, 0, 6])
        c = list_1 - list_2
        self.assertIsInstance(c, CustomList)
        self.assertListEqual(c, result)

    def test_sub_one_custom_and_reg_list_eq_len(self):
        """
        Тест работы метода __sub__, для одного кастомного и одного обычного списка
        равной длины
        """
        list_1 = CustomList([1, 2, 3, 4, 5])
        list_2 = [1, 2, 3, 4, 5]
        result = CustomList([0, 0, 0, 0, 0])
        c = list_1 - list_2
        self.assertIsInstance(c, CustomList)
        self.assertListEqual(c, result)

    def test_sub_one_custom_and_req_list_not_eq_len(self):
        """
        Тест работы метода __sub__, для одного кастомного и одного обычного списка
        не равной длины
        """
        list_1 = CustomList([1, 2, 3, 4, 5])
        list_2 = [1, 2, 3, 4, 5, 6]
        result = CustomList([0, 0, 0, 0, 0, 6])
        c = list_1 - list_2
        self.assertIsInstance(c, CustomList)
        self.assertListEqual(c, result)

    def test_rsub_two_custom_eq_len(self):
        """
        Тест работы метода __rsub__ для двух кастомных списков равной длины
        """
        list_1 = CustomList([1, 2, 3, 4, 5])
        list_2 = CustomList([1, 2, 3, 4, 5])
        result = CustomList([0, 0, 0, 0, 0])
        c = list_1 - list_2
        self.assertIsInstance(c, CustomList)
        self.assertListEqual(c, result)

    def test_rsub_two_custom_not_eq_len(self):
        """
        Тест работы метода __rsub__, для двух кастомных списков не равной длины
        """
        list_1 = CustomList([1, 2, 3, 4, 5])
        list_2 = CustomList([1, 2, 3, 4, 5, 6])
        result = CustomList([0, 0, 0, 0, 0, 6])
        c = list_1 - list_2
        self.assertIsInstance(c, CustomList)
        self.assertListEqual(c, result)

    def test_rsub_one_custom_and_reg_list_eq_len(self):
        """
        Тест работы метода __rsub__, для одного кастомного и одного обычного списка
        равной длины
        """
        list_1 = CustomList([1, 2, 3, 4, 5])
        list_2 = [1, 2, 3, 4, 5]
        result = CustomList([0, 0, 0, 0, 0])
        c = list_1 - list_2
        self.assertIsInstance(c, CustomList)
        self.assertListEqual(c, result)

    def test_rsub_one_custom_and_req_list_not_eq_len(self):
        """
        Тест работы метода __rsub__, для одного кастомного и одного обычного списка
        не равной длины
        """
        list_1 = CustomList([1, 2, 3, 4, 5])
        list_2 = [1, 2, 3, 4, 5, 6]
        result = CustomList([0, 0, 0, 0, 0, 6])
        c = list_1 - list_2
        self.assertIsInstance(c, CustomList)
        self.assertListEqual(c, result)

    def test_rsub_one_reg_and_custom_list_eq_len(self):
        """
        Тест работы метода __rsub__, для одного обычного и одного кастомного списка
        равной длины
        """
        list_1 = [1, 2, 3, 4, 5]
        list_2 = CustomList([1, 2, 3, 4, 5])
        result = CustomList([0, 0, 0, 0, 0])
        c = list_1 - list_2
        self.assertIsInstance(c, CustomList)
        self.assertListEqual(c, result)

    def test_rsub_one_reg_and_custom_list_not_eq_len(self):
        """
        Тест работы метода __rsub__, для одного обычного и одного кастомного списка
        не равной длины
        """
        list_1 = [1, 2, 3, 4, 5, 6]
        list_2 = CustomList([1, 2, 3, 4, 5])
        result = CustomList([0, 0, 0, 0, 0, 6])
        c = list_1 - list_2
        self.assertIsInstance(c, CustomList)
        self.assertListEqual(c, result)

    def test_lt_two_reg_list(self):
        """
        Тест работы оператора __lt__ для двух обычных списков
        """
        a = [1, 2, 3, 4]
        b = [1, 2, 3, 1]
        self.assertLess(b, a)

    def test_lt_two_custom_list(self):
        """
        Тест работы оператора __lt__ для двух кастомных списков
        """
        a = CustomList([1, 2, 3, 4])
        b = CustomList([1, 2, 3, 1])
        self.assertLess(b, a)

    def test_lt_one_custom_one_reg_list(self):
        """
        Тест работы оператора __lt__ для одного кастомного и одного обычного списка
        """
        a = CustomList([1, 2, 3, 4])
        b = [1, 2, 3, 1]
        self.assertLess(b, a)

    def test_lt_one_custom_one_req_list_not_eq(self):
        """
        Тест работы оператора __lt__ для двух кастомных списков разной длины
        """
        a = CustomList([6, 6, 6])
        b = CustomList([1, 2, 3, 4, 5])
        self.assertLess(b, a)

    def test_lt_two_custom_list_not_eq(self):
        """
        Тест работы оператора __lt__ для одного кастомного и одного обычного списка разной длины
        """
        a = CustomList([6, 6, 6])
        b = [1, 2, 3, 4, 5]
        self.assertLess(b, a)

    def test_lt_two_reg_list_not_eq(self):
        """
        Тест работы оператора __lt__ для двух обычных списков разной длины
        """
        a = [6, 6, 6]
        b = [1, 2, 3, 4, 5]
        self.assertLess(b, a)

    def test_le_two_custom_eq(self):
        """
        Тест работы оператора __le__ для двух кастомных спиской одинаковой длины
        """
        a = CustomList([1, 2, 3])
        b = CustomList([1, 2, 3])
        self.assertLessEqual(b, a)

    def test_le_custom_reg_eq(self):
        """
        Тест работы оператора __le__ для кастомного и обычного списка одинаковой длины
        """
        a = CustomList([1, 2, 3])
        b = [1, 2, 3]
        self.assertLessEqual(b, a)

    def test_le_custom_not_eq(self):
        """
        Тест работы оператора __le__ для кастомного списка разной длины
        """
        a = CustomList([1, 2, 3, 4, 5, 6, 7])
        b = CustomList([1, 2, 3])
        self.assertLessEqual(b, a)

    def test_le_custom_reg_not_eq(self):
        """
        Тест работы оператора __le__ для кастомного и обычного списка разной длины
        """
        a = CustomList([1, 2, 3, 4, 5, 6, 7])
        b = ([1, 2, 3])
        self.assertLessEqual(b, a)

    def test_eq_custom(self):
        """
        Тест оператора __eq__ для двух кастомных списков
        """
        a = CustomList([1, 2, 3, 4, 5])
        b = CustomList([1, 2, 3, 4, 5])
        self.assertEqual(b, a)

    def test_eq_reg_custom(self):
        """
        Тест оператора __eq__ для кастомного и обычного списков
        """
        a = [1, 2, 3, 4, 5]
        b = CustomList([2, 1, 3, 4, 5])
        self.assertEqual(b, a)

    def test_eq_custom_not_eq(self):
        """
        Тест оператора __eq__ для двух кастомных списков
        """
        a = CustomList([5, 2, 3, 4, 5])
        b = CustomList([2, 1, 3, 4, 5])
        self.assertNotEqual(b, a)

    def test_eq_reg_custom_not_eq(self):
        """
        Тест оператора __eq__ для одного кастомного и обычного списка
        """
        a = [5, 2, 3, 4, 5]
        b = CustomList([2, 1, 3, 4, 5])
        self.assertNotEqual(b, a)

    def test_ne_two_custom(self):
        """
        Тест оператора __ne__ для двух кастомных списков
        """
        a = CustomList([1, 3, 4, 5])
        b = CustomList([18, 5, 7, 4])
        self.assertNotEqual(a, b)

    def test_ne_reg_custom(self):
        """
        Тест оператора __ne__ для кастомного и обычного списков
        """
        a = [1, 3, 4, 5]
        b = CustomList([18, 5, 7, 4])
        self.assertNotEqual(a, b)

    def test_gt_custom(self):
        """
        Тест оператора __gt__ для двух кастомных списков
        """
        a = CustomList([1, 3, 5])
        b = CustomList([1, 6])
        self.assertGreater(a, b)

    def test_gt_reg_custom(self):
        """
        Тест оператора __gt__ для одного обычного и кастомного списков
        """
        a = [1, 3, 5]
        b = CustomList([1, 6])
        self.assertGreater(a, b)

    def test_ge_two_custom_eq(self):
        """
        Тест оператора __ge__ для двух кастомных списков
        """
        a = CustomList([1, 3, 5, 6])
        b = CustomList([1, 3, 5, 6])
        self.assertGreaterEqual(a, b)

    def test_ge_reg_custom_eq(self):
        """
        Тест оператора __ge__ для обычного и кастомного списков
        """
        a = [1, 3, 5, 6]
        b = CustomList([1, 3, 5, 6])
        self.assertGreaterEqual(a, b)

    def test_ge_custom_not_eq(self):
        """
        Тест оператора __ge__ для двух кастомных не равных списков
        """
        a = CustomList([1, 3, 6])
        b = CustomList([1, 4])
        self.assertGreaterEqual(a, b)

    def test_ge_reg_custom_not_eq(self):
        """
        Тест оператора __ge__ для кастомного и обычного списков, не равных
        """
        a = CustomList([1, 3, 6])
        b = [1, 4]
        self.assertGreaterEqual(a, b)
