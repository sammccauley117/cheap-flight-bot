# Current Build Status
This document contains a list of what actively needs to be done as well as an unordered list of how I feel about the current state of the project
## To Do
| Task | Status | Completion Date|
|:----:|:------:|:--------------:|
|Get initial data collection parsed to a useful .csv format| Active |N/A|
|Actually automate the thing so that it doesn't need to be called from the command line. Will need to see if we can get Selenium running on an AWS EC2 Linux instance | Active | N/A |
|Create data analyzer function | Active |N/A|
|Figure our a better file structure | N/A|N/A|
## Misc. Thoughts
Note: this section is very messy but used to provide transparency on the project
1. The .csv storage seems unreliable, would like to convert to SQL later on
2. Unsure if the bot and the data logging should be separated. Should the bot call the log function and wait or should the bot just expect the data to be done? In reality the logging function should probably call the bot once its finished, however, something about that just seems wrong to me. Maybe because it makes the bot feel less bot-like...
3. There is no "right" answer for making an algorithm that determines a "good" deal. I think the algorithm should be the last step to the bot before version 1.0.0
4. Selenium seems like the best choice right now, however, I think we should switch to a price alert email parser later on. Seems more reliable

Overall, lot of this seems "hack-ish" right now. However, it is still in version 0.0.0 so there is a lot of cleaning up to do
