import unittest

def check_brackets(string):
    dict_brackets = {"{":"}","(":")","[":"]"}
    key_list = list(dict_brackets.keys())
    val_list = list(dict_brackets.values())
    temp_stack = []
    matched = True
    for i in string:
        
        if i in key_list:
            #print("append: ",i)
            temp_stack.append(i)
        elif i in val_list:
            #print("pop")
            if temp_stack.pop() != key_list[val_list.index(i)]:
                return False
    if len(temp_stack) == 0:
        return True
    else:
        return False

class TestCheckBraces(unittest.TestCase):
    def test_1(self):
        self.assertEqual(check_brackets("({[]})"),True)

    def test_2(self):
        self.assertTrue(check_brackets("(){}[]"))

    def test_3(self):
        self.assertEqual(check_brackets("(){[]({}[])}[]"),True)

    def test_4(self):
        self.assertFalse(check_brackets("(){[]({[])}[]"))


if __name__ == '__main__':
    unittest.main(verbosity=3)
