# COSTANTI
N = 500
EPOCHS = 100
LEARNING_RATE = 0.1

def activation(x):
    if x > 0.5:
        return 1
    else:
        return 0

# Dati di addestramento (Lettura da file)
input_data = []
expected = []

file = open("dataset_concerto_500.txt", "r")
lines = file.readlines()
for i in range(N):
    valori = lines[i].split(',')
    # Carica i 6 pesi
    input_data.append([int(valori[0]), int(valori[1]), int(valori[2]), int(valori[3]), int(valori[4]), int(valori[5])])
    # Carica il risultato atteso
    expected.append(int(valori[6]))
file.close()

# Pesi casuali iniziali
weights = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
bias = 0.0

# Addestramento
for epoch in range(EPOCHS):
    for i in range(N):
        sum_val = bias
        for j in range(6):
            sum_val += weights[j] * input_data[i][j]

        output = activation(sum_val)
        error = expected[i] - output

        for j in range(6):
            weights[j] += LEARNING_RATE * error * input_data[i][j]
        bias += LEARNING_RATE * error

# Output dei pesi finali
print("Pesi allenati:")
for i in range(6):
    print(f"Peso {i}: {weights[i]:f}")
print(f"Bias: {bias:f}")

# Test finale
print("\nTest del percettrone:")
for i in range(N):
    sum_val = bias
    for j in range(6):
        sum_val += weights[j] * input_data[i][j]
    
    output = activation(sum_val)
    print(f"Input [{input_data[i][0]}, {input_data[i][1]}, {input_data[i][2]}, {input_data[i][3]}, {input_data[i][4]}, {input_data[i][5]}] => Concerto: {output} (Atteso: {expected[i]})")