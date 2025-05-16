import time
import random
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display

def subtract(d1, d2):
    """Display words from d1 that are not listed in d2"""
    words = {}
    for key in d1:
        if key not in d2:
            words[key] = None
    return words

def set_subtract(d1, d2):
    """Use set difference to find elements in d1 not in d2"""
    return set(d1) - set(d2)

def generate_random_dict(size):
    """Generate a random dictionary of given size"""
    return {f"key_{i}": i for i in range(size)}

def benchmark(sizes, overlap_percentage=50):
    """Benchmark both functions with various input sizes
    
    Args:
        sizes: List of sizes to test
        overlap_percentage: Percentage of overlap between d1 and d2
    """
    subtract_times = []
    set_subtract_times = []
    
    for size in sizes:
        # Generate dictionaries
        d1 = generate_random_dict(size)
        
        # Calculate how many items should overlap
        overlap = int(size * overlap_percentage / 100)
        
        # Generate d2 with specified overlap
        d2_keys = random.sample(list(d1.keys()), overlap)
        # Add some keys that aren't in d1
        extra_keys = [f"extra_key_{i}" for i in range(size - overlap)]
        d2 = {k: 1 for k in d2_keys + extra_keys}
        
        # Benchmark subtract function
        start_time = time.time()
        result1 = subtract(d1, d2)
        end_time = time.time()
        subtract_time = end_time - start_time
        subtract_times.append(subtract_time)
        
        # Benchmark set_subtract function
        start_time = time.time()
        result2 = set_subtract(d1, d2)
        end_time = time.time()
        set_subtract_time = end_time - start_time
        set_subtract_times.append(set_subtract_time)
        
        # Verify both functions return same result (accounting for different return types)
        assert set(result1.keys()) == result2, f"Functions returned different results for size {size}"
    
    return subtract_times, set_subtract_times

def plot_results(sizes, subtract_times, set_subtract_times):
    """Plot the benchmark results"""
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, subtract_times, 'o-', label='subtract()')
    plt.plot(sizes, set_subtract_times, 'o-', label='set_subtract()')
    plt.xlabel('Dictionary Size')
    plt.ylabel('Time (seconds)')
    plt.title('Performance Comparison: subtract() vs set_subtract()')
    plt.legend()
    plt.grid(True)
    
    # Log scale might be helpful for wide range of times
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, subtract_times, 'o-', label='subtract()')
    plt.plot(sizes, set_subtract_times, 'o-', label='set_subtract()')
    plt.xlabel('Dictionary Size')
    plt.ylabel('Time (seconds)')
    plt.title('Performance Comparison (Log Scale)')
    plt.legend()
    plt.grid(True)
    plt.yscale('log')
    
    plt.figure(figsize=(10, 6))
    plt.bar(np.array(sizes) - 0.2, subtract_times, width=0.4, label='subtract()')
    plt.bar(np.array(sizes) + 0.2, set_subtract_times, width=0.4, label='set_subtract()')
    plt.xlabel('Dictionary Size')
    plt.ylabel('Time (seconds)')
    plt.title('Performance Comparison (Bar Chart)')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

def run_benchmark():
    # Small to medium sizes
    small_sizes = [100, 1000, 10000, 50000, 100000]
    subtract_times_small, set_subtract_times_small = benchmark(small_sizes)
    
    # Larger sizes (if needed)
    large_sizes = [200000, 500000, 1000000]
    subtract_times_large, set_subtract_times_large = benchmark(large_sizes)
    
    # Plot results
    print("Results for small to medium dictionaries:")
    for size, t1, t2 in zip(small_sizes, subtract_times_small, set_subtract_times_small):
        print(f"Size: {size}, subtract: {t1:.6f}s, set_subtract: {t2:.6f}s, Ratio: {t2/t1 if t1 else 0:.2f}")
    plot_results(small_sizes, subtract_times_small, set_subtract_times_small)
    
    print("\nResults for large dictionaries:")
    for size, t1, t2 in zip(large_sizes, subtract_times_large, set_subtract_times_large):
        print(f"Size: {size}, subtract: {t1:.6f}s, set_subtract: {t2:.6f}s, Ratio: {t2/t1 if t1 else 0:.2f}")
    plot_results(large_sizes, subtract_times_large, set_subtract_times_large)
    
    # Additional test with different overlap percentages
    print("\nTesting with different overlap percentages (size=100000):")
    overlaps = [10, 30, 50, 70, 90]
    subtract_times_overlap = []
    set_subtract_times_overlap = []
    
    for overlap in overlaps:
        st, sst = benchmark([100000], overlap)
        subtract_times_overlap.append(st[0])
        set_subtract_times_overlap.append(sst[0])
        
    for overlap, t1, t2 in zip(overlaps, subtract_times_overlap, set_subtract_times_overlap):
        print(f"Overlap: {overlap}%, subtract: {t1:.6f}s, set_subtract: {t2:.6f}s, Ratio: {t2/t1 if t1 else 0:.2f}")
    
    # Plot overlap results
    plt.figure(figsize=(10, 6))
    plt.plot(overlaps, subtract_times_overlap, 'o-', label='subtract()')
    plt.plot(overlaps, set_subtract_times_overlap, 'o-', label='set_subtract()')
    plt.xlabel('Overlap Percentage')
    plt.ylabel('Time (seconds)')
    plt.title('Impact of Data Overlap on Performance (Size=100000)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Run the benchmark
run_benchmark()