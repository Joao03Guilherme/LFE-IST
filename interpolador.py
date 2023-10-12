class Interpolator:
    def __init__(self, xdata = None, ydata = None):
        self.xdata = xdata
        self.ydata = ydata

    def sort_data(self):
        combined_lists = list(zip(self.xdata, self.ydata))
        sorted_combined = sorted(combined_lists, key=lambda x: x[0])
        self.xdata, self.ydata = zip(*sorted_combined)

    def interpolate(self, x):
        """
        Returns interpolated value of y at x. Using an approximation of a straight line between two points.
        """

        self.sort_data()

        if x < self.xdata[0] or x > self.xdata[-1]:
            raise ValueError('x out of bounds')

        for i in range(len(self.xdata) - 1):
            if x >= self.xdata[i] and x <= self.xdata[i + 1]:
                return self.ydata[i] + (x - self.xdata[i]) * (self.ydata[i + 1] - self.ydata[i]) / (self.xdata[i + 1] - self.xdata[i])

# Read a excel with two columns x and y
xdata = []
ydata = []

with open('TEMPERATURA.csv', 'r') as file:
    for line in file:
        x, y = line.split(',')
        xdata.append(float(x))
        ydata.append(float(y))


def derivative(xdata, ydata):
    ddata = []
    ddata.append((ydata[1]-ydata[0])/(xdata[1]-xdata[0]))
    for i in range(1, len(xdata)-1):
        ddata.append((ydata[i+1]-ydata[i-1])/(xdata[i+1]-xdata[i-1]))
    ddata.append((ydata[-1]-ydata[-2])/(xdata[-1]-xdata[-2]))
    return ddata


IT = Interpolator(xdata, ydata)

while(1):
    i = float(input())
    n = IT.interpolate(i)
    print(n)

# d = derivative(ydata, xdata)
#
# def moving_average(data, window_size):
#     if window_size <= 0:
#         raise ValueError("Window size must be greater than 0")
#
#     moving_averages = []
#
#     for i in range(len(data)):
#         start = max(0, i - window_size + 1)
#         window = data[start:i + 1]
#         average = sum(window) / len(window)
#         moving_averages.append(average)
#
#     return moving_averages
#
# mov = moving_average(d, 10)
# for e in range(len(mov)):
#     print(ydata[e], mov[e], sep=',')
