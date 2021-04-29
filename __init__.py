from mycroft import MycroftSkill, intent_file_handler
import pychromecast


class TvControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        print("getting chromecasts")
        chromecasts  = pychromecast.get_chromecasts()
        self.cast = [c for c in chromecasts if c.device.friendly_name == 'TVn'][0]
        print("got cast")
        self.cast.wait()
        print("waited for cast")

    def get_media_controller(self):
        mc = self.cast.media_controller
        mc.block_until_active()
        return mc

    @intent_file_handler('control.tv.start.intent')
    def handle_control_tv(self, message):
        print("starting tv")
        self.get_media_controller().start()

    @intent_file_handler('control.tv.pause.intent')
    def handle_control_tv(self, message):
        self.get_media_controller().pause()


    @intent_file_handler('control.tv.stop.intent')
    def handle_control_tv(self, message):
        self.get_media_controller().stop()


def create_skill():
    return TvControl()

