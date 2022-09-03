LIGHT_SPEED = 300000  # km/s
LIGHT_YEAR = LIGHT_SPEED * 3600 * 24 * 365  # km
ACCELERATION = 0.01  # km/s2

engines = {'AM': 75000, 'EM': (100, LIGHT_SPEED * 24)}


def from_ly_to_km(distance):
    return distance * LIGHT_YEAR


def acc_time(boost_limit):
    acceleration_time = boost_limit / ACCELERATION
    return acceleration_time


def acc_distance(boost_limit):
    acceleration_and_deceleration_distance = (boost_limit / 2 * acc_time(boost_limit)) * 2
    return acceleration_and_deceleration_distance


def time_to_planet_system_calculator(distance, engine_type):
    if engine_type == 'AM':
        distance_1 = acc_distance(engines['AM'])
        distance -= distance_1
        full_speed_time = distance / engines['AM']
        main_time = acc_time(engines['AM']) * 2 + full_speed_time
        hours = round((main_time / 3600), 1)
        days = round((hours / 24), 1)
        years = round((days / 365), 1)
        print(f'The cosmic travel to chosen planet system will take {main_time} seconds or '
              f'{hours} '
              f'hours or {days} days or {years} years')
    elif engine_type == 'EM':
        distance_1 = acc_distance(engines['EM'][0])
        distance -= distance_1
        full_speed_time = distance / engines['EM'][1]
        main_time = acc_time(engines['EM'][0]) * 2 + full_speed_time
        hours = round((main_time / 3600), 2)
        days = round((hours / 24), 2)
        years = round((days / 365), 2)
        print(f'The cosmic travel to chosen planet system will take {main_time} seconds or '
              f'{hours} '
              f'hours or {days} days or {years} years')


print('Put in the distance you have (in light years)')
distance_in_ly = float(input())
print('Put in the type of the engine you have (AM or EM)')
engine_type = input()

time_to_planet_system_calculator(from_ly_to_km(distance_in_ly), engine_type=engine_type)

