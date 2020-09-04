import heapq
from collections import defaultdict
from typing import List


class DesignTwitter:

    def __init__(self):
        self.time = 0
        self.store = defaultdict(list)
        self.followees = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        self.store[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        pq=[]
        [heapq.heappush(pq, item) for item in self.store[userId]]

        for followee in self.followees[userId]:
            if userId==followee:
                continue
            for item in self.store[followee]:
                heapq.heappush(pq, item)

        '''
        1. All tweets
        '''
        result = []
        for _ in range(10):
            if pq:
                result.append(heapq.heappop(pq)[1])
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].discard(followeeId)


if __name__ == '__main__':
    twitter = DesignTwitter()
    #User 1 posts a new tweet (id = 5).
    twitter.postTweet(1, 5)

    # User 1's news feed should return a list with 1 tweet id -> [5].
    print(twitter.getNewsFeed(1))

    # User 1 follows user 2.
    twitter.follow(1, 2)

    # User 2 posts a new tweet (id = 6).
    twitter.postTweet(2, 6)

    # User 1's news feed should return a list with 2 tweet ids -> [6, 5].
    # Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
    print(twitter.getNewsFeed(1))

    # User 1 unfollows user 2.
    twitter.unfollow(1, 2)

    # User 1's news feed should return a list with 1 tweet id -> [5],
    # since user 1 is no longer following user 2.
    print(twitter.getNewsFeed(1))
    '''
    [5]
    [6, 5]
    [5]
    '''

    twitter.postTweet(1, 5)
    twitter.postTweet(1, 3)
    twitter.postTweet(1, 101)
    twitter.postTweet(1, 13)
    twitter.postTweet(1, 10)
    twitter.postTweet(1, 2)
    twitter.postTweet(1, 94)
    twitter.postTweet(1, 505)
    twitter.postTweet(1, 333)
    twitter.postTweet(1, 22)
    twitter.postTweet(1, 11)
    print(twitter.getNewsFeed(1)) #[11, 22, 333, 505, 94, 2, 10, 13, 101, 3]
