#!/usr/bin/env python3
import re
import operator
import csv

per_user = {}
error = {}

with open("syslog.log") as file:
    for line in file:
        line.strip()
        if "ERROR" or "INFO" in line:                         # working on per_user dictionary
            pattern = re.search(r"\(([^ ]+)\)$", line)
            username = pattern.group(1)
            if username not in per_user:
                per_user[username] = {"INFO": 0, "ERROR": 0}
            if "INFO" in line:
                per_user[username]["INFO"] += 1
            elif "ERROR" in line:
                per_user[username]["ERROR"] += 1
                pattern = re.search(r"ERROR:? (.+) \(", line)  # working on error dictionary
                error_name = pattern.group(1)
                if error_name not in error:
                    error[error_name] = 0
                error[error_name] += 1

error = sorted(error.items(), key=operator.itemgetter(1), reverse=True)
per_user = sorted(per_user.items(), key=operator.itemgetter(0))

with open("error_message.csv", "w") as error_file:
    fieldnames = ["Error", "Count"]
    writer = csv.DictWriter(error_file, fieldnames=fieldnames)
    writer.writeheader()
    for element in error:
        writer.writerow({"Error": element[0], "Count": element[1]})

with open("user_statistics.csv", "w") as stat_file:
    fieldnames = ["Username", "INFO", "ERROR"]
    writer = csv.DictWriter(stat_file, fieldnames=fieldnames)
    writer.writeheader()
    for element in per_user:
        writer.writerow({"Username": element[0], "INFO": element[1]["INFO"], "ERROR": element[1]["ERROR"]})
