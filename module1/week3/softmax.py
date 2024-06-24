import torch


class Softmax(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        exp_x = torch.exp(x)
        sum_exp_x = torch.sum(exp_x)
        return exp_x / sum_exp_x


class SoftmaxStable(torch.nn.Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, x):
        c = torch.max(x)
        exp_x = torch.exp(x - c)
        sum_exp_x = torch.sum(exp_x)
        return exp_x / sum_exp_x


data = torch.Tensor([1, 2, 3])
softmax = Softmax()
output_softmax = softmax(data)
print('softmax output: ', output_softmax)

data = torch.Tensor([1, 2, 3])
softmax_stable = SoftmaxStable()
output_softmax_stable = softmax_stable(data)
print('softmax stable output: ', output_softmax_stable)
