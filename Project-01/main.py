import winsound

print('Enter Temperature:')
temperature = int(input())

print('Enter Light:')
light = int(input())

print('Enter Humidity:')
humidity = int(input())

while True:
    inp = input("Does system work? Yes or No\n").lower().strip()
    if inp == "yes":
        workProperly = True
        break
    elif inp == "no":
        workProperly = False
        break
    else:
        print("Answer must be Yes or No")

while True:
    inp2 = input("Does system work without Error? Yes or No\n").lower().strip()
    if inp2 == "yes":
        workWithoutError = True
        break
    elif inp2 == "no":
        workWithoutError = False
        break
    else:
        print("Answer must be Yes or No")

if 15 <= temperature <= 20 and 10 <= light <= 15 and 5 <= humidity <= 12:
    print("System Working Properly, All is Well")

if workProperly is False:
    print("System doesn't work, ALARM")
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 1000  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)

else:
    if workWithoutError is False:
        print("There is an Error on the system, ALARM")
        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 1000  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
    else:
        if temperature < 15:
            temperature = 17
            print("Temperature is below ideal condition. Temperature increased and set to 17, which is an ideal condition")
        if temperature > 20:
            temperature = 17
            print("Temperature is above ideal condition. Temperature decreased and set to 17, which is an ideal condition")
        if light < 10:
            light = 13
            print("Light is below ideal condition. Light increased and set to 13, which is an ideal condition")
        if light > 15:
            light = 13
            print("Light is above ideal condition. Light decreased and set to 13, which is an ideal condition")
        if humidity < 5:
            humidity = 8
            print("Humidity is below ideal condition. Humidity increased and set to 8, which is an ideal condition")
        if humidity > 12:
            humidity = 8
            print("Humidity is above ideal condition. Humidity decreased and set to 8, which is an ideal condition")
