# Memory Allocation Test Suite

This project is designed to automate the testing of memory allocation strategies using different RAM sizes. It generates test files, runs allocation tests, and validates the results by counting occurrences of `FAIL` and `SUCCESS` while extracting memory usage statistics.

It isn't the most robust solution but it has the ability to easily share test cases, automate the testing of hundreds of files and provide easy to read debugging output for a user to validate if methods works properly.

---

## **Code Prerequisites**
- When your allocator has made an allocation, it must output SUCCESS
- When your allocator cannot make an allocation, it must output FAIL
- If your allocator can free a location, it must not output SUCCESS OR FAIL, something like FREED Location X is fine.
- Why? The code counts the number of SUCCESS's and FAIL's to determine if it mostly works as this will always remain constant. It may however still work if you use SUCCESS or FAIL for free's but I haven't tested this.


Your summary must look as close to this as possible:
```
SUMMARY:
990 bytes allocated
34 bytes free
```

- This is because I am looking for the bytes allocated keywords and the bytes free keyword

## **How to Run the Tests**

Ensure you built your code using `make`

Clone the project files using
```bash
git clone https://github.com/AlphaCloudX/Operating-Systems-Memory-Allocation-Grader.git
```
into the directory where you have your `allocator` program


Then just copy the files from inside the folder to the current directory with
```bash
cp -r Operating-Systems-Memory-Allocation-Grader/* .
```

It should be ready to run now!

If the bash file gives permission issues, simply type in `chmod +x runTests.sh` to allow the script to execute.

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

## **How Does This Actually Work?**
Although this approach may not cover every edge case, the Python scripts generate random allocation and deallocation operations. Since the total number of allocation calls is fixed, the number of successful allocations plus the number of failed allocations will always sum to that fixed number.

We can then compare the total allocated size for each method—Best-Fit, Worst-Fit, and First-Fit—and verify that they are consistent.

For instance, if Best-Fit and First-Fit result in a total count of 200, but Worst-Fit results in a total count of 199, it indicates an issue of 1 allocation not being account for.


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


Happy testing!

