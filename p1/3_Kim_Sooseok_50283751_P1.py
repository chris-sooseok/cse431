import heapq

def FIFO_FF(k, n, m, requests):
     # Please write your algorithm here, or create a new function if you prefer.

    # sanity check
    if m != len(requests):
        return 0, 0
    
    def fifo(k, n, m, requests):
        misses = 0
        inc = 0
        cache = []

        # make sure each request within the range of 1 and n
        for request in requests:
            # check cache miss
            if request not in [r for _, r in cache]:
                # if cache miss happens, increment misses
                misses += 1

                # since cache miss happended, check the current space of cache list
                # make sure size of cache doesn't exceed k
                if len(cache) < k:
                    # if there is a space in cache, append the requested page into cache
                    heapq.heappush(cache, (inc, request))
                    # make sure to increment inc to ensure FIFO is consistent
                    inc += 1
                else:
                    # if there is no space, take the first in out
                    heapq.heappop(cache)
                    # after making a space, push the requested page
                    heapq.heappush(cache, (inc, request))
                    # make sure to increment inc to ensure FIFO is consistent
                    inc += 1
            else:
                # if cache hits, continue
                continue

        return misses

    def ff(k, n, m, requests):
        misses = 0
        cache = []

        for cur_idx, request in enumerate(requests):
            if request in cache:
                # cache hits, continue
                continue

            misses += 1

            if len(cache) < k:
                # if there is a space, just append the page into cache
                cache.append(request)
            else:
                future_idxs = {}
                # find the index of each future request
                for c in cache:
                    nxt = float("inf")

                    # loop through future requests
                    for idx in range(cur_idx + 1, m):
                        if requests[idx] == c:
                            # if next future request is found, update the index
                            nxt = idx
                            break
                    # append the index of each future request
                    future_idxs[c] = nxt

                # find the furthest request
                furthest = max(cache, key=lambda f: future_idxs[f])
                # remove the page from the cache
                cache.remove(furthest)
                cache.append(request)

        return misses

    fifo_miss = fifo(k, n, m, requests)
    ff_miss = ff(k, n, m, requests)

    return fifo_miss, ff_miss

#You are allowed to use some built-in functions, such as the Python heap library, including heapq.heapify(). 

def read_input():
    k, n, m = map(int, input().split())
    requests = []
    for _ in range(m):
        request = int(input())
        requests.append(request)
    return k, n, m, requests


if __name__ == "__main__":
    k, n, m, requests = read_input()
    fifo, ff = FIFO_FF(k, n, m, requests)
    print(fifo)
    print(ff)
