import unittest
from custom_meta import CustomClass


class TestCustomMeta(unittest.TestCase):
    """Класс для тестирования класса CustomMeta"""

    def test_name_without_parameters(self):
        """
        Тестирование без заданных параметров того что имена методов
        и атрибутов начинаются с custom_
        """
        inst = CustomClass()
        self.assertTrue(hasattr(inst, 'custom_val'))
        self.assertTrue(hasattr(inst, 'custom_x'))
        self.assertTrue(hasattr(inst, 'custom_line'))
        self.assertTrue(hasattr(inst, 'custom_test_info'))
        self.assertTrue(hasattr(inst, '__init__'))
        self.assertFalse(hasattr(inst, 'val'))
        self.assertFalse(hasattr(inst, 'custom___init__'))
        self.assertFalse(hasattr(inst, 'x'))
        self.assertFalse(hasattr(inst, 'line'))
        self.assertFalse(hasattr(inst, 'test_info'))

    def test_name_with_parameters(self):
        """
        Тестирование с заданием параметров того что имена методов 
        и атрибутов начинаются с custom_
        """
        inst = CustomClass(75)
        self.assertTrue(hasattr(inst, 'custom_val'))
        self.assertTrue(hasattr(inst, 'custom_x'))
        self.assertTrue(hasattr(inst, 'custom_line'))
        self.assertTrue(hasattr(inst, 'custom_test_info'))
        self.assertTrue(hasattr(inst, '__init__'))
        self.assertFalse(hasattr(inst, 'val'))
        self.assertFalse(hasattr(inst, 'custom___init__'))
        self.assertFalse(hasattr(inst, 'x'))
        self.assertFalse(hasattr(inst, 'line'))
        self.assertFalse(hasattr(inst, 'test_info'))

    def test_name_with_named_parameters(self):
        """
        Тестирование с заданием именнованных параметров того что 
        имена методов и атрибутов начинаются с custom_
        """
        inst = CustomClass(val=75)
        self.assertTrue(hasattr(inst, 'custom_val'))
        self.assertTrue(hasattr(inst, 'custom_x'))
        self.assertTrue(hasattr(inst, 'custom_line'))
        self.assertTrue(hasattr(inst, 'custom_test_info'))
        self.assertTrue(hasattr(inst, '__init__'))
        self.assertFalse(hasattr(inst, 'val'))
        self.assertFalse(hasattr(inst, 'custom___init__'))
        self.assertFalse(hasattr(inst, 'x'))
        self.assertFalse(hasattr(inst, 'line'))
        self.assertFalse(hasattr(inst, 'test_info'))
