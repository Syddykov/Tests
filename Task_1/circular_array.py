import sys

def circular_array(n):
    return list(range(1, n + 1))

def get_path(n, m):
    arr = circular_array(n)
    path = []
    
    current_index = 0
    
    while True:
        # Определяем индекс начала текущего интервала
        start_index = current_index
        # Определяем индекс конца текущего интервала
        end_index = (current_index + m - 1) % n
        
        # Добавляем начальный элемент интервала в путь
        path.append(arr[start_index])
        
        # Обновляем текущий индекс
        current_index = end_index
        
        # Если мы вернулись к началу, выходим из цикла
        if current_index == 0:
            break
            
    return path

def main():
    if len(sys.argv) != 3:
        print("Usage: python program.py <n> <m>")
        sys.exit(1)

    n = int(sys.argv[1])
    m = int(sys.argv[2])
    
    path = get_path(n, m)
    print(''.join(map(str, path)))

if __name__ == "__main__":
    main()
