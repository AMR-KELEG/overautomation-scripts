# Generate csv file of prayer time events that can be imported to Google Calendar
# Source of prayer times: https://aladhan.com/calendar/Edinburgh/Scotland,%20UK#
#
# Steps:
# - Load csv file
# - Parse prayer times
# - Approximate start time to the nearest 30 minutes
# - Add a 15 minute offset to the start time
# - Handle timezones
# - Export to csv

import re
import datetime
import pandas as pd
from argparse import ArgumentParser


def normalize_prayer_time(prayer_time_string):
    """Convert time strings to datetime objects"""
    timezone_regex = r"\([a-zA-Z]+\)"
    timezone = re.findall(timezone_regex, prayer_time_string)[0][1:-1]

    prayer_time_str = re.sub(timezone_regex, "", prayer_time_string).strip()

    # Approximate prayer time to the nearest half hour mark
    prayer_time_datetime = datetime.datetime.strptime(prayer_time_str, "%H:%M").time()
    prayer_time_minutes = prayer_time_datetime.minute
    prayer_time_minutes = (1 + prayer_time_minutes // 30) * 30

    # TODO: Handle this in a better way
    return datetime.time(
        hour=prayer_time_datetime.hour
        + prayer_time_minutes // 60
        - (1 if timezone == "BST" else 0),  #  Unify all timezones to GMT+00
        minute=prayer_time_minutes % 60,
    )


def parse_prayer_times_column(prayer_time_column):
    """Convert prayer times column from strings to time objects"""
    return prayer_time_column.apply(
        lambda prayer_time: normalize_prayer_time(prayer_time)
    )


def generate_prayer_events(prayer_name):
    """Generate list of events for a specific prayer"""

    events = []
    for _, day_information_dict in df.iterrows():
        prayer_start_time = day_information_dict[f"timings.{prayer_name}"]

        # Make the event last for 15 minutes
        prayer_end_time = datetime.time(
            hour=prayer_start_time.hour, minute=prayer_start_time.minute + 15
        )
        prayer_dict = {
            "Subject": prayer_name,
            "Start Date": day_information_dict["date.gregorian.date"],
            "Start Time": prayer_start_time,
            "End Date": day_information_dict["date.gregorian.date"],
            "End Time": prayer_end_time,
        }
        events.append(prayer_dict)
    return events


if __name__ == "__main__":
    parser = ArgumentParser(
        "Convert csv file of prayer times into csv files of GCal events"
    )
    parser.add_argument(
        "-i",
        required=True,
        help="Path of the input csv file from https://aladhan.com/calendar/Edinburgh/Scotland,%20UK#",
    )
    parser.add_argument(
        "-o", required=True, help="Path of the output csv file of GCal events"
    )

    args = parser.parse_args()
    input_file_path = args.i
    output_file_path = args.o

    df = pd.read_csv(input_file_path)

    # Ignore the last row (A bug in the site's csv file?)
    df = df.iloc[:-1]

    #  Convert prayer times
    prayer_names = ["Dhuhr", "Asr", "Maghrib"]
    prayer_times_columns = [f"timings.{prayer_name}" for prayer_name in prayer_names]

    # Parse prayer times
    df.loc[:, prayer_times_columns] = df.loc[:, prayer_times_columns].apply(
        parse_prayer_times_column
    )

    # Form a dataframe of events
    events_df = pd.concat(
        [
            pd.DataFrame(generate_prayer_events(prayer_name))
            for prayer_name in prayer_names
        ]
    )

    events_df.to_csv(output_file_path, index=False)
