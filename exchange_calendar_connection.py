import os
from datetime import datetime, timedelta
from pyexchange import Exchange2010Service
from pyexchange import ExchangeNTLMAuthConnection
from pytz import timezone

FILE_PATH = os.path.dirname(os.path.abspath(__file__))
URL = u'https://mail.ist.com/ews/exchange.asmx'
USERNAME = u'IST\pieem'
PASSWORD = open(FILE_PATH + "/" + ".password", "r").read()[:-1]
TIMEZONE = timezone("Europe/Stockholm")


class ExchangeCalendarConnection:
    def __init__(self, url=URL, username=USERNAME, password=PASSWORD):
        connection = ExchangeNTLMAuthConnection(url, username, password)
        self.service = Exchange2010Service(connection)

    def get_todays_events(self):
        today = datetime.now(TIMEZONE).replace(hour=0, minute=0, second=0, microsecond=0);
        next_day = today + timedelta(days=1)
        events = self.service.calendar().list_events(
            start=today,
            end=next_day
        )
        return events

    @staticmethod
    def get_short_event_info(events):
        event_infos = []
        for event in events.events:
            event_info = "{subject} \n{start} -> {stop}".format(
                start=str(event.start.astimezone(TIMEZONE))[:-9],
                stop=str(event.end.astimezone(TIMEZONE))[:-9],
                subject=event.subject
            )
            event_infos.append(event_info)

        return event_infos
