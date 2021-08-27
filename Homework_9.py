import os

################## 1 #############################

path = "HW"
filename = "domains.txt"
path_filename = os.path.join(path, filename)

def do_list_domains(path_filename: str) -> list:
    with open(path_filename, "r") as txt_file:
        return [line.strip()[1:] for line in txt_file.readlines()]

result_list = do_list_domains(path_filename)

################## 2 ################################

path = "HW"
filename = "names.txt"
path_filename = os.path.join(path, filename)

def get_second_names(path_filename):
    with open(path_filename, "r") as file:
        return [line.split("\t")[1] for line in file.readlines()]

################## 3 ################################

path = "HW"
filename = "authors.txt"
path_filename = os.path.join(path, filename)

from datetime import datetime

my_month = datetime.strptime("February", "%B").month

date = "26th Feb 1802"
day, month, year = date.split()
res_date = f"{day[:-2]} {month} {year}"
my_date = datetime.strptime(res_date, "%d %b %Y")
my_date = datetime.strftime(my_date, "%d/%m/%Y")


def get_only_dates(path_filename):
    """
    :param filename:
    :return:
    """
    result = []
    with open(path_filename, "r") as file:
        for line in file.readlines():
            my_line = line.split(" - ")
            if len(my_line) > 1:
                date = my_line[0]
                day, month, year = date.split()
                my_date = datetime.strptime(f"{day[:-2]} {month} {year}", "%d %B %Y")
                result.append(
                    {
                        "date_original": date,
                        "date_modified": datetime.strftime(my_date, "%d/%m/%Y"),
                    }
                )
    return result

