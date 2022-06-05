# Maria plays college basketball and wants to go pro. Each season she maintains a record of her play.
# She tabulates the number of times she breaks her season record for most points and least points in a game.
# Points scored in the first game establish her record for the season, and she begins counting from there.
import os


def breakingRecords(scores):
    minimum = scores[0]
    maximum = scores[0]
    records = [0, 0]

    for score in scores[1:]:
        if score > maximum:
            maximum = score
            records[0] += 1
        if score < minimum:
            minimum = score
            records[1] += 1

    return records


if __name__ == "__main__":
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    fptr.write(''.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
