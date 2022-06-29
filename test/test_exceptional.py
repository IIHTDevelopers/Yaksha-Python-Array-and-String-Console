import unittest
from convert_to_uppercase import convert_upper_at_last
from get_first_n_elements import fetch_n_elements
from test.TestUtils import TestUtils
class ExceptionalTest(unittest.TestCase):
    def test_type_error_for_convert_upper_on_int(self):
        test_obj = TestUtils()
        try:
            convert_upper_at_last(12345,3)
            #convert_upper_at_last('Python',10)
            test_obj.yakshaAssert("TestTypeErrorForConvertUpperOnInt", False, "exception")
            print("TestTypeErrorForConvertUpperOnInt = Failed")
        except TypeError:
            test_obj.yakshaAssert("TestTypeErrorForConvertUpperOnInt", True, "exception")
            print("TestTypeErrorForConvertUpperOnInt = Passed")

    def test_type_error_for_convert_upper_miss_arg(self):
        test_obj = TestUtils()
        try:
            convert_upper_at_last("Python")
            test_obj.yakshaAssert("TestTypeErrorForConvertUpperMissArg", False, "exception")
            print("TestTypeErrorForConvertUpperMissArg = Failed")
        except TypeError:
            test_obj.yakshaAssert("TestTypeErrorForConvertUpperMissArg", True, "exception")
            print("TestTypeErrorForConvertUpperMissArg = Passed")

    def test_type_error_for_fetch_n_elements_miss_arg(self):
        test_obj = TestUtils()
        try:
            fetch_n_elements([4,16,3,7,8,12,10,8])
            test_obj.yakshaAssert("TestTypeErrorForFetchNElementsMissArg", False, "exception")
            print("TestTypeErrorForFetchNElementsMissArg = Failed")
        except TypeError:
            test_obj.yakshaAssert("TestTypeErrorForFetchNElementsMissArg", True, "exception")
            print("TestTypeErrorForFetchNElementsMissArg = Passed")
