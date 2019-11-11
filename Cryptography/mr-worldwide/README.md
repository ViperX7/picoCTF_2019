# Mr-Worldwide

> Cryptography | 200 Points
-----------------------------

## Problem Statement
> A musician left us a [message](./message.txt). What's it mean?


## Analysis 

* It seems that the given messages contains a bunch of cordinates
```
picoCTF{(35.028309, 135.753082)(46.469391, 30.740883)(39.758949, -84.191605)(41.015137, 28.979530)(24.466667, 54.366669)(3.140853, 101.693207)_(9.005401, 38.763611)(-3.989038, -79.203560)(52.377956, 4.897070)(41.085651, -73.858467)(57.790001, -152.407227)(31.205753, 29.924526)}
```

## Solution

* On searching through google and making list of places we have something like this
```
picoCTF{
(35.028309, 135.753082)    Kyoto,japan
(46.469391, 30.740883)     Odessa,Ukraine
(39.758949, -84.191605)    Dayton,usa
(41.015137, 28.979530)     Istambul,Turkey
(24.466667, 54.366669)     Al Manhal,Abudhabi 
(3.140853, 101.693207)     Kuala Lumpur,Malaysia
_
(9.005401, 38.763611)      Addis Abeba,Ethiopia
(-3.989038, -79.203560)    Loja Ecuador
(52.377956, 4.897070)      Amsterdam, Nederland
(41.085651, -73.858467)    New York, usa
(57.790001, -152.407227)   Sparows,Kodiak, Alaska,usa
(31.205753, 29.924526)     Alexandria,Egypt
}
```

* Let's take the first letter of each city and try to make a flag out of it
  > KODIAK_ALANSA

* Well it doesn't work so we might have missed any place

* But still we should be fairly close so we will search 


* we get a place named 
  > KODIAK ALASKA

* In fact if you notice the coordinates of this place is also part of the 
  problem

* Let's Submit
  > picoCTF{KODIAK_ALASKA}

* It worked

## Flag
`picoCTF{KODIAK_ALASKA}`
