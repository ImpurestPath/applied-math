import numpy as np
import scipy.stats 
import math
import random


class Gauss:


    def __init__(self):
        self.numbers = []

    def create_sample(self, n, mu, sigma):
        self.numbers = []
        for i in range(n):
            self.numbers.append(random.normalvariate(mu, sigma))

    def get_sample(self):
        return self.numbers

    def sign_test(self, a):
        #Page 337 
        """
        
        """
        # critical_values = {
        #     0.01 : 3,
        #     0.05 : 5,
        #     0.1 : 5
        # }
        numbers = np.array(self.numbers)
        positive = np.sum(numbers > a)
        negative = np.sum(numbers < a)
        n = positive + negative
        F = positive / (n - negative + 1)
        df1 = 2 * (n - positive + 1)
        df2 = 2 * positive
        p_value = scipy.stats.f.cdf(F, df1, df2)
        p_value = 2 * min(p_value, 1 - p_value)
        return p_value

    def wilcoxon_test(self, a):
        # Page 339
        # critical_values = {
        #     0.01 : 166,
        #     0.05 : 149,
        #     0.1 : 139
        # }
        y_sorted = sorted(self.numbers, key=abs)
        y = {}
        for i in range(len(y_sorted)):
            y[i] = [x for x in self.numbers if abs(x) == y_sorted[i]]

        T = 0
        for key, numbers in y.items():
            k = len([x for x in numbers if x > 0])
            if k > 0:
                T += k * key
        
        n = len(self.numbers)
        M = n * (n + 1) / 4
        D = M * (2 * n + 1) / 6
        p_value = scipy.stats.norm.cdf(T, M, D)
        p_value = 2 * min(p_value, 1 - p_value)
        return p_value
        
        


        
