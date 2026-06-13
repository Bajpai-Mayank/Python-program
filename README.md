# Python Logic & Algorithmic Collection 🚀

A curated Python repository with small programs, logic exercises, and data-driven scripts. This project is organized into focused folders that highlight number theory, string algorithms, Python concepts, creative utilities, and simple data science explorations.

## 📂 Repository Structure

- `Number_Logic/` — special number checks and sequence generation.
- `String_Algorithm/` — string puzzles, encodings, and validation tools.
- `Problem/` — Python demonstrations, utilities, and concept experiments.
- `Creative/` — interactive scripts, visualization helpers, and games.
- `Data_Science/` — data analysis, plotting, and dataset generation.
- `algorithm_submissions.csv` — sample performance dataset used by analysis scripts.
- `periodic_table.csv` — atomic element data used by visualization scripts.

## 🔍 Folder Summaries

### Number_Logic
These scripts implement common numeric patterns and checks.
- `automorphic_number.py` — checks whether a number ends with its square.
- `disarium_number.py` — verifies if the sum of powered digits equals the number.
- `fascinating_number.py` — tests if concatenated multiples form a "fascinating" result.
- `kaprekar_number.py` — determines Kaprekar numbers by splitting square digits.
- `magic_number.py` — identifies a magic number through repeated digit-squared sums.
- `neon_number.py` — validates if the sum of digits of a square equals the original number.
- `niven_number.py` — checks divisibility of a number by the sum of its digits.
- `pronic_number.py` — detects numbers that are products of two consecutive integers.
- `tech_number.py` — recognizes numbers formed by splitting digits and applying powers.
- `tribonacci_series.py` — generates a Tribonacci sequence.

### String_Algorithm
String manipulation and classic text problems.
- `caesar_ciper_shift.py` — shifts letters using Caesar cipher logic.
- `length_encoding.py` — compresses strings using run-length encoding.
- `longest_palindrome.py` — finds the longest palindromic substring.
- `pangram.py` — checks whether a sentence contains every alphabet letter.
- `vowel_eater.py` — removes or transforms vowels in text.
- `word_frame.py` — displays words inside a framed border.

### Problem
Python concept examples and small utility programs.
- `complex_lambda.py` — experiments with lambda expressions and sorting.
- `custom_map.py` — demonstrates a simple map-like data structure.
- `Infinite_prime.py` — contains a prime generation concept using loops.
- `receipt.py` — simulates a basic receipt or billing output.
- `time_decorator.py` — measures execution duration for a task.

### Creative
Fun, interactive, and visual Python utilities.
- `anagram_game.py` — an interactive word-matching game with easy/medium/hard levels.
- `bg_remove.py` — removes image backgrounds using `withoutbg`.
- `Cowsay_test.py` — prints fun ASCII art using the `cowsay` package.
- `distribution_curve.py` — plots sample statistical distributions with Seaborn.
- `Words/` — contains word lists used by `anagram_game.py`.

### Data_Science
Data analysis and dataset preparation scripts.
- `algorithm_performance_tracker.py` — loads `algorithm_submissions.csv`, computes summary statistics, and creates boxplots.
- `algorithm_submission_gen.py` — generates a synthetic algorithm performance dataset.
- `element_comp.py` — visualizes atomic numbers and electronegativity from `periodic_table.csv`.
- `reel_analytics.py` — demonstrates simple data plotting of statistical distributions.

## ▶️ How to Run

From the repository root, run a script with Python:

```bash
python Number_Logic/magic_number.py
python String_Algorithm/pangram.py
python Problem/custom_map.py
python Creative/anagram_game.py
python Data_Science/algorithm_performance_tracker.py
```

> Note: Some scripts require data files in the same directory (`algorithm_submissions.csv` or `periodic_table.csv`) or optional packages like `pandas`, `matplotlib`, `seaborn`, `numpy`, `cowsay`, and `withoutbg`.

## 🧰 Recommended Dependencies

- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn
- cowsay
- withoutbg

Install common packages with:

```bash
pip install pandas numpy matplotlib seaborn cowsay withoutbg
```

## 💡 Notes

- The repository is ideal for learning Python logic, practicing small algorithms, and experimenting with data visualization.
- Scripts are intentionally simple and often use input prompts or direct file I/O.
- Many examples can be extended into more robust utilities or packaged as functions.

## 👨‍💻 Author
**Mayank Bajpai**

Building practical Python logic, algorithm practice, and data exploration projects.