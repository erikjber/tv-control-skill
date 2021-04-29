from mycroft import MycroftSkill, intent_file_handler


class TvControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('control.tv.intent')
    def handle_control_tv(self, message):
        self.speak_dialog('control.tv')


def create_skill():
    return TvControl()

