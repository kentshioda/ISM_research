#!/usr/bin/python
#_*_coding:utf-8_*_


import numpy as np
import sys
from gensim.models import word2vec
from collections import defaultdict


#クエリと文中の語の単語ベクトルのカーネルを計算
def calculateGaussianKernel(queryWordVec, corpusWordVec):
    #σは0.01でやってみる（適当）
    sigma = 0.1
    gaussianKernel = np.exp(-np.square(np.linalg.norm(queryWordVec - corpusWordVec)) / sigma ** 2)
    #print gaussianKernel

    return gaussianKernel


#文中の語corpusWordとクエリの語queryWordのベクトルをとってcalculateKernelに渡す
def getSimilarity(queryWords, loadModel):
    corpus = open("/Users/shioda/reseach/ISM_joint_research/webpages/extracted_p/corpus.txt", "r")
    similarity = defaultdict(lambda: float)
    for line in corpus:
        corpusWords = line.strip().split(" ")
        #1文毎にsumKernelを初期化
        sumKernel = 0
        #短すぎる文を消去
        if len(corpusWords) < 10:
            continue
        for m, corpusWord in enumerate(corpusWords):
            for n, queryWord in enumerate(queryWords):
                try:
                    gaussianKernel = calculateGaussianKernel(loadModel[queryWord], loadModel[corpusWord])
                except:
                    continue
                sumKernel += gaussianKernel
        similarity[line.strip()] = sumKernel / ((m + 1) * (n + 1))

    return similarity


def main():
    #入力：modelファイル + 入力の単語（カンマ区切り）
    if len(sys.argv) == 3:
        model = sys.argv[1]
        queryWords = sys.argv[2].decode("utf-8").strip().split(",")
    else:
        print "\t python similar.py model_file queryWords"
        exit()

    loadModel = word2vec.Word2Vec.load(model)

    #クエリに与えられた各単語と文中の語の単語ベクトルを獲得して，カーネルを計算
    #類似度を返す
    similarity = getSimilarity(queryWords, loadModel)

    #類似度の中から上位10位を出力
    for key, value in sorted(similarity.items(), key=lambda x: x[1])[-10:]:
        print key, value


    #for similar_word, similarity in loadModel.most_similar(positive=[averageVec]):
    #    print similar_word, similarity


if __name__ == '__main__':
    main()
