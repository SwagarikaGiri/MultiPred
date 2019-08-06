import pickle
import click as ck
Unique_protein=[]
import pandas as pd

Root_out="data/unique_protein/"
Root="data/"
@ck.command()
@ck.option(
    '--function',
    default='mf',
    help='Ontology id (mf, bp, cc)')
@ck.option(
	'--filetype',
	default='train',
	help="train/test")

# @ck.option(
#     '--orgs',
#     help='HUMAN/MOUSE/RAT/DROME(Fruit fly)/SCHPM(Fission yeast)/YEAST/DANRE(Zebrafish)/MYCTU(Mycobacterium)/ECOLI/PSEAE(Pseudomonas)/BACSU',
#     default='DROME')

def main(function,filetype):
	input_pickle_file=str(Root+filetype+"-"+function+".pkl")
	protein_file=str(Root_out+filetype+"-"+function+"-"+"accessions.txt")
	# pickle_in = open(input_pickle_file,"rb")
	dict_data = pd.read_pickle(input_pickle_file)
	protein_name=dict_data["accessions"]
	for ele in protein_name:
		if ele not in Unique_protein:
			Unique_protein.append(ele)
	print(Unique_protein)
	with open(protein_file, 'a') as f:
		for ele in Unique_protein:
			print(ele)
			f.write(str(ele)+ '\n')

if __name__ == '__main__':
	main()