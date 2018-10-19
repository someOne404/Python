# Readability
# - Do not make any line too complicated

# print('You should get at least', 0.00471 * int(input('How many song?')), 'GB')
#
# - use names that describe the content of the variable
# implies you know the purpose of the variable (and that it has just one)
#
# - no magic numbers - - used named constants
#
# - follow good style
#   - constants use capitals
#   - variables (and functions) use lower-case
#   - 1 blank line = separation of thought
#   - spaces...complicated make it look nice and symmetric

GIGABYTES_PER_SONG = 0.00471

songs = int(input('How many songs? '))
gb_of_storage_for_songs = GIGABYTES_PER_SONG * songs
print('You should get at least', gb_of_storage_for_songs, 'GB')
