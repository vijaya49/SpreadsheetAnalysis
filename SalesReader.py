import csv


def read_data():
    data = []
    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)
    return data


def sales_list():
    data = read_data()
    sales = []
    for i in data:
        sales.append(int(i['sales']))
    return sales


def run():
    data = read_data()
    my_dict = {}
    sales = []
    for i in data:
        sales.append(int(i['sales']))
        total=sum(sales)
        my_dict[i['month']] = (int(i['sales']))

    max_key = list(my_dict)[0]
    min_key = list(my_dict)[0]

    for key, value in my_dict.items():
        if value > my_dict[max_key]:
            max_key = key
        if value < my_dict[min_key]:
            min_key = key

    avg = 0
    sales_li = sales_list()
    for i in sales_li:
        avg+=i/12

    return total,min_key,my_dict[min_key],max_key,my_dict[max_key], avg


