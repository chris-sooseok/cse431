def interval_scheduling(n, intervals):

    if n != len(intervals):
        return 0, 0, 0
    
    jobs = []
    cur_s_time = float("-inf")
    cur_f_time = float("inf")
    idx = 0

    # sort by the earliest finish time
    sorted_jobs = merge_sort(intervals, n, 1)

    # loop through given jobs
    while idx < len(sorted_jobs):
        chosen_job = None
        chosen_idx = None

        for offset, job in enumerate(sorted_jobs[idx:]):
            s, f = job
            # finds all suitable jobs
            if s >= cur_s_time:
                # among the suitable jobs, find the earliest finishing job
                if f < cur_f_time:
                    cur_f_time = f
                    chosen_job = job
                    # updates idx not to consider the jobs again
                    chosen_idx = idx + offset

        if chosen_job is not None:
            jobs.append(chosen_job)
            # updates the start time to find the next suitable jobs
            cur_s_time = chosen_job[1]
            # updates the finish time to find the next earliest finishing jobs
            cur_f_time = float("inf")
            # updates index to skip already considered jobs
            idx = chosen_idx + 1
        else:
            # break if there is no suitable job at all
            break

    if not jobs:
        return 0, 0, 0

    maximum = len(jobs)
    first_interval_s = jobs[0][0]
    first_interval_t = jobs[0][1]

    return maximum, first_interval_s, first_interval_t


def merge_sort(A, n, b):
    if n == 1:
        return A
    else:
        mid = n // 2
        left = merge_sort(A[:mid], mid, b)
        right = merge_sort(A[mid:], n - mid, b)

        return merge(left, right, mid, n - mid, b)
    
def merge(B, C, ln, rn, b):
    A = []
    i = 0
    j = 0
    while i < ln and j < rn:
        # compare start time to sort by the earliest start time
        if B[i][b] <= C[j][b]:
            A.append(B[i])
            i += 1
        else:
            A.append(C[j])
            j += 1
    if i < ln:
        for n in B[i:]:
            A.append(n)
    if j < rn:
        for n in C[j:]:
            A.append(n)
    
    return A


def read_input():
    n = int(input().strip())
    intervals = []
    for _ in range(n):
        s, f = map(int, input().split())
        intervals.append((s, f))
    return n, intervals


if __name__ == "__main__":
    n, intervals = read_input()
    maximum, first_interval_s, first_interval_t = interval_scheduling(n, intervals)
    print(maximum)
    print(first_interval_s, first_interval_t)
