
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
            
def strip_punctuation(x) :
    for each_char in x :
        if(each_char in punctuation_chars) : 
            x=x.replace(each_char, '')
    return x

def get_pos(x) :
    count = 0
    x = x.split()
    for each in x :
        word = strip_punctuation(each).lower()
        if(word in positive_words) : count += 1
    return count

def get_neg(x) :
    count = 0
    x = x.split()
    for each in x :
        word = strip_punctuation(each).lower()
        if(word in negative_words) : count += 1
    return count

# Open csv file to fetch data
csv_handle = open('project_twitter_data.csv')
to_handle = open('resulting_data.csv', 'w')

to_handle.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
to_handle.write('\n')
templist = list()
for line in csv_handle:
    line = line.strip()
    templist.append(line.split(','))
templist = templist[1:]
csv_handle.close()

for each in templist :
    pos_count = get_pos(each[0])
    neg_count = get_neg(each[0])
    retweets_count = each[1]
    replies_count = each[2]
    net_count = pos_count - neg_count
    entry = '{}, {}, {}, {}, {}'.format(retweets_count, replies_count, pos_count, neg_count, net_count)
    to_handle.write(entry)
    to_handle.write('\n')