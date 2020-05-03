from rwt.callers import *
import argparse
import os
import sys

def main():
    args = grab_arguments()

    print(args)

    if args.job == 'mask':
        # if dir isn't empty, remove previous results
        ofs = [args.outdir + "/" + args.fasta + x for x in [".tbl",".out",".masked",".cat"]]

        for f in ofs:
            if os.path.isfile(f):
                os.unlink(f)
        call_repeatmasker(args.fasta,
                args.repeat_lib,
                dir = args.outdir,
                cores = args.cores)
    elif args.job == 'fa2gtf':
        call_fa2gtf(args.fai, args.gtf)
    elif args.job == 'clean_repbase_fa':
        call_repbase_fixer(args.repeat_lib, args.ofasta)

    sys.exit(0)


def grab_arguments():
    desc = "Generation of masked genome references with consensus repeats added."
    parser = argparse.ArgumentParser(description = desc)


    subparsers = parser.add_subparsers(help='sub-command help', dest='job', required=True)


    parser_mask = subparsers.add_parser('mask', help='mask a reference genome fasta with RepeatMasker')
    parser_mask.add_argument("fasta",
        type = str,
        help = "path to genome fasta")
    parser_mask.add_argument("repeat_lib",
        type = str,
        help = "repeatmasker-compatible repeat library")
    parser_mask.add_argument("--outdir",
        dest="outdir",
        action="store",
        default = "./",
        help="Directory in which to place output.")
    parser_mask.add_argument("--cores",
        dest="cores",
        action="store",
        default = 1,
        help="Max N cores to use.")


    parser_repbase_gtf = subparsers.add_parser('clean_repbase_fa', help="create a fasta with cleanly formatted names from repbase library")
    parser_repbase_gtf.add_argument("repeat_lib",
        type = str,
        help = "repeatmasker-compatible repeat library")
    parser_repbase_gtf.add_argument("ofasta",
        type = str,
        help = "output fasta")

    parser_fa2gtf = subparsers.add_parser("fa2gtf", help="create a gtf with a feature for all sequences in a fasta")
    parser_fa2gtf.add_argument("fai", type=str, help="fasta index file [samtools faidx]")
    parser_fa2gtf.add_argument("gtf", type=str, help="output gtf")


    args = parser.parse_args()
    return args



if __name__ == "__main__":
    main()
