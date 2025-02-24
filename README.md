# Memory Allocation Test Suite

This project is designed to test memory allocation strategies using different RAM sizes. It generates test files, runs allocation tests, and validates the results by counting occurrences of `FAIL` and `SUCCESS` while extracting memory usage statistics.

## **How to Run the Tests**

Clone the project files using ```bash
git clone https://github.com/AlphaCloudX/Operating-Systems-Memory-Allocation-Grader.git
``` into the directory where you have your `allocator` program

Then just copy the files from inside the folder to the current directory with ```bash
cp -r Operating-Systems-Memory-Allocation-Grader/* .
```

It should be ready to run now!

### **Step 1: Generate Test Files**
Run the `runTests.sh` script, which prompts whether to select which ram sizes to test with. It will automatically generate the test files if they do not exist.
```bash
./runTests.sh
```
Enter the ram sizes like so:
`128 512 1024 2056`

There is no limit to the amount of test files, just keep in mind that they all have to be unique numbers so `10 10 10` will only generate 1 file.

### **Step 2: Run Allocation Tests**
The script will execute the allocator for each memory size and strategy (`first`, `best`, `worst`). Output files from your run are saved in `extremeTestOutputs/`.
As the user you only need to interact with the `runTests.sh` file.

## **Setup & Prerequisites**
- Ensure the **allocator** executable is available

---

## **CSV Output Format**
The generated `validation_results.csv` will look like this:

| RAM Size | Strategy | FAIL Count | SUCCESS Count | Total Count | Bytes Allocated | Bytes Free | Validation |
|----------|------------|------------|--------------|------------|----------------|------------|------------|
| 128      | first      | 5          | 3            | 8          | 126            | 2          |            |
| 128      | best       | 5          | 3            | 8          | 126            | 2          |            |
| 128      | worst      | 5          | 3            | 8          | 126            | 2          |            |
| 128      | TOTAL      | -          | -            | -          | -              | -          | PASSED     |

- **FAIL Count / SUCCESS Count:** Number of occurrences of each result.
- **Bytes Allocated / Free:** Extracted from the summary.
- **Validation:** Ensures all strategies have consistent totals. Shows `PASSED` (green) or `FAILED` (red).

---

## **Expected Output in Console**
```
Validating RAM size: 128
Validation result for RAM size 128: PASSED

Results saved to validation_results.csv
```
If there's a mismatch in total counts, it will flag as `FAILED` in red.

---

## **Notes**
- If a file is missing, the script will warn and continue. Make sure you compile your code!
- If the bash file gives permission issues, simply type in `chmod +x runTests.sh` to allow the script to execute.


Happy testing!

