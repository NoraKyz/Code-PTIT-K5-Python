# Cho 2 dữ liệu về chuyến bay và lương của nhân viên, sử dụng các thư viện tương ứng để thống kê dữ liệu:
# - Tìm giá trí lớn nhất, nhỏ nhất, trung bình theo tên cột được nhập vào (với các cột kiểu số), vẽ và hiễn thị biểu đồ tương ứng (dạng scatter)
# - Hiển thị biểu đồ biến thiên ngày tháng và distance(flights.csv); biểu đồ thống kê sex đạng cột (Salaries.csv);
# - Sắp xếp dữ liệu theo tên cột được nhập vào, vẽ và hiễn thị biểu đồ tương ứng

import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ CSV
flights = pd.read_csv('flights.csv')
salaries = pd.read_csv('salaries.csv')


def statistics(dataframe, column_name):
    max_val = dataframe[column_name].max()
    min_val = dataframe[column_name].min()
    avg_val = dataframe[column_name].mean()
    return max_val, min_val, avg_val


column_name = input("Enter column name to statistic: ")
max_val, min_val, avg_val = statistics(flights, column_name)
print(f"Max: {max_val}, Min: {min_val}, Avg: {avg_val}")

# Vẽ biểu đồ scatter
x = [1, 2, 3]
values = [min_val, avg_val, max_val]
plt.scatter(x, values, color='red', label=column_name)
plt.plot(x, values, color='blue', linestyle='dotted')
for i in range(len(x)):
    plt.annotate(f'{round(values[i], 1)}', (x[i], values[i]),
                 textcoords="offset points", xytext=(0, 10), ha='center')
plt.xticks(x, ['Min', 'Avg', 'Max'])
plt.title(f'Statistics of {column_name}')
plt.legend()
plt.show()

# Hiển thị biểu đồ biến thiên ngày tháng và distance
flights['date'] = pd.to_datetime(flights[['year', 'month', 'day']])
plt.figure(figsize=(18, 6))
flights.groupby('date')['distance'].sum().plot()
plt.title('Biến thiên ngày tháng và distance')
plt.ylabel('Distance')
plt.xlabel('Date')
plt.show()

# Biểu đồ thống kê sex
salaries['sex'].value_counts().plot(kind='bar')
plt.title('Thống kê giới tính')
plt.ylabel('Số lượng')
plt.xlabel('Giới tính')
plt.show()

# Sắp xếp dữ liệu
column_name_to_sort = input("Enter column name to sort: ")

if column_name_to_sort in flights.columns or column_name_to_sort in salaries.columns:
    if column_name_to_sort in flights.columns:
        dataframe_used = flights
    else:
        dataframe_used = salaries

    sorted_data = dataframe_used.sort_values(by=column_name_to_sort)
    
    plt.scatter(range(len(sorted_data)), sorted_data[column_name_to_sort])  # Use range(len(sorted_data)) as x values
    plt.title(f'Sorted data based on {column_name_to_sort}')
    plt.xlabel('Index')
    plt.ylabel(column_name_to_sort)
    plt.show()
else:
    print("Column name does not exist.")

