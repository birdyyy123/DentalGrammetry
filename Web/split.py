import subprocess
from subprocess import check_output


def split (x):
    X = x.decode("utf-8")
    Y = X.split("\n")
    return(Y)

def check_txt (x):
    for i in x:
        if "Mean distance" in i:
            Y = i[19:]
    return(Y)

out = subprocess.check_output(["cloudcompare.CloudCompare", "-silent" ,"-o", "/home/bird/Downloads/meshroom-2019.2.0/op/bird.bin", "-o", "/home/bird/Downloads/meshroom-2019.2.0/op/bird2.bin","-ICP", "-c2c_dist"])
V = split(out)
U = check_txt(V)
##if "[ComputeDistances]" in V:

print(U)
