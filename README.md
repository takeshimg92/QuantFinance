# Plan towards mastering quant finance
 
 
## My goal is to build concise library(ies) to invest. Python + LaTeX 
(and hopefully little-to-none C++ or Julia)
 
The final objective is to build mostly-Python libraries containing implementations to invest in the real world. The accompanying documentation should be a nice, mostly-LaTeX set of notes.
 
The main is to create some reference materials so I don’t have to Google so much or depend on Investopedia. But this is also a means to facilitate my own life investing and build some robots to trade and avoid losing too much money.
 
## To learn or review: theory and implementation
 
I am strong believer in really understanding the basics before jumping to complex things, especially when money is into play. This means understanding the following “WHAT” ITEMS:

1. Micro and macroeconomics, especially the economic cycle and how some quantities such as inflation, unemployment, interest rates and foreign exchange rates change over time;

2. The theory behind financial markets (Markowitz, CAPM) and how concepts such as liquidity and arbitrage appear;

3. Fixed income products: how lending money to people makes the world spin;

4. Stocks and indices;

5. Derivatives: futures, options, swaps etc : how they are priced, hedged, and why volatility is the greatest rug in finance (as in to sweep things under) 

6. Crypto: is it worth the hype? (this is not rhetoric – I really don’t know);

7. The “Brazilian special case” and how things change over here;

8. How these things have changed after 2008 (eg. multi-curve paradigms, CDOs and credit default swaps);

9. The trader zoo: fundamental vs technical analysis; options trading; FX trading; etc.
 

One thing that I came to appreciate about finance over time is that I don’t really understand something unless I can take a VERY physicist approach to it (and this is of course just me; I don’t know how other people learn). This means:

* Setting up a framework / system where there is some underlying microscopic dynamics which is simple (under some definition of simple)
* Writing down a few equations for modeling behaviors;
* Making a lot of assumptions and simplifications – and knowing when they don’t apply
* Implementing this on a computer and watching the world burn;
* Getting a QUALITATIVE intuition for the phenomena.
 
There are three SYMBIOTIC parts for this to happen:
1. A well-designed mathematical framework to write the dynamics. This is good old (1) probability theory. Expanding on it, we are really talking about (2) stochastic calculus.

2. A good computational framework to simulate all this. It all boils down to a lot of (3) Monte-Carlo simulations and (4) machine learning, which also requires a lot of (5) good quality data. Finally, whatever models we build need to be able to (6) trade online via brokers on our behalf (or, at least, give us some cute dashboards to track our portfolio), via some robust and secure (7) deployment.

3. A strong (8) community of guys who [organize meetups](https://www.linkedin.com/in/gautier-marti-344b565a/), have [blogs or YouTube channels](https://takeshimg92.github.io/posts/carr_madan.html) (:)), [write books](https://www.linkedin.com/in/dyjh/?locale=en_US) or just [write great papers](https://scholar.google.com/citations?user=abnvNIsAAAAJ&hl=en) so we can keep on learning
 
We have listed 8 “WHAT” items and 8 METHODS, for a total of 16 topics.
 
## The plan is to clear all these items while minimizing verbosity
 
One equation and one abstract class are worth 1 thousand words and probably a few more thousand dollars.
 
The plan:

* Break out this study plan over time on a timeline
* Have different parties study different things to present to the group
 
## OK but how are we actually going to make money?
 
I don’t have a clue. Yet.
 
## Tools (WIP)
* https://deepnote.com/ - to write “Jupyter notebooks” in a Google Docs-like real-time collaboration
* What else? TBD. Maybe a virtual machine? 

## References

* Udemy course on Quant Finance and Algo Trading
* Summary on the Multi-curve framework
* Marcos Lopez’s book on financial machine learning
* Shreve’s book on stochastic calculus
* Paul Glasserman’s book on Monte Carlo for financial engineering
* Python for Algorithmic Trading
* MetaTrader stuff
