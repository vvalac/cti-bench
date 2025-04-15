# cti-bench

This repository contains the data and evaluation scripts for the paper
[CTIBench: A Benchmark for Evaluating LLMs in Cyber Threat Intelligence](https://arxiv.org/abs/2406.07599), accepted at NeurIPS 2024. CTIBench is a comprehensive suite of benchmark tasks and datasets designed to evaluate Large Language Models (LLMs) in the field of Cyber Threat Intelligence (CTI).

Dataset details can be found at huggingface: https://huggingface.co/datasets/AI4Sec/cti-bench

`append_results.py` takes as input the path to a responses tsv file and a model name. It appends a new column to the _-responses.tsv of your choice along with the results from the corresponding model name's _{name}\_result.txt file. Its usage from within the evaluation directory is:

```
python append_results.py('results/cti-{test}-response.tsv', '{model_name}')
```

`evaluation` directory contains scripts to evaluate model performance and the response for 5 LLMs - ChatGPT3.5, ChatGPT4, Gemini-1.5, LLAMA3-70B, LLAMA3-8B. T

`logs` directory contains the unprocessed response from ChatGPT3.5, ChatGPT4 and Gemini-1.5, etc for the tasks. These are copies of the \_{model_name}\_response.txt files output from model-prediction.ipynb.

## workflow

To add a new model to the bench, add it to the `model_mapping` dict within `evaluation/model-prediction.ipynb` and set the model accordingly. Run the block for a single test to validate your configuration, then run the corresponding benchmarks.

This will output two text files within the evaluation directory.

```
_{model_name}_response.txt
_{model_name}_result.txt
```

You must manually scan the result.txt file to find and adjust any anomolous lines that may have appeared due to REGEX failures.

Once cleaned, run append_results.py to add the model's results to the corresponding tsv file.

Lastly, run the evaluation.ipynb notebook to calculate accuracy statistics.

Once you are done, rename \_response.txt to "cti-{benchmark}" and add it to a directory named after the model, i.e. `GPT4o/cti-mcq.txt`
