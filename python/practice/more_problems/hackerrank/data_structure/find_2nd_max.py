if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    print(arr)
    arr = set(arr)
    print(arr)
    max_int = max(arr)
    arr.remove(max_int)
    print (max(arr))
