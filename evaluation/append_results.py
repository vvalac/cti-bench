import csv
import os

def append_results_to_benchmark(benchmark_tsv_path, model_name):
    with open(benchmark_tsv_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        rows = list(reader)

    if not rows:
        raise ValueError("Benchmark TSV file is empty.")

    header = rows[0]
    if model_name in header:
        raise ValueError(f"Column for model '{model_name}' already exists in benchmark file.")

    results_file = f'_{model_name}_result.txt'
    if not os.path.exists(results_file):
        raise FileNotFoundError(f"Results file {results_file} not found.")

    with open(results_file, 'r', encoding='utf-8') as f:
        results = [line.strip() for line in f if line.strip()]

    num_data_rows = len(rows) - 1
    if len(results) != num_data_rows:
        raise ValueError(
            f"Number of results ({len(results)}) does not match number of data rows ({num_data_rows})."
        )

    header.append(model_name)
    for i, result in enumerate(results, start=1):
        rows[i].append(result)

    with open(benchmark_tsv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(rows)

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Append model results to benchmark TSV file.")
    parser.add_argument("benchmark_tsv_path", help="Path to the benchmark TSV file.")
    parser.add_argument("model_name", help="Model name.")
    args = parser.parse_args()
    append_results_to_benchmark(args.benchmark_tsv_path, args.model_name)

if __name__ == '__main__':
    main()
