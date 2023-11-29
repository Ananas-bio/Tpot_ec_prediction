# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 15:48:04 2023

@author: Ana Patricia Silva
"""

from sklearn import model_selection
from joblib import load
import os


from sklearn.exceptions import ConvergenceWarning

warnings.filterwarnings("ignore", category=ConvergenceWarning)

class C40_Model:
    def __init__ (self, embedding):
        self.embedding = embedding
        #self.lvl0 = 0
        self.lvl1 = 0
        self.lvl2 = 0
        self.lvl3 = 0
        self.lvl4 = 0

    #def is_enzyme(self, emb):
    #    model = load("EC_number_prediction/models/c40/c40_model_lvl0.pkl")
    #    m = model.predict(self.embedding)
    #    perc = model.predict_proba(self.embedding)
    #    if  m == 0:
    #        return "This sequence is not of an Enzyme", round(np.max(perc*100))
    #    else:
            return "This sequence is of an Enzyme", round(np.max(perc*100))

    def lvl1_pred(self, emb):
#        res, conf = self.is_enzyme(self.embedding)
#        if res == "This sequence is not of an Enzyme":
#            return "Not an Enzyme", conf
#        else:
        file = "EC_number_prediction/models/c40/c40_model_lvl1.pkl"
        model = load(file)
        conf = round(np.max(model.predict_proba(self.embedding)*100))
            m = model.predict(self.embedding)
            # print(f"this here is the embedding {self.embedding}")
        return int(m), conf

    def lvl2_pred (self, emb):
        #print(self.embedding)
        self.lvl1, conf = self.lvl1_pred(self.embedding)
        #if self.lvl1 == "Not an Enzyme":
        #    return "Not an Enzyme", conf

        file = f"EC_number_prediction/models/c40/c40_model_mainclass{int(self.lvl1)}.pkl"
        model = load(file)
        self.lvl2 = model.predict(self.embedding)
        conf_2 = round(np.max(model.predict_proba(self.embedding)*100))

        return f"{self.lvl1}.{int(self.lvl2)}", f"{conf}%.{conf_2}%"

    def lvl3_pred(self, emb):
        #add the fact that some will go immediately for other subclasses (each)
        # individual case

        self.embedding = np.array(self.embedding, dtype="float64")
        #if self.lvl2_pred(self.embedding)[0] == "Not an Enzyme":
        #    return self.lvl2_pred(self.embedding)

        lvl1_sc, lvl2_sc = self.lvl2_pred(self.embedding)
        self.lvl1, conf_1 = lvls_sc.split(".")
        self.lvl2, conf_2 = conf_sc.split(".")

        if self.lvl2 == "-":
            return f"{self.lvl1}.{self.lvl2}.-", f"{conf_1}%.{conf_2}%.-"

        file = f"EC_number_prediction/models/c40/subclassses/c40_model_c{self.lvl1}_s{self.lvl2}.pkl"

        if os.path.isfile(file) == True:
            model = load(file)
            #print(f"{self.lvl1}.{self.lvl2}")
            self.lvl3 = model.predict(self.embedding)
            conf_3 =  round(np.max(model.predict_proba(self.embedding)*100))
            return f"{self.lvl1}.{self.lvl2}.{int(self.lvl3)}", f"{conf_1}%.{conf_2}%.{conf_3}%"
        else:
            return f"{self.lvl1}.{self.lvl2}.-", f"{conf_1}%.{conf_2}%.-"