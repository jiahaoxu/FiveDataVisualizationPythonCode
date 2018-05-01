from visualization import *

x_data1 = np.random.rand(1000)
y_data1 = np.random.rand(1000)

x_data2 = np.arange(100)
y_data2 = 2 * np.arange(100) + np.random.randn(100)

x_data3 = np.random.randn(1000)
y_data3 = np.random.randn(1000)

# scatterplot(x_data1, y_data1)   
# lineplot(x_data2, y_data2)
# histogram(x_data1, 20)
overlaid_histogram(6 * x_data1 - 3, x_data3)