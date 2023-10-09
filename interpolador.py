class Interpolator:
    def __init__(self, xdata = None, ydata = None):
        self.xdata = xdata
        self.ydata = ydata

    def sort_data(self):
        self.xdata.sort()
        self.ydata.sort()

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

IT = Interpolator(xdata, ydata)

n = IT.interpolate(2000)
print(n)


