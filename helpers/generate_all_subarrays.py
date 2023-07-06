def generate_subarrays(arr):
    subarrays = []
    n = len(arr)

    # Generate all subarrays
    for i in range(n):
        for j in range(i, n):
            for k in range(i, j+1):
                print(arr[k], end=' ')
            print('')

    return subarrays

if __name__ == "__main__":
    print(generate_subarrays([1,2,3,4]))