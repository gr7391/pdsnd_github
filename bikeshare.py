"""
This program analyzes bikeshare data for several cities and
interactively displays important summary statistics for each city.
Gregory Rowe
"""

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('Would you like to see data for Chicago, New York City , or Washington?')
    def cityname():
        city = str(input('Type city name :')).lower()
        if city not in citynames:
            print('Please select city from chicago, new york city, or washington.')
            city = cityname()
        return city
    city = cityname()

    # TO DO: get user input for month (all, january, february, ... , june)
    print('Select a month from january, february, march, april, may, june, or all .')
    def monthname():
        month = str(input('Type month :')).lower()
        if month not in months:
            print('Please select month january, february, march, april, may, june, or all .')
            month = monthname()
        return month
    month = monthname()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print('Select a day monday, tuesady, wednesday, thursday, friday, saturday, sunday, or all .')
    def dayname():
        day = str(input('Type day :')).lower()
        if day not in days:
            print('Please select day from monday, tuesady, wednesday, thursday, friday, saturday, sunday, or all .').lower()
            day = dayname()
        return day
    day = dayname()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    original_df['Month'] = pd.DatetimeIndex(original_df['Start_Time']).month

    months_count = original_df['month'].value_counts()

    maxMonth = months_count.idxmax()
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    print('The most common month is {} and count is {}.'.format((months[maxMonth-1]).title(),month_count.max()))

    # TO DO: display the most common day of week
    original_df['Week Day'] = pd.DatetimeIndex(original_df['Start_Time']).weekday_name

    days_count = original_df['week day'].value_counts()

    maxDay = days_count.idxmax()
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    print('The most common day of week is {} and count is {}.'.format(maxDay.title(),days_count.max()))


    # TO DO: display the most common start hour
    original_df['Hours'] = pd.DatetimeIndex(original_df['Start_Time']).hour

    hours_count = original_df['hours'].value_counts()

    print('The most common hour is {} and count : {}'.format(hours_count.idmax(),hours_count.max()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Start_Station_counts = df['Start Station'].value_counts()
    print('The most commonly used start station is "{}" and count: {}'.format(Start_Station_counts.idmax(),Start_Station_counts.max()))

    # TO DO: display most commonly used end station
    End_Station_counts = df['End Station'].value_counts()
    print('The most commonly used end station is "{}" and count:      {}'.format(End_Station_counts.idmax(),End_Station_counts.max()))

    # TO DO: display most frequent combination of start station and end station trip
    df['Start End stations'] = df['Start Station'] + df['End Station']
    Start_End_Station = df['Start End Station'].value_counts()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time_sum = df['Trip Duration'].sum()
    print('Total travel time {}.'.format(total_time_sum))

    # TO DO: display mean travel time
    total_time_mean = df['Trip Duration'].mean()
    print('Total traveling mean time {}.'.format(total_time_mean))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user = df['User Type'].value_counts()
    print('Total count of user types {}.'.format(count_user))

    # TO DO: Display counts of gender
    df['Gender'].fillna('Not given',inplace=True)
    count_user_gender = df['Gender'].value_counts()
    if city == 'washington':
        print('Gender is not availble for this city {}.'.format(city))

    if city == 'chicago' or city == 'new york':
    print('Total Counts of user Gender type are {}.'.format(count_user_gender))
    # TO DO: Display earliest, most recent, and most common year of birth
    birth_year = df['Birth Year'].value_counts()
    if city == 'washington':
        print('Birth year is not availble for this city {}.'.format(city))

    if city == 'chicago' or city == 'new york':

        print('Earliest, most recent, and most common year of birth are "{}", "{}", and "{}" of"{}".'.format(birth_year.idmin(),df['Birth Year'].iloc[0],birth_year.idmax(),city))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    #allows the user the option of seeing 5 lines raw data

    show_data = input ('\nWould you like to see five lines of raw data? Enter yes or no\n')
    count = 1
    while show_data.lower() != 'no':
        print(df.iloc[[count, count + 1, count + 2, count + 3, count + 4]] )
        show_data = input ('\nWould you like to see five lines of raw data? Enter yes or no\n')
        count += 5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
