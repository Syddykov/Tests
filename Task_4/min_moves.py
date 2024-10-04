import sys

def read_numbers_from_file(file_path):
    """Читает числа из файла и возвращает их в виде списка."""
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file if line.strip().isdigit()]

def min_moves_to_equal_elements(nums):
    """Вычисляет минимальное количество ходов для приведения всех элементов к одному числу."""
    nums.sort()
    median = nums[len(nums) // 2]  # Находим медиану
    return sum(abs(num - median) for num in nums)

def main():
    if len(sys.argv) != 2:
        print("Usage: python min_moves.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    # Чтение данных из файла
    nums = read_numbers_from_file(file_path)
    if not nums:
        print("The file is empty or contains no valid numbers.")
        sys.exit(1)

    # Вычисление минимального количества ходов
    min_moves = min_moves_to_equal_elements(nums)
    
    # Вывод результата
    print(min_moves)

if __name__ == "__main__":
    main()