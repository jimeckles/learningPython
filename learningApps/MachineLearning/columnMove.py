import pandas as pd


def move_column_to_end(csv_file, column_name):
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Get the column to move
    col = df[column_name]

    # Remove the column from its current position
    df = df.drop(columns=[column_name])

    # Add the column back at the end
    df[column_name] = col

    # Save back to CSV
    df.to_csv(csv_file, index=False)


if __name__ == "__main__":
    # Get input from user
    # file_path = input("Enter the CSV file path: ")
    file_path = "learningApps/MachineLearning/data/ThousandsBlockAssignment_All.csv"
    # col_name = input("Enter the column name to move: ")
    col_name = "Block Available Date"

    try:
        move_column_to_end(file_path, col_name)
        print(f"Successfully moved column '{col_name}' to the end of the CSV file")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
