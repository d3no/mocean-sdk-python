from moceansdk.modules.command.mc_object import tg_send_text, tg_send_animation, tg_send_audio, tg_send_document, tg_send_photo, tg_send_video, tg_request_contact, send_sms, wa_send_audio, wa_send_contact, wa_send_document, wa_send_location, wa_send_photo, wa_send_sticker, wa_send_text, wa_send_video, wa_send_with_template


class Mc():

    @staticmethod
    def telegram_send_text():
        return tg_send_text.TgSendText()

    @staticmethod
    def telegram_send_animation():
        return tg_send_animation.TgSendAnimation()

    @staticmethod
    def telegram_send_audio():
        return tg_send_audio.TgSendAudio()

    @staticmethod
    def telegram_send_document():
        return tg_send_document.TgSendDocument()

    @staticmethod
    def telegram_send_photo():
        return tg_send_photo.TgSendPhoto()

    @staticmethod
    def telegram_send_video():
        return tg_send_video.TgSendVideo()

    @staticmethod
    def telegram_request_contact():
        return tg_request_contact.TgRequestContact()

    @staticmethod
    def send_sms():
        return send_sms.SendSMS()

    @staticmethod
    def wa_send_text():
        return wa_send_text.WaSendText()
    
    @staticmethod
    def wa_send_audio():
        return wa_send_audio.WaSendAudio()
    
    @staticmethod
    def wa_send_document():
        return wa_send_document.WaSendDocument()

    @staticmethod
    def wa_send_photo():
        return wa_send_photo.WaSendPhoto()
    
    @staticmethod
    def wa_send_video():
        return wa_send_video.WaSendVideo()

    @staticmethod
    def wa_send_sticker():
        return wa_send_sticker.WaSendSticker()
    
    @staticmethod
    def wa_send_contact():
        return wa_send_contact.WaSendContact()
    
    @staticmethod
    def wa_send_location():
        return wa_send_location.WaSendLocation()
    
    @staticmethod
    def wa_send_with_template():
        return wa_send_with_template.WaSendWithTemplate()