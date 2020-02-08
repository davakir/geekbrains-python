import json

firms_data1 = {'firms_count': 0, 'profits': 0}
firms_data = []

firms_count = 0
firms_profits = 0
with open(r'files/firms.txt') as file:
    for line in file.readlines():

        firm_info = line.split()
        revenue = int(firm_info[2])
        costs = int(firm_info[3])
        profit = revenue - costs
        if profit > 0:
            firms_count += 1
            firms_profits += profit

        firm_name = firm_info[0]
        firms_data.append({firm_name: profit})

firms_data.append({'average_profit': format(firms_profits / firms_count, '.2f')})
firms_info = json.dumps(firms_data)

print(firms_info)
