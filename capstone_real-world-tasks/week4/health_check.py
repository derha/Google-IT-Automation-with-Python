#!/usr/bin/env python3

import os
import psutil
import emails
import socket


def subject_line(issue):
    """Decide what subject line should be used in email"""
    if issue == "cpu_usage":
        return "Error - CPU usage is over 80%"
    elif issue == "disk_space":
        return "Error - Available disk space is less than 20%"
    elif issue == "memory":
        return "Error - Available memory is less than 500MB"
    elif issue == "localhost":
        return "Error - localhost cannot be resolved to 127.0.0.1"


def cpu_usage_check(issues):
    """Check if CPU usage is over 80%"""
    if psutil.cpu_percent(1) > 80:
        issues["cpu_usage"] = True


def disk_space_check(issues):
    """Check if available disk space is lower than 20%"""
    disk_usage = psutil.disk_usage('/')
    if disk_usage.percent > 80:
        issues["disk_space"] = True


def memory_check(issues):
    """Check if available memory is less than 500MB"""
    memory = psutil.virtual_memory()
    threshold = 500 * 1024 * 1024  # 500MB
    if memory.available < threshold:
        issues["memory"] = True


def localhost_check(issues):
    """Check if hostname 'localhost' cannot be resolved to '127.0.0.1'"""
    if socket.gethostbyname("localhost") != "127.0.0.1":
        issues["localhost"] = True


def all_checks():
    """Make all necessary health checks"""
    issues = {"cpu_usage": False, "disk_space": False, "memory": False, "localhost": False}
    cpu_usage_check(issues)
    disk_space_check(issues)
    memory_check(issues)
    localhost_check(issues)
    return issues


def main():
    # detect if there're any issues
    issues = all_checks()
    for issue, status in issues.items():
        # if there's an issue, send an email
        if status:
            sender = "automation@example.com"
            receiver = "{}@example.com".format(os.environ.get('USER'))
            subject = subject_line(issue)
            body = "Please check your system and resolve the issue as soon as possible"
            message = emails.generate_email(sender, receiver, subject, body)
            emails.send_email(message)


if __name__ == "__main__":
    main()
