#! /bin/sh
#
# transactionRed.sh
# Copyright (C) 2019 g <g@ABCL>
#
# Distributed under terms of the MIT license.
#
java -jar spmf.jar run Apriori_TID test_files/contextPasquier99.txt output_transaction.txt 40%
