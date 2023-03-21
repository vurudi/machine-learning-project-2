import matplotlib.pyplot as plt
import pandas as pd


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
    # create a scatter plot of column A against column B using Matplotlib
    print("plotting started wait a moment background indexing to finish")
    plt.scatter(column_A, column_B)
    plt.xlabel('Column A')
    plt.ylabel('Column B')
    plt.title('the graph of data.csv record A vs. B')
    print("graph preparing to show in GUI window")
    plt.show()


if __name__ == '__main__':
    main()
