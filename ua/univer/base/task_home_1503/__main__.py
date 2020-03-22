import _csv

def csv_reader(file_obj):
    """
    Read a csv file
    """
    reader = csv_reader(file_obj)
    for row in reader:
        print(" ".join(row))


if __name__ == "__main__":
    csv_path = "action_plan_19_20.csv"
    with open(csv_path, "r") as f_obj:
        csv_reader(f_obj)



