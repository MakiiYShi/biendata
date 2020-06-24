# 将训练集、测试集的所有org,title,abstract,venue都清洗，并存储在gene/all_text.txt中。
# 再用其训练word2vec

import json, codecs, re
from gensim.models import word2vec

'''
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\read trainset and validation set\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
f = codecs.open("./OAG-v2-track1/train_pub.json", "r", encoding="utf-8")
f1 = codecs.open("./OAG-v2-track1/valid/sna_valid_pub.json", "r", encoding="utf-8")
pubs_raw = json.load(f)  # train set
pubs_raw1 = json.load(f1)  # validation set

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\word2vec\\\\\\\\\\\\\\\\\\\\\\\\\\\ #
# \\\\\\\\cleaning data....\\\\\\\
r = '[!“”"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~—～’]+'
out = open('gene/all_text.txt', 'w', encoding='utf-8')
for paperid in pubs_raw:
    paper = pubs_raw[paperid]
    # author's organization
    for author in paper["authors"]:
        if "org" in author:
            org = author["org"]
            org = org.strip()
            org = org.lower()
            org = re.sub(r, ' ', org)
            org = re.sub(r'\s{2,}', ' ', org).strip()
            if org != "":
                out.write(org + '\n')
    # title
    title = paper["title"]
    title = title.strip()
    title = title.lower()
    title = re.sub(r, ' ', title)
    title = re.sub(r'\s{2,}', ' ', title).strip()
    if title != "":
        out.write(title + '\n')
    # abstract
    if "abstract" in paper and type(paper["abstract"]) is str:
        abstract = paper["abstract"]
        abstract = abstract.strip()
        abstract = abstract.lower()
        abstract = re.sub(r, ' ', abstract)
        abstract = re.sub(r'\s{2,}', ' ', abstract).strip()
        if abstract != "":
            out.write(abstract + '\n')
    # venue
    venue = paper["venue"]
    venue = venue.strip()
    venue = venue.lower()
    venue = re.sub(r, ' ', venue)
    venue = re.sub(r'\s{2,}', ' ', venue).strip()
    if venue != "":
        out.write(venue + '\n')
    # keywords
    for keyword in paper["keywords"]:
        keyword = keyword.strip()
        keyword = keyword.lower()
        keyword = re.sub(r, ' ', keyword)
        keyword = re.sub(r'\s{2,}', ' ', keyword).strip()
        if keyword != "":
                out.write(keyword + '\n')

for paperid in pubs_raw1:
    paper = pubs_raw1[paperid]
    # author's organization
    for author in paper["authors"]:
        if "org" in author:
            org = author["org"]
            org = org.strip()
            org = org.lower()
            org = re.sub(r, ' ', org)
            org = re.sub(r'\s{2,}', ' ', org).strip()
            if org != "":
                out.write(org + '\n')
    # title
    title = paper["title"]
    title = title.strip()
    title = title.lower()
    title = re.sub(r, ' ', title)
    title = re.sub(r'\s{2,}', ' ', title).strip()
    if title != "":
        out.write(title + '\n')
    # abstract
    if "abstract" in paper and type(paper["abstract"]) is str:
        abstract = paper["abstract"]
        abstract = abstract.strip()
        abstract = abstract.lower()
        abstract = re.sub(r, ' ', abstract)
        abstract = re.sub(r'\s{2,}', ' ', abstract).strip()
        if abstract != "":
            out.write(abstract + '\n')
    # venue
    venue = paper["venue"]
    venue = venue.strip()
    venue = venue.lower()
    venue = re.sub(r, ' ', venue)
    venue = re.sub(r'\s{2,}', ' ', venue).strip()
    if venue != "":
        out.write(venue + '\n')
    # keywords
    for keyword in paper["keywords"]:
        keyword = keyword.strip()
        keyword = keyword.lower()
        keyword = re.sub(r, ' ', keyword)
        keyword = re.sub(r'\s{2,}', ' ', keyword).strip()
        if keyword != "":
                out.write(keyword + '\n')

print("ok")

'''

# \\\\\\\\\\\\\\\generate word vectors\\\\\\\\\\\\\\\
sentences = word2vec.Text8Corpus(r'gene/all_text.txt')
model = word2vec.Word2Vec(sentences, size=150, negative=5, min_count=2, window=5)
model.save('word2vec/word2vec2.model')
