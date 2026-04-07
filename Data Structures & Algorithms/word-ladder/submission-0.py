from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        d={}
        for i in wordList:
            for j in range(len(beginWord)):
                pat=i[:j]+"*"+i[j+1:]
                if pat not in d:
                    d[pat]=[]
                d[pat].append(i)
        q=deque([(beginWord,0)])
        visited=set()
        visited.add(beginWord)
        print(d)
        while q:
            node,dist=q.popleft()
            if node==endWord:
                return dist+1
            
            for j in range(len(node)):
                pattern=node[:j]+"*"+node[j+1:]
                for word in d[pattern]:
                    if word not in visited:
                        visited.add(word)
                        q.append((word,dist+1))
        return 0

        

        