#!/usr/bin/python
#_*_coding:utf-8_*_

import sys
import re


#1行1文となるように、文の途中で改行されているものを探し、1行が"."で終わるようにする
def fix_line(changed_line):
    for line in changed_line:
        #if line.endswith("\n"):
         #   line = line.replace(" ", "\n")
        print line


def main():
    fin = open(sys.argv[1])
    char_1 = re.compile("\<.*?\>")
    char_2 = re.compile("UnhideWhenUsed=.*")
    char_3 = re.compile("<p><span style=\"color: #ffffff;\"> .</span></p>")
    char_4 = re.compile("\&.*?;")
    char_5 = re.compile("Javascript is .* this page\.")
    char_6 = re.compile("DefSemiHidden=\"[a-z]*\" DefQFormat=\"[a-z]*\" DefPriority=\"[0-9]*\"")
    char_7 = re.compile("<w:LsdException Locked=\"[a-z]*\" Priority=\"[0-9]*\" SemiHidden=\"[a-z]*\"")
    char_8 = re.compile("LatentStyleCount=\"[0-9]*\">")
    char_9 = re.compile("href=\"\#_[0-9]*\">[0-9]")
    char_10 = re.compile("\".*\+")
    char_11 = re.compile("[a-zA-Z]:\"[a-zA-Z]\"\,")

    sent_pattern = re.compile("(?P<end>\.|\;|\:|\?|\!|\") (?P<start>[A-Z])")
    #sentense_list = []
    #text_list = []
    #count_all = 0
    #count_not = 0
    #count_true = 0
    #count = 0

    for line in fin:
        line = line.strip()
        line = char_1.sub("", line)
        line = char_2.sub("", line)
        line = char_3.sub("", line)
        line = char_4.sub("", line)
        line = char_5.sub("", line)
        line = char_6.sub("", line)
        line = char_7.sub("", line)
        line = char_8.sub("", line)
        line = char_9.sub("", line)
        line = char_10.sub("", line)
        line = char_11.sub("", line)
        #line = line.replace("&nbsp;", "")
        if line:
            #print line
            if line == "\n":
                continue
            #if "=" in line or "jQuery" in line or "http://" in line or "html" in line or ">" in line or :
             #   pass
            if "=" in line or "jQuery" in line or "http:/" in line or "html" in line or ">" in line or "{" in line or "}" in line:
                continue
            if "universalPixelApi" in line:
                continue

            #1行1文にするため，(. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし，入力された文書を1行1文の形式で出力する．
            print sent_pattern.sub(lambda m: "%s\n%s" % (m.group("end"), m.group("start")), line.strip())
            #print count

        #正規表現にマッチしている文字列をリストで表示
        #m = changed.findall(line)
        #print m

    """
        #1行1文の形式にするため、ピリオドが無かったらsentense_listへ
        #ピリオドがあった場合はtext_listへappendしていく
        #if not changed_line.endswith("."):
            #sentense_list.append(changed_line)

        #if changed_line.endswith("."):
            #text_list.append(" ".join(sentense_list))
            #text_list.append(changed_line)
            #print text_list
            #sentense_list = []
    #print "".join(text_list)
    """

#extract_textで<p></p>, <dd></dd>で囲まれた文を抽出した文に
#含まれている細かいゴミ, タグなどを取り除く
if __name__ == '__main__':
    main()
