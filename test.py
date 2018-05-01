from visualization import *

x_data1 = np.random.rand(1000)
y_data1 = np.random.rand(1000)

x_data2 = np.arange(100)
y_data2 = 2 * np.arange(100) + np.random.randn(100)

x_data3 = np.random.randn(1000)
y_data3 = np.random.randn(1000)

x_data4 = list('abcd')
y_data4 = [100, 150, 200, 250]
y_err4 = [10, 15, 20, 20]

x_data5 = list('abcd')
y_data5 = [[100, 150, 200, 250], [110, 140, 198, 270]]
y_err5 = [[10, 15, 20, 20], [10, 15, 20, 20]]
colors5 = ['r', 'g']

# scatterplot(x_data1, y_data1)   
# lineplot(x_data2, y_data2)
# histogram(x_data1, 20)
# overlaid_histogram(6 * x_data1 - 3, x_data3)
# barplot(x_data4, y_data4, y_err4, x_label='', y_label='', title='')
# group_barplot(x_data5, y_data5, colors5, y_err5, y_data_names=['r', 'b'])
stack_barplot(x_data5, y_data5, colors5, y_data_names=['r', 'b'])