import _csv
with open('prognoz.csv', newline='') as File:
    reader = _csv.reader(File)
    headers = next(reader)
    print(headers)
    for row in reader:
        print(row)

"""
with open('action_plan_19_20.csv', newline='') as File:
    columns = ["№ з/п",
               "Показник",
               "2019 рік (прогноз)сценарій 1",
               "2019 рік (прогноз)сценарій 2",
               "2019 рік (прогноз)сценарій 3",
               "2020 рік (прогноз)сценарій 1",
               "2020 рік (прогноз)сценарій 2",
               "2020 рік (прогноз)сценарій 3"]
    writer = _csv.dictwriter(File, fieldnames=columns)
    writer.writeheader()
    writer.writerows()
    reader = _csv.reader(File)
    for row in reader:
        print(row)
"""