class Twitter:

    def __init__(self):
        self.tweets = {}
        self.following = {}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append([self.timestamp, tweetId])
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        def add_most_recent(uid):
            if uid in self.tweets and self.tweets[uid]:
                idx = len(self.tweets[uid]) - 1
                ts, tid = self.tweets[uid][idx]
                heapq.heappush(heap, (-ts, tid, uid, idx))
        
        add_most_recent(userId)

        for followee in self.following.get(userId, set()):
            add_most_recent(followee)

        feed = []
        while heap and len(feed) < 10:
            neg_ts, tid, uid, idx = heapq.heappop(heap)
            feed.append(tid)
            if idx - 1 >= 0:
                ts, twt_id = self.tweets[uid][idx - 1]
                heapq.heappush(heap, (-ts, twt_id, uid, idx - 1))
        return feed


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)
        
