from collections import defaultdict
from typing import List


class TweetCounts:

    def __init__(self):
        self.store = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.store[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        delta = 0
        if freq == "minute":
            delta = 60
        elif freq == "hour":
            delta = 3600
        else:
            delta = 86400


        result=[0]* ((endTime-startTime)//delta +1)
        if not self.store[tweetName]:
            return result

        times=sorted(self.store[tweetName])
        for time in times:
            if startTime<=time<=endTime:
                result[(time-startTime)//delta]+=1

        return result




if __name__ == '__main__':
    tweetCounts = TweetCounts()
    tweetCounts.recordTweet("tweet3", 0)
    tweetCounts.recordTweet("tweet3", 60)
    tweetCounts.recordTweet("tweet3", 10)  # All tweets correspond to "tweet3" with recorded times at 0, 10 and 60.
    print(tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0,59))
    # return [2]. The frequency is per minute (60 seconds), so there is one interval of time: 1) [0, 60> - > 2 tweets.
    print(tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0,60))  # return [2, 1]. The frequency is per minute (60 seconds), so there are two intervals of time: 1) [0, 60> - > 2 tweets, and 2) [60,61> - > 1 tweet.
    tweetCounts.recordTweet("tweet3",
                            120)  # All tweets correspond to "tweet3" with recorded times at 0, 10, 60 and 120.
    print(tweetCounts.getTweetCountsPerFrequency("hour", "tweet3", 0,
                                           210))  # return [4]. The frequency is per hour (3600 seconds), so there is one interval of time: 1) [0, 211> - > 4 tweets.
