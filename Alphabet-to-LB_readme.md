## Overview

```Alphabet-to-Linear-B.py``` takes a language corpus in an alphabetic script and converts it to the standard syllabification of Linear B, a pre-alphabetic writing system ca. 1400-1200 BCE used for writing the Greek language.  

This Python script removes punctuation, converts upper to lower-case letters, handles digraphs and many-to-one letter to phoneme mappings, neutralizes voicing distinctions, deletes final consonants, inserts dummy vowels at appropriate points, and inserts dashes to represent syllable breaks.  

## Usage

For language-specific processing, ```Alphabet-to-Linear-B.py``` takes a configuration file-- a Python script which eliminates many-to-one and one-to-many mappings between script and language, and also outlines the language's orthography and phonology.  ```Alphabet-to-Linear-B.py``` also takes a .txt file containing the section of text you would like converted.  Config files and data sets have been provided for Turkish and German, and sample inputs and outputs are as follows.

#### German:

1	"2022 war ein schwieriges Jahr mit einem holprigen Start, aber einem glänzenderen Abschluss", hiess es im Geschäftsbericht mit Blick auf die schwache erste Jahreshälfte.

	 fa a ʃi-fi-ri-ke ja mi-ti a-ne ho-pi-ri-ke ta-ta a-pe a-ne ke-le-ze-te-re a-pu-ʃu-lu hi e i ke-ʃe-te-pe-ri-ti mi-ti pi-li-ki a-u ti ʃa-fa-χe e-te ja-he-re-se-he-te

#### Turkish:

1	10. İkamet ettiği veya çalıştığı yeri değiştirdiğinde bağlı olduğu Parti Taban Örgütü’nü bilgilendirir.

	 i-ka-me-te e-ti fe-ya ça-lı-tı ye-ri te-i-ti-ti-te pa-lı o-tu pa-ti ta-pa ö-kü-tü-nü pi-ki-le-ti-ri

## Planned Improvements

Consonant clusters eliminated all at once as part of a for loop (currently debugging this)

Config files for additional languages (Finnish planned next)

Reduce runtime

## Disclaimer

Currently, this script is only made available as a code sample.  Many points of linguistic complexity are elided, and there is still some room to improve the accuracy of the script when it comes to acronyms and foreign words.  Please don't publish with this script!  You have been warned.

## Attribution

This script was developed by Christina Skelton.  Special thanks to Ivan Lee, Laurel Selvig, Taylor Berg-Kirkpatrick, Sherrylyn Branchaw, and Mike Skelton for troubleshooting assistance.  

Input data is taken from the [Leipzig Corpora Collection](https://corpora.uni-leipzig.de/)
