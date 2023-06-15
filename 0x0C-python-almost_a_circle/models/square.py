""" Square Class Model """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square Class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor that inherits all of its properties from its parent """
        super().__init__(size, size, x, y, id)
        self.__size = size

    def __str__(self):
        """ Class representation """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.__size}"

    @property
    def size(self):
        """ size getter """
        return self.__size
    
    @size.setter
    def size(self, size):
        """ size setter """
        super().check_validation("width", size)
        self.width = size
        self.height = size
        self.__size = size

    def update(self, *args, **kwargs):
        """ Update the existence arguments """
        if len(args) > 0:
            self.id = args[0]
            try:
                super().check_validation("width", args[1])
                self.__size = args[1]
            except Exception:
                pass

            try:
                super().check_validation("x", args[2])
                self.x = args[2]
            except Exception:
                pass

            try:
                super().check_validation("y", args[3])
                self.y = args[3]
            except Exception:
                pass
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    super().check_validation("width", value)
                    self.__size = value
                if key == "x":
                    super().check_validation("x", value)
                    self.x = value
                if key == "y":
                    super().check_validation("y", value)
                    self.y = value
