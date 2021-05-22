import torch
import Model
import Load_Data
import numpy as np
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
        for data in test_Loader:
            inputs, labels = data
            inputs, labels = inputs.to(device), labels.to(device)
            outputs = model(inputs)
            _, predicted = torch.max(outputs.data, dim=1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    print('Accuracy on test set :%d %%' % (100 * correct / total))


def train():
    count = 0
    plt.figure(figsize=(20, 8))
    global reals
    global predicts
    running_loss = 0.0
    for batch_idx, (inputs, target) in enumerate(train_Loader):
        optimizer.zero_grad()  # clear
        inputs, target = inputs.to(device), target.to(device)
        outputs = model(inputs)
        loss = criterion(outputs, target)
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
        if batch_idx % 300 == 299:
            print('[%d, %5d] loss: %.3f' % (epoch + 1, batch_idx + 1, running_loss / 300))
        predicts.append(outputs.data.cpu().numpy())
        reals.append(target.data.cpu().numpy())
        count = count + 1
    show_trend()
    reals.clear()
    predicts.clear()


def show_trend():
    predict = predicts[0]
    for i in range(1, len(predicts)):
        predict = np.append(predict, predicts[i])
    real = reals[0]
    for i in range(1, len(reals)):
        real = np.append(real, reals[i])
    x = np.arange(len(real))
    plt.plot(x, sorted(real), 'r-', linewidth=2, label=u'真实数据')
    plt.plot(x, sorted(predict), 'g-', linewidth=2, label=u'预测数据')
    plt.legend(loc='upper right')
    plt.grid(b=True)
    plt.show()
    if epoch == 9:
        for i, j in zip(real, predict):
            print(i, j)


if __name__ == '__main__':
    reals = []
    predicts = []
    dataset = Load_Data.Sample_Dataset()
    front = int(dataset.len * 0.7)
    back = int(dataset.len * 0.3) + 1
    train_data, test_data = random_split(dataset=dataset,
                                         lengths=[front, back],
                                         generator=torch.Generator().manual_seed(0))
    train_Loader = DataLoader(dataset=train_data,
                              batch_size=32,
                              shuffle=True)
    test_Loader = DataLoader(dataset=test_data,
                             batch_size=32,
                             shuffle=True)
    # model = Model.LLModel1()
    model = Model.LLModel3()
    # device = torch.device('cuda:1' if torch.cuda.is_available() else 'cpu')
    device = torch.device('cuda:0')
    model.to(device)
    criterion = torch.nn.MSELoss()  # 交叉商损失
    optimizer = optim.SGD(model.parameters(), lr=0.01)
    # plt.scatter(train_data.data.numpy(), test_data.data.numpy())
    for epoch in range(10):
        train()
        test()