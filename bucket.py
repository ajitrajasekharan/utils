import pdb
import sys
import argparse
from collections import OrderedDict

DEFAULT_DELIMITER=','
DEFAULT_PRECISION=3
NORM_PRECISION=2
DEFAULT_INDEX=1


def bucket(params):
        f_name = params.input
        delimiter = params.delimiter
        reverse = params.reverse
        field_index = params.field
        precision = params.precision
        cdf = params.cdf
        norm = params.norm
        norm_precision = params.norm_precision
        with open(f_name) as fp:
            bucket = {}
            for line in fp:
                if (len(line) >= 1):
                        line = line.rstrip('\n')
                        arr = line.split(delimiter)
                        if (len(arr) >= field_index):
                            val = round(float(arr[field_index]),precision)
                            if (val in bucket):
                                bucket[val] += 1
                            else:
                                bucket[val] = 1
            rev_stat = True if reverse else False
            sorted_d = OrderedDict(sorted(bucket.items(), key=lambda kv: kv[0], reverse=rev_stat))
            if (norm):
                sum_val = 0
                for k in sorted_d:
                    sum_val += sorted_d[k]
                for k in sorted_d:
                    sorted_d[k] = round((float(sorted_d[k])/sum_val)*100,norm_precision)
            if (cdf):
                sum_val = 0
                for k in sorted_d:
                    curr_val = sorted_d[k]
                    sorted_d[k] += sum_val
                    sum_val += curr_val
                for k in sorted_d:
                    print(str(k)+delimiter+str(round(float(sorted_d[k])/sum_val,1)))
            else:
                for k in sorted_d:
                    print(str(k)+delimiter+str(sorted_d[k]))
     


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate sentence embeddings for input  ',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-input', action="store", dest="input",required=True, help='Input file')
    parser.add_argument('-delimiter', dest="delimiter", action='store',default=DEFAULT_DELIMITER, help='field separator in input')
    parser.add_argument('-precision', dest="precision", action='store',default=DEFAULT_PRECISION,type=int,help='precision to bucket- an integer value')
    parser.add_argument('-norm_precision', dest="norm_precision", action='store',default=NORM_PRECISION,type=int,help='precision if normalizineg - an teger value')
    parser.add_argument('-field', dest="field", action='store',default=DEFAULT_INDEX,type=int,help='index of field to bucket - 0 indexing')
    parser.add_argument('-reverse', dest="reverse", action='store_true',help='Reverse sort')
    parser.add_argument('-no-reverse', dest="reverse", action='store_false',help='No reverse sort')
    parser.add_argument('-cdf', dest="cdf", action='store_true',help='CDF')
    parser.add_argument('-no-cdf', dest="cdf", action='store_false',help='No CDF')
    parser.add_argument('-norm', dest="norm", action='store_true',help='normalize the column being bucketed')
    parser.add_argument('-no-norm', dest="no-norm", action='store_true',help='do not normalize the column being bucketed')
    parser.set_defaults(cdf=False)
    parser.set_defaults(norm=False)
    parser.set_defaults(reverse=False)
    results = parser.parse_args()
    bucket(results)
