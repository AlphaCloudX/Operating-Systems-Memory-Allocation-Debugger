import csv
import argparse
import os
import re

# Directory where test results are stored
OUTPUT_DIR = "extremeTestOutputs"

# ANSI color codes for console output
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

def analyze_file(file_path):
    """Reads the file, counts FAIL/SUCCESS occurrences, and extracts bytes allocated/free."""
    fail_count = 0
    success_count = 0
    bytes_allocated = None
    bytes_free = None

    with open(file_path, "r") as file:
        for line in file:
            # Count occurrences of FAIL and SUCCESS (case insensitive)
            if "FAIL" in line.upper():
                fail_count += 1
            elif "SUCCESS" in line.upper():
                success_count += 1

            # Extract Bytes Allocated and Bytes Free
            allocated_match = re.search(r"(\d+)\s+bytes\s+allocated", line, re.IGNORECASE)
            free_match = re.search(r"(\d+)\s+bytes\s+free", line, re.IGNORECASE)

            if allocated_match:
                bytes_allocated = int(allocated_match.group(1))
            if free_match:
                bytes_free = int(free_match.group(1))

    return fail_count, success_count, bytes_allocated, bytes_free

def validate_ram_sizes(ram_sizes):
    """Validates RAM size results and writes data to CSV."""
    csv_filename = "validation_results.csv"
    strategies = ["first", "best", "worst"]

    with open(csv_filename, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["RAM Size", "Strategy", "FAIL Count", "SUCCESS Count", "Total Count", "Bytes Allocated", "Bytes Free", "Validation"])

        for ram_size in ram_sizes:
            print(f"Validating RAM size: {ram_size}")

            total_counts = []
            results = []

            for strategy in strategies:
                file_path = os.path.join(OUTPUT_DIR, f"{ram_size}_{strategy}.txt")

                if not os.path.exists(file_path):
                    print(f"Warning: File {file_path} not found, skipping...")
                    continue

                fail_count, success_count, bytes_allocated, bytes_free = analyze_file(file_path)

                total_count = fail_count + success_count
                total_counts.append(total_count)

                results.append((strategy, fail_count, success_count, total_count, bytes_allocated, bytes_free))

                # Write individual strategy result to CSV
                csv_writer.writerow([ram_size, strategy, fail_count, success_count, total_count, bytes_allocated, bytes_free, ""])

            # Validate that all total_counts are equal
            if len(set(total_counts)) == 1:  # All values should be the same
                validation_status = f"{GREEN}PASSED{RESET}"
                # Write validation row to CSV
                csv_writer.writerow([ram_size, "TOTAL", "-", "-", "-", "-", "-", "PASSED"])

            else:
                validation_status = f"{RED}FAILED{RESET}"
                # Write validation row to CSV
                csv_writer.writerow([ram_size, "TOTAL", "-", "-", "-", "-", "-", "FAILED"])



            print(f"Validation result for RAM size {ram_size}: {validation_status}")

    print(f"\nResults saved to {csv_filename}")

def main():
    # Define argument parser
    parser = argparse.ArgumentParser(description="Validate test files for specified RAM sizes.")
    parser.add_argument("ram_sizes", type=int, nargs="+", help="Specify one or more RAM sizes to validate")
    args = parser.parse_args()

    # Validate RAM sizes
    validate_ram_sizes(args.ram_sizes)

# Ensures script runs only when executed directly
if __name__ == "__main__":
    main()
