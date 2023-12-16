import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from sympy import symbols, lambdify
from sympy import sin, pi

def get_input_values():
    fs_input = entry_fs.get()
    T_input = entry_T.get()
    ff1_input = entry_ff1.get()
    ff2_input = entry_ff2.get()
    ff3_input = entry_ff3.get()

    try:
        Fs = float(fs_input)
        T = float(T_input)
        ff1 = float(ff1_input)
        ff2 = float(ff2_input)
        ff3 = float(ff3_input)
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ")
        return None

    return Fs, T, ff1, ff2, ff3

def apply_filter():
    input_values = get_input_values()
    if input_values is None:
        return

    Fs, T, ff1, ff2, ff3 = input_values

    t = np.linspace(0, T, int(T * Fs), endpoint=False)
    t_symbolic = symbols('t')
    signal_with_noise = (
            sin(2 * pi * ff1 * t_symbolic) +
            sin(2 * pi * ff2 * t_symbolic) +
            sin(2 * pi * ff3 * t_symbolic)
    )
    signal_with_noise_fn = lambdify(t_symbolic, signal_with_noise, modules='numpy')
    signal_with_noise_values = signal_with_noise_fn(t)

    filter_type = combo_filter.get()

    if filter_type == "Thông cao":
        cutoff_frequency = float(entry_cutoff.get())  # Lấy tần số cắt từ trường nhập liệu
        nyquist_frequency = 0.5 * Fs
        normal_cutoff = cutoff_frequency / nyquist_frequency
        b, a = signal.butter(4, normal_cutoff, btype='high', analog=False)
        filtered_signal = signal.filtfilt(b, a, signal_with_noise_values)
    elif filter_type == "Thông dải":
        low_cutoff = float(entry_low_cutoff.get())  # Lấy tần số cắt thấp từ trường nhập liệu
        high_cutoff = float(entry_high_cutoff.get())  # Lấy tần số cắt cao từ trường nhập liệu
        nyquist_frequency = 0.5 * Fs
        normal_low_cutoff = low_cutoff / nyquist_frequency
        normal_high_cutoff = high_cutoff / nyquist_frequency
        b, a = signal.butter(4, [normal_low_cutoff, normal_high_cutoff], btype='band', analog=False)
        filtered_signal = signal.filtfilt(b, a, signal_with_noise_values)
    elif filter_type == "Dải chắn":
        low_cutoff = float(entry_low_cutoff.get())  # Lấy tần số cắt thấp từ trường nhập liệu
        high_cutoff = float(entry_high_cutoff.get())  # Lấy tần số cắt cao từ trường nhập liệu
        nyquist_frequency = 0.5 * Fs
        normal_low_cutoff = low_cutoff / nyquist_frequency
        normal_high_cutoff = high_cutoff / nyquist_frequency
        b, a = signal.butter(4, [normal_low_cutoff, normal_high_cutoff], btype='bandstop', analog=False)
        filtered_signal = signal.filtfilt(b, a, signal_with_noise_values)
    elif filter_type == "Thông thấp":
        cutoff_frequency = float(entry_cutoff.get())  # Lấy tần số cắt từ trường nhập liệu
        nyquist_frequency = 0.5 * Fs
        normal_cutoff = cutoff_frequency / nyquist_frequency
        b, a = signal.butter(4, normal_cutoff, btype='low', analog=False)
        filtered_signal = signal.filtfilt(b, a, signal_with_noise_values)
    else:
        messagebox.showerror("Lỗi", "Bộ lọc không hợp lệ")
        return

    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    plt.plot(t, signal_with_noise_values, 'b-', label='Tín hiệu gốc')
    plt.xlabel('Thời gian (s)')
    plt.ylabel('Amplitude')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(t, filtered_signal, 'r-', label='Tín hiệu sau lọc')
    plt.xlabel('Thời gian (s)')
    plt.ylabel('Amplitude')
    plt.legend()

    plt.tight_layout()
    plt.show()

def filter_type_changed(event):
    selected_filter = combo_filter.get()
    if selected_filter in ["Thông thấp", "Thông cao"]:
        label_cutoff.grid(row=7, column=0)
        entry_cutoff.grid(row=7, column=1)
        label_low_cutoff.grid_remove()
        entry_low_cutoff.grid_remove()
        label_high_cutoff.grid_remove()
        entry_high_cutoff.grid_remove()
    elif selected_filter in ["Thông dải", "Dải chắn"]:
        label_cutoff.grid_remove()
        entry_cutoff.grid_remove()
        label_low_cutoff.grid(row=7, column=0)
        entry_low_cutoff.grid(row=7, column=1)
        label_high_cutoff.grid(row=8, column=0)
        entry_high_cutoff.grid(row=8, column=1)

# Tạo cửa sổ giao diện
window = tk.Tk()
window.title("Nhập thông số")

# Tạo các thành phần giao diện
label_fs = tk.Label(window, text="Tần số lấy mẫu (Fs):")
label_fs.grid(row=0, column=0)
entry_fs = tk.Entry(window)
entry_fs.grid(row=0, column=1)

label_T = tk.Label(window, text="Thời gian thu thập (T):")
label_T.grid(row=1, column=0)
entry_T = tk.Entry(window)
entry_T.grid(row=1, column=1)

label_ff1 = tk.Label(window, text="Tần số ff1:")
label_ff1.grid(row=2, column=0)
entry_ff1 = tk.Entry(window)
entry_ff1.grid(row=2, column=1)

label_ff2 = tk.Label(window, text="Tần số ff2:")
label_ff2.grid(row=3, column=0)
entry_ff2 = tk.Entry(window)
entry_ff2.grid(row=3, column=1)

label_ff3 = tk.Label(window, text="Tần số ff3:")
label_ff3.grid(row=4, column=0)
entry_ff3 = tk.Entry(window)
entry_ff3.grid(row=4, column=1)

label_filter = tk.Label(window, text="Chọn bộ lọc:")
label_filter.grid(row=5, column=0)
combo_filter = ttk.Combobox(window, values=["Thông cao", "Thông dải", "Dải chắn", "Thông thấp"])
combo_filter.grid(row=5, column=1)

# Thêm trường nhập liệu cho tần số cắt
label_cutoff = tk.Label(window, text="Tần số cắt:")
entry_cutoff = tk.Entry(window)

# Thêm trường nhập liệu cho tần số cắt thấp và tần số cắt cao
label_low_cutoff = tk.Label(window, text="Tần số cắt thấp:")
entry_low_cutoff = tk.Entry(window)
label_high_cutoff = tk.Label(window, text="Tần số cắt cao:")
entry_high_cutoff = tk.Entry(window)

# Gán sự kiện thay đổi loại bộ lọc
combo_filter.bind("<<ComboboxSelected>>", filter_type_changed)

button_apply = tk.Button(window, text="Áp dụng bộ lọc", command=apply_filter)
button_apply.grid(row=9, columnspan=2)

# Mặc định ẩn trường nhập liệu tần số cắt
label_cutoff.grid_remove()
entry_cutoff.grid_remove()
label_low_cutoff.grid_remove()
entry_low_cutoff.grid_remove()
label_high_cutoff.grid_remove()
entry_high_cutoff.grid_remove()

# Hiển thị cửa sổ
window.mainloop()