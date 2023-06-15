""" Rectanlge Class Module """

from models.base import Base


class Rectangle(Base):
    """ Rectangle Class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor with 4 private object instances """
        self.check_validation("width", width)
        self.check_validation("height", height)
        self.check_validation("x", x)
        self.check_validation("y", y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    def __str__(self):
        """ object representation """
        i = self.id
        x = self.__x
        y = self.__y
        w = self.__width
        h = self.__height
        return f"[Rectangle] ({i}) {x}/{y} - {w}/{h}"

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, width):
        """ width setter """
        self.check_validation("width", width)
        self.__width = width

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, height):
        """ height setter """
        self.check_validation("height", height)
        self.__height = height

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, x):
        """ x setter """
        self.check_validation("x", x)
        self.__x = x

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, y):
        """ y setter """
        self.check_validation("y", y)
        self.__y = y

    def check_validation(self, name, value):
        """
            width & height >  0
            x     & y      >= 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0 and (name == "height" or name == "width"):
            raise ValueError(f"{name} must be > 0")
        if value < 0 and (name == "x" or name == "y"):
            raise ValueError(f"{name} must be >= 0")

    def area(self):
        """ Area = width x height """
        return self.__width * self.__height

    def display(self):
        """ Display the Rectangle """
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """ Update the existence arguments """
        if len(args) > 0:
            self.id = args[0]
            try:
                self.check_validation("width", args[1])
                self.__width = args[1]
            except Exception:
                pass

            try:
                self.check_validation("height", args[2])
                self.__height = args[2]
            except Exception:
                pass

            try:
                self.check_validation("x", args[3])
                self.__x = args[3]
            except Exception:
                pass

            try:
                self.check_validation("y", args[4])
                self.__y = args[4]
            except Exception:
                pass
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.check_validation("width", value)
                    self.__width = value
                if key == "height":
                    self.check_validation("height", value)
                    self.__height = value
                if key == "x":
                    self.check_validation("x", value)
                    self.__x = value
                if key == "y":
                    self.check_validation("y", value)
                    self.__y = value
