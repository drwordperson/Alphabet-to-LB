with open('tur-cy_web_2016_10K-sentences.txt', encoding='utf8') as f:
    text = f.read()
    
myfile = open('Turkish_LBtext.txt', 'w')
myfile.write(text)
print('Input file opened')
myfile.close()

#  This looks like a good guide to understanding config files:  https://martin-thoma.com/configuration-files-in-python/

# What goes in the config file?
# What input data file
# Some brief line of code converting digraphs into single characters
# List of letters (phonemes) and digraphs in the language and phonoloical categories to which they belong
# Some brief line of code converting digraphs into single characters

######  Later moved to a config file

uppercase = ['A', 'Â', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'Ğ', 'H', 'I', 'İ', 'Î', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö', 'P', 'R', 'S', 'Ş', 'T', 'U', 'Ü', 'Û', 'V', 'Y', 'Z', 'Q', 'W', 'X']
lowercase = ['a', 'â', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'î', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş', 't', 'u', 'ü', 'û', 'v', 'y', 'z', 'q', 'w', 'x']

vowels = 'a|â|e|ı|i|î|o|ö|u|ü|û'
consonants = 'b|c|ç|d|f|g|h|j|k|l|m|n|p|r|s|ş|t|v|y|z|q|w|x'

stops = 'p|b|t|d|k|g|q'
affrics = 'c|ç'
frics = 'f|j|s|ş|v|h|z|w'
nasals = 'n|m'
liquids = 'l|r'
glides = 'y'
whitespace = r'\n|\s'

voiceless = ['p', 't', 'k', 'ç', 'f', 'ş', 's']
voiced = ['b', 'd', 'g', 'c', 'v', 'j', 'z']

ff = re.compile('Ğ|ğ') #Letter not realized as a consonant/vowel, so deleted.
text=re.sub(ff, '', text)

ff = re.compile('X|x') #Underlying ks.
text=re.sub(ff, 'ks', text)

ff = re.compile('Q|q') 
text=re.sub(ff, 'k', text) #Foreign letter.  Pronounced k.

ff = re.compile('W|w') 
text=re.sub(ff, 'v', text) #Foreign letter.  Pronounced either w or u; in my sample, w seemed to predominate and I wasn't going to sort these out by hand.
