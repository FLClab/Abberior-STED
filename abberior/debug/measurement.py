
import yaml
import operator
import numpy
import os

from functools import reduce

def find(_dict, element):
    """
    Returns an element from a dict using a path-like string

    :param _dict: A `dict`
    :param element: A path-like `str` with "/" separators

    :returns : The element at the desired path
    """
    if not element:
        return _dict    
    return reduce(operator.getitem, element.split("/"), _dict)

def nested_set(_dict, keys, value, create_missing=False):
    """
    Sets the value of a nested dict

    :param _dict: A `dict`
    :param keys: A path-like `str` with "/" separators
    :param value: The value of the keys
    :param create_missing: A `bool` wheter to create missing path

    :returns : An updated `dict`
    """
    d = _dict
    keys = keys.split("/")
    for key in keys[:-1]:
        if key in d:
            d = d[key]
        elif create_missing:
            d = d.setdefault(key, {})
        else:
            return _dict
    if keys[-1] in d or create_missing:
        d[keys[-1]] = value
    return _dict

class Stack:
    """
    Implements a `Stack` object
    """
    def __init__(self, shape=(256, 256)):
        self.image = numpy.random.rand(*shape)

    def data(self):
        """
        Returns a `list` of `list` of `numpy.ndarray`
        """
        return [[self.image]]

class Config:
    """
    Implements a `Config` object
    """
    def __init__(self):
        self._name = "conf.yml"
        self._stack_names = ["Overview 640"]
        with open(os.path.join(os.path.dirname(__file__), self._name), "r") as file:
            self.config = yaml.load(file, Loader=yaml.FullLoader)

    def number_of_stacks(self):
        """
        Returns the number of stacks

        :returns : An `int` of the number of stacks
        """
        return 1

    def parameters(self, key):
        """
        Gets the parameters at the desired key

        :param key: A path-like key with "/" separators

        :returns : The value at the desired key
        """
        return find(self.config, key)

    def set_parameters(self, key, value):
        """
        Sets the parameter at the desired key with the given value

        :param key: A path-like key with "/" separators
        :param value: The desired value

        :returns : An updated version of the `config`
        """
        self.config = nested_set(self.config, key, value)
        return self.config

    def stack(self, item):
        """
        Gets the stacks at the current position

        :param item: An `int` of the position

        :returns : A `Stack`
        """
        width = int(self.config["ExpControl"]["scan"]["range"]["x"]["len"] / self.config["ExpControl"]["scan"]["range"]["x"]["psz"])
        height = int(self.config["ExpControl"]["scan"]["range"]["y"]["len"] / self.config["ExpControl"]["scan"]["range"]["y"]["psz"])
        return Stack(shape=(height, width))

    def stack_names(self):
        """
        Gets the names of the stacks

        :returns : A `list` of stack names
        """
        return self._stack_names

    def name(self):
        """
        Gets the name of the config

        :returns : A `str` of the name
        """
        return self._name

    def __repr__(self):
        """
        Implements the `print` function

        :returns : A `str` of the object
        """
        return str(self.config)

    def copy(self):
        """
        Implements a `copy` method

        :returns : A copy of self
        """
        return self

class Measurement:
    """
    Implements a `Measurement` object
    """
    def __init__(self):
        self.configs = [Config()]

    def activate(self, conf):
        """
        Activates the desired config
        """
        pass

    def active_configuration(self):
        """
        Gets the current active configuration

        :returns : A `Config`
        """
        return self.configs[0]

    def clone(self, conf):
        """
        Clone the configuration object and adds it to the current `Measurement`

        :param conf: A `Configuration` object

        :returns : A cloned `Configuration` object
        """
        newconf = conf.copy()
        self.configs.append(newconf)
        return newconf

    def save_as(self, savepath, compress=False):
        """
        Saves the current measurement. This is not implemented.

        :param savepath: A `str` of the saving path
        :param compress: A `bool` wheter to compress the data
        """
        return

    def __repr__(self):
        """
        Implements the `print` function

        :returns : A `str` of the object
        """
        return "Measurement"

class Imspector:
    """
    Implements an `Imspector` object
    """
    def __init__(self):
        pass

    def run(self, measurement):
        """
        Runs the desired measurement
        """
        return measurement

    def active_measurement(self):
        """
        Gets the current active measurement
        """
        return Measurement()

if __name__ == "__main__":

    im = Imspector()
    measurement = Measurement()

    conf = measurement.active_configuration()
    measurement.activate(conf)
    im.run(measurement)
    stacks = [conf.stack(i) for i in range(conf.number_of_stacks())]
    image = [[image[2:].copy() for image in stack.data()[0]] for stack in stacks]
    image = numpy.array(image)
