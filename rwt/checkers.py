
def check_installation(executable = "RepeatMasker"):

    # https://stackoverflow.com/questions/11210104/check-if-a-program-exists-from-a-python-script
    from shutil import which

    return which(executable) is not None
