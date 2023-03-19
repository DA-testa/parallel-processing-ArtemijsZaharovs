# python3
#221RDC035, Artemijs Zaharovs, 18.gr.
def parallel_processing(n, m, data):
    
    str = [(0, i) for i in range(n)]
    
    
    output = []
   
    for i in range(m):
        time = data[i]
        min = float('inf')
        id = -1
        for j in range(n):
            if str[j][0] < min:
                min = str[j][0]
                id = j
        output.append((id, min))
        fin = min + time
        str[id] = (fin, str[id][1])
    
   
    return output


def main():
  
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    
   
    result = parallel_processing(n, m, data)
    for thread, s in result:
        print(thread, s)


if __name__ == "__main__":
    main()
