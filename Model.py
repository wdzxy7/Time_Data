import torch
import torch.nn.functional as F


class LLModel1(torch.nn.Module):
    def __init__(self):
        super(LLModel1, self).__init__()
        self.l1 = torch.nn.Linear(5, 10)
        self.l2 = torch.nn.Linear(10, 8)
        self.l3 = torch.nn.Linear(8, 4)
        self.l4 = torch.nn.Linear(4, 1)

    def forward(self, x):
        x = F.sigmoid(self.l1(x))
        x = F.sigmoid(self.l2(x))
        x = F.sigmoid(self.l3(x))
        return self.l4(x)


class LLModel2(torch.nn.Module):
    def __init__(self):
        super(LLModel2, self).__init__()
        self.l1 = torch.nn.Linear(5, 2)
        self.l2 = torch.nn.Linear(2, 1)

    def forward(self, x):
        x = F.relu(self.l1(x))
        return self.l2(x)


class LLModel3(torch.nn.Module):
    def __init__(self):
        super(LLModel3, self).__init__()
        self.l1 = torch.nn.Linear(5, 4)
        self.l2 = torch.nn.Linear(4, 3)
        self.l3 = torch.nn.Linear(3, 2)
        self.l4 = torch.nn.Linear(2, 1)

    def forward(self, x):
        x = torch.sigmoid(self.l1(x))
        x = torch.sigmoid(self.l2(x))
        x = torch.sigmoid(self.l3(x))
        # x = torch.sigmoid(self.l4(x))
        # return x
        return self.l4(x)


class LLModel4(torch.nn.Module):
    def __init__(self):
        super(LLModel4, self).__init__()
        self.l1 = torch.nn.Linear(5, 1)


    def forward(self, x):
        return self.l1(x)

    def show(self):
        w = self.l1.weight.data.cpu().numpy()
        b = self.l1.bias.data.cpu().numpy()
        print('w:{},b:{}'.format(w, b))


class MultiLinearRegression(torch.nn.Module):
    def __init__(self):
        super(MultiLinearRegression, self).__init__()
        self.linear1 = torch.nn.Linear(5, 3)  # 因为3个变量映射1个输出
        self.linear2 = torch.nn.Linear(3, 1)

    def forward(self, x):
        x = self.linear1(x)
        x = F.sigmoid(x)
        out = self.linear2(x)
        return out

    def show(self):
        w = self.linear1.weight.data.cpu().numpy()
        b = self.linear1.linear2.bias.data.cpu().numpy()
        print('w:{},b:{}'.format(w, b))
        w = self.linear2.weight.data.cpu().numpy()
        b = self.linear2.bias.data.cpu().numpy()
        print('w:{},b:{}'.format(w, b))
