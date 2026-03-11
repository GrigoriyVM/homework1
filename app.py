def hello():
    print("Hello, World!")

def goodbye():
    print("Goodbye!")

# Функция из master ветки
def master_func():
    print("This is master function")

# Функция из feature-a ветки
def feature_a_func():
    print("This is feature A")

def feature_x_func():
    print("Feature X implementation")

def feature_y_func():
    print("Feature Y implementation")

if __name__ == "__main__":
    hello()
    master_func()
    feature_a_func()
    feature_x_func()
    feature_y_func()
