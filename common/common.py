import os


class Common_Utils:

    def __init__(self):
        self.original_property_dict = dict()

    def load_properties(self):
        separator = "="
        try:
            with open("/Users/prathmesh/PycharmProjects/Learning/config/application.properties") as properties:
                for line in properties:
                    if separator in line:
                        name, value = line.split(separator, 1)
                        common_utils.original_property_dict[name.strip()] = value.strip().replace("\"", "")
            print("Properties intialized")
        except Exception as error:
            print("Error while loading the properties: ", error)


    def get_property(self, key_name):
        print("Get the value for the given key")
        return common_utils.original_property_dict[key_name]

    def set_property(self, key_name, value):
        print("Setting the keys in the dictionary")
        common_utils.original_property_dict[key_name] = value

common_utils = Common_Utils()