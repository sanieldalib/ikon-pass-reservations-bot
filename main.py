from parkwhiz import ParkwhizAPI
from ikon_driver import IkonDriver
from parser import Parser
from sms import TwilioSms

def main():
    parser = Parser()
    [ikon_prefs, parkwhiz_prefs] = parser.preferences()

    # parkwhiz_prefs[0].available = True

    if len(ikon_prefs) == 0 and len(parkwhiz_prefs) == 0:
        return



    parkwhiz = ParkwhizAPI(parkwhiz_prefs).check_availability()
    ikon_driver = IkonDriver(ikon_prefs)
    ikon = ikon_driver.check_availability()

    sms = TwilioSms()
    sms.notify_preferences(parkwhiz + ikon)
    ikon_driver.close_driver()

    for item in parkwhiz + ikon:
        print(item.__dict__)




main() 