# Advent of code solutions

This repo contains solutions for different years of advent of code. 

How to run:

```bash
python -m aocpy run {year} {day}
```

Or if you want to run it against test data you may run

```bash
python -m aocpy run {year} {day} --test
```


If you want to create a solution from a template and download inputs for the problem,
just call

```
python -m aocpy prepare {year} {day}
```

This will create a solution file. If you provide `AOC_SESSION` env variable, it will also download your inputs.