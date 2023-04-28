import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def read_csv_log(file_path):
    df = pd.read_csv(file_path, sep=";")
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    return df


def visualize_logs(df):
    sns.set(style="whitegrid")

    plt.figure(figsize=(15, 8))
    sns.lineplot(data=df, x='timestamp', y='value')
    plt.title("Value over Time")
    plt.xlabel("Timestamp")
    plt.ylabel("Value")
    plt.show()


def main():
    csv_file_path = "LOG DATA.csv"
    log_data = read_csv_log(csv_file_path)
    visualize_logs(log_data)


if __name__ == "__main__":
    main()
