violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

totalPlaytime = 0
songsCount = int(input('Сколько песен выбрать? '))
for i_name in range(1, songsCount + 1):
    print('Название', i_name, 'песни:', end=' ')
    songName = input()
    for i_song in violator_songs:
        if i_song[0] == songName:
            totalPlaytime += i_song[1]
            break
    else:
        print('Этой песни нету в списке, попробуй ещё раз.')

print('\nОбщее время звучания песен:', round(totalPlaytime, 2))

# зачёт!
