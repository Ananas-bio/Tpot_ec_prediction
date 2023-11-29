# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 14:49:00 2023

@author: Ana Patricia Silva
"""

import pandas as pd
import argparse
#from Bio import SeqIO
from Bio.SeqIO.FastaIO import SimpleFastaParser
from EC_number_prediction import Sequence, Swiss_Model, C40_Model

import time

def argument_parser(version=None):
    parser = argparse.ArgumentParser()
    #parser.add_argument('-o', '--output_dir', required=True, help="Output directory") #could be added as an option

    parser.add_argument('-i', '--fasta_file', required=True, help="Input fasta file") 
    parser.add_argument('-l', '--level', default=str(3), help="Level of prediction")
    parser.add_argument('-m', '--model', default="c40", choices=["c40", "swiss"], help="Choice of model")
    return parser



def main():
    start = time.time()
    parser = argument_parser(version=None)

    options = parser.parse_args()
    file = options.fasta_file
    level = options.level
    model = options.model

    # output_dir = options.output_dir
    # if not os.path.isdir(output_dir):
    #     os.mkdir(output_dir)
    #predicted = " "
    sequences = []
    cod = []
    conf_scores = []
    if model == "swiss":
    with open(file) as fasta_file:
        for codes, v in SimpleFastaParser(fasta_file):
            print(f"{codes}")

            print("Embedding start...", flush = True)
            value = Sequence.Sequence(v).embedding()
            print("Embedding done!", flush = True)
            print("Predicting...", flush = True)

##### Choice of Models ####
            if model == "swiss":
                prediction = Swiss_Model.Swiss_Model([value])
            elif model == "c40":
                prediction = C40_Model.C40_Model([value])

##### Prediction of up to which EC number

            #if str(level) == '0':
            #    predicted = prediction.is_enzyme([value])
            if level == '1':
                predicted = prediction.lvl1_pred([value])
            elif level == '2':
                predicted = prediction.lvl2_pred([value])
            else:
                predicted = prediction.lvl3_pred([value])
            sequences.append(predicted[0])
            cod.append(codes[0])
            conf_scores.append(predicted[1])
 
    end = time.time()
    print(f"Time spent in predictions: {round((end-start)/60)} minutes")
    df = pd.DataFrame(zip(cod,sequences,conf_scores))
    df.columns = ["Code", "EC_number", "Confidence"]
    print(df.head())
    df.to_csv("predicitions.tsv", sep=" ")
    
    #return sequences #in case one wishes to have the sequences returned in the terminal

if __name__ == "__main__":
    main()

