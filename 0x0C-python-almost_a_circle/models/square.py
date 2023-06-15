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
        self.__size = size