import gi

gi.require_version("Gtk", "3.0")
gi.require_version('Notify', '0.7')
from gi.repository import Gtk
from gi.repository import Notify


def notification_callback(notification):
    Gtk.main_quit()


class NotifyViewer:
    def __init__(self, title="Title", content="This is the content"):
        Notify.init(title)
        self.notification = Notify.Notification.new(title, content, None)
        self.notification.connect("closed", notification_callback)

    def run(self):
        self.notification
        self.notification.show()
        Gtk.main()
