import logging
import employee

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s')

file_handler = logging.FileHandler('test_log.log')
logger.addHandler(file_handler)

stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
stream_handler.setFormatter(formatter)


file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)



# logging.basicConfig(level=(logging.DEBUG),
#     format='%(asctime)s: %(levelname)s: %(name)s: %(message)s',
#     filename='test.log')

def add(x, y):
    """Add function"""
    return x + y

def substract(x, y):
    """substract function"""
    return x - y

def multiply(x, y):
    """ multiply function"""
    return x * y

def divide(x, y):
    """ divide function"""
    try:
        result = x / y
    except ZeroDivisionError:
        logger.exception('Try to divide by zero')
    else:
        return result

num_1 = 100
num_2 = 0

add_result = add(num_1, num_2)
logger.debug('{} + {} = {}'.format(num_1, num_2, add_result))

substract_result = substract(num_1, num_2)
logger.debug('{} - {} = {}'.format(num_1, num_2, substract_result))

multiply_result = multiply(num_1, num_2)
logger.debug('{} * {} = {}'.format(num_1, num_2, multiply_result))

divide_result = divide(num_1, num_2)
logger.debug('{}, / {}, = {}'.format(num_1, num_2, divide_result))
