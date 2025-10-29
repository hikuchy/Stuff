def read_large_file(file_path: str, chunk_size: int) -> Generator[str, None, None]:
    with open(file_path, 'r') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk
# Пример использования
    for chunk in read_large_file(file_path):
# Обработка каждого чанка по мере необходимости
        print(chunk)
