class Tree:
    def __init__(self, height, age):
        self.height = height
        self.age = age

    def __str__(self):
        return "Height {0}m.  Age  {1} y.o.".format(self.height, self.age)


class FruitTree(Tree):
    def __init__(self, fruit_type, height, age):
        self.fruit_type = fruit_type
        super().__init__(height, age)

    def get_height(self):
        return self.height

    def set_height(self, new_height):
        if new_height > 15:
            self.height = 15
        else:
            self.height = new_height


tree1 = FruitTree('apple', 10, 5)
print(tree1.get_height())
tree1.set_height(17)
print(tree1.get_height())