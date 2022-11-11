class Std:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    @property
    def n(self):
        return len(self.x)
        
    @property   
    def avg_x(self):
        return sum(self.x) / self.n
    
    @property   
    def avg_y(self):
        return sum(self.y) / self.n
    
    @property
    def x_varianza(self):
        de = sum([(xi - self.avg_x)**2 for xi in self.x])
        return de /self.n


    def y_varianza_or_quasi(self, quasi = False):
        if quasi == True:
            de = sum([(yi - self.avg_y)**2 for yi in self.y])
            return de/(self.n - 1)
        else:
            de = sum([(yi - self.avg_y)**2 for yi in self.y])
            return de/self.n

    @property
    def covariance(self):
        de = sum((xi * yi for xi, yi in zip(self.x, self.y)))
        first_term = de/self.n
        return first_term - self.avg_x * self.avg_y

    @property
    def r(self):
        de = self.covariance
        nu = ((self.x_varianza) ** 0.5 ) * ((self.y_varianza)** 0.5)
        return de/nu

    @property
    def B(self):
        nu = self.n * sum((xi * yi for xi, yi in zip(self.x, self.y))) - (sum(self.x) * sum(self.y))
        de = self.n * sum(xi ** 2 for xi in self.x) - sum(self.x) **2
        return nu/de

    @property
    def B0(self):
        return self.avg_y - self.B*self.avg_x

    @property
    def lineals(self):
        return tuple(self.y_prediction(week) for week in self.x)

    def y_prediction(self, x_value):
        return self.B * x_value + self.B0
        

    def __str__(self):
        return f"x: {self.x}\ny: {self.y}\nn: {self.n()}\n"

    
    

# a = std ([1,2,3],[10,20,30])
# print(a.avg_y)

# print(a.covariance)

# print(a.y_prediction(5))
