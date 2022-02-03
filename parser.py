import json

from preference import Preference
from config import IKON_RESORTS, PARK_WHIZ

class Parser:
    def __init__(self, path='dates.json'):
        with open(path, 'r') as data_file:
            pref_data = data_file.read()
            self.preference_data = json.loads(pref_data)
        self.ikon_resorts = list()
        self.parkwhiz_resorts = list()

        for pref in self.preference_data:
            item = self.parse_item(pref)

            if item.is_ikon:
                self.ikon_resorts.append(item)
            else:
                self.parkwhiz_resorts.append(item)

    def parse_item(self, preference):
        resort = preference['resort']
        date = preference['date']
        is_ikon = resort in IKON_RESORTS.keys()
        full_day = False

        if 'full_day' in preference.keys():
            full_day = preference['full_day']

        return Preference(resort, date, is_ikon, full_day)
    
    def preferences(self):
        return [self.ikon_resorts, self.parkwhiz_resorts]