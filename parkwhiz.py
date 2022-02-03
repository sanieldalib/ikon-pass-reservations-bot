from datetime import datetime

from config import PARK_WHIZ, PARK_WHIZ_ID
import requests
import re
import json
endpoint = '/events/?fields=%3Adefault%2Csite_url%2Cavailability%2Cvenue%3Atimezone&sort=start_time&zoom=pw%3Avenue'
api_base = 'https://api.parkwhiz.com/v4/venues/'


class ParkwhizAPI:
    def __init__(self, preferences):
        self.preferences = preferences
        # print(self.preferences)

    def get_event(self, venue):
        return requests.get('{}{}{}'.format(api_base, venue, endpoint)).json()

    def parse_dates(self, venue_json, full_day):
        dates = list()
        for slot in venue_json:
            indices = [i for i, x in enumerate(slot['name']) if x == " "]
            date = slot['name'][:indices[2]]
            # print('{}: {}'.format(PARK_WHIZ_ID[str(slot['venue_id'])], date))
            if slot['availability']['available'] > 0:
                if not full_day:
                    dates.append(date)
                else:
                    time = datetime.fromisoformat(slot['start_time'])
                    if time.hour <= 10:
                        dates.append(date)

        
        return dates

    def get_events(self):
        events = dict()
        for idx, pref in enumerate(self.preferences):
            events[idx] = self.parse_dates(self.get_event(pref.resort_id), pref.full_day)
        
        return events

    def check_availability(self):
        events = self.get_events()
        results = self.preferences.copy()

        for i, pref in enumerate(self.preferences):

            results[i].set_available(pref.date in events[i])
        
        return results


            




