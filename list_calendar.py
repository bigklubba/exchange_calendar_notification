#!/bin/env python3
import gi

from exchange_calendar_connection import ExchangeCalendarConnection
from notify_viewer import NotifyViewer

gi.require_version("Gtk", "3.0")
gi.require_version('Notify', '0.7')


def main():
    exchange_connection = ExchangeCalendarConnection()
    agenda_events = exchange_connection.get_todays_events()
    agenda_events_info = exchange_connection.get_short_event_info(agenda_events)
    agenda_s = ""
    for event_info in agenda_events_info:
        agenda_s += event_info
        agenda_s += "\n"

    notification = NotifyViewer("Agenda", agenda_s)
    notification.run()

if __name__ == '__main__':
    main()
