# Text Rhyme

## Description
This repo is the assignment of the Reading and Writing Electronic Text course at ITP.  

The assignment was to adapt an existing cut-up assignment to take make use of rhyme, meter, or sound symbolism. (or develop something new from scratch)

I created a program that takes a short text as input and outputs a new text that rhymes with the input text.

The program uses `pronouncing` library to find rhyming words and `SpaCy` to get the rhyming words with the same Part-of-speech, Tag, or Entitiy label as the original input words.

Finding the rhyming words can be done simply by the following:

```
rhyming_words_list = pronouncing.rhymes(input_word)
```

## Example input
```
Two roads diverged in a yellow wood,
And sorry I could not travel both
And be one traveler, long I stood
And looked down one as far as I could
To where it bent in the undergrowth;

Then took the other, as just as fair,
And having perhaps the better claim,
Because it was grassy and wanted wear;
Though as for that the passing there
Had worn them really about the same,

And both that morning equally lay
In leaves no step had trodden black.
Oh, I kept the first for another day!
Yet knowing how way leads on to way,
I doubted if I should ever come back.

I shall be telling this with a sigh
Somewhere ages and ages hence:
Two roads diverged in a wood, and I—
I took the one less travelled by,
And that has made all the difference.
```

## Example output
```
Two odes emerged in a mellow wood,   
And sorry I would not travel both 
And be one traveler, long I understood 
And overcooked down one as afar as I should  
Thru where it went in the undergrowth;  

Again mistook the other, as hust as fair,  
And halving perhaps the wetter claim, 
Because it was grassy and flaunted wear; 
Although as before that the passing leclaire 
Had reborn em dilly without the same, 

And both that morning equally overplay 
In greaves no schweppe had trodden black. 
Oh, I wept the first before another day! 
Yet snowing how overstay reads on abou way, 
I spouted if I could whatsoever bum back. 

I shall be gehling this with a thigh 
Everywhere wages and wages hence: 
Two modes purged in a wood, and I— 
I mistook the one less travelled by, 
And that has flayed all the difference.
```

## How to use
1. Installation of python3 is required. Follow [this guide](https://realpython.com/installing-python/) to install it.
2. Run the following commands in the Terminal. (Replace "Hello World" with your own input text)
```
git clone https://github.com/cuinjune/text-rhyme.git
cd text-rhyme
pip install -r requirements.txt
python main.py "Hello World"
```

## Author
* [Zack Lee](https://www.cuinjune.com/about): MPS Candidate at [NYU ITP](https://itp.nyu.edu).
