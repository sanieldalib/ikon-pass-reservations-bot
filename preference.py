import datetime

from config import IKON_RESORTS, PARK_WHIZ, PARKWHIZ_BOOKING, IKON_BOOKING


class Preference:
    def __init__(self, resort, date, is_ikon=False, full_day=False):
        self.resort = resort
        self.is_ikon = is_ikon
        self.available = False
        self.original_date = date
        self.full_day = full_day

        if self.is_ikon:
            self.resort_id = IKON_RESORTS[self.resort]
        else:
            self.resort_id = PARK_WHIZ[self.resort]

        self.date = self.format_date(date)
    
    def format_date(self, date):
        date = datetime.datetime.strptime(date, '%m-%d-%Y')
        if self.is_ikon:
            return date.strftime('%Y-%m-%d')
        return date.strftime('%b %d %Y')

    def set_available(self, is_available=True):
        self.available = is_available

    def sms_text(self):
        if not self.available:
            return

        message = '\n\nA reservation is available for {} on {}.\n\nHurry and book now: {}'

        if self.full_day:
            message = '\n\nA' + ' full day ' + 'reservation is available for {} on {}.\n\nHurry and book now: {}'

        
        if self.is_ikon:
            return message.format(self.resort, self.original_date, IKON_BOOKING)

        return message.format(self.resort, self.original_date, PARKWHIZ_BOOKING.format(self.resort_id))


        

