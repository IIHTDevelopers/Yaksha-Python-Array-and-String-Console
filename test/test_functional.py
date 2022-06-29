import unittest
from convert_to_uppercase import convert_upper_at_last
from get_first_n_elements import fetch_n_elements
from test.TestUtils import TestUtils
class FuctionalTests(unittest.TestCase):
    def test_convert_upper_at_last_2_chars(self):
        test_obj = TestUtils()
        result=convert_upper_at_last('ab',2)
        if result=='AB':
            test_obj.yakshaAssert("TestConvertUpperAtLast2Chars", True, "functional")
            print("TestConvertUpperAtLast2Chars = Passed")
        else:
            test_obj.yakshaAssert("TestConvertUpperAtLast2Chars", False, "functional")
            print("TestConvertUpperAtLast2Chars = Failed")

    def test_convert_upper_at_last_3_chars(self):
        test_obj = TestUtils()
        result=convert_upper_at_last('Python is a programming language',3)
        if result=='Python is a programming languAGE':
            test_obj.yakshaAssert("TestConvertUpperAtLast3Chars", True, "functional")
            print("TestConvertUpperAtLast3Chars = Passed")
        else:
            test_obj.yakshaAssert("TestConvertUpperAtLast3Chars", False, "functional")
            print("TestConvertUpperAtLast3Chars = Failed")

    def test_fetch_2_elements(self):
        test_obj = TestUtils()
        result=fetch_n_elements([4,16,3],2)
        if result==[4,16]:
            test_obj.yakshaAssert("TestFetch2Elements", True, "functional")
            print("TestFetch2Elements = Passed")
        else:
            test_obj.yakshaAssert("TestFetch2Elements", False, "functional")
            print("TestFetch2Elements = Failed")

    def test_fetch_5_elements(self):
        test_obj = TestUtils()
        result=fetch_n_elements([4,16,3,7,8,12,10,8],5)
        if result==[4,16,3,7,8]:
            test_obj.yakshaAssert("TestFetch5Elements", True, "functional")
            print("TestFetch5Elements = Passed")
        else:
            test_obj.yakshaAssert("TestFetch5Elements", False, "functional")
            print("TestFetch5Elements = Failed")
