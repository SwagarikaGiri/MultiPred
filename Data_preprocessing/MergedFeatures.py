import numpy as np
import pandas as pd
import click as ck
import pickle
import csv

unique_accession=[]

@ck.command()
@ck.option(
    '--function',
    default='mf',
    help='Ontology id (mf, bp, cc)')
@ck.option(
    '--filetype',
    default='test',
    help='test/train type')





def main(function,filetype):
	list_of_new_index=[]
	unique_accession=find_unique_accession(function,filetype)
	print unique_accession
	df=load_org_df(function,filetype)
	index = df.index.values
	count=0
	for ele in index:
		protein_accession=df.loc[ele]["accessions"]
		if protein_accession in unique_accession:
			list_of_new_index.append(ele)
	df=df.loc[list_of_new_index]
	accessions=df['accessions'].values
	labels=df['labels'].values
	gos=df['gos'].values
	ngrams=df['ngrams'].values
	proteins=df['proteins'].values
	sequences=df['sequences'].values
	orgs =df['orgs'].values
	embeddings=df['embeddings'].values
	res_df = pd.DataFrame({'accessions':accessions,
		'gos':gos,'labels':labels,'ngrams':ngrams,
		'proteins':proteins,'sequences':sequences,
		'orgs':orgs,'embeddings':embeddings})
	print res_df
	res_df.to_pickle("data/structure"+filetype+"-"+function+'.pkl')
			



def load_org_df(function,filetype):
	filename=str("data/"+filetype+"-"+function+".pkl")
	df = pd.read_pickle(filename)
	return df









def find_unique_accession(function,filetype):
	list_=[]
	input_file=str("data/unique_protein/"+filetype+"_"+function+"_"+"accession_pbd_mapped.csv")
	with open(input_file) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		for line in csv_reader:
			list_.append(line[0])
	return list_



if __name__ == '__main__':
	main()