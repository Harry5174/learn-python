import unittest
import capitalize_module

class TestCapitalize(unittest.TestCase):
    
    def test_one_word(self):
        text = 'python'
        result = capitalize_module.capitalize(text)
        
        self.assertEqual(result, 'Python')
        
    def test_multiple_words(self):
        text = 'monty python'
        result = capitalize_module.capitalize(text)
        
        self.assertEqual(result, 'Monty Python')
        
if __name__ == "__main__":
    unittest.main()