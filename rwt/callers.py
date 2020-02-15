
def call_repeatmasker(fasta, lib, engine = "ncbi", cores = 1, dir = "./"):

    # RepeatMasker -e ncbi -pa 28 -s
    #    -lib dmel_repbase_lib.fasta
    #    -no_is -nolow
    #    -dir .
    #    dmel-all-chromosome-r6.22.fasta
    import subprocess
    from checkers import check_installation
    if not (check_installation("RepeatMasker")):
        sys.exit()

    return(subprocess.run(["RepeatMasker",
        "-e " + engine,
        str(cores),
        "-s",
        "-lib " + lib,
        "-no_is",
        "-nolow",
        "-dir " + dir,
        fasta]))
