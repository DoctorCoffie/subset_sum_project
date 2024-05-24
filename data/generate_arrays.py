import numpy as np

def generate_array(size, low=-100, high=100):
    return np.random.randint(low, high, size)

def save_array(filename, array):
    np.save(filename, array)

def main():
    arrays = {
        "IA8.npy": generate_array(8),
        "IA10.npy": generate_array(10),
        "IA50.npy": generate_array(50),
        "IA100.npy": generate_array(100)
    }
    
    for filename, array in arrays.items():
        save_array(f"data/{filename}", array)
        print(f"Saved {filename} with values: {array}")

if __name__ == "__main__":
    main()
