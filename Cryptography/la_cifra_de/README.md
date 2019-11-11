# la cifra de

> Cryptography | 200 Points
-----------------------------

## Problem Statement
 >I found this cipher in an old book. Can you figure out what it says?  
 Connect with nc 2019shell1.picoctf.com 60147.
###### HINT
 > * There are tools that make this easy.
 > * Perhaps looking at history will help

## Analysis

* This text looks like Vigenere ciphered 
  > Encrypted message:
Ne iy nytkwpsznyg nth it mtsztcy vjzprj zfzjy rkhpibj nrkitt ltc tnnygy ysee itd tte cxjltk
Ifrosr tnj noawde uk siyyzre, yse Bnretèwp Cousex mls hjpn xjtnbjytki xatd eisjd
Iz bls lfwskqj azycihzeej yz Brftsk ip Volpnèxj ls oy hay tcimnyarqj dkxnrogpd os 1553 my Mnzvgs Mazytszf Merqlsu ny hox moup Wa inqrg ipl. Ynr. Gotgat Gltzndtg Gplrfdo 
Ltc tnj tmvqpmkseaznzn uk ehox nivmpr g ylbrj ts ltcmki my yqtdosr tnj wocjc hgqq ol fy oxitngwj arusahje fuw ln guaaxjytrd catizm tzxbkw zf vqlckx hizm ceyupcz yz tnj fpvjc hgqqpohzCZK{m311a50_0x_a1rn3x3_h1ah3x1119h336}
Ehk ktryy herq-ooizxetypd jjdcxnatoty ol f aordllvmlbkytc inahkw socjgex, bls sfoe gwzuti 1467 my Rjzn Hfetoxea Gqmexyt.
Tnj Gimjyèrk Htpnjc iy ysexjqoxj dosjeisjd cgqwej yse Gqmexyt Doxn ox Fwbkwei Inahkw.
Tn 1508, Ptsatsps Zwttnjxiax tnbjytki ehk xz-cgqwej ylbaql rkhea (g rltxni ol xsilypd gqahggpty) ysaz bzuri wazjc bk f nroytcgq nosuznkse ol yse Bnretèwp Cousex.
Gplrfdo’y xpcuso butvlky lpvjlrki tn 1555 gx l cuseitzltoty ol yse lncsz. Yse rthex mllbjd ol yse gqahggpty fce tth snnqtki cemzwaxqj, bay ehk fwpnfmezx lnj yse osoed qptzjcs gwp mocpd hd xegsd ol f xnkrznoh vee usrgxp, wnnnh ify bk itfljcety hizm paim noxwpsvtydkse.


## Solution

* Using online decoder gives us the following key:  
`fyatflagflagmlagflagfpagfldgfaagfuagflagflatfleaflpg`  
and the following message 
  > ig if interestbng how in hestorv pezple fften receiie cnkdie foe tuings they wid not crewteduoinr the tourse of hiftone, thp viteaère cipher aas been reenvenqed xany kimesit was salokly ltteiouted to bltise de viganère ap it has oiiginally drscnobeo in 1553 oy tiovan batmista bellwso in eis mook ca cifra del. fig. coovln bntgista belltso for the emplejeneatifn of this cichen g tamle vs sormed by seiding the hower ealq of ae ordinary ayphwhet qor nn npparentlr random nuiber oc pllces nith respecg to pne uapee hnlfpicocty{b311a50_0r_v1gn3r3_c1lh3r1119c336}tee ftrst nell-documeatez jesnrictvon of a polralphabetec cipeer sowemer, was made nroqtd 1467 bj lebn oattista aeberti.the rigenèoe ctphei is therefoee sksettmef cnlled the aeberti disy or alyerei cigher.in 1508, johaaneo zriehezihs inventew the so-calhed tayull recka (a matrix os shelteo alchnbets) that pould laten be a coittcal tomponent os tha bigpnèrr cvpher.belltso’s seconz bookiet lpperred in 1555 as a cbntetuaeioa os the first. mhe lower hwlves lf tse alghabets are aow onifeed eetularly, bum the alphaxets akd tse inuex letters nre ioxeo by zenns of a mnefonic key pdrase, thinh cae be differeat wezh elch poerespondegt.




* Form this key we can easily conclude that the key must be`flag` to confirm
lets put key length as 4 and decode again  
this time key comes up to be `flag` and this time decoded message is a 
perfectly readable paragraph

  >it is interesting how in history people often receive credit for things they did not createduring the course of history, the vigenère cipher has been reinvented many timesit was falsely attributed to blaise de vigenère as it was originally described in 1553 by giovan battista bellaso in his book la cifra del. sig. giovan battista bellaso for the implementation of this cipher a table is formed by sliding the lower half of an ordinary alphabet for an apparently random number of places with respect to the upper halfpicoctf{b311a50_0r_v1gn3r3_c1ph3r1119c336}the first well-documented description of a polyalphabetic cipher however, was made around 1467 by leon battista alberti.the vigenère cipher is therefore sometimes called the alberti disc or alberti cipher.in 1508, johannes trithemius invented the so-called tabula recta (a matrix of shifted alphabets) that would later be a critical component of the vigenère cipher.bellaso’s second booklet appeared in 1555 as a continuation of the first. the lower halves of the alphabets are now shifted regularly, but the alphabets and the index letters are mixed by means of a mnemonic key phrase, which can be different with each correspondent.


## Flag
`picocty{b311a50_0r_v1gn3r3_c1lh3r1119c336}`

## Resources
* Tool to solve simple substitution ciphers [SubstutionDecoder](https://github.com/ViperX7/SubstitutionDecoders/)
* Online tool for solving Vigenere Cipher [Vigenère Cipher Codebreaker](https://www.mygeocachingprofile.com/codebreaker.vigenerecipher.aspx)
* See: [Vigenere Cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)

