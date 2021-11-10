import unittest

def check_brackets(string):
    dict_brackets = {"{":"}","(":")","[":"]"}
    temp_stack = []
    
    for i in string:
        
        if i in dict_brackets:
            temp_stack.append(i)
        elif i in dict_brackets.values():
            if len(temp_stack) == 0:
                return False
            if dict_brackets[temp_stack.pop()] !=  i:
                return False
    if len(temp_stack) == 0:
        return True
    else:
        return False

class TestCheckBraces(unittest.TestCase):
    def test_1(self):
        self.assertEqual(check_brackets("({[]})"),True)

    def test_2(self):
        self.assertFalse(check_brackets("()}{}[]"))

    def test_3(self):
        self.assertEqual(check_brackets("(){[]({}[])}[]"),True)

    def test_4(self):
        self.assertFalse(check_brackets("(){[]({[])}[]"))


if __name__ == '__main__':
    unittest.main(verbosity=3)
