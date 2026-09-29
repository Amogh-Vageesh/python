class employee:

    def __init__(self):
        print("employee created")

    def __del__(self):
        print("Destructor called")

    @staticmethod
    def Create_obj():
        print("Making object")
        obj = employee()
        print("Function end")
        return obj

print("calling create obj function...")
obj = employee.Create_obj()
print("program end...")