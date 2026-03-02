# HDFS MapReduce — Movie Dataset Analytics

A Hadoop MapReduce pipeline that processes a movie dataset to extract and analyze titles, genres, and ratings by year. Implements mapper, combiner, and reducer stages in Python for Hadoop Streaming.

## Tech Stack

- **Python** — sys (stdin/stdout streaming)
- **Hadoop** — HDFS, MapReduce Streaming

## Prerequisites

- Java 8 or 11
- Apache Hadoop 3.x ([installation guide](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html))
- Python 3.x available on all cluster nodes

## Project Structure

```
├── mapper.py          # Parses input, filters by year, emits (year, title, rating)
├── combiner.py        # Local aggregation before shuffle
├── reducer.py         # Aggregates final output
├── results.txt        # Sample output
├── ITNPBD7_Assignment_2024_3003263.docx  # Assignment report
└── ITNPBD7_Assignment_2024_3003263.pdf   # Assignment report (PDF)
```

## Input Format

Tab-separated fields: `uid`, `title`, `genres`, `year`, `rating`

The mapper reads an optional `years.txt` filter file to restrict output to specific years, then emits records per genre with the format: `year\ttitle\trating`

## Running with Hadoop Streaming

```bash
hadoop jar hadoop-streaming.jar \
  -files mapper.py,reducer.py,combiner.py,years.txt \
  -mapper mapper.py \
  -combiner combiner.py \
  -reducer reducer.py \
  -input /input/movies \
  -output /output/results
```
