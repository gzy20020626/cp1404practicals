"""
function main()
    records = load_data(FILE_NAME)
    champion_count_dict, countries = process_data(records)
    display_data(champion_count_dict, countries)
    
function load_data(file_name)
    open file for reading as in_file:
        skip header
        for line in in_file:
            record = line.strip().split(',')
            records.append(record)
    return records
    
function process_data(records)
    for record in records:
        country = record[1]
        champion_name = record[2]
        get win_time from dict
        if win_time == 0:
            dict[name]=1
        else:
            dict[name]+=1
        countries.add(country)
    countries = sorted(countries)
    return dict, countries
    
function display_data(champion_count_dict, countries)
    for name, times in champion_count_dict.items():
        print name times
    print countries
    
"""

FILE_NAME = "wimbledon.csv"


def main():
    records = load_data(FILE_NAME)
    champion_count_dict, countries = process_data(records)
    display_data(champion_count_dict, countries)


def load_data(file_name):
    records = []
    with open(file_name, "r", encoding="utf-8-sig") as in_file:
        header = in_file.readline()
        for line in in_file:
            record = line.strip().split(',')
            records.append(record)

    return records


def process_data(records):
    champion_count_dict = {}
    countries = set()

    for record in records:
        country = record[1]
        champion_name = record[2]

        win_times = champion_count_dict.get(champion_name, 0)
        if win_times == 0:
            champion_count_dict[champion_name] = 1
        else:
            champion_count_dict[champion_name] += 1

        countries.add(country)
    countries = sorted(countries)

    return champion_count_dict, countries


def display_data(champion_count_dict, countries):
    print("Wimbledon Champions: ")
    for name, times in champion_count_dict.items():
        print(f"{name} {times}")

    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(country for country in sorted(countries)))


main()
