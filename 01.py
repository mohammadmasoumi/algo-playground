"""
pop_number_from_stack
push_number_to_stack
get_top_number_of_stack
get_minimum_number_of_stack

arr = []
push(10)
push(20) append
pop(20) pop
top(-1)
min() # min num in arr o(1)
"""

class numbers(list):
    __min_value = None

    def push_number_to_stack(self, item):
        if self.__min_value is None:
            self.__min_value = item
        else:
            if item < self.__min_value:
                self.__min_value = item

        self.append(item)

    def pop_number_from_stack(self, item):
        if len(self) == 0:
            raise Exception("empty numbers")
        
        self.remove(item)
        if item <= self.__min_value:
            self.__min_value = min(self)            

    def get_top_number_of_stack(self):
        return self.pop()
    
    def get_minimum_number_of_stack(self):
        if self.__min_value == None:
            raise Exception("empty numbers")
        return self.__min_value


def first_test(numbers):
    numbers.push_number_to_stack(10)
    numbers.push_number_to_stack(20)
    numbers.pop_number_from_stack(10)
    numbers.push_number_to_stack(30)
    top_number = numbers.get_top_number_of_stack()
    min_number = numbers.get_minimum_number_of_stack()
    print({"top": top_number, "min": min_number})


def second_test(numbers):
    numbers.push_number_to_stack(7)
    top_number = numbers.get_top_number_of_stack()
    min_number = numbers.get_minimum_number_of_stack()
    print({"top": top_number, "min": min_number})

def third_test(numbers):
    numbers.push_number_to_stack(25)
    top_number = numbers.get_top_number_of_stack()
    min_number = numbers.get_minimum_number_of_stack()
    print({"top": top_number, "min": min_number})


def run_tests(numbers):
    first_test(numbers)
    second_test(numbers)
    third_test(numbers)


n = numbers()
run_tests(n)