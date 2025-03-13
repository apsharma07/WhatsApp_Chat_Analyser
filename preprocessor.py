import re
import pandas as pd

def preprocess(data):
    # Ensure timestamps match both standard and non-breaking space formats
    pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s?[APap][Mm]\s-\s'  

    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)

    # Normalize timestamps (replace non-breaking spaces with regular spaces)
    dates = [date.replace('\u202F', ' ').replace('\xa0', ' ') for date in dates]

    df = pd.DataFrame({'user_message': messages, 'message_date': dates})

    # Convert to datetime (12-hour format with AM/PM)
    df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %I:%M %p - ')

    df.rename(columns={'message_date': 'date'}, inplace=True)

    users = []
    messages = []
    for message in df['user_message']:
        entry = re.split(r'([\w\W]+?):\s', message)
        if entry[1:]:  # User name exists
            users.append(entry[1])
            messages.append(" ".join(entry[2:]))
        else:
            users.append('group_notification')
            messages.append(entry[0])

    df['user'] = users
    df['message'] = messages
    df.drop(columns=['user_message'], inplace=True)

    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.strftime('%I')  # 12-hour format
    df['minute'] = df['date'].dt.minute
    df['am_pm'] = df['date'].dt.strftime('%p')  # AM/PM indicator

    # Create period column in 12-hour format
    period = []
    for hour, am_pm in zip(df['hour'], df['am_pm']):
        next_hour = str(int(hour) % 12 + 1)  # Convert "12" to "1" for next hour
        next_am_pm = 'AM' if am_pm == 'PM' and next_hour == '12' else 'PM' if am_pm == 'AM' and next_hour == '12' else am_pm
        period.append(f"{hour} {am_pm} - {next_hour} {next_am_pm}")

    df['period'] = period

    return df
