restart = 'y'
while restart == 'y':
    distance = input('Enter distance: ')
    distance = float(distance)


    units = input('Enter units, mi or km: ')


    target_units = input('Enter converted units, mi or km: ')


    if units == 'mi':

        if target_units == 'mi':
            new_distance = distance
            print(distance, units, 'equals', new_distance, target_units)

        elif target_units =='km':
            new_distance = distance * 1.609344
            print(distance, units, 'equals', new_distance, target_units)

    elif units == 'km':

        if target_units == 'mi':
            new_distance = distance / 1.609344
            print(distance, units, 'equals', new_distance, target_units)

        elif target_units =='km':
            new_distance = distance
            print(distance, units, 'equals', new_distance, target_units)
    else:
        print('only mi or km')
    restart = input('would you like to convert another? y or n: ')
    print('SHUTTING DOWN')