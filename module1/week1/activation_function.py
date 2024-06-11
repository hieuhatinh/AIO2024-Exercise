import math


def is_number(n):
    try:
        float(n)  # Type - casting the string to ‘float ‘.
        # If string is not a valid ‘float ‘ ,
        # it ’ll raise ‘ValueError ‘ exception
    except ValueError:
        return False
    return True


def is_valid_activation_name(activation_function_name):
    if activation_function_name not in list_activation_function_name:
        return False
    return True


def sigmoid(x):
    return 1 / (1 + math.e**-x)


def relu(x):
    if x <= 0:
        return 0
    return x


def elu(x):
    alpha = 0.1
    if x <= 0:
        return alpha * (math.e ** x - 1)
    return x


def compute_activation_function(activation_function_name, x):
    try:
        valid_number = is_number(x)
        valid_activation_function_name = is_valid_activation_name(
            activation_function_name)

        if not valid_number:
            raise ValueError('x must be a number')

        if not valid_activation_function_name:
            raise ValueError(f"{activation_function_name} is not supported")

        if activation_function_name == 'sigmoid':
            return sigmoid(x)
        elif activation_function_name == 'relu':
            return relu(x)
        elif activation_function_name == 'elu':
            return elu(x)
    except ValueError:
        print('x must be a number')
        return
    except Exception as err:
        print(err)
        return


list_activation_function_name = ['sigmoid', 'relu', 'elu']

x = input('Input x = ')
activation_function_name_input = input(
    'Input activation Function (sigmoid | relu | elu): ')

compute_activation_function(activation_function_name_input, x)
