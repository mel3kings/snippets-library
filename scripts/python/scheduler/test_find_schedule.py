import unittest
from find_schedule import sanitize_input, convert_to_local_timezones, find_recommended_time


class TestScheduler(unittest.TestCase):
    def test_response(self):
        print(self)
        response = sanitize_input(["5:30"])
        assert(response[0] == '05:30')

    def test_splitting_request(self):
        response = sanitize_input(["4:30-7:30"])
        assert(response[0] == '04:30')
        assert(response[1] == '07:30')

    def test_conversion_of_shorthand(self):
        response = sanitize_input(["6:30-7"])
        assert (response[0] == '06:30')
        assert (response[1] == '07:00')

    def test_sanitize_with_timezones(self):
        response = sanitize_input(["6:30-7:00", "IST"])
        assert (response[0] == '06:30')
        assert (response[1] == '07:00')

    def test_sanitize_multiple_timezones(self):
        response = sanitize_input(["6:30-7:00", "IST", "5-7"])
        assert (response[0] == '06:30')
        assert (response[1] == '07:00')
        assert (response[2] == '05:00')
        assert (response[3] == '07:00')
        response = sanitize_input(["12:30-1:00", "IST", "2-3"])
        assert (response[0] == '12:30')
        assert (response[1] == '01:00')
        assert (response[2] == '02:00')
        assert (response[3] == '03:00')
        response = sanitize_input(["13:30-14:00"])
        assert (response[0] == '13:30')
        assert (response[1] == '14:00')

    def test_find_office_hours_schedule(self):
        response = convert_to_local_timezones(["9:58 IST"])
        assert response [0] == '03:28 PM', response[0]
        response = convert_to_local_timezones(["6:00 PM IST"])
        assert response[0] == '11:30 PM', response[0]
        response = convert_to_local_timezones(["6:00p IST"])
        assert response[0] == '11:30 PM', response[0]

        response = convert_to_local_timezones(["12:30-1:00p IST"])
        assert response[0] == '06:00 PM', response[0]
        assert response[1] == '06:30 PM', response[1]

    def test_multiple_times(self):
        response = convert_to_local_timezones(["12:30-1:00p IST", "1-2 IST"])
        assert response[0] == '06:00 PM', response[0]
        assert response[1] == '06:30 PM', response[1]

    def test_find_recommended_time(self):
        response = find_recommended_time(["9:00-5:00p HKT"])

    def test_short_hand_version(self):
        response = find_recommended_time(["9-5 HKT"])



if __name__ == '__main__':
    unittest.main()