import random
import argparse
import os


def python_list_to_bash_list(py_list):
    """Convert a Python list to a Bash-style list"""
    return "(" + " ".join(map(str, py_list)) + ")"


def generate_test_file(ram_size):
    """Generate a test file for the given RAM size"""
    output_dir = "extremeTest"
    os.makedirs(output_dir, exist_ok=True)

    output_filename = f"{output_dir}/{ram_size}.txt"

    # Check if file already exists
    if os.path.exists(output_filename):
        print(f"File already exists, skipping: {output_filename}")
        return

    totalAllocations = int(ram_size * 0.4)
    upperBound = int(ram_size * (0.1 + random.uniform(0, 0.2)))  # Adding a random factor for more variance
    lowerBound = int(ram_size * (0.005 + random.uniform(0, 0.01)))  # Same for lower bound

    output_list = []

    # Generate unique ID allocations
    for j in range(totalAllocations):
        randomNum = random.randint(lowerBound, upperBound)
        output_list.append(f"A:{j}:{randomNum}:0")
        output_list.append(f"F:{j}:{randomNum}:0")

    # Shuffle the order
    random.shuffle(output_list)

    # Write to file
    with open(output_filename, "w") as f:
        for item in output_list:
            f.write(item + "\n")

    print(f"File generated: {output_filename}")


def main():
    # Define argument parser
    parser = argparse.ArgumentParser(description="Generate test files for specified RAM sizes.")
    parser.add_argument("ram_sizes", type=int, nargs="+", help="Specify one or more RAM sizes to test with")
    args = parser.parse_args()

    # Generate test files for each RAM size provided
    for ram_size in args.ram_sizes:
        print(f"Generating RAM size: {ram_size}")
        generate_test_file(ram_size)


# Ensures script runs only when executed directly
if __name__ == "__main__":
    main()
