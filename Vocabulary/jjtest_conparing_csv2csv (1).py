# coding:utf8
import jieba
import jieba.analyse
import csv

input_csv_file = 'C:/Users/PeiYu/Desktop/news/data/newtalk_2019.csv'
output_csv_file = 'C:/Users/PeiYu/Desktop/news/data/text2.csv'
userdict_txt = "C:/Users/PeiYu/Desktop/newss/userdict525.txt"
stop_txt = 'C:/Users/PeiYu/Desktop/newss/stopword525.txt'

with open(input_csv_file, 'r', encoding='utf8')as csvfile: #讀csv
    with open(output_csv_file, 'w', encoding='utf_8_sig', newline='') as wbb:  #寫成csv
        data = csv.reader(csvfile)

        # 增加csv的讀取句數
        csv.field_size_limit(100000000)

        with open(userdict_txt, 'r', encoding='utf8')as stopword: #(此處可用萬用辭庫(功用:篩選未知詞) or  停用詞庫(功用:篩選關鍵字))
            stop = stopword.readlines()
            stopwords=[]
            for i in stop:
                stopwords.append(i.replace('\n',''))

            writer = csv.writer(wbb, delimiter=',')

            jieba.load_userdict(userdict_txt)  # 載入萬用辭庫來切新聞
            for texts in data:
                if texts[0] == r'title':
                    continue
                text = texts[0] + '，' + texts[3]

                word = jieba.cut(text)

                result1 = [i for i in word]
                result2 = set(result1)-set(stopwords)
                writer.writerow(result1)
                writer.writerow(result2)
                print(">")
                all_len = len(result1)
                final_len = len(result2)
                wbb.write(str(all_len)+"=>"+str(final_len)+'  '+str(int(final_len/all_len*100))+"%"+'\n\n')


