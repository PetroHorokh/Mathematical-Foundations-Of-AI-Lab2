import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
import function as fun


def deviation(root, value):
    absolute_deviation, relative_deviation = np.abs(root - value), np.abs((root - value) / value)

    print("\nAbsolute deviation:")
    print(absolute_deviation)
    print("\nRelative deviation:")
    print(relative_deviation)


def precise_integration(a, b, function):
    result, error = quad(function, a, b)

    print("\nPrecise integration:")
    print(result)

    return result


def generate_dots(a, b, function, i):
    x_val = np.random.uniform(a, b, size=(i + 1) * 1000)
    line_val = function(x_val)

    y_val = np.random.uniform(0, line_val)

    return x_val, y_val


def mc_main_function(a, b, n):
    mc_estimates = np.zeros(n)
    mc_std = np.zeros(n)

    for i in range(n):
        x_val, y_val = generate_dots(a, b, fun.function, i)
        mc_estimates[i] = np.mean(y_val) * 2
        mc_std[i] = np.std(y_val) / np.sqrt((i + 1) * 1000)

    integration = precise_integration(a, b, fun.function)

    deviation(integration, mc_estimates)

    plt.plot([integration] * n)
    plt.plot(mc_estimates, '.')
    plt.plot(integration + np.array(mc_std) * 3, 'r')
    plt.plot(integration - np.array(mc_std) * 3, 'r')
    plt.xlabel('Sample size')
    plt.ylabel('Monte Carlo estimate')
    plt.xticks(plt.xticks()[0], plt.xticks()[0].astype(int) * 1000 + 1000)
    plt.show()


def mc_test_function(a, b, n):
    mc_estimates = np.zeros(n)
    mc_std = np.zeros(n)

    for i in range(n):
        x_val, y_val = generate_dots(a, b, fun.function_test, i)
        mc_estimates[i] = np.mean(y_val) * 2
        mc_std[i] = np.std(y_val) / np.sqrt((i + 1) * 1000)

    integration = precise_integration(a, b, fun.function_test)

    deviation(integration, mc_estimates)

    plt.plot([integration] * n)
    plt.plot(mc_estimates, '.')
    plt.plot(integration + np.array(mc_std) * 3, 'r')
    plt.plot(integration - np.array(mc_std) * 3, 'r')
    plt.xlabel('Sample size')
    plt.ylabel('Monte Carlo estimate')
    plt.xticks(plt.xticks()[0], plt.xticks()[0].astype(int) * 1000 + 1000)
    plt.show()
