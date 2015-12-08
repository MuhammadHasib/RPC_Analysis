#!/bin/bash

#sqlplus CMS_RPC_R/rpcr34d3r@cms_omds_adg     @wbm.sql


sqlplus CMS_RPC_R/rpcr34d3r@cms_omds_adg	@Re4all.sql

python RPC_Analysis.py  > Restfile_check

cat Restfile_check
