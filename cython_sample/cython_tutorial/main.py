import rectangle  # the dynamic library file (.so)


if __name__ == "__main__":
    obj = rectangle.PyRectangle(1, 1, 2, 3)
    print(obj.get_area())
    print(obj.get_size())
    vec = obj.getVector()
    print("vec = ", vec)
    obj.move(2, 5)
