#!/usr/bin/pyton
#_*_coding:utf-8_*_

import sys


def extract_dd():
    #試しにstanford/about/history/indexでやってみる
    #fin = open("/Users/shioda/reseach/ISM_joint_research/webpages/www.stanford.edu/about/history/index.html")
    fin = open(sys.argv[1])
    exist = False
    for line in fin:
        line = line.strip()
        #print exist
        if line.startswith("<dd>") or exist is True:
        #if line.startswith("<p>"):
            print line
            exist = True

            if line.endswith("</dd>"):
                #print line
                exist = False


def main():
    #試しにstanford/about/history/indexでやってみる
    #fin = open("/Users/shioda/reseach/ISM_joint_research/webpages/www.stanford.edu/about/history/index.html")
    fin = open(sys.argv[1])
    exist = False
    for line in fin:
        line = line.strip()
        #print exist

        #このタグの中にも文章が入ってそう。。
        #if line.startswith("<p class=\"lead\">"):
        #    print line

        #<li></li>が入るのを避けるため
        #if "<li>" in line:
        #    continue

        if line.startswith("<p>") or exist is True:
        #if line.startswith("<p>"):
            print line
            exist = True

            if line.endswith("</p>"):
                #print line
                exist = False


#クロールしたtextの中から<p></p>, <dd></dd>に囲まれたtextを抽出
if __name__ == '__main__':
    main()
    #extract_dd()
