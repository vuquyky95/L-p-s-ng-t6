import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Hàm tính cost
def compute_cost(X, y, w, bias):
    m = len(y)
    h = np.dot(X, w) + bias
    cost = (1/(2*m)) * np.sum((h - y)**2)
    return cost

# Hàm tối ưu gradient descent
def gradient_descent(X, y, w, bias, learning_rate, num_iterations):
    m = len(y)
    costs = []

    for i in range(num_iterations):
        h = np.dot(X, w) + bias
        dw = (1/m) * np.dot(X.T, (h - y))
        db = (1/m) * np.sum(h - y)
        w -= learning_rate * dw
        bias -= learning_rate * db

        # Tính cost và lưu vào danh sách costs
        cost = compute_cost(X, y, w, bias)
        costs.append(cost)

    return w, bias, costs

# Đường dẫn đến file CSV
csv_file = 'Student_Performance.csv'
column_index = 5

# Chỉ định dòng bắt đầu và dòng kết thúc
start_row = 1
end_row = 6000

# Đọc file CSV và lấy dữ liệu từ các dòng chỉ định
data = pd.read_csv(csv_file, usecols=range(5), skiprows=range(1, start_row), nrows=(end_row - start_row + 1))
data1 = pd.read_csv(csv_file, usecols=[column_index], skiprows=range(1, start_row), nrows=(end_row - start_row + 1))

# Chuyển đổi dữ liệu thành mảng numpy
array_data_1d = data1.to_numpy().flatten()
array_data = data.values

# Chuẩn bị dữ liệu
X = array_data
y = array_data_1d.reshape(-1, 1)

# Chuẩn hóa dữ liệu
X = (X - np.mean(X, axis=0)) / np.std(X, axis=0)

# Thêm cột bias vào ma trận X
X = np.hstack((np.ones((X.shape[0], 1)), X))

# Thiết lập các tham số
w = np.random.rand(X.shape[1], 1)
bias = 1.0
learning_rate = 0.01
num_iterations = 1000

# Chạy gradient descent và lưu giá trị cost vào danh sách costs
w, bias, costs = gradient_descent(X, y, w, bias, learning_rate, num_iterations)

# Vẽ đồ thị loss theo số lần lặp
for i in range(num_iterations):
    print("Lần lặp:", i+1, " - Loss:", costs[i])
print(w)
features = data.iloc[:, :-1].values
labels = data.iloc[:, -1].values

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
train_size = int(0.6 * len(features))
train_features = features[:train_size]
train_labels = labels[:train_size]
test_features = features[train_size:]
test_labels = labels[train_size:]
# Vẽ đồ thị loss theo số lần lặp
# Vẽ đồ thị giữa X và y
plt.scatter(X[:, 1], y, color='blue', label='Actual')
plt.plot(X[:, 1], np.dot(X, w) + bias, color='red', label='Predicted')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Relationship between X and y')
plt.legend()
plt.show()