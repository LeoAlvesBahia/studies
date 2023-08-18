# region setters and getters
class Rectangle:
    """
    In this class, we perform validations before storing attribute
    values. This is accomplished using properties and setters, providing
    controlled access and modification of the class attributes.

    With the `@property` decorator, we define the methods `width` and
    `height` as getter methods. These methods act as interfaces,
    allowing us to access the protected values stored in `self._width`
    and `self._height`, respectively.

    During class instantiation, when the `__new__` method is executed
    (before `__init__`), the namespaces for `self.width` and
    `self.height` are defined. These namespaces are created dynamically
    when the class instance is created and are referenced to the
    corresponding `@property` methods. At this point, you can access
    `self.width` and `self.height` as if they were regular attributes.

    The namespaces for `self._width` and `self._height`, on the other
    hand, are defined at their respective `@width.setter` and
    `@height.setter` methods. This occurs during the execution of the
    `__init__` method. The `self._width` and `self._height` attributes
    store the actual values for `self.width` and `self.height`,
    respectively.

    The `@width.setter` and `@height.setter` decorators define the
    setter methods for the `width` and `height` properties,
    respectively. These setter methods are called whenever we assign new
     values to `self.width` or `self.height`. The setters provide us
     with an opportunity to perform validations and constraints before
     storing the new values in `self._width` and `self._height`.

    This approach allows us to control access to the attributes and
    apply any necessary checks, ensuring that only valid data is stored
    in the `self._width` and `self._height` attributes. The properties
    `self.width` and `self.height` serve as clean interfaces,
    abstracting the internal attribute management and providing a
    user-friendly way to interact with the class attributes.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError('Width must be positive.')
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError('Height must be positive.')
        self._height = height

    def __repr__(self):
        """
        The __repr__ we usually use to demonstrate how we can replicate
        the object.
        """
        return 'Rectangle({0}, {1})'.format(self.width, self.height)

    def __str__(self):
        """
        The __str__ we usually use to represent in human-readable format
        """
        return 'Rectangle: width={0}, height={1})'.format(self.width,
                                                          self.height)

    def __eq__(self, other):
        """
        The __eq__ is to set how to compare the object.
        E.g., Rectangle(10, 10) == Rectangle(10, 10) will return True
        """
        if isinstance(other, Rectangle):
            return (self.width, self.height) == (other.width, other.height)
        else:
            return False


x = Rectangle(10, 10)
print(x)
# endregion
