from callers import *
import argparse
import os

def main():
    args = grab_arguments()

    # if dir isn't empty, remove previous results
    ofs = [args.outdir + "/" + args.fasta + x for x in [".tbl",".out",".masked",".cat"]]

    for f in ofs:
        if os.path.isfile(f):
            os.unlink(f)

    call_repeatmasker(args.fasta,
        args.repeat_lib,
        dir = args.outdir,
        cores = args.cores)

    #print(call_repeatmasker())

def grab_arguments():
    desc = "Generation of masked genome references with consensus repeats added."
    parser = argparse.ArgumentParser(description = desc)
    parser.add_argument("fasta",
        type = str,
        help = "path to genome fasta")
    parser.add_argument("repeat_lib",
        type = str,
        help = "repeatmasker-compatible repeat library")
    parser.add_argument("--outdir",
        dest="outdir",
        action="store",
        default = "./",
        help="Directory in which to place output.")
    parser.add_argument("--cores",
        dest="cores",
        action="store",
        default = 1,
        help="Max N cores to use.")
    args = parser.parse_args()
    return args



if __name__ == "__main__":
    main()
