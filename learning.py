import Model
import torch
import Load_Data
import numpy as np
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader
from torch.utils.data import random_split


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def test():
    correct = 0
    total = 0
    with torch.no_grad():
        for batch_idx, (data, labels) in enumerate(test_Loader):
            inputs, labels = data.to(device), labels.to(device)
            outputs = model(inputs)
            _, predicted = torch.max(outputs.data, dim=1)


def train():
    global predicts, reals, epoch, k, model
    for batch_idx, (inputs, target) in enumerate(train_Loader):
        reals = []
        predicts = []
        '''
        if torch.cuda.is_available():
            model = model.cuda()
            inputs = inputs.cuda()
            target = target.cuda()
        '''
        inputs = inputs.to(device)
        target = target.to(device)
        output = model(inputs)  # 前向传播
        loss = criterion(output, target)  # 损失计算
        loss_value = loss.data.cpu().numpy()  # 获取损失值
        optimizer.zero_grad()  # 梯度置零
        loss.backward()  # 反向传播
        optimizer.step()  # 更新梯度
        predicts.append(output.data.cpu().numpy())
        reals.append(target.data.cpu().numpy())
        epoch += 1
        if epoch % 100 == 0:  # 每100步打印一次损失
            print('Epoch:{}, loss:{:.6f}'.format(epoch, loss_value))
        if loss_value <= 0.10001:
            print('Epoch:{}, loss:{:.6f}'.format(epoch, loss_value))
            k = 1
            break
        if loss_value <= 0.20001:
            show_trend(loss_value)
    if k == 1:
        show_trend(loss_value)


def show_trend(loss_value):
    plt.figure(figsize=(20, 8))
    predict = predicts[0]
    for i in range(1, len(predicts)):
        predict = np.append(predict, predicts[i])
    real = reals[0]
    for i in range(1, len(reals)):
        real = np.append(real, reals[i])
    x = np.arange(len(real))
    plt.plot(x, real, 'r-', linewidth=2, label=u'真实数据')
    plt.plot(x, predict, 'g-', linewidth=2, label=u'预测数据')
    plt.legend(loc='upper right')
    plt.grid(b=True)
    plt.title(str(loss_value))
    plt.show()


if __name__ == '__main__':
    predicts = []
    reals = []
    dataset = Load_Data.Sample_Dataset()
    front = int(dataset.len * 0.7)
    back = int(dataset.len * 0.3) + 1
    train_data, test_data = random_split(dataset=dataset,
                                         lengths=[front, back],
                                         generator=torch.Generator().manual_seed(0))
    train_Loader = DataLoader(dataset=train_data,
                              batch_size=320,
                              shuffle=True)
    test_Loader = DataLoader(dataset=test_data,
                             batch_size=320,
                             shuffle=True)

    # model = Model.MultiLinearRegression()
    model = Model.LLModel4()
    device = torch.device('cuda:0')
    model.to(device)
    # criterion = nn.BCEWithLogitsLoss()
    criterion = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(), lr=0.0001)

    k = 0
    epoch = 0
    while True:
        train()
        if k == 1:
            break
    model.show()