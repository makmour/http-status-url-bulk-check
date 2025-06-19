# URL HTTP Status Bulk Check

## Short Description

A Python script for bulk-checking HTTP status codes from a list of URLs. The tool includes concurrency, retries, robust error handling, command-line interface (CLI), and structured CSV output.

---

## Features

- **Multithreaded Requests**: Uses `ThreadPoolExecutor` for fast, concurrent URL checking.
- **Automatic Retries**: Handles transient errors (500–504) with a configurable retry strategy.
- **Robust Error Handling**: Detects and clearly reports timeouts, connection errors, invalid URLs, and HTTP errors.
- **Custom Headers**: Uses a friendly `User-Agent` to reduce chances of getting blocked.
- **CSV Output**: Saves results to `results.csv` with structured information (URL, status code, message).
- **Command-Line Interface**:
  - Accepts a `--file` (or `-f`) argument to specify an input file.
  - Defaults to `urls.txt` if no file is provided.

---

## Files

| Filename              | Usage                                                                      |
|-----------------------|----------------------------------------------------------------------------|
| [check.py](check.py)  | The main executable Python script                                          |
| [urls.txt](urls.txt)  | Input file containing the list of URLs to check (one per line)             |
| [results.csv](results.csv) | Output file containing structured status check results                |
| [README.md](README.md)| This file                                                                  |
| [CHANGELOG](CHANGELOG.md) | Full changelog of changes and improvements                         |
| [LICENSE](LICENSE)    | Project license (MIT)                                                      |
| [CONTRIBUTING](CONTRIBUTING.md) | Guidelines for contributing to the project                     |

---

## How to Use

1. Create or edit `urls.txt` and include one URL per line.
2. Run the script using:

```bash
python3 check.py
```

3. (Optional) To use a custom input file:

```bash
python3 check.py -f myfile.txt
```

4. The results will be printed to the terminal and saved to `results.csv`.

---

## Example Output

**Console:**
```
https://example.com @ 200 - Success
https://nonexistent.example @ 404 - HTTP Error: 404 Client Error: Not Found for url
```

**results.csv:**
```
URL,Status Code,Message
https://example.com,200,Success
https://nonexistent.example,404,HTTP Error: 404 Client Error: Not Found for url
```

---

## Changelog

Please see [CHANGELOG](CHANGELOG.md) for detailed update history.

---

## Security

If you discover any security-related issues, please get in touch with me via [Twitter](https://x.com/infectedplus1) instead of using the public issue tracker.

---

## License

The MIT License (MIT). Please see the [License File](LICENSE) for more information.
