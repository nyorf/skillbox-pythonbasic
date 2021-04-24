dog_scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

maxIndex = 0
minIndex = 0
maxScore = max(dog_scores)
minScore = min(dog_scores)

current_index = -1
for score in dog_scores:
    current_index += 1
    if score == maxScore:
        maxIndex = current_index
    elif score == minScore:
        minIndex = current_index

print('Изначальный список очков:', dog_scores)
dog_scores[minIndex] = maxScore
dog_scores[maxIndex] = minScore
print('Исправленный список очков:', dog_scores)