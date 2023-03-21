import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit


def main():
    print("program just started")
    # read the CSV file into a Pandas DataFrame
    print("Reading data from  ...")

    df = pd.read_csv('data.csv', header=0, delimiter='\t')

    print("\t data read successfully")

    # extract column A and column B
    # extract column A and column B using positional indexing
    print(df.columns)
    print("extracting columns...")
    column_A = df['column_A']
    column_B = df['column_B']

    # create a figure with a single set of axes
    print("plotting started wait a moment background indexing to finish")
    fig, ax = plt.subplots(figsize=(10, 5))

    # plot the original graph
    ax.plot(column_A, column_B, label='Original')
    ax.axhline(y=0, color='black', linewidth=0.5)  # add horizontal line at y=0
    ax.axvline(x=0, color='black', linewidth=0.5)  # add vertical line at x=0

    # plot the reflected graph
    reflected_column_A = column_A * -1  # negate the values of column A
    ax.plot(reflected_column_A, column_B, label='Reflected')
    ax.axhline(y=0, color='black', linewidth=0.5)  # add horizontal line at y=0
    ax.axvline(x=0, color='black', linewidth=0.5)  # add vertical line at x=0

    # define a function to fit the data
    def func(x, a, b, c, d):
        return a * np.sin(b * x + c) + d

    # perform the curve fitting
    popt, pcov = curve_fit(func, column_A, column_B, maxfev=10000)

    # print the optimal parameters
    print("Optimal parameters: ", popt)

    # plot the curve fit
    x_fit = np.linspace(column_A.min(), column_A.max(), 1000)
    y_fit = func(x_fit, *popt)
    ax.plot(x_fit, y_fit, label='Curve Fit')
    ax.legend()

    # add the equations to the plot
    eq1 = f'Original: y = f(x)'
    eq2 = f'Reflected: y = f(-x)'
    eq3 = f'Curve Fit: y = {popt[0]:.2f} sin({popt[1]:.2f}x + {popt[2]:.2f}) + {popt[3]:.2f}'
    ax.text(0.05, 0.95, eq1, transform=ax.transAxes, fontsize=12, verticalalignment='top')
    ax.text(0.05, 0.90, eq2, transform=ax.transAxes, fontsize=12, verticalalignment='top')
    ax.text(0.05, 0.85, eq3, transform=ax.transAxes, fontsize=12, verticalalignment='top')

    ax.set_xlabel('Column A')
    ax.set_ylabel('Column B')
    ax.set_title('the graph of data.csv record A vs. B')
    ax.legend()

    print("graph preparing to show in GUI window")
    plt.show()


if __name__ == '__main__':
    main()
