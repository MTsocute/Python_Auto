import unittest
import re


class MyTestCase(unittest.TestCase):
    def setUp(self):
        """ 初始化参数 """
        self.text = "Contact us at: 123-456-7890 or (555) 123-4567 ext. 12345"
        self.phoneRegex = re.compile(r'''(
            (\d{3}|\(\d{3}\))?      # area code
            (\s|-|\.)?              # separator
            (\d{3})                 # first 3 digits
            (\s|-|\.)               # separator
            (\d{4})                 # last 4 digits
            (\s*(ext|x|ext.)\s*(\d{2,5}))?          # extension
        )''', re.VERBOSE)
        self.matches = []

    def test_phoneRegex_result(self):
        """ 测试下 phoneRegex 匹配出来是什么样的内容 """
        self.matches = self.phoneRegex.findall(self.text)
        print(self.matches)


if __name__ == '__main__':
    unittest.main()
