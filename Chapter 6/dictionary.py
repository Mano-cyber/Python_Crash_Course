# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(f"The alien is {alien_0['color']}.")
# alien_0['color'] = 'yellow'
# print(f"The alien is {alien_0['color']}.")
# print(alien_0)

# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print(f"Original position: {alien_0['x_position']}")

# # Move the alien to the riight.
# # Determine how far to move the alien based on its current speed.
# if alien_0['speed'] == 'slow':
# 	x_increment = 1
# elif alien_0['speed'] == 'medium':
# 	x_increment = 2
# else:
# 	#This must be a fast alien.
# 	x_increment = 3

# #The new position is the old position plus the increment.
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print(f"New position: {alien_0['x_position']}")

person = {'age': '18', 'race': 'black'}
# point_value = person.get('points', 'No point value assigned.')
# print(point_value)
# point_value = person.get('age')
# print(point_value)

for key, value in person.items():
	print(f"\nKey: {key}")
	print(f"Value: {value}")..append


















































	