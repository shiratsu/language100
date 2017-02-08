```
~/language100 on  master! ⌚ 0:38:32
$ wc -l hightemp.txt                                                                                                                                                                                                                  system
      24 hightemp.txt
```

```
~/language100 on  master! ⌚ 0:38:37
$ expand -t 1 hightemp.txt                                                                                                                                                                                                            system
高知県 江川崎 41 2013-08-12
埼玉県 熊谷 40.9 2007-08-16
岐阜県 多治見 40.9 2007-08-16
山形県 山形 40.8 1933-07-25
山梨県 甲府 40.7 2013-08-10
和歌山県 かつらぎ 40.6 1994-08-08
静岡県 天竜 40.6 1994-08-04
山梨県 勝沼 40.5 2013-08-10
埼玉県 越谷 40.4 2007-08-16
群馬県 館林 40.3 2007-08-16
群馬県 上里見 40.3 1998-07-04
愛知県 愛西 40.3 1994-08-05
千葉県 牛久 40.2 2004-07-20
静岡県 佐久間 40.2 2001-07-24
愛媛県 宇和島 40.2 1927-07-22
山形県 酒田 40.1 1978-08-03
岐阜県 美濃 40 2007-08-16
群馬県 前橋 40 2001-07-24
千葉県 茂原 39.9 2013-08-11
埼玉県 鳩山 39.9 1997-07-05
大阪府 豊中 39.9 1994-08-08
山梨県 大月 39.9 1990-07-19
山形県 鶴岡 39.9 1978-08-03
愛知県 名古屋 39.9 1942-08-02
```

```
~/language100 on  master! ⌚ 0:43:54
$ cut -f2 hightemp.txt                                                                                                                                                                                                                system
江川崎
熊谷
多治見
山形
甲府
かつらぎ
天竜
勝沼
越谷
館林
上里見
愛西
牛久
佐久間
宇和島
酒田
美濃
前橋
茂原
鳩山
豊中
大月
鶴岡
名古屋

~/language100 on  master! ⌚ 0:43:58
$ cut -f1 hightemp.txt                                                                                                                                                                                                                system
高知県
埼玉県
岐阜県
山形県
山梨県
和歌山県
静岡県
山梨県
埼玉県
群馬県
群馬県
愛知県
千葉県
静岡県
愛媛県
山形県
岐阜県
群馬県
千葉県
埼玉県
大阪府
山梨県
山形県
愛知県
```

```
~/language100 on  master ⌚ 0:45:35
$ paste co1.txt col2.txt                                                                                                                                                                                                              system
高知県	江川崎
埼玉県	熊谷
岐阜県	多治見
山形県	山形
山梨県	甲府
和歌山県	かつらぎ
静岡県	天竜
山梨県	勝沼
埼玉県	越谷
群馬県	館林
群馬県	上里見
愛知県	愛西
千葉県	牛久
静岡県	佐久間
愛媛県	宇和島
山形県	酒田
岐阜県	美濃
群馬県	前橋
千葉県	茂原
埼玉県	鳩山
大阪府	豊中
山梨県	大月
山形県	鶴岡
愛知県	名古屋

```


```
$ head -n 10 hightemp.txt                                                                                                                                                                                                                     2.3.1
高知県	江川崎	41	2013-08-12
埼玉県	熊谷	40.9	2007-08-16
岐阜県	多治見	40.9	2007-08-16
山形県	山形	40.8	1933-07-25
山梨県	甲府	40.7	2013-08-10
和歌山県	かつらぎ	40.6	1994-08-08
静岡県	天竜	40.6	1994-08-04
山梨県	勝沼	40.5	2013-08-10
埼玉県	越谷	40.4	2007-08-16
群馬県	館林	40.3	2007-08-16
```

```
$ tail -n 10 hightemp.txt                                                                                                                                                                                                                     2.3.1
愛媛県	宇和島	40.2	1927-07-22
山形県	酒田	40.1	1978-08-03
岐阜県	美濃	40	2007-08-16
群馬県	前橋	40	2001-07-24
千葉県	茂原	39.9	2013-08-11
埼玉県	鳩山	39.9	1997-07-05
大阪府	豊中	39.9	1994-08-08
山梨県	大月	39.9	1990-07-19
山形県	鶴岡	39.9	1978-08-03
愛知県	名古屋	39.9	1942-08-02
```

```
$ split -l 5 hightemp.txt

$ ll                                                                                                                                                                                                                                          2.3.1
total 176
-rw-r--r--  1 TTTTTTTT  XXXXXXXX\Domain Users   243B  2  7 13:11 co1.txt
-rw-r--r--  1 TTTTTTTT  XXXXXXXX\Domain Users   435B  2  7 13:11 col1_2.txt
-rw-r--r--  1 TTTTTTTT  XXXXXXXX\Domain Users   192B  2  7 13:11 col2.txt
-rw-r--r--  1 TTTTTTTT  XXXXXXXX\Domain Users   813B  2  7 13:11 hightemp.txt
-rwxr-xr-x  1 TTTTTTTT  XXXXXXXX\Domain Users    73B  2  4 00:38 language000.py
-rwxr-xr-x  1 TTTTTTTT  XXXXXXXX\Domain Users   149B  2  4 09:28 language001.py
-rwxr-xr-x  1 TTTTTTTT  XXXXXXXX\Domain Users    69B  2  4 10:00 language001_1.py
-rwxr-xr-x  1 TTTTTTTT  XXXXXXXX\Domain Users   217B  2  4 11:45 language002.py
-rwxr-xr-x  1 TTTTTTTT  XXXXXXXX\Domain Users   242B  2  4 11:55 language003.py
-rwxr-xr-x  1 TTTTTTTT  XXXXXXXX\Domain Users   1.0K  2  4 17:55 language004.py
-rwxr-xr-x  1 TTTTTTTT  XXXXXXXX\Domain Users   861B  2  5 10:36 language005.py
-rwxr-xr-x  1 TTTTTTTT  XXXXXXXX\Domain Users   569B  2  7 13:11 language006.py
-rwxr-xr-x  1 TTTTTTTT  XXXXXXXX\Domain Users   155B  2  7 13:11 language007.py
-rwxr-xr-x  1 TTTTTTTT  XXXXXXXX\Domain Users   734B  2  7 13:11 language008.py
-rwxr-xr-x  1 TTTTTTTT  XXXXXXXX\Domain Users   709B  2  7 13:11 language009.py
-rw-r--r--  1 TTTTTTTT  XXXXXXXX\Domain Users   3.6K  2  7 13:15 language010.md
-rw-r--r--  1 TTTTTTTT  XXXXXXXX\Domain Users   969B  2  7 13:11 language100_memo.txt
-rw-r--r--  1 TTTTTTTT  XXXXXXXX\Domain Users   169B  2  7 13:34 xaa
-rw-r--r--  1 TTTTTTTT  XXXXXXXX\Domain Users   174B  2  7 13:34 xab
-rw-r--r--  1 TTTTTTTT  XXXXXXXX\Domain Users   174B  2  7 13:34 xac
-rw-r--r--  1 TTTTTTTT  XXXXXXXX\Domain Users   161B  2  7 13:34 xad
-rw-r--r--  1 TTTTTTTT  XXXXXXXX\Domain Users   135B  2  7 13:34 xae
```

```
~/language100 on  master! ⌚ 13:34:25
$ cut -f1 hightemp.txt| sort | uniq                                                                                                                                                                                                           2.3.1
千葉県
埼玉県
大阪府
山形県
山梨県
岐阜県
愛媛県
愛知県
群馬県
静岡県
高知県
和歌山県
```


```
$ cut -f1 hightemp.txt | sort | uniq -c | sort -nr                                                                                                                                                                                            2.3.1
   3 群馬県
   3 山梨県
   3 山形県
   3 埼玉県
   2 静岡県
   2 愛知県
   2 岐阜県
   2 千葉県
   1 和歌山県
   1 高知県
   1 愛媛県
   1 大阪府
```
