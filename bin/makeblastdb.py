#!/usr/bin/env python

import os.path
import subprocess
import os
import sys

def is_newer(filename1, filename2):
    mtime1 = os.path.getmtime(filename1)
    mtime2 = os.path.getmtime(filename2)
    if mtime1 <= mtime2:
        return False
    else:
        return True

def makeblastdb(fasta_filename, dbname, dbtype='nucl'):
    if dbtype not in ['nucl', 'prot']:
        raise ValueError('Invalid dbtype: {}'.format(dbtype))
    dustbin_file = open(os.devnull, 'w') # make a file that writes to /dev/null
    cmd = ['makeblastdb', '-in', fasta_filename, '-out', dbname, '-dbtype', dbtype]
    return_code = subprocess.call(cmd, stdout=dustbin_file)
    if return_code == 0:
        return True
    else:
        return False

if len(sys.argv) != 3 and len(sys.argv) != 4:
    sys.exit("Usage: {} <FASTA filename> <BLAST db name> [<DB type>]".format(os.path.basename(sys.argv[0])))

seq_filename = sys.argv[1]
dbname = sys.argv[2]
if len(sys.argv) == 4:
    dbtype = sys.argv[3]
else:
    dbtype = 'nucl'

blastdb_filename = dbname + '.nhr'

if not os.path.exists(blastdb_filename) or is_newer(seq_filename, blastdb_filename):
    print "Making BLAST database"
    makeblastdb(seq_filename, dbname, dbtype)
else:
    print "BLAST database already up to date"
