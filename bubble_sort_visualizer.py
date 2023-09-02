import matplotlib.pyplot as plt
import random
import time

# Generate random data
data = [random.randint(1, 100) for _ in range(50)]

# Visualize the data
def visualize(data):
    plt.bar(range(len(data)), data)
    plt.show()
    time.sleep(0.1)

def bubble_sort_visualized(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        visualize(arr) # Call the visualize function after each pass

# Call the sorting function
bubble_sort_visualized(data)
