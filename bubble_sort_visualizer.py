import matplotlib.pyplot as plt
import random
import time

# Generate random data
data = [random.randint(1, 100) for _ in range(10)]

# Visualize the data
def visualize(data):
    plt.bar(range(len(data)), data)
    plt.show(block=False) # block=False means to not block code execution
    plt.pause(0.5)        # Pause to allow time for visualization
    plt.close()           # Close the graph window after pausing

def bubble_sort_visualized(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                visualize(arr) # Call the visualize function after each pass

# Call the sorting function
bubble_sort_visualized(data)
