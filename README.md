# Blockchain-API
Home assessment - 08/11/22.

**The assessment:**
Given timestamp TS, find the latest block prior to TS
(using API calls on https://blockchain.info/block-height/***?format=json)

**Workflow:**
First, I tried to implement the assessment using regular binary search.
After implementing code I felt code is too slow, and I decide to implement a former search in a way that is similar to radix sort.
I add a prior calculation that first, calculates how many digits are in latest block.
Then, for each digit (start from left to right) if finds the right range to search for the next digit.

**Example how code works:**
let’s say we enter the TS of block height 610592.
First it will find that the right range to continue searching is 600000 to 700000, then 610000 to 620000, then 610000 to 611000, then 610500 to 610600, then 610590 to 610600 and then it founds the right block height - 610592.


**What I could have done better:**
Code is still slow.
To make it even more efficient, it is possible to add calculations using the average time between blocks in seconds (can be found here - https://blockchain.info/q/interval).
It is possible to use this data to calculate a small rang in which our TS is in, and then use other searching methods as the methods I implemented.
Another improvement can be made is exporting the JSON in a more stable way than calling data in the first place ([0]).
