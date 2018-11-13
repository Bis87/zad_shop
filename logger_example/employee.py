import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('employee.log')
logger.addHandler(file_handler)

formatter = logging.Formatter('%(levelname)s: %(name)s: %(message)s')
file_handler.setFormatter(formatter)

class Employee:
    """A sample employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info('Employee created: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Vasya', 'Pupkin')
emp_2 = Employee('Petya', 'Zhopkin')
emp_3 = Employee('Olesha', 'Kashkin')
