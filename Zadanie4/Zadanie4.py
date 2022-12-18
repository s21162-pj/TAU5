def return_song():
    number_of_verses = 0
    f = open('song.txt', 'r')
    for line in f:
        if (len(line.strip()) != 0):
            number_of_verses += 1

    return return_verse(1, number_of_verses)


def return_verse(verse=None, end_verse=None):
    if verse is not None and not str(verse).isnumeric():
        raise Exception("value of a row must be a number")

    song_array = []
    f = open('song.txt', 'r')
    for line in f:
        if (len(line.strip()) != 0):
            song_array.append(line.strip())
    f.close()

    verses = ""

    for i in range(0, len(song_array)):
        if i + 1 == verse and end_verse == None:
            return song_array[i]
        if end_verse is not None and i + 1 >= verse and i + 1 <= end_verse:
            verses += song_array[i] + "\n"

    return verses

if __name__ == '__main__':
    print(return_verse(3))