"""Implement Person class."""


class PersonIterator(object):

    """Implement iterator for Person."""

    def __init__(self, attr):
        self.attr = attr

    def next(self):
        """Return next iterable value."""
        if len(self.attr):
            v = self.attr[0]
            self.attr = self.attr[1:]
            return v
        else:
            raise StopIteration


class Person(object):

    """Represent a person."""

    def __init__(self, name='Noname', age=0):
        self.name = name
        self.age = age
        self.attributes = {}

    def __str__(self):
        """Return string for object."""
        attr = ''
        if len(self.attributes) == 0:
            attr = 'None'
        else:
            attr = '; '.join(['%s -> %s' %
                              (k, v) for k, v in self.attributes.items()])
        s = 'Name: %s\nAge: %d\nAdditional attributes: %s' % (self.name,
                                                              self.age, attr)
        return s

    def add_attribute(self, key, value):
        """Add attribute."""
        self.attributes[key] = value

    def __iter__(self):
        """Return iterator."""
        values = [('Name', self.name), ('Age', self.age)]
        values.extend(self.attributes.items())
        return PersonIterator(values)
