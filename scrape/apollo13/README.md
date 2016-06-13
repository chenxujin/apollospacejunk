# Apollo 13 Lunar Flight Journal Scrape Script

Here is what you do:

Start by scraping the page, and see if everything goes smoothly. 

Things will probably not go smoothly, and the likely culprit will be 
feeding funny unicode symbols to the tokenizer. To prevent this from
being a problem, you will need to create a list of problematic unicode
characters that show up in the document, and do a find/replace with some 
other symbol, like a period or a space.

Once you have done that, and added all the unicode characters appearing
in the lunar flight journal, the script will be able to handle everything 
smoothly, and hand it off to the tokenizer without trouble.

From there, the text is tokenized, and a data file is created. This is then
used to power a bot.
