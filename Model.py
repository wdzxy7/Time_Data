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
        x = F.relu(self.l1(x))
        x = F.relu(self.l2(x))
        x = F.relu(self.l3(x))
        return self.l4(x)