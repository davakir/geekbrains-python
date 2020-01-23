seconds = int(input('Input seconds\' count: '))

hour = 3600  # seconds
minute = 60  # seconds

hours = seconds // hour
if hours < 10:
    hours = '0' + str(hours)
minutes = (seconds % hour) // minute
if minutes < 10:
    minutes = '0' + str(minutes)
seconds = (seconds % hour) % minute

print('Formatted time is {}:{}:{}'.format(hours, minutes, seconds))
