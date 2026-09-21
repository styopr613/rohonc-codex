# The Rohonc Codex

### a reader's edition

Every line of all 441 folios, in the order the manuscript has them.

The script is undeciphered. The dictionary that makes this possible is
**Levente Kiraly and Gabor Tokai's**, published at rechnitzer-kodex.hu, and
roughly three quarters of the words below are theirs or follow directly from
theirs. Their grammar paper is unpublished, so nothing here chooses between
the senses of a word that has several; the first sense is printed. This is not
their translation, which has never been published.

## How to read the marks

| mark | meaning |
|---|---|
| `word` | read |
| `word*` | read from one passage, with nothing in the book able to refuse it |
| `[word]` | **restored** -- a guess from the folio's source and its neighbours |
| `[...]` | dark: no reading, and no honest guess |

A hyphen inside a word (`hide_oneself-angel`) is one sign of the manuscript
read as the smaller signs it is built from -- this script writes phrases
without spaces, which is the central fact Kiraly and Tokai established about
it. A `~` marks a spelling their own apparatus files as a variant. A `|` is a
gap or an unreadable glyph in the transcription.

**Why the dark places are not filled in.** It would be easy to print a
plausible word in every bracket. The project measured what such a word is
worth: against Kiraly and Tokai's own hidden dictionary entries, the best
candidate drawn from a folio's cited passage was right **0.0%** of the time.
So the ellipsis stays. An edition that guesses everywhere is not more complete
than one that does not; it is only harder to check.

## What this edition is worth, in numbers

    words in the manuscript            29997
    read                               27962 (93.2%)
    read from one passage, marked *    1012 (3.4%)
    restored, in brackets              64 (0.2%)
    dark, printed as an ellipsis       959 (3.2%)

    lines with every word read         3566 of 4372 (81.6%)
    lines complete including
      restorations                     3620 of 4372 (82.8%)

The evidence for every single word is in `harness/proposals.json`, one entry
per sign, with its tier and the argument in full. `harness/ktprov.py` prints
where each reading came from and whether the manuscript itself can ever refuse
it. `harness/ktnull.py` and `harness/ktrederive.py` are the controls,
including the two that failed.

**Brackets are the measure of what is left to do.** Every time a source text
enters the corpus, or a formula turns up twice, some of them become plain
words. There are 64 of them now.

---


## 004v — the beginning: heaven, the angels, Lucifer

> In the beginning there was the Lord God. […] […] and the earth. The sun and the moon, [as] the scripture(?) [says]. Elijah the prophet. The angel of God said: […] before […] of man. The Father […]; man bowed down(?) before the Lord. God in heaven […] and the brethren. Many angels […]; and God the Father had many angels about him. Among the angels, two hundred and fifty(?) years […] before […] of man. The Father, Adam, and the angels […]; there was Lucifer, and the other angels. And the angels prayed, and for forty [days?] and forty nights […] Lucifer […] to Lucifer […] among the brethren, in hell. And again the angel said to Elijah: Elijah, when there is […] Lucifer, who did [this] — Lucifer, when he was […] seated on the throne of God the Father. God the Father went […]

  1  time then-exist Lord God
  2  heart one-on-sky and ~earth
  3  sun and moon write
  4  Elijah prophet say angel God
  5  [...] before heart <preposition_of_genitive>-somebody
  6  from-father ~Adam bow_down Lord
  7  God on-on-sky eternal* in_turn-brother
  8  many ~angel on-~angel and exist to-from-father God on-many angel
  9  on-angel two-half-hundred-year seven before heart <preposition_of_genitive>-somebody
 10  from-father ~Adam and angel brother-+name exist hide_oneself-angel and two ~angel
 11  and angel hide_oneself-angel pray and ten-ten-ten-ten day ten-ten-ten-ten night
 12  which hide_oneself-angel to hide_oneself-angel on-+one-?eternal on-in_turn-brother on-hell
 13  and two say angel to-Elijah Elijah and then-exist as*
 14  hide_oneself-angel who do, hide_oneself-angel then-exist
 15  day sit on throne from-father God go from-father God

## 004r — the cup

> The angel of the Father said; God the Father; the angel said to Lucifer: because the cup was hidden away. […] of the Father, on the throne […] God; the angel; Lucifer; the cup was hidden away. […] the Lord on the throne; and when the cup […] […] the cup was hidden away […] And when Lucifer […], the angel returned to the Father. […] the angel, the Lord, the cup, Lucifer […] the cup was hidden away […] and the other went. God the Father; the angel of the Father [spoke] to Lucifer; Lucifer said: because the cup was hidden away. […] with the Father, on the throne; and when Lucifer went to God the angel said: God; the angel; the cup was hidden away […] the Lord on the throne; and when the cup of Lucifer […] the cup was hidden away […] and then […] | was hidden. The angel returned, the angel, to God the Father, because there was said Lucifer; to the Lord; hidden; the Lord God; the mother […] […] to the Lord, to the Lord, this | hidden. The angel […] Lucifer, he on the throne […] God, the angel, the Lord. The cup of Lucifer […] the cup was hidden away […] said Lucifer to the Lord: hidden.

  1  angel <preposition_of_genitive>-father say from-father God angel say hide_oneself-angel because cup-to hide_oneself
  2  above* <preposition_of_genitive>-father on throne and_then God angel hide_oneself-angel cup-to hide_oneself
  3  above* Lord on throne and then-exist cup hide_oneself-~angel [steal] cup-to hide_oneself above*
  4  and then-exist from hide_oneself-angel return angel to-father
  5  and_then angel Lord cup hide_oneself-angel [steal] cup-to hide_oneself above* and two go
  6  father-<suffix_of_divine_name> <preposition_of_genitive>-father angel to-hide_oneself-angel say hide_oneself-angel because cup-to hide_oneself
  7  above* on-<preposition_of_genitive>-father on throne and then-exist to-hide_oneself-angel go God
  8  angel say God angel cup-to hide_oneself above* Lord on throne and then-exist
  9  cup hide_oneself-angel [steal] cup-to hide_oneself above* and then-exist from | hide_oneself
 10  angel return angel to-father God because-exist
 11  say hide_oneself-angel to-Lord hide_oneself Lord-<suffix_of_divine_name> mother coming* be_born* to-Lord to-Lord this | hide_oneself
 12  angel [...] hide_oneself-angel this on throne and_then God angel Lord
 13  cup hide_oneself-angel [steal] cup-to hide_oneself above* say hide_oneself-angel to-Lord hide_oneself

## 002r — Michael, the command to bow, and Lucifer's fall

> The mother of the Lord God was born; and Lucifer […] to the Lord, to the Lord; Lucifer […] Lucifer, he upon the throne […] of the Lord God […] There was the earth […] God the Father […] Michael. The angels, faithful servants, rose up; and when they had risen, the heavenly ones spoke. God the Father […] went to Lucifer, and Lucifer fell from the throne of the Lord; and when, within […] they bowed down — and of the angels every one — to whom Lucifer [would not] bow. And then […] God the Father […], and cried out. God the Father […]: Lucifer departed by commandment, because all were angels to whom Lucifer bowed. And […] […] said God the Father, from he departed. This was the angel. He left food(?) […], and […] said the angel to Elijah the prophet: Elijah, say(?) […] God the Father is. To the Son came the Holy Spirit. Father, Son […] man […] God the Father, the Holy Spirit — how man knows the image of the Father.

  1  Lord-<suffix_of_divine_name> mother be_born and hide_oneself-angel to-Lord to-Lord hide_oneself-angel [...]
  2  hide_oneself-angel this on throne [...] Lord-<suffix_of_divine_name> <preposition_of_genitive>-Lord [...]
  3  exist earth and_then from-father God eternal* Michael
  4  angel believe servant stand_up up and then-exist stand_up
  5  heavenly say from-father-<suffix_of_divine_name> eternal* go to-hide_oneself-angel and
  6  hide_oneself-angel bow_down on throne <preposition_of_genitive>-Lord and then-exist inside [?]-+one-understand
  7  bow_down and from angel each,_every to-which hide_oneself-angel bow_down
  8  and then-exist see* from-father God eternal* and shout
  9  from-father God eternal* leave hide_oneself-angel commandment because each,_every exist angel
 10  to-which hide_oneself-angel bow_down and [...] to-~go say from-father-<suffix_of_divine_name> from
 11  leave this exist angel leave food ~judge-year and three say angel
 12  to-Elijah prophet Elijah say <subject_marker> from-father-<suffix_of_divine_name> exist
 13  to-son go holy-spirit father son heart somebody and_then
 14  from-father-<suffix_of_divine_name> holy-spirit on-how? somebody shape,_form know father

## 002v — the Trinity, and the making of Adam

> The Son, the Spirit […] […]; the Son, in the image of the Lord. […] […] man is; all one; to the Father, the Son, the Spirit. Father, Son and Spirit took man, and every living thing […] The soul heard. Adam saw the living, truly, not many | Father and Son — not many; the Holy Spirit; but this Lord is all, one God. […] God, the angel, Elijah the prophet. Elijah the prophet, when there were Father, Son and Spirit, going forth […] […] and the brethren, in this world, and […] | […] the Lord God, Adam […] […]; and then Adam was […] as was said before […] and […] […] […] breathed into Adam, and he became living, and the Lord God took Adam, and Adam went into Paradise; and all […]. End of chapter. Adam

  1  son spirit heart and_then son on-<preposition_of_genitive> shape,_form on-Lord
  2  heart [likeness] exist somebody each,_every one to-father son
  3  spirit grab father son spirit somebody each,_every living [creature]
  4  soul hear Adam see living righteous(ly) not many | from
  5  father from son not many holy-spirit a) this Lord each,_every
  6  one God and_then God angel Elijah prophet
  7  prophet Elijah then-exist father son spirit to-go
  8  table from_the_eternal* in_turn-brother on-this world and out | to
  9  Paradise Lord-<suffix_of_divine_name> Adam heart slime_(of_the_earth)* and then-exist
 10  Adam ~exist heart earlier_mentioned slime_(of_the_earth)* and became* to-soul-+one
 11  heart breathe on-Adam and living leave and
 12  Adam grab Lord-<suffix_of_divine_name> and Adam go inside
 13  Garden_of_Eden and each,_every heart exist-chapter Adam

## 003r — the commandment, and the sleep

> […] the Lord God [and] Adam. The Lord [spoke] to Adam; he took every truly […] hunger, and thirst […] upon Adam; and one living [thing] dies. There shall be sin, hunger, thirst, to him who […] the Lord took. To Adam, all truly one. […] this yoke upon Adam, by commandment: not […] this […] […] […] […] Adam is […] […] Adam would die. And then Adam slept within | […] and then upon him […] first, from […] and | when the Holy Spirit came within […] […] this […] this […] and the Lord God took Adam […] and […] […] said the angel to you: mother. And then Adam, from […] […] this |

  1  and_then Lord-<suffix_of_divine_name> Adam this-Lord this-Adam grab
  2  each,_every righteous(ly) [nor] be_hungry and thirsty [nor] this-Adam and
  3  one living die sin have be_hungry thirsty to-to-this-who
  4  [...] grab-Lord this-Adam each,_every righteous(ly) one
  5  law this yoke this-Adam through commandment not eat.
  6  this to-+son evil-+sin thou_shalt_die* brethren-+<subject_marker> Adam exist eat.
  7  on-[?] die-Adam and then-exist Adam sleep inside | to
  8  Paradise and then-exist on-this name ~first from saying and | then
  9  exist go holy-spirit inside into_Paradise and_then this
 10  <subject_marker> this the_garden and grab Lord-<suffix_of_divine_name> Adam
 11  rib and it heart say angel you
 12  mother and then-exist Adam from laugh* and_then this | to

## 003v — the rib, Eve, and the serpent

> Bone of bone; and the two souls are one. | Before […] and […] said the angel. The Lord God departed […] | Chapter. […] and Eve went into Paradise; and | when Eve came to that tree which […] the Lord God had by commandment [forbidden]; and she saw a serpent in that tree, which […] was the Lord God's by commandment […] this serpent […] […] this fruit […] Eve […] ate, because […] Adam, the Master, by commandment […] this serpent. Eve ate […] Adam […] this fruit; and the fruit […] was […] […] Adam ate; and […] Adam knew

  1  bone bone in_turn two soul one | before
  2  day-+name and five say angel leave Lord-<suffix_of_divine_name> from_the_eternal* | in_turn-chapter
  3  day-~exist and go Eve on-Garden_of_Eden and | then
  4  exist Eve go to-this tree what stood_in_the_midst*
  5  exist Lord-<suffix_of_divine_name> through commandment and see one
  6  serpent on-this tree what stood_in_the_midst* exist
  7  Lord-<suffix_of_divine_name> through commandment and_then this serpent it
  8  from-+who-chapter this fruit and_then Eve shall_not_eat eat
  9  because it Adam Master through commandment and_then
 10  this serpent Eve eat it Adam
 11  one this fruit in_turn fruit <subject_marker> exist it
 12  one Adam eat exist it Adam know

## 001r — good and evil, shame, and back to Elijah

> evil and good, as the Lord God knows. And then they plucked, the serpent, this fruit, this serpent; and | Chapter. […] took […] and […] took the fruit. Adam. And then […] the two of them, Adam, [were] naked. […] saw Adam; and then […] Adam was ashamed. And [chapter] six: the angel of God said to Elijah […] Elijah; and this […] […] Lucifer, the Father […] […] Lucifer had fallen | Father God […] and the brethren […] and […] said the angel of God to Elijah the prophet: Elijah, the Lord God departed […] […] within Paradise, saying

  1  evil and good how?-to Lord-God know and then-exist pluck
  2  serpent this fruit this serpent and | then-chapter
  3  day grab it in_turn it fruit grab
  4  Adam and then-exist were_opened* on-two Adam naked
  5  see it Adam and then-exist it Adam
  6  be_ashamed_of_sg and six say God angel to-Elijah prophet.
  7  Elijah and this deadly_sin* afterward* hide_oneself-angel
  8  from-father eternal* son-+<subject_marker> hide_oneself-angel exist bow_down | father
  9  <suffix_of_divine_name> from_the_eternal* in_turn-brother hell* and seven say
 10  God angel to-Elijah prophet Elijah leave Lord-<suffix_of_divine_name>
 11  from_the_eternal* in_turn-[?] inside Garden_of_Eden say

## 001v — where art thou

> The Lord God, with the angels, came out(?) […] and then departed. The Lord God […] within […] […] the Lord God. […] Where [art thou]? […] Adam […] the Lord God. […] The Lord God [spoke] with his own mouth. Adam hid himself […] Adam, who […] […]. Said the Lord God: Where art thou, Adam? […] […] Eve [gave?] […] ate […] The Lord God […] heavenly […] […] Eve, to the Lord, […] the Lord God: Why, Eve? […] Eve […] […] the Lord God: Why, Eve? […] […] […] The serpent […] ate […] the Lord God, Adam one commandment: this Adam […] did not keep(?) the commandment.

  1  Lord-<suffix_of_divine_name> on-angel this ~out(ward) two from saying and then-exist leave
  2  Lord-<suffix_of_divine_name> from_the_eternal* inside into_Paradise and_then Lord-<suffix_of_divine_name> <suffix_of_divine_name>
  3  Adam why? and_then ~Adam hide_oneself-~Adam Lord-<suffix_of_divine_name>
  4  and_then Lord-<suffix_of_divine_name> who-mouth ~Adam hide_oneself and_then ~Adam
  5  who this-~Adam hast_thou_done* say Lord-<suffix_of_divine_name> why? ~Adam
  6  hast_thou_done* and_then Eve Adam food and_then.
  7  Lord-<suffix_of_divine_name> it heavenly and_then answered* Eve this-Lord-to
  8  and_then Lord-<suffix_of_divine_name> why? Eve answered* who Eve hast_thou_done*
  9  and_then Lord-<suffix_of_divine_name> why? Eve hast_thou_done* and_then it
 10  serpent it food and_then Lord-<suffix_of_divine_name> ~Adam
 11  to-one commandment this ~Adam name-[?]-ten commandment ~carry

## 007r — the curse, and the sword at the gate

> Adam was, to him who […] and why […] […] Adam was of the earth […] he would […] eat, and take, and […] […] it was through […]; and […] was painful. […] shall be; and this evil — this evil is […] the earth […] and […] evil. Man was made, all of this. The serpent dies; and he departed from among […] the Lord God; and there went the Lord God, the angel […] fire, a sword; and […] out | within Paradise. He drove them out, and set an angel […]

  1  exist ~Adam to-to-this-who [?]-~Adam in_turn why?-in_turn
  2  gates* exist ~Adam earth till_the_earth
  3  want to-~son food ~grab in_turn it this-+it
  4  exist through pine and this-+it exist painful
  5  coming* have in_turn this evil this-evil exist
  6  [...] earth slide ~and room
  7  evil this somebody create each,_every this serpent die and
  8  leave among Adam_and_Eve Lord-<suffix_of_divine_name> and go
  9  Lord-<suffix_of_divine_name> angel two-~earth-+Eve fire
 10  sword and ~earth-slide out(ward) | on-inside
 11  Garden_of_Eden exorcise and put angel sword

## 007v — outside the garden: Cain, Abel, Seth, and Adam goes blind

> […] […] Paradise; and one created […] within Paradise; but the angel […] the Lord God with the angel […] from […] and from eight(?) said | Elijah. The angel of God: Elijah, when the Lord God [drove] Adam out […] from Paradise; and then | […] he dwelt in the field many years; and Adam had […] offspring, these two sons. And the firstborn was Cain, and the second […] was Abel. […] […] was Seth. And then Adam was blind in both eyes; and then Adam went into […] the son […]; and this son was […] the son […] Adam. And then Adam said: bring Adam from […]

  1  on-~gate cherub* Garden_of_Eden and one create
  2  [cherubim] inside Garden_of_Eden a) angel and_then Lord-<suffix_of_divine_name>
  3  on-angel this table three from saying and from two-two-two-two say | to
  4  Elijah God angel Elijah then-exist Lord-<suffix_of_divine_name> ~Adam
  5  out(ward) cast_out on-Garden_of_Eden and then-exist | two-+name-donkey
  6  Eve leave inside ~field many year and ~have ~Adam Eve
  7  descendant this-two to-son and firstborn exist Cain and two [?]-end-+name exist
  8  Abel third and-before-end-+name exist Seth and then-exist
  9  ~Adam from eye-eye blind and then-exist go ~Adam inside Paradise
 10  son <preposition_of_genitive>-~Adam and this son exist [...] son [...]
 11  ~Adam and then-exist say ~Adam carry ~Adam from the_tree_of_mercy.

## 006r — Seth goes to Paradise for the branch

> a branch. And then the branch […] carry […] through the light; and then by that light […], through the eye, blind Adam sees; and Adam was made whole […]. And then Seth went | […] to Paradise; and […] to Seth appeared God's angel […] the angel of God [to] Seth […]; and he went […] Seth said: Adam my father. Seth […] went into Paradise | when it was Adam his father. Seth brought from […] a branch. […] […] Adam his father was, through sin; and Adam said, Adam, when […] Seth brought […] through the light; and then by that light […], through the eye, the blind man sees; and Adam was made whole […]. The angel truly […] spoke; and then the angel went into Paradise, and Seth carried the branch

  1  one ~branch and then-exist branch to-~Adam carry anointed* through
  2  ~light and then-exist through ~light anointed* through eye see blind ~Adam
  3  and healing leave ~Adam [...] and then-exist Seth go | [...]
  4  gate/open Garden_of_Eden and then-~exist Seth appear God
  5  angel and_then God angel Seth [...] and go one say Seth
  6  from-father ~Adam Seth <subject_marker> go inside Garden_of_Eden | then
  7  exist father ~Adam carry Seth from the_tree_of_mercy branch
  8  on-+the_tree_of_mercy <subject_marker> exist father ~Adam through sin and say ~Adam
  9  ~Adam then-exist seed carry Seth anointed* through
 10  ~light and then-exist through ~light anointed* through eye see blind ~and
 11  healing leave ~Adam and_then angel righteous(ly) <subject_marker> speak and then-exist
 12  go angel inside Garden_of_Eden and Seth carry branch

## 006v — the branch brought home, and a city

> out of Paradise, from […] […] Adam was, through sin. And then […] the angel gave(?) this branch; and then the branch […] he carried […] to his father Adam. And then […] he went into a city, and […] the city was […] where Adam was, a house. And then he came […] […]; and within, all from the city […] […]; and […] out of the city one […]; and then Seth went, this […] and within […] […]; and then Seth said, one […] […] […] the Father, the Spirit, the Father […] […] Adam. And Adam was blind in both eyes — Adam, who was the Lord God's, [driven] out of Paradise by the angel; and then […] […] the gospel, and they found […] years(?); and

  1  on-Garden_of_Eden from tree on-+tree exist ~Adam through
  2  sin and then-exist among-~exist ~exist ~grab angel this branch
  3  and then-exist branch among-~exist carry to-<preposition_of_genitive>-among-~exist father
  4  ~Adam and then-exist among-~exist go inside one town
  5  and believe-end-+name town exist name-[?]-who who exist ~Adam
  6  house and then-exist arrive can [the_way] recognize and inside each,_every from
  7  town can [the_way] recognize and then-~exist out(ward) town
  8  one [...] and then-exist Seth exist go this <someone_Seth_meets>
  9  and inside can [the_way] recognize and then-exist Seth say one
 10  <someone_Seth_meets> oh <preposition_of_genitive>-[?] from-father spirit father <subject_marker> recognize
 11  ~Adam and ~Adam exist eye-eye blind who ~Adam exist Lord
 12  God out(ward) cast_out on-Garden_of_Eden on-angel and then-exist <someone_Seth_meets>
 13  from-see gospel and find <someone_Seth_meets> ten-two-two-ten-year and

## 008r — Noah and the ark

> […] And then […] at that time the Lord God appeared to Noah; and then […] the Lord God. Noah. The Lord grieved […] man […] that he had made them, because […] he who keeps his commandment. The Lord God would have all destroyed. […] The Lord God [said to] Noah: make one […] the Lord | […] the Lord. It was forty(?) cubits long, and […] broad; and […] lift up […] take […] of every creature two by two; and […] of the ark. And then this […] the Lord […] the Lord went; and then […] he took of every creature two by two, and went before the Lord God; and […] the Lord God, to the cup, and to the Lord […] and […] the Lord God; all, two by two, [in every] direction […] and the rain came for forty days; and […] the cities were destroyed. The Lord God […]. The angel of God said [to] Elijah: the Lord God was [with] Noah; […] […] all this […] was; and the other […] departed; and this

  1  seven and then-exist three time appear Lord-<suffix_of_divine_name> Noah
  2  and then-exist and_then Lord-<suffix_of_divine_name> Noah sad(ly)-Lord year brethren* somebody on-<preposition_of_genitive> go_away*
  3  create because [...] this who carry <preposition_of_genitive> commandment ~exist Lord-<suffix_of_divine_name> want each,_every
  4  destroy and_then Lord-<suffix_of_divine_name> Noah do, one exist Lord | ark*
  5  ~exist Lord exist on-two-two-ten cubit long in_turn three_hundred*
  6  broad in_turn five lift_up one-hide_oneself grab Noah* each,_every create two-<infix_of_distributive_numeral>-two and
  7  [...] <preposition_of_genitive>-ark and then-exist this [...] this-Lord this-?Noah go-Lord
  8  and then-exist Noah* grab each,_every create two-<infix_of_distributive_numeral>-two and go before Lord-<suffix_of_divine_name>
  9  and inside-+exist Lord-<suffix_of_divine_name> to-cup and to-Lord lose* and [...]
 10  Lord-<suffix_of_divine_name> each,_every two-two direction water disperse fifth from_the_eternal* high
 11  and go rain two-two-ten-year and five town destroy
 12  Lord-<suffix_of_divine_name> and_then God angel Elijah say exist Lord-<suffix_of_divine_name> Noah
 13  Noah* remain* each,_every this [...] exist and two [...] leave and this

## 008v — from Noah to Abraham

> the people were, until Abraham the forefather […] believed. From Noah it was, until Abraham […] […] The angel of God to Elijah the prophet: Elijah, within this and that believe. One man was saved in that time. The angel departed from before Elijah the prophet; and this and that he said. […] Elijah the prophet wrote; and […] […] within […] chapter […] of the writing.

  1  people exist until Abraham forefather were_pagans* believe
  2  from Noah exist until Abraham seven-[?] and_then
  3  God angel to-Elijah prophet Elijah inside this-and-this
  4  believe one somebody ~be_saved inside time
  5  leave angel before Elijah prophet and this-and-this say
  6  <subject_marker> write Elijah prophet and [...] prophet.
  7  inside one chapter Elijah* <preposition_of_genitive>-write

## 005r — Abraham and Isaac

> […] and the son went [with] the father | the father; and a sheep, and a lamb. […] the son; the father sacrificed […]; the father Abraham, for love of the Lord, […] the Lord God, the offering. Chapter. And then Isaac was […] […] who was […] Isaac […] […] Abraham sacrificed, and drew out […] […] […] […] Isaac he would slay; and the Lord God cried out from the cloud, by the angel of the Lord God, […] to Abraham […] […] who […] Abraham. The Lord God. Love the Lord. […] peace to the Lord. And then he looked up and saw, Abraham, and saw […] a lamb in a thornbush.

  1  donkey* and go-son-father | son*
  2  father and one sheep and one lamb
  3  who-~exist son father sacrifice and_then father Abraham
  4  from love Lord to-hide_oneself-Lord Lord-<suffix_of_divine_name> offering-chapter and then-exist Isaac
  5  exist tie_up on-+pierce who exist [...] Isaac [...]
  6  name Abraham sacrifice and take_out on-+name
  7  understand-girl-chapter sword who Isaac want slay
  8  and shout Lord-<suffix_of_divine_name> on-cloud on-angel <preposition_of_genitive>-Lord-<suffix_of_divine_name>
  9  leave-leave Abraham-to will <subject_marker> who this.
 10  Abraham Lord-<suffix_of_divine_name> love Lord
 11  this_is to-Lord peace
 12  and then-exist from see look_up
 13  Abraham and see
 14  understand-eat ~lamb
 15  on-understand-eat (thorn)bush

## 005v — the ram, and a prophecy of Christ

> And then he sacrificed the lamb […]; the Lord God from the cloud, by the angel of the Lord, said to Abraham […] within […] A holy [Virgin]; of a virgin shall be born a son […] The son shall be […] Jesus; and the Lord went […] He preached the gospel, [did] many miracles […] and the Lord suffered […]; and […] rose from the dead. […] the Lord God, by the angel, [to] Abraham; and […] the Lord's chapter is believe truly [in] the Son of the living God; every man is saved […] One man […]; but every man is saved [from] the yoke; and man […] the Lord […] believes; and one […] […] but every man was damned, from Adam […] until Abraham, a hundred years and twenty years; from Abraham […] […] Moses began: three thousand and fifty from Abraham until

  1  and then-exist from lamb sacrifice and_then Lord-<suffix_of_divine_name> on-cloud
  2  on-angel <preposition_of_genitive>-Lord Abraham say coming* inside <preposition_of_genitive> understand-girl-chapter
  3  one holy-<reference_to_Virgin_Mary> from virgin-<reference_to_Virgin_Mary> on-be_born son and_his_name*
  4  son exist [?]-from-+name Jézus and go Lord among_the_people*
  5  exist gospel preach many who-and-this-and miracle afterward*
  6  and suffer Lord crucified and on_the_third_day from die stand_up-Lord
  7  and_then Lord-<suffix_of_divine_name> on-angel Abraham and from-and-see chapter-Lord exist
  8  believe righteous(ly) son living God each,_every somebody be_saved and.
  9  one somebody not_damned a) each,_every somebody be_saved yoke and
 10  somebody Lord not believe and one not be_saved.
 11  a) each,_every somebody be_damned from ~Adam onward* table until Abraham
 12  one hundred-year and ten-ten-year from Abraham <subject_marker> table [...]
 13  Moses ~begin-+three_thousand and fifty from Abraham until

## 015r — David the king

> […] David the king humbled himself before […] The king began his repentance […] […] the king […] have mercy; and the king's sin — have mercy. At that time there appeared to the king the angel of God […]; the angel of God [to] David the king: the Lord God. The king […] sin, have mercy. The king keeps the Lord's commandment; and the Lord confirmed the king […] upon the king's throne; and the king proclaimed [it to] the people. Chapter. […] there shall be born […] a son […]; the son shall be the Son of God. And the angel departed from before David […] From David the king until the Virgin Mary […] […] and […] and one […] […] […] and one […] | six(?) […] and […] from David the king until the Virgin Mary

  1  afterward* David king humble against Lord-<suffix_of_divine_name>.
  2  repentance begin king afterward* anointed king Lord-<suffix_of_divine_name>.
  3  have_mercy and sin king have_mercy time appear king
  4  God angel and_then God angel David king Lord-<suffix_of_divine_name>
  5  king <subject_marker> sin have_mercy carry-king <preposition_of_genitive>-Lord commandment and
  6  confirm-Lord king <subject_marker> on-<preposition_of_genitive>-king throne and announce king people-chapter
  7  [...] on-be_born host say son [...] son exist son
  8  God and leave angel before David king.
  9  from David king until virgin-Mary be_born-+day
 10  ~out(ward)-~begin-to-[?] and [?]-hundred-+day and one hundred-+day
 11  ~out(ward) nine_hundred and one hundred-+day | two-two-two
 12  ten-+day and five from David king until virgin-Mary

## 015v — the count of years

> the birthday: from Adam onward until the Virgin Mary | was born, years: five thousand and one hundred years and fifty and four years, and four years.

  1  be_born-+day from Adam onward* ~out(ward) until virgin-Mary | be_born
  2  day five_thousand and one hundred-+day and fifty
  3  and two-two-year and two-two-year

## 016r — Saint Luke

> Saint Luke writes; the sixth(?) […] of his writing; from […] […] […] […] they gave thanks, and prayed to the Lord God.

  1  write holy-Luke six-throne <preposition_of_genitive>-write from remain* kiss.*
  2  exist* holy-in_turn-+one-[?] thanks grab and pray to-Lord-<suffix_of_divine_name>

## 016v — Joachim's offering is refused

> And Saint Anne […]; of the two of them, all their rich substance […] […] one portion they took […]; and a second portion to the Lord […] to the people. […] a portion […] […] And all Joachim's household gave thanks to the Lord God; and […] | […] […] thirty years; and he prepared the offering. […] all […] […]; and then, and from Joachim he brought his offering; and at Joachim looked the chief of the Jews. […] This chief of the Jews [said to] Saint Joachim, […] to this Joachim […] who was […] go among the […] […] of the offering […] one […] and […] […] […] at this. And sorrowfully Joachim departed, and went into the field, into the wilderness […] and from […] […] and at one […] one

  1  and holy-Anne_(mother_of_the_Virgin_Mary) mouth-+day from-two from_the_two_of_them each,_every <preposition_of_genitive>-rich soul on-+three part*
  2  one division grab the_people_of_the_temple on-exist-chapter in_turn-two division
  3  from-Lord way people-chapter third division Joachim-+one-+his_household living.
  4  and each,_every Saint_Joachim_and_his_houseful thanks to-thanks Lord-<suffix_of_divine_name> in_turn have | Joachim
  5  his_household coming* thirty year and prepare offering-chapter
  6  exist-chapter each,_every <preposition_of_genitive>-in_turn-+one-[?] living-+day and then-exist and from Joachim_(the_father_of_Virgin_Mary)
  7  carry <preposition_of_genitive> offering and to-Joachim_(the_father_of_Virgin_Mary) see from head
  8  Jew(ish) and_then this head Jew(ish) holy-Joachim_(the_father_of_Virgin_Mary)
  9  food this-Joachim_(the_father_of_Virgin_Mary) [...] who-exist Joachim* go
 10  among <preposition_of_genitive> answered-year food <preposition_of_genitive> offering [...] one [...]
 11  and out Joachim cast_out on-this exist-chapter and sad(ly)
 12  Joachim_(the_father_of_Virgin_Mary) leave and go inside field inside forest_<hide-out_of_Joachim> chapter-<preposition_of_genitive> from love-exist-to
 13  and from rejoiced love-exist-to and on-one mount one

## 017r — the angel comes to Joachim

> a lamb […]; and then the lamb […] […] At that time, when Joachim was […] God […] […] the angel of God [to] Joachim […] hear […] […] […] the angel of God [to] Joachim, this […] The Lord God has had mercy. Go home, Joachim; and at the golden gate — this Joachim departed — Joachim's wife Anne, and […] a virgin maiden. And then […] and […] The virgin maiden shall be Mary; and Mary shall bear a son […] The son shall be […] Jesus; and the Lord went […] He preached the gospel, did many miracles, and suffered, the Lord […]; and […] rose from the dead; and […] shall be saved, every […] […]; and the man who believes in the Lord. And the angel departed from before Saint Joachim; and at that time the angel […]

  1  lamb sacrifice and then-exist lamb sacrifice [...]
  2  time then-exist Joachim_(the_father_of_Virgin_Mary) exist appear God [...]
  3  and_then God angel Joachim_(the_father_of_Virgin_Mary) have hear [...]
  4  <preposition_of_genitive>-[?] and_then God angel Joachim_(the_father_of_Virgin_Mary) this [...]
  5  Lord-<suffix_of_divine_name> have_mercy go Joachim_(the_father_of_Virgin_Mary) to-home and on-golden
  6  gate this Joachim_(the_father_of_Virgin_Mary) leave <preposition_of_genitive>-Joachim_(the_father_of_Virgin_Mary) wife Anne_(mother_of_the_Virgin_Mary) and conceived*
  7  one virgin-girl and then-exist coming* and [...]
  8  virgin-girl exist Mary and remit Mary on-be_born son whose.
  9  son exist [?]-brother-+name Jézus and go-Lord among_the_people.*
 10  exist gospel preach many who-and-this-and miracle do, and suffer
 11  Lord crucified and on_the_third_day from die stand_up-Lord and ascend* be_saved
 12  each,_every wide world* and somebody Lord exist believe and leave angel
 13  before holy-Joachim_(the_father_of_Virgin_Mary) and time then-exist angel appear

## 017v — the golden gate, and Mary carried nine months

> the angel of God [to] Saint Anne: […] this Anne, […] the Lord God has had mercy, has heard the Lord God, Anne's […]. Go home, Anne; and at the golden gate Anne came to(?) the Lord's Joachim; and there was conceived a virgin maiden. And then was born in the body the virgin maiden — she is Mary; and Mary shall bear a son […]; the son shall be, in the body, Jesus; and the Lord went […]; he preached the gospel, [did] many miracles; and the Lord suffered […]; and […] from death the Lord rose; and […] is saved, every […] […]; and the man who is the Lord's […]. And the angel departed from before Saint Anne; and there was conceived the blessed Virgin Mary. And Mary carried the child nine months, and in the tenth the child was born; and this […] two months; and […] […]; and at six years from Adam onward until the Virgin Mary was conceived and born: five thousand and one hundred and fifty and

  1  God angel holy-Anne_(mother_of_the_Virgin_Mary) have this Anne_(mother_of_the_Virgin_Mary) <subject_marker> Lord-<suffix_of_divine_name> have_mercy hear
  2  Lord-<suffix_of_divine_name> <preposition_of_genitive>-Anne_(mother_of_the_Virgin_Mary) as-reason go Anne_(mother_of_the_Virgin_Mary) to home and
  3  on-golden gate leave Anne_(mother_of_the_Virgin_Mary) <preposition_of_genitive>-Lord Joachim_(the_father_of_Virgin_Mary) and from-get_conceived one
  4  virgin-girl and then-exist be_born body virgin-girl exist Mary
  5  and remit Mary be_born son and_his_name* son exist and-body
  6  Jézus and go Lord among_the_people* exist gospel preach many who-and-this-and
  7  miracle do, and suffer Lord crucified and on_the_third_day from die
  8  stand_up-Lord and ascend* be_saved each,_every wide people* and somebody Lord exist
  9  believe and leave ~angel before holy-Anne_(mother_of_the_Virgin_Mary) and from-get_conceived happy
 10  virgin-Mary and from Mary foetus carry nine moon in_turn ten foetus be_born and this
 11  out(ward) two moon and on-out(ward) five and on-six-year-to
 12  ~out(ward) from Adam onward* until virgin-Mary get_conceived and on-be_born.
 13  five_thousand and one hundred and fifty and

## 018r — Gabriel: Hail, full of grace

> […] months, until the offering […] the blessed Virgin Mary. And then Mary was within […]; from the beginning she withdrew(?) into […] […] and said […] that Mary would keep her virginity | Mary […]. O! O! Amen. And then Mary was […] […] and […]; and at that time God the Father in heaven, because he saw […] all […] darkness […] and at that time God the Father in heaven, and […] the Lord's angel Gabriel […] to the blessed […] Saint Luke writes […] in his writing: at that time the angel said, Gabriel: Hail, thou virgin, maiden full of grace! The Lord God is with Mary […] This virgin maiden: How shall this be? […] this maiden […] this maiden […] this maiden would keep her virginity […] O! O! Amen. […] the angel Gabriel [to] Mary:

  1  ~begin-ten moon until offering inside chapter-year-chapter happy virgin-Mary
  2  and then-exist Mary exist inside three_days from begin go-hide_oneself-this inside exist-chapter
  3  [?]-+one and say [?]-+one this-Mary want virgin-carry | <preposition_of_genitive>
  4  Mary heart chapter-oh chapter-oh amen and then-exist Mary
  5  exist six-six feast and [?]-+three_days and time from-gate
  6  from-father-<suffix_of_divine_name> heaven because see hide_oneself each,_every world darkness sky.
  7  and time from-gate from-father-<suffix_of_divine_name> heaven and go.
  8  <preposition_of_genitive>-Lord angel Gabriel inside exist-chapter to-happy the_Virgin_Mary*
  9  write holy-Luke chapter* <preposition_of_genitive>-write time say angel
 10  Gabriel healing this-virgin-girl have_mercy-girl out(ward) Lord-<suffix_of_divine_name>-Mary and_then
 11  this virgin-girl how? this exist can this-girl know this-girl
 12  ~begin-be_damned this-girl want virgin-girl carry <preposition_of_genitive>-girl heart-[?]
 13  chapter-oh chapter-oh amen and_then angel Gabriel Mary

## 018v — the Holy Spirit, and Elizabeth six months gone

> […] the Holy Spirit shall come upon thee, and grace to all […] This maiden shall conceive a son; and the son […] shall be […] […] the Virgin Mary […] […] said this; and […] would from […] this […] […] the Lord, this […]; and then the maiden […] the Virgin Mary; the word of command to the Lord; Mary […] this […] which maiden the angel said; at this he said […] God the Father, the Virgin Mary | the Holy Spirit; and to the Lord […] […] the Lord Jesus Christ came; the Lord was conceived, Christ. And then […] the Virgin Mary […] the angel Gabriel [to] Mary: Behold, thy kinswoman is six months gone | […] who conceived […] Mary; the son, Saint John […] within the chapter […] […] chapter; the Lord God's mercy to this […]; from John shall be the way made [for] the Lord Jesus Christ, that is the Lord […] this Mary bore; and the Lord went forth […]; he preached the gospel

  1  have want to-girl this go holy-spirit to-each,_every have_mercy [...]
  2  this-girl get_conceived son and ~son shall_be_called* exist Jézus.
  3  and_then virgin-Mary blessed one-to this say and blessed want from Lord-<suffix_of_divine_name>.
  4  this [...] <subject_marker> Lord this overshadow* ~and then-exist girl [...]
  5  virgin-Mary commandment word to-Lord-hide_oneself Mary hide_oneself this overshadow* who girl
  6  exist angel say on-this say pour_out father-<suffix_of_divine_name> virgin-Mary | holy
  7  spirit in_turn to-Lord [...] one go Lord-Jézus-Christ from-get_conceived Lord
  8  Christ and then-exist [...] virgin-Mary and_then angel Gabriel
  9  Mary have lo out(ward) six moon <preposition_of_genitive>-girl relative | holy-+name-chapter
 10  Elizabeth who get_conceived Mary son holy-John [barren] inside chapter <subject_marker>
 11  go chapter Lord-<suffix_of_divine_name> <preposition_of_genitive> have_mercy to-this have from John exist way
 12  do, Lord-Jézus-Christ that_is Lord [...] this
 13  Mary be_born and from Lord go Lord on-+world exist gospel preach

## 019r — Joseph

> […] many miracles […]; and the Lord suffered [under] the Jews […]; and the man who is the Lord's […] truly the Son of the living God — every man […]; and one man is damned; and the Lord […] […]; and one […] but […] a man is damned. Here ends this holy gospel. And at that time the angel was […]; the angel of God the aged […] […] the angel of God […] Joseph. Go, aged one […] within […] […] to Mary; and this […] Joseph was […] aged […] of the son, well-pleasing, from Mary […]; and then the son shall be born […]; the son shall be Jesus; and the Lord went forth […]; he preached the gospel […], did many miracles, and the Lord suffered […]

  1  who-and-this-and miracle afterward* and suffer Lord Jew(ish)
  2  crucified and somebody to-Lord exist believe to righteous(ly)
  3  son living God each,_every somebody be_saved and one somebody
  4  be_damned to and Lord not believe and one to
  5  be_saved a) who_believes_not* somebody be_damned end this holy-gospel
  6  and time then-exist angel exist appear God angel
  7  very_old Joseph and_then God angel very_old
  8  Joseph go very_old Joseph.
  9  inside exist-chapter Joachim* to-to Mary and this very_old.
 10  Joseph exist [...] very_old Joseph-+cross-girl-+mouth
 11  from son to-pleasing from Mary on-?coming and then-exist ~son on-be_born
 12  and-[?]-from-+name ~son exist Jézus and from Lord go among_the_people* exist
 13  gospel preach who-and-this-and miracle do, and suffer Lord [...]

## 019v — the census of Augustus

> [under] the Jews […]; and the man who believes in the Lord […] truly the Son of the living God — every man is saved; and one man is damned; and the Lord […] believes; and one […] but […] a man is damned. Here ends this holy gospel. And then the blessed Virgin Mary was sixteen years old […] There was a decree, before […] the Lord Jesus Christ, twenty and | two years; and […] one year [before] the Lord Jesus Christ […] At that time Augustus the emperor commanded that all […] should be counted. And then […] Augustus […] all […] went back […] and | when it was, the two of them, Mary and aged Joseph, went | […] And then the two, Mary and aged Joseph, took one ox and one

  1  Jew(ish) crucified and somebody to-Lord exist ~believe to.
  2  righteous(ly) son living God each,_every somebody be_saved and one
  3  somebody be_damned to and Lord not believe and one
  4  to be_saved a) who_believes_not* somebody be_damned end this holy-gospel
  5  and then-exist out(ward) happy virgin-Mary ten-six-year time.
  6  exist commandment before coming* Lord-Jézus-Christ ten-ten and | two
  7  two-year and on-?coming one year Lord-Jézus-Christ and.
  8  time command Augustus emperor because
  9  each,_every people* exist make_census and then-exist law Augustus
 10  emperor each,_every world* back go law in_turn-chapter-in_turn and | then
 11  exist and from two Mary very_old Joseph go | to
 12  home* and then-exist two Mary very_old Joseph
 13  exist grab one ox and one

## 020r — no room, and a manger

> donkey; because this they took, aged Joseph the ox, the two of them — aged Joseph and Mary […] […] […] the two of them, the aged […] […] and the donkey was aged Joseph's; he took her who would bear this son | Mary and aged Joseph carried her on the donkey; and then […] aged Joseph, when he arrived | the aged Mary and Joseph, [at] Bethlehem town; and […] […] Mary and aged Joseph […] found none; but the two of them, Mary and aged Joseph, lodged in a barn; and […] […] a manger; and then bought […] Joseph hay; and then the ox

  1  donkey because this exist grab very_old Joseph
  2  from ox who two very_old Joseph Mary
  3  exist remain* [...] who two very_old Joseph.
  4  remain* exist in_turn donkey exist very_old Joseph
  5  grab who this son on-be_born want | very_old-Mary
  6  Joseph on-donkey from-carry and then-exist two.
  7  very_old Joseph exist from arrive | very_old
  8  Mary-Joseph Bethlehem town and [...]
  9  can very_old-Mary-Joseph room find
 10  a) leave two very_old-Mary-Joseph inside one
 11  barn and [...] very_old-?Joseph-Mary-+mouth.
 12  one manger and then-exist buy very_old.
 13  Joseph hay and then two ox

## 020v — the birth, the star, and the angel's news

> and the donkey; he laid the hay; and then the aged | […] a fire began to give light; and then, over his shoulder […] in the night the son was born; and the son was […] Jesus. At that time […] […] light through Bethlehem town; and then a star was seen […]; and from […] […]; and then at the star, a miracle. At that time the angel said […] […] joy! A king is born, a king […] born in Bethlehem town, within […], in a donkey's manger. […] the donkey […] hay within […] […] Christ, Mary's son. And then […] went [to] Bethlehem; and then […] knelt down, and every one of them knelt before […] […] to go […] and […]

  1  donkey exist hay put and then-exist very_old | Joseph*
  2  girl-+mouth ~fire begin-light ~and then-exist shoulder-to begin.
  3  night time on-be_born son and son exist
  4  and-?shall_be_called Jézus time then-exist sky star
  5  through light Bethlehem town and then-exist star
  6  see the_shepherds and from rejoiced love-exist-to and then-exist
  7  on-star miracle time say angel understand-chapter great
  8  joy be_born king king <subject_marker> be_born inside
  9  ~Bethlehem town inside barn inside donkey manger
 10  [...] donkey love hay inside [...] [...]
 11  Christ Mary son and then-exist the_shepherds go Bethlehem
 12  and then-exist rejoiced kneel_(down) and each,_every this exist kneel_(down)
 13  before from the_shepherds [...] to go another and to-Lord.

## 021r — the reckoning of years

> gave thanks, and gave thanks. Here ends this holy gospel […] Saint Luke writes, in […] […] of his writing, chapter […] […] from Adam onward until the birth of the Lord Jesus Christ. […] and […] hundred years and sixty years and six years, until the birth of the Lord Jesus Christ.

  1  thanks and thanks grab end this holy-gospel [...]
  2  write holy-Luke inside one [...] <preposition_of_genitive>-write chapter [...] [...]
  3  out(ward) from Adam onward* until be_born Lord-Jézus-Christ.
  4  five_thousand and one hundred-year and two-two-two-ten-year
  5  and six-year until be_born Lord-Jézus-Christ

## 021v — the flight into Egypt, and the eighth day

> At that time, in the year the Lord Jesus Christ was born […] at that time the angel said […] to the aged […] Rise up, and take this son and his mother(?), this son […] and flee into Egypt. And they went, all of them, beginning […] out of Egypt […] this; the angel […] said […] […] Here ends this holy gospel. At that time he rose up […] | […] and took the Lord Jesus Christ and his mother, and […] the year […] when […] | […] they went into Jerusalem […], that is, when was born the Lord Jesus Christ. On the eighth day the son was circumcised, and the son was named Jesus. And this Lord Jesus first […] shed his blood; and then […] the Lord Jesus was circumcised in Jerusalem. Chapter. And they fled […]

  1  time then-exist to-to-year on-be_born Lord-Jézus-Christ three_days
  2  time say angel understand-chapter very_old Joseph
  3  stand_up up and grab this son and <preposition_of_genitive> this son mother.
  4  and escape inside Egypt-to and go each,_every this begin [...]
  5  out(ward)-out(ward) Egypt [...] this this angel [...] say day [...] end
  6  this holy-gospel time stand_up up the_aged | Joseph
  7  [arise] ~and grab Lord-Jézus-Christ and <preposition_of_genitive> mother and five
  8  year out(ward) then-exist | [...]
  9  day-+Joseph-chapter go inside Jerusalem in_turn-~exist that_is on-be_born
 10  Lord-Jézus-Christ on-six-two-year time circumcise son
 11  and son exist and-from-+day-exist-+name Jézus and this Lord-Jézus first
 12  man* <preposition_of_genitive>-Lord blood shed and then-exist Lord.
 13  circumcise Lord-Jézus inside Jerusalem exist-chapter and escape
 14  Mary_his_mother_the_Holy_Spirit_and_Joseph*

## 022r — Egypt, and the twelve

> into the land of Egypt; and […]; and the Lord went […] in the land of Egypt, into every city […] […] […] the evil ones pierced and pierced; and | […] […] died. From […] they remained in Egypt twelve years, at that time the angel Gabriel said […] Flee into the land of Egypt, into […] city. And […] they remained […] [in that] city twelve years; and […]; and this […] […] years. Here ends this holy gospel. One […] He called twelve apostles; and […] […] and | many miracles […]: the blind eye […] the Lord, through light; the dead […] the Lord […] the evil among the people […]

  1  inside Egypt earth and [...] and go Lord Joseph
  2  on-Egypt earth inside each,_every town [...] hell.
  3  fall_down* evil pierce-pierce and | [?]-mother-?Joseph.
  4  [arise] die from Joseph leave-leave inside Egypt six-six-year
  5  time say ~Gabriel angel Joseph.
  6  escape on-Egypt earth inside Nazareth town
  7  and [?]-mother-+Joseph-chapter leave-leave Nazareth.
  8  town six-six-year and five and this [...] table
  9  ten-ten-two-nine-year end this holy-gospel one
 10  day call six-six apostle and three_days preach and | who-this
 11  and-this miracle afterward* eye blind <subject_marker> Lord through
 12  light die <subject_marker> Lord resurrect evil inside people to-+who-[?]

## 022v — the signs, numbered

> First, that is, […] the Lord made wine […] that is […] the Lord broke […] […] […] […] the people. The fourth sign the Lord Jesus showed, when | […] he raised up from […] a son […] the sign the Lord Jesus showed, when he raised up […] in Jerusalem. The sixth sign the Lord Jesus showed in […] […] when the Jews brought a sick man before the Lord Jesus: a sick man, and a sick man, and a sick man, and a paralytic; and the sick, the sick, the sick, the paralytic — the Lord Jesus healed […] The sign the Lord Jesus showed in Capernaum, when he healed alive the servant of a soldier; and […] […] […] The eighth sign the Lord Jesus showed in Tyre […] to a woman […]

  1  before that_is <subject_marker> Lord wine create-Lord water on-that_is <subject_marker> Lord
  2  break five loaves bread five-?thousand people
  3  in_turn-two-two can show Lord-Jézus then-exist | in_Nain.
  4  before in_turn-to-in_turn resurrect from virgin-~woman son fifth
  5  can show Lord-Jézus then-exist resurrect to-to lose*
  6  inside Jerusalem in_turn-six can show Lord-Jézus inside one.
  7  in_turn-chapter-in_turn then-exist Jew(ish) carry one ill
  8  before Lord-Jézus <man_suffering_from_illness> and <man_suffering_from_illness> and <man_suffering_from_some_kind_of_illness> and paralytic
  9  and <man_suffering_from_illness> <man_suffering_from_illness> <man_suffering_from_some_kind_of_illness> paralytic from-healing Lord-Jézus in_turn-+seven
 10  can show Lord-Jézus inside Capharnaum because from-healing living
 11  two servant one soldier and was_named* soldier.
 12  exist the_centurion in_turn-six-two can show Lord-Jézus
 13  inside Tyrus in_turn-chapter-in_turn to-to one ~woman head

## 023r — the ninth, tenth and eleventh signs

> a […]; and within her was a devil; and […] he cast it out […]. The ninth sign the Lord Jesus showed in | a proud man […] because the man […] did. The tenth sign the Lord Jesus showed in […] a king's son, because he was at the point of death; and the son […] […] The eleventh sign the Lord Jesus showed in Jerusalem: the evil spirit, when the Lord [cast] out of a man a devil […] First, before the birth of the Lord Jesus Christ, the Son of God […] a prophet, a forefather, this […] […] […] Christ […]; and by miracle they confessed […] the Lord Jesus is truly the Son of God. […] confessed […] the Lord Jesus […] the Lord Jesus is truly the Son of God. First confessed […] the Lord Jesus […] and Elijah. Secondly confessed

  1  one pagan and inside to-to exist hell evil and evil.
  2  out(ward) to-+who-[?] in_turn-nine can show Lord-Jézus inside | exist.
  3  proud on-one paralytic somebody because somebody healing.
  4  do, in_turn-ten can show Lord-Jézus inside apostle-oh-<suffix_of_divine_name>-chapter
  5  one king son because exist on-die and son healing.
  6  afterward* in_turn-and can show Lord-Jézus inside Jerusalem evil
  7  then-exist Lord inside one somebody hell evil exorcise
  8  first before be_born Lord-Jézus-Christ son God cannot.
  9  one prophet one forefather this miracle.
 10  afterward* he_is* Christ afterward* and miracle confess
 11  that Lord-Jézus righteous(ly) son God five confess ~have.
 12  Lord-Jézus that Lord-Jézus righteous(ly) son God first confess
 13  ~have Lord-Jézus Moses and Elijah in_turn-two confess

## 023v — who confessed him, and the Transfiguration

> […] the Lord Jesus; God the Father, the Lord's […]. Confessed the evil ones, […] the Lord Jesus is truly the Son of God. Fourthly confessed the Lord Jesus — the angels […] the Lord Jesus is truly the Son of God. They confessed […]; and the earth, the sun, the moon […] the Lord Jesus is truly the Son of God; and all this […] […] the Lord Jesus is truly the Son of God. First confessed it Saint Peter, […] and Elijah. Saint Luke writes that when the Lord Jesus was thirty […], at that time the Lord Jesus went […] [to] Mount Tabor with his apostles; and he was transfigured; and the apostles saw […] and Elijah […] […] and they saw the light […]; and then there stood | the Lord Jesus, and […] and Elijah; and then the apostles, through fear, fell down […]; and then the apostles […]

  1  ~have Lord-Jézus from-father-<suffix_of_divine_name> <preposition_of_genitive>-Lord third confess ~evil evil
  2  that* Lord-Jézus righteous(ly) son God in_turn-two-two confess ~have
  3  Lord-Jézus angel that Lord-Jézus righteous(ly) son God fifth
  4  confess sky and earth sun and.
  5  moon that Lord-Jézus righteous(ly) son God and this each,_every confess.
  6  that Lord-Jézus righteous(ly) son God first confess holy-Peter
  7  Moses and Elijah write holy-Luke then-exist
  8  Lord-Jézus inside thirty years* time go Lord-Jézus on.
  9  Mount_Tabor and <preposition_of_genitive> apostle and be_glorified ~and
 10  see apostle Moses and Elijah white who-+name-believe-year
 11  and see light [...] and then-exist from-leave-leave | Lord
 12  Jézus and Moses and Elijah and then-exist apostle through
 13  get_frightened and down [...] bow_down and then-exist apostle voice,_sound.

## 024r — Tabor and Carmel, and the baptism

> heard this word spoken […] of the Son; and the Father […] […] […] and then home […] not the apostles, and not every […] but to the Lord Jesus. Here ends this holy gospel. Secondly confessed […] the Lord Jesus, God the Father: first on Mount Tabor, secondly on Mount Carmel. Because when the Lord Jesus was thirty […], at that time the Lord Jesus went […] Saint John […] to Mount Carmel; and then the Lord went | [to] Saint John. The Lord Jesus said: John […]. The Lord said | Saint John: Master, and […] […] […]. And the Lord Jesus said, John […] the Lord; and […] is […] Saint John […] baptized the Lord Jesus, when the Lord was thirty years old; and […] the Holy Spirit

  1  hear this word say [...] <preposition_of_genitive> son and father mouth* [...] spoon-+name
  2  and then-exist home [...] not apostle and not each,_every see.
  3  a) to-Lord-Jézus end this holy-gospel in_turn-two confess
  4  ~have Lord-Jézus from-father <preposition_of_genitive>-Lord first on-Mount_Tabor
  5  in_turn-two on-Carmel to-mount because then-exist Lord-Jézus inside thirty
  6  one-+day time go Lord-Jézus understand baptize holy-John
  7  baptize on-Carmel to-mount and then-exist Lord go | to
  8  holy-John say Lord-Jézus John baptize Lord say | holy
  9  John Master and this-~John [...] baptize and say Lord-Jézus
 10  John baptize Lord and mouth-~John exist baptize.
 11  holy-John baptize see-baptize Lord-Jézus then-exist
 12  to-Lord inside thirty year and appear holy-spirit

## 024v — the dove

> in the form of a dove […]: This is the Lord's Son. […] the Spirit came to rest; and the Lord took the Holy Spirit; and the Lord went into […] […] the Lord Jesus […] years […] confessed

  1  inside ~shape,_form dove and_then this-Lord <preposition_of_genitive> son
  2  he_who spirit calm_down and Lord grab
  3  holy-spirit and Lord go inside field
  4  to-[?] Lord-Jézus ten-two-two-year third confess

## 025r — the devils confess him

> the devils […] the Lord Jesus is truly the Son of God. Because when the Lord Jesus was thirty years old, at that time the Lord Jesus went into | […] […]; and then he went into […]. At that time a man knelt down before the Lord Jesus, […] the Lord; the man […] one son; and […] a devil […]. The man's son — his apostles […] could not heal him. […] He begged the Lord to heal this man's son. Said the Lord Jesus: have mercy […] the son […] […] And then the son came before the Lord Jesus; and […] he was made whole; and this […] confessed — the devils […] the Lord Jesus is truly the Son of God, because by miracle they confessed. Fourthly confessed […] the Lord Jesus — the angels, at the birth of the Lord Jesus Christ. Because when the Lord Jesus was born [in] Bethlehem

  1  hell evil that Lord-Jézus righteous(ly) son God because exist
  2  Lord-Jézus inside thirty year time go Lord-Jézus inside | exist
  3  [...] in_turn-chapter-in_turn and then-exist go inside Capharnaum time
  4  then-exist kneel_(down) one somebody before Lord-Jézus
  5  and_then Lord mouth somebody have one son and inside-+<subject_marker>
  6  hell evil [...] somebody son <preposition_of_genitive> apostle to-hide_oneself-to son can
  7  from-healing that* ask_(for) from-healing this Lord <preposition_of_genitive>-somebody son say
  8  Lord-Jézus have_mercy gain [lunatic] son can from-+day healing.
  9  and then-exist son go before Lord-Jézus and on-~way.
 10  healing leave-to-leave and this three confess hell evil that
 11  Lord-Jézus righteous(ly) son God because miracle confess in_turn-two-two
 12  confess have Lord-Jézus angel on-be_born Lord-Jézus
 13  Christ because then-exist Lord-Jézus be_born Bethlehem

## 025v — the Nativity told again

> town; and first, before the birth, one […] was […] a star, light through Bethlehem town; and | then the star was seen […]; and from […] […] and then at the star, a miracle. At that time the angel said […] […] joy! A king is born, a king […] born in Bethlehem town, in a barn, in a donkey's manger […] the donkey, in the hay, in […] […] Christ, Mary's son. And | then […] […] they went [to] Bethlehem; and […] […] knelt down, and every one of them knelt | and […] from […] […] to go […] and […] gave thanks, and gave thanks. Here ends this holy gospel. […] confessed […] the Lord Jesus […]

  1  town and first before be_born one saying exist
  2  sky star through light Bethlehem town and | then
  3  exist star see sons* and from rejoiced son-before.
  4  and then-exist on-star miracle time say angel [...]
  5  great joy be_born king king <subject_marker>
  6  be_born inside ~Bethlehem town inside barn inside donkey
  7  manger [...] donkey inside hay inside
  8  [...] [...] Christ Mary son and | then
  9  exist* sons* go Bethlehem and then-exist.
 10  rejoiced kneel_(down) and each,_every this ~exist kneel_(down) | ~exist
 11  [...] from sons* [...] to go another and
 12  [the_Most_High_Lord] thanks and thanks grab end this holy-gospel
 13  fifth confess ~have Lord-Jézus sky

## 026r — the earth quakes

> and the earth, to the Lord […] and the moon, because because when the Lord Christ […] the earth quaked, the rocks and the stones split.

  1  and earth to-Lord-year and moon because
  2  because then-exist Lord-Christ crucified.
  3  earth quake-rock stone split

## 026v — the sun darkened, and Abraham's confession

> The sun and the moon were darkened; and all […] […] humbled themselves; and all creation […] when Christ […]; and all this […] confessed, in sorrow […], that the Lord Jesus is truly the Son of God; and by miracle they confessed […] the Lord Jesus is truly the Son of God, because […] miracle […]; and the Lord suffered [under] the Jews […] and […] […] the Lord God […] Abraham | […] came […] said. The Lord God said to Abraham by the angel; and this the Lord God said to the blessed Virgin Mary by the angel; and | Saint […] […]; and the man who believes in the Lord, that he is truly the Son of the living God — every man is saved; and […] a man is damned; and the Lord […] believes; and […] one is saved, but […] a man is damned; and | this thus he said. First confessed it Abraham the forefather | This one confessed […]; secondly confessed […]

  1  sun and moon this eclipse and each,_every tree into_the_world* this humble and each,_every
  2  create mourn then-exist Christ crucified and this each,_every five confess
  3  inside-to-sad(ly) that Lord-Jézus righteous(ly) son God and miracle confess
  4  that Lord-Jézus righteous(ly) son God because various.
  5  miracle afterward* and suffer Lord Jew(ish) crucified
  6  and to-+who-+day the_Lord Lord-<suffix_of_divine_name> announce Abraham | patriarch
  7  holy-+day arrive then* say exist say Lord-<suffix_of_divine_name> Abraham on-angel and this
  8  say say Lord-<suffix_of_divine_name> happy virgin-Mary on-understand-chapter angel and | holy
  9  very_old Joseph and somebody to-Lord exist believe
 10  what righteous(ly) son living God each,_every somebody be_saved and one.
 11  somebody be_damned to and Lord not believe and [...]
 12  one to be_saved a) who_believes_not* somebody be_damned and | this
 13  and-this say confess first Abraham forefather | on-this
 14  this confess holy-in_turn-+one-[?] on-that_is confess holy_Anne

## 027r — Mary's confession

> the mother, the blessed Virgin Mary. Thirdly confessed the blessed | Virgin Mary. The angel of God said: at that time the Lord was; the Lord God went; the Lord's angel [to] the blessed Virgin Mary, when […] from […] to the house of the Virgin Mary […]; and she bore; and […] […] and one hundred and sixteen(?) years and […] and and […] at that time God the Father in heaven, because he saw […] all […] darkness […]. At that time God the Father in heaven; and the Lord's angel Gabriel went […] to the blessed Virgin Mary, and said this and that. Saint Luke writes […] in his writing; and the man who believes in the Lord, that he is truly the Son of the living God — every man is saved; and one man is damned; and the Lord […] believes; and one is saved; but every man

  1  mother happy virgin-Mary on-that_is confess happy | virgin
  2  Mary say angel God time exist Lord go Lord-<suffix_of_divine_name> <preposition_of_genitive>-Lord
  3  angel happy virgin-Mary then-exist ~out(ward) from want-year to-house
  4  virgin-Mary get_conceived and be_born and [...] [?]-+day
  5  and one hundred and six-ten-year and five and and moon.
  6  time from-gate from-father-<suffix_of_divine_name> heaven because see hide_oneself each,_every
  7  people* darkness sky time from-gate from-father-<suffix_of_divine_name>
  8  heaven and go <preposition_of_genitive>-Lord angel Gabriel inside exist-chapter
  9  to-happy virgin-Mary and this-and-this say write holy-Luke
 10  chapter* <preposition_of_genitive>-write and somebody to-Lord exist believe
 11  to righteous(ly) son living God each,_every somebody be_saved and
 12  one somebody be_damned to and Lord not.
 13  believe and one to be_saved a) each,_every somebody

## 027v — Joseph's confession, and "there are not many gods"

> is damned; and thus he said. Confessed it Saint Joseph the aged | […] the angel of God said, because the Lord God spoke by the angel Gabriel; and […] who is the Lord's […] truly the Son of the living God — every man is saved; and one man is damned; and the Lord […] […]; and | […] […] is saved, but every […] is damned; and | thus he said. The Lord Jesus spoke of his many wounds, when the Lord went | to his death; and then the Lord […] the apostles in Jerusalem. At that time knelt the Lord Jesus before the blessed Virgin Mary; and the Lord Jesus said: there are not many gods […] one God […] the Lord Jesus […] and the Lord […] […] in the Lord Jesus Christ; and one is saved, but every man is damned; and Mary blessed the Lord Jesus, with all the apostles — the blessed Virgin Mary.

  1  be_damned and this-and-this say confess holy-very_old | Joseph
  2  [...] say angel God because exist say Lord-<suffix_of_divine_name> on-angel
  3  Gabriel and whosoever* to-Lord exist believe to righteous(ly)
  4  son living God each,_every somebody be_saved and one
  5  somebody be_damned to and Lord not believe and | one
  6  chapter to be_saved a) each,_every whosoever* be_damned and | this-and
  7  this say say Lord-Jézus on-many wound then-exist Lord go | on
  8  die and then-exist-Lord ~go-[?] apostle inside Jerusalem time kneel_(down)
  9  Lord-Jézus before happy virgin-Mary and say Lord-Jézus is_not
 10  many God but_rather* one God and_then Lord-Jézus
 11  to and Lord not believe inside Lord-Jézus-Christ and
 12  one to be_saved a) each,_every somebody be_damned
 13  and Mary bless Lord-Jézus on-each,_every apostle happy virgin-Mary

## 028r — the Passover lamb, and the twelfth sign

> And then Mary […] the Lord Jesus, the Lord's mother, the blessed Virgin Mary; and then Mary was, and from […] […] Mary's son the Lord Jesus Christ; and from Mary went the Lord Jesus […] the apostles in Jerusalem, because […] the apostles […] Before the Lord went into Jerusalem, where the apostles [were] at supper […] the apostles prepared a lamb, because at that time was the feast of the Jews, the Passover. […] There began the suffering of the Lord Jesus Christ, Son of God; because […] the Lord is truly the Son of God. And then the Lord, the Jews […]; and then the Lord, the apostles, the mother; he was laid in the tomb, and […] rose from the dead. And the | twelfth sign the Lord Jesus showed, when […] from […] the Lord and the apostles […] in Jerusalem; and […] the sign the Lord Jesus showed

  1  and then-exist-Mary exist-Lord kiss Lord-Jézus <preposition_of_genitive>-Lord mother
  2  happy virgin-Mary and then-exist-Mary exist and from Mary.
  3  kiss <preposition_of_genitive>-Mary son Lord-Jézus-Christ and from Mary from-go
  4  Lord-Jézus Bethany apostle inside Jerusalem because <subject_marker> apostle exist.
  5  before Lord go inside Jerusalem who-exist apostle to-dinner-to-to eat.
  6  prepare-apostle one lamb because time
  7  holiday exist Jew(ish) Easter this_is begin suffering
  8  Lord-Jézus-Christ son God because <subject_marker> Lord righteous(ly) son God
  9  and then-exist Lord Jew(ish) crucified and then-exist Lord apostle
 10  mother inside burial_chamber put and on_the_third_day from die stand_up-Lord and from | six
 11  six can show Lord-Jézus then-exist rise*
 12  from pray Lord and apostle appear inside Jerusalem and six-+seven can show Lord-Jézus

## 028v — the Ascension

> when […] […] on a mountain, two men and two men […] […] and […] and sixteen(?) and six devils and the two men were healed […] […] the sign showed the Lord Jesus; then […] when he went to God his Father | in heaven […]; the Lord sat at the right hand of God the Father.

  1  then-exist [...] [...] one mount two somebody and two somebody
  2  exorcise six-?hundred and six-?thousand and six-ten and six hell evil
  3  and two somebody healing afterward* fourteen can show
  4  Lord-Jézus then cross-wound then-exist leave to-<preposition_of_genitive>-Lord father-<suffix_of_divine_name> | on
  5  heaven in_turn-[?] from-sit-Lord from-father-<suffix_of_divine_name> God on-right_side

## 029r — the Passion begins: "Here begins"

> Here begins […] […] of a man […] the writing […] […] [of] Saint Matthew and Saint John, of the Passion | a man […] […] The Lord Jesus went […] to Jerusalem, because […] the Lord […] to the supper […] because […] Before the Lord went, the apostles [went] into Jerusalem […] the Lord Jesus […] to prepare the Passover lamb, where the Lord and the apostles […] should eat. And the Lord [said]: go, you. And then the Lord […] to the apostles in Jerusalem; and the Lord sat down at the table […] the apostles. At that time the apostles prepared the Passover lamb; and the lamb

  1  begins this begin the_account*
  2  Passion <preposition_of_genitive>-somebody heart-Lord
  3  write the_account* cup-not [...]
  4  holy-Matthew and holy-John
  5  from suffering | <preposition_of_genitive>.
  6  somebody heart-Lord time.
  7  go Lord-Jézus to_Bethany
  8  Jerusalem because from far-to-Lord to-dinner-chapter afterward* because exist Lord.
  9  before Lord go apostle inside Jerusalem and_then Lord-Jézus exist apostle.
 10  prepare from Easter lamb who-exist Lord apostle to-dinner-chapter.
 11  eat and this-Lord to you go and then-exist Lord go.
 12  to-apostle inside Jerusalem and sit to-throne Lord [...] this-apostle time
 13  exist apostle prepare from Easter lamb and lamb

## 029v — the supper, and the washing of feet

> the apostles brought to the table […] the Lord Jesus […] the Lord's […] […] the Lord would eat this with you […] lamb. Therefore the Lord asks you: do not, apostles, be offended in the Lord, because the Lord goes to his death — the Lord dies; and the Lord | […] […] […] and the Lord […] you […] and […] the Lord Jesus [rose] from the table, and laid aside | the Lord, his […] […]. The Lord Jesus, one apostle among […] the apostles, and among […] the apostles, and […] an apostle [named …] brought a bucket […] and a washing-dish; and then water into the dish he poured; and the Lord Jesus came to Saint Peter, and […] brought the water in the dish, which the Lord Jesus […] Saint Peter.

  1  carry apostle on throne and_then Lord-Jézus brother <preposition_of_genitive>-Lord from
  2  lamb* want Lord to you eat this Easter.
  3  lamb that_is_why ask_(for)-Lord you do_not apostle
  4  inside Lord stumble because this-Lord go on-die Lord die and this-Lord | on
  5  three_days again* rise-Lord and this-Lord you appear
  6  and rise to-throne Lord-Jézus and take_off-Lord | on
  7  Lord <preposition_of_genitive>-Lord believe-~exist and_then Lord-Jézus one apostle
  8  among seven-ten apostle and among seven apostle and [?]-from-+name
  9  apostle exist Titus_<Roman_emperor>-in_turn carry one bucket water
 10  and one washdish and then-exist water inside washdish
 11  pour and go Lord-Jézus to holy-Peter in_turn Titus_<Roman_emperor>-in_turn
 12  carry inside washdish water this-who Lord-Jézus and_then holy-Peter

## 030r — Peter objects

> Master […] Peter […] the Lord […] washes my feet? […] the Lord Jesus […] […] the Lord […] the feet washed […] […] […] within […] […] […] […] Master […] Peter, this […] trespass; the Lord, the sufferer […] […] […] […] the Lord in heaven […] | […] the Lord took […] […] washed; and all […] […] he washed; and | then […] […] the Lord washed their feet; and the feet […] […] […] and the two of them from […] among the apostles, every one he washed; and the feet […] […] […] and the Lord Jesus took […] his […] and

  1  Master not_let this-Peter brethren* this-Lord with* foot wash
  2  and_then Lord-Jézus with* if this-Lord this-?with foot
  3  wash understand-+one this-cut_off-[?] [...] inside heaven in_turn-[?]
  4  and_then holy-?with Master sky* this-Peter this
  5  love-to-+high-[?] trespass this-Lord sufferer brethren-to-+high-[?]
  6  with* cut_off-?be_born [...] this-Lord inside heaven in_turn-[?] | love-cut_off.
  7  this-?with this-Lord grab-cut_off-to [...] head.
  8  wash and each,_every <preposition_of_genitive>-?with shall_be_called* wash and | then
  9  exist with* <subject_marker> foot exist-Lord wash and foot
 10  <subject_marker> garment* towel and two from go_away apostle middle each,_every
 11  wash and foot <subject_marker> garment* [...] and
 12  grab Lord-Jézus on-Lord <preposition_of_genitive>-Lord believe-~exist and

## 030v — the bread, and the cup with water and wine

> The Lord Jesus sat at table with the apostles […]; the Lord Jesus looked […] the apostles […] see how the Lord […] you […] from […] and you shall eat […] […]; and took the Lord Jesus […] one baked loaf, and […] the Lord Jesus this […] and […] the Lord set it before them; and the Lord Jesus took wine in a cup, and poured water into the cup; and […] the Lord Jesus, the wine and the water; and the wine and water the Lord Jesus set before them […] the Lord Jesus; and […] whoever eats of this […], that man shall be | the Lord's […] […]; and the man who […] this […]

  1  sit Lord-Jézus to-throne to-apostle and_then Lord-Jézus see <subject_marker> apostle
  2  to-Lord see how? this-Lord you as* from rather*
  3  and you understand-eat two as* and grab
  4  Lord-Jézus inside why?-in_turn one baked „cake”
  5  and blessed Lord-Jézus this bread and bread
  6  before Lord put Lord-Jézus and grab Lord-Jézus
  7  wine one cup and water inside cup pour and blessed
  8  Lord-Jézus wine and water and wine water
  9  before Lord put Lord-Jézus and_then Lord-Jézus and somebody.
 10  exist this bread eat this somebody exist | <preposition_of_genitive>
 11  Lord shall_be_called* from-+who-chapter and somebody exist this bread

## 031r — one of you shall betray me

> eats and believes in the Lord […]; every man is damned […] and the man who believes in the Lord […] is from […] they ate the holy Host […] drank […] that man shall live. O! O! Amen. […] The Lord Jesus […] […]: one among you and […] the Lord […] one of the apostles shall betray him. And the apostles looked among the apostles, saying […] Master […] and […] the Lord Jesus said; and […] […] the Lord Jesus […] and John, and said: O […] […] […] Master, who is it? And then he leaned […] upon the Lord Jesus […] Master | thus said the Lord Jesus […]; the Lord took a morsel

  1  eat and Lord believe each,_every somebody be_damned cut_off-[?]
  2  and somebody exist Lord believe and exist from
  3  thirty holy-host eat and drink each,_every.
  4  somebody exist living chapter-oh chapter-oh amen and_then
  5  Lord-Jézus know* <subject_marker> one among you
  6  and [?]-+<subject_marker> Lord name-+one from apostle betray and see-apostle among
  7  apostle say holy-?with Master who_is_it and struck-to.
  8  say Lord-Jézus and [...] [...] Lord-Jézus
  9  with* and ~John and say oh <preposition_of_genitive>-?with ~exist-exist
 10  from-judge Master Who_is_it? and then-exist lean_on
 11  holy-~John on-end Lord-Jézus and_then Master | name-+one.
 12  this-and-this say Lord-Jézus to_whom this-Lord grab bite

## 031v — Satan enters into Judas

> […] It is he. And then […] […] upon the Lord Jesus; and he took this […] […] and […] the Lord Jesus […] this […] And then […] Judas […] took; and then […] Judas […] In that place the devil entered into Judas. […] the Lord Jesus; the apostles weeping […]; and he took this […] the Son of God […] the Lord Jesus. Judas did […] did; and then […] the apostles, how he said: Master, speak. But the apostles did not understand what Judas said. […] bought […] shepherd […] because […] the apostles […] because this was the Jews' Passover.

  1  bread That_is_it. and then-exist sleep holy-~John
  2  on-end Lord-Jézus and grab this Lord-Jézus.
  3  Nicodemus and see* Lord-Jézus [...] this
  4  bread and then-exist bread exist-Lord Judas
  5  Iscariot grab and then-exist bread Judas
  6  were_opened* on-to-place hell evil inside Judas go-this
  7  and_then Lord-Jézus apostle crying from somebody and grab this
  8  from son God and_then Lord-Jézus Judas do,
  9  who-exist do, and then-exist evil apostle how?
 10  say Master speak a) understand apostle how? say Judas
 11  bread buy brethren-exist shepherd from-+who-chapter because
 12  food apostle ~exist judge because this exist Jew(ish) Easter

## 032r — Wednesday, and the silver

> and […] Judas; and he went [to] the Jews' chief in Jerusalem; because the Lord was […]. On Wednesday one of the apostles betrayed him — Judas — because he took for the Lord […] silver […] the Lord Jesus; the Lord's brethren; the Lord goes to God his Father; and the Lord […] to you the Holy Spirit shall come; and you shall […] […] that is, the Lord goes to his death; the Lord dies, because the Lord, the Jews […]; and the Lord […] […] the Lord shall rise. Therefore the Lord asks you: do not, apostles, be offended in the Lord, because […] [to] God his Father […] […] […] the Lord […] […]

  1  and rise Judas and go Jew(ish)
  2  head inside Jerusalem because Lord exist inside Wednesday from apostle
  3  betray Judas because exist to-Lord grab thirty
  4  silver and_then Lord-Jézus brother <preposition_of_genitive>-Lord this-Lord
  5  go <preposition_of_genitive>-Lord father-<suffix_of_divine_name> and this-Lord you
  6  go holy-spirit and you exist see-two
  7  judge that_is this-Lord go on-die Lord die because
  8  Lord Jew(ish) crucified and this-Lord on_the_third_day
  9  again* stand_up-Lord that_is_why ask_(for) Lord you
 10  do_not apostle inside Lord stumble because what-go saying
 11  <preposition_of_genitive>-Lord father-<suffix_of_divine_name> [...] saying <subject_marker> Lord crucified and_then

## 032v — Peter will deny him

> Peter: Master — Peter would […] the Lord; the Lord dies. […] the Lord Jesus [to] Peter: first, but before […] […] thou shalt deny the Lord. And Peter said […] […] […] the Lord Jesus, Peter, this […] this […] Therefore the Lord asks you: do not […] be offended in the Lord; because the apostles were very sorrowful for the Lord; and one of the Jews was a judge; and the mouth […] the Lord Jesus said: but […]; and the Lord went on the way, because the Lord Jesus […] when the Lord […] Judas, in the house of the high priest; and many miracles and much preaching […] the Lord Jesus, on the way.

  1  Peter Master this-Peter want food Lord this-Lord die
  2  and_then Lord-Jézus Peter first a) before cock
  3  this-?with Lord-to three exist deny and Peter say with*
  4  emperor and_then Lord-Jézus Peter this <subject_marker> this
  5  ~out(ward) that_is_why ask_(for) Lord you do_not apostle.
  6  inside Lord stumble because exist apostle many sad(ly) on-Lord have
  7  in_turn one Jew(ish) exist judge and mouth
  8  can Lord say Lord-Jézus a) rise and go Lord
  9  on-way because have Lord-Jézus then-exist Lord know
 10  Judas inside house ~high_priest and many miracle
 11  and many ~preach afterward* Lord-Jézus on-way

## 033r — over the brook Cedron, into the garden

> And Saint John tells of many miracles and much preaching […] of the Lord Jesus […], but it is not written down. And then the Lord and the twelve apostles […] […] There was a brook […]; and of the apostles the rest of the apostles […]. The Lord took Peter, John, and […], and […] across the Cedron; and […] into […] and […], because there was a garden there […] […] Jerusalem […]; and […] the Lord went to Jerusalem; and in Jerusalem, behold, the Lord […] to the Lord Jesus and his apostles, because they would seize the Lord Jesus and take him in the garden. […] of the man, the father Adam […] […]

  1  and speak holy-John many miracle and many ~preach
  2  afterward* Lord-Jézus on-~way but inside write not
  3  write and then-exist Lord six-six apostle [?]-+day this.
  4  exist one brook Kidron and from apostle
  5  rest apostle third apostle Lord grab Peter and.
  6  John and James and [?]-[?].
  7  over-exist Cedron and to-?again inside mount
  8  and [?]-+one-[?] because-exist garden on-this mount
  9  trespass Jerusalem in_turn-to-in_turn and then-+<subject_marker> go-Lord on-Jerusalem and inside
 10  Jerusalem lo Lord [?]-Lord-apostle to Lord-Jézus and <preposition_of_genitive>-Lord apostle
 11  because want-Lord grab Lord-Jézus inside-garden capture
 12  he_is* <preposition_of_genitive>-somebody father ~Adam [...] [...]

## 033v — a stone's cast, and the prayer

> through […] this the Lord Jesus would, to a man […] […] suffering, not […]; and then from the Lord the apostles in the garden; and the Lord went […] tells Saint John. The Lord went […] from the apostles […] about a stone's throw […]; his Father; and he knelt down, the Lord Jesus […] Father, his God […] […] take from the Lord this suffering; nevertheless […] as it pleases thee. And […] the Lord Jesus; and the Lord went to the apostles […]; the apostles were asleep […] the Lord Jesus […] and […] woke them; and the Lord Jesus went […] Peter [to] the hilltop […] to see this […], because all the people were

  1  through sin this want Lord-Jézus to-somebody [...]
  2  [...] suffering not-to and then-exist from-to Lord
  3  apostle inside garden in_turn to-Lord go on-[?] speak
  4  holy-John from-go-Lord trespass from apostle [...] then-chapter
  5  stone to-throw pray father <preposition_of_genitive>-Lord and kneel_(down)
  6  Lord-Jézus and_then father <preposition_of_genitive>-Lord God heaven.
  7  from not_take-father from Lord this suffering in_turn
  8  <subject_marker> pleasing and rise Lord-Jézus and go-Lord
  9  to apostle but apostle to-sleep and_then Lord-Jézus rise
 10  and ~have-apostle awake and go Lord-Jézus Peter
 11  mountain_peak mount to see this people-+day because exist each,_every people

## 034r — the second prayer, and the sweat

> And a second time the Lord went […], and the Lord Jesus knelt […] God the Father […] take from […] from the Lord this suffering; nevertheless […] as it pleases thee. And then the sweat ran down the Lord Jesus, because […] the Lord Jesus […] the Lord's suffering […]. And the Lord went to the apostles […]; the apostles were asleep […] the Lord Jesus […]; and […] woke them. At that time Saint Peter went […] […] sat and […] the Lord went […] to God his Father, and knelt | the Lord Jesus […] God his Father […] from | Father, take from the Lord this suffering; nevertheless […] as it pleases thee; nevertheless […] as it pleases thee; because God the Father […] for the Lord, the whole wide world |

  1  and two go Lord on-?as-[?] and kneel_(down) Lord-Jézus and_then
  2  father-<suffix_of_divine_name> eternal* from not_take-father from Lord this suffering
  3  in_turn <subject_marker> pleasing and then-exist to-to-to sweat through
  4  Lord-Jézus because [...] Lord-Jézus how?-?first Lord suffering
  5  not-chapter and go Lord to-apostle but apostle to-sleep
  6  and_then Lord-Jézus rise and ~have-apostle awake
  7  time go holy-Peter and_say on-+three army-to sit
  8  and three go Lord as-before father-<suffix_of_divine_name> <preposition_of_genitive>-Lord and kneel_(down) | Lord
  9  Jézus and_then father-<suffix_of_divine_name> <preposition_of_genitive>-Lord eternal* from | not_take
 10  father from Lord this suffering in_turn <subject_marker> pleasing in_turn
 11  [...] pleasing because this-father-<suffix_of_divine_name> out(ward)-+one-out(ward) on-Lord ~the_whole_wide_world | <preposition_of_genitive>

## 034v — the angel from heaven

> the Father. And an angel came […] from on high, from God the Father […] the Lord, this […] this […] this suffering […] […] the angel […] offered the Lord […] the Lord's lot, of God the Father; the Son Jesus […] all […] redeemed. And the angel departed from before the Lord Jesus; because every night the angel came from on high, from God the Father, to the Lord Jesus; because the angel bore for the Lord all his suffering, it is written; and […] truly […] […] […] written. And the Lord went to the apostles […] the Lord Jesus […] his […]; and the Lord and the apostles had one […] […]; and then […] […]; and then the apostles |

  1  father and go angel from_the_eternal* high from-father-<suffix_of_divine_name> and_then
  2  Lord this ~have this the_Lord this suffering drink
  3  and_then angel this_is this-Lord offer from-father-<suffix_of_divine_name>.
  4  <preposition_of_genitive>-Lord fate <preposition_of_genitive>-father-<suffix_of_divine_name> son Jézus Nazareth
  5  each,_every people* from-buy and leave-to-leave angel before
  6  Lord-Jézus because each,_every night this-go angel high from-father-<suffix_of_divine_name>
  7  to-Lord-Jézus because Lord carry angel each,_every <preposition_of_genitive>-Lord suffering
  8  write and [...] righteous(ly) out(ward)-+one-out(ward) he_who* from-prophet.
  9  write and go-Lord to-apostle and_then Lord-Jézus
 10  brother <preposition_of_genitive>-Lord and have-Lord-apostle one little
 11  not-?not-?first and then-exist [...] [...] and then-exist apostle | to

## 035r — the sign, and the kiss

> slept. And the Lord Jesus could not sleep; but the Lord laid a stone at his head; and the Lord Jesus could not sleep; but […] […] the Lord, the apostles […] the apostles […] […] […] […] because from […] came the Jews […] […] the Son of God […] to take him. And then the Lord and the apostles went on the way, and saw | the Lord Jesus a great crowd coming; and among the Jews was Judas. […] the father died, and the mother […] […] Judas and the Jews. He gave a sign, to tell the Lord apart from James and John — a kiss — so that Judas […] the Jews might take the Lord. And then Judas went up to the Lord Jesus; and […] Judas […] the Lord's hand; because he had given the Jews the sign,

  1  sleep and can sleep Lord-Jézus a) Lord-put one stone
  2  to-head and can sleep Lord-Jézus a) rise
  3  and_then Lord apostle rise apostle to-?again have-apostle [...]
  4  serpent* because from know* go Jew(ish) [...]
  5  somebody-<suffix_of_divine_name> son recognize* capture and then-exist
  6  Lord apostle and apostle go-Lord-and-apostle on-way and see | Lord
  7  Jézus many people-chapter go and among Jew(ish) exist Judas
  8  he_who from-father die and mother [...] sleep [...] Judas and Jew(ish)
  9  ask_for_sign distinguish Lord James John with* kiss
 10  Judas from Lord capture Jew(ish) and then-exist
 11  go Judas against Lord-Jézus and kiss.
 12  ~Judas <preposition_of_genitive>-Lord hand because to-Jew(ish) ask_for_sign

## 035v — "Whom seek ye?" and they fell backward

> because John was like the Lord Jesus. And he cried out, | the Lord Jesus: Whom seek ye? The people, the Lord's — the Jews. And they cried, the Jews […] […] Jesus […]; and cried the Lord Jesus: I am he, if ye seek the Lord — the Jews. And all the Jews fell backward […] the Lord Jesus […] […] […] […] hidden […] staves; and […] […]; and the Jews' staves […] because the Lord Jesus […] did; God his Father, to the Jewish people; and […] […]; and a second time the Lord Jesus cried: […] seek ye, the people, the Lord's — the Jews. And they cried […] […] […] Jesus […]; and cried the Lord Jesus: I am he, if ye seek the Lord — the Jews; and

  1  because exist similar John to-Lord-Jézus ~and shout | Lord
  2  Jézus who(m)? search people <preposition_of_genitive>-Lord Jew(ish) and shout
  3  Jew(ish) say answered Jézus Nazareth and shout
  4  Lord-Jézus from this-Lord if Lord search Jew(ish) and each,_every
  5  Jew(ish) back bow_down and_then Lord-Jézus rise-Jew(ish) again*
  6  [...] say hide_oneself <preposition_of_genitive>-club and rise-+say again* and <preposition_of_genitive>-Jew(ish)
  7  club grab-+say inside why?-in_turn because Lord-Jézus as*
  8  do, father-<suffix_of_divine_name> <preposition_of_genitive>-Lord to-Jew(ish) people and
  9  rise-Jew(ish) to-?again and two shout Lord-Jézus whom search
 10  people <preposition_of_genitive>-Lord Jew(ish) and shout Jew(ish).
 11  say answered Jézus Nazareth and shout
 12  Lord-Jézus from this-Lord if Lord search Jew(ish) and

## 036r — the third cry, and Jesus of Nazareth

> All the Jews fell backward […] the Lord Jesus […] […] […] hidden […] staves; and […] […] and the Jews' staves […] because | the Lord Jesus […] […] God his Father, to the Jewish people; and […] […]; and a third time he cried | the Lord Jesus: Whom seek ye? The Lord's […] the Jews; and the Jews cried, they answered: Jesus of Nazareth. And the Lord Jesus cried: I am he. If ye seek the Lord — the Jews. And then the Lord Jesus cried: Take me, ye Jews, for I go […] to God my Father. And then the Jews […] the Jews, the Lord Jesus […]

  1  each,_every Jew(ish) back bow_down and_then Lord-Jézus rise-Jew(ish) again*
  2  he_said* hide_oneself <preposition_of_genitive>-club and rise-+say again* and <preposition_of_genitive>
  3  Jew(ish) club grab-+say inside why?-in_turn because | Lord
  4  Jézus as* afterward* father-<suffix_of_divine_name> <preposition_of_genitive>-Lord to Jew(ish)
  5  people ~and rise-Jew(ish) to-?again and three shout | Lord
  6  Jézus whom search <preposition_of_genitive>-Lord Jew(ish)
  7  and shout Jew(ish) say answered
  8  Jézus Nazareth and shout Lord-Jézus from this-Lord
  9  if Lord search Jew(ish) and_then shout Lord-Jézus
 10  grab Jew(ish) Lord because go living-~exist <preposition_of_genitive>-Lord father-<suffix_of_divine_name>
 11  and then-exist ~Jew(ish) from-leave-leave Jew(ish) Lord-Jézus [...]

## 036v — Malchus, and the ear put back

> He cut off […] […] the ear of one of the Jews, and that Jew was Malchus. And then the Lord Jesus [said]: Peter, Peter, […] thou hast cut off […] because the man Peter […] cut off from […] […] […] die. And the Lord Jesus took the ear and put it back in its place, and the ear was made whole. And the Lord Jesus [did] that miracle before the heathen […] and […] said, and believed in the Lord; but his […] | the Lord […]; and one of the Jews fled, and believed in the Lord Jesus; and from […] the Lord Jesus all said […] these Jews went; and […] from […] […] And then the Lord could have fled — the Lord did not flee, but […] […] the apostles, the Jews […] […]

  1  cut_off with* sword ear one Jew(ish)
  2  and was_named* Jew(ish) exist Malchus and_then
  3  Lord-Jézus Peter Peter blind* cut_off sword because and
  4  somebody Peter sword cut_off from sword.
  5  struck* somebody-+<subject_marker> die and grab Lord-Jézus this ear
  6  and ear-+<subject_marker> put on-place and healing ear
  7  leave-to-leave and from Lord-Jézus on-pagan miracle ~exist-+who-Lord-~exist
  8  and and say inside Lord believe a) <preposition_of_genitive>-Lord believe* | on
  9  Lord take_off and escape one Jew(ish)
 10  to-Lord believe Lord-Jézus and from [...] to-Lord [...] Lord-Jézus
 11  each,_every say [...] this-who Jew(ish) go and then-[?] from little
 12  [...] and then-exist Lord want escape exist Lord not escape
 13  a) good [...] to-?whosoever apostle Jew(ish) pagan-+day above-high

## 037r — bound, and struck

> […] and […] led the Lord […] the Lord Jesus; and then […] the hands of the Lord Jesus Christ […] all […] […] […]; and then […] they went to the chief of the Jews […]; and then the Lord went down from the mountain; and many […] […] Jews upon the Lord Jesus, because one struck the Lord […] […] secondly, to the Lord's house […] thirdly […] no man at all had mercy on the Lord Jesus. And then through […] through […] […] and the Lord […] went over the bridge […] but the Lord on the bridge […]; and […] […] no man had mercy on the Lord Jesus, because […] the Jews went

  1  cross-[?] and then-[?] carry to-Lord believe.
  2  Lord-Jézus and then-exist tie_up hand Lord-Jézus-Christ
  3  [...] each,_every to-<preposition_of_genitive>-Lord to-year-to [...] that* and then-exist Lord.
  4  go to-Jew(ish) head [...] and then-exist Lord
  5  go down on-to-mount and many [...] afterward*
  6  Jew(ish) on-Lord-Jézus because Lord one scourged* beat
  7  [...] town* in_turn-two to-Lord to-house [...] third
  8  to-Lord [...] from not-not <preposition_of_genitive>-somebody have_mercy Lord-Jézus
  9  and then-exist through [?]-+say through over-~exist Kidron
 10  and Lord grab-+say on-bridge go Lord-Jézus.
 11  a) Lord on-bridge fall_down and to-Lord [...] who.
 12  <preposition_of_genitive>-somebody have_mercy Lord-Jézus because Lord two [...] go Jew(ish)

## 038r — bound before Caiaphas

> […] they bound the Lord Jesus Christ; and then the Lord […] and dragged him out […]; no man had mercy on the Lord Jesus Christ. And then the Jews […] the Lord would the Jews went […] one […] the Lord | Pilate; secondly […] to Caiaphas; and | when the Lord […] to Caiaphas the high priest. And then the Jews […] accused the Lord; and then the Lord […] before the high priest's house; and | when the Lord […] […] the Lord this […] and then the Lord […] into a house; and | when the Lord […] one […] […] | not at all the Lord Jesus Christ said. And then Peter, one

  1  [...] who-chain-to Lord-Jézus-Christ and then-exist Lord
  2  exist and out(ward)-out(ward) draw [...] <preposition_of_genitive>-somebody have_mercy
  3  Lord-Jézus-Christ and_then Jew(ish) who Lord want
  4  Jew(ish) go say-+say one brought* Lord | to
  5  Pilate in_turn-two say brought-Lord to-Caiaphas and | then
  6  exist Lord brought-Lord to-Caiaphas high_priest and_then
  7  Jew(ish) would_say* Lord on-+three accuse and then-exist
  8  Lord to-[?] before <name_of_a_priest> high_priest house and | then
  9  exist Lord exist-+say inside-?brought Lord this high_priest.
 10  and then-exist Lord gate inside one house and | then
 11  exist Lord from-to-each,_every one [...] from-[?] | not-not
 12  say Lord-Jézus-Christ and_then Peter one

## 038v — the first denial, and Caiaphas's counsel

> of the Jews, this Malchus whose ear was cut off […] Peter […] this Peter […] and this was the first denial of the Lord Jesus, because Peter said […] the Lord, and denied him. And […] the Lord Jesus [was brought] to Caiaphas the high priest; and | when he said, the Lord went before Caiaphas; and there cried the Jews […] […] this went […] this […] the Lord; and to the Lord […] of the apostles […] […] all the people against the Lord […] | and the second said: the Son of God; the third said: the king. Caiaphas said: it is written, it is good that one man should die rather than all […] […]; and […] […] the high priest […] in the house, among the apostles Christ […]

  1  Jew(ish) this Malchus ear cut_off say.
  2  Peter [...] this-Peter and-to-Lord-to-Peter and this from
  3  first denial Lord-Jézus because say Peter not* Lord and-to-Lord-to
  4  and brought* Lord-Jézus to-Caiaphas high_priest and | then-exist
  5  say to-Lord go before Caiaphas and shout
  6  Jew(ish) this-Caiaphas-+say [expedient] go this believe
  7  this half-believe Lord and to-Lord <subject_marker> from apostle-exist-exist
  8  food bread each,_every people on-Lord [...] | in_turn
  9  two say-+say say son God third say-+say king
 10  say say Caiaphas write <subject_marker> good one Lord-somebody
 11  die a)-+who rather each,_every world perish and [...] [...]
 12  apostle-high inside-?brought inside house among apostle Christ look_up leave [...]

## 039r — the second denial

> Saint Peter before the gate; and then Peter was seen by the maid at the Jews' gate. And then the maid [said] to Peter: art thou an apostle of this Jesus? Peter said […] and denied him. This was the second denial of the Lord Jesus, because Peter said […] the Lord | and denied him. And John […] […] was known to the high priest. Caiaphas said to Jesus: sayest thou the Son of God? And how dost thou truly preach? Jesus said to Caiaphas […] Caiaphas […] answered […] hear my preaching […] truly […] And then Caiaphas, this Caiaphas, and […] in the Lord […] Caiaphas […] the Lord […] the man; Caiaphas said […] the Lord […] […] to Caiaphas […]

  1  holy-Peter before ~gate and then-exist Peter exist
  2  see from-handmaid ~gate Jew(ish) and_then handmaid this-Peter
  3  apostle this Jézus say Peter this-?with and-to-Lord-to and.
  4  this two denial Lord-Jézus because say Peter not* Lord | and.
  5  to-Lord-to in_turn John inside-[?] because-exist.
  6  acquaintance this high_priest say Caiaphas to-Jézus this-Lord say
  7  son God in_turn how? this righteous(ly) preach say Jézus
  8  to-Caiaphas from-judge-Caiaphas from say Lord-to.
  9  hear preach [...] ~righteous(ly) preach.
 10  and_then Caiaphas this-Caiaphas and [...] inside Lord new
 11  Caiaphas-year but_rather* this-Lord righteously somebody say Caiaphas
 12  [?]-field Lord brought* to-+Pilate to-<preposition_of_genitive>-Caiaphas exist-exist

## 039v — before Pilate

> And this […] the two […]; and the Lord […] | Pilate; and they accused the Lord […] […] Pilate; the Lord went […] and | when he said: they have done nothing at all against the Lord. The Lord went before Pilate, because all his […] | the Lord […] and his holy face […] and | when the Lord […] said […] […] […]; no man had mercy on the Lord Jesus. And then the Lord said, and went to Pilate. And then the Jews [said] to Pilate: the Lord went […]; and the Lord […] | of the apostles […] […] all the people against the Lord […] The second said: he saith he is the Son of God. The third said:

  1  and this ~out(ward) two hour and Lord brought* | to
  2  Pilate and from Lord on-+three accuse and_then-+say
  3  he_said* Pilate go this-Lord half-believe and | then
  4  exist say many not-not on-Lord do,
  5  go Lord before Pilate because each,_every <preposition_of_genitive>-Lord [...] | on
  6  Lord from [...] and <preposition_of_genitive>-Lord holy-face each,_every [...] and | then
  7  exist Lord exist say [...] to-?again [...] <preposition_of_genitive>-somebody
  8  have_mercy Lord-Jézus and then-exist Lord exist say go
  9  to-Pilate and_then Jew(ish) this Pilate say Lord
 10  go this-Lord half-believe and Lord <subject_marker> from | apostle-exist
 11  exist food bread each,_every people on-Lord [...]
 12  in_turn-two say say say son God third say say

## 040r — the third denial, and the cock

> he saith he is king. And then Peter went to a […] […] because […] […] […] […] […] […] said one of the Jews to him: […] art thou an apostle of this Jesus? Peter said […] and denied him, and this was the third denial of the Lord Jesus; and at that moment the cock crew. And Peter said […] Peter went out: Master, he spoke, and sorrowfully […] went out. And then Pilate [said] to Jesus: sayest thou that thou art the Son of God? And how dost thou preach? The Lord Jesus said to Pilate; Pilate answered […]: hear my preaching […] […] preach. And Pilate […]; the Lord Jesus spoke

  1  king say and then-exist Peter go to-one
  2  bread [...] because exist virgin-cut_off [...] [...]
  3  want with* [...] say one Jew(ish) to
  4  with* this apostle [?]-?half-+believe this Jézus
  5  say Peter grab God this-Peter know
  6  and this three denial Lord-Jézus and time crow cock
  7  and say Peter this <subject_marker> out(ward) he_who* Peter Master
  8  speak and sad(ly) with* leave-to-leave and_then Pilate
  9  to-Jézus this Lord say son God in_turn how? this righteously
 10  preach say Lord-Jézus to-Pilate from-judge-Pilate
 11  from say and-+say Lord-to hear preach [...]
 12  righteously preach and Pilate [...] from speak Lord-Jézus

## 040v — two lines

> but the Lord said […] with his own mouth, that he is truly the Son of the living God.

  1  a) say Lord this-+Pilate <subject_marker> mouth and-Lord this-Lord
  2  righteous(ly) son living God

## 041r — art thou the king of the Jews

> And then Pilate [said] to the Lord: speakest thou, Lord, king of the Jews? The Lord Jesus said to Pilate […] Pilate's mouth […] that he is truly the Son of the living God […] Pilate […] truly this man; Pilate how […] in the Lord […]; and there cried the Jews […] the Lord. Pilate: the cross! The Lord [is] accursed, this Pilate […] would say the Lord, say […] […] truly […]. And then […] […] they took the Lord, saying; and the Lord […] Herod, Pilate's […]; and then […] […] the hour; and then the Lord […] […] king; and then, and […] upon one

  1  and_then Pilate this Lord speak Lord king Jew(ish)
  2  say Lord-Jézus this Pilate <subject_marker> [...] Pilate mouth
  3  and this-Lord righteous(ly) son living God and_then.
  4  Pilate this-Lord <subject_marker> righteous(ly) somebody this Pilate
  5  how? [...] inside Lord [...] and shout
  6  Jew(ish) condemned* Lord Pilate cross Lord cursed this
  7  Pilate this-hide_oneself want say Lord say [...]
  8  emperor righteous(ly) condemned* and_then Pilate.
  9  [...] grab Lord say and Lord brought*
 10  ~Herod <preposition_of_genitive>-Pilate ~exist-exist and then-exist ~out(ward) three.
 11  hour and then-exist Lord brought* that*
 12  king and then-exist and [?]-+say on-one

## 041v — sent to Herod, because he is of Galilee

> […] […]; and then all cried out, the four […] the Lord […] this […] the Lord […] this Jesus blasphemeth; and the Lord is out of Galilee, he cometh […]; all the people against the Lord […] And then the Lord […] many judged […] Herod the king, because […] the Jews would […] the Lord to Herod […]; and the Lord […] Herod […]; but […] shone […] Herod, the Lord Jesus Christ; and then the Lord […] before Herod the king; and the Jews cried […] Herod said: the Lord went […]; and the Lord is out of Galilee, he cometh […] all

  1  love [...] and then-exist from shout each,_every two-two direction-+day-to
  2  Lord [...] this brought* this-Lord ~begin-believe
  3  this blasphemer-Lord this Jézus and <subject_marker> Lord from Galilee
  4  protrude bread each,_every people on-Lord [...]
  5  and then-exist Lord to-?brought many judge before.
  6  Herod king because to-+Elizabeth Jew(ish) to-Lord want
  7  Herod condemned* and Lord emperor.
  8  Herod condemned* a) [...] shine see.
  9  Herod Lord-Jézus-Christ and then-exist Lord brought* before
 10  Herod king and shout Jew(ish) this.
 11  Herod say Lord go this-Lord begin-believe and Lord <subject_marker>
 12  from Galilee protrude bread each,_every

## 042r — four lines

> the people against the Lord […]; and the Lord said, the Son of God. And then the false […] said of the Lord, and […] this […] destroy | he would the Lord, that he […] all […]

  1  people on-Lord [...] and Lord say son
  2  God and_then ~false and_then-confess say Lord and
  3  man* this exist-chapter destroy | want
  4  Lord this-Lord food three each,_every afterward*

## 042v — Herod questions him

> and […] confessed it […] Herod; but […] Herod said: Lord — Herod […] God, that the Lord is the Son; and one said, spoke of the Lord Jesus against Herod; and Herod […] Herod […] Herod the king […] the Lord […] Herod […] this death […] […] the Lord […] Herod said to him, Herod said […] to Herod: the Lord of the living God […]; Herod said […] God — that he is the Son; and […] the Lord […] his Father […]. And then the Lord Jesus to Herod | that the Lord is truly the Son of the living God. The Lord Jesus said: the Lord goeth to his Father […] to judge the living and the dead; and Herod did so: he brought a stone and […]

  1  and [...] to-this confess talent Herod a) say.
  2  Herod say Lord Herod [mock] God this Lord son and
  3  one say speak Lord-Jézus ~against Herod and
  4  Herod [...] Herod [...] this-Herod king this-Herod.
  5  this-Lord can Herod [...] this die condemned* [...]
  6  this-Lord [...] Herod to say say Herod [...]
  7  to-Herod this Lord-to living God one-to say Herod [mock]
  8  God this-Lord son and not* Lord was_named*
  9  <preposition_of_genitive>-Lord father [...] and_then Lord-Jézus to-Herod | this
 10  Lord righteous(ly) son living God say Lord-Jézus this-Lord go
 11  <preposition_of_genitive>-Lord father on-[?] judge living and die
 12  and do, Herod carry stone and inside.

## 043r — Herod hoped to see a miracle

> a vessel of water, and […] various […] before the Lord Jesus; and the Lord was asked by Herod, when the Lord [stood] before him, to do a miracle; and they set a yoke before the Lord Jesus, and […] to do a miracle, because when […] before Herod he did no miracle, though the Lord took […] […] but Herod said […] the Lord […] Pilate became Herod's brother […] who […] the Lord, because […] upon the Lord, Pilate did. And the Lord […] before Pilate, many […] And this was […] the sixth hour; and the Lord […] before Pilate. And then the Jews [said to] Pilate; Pilate said

  1  one vessel water and brought* various
  2  [...] before Lord-Jézus and Lord ~ask_(for)
  3  Herod then-exist-Lord before miracle do,
  4  and yoke Lord-Jézus before and understand-eat
  5  miracle do, because then-exist [...] before
  6  Herod miracle do, why?-Lord grab Herod.
  7  condemned* a) say Herod brought* this Lord [...]
  8  Pilate to-<preposition_of_genitive>-Herod brother understand-understand-+who who
  9  [...] this-Lord because on-Lord do, Pilate
 10  and Lord brought* before Pilate many judge
 11  and this ~out(ward) six hour and Lord brought* before
 12  Pilate and_then Jew(ish) Pilate say this-Lord Pilate <subject_marker>

## 043v — the scourging

> Herod […]; and Pilate […] the Jews would the Lord. He said […] […] truly […] And then Pilate […] the soldiers; the soldiers brought him [to] Pilate, the two […] […]; and then Pilate said, bring the two […] […]; and the Lord […] the gate […] […]; and Pilate took | two two soldiers to the Lord Jesus, and the Lord was scourged; and then the two […] flogged the Lord Jesus; and a second time the Lord the second began, saying, to flog; and then the second, and the second said, […] flogged the Lord Jesus Christ; and | there came one soldier to the Lord Jesus; and then […] the Lord Jesus, because the Lord had many […]

  1  Herod condemned* in_turn-who-Lord this Pilate if want Jew(ish)
  2  Lord say [...] inscription* righteous(ly) condemned*
  3  and_then Pilate understand-eat soldier carry-soldier Pilate
  4  two [...] [...] and then-exist Pilate say carry
  5  two [...] [...] and Lord gate inside.
  6  understand-eat ~until and grab Pilate | two
  7  two soldier to Lord-Jézus and Lord exist whip and then-exist
  8  two from [pillar] flog Lord-Jézus in_turn-two Lord
  9  begin two say flog and then-exist two and from two say
 10  from [pillar] flog Lord-Jézus-Christ and | leave
 11  to-leave one soldier to Lord-Jézus and then-exist
 12  from one-+Wednesday Lord-Jézus because exist Lord many tie_up

## 044v — the purple robe and the crown of thorns

> And then the Lord […]; they bowed before the Lord Jesus; and the Lord […] […] […]; and the Lord […] […] a purple robe; and the Lord, thorns […] upon his head […] and they set the Lord upon a seat; and […] knelt before the Lord Jesus, and spoke: Hail, Jesus, this day! And […] […] […] the soldiers […] […] […] the Lord Jesus; and […] […] […] the Lord Jesus; and then the Lord […] bowed; and the Jews took the Lord, and the Jews led the Lord to Pilate, into the house.

  1  and then-exist Lord collapse bow_down Lord-Jézus and
  2  Lord [...] again* lift_up-+say and Lord [...]
  3  believe-to understand-eat purple_robe and Lord
  4  thorn crown on-head get_conceived-+say
  5  and Lord sit on-understand-eat chair and
  6  then-[?] kneel_(down) before Lord-Jézus and
  7  speak healing Jézus today-this and leave-to-leave [...]
  8  understand-eat soldier that* [...] [...] Lord-Jézus and
  9  [...] from seat [...] Lord-Jézus and then-exist
 10  Lord collapse bow_down and Lord grab Jew(ish)
 11  and Lord go Jew(ish) to Pilate inside house

## 045v — twelve legions of angels

> And the Lord sat […] in a judgment seat | in the midst […]; and then Pilate knelt before the Lord Jesus, and Pilate said: Hail, Lord, King of the Jews! And the Lord Jesus said to Pilate […] speakest thou that the Lord is King of the Jews? Because | when […] his Father God, ye took the Lord prisoner; for if the Lord would, the Lord would ask of God his Father | twelve legions of angels […] the Lord, that ye took him prisoner; because if the Lord would, the Lord could […] you all

  1  and Lord sit say inside one throne | on
  2  middle ~until and then-exist kneel_(down) Pilate
  3  before Lord-Jézus and say Pilate healing Lord king
  4  Jew(ish) and say Lord-Jézus to-Pilate this-+the_Lord
  5  speak because this-Lord king Jew(ish) because | then
  6  exist will <preposition_of_genitive>-Lord father-<suffix_of_divine_name> you
  7  Lord take_prisoner because then-exist this-Lord want Lord
  8  this-Lord ask_(for) from <preposition_of_genitive>-Lord from-father God | six
  9  six an_army in_turn angel remain* this-Lord
 10  you grab take_prisoner because then-chapter
 11  this-Lord want this-Lord you each,_every can

## 046r — Barabbas, and Behold the man

> the Lord die […]; and ye took the Lord prisoner. And Pilate said to Jesus: sayest thou, Lord, the Son of God? And one said […] the Lord Jesus said to Pilate; and he released Barabbas […] Jesus; and they beat the Lord, […] […] […] all his […] quaked; and Jesus said […] the soldier, Barabbas, truly the Lord spoke […] they beat him; the scribes spoke, it is written […]; and […] […] they beat him. O! O! And so they did to the Lord. Pilate went out of the house, and cried, Pilate: Behold Jesus, […] the King of the Jews!

  1  Lord die cross-die and you grab
  2  Lord take_prisoner and say Pilate to-Jézus this
  3  Lord say son God and one say
  4  [...] say Lord-Jézus to-Pilate and leave-chapter-leave
  5  Barabbas to-Jézus and Lord beat scourged*
  6  [...] town* [...] each,_every <preposition_of_genitive>-Lord holy-nine-+name
  7  quake and say Jézus this soldier Barabbas this righteous(ly)
  8  speak-Lord to-inside-Lord beat speak church_father
  9  write that* exist and [...] [...] beat
 10  chapter-oh chapter-oh and Lord do,
 11  Pilate out(ward) go on-house and shout-to
 12  Pilate lo Jézus Nazareth king Jew(ish)

## 046v — crucify him, the second time

> […] and the angel […] Bethlehem […] And the Jews cried: the cross for the Lord! Pilate: the Lord is accursed, […] if ye will the Lord. He said […] […] truly […]; and Pilate said to the soldiers, lead the Lord into the house. And a second time the Lord […] went into the house, and Pilate cried: Behold Jesus […] the King of the Jews! […] and the angel | [to] Bethlehem […] and […] the Jews: the cross for the Lord! Pilate: the Lord is accursed, this Pilate, if ye will the Lord. He said […] […] truly […]; and Pilate said to the soldiers, lead the Lord

  1  [Caesar] in_turn angel Bethlehem city.
  2  and shout Jew(ish) cross Lord Pilate cursed Lord
  3  this-+Pilate if want Lord say enemy <preposition_of_genitive>-+emperor
  4  righteous(ly) condemned* and say Pilate to soldier go Lord
  5  inside house and two Lord afterward* go on-house
  6  and shout Pilate lo Jézus Nazareth
  7  king Jew(ish) [Caesar] in_turn angel | to
  8  Bethlehem city and shout.
  9  Jew(ish) cross Lord Pilate cursed Lord this
 10  Pilate if want Lord say enemy <preposition_of_genitive>-+emperor
 11  righteous(ly) condemned* and say Pilate to soldier go Lord

## 047r — the third time, and Caesar

> into the house. And a third time the Lord […] went into the house, and Pilate cried: Behold Jesus […] the King of the Jews! […] and the angel [to] Bethlehem […]; and there cried the Jews: the cross for the Lord! Pilate: the Lord is accursed […] Pilate, if ye will the Lord. He said […] | Caesar truly […]. And then the Jews […] that the Lord is King of the Jews […] half […] the Lord, half […] one the Lord blasphemeth. And Pilate cried, Pilate, and how […] in the Lord […] Pilate, that he is

  1  inside-house and three Lord afterward* go on-house
  2  and shout Pilate lo Jézus Nazareth
  3  king Jew(ish) [Caesar] in_turn angel
  4  to-Bethlehem city and shout
  5  Jew(ish) cross Lord Pilate cursed Lord this.
  6  Pilate if want Lord say enemy | <preposition_of_genitive>.
  7  emperor righteous(ly) condemned* and_then Jew(ish)
  8  [...] this-Lord king Jew(ish) this-Lord.
  9  half one Lord half-believe one
 10  blasphemer-Lord and shout Pilate this Pilate
 11  and how? [...] inside Lord [...] Pilate this-Lord <subject_marker>

## 047v — Pilate washes his hands

> truly this man. And then Pilate […] water in a basin, and […] […] brought it, and […] the two […]. And then Pilate […]: I am innocent of this Lord's blood. And then the Jews, because this was […] and […] the son; and Pilate cried: whom will ye | that I release, Barabbas or Jesus? And the Jews cried: release […] Barabbas, and Jesus to the cross! And then Pilate […] the soldiers led the Lord […] into the house; and then Pilate, the Lord went […] […] into the house; and Pilate cried |

  1  righteous(ly) somebody and_then Pilate carry-+say water
  2  inside one washdish and [?]-+Pilate exist.
  3  carry and high-wash-+Pilate <preposition_of_genitive> two why?-in_turn and_then
  4  Pilate this-+Pilate innocent from <preposition_of_genitive>-Lord blood and_then
  5  Jew(ish) because this exist on-+say and <preposition_of_genitive>-+say son
  6  and shout Pilate who want | Pilate
  7  to say release Barabbas in_turn Jézus and
  8  shout Jew(ish) release Pilate Barabbas
  9  in_turn Jézus cross condemned* and_then Pilate understand-eat
 10  soldier go Lord up on-house and then-exist Pilate this-who
 11  Lord go [...] up on-house and shout Pilate | from

## 048r — the Reproaches: O my people, what have I done to thee

> […] this man truly took […] because […] the Lord […]; and the Lord […] Pilate went out of the house […] among […] […] and the Lord Jesus cried: O my people, the Lord's people, the Jews, who […] […] I loved this people […] […] the people, the Lord's, the Jews, who […] this people, through sin […] I did good to this people […] the Lord among this people did miracles. First, | this people went into Egypt […] as servants; over […] […] I divided

  1  <subject_marker> somebody righteous(ly) grab on-?condemned because <subject_marker>
  2  not_want Lord-to condemned* and Lord afterward*
  3  Pilate out(ward) go on-house down among from [...]
  4  and_then-+say and shout Lord-Jézus people-chapter
  5  <preposition_of_genitive>-Lord Jew(ish) who this-Lord he_said* afterward*
  6  to-love this-people-chapter cross* afterward* people-chapter
  7  <preposition_of_genitive>-Lord Jew(ish) who this-Lord this-people-chapter through sin
  8  [...] this-people-to good [...] then-exist-Lord this-Lord
  9  among this-people-to miracle do, first | this
 10  people-chapter go on-Egypt [...] living-servant this
 11  over sea [?]-[?]-~exist divide

## 048v — forty years in the wilderness, and a cross for their Saviour

> in two parts, this people, over the sea; through […] the Lord led them by day, and from the beginning all […] to this people, the whole wide world | I kept this people alive forty years in the wilderness, and the angel […] to this people; […] […] I did for the Lord's people, the Jews […]; they lifted up the Lord on Palm Sunday | they would make the Lord king, a crown, and […] […] his […] lifted up upon the cross; and Pilate cried […] the Lord […] and the Lord […] the Jews; and then he said

  1  on-two direction this-people-chapter over sea
  2  through struck* go-Lord day in_turn from head
  3  each,_every sky to-<preposition_of_genitive>-people-chapter ~the_whole_wide_world | this
  4  people [...] living-Lord two-two-ten-year inside field
  5  in_turn angel bread to-this-people-chapter
  6  [...] cross do, people <preposition_of_genitive>-Lord
  7  Jew(ish) he_said* to-Lord-to lift_up on-Palm_Sunday | then
  8  chapter-Lord want king crown in_turn name-high
  9  would_say* <preposition_of_genitive>-Lord body cross lift_up-to
 10  and shout Pilate grab-+say Lord blind*
 11  and Lord take* Jew(ish) and then-exist say

## 049r — the two thieves, and Mary Magdalene told

> They brought two thieves to the Lord Jesus, and set […] upon the Lord Jesus; and of the two thieves | […] […] the good one […] […] the Lord Jesus. And Saint John went up into Bethany, to Mary Magdalene: […] Master, the Lord liveth […] to Mary Magdalene […]; and he said […]; Mary Magdalene went with John […] at that time

  1  to-go say two ~thief to Lord-Jézus and put
  2  say cross on-Lord-Jézus in_turn from two ~thief | carry
  3  say who-[?] good from [...] [...] Lord-Jézus
  4  and to-go up holy-John inside Bethany to
  5  two-Mary Magdalene good [...] Master living Lord [...]
  6  to-Mary Magdalene [...] and say <subject_marker>
  7  understand-go Mary Magdalene John [...] time

## 049v — over the Cedron, and Simon carries it

> The Lord went, he said, to the Cedron; and then the Lord went over the Cedron; and then down […] […] the Lord Jesus; and […] | […] the Lord Jesus […]; and the Jews knelt before the Lord Jesus, and […] Hail, Jesus! […] And there came to the Lord | the Virgin Mary; and Simon carried it for the Lord; and | when the Jews […] within […] and […] […] upon the earth, and […] believed in the Lord Jesus […] […] […] the Lord […] the Lord Jesus, and

  1  go this-Lord say exist Cedron and then-exist go Lord
  2  say over-exist Cedron and then-exist
  3  to-down [...] [...] Lord-Jézus and collapse | from
  4  fall_down Lord-Jézus to-+cross and kneel_(down) Jew(ish)
  5  before Lord-Jézus and speak-+say healing
  6  Jézus Nazareth and leave-to-leave to-Lord | virgin
  7  Mary and Lord Simon cross carry and | then
  8  exist Jew(ish) [?]-+cross-[?] inside chapter-+Paradise
  9  and put-+say cross on-earth and
 10  take_off believe on-Lord-Jézus food [...]
 11  [...] Lord take_off-+say Lord-Jézus and

## 050r — laid upon the cross

> the Virgin Mary came to the Lord Jesus; and | […] […] his bonds. And then the Lord Jesus […] his […] said, […] […] this, in the commandment […] his apostles; and the Jews saw […] the whole wide world To his passion the Lord went; and […] said, in the Lord believed; and they laid the Lord upon the cross, and the Lord […] one […] and the two […] the cross, and could […] and […] […] and […] […]; and his feet could

  1  leave-to-leave virgin-Mary to-Lord-Jézus and | from
  2  [...] <preposition_of_genitive>-exist-?first <preposition_of_genitive>-Lord handcuffs and_then
  3  Lord-Jézus name-[?]-~exist <preposition_of_genitive>-Lord have say
  4  trespass [...] this inside commandment this apostle-+one <preposition_of_genitive>-Lord apostle
  5  and see Jew(ish) [...] good the_whole_wide_world
  6  on-suffering-year go Lord and [...] say inside
  7  Lord believe and to-Lord place_onto cross
  8  and Lord this-pierce-+say one why?-in_turn
  9  and two [...] cross and can
 10  take* and why?-in_turn chain-draw-+say
 11  and why?-in_turn pierce-+say and <preposition_of_genitive>-Lord foot can

## 050v — the title, and the ninth hour

> […] and the feet […] and they pierced the feet; and all his […]; and | the Lord […] in the Lord […] in the Lord Jesus Christ. And Pilate wrote upon a tablet: Jesus […] King of the Jews. And then the Jews: write that the Lord said he is King of the Jews. But the Lord's writing, Jesus […]. And then Pilate: what I have written Pilate has written. And the two thieves; with the Lord they nailed them to the cross, and the Lord among the two thieves […] […]. And this was at the ninth hour. And then the Lord Jesus on the cross prayed to God his Father […]

  1  take* ~and foot chain-draw-+say
  2  and foot pierce and each,_every <preposition_of_genitive>-Lord [...] and | <preposition_of_genitive>
  3  Lord [...] inside Lord to-°trench-to-°trench inside Lord-Jézus-Christ
  4  and write Pilate on-one tablet Jézus
  5  Nazareth king Jew(ish) and_then Jew(ish)
  6  write Lord king Jew(ish) a) Lord write
  7  Jézus Nazareth and_then Pilate write <subject_marker>
  8  who ~Pilate write and two ~thief to-Lord pierce
  9  cross and Lord among two ~thief one-[?]
 10  say and this out(ward) nine hour and_then Lord-Jézus
 11  cross from-father <preposition_of_genitive>-Lord God eternal* ask_(for)-Lord

## 051v — three nails, and the sponge on a stick

> […] Mary's […]; but his three nails, long, with which they nailed the Lord to the cross. And then the Lord Jesus […] the Lord; and | the Lord's apostles, when they bought […] sweet, and wine; the apostles took […] the Jews' chief; and the Lord […]; but […] […] and the Lord | took […] vinegar; and […]; and the Lord, they took wine upon a sponge on a stick, and held the sponge to the Lord's face […]; and the wine […] his mouth […] […]. And then | the Lord Jesus upon the cross [prayed to] God his Father in heaven […] […] his Father […] into his Father's hands.

  1  remain* <preposition_of_genitive>-Mary woe a) <preposition_of_genitive>-Lord three_nails long this-who
  2  this-Lord pierce to-cross and_then Lord-Jézus thirst Lord and | <preposition_of_genitive>
  3  Lord apostle then-exist buy exist-nine sweet and
  4  wine grab apostle Jew(ish) head and
  5  Lord grab-+who a) say-to pine in_turn Lord | grab
  6  say vinegar and [hyssop] and Lord
  7  wine grab say on-one sponge_(hyssop?)_on_a_stick and
  8  then-exist-Lord sponge face wipe_off-+say and wine
  9  grab mouth little on-+pine and_then | Lord
 10  Jézus cross from-father <preposition_of_genitive>-Lord God heaven offer
 11  this-Lord this-father <preposition_of_genitive>-Lord commend* inside <preposition_of_genitive>-father-<suffix_of_divine_name>

## 052r — two lines

> […] and […] to the Lord Jesus, his […] […] Here ends […] […] […] the Passion of the Lord Jesus.

  1  why?-in_turn and from to-Lord-Jézus <preposition_of_genitive>-Lord commend* give_up_the_ghost
  2  end this the_account* Passion evangelist* suffering Lord-Jézus

## 052v — the earthquake, and Longinus

> And then the Lord Jesus, his […] […] upon the cross; the earth quaked, the rocks and the stones […]; the sun and the moon were darkened; and all […] […] humbled themselves; and all creation mourned, when Christ the Lord was crucified. And there came one soldier from Jerusalem, blind; and that soldier was Longinus; and the Jews' spear pierced the Lord Jesus Christ; and […] the spear […] the Lord Jesus Christ; and the soldier, the blood splashed from the Lord Jesus upon his eyes, and through it he saw, and the soldier was healed; and the soldier believed in the Lord Jesus Christ, and the soldier was baptized, and saw […]

  1  and then-exist Lord-Jézus <preposition_of_genitive>-Lord commend* give_up_the_ghost cross earth
  2  quake rock stone rent sun and moon
  3  this eclipse and each,_every creatures* among_the_people* this humble ~and each,_every
  4  create mourn then-exist Christ crucified Lord and go say.
  5  one soldier on-Jerusalem blind and was_named* soldier
  6  exist Longinus_<the_centurion,_who_pierced_Jesus’_side_on_the_cross> and pierce Jew(ish) spear ~exist-from-in_turn
  7  Lord-Jézus-Christ and can [...] spear on
  8  ~exist-from-in_turn Lord-Jézus-Christ how? soldier [...] splash
  9  to-to-to Lord-Jézus on-place through see and healing soldier
 10  leave and grab soldier believe Lord-Jézus-Christ
 11  and soldier see-baptize and see and_then-+say

## 053r — after the ninth hour

> […] the Lord Jesus Christ; and […] believed in the Lord, but many judged […] […] home. And the second said sorrowfully, accusing, because […] […] he said […] they crucified, saying, the Son of God; and sorrowfully they went, saying […] home; and this […] was the ninth hour, and four hours from that hour the Lord Jesus suffered upon the cross […] […] all […] home from […] […] and the apostles […] went, every one of the apostles […] | […] and one, and […]

  1  can Lord-Jézus-Christ and [...] inside Lord believe
  2  a) many judge brought* [?]-+say home
  3  in_turn-two say sad(ly) accuse because [...] [...]
  4  say that* ~execute say son God and
  5  sad(ly) go say [?]-+say home and this
  6  [...] out(ward) nine ~hour and two-two from ~hour
  7  cross suffer Lord-Jézus and-+say go-?brought
  8  each,_every [?]-?and_then home from [...] [...]
  9  in_turn apostle exist apart go-go each,_every to-apostle [...] | on
 10  Galilee and one and understand-eat

## 053v — Joseph and Nicodemus ask for the body

> the apostles […]; and then two […] Jerusalem, and […] was […]; and the second Nicodemus; and then the two asked of Pilate […] the Lord Jesus; and […] the two, the sufferer […] the Lord Jesus; and then the two went […] Christ was […]; and the two went […] many Jews; and the two were, that is, good and merciful men; and then the two saw the Virgin Mary, and […] Magdalene. Many people went out of Jerusalem, and were afraid, because the Jews would […] the Lord, all […] because

  1  apostle cut_off and then-exist two somebody-have_mercy Jerusalem one-+one
  2  and was_named* exist Joseph in_turn-two
  3  ~Nicodemus and then-exist two ask_(for) from Pilate
  4  exist-[?] Lord-Jézus and have two sufferer
  5  exist-[?] Lord-Jézus and then-exist two go [...]
  6  exist Christ condemned* and go to two
  7  many Jew(ish) and two people that_is good people have_mercy
  8  and then-exist two see virgin-Mary and Mary.
  9  Magdalene go many people on-Jerusalem and ~through
 10  startle because to Lord want Jew(ish) each,_every Lord [...] because

## 054r — taken down, and the tomb sealed

> this was […] | and […] went […] […] because Mary was […] fled […] the Jews; and in that place were these people, when the two Marys went to the people, and took Nicodemus the Lord Jesus from the cross, and the three nails, […] Saint John took […] saw | the Virgin Mary […] took the Virgin Mary into […] and […] Nicodemus, with his servants' […]; and the two covered the body, and […] […]; and Nicodemus laid the Lord Jesus within, and they closed the Lord within the tomb; and there stood, he said, four soldiers by the Lord […] […] the chief of Jerusalem; and […] went […]. Here ends this holy gospel.

  1  this exist from | and [...] go down [...]
  2  because exist-Mary on-+mount escape before.
  3  Jew(ish) and on-place exist this people then-exist
  4  from two-Mary to-people go-two-Mary and grab
  5  ~Nicodemus cross was_named* Lord-Jézus in_turn three three_nails
  6  seal-to grab holy-John then-+mouth-Mary see | virgin
  7  Mary then-~exist grab virgin-Mary inside bosom
  8  ~and afterward* Nicodemus <preposition_of_genitive>-living-servant
  9  [...] and cover two body and then-~exist [...] and
 10  inside-put Nicodemus name-end-to Lord-Jézus and
 11  Lord inside burial_chamber close and leave seal* say to-Lord two-two soldier from*
 12  were_opened* Jerusalem head ~and [...] go [...] end this
 13  holy-gospel

## 054v — a rubric, naming Mark

> Here begins this holy gospel, written by Saint Mark.

  1  begins this holy-gospel write holy-Mark

## 055r — the three women at the tomb

> in the […] chapter of his writing: at that time, when they went […] […] to the tomb of Christ, because they had prepared […] […] […] […] Jesus: Mary Salome, and Mary the mother of James, and Mary Magdalene. And then these Marys […] these Marys among […] […] […] the stone from the tomb; and then | Mary came to the tomb of Christ, and saw […] […] the tomb […]; and then […] within this […] and they went in […] and […] saw […] Jesus; but they saw one

  1  inside seven chapter-leave <preposition_of_genitive>-write time then-exist
  2  go the_three_Marys [...] burial_chamber Christ because-exist prepare
  3  [spices] another this-cut_off [...] exist-[?] Jézus
  4  Mary Salome and Mary James mother and
  5  Mary Magdalene and then-exist this-two-Mary [...] this-two-Mary
  6  among [...] among-Mary-+the_three_Marys-[?]-+one-Mary
  7  from-?again from stone on-burial_chamber and then-exist | keep_going-+three
  8  Mary to-burial_chamber Christ and see the_three_Marys [...]
  9  <subject_marker> burial_chamber from [...] and then-exist the_three_Marys inside this
 10  the_three_Marys and inside-to-go the_three_Marys and
 11  remain* see exist-[?] Jézus a) see one

## 055v — be not afraid, he is risen

> angel, sitting on the left side, from […] within […] […] Jesus. And then Mary, through was afraid, because Mary […] as a ghost. And then the angel: be not […] […] […] be not afraid. He is risen, whom ye mourn — the Lord Jesus, whom they crucified, is risen […]; but […] within […] and […] his apostles, and Peter […]. Here ends this holy gospel. And […] these women went […] from the tomb of Christ; and | Mary Magdalene went back to the tomb of Christ. At that time

  1  angel sit on-left_(side) direction from [...] inside exist
  2  cover exist-[?] Jézus and then-exist Mary through
  3  startle because rather-Mary supposed* <subject_marker> how? ghost
  4  and_then angel do_not have-+the_three_Marys [...]
  5  the_three_Marys through startle rise mourn to-Lord from Jézus
  6  execute rise seek* a) go-+the_three_Marys
  7  inside Galilee and say-+the_three_Marys
  8  <preposition_of_genitive>-Lord apostle and Peter say-+the_three_Marys end this
  9  holy-gospel and [?]-+the_three_Marys go this woman
 10  head from this burial_chamber Christ and | return
 11  return back Mary Magdalene to-burial_chamber Christ time

## 056r — Mary Magdalene takes him for the gardener

> the Lord Jesus appeared to Mary Magdalene in the form of a gardener. And then this gardener, the Lord Jesus Christ, | [said to] this woman: why […] woman, weepest thou for the Lord? He, Jesus, whom they crucified, is risen, because […] said […] […] […] light […] […] […] the tomb pierced, and the tomb light […]; and […] […] is risen. And the Lord Jesus stood before Mary Magdalene in that place; Mary […] […] […] Master! And the Lord […] to Mary: go to the apostles. And Mary went to these two sisters, the women,

  1  appear Lord-Jézus Mary Magdalene inside shape,_form from one
  2  gardener and_then this gardener-Lord-Jézus-Christ | this
  3  woman who-shore [...] woman mourn to-Lord this from
  4  Jézus execute rise seek* because
  5  say son-before [...] see-[?] light on-+heaven
  6  town-chapter-in_turn stooped_down* burial_chamber pierce and burial_chamber <subject_marker>
  7  light from-gate and verily can that rise
  8  and leave Lord-Jézus before Mary Magdalene
  9  on-to-place Mary [...] on-reason that
 10  this-Lord Master and Lord <subject_marker> to-Mary-apostle go-Lord-apostle
 11  and go-Mary to this two sister wife

## 056v — two lines

> and then Mary went with these women, and Mary would tell […]

  1  and then-exist Mary understand-go-Mary this woman
  2  and want say Mary from

## 057r — he stands among them

> Magdalene saw the Master in the form of a gardener. At that time the Lord Jesus Christ stood in the midst, living, among the three Marys, the Lord, among these sisters of Jerusalem. And then the Lord Jesus [gave] the commandment of God among you: his mercy to whoever believes in the Lord, and in his Father God […] O! Amen. And then the Lord Jesus the three Marys; Mary saw within the tomb […] […] Jesus whom they crucified; and Mary Magdalene said […] Mary saw the Lord risen from the dead; and the Lord Jesus Christ stood among the three Marys […] the apostles. This holy gospel.

  1  Magdalene see-Magdalene Master inside image from gardener
  2  time leave Lord-Jézus-Christ middle living
  3  among the_three_Marys Lord among this sister
  4  Jerusalem and_then Lord-Jézus commandment God among
  5  you <preposition_of_genitive>-Lord have_mercy somebody to and believe
  6  inside Lord and inside <preposition_of_genitive>-Lord from father-<suffix_of_divine_name> chapter-oh.
  7  chapter-oh amen and_then Lord-Jézus <subject_marker>
  8  the_three_Marys see-Mary inside burial_chamber brother-chapter
  9  from Jézus execute and say Mary Magdalene that*
 10  Lord-Mary see-Mary rise on-die and
 11  leave Lord-Jézus-Christ among the_three_Marys this apostle holy-gospel

## 057v — an Old Testament prophecy, and Mark again

> Written by Saint […] the prophet, the prophet, in the Old Testament, truly, the sixth chapter of his writing, and Saint Mark […] it is written. Said Saint […] the prophet: because he saith […] it is found, in the Old Testament is truly written this word: the Lord shall rise from the dead. The King — thanks to the Lord […]; and the Lord Christ destroyed the evil one; and […] […] the evil one […] Lucifer. This is written | Saint Mark, in the […] chapter of his writing: when the Lord Christ upon the cross breathed out his soul, the earth quaked, the rocks and stones […]; the sun and the moon

  1  write holy-<name_of_a_prophet>
  2  prophet <pertaining_to_the_Old_Testament> righteous(ly)
  3  six chapter-leave <preposition_of_genitive>-write
  4  in_turn holy-Mark seven
  5  write say holy-<name_of_a_prophet>
  6  because say <subject_marker> exist find
  7  inside <pertaining_to_the_Old_Testament> righteous(ly) write this word stand_up-Lord on-die-Lord
  8  king to-Lord thanks [...] and destroy Lord ~evil Christ and from
  9  [...] [...] ~evil can hide_oneself-angel this_is write | to
 10  holy-Mark inside seven chapter-leave <preposition_of_genitive>-write then-exist Lord
 11  Christ cross <preposition_of_genitive>-Lord soul breathe_out earth quake
 12  rock stone this rend sun and moon this

## 058r — the harrowing of hell

> were darkened; and all […] […] humbled themselves; and all creation mourned when Christ was crucified. And four hours the Lord Jesus suffered upon the cross; and the Lord within the tomb | the apostles laid him, […] and then they laid the Lord within the tomb; and at that hour there came from God the Father in heaven, from the Father, an angel into […] the Lord Jesus; and […] […] and the angel within the tomb […] and the Lord went […], and destroyed the evil one; and […] the people who died within a hundred years, and within | five […] and within […] and […] all the prophets went into hell; and […] three souls, all […] the Lord went, and the three souls within the evil one's […] the Lord |

  1  eclipse and each,_every creatures* into_the_world* this humble and each,_every create mourn
  2  then-exist Christ crucified and two-two hour
  3  cross suffer Lord-Jézus and Lord inside burial_chamber | put-apostle
  4  Mary-angel and then-exist-Lord inside burial_chamber lay Lord and
  5  hour time go from-father God heaven
  6  on-<preposition_of_genitive>-father angel inside exist-[?] Lord-Jézus and
  7  rise* from [?]-+day in_turn angel inside burial_chamber stay
  8  in_turn to-Lord go-Lord on-~evil and ~evil destroy and he_who*
  9  people die inside one hundred-year and inside | five
 10  sit-+day and inside nine-[?] and nine-+day each,_every prophet
 11  go on-netherworld and [...] three soul each,_every out go Lord
 12  in_turn three soul inside ~evil stay Lord | speak.

## 058v — Adam's soul kneels to the Virgin

> Saint Augustine the doctor: within many years, and one soul […] went into the […] land; but when the Lord went to the souls, the Lord, and […] three souls […] […] the Lord went to the souls; and the Lord appeared to the blessed Virgin Mary; and Adam's soul knelt before the blessed Virgin Mary; and the maiden […] prayed; and blessed the blessed Virgin Mary; and all the souls stood before the blessed Virgin Mary; and within […] the souls, the Lord, the souls; and the Lord went to the souls; and then twenty-five(?) hours; and this was […] the sixth hour.

  1  holy-Augustine-church_father inside many-to-year and one soul [...]
  2  ~go inside eternal* land a) then-exist to-Lord
  3  to-soul-soul-soul-soul-soul go Lord and [...] three soul
  4  [...] out to-go Lord soul and Lord appear Lord
  5  to-happy virgin-Mary and kneel_(down) ~Adam soul
  6  before to-happy virgin-Mary and girl <subject_marker>-have_mercy
  7  ask_(for) and bless-year to-happy virgin-Mary
  8  and to-soul-soul-soul each,_every leave before to-happy
  9  virgin-Mary and inside Paradise soul Lord soul
 10  and go Lord soul and then-exist two-ten-ten five
 11  hour and this out(ward) thirty-[?] six hour

## 059r — one line

> And on the third day the Lord Jesus Christ rose from the dead.

  1  to-and on_the_third_day from die stand_up Lord-Jézus-Christ

## 059v — the road to Emmaus

> Here begins this holy gospel, written by Saint Luke, in the first [chapter] of his writing: at that time, when there went two apostles out of Jerusalem into a […] and | […] was Emmaus; and then the two apostles […] of the living Lord Jesus; and then the two spoke of how the Lord was truly a man, truly the Lord, preaching, and many miracles he did […]; the two apostles; the Jews' chief crucified him. At that time there appeared to the two apostles the Lord Jesus, in the form of a traveller; and then

  1  begins this holy-gospel
  2  write holy-Luke one
  3  <preposition_of_genitive>-write time
  4  then-exist go two
  5  apostle Jerusalem inside one
  6  in_turn-chapter-in_turn and | exist-chapter
  7  day-+name exist Emmaus and then-exist to-high-two-apostle from living
  8  Lord-Jézus and then-exist two speak how?-Lord this-Lord
  9  exist righteous(ly) somebody righteous(ly) Lord ~preach who-and-this-and
 10  miracle do, [...] <preposition_of_genitive>-two-apostle Jew(ish)
 11  head execute time appear
 12  two-apostle Lord-Jézus shape,_form traveller and then-exist

## 060r — the Lord asks the two what they are speaking of

> The two apostles […] Lord Jesus, and the two apostles began to talk, and the Lord spoke from among them; and then Lord Jesus: O my two apostles, are you not saying, two apostles, Lord, how, saying among […] have, two apostles, because they said the Lord Jesus Christ apostle […] the two men spoke of the Lord, this Lord, the two Lord's apostles; the third Lord; and then Luke this […] the way, the man, this Lord, this good […] […] how […] the miracles in Jerusalem afterwards, and how the man […] said, the chief truly crucified this Jesus; and the Lord came into the world, went went preaching, and this and that miracle he did

  1  two-apostle [drew_near] Lord-Jézus and two-apostle (begin_to)_talk and
  2  Lord from-speak and_then Lord-Jézus oh <preposition_of_genitive>-Lord
  3  two-apostle exist-~exist say two-apostle Lord how? say ~among
  4  [...] have two-apostle because say exist Lord-Jézus-Christ
  5  apostle that* two somebody from-Lord speak this-Lord two
  6  Lord apostle three Lord and_then Luke this [...]
  7  way somebody this Lord this good remain* [...]
  8  how? [...] <subject_marker> miracle Jerusalem afterward* how?-to
  9  somebody [?]-+say head righteous(ly)
 10  execute this Jézus and the_Lord into_the_world* go-Lord
 11  go-+<subject_marker> preach-[?] who-and-this-and miracle do,

## 060v — the miracles, and the women's news they did not believe

> the blind, through him light; the dead, through him […] […] […] the body, and the evil, those possessed by the evil one, healed and the Lord […] was from […] […] he rose, and one said, the one baptized, the Baptist, the chief the news was of the Lord […] he rose; the news the two apostles […] believed, who from the Lord, from the dead rose; because he is the Lord's, to the brethren […] this pleasing, and who from the Lord, from the dead rose; and then Lord Jesus […] the two […] the man, to hide, the two believing

  1  eye-eye ~blind <subject_marker> through light die <subject_marker> resurrect | lame
  2  lame body and evil obsessed_by_the_evil from-healing
  3  and Lord <subject_marker> exist from [...] up
  4  stand_up-Lord and say one [?]-+the_Baptist/woman ~head
  5  news exist-Lord up stand_up-Lord news two
  6  apostle [...] believe who from Lord from die
  7  stand_up-Lord because he_is* <preposition_of_genitive>-Lord brother-to
  8  rot this pleasing who from Lord from
  9  die stand_up and_then Lord-Jézus you two
 10  ~exist-+baptize-to-+humble somebody to-hide_oneself believe-two

## 061r — O fools and slow of heart, and Cleopas is named

> Is it that these, to him, rise from the […] And then Lord Jesus left; the Son of God died more than these, rise from the, from the the Lord, from the eternal Father, and began, through Lord Jesus expounded from Adam, the trespass, written said; and then Cleopas, Luke, this Lord, to the two […] the Lord wished good, said; and then Lord Jesus from […] […] signified this Jesus crucified, how, in turn […] died, the brother's […] and this Jesus died, the Lord's brother; and then Lord Jesus, the trespass […]

  1  is_he-two this to-+<subject_marker> rise* from as*
  2  and_then Lord-Jézus leave exist die son God
  3  more_than_these* rise* from as* from as*
  4  the_Lord from father-<suffix_of_divine_name> eternal* and begin through
  5  explain Lord-Jézus from ~Adam ~trespass write
  6  say and_then Cleopas Luke this Lord to-two [...]
  7  want-Lord good say and_then Lord-Jézus from Abel
  8  Abel symbolize this Jézus execute how? | in_turn
  9  [...] die <preposition_of_genitive>-brother he_said* and this Jézus
 10  die <preposition_of_genitive>-Lord brother and_then Lord-Jézus trespass Noah

## 061v — Abraham as the figure of the crucifixion

> […] signified this Jesus crucified, he is […] redeemed every people in […] this […] and on this Jesus crucified, saved every one, Adam gained; and then Lord Jesus, above; Abraham — Abraham's [deed] signified this Jesus crucified, and Lord Jesus said, said the Lord. Abraham, to the Lord's angel — Abraham gave his son […] and the Lord […] […] who did, Abraham on […] the faggots […] in turn Abraham took […] who […] wished to slay

  1  go_up-+day-why? symbolize this Jézus execute he_is* go_up-+gate/open-why?
  2  redeem each,_every people* inside [...] this [...] and on-this Jézus
  3  execute be_saved each,_every ~Adam gain and_then
  4  Lord-Jézus trespass Abraham Abraham symbolize this
  5  Jézus execute and say Lord-Jézus say exist Lord-<suffix_of_divine_name>.
  6  Abraham on-~angel <preposition_of_genitive>-Lord-<suffix_of_divine_name> Abraham grab
  7  <preposition_of_genitive>-son Isaac and Lord sacrifice.
  8  on-to-+offering who do, Abraham on
  9  tie_up faggot on-+Isaac in_turn Abraham
 10  grab sword who Isaac want slay

## 062r — the mount, the ram, and the angel

> And then he went on this, to the mount […] wished […] and then […] O my father […] and went far […] and a, and the ram, and a […] the young men […] father […] and said from father Abraham, from the brethren, the Lord […] […] and then […] […] of […] living, the Lord wished to slay, and the Lord cried […] to the angel […] Abraham, to the whole wide world, the Lord's love, this is

  1  and then-exist go on-this to-mount [?]-+Isaac
  2  want sacrifice and_then Isaac oh
  3  <preposition_of_genitive>-father donkey* and go far
  4  to_whom-+one and one and sheep and one
  5  lamb brethren* Isaac father sacrifice and say
  6  from-father Abraham from brethren* Lord-<suffix_of_divine_name> ox.*
  7  offering and then-exist tie_up bundle_of_wood*
  8  <preposition_of_genitive> Isaac [?]-living want Lord slay and
  9  shout Lord-<suffix_of_divine_name> in_the_cloud on-angel go_away
 10  Abraham to-the_whole_wide_world <subject_marker> Lord <preposition_of_genitive> love this_is

## 062v — he made as though he would go further, and they constrained him

> Lord […] and then Lord Jesus, he is, was […] as he gave his father's [son], so this Jesus was crucified the Lord gave, his divine Father, and he rose the Lord from the […] because the Lord from the […] from the Father, eternal God; and then the Lord's apostles went, this in turn and then Lord Jesus went, the two apostles, you, because this Lord the Lord had a long way; and the Lord began, the two apostles persuaded; and then the Lord was, the two apostles persuaded, and the two the Lord's apostles went, and then the Lord's two apostles into the room went the Lord's two apostles, and the two apostles sat the Lord at the table, and

  1  Lord peace and_then Lord-Jézus he_is* exist Isaac
  2  to-grab <preposition_of_genitive> father this and this Jézus execute exist
  3  to-grab-Lord <preposition_of_genitive>-Lord father-<suffix_of_divine_name> and <subject_marker> rise*
  4  Lord from [?]-+day because-+the_Lord from [?]-+day from-father
  5  God eternal* and then-exist go-apostle-Lord this in_turn-chapter-in_turn
  6  and_then Lord-Jézus go-two-apostle you because this-Lord
  7  have-Lord long way and Lord begin two apostle
  8  persuade and then-exist-Lord exist two-apostle persuade and | two
  9  apostle-Lord go and then-exist two-apostle-Lord on-+room | go
 10  two-apostle-Lord and sit-two-Lord-apostle to-throne and

## 063r — the breaking of bread, and he vanished out of their sight

> the two apostles carried […] water and wine. Lord Jesus took one […] and […] […] this, how, then […] […] and from […] today's, and wine, and the cloud Lord Jesus blessed; and then the two apostles ate, the two apostles, and the two apostles drank, in the place, to the two apostles in the Holy Spirit, the farm, truly the Son of God to Lord Jesus; the two apostles, he left them, and […] among the two apostles, Lord Jesus Christ, the chapter answered to the Lord […] the two apostles saw. Here ends this holy gospel.

  1  carry apostle two cup ~water and wine and.
  2  grab Lord-Jézus one cup and cup
  3  [...] this how? then-exist [...] [...]
  4  and from bread and wine and cloud
  5  bless Lord-Jézus and then-exist two apostle | eat-two
  6  apostle and drink-two-apostle on-place to-two-apostle
  7  on-spirit holy-farm <subject_marker> righteous(ly) son God
  8  to Lord-Jézus two apostle <preposition_of_genitive>-to-leave-this and
  9  go_away among two apostle Lord-Jézus-Christ chapter-?answered
 10  Lord-to [vanished] see-two-apostle end this holy-gospel

## 063v — Thomas was not with them

> Here begins this holy gospel written by holy John in the twentieth chapter of his writing. At that time the apostles were found in Jerusalem in […] house, six in the Lord's house, where the Lord Lord Jesus, after supper; and then holy Thomas went […] one Saturday evening, to the apostles; and the apostles said, Thomas, apostle, we have seen the Lord. And holy Thomas said, I do not believe this at all; unless I hide this, unless Thomas believes […] not, unless he sees Thomas the Lord's end, and unless Thomas puts his finger in […]

  1  begins this holy-gospel
  2  write holy-John
  3  inside two-ten-ten chapter-leave
  4  <preposition_of_genitive>-write time
  5  ~find apostle inside Jerusalem
  6  inside one house six
  7  inside Lord house where Lord-<suffix_of_divine_name>
  8  Lord-Jézus dinner afterward* and then-exist go holy-Thomas Didymus*
  9  one Saturday evening to-apostle and say-apostle Thomas apostle
 10  see Lord and say holy-Thomas this-Thomas this not believe
 11  each,_every this this-hide_oneself this-Thomas this believe if not | see
 12  Thomas <preposition_of_genitive>-Lord end and <preposition_of_genitive>-Thomas finger not put inside | <preposition_of_genitive>

## 009r — reach hither thy finger, and my Lord and my God

> the Lord's end, who from the Lord, rose from the dead; at that time Lord Jesus Christ left into the midst of the apostles […] and said, you have the commandment, and judge; he left the apostles in turn; Thomas began […] and Lord Jesus said, Thomas, thou shalt go to put thy finger, Thomas, into the Lord's wound […] see and believe; and […] Lord Jesus, the Lord's wound and Lord Jesus said, Thomas, blessed are they, and the man who sees and believes […] and blessed are they, and the food he sees […] believe. Here ends this holy gospel. And he kneeled, holy Thomas, before Lord Jesus, and holy Thomas said, Lord, Thomas's God; Thomas asked this of the Lord, have mercy on Thomas, who through sin against this Lord

  1  Lord end who from Lord from die stand_up time leave Lord-Jézus-Christ
  2  middle apostle closed and say commandment you exist and judge leave
  3  apostle in_turn Thomas begin have and say Lord-Jézus Thomas
  4  go-+name to put <preposition_of_genitive>-Thomas finger inside <preposition_of_genitive>-Lord wound
  5  [...] see believe and [...] Lord-Jézus <preposition_of_genitive>-Lord wound
  6  and say Lord-Jézus Thomas happy-to from and somebody see
  7  and believe but and happy-to from and food see
  8  from* believe end this holy-gospel and kneel_(down)
  9  holy-Thomas before Lord-Jézus and say holy-Thomas Lord
 10  <preposition_of_genitive>-Thomas God <preposition_of_genitive>-Thomas ask_(for)-Thomas this-Lord-<suffix_of_divine_name>
 11  have_mercy Thomas who this-Thomas through sin against this-Lord-<suffix_of_divine_name>

## 009v — Thomas blesses him, and the Good Shepherd begins

> Thomas, this Lord, Thomas believed […] this Lord truly the Son of the living God. And then Thomas blessed Lord Jesus Christ. And have mercy on Thomas's sin. And Lord Jesus said, every […] and […] […] from […] believing in Lord Jesus Christ, every gentile man and Jew […] have mercy on sin. Here ends this apostle's holy gospel; blessed be the Lord. Here ends this holy gospel. Written by holy John in the tenth chapter of his writing. At that time Lord Jesus said […] supper, apostles, to his Lord, this good Lord, before the son, in turn, you, from the apostles

  1  this-Thomas this-Lord believe-Thomas remain* this-Lord righteous(ly)
  2  son living God and then-exist Thomas exist bless Lord-Jézus-Christ.
  3  and sin Thomas have_mercy and say Lord-Jézus each,_every [...] and [...] [...] from
  4  [...] on-believe to-Lord-Jézus-Christ each,_every of_an_alien_nation,_pagan somebody Jew(ish)
  5  above-pagan sin have_mercy end this apostle holy-gospel on-Lord-<suffix_of_divine_name> bless
  6  end this holy-gospel
  7  write holy-John
  8  inside ten chapter <preposition_of_genitive>-write
  9  time say Lord-Jézus
 10  on-who-+who-to dinner apostle
 11  <preposition_of_genitive>-Lord this-Lord good son-before in_turn you from apostle

## 064r — the good shepherd and the hireling

> his sheep, and the Lord knows his sheep, and this Lord knows his sheep. And then Lord Jesus: then there was a king, and then he had two shepherds, one who kept the house well, a shepherd; the other in turn a hired shepherd. And then, of the two shepherds […] from one herd of sheep of this king; and then came the wolf to this sheep, and would carry this sheep away and this hired shepherd, of the shepherds […] this sheep; in turn the good shepherd, of the house, of the shepherds redeemed this sheep, and made the sheep ready in the herd and took it into the good keeping, and one carried away, and

  1  <preposition_of_genitive>-Lord sheep and Lord ~know <preposition_of_genitive>-Lord sheep and
  2  this-Lord ~know <preposition_of_genitive>-Lord sheep and_then Lord-Jézus | then
  3  exist one king and then-exist ~have two sons*
  4  one ~who home good sons* in_turn-two farm_hand
  5  sons* and then-exist from two sons* chapter-[?] from one
  6  herd sheep this king and then-exist go wolf
  7  this sheep and want this sheep from-~carry
  8  and this farm_hand sons* from sons* leave
  9  this sheep/a_female_person in_turn-this good sons* home from sons*
 10  redeem this sheep/a_female_person and sheep/a_female_person prepare inside herd
 11  and inside-good-exist-to grab and one from-~carry and

## 064v — the good shepherd giveth his life, and other sheep I have

> in turn who […] […] this herd, and went. The wolf, and the sheep carried away; and then Lord Jesus: he who is the good shepherd, of the shepherds, lays down his […] for his sheep; and the Lord takes and one […] he who is the good shepherd, of the shepherds, is the gate of his sheep; and then they hear the voice of the Lord; the sheep […] the shepherd go; and then Lord Jesus, his apostles, one creature […] one sheep and these sheep I will bring to you […] and go you shall be every one, one shepherd, shepherds one; thanks to the Lord. Here ends this holy gospel.

  1  in_turn-who rebuke-trespass out this herd and go.
  2  wolf and sheep from-~carry and_then
  3  Lord-Jézus to-+he_who good sons* from sons* put
  4  down <preposition_of_genitive>-Lord living to-<preposition_of_genitive>-Lord sheep/a_female_person and grab-Lord
  5  and one [...] he_who good sons* from sons*
  6  <subject_marker> ~gate <preposition_of_genitive>-Lord sheep and then-exist hear
  7  voice,_sound <preposition_of_genitive>-Lord-<suffix_of_divine_name> sheep blind-Lord sons* go and_then
  8  Lord-Jézus apostle <preposition_of_genitive>-Lord creature-+one [...] one sheep/a_female_person
  9  and this-sheep want to-you blind* go and
 10  you exist each,_every one sons* sons*
 11  one to-Lord thanks Lord-<suffix_of_divine_name> end this holy-gospel

## 065r — beware of false prophets

> Here ends this holy gospel. Written by holy Matthew in the last of his writing. At that time, then the chapter of the day of Lord Jesus Christ, thirty, three days. At that time Lord Jesus said to his apostles, go, and to you […] believe false prophets, pagan, evil […] they are pagan evil, the Lord's trespass […] […] the apostles, men, and the pagan evil believe, because they are false

  1  end this holy-gospel
  2  write holy-Matthew
  3  inside seven <preposition_of_genitive>-write
  4  time | then-chapter
  5  day Lord-Jézus-Christ
  6  thirty three_days
  7  time say Lord-Jézus
  8  apostle <preposition_of_genitive>-Lord go to-you lamb believe-chapter
  9  false prophet pagan evil [...] exist pagan
 10  evil trespass Lord [...] mouth* apostle somebody
 11  and pagan evil believe because exist false | <preposition_of_genitive>

## 065v — by their fruits ye shall know them

> the Lord's name […]; and then Lord Jesus, to his apostles, […] […] this Lord spoke to you; and then Lord Jesus: do not pick figs from thistles, but rather from the fig, and […] food, grapes […] not from the grapevine, because he who is a good tree brings this good fruit; in turn likewise the evil tree brings this evil of hell. Because a good tree cannot bring forth the evil of hell, every good fruit it brings; in turn likewise the evil tree cannot bring good fruit, but every evil of hell it brings. And then Lord Jesus, many people were crying out against the judgment the Lord's year, to the Lord; this man's trespass; this the Lord preached, and Lord Jesus said

  1  Lord name confess and_then Lord-Jézus apostle <preposition_of_genitive>-Lord
  2  verily verily this-Lord you speak and_then
  3  Lord-Jézus do_not_pick fig on-thistle but_rather-to on-fig and | [...]
  4  food grape thornbush* ~a) on-grapevine
  5  because he_who* good tree this good_fruit grab | in_turn
  6  likewise* die-evil tree this die-evil-hell grab
  7  because good tree can die-evil-hell grab ~a)
  8  each,_every good_fruit grab in_turn-?likewise die-evil tree
  9  can good_fruit grab ~a) each,_every die-evil-hell
 10  grab and_then Lord-Jézus many people exist shout | on-judge
 11  year Lord to-Lord this somebody trespass this Lord preach and say Lord-Jézus

## 066r — the weeping and gnashing of teeth

> and […] the man who can speak of the Lord, go to the Lord, the Lord's heart the man, and the Lord saved every one, Adam gained, this man […] the year out, the man […] of his Father, and this man every man […] into […] the heavenly home of his Father; but every one goes, the man, to hell fire; there is seen the gnashing of teeth and crying for ever; in turn, and the man is […] the man says, three, Lord upon Lord upon Lord, saved by the Lord, every people, this man every one goes into […] the heavenly home of his Father; there is the man's judgment, to the Lord, and the angels, and his Lord Father God, for ever, amen. Here ends this holy gospel.

  1  and [...] somebody can-say-Lord go Lord-<suffix_of_divine_name> Lord heart | <preposition_of_genitive>
  2  somebody and be_saved Lord each,_every ~Adam gain this somebody
  3  [...] out(ward)-year somebody chapter* <preposition_of_genitive>-Lord father-<suffix_of_divine_name> and this somebody
  4  each,_every somebody [...] inside [...] heavenly home <preposition_of_genitive>-Lord
  5  father-<suffix_of_divine_name> a) each,_every go somebody on-chapter-oh chapter-oh hell
  6  fire there exist see grinding tooth crying
  7  chapter-oh chapter-oh in_turn and somebody exist [...] somebody
  8  say three Lord-chapter-Lord-chapter-Lord be_saved Lord each,_every people* this somebody
  9  each,_every go inside [...] heavenly home <preposition_of_genitive>-Lord father-<suffix_of_divine_name> there
 10  exist somebody judge to-Lord and angel and <preposition_of_genitive>-Lord-father
 11  God chapter-oh chapter-oh amen end this holy-gospel

## 066v — whatsoever ye shall ask the Father in my name

> Here begins this holy gospel written by holy John in the fourteenth chapter of his writing. At that time Lord Jesus said to his apostles, at the last supper, […] […] this the Lord spoke to you: love. Whatsoever ye shall ask of the Lord's Father in the Lord's name, ye shall all receive it saved from heaven, from this Lord Christ. And this Lord Jesus spoke, saying, on the way, to his apostles, and said, O the Lord's son.

  1  begins this holy-gospel
  2  write holy-John
  3  14-+one chapter <preposition_of_genitive>-write
  4  time say Lord-Jézus
  5  apostle <preposition_of_genitive>-Lord on-last dinner
  6  verily verily this-Lord you speak love
  7  whatever you exist ~ask_(for) from <preposition_of_genitive>-Lord-from father-<suffix_of_divine_name>
  8  inside <preposition_of_genitive>-Lord name each,_every you be_saved grab
  9  from heavenly from this-Lord Christ and this say speak Lord-Jézus
 10  on-way apostle <preposition_of_genitive>-Lord and say oh <preposition_of_genitive>-Lord son.

## 067r — whose son is he, and thou art the Son of the living God

> Judge this: whose son is he? […] the apostles spoke to the Lord, and the apostles said, the apostles answered, this Lord believe […] this Lord […] truly the Son of the living God. And Lord Jesus said, O the Lord's son, this Lord casts this out; if you believe this, it is to the Lord that this Lord is truly the Son of the living God […] and […] […] believe, believing, because this Lord who goes to the death, to the Lord's death […] ask this of you […] in the Lord […] the apostles, because you are apostles, many sorrowing on the Lord you have, because you apostles, all the apostles […] […] go and go […] and to and one and

  1  judge this-Lord you whose? son | is_he*
  2  yours to-Lord speak apostle and say apostle answered apostle this Lord
  3  believe that* this Lord [...] righteous(ly) son living God and say
  4  Lord-Jézus oh <preposition_of_genitive>-Lord son this-Lord this exorcise
  5  if-to you this believe exist to-Lord
  6  this-Lord righteous(ly) son living God mouth-+who and [?]-+one | is_he*
  7  yours believe exist-~exist because this-Lord who-go
  8  on-die to-Lord-die name-[?] ~ask_(for) this-Lord you [...]
  9  inside Lord herd apostle because you exist apostle many sad(ly)
 10  on-Lord have because you apostle each,_every apostle | on-apostle-chapter
 11  [...] chapter-?ark-to go-go mourn and to-and one and

## 067v — he that believeth and is baptized shall be saved

> one […] and this Lord, on the third day, rose again. He stood up, and this Lord, believing in you, within belief, afterwards […] there is a leaving; for ever, amen. And the two men […] you, and the apostles are one God; the apostles believe, and the man who is outside this […] and one man is saved, but every man is damned and the man who believes in […] Christ, this whosoever shall be saved, because this is to the Lord, one God. Here ends this holy gospel. […] the man has, he asks in Jesus' name he is saved, speaks holy Paul the apostle

  1  one [...] and this-Lord on_the_third_day one-?again.
  2  stand_up-to and this-Lord you exist-~exist inside
  3  believe afterward* believe* exist
  4  leave-chapter-leave chapter-oh chapter-oh amen and two
  5  somebody [...] you and exist apostle one
  6  God believe apostle and somebody exist out(ward) this believe
  7  and one somebody be_saved a) each,_every somebody be_damned
  8  ~to and somebody exist believe inside [?]-~Christ this
  9  whosoever* exist be_saved because this to-Lord one God
 10  end this holy-gospel whatsoever* have somebody ask_(for)
 11  inside Jézus name be_saved speak holy-Paul apostle

## 068r — love the Lord, and thy neighbour as thyself

> this word, Paul's brethren; Paul the man has, he asks in Jesus' name; three things Paul the man asks; in turn the brethren, Paul the man would be saved first; he asks, the man, Paul: love the Lord most high with all the heart, and every man as his neighbour as the neighbour; and the man shall be saved. In turn the second he has, Paul the man asks, in Jesus' name […] believe; Paul the man asks of Lord Jesus, in his name. The third Paul the man has, he asks, in Jesus' name, saved by Lord Jesus, in his […] name, and the man shall be saved. Here ends this apostle's holy gospel.

  1  this word brother <preposition_of_genitive>-Paul have somebody-Paul ask_(for)
  2  inside Jézus name three ask_(for)-somebody-Paul | in_turn
  3  brethren* want-somebody-Paul be_saved first | ask_(for)-somebody
  4  Paul love Lord-<suffix_of_divine_name> most_high each,_every heart and each,_every somebody how?-to neighbour
  5  to-+neighbour and exist somebody be_saved in_turn-two have
  6  somebody-Paul ask_(for) inside Jézus name go_away
  7  believe ask_(for) somebody-Paul from Lord-Jézus inside <preposition_of_genitive>-Lord
  8  and-to-end-+name third have somebody-Paul ask_(for) | inside
  9  Jézus and-to-end-+name be_saved from Lord-Jézus inside <preposition_of_genitive>-Lord
 10  [...] and-to-end-+name and exist somebody be_saved end
 11  this apostle holy-gospel

## 068v — of sin, and of righteousness, and of judgment

> Here begins this holy gospel written by holy John, in the sixteenth chapter of his writing. At that time Lord Jesus said to his apostles, at the last supper: this Lord goes to his Father; you learn, he does, heaven and earth, that is, this Lord […] to the death; the Lord dies, and this Lord goes from you […] the day; in turn he who, this Lord, this dies for you […] the Holy Spirit; the Lord dies, and this Lord, to you the Holy Spirit goes, and you shall see two judgments: first of sin; in turn the second of righteousness; the third, judgment

  1  begins this holy-gospel
  2  write holy-John inside
  3  ten-six chapter <preposition_of_genitive>-write
  4  time say Lord-Jézus
  5  apostle <preposition_of_genitive>-Lord on-last
  6  dinner this-Lord go-Lord <preposition_of_genitive>-Lord father-<suffix_of_divine_name> you learn
  7  do, heavenly land that_is this-Lord go_away*
  8  on-die Lord die and this-Lord you go | [...]
  9  day in_turn-who this-Lord this die to you go_not_away
 10  holy-spirit Lord die and this-Lord you
 11  go holy-spirit and you exist see-two
 12  judge first from sin in_turn-two from righteous(ly) third judge

## 069r — the Spirit, the tongues, and the signs

> And then this Holy Spirit goes to you, from the Spirit through it you receive […] every good thing, and there are apostles […] who lift up tongues […] […] you shall have many miracles […] which the mouth speaks in the Old Testament word, and it lives goes before […] […] […] the day of judgment because there are many miracles afterwards. Here ends this holy gospel. Here begins this holy gospel written by holy Luke, in the tenth the last chapter of his writing. Said Lord Jesus to his apostles, at the last supper, this Lord […] his Father

  1  and then-exist you go this holy-spirit from-spirit
  2  through grab you humble each,_every good and exist
  3  apostle new who-go_up language say [...] you exist many
  4  miracle say which-mouth exist inside <pertaining_to_the_Old_Testament> word and living exist
  5  go before [...] [?]-[?] [...] judge-+day
  6  because-exist many miracle afterward* end this holy-gospel
  7  begins this holy-gospel
  8  write holy-Luke inside | ten
  9  seven chapter <preposition_of_genitive>-write say
 10  Lord-Jézus apostle <preposition_of_genitive>-Lord | on
 11  last dinner this-Lord grapevine father-<suffix_of_divine_name> <preposition_of_genitive>-Lord <subject_marker>

## 069v — I am the vine, ye are the branches

> the vineyard; in turn you are the branches, and the Father, the Lord's vineyard, the angel […] this […] […] and without a name […] […] […] he takes this and cuts it off, and […] out onto the way […] and then Lord Jesus, and the man who is within the Lord, carried by the Lord, stays; and this Lord is within […]. And then Lord Jesus, to his apostles, O the Lord's son, this law and love the Lord carries; can the apostles […] understand what this Lord […] to you, speaking Lord; and the man who is in the Lord's commandment of love, the man carries, from the man who is within the Lord's law […] stays, and this Lord

  1  farm in_turn you vine_branch and go
  2  father-<suffix_of_divine_name> <preposition_of_genitive>-Lord farm angel vine* this | name-Lord
  3  grapevine and without-+name vine_branch | [nothing]
  4  name grab this cut_off and vine_branch out(ward)
  5  on-~way throw_out and_then Lord-Jézus and somebody exist
  6  inside Lord-[?]-~carry-Lord stay and this-Lord exist
  7  inside [...] and_then Lord-Jézus apostle <preposition_of_genitive>-Lord oh | <preposition_of_genitive>
  8  Lord son this law-love-~carry-Lord can apostle [...]
  9  understand who this-Lord you [...] | speak
 10  Lord and somebody exist <preposition_of_genitive>-Lord commandment-love carry-somebody from
 11  somebody exist inside Lord-+law-[?] stay and this-Lord

## 070r — the branch that beareth not is cast into the fire

> the Lord is within […]; Lord Jesus said, who afterwards to his Father, this […] […] is good […] takes this and that […] […] from the Father of the Lord, upon whom every […] carries; and the Lord's Father goes two evil vineyards, and this in turn what […] takes the evil vineyard, and […] to the evil […] there is seen the gnashing of teeth and crying, for ever. And then Lord Jesus, he is from his Father the Lord loves, and this Lord loves you; and Lord Jesus said, O the Lord's son, and you love, because the apostles are in love

  1  exist-Lord inside [...] say Lord-Jézus who afterward*
  2  to-father-<suffix_of_divine_name> <preposition_of_genitive>-Lord this vine_branch [...] exist | good
  3  grape grab this-and-this vine_branch from-?blind from-father-<suffix_of_divine_name>
  4  <preposition_of_genitive>-Lord who-chapter each,_every grape carry and go father <preposition_of_genitive>-Lord
  5  two evil farm and this in_turn-what vine_branch
  6  grab evil farm and <subject_marker> throw_out on-~evil
  7  fire there exist see grinding tooth crying chapter-oh
  8  chapter-oh and_then Lord-Jézus he_is* from-father-<suffix_of_divine_name> <preposition_of_genitive>-Lord
  9  Lord love and this-Lord you love and say Lord-Jézus oh
 10  <preposition_of_genitive>-Lord son and you love because-exist apostle inside-love

## 070v — ask in my name, and Paul's three askings again

> in the commandment you are, the Lord's ten laws of love the apostles carry Lord Jesus said, and the man who carries […] […] […] you first […] love the Lord, whatsoever it is ye shall ask of the Father, of the Lord's Father, in the Lord's name, ye shall all receive it saved. Here ends this holy gospel. […] the man has, he asks in Jesus' name he is saved, speaks holy Paul the apostle this word; Paul's own; whosoever Paul asks in Jesus' name; three things Paul the man asks if Paul the man would be saved, first he asks

  1  inside commandment you exist <preposition_of_genitive>-Lord law-love-ten carry-apostle
  2  say Lord-Jézus and somebody exist carry [...] this-?Pharisees-+one
  3  [...] you first say Lord love whatever | is_he*
  4  exist ~ask_(for) from-father-<suffix_of_divine_name> from <preposition_of_genitive>-Lord from-father-<suffix_of_divine_name> inside
  5  <preposition_of_genitive>-Lord name each,_every you be_saved grab
  6  end this holy-gospel whatsoever* have somebody ask_(for)
  7  inside-Jézus name be_saved speak holy-Paul apostle
  8  this word exist-exist <preposition_of_genitive>-Paul have whosoever-Paul
  9  ask_(for) inside-Jézus name three ask_(for) somebody-Paul
 10  if want somebody-Paul be_saved first ask_(for)

## 071r — the great commandment, repeated

> Paul the man: love the Lord most high, literally with all the heart, and every man as the neighbour […] and the man shall be saved. In turn the second Paul the man has, he asks, in his […] and was named […] believe; Paul the man asks of Lord Jesus, in the Lord's name. The third he has, Paul the man asks in the Lord's name, saved by Lord Jesus, in the Lord's name; and the man shall be saved. Here ends this apostle's holy gospel […] Here begins this holy gospel, written by holy Luke, in […] of his writing. Lord Jesus said to his apostles at the last supper: you shall be driven out

  1  somebody Paul love Lord-<suffix_of_divine_name> from literal each,_every heart and each,_every somebody | how?
  2  to neighbour [?]-from-°creature and exist somebody be_saved
  3  in_turn-two have somebody Paul ask_(for) inside <preposition_of_genitive>-Lord | and
  4  was_named* go_away believe ask_(for) somebody Paul
  5  from Lord-Jézus inside <preposition_of_genitive>-Lord name third have
  6  somebody Paul ask_(for) inside <preposition_of_genitive>-Lord name be_saved
  7  from Lord-Jézus inside <preposition_of_genitive>-Lord name and exist
  8  somebody be_saved end this apostle holy-gospel [...]
  9  begins this holy-gospel write
 10  holy-Luke inside [...] | <preposition_of_genitive>
 11  write say Lord-Jézus apostle <preposition_of_genitive>-Lord
 12  on-last dinner you | chase

## 071v — a woman when she is in travail hath sorrow

> cast out, for hearing; how one […] every for the Lord's name. And then you they will drive out, the apostles say; this is it: out, he who, apostle by apostle, Master […] and the Lord, the Jews put to death; and you shall have much sorrow upon the Lord; in turn, one word, joy […] your sorrow is […] until […] how; then one woman, the chief, a son is born […] she has no more; in turn, then the son is born, and of that comes joy over the son and your sorrow, in turn, joy; much sorrow cast out, and […] in the year of judgment; in turn your sorrow, much joy cast out, and […] in the year of judgment. Here ends this holy gospel.

  1  say out(ward) on-hear how? one have_mercy-apostle-?believe each,_every
  2  to-<preposition_of_genitive>-Lord name and then-exist you
  3  chase want apostle say this_is ~out(ward) he_who* apostle-apostle
  4  Master spoke* and Lord Jew(ish) die and you
  5  exist many sad(ly) on-Lord have in_turn one say-exist
  6  joy [...] you sad(ly) exist and-go_up ~until
  7  little how? then-exist one baptize head
  8  son be_born remain* many not-not have in_turn | then
  9  exist be_born from-~exist on-son joy this-Peter
 10  and ~you sad(ly) in_turn-+say joy want many sad(ly)
 11  ~out(ward) and that* on-judge-year in_turn you sad(ly) many
 12  joy ~out(ward) and that* on-judge-year end this holy-gospel

## 072r — after the crucifixion, they sit at meat in Jerusalem

> Here begins this holy gospel, written by […] in the twenty- fifth chapter of his writing. At that time, then, after the crucifixion of Lord Christ […] at that time then the apostles sat […] in Jerusalem, in the Lord's house, where the Lord Lord Jesus made the supper; at that time he appeared, the Lord Jesus, to his apostles, in […] name, the man; and he sat with the apostles […] and began to rebuke their unbelief

  1  begins this
  2  holy-gospel write
  3  holy_Mark inside | two
  4  ten-ten five chapter
  5  <preposition_of_genitive>-write time
  6  then-exist on-execute
  7  Lord-Christ [?]-+day time then-exist
  8  sit apostle at_table inside Jerusalem inside Lord house where Lord-<suffix_of_divine_name>
  9  Lord-Jézus dinner do, time appear | Lord
 10  Jézus apostle <preposition_of_genitive>-Lord inside [?]-+name somebody and.
 11  sit to-apostle at_table and begin-admonish on-believe

## 072v — go ye into all the world, he that believeth and is baptized

> and Lord Jesus said, go ye, apostles, among the people, and baptize in the Lord's name; and the man who is baptized in the name of the Father and the Son and the Holy Spirit, and believes in the Lord, every such man shall be saved; and one is damned […] […] and the man […] baptized, and believes in the Lord and one […] but every man is damned […] […] and the man who believes in the Lord shall do many miracles, all in the Lord's name; the man in the Lord's […] […] name: the blind through light, the dead see and rise up.

  1  and say Lord-Jézus you go apostle among_the_people* and
  2  exist baptize inside <preposition_of_genitive>-Lord was_named* and somebody
  3  exist baptize inside name father-<suffix_of_divine_name> and son
  4  and holy-spirit and exist Lord-to believe
  5  each,_every somebody be_saved and one be_damned [...]
  6  [...] and somebody exist baptize and exist Lord-to
  7  believe and one be_saved a) each,_every somebody
  8  be_damned [...] [...] and somebody exist Lord-to believe
  9  from exist many miracle do, each,_every inside <preposition_of_genitive>-Lord
 10  name exist somebody inside <preposition_of_genitive>-Lord | and-exist
 11  [?]-+name ~blind through light die from-see resurrect stand_up.

## 073r — and these signs shall follow them that believe

> the man in the Lord's name, the evil in the man casts out; he carries serpents in the hand, and the man cannot be bitten; the man, in the Lord's name […] […] and whatever the man […] the man, in the Lord's name, at the cup […] of the man, why in turn he puts […] the man is healed, all in the Lord's name; the man does many miracles, and Lord Jesus said, this Lord goes to his Father, to you the Lord, and the Lord goes, and this Lord, to you goes the Holy Spirit, and the apostles […] lift up tongues

  1  exist somebody inside <preposition_of_genitive>-Lord name evil inside
  2  somebody exorcise exist serpent carry inside
  3  hand ~exist somebody can bite exist somebody inside
  4  <preposition_of_genitive>-Lord name deadly_poison drink and what-to
  5  who somebody ~exist not_ill exist somebody inside <preposition_of_genitive>-Lord
  6  name on-cup-[?]-+day <preposition_of_genitive>-somebody why?-in_turn put
  7  [...] exist somebody from-healing each,_every inside <preposition_of_genitive>-Lord | and-exist-from
  8  day-+name exist somebody many miracle do, and
  9  say Lord-Jézus this-Lord go to-<preposition_of_genitive>-Lord from-father-<suffix_of_divine_name> to-you
 10  Lord and Lord-<suffix_of_divine_name> <subject_marker> Lord go and this-Lord you go-Lord
 11  holy-spirit and exist apostle new who-go_up language

## 073v — he went on the way, and each time he said the same

> […] and Lord Jesus said to his apostles, go, apostles […] the mount; this Lord would go out truly, and the whole wide world; from his Father; and he passed on, from the apostles; in turn the apostles knew the Lord went and then the Lord looked on the apostles and said, peace be unto you and then the Lord passed on the way; and a second time he looked on the apostles and said, peace be unto you; and then the Lord passed on the way; in turn the apostles knew the Lord; on the Monday; and a third time he looked on the apostles and said, peace be unto you; and then the Lord passed on the way; and a fourth time he looked on the apostles and said, peace be unto you […] and then the Lord passed on the way; and a fifth time the Lord looked on the apostles and said, this Lord, to you, the eye

  1  say and say Lord-Jézus apostle <preposition_of_genitive>-Lord go-apostle today*
  2  mount this-Lord want-Lord ~out(ward) righteous(ly) and the_whole_wide_world <preposition_of_genitive>-Lord | from
  3  father-<suffix_of_divine_name> and trespass go-Lord from apostle in_turn apostle know Lord go apostle
  4  and then-exist from-see-Lord on-apostle and say-Lord law you
  5  and then-exist trespass go-Lord on-~way and two from-see-Lord on-apostle
  6  and say-Lord law you and then-exist trespass go-Lord | on
  7  ~way in_turn apostle know Lord Monday-apostle and three from-see-Lord on-apostle
  8  and say-Lord law you and then-exist trespass go-Lord
  9  on-~way and two-two from-see-Lord on-apostle and say-Lord law | is_he*
 10  yours and then-exist trespass go-Lord on-~way and five | from
 11  see-Lord on-apostle and say-Lord this-Lord you law eye

## 074r — he was received up into glory

> to his sufferer, and to his Father, for ever amen; because Lord Jesus would have him confess before his Father, in the year of judgment; then the Father goes to judge the living and the dead, the man; and the Lord said to the apostles, ye shall hear; his mother, and Mary blessed upon all the apostles, and among this […] […] knew Lord Jesus, and […] Lord Jesus […] […] went […] and blessed all the whole wide world and the Lord was taken into eternal glory. At that time said holy Peter: Master, how does this Lord have apostles, as it were, saying

  1  to-sufferer <preposition_of_genitive>-Lord and <preposition_of_genitive>-Lord from-father-<suffix_of_divine_name> chapter-oh chapter-oh
  2  amen because want Lord-Jézus to-Lord confess have
  3  before from-father-<suffix_of_divine_name> <preposition_of_genitive>-Lord on-judge-year then-exist
  4  go father-<suffix_of_divine_name> judge living and die somebody and say-Lord apostle
  5  you exist hear <preposition_of_genitive>-Lord mother and
  6  Mary bless on-each,_every apostle and among this earth
  7  [...] know Lord-Jézus and [...] Lord-Jézus | remain*
  8  sun go sky and bless each,_every the_whole_wide_world world*
  9  and Lord grab to-?eternal glory* time say | holy
 10  Peter Master how? this-Lord have apostle as* say

## 074v — the Lord's Prayer

> Lord Jesus, this his son, as the Father of the man and the Lord, in the eternal holy name of the Father; the man goes into the Father's kingdom; the whole wide world is the Lord's, as in heaven so on earth […] of the man, every year the Lord gives the man this day's bread; this man's trespass forgive, as the man forgives his own; joy the man goes into pleasing […] from evil. Amen. Written by holy Matthew in his gospel. And the second time said holy Peter: Master, Lord, when shall be […] the year of judgment? Lord Jesus Christ said […] out and out

  1  Lord-Jézus this <preposition_of_genitive>-Lord son as* father-<suffix_of_divine_name> <preposition_of_genitive>-somebody
  2  and-Lord inside eternal* holy name <preposition_of_genitive>-father-<suffix_of_divine_name> go somebody
  3  inside king <preposition_of_genitive>-father-<suffix_of_divine_name> exist the_whole_wide_world <preposition_of_genitive>-Lord how? heaven
  4  this and ~earth bread <preposition_of_genitive>-somebody each,_every year
  5  grab-Lord somebody today’s year this-somebody trespass
  6  remit how?-to somebody remit <preposition_of_genitive>-somebody joy
  7  go somebody inside pleasing-chapter redeem from evil amen
  8  write holy-Matthew inside <preposition_of_genitive> gospel and two say
  9  holy-Peter Master Lord when? exist pass
 10  judge-year say Lord-Jézus-Christ or out(ward)-out(ward)

## 075r — two men in white apparel

> In turn, out and out, two thousand years. And the third time said holy Peter: Master, how shall the apostles […] write of the Lord? Lord Jesus said, one year write, apostles, literally; in turn the second, figuratively. And then the eternal […] was to Lord Jesus; and then Lord Jesus went into heaven, into glory; and the Lord's light departed, because Lord Jesus would have it so; then the Lord shone on the apostles of God, upon this world; and then the two appeared, two angels, white […] […] and then the two angels, to you apostles, O men, how see ye the Lord's joy? Jairus

  1  in_turn out(ward)-to-out(ward) two-to-?thousand-year and three say holy-Peter
  2  Master how? apostle good_news Lord write say Lord-Jézus one
  3  year write apostle literal in_turn two metaphoric and then-exist
  4  eternal* gate exist-to Lord-Jézus and then-exist
  5  go Lord-Jézus heaven glory* and Lord light from
  6  ~leave because want Lord-Jézus then-exist Lord
  7  apostle God shine on-this world* and then-exist-two
  8  appear two angel-angel white | clothes
  9  believe* and_then two angel-angel you
 10  apostle-oh-<suffix_of_divine_name>-chapter man how? Lord joy see Jairus

## 075v — he shall so come, to judge the quick and the dead

> he departed, from the eternal; in turn, to the end, this joy the Lord would go to […] judge the living and the dead, the man. And the two said, these two angels, go, apostles, into the apostles, O; and the Lord […] the apostle-man. And […] they saw; the word was done by the two angels. Here ends this holy gospel. Love the Lord with all thy heart. The Lord spoke, the apostles, Lord Jesus Christ; then the apostles prayed, his son, this Father of the man

  1  ~leave from_the_eternal* in_turn-chapter-end-chapter this joy
  2  want Lord go on-[?] judge living and die
  3  somebody and say-two this two angel-angel go-apostle inside
  4  apostle-oh-<suffix_of_divine_name>-chapter and Lord find apostle-somebody.
  5  and [...] see word do, two | angel
  6  angel end this holy-gospel the_Lord love Lord-<suffix_of_divine_name> with_all_thy_heart*
  7  speak-Lord apostle Lord-Jézus-Christ
  8  then-exist apostle pray
  9  <preposition_of_genitive>-Lord son
 10  this father-<suffix_of_divine_name>-<preposition_of_genitive>-somebody

## 076r — how oft shall my brother sin against me

> […] to the apostles many said […] written […] […] in the first chapter of his writing. At that time, then, Lord Jesus Christ in the thirtieth year, and three days, and five months, and three days, at that time left the apostles, to Lord Jesus; and then holy Peter answered, would the most high, this Peter, have mercy […] Peter is […] and then Lord Jesus Christ: Peter, Peter, in turn the brethren, one […] […] one year, through the sin of a man against this Peter; have mercy, the man, if the man goes to mercy, asks mercy, the man receives […] goes […] the man of mercy; and cried to Lord Jesus Christ

  1  [...] to-apostle many say say write [...] apostolic_letter
  2  inside one chapter <preposition_of_genitive>-write time then-exist Lord-Jézus-Christ
  3  inside thirty year and three_days and five moon and three_days inside
  4  time leave-to-leave apostle ~to Lord-Jézus and_then holy-Peter
  5  answered want-high this-Peter have_mercy [how_often] exist Peter
  6  [...] and_then Lord-Jézus-Christ Peter Peter | in_turn
  7  brethren* one-[?] dry* one year through sin somebody
  8  against this-Peter have_mercy somebody <subject_marker> if go somebody-have_mercy
  9  ask_(for)-have_mercy-somebody <subject_marker> grab sun* go
 10  understand-+say somebody-have_mercy and shout-to Lord-Jézus-Christ

## 076v — the catalogue of sins

> he departed on the water of heaven […] Peter, Peter, if rather a man among the apostles sins against you […] from […] the man, the apostle, the sin […] […] the man, of the man's sin, leave it; but if a man's sins are many, in turn he who is a thief; in turn […]; in turn a shedder of blood, that is a killer of men; the man in turn […]; the man in turn from […] the man in turn proud; the man in turn a drinker; the man in turn many […]; the man in turn under many yokes; this Peter said Lord Jesus Christ, because Peter is […] in turn in […] the man, this […] how then the man dies in turn

  1  ~leave on-water heaven [...] Peter Peter if-?but_rather
  2  <subject_marker> somebody among apostle you sin witness* from
  3  heathen* somebody apostle sin witness* publican* somebody | <preposition_of_genitive>
  4  somebody-+sin leave a) if-exist many somebody-+sin in_turn
  5  thief-who in_turn robber in_turn blood blood_shedder that_is
  6  people-die somebody in_turn [...] somebody in_turn from [...]
  7  somebody in_turn proud somebody in_turn drink somebody in_turn many
  8  [...] somebody in_turn many yoke-chapter somebody this-on-Peter
  9  say Lord-Jézus-Christ because exist Peter [...] in_turn inside humble
 10  somebody this be_damned* how? then-exist somebody die in_turn

## 077r — one sin, and whosoever sins is damned

> […] the man […] have mercy; the man in turn from riches […] the man in turn […] truly; the man, or the man judges of whom holy Paul speaks […] said Lord Jesus Christ, this […] the man sins one sin […] he is saved; and he who hides the man […] […] in sin, to Lord Jesus Christ one sin […] is saved; but every one, whosoever sins, is damned said Lord Jesus Christ: Peter, Peter […] that is […] whosoever sins […] the apostle, this whosoever sins, from […] […] […] the man, of […] leaves […] the man […] the voice […] the brethren, the man says, this man

  1  Adam somebody penance* have_mercy somebody in_turn from-rich-from [...]
  2  somebody in_turn penance* righteous(ly) somebody or ~judge somebody
  3  who speak holy-Paul apostolic_letter say Lord-Jézus-Christ this [...]
  4  somebody sin one sin penance* be_saved and who-hide_oneself
  5  somebody [...] heavenly* on-sin to Lord-Jézus-Christ
  6  one sin penance* be_saved a) each,_every whosoever-+sin be_damned
  7  say Lord-Jézus-Christ Peter Peter [...] that_is [...]
  8  whosoever-+sin exist apostle-this-?whosoever-+sin from heathen* witness*
  9  publican* somebody <preposition_of_genitive>-[?] leave [...]
 10  somebody [...] voice,_sound [...] brethren-exist somebody say somebody this

## 077v — go to him alone, then take two, then three

> he loves Lord Jesus Christ more than these. Lord Jesus Christ said to Peter: in turn […] the apostle-man among […]; the man who sins, go to Peter, […] the sin, to the house; and the man upon his sin rebuke, because this man who sins suffers; in turn, to whom this man suffers […] the apostle, this whosoever sins, from […] […] he looks; of […] he leaves; but Peter goes, to Peter, two […] the sin; and the man upon his sin rebuke, because this whosoever sins suffers; in turn, to whom this man suffers […] the apostle, this whosoever sins from […] […] the man, of […] leaves; but Peter goes, to Peter, a third time […] the sin, and the man

  1  <subject_marker> love Lord-Jézus-Christ more_than_these* say Lord-Jézus-Christ to-Peter
  2  in_turn [...] apostle-somebody among [...] somebody-+sin go | to
  3  Peter [?]-+sin to-home and somebody-on-+sin
  4  admonish because this somebody-+sin sufferer in_turn to-which this-somebody
  5  sufferer exist apostle this whosoever-+sin from heathen* publican*
  6  from-see <preposition_of_genitive>-[?] leave a) go-Peter to-Peter two
  7  [?]-+sin and somebody-on-+sin admonish because this whosoever-+sin
  8  sufferer in_turn to-which this-somebody sufferer exist apostle this whosoever-+sin
  9  from heathen* publican* somebody <preposition_of_genitive>-[?] leave a)
 10  go Peter to-Peter three [?]-+sin and somebody

## 078r — judge righteous judgment

> upon his sin rebuke, because this whosoever sins suffers; in turn, to whom this man suffers, take him, whosoever sins […] from […] within why in turn? because this is truly, truly, to whosoever sins; because a false judge […] judges whosoever, truly judge but rather every […] false judgment; in turn the false judge the true man falsely judged is damned, in the evil for ever; in turn the true judge, every one to whom he judges truly […] the judge falsely judging, but rather to whom he judges truly; the Lord speaks, every writing and every prophet and every church father and every forefather and […]

  1  on-sin admonish because this whosoever-+sin sufferer in_turn to-which this-somebody
  2  sufferer grab whosoever-+sin take* from [...] inside
  3  why?-in_turn because this exist righteous(ly) righteous(ly) to-?whosoever-+sin because
  4  false ~judge-somebody according_to* chapter-judge-?whosoever righteous(ly) judge
  5  but_rather-each,_every [...] false judge in_turn false ~judge-somebody
  6  righteous(ly) somebody false from-judge be_damned <subject_marker> inside ~evil
  7  <subject_marker> chapter-oh chapter-oh in_turn righteous(ly) ~judge-somebody each,_every
  8  to-which-chapter righteous(ly) judge according_to* judge-somebody false
  9  from-judge but_rather-each,_every to-which-chapter righteous(ly) judge Lord-<suffix_of_divine_name> speak each,_every write
 10  and each,_every prophet and each,_every church_father and each,_every forefather and evangelist*

## 079r — the orders of angels, and one word

> among all peoples, to eternal glory, most high, all the angels, the orders of angels […] eat literally, from the one Lord, truly […] speaks holy Paul […] Paul's own, this Lord truly […] Lord Jesus Christ this Lord judges all peoples by one word […] the word, every man […] of the man, truly, good, mercy, saying, love, doing; and the Lord takes; this Lord truly […] and the Lord, every man receives […] from the Lord […] the man the firstborn is damned, to be […] […] […] damned […] […] […] and nine […]

  1  inside each,_every people* to-?eternal glory* most_high each,_every angel angel angel order
  2  [...] eat literal from one Lord righteous(ly) somebody* speak holy-Paul
  3  apostolic_letter exist-exist <preposition_of_genitive>-Paul this-Lord righteous(ly) ~judge-+somebody Lord-Jézus-Christ
  4  this-Lord exist judge each,_every people* one word [...] word each,_every
  5  somebody [...] <preposition_of_genitive>-somebody righteous(ly)-good-have_mercy-say-love-do, and
  6  grab Lord-<suffix_of_divine_name> <subject_marker> this-Lord righteous(ly) ~judge-+somebody and Lord-<suffix_of_divine_name> each,_every
  7  somebody exist grab [...] exist from Lord-<suffix_of_divine_name> [...] somebody
  8  firstborn exist be_damned to-exist-~exist [...] on-+Lazarus [...]
  9  be_damned [...] [...] [...] and nine [...]

## 080r — the Comforter, and the threefold reproof

> Before the gospel: written by holy John, in the sixteenth chapter of his writing. Then said the Lord Jesus to his apostles at the last supper: this Lord goes to his Father. You know that the heavenly kingdom, that is: this Lord goes away, to die; the Lord dies, and this Lord sends you the Holy Spirit. In turn, if this Lord did not die, did not go away, to you the Holy Spirit [would not come]. The Lord dies, and this Lord sends you the Holy Spirit, and you shall see two judgments: the first, of sin; the second, of righteousness; the third, judgment. And then you receive this Holy Spirit; from the Spirit, through him, he takes you.

  1  before gospel write holy-John inside ten-six chapter <preposition_of_genitive>-write
  2  time say Lord-Jézus apostle <preposition_of_genitive>-Lord on-last dinner this-Lord
  3  go-Lord <preposition_of_genitive>-Lord father-<suffix_of_divine_name> you learn do,
  4  heavenly land that_is this-Lord go_away* on-die Lord
  5  die and this-Lord you go holy-spirit | in_turn
  6  who this-Lord this die to you go_not_away holy-spirit
  7  Lord-die and this-Lord you go holy-spirit
  8  and you exist see-two judge first from sin
  9  in_turn-two from righteous(ly) third judge and then-exist you
 10  go this holy-spirit from-spirit through grab you

## 080v — the apostles wait in prayer with Mary

> […] every good thing; and the apostles […] lift up […] […] […] ye shall have many miracles, says the mouth in the Old Testament word, and it lives; go before […] […] […] the day of judgment. Here ends this teaching gospel. Here begins this holy gospel, written by holy Luke, in the second chapter of his writing. At that time, then, after the crucifixion of Lord Christ […] year; and then the Lord was […] year; at that time the apostles remained in prayer in the Lord's, until where the Lord, Lord Jesus, made the supper; out ten years; and then this went on ten years; at that time the apostles remained in prayer; and holy Peter left, to the Virgin Mary. And then

  1  humble each,_every good and exist apostle new who-go_up language say
  2  [...] you exist many miracle say which-mouth-chapter-year
  3  inside <pertaining_to_the_Old_Testament> word and living-exist go before [...] [?]-[?]
  4  [...] judge-+day end this <subject_marker> learn holy-gospel begins
  5  this holy-gospel write holy-Luke inside two chapter <preposition_of_genitive>-write time
  6  then-exist on-execute Lord-~Christ [?]-year and | then
  7  Lord-exist [?]-year time leave apostle pray
  8  inside Lord ~until where Lord-<suffix_of_divine_name> Lord-Jézus dinner do, on-~out(ward)
  9  ten-year and then-exist keep_going this ten-year time leave apostle on
 10  pray and leave-to-leave holy-Peter to virgin-Mary and_then

## 081r — the Spirit comes upon them

> holy Peter, the wife, to the apostles answered, speaking; understand, apostles, the Lord is from […] the Holy Spirit goes, to Peter the rock […] this is. And then the Virgin Mary, then the Father, from […] the Holy Spirit goes; father Abraham, and Abraham the spirit goes upon the eleven […] understand the spirit and the apostles, Mary, on high; go, upon this; said Lord Jesus, his Father, this Lord from […] goes, his own Holy Spirit and his mother. And then the Father, how, in what form would he go if he goes into God, the Son, the Spirit; the Lord, Father, Son, Holy Spirit […] this people crucified; and then the Father, holy

  1  holy-Peter wife apostle-to answered speak understand apostle exist-Lord
  2  from sky go holy-spirit rock-to Peter [?]-+day this
  3  exist and_then virgin-Mary then-exist father-<suffix_of_divine_name> from sky
  4  go holy-spirit father Abraham and Abraham
  5  spirit go on-ten-+one-[?] understand spirit
  6  and apostle-Mary to-high go on-this say say Lord-Jézus father-<suffix_of_divine_name> <preposition_of_genitive>-Lord
  7  this-Lord from sky go <preposition_of_genitive>-Lord exist-exist holy-spirit
  8  and <preposition_of_genitive>-Lord mother and_then father-<suffix_of_divine_name> how? shape,_form want go
  9  if go inside God-son-spirit-Lord father son holy-spirit
 10  not_suffer this people* cross execute and_then father-<suffix_of_divine_name> | holy

## 081v — cloven tongues like as of fire

> the Spirit took, upon the spirit, the form of fire and the Spirit went out from the apostles, Mary, the Jews, and the man this Spirit […] the apostles, the Jews; and it took, upon the spirit, the Spirit, the form of holy fire, and the Spirit went out from the apostles, Mary, the Jews; and the man, the Spirit […] the apostles, Mary, the Jews, many […] […] many a wind, in that form […] in fire in that form; and the Jews saw this fire, that form, and it came down upon this house where the apostles and Mary were at prayer. And then the Jews said, the chief, that is

  1  spirit grab on-spirit fire shape,_form
  2  and go spirit from somebody-apostle-Mary-Jew(ish) and somebody
  3  this spirit [...] apostle-Jew(ish) and grab on-spirit
  4  spirit holy-fire shape,_form and go-spirit
  5  from somebody-apostle-Mary-Jew(ish) and somebody spirit [...]
  6  somebody-apostle-Mary-Jew(ish) many drink-+day [...]
  7  many sough inside shape,_form dove inside fire
  8  inside shape,_form and see Jew(ish) this fire.
  9  shape,_form and bow_down on-this house where apostle-Mary
 10  on-pray and_then-+say Jew(ish) ~head-chapter that_is

## 082r — the Jews see it, and three thousand are added

> the Lord; the apostles began to believe, every wind, and […] the Jews saw it, because […] the Jews […] every wind; and then the Jews were […] in the house where the apostles and Mary were at prayer, to […] from the apostles and Mary at prayer, they left the heavenly word; thanks, apostles and Mary, to the Lord; thanks to the Lord God; and various […] […] and then the Jews […] these apostles; the sons of Jerusalem saw how […] […] and then the apostles are apostles, Master, from […] the Holy Spirit goes […] the apostles, the one who […] went from the people, the Jews, one […] the people received belief in Lord Jesus Christ, and every

  1  Lord ~begin-believe apostle each,_every sough and go_to Jew(ish)
  2  on-see because exist-+name Jew(ish) [...] each,_every sough and | then
  3  exist Jew(ish) go_to inside house where apostle-Mary | on
  4  pray to sky from apostle-Mary on-pray leave
  5  heavenly word thanks apostle-Mary to-Lord thanks Lord God and
  6  various language say and_then Jew(ish) blind-to.
  7  this-apostle Jerusalem son see how? language say and_then apostle
  8  <subject_marker> exist apostle Master from sky go holy-spirit [...]
  9  apostle one-who food go from people-+day Jew(ish) three_thousand
 10  people-+day grab believe Lord-Jézus-Christ and each,_every

## 082v — three thousand added, and the Trinity begins

> man, Jew, apostle, Mary, received the Holy Spirit; and two years, three baptisms, from the Jews […] and […] baptism […] three thousand, and one […] son, seven sons; and from the son received holy Spirit […] upon the spirit, the Holy Spirit, every man, Jew, son […] received the Holy Spirit and believed in the Lord Jesus Christ […] believing, the man would […] in turn […] Here ends this holy gospel, this Holy Spirit. […] from the Father, out and out, the Spirit proceeds; in turn the Son, this Son, from the Father, sitteth; see, he is this […] […] the Sun; this sun has three good things; first

  1  somebody-Jew(ish)-apostle-Mary grab holy-spirit and two-year three-+baptize from
  2  Jew(ish) [...] and [...] woman-[?] three_thousand and
  3  one-[?]-[?] ~son seven ~son and from ~son grab | holy
  4  spirit proceed* on-spirit holy-spirit each,_every | somebody-Jew(ish)
  5  ~son-[?] grab holy-spirit and believe | Lord
  6  Jézus-Christ proceed* on-believe somebody want one-can heaven
  7  in_turn-[?] end this holy-gospel this holy-spirit.
  8  [...] on-father out(ward)-out(ward) go_out-spirit in_turn son
  9  this-son from to-father-<suffix_of_divine_name> sit see he_is* this | remain*
 10  sun Sun this sun <subject_marker> three good first

## 083v — the sun, its light and its warmth

> is good […] he who is light; in turn the second is good, warmth; the third is good from the Sun; the sun's light signifies the Son of God; in turn the warmth signifies the Holy Spirit; in turn the Sun itself signifies the Father; upon this Lord, from the Sun proceeds the light, proceeds the warmth, proceeds the Son from the Father, proceeds the Holy Spirit from the Father; he is the sun, one form; this is one God; in turn who is, this can have, how can heaven and earth quake, and in his […] prepare heaven, in turn, and the earth

  1  <subject_marker> good first* he_who* light in_turn-two <subject_marker> good warmth third <subject_marker> good
  2  from-Sun sun Sun light symbolize son God in_turn warmth
  3  symbolize holy-spirit in_turn from-Sun symbolize from-father-<suffix_of_divine_name> on-this-Lord from-Sun
  4  on-go_out light on-go_out warmth on-go_out son on-from-father-<suffix_of_divine_name>
  5  on-go_out holy-spirit on-from-father-<suffix_of_divine_name> he_is* sun
  6  one shape,_form | this
  7  <subject_marker> one God in_turn-who
  8  <subject_marker> this can have how?
  9  can heaven earth
 10  quake and inside <preposition_of_genitive>-Lord [...] prepare
 11  heaven in_turn-chapter-in_turn-from-in_turn and earth

## 084r — Augustine and the child on the seashore

> At that time, then, after the condemning of Lord Jesus Christ, in the sixtieth year, at that time holy Augustine went to the shore of the sea, because he would understand how it is that three, Lord, Lord, Lord, Father, Son, Spirit, are one God; and this is one […] in the evening […] at the going down of the sun; and then he found one little child on the shore; this […] that day the little child sat […] and the child […] one pit […] and the child carried in his hand one spoon, and this that day the child scooped with this spoon into this pit, this child

  1  time then-exist
  2  on-?condemned Lord-Jézus
  3  Christ six-ten-year time
  4  go holy-Augustine shore
  5  sea because want
  6  understand likewise*
  7  three Lord-Lord-Lord father
  8  son spirit one God and this exist one
  9  [...] evening in_the_middle sun on-go_out and then-exist
 10  find one little son-Lord-<suffix_of_divine_name> on-shore this
 11  [?]-daily,_of_that_day sit son-Lord-<suffix_of_divine_name> little [...] and | <preposition_of_genitive>
 12  son-Lord-<suffix_of_divine_name> [...] one pit son* and | <preposition_of_genitive>
 13  son-Lord-<suffix_of_divine_name> hand one spoon carry-son-Lord-<suffix_of_divine_name> and this
 14  [?]-daily,_of_that_day this spoon inside this pit scoop-son-Lord-<suffix_of_divine_name> this son

## 084v — thou shalt sooner empty the sea

> And then holy Augustine, this […] child, what does this child want? Said the child, this: that day into this pit I scoop. Said holy Augustine, this child, can this child do it? What child, this, that day, into this pit the child scoops said this […] child; first this child, can the child do it, and this Augustine, upon leaving and the child […] saw the word afterwards, before holy Augustine; and he could tell many this […] in writing […] but believe truly, this woman, one God, of the man, heaven and earth, that is, he has carries the law of God […] sin, the man is saved the man answered, to many, he shall never die, for ever, amen; speaks […] […] his own

  1  and_then holy-Augustine this little son-Lord-<suffix_of_divine_name>
  2  who this want-son-Lord-<suffix_of_divine_name> say want-son-Lord-<suffix_of_divine_name> this.
  3  [?]-daily,_of_that_day inside this pit scoop say holy-Augustine | this
  4  son-Lord-<suffix_of_divine_name> this can-son-Lord-<suffix_of_divine_name> do, who | this
  5  son-Lord-<suffix_of_divine_name> this [?]-daily,_of_that_day inside this pit scoop-son-Lord-<suffix_of_divine_name>
  6  say this little son-Lord-<suffix_of_divine_name> first this-son this | can
  7  son-Lord-<suffix_of_divine_name> do, a)-who this-Augustine on-chapter-leave-this
  8  and son-Lord-<suffix_of_divine_name> [...] see word afterward* before
  9  holy-Augustine and can to-many this [...] on-write [...]
 10  a) believe righteous(ly) this-woman one God | <preposition_of_genitive>
 11  somebody-+<subject_marker> heaven land that_is have
 12  carry law God [...] sin somebody be_saved
 13  somebody answered* to-many not-not-die chapter-oh chapter-oh
 14  amen speak holy_James apostolic_letter exist-exist <preposition_of_genitive>

## 085r — one commandment broken is all of them broken

> and among you, through transgressing one of God's laws, the commandment, every man […] receives before […] thanks to the Lord, because if a man one transgresses, how then is he a transgressor of every law? because it is the Lord's; he received it from his angel, in the Old Testament word, father Abraham […] ten and one commandment […] this, more than these, go and be saved among men; the Lord of the Jews, Jesus, apostle to the gentiles, most high […] the Son of the living God Lord Jesus Christ; and to the man from […] and to the man the soul upon the cross […] and for the man his blood was shed, and the man the Lord redeemed from hell fire […] the man, to many, until the ten laws; believe truly, be baptized […] one God

  1  and among you through transgress one
  2  law God to-commandment each,_every somebody-+<subject_marker> [...] grab before
  3  face to-Lord thanks Lord-<suffix_of_divine_name> because and somebody one
  4  transgress how? then-exist each,_every law ~transgress somebody | because
  5  <subject_marker> exist Lord-<suffix_of_divine_name> grab on-angel <preposition_of_genitive>-Lord inside <pertaining_to_the_Old_Testament>
  6  word father Abraham seventy and one-[?] commandment
  7  [...] this more_than_these* go be_saved among somebody Lord
  8  Jew(ish) Jézus apostle-pagan above-high serpent son living God
  9  Lord-Jézus-Christ and to-somebody from face and to-somebody soul
 10  ~on-+cross-[?] and to-somebody <subject_marker> <preposition_of_genitive> blood shed and somebody <subject_marker>
 11  redeem-Lord from hell fire [...] somebody to-many from-until
 12  ten-+law believe righteous(ly) woman-[?] one God

## 085v — Elijah calls down fire

> of the man, heaven and earth, that is, he has carries the law of God […] sin, the man is saved the man answered, to many, he shall never die, for ever, amen. Speaks holy Augustine, to many: believe, the man, in God for ever […] God can, for ever. […] this day, in the place, the man receives in his mouth; speaks holy Elijah the prophet, it is written. Holy the prophet, holy Moses, there was […] fire upon all peoples to heaven on high, because all peoples were destroyed; kneeled one holy Elijah the prophet. At that time, then, the Lord destroyed the earth; there was fire in one place, and […] from piercing […] to the Lord, in water; upon this the destroying was three

  1  <preposition_of_genitive>-somebody <subject_marker> heaven land that_is have
  2  carry law God [...] sin somebody be_saved
  3  somebody answered* to-many not-not-die chapter-oh chapter-oh
  4  amen speak holy-Augustine to-many believe somebody inside
  5  God exist-exist-chapter that God can inside exist-exist-chapter.
  6  to-from face exist-today’s on-place grab somebody
  7  inside <preposition_of_genitive>-somebody mouth speak holy-Elijah prophet write.
  8  holy-<name_of_a_prophet> holy-Moses exist [...] fire on-each,_every people*
  9  to-heaven high because-exist each,_every people* destroy kneel_(down) one
 10  holy-Elijah prophet time then-exist Lord-<suffix_of_divine_name> destroy-Lord
 11  earth exist fire inside one place and flame* | from
 12  pierce [...] to-to Lord-<suffix_of_divine_name> inside water on-this destroy exist three

## 086r — the torch lit from heaven

> twenty years and six years; at that time holy Elijah kneeled and prayed; thanks to the Lord; and fire from the gate of God, the angel of heaven; and rather fire […] one […] […] said the angel of God: Elijah, this signifies the Lord, the Lord of angels. And then holy Elijah took a torch, and the torch gave light; in turn this […] […] went to Elijah, from twenty twenty peoples, and every one […] the torch gave light; in turn holy Elijah […] […] and in Elijah, until until; and then holy Elijah, then, forty days. This is written by holy Moses in the Old Testament word.

  1  two-two-ten-year and six-year time kneel_(down) holy-Elijah
  2  and pray to-Lord thanks Lord-<suffix_of_divine_name> to fire
  3  from-gate God angel heaven and from but_rather*
  4  fire [...] one [...] [...] say
  5  God angel Elijah this exist symbolize Lord-<suffix_of_divine_name> Lord | <preposition_of_genitive>
  6  angel and then-exist grab holy-Elijah torch ~and torch
  7  light in_turn this [...] flame* go to-Elijah from | two-two
  8  two-two people-+day and each,_every from-[?] torch light in_turn
  9  holy-Elijah [...] little and inside Elijah from-until
 10  from-until and_then holy-Elijah then-exist | two-two-two-two
 11  ten-+day this_is write holy-Moses inside <pertaining_to_the_Old_Testament> word

## 086v — the torch signifies the Virgin

> it signifies […] […] the angel from the Father, for ever to the blessed Virgin Mary, one son, the Lord […] signifies the man, for ever […] received, upon the Lord Jesus Christ; it signifies the torch, for ever, to the blessed Virgin Mary; then Mary conceived the Lord, and Jesus saved the whole wide world; and Christ […] of the man, and the Lord, the head […] heaven and earth […] signifies, for ever, Lord Jesus Christ […] the fire signifies the Lord, and every one can […] God the Father Lord Jesus Christ, the angel, the Holy Spirit, Mary, the apostles, one […] God […] and this […] is, until the crucifying of Lord Jesus Christ, at thirty, in […] the Lord's year, upon the whole wide world

  1  symbolize [...] good_news exist angel from-father inside exist-exist-chapter
  2  to-happy virgin-Mary son one Lord-<suffix_of_divine_name> [...] symbolize
  3  somebody exist-exist-chapter good_news exist grab | on-Lord
  4  Jézus-Christ symbolize torch exist-exist-chapter to-happy | virgin
  5  Mary then-exist-Mary get_conceived Lord-<suffix_of_divine_name> and Jézus be_saved each,_every the_whole_wide_world
  6  world* and Christ [?]-to-[?] <preposition_of_genitive>-somebody and Lord ~head-[?]-~son
  7  heaven and earth [...] symbolize exist-exist-chapter Lord-Jézus
  8  Christ [...] symbolize fire Lord-<suffix_of_divine_name> and can each,_every | father-God
  9  Lord-Jézus-Christ-angel-holy-spirit-Mary-apostle one [...]
 10  God [...] and this [...] exist from-until on-execute
 11  Lord-Jézus-Christ on-thirty inside the_host* Lord-year on-each,_every the_whole_wide_world world*

## 087r — the torch and the light

> and the man who eats this day […] the Son of God […] every man shall be saved; and one man […] Elijah signifies, for ever, the blessed Virgin Mary, how from Mary the torch gave light at his coming the Lord created of the man, and the cross could, to one man's death, but all peoples die; this one, one man could, God, everything, in his mouth receives, because the Lord […] for ever, but rather […] God is many […] and […] and from […] […] the earth […] and heaven on high, and God is this can; then the Lord would have heaven and earth quake

  1  and somebody exist this exist-today’s eat man* son
  2  God man* each,_every somebody be_saved and one
  3  somebody be_damned Elijah symbolize exist-exist-chapter to-happy
  4  virgin-Mary how? from-Mary torch light then-?coming
  5  create-Lord <preposition_of_genitive>-somebody and can cross to-one
  6  somebody die a) each,_every people* die this-+one one somebody
  7  can God each,_every inside <preposition_of_genitive>-somebody mouth grab because Lord-<suffix_of_divine_name>
  8  have-[?] exist-exist-chapter but_rather [...] God-+<subject_marker>
  9  many [...] and high-Lord and from [...] [...]
 10  earth [...] and heaven high and God-+<subject_marker>
 11  this can then-exist want-Lord heaven earth quake

## 087v — the blind of God

> […] the gospel written by holy Matthew […] of his writing, who is whosoever is an apostle, this from this […] the son […] afterwards, in Jesus' name, one man is saved, one […] in heaven; in turn the day is not so; every man is damned, judged, the man, by Christ. Holy Matthew speaks […] this man says, this […] the son, this […] the man trespasses, blind to God, and blind to God is the man, and […] […] the man in turn, this

  1  ~exist-chapter gospel write
  2  holy-Matthew [...]
  3  <preposition_of_genitive>-write who-exist-to
  4  whosoever-apostle this from this
  5  little son to*
  6  afterward* inside <preposition_of_genitive>-Jézus
  7  and-~exist-exist-from-+name one
  8  somebody be_saved one man* inside heaven | in_turn-chapter
  9  day-exist ~a) each,_every somebody be_damned judge somebody Christ | holy
 10  Matthew speak [...] this somebody say this little
 11  son this little somebody trespass blind God and
 12  blind God somebody and [...] have somebody in_turn this

## 088r — the rich man, and the soul in purgatory

> the man is rich, he has wealth, he sees, blind he goes […] or sits, and […] asks of this man alms, in Jesus' name […] the blind, the high receives; the man is damned, the man, for ever […] […] judged and damned, the man upon the blind; in turn damned, whosoever is damned, the man, for ever […] saved; the man is damned, the man […] whosoever, in the evil […] […] it is written, the man in the evil until the death of the man […] in turn upon death the soul is in purification […] until the day of judgment; in turn upon the day of judgment, and the soul, and for ever in the evil, for ever

  1  somebody rich have-somebody wealth see blind
  2  go name-somebody or sit and blind* exist ask_(for) from this
  3  somebody alms inside Jézus and-~exist-exist-from-+name [...]
  4  blind high-grab somebody be_damned exist somebody chapter-oh
  5  chapter-oh riches* but-somebody from-judge be_damned somebody
  6  on-blind in_turn be_damned whosoever* be_damned exist somebody chapter-oh
  7  chapter-oh [...] be_saved somebody be_damned exist somebody get_conceived
  8  whosoever* inside ~evil bury [...] write somebody
  9  inside ~evil until to-die <preposition_of_genitive>-somebody and-[?]-from-+name in_turn | on
 10  die soul inside purification fire until judge-+day in_turn | on
 11  judge-+day and soul and exist-exist-chapter inside ~evil chapter-oh chapter-oh

## 088v — there was a certain rich man, clothed in purple

> Here begins this holy gospel written by holy Luke in the sixth […] of his writing. At that time Lord Jesus said to his apostles, and the Jewish people, there was a rich man, one rich man, and the rich man, every […] and purple the rich man wore, and the rich man from day to day made merry; and then […] came one Lazarus to the rich man's house; and Lazarus was all over […] until […] […] wounds, Lazarus; at that time this rich man to […] the rich man sat, the man, the Lord […] the Lord king […] this and that, the Lord; and then the rich man, this poor man asked

  1  begins this holy-gospel
  2  write holy-Luke inside
  3  six chapter <preposition_of_genitive>-write
  4  time say Lord-Jézus
  5  apostle <preposition_of_genitive>-Lord and Jew(ish)
  6  people-chapter exist-rich
  7  one rich-somebody
  8  and somebody-rich each,_every [linen] and purple go-somebody-rich | and
  9  rich from day until day joy-rich and then-exist that_way go
 10  one ~Lazarus to-house this-rich and ~Lazarus exist each,_every from
 11  head until toe covered* wound ~Lazarus time this rich
 12  to table sit-rich somebody Lord [...] king-Lord [...]
 13  who-and-this-and Lord and then-exist rich exist this the_poor_man/woman* ask_(for)

## 089r — the dogs licked his sores, and angels carried him

> alms; and the poor man, alms […] the rich man […] but the poor man he drove out; and then this poor man lay outside the gate of the rich man, alone, because the poor man was […] was […]; and then the poor man desired the crumbs that fell […] from the rich man's table […] the poor man […]; and then the rich man had many dogs, and the dogs came, this […] and the dogs licked Lazarus […] and Lazarus more was of the dogs […] mercy, this Lazarus; in turn from the rich man mercy […] […] mercy; and then this Lazarus died, went with angels to heaven, to glory, literally, from God the Father […] this Lazarus, and Lazarus the angels took, and carried Lazarus into the bosom of Abraham the forefather. And then this rich man saw this miracle, of this Lazarus

  1  alms and the_poor_man/woman* alms take rich [...]
  2  a) the_poor_man/woman* out(ward) chase and then-exist lie this
  3  the_poor_man/woman* out(ward) ~gate to-<preposition_of_genitive>-rich exist-+one because exist the_poor_man/woman* [...]
  4  exist [...] and then-exist want the_poor_man/woman* trespass from crumbs the_dogs*
  5  on-<preposition_of_genitive>-rich throne [...] the_poor_man/woman* take and then-exist | have
  6  rich many dog and go-dog this Lazarus ~and
  7  lick-dog <preposition_of_genitive>-Lazarus wound-+mouth and Lazarus more
  8  exist from dog have have_mercy this Lazarus in_turn from-rich
  9  have_mercy robe-Lazarus lame have_mercy and then-exist this Lazarus
 10  die go angel heaven glory* literal from-father God the_Most_High* this Lazarus and Lazarus
 11  grab-angel and Lazarus carry inside öl Abraham
 12  forefather and then-exist see this miracle this rich from this Lazarus

## 089v — in hell he lifted up his eyes

> […] Lazarus did, the angels, the Father, heaven; and then this rich man died, and this rich man […] in the evil was buried; and then he suffered in the evil, this rich man; he looked up and saw Lazarus in the bosom of father Abraham, and this rich man cried father Abraham, said the father, Lazarus, because this […] the poor man, of Lazarus, a little […] dip in water, and cool it on the rich man's tongue […] […] the soul of the rich man; and from […] for ever, of the rich man. And then father Abraham: this rich man, son of the Father, this rich man had good things […] he is Lazarus was […] […] the people; in turn this rich man was rich […] […] this rich man, Lazarus took the crumbs that fell […] the rich man's table; the rich man took […] the rich man, Lazarus […]

  1  who do, Lazarus angel father heaven and then-exist this
  2  rich die and this-~rich [...] inside ~evil bury and then-exist
  3  suffer inside ~evil this ~rich see ~trespass-~rich and see Lazarus
  4  inside öl father Abraham and shout this rich
  5  father Abraham say-father Lazarus because-this from-understand the_poor_man/woman* | <preposition_of_genitive>
  6  Lazarus little finger immerge water and cool
  7  on-<preposition_of_genitive>-rich tongue [...] flame* soul <preposition_of_genitive>-rich and from
  8  [remember] exist-exist-chapter <preposition_of_genitive>-rich and_then father Abraham | this
  9  ~rich son <preposition_of_genitive>-father-<suffix_of_divine_name> this-~rich good [...] he_is*
 10  Lazarus exist [...] [...] people* in_turn this-~rich exist
 11  rich blind* [...] this-~rich grab-Lazarus trespass from crumbs
 12  the_dogs* [?]-~rich throne ~rich grab [...] ~rich Lazarus take

## 090r — a great gulf fixed, and they have Moses and the prophets

> said father Abraham, take Lazarus […] […] the people. And then father Abraham: a great chasm between the rich man […] or […] this is the netherworld, most high, evil upon evil; who cries, this […] father Abraham; and Lazarus […] in the bosom of father Abraham; and a second time this rich man cried, father Abraham, send Lazarus […] […] […] the rich man has, the trespass, these two, of the rich man brethren, because the brethren […] of the rich man, how in this rich man's suffering because these brethren, the man sins, from […] then is damned the man, as the rich man, this rich man is damned. Said father Abraham, they have the brethren, the trespass, this prophet, and preaching, because this prophet preaches evil; the man, the brethren […] and a third time he cried, this

  1  say father Abraham grab-Lazarus [...] opposite people* and_then
  2  father Abraham many chasm among-~rich-[?] or [...]
  3  this_is netherworld most_high ~evil on-~evil who-shout this-[?]
  4  father Abraham and Lazarus [...] inside öl father
  5  Abraham and two who-shout this-~rich father-<suffix_of_divine_name> Abraham
  6  go Lazarus [great_gulf] opposite world have-~rich trespass this-two-two <preposition_of_genitive>-rich
  7  ~exist-exist because ~exist-exist say-Lazarus from-~rich how? inside this-rich suffer
  8  because this ~exist-exist somebody sin from [...] then-exist be_damned
  9  somebody how?-rich this-rich be_damned say father-<suffix_of_divine_name> Abraham have
 10  exist-exist trespass this prophet and preach because this prophet preach
 11  evil somebody brother be_damned* and three who-shout this

## 090v — neither will they be persuaded, though one rose from the dead

> the rich man; father Abraham […] the prophet preaches, believe […] […] good, the man Lazarus, believing and the body rose from the dead, the poor man. Said father Abraham, in turn who […] the brethren, the prophet, let the brethren believe, and the preaching and good, from the man […] […] the brethren believe; and the body rose from the dead, the man Lazarus […] this holy day. Here ends this holy gospel. Here begins this holy gospel, written by holy John, in the second chapter of his writing. At that time Nicodemus came by night to Lord Jesus, because he feared the Jews; and […] to the Lord he came

  1  rich father-<suffix_of_divine_name> Abraham name-°vanished-from prophet preach believe [...]
  2  [...] good somebody-Lazarus believe-exist-exist
  3  and body from die stand_up-somebody-?the_poor_man/woman say father-<suffix_of_divine_name> Abraham in_turn-who cannot*
  4  brother prophet believe-brother-somebody and preach
  5  and good from somebody-+the_Baptist/woman-[?] cannot* exist-exist believe and body
  6  from die stand_up-somebody-Lazarus [?]-this-holy-+day end this holy-gospel
  7  begins this holy-gospel write
  8  holy-John inside two chapter | <preposition_of_genitive>
  9  write time go Nicodemus
 10  inside night to-Lord-Jézus
 11  because ~have Jew(ish) and
 12  not_want to-Lord go-this

## 091r — except a man be born again

> but by night to the Lord came Nicodemus. And then Nicodemus: O. Nicodemus answered, this Nicodemus, this Lord Nicodemus believes. […] this Lord is truly the Son of the living God, because this Lord goes to heaven. In turn […] and the Lord, this Lord truly the Son of the living God. And then Lord Jesus, Nicodemus […] […] this Lord to you speaks: and the man […] who believes in the Lord […] a second time is born into this world, that one man is saved; but every man is damned. Said Nicodemus, answering, how can this be, who a second time a second time from his mother goes, Nicodemus, and a second time is born into this world? For this, thanks. Said Lord Jesus, Nicodemus […] this Lord, this

  1  a) inside night to-Lord go-Nicodemus and_then Nicodemus oh.
  2  <preposition_of_genitive>-Nicodemus answered this-Nicodemus this-Lord believe-Nicodemus.
  3  that this-Lord righteous(ly) son living God because this-Lord go on-heaven.
  4  in_turn-[?] and-Lord this-Lord righteous(ly) son living God and_then.
  5  Lord-Jézus Nicodemus verily verily this-Lord you.
  6  speak and somebody cannot* exist to-Lord believe born_again* two.
  7  be_born on-this world* one somebody be_saved a) each,_every-somebody
  8  be_damned say Nicodemus answered how?-this can exist who to-two-before
  9  two from <preposition_of_genitive> mother go-Nicodemus and two be_born-Nicodemus on-this world.*
 10  this thanks say Lord-Jézus Nicodemus speak* this-Lord this-donkey-to

## 091v — born of water and of the Spirit, and God so loved the world

> this host, this Nicodemus, a second time born of his mother; but this Lord speaks: then, born a second time, the man Nicodemus, of water and of the Holy Spirit, that one man Nicodemus is saved; but every man Nicodemus is damned. Said Lord Jesus, Nicodemus, in turn then this Lord to you began, the Lord, to preach of heaven and earth, how you from […] left, Nicodemus the man; then can this world, Nicodemus, the man […] he left, the brethren; this Lord to you preached, said the Lord Jesus, Nicodemus: so did you love the Father, his God of heaven but the Father's only begotten Son, Jesus, that is, to the Lord, so did you love the Father, said Lord Jesus; and […] and the man, the Lord

  1  this host this-Nicodemus two be_born from <preposition_of_genitive>-Nicodemus mother a)
  2  this-Lord speak then two be_born-somebody-Nicodemus from water and
  3  from holy-spirit one somebody-Nicodemus be_saved a)
  4  each,_every-somebody-Nicodemus be_damned say Lord-Jézus Nicodemus in_turn | then
  5  exist this-Lord you begin-Lord preach from-heaven
  6  land how? you from enter* | leave-Nicodemus
  7  somebody then-exist this world* can Nicodemus-somebody enter*
  8  leave-to-leave brethren* this-Lord you preach-Lord say | Lord
  9  Jézus Nicodemus [?]-+one you love father <preposition_of_genitive>-Lord God heaven
 10  a) <preposition_of_genitive>-father-<suffix_of_divine_name> only_one son Jézus that_is to-Lord [?]-+one
 11  you love father-<suffix_of_divine_name> say Lord-Jézus and [...] and somebody Lord

## 092r — that whosoever believeth should not perish

> believes in the Son of the Father, the only begotten, Lord Jesus Christ, and one man Nicodemus is saved; but every man Nicodemus is damned. Said Lord Jesus, Nicodemus […] to the Lord goes the Father, his God of heaven; he loved this Lord; this people he judges, but rather to the Lord goes the Father, the brethren, this Lord saved this world by his death; and […] is, to the Lord believes, this man Nicodemus, and his Father believes more than these; this one, one God. Said Lord Jesus […] one […] among you […] from the dog and […] […] […] not; and said Lord Jesus, and the man Nicodemus who does evil among you

  1  believe son <preposition_of_genitive>-father-<suffix_of_divine_name> only_one Lord-Jézus-Christ and one
  2  somebody-Nicodemus be_saved a) each,_every-somebody-Nicodemus be_damned say
  3  Lord-Jézus Nicodemus [...] to-Lord go father <preposition_of_genitive>-Lord God heaven
  4  love this-Lord this people* judge but_rather* to-Lord go father-<suffix_of_divine_name> brethren* this-Lord
  5  this world* be_saved on-<preposition_of_genitive>-Lord die and man* exist to-Lord
  6  believe this somebody-Nicodemus exist and <preposition_of_genitive>-Lord father-<suffix_of_divine_name>
  7  believe more_than_these* this one one God say Lord-Jézus [...]
  8  one ~exist-[?] among you [...] from
  9  dog and [...] [...] [...] not and say
 10  Lord-Jézus and <subject_marker> do_evil-somebody-Nicodemus among you

## 092v — men loved darkness rather than light

> from the man Nicodemus who will not come to the light, but loves the darkness, the man Nicodemus; said Lord Jesus, and the true man Nicodemus, from the man Nicodemus, the light, the man Nicodemus loves, and all come to the light the man Nicodemus. Here ends this holy gospel. The Lord, with all thy heart, Lord. Here begins this holy gospel written by holy Luke in the fourteenth […] in his writing. At that time Lord Jesus said to his apostles and to the Jewish people: then a rich lord made, one rich man, many […]

  1  from somebody-Nicodemus not_want on-light go a) darkness love
  2  somebody-Nicodemus say Lord-Jézus and <subject_marker> righteous(ly)-somebody-Nicodemus from
  3  somebody-Nicodemus light love-somebody-Nicodemus and each,_every on-light | go
  4  somebody-Nicodemus end this holy-gospel Lord-<suffix_of_divine_name> with_all_thy_heart* Lord
  5  begins this holy-gospel
  6  write holy-Luke inside
  7  14 chapter inside | <preposition_of_genitive>
  8  write time
  9  say Lord-Jézus apostle
 10  <preposition_of_genitive>-Lord and Jew(ish)
 11  people-chapter | then-exist
 12  rich-Lord-<suffix_of_divine_name> do, one rich somebody many dinner

## 093r — a certain man made a great supper, and bade many

> And then the rich lord, among the rich lord's, the redeemer's day, three […] upon this […] said this rich lord to his living servant, go […] speak this word, go, the man; at that time all is finished, say. This living servant, this […] […] lo, the living servant. Go to the rich lord's living man […] then the lord […] of the lord […] said this first: not. […] because […] a piece of ploughland; I must […] go and see it, and I must, the ploughland […] he asks […] to speak […] he is to […] the lord; and said this second, lo. The living servant goes, the lord's living servant, this man

  1  and then-exist-rich-Lord-<suffix_of_divine_name> among-rich-Lord-<suffix_of_divine_name> redeemer-+day three friend.
  2  on-this dinner say this-rich-Lord-<suffix_of_divine_name> <preposition_of_genitive>-Lord living-servant go-[?].
  3  this word speak-angel go-somebody time <subject_marker> each,_every finished say.
  4  this-living-servant this living-+one man* lo living-servant.
  5  go <preposition_of_genitive>-living-somebody-Lord-<suffix_of_divine_name> this-?man then-chapter-Lord-<suffix_of_divine_name> go-?man
  6  <preposition_of_genitive>-Lord-<suffix_of_divine_name> dinner say this first this-?man not.
  7  can-?man because buy-?man plough_land | want
  8  man* <subject_marker> -anus-go see and want plough_land [...]
  9  ask_(for) this-+servant to-speak man* exist-to
 10  <preposition_of_genitive>-living-+servant Lord-<suffix_of_divine_name> and say this two sense lo.
 11  living-servant go <preposition_of_genitive>-living-servant Lord-<suffix_of_divine_name> this-somebody-sense

## 093v — I have bought five yoke of oxen

> then the lord; the man goes, of the lord […] said this second man, this man cannot the man cannot, because the man has bought five yoke of oxen […] the man must the man goes […] the man must […] thanks; he can […] […] […] […] believe; this living servant, to speak the man, before […] the lord said this third man, lo, the living servant goes, the lord's living servant the lord; this third man, then the lord, the man goes of the lord […] said this third, this man

  1  then-chapter-Lord-<suffix_of_divine_name> go-somebody-sense <preposition_of_genitive>-Lord-<suffix_of_divine_name> dinner say this
  2  two somebody-sense this-somebody-sense not
  3  can-somebody-sense because buy-somebody-sense
  4  five yoke sense ox want-somebody-sense
  5  go-somebody-sense in_the_field* want-somebody-sense
  6  <subject_marker> ox thanks exist can ox | [...]
  7  [...] [...] believe this-living-~servant to-speak
  8  somebody-sense before <preposition_of_genitive>-living-+servant Lord-<suffix_of_divine_name> say
  9  this three somebody-thief lo living-servant go <preposition_of_genitive>-living-servant
 10  Lord-<suffix_of_divine_name> this-somebody-thief then-chapter-Lord-<suffix_of_divine_name> go-somebody-thief
 11  <preposition_of_genitive>-Lord-<suffix_of_divine_name> dinner say this three thief this-somebody-thief

## 094r — go out into the highways and hedges

> the man cannot, and the man must go because the man must go, he has married; this man cannot the man cannot, and the man must go, and this and that the man […] said, to speak, the man is to of […] the lord; and then, and one goes, the man […] upon this, to the supper, said this lord, that is, the people; and the people spoke of the lord […] and the lord said to the living servant, go out into the roadside and the way and into the town, and to the town gate, and. […] within, the one-eyed, the blind, to be […] the body hungry, and […] within the one-eyed, and […]

  1  not can-somebody-thief and to-go-somebody-thief
  2  because to-go-somebody-thief marry this-somebody-thief not
  3  can somebody-thief and to-go-somebody-thief and this-and-this
  4  somebody-thief [...] say to-speak somebody-thief exist-to
  5  <preposition_of_genitive>-[?] Lord-<suffix_of_divine_name> and then-exist and one | go-somebody
  6  man* on-this to-dinner-to say this
  7  Lord-<suffix_of_divine_name> that_is people-chapter and people-chapter from-speak <preposition_of_genitive>-Lord-<suffix_of_divine_name> dinner
  8  and say <preposition_of_genitive>-Lord-<suffix_of_divine_name> living-servant go on-(on_the)_roadside and on-way
  9  and on-town and on-gate town and.
 10  find-[?] inside only_one-+day-~exist blind-eye | to-exist-chapter
 11  [...] body be_hungry and thirst inside only_one-+day-~exist and [?]-?first.

## 094v — blessed is he that shall eat bread in the kingdom of God

> […] he found; every man went, the angel, into the lord's house said this living servant, the angel, Lord, it is done; and the mountain top, which the Lord said […] said this living servant, the angel […] one to the place, and to the place the living servant would go out and then there rose at the table one Jew, and cried out: blessed is he, from within the one-eyed, the blind, because the one-eyed, of the blind, heaven and earth; and said Lord Jesus truly, speaking to the Jew, more than these, within the one-eyed, heaven and earth. And then this rich man, the lord […] […] many, to go, the mouth […] the thief upon the rich lord's […] Here ends this holy gospel.

  1  man* find each,_every somebody go-angel inside <preposition_of_genitive>-Lord-<suffix_of_divine_name> house
  2  say this living-servant-angel Lord do, and mountain_peak who-Lord
  3  say [...] say this living-servant-angel servant*
  4  one to-place and to-place want living-servant-angel on-out(ward)
  5  and then-exist rise to-throne one Jew(ish) and
  6  shout-to happy from inside only_one-+day-~exist blind-eye because
  7  only_one-+day-~exist <preposition_of_genitive>-blind-eye heaven land and say | Lord
  8  Jézus righteous(ly) speak-Jew(ish) more_than_these* inside only_one-+day-~exist heaven
  9  land and_then this-rich somebody-Lord-<suffix_of_divine_name> [...] [...]
 10  many to-go-mouth | man-[?]-somebody
 11  thief on-<preposition_of_genitive>-somebody-rich-Lord-<suffix_of_divine_name> dinner end this holy-gospel

## 095r — the bread blessed at the supper

> Here begins this holy gospel written by holy John in the sixth chapter of his writing. At that time Lord Jesus said to his apostles and the Jewish people: ye shall eat of his, for ever, and of his shall ye drink. And then Lord Jesus, with his apostles, at the last supper, this at the last supper; and Lord Jesus took, in turn, one baked cake, and Lord Jesus blessed this bread and […] before the Lord, Lord Jesus put it. And

  1  begins this holy-gospel
  2  write holy-John
  3  inside six chapter <preposition_of_genitive>-write
  4  time say Lord-Jézus
  5  apostle <preposition_of_genitive>-Lord and Jew(ish)
  6  people-chapter you
  7  exist <preposition_of_genitive>-Lord exist-exist-chapter
  8  eat and <preposition_of_genitive>-Lord to-to-this
  9  drink and_then Lord-Jézus apostle <preposition_of_genitive>-Lord last dinner-to this
 10  on-last dinner and grab Lord-Jézus inside why?-in_turn one baked
 11  „cake” and blessed Lord-Jézus this bread.
 12  and bread before Lord put Lord-Jézus and.

## 095v — except ye eat my flesh and drink my blood

> Lord Jesus took wine, one cup, and water into the cup poured, and Lord Jesus blessed the wine and the water; and the wine and water before the Lord, Lord Jesus put. And then Lord Jesus: and the man who eats this bread, this man is called his own […] and the man […] who eats this bread […] believes in the Lord every man is damned […] and the man who believes in the Lord […] from the altar, from the thirty, the holy host eats […] […] every man shall be living, for ever, amen. And then the Jews: how can this be, his own, to be eaten, and his

  1  grab Lord-Jézus wine one cup and water inside cup
  2  pour and blessed Lord-Jézus wine and water and
  3  wine water before Lord put Lord-Jézus and_then | Lord
  4  Jézus and somebody exist this bread eat this somebody
  5  exist <preposition_of_genitive>-Lord shall_be_called* from-+who-chapter and somebody exist
  6  this bread eat and Lord believe
  7  each,_every somebody be_damned cut_off-[?] and somebody exist Lord believe
  8  and from altar(table) exist from thirty holy-host
  9  eat and drink each,_every somebody exist
 10  living chapter-oh chapter-oh amen and_then Jew(ish)
 11  how? exist-+say <preposition_of_genitive>-Lord shall_be_called* eat and <preposition_of_genitive>-Lord

## 096r — whoso eateth my flesh hath eternal life

> drink of this? This pleasing, which this Lord speaks, because food the Jews, who […] […] and his body to eat and to drink of it; which is hidden, said this Lord Jesus, who is the Lord […] but said Lord Jesus, believe; then the man believes in the Lord, to the Lord, he who is truly the Son of the living God. And then Lord Jesus: his own, this is truly to eat, and of his, this is truly to drink And then Lord Jesus: then the man who eats this bread is a man, an apostle […] upon his, never […] is from eating, how the bread of […]

  1  to-to-this drink this pleasing who this-Lord speak because food
  2  Jew(ish) who-[?] strive* and <preposition_of_genitive>-Lord body eat
  3  and to-to-this drink which-hide_oneself say this Lord-Jézus who-Lord-exist
  4  strive* a) say Lord-Jézus to-believe then-exist
  5  believe-somebody inside Lord to-Lord this-?he_who righteous(ly) son
  6  living God and_then Lord-Jézus <preposition_of_genitive>-Lord shall_be_called* this_is
  7  righteous(ly) eat and <preposition_of_genitive>-Lord to-to-this this_is righteous(ly) drink
  8  and_then Lord-Jézus then-exist somebody this bread eat
  9  exist somebody apostle [...] on-<preposition_of_genitive>-Lord not-not [...]
 10  exist from eat how? bread <preposition_of_genitive>-[?]

## 096v — I am the living bread which came down from heaven

> your fathers did eat in […] because that is the bread of life; he who goes, the Lord, the Lord's bread; in turn he left the eternal town from that day, upon this world; and the man who eats this bread from him, the man shall live for ever, amen and this Lord, this […] because the Lord, this Lord goes the Lord from his Father, upon this world; and this Lord to his Father, the living Lord; and the man who in the Lord believes, from him the man lives to the Lord, for ever […] and the man who is within the Lord's law of love, carried by the Lord, stays; and this Lord is

  1  you father eat inside field because that_is bread
  2  living he_who go-Lord bread-Lord in_turn leave from_the_eternal* | town
  3  from-+day on-this world* and somebody exist this bread eat
  4  from somebody exist living chapter-oh chapter-oh amen
  5  and this-Lord this bread because-Lord this-Lord | go
  6  Lord from <preposition_of_genitive>-Lord from-father-<suffix_of_divine_name> on-this world* and this-Lord
  7  to-<preposition_of_genitive>-Lord from-father living-Lord and somebody exist Lord.
  8  believe from somebody exist to-Lord living chapter-oh
  9  chapter-oh man* and somebody exist
 10  inside Lord-+law-love-~carry-Lord stay and this-Lord exist

## 097r — he that dwelleth in me, and I in him

> within […] and the man who carries his commandment, from the man who is in the Lord, from the Lord's law of love, carried by the Lord, stays; and this Lord is within […] And then Lord Jesus […] the man, and the man who is within the Lord, the Father, the Son, God, Jesus, the Holy Spirit, Mary, Christ, the apostles, the angels […] stays; the Lord, the Father, the Son, God would have Jesus, the Holy Spirit, Mary, Christ, the apostles, the angels go; and the man goes, the Lord, the Father, the Son, God, Jesus, the Holy Spirit, Mary, Christ, the apostles, the angels into the heavenly land. And then Lord Jesus, and this man would have the Lord, the Father, the Son, God, Jesus, the Holy Spirit, Mary, Christ, the apostles, the angels take his house, at the Lord's, the Father's, the Son's, God's, Jesus', the Holy Spirit's

  1  inside somebody and somebody exist <preposition_of_genitive>-Lord commandment carry from somebody
  2  exist inside Lord from Lord-+law-love-~carry-Lord stay and this-Lord exist
  3  inside somebody and_then Lord-Jézus [...] somebody and somebody exist
  4  inside Lord-father-<suffix_of_divine_name>-son-God-Jézus-holy-spirit-Mary-Christ-apostle-angel
  5  [?]-stay | want-Lord-father-<suffix_of_divine_name>-son-God
  6  Jézus-holy-spirit-Mary-Christ-apostle-angel go and somebody
  7  go-Lord-father-<suffix_of_divine_name>-son-God-Jézus-holy-spirit-Mary-Christ-apostle-angel
  8  inside heavenly land and_then Lord-Jézus and this somebody
  9  want-Lord-father-<suffix_of_divine_name>-son-God-Jézus-holy-spirit-Mary-Christ-apostle-angel
 10  house grab at | <preposition_of_genitive>-Lord-father-<suffix_of_divine_name>-son-God-Jézus-holy-spirit

## 097v — the whole company of heaven, and the host

> Mary, Christ, the apostles, the angels; from God the Father, hidden, through staying the man, for ever, amen. And then Lord Jesus, and the man who from the altar, from the thirty, the holy host eats […] from him the man lives, for ever, amen. Here ends this holy gospel. The Lord, with all thy heart. Here begins this holy gospel written by holy Luke, in the […] chapter of his writing. Then Lord Jesus, in the thirtieth day and in the first year; at that time he left

  1  Mary-Christ-apostle-angel from-father-God to-hide_oneself-exist through stay
  2  somebody chapter-oh chapter-oh amen and_then Lord-Jézus and
  3  somebody exist from altar(table) from thirty holy-host
  4  eat [...] from somebody exist living-somebody chapter-oh
  5  chapter-oh amen end this holy-gospel Lord-?with_all_thy_heart
  6  begins this holy-gospel
  7  write holy-Luke inside
  8  and chapter <preposition_of_genitive>-write
  9  then-exist Lord-Jézus inside
 10  thirty day and inside one
 11  year time leave-to-leave

## 098r — the light of the body is the eye

> Lord Jesus […] among the chief of the Jews, and his apostles And then Lord Jesus, to his apostles and the Jewish people […] have mercy […] the eye […] […] of the apostles the man said, the eye. And then Lord Jesus, the eye of […] the man, this is the lamp of […] and the lamp of the apostles the man said, this is for ever, of […] and in turn, it is within […] for ever […] one the heart, sin protruding, is all of […] for ever darkness. And then Lord Jesus, in turn who […] […] sins against the Lord, from God the Father, from the heart; he would, from the Father

  1  Lord-Jézus [...] among Jew(ish) head and <preposition_of_genitive>-Lord apostle
  2  and_then Lord-Jézus apostle <preposition_of_genitive>-Lord and Jew(ish) people-+day [...]
  3  have_mercy-+<subject_marker> <preposition_of_genitive>-[?] eye-from [...] [...] | <preposition_of_genitive>-apostle
  4  say-somebody eye-from and_then Lord-Jézus eye-from | <preposition_of_genitive>-[?]
  5  somebody this_is lamp <preposition_of_genitive>-[?] and lamp | <preposition_of_genitive>-apostle
  6  say-somebody this_is exist-exist-chapter <preposition_of_genitive>-[?] and
  7  in_turn exist inside <preposition_of_genitive>-[?] exist-exist-chapter remain* one
  8  heart sin protrude exist each,_every <preposition_of_genitive>-[?] exist-exist-chapter
  9  darkness and_then Lord-Jézus in_turn-who [...] [...]
 10  sin against <preposition_of_genitive>-Lord from-father God from heart want from-father

## 098v — a candle set on a candlestick

> his scourges, various, of the ass. And then Lord Jesus, this hidden is within […] for ever; every […] is clean all of […] for ever, light. And then Lord Jesus, how then […] the lamp gives light, to the light; the lamp, a hundred, gives light, of […] for ever. Here ends this holy gospel. The Lord with all thy heart; the Lord have mercy; and truly speaks holy John: God can bear the sky and the earth; to this speaks holy John, the Lord God; and the man who bears the living man upon this world, and healing

  1  <preposition_of_genitive>-Lord whip-whip various from-donkey and_then Lord-Jézus this-hide_oneself
  2  exist inside <preposition_of_genitive>-[?] exist-exist-chapter each,_every heart clean exist
  3  each,_every <preposition_of_genitive>-[?] exist-exist-chapter light and_then Lord-Jézus
  4  how? then-exist [?]-[?] lamp light to-+<subject_marker>
  5  light lamp hundred exist light <preposition_of_genitive>-[?] exist-exist-chapter
  6  end this holy-gospel Lord-<suffix_of_divine_name> with_all_thy_heart* Lord-<suffix_of_divine_name> <subject_marker> have_mercy and righteous(ly)
  7  speak holy-John God
  8  can carry sky
  9  and earth to-this
 10  speak holy-John Lord
 11  God and somebody carry living
 12  somebody on-this world* and healing

## 099r — he that dwelleth in love dwelleth in God

> the man receives, and God receives the man […] the man, God. To this the man has: the Lord God, Jesus Christ, the Son of God; and the Lord, the Lord's head, heaven and earth; and love his brother as thy neighbour. In turn […] the holy man; the man has wealth, he sees; trespass; the unseen God; and the man […] has God, the man loves the holy man as thy neighbour. Of whosoever is holy, one, the kingdom of heaven, speaks holy Matthew; and the man […] says: this man loves God. In turn, of the holy man, his brother […] loves the holy man, from […]

  1  somebody grab and God somebody grab [...] somebody God | to
  2  this have somebody Lord-<suffix_of_divine_name> Jézus Christ son <preposition_of_genitive>-God
  3  and Lord ~head-Lord heaven and earth
  4  and love <preposition_of_genitive>-somebody father son how?-to somebody neighbour
  5  in_turn [...] ~rich somebody have somebody wealth see
  6  trespass blind God and somebody [...] have God somebody
  7  <subject_marker> love-rich-somebody how?-to somebody neighbour exist | <preposition_of_genitive>
  8  whosoever-rich-+one heaven land speak holy-~Matthew and
  9  somebody [...] say this-somebody God love in_turn | <preposition_of_genitive>-rich.
 10  somebody father son hateth love-rich-somebody from [...]

## 099v — if a man say, I love God, and hateth his brother, he is a liar

> he is a liar; how does this man love God, in turn, of his brother […] loves God […] the Most High, this he sees. the man, in turn, his brother he sees; whosoever […] the son […] the man loves; how does this man love God, this pleasing; in turn the rich man would love God; first love, of the rich man, his brother, as the holy man, the holy man's neighbour, God and good; the rich man is loved […] […] the eternal land, the evil […] the rich man sees, saved the rich man is, for ever, amen. In turn who is the rich man; the Lord, the apostles, love every man as the rich man

  1  one liar exist how? this somebody God love in_turn | <preposition_of_genitive>
  2  somebody father son hateth love God [...] high-this see.
  3  somebody in_turn <preposition_of_genitive>-somebody father son see whosoever* hateth
  4  son hateth love-somebody how? this-somebody God love this
  5  pleasing in_turn want-rich-somebody God love first love | <preposition_of_genitive>-rich
  6  somebody father son how?-to rich-somebody rich-+neighbour God
  7  and good exist somebody-~rich love [?]-[?] eternal*
  8  land ~evil [...] see-rich-somebody | be_saved
  9  rich-somebody exist chapter-oh chapter-oh amen.
 10  in_turn-who-exist rich-somebody Lord apostle love each,_every somebody how?-to rich-somebody

## 100r — Elijah taken up by fire, and the list of miracles

> the neighbour is of the holy man; the eternal kingdom […] the holy man, from […] the Lord, from the Father and the Son and the Holy Spirit. Elijah the prophet was taken, by fire, into heaven. Various miracles: afterward the blind eyes, through light [saw]; the dead were raised up; the lame [walked]; the body, and the possessed of the evil one, were healed. Elijah? Who? and this, and this miracle: did Elijah do it? writes the church father, the scholar […] First writes the scholar […]; the church father […] Elijah.

  1  neighbour exist <preposition_of_genitive>-rich-somebody eternal* land [...]
  2  rich somebody from [...] Lord from father-<suffix_of_divine_name> and son and holy-spirit
  3  Elijah prophet grab
  4  fire on-+heaven
  5  various miracle
  6  afterward* blind eye
  7  <subject_marker> through light die <subject_marker>
  8  raised_up* lame
  9  body and evil obsessed_by_the_evil <subject_marker> from-healing Elijah | who-and-this
 10  and-this miracle do, Elijah write church_father scholar pagan
 11  first write scholar pagan church_father [...] Elijah

## 100v — the fathers on the sepulchre, a chronology, and the temple of forty-six years

> the sepulchre; to heaven; on earth; on that, writes […] […] the church father, on that, writes: the Most High hid himself, and from […] the scholar. […] the church father, on that, writes the scholar […] the Pharisees. And the church father writes this three; and Saint Augustine the church father: Elijah the Lord God [heart-Lord] first, but rather [heart-Lord] the sun and the moon, and there is living Elijah; to Elijah, two; then, from Adam [heart-Lord] fifty; and on this man […] seven people. Then is this man five hundred and thirty. In the thirtieth year, then: "destroy", the Lord; five towns; and then on this: "destroy", forty years and six years.

  1  burial_chamber to-+heaven on-earth on-that_is write [...]
  2  pagan church_father on-that_is write high-hide_oneself-and-from scholar.
  3  pagan church_father on-that_is write scholar pagan Pharisees*
  4  and church_father this three write and Saint_Augustine_the_church_father Elijah
  5  Lord-<suffix_of_divine_name> heart-Lord first but_rather heart-Lord sun and moon
  6  and exist living Elijah to Elijah two then-exist from
  7  Adam heart-Lord fifty and on-this somebody [...] seven
  8  people-chapter time exist this somebody five_hundred and
  9  thirty thirty-+day time destroy Lord-<suffix_of_divine_name> five
 10  town and then-exist on-this destroy two-two-ten-year and six-year

## 101r — Elijah's fire, and Enoch and Elijah kept for Antichrist

> Then holy Elijah knelt down and prayed to the Lord God; to fire; and took; the angel of God said, the angel of God, to Elijah: this is the angel of the Lord; and this man from […] And Elijah, the man, from […] […] […] and Elijah, the man, was taken up into heaven […] and […]. Elijah, the man […] from the day; Noah and Elijah shall bear the sword; the evil one […] and […] […] Noah and Elijah on the earth. […] […] shall be born; two; the chief evil, the evil one, and the son of the devil; and there is […] evil, who is Antichrist.

  1  time kneel_(down) holy-+Elijah and pray Lord-<suffix_of_divine_name> | to
  2  fire and grab God angel say God angel Elijah
  3  this exist-<preposition_of_genitive>-angel Lord-<suffix_of_divine_name> and this somebody from-exist
  4  and Elijah-somebody from-leave-to-leave [...] [...] and
  5  Elijah-somebody get_raptured heaven most_high and gate/open | Elijah
  6  somebody man* from-+day Noah Elijah sword carry
  7  ~evil one-+gate/open and [Enoch] leave-to-leave Noah Elijah on-earth
  8  [...] [...] through be_born two ~head-evil ~evil
  9  and son hide_oneself-angel and exist-[?] evil exist Antichrist

## 101v — the opening of a reading from Luke: Simeon

> Before the gospel, says holy Luke: thanks to the Lord, the Lord God, thanks be; of the Lord, holy mercy, Lord; this Lord, the gate, Lord; of the Lord, many homes. Before, many holy fathers before, many, writes […] the church father: heaven; the Lord's Son […] the Lord taken; to see one […] because many holy fathers wanted to see the Lord Jesus Christ […] The Lord's chapter: many; how shall we see? In turn, Simeon; one, Simeon.

  1  before gospel speak
  2  holy-Luke to-Lord thanks
  3  Lord God thanks exist
  4  <preposition_of_genitive>-Lord holy-have_mercy Lord
  5  this Lord gate Lord
  6  <preposition_of_genitive>-Lord many home
  7  before many holy-father-before many write church_father church_father
  8  heaven Lord son <subject_marker> grab-Lord see one [...]
  9  because because many holy-father want see Lord-Jézus-Christ [...]
 10  Lord-chapter many how_shall_we* see a) Simeon one-Simeon

## 102r — Simeon's arms, and the thirtieth year

> and shall be called; it is Simeon; for Simeon carried him in his bosom: the Lord Jesus Christ […]. The Lord saw the apostles and the Jewish people, and these apostles, the Jews, the Lord; all saw within […] of the name of the man. Then was the Lord Jesus within his thirtieth year. Then, from the woman, the Lord Jesus; and the Lord went from town to town, from temple to temple, from field to field; and the Lord's apostles went into the world; the gospel the Lord preached; various miracles the Lord did afterward: […] […] the Lord: through light [the blind saw]; the dead the Lord raised up; the lame [walked];

  1  and shall_be_called* exist Simeon because from Simeon carry bosom
  2  Lord-Jézus-Christ [...] Lord see apostle and Jew(ish) people-chapter and
  3  this apostle Jew(ish) Lord each,_every see inside [?]-from-+name somebody
  4  time then-exist Lord-Jézus inside thirty year time
  5  from-woman-woman Lord-Jézus and go-Lord from town
  6  until town from temple until temple from
  7  plough_land until plough_land and <preposition_of_genitive>-Lord apostle go-Lord into_the_world* gospel
  8  preach-Lord various miracle afterward-Lord | blind*
  9  blind* <subject_marker>-Lord through light-Lord die raised_up_(by_the_Lord)* lame*

## 102v — the Passion in short: the sun darkened, the rocks rent

> the body, and the possessed of the evil one, the Lord healed. And the Lord suffered for man's sin, the good of the whole world; the cross […]; and for man of the Lord; to the thief, who […]; and the Lord redeemed man from hell fire. And then the Lord, the cross […] […] […] and the moon, this darkened, before the sun darkened; and before the moon darkened, the face of the earth quaked; the rock, the stone rent; and at the sun's darkening every creature […] this humbled itself, and every creature mourned. Then Christ, the cross […]; and the Lord was put in the sepulchre.

  1  body and evil obsessed_by_the_evil from-healing-Lord and suffer <subject_marker> Lord to
  2  somebody-sin good the_whole_wide_world cross-[?] and to-somebody
  3  <subject_marker> <preposition_of_genitive>-Lord to-to-thief-who and somebody redeem-Lord from hell
  4  fire and then-exist-Lord cross-[?] | sun*
  5  Lord-+name and moon this eclipse before sun eclipse
  6  and before moon eclipse [?]-earth quake rock
  7  stone rent and on-sun eclipse each,_every
  8  creatures* on-+world this humble and each,_every create mourn
  9  then-exist Christ cross-[?] ~and Lord inside burial_chamber | put

## 103r — the three days: where was the soul?

> said; and then the Lord lay in the sepulchre, the Lord; and the hour, then, went to the Father, God, heaven; to the Father's; the angel; the soul within […] the Lord Jesus, and rose from prayer(?). In turn: the devil in the sepulchre stayed; in turn, the Lord went to hell, and destroyed hell, and redeemed man; hell fire, because | he carried, the Lord, his cross on his shoulder; and man's soul […] of the Lord the Father, all the world, the people. And then the Lord Jesus, from the Father, the Lord God eternal; the soul […] of this Father, this soul

  1  say and then-exist-Lord inside burial_chamber lay-Lord and hour time
  2  go from-father God heaven on-<preposition_of_genitive>-father angel soul inside
  3  exist-[?] Lord-Jézus and rise* from pray
  4  in_turn angel inside burial_chamber stayed in_turn to-Lord go-Lord on-hell
  5  and hell destroy and somebody redeem-Lord fire hell because | carry
  6  Lord <preposition_of_genitive>-Lord cross on-<preposition_of_genitive>-Lord shoulder and somebody soul-[?]
  7  <preposition_of_genitive>-Lord father-<suffix_of_divine_name> each,_every the_whole_wide_world people* and_then Lord-Jézus | from
  8  father <preposition_of_genitive>-Lord God eternal* soul-[?] this-father-<suffix_of_divine_name> this soul

## 103v — the lost sheep, a doxology, and the names in one sign

> of the Lord; from the lost sheep this Lord's soul the Lord redeemed; the wolf; the face of the earth; this Father's soul; the lost sheep […] the Lord took; this Father's soul. […] […] until the ages of ages, amen. From every ghost, and from […] the Lord, from the heavenly, on this the people believe; woman, woman; and […] the Lord […] the angel. On […]-[…]-Mary-Jesus-God-Christ-angel-the-lost-sheep speaks Saint […], the church father. Holy Anne, this Anne, gave birth: […] […] […] to mercy, the commandment; go, on everyone, the whole world.

  1  <preposition_of_genitive>-Lord from-+the_lost_sheep this-Lord soul redeem-Lord wolf [?]-earth
  2  this-father-<suffix_of_divine_name> soul the_lost_sheep [...] grab-Lord this-father-<suffix_of_divine_name> soul
  3  redeem heavenly until chapter-oh chapter-oh
  4  amen from each,_every ghost and from [...] Lord from heavenly* on-this
  5  people* believe woman woman and [...] Lord [...] angel | on
  6  [?]-[?]-Mary-Jézus-God-Christ-angel-+the_lost_sheep
  7  speak Saint_[a_church_father] church_father | holy
  8  Anne_(mother_of_the_Virgin_Mary) this Anne_(mother_of_the_Virgin_Mary) be_born
  9  [...] [...] [...] <subject_marker>
 10  to-have_mercy commandment go on-each,_every the_whole_wide_world

## 104r — a creed, from Anne's daughter to the judgment

> the world, that is: then from Anne was born the blessed | Virgin Mary; from Mary the coming of the Lord Jesus Christ; and the Lord went into the world, preached the gospel, various miracles; afterward the Lord suffered for man's sin, for the whole world; the Lord was crucified, and for man the Lord shed his blood, and the Lord redeemed man from hell fire; and man, the Lord; there is the faith in the true Son of the living God: every man shall be saved; and one man shall be damned; and the Lord: he that believeth not, and […] one shall be saved; in turn, every man shall be damned.

  1  world* that_is then-exist from Anne_(mother_of_the_Virgin_Mary) be_born happy | virgin
  2  Mary from Mary coming* Lord-Jézus-Christ and from Lord go
  3  into_the_world* gospel preach various miracle afterward*
  4  Lord and suffer to somebody sin the_whole_wide_world crucified Lord and
  5  to somebody <subject_marker> <preposition_of_genitive>-Lord shed_his_blood and somebody <subject_marker> redeem-Lord
  6  from hell fire and somebody Lord exist believe-chapter
  7  to righteous(ly) son living God each,_every somebody be_saved and one
  8  somebody be_damned to and Lord not believe and [...]
  9  one to be_saved ~a) each,_every somebody be_damned

## 104v — blessed are the eyes which see

> Begins this holy gospel, written by holy Luke, in the tenth chapter of his writing. Then said | the Lord Jesus to his apostles and the Jewish people: blessed the two eyes, the two eyes that see the Lord; and you [see] those things which | the apostles see. He said: for many holy fathers, many, writes the church father, many prophets, many kings, many emperors | would have liked, the fathers, church fathers, prophets, kings, emperors, to see this which you […] from […]; and there rose among these Jews one; another church father wanted

  1  begins this holy-gospel
  2  write holy-Luke inside
  3  ten chapter <preposition_of_genitive>-write
  4  time say | Lord
  5  Jézus apostle <preposition_of_genitive>-Lord
  6  and Jew(ish) people-chapter
  7  to-happy two from
  8  eye-from to-two eye-from this Lord see who you those_things_which* | see-apostle
  9  say because many holy-father many write church_father many prophet many
 10  king many emperor | would_like_to-father-church_father-prophet-king-emperor
 11  this see who you [...] from-[?] and
 12  rise among this Jew(ish) one another church_father want

## 105r — the lawyer's question, and the great commandment

> tempted the Lord Jesus. And then this Jew answered, the lawyer […]: he who, says the scribe, must do; how? this […] to gain life for ever and ever. Said the Lord Jesus, this […]: […] he said: as the scripture is written, says this Jew, this scribe: as the scribe, the scripture is written, within the sixth chapter. Said the Lord Jesus, glad, this Lord, to this Jew: how readest thou the scripture? Right. And then this Jew, this reading, the scripture is written: love the Lord God most high with all thy heart, all thy soul, all thy might, all thy heart; and | thy neighbour as thyself, thy neighbour, the kingdom of heaven. And then the Lord Jesus spoke: right.

  1  tempt Lord-Jézus and_then this Jew(ish) answered learn-[?]
  2  he_who* say-church_father must do, how? this-[?] gain
  3  living chapter-oh chapter-oh say Lord-Jézus this-[?]
  4  [...] to-+say as* say the_scripture* write say this
  5  Jew(ish) this-church_father as* church_father the_scripture* write inside
  6  six chapter say Lord-Jézus joy this-Lord this-Jew(ish) how?
  7  contain the_scripture* righteous(ly) and_then this Jew(ish) this contain
  8  the_scripture* write love Lord-<suffix_of_divine_name> most_high ~each,_every heart each,_every <preposition_of_genitive>-somebody
  9  soul each,_every <preposition_of_genitive>-somebody might each,_every <preposition_of_genitive>-somebody heart and | <preposition_of_genitive>
 10  somebody exist-exist how?-to somebody neighbour <preposition_of_genitive>-somebody <subject_marker>
 11  heaven land and_then Lord-Jézus righteous(ly) speak

## 105v — who is my neighbour? A certain man went down to Jericho

> the Jew: for whoever believes in one God, to […] literally, love thy neighbour as thyself, thy neighbour; of […] heaven; in turn […]; and the man's mouth went on; and then […] proud, this Jew. And then he answered: who is my neighbour? […] said the Lord Jesus […] and said, as he said, the scripture, right: and from there was a living servant; through sin whosoever, a man, the Lord God; and exorcised(?); on the Lord's mercy; and then whosoever, the man, went into the wilderness, to one place […] Jericho; in turn, in turn; from evening to build(?); and then went the servant, the man, into the wilderness; and then fell among robbers.

  1  Jew(ish) because and somebody believe one God to-cut_off-literal
  2  love somebody <preposition_of_genitive>-somebody exist-~exist how?-to somebody neighbour
  3  <preposition_of_genitive>-[?] heaven in_turn-[?] and mouth somebody
  4  leave-leave and then-[?] proud this Jew(ish) and_then
  5  answered who? exist <preposition_of_genitive>-+say [?]-+day-~exist-<suffix_of_divine_name> say
  6  Lord-Jézus [...] to-+say as* who-+say the_scripture* righteous(ly)
  7  and from exist living-~servant through sin <preposition_of_genitive>-?whosoever-~Adam
  8  Lord-<suffix_of_divine_name> and exorcise on-<preposition_of_genitive>-Lord have_mercy and then-exist
  9  go-?whosoever-~Adam on-~field to-one place [...]
 10  Jericho in_turn-chapter-in_turn evening-from-to build-to and then-exist go
 11  ~servant ~Adam on-~field and then-exist fell_among robber

## 106r — stripped, half dead; the priest and the Levite pass by

> And the robbers began, to the man; the holy(?) found; and then these robbers let the man go, having taken the booty; and the robbers beat the man, this man dying; and half dead and half alive. That way went one, a descendant of Abraham, a priest's son; the man; on seeing, the descendant of Abraham passed the man by, and | went. The descendant of Abraham went. Then, second, began a descendant of the scripture, a Levite's son; the man […] the descendant of the scripture passed the man by, and went […] the man could; the two, of Abraham, of the scripture, good, afterward, passed the man by; through went the two of Abraham, that way.

  1  and begin robber to-~Adam ~rich ~find
  2  and then-exist this robber remit ~Adam grab
  3  booty and ~Adam beat robber
  4  die-this ~Adam and half_dead and half_alive
  5  that_way go ~on one descendant-Abraham son-to
  6  ~Adam on-see-descendant-Abraham long-~Adam and | go
  7  descendant-Abraham go ~on two ~begin descendant-?the_scripture son-to ~Adam
  8  [?]-descendant-?the_scripture long-~Adam and go [...]
  9  ~Adam can-two-Abraham-?the_scripture good afterward*
 10  long-~Adam through go-two-Abraham that_way

## 106v — the Samaritan binds his wounds and pays the host

> Went on one Samaritan, to Jerusalem, the Lord's living servant; and saw his face, found him, and had compassion on the man; afterward, for the Lord poured wine into the man's wounds, and had mercy; one; to the Lord long; in turn the Lord's faith; bound up the man's wounds, and the man | he put, the Lord, on his own shoulder; and the man he carried, to the Lord's lodging; and the man this innkeeper took. And the innkeeper took two […], two denarii; and then this innkeeper, this innkeeper, on the man take care; on this, that, whatever more on the man | […]

  1  go ~on one Samaritan on-Jerusalem <preposition_of_genitive>-Lord living-servant
  2  and face found and have_mercy to-~Adam
  3  afterward* because pour-Lord wine <preposition_of_genitive>-~Adam
  4  wound and have_mercy one-to long-Lord in_turn <preposition_of_genitive>-Lord believe
  5  bound_up <preposition_of_genitive>-~Adam wound and ~Adam | put
  6  Lord on-<preposition_of_genitive>-Lord shoulder and ~Adam from-carry to-Lord
  7  on-lodging and ~Adam grab this innkeeper
  8  and innkeeper grab two [...] two denarius
  9  and_then this innkeeper this-innkeeper on-~Adam
 10  carry on-~exist-this who to-whatever on-~Adam | little

## 107r — which of these three was neighbour? Then Augustine begins

> the innkeeper; then, when I come again, everything this innkeeper I repay. And then the Lord Jesus asked, this Lord, this Jew: who was this good neighbour among | the […] of Abraham, the one of the scripture, the Samaritan? And then this Jew […]: and this said, he spoke and said: he is […] the good neighbour, and […] did mercy to the man. And then the Lord Jesus, right, spoke to the Jew. And then the Lord Jesus, | this Jew brought(?); and he said: stay, do, said, it is, said he, the kingdom of heaven. The end of this holy gospel. Speaks holy Matthew: from the one denarius is signified

  1  innkeeper then-chapter go again* each,_every this-innkeeper regive
  2  and_then Lord-Jézus judge this-Lord this-Jew(ish) who?
  3  <subject_marker> this good was_accused* among | [?]-Abraham-+one-?the_scripture
  4  the_Samaritan and_then this Jew(ish) say*
  5  and this-+say speak-+say he_is* [...] good was_accused*
  6  and name-[?] have_mercy to-~Adam do, and_then
  7  Lord-Jézus righteous(ly) <subject_marker> speak-Jew(ish) and_then Lord-Jézus | this
  8  Jew(ish) brought* and he_said* stay do,-+say
  9  exist <preposition_of_genitive>-+say heaven land end this
 10  holy-gospel speak holy-Matthew from one denarius symbolize

## 107v — the two pence, by Augustine; and the opening of the next reading

> the Old Testament faith; in turn the two denarii signify the birth and death of the Lord Christ, speaks Saint Augustine the church father, […] […]. […] […] […] says God, in turn, for ever; God […]; from the thirty […] […], from the high food. Before the gospel, says | the Lord Jesus to his apostles and the Jewish people: because see | he is […] good; do what is pleasing, and thanks to the Lord, the Lord God. Begins this holy gospel, written

  1  <pertaining_to_the_Old_Testament> believe in_turn-two denarius symbolize ~on-be_born
  2  and die Lord-Christ speak Saint_Augustine_the_church_father [...] [...]
  3  little [...] [...] say God a) exist-exist-chapter
  4  God swallow on-from thirty [...] [...] from to-high-food
  5  before gospel say | Lord
  6  Jézus apostle <preposition_of_genitive>-Lord and
  7  Jew(ish) people
  8  because see | is_he-chapter
  9  [...] good
 10  do, pleasing
 11  and thanks to-Lord Lord-<suffix_of_divine_name> begins this holy-gospel write

## 108r — ye are the salt of the earth, and a city set on a hill

> written by holy Matthew, in the fifth chapter of his writing. Then said the Lord Jesus to his apostles and the Jewish people: ye are the salt of this world. In turn, if this salt lose its taste, it is good for nothing, out, the salt is thrown out, and the people trample on the salt, because this is set on high. Do ye good. And then the Lord Jesus: a city on a high mount, and the city cannot be hid; the people see it; and then […] the people to the city. Chapter to chapter, this; and you, learn, you, do good; in turn whosoever is high, of the two, teach the people, and do; found among the people, a man, mercy.

  1  holy-Matthew inside five chapter <preposition_of_genitive>-write time say Lord-Jézus
  2  apostle <preposition_of_genitive>-Lord and Jew(ish) people you salt
  3  this world* in_turn lose_taste this salt good-apostle-God out(ward)-out(ward)
  4  salt throw_out and salt people trample_on
  5  because this exist high you good do, and_then
  6  Lord-Jézus and <subject_marker> city on-high mount and city hid*
  7  people see and then-+<subject_marker> [...] people to-+city.
  8  chapter-go-to-chapter this and you on-learn you
  9  good do, in_turn-who-exist high from-two people on-learn
 10  and do, found among people somebody have_mercy

## 108v — the candle and the bushel, and the Father's house

> and love the Lord […]; whosoever loveth the Lord, and believeth in the Lord, and from the man receives; of you, of the Lord, in teaching […] the Lord teacheth; this Lord taketh you; and from the man goes into the Lord's Father's house, | where is joy for ever and ever, amen. In turn, then, out, the building, to cut off, the man is the city from […]. And then the Lord Jesus: then a man giveth light, lighteth a man; to this […] light, who is a lamp on a candlestick put; a man doth, a man, to the pit(?), the bushel; a lamp on a candlestick a man putteth, who letteth it give light; all the people see, he who is in the house; and you,

  1  and love-Lord [...] whosoever-and love-Lord somebody and believe inside-Lord and from
  2  somebody grab from you <preposition_of_genitive>-Lord on-learn [...]
  3  learn-Lord this-Lord you grab-Lord and from somebody go
  4  inside <preposition_of_genitive>-Lord father-<suffix_of_divine_name> house | exist joy chapter-oh
  5  chapter-oh amen in_turn then-chapter out(ward) building to-cut_off somebody
  6  exist city from-[?] and_then Lord-Jézus then-chapter somebody
  7  giveth_light* light somebody to this [...] light who-exist lamp
  8  on-candlestick put somebody do somebody to-pit-+day a)
  9  lamp on-candlestick put-somebody who-exist remit
 10  giveth_light* each,_every people see he_who* inside house and you

## 109r — whosoever shall do and teach them

> the lamp of this world, that is: learn from the Lord Jesus and from the holy gospel. And then the Lord Jesus: many believe; there is a man who beareth the people until the day of judgment; and one believeth, the second is gone. In turn […] this Lord letteth you go. And then the Lord Jesus: and whosoever keepeth that which the scripture […], and from the man is this rightly taught; in turn, and whosoever keepeth that which the scripture […] and from whosoever teacheth this not rightly. And then the Lord Jesus: and whosoever keepeth that which the scripture writeth, of the man good afterward; he shall see heaven, pleasing. In turn, and

  1  lamp this world* that_is learn from Lord-Jézus and from holy-gospel
  2  and_then Lord-Jézus many believe exist somebody carry people
  3  until judge-+day and one believe two exist
  4  leave-leave a) believe* this-Lord you remit-Lord
  5  and_then Lord-Jézus and somebody exist carry he_who* the_scripture*
  6  abound* and from somebody exist this righteous(ly) on-learn
  7  in_turn and somebody exist carry he_who* the_scripture* abound*
  8  and from whosoever* is_not this righteous(ly) on-learn and_then Lord-Jézus
  9  and somebody exist carry he_who* the_scripture* write <preposition_of_genitive>-somebody
 10  good afterward* exist see heaven pleasing in_turn and

## 109v — the end of the Matthew reading, and a new one from Luke

> the man keepeth not that which the scripture […] | of the man, good afterward, shall not see the pleasing things of the Lord, from the Father. The end of this holy gospel. The Lord God: love the Lord God. Begins this holy word, written by holy Luke, in the ninth chapter of his writing. Then went the Lord Jesus to Jerusalem; and then went the Lord Jesus to the mount of Olives, over against Jerusalem, in turn; and the Son of God saw down over Jerusalem, in turn; and cried out, | the Lord Jesus. And then: Jerusalem, Jerusalem! Then this Jerusalem […] and this Jerusalem

  1  somebody is_not carry he_who* the_scripture* abound* | <preposition_of_genitive>
  2  somebody good afterward* is_not see pleasing <preposition_of_genitive>-Lord
  3  from-father-<suffix_of_divine_name> end this holy-gospel Lord-<suffix_of_divine_name> love Lord-<suffix_of_divine_name>
  4  begins this holy-gospel
  5  write holy-Luke
  6  inside nine chapter <preposition_of_genitive>-write
  7  time go Lord-Jézus
  8  Jerusalem and then-exist go
  9  Lord-Jézus of_the_olives mount most_high Jerusalem in_turn-chapter-in_turn and
 10  see son God down Jerusalem in_turn-chapter-in_turn and cry_out | Lord
 11  Jézus and_then Jerusalem Jerusalem then-exist this-Jerusalem [...] and this-Jerusalem

## 110r — if thou hadst known; the army that shall compass thee

> […] because there is much misery upon this Jerusalem. Why? this | what […] who this […], said the man; the apostles | of the Lord said; and who this Lord preached, and this […] And then the Lord Jesus, then this Lord, the Son of God, weeping over this Jerusalem, because there shall come upon this Jerusalem […] an army; | this this shall sit about Jerusalem, and this Jerusalem […] compass round; […] and thou knewest not, man, the devil […] a man, the devil, out; and […] […] […] among you taken captive, all of them, the cross, condemned, the man, the devil, and not, he said, of hunger shall die; and there is much misery upon this

  1  chapter-+new because exist many misery ~on-this Jerusalem why? this | what
  2  believe* who this faith* say-somebody apostle | <preposition_of_genitive>
  3  Lord say and who this-Lord preach and this faith*
  4  and_then Lord-Jézus then-exist this-Lord son God crying
  5  this-Jerusalem because exist on-this-Jerusalem [trench] an_army | this
  6  this to-sit Jerusalem and this-Jerusalem [...] surround
  7  [...] and you is_not somebody angel exist
  8  somebody angel out(ward) and [...] name-Jerusalem a) [...] among you
  9  capture each,_every-+say cross condemned* somebody angel and
 10  ~exist-+say *hunger die and exist many misery ~on-this

## 110v — Jerusalem destroyed by Vespasian and Titus, and the temple cleansed

> Jerusalem; for this Jerusalem, all Jerusalem, the Roman destroyed, at their head | Vespasi- -anus, and his son Titus; […] stone upon stone | shall not be left; […] faith. And the Lord Jesus went into the Jerusalem temple; and then the Lord found within them that sold, the sellers of doves; and the Lord Jesus made of small cords a whip, and all of them […] out, out, cast out the Lord. And then the Lord Jesus: this is the house of prayer, this house; make it pleasing to the Lord, of the Father. In turn ye, the house, have made, said he, a den of thieves. And from thence the Lord Jesus, from until Palm Sunday, until many […]. The end of this | holy gospel.

  1  Jerusalem because this-Jerusalem each,_every-Jerusalem destroyed the_Roman on-head | Vespasi-
  2  -anus son Titus_<Roman_emperor> that stone on-stone | shall_not_be
  3  left [...] believe and go Lord-Jézus
  4  inside Jerusalem temple and then-exist Lord inside found them_that_sold*
  5  seller_of_doves and do, Lord-Jézus of_cords
  6  cords whip and each,_every-+say [...] out(ward)-out(ward)
  7  cast_out Lord and_then Lord-Jézus this_is pray
  8  house this house <subject_marker> do, on-pleasing <preposition_of_genitive>-Lord from
  9  father-<suffix_of_divine_name> in_turn you house do,-+say
 10  one thief house and from-exist Lord-Jézus from
 11  until Palm_Sunday until many Wednesday end this | holy
 12  gospel

## 111r — the five sorrows of the Son of God

> All the writings speak of five sorrows of the Son of God. The first sorrow of the Son of God: then the Lord God destroyed five, in turn; and not only sorrow of the Lord's eye, but rather greatly sad. The second sorrow, the writing speaks of the coming to the city of Bethlehem, because the Lord Jesus foresaw that he is, upon many, […] suffering | upon the coming of the Lord. The third sorrow, the writing speaks | of Palm Sunday: then he sat and saw, in turn, Jerusalem; not only the sorrow of the Lord Jesus for the house and for the building, literally, in the middle; in turn, the sorrow of the Lord Jesus for his own creature, who the Lord created for himself, […] because the Lord Jesus foresaw then

  1  each,_every write speak five sorrow* son God first sorrow*
  2  son God then-exist destroy Lord-<suffix_of_divine_name> five in_turn-chapter-in_turn
  3  and not_only sorrow* Lord eye but_rather* most_high sad(ly) two sorrow* write
  4  speak on-?coming Bethlehem city because
  5  foresee Lord-Jézus he_is* on-many [...] suffering | on
  6  coming* Lord third sorrow* write speak | on
  7  Palm_Sunday then-exist sit see on-in_turn-chapter-in_turn
  8  Jerusalem not_only sorrow* Lord-Jézus to-house and to-+building literal in_the_middle
  9  in_turn-chapter-in_turn a) sorrow* Lord-Jézus to-<preposition_of_genitive>-Lord create he_who*
 10  create-Lord to-Lord [...] because foresee Lord-Jézus then-exist <subject_marker>

## 111v — Jerusalem falls, and a mother eats her son

> the people shall go, all scattered. And then, at the execution of the Lord Christ: ten and ten, and four years; then took the Lord God power, the Roman, at their head; and at their head | there was by name Vespasian, and Titus; and these were father and son; and then the two, father and son, destroyed Jerusalem, all Jerusalem, […] even to the ground; and stone upon stone shall not be left. And | two, father and son, much misery upon them, did the son, the two, the father; because one said: of hunger they die. In turn the second said: how shall we, of hunger? […] In turn, of my son eat. The third said, they said, and they said, out, […] and […] head.

  1  say people go each,_every scattered and then-exist on-execute Lord
  2  Christ one-ten-+one-ten and two-two-year time grab Lord-<suffix_of_divine_name>
  3  can Roman on-head and on-head | and-exist
  4  exist-+name exist Vespasian and Titus_<Roman_emperor> and this exist
  5  from-father son and then-exist two-father-son destroyed Jerusalem each,_every Jerusalem [...]
  6  until ground and stone on-stone shall_not_be_left and | two
  7  father-son many misery on-+say do,-son-two-father
  8  because one say hunger die in_turn-two say how_shall_we-+say
  9  hunger [...] a) <preposition_of_genitive>-+say son eat third say
 10  say and-+say out(ward) [?]-+say and [...] head

## 112r — thirty Jews for one penny, because Judas sold for thirty

> among them taken captive, all of them, the cross, executed, but […] and there is a head […] […] a head; and they could a head […] find; and there they were, executed, a head […] sold, a head thirty for one denarius; and they, | from […] a head let go; in turn, until, in turn, went […] a head; and they, nine hundred for thirty denarii; and the head, more, they took; but it is. Judas, and they sold. The fourth sorrow, the writing speaks of Holy Tuesday: then Lazarus at the tomb, of the Lord; not only sorrow,

  1  among say capture each,_every say cross execute but_rather-[?] and
  2  exist head crucify* [...] head and say can
  3  head [...] on-find on-exist-+say-+<subject_marker>
  4  execute head [?]-+<subject_marker> vend head
  5  on-thirty to-one denarius and-+say <subject_marker> | from
  6  sell* head remit in_turn-chapter-in_turn ~until in_turn-chapter-in_turn go
  7  take* head and say nine hundred to-thirty denarius
  8  and head <subject_marker> more grab but_rather* exist.
  9  Judas and say vend in_turn-two-two sorrow* write
 10  speak on-many Tuesday then-chapter Lazarus on-burial_chamber among-Lord not_only sorrow*

## 112v — the fourth and fifth sorrows: Lazarus, and Good Friday

> the eye of the Lord Jesus, | but rather greatly sad, because Lazarus […] […] among, out, at the tomb; because three days was Lazarus in the tomb; and Lazarus […] […] out, of the Lord. The fifth sorrow, the writing speaks of Good Friday: then Christ crucified, because […] […] man, the Lord died; not only sorrow of the eye of the Lord Jesus, but rather greatly sad, sad for the people […] in the Lord […] believe; because foresaw | the Lord Jesus […] that the people shall go, all scattered; because there is […] the heavenly Jerusalem. The end of this teaching, the holy gospel. For on the day of judgment […] the angel divideth, the angel, the evil: how? one rejoiced […]; one […]

  1  eye Lord-Jézus | but_rather most_high sad(ly) because Lazarus [...] health among
  2  out(ward) on-burial_chamber because three_days exist Lazarus inside burial_chamber and Lazarus
  3  [...] health out(ward) among-Lord fifth sorrow* write
  4  speak on-many Friday then-chapter Christ crucified because [...]
  5  [...] somebody die-Lord not_only sorrow* eye Lord-Jézus but_rather most_high sad(ly)
  6  sad(ly) to people [...] inside-Lord [...] believe because foresee | Lord
  7  Jézus [?]-+<subject_marker> say people go each,_every scattered because-exist
  8  say [...] heaven Jerusalem end this learn holy-gospel
  9  because on-judge-year [?]-angel divide angel evil
 10  how? one rejoiced [...] one [?]-+say

## 113r — the division at the judgment, and the opening of the Prodigal Son

> die; this is: in two divided, the firstborn rejoiced, let go; in turn this younger rejoiced, let go, this; and the man divideth on the day of judgment: one gate to the evil; in turn the second taketh within the kingdom of heaven, but the Lord; there are many […] joy. Begins this holy gospel, the writing, the holy gospel, written by holy Matthew, in the first chapter of his writing. Then said the Lord Jesus to his apostles and the Jewish people: there was one holy Lord God; and then the Lord God had two sons, the angel, the soul; and this younger son of the soul then asked for the soul's

  1  die this_is on-two divide firstborn rejoiced remit
  2  in_turn this younger rejoiced remit this and somebody divide
  3  on-judge-year one gate on-~evil in_turn-two grab inside
  4  heaven land but_rather-Lord exist many speak* joy
  5  begins this holy-gospel
  6  write holy-gospel
  7  write holy-Matthew inside one chapter
  8  <preposition_of_genitive>-write time
  9  say Lord-Jézus apostle <preposition_of_genitive>-Lord
 10  and Jew(ish) people exist
 11  one ~rich Lord-<suffix_of_divine_name> and then-exist have Lord-<suffix_of_divine_name> two son
 12  angel soul and this younger soul-son then-exist soul ask_(for)

## 113v — the younger son takes his portion and wastes it

> portion of the soul's son, of the Father; and then the son of the soul had much wealth, took it of the Father; because the son of the soul rightly […] took of the Father this, of the soul's son, of the Father. And the son of the soul went far, into a | city there was; and the son of the soul stayed in that land, and | began the soul's son to waste it all; the son of the soul stayed in that land, because | began the soul's son to live riotously; and then, many years, the son of the soul stayed there. | In turn it was; and there was left; he began to be hungry, this; and the son of the soul how shall he understand? for the […] son: the holy eye, speech, hearing, love, mercy, faith, righteousness: the five senses […] of the Father. And the son of the soul went to a swineherd, and

  1  divide_into_parts <preposition_of_genitive>-soul-son father-<suffix_of_divine_name> and then-exist soul-son exist many ~rich
  2  grab father-<suffix_of_divine_name> because soul-son righteous(ly) [substance] grab father-<suffix_of_divine_name> this
  3  <preposition_of_genitive>-soul-son father-<suffix_of_divine_name> and go soul-son far inside | town
  4  exist and leave soul-son inside land and | begin-soul
  5  son from each,_every prodigalize leave soul-son this land because | begin-soul
  6  son lived_riotously and then-exist many-year leave soul-son this | in_turn
  7  exist-exist and leave be_hungry this and soul-son
  8  how_shall_we* understand because remain-[?] | rich-eye-say-hear-love-have_mercy
  9  believe-righteous(ly)-+five-sense-[?]
 10  father-<suffix_of_divine_name> and go soul-son one pigman and

## 114r — the swine, the husks, and "I will arise and go to my father"

> […] this swineherd, evil; and the son of the soul began of the evil swine […]; and the son of the soul, how shall he be fed? In turn the son of the soul began […] […] […] he who | sinned, from […] understood; and the son of the soul began to speak: my | Father God has hired men and servants, goodly, left over, in turn; this son of the soul is left, and good bread they eat. Mercy, Lord God! The hired men, the servants, in turn; this son of the soul eateth. And then this younger son, this son of the soul, and the son of the soul went. The son of the soul would go to the Father […]; the son of the soul, humbled, would

  1  son* this pigman evil and begin-soul-son
  2  <preposition_of_genitive>-evil pig son* and soul-son how_shall_we*
  3  food a) begin-soul-son name-from-+name [...] [...] he_who* | sin
  4  [?]-from understand and begin-soul-son speak have | from-father
  5  <suffix_of_divine_name> <preposition_of_genitive>-soul-son farm_hand and servant good leave
  6  a) this-soul-son leave and tasty bread eat have_mercy
  7  Lord-<suffix_of_divine_name> farm_hand servant a) this-soul-son eat and_then
  8  this the_younger_son this-soul-son and go-soul-son.
  9  <preposition_of_genitive>-soul-son from-father-<suffix_of_divine_name> want [...] soul-son ~humble want-soul-son

## 114v — the father sees him afar off; Father, I have sinned

> mercy, this; and this younger son went to his Father God. And the son of the soul saw afar off, this, his Father God; and the son of the soul began […] that, rightly, of his Father God, the son of the soul; and the son of the soul […] that, God, the son of the soul; and the son of the soul went, this son of the soul, before his Father God; and the son of the soul knelt down before his Father God; and the Father God began to pray, the Father God of the son of the soul asked, this son of the soul; this Father had mercy on the son of the soul, who, this son of the soul, through the sin of the soul against this Father and against the Lord God

  1  have_mercy this and go this the_younger_son to-<preposition_of_genitive>-soul-son
  2  father-<suffix_of_divine_name> and soul-son see far this <preposition_of_genitive>-soul-son
  3  father-<suffix_of_divine_name> and soul-son begin-soul-son recognize that* righteous(ly)
  4  <preposition_of_genitive>-father-<suffix_of_divine_name> soul-son and soul-son recognize that*
  5  God soul-son and go-soul-son this-soul-son before
  6  <preposition_of_genitive>-soul-son father-<suffix_of_divine_name> and kneel_(down)-soul-son before
  7  <preposition_of_genitive>-soul-son father-<suffix_of_divine_name> and father-<suffix_of_divine_name> begin pray father-<suffix_of_divine_name>
  8  <preposition_of_genitive>-soul-son ask_(for) this-soul-son this-father have_mercy-soul-son
  9  who this-soul-son through sin-soul against this-father and against Lord-<suffix_of_divine_name>

## 115r — bring forth the best robe: of love, of mercy, of righteousness

> and the son of the soul, mercy, this Father, of the son of the soul, all of the son of the soul, through the sin he who left, through the sin […]. And then this Father God of the son of the soul, the hired men and the servants, the holy apostles, the teaching, and the angel went, the apostles, the teaching, the angel; and | they brought, the apostles, the teaching, the angel, the most beautiful robe: the Lord's robe, that is love, the Lord God; the Lord's robe, that is mercy, the Lord God; the Lord's robe, that is | the Lord God; the Lord's robe, that is righteousness, the Lord God. And the son of the soul, from | the Father, the apostles, the teaching, the angels, within the law, to the Lord's faith; and | the son of the soul went, the apostles, the teaching, the angels, into his Father God's house; there is

  1  and soul-son have_mercy this father <preposition_of_genitive>-soul-son each,_every <preposition_of_genitive>-soul-son
  2  through sin he_who* from-leave through sin-[?] and_then this
  3  <preposition_of_genitive>-soul-son from-father-<suffix_of_divine_name> farm_hand and servant holy-apostle-learn
  4  and angel go-apostle-learn-angel and | carry-apostle-learn
  5  angel the_most_beautiful robe Lord believe <subject_marker> love Lord-<suffix_of_divine_name>
  6  Lord believe <subject_marker> have_mercy Lord-<suffix_of_divine_name> Lord believe <subject_marker> | Lord-<suffix_of_divine_name>
  7  Lord believe <subject_marker> righteous(ly) Lord-<suffix_of_divine_name> and soul-son from | father
  8  apostle-learn-angel-angel inside law to-Lord believe and | soul
  9  son go-apostle-learn-angel-angel inside <preposition_of_genitive>-father-<suffix_of_divine_name> house there exist

## 115v — the elder brother in the field hears the music

> joy for ever and ever, amen. And | among this. The Father of the son of the soul, the Father God, all of the Father God […] […] the neighbour; and the neighbour began to rejoice, the apostles, the Father God, the teaching, the angel, from […] the word […] and […] […]; and then was not this firstborn at home, because he was in the field. That is: within, the angel's joy; and he heard a sound, | of the son of the soul, of the Father God, the heavenly house, that is, within the heavenly city it is. And the son of the soul went, dying, this younger son, to his Father God's heavenly house; and the angel went,

  1  joy chapter-oh chapter-oh amen and | among-this.
  2  father <preposition_of_genitive>-soul-son from-father-<suffix_of_divine_name> each,_every <preposition_of_genitive>-father-<suffix_of_divine_name> [...] [...]
  3  was_accused* and begin-?was_accused ~joy apostle-father-<suffix_of_divine_name>-learn-angel
  4  from-[?] word [...] and [...] [...] and then-+is_not this
  5  firstborn exist-exist home because-exist on-field
  6  that_is inside angel joy and hear voice,_sound | to-<preposition_of_genitive>
  7  soul-son from-father-<suffix_of_divine_name> heaven house that_is inside heaven | town
  8  exist and go-soul-die-son this the_younger_son | on
  9  <preposition_of_genitive>-soul-son from-father-<suffix_of_divine_name> heaven house and go-angel

## 116r — he was lost, and is found; the end of the gospel

> this angel, the firstborn, was, to his angel, of the Father God. And then his angel, of the Father God, of the Father God, his angel […] this Father, the angel, took one, rejoiced, died; and one loaf of bread, love was, this angel, of the joy of his angel […]; in turn, on this the son of the soul, joy, the Father. And understanding he took from this Father: much wealth, the eye, speech, hearing, love, mercy, faith, righteousness, the five senses. And then this Father, of his angel, of the Father God, the son, of the Father God: lo, there is the son of the soul, who was lost, […] the servant; and the son of the soul was dead, and is risen from death, and is saved. The end of this holy gospel.

  1  this angel-firstborn exist-exist to-<preposition_of_genitive>-angel from-father-<suffix_of_divine_name>
  2  and_then <preposition_of_genitive>-angel from-father-<suffix_of_divine_name> from-father-<suffix_of_divine_name> <preposition_of_genitive>-angel [...]
  3  this father angel grab one rejoiced die and
  4  one loaf bread love-exist this-angel
  5  from-joy <preposition_of_genitive>-angel one-+friend in_turn on-this soul-son joy
  6  father and understand grab from this father many ~rich | eye-say-hear
  7  love-have_mercy-believe-righteous(ly)-+five-sense and_then
  8  this father <preposition_of_genitive>-angel from-father-<suffix_of_divine_name> son <preposition_of_genitive>-father-<suffix_of_divine_name> lo
  9  exist soul-son was_lost | release-angel-[?]-[?]-farm_hand
 10  servant-and soul-son exist die and rise* on-die be_saved
 11  end this holy-gospel

## 116v — John the Baptist, and the soldiers and publicans who came to him

> Before the gospel: written by holy John the Baptist; this word is written. Then it was, the Lord Jesus within his twentieth year and within the ninth year, within that time preached holy John the Baptist, on Carmel, on the mount; and he went. This John, the two […], the soldiers, the Pharisees, the farmers, and the sinful people; because there went soldiers, Pharisees, farmers, and sinners, to be taught by John on Carmel; and first the people were, the soldiers,

  1  before gospel-+<subject_marker>
  2  write holy-John
  3  the_Baptist/woman this word write
  4  time then-exist
  5  Lord-Jézus inside | two-ten-ten
  6  year and inside nine year inside
  7  time preach
  8  holy-John the_Baptist/woman on-Carmel to-mount and go.
  9  this-who John two-two [...] soldier Pharisee farm and sin
 10  people because exist go soldier Pharisee farm and sin on-learn
 11  to-John on-Carmel on first people exist soldier

## 117r — John the Baptist answers the soldiers, and then the Pharisees

> people; in turn the second people are the Pharisees, the Jews; the third people are the farmers, the people; in turn the fourth people are the sinners. First said the soldiers, the people; the soldiers answered; the soldiers went to this John to be taught, in a dream(?) taught. The soldiers: how shall we be saved? they spoke. And to the soldiers, holy John the Baptist: the soldiers' holiness, and of the soldiers' faith: begin to give alms, soldiers, to God, […] the blind, and be merciful, soldiers, and righteous, soldiers; that is, yours is the kingdom of heaven. Then said the Pharisees, the Jews, to John; the Pharisees answered; the Pharisees went to this John to be taught, in a dream taught. The Pharisees: how shall we be saved?

  1  people in_turn-two people exist Pharisee Jew(ish) third people exist
  2  farm people in_turn-two-two people exist sinners*
  3  first say soldier people answered-soldier go-soldier this-John
  4  on-learn on sleep learn exist soldier how_shall_we* be_saved | from
  5  speak and soldier holy-John the_Baptist/woman <preposition_of_genitive>-soldier ~rich and | <preposition_of_genitive>
  6  soldier believe on-begin donate soldier God [...] blind
  7  and exist-soldier have_mercy-soldier and righteous(ly)-soldier exist | is_he*
  8  yours heaven land time say the_Pharisees*
  9  Jew(ish) to-John answered-Pharisee go-Pharisee | this
 10  John on-learn on sleep learn exist the_Pharisees* how_shall_we* be_saved

## 117v — the Pharisees and the farmers get their answers

> they spoke. And to the Pharisees, holy John the Baptist: and have this, ye Pharisees, righteous people; preach, and teach the sinful; how is sin, from […]. And be ye Pharisees merciful, ye Pharisees, and righteous, ye Pharisees; there is yours the kingdom of heaven. Then said the farmers, the people, to John; the farmers answered; the farmers went to this John to be taught, in a dream taught. The farmers: how shall we be saved? they spoke. And to the farmers, holy John the Baptist: and have this, ye farmers; you, farmers, farm, till the ground, and conceive, and rightly, of the farmers, not, living; and to God, the blind, give alms; be ye farmers merciful, ye farmers, and righteous, ye farmers; yours is the kingdom of heaven.

  1  from-speak and the_Pharisees* holy-John the_Baptist/woman and have this the_Pharisees.*
  2  righteous(ly) people preach and sin learn how? exist sin | from
  3  redeem* and exist-Pharisee have_mercy-?the_Pharisees and righteous(ly)-?the_Pharisees exist
  4  you heaven land time say farm.
  5  people to-John answered-farm go-farm this-John
  6  on-learn on sleep learn exist farm how_shall_we* be_saved from-speak
  7  and farm holy-John the_Baptist/woman and have this-farm you
  8  farm farm <agricultural_expression> and get_conceived and righteous(ly) <preposition_of_genitive>-farm not-not
  9  living and God blind donate exist-farm have_mercy-farm
 10  and righteous(ly)-farm exist you heaven land

## 118r — and the sinners, who get the great commandment

> Then said the sinners; the sinners answered; there went the sinners to this John to be taught, in a dream taught. The sinners: how shall we be saved? they spoke. And to the sinners, holy John the Baptist: and have this, sinners; love the Lord God, lift up all your hearts, all your souls, all your might, all your heart; and your neighbour as thyself. Be ye sinners merciful, sinners, and righteous, sinners; and keep, sinners, the commandments of God; […] a hundred […] sins, and be saved, sinners, […], not, for ever and ever, amen; there is

  1  time say sinners* answered-?sinners | go
  2  sinners* this-John on-learn on sleep learn exist.
  3  sinners* how_shall_we* be_saved from-speak and sinners*
  4  holy-John the_Baptist/woman and have sinners* love Lord-<suffix_of_divine_name>
  5  from-lift_up each,_every heart each,_every <preposition_of_genitive>-?sinners soul each,_every <preposition_of_genitive>-?sinners
  6  might each,_every <preposition_of_genitive>-?sinners heart and <preposition_of_genitive>-?sinners
  7  exist-exist how?-to somebody neighbour exist-?sinners | have_mercy
  8  sinners* and righteous(ly)-?sinners and carry sinners*
  9  commandment God ~exist-hundred-[?]-+sin be_saved sinners*
 10  [...] not-not chapter-oh chapter-oh amen exist

## 118v — the commandment summed up, and a new reading from Luke

> yours the kingdom of heaven. This teaching is […] […] love the Lord God most high with all thy heart; and the man who keepeth the commandments of God, his is the kingdom of heaven. And this is: this love, the commandment, take from […] to be saved; and the man who believeth in the Lord Jesus Christ, that he is the true Son of the living God, every man shall be saved; and one is not damned […]: every man shall be saved. Begins this holy gospel, written by holy Luke, in the seventh chapter of his writing. Then was the Lord Jesus in his thirtieth year and one day; then went the Lord Jesus into the Pharisees' town; and there went to the Lord all these, and the sinners; this, who, the Lord Jesus, and

  1  you heaven land this learn exist [...] not* love | Lord
  2  <suffix_of_divine_name> most_high each,_every heart and somebody and exist carry commandment God <preposition_of_genitive>-somebody
  3  <subject_marker> heaven land and this_is this love commandment grab
  4  from [...] on-be_saved and somebody and exist believe
  5  inside Lord-Jézus-Christ he_is* righteous(ly) son living God each,_every somebody
  6  be_saved and one is_not be_damned but each,_every somebody be_saved
  7  begins this holy-gospel write holy-Luke inside seven chapter | <preposition_of_genitive>
  8  write time then-exist Lord-Jézus inside thirty one-+day
  9  time go Lord-Jézus inside Pharisee town and go
 10  to-Lord who-and-this-and sinners* this-who Lord-Jézus and

## 119r — the Lost Sheep

> […] […] and the scribes murmured at the Lord Jesus, that the Lord spoke [as] the Son of God; and when the Lord was the Son of God | this Lord […] went, this […] […] the Lord Jesus | when What man is there among you | who has one hundred sheep in the wilderness, and if he lose one of them […] […] […] the man is […] the lost one […] and does he not leave the ninety sheep and nine in the wilderness, and go, the man […] nine, [after] the lost one to find it; and when he finds the lost one, and the man takes it up […] | upon

  1  begin-?the_Pharisees Pharisees* and church_father murmur on-Lord-Jézus this-Lord speak
  2  son God in_turn then-exist this-Lord exist son God | this
  3  Lord [...] go this [...] and_then Lord-Jézus | then
  4  exist one have among you | one
  5  hundred sheep inside field and then-exist lose one
  6  among end* [...] [...] somebody exist answered-hide_oneself-+day ~who-chapter-say
  7  and exist from-food-somebody from nine-ten sheep and nine
  8  inside field and go-somebody ninety* nine the_lost_sheep
  9  find and then-exist the_lost_sheep find-somebody
 10  and the_lost_sheep grab-somebody man* | on

## 119v — the lost sheep found, and the woman with ten pieces of silver

> on his shoulder; and the man went to his friends and neighbours, and he is, with friend and neighbour; he said to them: I have found, my sheep, which […]; mine is this, this. Oh! And good, over the sheep, joy; in turn, over the ninety and nine sheep. And then the Lord Jesus: then one woman, the head, and she had ten drachmas; and then of these ten she loseth one. Eve; and there is light, Eve, the son of Mary, born, crucified, the lamp; and then Eve findeth this drachma, the kingdom of heaven; and there is good, over heaven, the kingdom, joy, Eve; over the Lord Christ's dying,

  1  <preposition_of_genitive>-somebody shoulder and go-somebody to-<preposition_of_genitive>-somebody friend and neighbours
  2  and exist and-friend-neighbor say-somebody say exist | found
  3  somebody sheep [...] somebody exist this-this oh and
  4  good on-+sheep/a_female_person joy ~a) on-nine-ten and nine sheep/a_female_person
  5  and_then Lord-Jézus then-exist one woman ~head-chapter
  6  and exist have ten drachma and then-exist this ten loseth_one*
  7  Eve and exist light Eve | Mary-son
  8  be_born-+crucified lamp and then-exist find Eve
  9  this drachma heaven land and exist good
 10  on-+heaven land joy Eve on-die-Lord-Christ

## 120r — the ninety-nine, and the nine orders of angels

> Eve's joy; in turn, over the feeding, the nine drachmas, the law. The end of this holy gospel. Then the Lord […], the Lord Jesus […], the sufferer. The gospel: said the Lord Jesus to his apostles and the Jewish people, this Lord: one Lord, this sheep; because to the Lord, this Lord […] the Lord, the nine orders of angels within the kingdom of heaven. And then the Lord Jesus, then the Lord bowed down, from the Father God, heaven, into the kingdom of heaven, upon many angels, upon the angel whose name is the hidden angel, and the second angel, and the hidden angel, as he was; and forty thousand years

  1  Eve joy a) on-food nine drachma law end
  2  this holy-gospel then-exist-Lord [...] Lord-Jézus [...] sufferer
  3  gospel say Lord-Jézus apostle <preposition_of_genitive>-Lord and Jew(ish) people this-Lord
  4  one Lord this sheep/a_female_person because to-Lord this-Lord | abandon
  5  Lord nine order angel inside heaven land
  6  and_then Lord-Jézus then-exist-Lord bow_down from-father-<suffix_of_divine_name>
  7  heaven on-heaven land on-many angel
  8  on angel name exist hide_oneself-angel and two
  9  angel and hide_oneself-angel as-~exist-exist and ten-ten-ten-ten-year

## 120v — the fall of Lucifer, and the order left empty

> and forty thousand, and night, which the hidden angel, to the hidden angel, into the kingdom of heaven, unto the evil […]; there is one order, the day […]; and then this Lord went from the Father God, of the Lord; from this the Lord would […] begin the order of angels; and from the leaving of the Lord until the day of judgment the Lord would, of the Lord, from the Father God, […] from the order, in the place […] there is the Lord; the Lord bowed down from the Father God, of the Lord, into the kingdom of heaven, unto the evil; then went the Lord, the Father God, the Son, God, Jesus, the Holy Spirit, Mary, Christ, the apostles, the angels […] living, and dying […] […]

  1  and ten-ten-ten-ten and night which-hide_oneself-angel to-hide_oneself-angel
  2  on-heaven land on-~evil redeem* <subject_marker> one
  3  order day-chapter from* and then-exist this-Lord go-Lord from-father-<suffix_of_divine_name>
  4  <preposition_of_genitive>-Lord from this-Lord want-Lord [the_tenth] ~begin order angel and from
  5  to-leave <preposition_of_genitive>-Lord ~until judge-year want-Lord <preposition_of_genitive>-Lord | from
  6  father-<suffix_of_divine_name> [the_tenth] from order on-place [...] <subject_marker> | exist
  7  Lord bow_down-Lord from-father-<suffix_of_divine_name> <preposition_of_genitive>-Lord on-heaven land
  8  on-~evil then-exist | go-Lord-father-<suffix_of_divine_name>-son-God-Jézus-holy-spirit
  9  Mary-Christ-apostle-angel judge living and die redeem* [...]

## 121r — the tenth order, and the drachma that was lost

> This Lord is […] of the Lord, of the Father God, upon the sheep, the righteous people; and believe in the Lord, and in his Father God, many […], and the neighbours, and the friends, the angels, and the apostles, for ever and ever, amen. And then the Lord Jesus, this […] […] baptized: this is his creature; you, the mother; she, from her, is she; she lost one drachma, one order, the order within the kingdom of heaven; because then he bowed down from the Father God, heaven, upon many angels, upon heaven, the kingdom, unto the evil. And then the Lord Jesus said: there is

  1  exist this-Lord judge-Lord <preposition_of_genitive>-Lord from-father-<suffix_of_divine_name> on-sheep
  2  righteous(ly) people and believe inside Lord and inside <preposition_of_genitive>-Lord from-father-<suffix_of_divine_name> many
  3  judge and neighbours and friend angel and apostle chapter-oh chapter-oh
  4  amen and_then Lord-Jézus this [?]-[?]-+baptize this_is <preposition_of_genitive>-Lord
  5  create you mother it from it <subject_marker> | exist
  6  it loseth_one-+it one drachma one
  7  order order inside heaven land because then
  8  bow_down from-father-<suffix_of_divine_name> heaven on-many angel on-heaven.
  9  land on-~evil and_then Lord-Jézus say exist

## 121v — the Trinity: Father, Son and Spirit, and one God

> from the Father God, to the Son, goeth the Holy Spirit; Father, Son, heart, man. And then from the Father God the Holy Spirit; how the man was shaped he would, the Father, the Son, the Spirit, the heart. And then the Son, in his image […] […]: man is, all one, to the Father, the Son, the Spirit. Father, Son and Spirit took man, and every living thing […]; the soul heard; Adam saw rightly; not many from the Father, from the Son; not many the Holy Spirit; in turn this Lord is all one God. And then the Lord Jesus went forth, Father, Son and Spirit, out, into the kingdom of heaven, into this world.

  1  from-father-<suffix_of_divine_name> to-son go holy-spirit father son heart somebody
  2  and_then from-father-<suffix_of_divine_name> holy-spirit on-how? somebody shape,_form
  3  want father son spirit heart and_then son | on-<preposition_of_genitive>
  4  shape,_form [...] [likeness] exist somebody each,_every one | to
  5  father son spirit grab father son spirit somebody
  6  each,_every living [creature] soul hear Adam see righteous(ly) not
  7  many from-father from son not many holy-spirit a)
  8  this Lord each,_every one God and_then Lord-Jézus go_out-Lord
  9  father son spirit out(ward) on-heaven land on-this world*

## 122r — the Lord God forms Adam and breathes into him

> And out of Paradise the Lord God, Adam, the heart […] And then Adam was, the heart, as was said before […] and […] to one soul, the heart, breathed upon Adam; and he became living. And the Lord took Adam, the Father, the Son, the Spirit; and Adam went, the Lord, the Father, the Son, the Spirit, into Paradise; and every heart is Adam's, the heart, the Lord, the Father, the Son, the Spirit. And then the Lord Jesus said, from the Father, of the Lord God, heaven, Adam […] this Adam took all rightly […] hunger and thirst […] this Adam;

  1  and out(ward) Paradise Lord-<suffix_of_divine_name> Adam heart slime_(of_the_earth)*
  2  and then-exist Adam exist heart earlier_mentioned [...] and
  3  became* to-soul-+one heart breathe on-Adam and
  4  living leave and Adam grab Lord-father son.
  5  spirit and Adam go Lord-father son spirit
  6  inside Paradise and each,_every heart exist-to Adam
  7  heart Lord-father son spirit and_then Lord-Jézus say from-father
  8  <preposition_of_genitive>-Lord God heaven Adam name-[?] this-Adam
  9  grab each,_every righteous(ly) [nor] be_hungry and thirsty [nor] this-Adam

## 122v — the commandment, the sleep, and the rib

> and one living thing dieth; there shall be sin, hunger, thirst, to him who. […] the Lord took, this Adam, all rightly one: the law, this yoke, this Adam, by commandment: do not eat of this tree, evil, sin, thou shalt die. Likewise Adam did eat, in that place, and died. And then Adam slept, into Paradise; and then the throne, first, from the saying; and then went the Holy Spirit into Paradise. And then this, this the garden; and the Lord God took from Adam a rib; and she, the heart, and then the Lord Jesus: thou, mother. And then Adam

  1  and one living-die-sin have be_hungry thirsty to-to-this-who.
  2  [...] grab Lord this Adam each,_every righteous(ly) one
  3  law this yoke this Adam through commandment do_not eat
  4  this to-+son evil-+sin thou_shalt_die* likewise* Adam exist eat
  5  on-place die and then-exist Adam sleep inside into_Paradise
  6  and then-exist table first from saying and then-exist go holy-spirit
  7  inside Paradise and_then this <subject_marker> this the_garden and
  8  grab Lord-<suffix_of_divine_name> Adam rib and it heart
  9  and_then Lord-Jézus you mother and then-exist Adam

## 123r — bone of my bones, and the serpent

> laughed; and then this: bone of my bones. In turn, the two souls, one […] by name. And then the Lord Jesus left, the Lord, the Father God, the Son, the Spirit, into the kingdom of heaven; and there went she into the Garden of Eden; and then Eve, Eve went to this tree which stood in the midst; it is the Lord God's, by the law; and she saw a serpent. And then this serpent: she, eat of this fruit. And then she: ye shall not eat, because she, Adam, answered by the commandment. And then this serpent: Eve, eat; she, Adam.

  1  from laugh and_then this bone bones in_turn two soul
  2  one [?]-+name and_then Lord-Jézus leave Lord-father-<suffix_of_divine_name>
  3  son spirit on-heaven land and go
  4  it on-Garden_of_Eden and then-exist Eve
  5  Eve go to this tree what stood_in_the_midst*
  6  exist Lord-<suffix_of_divine_name> through law and see one serpent and_then this serpent it
  7  eat this fruit and_then it shall_not_eat eat
  8  because it Adam answered through commandment and_then
  9  this serpent Eve eat it Adam

## 123v — she took of the fruit, and their eyes were opened

> this; in turn the fruit, it is; she, one, Adam did eat. Eve is, Adam; they knew evil and good, how to the Lord God it is known. And then she plucked, the serpent, this […], this serpent; and then she took, in turn she, the fruit, and gave to Adam; and then were opened, in that place, Adam, naked; she saw, Adam; and then she, Adam, was ashamed. And then the Lord Jesus: and this, unto death, the sin, to hide, they did; the hidden angel, the Lord, the Father, the Son, the Spirit, of the Lord, the man, from the Father God,

  1  this in_turn fruit <subject_marker> exist it one Adam eat
  2  exist Eve Adam know evil and good | how?
  3  to Lord-God know and then-exist pluck serpent this
  4  [...] this serpent and then-exist grab it
  5  in_turn it fruit grab Adam and then-exist
  6  were_opened* on-place Adam naked see it
  7  Adam and then-exist it Adam be_ashamed_of_sg
  8  and_then Lord-Jézus and this on-die sin-hide_oneself do,
  9  hide_oneself-angel Lord-father son spirit <preposition_of_genitive>-Lord somebody from-father-<suffix_of_divine_name>

## 124r — Adam, where art thou?

> the son, the hidden angel, is bowed down, the Father God, into heaven; in turn the day is unto hell. And then the Lord Jesus left, the Lord, the Father, the Son, the Spirit, into heaven; in turn […] within the Garden of Eden. And then the Lord Jesus, this second throne, from the saying; and then left, the Lord, the Father, the Son, the Spirit; left into the kingdom of heaven, into Paradise; he said: there is […] of […]. The Spirit to Adam: Adam, where art thou? And then Adam, which Adam; the Lord God said, the Lord, the Father, the Son, the Spirit, by mouth: Adam, which, said Adam,

  1  son-+<subject_marker> hide_oneself-angel exist ~bow_down father-<suffix_of_divine_name> on-heaven | in_turn-chapter
  2  day-exist on-hell and_then Lord-Jézus leave Lord-father son
  3  spirit on-heaven in_turn-[?] inside Garden_of_Eden
  4  and_then Lord-Jézus this table two from saying and then-exist
  5  leave Lord-father son spirit leave on-heaven land
  6  inside into_Paradise say exist [...] | <preposition_of_genitive>-[?].
  7  spirit to-Adam Adam why? and_then
  8  Adam which Adam Lord-<suffix_of_divine_name> say | Lord-father-son
  9  spirit who-mouth Adam which say Adam

## 124v — the woman gave me, and the serpent beguiled me

> who, this Adam answered and said to the Lord, the Father, the Son, the Spirit: where? Adam answered and said: the woman, Eve, Adam, she gave me to eat. Said the Lord, the Father, the Son, the Spirit: Eve, heavenly, said; Eve, which Eve, to this Lord said. The Lord, the Father, the Son, the Spirit: where art thou? she, which, who. Who? She answered and said to the Lord, the Father, the Son, the Spirit: where? Eve answered and said: she, the serpent, she gave her food. Said the Lord Jesus: there is, of the Lord, from the Father God, to Adam: Adam, to one

  1  who this-Adam answered* say Lord-father-son-spirit
  2  why? Adam answered* say ~Adam Eve
  3  Adam gave_to_eat say Lord-father-son-spirit Eve
  4  heavenly say Eve which Eve this-Lord-to say
  5  Lord-father-son-spirit why? it which who.
  6  who it answered* say Lord-father-son-spirit
  7  why? Eve answered* say it serpent
  8  it food say Lord-Jézus say exist <preposition_of_genitive>-Lord
  9  from-father-<suffix_of_divine_name> to-Adam Adam to-one

## 125r — to till the ground, and the sorrow

> the law; this Adam is […]; the commandment he kept; it is Adam, to him who, upon Adam; in turn, chapter, who. […] Adam is, the earth, to till the ground; he would, to the son, food take; in turn […] this; […] is through pining, and this […] is painful, the coming, he hath; in turn this evil is […] the earth, the serpent slideth, and a room for evil; this man was made, all of this; the serpent

  1  law this-Adam exist name-[?]-ten commandment carry exist
  2  Adam to-to-this-who on-<preposition_of_genitive>-Adam in_turn chapter-~who.
  3  gates* exist Adam earth to_till_the_ground
  4  want to-~son food grab in_turn Eve this
  5  Eve exist through pine and this Eve
  6  exist painful coming* have in_turn this evil
  7  exist [...] earth slide and
  8  room evil this somebody create each,_every this serpent

## 125v — driven out, and the flaming sword

> dieth; and he departed from among […] the Lord, the Father, the Son, God, the Spirit, from the Father God, Jesus, the angel, the Virgin Mary, Christ, and the apostles, and the Jews, and the man baptized, and all. […] and all the kingdom of heaven, the Lord, and the Lord's heart, all the earth, and the evil, and the kingdom of heaven; and there went the Lord God, the angel, the second, the earth, and […] fire, the sword, and | the earth; the serpent slid out; into the Garden of Eden he was cast out.

  1  die and leave among Adam_and_Eve
  2  <preposition_of_genitive>-Lord father son God spirit from-father God Jézus angel
  3  virgin-Mary Christ and apostle and Jew(ish) and somebody [?]-+woman and each,_every.
  4  [...] and each,_every heaven land Lord and Lord-+heart
  5  each,_every earth and ~evil and heaven land
  6  and go Lord-<suffix_of_divine_name> angel two earth and.
  7  Eve fire sword and | ~earth
  8  slide out(ward) on-inside Garden_of_Eden exorcise

## 126r — the cherub at the gate, and the third saying

> And he set the angel with the sword at the gate, the cherub of the Garden of Eden; and one creature […] within the Garden of Eden; in turn, the angel. And then the Lord Jesus, this third throne, from the saying, said the Lord Jesus: this is this drachma; and it is lost, then, from the evil, the sin: they did eat, the two, Adam; and […] and Adam slid out; cast out, the Lord, the Father, the Son, the Holy Spirit; and then hell, the evil; from […] the serpent took, from the good, one commandment of God; which chapter […] the serpent hath.

  1  and put angel sword on-gate cherub*
  2  Garden_of_Eden and one create [cherubim] inside
  3  Garden_of_Eden a) angel and_then Lord-Jézus
  4  this table three from saying say Lord-Jézus this <subject_marker> this
  5  drachma and exist lose then from evil-+sin eat two
  6  ~Adam and Eve and ~Adam slide out(ward)
  7  exorcise Lord-father son holy-spirit and then-exist hell
  8  evil from [?]-slide grab from good
  9  one commandment God which-chapter [?]-slide have

## 126v — the Lord seeks the drachma he lost

> The Lord, the Father, the Son, the Spirit, took what was lost; | the two, Adam, the serpent. Said the Lord Jesus: then therefore the two could find it. All, until this | redemption; therefore have mercy on the angel of the Lord, from the Father God; he could […] find, redemption, therefore. He was born of a mother, the Lord's love, and redemption; this Lord, of a mother […] was born; and redemption, this Lord, the cross […]; in turn […] […] the cross; from there he would find this drachma, this eternal kingdom […] there is, from […] the serpent; […] the hidden angel. And said the Lord Jesus: this Lord would take the trespass, and redeem, of the Lord, from the Father God, heaven.

  1  Lord-father son spirit exist grab lose | two-~Adam
  2  slide say Lord-Jézus then-?therefore two can find.
  3  each,_every ~until this | redemption therefore* have_mercy on-angel <preposition_of_genitive>-Lord
  4  from-father-<suffix_of_divine_name> can to-[?] find redemption therefore*
  5  exist be_born mother <preposition_of_genitive>-Lord love and redemption this-Lord from mother
  6  [...] be_born and redemption this-Lord cross [...] in_turn
  7  [?]-[?] cross from want find this drachma this eternal*
  8  land [?]-+<subject_marker> exist from [?]-slide
  9  abandon hide_oneself-angel and say Lord-Jézus this-Lord want-Lord
 10  trespass grab and ~redeem-Lord <preposition_of_genitive>-Lord from-father-<suffix_of_divine_name> heaven

## 127r — Hezekiah is told he shall die, and is given more years

> He said, in sleep, the angel of God, to holy Hezekiah the prophet; Hezekiah, the Lord God, this is, saith the Lord: within three days, this | one shall die. And then from laughter, holy Hezekiah began, Hezekiah, to be sad, holy Hezekiah, and cried out: who shall make ready? There went to Hezekiah […] and a second time said the angel of God: Hezekiah, the Lord God, this is, saith: I have had mercy on thee; it is until […] years thou shalt live; and mercy.

  1  say inside sleep God angel
  2  holy-Hezekiah_<king>
  3  prophet Hezekiah_<king>
  4  Lord-<suffix_of_divine_name> this_is say-Lord
  5  until three_days | this
  6  <subject_marker> die and then-exist
  7  from laugh holy-Hezekiah_<king>
  8  begin Hezekiah_<king> sad(ly)
  9  holy-Hezekiah_<king> and cry_out who-exist prepare-chapter-to-and
 10  go to-<preposition_of_genitive>-Hezekiah_<king> heart-Lord and two say God angel
 11  Hezekiah_<king> Lord-<suffix_of_divine_name> this_is say elongate_one’s_life-chapter-to-and exist
 12  until five-14-?years living-chapter-to-and and elongate_one’s_life

## 127v — Hezekiah dies, and Paul sets his house in order

> Made ready, holy Hezekiah; and upon […] Hezekiah's soul breathed out; and then of Hezekiah the soul breathed out; then appeared the angel of God, and said to the servants: of Hezekiah, lay him. This is for ever, in the sepulchre; in turn the soul of Hezekiah, | this the angel would take; and the angel left, in turn, holy Hezekiah for ever in the sepulchre laid. The servants speak; holy Paul […] […] the brethren of Paul […] and Paul made ready, of Paul, in his last year.

  1  prepare holy-Hezekiah_<king> and on-[?]
  2  <preposition_of_genitive>-Hezekiah_<king> soul breathe_out and then-exist-chapter-to-and
  3  of_Hezekiah soul breathe_out time appear.
  4  God angel and say servant of_Hezekiah put.
  5  this exist-exist-chapter inside burial_chamber in_turn soul Hezekiah | this
  6  angel want-angel grab and leave angel
  7  in_turn holy_Hezekiah exist-exist-chapter inside burial_chamber put.
  8  servant speak holy-Paul apostolic_letter [...] brother <preposition_of_genitive>-Paul
  9  have-[?] and Paul prepare <preposition_of_genitive>-Paul last year

## 128r — Paul's one only Son, and a new reading begins

> that he is, made ready, Hezekiah, holy Hezekiah the prophet; this […] hath; and Paul, the man, made ready, he who, the Lord Jesus, the Son of God, of Paul, the man, the one only, who was; that man went, because he lost […] Begins this | holy gospel, written | by holy Luke, in the first chapter, in his writing. Then, when he was condemned, the Lord Christ, three days

  1  he_is* exist prepare-Hezekiah_<king> holy-Hezekiah_<king>
  2  prophet this [...] have and Paul-somebody prepare this-who
  3  Lord-Jézus son God <preposition_of_genitive>-Paul-somebody one only_one
  4  exist-exist go-this-somebody because lose [...]
  5  begins this | holy
  6  gospel write | holy
  7  Luke inside one chapter inside
  8  <preposition_of_genitive>-write time
  9  then-exist on-?condemned
 10  Lord Christ three_days

## 128v — they were terrified, and believed not for joy

> […] night; then appeared to his apostles, the gate. And then the Lord Jesus: the law, he is, […] he is; and through, the apostles were startled, because the apostles believed that he is; how, for gladness? And then the Lord Jesus had the apostles; the Lord, this Lord, the apostles saw; within is for ever a man […] the angel, for ever; in turn, one, for gladness, could the apostles, the Lord, […] the Lord, who […] this Lord, to you, […] be thirty days and three, and literally

  1  another* night time appear
  2  apostle <preposition_of_genitive>-Lord gate and_then Lord-Jézus law | is_he-chapter
  3  [...] exist and through startle apostle because
  4  believe apostle he_is* how? thanks-evil and_then
  5  Lord-Jézus have-apostle Lord this-Lord see-apostle inside | exist
  6  exist-chapter somebody [...] angel exist-exist-chapter
  7  in_turn one thanks-evil can apostle Lord
  8  because* Lord ~who-[?] this-Lord to-you
  9  through stay thirty day and three and literal

## 129r — receive ye the Holy Ghost, and go into all the world

> and the apostles could […] the Lord Jesus, Christ, because therefore out, the Holy Spirit, mercy; and spake holy John: he breathed upon them, the apostles; and all the apostles received the Holy Spirit. And then the Lord Jesus to his apostles: go ye, apostles, into the world, and be ye his apostles; preach the gospel.

  1  and can apostle because* Lord-Jézus ~Christ-to because-?therefore
  2  out(ward) holy-spirit have_mercy and speak holy-John | breathed
  3  upon_them on-apostle and each,_every apostle grab holy-spirit
  4  and_then Lord-Jézus apostle <preposition_of_genitive>-Lord you go-apostle
  5  into_the_world* and exist-apostle <preposition_of_genitive>-Lord gospel preach
  6  and exist-apostle baptize inside <preposition_of_genitive>-Lord name
  7  and somebody exist Lord believe and exist
  8  baptize somebody inside name from-father-<suffix_of_divine_name> and son
  9  and holy-spirit each,_every somebody be_saved if and somebody therefore*

## 129v — baptize them, and be brought before kings

> baptizing them in the name of the Father, and the Son, and the Holy Spirit. One man shall be saved; in turn, every man shall be damned. And said the Lord Jesus to his apostles: ye shall | go, said he, before kings, before emperors. | Therefore the apostles have, because this Lord is with you […] therefore the apostles […] how shall they say? it is the apostles that speak. And then the Lord Jesus had these apostles from him; and a man, you, the apostles, for ever, to die rather, the apostles of the Lord God. Have, and the Lord, you, the apostles, the soul, and for ever

  1  baptize inside name from-father-<suffix_of_divine_name> and son and holy-spirit
  2  one somebody be_saved a) each,_every somebody be_damned and
  3  say Lord-Jézus apostle <preposition_of_genitive>-Lord you exist | go
  4  say before king before emperor | therefore*
  5  apostle have because this-Lord exist you that
  6  therefore* apostle [...] how? say exist speak-apostle and_then
  7  Lord-Jézus have this-apostle from and somebody you apostle
  8  exist-exist-chapter die rather somebody-apostle from Lord-<suffix_of_divine_name>.
  9  have and-Lord you apostle soul and exist-exist-chapter

## 130r — the apostles go out, and a new reading from John

> the dying of the Lord. And then the Lord Jesus: then went the apostles and preached, and began at Jerusalem; and the apostles preached in all the whole wide world. The end of this holy gospel; and the Lord Jesus departed from among the apostles. Begins this holy gospel, written by holy John, in the second chapter of his writing. Then said the Lord Jesus to his apostles, the Lord, at the last supper: this Lord goeth to his Father; he who, the Lord, goeth

  1  die-die-Lord and_then Lord-Jézus then go-apostle preach and
  2  ~begin from Jerusalem ~and preach apostle on-each,_every the_whole_wide_world world.*
  3  end this holy-gospel and leave among apostle Lord-Jézus
  4  begins this.
  5  holy-gospel write
  6  holy-John inside two chapter
  7  inside <preposition_of_genitive>-write time
  8  say Lord-Jézus apostle | <preposition_of_genitive>
  9  Lord on-last dinner-to.
 10  this-Lord go-Lord to-<preposition_of_genitive>-Lord from-father-<suffix_of_divine_name> he_who Lord go-Lord

## 130v — Thomas, and Philip: shew us the Father

> And then holy Thomas answered: goeth the Lord to his Father? Said | the Lord Jesus: Thomas, this Lord goeth to his Father, and the Lord goeth. And then | holy Philip answered: shew us, the apostles, thy Father. And then the Lord Jesus: Philip, the apostles, the Lord the apostles have seen; then this Lord did miracles, […] miracles; one, the Lord; this Lord, to the Lord, the trespass did; but rather the Father, of the Lord, […] doeth them, the Lord's finger. And he began to rebuke the apostles for their unbelief. And then the | Lord Jesus: and a man, the Lord, the apostles have seen, these apostles, and of the Lord the Father have seen; and a man who believeth in the Lord, this is

  1  and_then holy-Thomas answered go-Lord to-<preposition_of_genitive>-Lord father-<suffix_of_divine_name> say | Lord
  2  Jézus Thomas this-Lord go-Lord to-<preposition_of_genitive>-Lord father-<suffix_of_divine_name> and <subject_marker>-Lord
  3  go-Lord and_then | holy-Philip answered shew apostle
  4  <preposition_of_genitive>-Lord from-father-<suffix_of_divine_name> and_then Lord-Jézus Philip <subject_marker> apostle
  5  Lord see-apostle then this-Lord miracle do, [...] miracle
  6  one-Lord this-Lord to-Lord trespass do, but_rather* father-<suffix_of_divine_name>
  7  <preposition_of_genitive>-Lord [...] do, <preposition_of_genitive>-Lord finger
  8  and apostle begin rebuke on-believe and_then | Lord
  9  Jézus and <subject_marker> somebody Lord see-apostle this-apostle <subject_marker> and <preposition_of_genitive>-Lord
 10  from-father-<suffix_of_divine_name> see and somebody exist Lord believe this exist

## 131r — the Sadducees and the resurrection

> and in the Lord's Father believe, because this is one God. And then the Lord Jesus: go ye, apostles, into land and land, among the Sadducees; and the Sadducees, preach ye, apostles, how this Lord from death stood up, and ate; how it is that the Sadducees, ye, apostles, believe, because God said, the mouth of the day, hear; and the Lord ye have seen, Sadducees. And then the Lord Jesus said: he is yours; how ye, apostles, are, the Sadducees, to […]: because the Sadducees, before you, the dead they bear, the Sadducees, to rise, resurrect; and this is

  1  and <preposition_of_genitive>-Lord from-father-<suffix_of_divine_name> believe because this one
  2  God and_then Lord-Jézus you go-apostle inside
  3  land land among the_Sadducees* and
  4  the_Sadducees* exist preach-apostle how? this-Lord from-die
  5  stand_up food how? exist from the_Sadducees* you
  6  apostle believe because God say mouth-+day hear and <subject_marker>
  7  Lord see the_Sadducees* and_then Lord-Jézus say-Lord | is_he*
  8  yours how? you apostle exist the_Sadducees* | to
  9  believe* because-exist the_Sadducees* before you
 10  die carry-?the_Sadducees on-+rise resurrect and this | exist

## 131v — in my name, and he that believeth and is baptized

> the apostles say, these dead men offer; the apostles can, Jesus of Nazareth have; the dead again stand up, rise; in that place stand up, rise, the man, in his name. And then the Lord Jesus: and the man who believeth in the Lord, every such man shall be saved; and one man shall be damned. And then the Lord Jesus: and the man who therefore believeth the Lord, one man shall be saved; in turn every man shall be damned. And then the Lord Jesus: and the man who believeth the Lord, to be baptized with the second baptism, the Baptist's, in the name of the Father, and the Son, and the Holy Spirit: every such man shall be saved, and one man

  1  apostle say-apostle this-die-somebody offer apostle can Jézus Nazareth
  2  have die-somebody again* stand_up resurrect on-place stand_up resurrect
  3  somebody inside <preposition_of_genitive>-Lord name and_then Lord-Jézus and
  4  somebody exist Lord believe each,_every somebody be_saved
  5  and one somebody be_damned and_then Lord-Jézus and
  6  somebody therefore* Lord believe one somebody
  7  be_saved a) each,_every somebody be_damned and_then Lord-Jézus
  8  and somebody exist Lord believe to exist | two-+baptize
  9  the_Baptist/woman inside name from-father-<suffix_of_divine_name> and son and holy
 10  spirit each,_every somebody be_saved and one somebody

## 132r — the signs that shall follow them that believe

> shall be damned. And then the Lord Jesus: and the man who believeth the Lord shall do many miracles, all in the Lord's name; | and there is […]; then the apostles saw him taken up into heaven, the kingdom, the light. And then the apostles answered: they saw, the apostles, the light, taken up into heaven; in turn […] said the Lord Jesus: lo, taken up; the hidden angel could. And then the Lord Jesus: go ye, apostles, into the world; be ye apostles to the ass; heal ye, apostles; be ye apostles; the evil | upon the people cast ye out, apostles; the blind eyes, through light, apostles; the dead shall stand up, rise, apostles: all in the Lord's name.

  1  be_damned and_then Lord-Jézus and somebody exist Lord believe
  2  exist many miracle do, each,_every inside <preposition_of_genitive>-Lord | and
  3  exist-[?] time see apostle bow_down on-heaven
  4  land light and_then apostle answered see
  5  apostle light bow_down on-heaven in_turn-[?] say
  6  Lord-Jézus lo bow_down can hide_oneself-angel and_then
  7  Lord-Jézus you-apostle go into_the_world* exist-apostle
  8  to-from-donkey from-healing-apostle exist-apostle evil | on
  9  people cast_out-apostle eye-blind through light-apostle
 10  die-somebody stand_up resurrect-apostle each,_every inside <preposition_of_genitive>-Lord name

## 132v — the end of the reading, and the angel comes to Elijah

> and as the man, from the ass, go ye, apostles, all, from healing, apostles, in the Lord's name. The end of this holy gospel. Then appeared the angel of God to holy Elijah the prophet. Then

  1  and ~on-how? chapter-somebody | from-donkey go-apostle each,_every chapter | from
  2  healing-apostle inside <preposition_of_genitive>-Lord name end this holy-gospel
  3  time then-exist appear God angel
  4  holy-+Elijah prophet time then-exist

## 133r — Elijah's forty days, and the angel at Horeb

> From Adam […] until this […] five hundred years and thirty-six years. Then appeared the angel of God to holy Elijah the prophet. And then the angel of God: Elijah, the Lord God, this is, saith the Lord: it is this year, forty days go, Elijah, afar […]; and from […] by name it is Horeb. And then went Elijah upon this […] Horeb; and then Elijah lay down, to one tree; and a second time said the angel of God: Elijah, take, and Elijah found, and Elijah did eat, and Elijah was strengthened; and Elijah went […], Elijah, upon this mount Horeb, the love of the Lord God.

  1  from ~Adam heart-Lord until this [...] | five_hundred
  2  year and thirty six-year time appear God
  3  angel holy-+Elijah prophet and_then God angel
  4  Elijah Lord-<suffix_of_divine_name> this_is say-Lord exist this-year
  5  two-two-ten-year go-+Elijah on-far mount and [?]-from-+name
  6  exist Horeb and then-exist go Elijah on-this mount
  7  Horeb and then-exist from Elijah lie | to
  8  one tree and two say God angel Elijah grab
  9  find-+Elijah eat-+Elijah exist-+Elijah strengthen
 10  and go-+Elijah [...] Elijah on-this mount Horeb love Lord-<suffix_of_divine_name>

## 133v — the cake and the cruse, and Elijah taken up

> This is this mount, the love of the Lord God most high, of every creature. And then went Elijah upon this mount Horeb, and before he went, in that place […] lay down holy Elijah the prophet; and Elijah found one cake, and one cup of water; and he did eat, and drank, and was strengthened, upon this mount […] Elijah. And from that year, forty years; and these forty years, then, then he took Elijah, the two, Noah […] […] and Elijah and Noah were caught up into heaven on high; and from Elijah […] is Noah, Elijah, the sword shall bear; the evil […] and […] shall leave Noah and Elijah on the earth,

  1  this_is this mount love Lord-<suffix_of_divine_name> most_high each,_every create and then-exist go Elijah
  2  on-this mount Horeb and before go from on-place [...]
  3  lie holy-+Elijah prophet exist find-+Elijah
  4  one a_cake and one cup water and
  5  eat and drink and strengthen on-this mount [...] Elijah
  6  and from this-year two-two-ten-year and this two-two-ten-year then-exist
  7  time grab to-+Elijah-two-?Noah [...] [...]
  8  and Elijah-?Noah get_raptured heaven high and from
  9  Elijah man* exist ~Noah Elijah sword
 10  carry ~evil one-+gate/open and [Enoch] leave-to-leave Noah Elijah on-earth

## 134r — Antichrist, and a new reading: the king who took account

> […] […] through birth, the two, the chief evil, the evil one, and the son of the devil, by name evil; it is | Anti- christ. Before the gospel, said the Lord Jesus, leaving: a king, a man, from the king; hear all […] | of the kingdom. Begins this holy gospel, written by holy Matthew, in the […] chapter of his writing. Then said the Lord Jesus to his apostles and the Jewish people: there is, among the Lord God, the day of judgment, one king; all […] heavenly, the Lord, the man, before the Lord God the king; and then he had one heavenly

  1  [...] [...] through be_born two ~head-evil ~evil and
  2  son hide_oneself-angel name evil exist | Anti-
  3  baptize before gospel say
  4  Lord-Jézus leave-to-leave
  5  king somebody from-+king
  6  hear each,_every priest | <preposition_of_genitive>
  7  from-+king land begins
  8  this holy-gospel write
  9  holy-Matthew inside [...] chapter <preposition_of_genitive>-write time say Lord-Jézus
 10  apostle <preposition_of_genitive>-Lord and Jew(ish) people exist among Lord-<suffix_of_divine_name> judge-+day
 11  one king each,_every priest heavenly Lord somebody before
 12  Lord-<suffix_of_divine_name>-king and then-exist have one heavenly

## 134v — ten thousand talents, and the servant sold

> a servant; and the lord's servant owed ten thousand talents; and there went this Lord God the king, this heavenly servant; and then the servant, the angel, went before this | Lord God the king, before the Lord Christ; and the servant began to believe, this […] whosoever, the king, of the Lord | […] to do good. And then the Lord God the king, | the law, love, mercy, righteousness, good deeds […] took. And then this Lord God the king sold the servant, the angel, to be lost, | of the man, his son, the sin; and the people, to the holy; and the man knelt down, this man, this heavenly servant, before this | Lord God

  1  somebody-servant and Lord servant exist indebted ten_thousand talent
  2  and go this Lord-<suffix_of_divine_name>-king this heavenly servant and
  3  then-exist somebody-servant-angel go-angel before this | Lord-<suffix_of_divine_name>
  4  king before Lord Christ and somebody-servant begin
  5  believe this [?]-?whosoever-+king <preposition_of_genitive>-Lord | forgave_the_debt*
  6  good-do, and then-exist Lord-<suffix_of_divine_name>-king | law-love-have_mercy
  7  righteous(ly)-good-do, [...] grab and_then
  8  this Lord-<suffix_of_divine_name>-king sold angel-somebody to_be_lost | <preposition_of_genitive>
  9  somebody ~son sin and people* ~rich-to and kneel_(down)-somebody
 10  this somebody this heavenly servant before this | Lord-<suffix_of_divine_name>

## 135r — the Unmerciful Servant

> A king, and the Lord God begins […] […] […] […] […] […] would a man, the Lord God […] forgive the debt. And behold, the Lord God the king […] The servant of the Lord God the king humbled himself — the man-servant — and the man had mercy, the Lord God the king; and the man forgave all […] of the man's sin. And the man went […] to his home. And then, as the man went on, the fellow-servant of his household — and then he met one | God the man, this man, the fellow-servant; and the man was in debt […] pence; and the man of God began to demand it.

  1  king and Lord-<suffix_of_divine_name> begin as-believe [...] [...]
  2  have law to somebody-+sin want somebody this Lord-<suffix_of_divine_name> have_compassion
  3  remit indebted ~and see this Lord-<suffix_of_divine_name>-king besought*
  4  ~humble this servant <preposition_of_genitive>-Lord-<suffix_of_divine_name>-king somebody-servant and
  5  somebody have_mercy this Lord-<suffix_of_divine_name>-king and somebody have_mercy each,_every ~exist-+one
  6  <preposition_of_genitive>-somebody sin and somebody go-angel <preposition_of_genitive>-somebody
  7  home and then-exist keep_going-somebody this heavenly servant
  8  <preposition_of_genitive>-somebody home and then-exist appear one | God
  9  somebody this somebody heavenly servant and somebody exist
 10  indebted hundred* denarius and God-somebody begin ask_(for)

## 135v — the fellowservant cast into prison

> of the debt; and rather love he took; in turn he knelt down, the man of God, before this heavenly servant; and the servant began, as before […] […] to have the law, | to the man of God; the man of God would, this man, the heavenly servant, […] forgive the debt; and the man of God […] in turn the man of God took him into prison; and the man of God, until, from […] he bowed the head upon the scaffold; and this saw, sadly, the second servant; this Lord God the king, the angel, had mercy, the one only Lord God; and the angel went, sorrowing, the angel, this this Lord God the king; and the Lord God the king said to the angel

  1  <preposition_of_genitive>-indebted and rather-love grab a) kneel_(down) God-somebody
  2  before this heavenly servant and somebody-servant
  3  begin as-before [...] [...] have law | to
  4  God-somebody want-God-somebody this somebody heavenly servant
  5  have_compassion remit indebted and God-somebody release*
  6  a) God-somebody grab inside jail and God-somebody
  7  until-from bowed head inside scaffold and
  8  see this sad(ly) two servant this Lord-<suffix_of_divine_name>-king angel have_mercy
  9  one only_one Lord-<suffix_of_divine_name> and go-angel sad(ly)-angel-this
 10  this Lord-<suffix_of_divine_name>-king and Lord-<suffix_of_divine_name>-king say angel

## 136r — the parable told a second time

> the Father of heaven, he who is king of all heaven and earth, and king of all on earth; and then of his mercy the servant believes in the Lord God, the one only Lord God […] This Lord God had mercy. The Lord: ten thousand talents appeared. One man of God; and whosoever was in debt a hundred denarii; and the man of God began to ask | for the debt, and rather with love he took him; in turn he knelt down, the man of God, before this heavenly servant; and the servant began, as before, […] […] to have the law upon the man of God.

  1  from-father heaven he_who king each,_every heaven land
  2  and on-earth each,_every king and_then from have_mercy ~servant
  3  believe <preposition_of_genitive>-Lord-<suffix_of_divine_name> one only_one Lord-<suffix_of_divine_name> [...]
  4  this Lord-<suffix_of_divine_name> have_mercy Lord ten-?thousand talent appear.
  5  one God-somebody and whosoever* exist indebted hundred*
  6  denarius and God-somebody begin ask_(for) | <preposition_of_genitive>
  7  indebted and rather-love grab
  8  a) kneel_(down)-God-somebody before this
  9  heavenly servant and somebody-servant begin as-before
 10  [...] [...] have law to God-somebody

## 136v — he would not forgive, and the king was wroth

> The man of God would not, this heavenly servant, have compassion, forgive the debt, and release the man; in turn the man of God took him into prison; and the man of God, from house to house, bowed his head upon the scaffold. This king, the Lord Christ, grew angry, and went upon this heavenly servant; and the servant went to die, before the angel, before this king, before the Lord Christ, the one only Lord God. And then this king, on this servant had mercy | of the Lord, the Father God; that servant hid himself; how the Lord [came] to him; and the king — that servant: "Lord have mercy, Lord have mercy" — that servant.

  1  want-God-somebody this heavenly servant have_compassion
  2  remit indebted and God somebody release*
  3  a) God-somebody grab inside jail and God-somebody
  4  to-house-from bowed ~head-chapter inside scaffold
  5  get_angry this king Lord Christ and go on-this
  6  heavenly servant and servant go die angel before
  7  this king before Lord Christ one only_one
  8  Lord-<suffix_of_divine_name> and_then this king this servant have_mercy | <preposition_of_genitive>
  9  Lord from-father God to-hide_oneself that_servant ~how? Lord to and
 10  king that_servant have_mercy-Lord have_mercy-Lord that_servant

## 137r — the end of the reading

> Ten thousand talents. In turn this man, from the man of God […] had mercy: a hundred denarii. And the man took this king, the Lord Christ; and then took of the Lord the king the evil out, the evil of hell; and then this king, the Lord Christ, all of it, until this: that the man suffer […] […] […] likewise the king: the debt of the sin of the man. And then this king remitted all of the man; and the man therefore had mercy. Here ends this holy gospel.

  1  ten_thousand talent in_turn this-somebody from God-somebody [...]
  2  have_mercy hundred* denarius ~and somebody grab this
  3  king Lord Christ and then-exist grab <preposition_of_genitive>-Lord-king
  4  evil exorcise hell evil and_then this king
  5  Lord Christ each,_every until-from this that somebody suffering
  6  [...] [...] [...] likewise* king indebted sin
  7  somebody and_then this king this exist each,_every remit
  8  somebody and somebody therefore* have_mercy end this holy-gospel

## 137v — a prayer to the Virgin, with the author's colophon

> Hail, O Virgin. Through holy Mary, mother of God, […] […] Queen Mary, […] Lady […] […] | thou Mary, the one and only virgin maiden — thou, Mary, didst conceive Jesus without [sin]. Born of Mary […]; and from the Lord the Redeemer, in the Lord | I, [author], we do not doubt, [author]; we […] | I, [author], we pray to thee, Mary, […] | of [author], that when there is […], our soul may be forgiven | of [author], we […]. End of chapter. Amen. This prayer must be [said]. […] have mercy. Hail Mary. […] have mercy […] | Lord

  1  healing-girl through holy-Mary mother God gate into_Paradise
  2  king-Mary heaven wife world* go_up-Mary | this
  3  Mary one only_one virgin-girl this-Mary ~get_conceived Jézus without sin
  4  be_born-Mary Lord-+heart and from Lord-redeemer inside Lord | this-<the_name_of_the_author>
  5  somebody do_not_doubt-<the_name_of_the_author>-somebody believe | this-<the_name_of_the_author>
  6  somebody this-Mary pray to-+sin | <preposition_of_genitive>-<the_name_of_the_author>
  7  somebody then-exist go_up soul remit | <preposition_of_genitive>-<the_name_of_the_author>
  8  somebody exist-exist-chapter amen this pray have
  9  hundred-year have_mercy healing Mary name-high have_mercy ~out(ward)-Mary | Lord

## 138r — the Hail Mary, and the healing of a girl

> … God: this Mary of God. Blessed Mary, this Mary among women; blessed is the son of Mary, he who went to the Lord | from above, of Mary. Here ends the chapter. Jesus Christ. Amen. The healing of a girl through holy Mary, who took hold of the virgin girl. N. believes, this N., that this Mary is; N. through the mercy of the virgin girl; and N. is […] […] this […] and in every saying, and | redeem Mary; N., on the day of wrath of Mary, through the day of wrath, through — O son of Mary, Lord of N. — Jesus Christ.

  1  <suffix_of_divine_name> this-Mary-<suffix_of_divine_name> blessed-Mary this-Mary ~among
  2  the_poor_man/woman* blessed-+<subject_marker> <preposition_of_genitive>-Mary son he_who go-Lord | from
  3  up <preposition_of_genitive>-Mary exist-exist-chapter Jézus Christ amen
  4  healing-girl through holy-Mary from grab-virgin-girl
  5  believe this-<the_name_of_the_author>-somebody this-Mary exist <the_name_of_the_author>-somebody
  6  through have_mercy-virgin-girl and exist <the_name_of_the_author>-somebody [...]
  7  [...] this [...] and inside each,_every saying and | redeem
  8  Mary <the_name_of_the_author>-somebody get_angry-+day <preposition_of_genitive>-Mary through get_angry-+day
  9  through oh son <preposition_of_genitive>-Mary Lord <preposition_of_genitive>-somebody Jézus Christ

## 138v — Saint Augustine and the three Hail Marys

> Amen. This prayer has from […] mercy. So speaks the holy church father of the happy virgin Mary […] above: this Mary is; believe Mary; from Mary the son, from the Lord Jesus Christ. Everyone who would take hold, says holy Augustine the church father. Saint Augustine prays this: three prayers to the happy virgin Mary, to her pleasure and to her thanks. There is — Saint Augustine — the man who must be lost, O chapter, O chapter; and upon the cloud destroyed; and by three prayers many sins of a man are taken away, the sins of a man, in […]

  1  amen this pray have from [...] have_mercy
  2  speak holy-<name_of_a_church_father> church_father from happy virgin-Mary who up
  3  exist this-Mary exist believe-Mary from <preposition_of_genitive>-Mary
  4  son from Lord-Jézus-Christ each,_every want grab speak
  5  holy-Augustine-church_father pray-+Saint_Augustine this
  6  three pray happy virgin-Mary on-pleasing on-thanks
  7  exist-+Saint_Augustine-somebody have lose chapter-oh
  8  chapter-oh and on-+cloud destroy and on-+three pray
  9  from many somebody-sin go-somebody-sin inside heaven-chapter

## 139r — Mary shows her breast

> the earth. Because whoever prays to the happy virgin Mary, every man is saved and goes not into the fire of hell; because [whoever prays to] the happy virgin Mary every day, kneeling to Mary, there is of Mary | the son; she shows, of Mary, the breast, this breast, this of Mary, that nursed the Lord God — believe — "the lost and damned man: have mercy, Christ" | "the man lost and damned." And whoever prays to the mother of Christ, every man is saved, and not one is damned; in turn every man is saved, because a good servant, every […] servant

  1  land because and somebody pray happy virgin-Mary
  2  each,_every somebody be_saved not-go on-hell fire because
  3  happy virgin-Mary each,_every day kneel_(down)-Mary exist-to
  4  <preposition_of_genitive>-Mary | son show <preposition_of_genitive>-Mary
  5  breast this breast this-Mary this-Lord-<suffix_of_divine_name> nurse believe
  6  the_man-+lost_and_damned have_mercy Christ | the_man*
  7  lost_and_damned and somebody pray mother Christ each,_every
  8  somebody be_saved and one be_damned a) each,_every somebody
  9  be_saved because good servant each,_every [...] servant

## 139v — the curse and the blessing

> So speaks holy Moses to Aaron; of Moses it is: this people, the man, is cursed from every good. That is, therefore the man is saved; in turn, whoever is merciful, righteous, to God blind, and to his brother as to himself, to his own. There is heaven and earth; in turn, whoever is merciful, righteous to God, blind, and to his brother: this man the Lord God would. Cursed from every good; and all he has, that is, all his riches […] […] what the man has is damned, and the rich man cursed. This

  1  speak holy-Moses Aaron <preposition_of_genitive>-Moses exist-exist
  2  exist this people somebody exist through cursed from each,_every
  3  good that_is therefore* be_saved-somebody in_turn and somebody exist
  4  have_mercy-somebody righteous(ly)-somebody God blind and to <preposition_of_genitive>-somebody
  5  from-father son how?-to somebody himself <preposition_of_genitive>-somebody.
  6  exist heaven land in_turn and somebody exist
  7  have_mercy righteous(ly)-somebody to God blind and to <preposition_of_genitive>-somebody
  8  from-father son this somebody want Lord-<suffix_of_divine_name> cursed from
  9  each,_every good be_saved and each,_every have that_is each,_every ~rich who
 10  [...] have-somebody be_damned-somebody and ~rich cursed this

## 140r — cursed be thy herd and thy field

> the man. Of the Lord the herd, cursed; of the Lord the field; then the man's harvest, the field, cursed; of the Lord, his […] then the man's grape, harvest, […] cursed, this man of the Lord, within his house. There is this man […] […] damned, O chapter, O chapter; into hell the man falls; in turn, whoever is | merciful, righteous, the man, to God blind, this, to his brother as to himself, this man. Blessed of the Lord the herd; blessed of the Lord the field; then the man's field, harvest, blessed;

  1  somebody Lord-<suffix_of_divine_name> <preposition_of_genitive> herd cursed Lord-<suffix_of_divine_name> <preposition_of_genitive> field
  2  then-this-somebody harvest field cursed Lord-<suffix_of_divine_name> <preposition_of_genitive>-somebody
  3  mount then-this-somebody exist-nine harvest mount.
  4  cursed this-somebody Lord-<suffix_of_divine_name> inside <preposition_of_genitive>-somebody home
  5  exist this-somebody [...] [...] be_damned-somebody chapter-oh
  6  chapter-oh inside hell somebody fall_down in_turn and somebody exist | have_mercy
  7  somebody righteous(ly) somebody to God blind this <preposition_of_genitive>-somebody
  8  from-father son how?-to somebody himself this-somebody.
  9  blessed Lord-<suffix_of_divine_name> <preposition_of_genitive> herd blessed Lord-<suffix_of_divine_name> <preposition_of_genitive>
 10  field then-this-somebody field harvest blessed

## 140v — write it, and pray to the virgin Mary

> of the Lord the […]; then the man's […], grape. Harvest blessed, this man of the Lord, and within his | house in turn […] and in every place […] the man is left, the man is saved, there is. O chapter, O chapter, amen. It is written, it is said: all the wide […], to the pleasure of the Father God, and the Son of the Father God. Pray to the virgin Mary, believe; to all who would, the Lord the Father God hears; all the wide people the Lord would, to his will do; and the Lord: whoever is righteous, believe, the man. This the apostles all wrote, because every man's sin goes to the virgin Mary for mercy. Believe, man.

  1  Lord-<suffix_of_divine_name> <preposition_of_genitive> mount then-this-somebody mount exist-nine.
  2  harvest blessed this-somebody Lord-<suffix_of_divine_name> and inside <preposition_of_genitive>-somebody | ~home-in_turn
  3  home* and each,_every to-place [...] leave-somebody be_saved-somebody
  4  exist chapter-oh chapter-oh amen write speak
  5  each,_every wide world pleasing from-father-<suffix_of_divine_name> in_turn son <preposition_of_genitive>-father-<suffix_of_divine_name>.
  6  pray from virgin-Mary believe to each,_every want Lord
  7  from-father-<suffix_of_divine_name> hear each,_every wide people* want Lord to-+will
  8  do, and Lord somebody exist righteous(ly) believe
  9  somebody this <subject_marker> apostle each,_every write because each,_every somebody sin
 10  go-somebody to virgin-Mary have_mercy believe somebody.

## 141r — the fruit of Mary

> Because of this, pray to Mary: the fruit of Mary, the son, to all the wide world; because the Lord Christ made the law among men, among the Father God's, of the Lord, because they are many. Have mercy, Lord Christ, on every man's sin, speaks the holy church father; then this man is, from many a man's sin, […] left, the man, of the man, the heart of the Lord, because this is the creature of the Lord: the sin, the mercy […]; this is within the man's law, that is; and the man must carry the law of God, | as the scribes say, […] the sin; the man is saved through many sufferings.

  1  because this from Mary pray <preposition_of_genitive>-Mary fruit son
  2  to-each,_every wide world* because Lord Christ law do, among
  3  somebody among from-father-<suffix_of_divine_name> <preposition_of_genitive>-Lord because <subject_marker> many.
  4  have_mercy Lord Christ to-each,_every somebody sin speak holy-<name_of_a_church_father>
  5  church_father then-exist this somebody exist from many somebody sin
  6  [...] leave-somebody <preposition_of_genitive>-somebody Lord-+heart because this_is.
  7  creature* Lord sin have_mercy [...] this exist inside law somebody
  8  that_is and have somebody carry law God | ~exist-?the_scribes
  9  [...] sin somebody be_saved-somebody to-many suffering

## 141v — a woman in Rome

> O chapter, O chapter, amen. It is written by the name | of the man; in heaven and earth, until he dies; in turn upon death. Here ends the chapter. And the soul. O chapter, O chapter, amen. There was in Rome a woman, the head, and then, it is believed, the woman in Rome […] every day two: God. Here ends the chapter. She took, and fasted […] […]; she fasted to […], the woman, many years; and the woman would give thanks; this […] fasted one […]; and the woman took this holy host, and then

  1  chapter-oh chapter-oh amen write <subject_marker> name | <preposition_of_genitive>
  2  somebody inside heaven land until die in_turn | on
  3  die exist-exist-chapter and soul chapter-oh chapter-oh amen
  4  exist inside Rome one
  5  woman the_Baptist/woman head and
  6  then-exist believe-+woman
  7  inside Rome father*
  8  each,_every day two God exist-exist-chapter
  9  grab and fast half* [...] <subject_marker> fast to-[?] the_Baptist/woman
 10  many year and woman want thanks this [...] fast one
 11  [...] and woman grab this holy-host and then-exist

## 142r — the woman who lived on the host

> The woman took, and cried out; the woman was lost and died; and then she carried the host; and then the woman […] was; she took it to the place; hungering, she left […] this day's food. The woman ate many years […]; the woman understood Christ in the high heavens, the Holy Spirit, spirit to spirit, from the woman; living […] […] there were two; the woman's head, in Rome; and then the woman, through sin, the woman went out; of the woman the Lord, who was a thief, did; and then the woman cast out; the Lord, upon the Lord, had mercy; and one sister went; and then, O, of

  1  woman grab and shout-to lose die-+woman the_Baptist/woman
  2  and then-exist carry host and then-exist woman the_Baptist/woman host exist
  3  grab on-place *hunger leave [...] exist-today’s
  4  eat woman the_Baptist/woman many year [...] <subject_marker> woman the_Baptist/woman understand
  5  Christ on-heaven high holy-spirit to-spirit from woman
  6  living-[?] half* exist two woman the_Baptist/woman head inside Rome
  7  and then-exist woman the_Baptist/woman through sin woman the_Baptist/woman out(ward)
  8  <preposition_of_genitive>-+woman the_Baptist/woman Lord thief-who do, and then-exist
  9  woman the_Baptist/woman exorcise Lord on-<preposition_of_genitive>-Lord have_mercy and
 10  go one sister and_then oh | <preposition_of_genitive>

## 142v — the woman fasts and takes the host

> The woman: the father, to him in turn, who — this, to the wife — could do, how this woman could. The woman went into mercy, the woman; of the woman the Lord; and then would say this chapter, sister: to fast, the woman […]; and God. Here ends the chapter. She carried the woman, within the woman's mouth; and the Lord is God. Here ends the chapter. She kissed the woman; the Lord would, this woman; mercy there is; and then the woman, the woman, to fast, and took God. Here ends the chapter. And she carried the woman, within the woman's

  1  woman the_Baptist/woman from-father to-to in_turn-who this to-to-wife can do,
  2  how? this-+woman can woman the_Baptist/woman inside have_mercy go woman
  3  <preposition_of_genitive>-+woman the_Baptist/woman Lord and_then want say this chapter-+sister
  4  to-fast woman [...] and God exist-exist-chapter carry
  5  woman inside <preposition_of_genitive>-+woman the_Baptist/woman mouth and Lord exist
  6  God exist-exist-chapter kiss woman the_Baptist/woman want-Lord this
  7  woman the_Baptist/woman have_mercy exist and then-exist woman
  8  the_Baptist/woman to-fast and grab God exist-exist-chapter
  9  and carry woman the_Baptist/woman inside <preposition_of_genitive>-+woman the_Baptist/woman

## 143r — the face, the cloud, and the two grinding

> mouth; and the Lord would, to God. Here ends the chapter. She kissed; and the woman's face beat upon the place […] outward. God. Here ends the chapter. And there was a miracle, a farm; and the Lord God cried out, in the cloud, to the angel | of the Lord, leaving. O, to […] the woman, of the Lord, the father, the daughter, to love. The Lord is a miracle; the farm; the woman must the woman […] the woman […] this Lord; this woman, the creature of the Lord: the sin, the mercy; and then this woman in turn, grinding as one — thou, Lord God, sayest

  1  mouth and Lord want to God exist-exist-chapter kiss
  2  and woman the_Baptist/woman face beat on-place [...]
  3  out(ward) God exist-exist-chapter and <subject_marker> exist ~miracle farm
  4  and shout-to Lord-<suffix_of_divine_name> on-+cloud on-angel | <preposition_of_genitive>
  5  Lord leave oh to-[?] the_Baptist/woman <preposition_of_genitive>-Lord from-father daughter
  6  to-love Lord exist ~miracle farm woman the_Baptist/woman have
  7  woman the_Baptist/woman [...] woman the_Baptist/woman [...] this-Lord
  8  this woman the_Baptist/woman creature* Lord sin have_mercy and_then
  9  this woman the_Baptist/woman in_turn grinding-+one you Lord-<suffix_of_divine_name> say

## 143v — crucified, and the sin that dies

> the Lord God, in the cloud, to the angel of the Lord, this Lord, from Jesus; | and the Lord was crucified. And then this wife, the Lord, of the wife, the Lord God, of the wife mercy, to […] the woman, the brethren, this wife, through sin against the Lord, could; and then the Lord God, this Lord, this woman's sin — have mercy, Lord […] Lord, upon the sin. […] This says: the Son of God, the king of the high day, would the Lord, heaven, earth […] in turn one. A man's sin dies; that is, damned […] the man damned. The Lord God, in turn: this man to the Lord, among the Lord

  1  Lord-<suffix_of_divine_name> in_the_cloud on-angel <preposition_of_genitive>-Lord this-Lord from Jézus | and-Lord
  2  <subject_marker> crucified and_then this wife Lord <preposition_of_genitive>-wife Lord God
  3  <preposition_of_genitive>-wife have_mercy to-[?] the_Baptist/woman brethren* this-wife through sin
  4  against <preposition_of_genitive>-Lord can and_then Lord-<suffix_of_divine_name> this-Lord this
  5  woman the_Baptist/woman sin have_mercy Lord [...] Lord on-sin
  6  [...] this say <subject_marker> son God high-+day-+king want Lord
  7  heaven earth [...] a) one
  8  somebody sin die that_is be_damned to-+little somebody
  9  be_damned Lord God a) this somebody to-Lord among Lord

## 144r — Saint Augustine, and an image of the Virgin

> […] the people, the man, to the Lord God, this Lord — thou, creature of the Lord, the sin, the mercy, […]; this must the man carry: the commandment of God. The man is saved through many sufferings. O chapter, O chapter, amen. It is written by | holy Saint Augustine: there was a woman, and a Lady who prayed to the happy virgin Mary, outwardly, three years. In […] there was an image | of the virgin Mary; and then […] this image | of the virgin Mary; and she said this: from the Lady, hear, Lady — and the man

  1  heavenly* people somebody to-Lord-<suffix_of_divine_name> this-Lord you creature*
  2  Lord sin have_mercy seal-from this have somebody carry
  3  commandment God be_saved somebody to-many suffering
  4  chapter-oh chapter-oh amen write <subject_marker> | holy
  5  Saint_Augustine exist one ~sheep and Lady
  6  <subject_marker> pray happy virgin-Mary on-~out(ward) three
  7  year inside mount exist one image | virgin
  8  Mary and then-exist [...] this image | virgin
  9  Mary and say this from-+Lady hear-+Lady and somebody

## 144v — thou who holdest heaven and earth

> pray to the virgin Mary. The man would: "Good Queen, thou who holdest heaven and earth" — this Lady would, the Lady, pray. And she served one day; then Mary, every day, she took bread, and […] truly, at the day's beginning. Then, the year out, in time, the woman went to this image of the virgin Mary, and said this, the woman: | "Lord, […] thou who holdest heaven and earth, Lady, | virgin Mary." This Lady spoke from thence; and two said; the girl said:

  1  pray virgin-Mary want-somebody good queen grab heaven
  2  land this-+Lady want-+Lady pray
  3  and servant one day then-exist Mary each,_every day
  4  grab bread and [...] righteous(ly) ~begin-+day
  5  then-exist year ~out(ward) inside time go this sheep
  6  this image virgin-Mary and say this sheep | Lord
  7  queen grab heaven land Lady | virgin
  8  Mary this-+Lady from speak and two say girl say

## 145r — how shall we creatures speak?

> "Queen, thou who holdest heaven and earth, Lady virgin Mary" — this woman spoke thus: how shall we creatures speak? How can she speak? Said this woman, this woman, […] love: this Mary would; and then Mary, the woman, served, fasted, and prayed two healings of Mary, and truly at the day's beginning this day's; and […] she took; and then, two years out, in time, the woman went to this image of the virgin Mary, and said, this woman: "Queen, thou who holdest heaven and earth, Lady virgin Mary"

  1  queen grab heaven land Lady virgin-Mary
  2  this-+a_female_person from speak how? how_shall_we* creatures* speak
  3  can speak say this sheep this-+sheep/a_female_person
  4  [...] love this Mary want and then-exist Mary sheep/a_female_person
  5  servant fast and two healing-Mary pray and righteous(ly) begin-+day
  6  exist-today’s and [...] grab and then-exist
  7  ~out(ward) two-year inside time go this sheep this
  8  image virgin-Mary and say this sheep queen
  9  grab heaven land Lady virgin-Mary

## 145v — three days, three Hail Marys

> This Lady spoke from thence; and two said, this woman: "Queen, thou who holdest heaven and earth, Lady virgin Mary." The Lady prayed this to Mary, outwardly, fasting, fasting. The girl, the Lady: "Queen, thou who holdest heaven and earth" — this girl, the Lady, spoke; this woman […] love, this Mary would; and then Mary, the woman, served three days out; and three Hail Marys she prayed; and truly at the day's beginning, this day's; and […] she took; and then, out, three days, in time, the woman went to this image of the virgin Mary and said, this woman: "Queen, thou who holdest heaven

  1  this-+Lady from speak and two say this sheep queen
  2  grab heaven land Lady virgin-Mary
  3  pray Lady this Mary on-~out(ward) fast fast
  4  girl Lady queen grab heaven land
  5  this-girl Lady speak this-+sheep/a_female_person [...] love
  6  this-Mary want and then-exist Mary sheep/a_female_person servant
  7  on-out(ward) three_days and three healing-Mary pray and righteous(ly) begin-+day
  8  exist-today’s and [...] grab and then-exist out(ward).
  9  three_days inside time go this sheep this image
 10  virgin-Mary and say this sheep queen grab heaven

## 146r — the Lady speaks from the image

> and earth, Lady virgin Mary." This Lady spoke from thence; and two said, this woman: "Queen, thou who holdest heaven, | the town there is, Lady virgin Mary." This Lady spoke from thence. This woman grew angry. Forgive — the Lady went, of the Lady the Lord said, this woman, this Lady; and the Lady went. Forgive, this Lord. The Lady prayed, and the Lady served the virgin Mary three days out. This girl, the Lady: "Queen, thou who holdest heaven and earth" — this Lady; and | went the Lady. Forgive, this Lord said, this woman, this Lord.

  1  land Lady virgin-Mary this-+Lady from speak
  2  and two say this sheep queen grab heaven | town
  3  exist Lady virgin-Mary this-+Lady from speak
  4  get_angry this sheep remit go-+Lady <preposition_of_genitive>-+Lady
  5  Lord say this sheep this-+Lady and go-+Lady
  6  remit this Lord pray Lady and servant Lady
  7  virgin-Mary on-out(ward) three_days this-girl Lady queen
  8  grab heaven land this-+Lady and | go
  9  Lady remit this Lord say this sheep this-Lord

## 146v — the nail, and the Virgin in the image

> The Lady went […], this Lord; this Lady the Lord would, in the place. The girl: "Queen, thou who holdest heaven and earth" […] this woman, of the Lady, the Lord; and the Lady took this Lord, one […] […] upon the piercing. And one […] […]; and the Lady went, this, | from the woman; and then […] the Lady went, this woman; and many went. | In time appeared the Lady, the virgin Mary, within the image, the woman; and then […] the virgin Mary took the woman, to this | […]

  1  go-+Lady from-Lord this-Lord this-+Lady want-Lord on-place
  2  girl queen grab heaven land heavenly*
  3  this sheep <preposition_of_genitive>-+Lady Lord and Lady grab
  4  this Lord one [...] [...] on-pierce and.
  5  one [...] [...] and go-+Lady this | from
  6  sheep/a_female_person and then-[?] go-+Lady this sheep
  7  and go many | inside time appear
  8  Lady virgin-Mary inside image woman the_Baptist/woman and_then
  9  happy virgin-Mary grab woman the_Baptist/woman to this | [...]

## 147r — the son, and the king

> […] from the son, in the name of the virgin Mary, said this woman, this Lady; and the girl prayed; and the Lady served Mary three outward, this living day. "Queen, thou who holdest heaven and earth" — Mary took the girl, the Lady; this son the Lady would, the son, to this […] put | and take; the girl, the Lady, the son; in turn the Lady took one […]; and then the virgin Mary, the Lady, went again to the king; and the king took the Lady, this […]; and the brethren, this Lady said; from the king, living, the Lady did.

  1  [...] from son inside name virgin-Mary say this
  2  sheep this-+Lady pray girl and servant Lady
  3  Mary on-~out(ward) three this-living-+day queen grab heaven
  4  land Mary grab-girl Lady this son
  5  want-+Lady son to this [...] put | grab
  6  girl Lady son a) Lady grab one
  7  know* and_then virgin-Mary go-+Lady to-?again king
  8  and king grab Lady this know* and brethren*
  9  this Lady say from-+king living-exist Lady do,

## 147v — the Virgin seen by all the people

> And then the Lady went to this king; and from the […] king this […]; and took […] this woman; and | then there were Pharisees; they left the Lady; and then the Lady, the heavenly host […] served the Lady. In time appeared the Lady, […] the virgin Mary, within the image, the woman, and upon all the people she was seen. And then […] the virgin Mary, this woman: this is it. This Lady, like her, loved the girl, | this Mary; this Lady, the man did, the girl. The Lady is good; the Lady therefore […] in turn

  1  and then-exist go-+Lady this king and from from-[?]-+king
  2  this know* and grab [...] this sheep and | then
  3  exist Pharisees* leave Lady and then-exist Lady heavenly
  4  host say servant Lady inside time appear
  5  Lady happy virgin-Mary inside image woman the_Baptist/woman
  6  on-each,_every people see and_then happy virgin-Mary this
  7  sheep this_is this Lady like love-girl | this
  8  Mary this Lady somebody do, girl
  9  exist-+Lady good Lady therefore* [...] in_turn

## 148r — Adam went down to Jericho

> the Lady is […]; she was lost, this Lady; and here ends the chapter. […] the virgin Mary, before the people, forgave. It is written of Adam. The son, Seth. And this is the word. It is written: Adam went, one man, to Jerusalem, into the town of Jericho; and then Adam went into the field; and then there appeared an evil one; and then Adam a year of chapters […] the evil one in the field; and then

  1  exist-+Lady [...] lose this Lady and
  2  leave-chapter-leave happy virgin-Mary before remit people.
  3  write Adam.
  4  son Seth.
  5  and this word.
  6  write go-~Adam
  7  one somebody on-Jerusalem
  8  inside Jericho town
  9  and then-exist and go ~Adam on-~field and then-exist.
 10  appear one can-evil and then-exist ~Adam
 11  chapter-year [...] can-evil on-~field and then-exist

## 148v — the man in the pit, and the two mice

> The man fled across the field, and then the man | fell the man into a pit; and then […] […] the man onto a tree, because there was a branch sticking out […]; and there came two mice, one black, the other white; and this tree the two mice began to eat. And then the man saw, and to the man he saw an evil one […] and which cried out to the man: the man is lost […] if the man goes back again; this man, this | can

  1  escape ~Adam on-~field and then-exist ~Adam | get_conceived
  2  ~Adam inside one pit and then-exist hang
  3  cling ~Adam on-one tree because exist
  4  protrude [root] and go two mouse one black
  5  in_turn-two white and this tree ~begin two mouse
  6  to-eat and then-exist see ~Adam to-~Adam
  7  and see one evil [dragon] and
  8  who-shout-to ~Adam lose-~Adam [...]
  9  if again* go-~Adam this ~Adam this | can

## 149r — the lance of the soldier

> the evil one dies, if […] the man bows down to this. The evil one […] tears the man apart; and then the man […] startled the man, and | he went to the dying Lord Christ; one soldier of the Lord Jesus Christ who died […] […] the suffering; and this | can the evil one at the beginning, through […] and the man took hold of this soldier of Christ who died, the chapter | of the soldier of the Lord Jesus Christ who died: the suffering, the lance. And then this soldier of the Lord Jesus Christ who died freed the man from this

  1  evil die if cling bow_down ~Adam this.
  2  evil [dragon] ~Adam tear_apart and then-exist ~Adam
  3  [...] through startle ~Adam and | go-die-Lord
  4  Christ one soldier-Lord-Jézus-die-Christ [...]
  5  [...] suffering and this | can
  6  evil on-~begin through the_death_of_the_Lord_Christ* and
  7  ~Adam grab this soldier-[?]-die-~Christ-chapter | <preposition_of_genitive>
  8  soldier-Lord-Jézus-die-Christ suffering lance and_then
  9  this soldier-Lord-Jézus-die-Christ escape-~Adam on-this

## 149v — pulled out of the pit

> the pit; the man was scattered, and then the man was with the Lord; the Lord took hold of the suffering and the lance of the soldier of the Lord Jesus Christ who died and the man out of this pit, the chapter of the soldier of Christ who died, took hold; and then this soldier of the Lord Jesus Christ who died, then this man therefore the Lord took out, upon this pit there was the man inside this pit; and the man died, because | this man, this the evil one can: he dies, that is, he is damned. There is, there is a man […] who is saved. the man; God is […] […] the man saw

  1  pit scatter ~Adam and then-exist ~Adam exist-Lord
  2  grab-Lord <preposition_of_genitive>-soldier-Lord-Jézus-die-Christ suffering lance
  3  and ~Adam ~out(ward) this pit soldier-[?]-die-~Christ-chapter
  4  grab and_then this soldier-Lord-Jézus-die-Christ then-exist
  5  this-~Adam therefore* out(ward) grab-Lord on-this pit exist
  6  ~Adam inside this pit and die-~Adam because-exist | this
  7  ~Adam this can-evil die that_is be_damned
  8  exist exist ~Adam [...] be_saved.
  9  ~Adam God-exist [...] [...] see ~Adam

## 150r — a certain man had two sons

> wrote the church father, to the heathen; first wrote […] | upon this this wrote the church father, the church father […] upon that wrote […] the church father, upon that, wrote the church father the Pharisees; and the church father […] the gospel: there was one man, and then this man had one. son; and this son was three(?); he sold | and bought from him; and the son […] wanted, the man could the son bought; and then the son went away […] among; this son, of the son, from the father, said this

  1  write church_father to-+pagan first write [...] | on-this
  2  this write church_father church_father [...] on-that_is write
  3  [...] church_father on-that_is <subject_marker> write church_father
  4  Pharisees* and church_father [...] good_news exist one
  5  somebody and then-exist have somebody one.
  6  son and this son exist three sell | from-buy
  7  somebody and son two-two want-somebody can
  8  son from-buy and then-exist son go exorcise
  9  [...] among this son <preposition_of_genitive>-son from-father say this

## 150v — the father kissed him

> the son; oh, of the son, from the father: the father kissed the son upon this last year; and then the son, the father kissed; and cursed […] and then that father was […] a dog then this father was, the father, the son, the apostle, for good, therefore this son upon this went, to the son, in love the son went, speaking […] the church father, of the man, the church father, upon […] the name: Saint Augustine the church father spoke; it is of Saint Augustine; and the man believes in the Lord Jesus Christ; the man has this, of the man. the son, for good, the apostle: how […] dies, the good man.

  1  son oh <preposition_of_genitive>-son from-father kiss son father on-this
  2  last year and then-exist son father kiss and cursed
  3  [...] and_then that_is father exist [...] dog
  4  then-exist this-father exist father son apostle on-good therefore*
  5  this-son on-this go-~son on-love son go-~son speak-[?]
  6  church_father <preposition_of_genitive>-somebody church_father on-[?]-+name Saint_Augustine_the_church_father
  7  speak exist-~exist <preposition_of_genitive>-+Saint_Augustine and somebody believe
  8  inside Lord-Jézus-Christ have-somebody this <preposition_of_genitive>-somebody.
  9  son on-good apostle how? [?]-die good-somebody.

## 151r — for the good, to the father

> […] dies, from the father, for good, the apostle of the father, this; and you the man, of the man, the son, for good, the apostle, this man, because […] and the son, therefore this man, for good, the apostle of the man the son wants […] from […] dies, at the coming, two the son's sin; and the son's sin, you are, you light upon you: take the forgiveness of sins, and you. Cursed […] the son's sin, upon […] said the Lord God, holy Hezekiah the king, the prophet, to the angel of the Lord; Hezekiah the king was; the man had three born from […]; and from three born

  1  [?]-die from-father on-good apostle-father this and you
  2  somebody <preposition_of_genitive>-somebody son on-good apostle-this-somebody because
  3  seal* and son therefore-somebody-this on-good apostle <preposition_of_genitive>-somebody
  4  son want-[?] from [?]-die on-?coming two
  5  ~son-sin and son-sin you exist you
  6  light on-you grab-+forgiveness_of_sins and you.
  7  cursed [...] ~son-sin on-[?] say Lord-<suffix_of_divine_name> holy-Hezekiah_<king>
  8  prophet on-angel <preposition_of_genitive>-Lord Hezekiah_<king> exist somebody have
  9  three on-be_born from whosoever* and from three on-be_born

## 151v — the forgiveness of sins

> therefore […] and has; a) there is the son's sin; remit it; you, light, leave; and then the man sees the light, and there is the forgiveness of sins for you; go to the forgiveness of sins in the image […] the heart; how one woman the forgiveness of sins; and there is the forgiveness of sins, […] the forgiveness of sins of the man, the son; the forgiveness of sins for you, son; the other, and the son from […] the son in turn, to and upon the son, to […] the man is damned; if, and the son, to therefore the man, the apostle, for good; and upon the son, to, is damned | in turn

  1  therefore* ~exist-[?] and have a) exist ~son-sin remit
  2  you light to-leave then-+exist somebody see light and
  3  exist forgiveness_of_sins to you go-+forgiveness_of_sins
  4  inside image [...] heart how? one a_female_person
  5  forgiveness_of_sins and exist-+forgiveness_of_sins [?]-+forgiveness_of_sins
  6  <preposition_of_genitive>-somebody son forgiveness_of_sins you son
  7  in_turn-two and <subject_marker> son from whosoever* son in_turn to-to
  8  and on-son to-to [...] somebody be_damned if and son to-to
  9  therefore* somebody apostle on-good and on-son to-to be_damned | in_turn

## 152r — saved or damned, and the litany

> the brother, the son, to; there is the man, the apostle, for good; there is the man saved; therefore the man is damned; the man, the third son; and from […] this, of the man, good do […] do; this the man can do, | upon out of darkness into the light goes the man of the Lord God; love the Lord God; have mercy, Lord God; righteous, Lord God; hope, Lord God; every one of the man […] Lord God; every one of the man, good the apostle, Lord God; of the man, fast, Lord God; of the man repentance; from town to town carry, Lord God; of the man, believe

  1  brethren-+<subject_marker> son to-to exist somebody apostle on-good exist somebody
  2  be_saved somebody therefore* somebody be_damned somebody third
  3  son and <subject_marker> from whosoever* this <preposition_of_genitive>-somebody good do,
  4  [...] do, this somebody can do, | on
  5  darkness out(ward) on-light go-somebody Lord-<suffix_of_divine_name> <subject_marker> love Lord-<suffix_of_divine_name>
  6  <subject_marker> have_mercy Lord-<suffix_of_divine_name> <subject_marker> righteous(ly) Lord-<suffix_of_divine_name> <subject_marker> hope Lord-<suffix_of_divine_name>
  7  <subject_marker> each,_every <preposition_of_genitive>-somebody [...] Lord-<suffix_of_divine_name> <subject_marker> each,_every <preposition_of_genitive>-somebody good
  8  apostle Lord-<suffix_of_divine_name> <subject_marker> <preposition_of_genitive>-somebody fast Lord-<suffix_of_divine_name> <subject_marker> <preposition_of_genitive>-somebody
  9  repentance from_town_to_town* carry Lord-<suffix_of_divine_name> <subject_marker> <preposition_of_genitive>-somebody believe

## 152v — God be merciful to me a sinner

> Lord God; every good deed, Lord God; of the man a good life; oh chapter, oh chapter, in heaven and earth in the gospel a man speaks the Lord Christ, the son of the Lord and then a man went into the temple. And the man knelt down inside. In the temple every man has this; he said to the Lord: thanks, Lord God, pleasing it is to the Lord; holy mercy, have mercy on the sinner because this is he who repents; every sinner, to the Lord, thanks

  1  Lord-<suffix_of_divine_name> <subject_marker> each,_every good do, Lord-<suffix_of_divine_name> <subject_marker> <preposition_of_genitive>-somebody
  2  good living chapter-oh chapter-oh inside heaven land
  3  inside gospel somebody speak
  4  Lord-~Christ son <preposition_of_genitive>-Lord
  5  then-exist go somebody
  6  inside temple and.
  7  kneel_(down)-somebody inside.
  8  temple each,_every somebody have this say to-Lord thanks Lord-<suffix_of_divine_name>
  9  pleasing exist <preposition_of_genitive>-Lord holy-have_mercy have_mercy somebody-sin
 10  because this who repentance each,_every somebody-sin to-Lord thanks

## 153r — Lord, remember me

> Lord God, have mercy on the sinful man. Holy John speaks: how from the thief; and Christ was crucified, and the thief; and then the thief went up, he who from that day, the Lord Jesus, to the place […] that Lord Jesus righteous, the son of God, because he is; out, the thief, the Holy Spirit have mercy; and he cried to the cross, he answered | asking the thief; this thief, to this Lord: remember me, the thief. then to go with the Lord into the land of the Lord. And then these two thieves; and there was the Lord, the thief condemned. […] this […] then this Lord loved | can

  1  Lord-<suffix_of_divine_name> have_mercy somebody sin speak holy-John how?
  2  from thief and Christ crucified thief and then-exist thief
  3  on-go who-from-+day Lord-Jézus on-place ~exist-this that Lord-Jézus
  4  righteous(ly) son God because-exist ~out(ward) thief holy-spirit
  5  have_mercy and shout-to cross answered | ask_(for)
  6  thief this-thief this-Lord remember on-thief
  7  then-to go-Lord inside <preposition_of_genitive>-Lord land and_then
  8  this two thief and exist Lord thief condemned.*
  9  [...] this [...] then-exist this-Lord love | can

## 153v — today shalt thou be in paradise

> the Lord; this Lord is to redeem; and the thief, the thief, the one Lord and cried out, this thief, first, to this Lord: righteous the man; the two thieves, these die, they deserve it and turned toward the Lord Jesus, the head of the Lord, to the thief and then the Lord Jesus, the robe, the Lord […] the year until wherefore hidden; the thief is […] before, in Paradise and one said, from the thief: how shall we | upon the thief, the last year, heaven and earth it is written, in the days of Moses, righteous […]

  1  Lord this-Lord exist to-Lord redeem and thief thief one-Lord
  2  and shout-to this thief first this-Lord <subject_marker> righteous(ly)
  3  somebody two thief-thief this die from deserve
  4  and turn_toward Lord-Jézus <preposition_of_genitive>-Lord head to-thief
  5  and_then Lord-Jézus robe the_Lord believe* year until
  6  why?-hide_oneself exist-thief [...] before inside into_Paradise
  7  and one say from thief how_shall_we* | on-<preposition_of_genitive>
  8  thief last year-heaven land
  9  write <subject_marker> inside Moses-+day righteous(ly) [...]

## 154r — the fire of purgatory

> […] the fire of purification, rather than hell […] on the day […] the soul goes out, into purification; this soul, joy because the soul goes before the face of the Lord Jesus Christ. The end of this holy gospel. […] the world, one year redeemed, a hundred years of suffering; heaven and earth; the other, the ways there is a man, for one day of repentance | atonement the man inside the fire of purification, a hundred years for one day in turn; and the man, righteous, to fast and repentance | atonement the man, of the man, heaven and earth, and

  1  [...] purification fire but_rather* hell [...]
  2  day-to [...] soul go out(ward) on-purification this soul joy
  3  because go-soul before from face Lord-Jézus-Christ end
  4  this holy-gospel [?]-?world one year redeem hundred-year
  5  suffering heaven land in_turn-two ways*
  6  exist somebody to one day repentance | atone
  7  somebody inside purification fire hundred-year to-one
  8  day in_turn and somebody righteous(ly) to-fast and repentance | atone
  9  somebody <preposition_of_genitive>-somebody <subject_marker> heaven land and

## 154v — the captive and the king

> this man, repentance, leave; because the man, the righteous man the suffering of the Lord Christ; and the man | is saved. the man; oh chapter, oh chapter, amen; Lord God, with all thy heart wrote holy Elijah the prophet and holy Luke. And then he was taken prisoner, the robber, the […] son one, from the king of the world; and and then it is written, this […] son, of the […] […] the world […]; then the […] son bought

  1  this somebody repentance leave because somebody <subject_marker> righteous(ly)-somebody
  2  suffering Lord-Christ and somebody | be_saved.
  3  somebody chapter-oh chapter-oh amen Lord-<suffix_of_divine_name> with_all_thy_heart*
  4  write holy-Elijah prophet
  5  and holy-Luke.
  6  then-exist take_prisoner
  7  robber [?]-son
  8  one from-?world-from-+king and
  9  then-exist write this [?]-son <preposition_of_genitive>-[?]
 10  [?]-?world-[?] then-exist [?]-son from-buy

## 155r — held in bondage

> from the king of the world, in bondage; and the […] son could not get out […]; this humble, this […] son; and sadly the […] son left; and then […] this robber, the daughter, at the building, the daughter inside one house; and then for many years he led her out. This robber, upon this, until; and then | the daughter believed; the believing daughter went out, home and then the believing daughter went home, this from […] the […] son; and the believing daughter began to […]

  1  from-?world-from-+king on-bondage and [?]-son can_not
  2  out(ward) [...] this humble this [?]-son and
  3  sad(ly) [?]-son leave and then-exist [...]
  4  this robber daughter on-to-+building daughter inside
  5  one house and then-exist many year out(ward) lead.
  6  this robber on-this ~until and then-exist | daughter
  7  believe out(ward) go-daughter-believe to-home
  8  and then-exist go daughter-believe to-home this from-[?]
  9  [?]-son and begin-daughter-believe to-[?]

## 155v — he could not buy him back

> speak; and the daughter could not speak, because there was sadness; the […] son upon this, of the […], the […] world […] the brother, the […] son, could not buy him back, and | went the believing daughter from the […] son; and then the believing daughter, and the two, the believing daughter went; then the […] son, good, the whole wide world; and then to […] | the daughter believed, and began to talk; and the believing daughter, spoke to […], said to […] this. From the king of the world: if, how shall we ransom the believing daughter?

  1  speak and can_not daughter speak because exist
  2  sad(ly) [?]-son on-this <preposition_of_genitive>-[?] [?]-?world-[?]
  3  brethren* [?]-son can_not from-buy and | from-go
  4  daughter-believe from* [?]-son and then-exist
  5  daughter-believe and two go-daughter-believe then-exist
  6  [?]-son good the_whole_wide_world and then-exist to-[?] | daughter
  7  believe begin_to_talk and daughter-believe.
  8  speak to-[?] say to-[?] this.
  9  from-?world-from-+king if how_shall_we* daughter-believe | redeem-daughter.

## 156r — how shall she be ransomed

> believe; the […] son, this believing; how is this believing daughter to be ransomed? this, the day on which, before the believing daughter | from the father the king of the world, the evil one; and then this believing daughter, this robber if the believing daughter wants […] to take | this to […] the […] son, the wife | this daughter believing, this […] the believing daughter wants to be ransomed; this, the day on which, said this to the son of the son, this from the king of the world, this […] wants […]

  1  believe to-[?] this hide_oneself-+day-which say this | daughter
  2  believe how?-exist this-daughter-believe redeem-daughter-believe
  3  this hide_oneself-+day-which before <preposition_of_genitive>-daughter-believe | from-father
  4  world-from-+king evil and_then this daughter-believe this robber
  5  if daughter-believe want-[?] grab | this
  6  to-[?] [?]-son wife | this-daughter
  7  believe this-[?] want-daughter-believe
  8  redeem this hide_oneself-+day-which say this to-son-son this
  9  from-?world-from-+king this-[?] want-[?]

## 156v — the escape by night

> this believing daughter has the […] son as husband and then this time; and then the believing daughter to […] in the night | fled, the daughter believing […]; and the rich | carried away the daughter believing […], the brother | the believing daughter to […] the rich could carry; and then […] to […] | to the woman the son, […] the world […]; and | […] the daughter believing, saw; and went, this of the […]

  1  this-daughter-believe have [?]-son wife
  2  then-exist this time and then-exist daughter-believe
  3  to-[?] inside night | escape-daughter
  4  believe-[?] and ~rich | from-carry-daughter
  5  believe-[?] brethren* | daughter-believe
  6  to-[?] ~rich can carry and then-exist
  7  [?]-to-[?] | to-<preposition_of_genitive>-+woman
  8  son [?]-?world-[?] and | [?]-daughter
  9  believe see and go this <preposition_of_genitive>-[?]

## 157r — the virgin daughter

> […] the world […]; and sadly the father left; and then to […] the believing daughter went to […] | to of […] […] and then this from […] oh, of […], to […], oh, from […] love went to […] | judged from […] | this to […]; he is this virgin, the believing daughter, said this to […]: this is the believing daughter, from the robber he who is to […], the robber taken prisoner said this from […]: he is this believing daughter, this woman

  1  [?]-?world-[?] and sad(ly) leave-father-[?] and then-exist
  2  to-[?] daughter-believe go-to-[?] | to
  3  <preposition_of_genitive>-[?] [?]-[?] and_then this from-[?]
  4  oh <preposition_of_genitive>-[?] to-[?] oh from-[?]
  5  <subject_marker> love go-to-[?] | judge from-[?] | this
  6  to-[?] he_is* this virgin-daughter-believe say
  7  this to-[?] this_is daughter-believe from robber
  8  he_who exist to-[?] take_prisoner-+robber
  9  say this from-[?] he_is* this-daughter-believe this woman

## 157v — she is led before the Father

> The believing daughter eloped; she was led before God the Father | of the daughter the Lord Christ. This is the daughter who believes in the Lord Christ, in unbelief […] of the daughter of the Lord Jesus Christ, from God the Father; and said this | the daughter of the Lord Jesus Christ, this from […] […] this believing daughter of the Lord Jesus Christ in unbelief […] of the believing daughter of the Lord Jesus Christ | from God the Father, because from God the Father, of the daughter of the Lord Jesus Christ, the wealth she has; remit […] […] […] in turn | then this king of the world was; every one of […] the rich | was sold from […] therefore there is, to […]: how shall we | from

  1  elope-daughter-believe lead before from-father-<suffix_of_divine_name> | <preposition_of_genitive>-daughter
  2  Lord-Christ this_is daughter-Lord-Christ-believe inside not_believe
  3  [...] <preposition_of_genitive>-daughter-Lord-Jézus-Christ from-father-<suffix_of_divine_name> and say this | daughter-Lord
  4  Jézus-Christ this from-[?] [...] this-daughter-Lord-Jézus-Christ-believe
  5  inside not_believe [...] <preposition_of_genitive>-daughter-Lord-Jézus-Christ-believe | from
  6  father-<suffix_of_divine_name> because from-father-<suffix_of_divine_name> <preposition_of_genitive>-daughter-Lord-Jézus-Christ wealth
  7  have remit man* [...] [...] in_turn | then
  8  exist this-from-?world-from-+king exist each,_every <preposition_of_genitive>-[?] ~rich | sold
  9  from-[?] therefore* exist to-[?] how_shall_we* | from

## 158r — the buying and the selling

> buy this, in turn; and then to […] he wanted from […] to buy this; it is, it is, from […] from […] oh chapter, oh chapter; said this from […] of […] to […] this […] this | the daughter of the Lord Jesus Christ who believes, […] took | to scatter every one of […] the rich; and said this to […] of […] […] | this to […] this believing daughter of the Lord Jesus Christ | wanted

  1  buy-this in_turn then-exist to-[?] want-from-[?]
  2  from-buy-this exist exist from God-?seal from-[?]
  3  chapter-oh chapter-oh say this from-[?] <preposition_of_genitive>-[?]
  4  to-[?] this-[?] this | daughter-Lord-Jézus
  5  Christ-believe son* grab | to
  6  scatter each,_every <preposition_of_genitive>-[?] ~rich and say this
  7  to-[?] <preposition_of_genitive>-[?] [?]-[?] | this
  8  to-[?] this daughter-Lord-Jézus-Christ-believe | want

## 158v — a wife, and the end of it

> to […] took; and then this time | to the woman the son, righteous, a wife; and the […] son, righteous. until the daughter of the Lord Jesus Christ who believes, and | the woman wanted the son of the believing daughter of the Lord Jesus Christ lived […] God, the whole wide world; oh chapter, oh chapter, amen; Lord God, with all thy heart. Before the gospel, written by holy Luke, in the twenty-second chapter | of the writing; the time | then the Lord Jesus was, in the thirtieth

  1  to-[?] grab then-exist this time | to-<preposition_of_genitive>-+woman
  2  son righteous(ly) wife and [?]-son righteous(ly).
  3  ~until Lord-daughter-Jézus-believe-Christ and | want-+woman
  4  son-daughter-Lord-Jézus-Christ-believe living [...] exist.
  5  God the_whole_wide_world chapter-oh chapter-oh amen Lord-<suffix_of_divine_name> with_all_thy_heart*
  6  before gospel write
  7  holy-Luke inside two-two chapter | <preposition_of_genitive>
  8  write time | then
  9  exist Lord-Jézus inside thirty

## 159r — two men with spirits

> and second year; the time; the Lord Jesus went to the shore; bread and then the Lord Jesus found the shore of the sea one hundred; the sin of this; and then he found, the Lord Jesus, the shore of the sea, among one mountain, two men with spirits; in the two men there were | six hundred and […] and sixty and six evil devils; and how the two men's hearts were found, the hearts of these two men aforesaid […] in turn […] the two men were, to take | the Lord

  1  two-year time go Lord-Jézus shore bread
  2  and then-exist find Lord-Jézus shore sea
  3  one hundred* sin-this-from and then-exist find
  4  Lord-Jézus shore sea among one
  5  mount two somebody-spirit inside two somebody exist | six
  6  hundred* and six_hundred* and six-ten and six ~evil evil and how?
  7  two somebody heart find-two-somebody this heart two somebody
  8  earlier_mentioned [...] in_turn [...] exist two somebody to-grab | Lord

## 159v — the devils ask to be sent into the swine

> Jesus Christ; and the two men went to the Lord Jesus, and began the two men to cry out; he answered […] and the Lord went before the time; he loved the two men; the evil suffering, the Lord, every died of many sufferings; and the two men began the devils to ask, into the leftover food; and then the two, whatsoever devils there were, were driven by the Lord Jesus into the leftover food, because […] the Lord Jesus scattered them from the leftover food in turn; and from the two men the woman's spirit, the Lord God redeemed

  1  Jézus Christ and go two somebody to-Lord-Jézus and begin
  2  two somebody shout-to answered [torment] and Lord go before
  3  time love two somebody evil suffering Lord each,_every
  4  die from* many suffering ~and begin two somebody
  5  evil ask_(for) inside leftovers *food and
  6  then-exist two whosoever* evil exist chase
  7  Lord-Jézus inside leftovers *food because [...]
  8  Lord-Jézus from leftovers *food scatter
  9  in_turn from two somebody woman the_Baptist/woman spirit redeem Lord-<suffix_of_divine_name>

## 160r — the herd runs into the sea

> and then the herdsmen saw this, and were startled, and fled to the herdsmen's home and the herdsmen said what they had seen of the Lord; and then they went from the Lord […] saying: Jesus of Nazareth. And every aforesaid herd of the herdsmen was destroyed in the sea; the Lord humbly spoke, and sadly they left […]. The end of this apostolic holy gospel. This holy gospel begins, written by holy Luke in the twenty-second chapter of the writing; the time the Lord Jesus sat by the sea; then, in his thirty-second year

  1  and then-exist see this-Lord this shepherd and through
  2  startle and escape to-<preposition_of_genitive>-shepherd home
  3  and say shepherd Lord-see <preposition_of_genitive>-shepherd and_then
  4  go-from-Lord [?]-from say Jézus Nazareth and each,_every
  5  earlier_mentioned <preposition_of_genitive>-shepherd herd inside sea destroy
  6  Lord humble-+say and sad(ly) leave-[?] end this
  7  apostle holy-gospel begins this holy-gospel write holy-Luke
  8  inside two-two chapter <preposition_of_genitive>-write time sit Lord-Jézus
  9  on-sea then-exist inside thirty two-year

## 160v — the Lord returns to Capharnaum

> Within, there was one of the Lord God, and through […] the Lord Jesus into one land […] into one […] […] the house; and then he was seen, the Lord Jesus going, and they began to cry out […], and the Lord went; this Lord would; he says from on high, of the rich […] he made ready, and the Lord Jesus returned | into the middle of the Lord's town; and this town | was named Capharnaum; and he took to himself three apostles, Peter and Paul and

  1  inside one ~exist Lord-<suffix_of_divine_name> and through [...] Lord-Jézus inside
  2  one land [...] inside one in_turn-chapter-in_turn
  3  [...] home and then-exist see-+say go-Lord-Jézus
  4  and begin-+say shout-to [...] and go-Lord
  5  this-Lord want-Lord say from-high <preposition_of_genitive>-+say ~rich [...]
  6  prepare and-Lord return Lord-Jézus | inside-and
  7  in_the_middle-inside <preposition_of_genitive>-Lord town and this town | and
  8  was_named* exist Capharnaum and grab
  9  to-Lord three apostle Peter and Paul and

## 161r — the paralytic, and the four who carried him

> John; because then the Lord Christ would do a miracle, and every miracle the Lord had to confess; and then | he preached, the Lord, in Capharnaum; and many people made ready to him, and then they carried one upon an ass before the Lord Jesus, within | two by two, the men, at the head. Among them: faith, love, hope, mercy; and | they could not — the four friends of the paralytic — so instead, up onto the temple they went, the four friends; and the temple they pierced through, the four friends, to let him down

  1  John because then-exist Lord Christ miracle do, want
  2  Lord-to each,_every miracle confess have and then-exist | preach
  3  Lord inside Capharnaum and prepare to-Lord many people
  4  and then-[?] carry one from-donkey before
  5  Lord-Jézus inside | somebody two-two man head.
  6  among believe love hope have_mercy and | can
  7  <the_four_friends_of_the_paralytic_man_in_Lk_5,_17ff> inside but_rather-?again on-temple
  8  go <the_four_friends_of_the_paralytic_man_in_Lk_5,_17ff> and temple
  9  through pierce <the_four_friends_of_the_paralytic_man_in_Lk_5,_17ff> to-?again

## 161v — thy sins are forgiven thee

> onto the roof; and a man, with a rope, | let down faith, love, hope, mercy, to the Lord, before the Lord Jesus Christ; the Lord Jesus saw, and was saved the man; from the faith of the two and two, what and who, and a man had mercy, the Lord Jesus Christ; and then the Lord Jesus: son, of the Lord believing son, loving son, hoping son, | mercy; the son shall have health, the son; and then the Lord was there […]; the Lord, the Jews, the Lord Jesus; and then the Lord Jesus […] | said: believe, man, love, hope, man, have mercy, man; there is […] a man, or rise, and go, man.

  1  on-roof and somebody rope | go-+believe-love-hope
  2  have_mercy Lord before Lord-Jézus-Christ see Lord-Jézus be_saved
  3  <preposition_of_genitive>-somebody believe from two-two what-+who and somebody
  4  have_mercy Lord-Jézus-Christ and_then Lord-Jézus son <preposition_of_genitive>-Lord
  5  believe-son love-son hope-son | have_mercy
  6  son exist have-son health son and
  7  then-exist-Lord exist [...] Lord Jew(ish) Lord-Jézus
  8  and_then Lord-Jézus [...] | say-believe-somebody-love
  9  somebody-hope-somebody-have_mercy-somebody exist [...]
 10  have-somebody or rise and* go-somebody

## 162r — rise, take up thy bed and walk

> The Jews said […] | said: believe, man, love, man, hope, man, have mercy, man; there is, therefore, a man, said the Lord Jesus truly; the Jews spoke, and then | the Lord Jesus took […] of the son | faith, love, hope, mercy, that day; and the stretcher he took, and put the son on the stretcher, upon the son's shoulder; and the man went, and the son was saved, the man's son, home to heaven. Here ends this holy gospel. The Lord Christ raised three dead, stood them up, the Lord | of

  1  say Jew(ish) [...] | say-believe-somebody-love-somebody
  2  hope-somebody-have_mercy-somebody exist therefore* have-somebody
  3  say Lord-Jézus righteous(ly) <subject_marker> speak Jew(ish) and_then | Lord
  4  Jézus grab-[?] <preposition_of_genitive>-son | believe-love-hope
  5  have_mercy-+day and stretcher
  6  grab and put son stretcher
  7  on-<preposition_of_genitive>-son shoulder and go-somebody-son be_saved
  8  <preposition_of_genitive>-somebody son ~home heaven end this holy-gospel
  9  Lord-Christ three die-somebody <subject_marker> stand_up resurrect-Lord | <preposition_of_genitive>

## 162v — the three whom the Lord raised

> the Lord, of the Father; first he could stand up and raise, the Lord Jesus, one chief man's daughter in Jerusalem; and the second | dead man he stood up and raised, the Lord Jesus: Lazarus, in Jerusalem; | and the third dead man he stood up and raised, the Lord Jesus, at Nain; […] therefore stood up and raised the three dead to the Lord, the Lord Christ: rather, the daughter, Lazarus, the son; of the Father, of the Lord, he stood up and raised; of the Lord, why in turn, of the Lord the finger […] the miracle he did. | The Lord, Father, Son, God, Jesus, Holy Spirit, the Lord God, with all thy heart.

  1  Lord from-father-<suffix_of_divine_name> can first stand_up resurrect Lord-Jézus
  2  one head daughter inside Jerusalem in_turn-two | die
  3  somebody stand_up resurrect Lord-Jézus Lazarus inside Jerusalem | in_turn
  4  three die-somebody stand_up resurrect Lord-Jézus Nain
  5  [...] therefore* stand_up resurrect and three die-somebody to-Lord
  6  Lord-Christ but_rather* daughter Lazarus son from-father-<suffix_of_divine_name>
  7  <preposition_of_genitive>-Lord stand_up resurrect <preposition_of_genitive>-Lord why?-in_turn <preposition_of_genitive>-Lord
  8  finger [...] miracle do, | Lord
  9  father-<suffix_of_divine_name>-son-God-Jézus-holy-spirit Lord-<suffix_of_divine_name> with_all_thy_heart*

## 163r — the widow of Nain

> This holy gospel begins, written by holy Luke, in the […] chapter of the writing: the time, then, the Lord Jesus, in his thirty- | second year; the time he went, | the Lord Jesus, into one town; and this town's name was Nain; and the Lord went to the farm, and many people, and then to the Lord the seventy and the twelve apostles, and | then then the Lord Jesus kept going to this town, and then there died in this town the son of one widow woman.

  1  begins this holy-gospel
  2  write holy-Luke inside
  3  one-[?] chapter <preposition_of_genitive>-write
  4  time then-exist
  5  Lord-Jézus inside thirty | two
  6  year time go | Lord
  7  Jézus inside one town and this town name
  8  exist Nain and go farm Lord many people
  9  and then-exist to-Lord seventy and six-six apostle and | then
 10  then-exist keep_going Lord-Jézus this town and then-exist
 11  die inside this town son one virgin-woman

## 163v — weep not

> and the son was carried; therefore the brethren of the son, the Lord God, the thief, therefore humble; the son was of the Lord God, therefore God had the son carried out of the town, two by two among the men, at the head, because they had him within. The word of the Old Testament: he was borne out of the town, to the aforesaid wide world; and there were to the son many people; and then they left behind an army, an army, among the gates, from the two peoples, the people, two; and they left […]; and the Lord Jesus saw many sorrowing; and then this woman, the chief, remained a widow, sorrowing, this one; how then this? Said the Lord Jesus: stand up | this

  1  and son carry therefore* brethren-~son Lord-<suffix_of_divine_name> thief therefore* humble
  2  son exist Lord-<suffix_of_divine_name> therefore* God have-~son out(ward) on-town
  3  two-two among man head because have inside.
  4  <pertaining_to_the_Old_Testament> word get_conceived out(ward) town to-from earlier_mentioned the_whole_wide_world and exist
  5  to son many people and then-exist leave-to-leave an_army
  6  an_army among ~gate from-two people people two
  7  and leave [...] and see Lord-Jézus many
  8  sad(ly) and_then this woman head remain-+the_Baptist/woman
  9  sad(ly) this how? then-exist this say Lord-Jézus stand_up | this

## 164r — young man, I say to thee, arise

> the woman's son; and the Lord Jesus left off from the coffin, which within the coffin to the son, from the two by two men at the head; and the Lord Jesus touched, why in turn, from the coffin, which within the coffin lay dead, the son of this widow woman; and then | the Lord Jesus raised this son -- in this example, the son […] -- and he rose and sat up. How? As one prophet; and thus the Lord went; his descendant, to the pleasing of the Lord, the prophet foretold through this the Lord went; and then the Lord Jesus took the son, of the son | faith, love, hope […]; and | faith, love, hope

  1  woman <preposition_of_genitive> son and leave Lord-Jézus from coffin which inside coffin
  2  to-~son to-+son from two-two man head and
  3  touch Lord-Jézus <preposition_of_genitive> why?-in_turn from coffin which inside coffin
  4  lie die son this virgin-woman and_then | Lord
  5  Jézus rise this son example* son [...] and rise
  6  on-sit how? one prophet and_then this_is
  7  go-Lord descendant to-pleasing-Lord prophet through predict this_is
  8  go-Lord and_then Lord-Jézus grab-~son <preposition_of_genitive>-son | believe
  9  love-hope-[?] and | believe-love-hope

## 164v — and he gave him to his mother

> mercy, the day; and they put the son, faith, love, hope, mercy, | upon the son's shoulder; and the son took, why in turn, the Lord Jesus; and then the son was; the Lord took the son's mother, and the son went to the temple, the mother; he was saved; the son's temple, the mother, home to heaven; much joy, in turn, one sorrow remitted. And in turn the two of them could see the Lord Jesus Christ; and the Lord, every thanks they gave him. Here ends this holy gospel. The Lord's love. Written by holy Luke in the […] chapter of the writing. This woman signifies the mother, the temple, faith, the three baptisms,

  1  have_mercy day and put son believe-love-hope-have_mercy | on-<preposition_of_genitive>
  2  son shoulder and son grab on-why?-in_turn Lord-Jézus and
  3  then-exist son exist grab-Lord <preposition_of_genitive>-son mother and
  4  go son temple mother be_saved <preposition_of_genitive>-son temple mother
  5  ~home heaven many joy in_turn one sad(ly) remit
  6  in_turn-two see-somebody can Lord-Jézus-Christ and Lord
  7  each,_every thanks grab-somebody end this holy-gospel the_Lord love
  8  write holy-Luke inside one-[?] chapter <preposition_of_genitive>-write
  9  this woman symbolize mother temple believe three-+baptize

## 165r — what the widow and her son signify

> the widow; the son signifies the soul of every man, that the Lord God, the Lord's heart, every man; this town signifies that, that he is saved, that […] the Lord Jesus Christ, all the wide world | this this is saved: every man who believes, the three baptisms, the widow […] the Lord saves, the Lord Jesus Christ, of the Father, of the Lord. In this gospel, as holy Luke writes, there went two by two men at the head, to the son; in this example the son […] and the son was dead; and the son they took and carried; therefore love | the Lord God. The thief, therefore, is humble; the Lord God, therefore, has

  1  the_Baptist/woman son symbolize soul each,_every somebody that* Lord-<suffix_of_divine_name> heart-Lord
  2  each,_every somebody this town symbolize that* that* be_saved
  3  that* [...] Lord-Jézus-Christ each,_every the_whole_wide_world world | this
  4  this be_saved each,_every somebody believe three-+baptize the_Baptist/woman [...]
  5  the_Lord be_saved Lord-Jézus-Christ from-father-<suffix_of_divine_name> <preposition_of_genitive>-Lord
  6  inside this gospel <subject_marker> write holy-Luke go two-two man
  7  head to-~son this example* son [...] and son
  8  exist die and son grab and carry therefore* love | Lord
  9  <suffix_of_divine_name> thief <subject_marker> therefore* exist humble Lord-<suffix_of_divine_name> therefore* have

## 165v — the first of the four ways

> the Lord God; and this, therefore, repentance […] took this son, this widow woman; and the son was carried out, into belief. The three baptisms, the widow: that is, the son cast out, remitted, saved, the damned son. Chapter. Chapter. In the gospel written by holy Luke, this example: therefore love the most high Lord God | from the letter, with all the heart; rather, love, and this, and the heart, love the son, and therefore the brethren. Then the dead son goes to the son, and leaves; therefore love on the first way. In the gospel written by holy Luke, this example: there were many thieves, but by name the son

  1  Lord-<suffix_of_divine_name> and this therefore* repentance [...] grab this son this
  2  virgin-woman and son carry out(ward) on-believe.
  3  three-+baptize the_Baptist/woman that_is throw_out son remit be_saved
  4  be_damned son chapter-oh chapter-oh inside gospel write
  5  holy-Luke this example* therefore* love high Lord-<suffix_of_divine_name> | from
  6  literal each,_every heart but_rather love-and-this-and heart love-son and therefore* brethren*
  7  then-chapter die-son go to-son and leave therefore* love
  8  on-one ways* inside gospel write holy-Luke
  9  this example* <subject_marker> exist many thief but-+name-to son

## 166r — the second, third and fourth ways

> in repentance took; then the dead son goes to the son. And the thief leaves, on the second way. In the gospel written by holy Luke, this example: therefore be humble, son, man; and the Lord God; then the dead son goes to the son, and leaves; therefore be humble, on the third way. In the gospel written by holy Luke, this example: therefore he has, the son, the Lord God, in all of the son's […] […] the son is within […] then the dead son goes to the son, and leaves; therefore he has

  1  on-repentance grab then-chapter die-son go to-son.
  2  and leave thief on-two ways* inside-gospel write
  3  holy-Luke this example* therefore* exist humble son
  4  somebody and Lord-<suffix_of_divine_name> then-chapter die-son go to-son
  5  and leave therefore* exist humble on-+three ways* inside-gospel
  6  write holy-Luke this example* therefore* have
  7  son Lord-<suffix_of_divine_name> inside each,_every <preposition_of_genitive>-son [whosoever_sins_dies]
  8  [...] <subject_marker> exist son inside [whosoever_sins_dies]
  9  then-chapter die-son go to-son and leave therefore* have

## 166v — the whole law in two commandments

> on the fourth way; and […] the two by two men, and the son they took, the two by two men, and carried the son out […] of the town, into belief; the three baptisms, the widow; into damnation, then the son is carried into hell, damned. Chapter. Chapter. […] therefore be saved. It is written in Moses, truly: love the Lord God most high with all thy heart, with all thy soul, with all thy might, with all thy heart; and of thy father's son, how a man loves his neighbour | of the man; heaven and earth. Here ends this holy gospel.

  1  on-two-two ways* and [...] two-two man and son
  2  grab two-two man and son carry out(ward) [...]
  3  town on-believe three-+baptize the_Baptist/woman on-be_damned then-chapter
  4  son carry inside hell be_damned exist chapter-oh.
  5  chapter-oh [...] therefore* be_saved write inside
  6  Moses righteous(ly) love Lord-<suffix_of_divine_name> most_high each,_every heart each,_every <preposition_of_genitive>-somebody
  7  soul each,_every <preposition_of_genitive>-somebody might each,_every <preposition_of_genitive>-somebody heart and
  8  <preposition_of_genitive>-somebody from-father son how?-to somebody neighbour | <preposition_of_genitive>
  9  somebody <subject_marker> heaven land end this holy-gospel

## 167r — a certain rich man had a steward

> This holy gospel begins, written by holy Luke in the sixth chapter of the writing: the time the Lord Jesus said to the apostles of the Lord, and to the Jewish people: there was a certain rich man, who left in his sight, a steward over the rich man's goods | — sight, speech, life, hearing, soul, mind, reason, sense — all to manage; and the man began, the steward, this rich man's sight, speech, life, hearing, soul, mind, reason,

  1  begins this holy-gospel
  2  write holy-Luke
  3  inside six chapter <preposition_of_genitive>-write
  4  time say Lord-Jézus
  5  apostle <preposition_of_genitive>-Lord and Jew(ish)
  6  people exist one rich-?whosoever who leave-from-rich-see
  7  manager on-<preposition_of_genitive>-Lord-rich-somebody | rich-see-say-living-hear
  8  soul-exist-exist-chapter-reason-sense each,_every manage
  9  and begin-somebody-manager this rich <preposition_of_genitive>-Lord-rich-somebody
 10  see-say-living-hear-soul-exist-exist-chapter-reason

## 167v — the same was accused unto him

> sense to manage; and then he began, the man, and then a man came to accuse one servant before the steward; the man's lord spoke to the servant, this serving angel: all of the rich man's | […] soul, mind, reason, sense […] sense, the word, he scattered; be humble, this rich Lord God | this rich man. The man, and then, to the account: therefore many of the rich man's, the steward; and he heard this, the steward, this said from the steward's rich lord […] and | sorrowing

  1  sense manage and then-exist <subject_marker> ~begin man* and then
  2  somebody exist accuse one servant before
  3  <preposition_of_genitive>-manager somebody-Lord say-~servant this angel-servant
  4  each,_every <preposition_of_genitive>-Lord-rich-somebody | [?]-soul.
  5  exist-exist-chapter-reason-sense [...] sense
  6  word scatter humble this rich-rich-Lord-<suffix_of_divine_name> | this-rich.
  7  somebody and_then to-?the_account many therefore* <preposition_of_genitive>-Lord-rich-somebody
  8  manager and hear this manager this say from
  9  <preposition_of_genitive>-manager Lord-rich-somebody [...] and | sad(ly)

## 168r — what shall I do?

> the steward, the steward left off; and then this steward, the weeping steward […] and […] […] and […] […] the steward […]; and he found one accusation against the steward, and then this steward had two debtors | of the steward, a man of mercy and of alms; and | then there was, among the steward's, this one debtor of mercy; and this said, the steward: how much mercy dost thou owe the steward? […] And then the debtor of mercy: a hundred measures of oil. And then this steward sat him down, the man of mercy,

  1  manager leave-manager and_then this manager crying-manager
  2  [dig] and [...] [...] and [...] [...]
  3  manager [...] and one was_accused* find-manager
  4  and then-exist have this manager two indebted | <preposition_of_genitive>
  5  manager man* have_mercy and alms and | then
  6  exist among-manager this one indebted have_mercy and say this
  7  manager how_much? have_mercy indebted <preposition_of_genitive>-manager [...]
  8  and_then indebted have_mercy-somebody hundred* measure
  9  oil and_then this manager sit-have_mercy-somebody

## 168v — sit down quickly, and write fifty

> to write down fifty, in turn fifty | mercy, the man, down […] this, and this […] of the steward's rich Lord God; and then these two, the steward | mercy, the man […] […] divided into two parts, the steward of mercy, and among these, the steward, these two debtors | alms, the man; and this said, the steward: how much alms dost thou owe, to the steward's rich lord? And then the debtor of alms: a hundred measures of wheat. And then this steward | sat the man of alms down, to write down | from five,

  1  to-down and write fifty in_turn five-rich-ten | have_mercy
  2  somebody to-down [...] this and this [...] <preposition_of_genitive>-manager
  3  Lord-<suffix_of_divine_name>-rich-somebody and_then this two manager | have_mercy
  4  somebody [...] [...] divide_into_parts-two-manager-have_mercy-somebody
  5  ~and among this manager this two indebted | alms
  6  somebody and say this manager how_much? alms indebted
  7  <preposition_of_genitive>-manager Lord-rich-somebody and_then indebted alms
  8  hundred* food wheat and_then this manager | sit
  9  alms-somebody to-down and write from | five

## 169r — the lord commended the unjust steward

> thirty, in turn twenty, the man of alms, down […] this, and these two […] […] of the steward's rich Lord God; and in turn […] he took, this, the steward's rich Lord God, because the steward was found accused; and then this steward, these two, the steward's men of alms […] […] | divided, the steward's two men of alms. And then the Lord Jesus: O, of the Lord, son; have, apostles, truly: the steward was have, apostles, found accused, because the Lord, this Lord, this rich Lord God, the man; the Lord took to you many riches,

  1  thirty in_turn two-ten-rich alms-somebody to-down [...]
  2  this and this two [...] [...] <preposition_of_genitive>-manager Lord-<suffix_of_divine_name>-rich-somebody
  3  in_turn unjust_steward* grab this <preposition_of_genitive>-manager Lord-<suffix_of_divine_name>-rich-somebody
  4  because manager was_accused* find and_then this manager
  5  this two-manager-alms-somebody [...] [...] | divide
  6  two-manager-alms-somebody and_then Lord-Jézus
  7  oh <preposition_of_genitive>-Lord son have-apostle righteous(ly) manager exist
  8  have-apostle was_accused* find because-Lord this-Lord this
  9  rich-Lord-<suffix_of_divine_name>-somebody grab-Lord you many rich

## 169v — the goods are the senses

> the Lord took to you sight, the Lord took to you speech, the Lord took to you life, the Lord took to you hearing, the Lord took to you soul, the Lord took | is he yours? The mind the Lord took to you, reason the Lord took to you, sense the Lord took. To you, all of the rich Lord God's | sight, speech, life, hearing, soul, mind, reason, sense; and the apostles and the Jews are, truly, stewards over | sight, speech, life, hearing, soul, mind, reason, sense, in turn, in this world; the rich man has these apostles and Jews found accused.

  1  grab-Lord you see grab-Lord you
  2  say grab-Lord you living grab-Lord you
  3  hear grab-Lord you soul grab-Lord | is_he*
  4  yours exist-exist-chapter grab-Lord you reason
  5  grab-Lord you sense grab-Lord.
  6  you each,_every <preposition_of_genitive>-Lord-<suffix_of_divine_name>-rich-somebody | rich-see-say.
  7  living-hear-soul-exist-exist-chapter-reason-sense
  8  and exist-apostle-Jew(ish) righteous(ly) manager inside | rich-see-say
  9  living-hear-soul-exist-exist-chapter-reason-sense
 10  in_turn inside this world* rich have this-apostle-Jew(ish) was_accused* find

## 170r — the account, and a new gospel begins

> Here ends this holy gospel, spoken by holy Luke. Have | this: the apostles, the Jews, the man, truly, are stewards of the man's father, the son; and among them the man has the son. He is found accused, because then the dead man is accused; the man is quieted; accused. Here ends this holy gospel. To the apostles, the Lord God, with all thy heart; the Lord God have mercy. This holy gospel begins, written by holy Matthew in the fifth chapter | of the writing; by holy Luke in the | twenty- second chapter; the holy chapter of Jerusalem, in the ninth chapter: the time, then, the Lord Jesus, in

  1  end this holy-gospel speak holy-Luke have | this
  2  apostle-Jew(ish)-somebody righteous(ly) manager <preposition_of_genitive>-somebody father
  3  son and among somebody son have somebody.
  4  was_accused* find because then-chapter die-somebody exist
  5  was_accused* somebody calm_down was_accused* end
  6  this holy-gospel on-apostle Lord-<suffix_of_divine_name> with_all_thy_heart* Lord-<suffix_of_divine_name> <subject_marker>-have_mercy
  7  begins this holy-gospel write
  8  holy-Matthew inside five chapter | <preposition_of_genitive>
  9  write holy-Luke inside | two-two
 10  two-two chapter holy-chapter-+one-Jerusalem inside nine chapter
 11  time then-exist Lord-Jézus inside

## 170v — can the children of the bridegroom mourn?

> his thirtieth year; the time the Lord Jesus went into the temple at Jerusalem, and | then he was in the temple; the Lord Jesus went, and the Lord saw the son, much joy and much sorrow; and from afar off were the apostles of holy John the Baptist; and then the Lord Jesus left off; and then the apostles answered: the apostles fast, and the Pharisees fast; in turn, the Lord's apostles — why do thy apostles not fast? And then the Lord Jesus to the apostles: | in joy, in turn; then the apostles go in joy, keeping watch, while the apostles are two years; thus the apostles leave the Lord Jesus, from the chief man; and then the apostle Jairus: Jairus's daughter is dead; to the high priest, this one who answered; and he took this chief man.

  1  thirty years* time go Lord-Jézus inside Jerusalem temple and | then
  2  exist inside temple go Lord-Jézus and see-Lord son* many joy
  3  and many sad(ly) and from-to-far exist apostle holy-John
  4  three-+baptize the_Baptist/woman and then-exist leave Lord-Jézus and_then apostle
  5  answered apostle fast-apostle and Pharisee fast in_turn <preposition_of_genitive>-Lord apostle
  6  therefore* fast-apostle and_then Lord-Jézus to apostle | on
  7  joy in_turn then-exist go apostle on-joy observe exist
  8  apostle two-year ~on-that_is leave apostle Lord-Jézus from head
  9  and_then apostle Jairus <preposition_of_genitive>-Jairus daughter <subject_marker> die to-high_priest
 10  this ~exist-who answered and grab this head.

## 171r — the woman who touched the hem

> The Lord Jesus; and the Lord Jesus went with the chief man to this chief man's house; and this one went, the Lord, and many people; and there was among this people one woman, a chief woman, which chief woman had been twelve years in an issue of blood; and then this woman, the chief, then this woman: how shall we touch the woman? Why in turn? Of the Lord she believed: the hem — this woman, the woman's healing, the woman left off; and then she touched, believing, the Lord Jesus, | within the hour the woman was healed, the woman left off; and the Lord Jesus saw upon the people; the Lord's hand; there were many people; and then the Lord Jesus, this

  1  Lord-Jézus and go-Lord-head-Jézus this head
  2  house and go this-who Lord many people and exist
  3  among this people one woman head which
  4  woman head exist nine-year-six-six-year inside blood from-donkey
  5  and_then this woman head then-exist this-woman
  6  how_shall_we* touch <preposition_of_genitive>-woman why?-in_turn <preposition_of_genitive>-Lord believe-exist
  7  hem this-woman healing-woman leave-woman and
  8  then-exist touch believe-exist Lord-Jézus | inside
  9  hour healing-woman leave-woman and see Lord-Jézus
 10  on-people hand-Lord ~exist many people and_then Lord-Jézus this

## 171v — thy faith hath made thee whole

> woman: the woman's faith healed the woman. Afterward, which day the Lord Jesus said, this Lord, to this woman, the Lord healed her; but the Lord Jesus said to this woman: the woman's faith hath healing done. And | the Lord went, the chief man, the apostles, Jesus, the woman; this chief man's house said, and | then the Lord, the chief man […] Jesus, the woman, going in; and he saw, the Lord Jesus, much sorrow; and then the Lord Jesus […] therefore: this daughter is not a dead daughter, but rather the daughter sleeps. And then they laughed, said the Lord Jesus; and then he said: see, love | this

  1  woman <preposition_of_genitive>-woman believe healing-woman afterward*
  2  who-+day say Lord-Jézus this-Lord this-woman from-healing-Lord but
  3  say Lord-Jézus this-woman <preposition_of_genitive>-woman believe healing
  4  do, and | go-Lord-head-apostle-Jézus-woman
  5  say this head house and | then-exist-Lord
  6  ~head-[?]-Jézus-woman-+say inside-go and see
  7  Lord-Jézus many sad(ly) and_then Lord-Jézus [...]
  8  therefore* this daughter die-daughter but_rather to-sleep-daughter and then-exist
  9  say laugh Lord-Jézus and_then say see love | this

## 172r — damsel, arise

> the Lord […] spoke; and then the Lord Jesus, this chief man, cast this people out; and then, having cast out, the chief man, and with the Lord Jesus the daughter's father and mother; and then the Lord Jesus to the sky said, said, named this: servant, arise, servant daughter, among maidens; and | then the daughter stood up and sat; and then, lo, the Lord went, his descendant, to the pleasing of the Lord, the prophet foretold through; lo, the Lord went; and then the Lord Jesus had the father and mother bring wine and bread […] […] and drink; and then the daughter

  1  Lord [...] speak and_then Lord-Jézus this head.
  2  cast_out this people out(ward) and then-exist out(ward) cast_out
  3  head and among Lord-Jézus <preposition_of_genitive>-daughter father
  4  and mother and_then Lord-Jézus sky say say name-this
  5  one-+servant rise servant daughter among virgin-girl and | then
  6  exist stand_up daughter on-sit and_then lo go-Lord
  7  descendant to-pleasing-Lord prophet through predict lo go-Lord
  8  and_then Lord-Jézus carry father mother wine and bread
  9  [...] [...] and drink and then-exist daughter

## 172v — the fame of it went abroad, and the talents begin

> drank; and the daughter […]; and then the Lord Jesus, this month, […] therefore said; and the news went out into all the sky and earth. Here ends this holy gospel. The Lord God, with all thy heart. This holy gospel begins, written by holy Stephen the king; this word, written, the chief; this world, the Lord, the priest; and the high Magdalene day, the king, all the Lord […]; and the farm, the people; this word he speaks, from the king; there was a rich lord going a long way; and | then the Lord had three living servants; and then the servants

  1  drink and [?]-daughter and_then Lord-Jézus this moon
  2  [...] therefore* say ~and news leave each,_every sky
  3  earth end this holy-gospel Lord-<suffix_of_divine_name> with_all_thy_heart*
  4  begins this holy-gospel.
  5  write holy-Stephen king
  6  this word write head
  7  this world* Lord priest.
  8  and high-Magdalene-+day king each,_every
  9  Lord to-[?] and farm people this word speak-from-+king exist
 10  go-Lord one rich Lord long way and | then
 11  exist have-Lord three living-servant and then-exist living-servant

## 173r — one talent, three talents, five talents

> before the Lord; he was with the Lord; and then the Lord took one servant, one talent of gold; and in turn the Lord took three talents of gold; the third the Lord took, five talents of gold; and then this rich lord, all, until this […]: five senses, mercy, prayer, alms, faith […]; the servant's mouth, this Lord went to […]; be saved, how shall we, living servant; and the Lord took the priest, the high Magdalene day, the king, the Lord, to […], the farm, the people, the man, soul, soul, soul, soul. Here ends this holy gospel. The Lord's love.

  1  <subject_marker> before Lord exist ~among-Lord and then-exist grab-Lord
  2  one servant one gold* talent in_turn-two
  3  grab-Lord three gold* talent third grab-Lord
  4  five gold* talent and_then this rich-Lord each,_every until
  5  this [...] five sense have_mercy pray.
  6  alms believe [ability] servant mouth
  7  this-Lord go to-[?] be_saved how_shall_we* living-servant and Lord grab priest
  8  high-Magdalene-+day king Lord to-[?] farm people somebody
  9  soul soul soul soul end this holy-gospel the_Lord love

## 173v — after a long time the lord came

> Many years passed; then this rich lord returned | to the lodging, because from the lodging the way of the people lay into the house of this rich lord; and from the people, the servant carried this rich lord; and then he went out | among the Lord's, this rich man and the Lord's living servants, the apostles, the angels; and then he did so among this rich lord's; the Lord's servant, before the rich lord […] the three servants stood; the Lord took | of the rich Lord; and then this rich lord, this one to whom the Lord had given five talents of gold — and then this rich lord reckoned with the servant: how shall the man

  1  many year exist then-exist return this rich-Lord | on
  2  lodging because from* lodging way people inside house this
  3  rich-Lord and from people servant carry this rich-Lord and
  4  then-exist go out(ward) on | among-Lord this rich
  5  and <preposition_of_genitive>-Lord living-servant-apostle-angel and then-exist do,
  6  among this rich-Lord <preposition_of_genitive>-Lord servant before rich-Lord
  7  [...] three <subject_marker> servant exist-Lord grab-Lord | <preposition_of_genitive>
  8  Lord rich and_then this rich-Lord this one to_whom
  9  <subject_marker> exist-Lord grab-Lord five gold.*
 10  talent and_then this rich-Lord reckon_with* servant how_shall_we-somebody

## 174r — well done, good and faithful servant

> of the rich Lord? This servant said: how shall the man be pleasing to the Lord God? And he received the aforesaid five talents of gold; and then this rich lord: go, servant, into the Lord's house, to the Lord's Father, and to the Father; the man shall be a man of joy. Chapter. Chapter. Amen. And then, among the Lord's, this second, to whom the Lord had given three talents of gold; and then this rich lord reckoned with the servant: how shall the man | of the rich Lord? This servant said: how shall the man be pleasing to the Lord God? And he received the aforesaid three talents of gold; and then this rich lord:

  1  <preposition_of_genitive>-Lord rich say this servant how_shall_we-somebody to-pleasing Lord-<suffix_of_divine_name> and
  2  receive* five gold* earlier_mentioned talent and_then this rich Lord
  3  go-servant inside <preposition_of_genitive>-Lord to-house to-<preposition_of_genitive>-Lord from-father-<suffix_of_divine_name> and
  4  to-father-<suffix_of_divine_name> somebody exist joy-somebody chapter-oh
  5  chapter-oh amen and then-exist among-Lord this two
  6  to_whom <subject_marker> exist-Lord grab-Lord three gold* talent
  7  and_then this rich-Lord reckon_with* servant how_shall_we-somebody | <preposition_of_genitive>
  8  Lord rich say this servant how_shall_we-somebody to-pleasing Lord-<suffix_of_divine_name>
  9  and receive* three gold* earlier_mentioned talent and_then this rich Lord

## 174v — the third servant

> go, servant, into the Lord's house, to the Lord's Father, and | to the Father; the man shall be in joy. Chapter. Chapter. Amen. And then, among the Lord's, this third, to whom the Lord had given one talent of gold; and then this rich lord reckoned with the servant: how shall the man? Of the rich Lord, this servant said […] servant […] […] […] […] there is love, there is riches […] servant, because this Lord […] the servant has, because then this servant of the rich Lord lost the servant; this Lord is […]

  1  go servant inside <preposition_of_genitive>-Lord to-house to-<preposition_of_genitive>-Lord from-father-<suffix_of_divine_name> and | to
  2  father-<suffix_of_divine_name> somebody exist ~joy chapter-oh chapter-oh
  3  amen and then-exist among-Lord this three to_whom <subject_marker>
  4  exist-Lord grab-Lord one gold* talent
  5  and_then this rich Lord reckon_with* servant how_shall_we-somebody
  6  <preposition_of_genitive>-Lord rich say this servant [...] servant [...]
  7  [...] [...] [...] love-exist exist-rich [ability] servant
  8  because this-Lord [...] have servant because then-exist this-servant
  9  <preposition_of_genitive>-Lord rich lose ~servant this-Lord exist [...]

## 175r — take the talent from him

> upon the servant; the rich man has this Lord, and from extortion upon the servant he took; because this rich Lord God […] […] | […] said, the man; and he said; and then this rich lord: this unprofitable servant, high, this servant, this | servant's love is this: the eye sees the servant, the Lord's house is far off, this | love is: go, servant, into the Lord's house. And then this rich Lord's servant, the angel, took from this unprofitable servant this one talent; and the angel took the talent from him and gave it to the faithful servant, the servant who has ten talents. Here ends this holy gospel.

  1  on-~servant rich have this-Lord and from extort* on-~servant
  2  grab because this-rich Lord-<suffix_of_divine_name> [...] [...] | [?]-+say
  3  man* and say and_then this-rich-Lord
  4  this unhelpful servant high this-servant this | ~servant-love
  5  exist this eye see servant <preposition_of_genitive>-Lord to-house long this | love
  6  exist go-~servant inside <preposition_of_genitive>-Lord to-house and_then this rich
  7  <preposition_of_genitive>-Lord ~servant grab angel from this unhelpful ~servant
  8  this one talent and talent grab angel from
  9  believe ~servant servant talent ten have end this holy-gospel

## 175v — the Lord goes from town to town

> This holy gospel begins, written by holy Luke in the sixth chapter of the writing: the time, then, the Lord Jesus, in his thirtieth year; the time the Lord Jesus went among the people, and the Lord's apostles, from town to town, town; from temple to temple, temple; from village to village, village; and the Lord's apostles; and they went

  1  begins this holy-gospel write holy-Luke
  2  inside six chapter <preposition_of_genitive>-write time
  3  then-exist Lord-Jézus inside thirty years*
  4  time go Lord-Jézus among_the_people* and <preposition_of_genitive>-Lord apostle from town
  5  from_town_to_town* town from temple from_town_to_town* temple from
  6  village from_town_to_town* village and <preposition_of_genitive>-Lord apostle and go

## 176r — the woman of Samaria at the well

> the Lord Jesus, to one well; and the Lord Jesus sat by this well, because there was […]; the Lord was wearied; in turn the apostles went, the apostles, into the village for bread, and the living brethren, the mind, living; and then there came one chief woman | to this well; and then she dipped […] this well; and then the Lord Jesus was thirsty, and […] the Lord asked her for water; and then this woman of an alien nation: how is it, this Lord | dares, the Lord, to ask water of a pagan? This woman of an alien nation in turn: | this Lord is a Jew; she dipped for the Lord […] to drink, the Lord, and

  1  Lord-Jézus one well and sit Lord-Jézus to-this
  2  well because exist [...] get_tired-Lord in_turn apostle go-apostle
  3  inside village on-+bread ~and living brethren-+<subject_marker> exist-exist-chapter
  4  living and then-exist go one woman head | to
  5  this well and then-exist dip-[?] this well and_then
  6  Lord-Jézus thirsty-Lord and [?]-[?]-+<subject_marker> exist-Lord water
  7  ~ask_(for) and_then this of_an_alien_nation,_pagan how? this-Lord | dare
  8  Lord from pagan water ~ask_(for) this of_an_alien_nation,_pagan in_turn | this
  9  Lord Jew(ish) dip-+the_Lord [...] on-drink Lord and

## 176v — the Lord begins to speak to the Gentiles

> he began to speak through the pagan, the Lord Jesus; and the woman of an alien nation | judged this; she had, to the pagan man; and of an alien nation the Lord began | to speak this: lift up, woman of an alien nation, do at home likewise, | do, pagan; she left off, the woman of an alien nation; and then this woman of an alien nation | upon the alien nation […] which; and from […] this Lord, this Lord's descendant, the Lord, to the pleasing of the Lord, the prophet foretold; and the apostles went to the Lord, and the apostles began; the miracle upon the Lord; the Lord's love; the Lord spoke this | one baptism, two baptisms, the chief; and this woman of an alien nation believed in the Lord Jesus; and the woman of an alien nation went to her own | […] from

  1  begin through speak pagan Lord-Jézus and of_an_alien_nation,_pagan-+<subject_marker> | ~judge
  2  this ~have to-+pagan man and of_an_alien_nation,_pagan begin-Lord | say
  3  this-lift_up of_an_alien_nation,_pagan home do, likewise* | do,
  4  pagan from-leave <preposition_of_genitive>-of_an_alien_nation,_pagan and_then this of_an_alien_nation,_pagan | on-<preposition_of_genitive>
  5  of_an_alien_nation,_pagan [...] which and from [...] this-Lord this-Lord descendant
  6  Lord to-pleasing-Lord prophet predict and go apostle to-Lord
  7  and begin-apostle miracle on-Lord love-Lord speak-Lord this | one-+baptize
  8  two-+baptize head and believe this of_an_alien_nation,_pagan inside
  9  Lord-Jézus and go of_an_alien_nation,_pagan to-<preposition_of_genitive>-of_an_alien_nation,_pagan | [?]-from

## 177r — come, see a man who told me all things

> […] and then she went into the village, and the woman of an alien nation began to speak | this: this people, sit; one Lord at the well, and even more from the Lord, to the pleasing of the Lord, the prophet foretold through; because the alien woman's home he did; the love of the alien woman he did; the alien woman left off, the alien woman's all that she was and did […]; the alien woman said […]; and then this people believed in the Lord, the man, the people; and the people went to this well, because they would pray to the Lord; | then and the people were there, and the Lord preached one to two years.

  1  [...] and then-exist go inside village and begin-of_an_alien_nation,_pagan say | this
  2  this people sit one Lord to-well even_more from-Lord
  3  to-pleasing-Lord prophet through predict because <preposition_of_genitive>-of_an_alien_nation,_pagan home
  4  do, love-of_an_alien_nation,_pagan do, of_an_alien_nation,_pagan from-leave
  5  <preposition_of_genitive>-of_an_alien_nation,_pagan each,_every exist-+who-+day [...] of_an_alien_nation,_pagan-+<subject_marker> say-[?] and
  6  then-exist this people inside Lord-somebody believe-people and
  7  go-people this well because-Lord want-people pray | then
  8  exist and people exist-Lord preach one to-two-year

## 177v — the gospel ends, and another begins

> and even more to the Lord Jesus; but the Lord went into Galilee, to the town. Here ends this holy gospel. The Lord God, with all thy heart. This holy gospel begins, written by holy Luke, in

  1  and even_more-to Lord-Jézus a) to-go-Lord inside Galilee
  2  town end this holy-gospel Lord-<suffix_of_divine_name> with_all_thy_heart.*
  3  begins this holy-gospel
  4  write holy-Luke inside

## 178r — the ten lepers

> the fifth chapter of the writing: the time, then, the Lord Jesus, in his thirty- | first year; the time the Lord Jesus went into Jerusalem; and this one went, the Lord, and many people; and then the Lord Jesus went, the people, into the field, and there stood […] afar off ten leprous people; and the ten lepers began to cry out: son of David, king, have mercy — the ten lepers, son; and they cried to the Lord Jesus; go, ten lepers, and let the ten shew themselves to the priest; and the priest took the ten lepers, from all that was […] in the law of Moses; and then the ten lepers went | from

  1  five chapter <preposition_of_genitive>-write time then-exist Lord-Jézus inside thirty | one
  2  years* time go Lord-Jézus inside Jerusalem and go this-who Lord
  3  many people and then-exist go Lord-Jézus people on-+field-+one and
  4  leave [...] far ten leper people and begin ten
  5  leper shout-to son David king have_mercy
  6  ten leper son and shout-to Lord-Jézus go ten
  7  ~leper and ten appear priest and
  8  priest grab ten leper from each,_every-~exist [...]
  9  Moses law and then-exist go ten leper | from

## 178v — the priests dispute over them

> and they saw the lepers' minds; and then there were lepers, the mind, healing; and one Wednesday, ten […] […] […]; and then the ten lepers went, the ten people, there to the chief men of the Jews, before the priest; and then the priests of the Jews: how are you people, ten | lepers? Chapter. Said […] the lepers, from the people […] the lepers; the people were before the priest, among the priests, the Jews, the man; they cast the priest out; the Jews said to the priest; the Jews: who of you men is healed? | said the leper

  1  see <preposition_of_genitive>-leper exist-exist-chapter and then-exist exist
  2  leper exist-exist-chapter healing and one-+Wednesday ten [...]
  3  [...] [...] and then-exist ten leper go-ten-people-exist-to
  4  head Jew(ish) before priest and_then
  5  priest Jew(ish) how? you people ten | leper
  6  chapter say [...] leper from-people [...] leper.
  7  people exist priest among priest Jew(ish)-somebody
  8  out(ward) cast_out priest Jew(ish) say priest.
  9  Jew(ish) who? you somebody from-healing | say-leper

## 179r — where are the nine?

> the ten people healed: son of David, king; said the chief men, the Jews, the priest […]: you people, from the son have sinned; the Lord healed you; but you people were healed by Moses truly, because there is the word of the Old Testament, from the lepers; among the priests, the Jews, they cast them out, and then of the nine people a man believed the priests, the Jews; in turn the tenth man had faith, and returned back to the Lord Jesus; and the leper bowed down before the Lord's feet; and then the Lord's sister

  1  ten-people from-healing son David king say head
  2  Jew(ish) priest [...] you people from son
  3  sin_against from-healing-Lord a) you people-+<subject_marker> from-healing
  4  Moses righteous(ly) because-exist <pertaining_to_the_Old_Testament> word from
  5  leper-+say among priest Jew(ish) out(ward) exorcise
  6  and then-exist from nine people somebody believe from priest
  7  Jew(ish) in_turn ten somebody faith* a) return
  8  back against Lord-Jézus and bow_down leper
  9  before <preposition_of_genitive>-Lord foot and then-exist-Lord sister

## 179v — were not ten made clean?

> kissed, the tenth man, the Lord's feet; and the Lord was pleased, and the tenth man gave thanks; and then the Lord Jesus to the apostles | of the Lord, to all by name: and the people, were there not ten lepers? Which […] one, whosoever keeps the commandment; and whosoever keeps the commandment the Lord loves. And then the Lord Jesus to the apostles: of the Lord, good […] from | he is. Chapter. […] the son, the man; there is the Lord; the alien nation's love. Here ends this holy gospel. The Lord God's love. Three things must be believed in the world: first, believe in the most high; and then the pagan day, and the Jews believe in this and this; believe, one man,

  1  kiss-ten-somebody <preposition_of_genitive>-Lord foot and Lord pleasing
  2  and thanks grab-ten-somebody and_then Lord-Jézus apostle | <preposition_of_genitive>
  3  Lord name-each,_every-to and people exist ten leper in_turn-+who
  4  <subject_marker> [...] one whosoever-commandment and whosoever-commandment Lord love
  5  and_then Lord-Jézus apostle <preposition_of_genitive>-Lord good [...] from | is_he-chapter
  6  [...] son somebody exist Lord of_an_alien_nation,_pagan love end
  7  this holy-gospel Lord-<suffix_of_divine_name> <subject_marker> love three believe have
  8  from world* first <subject_marker> believe above-high and and_then-pagan-+day and Jew(ish)
  9  believe inside this-and-this believe one somebody

## 180r — one faith, one Church

> and the Jews, the pagan day, the most high; in turn, therefore, to be saved; and a man, therefore, believes, the man, in the Lord Jesus Christ; one man, therefore, is saved; but every man is damned; and secondly, believe the Church; and the Church's belief is good, because there is one Church; the Church, and in believing is salvation, because from the Church, the Church, one way, belief, the Church, the Church, in the Lord Jesus Christ, in his coming and in his death; then on the cross the Lord gave up the ghost; thirdly, believe in the coming of the Lord Christ; and through him escape.

  1  and Jew(ish)-pagan-+day above-high in_turn therefore* be_saved and somebody
  2  therefore* believe somebody inside Lord-Jézus-Christ one
  3  somebody therefore* be_saved a) each,_every somebody be_damned in_turn-two <subject_marker>
  4  believe <Christian_or_related_church_or_denomination> and <Christian_or_related_church_or_denomination> believe this_is good
  5  because one <Christian_or_related_church_or_denomination> <Christian_or_related_church_or_denomination> and inside believe be_saved
  6  because from <Christian_or_related_church_or_denomination> <Christian_or_related_church_or_denomination> one ways* believe
  7  <Christian_or_related_church_or_denomination> <Christian_or_related_church_or_denomination> inside Lord-Jézus-Christ inside coming* and inside
  8  die then-+<subject_marker> cross <preposition_of_genitive>-Lord soul give_up_the_ghost third
  9  <subject_marker> believe on-?coming Lord-Christ and through escape

## 180v — a summary of the Lord's life

> The Lord Jesus, and the Lord Christ made ready the twelve apostles; and many wearied, the Lord Christ, who wearied; the Lord did it; he went into the world | of the Lord, the apostles; and many a miracle the Lord Christ, in love, did | upon the world; the Lord's apostles went; the blind of eye he gave light; the dead man he stood up and raised; the evil upon the people […] the Lord | love, and this and this; the cup […] that day; the Lord healed; and the holy host, the mind, the Lord Christ, the brethren; the Lord at thirty stayed, the Lord, within the host; and the Lord Christ was humble, because the Lord was humble in this world. The chief men took the Lord, and the Jews captured him […]

  1  Lord-Jézus and prepare Lord-Christ six-six apostle and many get_tired
  2  Lord-Christ who get_tired-+<subject_marker> do,-Lord into_the_world* go-Lord | <preposition_of_genitive>
  3  Lord apostle and many miracle Lord-Christ love miracle-+<subject_marker> do, | on
  4  world go <preposition_of_genitive>-Lord apostle eye-blind <subject_marker> through light Lord die somebody
  5  <subject_marker> stand_up resurrect-chapter-Lord evil <subject_marker> on-people [?]-to-+who-Lord | love-and
  6  this-and-this cup-[?]-+day from-healing-Lord and holy-+host God exist-exist-chapter
  7  Lord-Christ brethren-+<subject_marker> Lord on-thirty stay-Lord inside host
  8  and humble Lord-Christ because-+the_Lord exist-Lord humble-Lord this world.*
  9  head grab-Lord and Jew(ish) <subject_marker> capture [...]

## 181r — Thomas was not with them

> […] and a crown of thorns upon his head | conceived, he said; and […] the Lord Christ died, and the Lord Christ rose, and the Lord Christ appeared to the Lord's apostles, one Saturday evening; and this evening it was; then the Lord appeared to the twelve apostles in the Lord's house, where the Lord God, the Lord Jesus, had made the supper; and | then holy Thomas came […] one Saturday evening to the apostles; and the apostles said: Thomas, the apostles have seen the Lord. And holy Thomas said, this Thomas: this I will not believe, all this, to whom | this; Thomas, this belief is blind […] unless Thomas sees

  1  [...] and thorn crown on-head | get_conceived
  2  say and [...] die Lord-Christ and rise Lord-Christ and appear
  3  Lord-Christ apostle <preposition_of_genitive>-Lord one Saturday evening and this
  4  evening exist then-exist-Lord appear-Lord six-six apostle
  5  inside Lord house where Lord-<suffix_of_divine_name> Lord-Jézus dinner-to do, and | then
  6  exist go holy-Thomas Didymus* one Saturday evening
  7  to-apostle and say apostle Thomas apostle see Lord and say holy-Thomas
  8  this-Thomas this not believe each,_every this to_whom | this
  9  Thomas this believe blind-[?] [...] see-Thomas

## 181v — blessed are they that have not seen

> the Lord's wounds, and unless Thomas puts his finger into the Lord's wounds, who from the Lord, from death, stood up. The time the Lord Jesus Christ came, into the midst of the apostles, the doors being shut, and said: peace be to you; and the judgment year; the apostles; in turn Thomas began to have, and said | the Lord Jesus: Thomas, come by name […] put thy finger into the Lord's wound […] see and believe; and […] the Lord Jesus, the Lord's wound; and the Lord Jesus said: Thomas, happy art thou from this; and the man who sees that day, believing; but also | blessed is the day, and the food; he sees, from believing. Here ends this holy gospel.

  1  <preposition_of_genitive>-Lord end and <preposition_of_genitive>-Thomas finger not put inside <preposition_of_genitive>-Lord
  2  end who from Lord from die stand_up time leave Lord-Jézus-Christ
  3  middle apostle closed and say commandment you exist
  4  and judge-year apostle in_turn Thomas begin have and say | Lord
  5  Jézus Thomas go-+name [hither] put <preposition_of_genitive>-Thomas finger
  6  inside <preposition_of_genitive>-Lord wound [...] see believe and [...]
  7  Lord-Jézus <preposition_of_genitive>-Lord wound and say Lord-Jézus Thomas happy-to
  8  from and somebody see [?]-+day ~believe but and | blessed
  9  day-to and food see from* believe end this holy-gospel

## 182r — the appearance at table, and the sending out

> The Lord God, with all thy heart. And this […] the man said, the Lord Jesus […] the man, the Lord, therefore, within that day […] the man; and then, after the Lord Christ was executed, in the […] year, the time the apostles sat at table in Jerusalem, in the Lord's house, | at the place where the Lord God, the Lord Jesus, had made the supper; the time the Lord Jesus appeared to the Lord's apostles, in the mind, the man; and he sat with the apostles, outside, and began to upbraid them | for their belief; and the Lord Jesus said: go, apostles, | into the world; and be baptized in the Lord's […]

  1  Lord-<suffix_of_divine_name> with_all_thy_heart* and this [...] somebody say Lord-Jézus [...]
  2  somebody Lord therefore* inside-+day-[?] somebody and then-exist
  3  on-execute Lord-Christ [?]-year inside
  4  time sit apostle to-table inside Jerusalem inside Lord house | to
  5  where* Lord-<suffix_of_divine_name> Lord-Jézus dinner do, time
  6  appear Lord-Jézus apostle <preposition_of_genitive>-Lord inside exist-exist-chapter somebody
  7  and sit to-apostle to-+out and begin admonish | on
  8  believe and say Lord-Jézus you go-apostle | on
  9  world* and exist two-+baptize the_Baptist/woman inside <preposition_of_genitive>-Lord exist-[?]

## 182v — baptize them in the name of the Father

> and let a man be baptized in the name of the Father and of the Son and of the Holy Spirit; and let him be to the Lord | to believe; every such man is saved, and one is damned […] […]; and let a man be baptized and be the Lord's; one is saved, but every man is damned. Here ends this holy gospel. The Lord God's love. Written by holy Luke in the second chapter of the writing: the time, then, after the execution

  1  and somebody exist two-+baptize the_Baptist/woman inside name father-<suffix_of_divine_name>
  2  and son and holy-spirit and exist Lord-to | to
  3  believe* each,_every somebody be_saved and one
  4  be_damned [...] [...] and somebody exist two-+baptize the_Baptist/woman
  5  and exist Lord-to one be_saved a)
  6  each,_every somebody be_damned end this holy-gospel Lord-<suffix_of_divine_name> <subject_marker>
  7  love write holy-Luke inside two
  8  chapter <preposition_of_genitive>-write time
  9  then-exist on-execute

## 183r — Chosroes carries off the Cross

> of the Lord Christ, twenty-six days; the time of sitting at Jerusalem. One of an alien nation there was, a man of substance, whose name was Chosroes; and then he seized upon Jerusalem, the tree of the Cross — the tree upon which Christ was executed — and the tree he carried off into the town of Ctesiphon, into one tower; and then there was war many years upon the Roman emperor, whose name was Heraclius; and then war went, this, to the pagan emperor.

  1  Lord-~Christ two-ten-ten six-+day time to-sit Jerusalem.
  2  one to-of_an_alien_nation,_pagan exist-+talent name
  3  exist Khosrow_(Chosroes)_<Sasanian_king> and then-exist grab on-Jerusalem
  4  cross tree ~on tree exist Christ
  5  execute and tree <subject_marker> from-carry inside
  6  Ctesiphon_<city_in_Persia> town inside one tower
  7  and then-exist exist many year war* on-Roman.
  8  emperor name exist Heraclius_<Byzantine_emperor>
  9  and then-exist war* go this to-of_an_alien_nation,_pagan emperor

## 183v — the sign given to Heraclius

> This Roman emperor then had two wars to fight, sinned against; and then Heraclius the emperor had a small army; and then he believed, as much as he could | from the Lord, giving thanks; the Lord God heard, the Lord God, the emperor's prayer; and God's angel cried out upon the water; Heraclius had it; the Lord God heard Heraclius's prayer; and then God's angel, Heraclius, the daughter, had him write upon his armour the tree of the Cross, and

  1  this Roman emperor then-exist have two war*
  2  on-fight sin_against and then-exist.
  3  little an_army have Heraclius_<Byzantine_emperor> emperor
  4  and then-exist believe on-?as can | from-to
  5  Lord to-thanks Lord-<suffix_of_divine_name> hear Lord-<suffix_of_divine_name> <preposition_of_genitive>-+emperor.
  6  as* and shout-to God angel on-water
  7  have Heraclius_<Byzantine_emperor> hear Lord-<suffix_of_divine_name> <preposition_of_genitive>-Heraclius_<Byzantine_emperor>
  8  as* and_then God angel Heraclius_<Byzantine_emperor> daughter
  9  have write on-<a_kind_of_armor_or_weapon> cross tree and

## 184r — the battle, and the tower at Ctesiphon

> the emperor won the fight, because the pagan emperor lost, the emperor; and then the two left, this pagan emperor and this Roman emperor; and then the two did battle | upon the chapter, within, to the Lord, the two; and the pagan people […] the people among […] died; in turn the Jewish people; and the pagan, to many […]; and then the pagan people died, and they began to pierce […] […] upon the pagan earth; and then Heraclius went into the town of Ctesiphon, to the place of this pagan emperor Chosroes, because the emperor sat in one

  1  win emperor on-fight because lose to-of_an_alien_nation,_pagan
  2  emperor and then-exist two leave this to-of_an_alien_nation,_pagan emperor
  3  this Roman emperor and then-exist-two do_battle | on-chapter-+one
  4  inside-to-Lord-two ~and to-of_an_alien_nation,_pagan people [...] people among [...]
  5  die in_turn Jew(ish) people and to-of_an_alien_nation,_pagan <subject_marker> to-many [...] and
  6  then-exist people to-of_an_alien_nation,_pagan die and begin pierce [...]
  7  [...] on-to-of_an_alien_nation,_pagan earth and then-exist go Heraclius_<Byzantine_emperor>
  8  inside Ctesiphon_<city_in_Persia> town on-place to-this to-of_an_alien_nation,_pagan
  9  emperor Khosrow_(Chosroes)_<Sasanian_king> because sit emperor inside one

## 184v — the tower of gold and precious stones

> tower; and the tower was all of gold, and built of precious stone, the tower, as though for one God; the emperor sat within, because he had set himself, the emperor, in one way, the emperor; and the emperor was all of gold, shedding blood; and in the second way the emperor had set the tree of the Cross, he himself, upon the gold; and then the emperor […] the water went up again upon the tower; and lo, the emperor took the rain, the emperor […] the emperor would take, and then the emperor made it within the tower, the day […] and to […] and […] and among the tree of the Cross

  1  tower and tower exist each,_every golden and precious_stone stone build tower
  2  how? one God inside-sit emperor because exist put
  3  emperor on-one ways* emperor and emperor exist each,_every
  4  golden shed_blood in_turn-two ways* put emperor cross tree
  5  he_is* exist on-golden and then-exist emperor [...]
  6  water go_up again* on-tower and lo rain grab
  7  emperor [?]-+<subject_marker> want emperor grab
  8  and then-exist emperor do, inside tower.
  9  day-[?] and to-[?] and [...] and among cross tree

## 185r — Chosroes sits between the cross and the cock

> of gold, among the cross, among the cock, the emperor sat, as though one […] from […] the emperor, to God he said, from, because there is the whole world […] and then Heraclius the emperor went to this pagan emperor in the tower; and then Heraclius the emperor believed, Heraclius's God, in turn, the whole wide world; this […] the chief; he said he must die, this | there was the emperor […]; and they took the emperor by the head, and then Heraclius the emperor did all

  1  golden among cross among cock sit emperor
  2  how? one [...] from [...] emperor
  3  to-God as-+say from because-exist each,_every world* [...]
  4  and then-exist Heraclius_<Byzantine_emperor> emperor go this to-of_an_alien_nation,_pagan
  5  emperor inside tower and_then Heraclius_<Byzantine_emperor> emperor
  6  believe <preposition_of_genitive>-Heraclius_<Byzantine_emperor> God in_turn the_whole_wide_world this
  7  [...] ~head-chapter die say this | ~exist
  8  emperor [...] and emperor ~head-grab and
  9  then-exist do, Heraclius_<Byzantine_emperor> emperor each,_every

## 185v — the Cross comes back to Jerusalem

> […] the tower he pierced; and the tower, God, he took up, and […] […] the son | from one woman; and the son the emperor left […] and he took the tree of the Cross, and carried it off into the town of Jerusalem; and then […] before | the army, the army; and then […] Jerusalem; and at the gate God's angel, the gate of Jerusalem; and the angel cried out to Heraclius: thus the Lord Christ did not carry the tree of the Cross out to Jerusalem in pride, but carried it in humility; and then he sat down […]

  1  [...] tower on-+pierce ~and tower God up grab
  2  ~and [...] [...] son | from
  3  one-woman and son emperor leave [...] and
  4  grab cross tree and <subject_marker> from-carry inside
  5  Jerusalem town and then-exist [...] before | army
  6  army and then-exist [...] Jerusalem and to-gate God
  7  angel ~gate Jerusalem ~and shout-to angel Heraclius_<Byzantine_emperor>
  8  this-this Lord-Christ proud out(ward) on-Jerusalem carry cross tree
  9  but humble carry and then-exist sit down [...]

## 186r — the emperor takes off his robes

> and took off from the emperor his clothes; and then […] and with bowed head carried the tree of the Cross into Jerusalem; and then, from the gate, God's angel, the gate of Jerusalem; and the emperor, many […] loved, he said, the tree of the Cross; and the emperor put the cross within Jerusalem, in the temple; and the emperor gave thanks to the Lord, the Lord God, the whole wide world; and there is a man who takes the holy tree of the Cross, the tree; and […] the tree of the Cross; and the tree of the Cross, two by two, through the law, upon all

  1  and take_off on-+emperor <preposition_of_genitive> clothes and_then*
  2  [...] and bowed head carry cross tree inside
  3  Jerusalem and then-exist from-gate God angel ~gate Jerusalem
  4  and emperor many [...] [?]-love-+say cross
  5  tree and cross <subject_marker> put emperor inside Jerusalem
  6  temple and as-+emperor to-Lord thanks Lord-<suffix_of_divine_name>
  7  each,_every the_whole_wide_world world* and exist somebody to grab holy-cross
  8  tree and [...] cross tree
  9  and cross tree two-from-from through law on-each,_every

## 186v — the holy Cross against the evil

> the wide world; because this holy tree of the Cross, this cross, of a man's […] and of a man's […]; and this holy tree of the Cross, this, of a man's […] against […]; and believe: the evil, the evil one, the Lord God, that is, against the evil one, the evil. On the Sunday the Lord God created from the world and

  1  the_whole_wide_world world because this holy-cross tree this cross <subject_marker> <preposition_of_genitive>-somebody
  2  [...] and <preposition_of_genitive>-somebody [...] and this holy-cross tree this
  3  <subject_marker> <preposition_of_genitive>-somebody [...] against [...] and believe
  4  evil ~evil Lord-<suffix_of_divine_name> that_is against ~evil evil
  5  inside Sunday
  6  create Lord-<suffix_of_divine_name>
  7  from world
  8  and

## 187r — the Red Sea

> the angel, in the eternal land; thus the Lord God, on the Sunday, led them through, through […] the Red Sea, by Moses and by Aaron, the Jewish people, from the land of Egypt, from Pharaoh king's earth; and then Moses and Aaron went to the Red Sea; and then God's angel: Moses, hold out this rod over the Red Sea; and then he held it out over the Red Sea; and then | the Red Sea, in the Lord's name, left apart in two ways; and then the people went through, said Moses, Aaron, the angel, through the Red Sea.

  1  angel inside eternal* land on-that_is Lord-<suffix_of_divine_name> inside Sunday
  2  through go-Lord through dry* the_Red_Sea on-+Moses
  3  and on-Aaron Jew(ish) people on-Egypt earth
  4  on-Pharaoh king earth and then-exist Moses
  5  and Aaron to-+the_Red_Sea go and_then
  6  God angel Moses hold_out this stick on-+the_Red_Sea
  7  and then-exist hold_out on-+the_Red_Sea and then-exist | the_Red_Sea
  8  Lord-+name apart leave on-two ways* and then-exist through go people
  9  say Moses Aaron angel through the_Red_Sea

## 187v — Pharaoh in the midst of the sea

> The time Pharaoh the king went into the Red Sea, the king, Pharaoh's army; and then the king went | into the middle of the Red Sea; the time God's angel said: Moses, hold out this rod over the Red Sea; and then he held it out; the time the Red Sea closed in upon Pharaoh the king; and then went Moses and Aaron […]; thus the Lord God, on the Sunday […] from the people, who was the Lord's, going | upon […] the earth; the Lord God took the heavenly manna from the eternal land; and this manna, this, is this day's

  1  time Pharaoh king inside the_Red_Sea go-king
  2  <preposition_of_genitive>-Pharaoh an_army and then-exist go-king | on
  3  half the_Red_Sea time say God angel Moses hold_out
  4  this stick on-+the_Red_Sea and then-exist hold_out time
  5  the_Red_Sea close_in Pharaoh king and then-exist to-go
  6  Moses and Aaron [...] on-that_is Lord-<suffix_of_divine_name>
  7  inside Sunday [...] from people who exist-Lord on-go-Lord | on
  8  [...] earth grab Lord-<suffix_of_divine_name> heavenly manna
  9  from_the_eternal* land and this manna this <subject_marker> exist-today’s

## 188r — the manna and the bread of this day

> the angel; and this is this day's living, the people said | […] the year; and how at table they ate of it, they ate of it, they left off; and then this manna […] a bucket; and he said […] brought […] from the manna, thanks and pleasing he did; in turn […] Christ stayed, that day's […] manna; and then the Lord Jesus, in his thirty- third year, the time the Lord Jesus said, at the last supper, he took within, why in turn, one baked cake, and the Lord Jesus said: and let a man eat this day's bread; and the Lord

  1  angel and this exist-today’s living people-+say | [?]-[?]-+one
  2  year and how? table-+say eat on-+say from eat <subject_marker> leave
  3  and then-exist this manna [...] bucket and
  4  say [...] brought* [...] from manna thanks
  5  and pleasing do,-+say in_turn [...] Christ stay daily,_of_that_day
  6  [...] manna and then-exist Lord-Jézus inside thirty half*
  7  three_days time say Lord-Jézus on-last dinner-to grab
  8  inside why?-in_turn one baked „cake” and
  9  say Lord-Jézus and somebody exist this exist-today’s eat and Lord

## 188v — he that believeth not

> believeth not: every such man is damned […]; and a man who is the Lord's believes; and there is a man who from the altar from the thirty, eats the holy host and drinks; he that believeth not, that man lives. Chapter. Chapter. Amen. On the Sunday from […] Christ came into this world; and before the Lord Christ's coming, nine months and two Sundays; on the Sunday the Lord was announced, to the understanding, by the angel; in | not the Sunday, in the mind, the happy virgin Mary, and | […] […] Joseph; on the Sunday the Lord was

  1  not_believe each,_every somebody be_damned cut_off-[?] and somebody exist Lord
  2  believe and exist somebody from altar(table) exist
  3  from thirty holy-host eat and drink who_believes_not*
  4  somebody exist living chapter-oh chapter-oh amen
  5  to Sunday from [...] Christ on-this world coming*
  6  and before Lord-Christ coming* nine moon and two Sunday inside
  7  Sunday the_Lord exist announce on-understand-chapter angel inside | not
  8  ~Sunday inside exist-exist-chapter happy virgin-Mary and | [...]
  9  [...] Joseph inside Sunday the_Lord exist

## 189r — what was done on the Sundays

> announced, this angel, to the understanding, the angel; and then the Lord | into this world came; and then the Lord, in his thirty-first day, the time, on a Sunday, the Lord Jesus Christ made at the wedding water into wine; on a Sunday the Lord stood up and raised | the Lord Jesus Christ, the daughter of one chief man in Jerusalem; on a Sunday the Lord […] upon Carmel, to the mount, and the Holy Spirit appeared in the shape of a dove; and then this Lord, of the son, he who quieted the spirit, and the Lord took the Holy Spirit; and the Lord went into the field

  1  announce this angel on-understand-chapter angel and then-exist-Lord | on
  2  this world* coming* and then-exist-Lord inside thirty one-+day
  3  time inside Sunday create on-wedding Lord-Jézus-Christ
  4  water wine inside Sunday the_Lord stand_up resurrect | Lord
  5  Jézus-Christ daughter one head inside Jerusalem inside Sunday
  6  the_Lord from-[?]-[?] on-Carmel to-mount and
  7  appear holy-spirit inside ~shape,_form dove and_then
  8  this-Lord <preposition_of_genitive> son he_who spirit calm_down and
  9  Lord grab holy-spirit and Lord go inside field

## 189v — Nain, the blind man, the cleansing of the temple

> to […] the Lord Jesus, that day; on a Sunday the Lord stood up and raised, the Lord Jesus Christ, in the town of Nain, the son of one widow; and before that, he himself | was the Lord; this widow's son the Lord raised; one blind man he gave light; on a Sunday the Lord Jesus Christ […] the town of Jericho; then the Lord went into Jerusalem, and the Lord's apostles; on a Sunday the Lord cast out, in Jerusalem, from one man, hell, the mind; then the Lord, in his thirty-third year, on a Sunday the Lord | broke

  1  to-[?] Lord-Jézus [?]-+day inside Sunday the_Lord
  2  stand_up resurrect Lord-Jézus-Christ inside Nain town son
  3  one virgin-[?] the_Baptist/woman and before that_is he_is* | exist
  4  Lord this virgin-[?] the_Baptist/woman son stand_up resurrect-Lord one
  5  ~blind through light inside Sunday Lord-Jézus-Christ [...]
  6  Jericho town then-chapter and go-Lord inside Jerusalem and
  7  <preposition_of_genitive>-Lord apostle inside Sunday the_Lord cast_out-Lord inside Jerusalem
  8  on-one somebody hell exist-chapter then-exist-Lord
  9  inside thirty half three inside Sunday the_Lord | break

## 190r — the week of the Passion, day by day

> the Lord, five loaves of this day's bread, for five thousand people; then the Lord, in his thirty-third year, from Galilee through the Red Sea to one mount; on a Sunday the Lord went to suffer in Jerusalem; then the Lord, in his thirty- third year, on the Monday the Lord preached many a miracle; in turn on the Tuesday the Lord stood up and raised Lazarus from the tomb; in turn on the Wednesday the Lord — but Judas sold him for thirty pieces of silver; in turn the wounded one made the supper, and they captured the Lord; in turn on the Friday the cross […]; and the evil one was bound; in turn on the Saturday, hell

  1  Lord five baked exist-today’s five-?thousand people
  2  then-exist-Lord inside thirty half three_days from Galilee
  3  through the_Red_Sea to-one to-mount inside Sunday
  4  the_Lord exist go-Lord on-suffer inside Jerusalem then-exist-Lord inside thirty
  5  half three_days inside Monday the_Lord many miracle preach-Lord in_turn
  6  Tuesday the_Lord Lazarus on-burial_chamber stand_up resurrect-Lord in_turn Wednesday
  7  Lord-+but-+<subject_marker> exist Judas sold to-thirty silver
  8  in_turn wound dinner-to do,-Lord and capture-Lord in_turn
  9  Friday cross-[?] and evil bound_up in_turn inside Saturday hell

## 190v — the five appearances, and Emmaus

> the Lord destroyed; on the Sunday the Lord rose from the dead; and to the apostles the Lord appeared. First the Lord appeared in Bethany | to the virgin Mary; secondly the Lord appeared at the tomb to Mary Magdalene; thirdly the Lord appeared on the way […] the people to Jerusalem; fourthly the Lord appeared to two apostles; then the two apostles went, on the Sunday, out of Jerusalem, into one […]; and the name of that […] was Emmaus; in turn the apostles | and the names of that day were Luke and Cleopas; and there was […] one apostle; this day's bread, and nine, and water; the Lord Jesus blessed; on the Sunday the Lord appeared a fifth time, in Jerusalem, to the ten apostles | of

  1  <subject_marker> destroy-Lord inside Sunday the_Lord rise on-die and apostle the_Lord
  2  appear-Lord first the_Lord appear inside Bethany | virgin
  3  Mary in_turn-two the_Lord appear to-burial_chamber Mary Magdalene third
  4  the_Lord appear on-way [?]-[?] people
  5  on-Jerusalem in_turn-two-two the_Lord appear two apostle then two
  6  apostle and go inside Sunday on-Jerusalem inside one in_turn-chapter-in_turn and
  7  [?]-+name in_turn-chapter-in_turn exist Emmaus in_turn apostle | and-exist-chapter
  8  day-+name exist Luke and Cleopas and ~exist-[?] one
  9  apostle exist-today’s and exist-nine and water bless Lord-Jézus
 10  inside Sunday the_Lord five appear inside Jerusalem ten apostle | <preposition_of_genitive>

## 191r — the Ascension, and the two men in white

> the Lord, the gate; and then, after the Lord Christ's execution, in the twelfth year, the time the Lord Jesus appeared, on a Sunday, in Jerusalem, to the Lord's twelve apostles, to the whole wide world, and to Thomas; and then, after the Lord Christ's execution, | in the twentieth […] year, the time the apostles sat at table in Jerusalem, in the Lord's house where the Lord God, the Lord Jesus, made the supper; the time there appeared two, from the execution of the Lord Christ, from town to town | […] the year; and he left, to the Lord's Father, to the eternal town; and there appeared two angels in white clothes, and then the two angels: you, apostles,

  1  Lord gate and then-exist on-execute Lord-Christ six-two-year time
  2  appear Lord-Jézus inside Sunday inside Jerusalem six-six apostle <preposition_of_genitive>-Lord
  3  to-the_whole_wide_world Thomas and then-exist on-execute Lord-Christ | one-ten-+one-ten
  4  [?]-year time sit apostle at_table inside Jerusalem inside Lord house
  5  where Lord-<suffix_of_divine_name> Lord-Jézus dinner do, time appear
  6  two-?from execute Lord-Christ from_town_to_town* | [?]-[?]
  7  year and to-leave to-<preposition_of_genitive>-Lord from-father-<suffix_of_divine_name> from_the_eternal* town-chapter-in_turn
  8  and two appear two angel-angel white clothes
  9  and_then two angel-angel you apostle-oh-<suffix_of_divine_name>-chapter

## 191v — why stand you looking up to heaven?

> which and how? The Lord, joy, see […]; he left, into heaven | the town; this joy is to be, the Lord would […] on the judgment year, to judge whosoever liveth and the dead; this word, from the Lord, the living Lord; and in this world | the Lord went into heaven, in turn […] the Lord, with all thy heart, the Lord God, with all thy heart, pleasing and thanks. This holy gospel begins, written by holy Luke in the second chapter of the writing: the time, because the time the virgin Mary, at the coming of the Lord Jesus | […]

  1  what-+who how? Lord joy see [...] leave-chapter-leave on-heaven | town
  2  exist-to this joy want-Lord [shall_come] on-+judge-year judge whosoever_liveth*
  3  and dead this word <subject_marker> from Lord living-Lord and on-this world* | from-go
  4  Lord on-heaven in_turn-[?] Lord with_all_thy_heart* Lord-<suffix_of_divine_name> with_all_thy_heart* pleasing and thanks
  5  begins this holy-gospel
  6  write holy-Luke
  7  inside two chapter <preposition_of_genitive>-write
  8  time because time
  9  virgin-Mary on-?coming
 10  Lord-Jézus | [?]-[?]

## 192r — Simeon in the temple

> the year; the time the virgin Mary carried, as a wife, in her lap, to the temple the Lord Jesus; because this girl would destroy — truly the Lord, but the girl would out […] the salvation of the Jews; and then the girl went to this temple; the time Simeon went into the temple, by the Holy Spirit, in mercy, and the virgin Mary appeared; and then Simeon, the virgin Mary, Simeon took this son, more than these, this son, Simeon; […] he carried the son within, Simeon, why in turn; and Simeon knelt down before the Lord Jesus, and asked the Lord for mercy; and then Simeon: Lord, dismiss thy servant in peace.

  1  year time carry wife virgin-Mary inside öl who temple
  2  Lord-Jézus because which this-girl destroy righteous(ly) Lord ~a) want-girl
  3  out(ward) [...] from-salvation Jew(ish) and then-exist girl go this temple
  4  time go Simeon inside temple on-holy-spirit have_mercy
  5  and appear virgin-Mary and_then Simeon virgin-Mary
  6  grab-Simeon this son more_than_these* this son Simeon
  7  [...] son carry inside <preposition_of_genitive>-Simeon why?-in_turn and kneel_(down)
  8  Simeon before Lord-Jézus and Lord have_mercy ~ask_(for)
  9  and_then Simeon Lord remit servant <preposition_of_genitive>-Lord peace <subject_marker>

## 192v — mine eyes have seen thy salvation

> Simeon: for which two reasons? Simeon's two eyes have seen salvation | of Simeon; and holy Simeon blessed the Lord Jesus; and Simeon's sin the Lord had mercy on; and the Lord took him in his lap, and the Lord carried him into the temple at Jerusalem; and then into the temple went the Lord, Simeon and Mary; and Simeon raised the Lord Jesus within, Simeon, why in turn; and then Simeon: lo, from the Lamb; and the Lord went upon heaven and earth, upon this world, the Lord Jesus Christ; and from the Lord, the cross; and upon the Lord there is blessing, all the wide world; and blessing there is; he left. Chapter.

  1  Simeon who-two-why? see two <preposition_of_genitive>-Simeon eye-eye be_saved | <preposition_of_genitive>
  2  Simeon and bless Lord-Jézus holy-Simeon and sin
  3  Simeon have_mercy-Lord and Lord grab inside öl
  4  and Lord carry inside Jerusalem temple and then-exist inside temple
  5  go-Lord-Simeon-Mary and raise Simeon Lord-Jézus
  6  inside <preposition_of_genitive>-Simeon why?-in_turn and_then Simeon ~lo from
  7  lamb and the_Lord go-Lord on-heaven land
  8  on-this world* Lord-Jézus-Christ and from Lord cross-[?] and on-Lord exist
  9  bless each,_every ~the_whole_wide_world world* and bless exist leave chapter-oh

## 193r — Simeon carries the news to the fathers in hell

> Chapter. Amen. Here ends this holy gospel. The Lord God's love. This, out of high Moses, truly, in one chapter, he who is written, written: holy Simeon, three days from going out of this world, said: Christ, the apostles of the Lord, announce; Simeon, in the netherworld, to the holy fathers, | at the coming of the Lord: and see, you are saved, and many in judgment who are in the netherworld, from the holy fathers and the holy prophets. Written; and from the holy gospel, that is […] the Lord, this Lord, the holy gospel: this Lord, the nine, upon the water created; this Lord gave light to the blind; this Lord cast the evil out of the people; this Lord the dead raised and resurrected; and this and that; the leper the Lord healed; this Lord, the cross, the holy gospel.

  1  chapter-oh amen end this holy-gospel Lord-<suffix_of_divine_name> <subject_marker> love this <end_of_line_mark>
  2  out(ward) high-Moses righteous(ly) inside one chapter he_who* exist write write <end_of_line_mark>
  3  holy-Simeon three_days on-this world from-go-Simeon say Christ apostle <end_of_line_mark>
  4  <preposition_of_genitive>-Lord announce <subject_marker> Simeon inside netherworld holy-from-father | on-+<end_of_line_mark>
  5  coming* <preposition_of_genitive>-Lord and see be_saved you and many <end_of_line_mark>
  6  judge-+<subject_marker> exist inside netherworld from father-holy and prophet-holy. <end_of_line_mark>
  7  write and from holy-gospel that_is [...] Lord this-Lord holy-gospel <end_of_line_mark>
  8  this-Lord exist-nine on-water create this-Lord blind through light <end_of_line_mark>
  9  this-Lord evil on-people exorcise this-Lord dead <end_of_line_mark>
 10  rise* ~resurrect who-and-this-and leper from-healing-Lord this-Lord cross holy-gospel

## 193v — the call of Matthew at the receipt of custom

> This holy gospel begins, written by holy Matthew, in the […] chapter of the writing: the time, then, the Lord Jesus, in his thirtieth year, the time he preached in | there was […] and then the Lord Jesus preached in Capharnaum, and left off, down, from preaching; and many people made ready to him; and then the Lord went into the town, and saw, the Lord Jesus, holy Matthew sitting at the receipt of custom; and then the Lord Jesus

  1  begins this holy-gospel
  2  write holy-Matthew inside and
  3  chapter <preposition_of_genitive>-write time
  4  then-exist Lord-Jézus inside
  5  thirty years* time
  6  preach inside | ~exist
  7  [...] and then-exist from-preach Lord-Jézus inside Capharnaum
  8  and leave to-down on-preach and prepare to-Lord
  9  many people and then-exist go-Lord on-town and see
 10  Lord-Jézus on-tax_collector sit holy-Matthew and_then Lord-Jézus

## 194r — he sat at meat in the house

> Matthew went to the Lord, to the food, to the place; holy Matthew rose, and Matthew went to the Lord Jesus; and the Lord went with Matthew to holy Matthew's house, and he made, out of many, out of […] — how? Holy Luke speaks: he made, out of many, out of […] […] and there went to the Lord the Jews, the Pharisees, and the tax collectors, the chief men; and together with the Lord Jesus they drank and ate, the sinners; and the Jews began, the Pharisees, to speak to the Lord's apostles: this, you answered, the salvation of sinners? In turn, then, this Lord is

  1  Matthew go to-Lord on-food to-place rise holy-~Matthew and
  2  go-Matthew to-Lord-Jézus and go-Lord-Matthew holy-~Matthew house
  3  and do, from-many-to from-+out [...] how?
  4  speak holy-Luke do, from-many-to from-+out.
  5  [...] and go to-Lord Jew(ish) pharisee and
  6  tax_collector exist head and together Lord-Jézus drink
  7  and eat sinners* and begin Jew(ish).
  8  pharisee speak apostle <preposition_of_genitive>-Lord this you answered
  9  sinners* from-salvation in_turn then-exist this-Lord exist

## 194v — they that are well need not a physician

> and the Lord said: this Lord is sin, therefore the Lord's salvation; and the blind to the Lord Jesus […] humble; and then the Lord Jesus […] to the Lord: this Lord went not to the righteous man in this world, but to the sinner; and then the Lord Jesus: you, righteous man; and then the Lord Jesus: the healthy man needs no recovery, but rather he needs one sin — this is recovery. Here ends this holy gospel, written by holy Matthew in the […] chapter. Holy Paul speaks and says: | the Lord Jesus Christ, from the beginning of the world, from the creating of Adam, | to […] the coming of the Lord Jesus Christ into this world […]

  1  and Lord say this-Lord exist sin therefore* from-salvation-Lord and
  2  blind-to Lord-Jézus [...] humble and_then Lord-Jézus [...]
  3  to-Lord this-Lord go-Lord to-righteous_man on-this world* a) to-sin
  4  and_then Lord-Jézus you righteous_man and_then
  5  Lord-Jézus need healing-somebody recovery but_rather need.
  6  one-sin ~exist-this recovery end this holy-gospel
  7  write holy-Matthew inside and chapter holy-Paul speak say | Lord
  8  Jézus-Christ from* ~begin-to world* from* ~Adam create | to
  9  [...] coming* Lord-Jézus-Christ on-this world [...]

## 195r — from Adam to the coming of Christ

> truly, the man; and one prophet, and one forefather, and one holy father, holy living; and one | […] the father […] in the eternal land; but rather, then, at the coming of Christ into this world, and then, in his thirtieth day, the time […] the Lord Jesus upon Carmel, the mount; and then out, in his thirty-third year, the time he was crucified, and on the third day stood up from the dead; and many holy prophets and holy forefathers and holy fathers, holy living, out of the netherworld | to the Lord went; and then, that day, the time he left

  1  righteous(ly) somebody and one prophet and one forefather
  2  and one holy-father holy-living and one | [...]
  3  father-[?]-[?]-[?] inside eternal* land
  4  but_rather-+one then coming* Christ on-this world* and then-exist inside
  5  thirty day time from-[?]-[?] Lord-Jézus on-Carmel
  6  mount and then-exist out(ward) thirty ~begin-+three_days time
  7  crucified and on_the_third_day from die stand_up and many holy-prophet
  8  and holy-forefather and holy-father holy-living on-netherworld out(ward) | to
  9  go-Lord and then-exist [?]-+day time to-leave

## 195v — he shall come to judge the quick and the dead

> to the Lord's Father, upon heaven and earth; | the Lord sits at the Father's right hand, at the food; the Lord shall go to judge the living and the dead; and before going away he blessed all the wide world. This holy gospel begins, written by holy Matthew | […] the twenty-second chapter of the writing: the time, then, | the Lord Jesus, in his thirty-third year, the time the Lord Jesus said to the apostles; they answered: who shall be to the Lord, this Lord, the greatest in the eternal

  1  to-<preposition_of_genitive>-Lord from-father-<suffix_of_divine_name> on-heaven land | from-sit
  2  Lord from-father-<suffix_of_divine_name> on-right_side from-food have-Lord go-Lord judge
  3  living-somebody and die-somebody and before go_away bless each,_every the_whole_wide_world
  4  world begins this holy-gospel.
  5  write holy-Matthew | [...]
  6  two-two chapter <preposition_of_genitive>-write.
  7  time then-exist | Lord
  8  Jézus thirty ~begin-+three time say apostle Lord-Jézus.
  9  answered who? exist to-Lord this-Lord on-many inside eternal*

## 196r — except you become as little children

> land? Because this is the apostles' — he himself, the Lord, was crucified and on the third day stood up from the dead; and the Lord to these apostles, to judge who shall be to the Lord, this Lord, greatest in the eternal land; and the Lord Jesus took among them one little son, and the son the Lord Jesus set upon the head, of the Lord, why in turn; and then the Lord Jesus: whosoever therefore is humble | as this little son, that one therefore is saved. The time the Jews brought one | before | the Lord Jesus, from this emperor, to whom, and he was a pagan.

  1  land because ~exist-this apostle he_is* Lord crucified and
  2  on_the_third_day from die stand_up and Lord to-this apostle judge
  3  who exist to-Lord this-Lord on-many inside eternal* land
  4  and among Lord-Jézus one little son.
  5  and son <subject_marker> put_on Lord-Jézus on-head.
  6  <preposition_of_genitive>-Lord why?-in_turn and_then Lord-Jézus who-?therefore this humble | how?
  7  <subject_marker> this little son one therefore* be_saved
  8  time carry Jew(ish) one | before | Lord
  9  Jézus from* this emperor to-+who-to and exist pagan.

## 196v — the keys, and whatsoever thou shalt bind

> Because he heard from every man, upon one | before; this was: the Lord Jesus took the key of salvation, holy Peter; said | the Lord Jesus: whom this Peter […] in this world, from a man there is […] and from the eternal land; in turn whom this one […] in this world, from a man there is […] and from the eternal land. And then the Lord Jesus: he who among many, the Lord, you, from the Lord — every one a servant; and then the Lord Jesus: whosoever therefore this apostle, from this little son, does

  1  because hear from each,_every somebody on-one | before this exist
  2  grab Lord-Jézus key be_saved holy-Peter say | Lord
  3  Jézus who(m) this-Peter loose* on-this world from
  4  somebody exist loose* and from_the_eternal* land
  5  in_turn who(m) this-?with loose* on-this world from
  6  somebody exist loose* and from_the_eternal* land
  7  and_then Lord-Jézus he_who on-many Lord you from
  8  the_Lord each,_every servant and_then Lord-Jézus who-?therefore this
  9  apostle this from little son to* do,

## 197r — their angels always see the face of my Father

> in the Lord's name, that one therefore is saved; and then the Lord Jesus taught the Lord's, therefore, apostles; and one […] […] did; and then the Lord Jesus to the apostles of the Lord: happy are the people, and the angels see the face of the Lord's Father; it is the will, from the people; and the angels look upon the face of the Lord's Father. Here ends this holy gospel. This holy gospel begins, written by holy Matthew: the time | the Lord Jesus said to the Lord's apostles, and to the Jewish

  1  inside <preposition_of_genitive>-Lord [?]-+name and one therefore* be_saved
  2  and_then Lord-Jézus learn <preposition_of_genitive>-Lord therefore* apostle and one
  3  [...] [...] do, and_then Lord-Jézus apostle
  4  <preposition_of_genitive>-Lord happy from people and angel see face
  5  <preposition_of_genitive>-Lord from-father-<suffix_of_divine_name> will from-people and angel on-see.
  6  face <preposition_of_genitive>-Lord from-father-<suffix_of_divine_name> end this holy-gospel
  7  begins this holy-gospel write
  8  holy-Matthew time say | Lord
  9  Jézus apostle <preposition_of_genitive>-Lord and Jew(ish)

## 197v — take up his cross and follow me

> people; and the apostles, the man, the Jews: whosoever would come after the Lord, let him | deny himself, and all that is his, and take his own cross upon his own shoulder, and let the man go after the Lord; and then the Lord Jesus: who is this man […] and this world | rich […] then this man took his own soul | to riches […] and then the Lord Jesus: good is it that this man release | of the man's soul; damned, but saved, because many a man; and the man is […] […] […] saved, every man damned […] […] the man is, from the judgment, said,

  1  people and apostle-somebody-Jew(ish) want what Lord go | deny
  2  somebody <preposition_of_genitive>-somebody the_whole_wide_world and grab <preposition_of_genitive>-somebody
  3  ~cross on-<preposition_of_genitive>-somebody shoulder and go-somebody what
  4  Lord and_then Lord-Jézus who this somebody [profit] and this world | rich
  5  [...] then this somebody <subject_marker> grab <preposition_of_genitive>-somebody soul | to-rich
  6  [...] and_then Lord-Jézus good <subject_marker> this somebody release* | <preposition_of_genitive>
  7  somebody soul be_damned ~a) be_saved because many somebody
  8  and somebody exist [...] [...] [...] be_saved-somebody each,_every
  9  somebody be_damned [...] [...] somebody exist from-judge say

## 198r — go into all the world

> to damnation; every man saved. And then the Lord Jesus: you, therefore, go from town to town, this believing; who this Lord, you, preach the Lord, every one, from town to town, this […] and see, go into this world, from prayer, the Son of God, in the mind of man, on the judgment year, every one, from town to town, this […] believe; and then the Lord Jesus […] Peter, one among you; and the apostles | see, the apostles, from prayer, the Son of God, within […] the man, and the apostles are within; the apostles believe. Here ends this holy gospel.

  1  on-be_damned each,_every somebody be_saved and_then Lord-Jézus you
  2  therefore-+say each,_every from_town_to_town* this-believe-+say who
  3  this-Lord you preach-Lord each,_every from_town_to_town*
  4  this [...] see-+say go on-this world from pray
  5  son God inside exist-exist-chapter somebody on-judge-year each,_every from_town_to_town*
  6  this-[?] believe and_then Lord-Jézus [...]
  7  Peter one among you and apostle | see
  8  apostle from pray son God inside ~exist-[?] somebody
  9  and apostle exist inside son believe-apostle end
 10  this holy-gospel

## 198v — write your names in the eternal land

> Said the Lord God to the angel | of the Lord, holy […] the prophet, and | holy Elijah the prophet […] | said the apostles, the man, to the Lord, this Lord: thou creature, Lord, have mercy on sin […] this is in the commandment, the man, that is; and the man who bears the commandment of God […] the sinful man is saved, to many | not, not, not. Chapter. Chapter. Amen. Written are the names of men in the eternal land, in the house; he dies, in turn | upon death, the mind and the soul. Chapter. Chapter. Amen.

  1  say <subject_marker> Lord-<suffix_of_divine_name> on-angel | <preposition_of_genitive>
  2  Lord holy-<name_of_a_prophet> prophet and | holy
  3  Elijah prophet [...] | say
  4  apostle-somebody to-Lord this-Lord.
  5  you creature* Lord sin have_mercy [...] this exist
  6  inside commandment somebody that_is and have somebody ~carry commandment
  7  God [...] sin somebody be_saved to-many | not-not
  8  not chapter-oh chapter-oh amen write <subject_marker> name
  9  <preposition_of_genitive>-somebody inside eternal* land to-house die in_turn | on
 10  die exist-exist-chapter and soul chapter-oh chapter-oh amen

## 199r — a man had a vineyard and two sons

> This holy gospel begins, written by holy Matthew | in the twentieth, in the fifth chapter of the writing: the time, then, the Lord Jesus, in his thirty-third year, the time the Lord Jesus preached in Jerusalem; and the Lord Jesus said to the apostles of the Lord, and to the Jewish people: the kingdom of heaven left a man and earth; and then the Lord Jesus: there was […] one rich man, a vineyard; and then he had

  1  begins this holy-gospel
  2  write holy-Matthew | one
  3  ten-+one-ten inside five chapter
  4  <preposition_of_genitive>-write time
  5  then-exist Lord-Jézus inside
  6  thirty ~begin-+three_days
  7  time preach Lord-Jézus inside Jerusalem and say Lord-Jézus apostle
  8  <preposition_of_genitive>-Lord and Jew(ish) people leave king somebody heaven
  9  land and_then Lord-Jézus exist [...]
 10  one rich-somebody vineyard and then-exist have

## 199v — go work today in my vineyard

> two sons, to the pagan and the Jew; and then this rich man | of the Lord, the man, the son, said […] he brought the son into | the Lord's man's vineyard, the farm; he said, brought the son to this, go, and then this rich man […] the second, to the son, […] the man, into the rich man's vineyard, the farm; and then he said, said the priest, and […] […] the man; and said the Lord Jesus to the chief men of the Jews and to the Lord's apostles: judge, Lord, this Lord, you: which of these did good? Say. Said the chief men of the Jews: which did good? He who

  1  two son to-+pagan Jew(ish) and_then this rich-somebody | <preposition_of_genitive>
  2  Lord-somebody son on-+say [...] brought-son inside | <preposition_of_genitive>-Lord-from
  3  man vineyard farm say brought-son to-this ~go-+say
  4  and_then this rich-somebody [?]-[?] two to-~son
  5  [?]-somebody inside <preposition_of_genitive>-Lord-somebody vineyard farm and_then-say-say
  6  priest* and [?]-[?] [?]-somebody and say
  7  Lord-Jézus head Jew(ish) and apostle <preposition_of_genitive>-Lord judge-Lord
  8  this-Lord you who? <subject_marker>-this good say.
  9  say head Jew(ish) who? <subject_marker> good say he_who

## 200r — he let out the vineyard to husbandmen

> said, to the pagan, the priest; and whosoever would be named, in turn went to the pagan; and then the Lord Jesus spoke truly; and secondly the Lord Jesus said a parable, and said: there was one rich lord who let out on lease the Lord's vineyard to husbandmen, the farm, the Lord's vineyard; and then the vineyard, many years he bore it, to take, to remit the vineyard's lease; and then this rich lord | of the Lord's servants, prophets and angels, the prophets and angels went, this lease from them to ask, the prophets and angels; and | the prophets and angels, the lease they would not take from them, but rather

  1  say-to-+pagan priest* and name-+who-want in_turn go-to-+pagan
  2  and_then Lord-Jézus righteous(ly)-+say speak and two say Lord-Jézus
  3  parable say exist grab one rich-Lord on-lease
  4  <preposition_of_genitive>-Lord vineyard_worker farm <preposition_of_genitive>-Lord vineyard and then-exist
  5  vineyard-+say many year carry-+say to-+say grab remit
  6  vineyard lease and_then this rich-Lord | <preposition_of_genitive>
  7  Lord servant prophet and angel go-prophet-angel this lease
  8  from* say ask_(for)-prophet-angel and | prophet
  9  angel lease to-+say grab-+say but_rather

## 200v — last of all he sent his son

> they all died; and the Lord's son went; this rich lord said to this son: they will have, they would say, the lease the Lord will take; and then the Lord was; they saw, and went; and the son they said; and then, thus: the son from […] the vineyard […] the son […]; and this son is the vineyard's heir; and then they carried him off to die, they said; and […] to the Lord; and the son died, they said; and then it was, from town to town […] and the Jews, the chief men: how? he said; spoke the Lord Jesus; and thirdly the Lord Jesus said a parable,

  1  each,_every die and go-Lord <preposition_of_genitive>-Lord son this rich-Lord say this son
  2  exist-+say have would_say* lease Lord grab
  3  and then-exist-Lord exist-+say see and go and son.
  4  say* and_then-+say this_is son from [...]
  5  <subject_marker> vineyard [?]-~son [...] and this
  6  son exist vineyard carry and_then-+say go-die
  7  say and sent_saying* to-Lord and son die-+say and
  8  then-exist exist from_town_to_town* [...] and Jew(ish) ~head
  9  how? he_said* speak Lord-Jézus and three say Lord-Jézus parable

## 201r — the marriage of the king's son

> and said: there was one king in a land, and then he had one son; and the king would make a wedding; and then, among this king's, all the Lord king's, in turn […] to this wedding; and | then, therefore, not one went to this wedding; this king grew angry; and then, thus, the people; and he spoke, the people of the Lord, out, in turn, the whole wide world, to the supper; and then the Lord Jesus: what did this king? He said to the Lord's servants: all, from the town, destroy with fire and with water; and then this king

  1  say exist one king inside land and then-exist
  2  have one son and son want king
  3  wedding as* and then-exist among this king
  4  each,_every <preposition_of_genitive>-Lord king in_turn-[?] on-this wedding and | then
  5  therefore* one go on-this wedding get_angry this
  6  king and_then that_is people and speak people
  7  <preposition_of_genitive>-Lord out in_turn the_whole_wide_world dinner-to and_then Lord-Jézus who do,
  8  this king say <preposition_of_genitive>-Lord servant each,_every from town.
  9  destroy fire and* water and_then this king

## 201v — go out into the highways

> said to the Lord's servants: go, and speak this word, to the understanding, to the hidden; leave them behind, and let them be among those at this wedding; and then this Lord king's servants went, to the blind, to the hidden, and the way, and to the town; and they found the blind of God […] blind, and even more […] and the hungry and the thirsty, and […] the blind of God, and […] […] the servants found; all the servants went, […] into the Lord king's house; and then, out of the house, this king, the various heaven

  1  <preposition_of_genitive>-Lord servant go and this word speak-understand-hide_oneself exist
  2  leave-to-leave and exist among on-this wedding and_then
  3  this Lord-king <preposition_of_genitive>-Lord servant go-?blind-hide_oneself and
  4  way and on-town and find
  5  God blind ninety-~exist blind and even_more-[?]-to and
  6  be_hungry and thirst and [feeble] God blind and
  7  [...] [...] find servant each,_every go-servant
  8  [...] inside <preposition_of_genitive>-Lord-king house and then-exist out
  9  house this king various heaven

## 202r — the man without a wedding garment

> Lord; and this king said, this king; and the king went into the Lord king's house; the king would go before, out of the Lord king's house; and then this king went into the Lord king's house; and this king saw one man of God in ragged clothes; and thus the king said: this friend […] which man […] the man went […] the man, friend, the wedding clothes, by name, which this man

  1  Lord and say this king this-king and go-king inside
  2  <preposition_of_genitive>-Lord-king house want-king to-before on-+out
  3  <preposition_of_genitive>-Lord-king house and then-exist ~go this king
  4  inside <preposition_of_genitive>-Lord-king house and see this king
  5  one God-somebody ragged clothes and
  6  say that_is king this friend [...] who somebody
  7  [...] go-somebody [...] somebody friend
  8  wedding clothes to-+name who this somebody

## 202v — bind him hand and foot

> said, in the Lord God's house of heaven, that day; good, said this king, Gabriel, friend, brother by name, this most high […] the will; Gabriel spoke and said: bind the man's hands and feet, and cast the man out, the angel, outside […] […] there is; see, the grinding of teeth, weeping. Chapter. Chapter. Here ends this holy gospel. The Lord God, with all thy heart. This holy gospel begins, written by holy Matthew, […] chapter | of the writing: the time, then, | the Lord Jesus, in his thirty-third year, the time

  1  say inside <preposition_of_genitive>-Lord-<suffix_of_divine_name> heaven house [?]-+day good say this king
  2  Gabriel friend brother-+name this-high [...] will
  3  speak-+Gabriel say tie_(up) somebody hand and.
  4  foot and somebody throw_out angel on-out(ward) [outer_darkness]
  5  [?]-~exist exist see grinding tooth crying chapter-oh
  6  chapter-oh end this holy-gospel Lord-<suffix_of_divine_name> with_all_thy_heart*
  7  begins this holy-gospel write.
  8  holy-Matthew [...] chapter | <preposition_of_genitive>.
  9  write time then-exist | Lord
 10  Jézus thirty ~begin-+three_days time

## 203r — is it lawful to give tribute to Caesar?

> The Lord Jesus preached in Jerusalem, and the Jews came to him, | to the Lord Jesus; and then they said, they answered […] […] truly the man; and truly the Lord is a prophet, because truly in God's way the Lord goes; and the Lord has the king and the emperor […] go; the Lord's name, to the apostles; how teachest thou? | Would the Lord take from what they would do? | […] He said: take from every man one drachma, the emperor, to the pagan; and they said: how teachest thou? Would the Lord take from what they would do? Said

  1  preach Lord-Jézus inside Jerusalem and to-leave Jew(ish) | to-Lord
  2  Jézus and_then say answered-+say [...] [...] righteous(ly)
  3  somebody and righteous(ly)-Lord prophet because righteous(ly) God way
  4  go-Lord and Lord ~have king and emperor
  5  [...] go name-Lord on-apostle how? learn-+say-learn | want
  6  Lord grab from would_say* do, | [?]-[?]
  7  say grab from each,_every somebody on-one drachma.
  8  emperor to-of_an_alien_nation,_pagan and say-+say how? learn-+say-learn
  9  want-Lord grab from would_say* do, say

## 203v — whose image and superscription?

> the Lord Jesus: bring the Lord the tax; and they brought it before the Lord Jesus; and then the Lord Jesus: whose is this image? Said the Jews: this is the inscription, the image. And then the Lord Jesus: whose is this writing? Said the Jews: this is the inscription, the writing. And then | the Lord Jesus: this is the inscription, the image; and the inscription, the writing; this inscription, from town to town, leave it. And then | the Lord Jesus: the brethren […] owe the inscription […] to the emperor, take it; in turn | love, they said, the apostles;

  1  Lord-Jézus carry-+say Lord tax and carry-+say
  2  before Lord-Jézus and_then Lord-Jézus Whose?-+<subject_marker> this
  3  shape,_form say Jew(ish) this_is inscription* shape,_form
  4  and_then Lord-Jézus Whose?-+<subject_marker> this write say
  5  Jew(ish) this_is inscription* write and_then | Lord
  6  Jézus this_is inscription* shape,_form and inscription*
  7  write this inscription* from_town_to_town* leave and_then | Lord
  8  Jézus brethren-[?] indebted inscription* [...]
  9  emperor grab-[?] in_turn | love-+say-apostle

## 204r — render to God the things that are God's

> the man owes God; this, God, take it. And then the Lord Jesus: he that believeth not […] the inscription, and God; and a man, from what he owes, as therefore he takes, likewise he owes. Here ends this holy gospel. Said the Lord Jesus: there is humble, the chief, the inscription, this world; and take it, the inscription, which he said; and he owes it, because this from the inscription, you […]

  1  somebody indebted God this God grab-[?]
  2  and_then Lord-Jézus exist not_believe-[?]
  3  inscription* and God and somebody from indebted as* therefore*
  4  grab-[?] likewise* indebted-[?]
  5  end this holy-gospel say Lord-Jézus exist-[?]
  6  humble head [?]-?inscription-[?] this world* and
  7  grab-[?] [?]-?inscription-[?] who
  8  say-[?] and indebted-[?] because this
  9  from [?]-?inscription-[?] you [...]

## 204v — what a man owes the Church

> from the heavenly faith, baptized, a man remits; the alien nation, out; believe, baptized, a man; and | the apostles, the man; and the emperor, the king | humble, they said, the apostles; the man; and he owes the Church, this man, […] in turn, upon, to many churches; and of […] the Lord, the earth; in turn, before, secondly they said, he owes the Church, this man, upon […] before the man's spirit, from the Father; and the Father, this man, the way he makes before the Lord | the Father

  1  from heavenly* believe [?]-[?]-+baptize somebody remit of_an_alien_nation,_pagan
  2  out(ward) believe [?]-[?]-+baptize somebody and | [?]-apostle
  3  somebody and [?]-+emperor-king | humble-+say-apostle.
  4  somebody and indebted-[?] church this somebody
  5  [...] in_turn on on-many church and
  6  <preposition_of_genitive>-[?] Lord earth in_turn before two
  7  say-[?] indebted church this somebody on
  8  [...] before <preposition_of_genitive>-somebody spirit from-father and father this
  9  somebody way do, before <preposition_of_genitive>-Lord | from-father

## 205r — fasting, the ten commandments, and thanks

> God; thirdly, they said, he owes, take | of the man's fast, and the man's prayer, and the ten commandments of the Lord's Father God; and he owes to kneel down before the Lord's Father God […] and the man owes the Lord prayer, at home, in humility, the Lord's pleasing and thanks afterward; and to the Lord all heaven and earth; and a man takes the chief, the Lord, from the emperor, the king, the world, he who owes; the man who believeth not, every Lord and every emperor and every king, every believer

  1  <suffix_of_divine_name> third say-[?] indebted grab | <preposition_of_genitive>
  2  somebody-fast and <preposition_of_genitive>-somebody as* and ten commandment
  3  <preposition_of_genitive>-Lord from-father-<suffix_of_divine_name> and indebted-[?] kneel_(down)
  4  before <preposition_of_genitive>-Lord from-father-<suffix_of_divine_name> [...] and
  5  indebted-somebody Lord as* home-+humble Lord pleasing
  6  and thanks afterward* and to-Lord each,_every heaven land
  7  and somebody grab head Lord from emperor king
  8  world he_who* indebted somebody exist not_believe-somebody
  9  each,_every Lord and each,_every emperor and each,_every king each,_every believe

## 205v — Jericho

> baptized, the man […] of the Lord's Father God. Here ends this holy gospel, and to the apostles the holy gospel. The Lord God, with all thy heart. This holy gospel begins, written by holy Luke, in the ninth […] chapter of the writing: the time, then, the Lord Jesus, thirty, in one day; the time | the Lord Jesus went into another town; and this town's name was Jericho; and then

  1  [?]-[?]-+baptize somebody [...] <preposition_of_genitive>-Lord from-father-<suffix_of_divine_name>
  2  end this holy-gospel and on-apostle holy-gospel Lord-<suffix_of_divine_name> with_all_thy_heart*
  3  begins this holy-gospel
  4  write holy-Luke inside
  5  nine end_of_numeral* chapter <preposition_of_genitive>-write
  6  time then-exist
  7  Lord-Jézus thirty inside one
  8  day time go | Lord
  9  Jézus inside one another town and this town
 10  name exist Jericho and then-exist

## 206r — Zacchaeus climbs the tree

> the Lord Jesus kept going, the town of Jericho; and then in Jericho there was one chief tax collector, and the man's name was Zacchaeus; and then he was seen, the Lord Jesus going into Jericho; and Zacchaeus could not see the Lord Jesus, but from […] Zacchaeus, this many people; and he climbed up one tree, because […] Zacchaeus […] the Lord Jesus went; and then the Lord Jesus came to this tree, and the Lord Jesus saw

  1  keep_going Lord-Jézus Jericho town and then-exist inside
  2  Jericho one tax_collector head and.
  3  [?]-+name somebody exist Zacchaeus
  4  and then-exist Lord see-+say go Lord-Jézus inside Jericho
  5  and Lord can see Zacchaeus Lord-Jézus
  6  a) from [...] Zacchaeus this many people
  7  and go_up one creatures* because [...]
  8  Zacchaeus [?]-go Lord-Jézus and then-exist
  9  go Lord-Jézus to-this creatures* and see Lord-Jézus

## 206v — make haste and come down

> Zacchaeus sitting upon this tree; and then the Lord Jesus: Zacchaeus, come down, for this Lord must be today in Zacchaeus's house, that day, the Lord; and with joy he left, Zacchaeus; and he came down, this Zacchaeus; and the Lord and the apostles, Jesus, went into Zacchaeus's house; and | from the name of the Lord Jesus, that day, the Lord sat; and they began to murmur against the Lord Jesus, the chief men of the Jews, saying:

  1  Zacchaeus sit on-this creatures*
  2  and_then Lord-Jézus Zacchaeus go to-down
  3  this-Lord today exist-Lord inside <preposition_of_genitive>-Zacchaeus
  4  house [?]-+day-Lord and joy leave-chapter-leave.
  5  Zacchaeus and go down this.
  6  Zacchaeus and go-Lord-apostle-Jézus inside
  7  Zacchaeus [?]-+who-to house and | from
  8  name Lord-Jézus [?]-+out-+day sit-Lord and begin-+say
  9  murmur on-Lord-Jézus Jew(ish) head this-Lord say

## 207r — the half of my goods I give to the poor

> the Son of God, in turn, with one sinner, from one […] one extortioner; and he left afar | the name of Jerusalem, Zacchaeus; and then Zacchaeus: Master, this Zacchaeus takes the half, the half truly, of Zacchaeus's riches, to God, the spiritually blind, truly the half; in turn he left afar one among you, in turn, Jerusalem […] | take, Jerusalem, one denarius; upon the extortion, Jerusalem would, the man, to every one, two by two, take; and the Lord Jesus saw that he himself was

  1  son God in_turn one sin from-one
  2  extorter* one extort and leave far | name-Jerusalem
  3  Zacchaeus and_then Zacchaeus
  4  Master this-Zacchaeus half grab
  5  half-righteous(ly) <preposition_of_genitive>-Zacchaeus ~rich God
  6  spiritually blind righteous(ly)-half in_turn leave far one
  7  among you in_turn-chapter-Jerusalem [...] | grab
  8  chapter-Jerusalem one denarius on-extort want-chapter-Jerusalem somebody
  9  to-each,_every two-two grab and see Lord-Jézus he_is*

## 207v — this day is salvation come to this house

> truly a son of father Abraham; and then the Lord Jesus: | Zacchaeus, Zacchaeus, have it, because this day, in Zacchaeus's house is salvation, Zacchaeus's; because the Lord, this Lord, truly the Son of the living God; and then the Lord Jesus to the chief men of the Jews: take the commandment; Zacchaeus, therefore, the Lord to this, this Lord went into this world, who is, this Lord, sin […] […] | but the Lord, this Lord went, who is, this Lord, sin; the Lord loves; and the Lord, the sinful man; and […] of the Lord, the sinful man is saved, and the Lord is pleased; and the sinful man gives thanks. Here ends this holy gospel. The Lord God,

  1  righteous(ly) son father Abraham and_then Lord-Jézus | Zacchaeus
  2  Zacchaeus have because this-[?]-+name today inside <preposition_of_genitive>-+Zacchaeus
  3  house be_saved <preposition_of_genitive>-+Zacchaeus because Lord this-Lord
  4  righteous(ly) son living God and_then Lord-Jézus Jew(ish) head
  5  grab-+say commandment Zacchaeus therefore-Lord to-this this-Lord
  6  go-Lord on-this world* who-exist this-Lord sin [...] [...] | a)
  7  Lord this-Lord go-Lord who-exist this-Lord sin love-Lord and Lord sin
  8  man* and [...] <preposition_of_genitive>-Lord be_saved sin-somebody exist
  9  and Lord pleasing and thanks grab sin-somebody end this holy-gospel Lord-<suffix_of_divine_name>

## 208r — what Zacchaeus signifies

> with all thy heart. This Zacchaeus is every chief among sinners, and every tax collector, and every man who takes from the sinner, in mercy, the Lord God; and every sinful man, and the sinner in love, the Lord God; and every sinful man truly, and the sinner in truth, the Lord God, that is; and the sinner bears the law of God — this is truly the law of the Lord God; and this Zacchaeus is mercy, God, the spiritually blind; and this Zacchaeus loves the Lord God most high, all creation, and every man, as a man his neighbour; and this Zacchaeus is in the truth, the law of the Lord God, that is, | bearing

  1  with_all_thy_heart* this Zacchaeus exist each,_every sin-somebody head
  2  and each,_every tax_collector and each,_every somebody from-grab somebody-sin inside have_mercy.
  3  Lord-<suffix_of_divine_name> and each,_every somebody-sin and somebody-sin inside love Lord-<suffix_of_divine_name> and each,_every
  4  somebody-sin righteous(ly) and somebody-sin inside righteous(ly) Lord-<suffix_of_divine_name> that_is
  5  and somebody-sin carry law God this_is righteous(ly) law Lord-<suffix_of_divine_name>
  6  and this Zacchaeus exist have_mercy God spiritually
  7  blind and this Zacchaeus love Lord-<suffix_of_divine_name> high each,_every create
  8  and each,_every somebody how?-to somebody neighbour* and this.
  9  Zacchaeus exist inside righteous(ly) law Lord-<suffix_of_divine_name> that_is | carry

## 208v — the first three commandments

> the commandment of God, he who is; take it, in the word of the Old Testament, | from father Abraham. The first commandment of God: believe, man, truly, baptized; one God saves a man, to many | not, not, not; the man's is heaven and earth. The second law, take it in the word of the Old Testament, from father Abraham: God's name take not in vain. The third law, take it in the word of the Old Testament, from father Abraham: a man shall, truly, baptized, the holy Sunday and the feast, this holy man, from the mother, the temple; let a man hear the preaching, of […]

  1  <subject_marker>-[?] commandment God he_who* exist grab inside <pertaining_to_the_Old_Testament> word | from
  2  father Abraham first God commandment believe somebody righteous(ly)
  3  [?]-[?]-+baptize one God be_saved somebody to-many | not
  4  not-not <preposition_of_genitive>-somebody <subject_marker> heaven land two law
  5  exist grab inside <pertaining_to_the_Old_Testament> word from-father Abraham God
  6  name in_vain grab three law exist grab
  7  inside <pertaining_to_the_Old_Testament> word from-father Abraham shall somebody
  8  righteous(ly) [?]-[?]-+baptize holy-~Sunday and feast holy-this-somebody from*
  9  mother temple preach hear-somebody <preposition_of_genitive>-[?].

## 209r — from Adam to Abraham to Moses

> heaven and earth; and these three laws the Lord God confirmed to Moses by the Lord's angel; the time, then, from Adam onward until Abraham, one hundred years and […] years; from Abraham out until Moses, three thousand and fifty; from Abraham until Moses, the time the Lord God first confirmed to Moses by the Lord's angel; and God's angel said: Moses, because of this, teach, Moses, this people the three laws of the Lord; because of this let the people believe in one

  1  heaven land and this three law confirm Lord-<suffix_of_divine_name> Moses
  2  on-angel <preposition_of_genitive>-Lord time then-exist from ~Adam onward.*
  3  until Abraham one hundred-year and [?]-year from
  4  Abraham <subject_marker> ~out(ward) until Moses ~begin-+three_thousand
  5  and fifty from Abraham until Moses time
  6  first confirm Lord-<suffix_of_divine_name> Moses on-angel <preposition_of_genitive>-Lord and say
  7  God angel Moses because-this on-learn this Moses this
  8  people three law <preposition_of_genitive>-Lord because-this people believe one

## 209v — the three laws, and what Zacchaeus kept

> God; second, take not God's name in vain; third, God's law: […] the holy Sunday and the feast, this holy man, from the mother, the temple; let a man hear the preaching. This is God's law; and the law a man bears; every such man is saved. And this Zacchaeus […] the word, loved, and bore these three laws of the Lord God. Here ends this teaching, the holy gospel. The Lord God, with all thy heart.

  1  God two God name in_vain grab three God law
  2  [...] holy-~Sunday and feast holy-this-somebody from* mother temple
  3  preach hear-somebody this God law and law somebody exist
  4  carry each,_every somebody exist be_saved and this Zacchaeus
  5  [...] word love and carry this three law Lord-<suffix_of_divine_name> end this
  6  learn holy-gospel Lord-<suffix_of_divine_name> with_all_thy_heart*

## 210r — a man possessed brought before the Lord

> This holy gospel begins, written by holy Matthew, in the fourteenth […] chapter | of the writing: the time, then, the Lord Jesus, in his thirty-third year, the time | the Lord Jesus preached in Jerusalem; and then they brought one man before the Lord Jesus, in […]; the man was evil, the evil one in him; and then the Jews: this Lord, by Lucifer, the help

  1  begins this holy-gospel
  2  write holy-Matthew inside
  3  14-+one end_of_numeral* chapter | <preposition_of_genitive>
  4  write time
  5  then-exist Lord-Jézus
  6  inside thirty ~begin-+three_days time preach | Lord
  7  Jézus inside Jerusalem and then-exist brought* one somebody
  8  before Lord-Jézus inside [...] somebody exist ~evil evil
  9  and_then Jew(ish) this-Lord hide_oneself-evil help

## 210v — the unclean spirit walks through dry places

> of the evil, from the people he casts out. And then the Lord Jesus: this Lord […] of the Lord's Father God; and this Lord, of the Father God, can do it, the Lord. And then the Lord Jesus: this, therefore, is pleasing; who is from the evil, he is pierced. And then the Lord Jesus: then he casts out from a man one unclean spirit, and the evil one goes to a dry place, and […] to the Lord, the place, that is, to the virgin, from the people, and to the word, the people; and there is […] the evil one's lodging; and then this evil one, this evil

  1  evil inside from people exorcise and_then Lord-Jézus this-Lord
  2  [...] <preposition_of_genitive>-Lord from-father-<suffix_of_divine_name> and this-Lord <preposition_of_genitive>-father-<suffix_of_divine_name> can miracle
  3  do,-Lord and_then Lord-Jézus this therefore-pleasing who-exist
  4  from evil exist pierce and_then Lord-Jézus then-exist.
  5  exorcise inside somebody one unclean
  6  ~spirit and go evil arid,_dry place and
  7  [walketh] to-Lord place that_is on-virgin-from people and
  8  on-word people and exist [...] evil
  9  lodging-+and_then this evil this-evil

## 211r — seven other spirits worse than himself

> and the evil one goes […] because from the evil, love, sin, the sinful man; and he takes […] seven evil ones, from the evil, trespass, mourning; and there are […] seven evil ones; and | they go, the evil ones, all seven. And then the Lord Jesus: how then this man, the one aforesaid […] and every man, O, into the house goes, this; and there stood up again one […] chief among this people, the Jews; and then: blessed is the womb which bore this Lord, and blessed are the breasts which | this Lord did nurse. And then the Lord Jesus: blessed is the Lord's mother,

  1  and go-evil [wicked] because from evil love sin somebody-sin
  2  and exist grab [...] seven evil from evil
  3  trespass mourn and exist [wicked] seven evil and | go
  4  evil each,_every seven and_then Lord-Jézus how? then-chapter this somebody
  5  one earlier_mentioned [...] and each,_every somebody oh inside house
  6  go-this ~and stand_up-?again one [?]-to-[?] head
  7  among this people Jew(ish) and_then blessed from womb
  8  which-+<subject_marker> this-Lord carry and blessed from breast which | this
  9  Lord nurse and_then Lord-Jézus blessed <subject_marker> <preposition_of_genitive>-Lord mother

## 211v — rather, blessed are they that hear the word of God

> the virgin Mary, which bore the Lord; and blessed are the breasts which did nurse the Lord; and even more blessed are the people, and God said: let a man hear, and say, and let a man bear it. Here ends this holy gospel. The Lord God, with all thy heart. This holy gospel begins, written by holy John

  1  virgin-Mary which-+<subject_marker> to-Lord carry and blessed from breast which
  2  to-Lord nurse even_more and blessed from people and God say.
  3  hear-somebody and say <subject_marker> carry-somebody end this
  4  holy-gospel Lord-<suffix_of_divine_name> with_all_thy_heart*
  5  begins this holy-gospel
  6  write holy-John

## 212r — whence shall we buy bread?

> in the sixth chapter of the writing: the time, then, the Lord Jesus in his thirty-third year, the time the Lord Jesus sat | by the Red Sea […]; and the Lord went through, the Lord Jesus went through the Red Sea to one mount; and the Lord Jesus sat upon this mount, and […] the Lord's two eyes to heaven […] and the Lord Jesus saw, upon every side, […] people coming to the Lord; and they came; and then the Lord Jesus: Philip, this people | take, the Lord's apostle Philip, to eat. And then holy Philip answered:

  1  inside six chapter <preposition_of_genitive>-write time then-exist Lord-Jézus
  2  inside thirty ~begin-+three_days time sit Lord-Jézus | on
  3  the_Red_Sea [...] and Lord through
  4  go-Lord Lord-Jézus through the_Red_Sea to-one
  5  mount and sit Lord-Jézus to-this to-mount
  6  and [...] <preposition_of_genitive>-Lord two eye heaven [...] and
  7  see Lord-Jézus on-each,_every two-two [...] people to-Lord and
  8  go and_then Lord-Jézus Philip this people | grab
  9  apostle-Lord-Philip eat and_then holy-Philip answered

## 212v — five barley loaves and two fishes

> then two hundred pennyworth would not be enough, this day's bread to buy, therefore, for the people. And then holy Andrew answered: this […] one […] son; and the son has five loaves of barley bread, and two fishes. And the apostles brought these five loaves of barley bread and these two fishes before the Lord Jesus; and the Lord Jesus took this bread and these two fishes; and this bread and

  1  then-exist have two-hundred denarius who-exist people
  2  exist-today’s buy therefore* people enough and_then
  3  holy-Andrew answered <subject_marker> this [...] one.
  4  [...] son and have son five.
  5  loaves barley bread and two fish
  6  and carry apostle this loaves five barley
  7  bread and this two fish before Lord-Jézus
  8  and grab Lord-Jézus this bread and
  9  this two fish and this bread and

## 213r — twelve baskets full

> these two fishes the Lord Jesus blessed; and then the Lord Jesus to the apostles of the Lord: apostles, sit this people down upon the grass; and the Lord Jesus divided this bread to the apostles, and these two fishes, in turn, the apostles to this people; and then the apostles, every apostle took his portion, and then the apostles to the whole wide world, upon eating; and then | the Lord Jesus to the Lord's apostles: go, apostles, and take this, of the leftovers; and into baskets the apostles, of the leftovers, twelve filled up; and then the Lord Jesus to the Lord's apostles: go out among this people; and then the apostles carried the twelve baskets filled up out

  1  this two fish bless* Lord-Jézus and_then Lord-Jézus apostle
  2  <preposition_of_genitive>-Lord sit-apostle down this people on-grass and on-divide_into_parts
  3  Lord-Jézus this bread apostle and this two fish in_turn apostle this
  4  people and then-exist apostle each,_every apostle-[?] portion grab-apostle
  5  and then-exist apostle-[?] to the_whole_wide_world on eat and_then | Lord
  6  Jézus apostle <preposition_of_genitive>-Lord go-apostle and grab-apostle this from
  7  leftovers and on-basket apostle from leftovers six-six
  8  fill_up and_then Lord-Jézus apostle <preposition_of_genitive>-Lord go this out(ward) among
  9  people and then-exist apostle carry basket six-six fill_up out(ward)

## 213v — this is of a truth the prophet

> among this people, to the many; and this many people saw what the Lord Jesus could do, and all the people gave the Lord thanks; and this word they cried out, thanks: there is God, by the letter, the most high; and the Lord took a man by name, he could, and a man could do this miracle; and he left, among this people, the Lord Jesus. Here ends this holy gospel. The Lord God, with all thy heart. This holy gospel begins, written by holy John, in the eighth chapter of the writing: the time, then, the Lord Jesus, in his thirty- | third year, the time.

  1  among this people to-many and see this to-many people can Lord-Jézus
  2  and Lord each,_every people thanks grab and this word who-shout-to
  3  thanks exist God literal-on most_high and the_Lord grab-somebody name-+one can
  4  and somebody can this miracle do, and leave among
  5  this people Lord-Jézus end this holy-gospel Lord-<suffix_of_divine_name> with_all_thy_heart.*
  6  begins this holy-gospel
  7  write holy-John inside
  8  six-two chapter <preposition_of_genitive>-write
  9  time then-exist
 10  Lord-Jézus inside thirty | ~begin
 11  three_days time.

## 214r — he that is of God heareth the words of God

> The Lord Jesus preached in Jerusalem, and the Lord Jesus said to the Lord's apostles and to the Jewish people: he left behind one, afar, among you, apostles; and the Lord upbraided them for sin; and then the Lord Jesus: amen, amen, this Lord says to you, apostles, and […] from God: whosoever is of God heareth God's word; in turn whosoever, therefore, is not of God, whosoever, God's word he heareth not. And this […] from the two […]; and then the Jews: this Lord is a blasphemer; this Lord, Lucifer, the evil one, the evil, the Lord has; this Lord is one who began to believe

  1  preach Lord-Jézus inside Jerusalem and say Lord-Jézus apostle <preposition_of_genitive>-Lord and Jew(ish)
  2  people leave-leave one far among you-apostle
  3  and Lord on-sin admonish-chapter and_then Lord-Jézus amen amen
  4  this-Lord you-apostle speak-Lord and [?]-+<subject_marker> from*
  5  God this whosoever-[?] God say hear in_turn and whosoever-[?] therefore*
  6  from* God this whosoever-[?] God say therefore* hear and this
  7  [?]-+<subject_marker> from* two hath_a_devil* and_then Jew(ish)
  8  this-Lord one blasphemer this-Lord hide_oneself-angel hide_oneself-evil
  9  evil have-Lord this-Lord one ~begin-believe

## 214v — before Abraham was made, I am

> and this Lord, on the holy feast, healed the sick. And then the Lord Jesus, in this […]: this Lord, through sin, this healing; you are sorrowful, love; this Lord, you, on the holy feast healed the sick. And then the Lord Jesus: amen, amen, this Lord says to you; and whosoever, therefore, believes the Lord, that one therefore, whosoever, is saved; but every man is damned who remains; and | the man, the apostles said, is the Lord's; believe, whosoever lives | whosoever, one, the apostles said. Chapter. Chapter. He shall not die. And then the Jews: Abraham of theirs, the black, believed God;

  1  and this-Lord on-holy-feast ill from-healing-Lord and_then Lord-Jézus inside
  2  this [...] this-Lord through sin this healing <subject_marker> you sad(ly)
  3  love this-Lord you on-holy-feast ill from-healing-Lord
  4  and_then Lord-Jézus amen amen this-Lord you
  5  speak-Lord and whosoever-[?] therefore* Lord believe and one
  6  therefore-?whosoever-[?] be_saved a) each,_every somebody be_damned remain* and | somebody
  7  apostle-+say exist Lord believe from whosoever-[?] exist | living-?whosoever
  8  one-apostle-+say chapter-oh chapter-oh not die and_then
  9  Jew(ish) <preposition_of_genitive>-+say Abraham black <subject_marker> God believe

## 215r — Abraham saw my day

> and the black one, God's word he heard, Abraham, and still […] in turn, this Lord shall not die. And then the Lord Jesus: this Lord saw the death of father Abraham. Said the Jews to the chief men: therefore this Lord is fifty, in turn this | two thousand years, likewise, of their father Abraham […] in turn | this Lord spoke […] Abraham; the Lord saw; this, therefore, is pleasing; this Lord is a blasphemer. And then the Lord Jesus: the Lord is first; this Lord left, but rather your father Abraham, in this world […]

  1  and black <subject_marker> God say hear Abraham and still <subject_marker> is_dead*
  2  in_turn this-Lord not die and_then Lord-Jézus this-Lord see
  3  [?]-die from-father Abraham say Jew(ish) on-head
  4  therefore* this-Lord fifty in_turn-+<subject_marker> this | two-?thousand
  5  year likewise* <preposition_of_genitive>-+say from-father Abraham is_dead* in_turn | this
  6  Lord speak-Lord [...] Abraham Lord see-Lord this therefore* pleasing
  7  this-Lord blasphemer and_then Lord-Jézus first-Lord this-Lord leave but_rather
  8  you from-father Abraham on-this world* [...]

## 215v — then they took up stones

> And then the Jews: this, therefore, is pleasing; this Lord is a blasphemer; and they carried stones, and would have stoned the Lord Jesus; and the Lord Jesus left from among them, and out | of the temple the Lord went, and the Lord's apostles. Here ends this holy gospel. The Lord God, with all thy heart. Because it is written in Moses, truly, in turn […] among you, if a man begin to blaspheme, and a man has stones, and out from among them […] […] spoke holy Elijah the prophet and holy Moses; therefore he said they could, because of […] the Lord, the Lord God created, of theirs

  1  and_then Jew(ish) this therefore* pleasing this-Lord one blasphemer
  2  and carry-+say stone and would_say* stone-stone-this
  3  Lord-Jézus and leave among-+say Lord-Jézus and out(ward) | on
  4  temple and go-Lord and <preposition_of_genitive>-Lord apostle end this holy-gospel
  5  Lord-<suffix_of_divine_name> with_all_thy_heart* because-exist inside Moses righteous(ly) write in_turn [...]
  6  among you ~begin somebody how? blasphemer and have
  7  somebody stone-stone-this and among-+say out(ward) [...] [...]
  8  speak holy-+Elijah prophet and holy-Moses therefore* he_said*
  9  can-+say because* <preposition_of_genitive>-[?] Lord create Lord-<suffix_of_divine_name> <preposition_of_genitive>-+say

## 014r — the Lord went in humility

> the Lord God; because the Lord went in humility, in turn the king, there is heaven and earth, and many a miracle there was afterward, the Lord; and you, the Lord, | upon the cross died, and on the third day stood up from the dead, and appeared to many people, and the Lord was to you, through staying […] the year; and then this […] year […] see, they said, upon all the people; see, he left behind, into heaven and earth; and he left behind, they said […] believe: he himself is truly the Son of the living God, and King of all kings, and Lord of all lords, the chief Lord of heaven and earth.

  1  Lord-<suffix_of_divine_name> because go-Lord humble-Lord in_turn king exist heaven and ~earth
  2  and many miracle exist afterward-Lord and you Lord | on
  3  cross-die and on_the_third_day from die stand_up and appear many people
  4  and exist-Lord to-you through stay [?]-year
  5  and then-exist this [?]-year [...] see
  6  say-[?] on-each,_every people see leave-leave inside heaven
  7  land and on-leave-leave exist-+say that* believe
  8  he_is* righteous(ly) son living God and king each,_every king and
  9  Lord each,_every Lord head Lord heaven and ~earth

## 014v — a new gospel begins

> This holy gospel begins, written by holy Matthew, in the twentieth, in the first chapter of the writing: the time | then

  1  begins this holy-gospel write holy-Matthew inside
  2  one-ten-+one-ten inside one chapter <preposition_of_genitive>-write time | then

## 011r — go into the village, and you shall find an ass

> the Lord Jesus was in his thirty-third year, the time | the Lord Jesus went to Bethany, into Jerusalem, and the twelve apostles; and then | the Lord went to the lodging […] there was […] prayer, until, because the trespassing way of the people, the lodging; and the trespassing, through the night, the lodging of the Lord Jesus; and then the Lord Jesus sent two apostles down to Bethany, because the trespassing, they carried all […] the way of the people, one ass; and then the Lord Jesus: in turn, brethren, you […] therefore take it, they said, the two disciples, take it, the two disciples, the ass […] the apostles […] love

  1  exist Lord-Jézus thirty ~begin-+three_days time go | Lord
  2  Jézus on-Bethany inside Jerusalem six-six apostle and then-exist | go
  3  Lord on-+lodging [...] exist [...] as* ~until because
  4  trespass way people lodging and trespass through night
  5  lodging Lord-Jézus and then-exist-Lord go Lord-Jézus two apostle down
  6  Bethany because trespass carry-+say each,_every [...] way people
  7  one donkey and_then Lord-Jézus in_turn-?brethren you
  8  [...] therefore-+say grab-+say say learn-two-learn
  9  grab-+say learn-two-learn donkey [tied] apostle-+<subject_marker> [...] love

## 011v — they set him thereon

> […] they answered, going […] the ass, in the place, you, the ass, to say; and then the two disciples were […] one […] the ass, to the ass, two asses, the ass; and then the apostles untied this ass, and […] this commandment; but […] and the Lord Jesus sat down upon the ass, he said; and the Lord had the apostles tie this, from the ass, the mother of this ass; and the Lord sat upon this ass, and the Lord went into Jerusalem; and then the Lord was; the Lord went upon the mount of Olives, the most high, Jerusalem, […]

  1  [...] answered on-go [...] donkey on-place you donkey to
  2  say and then-exist learn-two-learn exist [?]-[?].
  3  one [...] donkey to-donkey two donkey
  4  donkey and then-exist tie_up-apostle this donkey and
  5  [...] this commandment a) [...] and sit down Lord-Jézus
  6  on-?he_said donkey and Lord tie_up apostle this from
  7  donkey mother this donkey and sit-Lord on-this
  8  from donkey and go-Lord inside Jerusalem and then-exist.
  9  exist-Lord go-Lord on-tasty-to mount most_high Jerusalem in_turn-chapter-in_turn

## 012r — the multitude went before him

> and […] the Lord Jesus and the Lord's apostles, because they were taught […] and then the Lord Jesus to the Lord's apostles: go, you, […] and in turn, brethren, you […] there is judgment, who is it; and the apostles went, the apostles said, and the apostles went to the Lord, to answer; in turn, to the Lord, they went the two ways; and then the Lord was to the Lord […] many people, because they preached, this people […] the Lord Jesus went; and an army went to the Lord Jesus; and then the Lord Jesus kept going to Jerusalem, and then the Lord was; he saw upon Jerusalem the people; and the Lord Jesus went

  1  and [...] Lord-Jézus and <preposition_of_genitive>-Lord apostle because learn exist [...]
  2  and_then Lord-Jézus apostle <preposition_of_genitive>-Lord go you
  3  [...] and in_turn-?brethren you [...] exist judge
  4  who_is_(it) and go-apostle say-apostle and go-apostle to Lord to
  5  answered in_turn to-Lord go two way and then-exist-Lord
  6  exist to-Lord [...] many people because [?]-+preach this
  7  people [...] go Lord-Jézus and and go an_army
  8  to Lord-Jézus and then-exist keep_going Lord-Jézus to-Jerusalem
  9  and then-exist-Lord exist see on-Jerusalem people and go Lord-Jézus

## 012v — hosanna to the son of David

> into Jerusalem; and with much joy they cried out, this Lord; and the son came, David the king; and the Lord, with much joy, said, because one man, they said, of […] believed; mercy and love, they spread, the men, before the Lord Jesus; and secondly they said, the men, branches of trees | they cut off, they said, the men; and […] | […] the men, before the Lord Jesus; and they cried out | this Lord is the son of David the king; they brought the king a crown, they said; and the Jews spoke: this Lord

  1  inside Jerusalem and many joy shout-[?] this-Lord and go son
  2  David king ~and-Lord many joy say
  3  because one somebody-+say <preposition_of_genitive>-[?] believe
  4  have_mercy-love spread-+say-somebody before Lord-Jézus
  5  in_turn-two say-somebody tree_branch-+<subject_marker> | cut_off
  6  say-somebody and [...] | [...]
  7  somebody before Lord-Jézus and shout-[?] | this
  8  Lord <subject_marker> son David king brought-[?].
  9  king crown-+say and speak Jew(ish) this-Lord

## 010r — my house shall be called the house of prayer

> is the king of the Jews. And this word they cried out: thanks to the Lord from all the people on earth, and the angels of the eternal height; and the Lord Jesus went into the temple at Jerusalem; and then the Lord found the money changers; and the Lord, all the money changers, out […] | cast out, the Lord; and then the Lord Jesus: this temple is a house of prayer, a house by name; you have made it a den of thieves. And then, from one little son they cried out: this Lord is […] the king. And then one of the Jews answered: see, the Lord, the brethren, this

  1  king Jew(ish) and this word shout-[?] thanks
  2  Lord each,_every people on-earth and angel from_the_eternal* high and
  3  go Lord-Jézus inside temple Jerusalem and then-exist exist-Lord find
  4  money_changer and-Lord each,_every money_changer out(ward) [...] | exorcise
  5  Lord and_then Lord-Jézus this temple-+<subject_marker> pray house
  6  name-+one house you say do, one
  7  thief-+one-house and then-exist from one little son
  8  and shout-to this-Lord <subject_marker> [?]-+say king
  9  and_then one Jew(ish) answered see-Lord brethren* this

## 010v — out of the mouth of infants

> little son speaks […] this Lord is their king. And then the Lord Jesus: then this, every one, this little son, therefore | speaks; the son, then, the earth is, and the rock and stone, all are, they cry out […] this Lord is your king. Here ends this holy gospel. The Lord God, with all thy heart. And then the law of the Jews; and the Lord said: take, in this […] Jerusalem, one rather, but rather they said, they could […] this, they would, the chief, take; and then […] the lodging to find, the Lord's heart, heaven and earth, Lord of all lords,

  1  little son speak-~son [...] this-Lord <preposition_of_genitive>-+say king and_then
  2  Lord-Jézus then-exist this each,_every this little son therefore* | speak
  3  ~son then exist earth and rock-stone each,_every exist.
  4  shout-to [...] this-Lord you-+say king
  5  end this holy-gospel Lord-<suffix_of_divine_name> with_all_thy_heart* and then-[?]
  6  law Jew(ish) and say Lord grab inside this in_turn-chapter-in_turn Jerusalem
  7  one rather but_rather-+say exist-+say can-+say [...] this
  8  would_say* head grab and then-exist [...]
  9  lodging find heart-Lord heaven and earth Lord each,_every Lord

## 013r — the prophet foretold it

> King of all kings; spoke holy […] the prophet, and holy […] the prophet, therefore, could the lodging find, the Lord's heart; and the chief of heaven and earth, Lord of all lords, King of all kings; and out, the two, loving, foretold, the prophet, and holy […] the prophet; and the Lord Jesus went […] into Bethany, this […] went […] the two, above, hidden, the earth; and this, many thanks the Lord did; in turn […] the Lord […] much sorrow; and then the Lord Jesus: this is […] every one, from a man; and a man is of the Lord's name among men; and out of the man, the good man does.

  1  king each,_every king speak holy-<name_of_a_prophet> prophet and holy-<name_of_a_prophet>
  2  prophet therefore* can lodging find heart-Lord and head
  3  heaven and earth Lord each,_every Lord king each,_every king and
  4  ~out(ward) love-two-exist predict <name_of_a_prophet> prophet and holy-<name_of_a_prophet>
  5  prophet and go Lord-Jézus [...] inside Bethany this [...]
  6  go [...] two above-hide_oneself earth and this many thanks Lord do,
  7  in_turn [...] Lord [...] many sad(ly) and_then Lord-Jézus this
  8  exist [...] each,_every from somebody and somebody exist <preposition_of_genitive>-Lord name
  9  among somebody and out(ward)-somebody good-somebody do,

## 013v — the three tables of Moses

> Three tables Moses took, and the Lord God wrote by the Lord's angel.

  1  three tablet Moses grab and write Lord-<suffix_of_divine_name> on-angel <preposition_of_genitive>-Lord

## 218r — Gamaliel and Nicodemus, and a servant named Saul

> the second, this holy man remits; the mother, the temple; let a man hear the preaching, from the seeing; heaven and earth; and the time of prayer, the two church fathers at Jerusalem; three chiselled on tables of stone, because the Lord God had Moses chisel three tables of stone by the Lord's angel, and wrote three commandments. Thanks to the Lord God. The time, then, from Adam onward, seven […] and three thousand; and the time of these three tables of Moses, the prayer, two church fathers, two high priests at Jerusalem: Gamaliel the high priest and Nicodemus the high priest; and then two servants hired themselves to these two high priests, as apostles; one man there was, and his name was Saul,

  1  two holy-this-somebody remit mother temple preach hear-somebody
  2  <preposition_of_genitive>-from-see <subject_marker> heaven land and time pray two
  3  church_father on-Jerusalem three on-stone-tablet chisel because exist Lord-<suffix_of_divine_name> Moses
  4  three stone-tablet chisel on-angel <preposition_of_genitive>-Lord and write three commandment
  5  to-Lord thanks Lord-<suffix_of_divine_name> time then-exist from ~Adam onward* seven-[?] and
  6  ~begin-+three_thousand and time this three tablet Moses pray
  7  two church_father two high_priest-high_priest on-Jerusalem Gamaliel high_priest and Nicodemus
  8  high_priest and then-exist two servant hire_oneself_out on-apostle this two high_priest-high_priest
  9  one somebody exist and-~exist-exist-+name Saul

## 218v — Stephen, the first martyr

> and the second apostle was holy Stephen, the Lord God's first martyr; and | then there were two servants, these two, two apostles, these two, two high priests; in turn these two, two apostles, the two of them from […] the two, in belief, of Christ; this was the time, then, the Lord Christ was crucified, and then the Jews […] down, believing Christ, the Jews, the chief men; and they were, they said […]; and there was a man, to many […]; a man by the name of Christ, every man suffering; in turn, a man rather, the chief | take, they said; and then holy Stephen […] […] the name

  1  in_turn-two apostle exist holy-Stephen first-suffering-Lord-<suffix_of_divine_name> and | then
  2  exist two servant two this-two two apostle this-two two high_priest-high_priest
  3  in_turn this-two two apostle exist-two from [...] two on-believe
  4  [?]-~Christ this exist time then Lord-~Christ crucified
  5  and then-exist Jew(ish) [...] to-down believe ~Christ Jew(ish)
  6  head and exist exist-+say [...] and exist
  7  somebody to-many [...] somebody name [?]-~Christ
  8  each,_every somebody suffering in_turn somebody-?but_rather head | grab
  9  say and then-exist holy-Stephen [...] confess name

## 217r — they brought him to suffer

> of Christ; and then the Jews, the chief men, made ready against this holy Stephen, the Lord God's first martyr; and then Stephen they brought, they said, to suffer, within the temple at Jerusalem, the two of them, among them; Stephen went […]; and this Saul to them; and Saul went, because therefore […] many; and this Saul, and then Stephen, they said, was brought within the temple at Jerusalem, because they would stone Stephen, because it is written in Moses, truly, in turn […] among you, if a man begin to blaspheme, and a man has stones, and | among

  1  [?]-~Christ and then-exist prepare Jew(ish) ~head-chapter on-this
  2  holy-Stephen first-suffering-Lord-<suffix_of_divine_name> and then-exist Stephen
  3  exist-+say brought* on-suffering inside Jerusalem temple
  4  two-+say among-+say Stephen go-[?] and this Saul
  5  to-+say and go Saul because therefore* [...] many and this Saul
  6  and then-exist Stephen exist-+say to-?brought inside temple Jerusalem
  7  because Stephen would_say* stone-stone-this because-exist write inside
  8  righteous(ly) Moses in_turn [...] among you begin somebody
  9  how? blasphemer and have somebody stone-stone-this and | among

## 217v — the heavens opened

> they said, out […] […] | and then holy Stephen knelt down; and | then Stephen prayed to the Lord, gave thanks to the Lord God, they said; and then Stephen prayed, redeemed, to the Lord, gave thanks to the Lord God; and Stephen lifted up Stephen's two eyes to heaven and earth, and to the Lord, to thanks, the Lord God; and this word holy Stephen said, to the Lord, to thanks, the Lord God, through offering, Stephen, this Stephen, this Lord, Stephen's soul within, the Lord's, why in turn; the time, then, the gate of heaven; and then Stephen saw one king sitting on a throne, and […] an army, an army

  1  say out(ward) [...] [...] | and then-exist kneel_(down) holy-Stephen and | then
  2  exist pray-Stephen to-Lord to-thanks Lord-<suffix_of_divine_name> to-+say and then
  3  pray ~redeem Stephen to-Lord to-thanks Lord-<suffix_of_divine_name> and lift_up-Stephen
  4  <preposition_of_genitive>-Stephen two-eye-eye heaven land and to-Lord to-thanks.
  5  Lord-<suffix_of_divine_name> and this word say holy-Stephen to-Lord to-thanks Lord-<suffix_of_divine_name> through
  6  offer Stephen this-Stephen this-Lord <preposition_of_genitive>-Stephen soul
  7  inside <preposition_of_genitive>-Lord why?-in_turn time then-exist from-gate
  8  heaven and then-exist-Stephen see-Stephen one king
  9  inside throne sit and [...] an_army army

## 216r — they stopped their ears

> of angels; and holy Stephen cried out; Stephen saw […] | see, the gate of heaven and earth is opened, and Stephen saw one king, crowned, sitting on a throne, and […] an army, an army of angels. And then the Jews: this Stephen is a blasphemer, Stephen; and they took off from themselves their belief; and they left, the letter, the man, one son; and this son was this Saul; and the man was this belief; and the scribes would stone holy Stephen | the first martyr

  1  angel and shout-to holy-Stephen see-Stephen [...] | see*
  2  gate/open heaven land and see-Stephen one
  3  king crown inside throne sit and [...]
  4  an_army army angel and_then Jew(ish)
  5  this-Stephen-+<subject_marker> one blasphemer-Stephen and.
  6  take_off-+say on-+say <preposition_of_genitive>-+say believe and.
  7  leave-+say literal man* one son and this son.
  8  exist this Saul and man* exist this believe
  9  and from the_scribes* want stone-stone-this holy-Stephen | first-suffering

## 216v — Stephen prays for those who stone him

> of the Lord God […] and the scribes judged; they could stone Stephen; and the scribes were […] in Stephen's death; and this, spoken, written; then, therefore, Stephen prayed for the scribes, and Stephen, the Lord God's first martyr, to the Lord, to thanks, the Lord God; the scribes were; they are damned; and then Stephen, they said, out of the town, stoned […] […]; and | then that day he was; he saw this suffering, this Saul, […] what the Jews did to holy Stephen; | the first, not, not, not; to the Lord, to thanks, the Lord God; and then | there were the scribes; through startling, this Saul, and trespassing, to the place

  1  Lord-<suffix_of_divine_name> [...] and judge-?the_scribes can Stephen stone-stone-this
  2  and from the_scribes* exist [...] inside <preposition_of_genitive>-Stephen die and this speak
  3  write then-exist therefore* Stephen to-?the_scribes pray-Stephen
  4  and Stephen first-suffering-Lord-<suffix_of_divine_name> to-Lord to-thanks Lord-<suffix_of_divine_name>
  5  exist-?the_scribes exist be_damned and then-exist Stephen exist-+say
  6  out(ward) on-town stone-stone [...] [...] and | then-chapter
  7  day exist see this suffering this Saul
  8  [...] do, Jew(ish) on-holy-Stephen | first-not
  9  not-not to-Lord to-thanks Lord-<suffix_of_divine_name> and then-exist | exist
 10  the_scribes* through startle this Saul and trespass to-place

## 219r — Saul takes letters to Damascus

> and by the name of the brethren of the Lord Jesus Christ; and this Saul went to the chief men of the Jews, to Jerusalem; one from this Saul they took, the chief men, the scribes; they could, upon this man that believeth not, and the man who this Jesus, this Christ, believes; and […] the scribes, the mother, the scribes would, every one take prisoner, and whosoever, to many […] see, by the name of the brethren of the Lord, the scribes would, every man to you, this going; and then the scribes, they said, took a commission, many riches; and then the scribes were […] many servants on the commission.

  1  and-brother-+name Lord-Jézus-Christ and go this
  2  Saul to-head Jew(ish) on-in_turn-chapter-in_turn Jerusalem
  3  one-from this Saul grab-+say head the_scribes*
  4  can on-this somebody not_believe and somebody this Jézus this
  5  Christ believe and [...] the_scribes* mother want-?the_scribes <subject_marker> each,_every
  6  take_prisoner and whosoever-+<subject_marker> to-many [...] see* and-brother-+name
  7  <preposition_of_genitive>-Lord want-?the_scribes each,_every somebody to-you this-go-this
  8  and then-exist the_scribes* exist-+say grab mission many ~rich
  9  and then-exist exist-?the_scribes [...] many servant on-mission

## 219v — a light from heaven

> And then, within | within Jerusalem, one […] a town there was, named Damascus, because, and within […] they believed the Lord Jesus Christ; and then this one went, Saul, upon this town, many an army; and | then Saul said to the servants, at the beginning of the way, Saul and the servants going, the time; and this Saul went, the scribes' servant, and then there was a light […] from heaven and earth, and then there was a light […] to the heavenly; he bowed down, and the Lord God cried out upon the water: Saul, Saul,

  1  and then-exist inside | inside Jerusalem one-in_turn-chapter-in_turn
  2  exist-[?] town exist Damascus because and
  3  inside that* believe Lord-Jézus Christ and then-exist go this-who
  4  Saul on-this town many an_army and | then-exist
  5  say-Saul-servant on-~begin way to-go-Saul-servant
  6  time and go this Saul ~exist-chapter <preposition_of_genitive>-?the_scribes servant
  7  and then-[?] exist light [...] on-heaven land
  8  and then-[?] exist light [...] on-+heavenly-to bow_down
  9  and shout-to Lord-<suffix_of_divine_name> on-water Saul Saul

## 220r — I am Jesus of Nazareth

> to the brethren of the Lord, through persecuting the scribes; and he cried out, this | Saul, the scribes […] lie; in turn the Lord […] this Lord; and the Lord God cried out upon the water: this Lord is Jesus of Nazareth, the Lord, on the cross executed; and this Saul cried out: Lord, brethren, Saul, the Lord, afterward; and the Lord God cried out upon the water: go, scribes, into the […]; from the scribes, teach a man love; the scribes were; the scribes did it, the time, the hour, from the blinding of the scribes' eyes; and […] and then there were those who took Saul's servants; and Saul they carried,

  1  to-?brethren Lord through persecute-?the_scribes and shout-to this | Saul
  2  the_scribes* [...] lie in_turn Lord [...] this-Lord and
  3  shout-to Lord-<suffix_of_divine_name> on-water this-Lord from Jézus Nazareth
  4  the_Lord cross execute and shout-to this Saul
  5  Lord brethren* Saul Lord afterward* and shout-to
  6  Lord-<suffix_of_divine_name> on-water go-?the_scribes inside in_turn-chapter-in_turn from the_scribes* on-learn somebody
  7  love exist-?the_scribes do,-?the_scribes time hour from
  8  blind-eye-?the_scribes and [...] and then-[?] exist
  9  grab <preposition_of_genitive>-Saul servant and Saul from-carry

## 220v — the house of Judas, and Ananias

> Saul, the servants, into the […]; and they put Saul, the servants, one man, Ananias; and a man, Ananias, was coming, Gamaliel, the […]; and this Saul, trespassing, the scribes were at the coming; and then there was this Saul, this Ananias put Saul, the servants, into one house; and then three days the scribes lay, this Saul, within this house, this Ananias, the man; and this man's name was Judas; and then one man within this […] could, the man said, to the high understanding; in turn the man's name was

  1  Saul servant inside in_turn-chapter-in_turn and Saul put servant
  2  one man* Ananias* and somebody Ananias* exist coming*
  3  Gamaliel in_turn-chapter-in_turn and this Saul trespass exist-?the_scribes
  4  on-?coming and then-[?] exist this Saul this
  5  Ananias* put <preposition_of_genitive>-Saul servant inside one house
  6  and then-[?] three lie-?the_scribes this Saul inside
  7  this house this Ananias* somebody and this somebody [?]-~exist-+name
  8  exist Judas and then-exist one somebody inside this in_turn-to-in_turn
  9  can somebody say to-high-understand in_turn [?]-~exist-+name somebody exist

## 221r — a vessel to bear my name

> Ananias; and Paul, from Paul; and he bowed down, […] upon Paul […]; and Ananias put the Lord's name upon Paul, because from Paul, Paul is | of the Lord; the name Paul bears into the wide world; Paul is | of the Lord; the name Paul confesses. And then holy Ananias: Lord, how is it, from Saul, of the Lord, the name | bears Saul, and Saul, of the Lord, the name, through persecuting, Saul? And secondly the Lord God said to holy Ananias: go, Ananias; the Lord's servant, in truth and love, drink

  1  Ananiah and Paul from-[?]-Paul and bow_down
  2  [...] on-<preposition_of_genitive>-Paul [...] and put Ananiah <preposition_of_genitive>-Lord
  3  name on-Paul because from Paul exist-Paul | <preposition_of_genitive>
  4  Lord name carry Paul on-+wide world* exist-Paul | <preposition_of_genitive>
  5  Lord name confess Paul and_then holy-Ananiah
  6  Lord how? exist from Saul <preposition_of_genitive>-Lord [?]-~exist-+name | carry
  7  Saul and Saul <subject_marker> <preposition_of_genitive>-Lord [?]-~exist-+name through
  8  persecute-Saul and two say Lord-<suffix_of_divine_name> holy-Ananiah
  9  go Ananiah <preposition_of_genitive>-Lord servant inside righteous(ly)-love drink

## 221v — a table of earthquakes and eclipses

> Before the Spirit, on the Friday, the earth, one quake; on the Spirit, on the Wednesday, the moon eclipsed one hour; and from the year before God, on the Friday, the earth quaked, from the Spirit; the first year from God, the first year, in turn, on the fast | three days before the virgin Mary; on the Sunday the earth quaked; and this, and the day […] […] upon heaven and earth, living, and confessing, to the letter; and a man […] sees […] […] to, within […] […] in turn, two years […] from the Spirit […]

  1  before spirit inside Friday earth one
  2  quake on-spirit inside Wednesday moon eclipse
  3  one hour and from year before God
  4  inside Friday earth quake from spirit
  5  first year from God first year in_turn on-fast | three
  6  day before virgin-Mary inside ~Sunday earth
  7  quake and this and day [...] [...] on-heaven
  8  land living and confess to-literal-to and somebody
  9  [...] see [...] [...] to inside [...]
 10  [...] in_turn two-year [...] from spirit [...]

## 223r — more of the same table

> the day the earth quaked, out, the first Spirit, Friday; and the years and three days of God, from the Spirit, twenty-two years […] from the Spirit […] the earth quaked, and the moon in turn, upon; and the year, at the beginning, from the Father of a man […] from […] whosoever; and […] in truth believing, the Lord bears the man […] believeth not; and this, every one, therefore have mercy, man […] and the man would, Christ, against, leave; the man, God, learn, the throne […] would, whosoever […] the Lord's throne […] truly of the Lord.

  1  day <subject_marker> earth quake out(ward) first
  2  spirit Friday and years* and three_days God from spirit two-two-year
  3  [...] from spirit [...] earth quake and moon
  4  in_turn on and year <subject_marker> ~begin
  5  from-father <preposition_of_genitive>-somebody [...] from [...] whosoever* and
  6  [...] inside righteous(ly) believe carry-Lord somebody [...]
  7  not_believe and this each,_every therefore-have_mercy somebody [...]
  8  and somebody want Christ against leave somebody God learn
  9  throne [...] want whosoever* [...] Lord-throne [...] righteous(ly)
 10  Lord-<preposition_of_genitive>

## 223v — the date, and the age of the world

> From the leaving of the Lord Jesus Christ to the Lord's Father, out, a thousand years, five hundred and sixty years; and by name, that day, thus, the beginning of the year, written. Twenty-two sons. From […] then it was, that day, in turn, see; and then the son, Moses […] by name, the year, the first day, seven, in turn, from the seeing, two years […] from the understanding, the earth; understanding; the Lord Jesus Christ was born into this world, out, five thousand and a hundred days, and | ninety years, and nine years; and this signifies nine, from the understanding, the beginning of this world, until the Lord Jesus Christ was born into this world; in turn, and from, out, from the understanding, to the leaving of the Lord Jesus to the Lord's Father, eternal, in turn […] the time the apostles said to the Lord Jesus: Master, when shall the judgment day be? Said

  1  from* to-leave Lord-Jézus-Christ from-father <preposition_of_genitive>-Lord out(ward)
  2  thousand-year five_hundred and six-ten-year and from-+name-+day
  3  this_is begin-year write
  4  two-two-son
  5  from* [...] then-exist exist [?]-+day in_turn see* and_then*
  6  son Moses [...] from-+name-year first-+day
  7  seven in_turn <preposition_of_genitive>-from-see two-year [...]
  8  from-understand earth understand be_born Lord-Jézus-Christ
  9  on-this world* ~out(ward) five_thousand and hundred-+day and | nine-ten
 10  year and nine-year and this symbolize nine from-[?] from-understand begin this world.
 11  until be_born Lord-Jézus-Christ on-this world in_turn and from-[?] ~out(ward)
 12  from-understand to-leave Lord-Jézus to-from-father <preposition_of_genitive>-Lord eternal* in_turn-[?]
 13  time say apostle Lord-Jézus Master when? exist understand judge-+day say

## 222r — when shall the judgment day be?

> […] the name of the Lord, of the Lord's Father God. In turn, out […] two thousand years, to this, the brother, of the chapter, one day; and he has from […] the judgment day; because anew, from the Son of God, judgment; the dead man, the sinful man damned, the sinful man; and saved, the light, said, said the Lord Jesus; this said the Lord's apostles; there is upon a man one, one, to the earth, water, sun, all […] the earth, the sun, Christ, […] the Lord God.

  1  [...] name <preposition_of_genitive>-Lord <preposition_of_genitive>-Lord from-father-<suffix_of_divine_name>.
  2  in_turn-[?]-~out(ward) [...] two-thousand-year to-+this_is
  3  [?]-+brother <preposition_of_genitive> chapter one day and have
  4  from covered-+one judge-+day because new-from son God judge
  5  die somebody sin be_damned somebody sin and be_saved
  6  light say say Lord-Jézus this say apostle <preposition_of_genitive>-Lord exist on-somebody
  7  one one to-to earth water sun each,_every [...]
  8  earth sun Christ
  9  [...] Lord-<suffix_of_divine_name>

## 222v — a calendar, with the writer's own name in it

> […] Monday, in the wound, he went, the writer of this book […] to the house, the brother, trespassing, he carried, the writer of this book […] on the Friday, […] the writer of this book […] on the Sunday he went, the writer of this book, to the seal […] remitted, at the beginning of the year […] this, out, one holy Philip's year […] Monday, on the […] he took, the writer of this book, until the beginning of the year; in turn, from the beginning of the year, one in turn […] […] […] the Lord, have mercy; in turn […] one […] in turn, in the middle, the man […] more than these; this said […] the writer of this book […] Friday […] […] the writer of this book; this, out, two; Sunday, by name, Sunday three, in turn, two by two; Sunday three, the Lord | Father, Son and Spirit; on the Monday there was […] conceived, to

  1  [...] Monday inside wound go-+the_name_of_the_author-somebody [...] to-house
  2  brother-trespass carry-+the_name_of_the_author-somebody [...] inside Friday
  3  [...] the_name_of_the_author-somebody [...] inside Sunday go-+the_name_of_the_author-somebody seal-to
  4  [...] remit ~begin-year [...] this out(ward) one
  5  holy-Philip-year [...] Monday inside <name_of_a_time_unit_or_calendar_date> grab-+the_name_of_the_author-somebody
  6  until ~begin-year in_turn from* ~begin-year one in_turn [...]
  7  [...] [...] Lord have_mercy in_turn [...] one [...] in_turn in_the_middle
  8  somebody [...] more_than_these* this say [...] the_name_of_the_author [...]
  9  Friday [...] [lunatic] the_name_of_the_author-somebody this out(ward) two Sunday name
 10  Sunday three in_turn-two-two <subject_marker> Sunday three Lord | father
 11  son-spirit inside Monday exist [...] get_conceived to

## 224r — the last leaf but one

> ninety-six, little, one […] Michael, on the Saturday, of the woman […] of Mark; he himself took, and […] and two, from two, the mother, on the Saturday […] […] on the Saturday, upon good […] more than these; upon a man there is, then, upon death, that day, upon the name […] […] […] Matthew, on the Saturday; and lo, one, this is […] Matthew […] […] on the Saturday […] […] […] understanding, who […] the cup by name; and from a man to this rich good […] and one […] three, and one […] three, believe upon this […] […] […] […]

  1  nine-ten six little one-[?]
  2  Michael on-Saturday <preposition_of_genitive>-woman [...]
  3  <preposition_of_genitive> Mark is_he* grab and [...] and two from two mother
  4  on-Saturday [...] [...] on-Saturday
  5  on-good [...] more_than_these* on-somebody exist then-+<subject_marker>
  6  on-die [?]-+day on-exist-~exist-+name [...]
  7  [...] [...] Matthew on-Saturday and lo
  8  one this <subject_marker> exist [...] Matthew [...]
  9  [...] on-Saturday [...] [...] [...]
 10  understand-who [...] cup-+name and from somebody to this rich good [...]
 11  and one [...] three and one [...] three
 12  believe on-this [...] [...] [...] [...]

## 224v — the end of the book

> the Lord Jesus Christ, saved; the Lord, wide, […] the son, living, of he said; and this man, upon the food, to, in turn, living, the woman, Matthew […] on the Saturday, within the seal […] Lord have mercy, you, have mercy, of Christ; and through offering, you, have mercy, have mercy, Lord; in turn, the woman […] […] and of […] and all, from the leaving […] […] on high; and […] there is, then, the soul from losing, from riches […] there is […] […] from the day, this why; and understanding, the man, the woman, this world, truly, two.

  1  Lord-Jézus-Christ be_saved Lord wide
  2  [...] ~son living-exist <preposition_of_genitive>
  3  say and this somebody on-food to-on in_turn
  4  living woman ~Matthew [...] on-Saturday inside
  5  seal-chapter [...] Lord have_mercy you have_mercy
  6  [?]-~Christ
  7  and through offer you have_mercy
  8  have_mercy Lord in_turn woman [...] [...]
  9  and <preposition_of_genitive> [...] and each,_every <preposition_of_genitive>-from-leave ark-+day [...]
 10  on high and <subject_marker> [...] exist then-+<subject_marker> soul from
 11  lose from-rich [...] exist [...] [...] from
 12  day this-why? and understand somebody woman
 13  this world righteous(ly) two
