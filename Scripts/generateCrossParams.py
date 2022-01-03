import os
import sys

if not os.path.isdir('../ModelSetup'):
    os.mkdir('../ModelSetup')

language = "python3"
filePath = "../Scripts/crossTrain.py"
setupPath = "../ModelSetup/"

# models = ["bert-base-uncased", "bert-large-uncased", "bert-base-multilingual-uncased", "roberta-base", 
#           "roberta-large", "xlm-roberta-base", "xlm-roberta-large", "albert-base-v2", "albert-large-v2", 
#           "microsoft/deberta-v3-base", "microsoft/deberta-v3-large","facebook/bart-base","facebook/bart-large",
#           "vinai/bertweet-base", "vinai/bertweet-large", "cardiffnlp/twitter-xlm-roberta-base", "cardiffnlp/twitter-roberta-base"]
models = ["microsoft/deberta-v3-base"]
batchSize = [16]
warmupSteps = [125]
learningRate = [7e-5]
weightDecay = [0.5]

# ContextConfig = [i for i in range(1,32)]
ContextConfig = [1]

# normalizeDataset = ["regular", "normalized"]
normalizeDataset = ["regular"]

# samplingSize = [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0]
samplingSize = [0.95]

# randomSeed = [1,2,3,4,5]
randomSeed = [6,7,8,9,10,11,12,13,14,15]

# targetLabels = ["Gold","Predicted"]
targetLabels = ["Gold"]

domain = ["CrossDomain"]

with open(setupPath + "modelList.txt", "w") as file:
    for model in models:
        line = " ".join([language, filePath, model])
        for bs in batchSize:
            line1 = " ".join([line, str(bs)])
            for ws in warmupSteps:
                line2 = " ".join([line1, str(ws)])
                for lr in learningRate:
                    line3 = " ".join([line2, str(lr)])
                    for wd in weightDecay:
                        line4 = " ".join([line3,str(wd)])
                        for cc in ContextConfig:
                            line5 = " ".join([line4, str(cc)])
                            for state in normalizeDataset:
                                line6 = " ".join([line5, state])
                                for ss in samplingSize:
                                    line7 = " ".join([line6, str(ss)])
                                    for rs in randomSeed:
                                        line8 = " ".join([line7, str(rs)])
                                        for ts in targetLabels:
                                            line9 = " ".join([line8, ts])
                                            for d in domain:
                                                file.write(" ".join([line9, d, "\n"]))

    file.close()
