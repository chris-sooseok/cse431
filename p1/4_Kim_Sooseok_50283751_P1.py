def ascending_sort(cities):

    sorting_arr = cities[:]

    def quicksort(low, high):
        if low < high:
            # split the arr into lower half and higher half
            p = partition(low, high)
            # recursive split based on the partition
            quicksort(low, p - 1)
            quicksort(p + 1, high)
    
    def partition(low, high):
        # find pvt
        mid = (low + high) // 2
        sorting_arr[high], sorting_arr[mid] = sorting_arr[mid], sorting_arr[high]
        pvt = sorting_arr[high]

        i = low - 1
        # perform swapping based on the pvt to sort each sub array
        for j in range(low, high):
            if check_if_pops_comes_before_idx(sorting_arr[j], pvt):
                i += 1
                sorting_arr[i], sorting_arr[j] = sorting_arr[j], sorting_arr[i]
        sorting_arr[i + 1], sorting_arr[high] = sorting_arr[high], sorting_arr[i + 1]
        return i + 1
    
    def check_if_pops_comes_before_idx(arr, pvt):
        # if pops are not equal, smaller pop goes first
        if arr[1] != pvt[1]:
            return arr[1] < pvt[1]
        # if pops are equal, larger city index goes first
        return arr[0] > pvt[0]

    if sorting_arr:
        # start with 0 and n - 1
        quicksort(0, len(sorting_arr) - 1)
    
    return sorting_arr


def read_input():
    cities = []
    while True:
        city_input = input().strip()
        if not city_input:
            break
        city_info = city_input.split()
        city_index, population = int(city_info[0]), int(city_info[1])
        cities.append((city_index, population))

    return cities


if __name__ == "__main__":
    cities = read_input()
    sorted_cities = ascending_sort(cities)
    for city in sorted_cities:
        print(city[0], city[1])
