import torch
import numpy as np
from torch.utils.data import Dataset
from torch.utils.data import DataLoader


class Sample_Dataset(Dataset):
    def __init__(self):
        data = np.loadtxt('result.csv', str, delimiter=',', skiprows=1)
        self.len = data.shape[0] - 1
        self.x_data = torch.from_numpy(data[:, 0:5].astype(np.float32))
        self.y_data = torch.from_numpy(data[:, [-1]].astype(np.float32))

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.len
