import pytest

class ProcessIntegerList:
    def __init__(self, input_list):
        self.input_list = input_list
    
    def process_list(self):
        # Check if the length of the list is a multiple of 10
        if len(self.input_list) % 10 != 0:
            raise ValueError("Input list length must be a multiple of 10")
        
        # Remove items at positions which are a multiple of 2 or 3
        processed_list = [round(float(item)) for item in self.input_list if round(float(item)) % 2 != 0 and round(float(item)) % 3 != 0]
        return processed_list
# test class
class TestProcessIntegerList:
    # test cases
    def test_valid_input(self):
        task_instance = ProcessIntegerList([1, "2.67", 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
        result = task_instance.process_list()
        assert result == [1, 5, 7,11, 13, 17, 19]

    def test_valid_input_with_decimal(self):
        task_instance = ProcessIntegerList([1.132, 2.0, 3.1, 4.23, 5.5, 6.87, 7.0, 8.32, 9.98, 10.4, 11.0, 12.0, 13.12, 14.32, 15.0, 16.77, 17.9, 18.4, 19.0, 20.5])
        result = task_instance.process_list()
        assert result == [1,7,7, 11, 13,17,19]

    def test_string_int(self):
        task_instance = ProcessIntegerList(['6.1','3',22,'11',343,'47',19,44,21,29])
        result = task_instance.process_list()
        assert result == [11,343,47,19,29]

    def test_valid_input_with_mix_number(self):
        task_instance = ProcessIntegerList([1, '2', -29, 4, 5, '6', 7, 8, 29, 10, 11, 12, -13, '-14', -23, 15, 16, 17, '18', -209])
        result = task_instance.process_list()
        assert result == [1,-29, 5, 7,29,11, -13,-23, 17, -209]

    def test_invalid_input_length(self):
        task_instance = ProcessIntegerList([9,6,0,8,7])
        with pytest.raises(ValueError, match="Input list length must be a multiple of 10"):
            task_instance.process_list()

    def test_empty_input(self):
        task_instance = ProcessIntegerList([])
        result = task_instance.process_list()
        assert result == []
            
    def test_empty_result(self):
        task_instance = ProcessIntegerList([2,99,44,24,18,45,9,102,33,21])
        result = task_instance.process_list()
        assert result == []

    def test_input_with_zeros(self):
        task_instance = ProcessIntegerList([0, 2, 0, 4, 5, 6, 0, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
        result = task_instance.process_list()
        assert result == [5, 11, 13, 17, 19]

    def test_negative_input(self):
        task_instance = ProcessIntegerList([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20])
        result = task_instance.process_list()
        assert result == [-1, -5, -7, -11, -13, -17, -19]

    def test_input_with_duplicates(self):
        task_instance = ProcessIntegerList([13, 2, 3, 2, 4, 5, 3, 6, 7, 8, 9, 10, 11, 12, 13, 11, 15, 11, 2, 18])
        result = task_instance.process_list()
        assert result == [13, 5, 7, 11, 13,11,11]

if __name__ == '__main__':
    pytest.main()
