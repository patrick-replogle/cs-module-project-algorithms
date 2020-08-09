import sys


def rock_paper_scissors(n):
    options = ['rock', 'paper', 'scissors']
    results = []

    def getResults(roundsPlayed, roundsLeft):
        if roundsLeft == 0:
            results.append(roundsPlayed)
        else:
            for i in range(len(options)):
                getResults(roundsPlayed + [options[i]], roundsLeft - 1)

    getResults([], n)
    return results


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
