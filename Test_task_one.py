class Test_task_one:
    input_data = []

    def __init__(self, input_data):
        self.input_data = input_data

    def sort_data(self):
        """
        This method developed to sort inbound
        data and print this values. Just for
        information and as the first stage
        """
        self.input_data.sort()
        print("Inbound data")
        print(self.input_data)
        print("-------------------------")
        print("-------------------------")


    def range_checker(self):
        """
        This method developed for data processing.
        It is serarching for range and returns common
        digits or range. This data still sorted
        """
        array_data = self.input_data
        result = ""
        temp_array = []

        for i in range (0, len(array_data) -1):
            current_val = array_data[i]
            if(current_val != array_data[-1]):
                if(current_val + 1 == array_data[i+1]):
                    if not current_val in temp_array:
                        temp_array.append(current_val)
                    temp_array.append(array_data[i+1])

                else:
            
                    if not current_val in temp_array:
                        result += str(current_val) + ", "

                    if(current_val == array_data[-1]-1):
                        if not array_data[-1] in temp_array:
                            temp_array.append(array_data[-1])
                    if(len(temp_array) >= 3):
                        item = str(temp_array[0]) + " - "+ str(temp_array[-1]) + ", "
                        result += item
                        temp_array = []

                    if(len(temp_array) <3):
                        for temp_ar in temp_array:
                            result += str(temp_ar) + ", "
                        temp_array = []

        if(len(temp_array) >= 3):
            item = str(temp_array[0]) + " - "+ str(temp_array[-1]) + ", "
            result += item

        if(len(temp_array) <3):
            for temp_ar in temp_array:
                result += str(temp_ar) + ", "
            

        if(array_data[-1] not in temp_array):
            result += str(array_data[-1])
        temp_array = []

        
        if(result [-2] == ","):
            result = result[:-2]

        
    
        print("This is result")
        print(result)
                

items = [-11, -9, -8, -6, -5, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20, 21, 22,57, 64, 65, 66, 67, 68, 69, 70, 76,77, 78]
test = Test_task_one(items)
res = test.sort_data()
r = test.range_checker()
    
