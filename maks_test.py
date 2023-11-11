def cyclic_encode(data, generator):
    n = len(generator) - 1  #длина генератора определяет длину информационных битов
    encoded_data = list(data)  #создаем копию входных данных
    encoded_data.extend([0] * n)  #дополняем нулями для заполнения промежуточных битов

    for i in range(len(data)):
        if encoded_data[i] == '1':
            for j in range(n + 1):
                encoded_data[i + j] = str(int(encoded_data[i + j]) ^ int(generator[j]))  #выполняем операцию XOR

    return "".join(encoded_data)

#пример использования:
data = "110101"  #входные данные
generator = "1101"  #генератор (полином, определяющий кодирование)

encoded = cyclic_encode(data, generator)
print("Закодированные данные:", encoded)