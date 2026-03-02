# HDFS MapReduce — Movie Dataset Analytics

A Hadoop MapReduce pipeline that processes a movie dataset to extract and analyze titles, genres, and ratings by year. Implements mapper, combiner, and reducer stages in Python for Hadoop Streaming.

## Use Case

Big data coursework or practitioners learning Hadoop Streaming with a real-world dataset. Demonstrates how to build a multi-stage MapReduce pipeline (mapper → combiner → reducer) using plain Python scripts piped through Hadoop.

## Features

- Parses tab-separated movie records (uid, title, genres, year, rating)
- Optional year-filter via `years.txt` to restrict output to specific years
- Three-stage pipeline: mapper emits per-record tuples, combiner does local aggregation, reducer produces final output
- Compatible with any Hadoop 3.x cluster or pseudo-distributed single-node setup

## Tech Stack

| Layer | Tools |
|---|---|
| Language | Python 3.x (stdin/stdout streaming) |
| Distributed Processing | Apache Hadoop 3.x (MapReduce Streaming) |
| Storage | HDFS |

## Prerequisites

- **Java 8 or 11** — verify with `java -version`
- **Apache Hadoop 3.x** — verify with `hadoop version`
  - [Single-node setup guide](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html)
- **Python 3.x** available on all cluster nodes — verify with `python3 --version`

## Installation

No Python packages required — only the standard library (`sys`) is used.

Ensure Hadoop is running:

```bash
start-dfs.sh
start-yarn.sh
```

## Upload Input Data to HDFS

```bash
hdfs dfs -mkdir -p /input/movies
hdfs dfs -put your_movies_dataset.tsv /input/movies/
```

Input must be tab-separated with columns: `uid`, `title`, `genres`, `year`, `rating`

## Running with Hadoop Streaming

```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -files mapper.py,reducer.py,combiner.py,years.txt \
  -mapper "python3 mapper.py" \
  -combiner "python3 combiner.py" \
  -reducer "python3 reducer.py" \
  -input /input/movies \
  -output /output/results
```

View results:

```bash
hdfs dfs -cat /output/results/part-*
```

## Local Testing (No Hadoop Required)

Test the pipeline locally using Unix pipes:

```bash
cat your_movies_dataset.tsv | python3 mapper.py | sort | python3 combiner.py | sort | python3 reducer.py
```

## Project Structure

```
├── mapper.py     # Parses input, filters by year, emits (year, title, rating)
├── combiner.py   # Local aggregation before shuffle phase
├── reducer.py    # Final aggregation to produce output
├── years.txt     # Optional year filter file (one year per line)
├── results.txt   # Sample output from a previous run
├── ITNPBD7_Assignment_2024_3003263.docx  # Assignment report
└── ITNPBD7_Assignment_2024_3003263.pdf   # Assignment report (PDF)
```

## Output & Results

The reducer outputs aggregated movie data grouped by year. See `results.txt` for a sample of expected output format.

| Output | Description |
|---|---|
| HDFS `/output/results/` | Final MapReduce output files (part-00000, etc.) |
| `results.txt` | Sample output included in repo for reference |

## Notes

- The combiner stage is optional but reduces network shuffle traffic significantly on large datasets
- Ensure input files use **LF** (Unix) line endings — Windows CRLF line endings will cause parsing issues in the mapper
- Adjust the `years.txt` file to filter for specific years; leave it empty or remove the filter logic in `mapper.py` to process all years
