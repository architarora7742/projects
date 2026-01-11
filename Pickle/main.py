# Pickling __> In Python means serializing an object so that we can save it somewhere, and also we can unpickle it and retrieve it when we need it.
#  In general, when we save some data from a program we usually put it into JSON file or text file
# But what if you have a class and that class has attributes, and you already made modifications and created an instance, and you want to save the instance of the class.
# we can save the instance and load it back into the memory later
import pickle, json


class Fruit:
    def __init__(self, name: str, calories: float):
        self.name = name
        self.calories = calories

    def describe_fruit(self):
        print(self.name, self.calories, sep=": ")


if __name__ == "__main__":
    # fruit: Fruit = Fruit('Banana', 100)
    # fruit.describe_fruit()
    #
    # fruit.calories = 150

    # with open("banana.json", "w") as file:
    #     data = {'name': fruit.name, 'calories': fruit.calories}
    #     json.dump(data, file)
    #
    # with open("banana.json", "r") as file:
    #     data = json.load(file)
    #     print(data)

    # we have done a lot of steps just to create that data and dump it into a JSON file and to get that data back it also took a considerable amount of code.
    #  we didn't even get to the point where we have to dump this data into the fruit object once again so we can use that data.
    # instead of .pickle, you can put any extension but try to avoid common ones like .txt
    #     wb = write bytes
    #     with open("data.pickle", "wb") as file:
    #         pickle.dump(fruit, file)  # any actual object of Python and it's going to serialize that.
    #         Serializing means converting an object into byte stream

    with open("data.pickle", "rb") as file:
        fruit: Fruit = pickle.load(file)


        fruit.describe_fruit()
        fruit.calories = 200
        fruit.describe_fruit()

#         now we have unpickled it which means also deserializing __> converting from byte stream to the actual object that we can use in Python.

# Disclaimer: Pickled data can be extremely dangerous because there's no way to understand what's inside the file until you actually run this file so that what practically means that someone can put shell command in that pickled data
# So when you run it, it can actually gain access to your computer and that's something you don't want to happen so it's really important that you only load pickle data that you absolutely trust.

