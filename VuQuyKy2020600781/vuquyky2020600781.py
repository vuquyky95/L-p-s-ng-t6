# Đoạn code đề cho
# Import thư viện sympy để sử dụng các tính năng tích phân và định nghĩa hai hàm để tính toán tích phân không xác định và tích phân xác định
from sympy import *
x = Symbol('x')
ans1=diff(sin(x)*exp(x), x)
print("derivative of sin(x)*e^x: ", ans1)
ans2=integrate(exp(x)*sin(x)+exp(x)*cos(x), x)
print("indefinite integration is : ", ans2)
ans3 = integrate(sin(x**2), (x, -oo,oo))
print("definite integration is : ", ans3)
ans4=limit(sin(x)/x,x,0)
print("limit is : ", ans4)
ans5 = solve(x**2 - 2,x)
print("roots are: ", ans5)

# Import thư viện tkinter để xây dựng giao diện người dùng

# Phát triển thành phần mềm tính tích phân

# Thêm các nút tính tích phân xác định, tích phân không xác định , thông tin, các ô text điền dữ liệu

import tkinter as tk
from tkinter import ttk, messagebox

# Hàm tính tích phân không xác định
def indefinite_integral(expression, variable):
    x = Symbol(variable)
    return integrate(expression, x)

# Hàm tính tích phân xác định
def definite_integral(expression, variable, lower_limit, upper_limit):
    x = Symbol(variable)
    return integrate(expression, (x, lower_limit, upper_limit))

# Hàm thực hiện tính toán và hiển thị kết quả tích phân không xác định
def calculate_indefinite_integral():
    expression = entry_expression.get()
    variable = entry_variable.get()
    result = indefinite_integral(expression, variable)
    result_label.config(text=f"Kết quả tích phân không xác định là: {result}")

# Hàm thực hiện tính toán và hiển thị kết quả tích phân xác định
def calculate_definite_integral():
    expression = entry_expression.get()
    variable = entry_variable.get()
    lower_limit = entry_lower_limit.get()
    upper_limit = entry_upper_limit.get()

    try:
        lower_limit = float(lower_limit)
        upper_limit = float(upper_limit)
        result = definite_integral(expression, variable, lower_limit, upper_limit)
        result_label.config(text=f"Kết quả tích phân xác định là: {result}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập giới hạn là số.")

# Hàm hiển thị thông tin "About"
def show_about():
    messagebox.showinfo("About", "Phần mềm tính toán phép tích phân sử dụng sympy và tkinter")

# Tạo cửa sổ chính của ứng dụng
root = tk.Tk()
root.title("Tính toán Phép Tích Phân")

# Tạo các thành phần giao diện người dùng
label_expression = tk.Label(root, text="Nhập biểu thức:")
label_variable = tk.Label(root, text="Nhập biến:")
label_lower_limit = tk.Label(root, text="Nhập giới hạn dưới:")
label_upper_limit = tk.Label(root, text="Nhập giới hạn trên:")

entry_expression = tk.Entry(root)
entry_variable = tk.Entry(root)
entry_lower_limit = tk.Entry(root)
entry_upper_limit = tk.Entry(root)

button_calculate_indefinite = tk.Button(root, text="Tính tích phân không xác định", command=calculate_indefinite_integral)
button_calculate_definite = tk.Button(root, text="Tính tích phân xác định", command=calculate_definite_integral)
button_about = tk.Button(root, text="About", command=show_about)

result_label = tk.Label(root, text="Kết quả sẽ được hiển thị ở đây.")

# Định vị các thành phần trong cửa sổ
label_expression.grid(row=0, column=0, padx=10, pady=5)
label_variable.grid(row=1, column=0, padx=10, pady=5)
label_lower_limit.grid(row=2, column=0, padx=10, pady=5)
label_upper_limit.grid(row=3, column=0, padx=10, pady=5)

entry_expression.grid(row=0, column=1, padx=10, pady=5)
entry_variable.grid(row=1, column=1, padx=10, pady=5)
entry_lower_limit.grid(row=2, column=1, padx=10, pady=5)
entry_upper_limit.grid(row=3, column=1, padx=10, pady=5)

button_calculate_indefinite.grid(row=4, column=0, columnspan=2, pady=10)
button_calculate_definite.grid(row=5, column=0, columnspan=2, pady=10)
button_about.grid(row=6, column=0, columnspan=2, pady=10)

result_label.grid(row=7, column=0, columnspan=2, pady=10)

# Bắt đầu vòng lặp giao diện người dùng
root.mainloop()
