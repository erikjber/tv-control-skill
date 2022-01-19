from mycroft import MycroftSkill, intent_file_handler
import pychromecast


class TvControl(MycroftSkill):

    def __init__(self):
        print("TvControl constructor")
        self.mc = None
        MycroftSkill.__init__(self)


    def get_media_controller(self):
        print("Initing chromecast.")
        chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=["TVn"])
        print("Chromecasts found")
        cast = chromecasts[0]
        print("Got chromecast "+str(cast))
        cast.wait()
        print("Waited for chromecast")
        self.mc = cast.media_controller
        self.mc.block_until_active()
        print("controller active")
        #pychromecast.discovery.stop_discovery(browser)
        browser.stop_discovery()
        print("Init complete")

        return self.mc


    @intent_file_handler('control.tv.start.intent')
    def handle_control_tv_start(self, message):
        print("starting tv")
        self.get_media_controller().play()

    @intent_file_handler('control.tv.pause.intent')
    def handle_control_tv_pause(self, message):
        print("pause tv")
        self.get_media_controller().pause()

    @intent_file_handler('control.tv.stop.intent')
    def handle_control_tv_stop(self, message):
        print("stop tv")
        self.get_media_controller().stop()


def create_skill():
    return TvControl()

