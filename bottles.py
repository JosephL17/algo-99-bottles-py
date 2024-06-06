def bottle_song(num):
	for i in range(num, 0, -1):
		if i == 1:
			bottle = 'bottle'
			next_bottle = 'no more bottles'
		else:
			bottle = 'bottles'
			next_bottle = 'bottle' if i - 1 == 1 else 'bottles'

		print(f"{i} {bottle} of beer on the wall, {i} {bottle} of beer")
		print(f"Take one down and pass it around, {i - 1 if i > 1 else 'no more'} {next_bottle} of beer on the wall.\n")

		print("No more bottles of beer on the wall, no more bottles of beer.")
		print("Go to the store and buy some more, 99 bottles of beer on the wall.")

bottle_song(99)

####kldjsfalkfdajalskdfjdfls
