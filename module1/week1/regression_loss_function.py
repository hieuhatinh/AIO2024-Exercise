import random


def mae_loss_function(y, y_hat):
    return abs(y - y_hat)


def mse_loss_function(y, y_hat):
    return (y - y_hat) ** 2


def is_valid_numeric(number):
    try:
        int(number)
        return True
    except ValueError:
        return False


def print_result(loss_name, sample, pred, target, loss):
    print(
        f'loss name: {loss_name.upper()}, sample: {sample}, pred: {pred}, target: {target}, loss: {loss}')


def regression_loss_function(num_samples, loss_name):
    try:
        if not is_valid_numeric(num_samples):
            raise TypeError('number of samples must be an integer number')

        num_samples = int(num_samples)
        arr_loss_item_values = []
        for i in range(num_samples):
            pred = random.uniform(0, 10)
            target = random.uniform(0, 10)

            if loss_name.lower() == 'mae':
                loss = mae_loss_function(y=target, y_hat=pred)
                arr_loss_item_values.append(loss)
            elif loss_name.lower() == 'mse':
                loss = mse_loss_function(y=target, y_hat=pred)
                arr_loss_item_values.append(loss)

            print_result(loss_name=loss_name,
                         sample=i,
                         pred=pred,
                         target=target,
                         loss=loss)

        final_value_loss = sum(arr_loss_item_values) / num_samples
        print(f'final {loss_name.upper()}: {final_value_loss}')
    except Exception as e:
        print(e)
        return


num_samples = input('input number of samples: ')
loss_name = input('loss name: ')

regression_loss_function(num_samples, loss_name)
