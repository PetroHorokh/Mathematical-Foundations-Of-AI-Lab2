import random
from datetime import datetime
import supporting_functions as sup_fun

random.seed(datetime.now().timestamp())

N = 100
a = [0, 1]
b = [1, 2]

sup_fun.mc_main_function(a[1], b[1], N)
sup_fun.mc_test_function(a[0], b[0], N)
