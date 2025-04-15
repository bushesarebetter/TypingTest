# TypingTest
Typing Test hacker to get 14k+ wpm on certain sites


## How to run:
First, run ```pip3 install -r requirements.txt```. Then, after all dependencies have been downloaded, use ```coorddebug.py``` to find the coordinates of what you want to capture. Just click c on the top left corner, and then move your mouse to the bottom right corner and click c again. This will make x-y bounds and take a test screenshot in the directory as the rest of the project. Check the image to make sure it is capturing what you want, then continue (This step will not need to be done again as long as you don't scroll or change where the typing box is)

Now, run ```python3 main.py``` and quickly alt+tab over to the typing test you are taking. Wait a quick second, and watch in amazement as the bot instantly fills out the test. 

## Notes#
This works best on this site: https://humanbenchmark.com/tests/typing

It also works fairly well on: https://monkeytype.com

For humanbenchmark, I can easily get 14k WPM as you don't have to wait for the site to scroll, and for monkeytype I got about 1.2k WPM

EDIT (before it's released is crazy): I added auto scrolling, so now if the test has text that scrolls as you type, it can adapt to that. 
EDIT 2: This also works fairly good on monkeytype, just make sure you're using the DARK theme as that makes the words you already typed darker and it allows for the bot to ignore previous lines, which is really handy. I got about 1206 WPM and 97% accuracy. Tesseract has a weird thing with not being able to process some text very well, I"m not sure how to fix it currently but I might come back later if I figure out how

I am planning to add functionality to other sites as well, however I doubt it would be too possible with standard Tesseract OCR for python unless I find a way to unhighlight the currently-typed words (a common feature for most typing websites), since Tesseract is unable to identify these unusually formatted sections.

## Script performance:
![image](https://github.com/user-attachments/assets/379c3b65-ead4-4f06-aae1-8f99bc5d06ac)

