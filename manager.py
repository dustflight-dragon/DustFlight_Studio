#!/usr/bin/env python
"""
Command-line utility for administrative tasks.

# For more information about this file, visit
# https://docs.djangoproject.com/en/2.1/ref/django-admin/
"""

import os
import sys

error_message = "Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?"


notifications_value = """
    Welcome to Enjoy DustFlight Professional System
    Maybe there are something error at current process running:
    [ERROR] =>
    """


def start_application():
    print("---------------------------------------------------------------------------------------")
    running_welcome_info
    print("[NOTICE] Engine Processing Running ====>>> [running_welcome_info] Successfully !")
    print("---------------------------------------------------------------------------------------")
    print("---------------------------------------------------------------------------------------")
    engine_processing_start()
    print("[NOTICE] Engine Processing Running ====>>> [engine_processing_start] Successfully !")
    print("---------------------------------------------------------------------------------------")


def running_welcome_info():
    print("##########################################################################")
    print("#                                    #")
    print("#  Wlecome to running DustFlight_VNS.wsgi Powered By DustFlight #")
    print("#                                    #")
    print("##########################################################################")


def engine_processing_start():
    try:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                              'DustFlight_Studio.settings')
        from django.core.management import execute_from_command_line
        execute_from_command_line(sys.argv)
    except Exception as ex:
        print("[NOTICE] Notifications Value => [%s]" %
              str(notifications_value))
        print("[INVALID] Running Django Project Engine Invalid By => [%s]" % str(ex))


def main():
    print("=======================================================================================")
    print(
        "#################################[Processing_Running!]#################################")
    start_application()
    print(
        "#################################[Processing_Running!]#################################")
    print("=======================================================================================")


if __name__ == '__main__':
    main()
