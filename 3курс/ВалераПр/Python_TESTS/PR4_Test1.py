def read_car_batches(file: Iterator[str]) -> Iterator[List[str]]:
    batch: List[str] = []
    for line in file:
        batch.append(line.strip())
        if len(batch) == 5:
            yield batch
            batch = []
    if batch:
        yield batch
# Откройте файл для чтения
with open('cars.txt', 'r') as file:
    for batch in read_car_batches(file):
# Выполняем преобразования с batch, если необходимо
# Например, можно выполнить проверку или очистку данных
        try:
            car = Car(*batch)
            print(car)
        except Exception as e:
            print(f"Error creating Car object: {e}")
