## feature_selection based on Meta-Signer-master
#!/usr/bin/python
# File created on 2021/11
__author__ = "Wang,Yansu"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Wang,yansu"
__email__ = "Wangys_c@hotmail.com"


import subprocess
import datetime
import os
from optparse import OptionParser


def MakeOption():
    # make option
    parser = OptionParser(usage="%prog [-h] [-v] -i[--input=]-o[--output]",
                          version="%prog 1.2")
    parser.add_option("-i", "--input", action="store", dest="input",
                      help="the feature table with tsv format",
                      default=False)
    parser.add_option("-k", "--k_value", action="store", dest="k_values",
                      help="the top k features",
                      default=False)
    parser.add_option("-o", "--output", action="store", dest="output",
                      help="the results file",
                      default=False)
    (options, args) = parser.parse_args()

    # extract option from command line
    input = options.input
    output = options.output
    k = options.k_values
    return (input,k,output)

def run_command(cmd):
    # print("INFO: Running command: {0}".format(cmd), flush=True)
    print(cmd)
    return_code = subprocess.call(cmd, shell=True)
    if return_code != 0:
        print("ERROR: [{2}] Return code {0} when running the following command: {1}".format(return_code, cmd, datetime.datetime.now()))


def feature_ranking(inputfile,k,feature_selection_results):

    cmd1 = "python ./Meta-Signer-master/src/generate_feature_ranking.py -i "+ str(inputfile) + " -k "+ k+ " -o " + str(feature_selection_results)
    run_command(cmd1)

    return()

def main():
    input,k,output = MakeOption()
    feature_ranking(input,k, output)

if __name__ == "__main__":
    main()




