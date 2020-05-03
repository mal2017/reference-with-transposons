# reference-with-transposons

`rwt` is a set of small utilies for making reference genomes/transcriptomes that contain additional records, such as consensus transposable element sequence.

Currently, most utilites are written with consensus TE sequences from RepBase in mind.

# usage

Runs `Repeatmasker`.

Outputs your.fa.{tbl, out, masked, cat} to the directory of your choosing ('./' by default).

Files fitting this pattern will be removed prior to running `rwt`.

```
rwt mask your.fa repbase.fa

```

Removes '#' from record names in RepBase lib.

```
rwt clean_repbase_fa repbase.fa repbase.clean.fa
```

Makes a gtf with a record for each sequence in a fasta.
```
rwt fa2gtf repbase.clean.fa repbase.gtf
```

# installation

```
# from source

cd reference-with-transposons
pip install .

# from conda

conda install -c mal2017 rwt

# singularity/docker

... in progress ...


```

# dependencies

* R
* multiple tidyverse packages
* rtracklayer
* RepeatMasker
