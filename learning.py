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
    total = 0
    loss_value = 0
    with torch.no_grad():
        for batch_idx, (data, labels) in enumerate(test_Loader):
            inputs, labels = data.to(device), labels.to(device)
            outputs = model(inputs)
            _, predicted = torch.max(outputs.data, dim=1)
            loss = criterion(outputs, labels)
            loss_value += loss.data.cpu().numpy()
            total += 1
    print('test error rate %f' % (loss_value / total))



def train():
    global predicts, reals, epoch, k, model
    for batch_idx, (inputs, target) in enumerate(train_Loader):
        reals = []
        predicts = []
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
        if epoch % 10000 == 0:  # 每100步打印一次损失
            print('Epoch:{}, loss:{:.6f}'.format(epoch, loss_value))
        if loss_value <= 0.800000001:
            print('end Epoch:{}, loss:{:.6f}'.format(epoch, loss_value))
            k = 1
            test()
            break
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


def get_parameter():
    global parameter
    for i in range(len(parameter)):
        t = parameter[i][0]
        for par in parameter[i]:
            t = torch.add(t, par)
        t = torch.sub(t, parameter[i][0])
        result_parameter[i] = t


if __name__ == '__main__':
    predicts = []
    reals = []
    dataset = Load_Data.Sample_Dataset()
    result_parameter = [[], []]
    parameter = [[], []]
    for j in range(2):
        front = int(dataset.len * 0.8)
        back = int(dataset.len * 0.2) + 1
        train_data, test_data = random_split(dataset=dataset,
                                             lengths=[front, back],
                                             generator=torch.Generator().manual_seed(0))
        train_Loader = DataLoader(dataset=train_data,
                                  batch_size=320,
                                  shuffle=True)
        test_Loader = DataLoader(dataset=test_data,
                                 batch_size=320,
                                 shuffle=True)
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
        t_count = 0
        for parameters in model.parameters():
            parameter[t_count].append(parameters.data.cpu())
            t_count = t_count + 1
    print(parameter)
    get_parameter()
    print(result_parameter)