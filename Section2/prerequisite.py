class MyClass:
    def __init__(self):
        self.my_variable = "My message"

    def my_function(self):
        return self.my_variable

def main():
    obj = MyClass()
    print(obj.my_function())

    my_list = [1, 1, 2, 3, 5, 7, 13]

    if len(my_list) > 0:
        print("The list is not empty")
    else:
        print("The list is empty")

    while len(my_list) > 0:
        print(my_list)
        my_list.pop()


if __name__ == "__main__":
    main()