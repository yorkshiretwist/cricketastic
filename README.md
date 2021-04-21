# Welcome to Cricketastic!

This is a simple text-based cricket game written in python. It's not particularly clever, I wrote it to practice using python classes. Expect quirks and bugs!

## How to run it

Clone the repo, and run `python app/Cricketastic.py` from the main folder.

## How to play it

First, enter the names of both teams:

```
Enter the name for team 1: Yorkshire
Enter the name for team 2: Lancashire
```

Then choose whether this is a mens, womens or mixed game (this sets the gender of names generated randomly for the players):

```
Is this a mens (M), womens (W) or mixed (X) game?: x
```

And set the number of overs in an innings:

```
And how many overs in an innings? (5, 10, 20, 30, 50): 20
```

The squads will be displayed. Press enter to toss up:

```
Yorkshire vs Lancashire

Squads:

Yorkshire:
1: Natasha CHAPMAN
2: Jasmine WILSON
3: Victoria REID
4: Ashleigh MURRAY (WK)
5: Emily WILKINSON
6: Lewis MORGAN
7: Demi RICHARDS
8: Paige OWEN
9: Chloe MARSHALL
10: Paige HARRISON (C)
11: Alexandra GREEN

Lancashire:
1: Hannah FOSTER (WK)
2: Kimberley HUGHES
3: Molly ADAMS
4: Jessica WEBB
5: Tyler GRIFFITHS
6: Euan CARTER
7: Ashleigh KNIGHT
8: Gary JAMES
9: Laura PRICE
10: Ben MORRIS (C)
11: Aaron HUGHES

Ready to play? Press enter to toss up
```

And press enter to start the match:

```
Lancashire have elected to bat first.

Press enter to start the match
```

While the match is being played you'll see a simple scorecard:

```
Yorkshire vs Lancashire

------------------------------------------------------------

Innings of Lancashire

0 / 0 (0.0 overs)

Hannah FOSTER * (0 off 0)
Kimberley HUGHES (0 off 0)

Over 1
Bowler: Jasmine WILSON
```

Press enter to bowl a ball. As the over progresses the scoreboard will be updated:

```
Yorkshire vs Lancashire

------------------------------------------------------------

Innings of Lancashire

4 / 0 (1.0 overs)

Hannah FOSTER * (2 off 4)
Kimberley HUGHES (2 off 2)

Over 2
Bowler: Jasmine WILSON
. 1 1 . 1 1
```

Press enter to start the next over, the batters will swap ends and you'll get a new bowler.

## It looks randomised, right?

Right. Each ball could be a dot, 1, 2, 4, 6 or wicket. Dots and 1s are more likely than sixes and wickets, though.

If the ball results in a wicket, the dismissal type will be one of:

- Bowled
- Caught
- Run Out
- Stumped
- Hit Wicket
- Caught and Bowled

You also get a little animation for fours, sixes and wickets. What fun.

## Future plans

I'd like to make the app prettier, using something like [Rich](https://github.com/willmcgugan/rich). I also want to be able to show the whole scorecard, and maybe some simple stats diagrams (Manhattan is probably the easiest to implement).