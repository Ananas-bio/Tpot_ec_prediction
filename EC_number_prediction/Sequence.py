# -*- coding: utf-8 -*-
"""
Created on Thu May 25 16:42:04 2023

@author: Patricia
"""
import numpy as np
from bio_embeddings.embed import ProtTransBertBFDEmbedder, ProtTransT5XLU50Embedder

class Sequence:
    def __init__ (self, seq):
        if (len(seq) > 5000):
            raise Exception("Protein sequence with more than 5000 aminoacids.")
        self.seq = seq
        #self.codes = seq[0]


    def embedding(self):
        embedder_bert, embedder_t5 = ProtTransBertBFDEmbedder(), ProtTransT5XLU50Embedder(legacy=True)
        embedding_bert,embeddings_t5 = embedder_bert.embed(self.seq), embedder_t5.embed(self.seq)
        red_emb_bert, red_emb_t5 = ProtTransBertBFDEmbedder.reduce_per_protein(embedding_bert), ProtTransT5XLU50Embedder.reduce_per_protein(embeddings_t5)
        #print(f"And this is the embedding length: {len(np.concatenate([red_emb_bert, red_emb_t5]))}")

        return np.concatenate([red_emb_bert, red_emb_t5])


    def codes_embs(self):
        seqs = self.embedding()
        #print(seqs)
        return self.codes, seqs

if __name__ == "__main__":
    array =  "MTQPQMAPICLVENHNEQLSVNQEAIEILDKISQPVVVVAIVGWSHTGKSYLMNCLAGQNHVSGTLPTSQRFPSGLHRAVSDQGHLDVVHAPPHQARALVLLDTEGLGDVEKGDPKNDLWIFALSVLLSSTFVYNSMNTINHQALEQLHYVTELTELIRAKSSPNPHGIKNSTEFVSFFPDFVWTVRDFMLELKLNGEDITSDEYLENALKLIPGNNPRIQASNSARECIRRFFPNRKCFVFEWPTHDIEPSESEKAISSVLSLLRKKDRL"
    print(len(array))
    s = Sequence(array)
    s.embedding()
