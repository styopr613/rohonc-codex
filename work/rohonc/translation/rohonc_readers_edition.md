# The Rohonc Codex

### a reader's edition

Every line of all 441 folios, in the order the manuscript has them.

The script is undeciphered. The dictionary that makes this possible is
**Levente Király and Gábor Tokai's**, published at rechnitzer-kodex.hu, and
roughly three quarters of the words below are theirs or follow directly from
theirs. Their grammar paper is unpublished, so nothing here chooses between
the senses of a word that has several; the first sense is printed. This is not
their translation, which has never been published.

The English wording of the gloss is this edition's own. Which sign means which
word is Király and Tokai's finding and is credited to them; how each sense is
put in English here is ours, and their entries, with every sense in their own
words, are in their publication. Where a sign is grammatical rather than a word,
a short label stands for it: `DIV` the suffix of a divine name, `SUBJ` `OBJ`
`DAT` the markers of subject, object and dative, `AUX` `CAUS` `FUT` auxiliaries,
`PTCL` a particle, `DISTR` `PLACE` `END` the signs inside a numeral, `DATE` and
`DAY` a calendar name, and `NAME` a proper name known only by what it names
(`NAME.prophet`). `EOL` is a mark the scribe sets at the end of a line. A word
that begins with a hyphen (`-but`) is the second half of one word that the
transcription splits in two.

## How to read the marks

| mark | meaning |
|---|---|
| `word` | read |
| `word*` | read from one passage, with nothing in the book able to refuse it |
| `[word]` | **restored** -- a guess from the folio's source and its neighbours |
| `[...]` | dark: no reading, and no honest guess |
| `=` | this sign belongs to the phrase just before it: Király and Tokai read the signs together |

A hyphen inside a word (`cup-to`) is one sign of the manuscript
read as the smaller signs it is built from -- this script writes phrases
without spaces, which is the central fact Király and Tokai established about
it. A `~` marks a spelling their own apparatus files as a variant. A `|` is a
gap or an unreadable glyph in the transcription.

**What a bracket is worth.** The brackets are guesses, and they are printed
because a reader asked for the book completed rather than left in holes. Each
one was made by reading the line and the passage the folio itself cites, and
choosing the word that passage supplies for that slot. None of them is
verified, none is counted in the figures above, and the project measured what
a guess of this kind is worth before printing any: on words as rare as these,
the folio's cited passage contains the true word only 7.8% of the time, and
when it is there the best candidate is right about one time in four. Against
Király and Tokai's own hidden entries the top candidate scored 0.0%.

Three quarters of the content guesses do land on a word that actually stands
in the verse the folio cites, which is the only part of this that can be
checked from inside the book. Read a bracket as a suggestion by an editor who
knows the source and does not know the word.

**There are now no ellipses left.** Every word of the manuscript has an
English word against it. That is not the same as every word being read: 3.3%
of them are in brackets, and the brackets are the weakest thing in this
edition. The weakest of the weak are the last two leaves, 224r and 224v, which
are the worst-preserved in the book and cite no source; their brackets are
marked WEAK in the deposit and should be read as little more than placeholders.

Five brackets carry a chapter number that differs from folio to folio. The
sign is four strokes, a mark, four strokes, and the passage that follows it is
Matthew 16 on 195v, Matthew 18 on 134r, Matthew 22 on 202v and Luke 14 on
071r. One sign cannot be four chapters, so it is not read; each folio simply
prints the chapter its own following text shows.

## What this edition is worth, in numbers

    words in the manuscript            29997
    read                               28226 (94.1%)
    read from one passage, marked *    743 (2.5%)
    restored, in brackets              982 (3.3%)
    dark, printed as an ellipsis       46 (0.2%)

    lines with every word read         3565 of 4372 (81.5%)
    lines complete including
      restorations                     4326 of 4372 (98.9%)

The evidence for every single word is in `harness/proposals.json`, one entry
per sign, with its tier and the argument in full. `harness/ktprov.py` prints
where each reading came from and whether the manuscript itself can ever refuse
it. `harness/ktnull.py` and `harness/ktrederive.py` are the controls,
including the two that failed.

**Brackets are the measure of what is left to do.** Every time a source text
enters the corpus, or a formula turns up twice, some of them become plain
words. There are 982 of them now.

---


## 004v — the beginning: heaven, the angels, Lucifer

> In the beginning there was the Lord God. heart […] and the earth. The sun and the moon, [as] the scripture(?) [says]. Elijah the prophet. The angel of God said: [forefather] before heart of man. The Father […]; man bowed down(?) before the Lord. God in heaven eternal and the brethren. Many angels […]; and God the Father had many angels about him. Among the angels, two hundred and fifty(?) years seven before heart of man. The Father, Adam, and the angels […]; there was Lucifer, and the other angels. And the angels prayed, and for forty [days?] and forty nights […] Lucifer […] to Lucifer […] among the brethren, in hell. And again the angel said to Elijah: Elijah, when there is as Lucifer, who did [this] — Lucifer, when he was […] seated on the throne of God the Father. God the Father went […]

  1  time then-exist Lord God
  2  heart one-on-sky and ~earth
  3  sun and moon write
  4  Elijah prophet say angel God
  5  [forefather] before heart of-somebody
  6  from-father ~Adam bow Lord
  7  God on-on-sky heaven* in_turn-brother
  8  many ~angel on-~angel and exist to-from-father God on-many angel
  9  on-angel two-half-hundred-year seven before heart of-somebody
 10  from-father ~Adam and angel brother-+name exist Satan and two ~angel
 11  and angel Satan pray and forty days forty nights
 12  which Satan to Satan on-+one-?heaven on-in_turn-brother on-hell
 13  and two say angel to-Elijah Elijah and then-exist pray
 14  Satan who do Satan then-exist
 15  day sit on throne from-father God go from-father God

## 004r — the cup

> The angel of the Father said; God the Father; the angel said to Lucifer: because the cup was hidden away. above of the Father, on the throne and then God; the angel; Lucifer; the cup was hidden away. above the Lord on the throne; and when the cup […] [steal] the cup was hidden away above And when Lucifer […], the angel returned to the Father. and then the angel, the Lord, the cup, Lucifer [steal] the cup was hidden away above and the other went. God the Father; the angel of the Father [spoke] to Lucifer; Lucifer said: because the cup was hidden away. above with the Father, on the throne; and when Lucifer went to God the angel said: God; the angel; the cup was hidden away above the Lord on the throne; and when the cup of Lucifer […] the cup was hidden away […] and then […] | was hidden. The angel returned, the angel, to God the Father, because there was said Lucifer; to the Lord; hidden; the Lord God; the mother […] […] to the Lord, to the Lord, this | hidden. The angel [proud] Lucifer, he on the throne and then God, the angel, the Lord. The cup of Lucifer [steal] the cup was hidden away above said Lucifer to the Lord: hidden.

  1  angel of-father say from-father God angel say Satan because cup-to hide
  2  above* of-father on throne and_then God angel Satan cup-to hide
  3  above* Lord on throne and then-exist cup ~Satan [steal] cup-to hide above*
  4  and then-exist from Satan return angel to-father
  5  and_then angel Lord cup Satan [steal] cup-to hide above* and two go
  6  God_the_Father of-father angel to-Satan say Satan because cup-to hide
  7  above* on-of-father on throne and then-exist to-Satan go God
  8  angel say God angel cup-to hide above* Lord on throne and then-exist
  9  cup Satan [steal] cup-to hide above* and then-exist from | hide
 10  angel return angel to-father God because-exist
 11  say Satan to-Lord hide Lord_God mother ~be_born be_born* to-Lord to-Lord this | hide
 12  angel [proud] Satan this on throne and_then God angel Lord
 13  cup Satan [steal] cup-to hide above* say Satan to-Lord hide

## 002r — Michael, the command to bow, and Lucifer's fall

> The mother of the Lord God was born; and Lucifer […] to the Lord, to the Lord; Lucifer […] Lucifer, he upon the throne [set] of the Lord God [equal] There was the earth and then God the Father eternal Michael. The angels, faithful servants, rose up; and when they had risen, the heavenly ones spoke. God the Father eternal went to Lucifer, and Lucifer fell from the throne of the Lord; and when, within […] they bowed down — and of the angels every one — to whom Lucifer [would not] bow. And then see God the Father eternal, and cried out. God the Father eternal: Lucifer departed by commandment, because all were angels to whom Lucifer bowed. And [refused] […] said God the Father, from he departed. This was the angel. He left food(?) […], and three said the angel to Elijah the prophet: Elijah, say(?) God the Father is. To the Son came the Holy Spirit. Father, Son heart man and then God the Father, the Holy Spirit — how man knows the image of the Father.

  1  Lord_God mother be_born and Satan to-Lord to-Lord Satan [envied]
  2  Satan this on throne [set] Lord_God of-Lord finger
  3  exist earth and_then from-father God heaven* Michael
  4  angel believe servant stand_up up and then-exist stand_up
  5  heavenly say from-God_the_Father heaven* go to-Satan and
  6  Satan bow on throne of-Lord and then-exist inside [?]-+one-understand
  7  bow and from angel every to-which Satan bow
  8  and then-exist see* from-father God heaven* and shout
  9  from-father God heaven* leave Satan commandment because every exist angel
 10  to-which Satan bow and [refused] to-~go say from-God_the_Father from
 11  leave this exist angel leave food ~judge-year and three say angel
 12  to-Elijah prophet Elijah say SUBJ from-God_the_Father exist
 13  to-son go holy-spirit father son heart somebody and_then
 14  from-God_the_Father holy-spirit on-how? somebody form know father

## 002v — the Trinity, and the making of Adam

> The Son, the Spirit heart and then; the Son, in the image of the Lord. heart [likeness] man is; all one; to the Father, the Son, the Spirit. Father, Son and Spirit took man, and every living thing [creature] The soul heard. Adam saw the living, truly, not many | Father and Son — not many; the Holy Spirit; but this Lord is all, one God. and then God, the angel, Elijah the prophet. Elijah the prophet, when there were Father, Son and Spirit, going forth […] […] and the brethren, in this world, and […] | Paradise the Lord God, Adam heart slime (of the earth); and then Adam was heart as was said before slime (of the earth) and became […] heart breathed into Adam, and he became living, and the Lord God took Adam, and Adam went into Paradise; and all heart. End of chapter. Adam

  1  son spirit heart and_then son on-of form on-Lord
  2  heart [likeness] exist man^ all^ one to-father son
  3  spirit grab father son spirit man^ all^ living [creature]
  4  soul hear man^ see living righteous not many | from
  5  father from son not many holy-spirit but this Lord all^
  6  one God and_then God angel Elijah prophet
  7  prophet Elijah then-exist father son spirit to-go
  8  table from_the_eternal* in_turn-brother on-this world and out | to
  9  Paradise Lord_God man^ heart slime_(of_the_earth)* and then-exist
 10  man^ ~exist heart aforesaid slime_(of_the_earth)* and became* to-soul-+one
 11  heart breathe on-Adam and living leave and
 12  man^ grab Lord_God and man^ go inside
 13  Eden and all^ heart exist-chapter man^

## 003r — the commandment, and the sleep

> […] the Lord God [and] Adam. The Lord [spoke] to Adam; he took every truly [nor] hunger, and thirst [nor] upon Adam; and one living [thing] dies. There shall be sin, hunger, thirst, to him who [afterward] the Lord took. To Adam, all truly one. law this yoke upon Adam, by commandment: not […] this […] […] thou shalt die […] Adam is […] […] Adam would die. And then Adam slept within | […] and then upon him […] first, from […] and | when the Holy Spirit came within into Paradise and then this this the garden and the Lord God took Adam rib and it heart said the angel to you: mother. And then Adam, from […] […] this |

  1  and_then Lord_God Adam this-Lord this-Adam grab
  2  every righteous [nor] hunger and thirsty [nor] this-Adam and
  3  one living die sin have hunger thirsty to-to-this-who
  4  [afterward] grab-Lord this-Adam every righteous one
  5  law this yoke this-Adam command = not eat.
  6  this to-~son evil-~sin thou_shalt_die* ~if Adam exist eat.
  7  on-[?] die-Adam and then-exist Adam sleep inside | to
  8  Paradise and then-exist on-this name ~first from saying and | then
  9  exist go holy-spirit inside into_Paradise and_then this
 10  SUBJ this the_garden and grab Lord_God Adam
 11  rib and it heart say angel you
 12  mother and then-exist Adam from laugh* and_then this | to

## 003v — the rib, Eve, and the serpent

> Bone of bone; and the two souls are one. | Before […] and […] said the angel. The Lord God departed […] | Chapter. […] and Eve went into Paradise; and | when Eve came to that tree which stood in the midst the Lord God had by commandment [forbidden]; and she saw a serpent in that tree, which stood in the midst was the Lord God's by commandment and then this serpent it […] this fruit and then Eve shall not eat ate, because it Adam, the Master, by commandment and then this serpent. Eve ate it Adam one this fruit; and the fruit was it one Adam ate; and it Adam knew

  1  bone bone in_turn two soul one | before
  2  ~year-+name and five say angel leave Lord_God from_heaven* | in_turn-chapter
  3  ~year-~exist and go Eve on-Eden and | then
  4  exist Eve go to-this tree what stood_in_the_midst*
  5  exist Lord_God command = and see one
  6  serpent on-this tree what stood_in_the_midst* exist
  7  Lord_God command = and_then this serpent it
  8  ~eat this fruit and_then Eve shall_not_eat eat
  9  because it Adam Master command = and_then
 10  this serpent Eve eat it Adam
 11  one this fruit in_turn fruit SUBJ exist it
 12  one Adam eat exist it Adam know

## 001r — good and evil, shame, and back to Elijah

> evil and good, as the Lord God knows. And then they plucked, the serpent, this fruit, this serpent; and | Chapter. day took it and it took the fruit. Adam. And then […] the two of them, Adam, [were] naked. it saw Adam; and then it Adam was ashamed. And [chapter] six: the angel of God said to Elijah […] Elijah; and this deadly sin afterward Lucifer, the Father […] […] Lucifer had fallen | Father God from the eternal and the brethren hell and seven said the angel of God to Elijah the prophet: Elijah, the Lord God departed from the eternal […] within Paradise, saying

  1  evil and good how?-to Lord-God know and then-exist pluck
  2  serpent this fruit this serpent and | then-chapter
  3  day grab it in_turn it fruit grab
  4  Adam and then-exist were_opened* on-two Adam naked
  5  see it Adam and then-exist it Adam
  6  be_ashamed and six say God angel to-Elijah prophet.
  7  Elijah and this [deadly_sin] ~do Satan
  8  from-father heaven* who-+SUBJ Satan exist bow | father
  9  DIV from_heaven* in_turn-brother hell* and seven say
 10  God angel to-Elijah prophet Elijah leave Lord_God
 11  from_heaven* ~land inside Eden say

## 001v — where art thou

> The Lord God, with the angels, came out(?) saying and then departed. The Lord God from the eternal within into Paradise and then the Lord God. […] Where [art thou]? […] Adam […] the Lord God. […] The Lord God [spoke] with his own mouth. Adam hid himself […] Adam, who […] hast thou done. Said the Lord God: Where art thou, Adam? […] […] Eve [gave?] […] ate […] The Lord God it heavenly and then answered Eve, to the Lord, and then the Lord God: Why, Eve? answered Eve hast thou done and then the Lord God: Why, Eve? hast thou done and then it The serpent it ate and then the Lord God, Adam one commandment: this Adam […] did not keep(?) the commandment.

  1  Lord_God on-angel this ~out two from saying and then-exist leave
  2  Lord_God from_heaven* inside into_Paradise and_then Lord_God DIV
  3  Adam why? and_then ~Adam hide-~Adam Lord_God
  4  and_then Lord_God who-mouth ~Adam hide and_then ~Adam
  5  who this-~Adam hast_thou_done* say Lord_God why? ~Adam
  6  hast_thou_done* and_then Eve Adam food and_then.
  7  Lord_God it heavenly and_then answered* Eve this-Lord-to
  8  and_then Lord_God why? Eve answered* who Eve hast_thou_done*
  9  and_then Lord_God why? Eve hast_thou_done* and_then it
 10  serpent it food and_then Lord_God ~Adam
 11  to-one commandment this ~Adam name-[?]-ten commandment ~carry

## 007r — the curse, and the sword at the gate

> Adam was, to him who […] and why […] gates Adam was of the earth till the earth he would […] eat, and take, and it […] it was through pine; and […] was painful. coming shall be; and this evil — this evil is [cursed] the earth slide and room evil. Man was made, all of this. The serpent dies; and he departed from among Adam and Eve the Lord God; and there went the Lord God, the angel […] fire, a sword; and […] out | within Paradise. He drove them out, and set an angel sword

  1  exist ~Adam to-to-this-who [?]-~Adam in_turn why?-in_turn
  2  gates* exist ~Adam earth till_the_earth
  3  want to-~son food ~grab in_turn it this-+it
  4  exist through pine and this-+it exist painful
  5  ~be_born have in_turn this evil this-evil exist
  6  [cursed] earth slide ~and room
  7  evil this man^ create every this serpent die and
  8  become^ among Adam_and_Eve Lord_God and go
  9  Lord_God angel two-~earth-+Eve flame^
 10  sword and ~earth-slide out | on-inside
 11  Eden exorcise and place^ angel sword

## 007v — outside the garden: Cain, Abel, Seth, and Adam goes blind

> […] cherub Paradise; and one created [cherubim] within Paradise; but the angel and then the Lord God with the angel […] from […] and from eight(?) said | Elijah. The angel of God: Elijah, when the Lord God [drove] Adam out […] from Paradise; and then | Eve he dwelt in the field many years; and Adam had Eve offspring, these two sons. And the firstborn was Cain, and the second […] was Abel. third […] was Seth. And then Adam was blind in both eyes; and then Adam went into Paradise the son […]; and this son was [Cain] the son [Abel] Adam. And then Adam said: bring Adam from the tree of mercy

  1  on-~gate cherub* Eden and one create
  2  can_be inside Eden but angel and_then Lord_God
  3  on-angel this table three from saying and from two-two-two-two say | to
  4  Elijah God angel Elijah then-exist Lord_God ~Adam
  5  out cast_out on-Eden and then-exist | two-+name-donkey
  6  Eve leave inside ~field many year and ~have ~Adam Eve
  7  descendant this-two to-son and firstborn exist Cain and two [?]-end-+name exist
  8  Abel third ~name exist Seth and then-exist
  9  ~Adam from eye-eye blind and then-exist go ~Adam inside Paradise
 10  son of-~Adam and this son exist [Cain] son [Abel]
 11  ~Adam and then-exist say ~Adam carry ~Adam from the_tree_of_mercy.

## 006r — Seth goes to Paradise for the branch

> a branch. And then the branch […] carry anointed through the light; and then by that light anointed, through the eye, blind Adam sees; and Adam was made whole […]. And then Seth went | gate/open to Paradise; and […] to Seth appeared God's angel […] the angel of God [to] Seth […]; and he went […] Seth said: Adam my father. Seth […] went into Paradise | when it was Adam his father. Seth brought from the tree of mercy a branch. […] Adam his father was, through sin; and Adam said, Adam, when seed Seth brought anointed through the light; and then by that light anointed, through the eye, the blind man sees; and Adam was made whole and then. The angel truly spoke; and then the angel went into Paradise, and Seth carried the branch

  1  one ~branch and then-exist branch to-~Adam carry ~place through
  2  ~light and then-exist through ~light ~place through eye see blind ~Adam
  3  and be_healed = ~Adam [sick] and then-exist Seth go | [to_Paradise]
  4  gate/open Eden and then-~exist Seth appear God
  5  angel and_then God angel Seth [answered] and go one say Seth
  6  from-father ~Adam Seth SUBJ go inside Eden | then
  7  exist father ~Adam carry Seth from the_tree_of_mercy branch
  8  on-+the_tree_of_mercy SUBJ exist father ~Adam commit sin and say ~Adam
  9  ~Adam then-exist seed carry Seth ~place through
 10  ~light and then-exist through ~light ~place through eye see blind ~and
 11  be_healed = ~Adam and_then angel righteous SUBJ speak and then-exist
 12  go angel inside Eden and Seth carry branch

## 006v — the branch brought home, and a city

> out of Paradise, from tree […] Adam was, through sin. And then […] the angel gave(?) this branch; and then the branch […] he carried […] to his father Adam. And then […] he went into a city, and […] the city was […] where Adam was, a house. And then he came [the way] recognize; and within, all from the city [the way] recognize; and […] out of the city one [road]; and then Seth went, this the one Seth met and within [the way] recognize; and then Seth said, one the one Seth met oh […] the Father, the Spirit, the Father recognize Adam. And Adam was blind in both eyes — Adam, who was the Lord God's, cast out out of Paradise by the angel; and then the one Seth met […] the gospel, and they found […] years(?); and

  1  on-Eden from tree on-+tree exist ~Adam through
  2  sin and then-exist among-~exist ~exist ~grab angel this branch
  3  and then-exist branch among-~exist carry to-of-among-~exist father
  4  ~Adam and then-exist among-~exist go inside one town
  5  and believe-end-+name town exist name-[?]-who who exist ~Adam
  6  house and then-exist arrive can [the_way] recognize and inside every from
  7  town can [the_way] recognize and then-~exist out town
  8  one [road] and then-exist Seth exist go this NAME
  9  and inside can [the_way] recognize and then-exist Seth say one
 10  NAME oh of-[?] from-father spirit father SUBJ recognize
 11  ~Adam and ~Adam exist eye-eye blind who ~Adam exist Lord
 12  God out cast_out on-Eden on-angel and then-exist NAME
 13  from-see gospel and find NAME ten-two-two-ten-year and

## 008r — Noah and the ark

> seven And then three at that time the Lord God appeared to Noah; and then and then the Lord God. Noah. The Lord grieved brethren man go away that he had made them, because [flood] he who keeps his commandment. The Lord God would have all destroyed. […] The Lord God [said to] Noah: make one […] the Lord | […] the Lord. It was forty(?) cubits long, and […] broad; and five lift up […] take Noah of every creature two by two; and [inside] of the ark. And then this [dove] the Lord […] the Lord went; and then Noah he took of every creature two by two, and went before the Lord God; and […] the Lord God, to the cup, and to the Lord lose and [drunken] the Lord God; all, two by two, [in every] direction […] and the rain came for forty days; and five the cities were destroyed. The Lord God […]. The angel of God said [to] Elijah: the Lord God was [with] Noah; Noah remain all this [three] was; and the other [sons] departed; and this

  1  seven and then-exist three time appear Lord_God Noah
  2  and then-exist and_then Lord_God Noah sad-Lord year brethren* somebody on-of leave*
  3  create because [flood] this who carry of commandment ~exist Lord_God want every
  4  destroy and_then Lord_God Noah do one exist Lord | [...]
  5  ~exist Lord exist on-two-two-ten cubit long in_turn three_hundred*
  6  broad in_turn five raise one-hide grab Noah* every create two-DISTR-two and
  7  [inside] of-ark and then-exist this [dove] this-Lord this-?Noah go-Lord
  8  and then-exist Noah* grab every create two-DISTR-two and go before Lord_God
  9  and inside-~exist Lord_God to-cup and to-Lord lose* and [drunken]
 10  Lord_God every two-two direction water disperse fifth from_heaven* high
 11  and go rain forty and five town destroy
 12  Lord_God and_then God angel Elijah say exist Lord_God Noah
 13  Noah* remain* every this [three] exist and two [sons] leave and this

## 008v — from Noah to Abraham

> the people were, until Abraham the forefather were pagans believed. From Noah it was, until Abraham […] and then The angel of God to Elijah the prophet: Elijah, within this and that believe. One man was saved in that time. The angel departed from before Elijah the prophet; and this and that he said. Elijah the prophet wrote; and [holy Enoch] […] within one chapter Elijah of the writing.

  1  people exist until Abraham forefather were_pagans* believe
  2  from Noah exist until Abraham seven-[?] and_then
  3  God angel to-Elijah prophet Elijah inside this-and-this
  4  believe one somebody ~be_saved inside time
  5  leave angel before Elijah prophet and this-and-this say
  6  SUBJ write Elijah prophet and [holy_Enoch] prophet.
  7  inside one chapter Elijah* of-write

## 005r — Abraham and Isaac

> […] and the son went [with] the father | the father; and a sheep, and a lamb. […] the son; the father sacrificed and then; the father Abraham, for love of the Lord, […] the Lord God, the offering. Chapter. And then Isaac was tie up […] who was [ram] Isaac [instead] name Abraham sacrificed, and drew out […] […] […] […] Isaac he would slay; and the Lord God cried out from the cloud, by the angel of the Lord God, […] to Abraham […] […] who […] Abraham. The Lord God. Love the Lord. this is peace to the Lord. And then he looked up and saw, Abraham, and saw […] a lamb in a thornbush.

  1  donkey* and go-son-father | son*
  2  father and one sheep and one lamb
  3  who-~exist son father sacrifice and_then father Abraham
  4  from love Lord to-hide-Lord Lord_God offering-chapter and then-exist Isaac
  5  exist tie_up on-+pierce who exist [ram] Isaac [instead]
  6  name Abraham sacrifice and take_out on-+name
  7  understand-girl-chapter sword who Isaac want slay
  8  and shout Lord_God on-cloud on-angel of-Lord_God
  9  leave-leave Abraham-to will SUBJ who this.
 10  Abraham Lord_God love Lord
 11  this_is to-Lord peace
 12  and then-exist from see look_up
 13  Abraham and see
 14  understand-eat ~lamb
 15  on-understand-eat bush

## 005v — the ram, and a prophecy of Christ

> And then he sacrificed the lamb and then; the Lord God from the cloud, by the angel of the Lord, said to Abraham […] within […] A holy [Virgin]; of a virgin shall be born a son […] The son shall be […] Jesus; and the Lord went among the people He preached the gospel, [did] many miracles […] and the Lord suffered crucified; and on the third day rose from the dead. […] the Lord God, by the angel, [to] Abraham; and […] the Lord's chapter is believe truly [in] the Son of the living God; every man is saved […] One man […]; but every man is saved [from] the yoke; and man […] the Lord […] believes; and one […] […] but every man was damned, from Adam onward until Abraham, a hundred years and twenty years; from Abraham [until] Moses began: three thousand and fifty from Abraham until

  1  and then-exist from lamb sacrifice and_then Lord_God on-cloud
  2  on-angel of-Lord Abraham say ~be_born inside of understand-girl-chapter
  3  one holy-Mary from virgin-Mary on-be_born son and_his_name*
  4  son exist ~body Jézus and go Lord among_the_people*
  5  exist gospel preach many who-and-this-and miracle ~do
  6  and suffer Lord crucified and on_the_third_day from die stand_up-Lord
  7  and_then Lord_God on-angel Abraham and from-and-see chapter-Lord exist
  8  believe righteous son living God everybody = be_saved and.
  9  one somebody not_damned but everybody = be_saved yoke and
 10  somebody Lord not believe and one not be_saved.
 11  but everybody = be_damned from ~Adam ~trespass table until Abraham
 12  one hundred-year and ten-ten-year from Abraham SUBJ table [until]
 13  Moses ~begin-+three_thousand and fifty from Abraham until

## 015r — David the king

> afterward David the king humbled himself before […] The king began his repentance afterward anointed the king […] have mercy; and the king's sin — have mercy. At that time there appeared to the king the angel of God […]; the angel of God [to] David the king: the Lord God. The king sin, have mercy. The king keeps the Lord's commandment; and the Lord confirmed the king […] upon the king's throne; and the king proclaimed [it to] the people. Chapter. [the Lord] there shall be born say a son [of David]; the son shall be the Son of God. And the angel departed from before David […] From David the king until the Virgin Mary […] […] and […] and one […] […] […] and one […] | six(?) […] and five from David the king until the Virgin Mary

  1  ~do David king humble against Lord_God.
  2  repentance begin king ~do anointed king Lord_God.
  3  have_mercy and sin king have_mercy time appear king
  4  God angel and_then God angel David king Lord_God
  5  king SUBJ sin have_mercy carry-king of-Lord commandment and
  6  confirm-Lord king SUBJ on-of-king throne and announce king people-chapter
  7  [the_Lord] on-be_born host say son [of_David] son exist son
  8  God and leave angel before David king.
  9  from David king until virgin-Mary be_born-~year
 10  ~out-~begin-to-[?] and [?]-hundred-~year and one hundred-~year
 11  ~out nine_hundred and one hundred-~year | two-two-two
 12  ten-~year and five from David king until virgin-Mary

## 015v — the count of years

> the birthday: from Adam onward until the Virgin Mary | was born, years: five thousand and one hundred years and fifty and four years, and four years.

  1  be_born-~year from Adam ~trespass ~out until virgin-Mary | be_born
  2  day five_thousand and one hundred-~year and fifty
  3  and two-two-year and two-two-year

## 016r — Saint Luke

> Saint Luke writes; the sixth(?) […] of his writing; from […] […] exist […] they gave thanks, and prayed to the Lord God.

  1  write holy-Luke six-throne of-write from remain* kiss.*
  2  exist* holy-in_turn-+one-[?] give_thanks = and pray to-Lord_God

## 016v — Joachim's offering is refused

> And Saint Anne […]; of the two of them, all their rich substance […] part one portion they took the people of the temple; and a second portion to the Lord way to the people. third a portion […] […] And all Joachim's household gave thanks to the Lord God; and […] | his household coming thirty years; and he prepared the offering. […] all […] […]; and then, and from Joachim he brought his offering; and at Joachim looked the chief of the Jews. […] This chief of the Jews [said to] Saint Joachim, […] to this Joachim […] who was […] go among the […] […] of the offering […] one […] and out Joachim cast out at this. And sorrowfully Joachim departed, and went into the field, into the wilderness […] and from […] […] and at one […] one

  1  and holy-Anne mouth-~year from-two from_both every of-rich soul on-+three part
  2  one division grab the_people_of_the_temple on-exist-chapter in_turn-two division
  3  from-Lord way people-chapter third division Joachim-+one-+his_household living.
  4  and every Joachim's_household thanks to-thanks Lord_God in_turn have | Joachim
  5  his_household ~be_born thirty year and prepare offering-chapter
  6  exist-chapter every of-in_turn-+one-[?] ~sheep and then-exist and from Joachim
  7  carry of offering and to-Joachim see from head
  8  Jew and_then this high_priest = holy-Joachim
  9  food this-Joachim [the_temple] who-exist Joachim* go
 10  among of answered-year food of offering [the_temple] one [portion]
 11  and out Joachim cast_out on-this exist-chapter and sad
 12  Joachim leave and go inside field inside forest chapter-of from love-exist-to
 13  and from rejoiced love-exist-to and on-one mount one

## 017r — the angel comes to Joachim

> a lamb sacrifice; and then the lamb sacrifice [rejected] At that time, when Joachim was appear God [in the desert] […] the angel of God [to] Joachim […] hear […] […] […] the angel of God [to] Joachim, this […] The Lord God has had mercy. Go home, Joachim; and at the golden gate — this Joachim departed — Joachim's wife Anne, and conceived a virgin maiden. And then coming and [shall conceive] The virgin maiden shall be Mary; and Mary shall bear a son whose The son shall be […] Jesus; and the Lord went among the people He preached the gospel, did many miracles, and suffered, the Lord crucified; and on the third day rose from the dead; and ascend shall be saved, every wide world; and the man who believes in the Lord. And the angel departed from before Saint Joachim; and at that time the angel appear

  1  lamb sacrifice and then-exist lamb sacrifice [rejected]
  2  time then-exist Joachim exist appear God [in_the_desert]
  3  and_then God angel Joachim have hear [the_Lord_God]
  4  of-~pray and_then God angel Joachim this [hath_had_mercy]
  5  Lord_God have_mercy go Joachim to-home and on-golden
  6  gate this Joachim leave of-Joachim wife Anne and conceived*
  7  one virgin-girl and then-exist ~be_born and [shall_conceive]
  8  virgin-girl exist Mary and remit Mary on-be_born son whose.
  9  son exist ~name Jézus and go-Lord among_the_people.*
 10  exist gospel preach many who-and-this-and miracle do and suffer
 11  Lord crucified and on_the_third_day from die stand_up-Lord and ascend* be_saved
 12  every wide world* and somebody Lord exist believe and leave angel
 13  before holy-Joachim and time then-exist angel appear

## 017v — the golden gate, and Mary carried nine months

> the angel of God [to] Saint Anne: […] this Anne, […] the Lord God has had mercy, has heard the Lord God, Anne's […]. Go home, Anne; and at the golden gate Anne came to(?) the Lord's Joachim; and there was conceived a virgin maiden. And then was born in the body the virgin maiden — she is Mary; and Mary shall bear a son and his name; the son shall be, in the body, Jesus; and the Lord went […]; he preached the gospel, [did] many miracles; and the Lord suffered crucified; and on the third day from death the Lord rose; and ascend is saved, every wide people; and the man who is the Lord's believe. And the angel departed from before Saint Anne; and there was conceived the blessed Virgin Mary. And Mary carried the child nine months, and in the tenth the child was born; and this […] two months; and […] […]; and at six years from Adam onward until the Virgin Mary was conceived and born: five thousand and one hundred and fifty and

  1  God angel holy-Anne have this Anne SUBJ Lord_God have_mercy hear
  2  Lord_God of-Anne ~pray go Anne to home and
  3  on-golden gate leave Anne of-Lord Joachim and from-conceive one
  4  virgin-girl and then-exist be_born body virgin-girl exist Mary
  5  and remit Mary be_born son and_his_name* son exist and-body
  6  Jézus and go Lord among_the_people* exist gospel preach many who-and-this-and
  7  miracle do and suffer Lord crucified and on_the_third_day from die
  8  stand_up-Lord and ascend* be_saved every wide people* and somebody Lord exist
  9  believe and leave ~angel before holy-Anne and from-conceive happy
 10  virgin-Mary and from Mary foetus carry nine moon in_turn ten foetus be_born and this
 11  out two moon and on-out five and on-six-year-to
 12  ~out from Adam ~trespass until virgin-Mary conceive and on-be_born.
 13  five_thousand and one hundred and fifty and

## 018r — Gabriel: Hail, full of grace

> […] months, until the offering […] the blessed Virgin Mary. And then Mary was within […]; from the beginning she withdrew(?) into […] […] and said […] that Mary would keep her virginity | Mary heart. O! O! Amen. And then Mary was […] […] and […]; and at that time God the Father in heaven, because he saw […] all […] darkness […] and at that time God the Father in heaven, and […] the Lord's angel Gabriel […] to the blessed […] Saint Luke writes chapter in his writing: at that time the angel said, Gabriel: Hail, thou virgin, maiden full of grace! The Lord God is with Mary and then This virgin maiden: How shall this be? exist this maiden know this maiden […] this maiden would keep her virginity […] O! O! Amen. […] the angel Gabriel [to] Mary:

  1  ~begin-ten moon until offering inside chapter-year-chapter blessed^ virgin-Mary
  2  and then-exist Mary exist inside three_days from begin go-hide-this inside exist-chapter
  3  [?]-+one and say [?]-+one this-Mary want virgin-carry | of
  4  Mary heart chapter-oh chapter-oh amen and then-exist Mary
  5  exist six-six feast and [?]-+three_days and time from-gate
  6  from-God_the_Father heaven because see hide every world darkness sky.
  7  and time from-gate from-God_the_Father heaven and go.
  8  of-Lord angel Gabriel inside exist-chapter to-happy the_Virgin_Mary*
  9  write holy-Luke chapter* of-write time say angel
 10  Gabriel healing this-virgin-girl have_mercy-girl out Lord_God-Mary and_then
 11  this virgin-girl how? this exist can this-girl know this-girl
 12  ~begin-be_damned this-girl want virgin-girl carry of-girl heart-[?]
 13  chapter-oh chapter-oh amen and_then angel Gabriel Mary

## 018v — the Holy Spirit, and Elizabeth six months gone

> […] the Holy Spirit shall come upon thee, and grace to all […] This maiden shall conceive a son; and the son shall be called shall be […] and then the Virgin Mary blessed […] said this; and blessed would from […] this [power] the Lord, this overshadow; and then the maiden [answered] the Virgin Mary; the word of command to the Lord; Mary […] this […] which maiden the angel said; at this he said […] God the Father, the Virgin Mary | the Holy Spirit; and to the Lord [came upon] one the Lord Jesus Christ came; the Lord was conceived, Christ. And then [departed from] the Virgin Mary and then the angel Gabriel [to] Mary: Behold, thy kinswoman is six months gone | […] who conceived […] Mary; the son, Saint John […] within the chapter […] […] chapter; the Lord God's mercy to this […]; from John shall be the way made [for] the Lord Jesus Christ, that is the Lord […] this Mary bore; and the Lord went forth […]; he preached the gospel

  1  have want to-girl this go holy-spirit to-every have_mercy [full_of_grace]
  2  this-girl conceive son and ~son ~body exist Jézus.
  3  and_then virgin-Mary blessed one-to this say and blessed want from Lord_God.
  4  this [power] SUBJ Lord this overshadow* ~and then-exist girl [answered.]
  5  virgin-Mary commandment word to-Lord-hide Mary hide this overshadow* who girl
  6  exist angel say on-this say pour_out God_the_Father virgin-Mary | holy
  7  spirit in_turn to-Lord [came_upon] one go Lord-Jézus-Christ from-conceive Lord
  8  Christ and then-exist [departed_from] virgin-Mary and_then angel Gabriel
  9  Mary have lo out six month^ of-girl relative | holy-+name-chapter
 10  Elizabeth who conceive Mary son holy-John [barren] inside chapter SUBJ
 11  go chapter Lord_God of have_mercy to-this have from John exist way
 12  do Lord-Jézus-Christ that_is Lord [according_to_thy_word] this
 13  Mary be_born and from Lord go Lord on-+world exist Word^ preach

## 019r — Joseph

> […] many miracles […]; and the Lord suffered [under] the Jews crucified; and the man who is the Lord's believe truly the Son of the living God — every man be saved; and one man is damned; and the Lord not believe; and one be saved but who believes not a man is damned. Here ends this holy gospel. And at that time the angel was appear; the angel of God the aged Joseph and then the angel of God very old Joseph. Go, aged one Joseph within […] […] to Mary; and this […] Joseph was [already] aged […] of the son, well-pleasing, from Mary […]; and then the son shall be born […]; the son shall be Jesus; and the Lord went forth among the people; he preached the gospel preach, did many miracles, and the Lord suffered [death]

  1  who-and-this-and miracle ~do and suffer Lord Jew
  2  crucified and somebody to-Lord exist believe to righteous
  3  son living God everybody = be_saved and one somebody
  4  be_damned to and Lord not believe and one to
  5  be_saved but who_believes_not* somebody be_damned here_ends this holy_gospel
  6  and time then-exist angel exist appear God angel
  7  aged Joseph and_then God angel aged
  8  Joseph go aged Joseph.
  9  inside exist-chapter Joachim* to-to Mary and this aged.
 10  Joseph exist [already] aged Joseph-+cross-girl-+mouth
 11  from son to-pleasing from Mary on-~be_born and then-exist ~son on-be_born
 12  and-~body ~son exist Jézus and from Lord go among_the_people* exist
 13  gospel preach who-and-this-and miracle do and suffer Lord [death]

## 019v — the census of Augustus

> [under] the Jews […]; and the man who believes in the Lord […] truly the Son of the living God — every man is saved; and one man is damned; and the Lord not believes; and one be saved but who believes not a man is damned. Here ends this holy gospel. And then the blessed Virgin Mary was sixteen years old […] There was a decree, before […] the Lord Jesus Christ, twenty and | two years; and […] one year [before] the Lord Jesus Christ […] At that time Augustus the emperor commanded that all people should be counted. And then law Augustus […] all […] went back […] and | when it was, the two of them, Mary and aged Joseph, went | home And then the two, Mary and aged Joseph, took one ox and one

  1  Jew crucified and somebody to-Lord exist ~believe to.
  2  righteous son living God everybody = be_saved and first^
  3  somebody be_damned to and Lord not believe and first^
  4  to be_saved but who_believes_not* somebody be_damned here_ends this holy_gospel
  5  and then-exist out happy virgin-Mary ten-six-year time.
  6  exist commandment before ~be_born Lord-Jézus-Christ ten-ten and | two
  7  two-year and on-~be_born first^ day^ Lord-Jézus-Christ and.
  8  time command Augustus emperor because
  9  all^ people* exist enrol and then-exist law Augustus
 10  emperor all^ world* back go law in_turn-chapter-in_turn and | then
 11  exist and from two Mary aged Joseph go | to
 12  home* and then-exist two Mary aged Joseph
 13  exist grab first^ ox and first^

## 020r — no room, and a manger

> donkey; because this they took, aged Joseph the ox, the two of them — aged Joseph and Mary exist remain [together] the two of them, the aged […] remain and the donkey was aged Joseph's; he took her who would bear this son | Mary and aged Joseph carried her on the donkey; and then […] aged Joseph, when he arrived | the aged Mary and Joseph, [at] Bethlehem town; and […] […] Mary and aged Joseph […] found none; but the two of them, Mary and aged Joseph, lodged in a barn; and [manger] […] a manger; and then bought […] Joseph hay; and then the ox

  1  donkey because this exist grab aged Joseph
  2  from ox who two aged Joseph Mary
  3  exist remain* [together] who two aged Joseph.
  4  remain* exist in_turn donkey exist aged Joseph
  5  grab who this son on-be_born want | aged-Mary
  6  Joseph on-donkey from-carry and then-exist two.
  7  aged Joseph exist from arrive | aged
  8  Mary-Joseph Bethlehem town and [arrived]
  9  can aged-Mary-Joseph room find
 10  but leave two aged-Mary-Joseph inside first^
 11  barn and [manger] aged-?Joseph-Mary-+mouth.
 12  first^ manger and then-exist buy aged.
 13  Joseph hay and then two ox

## 020v — the birth, the star, and the angel's news

> and the donkey; he laid the hay; and then the aged | […] a fire began to give light; and then, over his shoulder […] in the night the son was born; and the son was […] Jesus. At that time sky star light through Bethlehem town; and then a star was seen […]; and from […] […]; and then at the star, a miracle. At that time the angel said […] […] joy! A king is born, a king born in Bethlehem town, within barn, in a donkey's manger. […] the donkey […] hay within […] […] Christ, Mary's son. And then […] went [to] Bethlehem; and then rejoiced knelt down, and every one of them knelt before the shepherds [hastened] to go another and […]

  1  donkey exist hay put and then-exist aged | Joseph*
  2  girl-+mouth ~fire begin-light ~and then-exist shoulder-to begin.
  3  night time on-be_born son and son exist
  4  and-~body Jézus time then-exist sky star
  5  through bright^ Bethlehem town and then-exist star
  6  see the_shepherds and from rejoiced love-exist-to and then-exist
  7  on-star miracle time say angel understand-chapter great
  8  joy be_born king king SUBJ be_born inside
  9  ~Bethlehem town inside barn inside donkey manger
 10  [ox] donkey love hay inside [manger] [laid]
 11  Christ Mary son and then-exist the_shepherds go Bethlehem
 12  and then-exist rejoiced kneel and every this exist kneel
 13  before from the_shepherds [hastened] to go another and to-Lord.

## 021r — the reckoning of years

> gave thanks, and gave thanks. Here ends this holy gospel [amen] Saint Luke writes, in one [then] of his writing, chapter [of the book] [the reading] from Adam onward until the birth of the Lord Jesus Christ. five thousand and one hundred years and sixty years and six years, until the birth of the Lord Jesus Christ.

  1  thanks and give_thanks = here_ends this holy_gospel [amen]
  2  write holy-Luke inside one [then] of-write chapter [of_the_book] [the_reading]
  3  out from Adam ~trespass until be_born Lord-Jézus-Christ.
  4  five_thousand and one hundred-year and sixty
  5  and six-year until be_born Lord-Jézus-Christ

## 021v — the flight into Egypt, and the eighth day

> At that time, in the year the Lord Jesus Christ was born three days at that time the angel said […] to the aged […] Rise up, and take this son and his mother(?), this son […] and flee into Egypt. And they went, all of them, beginning [by night] out of Egypt [into] this; the angel [appeared] said day [Herod] Here ends this holy gospel. At that time he rose up […] | [arise] and took the Lord Jesus Christ and his mother, and five the year […] when […] | […] they went into Jerusalem […], that is, when was born the Lord Jesus Christ. On the eighth day the son was circumcised, and the son was named Jesus. And this Lord Jesus first man shed his blood; and then […] the Lord Jesus was circumcised in Jerusalem. Chapter. And they fled Mary his mother the Holy Spirit and Joseph

  1  time then-exist to-to-year on-be_born Lord-Jézus-Christ three_days
  2  time say angel understand-chapter aged Joseph
  3  stand_up up and take^ this son and of this son mother.
  4  and escape inside Egypt-to and go every this begin [by_night]
  5  out-out Egypt [into] this this angel [appeared] say day [Herod] end
  6  this holy-gospel time stand_up up the_aged | Joseph
  7  [arise] ~and take^ Lord-Jézus-Christ and of mother and five
  8  day^ out then-exist | [the_son_and_the_aged_Joseph_and_the_holy_mother_Mary]
  9  ~year-+Joseph-chapter go inside Jerusalem ~town that_is on-be_born
 10  Lord-Jézus-Christ on-six-two-year time circumcise son
 11  and son exist and-from-~year-exist-+name Jézus and this Lord-Jézus first
 12  man* of-Lord blood shed and then-exist Lord.
 13  circumcise Lord-Jézus inside Jerusalem exist-chapter and escape
 14  Mary_his_mother_the_Holy_Spirit_and_Joseph*

## 022r — Egypt, and the twelve

> into the land of Egypt; and [dwelt]; and the Lord went Joseph in the land of Egypt, into every city [idols] […] […] the evil ones pierced and pierced; and | […] [arise] died. From Joseph they remained in Egypt twelve years, at that time the angel Gabriel said Joseph Flee into the land of Egypt, into Nazareth city. And […] they remained Nazareth [in that] city twelve years; and […]; and this […] […] years. Here ends this holy gospel. One […] He called twelve apostles; and […] […] and | many miracles afterward: the blind eye the Lord, through light; the dead the Lord resurrect the evil among the people […]

  1  inside Egypt earth and [dwelt] and go Lord Joseph
  2  on-Egypt earth inside every town [idols] hell.
  3  fall* evil pierce-pierce and | [?]-mother-?Joseph.
  4  [arise] die from Joseph leave-leave inside Egypt six-six-year
  5  time say ~Gabriel angel Joseph.
  6  escape on-Egypt earth inside Nazareth town
  7  and [?]-mother-+Joseph-chapter leave-leave Nazareth.
  8  town six-six-year and five and this [returned] table
  9  ten-ten-two-nine-year here_ends this holy_gospel one
 10  day call six-six apostle and three_days preach and | who-this
 11  and-this miracle ~do eye blind SUBJ Lord through
 12  light die SUBJ Lord resurrect evil inside people to-+who-[?]

## 022v — the signs, numbered

> First, that is, the Lord made wine water that is the Lord broke five loaves bread […] the people. The fourth sign the Lord Jesus showed, when | […] he raised up from […] a son […] the sign the Lord Jesus showed, when he raised up lose in Jerusalem. The sixth sign the Lord Jesus showed in […] […] when the Jews brought a sick man before the Lord Jesus: a sick man, and a sick man, and a sick man, and a paralytic; and the sick, the sick, the sick, the paralytic — the Lord Jesus healed […] The sign the Lord Jesus showed in Capernaum, when he healed alive the servant of a soldier; and was named […] the centurion The eighth sign the Lord Jesus showed in Tyre […] to a woman […]

  1  before that_is SUBJ Lord wine create-Lord water on-that_is SUBJ Lord
  2  break five loaves bread five-?thousand people
  3  in_turn-two-two can show Lord-Jézus then-exist | in_Nain.
  4  before in_turn-to-in_turn resurrect from virgin-~woman son fifth
  5  can show Lord-Jézus then-exist resurrect to-to lose*
  6  within^ Jerusalem in_turn-six can show Lord-Jézus within^ first^
  7  in_turn-chapter-in_turn then-exist Jew keep^ first^ ill
  8  before Lord-Jézus sick_man and sick_man and sick_man and paralytic
  9  and sick_man sick_man sick_man paralytic heal Lord-Jézus in_turn-+seven
 10  can show Lord-Jézus within^ Capharnaum because raise_from_the_dead =
 11  two servant first^ soldier and was_named* soldier.
 12  exist the_centurion in_turn-six-two can show Lord-Jézus
 13  within^ Tyrus in_turn-chapter-in_turn to-to first^ ~woman head

## 023r — the ninth, tenth and eleventh signs

> a pagan; and within her was a devil; and […] he cast it out […]. The ninth sign the Lord Jesus showed in | a proud man paralytic because the man […] did. The tenth sign the Lord Jesus showed in […] a king's son, because he was at the point of death; and the son […] afterward The eleventh sign the Lord Jesus showed in Jerusalem: the evil spirit, when the Lord [cast] out of a man a devil […] First, before the birth of the Lord Jesus Christ, the Son of God cannot a prophet, a forefather, this […] afterward he is Christ afterward; and by miracle they confessed that the Lord Jesus is truly the Son of God. five confessed […] the Lord Jesus that the Lord Jesus is truly the Son of God. First confessed […] the Lord Jesus […] and Elijah. Secondly confessed

  1  one pagan and inside to-to exist devil = and evil^
  2  out to-+who-[?] in_turn-nine can show Lord-Jézus inside | exist.
  3  proud on-one paralytic man^ because man^ healing.
  4  do in_turn-ten can show Lord-Jézus inside apostle-oh-DIV-chapter
  5  one king son because exist on-die and son healing.
  6  ~do in_turn-and can show Lord-Jézus inside Jerusalem evil^
  7  then-exist Lord inside one man^ devil = exorcise
  8  first before be_born Lord-Jézus-Christ son God cannot.
  9  one prophet one forefather this miracle.
 10  ~do he_is* Christ ~do and miracle confess
 11  that Lord-Jézus righteous son God five confess ~have.
 12  Lord-Jézus that Lord-Jézus righteous son God first confess
 13  ~have Lord-Jézus Moses and Elijah in_turn-two confess

## 023v — who confessed him, and the Transfiguration

> […] the Lord Jesus; God the Father, the Lord's […]. Confessed the evil ones, that the Lord Jesus is truly the Son of God. Fourthly confessed the Lord Jesus — the angels […] the Lord Jesus is truly the Son of God. They confessed […]; and the earth, the sun, the moon that the Lord Jesus is truly the Son of God; and all this […] that the Lord Jesus is truly the Son of God. First confessed it Saint Peter, Moses and Elijah. Saint Luke writes that when the Lord Jesus was thirty years, at that time the Lord Jesus went […] [to] Mount Tabor with his apostles; and he was transfigured; and the apostles saw Moses and Elijah white […] and they saw the light […]; and then there stood | the Lord Jesus, and Moses and Elijah; and then the apostles, through fear, fell down [fell]; and then the apostles […]

  1  ~have Lord-Jézus from-God_the_Father of-Lord third confess devil =
  2  that* Lord-Jézus righteous son God in_turn-two-two confess ~have
  3  Lord-Jézus angel that Lord-Jézus righteous son God fifth
  4  confess sky and earth sun and.
  5  moon that Lord-Jézus righteous son God and this every confess.
  6  that Lord-Jézus righteous son God first confess holy-Peter
  7  Moses and Elijah write holy-Luke then-exist
  8  Lord-Jézus inside thirty years* time go Lord-Jézus on.
  9  Tabor and of disciple^ and be_glorified ~and
 10  see disciple^ Moses and Elijah white who-+name-believe-year
 11  and see bright^ [from_heaven] and then-exist from-leave-leave | Lord
 12  Jézus and Moses and Elijah and then-exist disciple^ through
 13  take_fright and down [fell] bow and then-exist disciple^ voice.

## 024r — Tabor and Carmel, and the baptism

> heard this word spoken [beloved] of the Son; and the Father mouth [voice] […] and then home [alone] not the apostles, and not every […] but to the Lord Jesus. Here ends this holy gospel. Secondly confessed […] the Lord Jesus, God the Father: first on Mount Tabor, secondly on Mount Carmel. Because when the Lord Jesus was thirty […], at that time the Lord Jesus went baptize Saint John […] to Mount Carmel; and then the Lord went | [to] Saint John. The Lord Jesus said: John […]. The Lord said | Saint John: Master, and […] [came] baptize. And the Lord Jesus said, John baptize the Lord; and […] is baptize Saint John baptize baptized the Lord Jesus, when the Lord was thirty years old; and appear the Holy Spirit

  1  hear this word say [beloved] of son and father mouth* [voice] spoon-+name
  2  and then-exist home [alone] not apostle and not every see.
  3  but to-Lord-Jézus here_ends this holy_gospel in_turn-two confess
  4  ~have Lord-Jézus from-father of-Lord first on-Tabor
  5  in_turn-two on-Carmel to-mount because then-exist Lord-Jézus inside thirty
  6  one-~year time go Lord-Jézus understand baptize holy-John
  7  baptize on-Carmel to-mount and then-exist Lord go | to
  8  holy-John say Lord-Jézus John baptize Lord say | holy
  9  John Master and this-~John [came] baptize and say Lord-Jézus
 10  John baptize Lord and mouth-~John exist baptize.
 11  holy-John baptize see-baptize Lord-Jézus then-exist
 12  to-Lord inside thirty year and appear holy-spirit

## 024v — the dove

> in the form of a dove and then: This is the Lord's Son. he who the Spirit came to rest; and the Lord took the Holy Spirit; and the Lord went into field […] the Lord Jesus […] years […] confessed

  1  inside ~form dove and_then this-Lord of son
  2  he_who spirit grow_calm and Lord grab
  3  holy-spirit and Lord go inside field
  4  to-[?] Lord-Jézus ten-two-two-year third confess

## 025r — the devils confess him

> the devils that the Lord Jesus is truly the Son of God. Because when the Lord Jesus was thirty years old, at that time the Lord Jesus went into | […] […]; and then he went into […]. At that time a man knelt down before the Lord Jesus, and then the Lord; the man have one son; and […] a devil [cast out]. The man's son — his apostles son could not heal him. that He begged the Lord to heal this man's son. Said the Lord Jesus: have mercy [lunatic] the son […] […] And then the son came before the Lord Jesus; and […] he was made whole; and this three confessed — the devils that the Lord Jesus is truly the Son of God, because by miracle they confessed. Fourthly confessed […] the Lord Jesus — the angels, at the birth of the Lord Jesus Christ. Because when the Lord Jesus was born [in] Bethlehem

  1  devil = that Lord-Jézus righteous son God because exist
  2  Lord-Jézus inside thirty year time go Lord-Jézus inside | exist
  3  [afterward] in_turn-chapter-in_turn and then-exist go inside Capharnaum time
  4  then-exist kneel one man^ before Lord-Jézus
  5  and_then Lord mouth man^ have one son and inside-+SUBJ
  6  devil = [cast_out] man^ son of disciple^ to-hide-to son can
  7  heal that* ask heal this Lord of-somebody son say
  8  Lord-Jézus have_mercy gain [lunatic] son can from-~year healthy_man^
  9  and then-exist son go before Lord-Jézus and ~way.
 10  be_healed = and this three confess devil = that
 11  Lord-Jézus righteous son God because miracle confess in_turn-two-two
 12  confess have Lord-Jézus angel on-be_born Lord-Jézus
 13  Christ because then-exist Lord-Jézus be_born Bethlehem

## 025v — the Nativity told again

> town; and first, before the birth, one saying was […] a star, light through Bethlehem town; and | then the star was seen sons; and from rejoiced […] and then at the star, a miracle. At that time the angel said [shepherds] great joy! A king is born, a king born in Bethlehem town, in a barn, in a donkey's manger [ox] the donkey, in the hay, in […] […] Christ, Mary's son. And | then […] […] they went [to] Bethlehem; and […] […] knelt down, and every one of them knelt | and [and then] from sons [hastened] to go another and [the Most High Lord] gave thanks, and gave thanks. Here ends this holy gospel. […] confessed […] the Lord Jesus […]

  1  town and first before be_born one saying exist
  2  sky star through light Bethlehem town and | then
  3  exist star see shepherd and from rejoiced who-before.
  4  and then-exist on-star miracle time say angel [shepherds]
  5  great joy be_born king king SUBJ
  6  be_born inside ~Bethlehem town inside barn inside donkey
  7  manger [ox] donkey inside hay inside
  8  [manger] [laid] Christ Mary son and | then
  9  exist* shepherd go Bethlehem and then-exist.
 10  rejoiced kneel and every this ~exist kneel | ~exist
 11  [and_then] from shepherd [hastened] to go another and
 12  [the_Most_High_Lord] thanks and give_thanks = here_ends this holy_gospel
 13  fifth confess ~have Lord-Jézus sky

## 026r — the earth quakes

> and the earth, to the Lord […] and the moon, because because when the Lord Christ crucified the earth quaked, the rocks and the stones split.

  1  and earth to-Lord-year and moon because
  2  because then-exist Lord-Christ crucified.
  3  earth quake-rock stone split

## 026v — the sun darkened, and Abraham's confession

> The sun and the moon were darkened; and all tree into the world humbled themselves; and all creation mourn when Christ crucified; and all this five confessed, in sorrow that, that the Lord Jesus is truly the Son of God; and by miracle they confessed that the Lord Jesus is truly the Son of God, because […] miracle […]; and the Lord suffered [under] the Jews […] and […] […] the Lord God […] Abraham | […] came then said. The Lord God said to Abraham by the angel; and this the Lord God said to the blessed Virgin Mary by the angel; and | Saint very old Joseph; and the man who believes in the Lord, that he is truly the Son of the living God — every man is saved; and […] a man is damned; and the Lord not believes; and [perish] one is saved, but […] a man is damned; and | this thus he said. First confessed it Abraham the forefather | This one confessed […]; secondly confessed holy Anne

  1  sun and moon this eclipse and every tree into_the_world* this humble and every
  2  create mourn then-exist Christ crucified and this every five confess
  3  inside-to-sad that Lord-Jézus righteous son God and miracle confess
  4  that Lord-Jézus righteous son God because various.
  5  miracle ~do and suffer Lord Jew crucified
  6  and to-+who-~year the_Lord Lord_God announce Abraham | patriarch
  7  holy-~year arrive then* say exist say Lord_God Abraham on-angel and this
  8  say say Lord_God happy virgin-Mary on-understand-chapter angel and | holy
  9  aged Joseph and somebody to-Lord exist believe
 10  what righteous son living God everybody = be_saved and one.
 11  somebody be_damned to and Lord not believe and [perish]
 12  one to be_saved but who_believes_not* somebody be_damned and | this
 13  and-this say confess first Abraham forefather | on-this
 14  this confess holy-in_turn-+one-[?] on-that_is confess holy_Anne

## 027r — Mary's confession

> the mother, the blessed Virgin Mary. Thirdly confessed the blessed | Virgin Mary. The angel of God said: at that time the Lord was; the Lord God went; the Lord's angel [to] the blessed Virgin Mary, when […] from […] to the house of the Virgin Mary get conceived; and she bore; and [on the eighth] […] and one hundred and sixteen(?) years and five and and […] at that time God the Father in heaven, because he saw […] all people darkness sky. At that time God the Father in heaven; and the Lord's angel Gabriel went […] to the blessed Virgin Mary, and said this and that. Saint Luke writes chapter in his writing; and the man who believes in the Lord, that he is truly the Son of the living God — every man is saved; and one man is damned; and the Lord not believes; and one is saved; but every man

  1  mother happy virgin-Mary on-that_is confess happy | virgin
  2  Mary say angel God time exist Lord go Lord_God of-Lord
  3  angel happy virgin-Mary then-exist ~out from want-year to-house
  4  virgin-Mary conceive and be_born and [on_the_eighth] [?]-~year
  5  and one hundred and six-ten-year and five and and moon.
  6  time from-gate from-God_the_Father heaven because see hide every
  7  people* darkness sky time from-gate from-God_the_Father
  8  heaven and go of-Lord angel Gabriel inside exist-chapter
  9  to-happy virgin-Mary and this-and-this say write holy-Luke
 10  chapter* of-write and somebody to-Lord exist believe
 11  to righteous son living God everybody = be_saved and
 12  one somebody be_damned to and Lord not.
 13  believe and one to be_saved but everybody =

## 027v — Joseph's confession, and "there are not many gods"

> is damned; and thus he said. Confessed it Saint Joseph the aged | [understand] the angel of God said, because the Lord God spoke by the angel Gabriel; and whosoever who is the Lord's believe truly the Son of the living God — every man is saved; and one man is damned; and the Lord […] […]; and | […] […] is saved, but every […] is damned; and | thus he said. The Lord Jesus spoke of his many wounds, when the Lord went | to his death; and then the Lord […] the apostles in Jerusalem. At that time knelt the Lord Jesus before the blessed Virgin Mary; and the Lord Jesus said: there are not many gods but rather one God and then the Lord Jesus […] and the Lord […] […] in the Lord Jesus Christ; and one is saved, but every man is damned; and Mary blessed the Lord Jesus, with all the apostles — the blessed Virgin Mary.

  1  be_damned and this-and-this say confess holy-aged | Joseph
  2  [understand] say angel God because exist say Lord_God on-angel
  3  Gabriel and whosoever* to-Lord exist believe to righteous
  4  son living God everybody = be_saved and one
  5  somebody be_damned to and Lord not believe and | one
  6  chapter to be_saved but every whosoever* be_damned and | this-and
  7  this say say Lord-Jézus on_Maundy_Thursday = then-exist Lord go | on
  8  die and then-exist-Lord ~go-[?] apostle inside Jerusalem time kneel
  9  Lord-Jézus before happy virgin-Mary and say Lord-Jézus is_not
 10  many God but_rather* one God and_then Lord-Jézus
 11  to and Lord not believe inside Lord-Jézus-Christ and
 12  one to be_saved but everybody = be_damned
 13  and Mary bless Lord-Jézus on-every apostle happy virgin-Mary

## 028r — the Passover lamb, and the twelfth sign

> And then Mary kiss the Lord Jesus, the Lord's mother, the blessed Virgin Mary; and then Mary was, and from […] kiss Mary's son the Lord Jesus Christ; and from Mary went the Lord Jesus Bethany the apostles in Jerusalem, because the apostles […] Before the Lord went into Jerusalem, where the apostles [were] at supper […] the apostles prepared a lamb, because at that time was the feast of the Jews, the Passover. this is There began the suffering of the Lord Jesus Christ, Son of God; because the Lord is truly the Son of God. And then the Lord, the Jews crucified; and then the Lord, the apostles, the mother; he was laid in the tomb, and […] rose from the dead. And the | twelfth sign the Lord Jesus showed, when rise from pray the Lord and the apostles appear in Jerusalem; and the thirteenth sign the Lord Jesus showed

  1  and then-exist-Mary exist-Lord kiss Lord-Jézus of-Lord mother
  2  happy virgin-Mary and then-exist-Mary exist and from Mary.
  3  kiss of-Mary son Lord-Jézus-Christ and from Mary from-go
  4  Lord-Jézus Bethany apostle inside Jerusalem because SUBJ apostle exist.
  5  before Lord go inside Jerusalem who-exist apostle to-dinner-to-to eat.
  6  prepare-apostle one lamb because time
  7  holiday exist Jew Easter this_is begin suffering
  8  Lord-Jézus-Christ son God because SUBJ Lord righteous son God
  9  and then-exist Lord Jew crucified and then-exist Lord apostle
 10  mother inside tomb put and on_the_third_day from die stand_up-Lord and from | six
 11  six can show Lord-Jézus then-exist rise*
 12  from pray Lord and apostle appear inside Jerusalem and six-+seven can show Lord-Jézus

## 028v — the Ascension

> when [he ascended] [into heaven] on a mountain, two men and two men exorcise […] and […] and sixteen(?) and six devils and the two men were healed afterward fourteen the sign showed the Lord Jesus; then […] when he went to God his Father | in heaven […]; the Lord sat at the right hand of God the Father.

  1  then-exist [among] [one_another] one mount two somebody and two somebody
  2  exorcise six-?hundred and six-?thousand and six-ten and six devil =
  3  and two somebody healing ~do fourteen can show
  4  Lord-Jézus then Holy_Thursday then-exist leave to-of-Lord God_the_Father | on
  5  heaven ~land from-sit-Lord from-God_the_Father God on-right

## 029r — the Passion begins: "Here begins"

> Here begins the account Passion of a man […] the writing the account [the Passion] [of] Saint Matthew and Saint John, of the Passion | a man […] […] The Lord Jesus went to Bethany to Jerusalem, because […] the Lord […] to the supper […] because […] Before the Lord went, the apostles [went] into Jerusalem […] the Lord Jesus […] to prepare the Passover lamb, where the Lord and the apostles […] should eat. And the Lord [said]: go, you. And then the Lord […] to the apostles in Jerusalem; and the Lord sat down at the table [with] the apostles. At that time the apostles prepared the Passover lamb; and the lamb

  1  begins this begin the_account*
  2  Passion of-somebody heart-Lord
  3  write the_account* cup-not [the_Passion]
  4  holy-Matthew and holy-John
  5  from suffering | of.
  6  somebody heart-Lord time.
  7  go Lord-Jézus to_Bethany
  8  Jerusalem because from far-to-Lord to-dinner-chapter ~do because exist Lord.
  9  before Lord go apostle inside Jerusalem and_then Lord-Jézus exist apostle.
 10  prepare from Easter lamb who-exist Lord apostle to-dinner-chapter.
 11  eat and this-Lord to you go and then-exist Lord go.
 12  to-apostle inside Jerusalem and sit to-throne Lord [with] this-apostle time
 13  exist apostle prepare from Easter lamb and lamb

## 029v — the supper, and the washing of feet

> the apostles brought to the table […] the Lord Jesus […] the Lord's […] lamb the Lord would eat this with you […] lamb. Therefore the Lord asks you: do not, apostles, be offended in the Lord, because the Lord goes to his death — the Lord dies; and the Lord | […] […] […] and the Lord […] you […] and […] the Lord Jesus [rose] from the table, and laid aside | the Lord, his […] and then. The Lord Jesus, one apostle among […] the apostles, and among seven the apostles, and […] an apostle [named …] brought a bucket […] and a washing-dish; and then water into the dish he poured; and the Lord Jesus came to Saint Peter, and […] brought the water in the dish, which the Lord Jesus and then Saint Peter.

  1  carry apostle on throne and_then Lord-Jézus brother of-Lord from
  2  lamb* want Lord to you eat this Passover^
  3  lamb therefore ask-Lord you do_not apostle
  4  inside Lord take_offence^ because this-Lord go on-die Lord die and this-Lord | on
  5  three_days again* rise-Lord and this-Lord you appear
  6  and rise to-throne Lord-Jézus and take_off-Lord | on
  7  Lord of-Lord ~ask-~exist and_then Lord-Jézus one apostle
  8  among seven-ten apostle and among seven apostle and ~body
  9  apostle exist Titus-in_turn carry one bucket water
 10  and one washdish and then-exist water inside washdish
 11  pour and go Lord-Jézus to holy-Peter in_turn Titus-in_turn
 12  carry inside washdish water this-who Lord-Jézus and_then holy-Peter

## 030r — Peter objects

> Master not let Peter brethren the Lord with washes my feet? and then the Lord Jesus with if the Lord […] the feet washed […] […] [part] within heaven […] and then […] Master sky Peter, this […] trespass; the Lord, the sufferer […] […] […] […] the Lord in heaven […] | […] the Lord took [hands and] […] washed; and all […] […] he washed; and | then with the Lord washed their feet; and the feet garment towel and the two of them from go away among the apostles, every one he washed; and the feet garment [wiped] and the Lord Jesus took […] his […] and

  1  Master not_let this-Peter brethren* this-Lord with* foot wash
  2  and_then Lord-Jézus with* if this-Lord this-?with foot
  3  wash understand-+one this-cut_off-[?] [part] inside heaven ~land
  4  and_then holy-?with Master sky* this-Peter this
  5  love-to-+high-[?] trespass this-Lord sufferer brethren-to-+high-[?]
  6  with* cut_off-?be_born [part] this-Lord inside heaven ~land | love-cut_off.
  7  this-?with this-Lord grab-cut_off-to [hands_and] head.
  8  wash and every of-?with ~body wash and | then
  9  exist with* SUBJ foot exist-Lord wash and foot
 10  SUBJ garment* towel and two from leave apostle middle every
 11  wash and foot SUBJ garment* [wiped] and
 12  grab Lord-Jézus on-Lord of-Lord believe-~exist and

## 030v — the bread, and the cup with water and wine

> The Lord Jesus sat at table with the apostles and then; the Lord Jesus looked the apostles […] see how the Lord […] you […] from […] and you shall eat […] […]; and took the Lord Jesus […] one baked loaf, and blessed the Lord Jesus this bread and bread the Lord set it before them; and the Lord Jesus took wine in a cup, and poured water into the cup; and blessed the Lord Jesus, the wine and the water; and the wine and water the Lord Jesus set before them and then the Lord Jesus; and […] whoever eats of this […], that man shall be | the Lord's shall be called […]; and the man who exist this bread

  1  sit Lord-Jézus to-throne to-apostle and_then Lord-Jézus see SUBJ apostle
  2  to-Lord see how? this-Lord you pray from rather*
  3  and you understand-eat two pray and grab
  4  Lord-Jézus inside why?-in_turn one baked cake
  5  and blessed Lord-Jézus this bread and bread
  6  before Lord put Lord-Jézus and grab Lord-Jézus
  7  wine one cup and water inside cup pour and blessed
  8  Lord-Jézus wine and water and wine water
  9  before Lord put Lord-Jézus and_then Lord-Jézus and somebody.
 10  exist this bread eat this somebody exist | of
 11  Lord ~body ~eat and somebody exist this bread

## 031r — one of you shall betray me

> eats and believes in the Lord […]; every man is damned […] and the man who believes in the Lord and is from […] they ate the holy Host […] drank […] that man shall live. O! O! Amen. and then The Lord Jesus know: one among you and […] the Lord […] one of the apostles shall betray him. And the apostles looked among the apostles, saying […] Master who is it and […] the Lord Jesus said; and [leaning] [breast] the Lord Jesus with and John, and said: O […] […] […] Master, who is it? And then he leaned […] upon the Lord Jesus […] Master | thus said the Lord Jesus to whom; the Lord took a morsel

  1  eat and Lord believe everybody = be_damned cut_off-[?]
  2  and somebody exist Lord believe and exist from
  3  thirty holy-host eat and drink every.
  4  somebody exist living chapter-oh chapter-oh amen and_then
  5  Lord-Jézus know* SUBJ one among you
  6  and [?]-+SUBJ Lord name-+one from apostle betray and see-apostle among
  7  apostle say holy-?with Master who_is_it and struck-to.
  8  say Lord-Jézus and [leaning] [breast] Lord-Jézus
  9  with* and ~John and say oh of-?with ~brother
 10  from-judge Master who_is_it? and then-exist lean_on
 11  holy-~John on-end Lord-Jézus and_then Master | name-+one.
 12  this-and-this say Lord-Jézus to_whom this-Lord give^ bite

## 031v — Satan enters into Judas

> […] It is he. And then […] […] upon the Lord Jesus; and he took this […] Nicodemus and see the Lord Jesus [the morsel] this bread And then bread Judas Iscariot took; and then bread Judas were opened In that place the devil entered into Judas. […] the Lord Jesus; the apostles weeping […]; and he took this […] the Son of God […] the Lord Jesus. Judas did […] did; and then evil the apostles, how he said: Master, speak. But the apostles did not understand what Judas said. bread bought […] shepherd […] because […] the apostles […] because this was the Jews' Passover.

  1  bread so_it_is and then-exist sleep holy-~John
  2  on-end Lord-Jézus and give^ this Lord-Jézus.
  3  Nicodemus and see* Lord-Jézus [the_morsel] this
  4  bread and then-exist bread exist-Lord Judas
  5  Iscariot give^ and then-exist bread Judas
  6  were_opened* on-to-place devil = inside Judas go-this
  7  and_then Lord-Jézus apostle crying from man^ and give^ this
  8  from son God and_then Lord-Jézus Judas do
  9  who-exist do and then-exist evil apostle how?
 10  say Master speak but understand apostle how? say Judas
 11  bread buy brethren-exist shepherd ~eat because
 12  feed^ apostle ~exist judge because this exist Jew Easter

## 032r — Wednesday, and the silver

> and […] Judas; and he went [to] the Jews' chief in Jerusalem; because the Lord was […]. On Wednesday one of the apostles betrayed him — Judas — because he took for the Lord thirty silver and then the Lord Jesus; the Lord's brethren; the Lord goes to God his Father; and the Lord […] to you the Holy Spirit shall come; and you shall […] […] that is, the Lord goes to his death; the Lord dies, because the Lord, the Jews crucified; and the Lord on the third day again the Lord shall rise. Therefore the Lord asks you: do not, apostles, be offended in the Lord, because saying [to] God his Father […] […] […] the Lord […] […]

  1  and rise Judas and go Jew
  2  head inside Jerusalem because Lord exist inside Wednesday from apostle
  3  betray Judas because exist to-Lord grab thirty
  4  silver and_then Lord-Jézus brother of-Lord this-Lord
  5  go of-Lord God_the_Father and this-Lord you
  6  go holy-spirit and you exist see-two
  7  judge that_is this-Lord go on-die Lord die because
  8  Lord Jew crucified and this-Lord on_the_third_day
  9  again* stand_up-Lord therefore ask Lord you
 10  do_not apostle inside Lord stumble because what-go saying
 11  of-Lord God_the_Father [willed] saying SUBJ Lord crucified and_then

## 032v — Peter will deny him

> Peter: Master — Peter would […] the Lord; the Lord dies. […] the Lord Jesus [to] Peter: first, but before […] […] thou shalt deny the Lord. And Peter said […] […] […] the Lord Jesus, Peter, this […] this […] Therefore the Lord asks you: do not […] be offended in the Lord; because the apostles were very sorrowful for the Lord; and one of the Jews was a judge; and the mouth […] the Lord Jesus said: but […]; and the Lord went on the way, because the Lord Jesus […] when the Lord […] Judas, in the house of the high priest; and many miracles and much preaching afterward the Lord Jesus, on the way.

  1  Peter Master this-Peter want food Lord this-Lord die
  2  and_then Lord-Jézus Peter first but before cock
  3  this-?with Lord-to three exist deny and Peter say with*
  4  emperor and_then Lord-Jézus Peter this SUBJ this
  5  ~out therefore ask Lord you do_not apostle.
  6  inside Lord stumble because exist apostle many sad on-Lord have
  7  in_turn one Jew exist judge and mouth
  8  can Lord say Lord-Jézus but rise and go Lord
  9  on-way because have Lord-Jézus then-exist Lord know
 10  Judas inside house ~high_priest and many miracle
 11  and many ~preach ~do Lord-Jézus on-way

## 033r — over the brook Cedron, into the garden

> And Saint John tells of many miracles and much preaching afterward of the Lord Jesus […], but it is not written down. And then the Lord and the twelve apostles […] […] There was a brook Kidron; and of the apostles the rest of the apostles […]. The Lord took Peter, John, and James, and […] across the Cedron; and […] into mount and […], because there was a garden there mount […] Jerusalem […]; and […] the Lord went to Jerusalem; and in Jerusalem, behold, the Lord […] to the Lord Jesus and his apostles, because they would seize the Lord Jesus and take him in the garden. he is of the man, the father Adam [wrote] [the world]

  1  and speak holy-John many miracle and many ~preach
  2  ~do Lord-Jézus ~way but inside write not
  3  write and then-exist Lord six-six apostle [?]-~year this.
  4  exist one brook Kidron and from apostle
  5  rest apostle third apostle Lord give^ Peter and.
  6  John and James and [?]-[?].
  7  over-exist Cedron and to-?again inside to_the_mount
  8  and [?]-+one-[?] because-exist garden on-this to_the_mount
  9  trespass Jerusalem in_turn-to-in_turn and then-+SUBJ go-Lord on-Jerusalem and inside
 10  Jerusalem lo Lord [?]-Lord-apostle to Lord-Jézus and of-Lord apostle
 11  because want-Lord give^ Lord-Jézus inside-garden capture
 12  he_is* of-somebody father ~Adam [on_the_tree] [tree.]

## 033v — a stone's cast, and the prayer

> through sin this the Lord Jesus would, to a man [wrote] […] suffering, not […]; and then from the Lord the apostles in the garden; and the Lord went […] tells Saint John. The Lord went […] from the apostles […] about a stone's throw pray; his Father; and he knelt down, the Lord Jesus and then Father, his God […] […] take from the Lord this suffering; nevertheless as it pleases thee. And rise the Lord Jesus; and the Lord went to the apostles but; the apostles were asleep and then the Lord Jesus rise and […] woke them; and the Lord Jesus went […] Peter [to] the hilltop […] to see this […], because all the people were

  1  commit sin this want Lord-Jézus to-somebody [on_the_tree]
  2  [tree] suffering not-to and then-exist from-to Lord
  3  apostle inside garden in_turn to-Lord go on-~pray speak
  4  holy-John from-go-Lord trespass from apostle [answered] then-chapter
  5  a_stone's_throw = pray father of-Lord and kneel
  6  Lord-Jézus and_then father of-Lord God heaven.
  7  from ~grab-father from Lord this suffering in_turn
  8  SUBJ temptation^ and rise Lord-Jézus and go-Lord
  9  to apostle but apostle to-sleep and_then Lord-Jézus rise
 10  and ~have-apostle awake and go Lord-Jézus Peter
 11  peak of_the_mountain to see this ~people because exist every people

## 034r — the second prayer, and the sweat

> And a second time the Lord went […], and the Lord Jesus knelt and then God the Father eternal take from […] from the Lord this suffering; nevertheless as it pleases thee. And then the sweat ran down the Lord Jesus, because [in an agony] the Lord Jesus […] the Lord's suffering […]. And the Lord went to the apostles […]; the apostles were asleep and then the Lord Jesus rise; and […] woke them. At that time Saint Peter went and say […] sat and […] the Lord went […] to God his Father, and knelt | the Lord Jesus […] God his Father […] from | Father, take from the Lord this suffering; nevertheless as it pleases thee; nevertheless […] as it pleases thee; because God the Father […] for the Lord, the whole wide world |

  1  and two go Lord on-°pray-[?] and kneel Lord-Jézus and_then
  2  God_the_Father heaven* from ~grab-father from Lord this suffering
  3  in_turn SUBJ pleasing and then-exist to-to-to sweat through
  4  Lord-Jézus because [in_an_agony] Lord-Jézus how?-°first Lord suffering
  5  not-chapter and go Lord to-apostle but apostle to-sleep
  6  and_then Lord-Jézus rise and ~have-apostle awake
  7  time go holy-Peter and_say on-+three army-to sit
  8  and three go Lord ~pray God_the_Father of-Lord and kneel | Lord
  9  Jézus and_then God_the_Father of-Lord heaven* from | not_take
 10  father from Lord this suffering in_turn SUBJ pleasing in_turn
 11  [thy_will] pleasing because this-God_the_Father ~out on-Lord ~all_the_world | of

## 034v — the angel from heaven

> the Father. And an angel came from the eternal from on high, from God the Father and then the Lord, this […] this […] this suffering […] and then the angel this is offered the Lord […] the Lord's lot, of God the Father; the Son Jesus Nazareth all people redeemed. And the angel departed from before the Lord Jesus; because every night the angel came from on high, from God the Father, to the Lord Jesus; because the angel bore for the Lord all his suffering, it is written; and [spoken] truly […] he who […] written. And the Lord went to the apostles and then the Lord Jesus […] his […]; and the Lord and the apostles had one […] […]; and then […] […]; and then the apostles |

  1  father and go angel from_heaven* high from-God_the_Father and_then
  2  Lord this ~have this the_Lord this suffering drink
  3  and_then angel this_is this-Lord offer from-God_the_Father.
  4  of-Lord fate of-God_the_Father son Jézus Nazareth
  5  every people* from-buy and leave-to-leave angel before
  6  Lord-Jézus because every night this-go angel high from-God_the_Father
  7  to-Lord-Jézus because Lord carry angel every of-Lord suffering
  8  write and [spoken] righteous ~out he_who* from-prophet.
  9  write and go-Lord to-apostle and_then Lord-Jézus
 10  brother of-Lord and have-Lord-apostle one little
 11  not-?not-°first and then-exist [he_rose] [from_prayer] and then-exist apostle | to

## 035r — the sign, and the kiss

> slept. And the Lord Jesus could not sleep; but the Lord laid a stone at his head; and the Lord Jesus could not sleep; but rise and then the Lord, the apostles rise the apostles […] […] [a sign] serpent because from know came the Jews [betray] […] the Son of God […] to take him. And then the Lord and the apostles went on the way, and saw | the Lord Jesus a great crowd coming; and among the Jews was Judas. he who the father died, and the mother [while] [came] Judas and the Jews. He gave a sign, to tell the Lord apart from James and John — a kiss — so that Judas […] the Jews might take the Lord. And then Judas went up to the Lord Jesus; and […] Judas […] the Lord's hand; because he had given the Jews the sign,

  1  sleep and can sleep Lord-Jézus but Lord-put one stone
  2  to-head and can sleep Lord-Jézus but rise
  3  and_then Lord apostle rise apostle to-?again ~have-apostle [a_sign]
  4  serpent* because from know* go Jew [betray]
  5  Son_of_Man = recognize* capture and then-exist
  6  Lord apostle and apostle go-Lord-and-apostle on-way and see | Lord
  7  Jézus great^ people-chapter go and among Jew exist Judas
  8  he_who from-father die and mother [while] sleep [came] Judas and Jew
  9  ask_a_sign distinguish Lord James John with* kiss
 10  Judas from Lord capture Jew and then-exist
 11  go Judas against Lord-Jézus and kiss.
 12  ~Judas of-Lord hand because to-Jew ask_a_sign

## 035v — "Whom seek ye?" and they fell backward

> because John was like the Lord Jesus. And he cried out, | the Lord Jesus: Whom seek ye? The people, the Lord's — the Jews. And they cried, the Jews say answered Jesus Nazareth; and cried the Lord Jesus: I am he, if ye seek the Lord — the Jews. And all the Jews fell backward and then the Lord Jesus […] again […] […] hidden […] staves; and […] […]; and the Jews' staves […] because the Lord Jesus as did; God his Father, to the Jewish people; and […] […]; and a second time the Lord Jesus cried: whom seek ye, the people, the Lord's — the Jews. And they cried […] say answered Jesus Nazareth; and cried the Lord Jesus: I am he, if ye seek the Lord — the Jews; and

  1  because exist similar John to-Lord-Jézus ~and shout | Lord
  2  Jézus who? search people of-Lord Jew and shout
  3  Jew say answered Jézus Nazareth and shout
  4  Lord-Jézus from this-Lord if Lord search Jew and every
  5  Jew fall_back = and_then Lord-Jézus rise-Jew again*
  6  [swords] say hide of-club and rise-+say again* and of-Jew
  7  club grab-+say inside why?-in_turn because Lord-Jézus pray
  8  do God_the_Father of-Lord to-Jew people and
  9  rise-Jew to-?again and two shout Lord-Jézus whom search
 10  people of-Lord Jew and shout Jew.
 11  say answered Jézus Nazareth and shout
 12  Lord-Jézus from this-Lord if Lord search Jew and

## 036r — the third cry, and Jesus of Nazareth

> All the Jews fell backward and then the Lord Jesus […] again […] hidden […] staves; and […] […] and the Jews' staves […] because | the Lord Jesus as afterward God his Father, to the Jewish people; and […] […]; and a third time he cried | the Lord Jesus: Whom seek ye? The Lord's whom the Jews; and the Jews cried, they answered: Jesus of Nazareth. And the Lord Jesus cried: I am he. If ye seek the Lord — the Jews. And then the Lord Jesus cried: Take me, ye Jews, for I go […] to God my Father. And then the Jews […] the Jews, the Lord Jesus […]

  1  every Jew fall_back = and_then Lord-Jézus rise-Jew again*
  2  he_said* hide of-club and rise-+say again* and of
  3  Jew club grab-+say inside why?-in_turn because | Lord
  4  Jézus pray ~do God_the_Father of-Lord to Jew
  5  people ~and rise-Jew to-?again and three shout | Lord
  6  Jézus whom search of-Lord Jew
  7  and shout Jew say answered
  8  Jézus Nazareth and shout Lord-Jézus from this-Lord
  9  if Lord search Jew and_then shout Lord-Jézus
 10  grab Jew Lord because go ~hour of-Lord God_the_Father
 11  and then-exist ~Jew from-leave-leave Jew Lord-Jézus [backward]

## 036v — Malchus, and the ear put back

> He cut off with sword the ear of one of the Jews, and that Jew was Malchus. And then the Lord Jesus [said]: Peter, Peter, […] thou hast cut off […] because the man Peter sword cut off from sword struck […] die. And the Lord Jesus took the ear and put it back in its place, and the ear was made whole. And the Lord Jesus [did] that miracle before the heathen […] and […] said, and believed in the Lord; but his […] | the Lord take off; and one of the Jews fled, and believed in the Lord Jesus; and from […] the Lord Jesus all said [forsook] these Jews went; and […] from little [if] And then the Lord could have fled — the Lord did not flee, but [shepherd] […] the apostles, the Jews […] […]

  1  cut_off with* sword ear one Jew
  2  and was_named* Jew exist Malchus and_then
  3  Lord-Jézus Peter Peter ~blind cut_off sword because and
  4  somebody Peter sword cut_off from sword.
  5  struck* somebody-+SUBJ die and give^ Lord-Jézus this ear
  6  and ear-+SUBJ put on-place and healing ear
  7  leave-to-leave and from Lord-Jézus on-pagan miracle ~do
  8  and and say inside Lord believe but of-Lord believe* | on
  9  Lord take_off and escape one Jew
 10  to-Lord believe Lord-Jézus and from [fear] to-Lord [fled] Lord-Jézus
 11  every say [forsook] this-who Jew go and then-[?] from little
 12  [if] and then-exist Lord want escape exist Lord not escape
 13  but good [will] to-~somebody apostle Jew pagan-~year above-high

## 037r — bound, and struck

> […] and […] led the Lord believe the Lord Jesus; and then tie up the hands of the Lord Jesus Christ […] all […] […] […]; and then […] they went to the chief of the Jews [before]; and then the Lord went down from the mountain; and many [people] afterward Jews upon the Lord Jesus, because one struck the Lord [from] town secondly, to the Lord's house [and] thirdly [answered] no man at all had mercy on the Lord Jesus. And then through […] through […] Kidron and the Lord […] went over the bridge […] but the Lord on the bridge fall down; and [struck] […] no man had mercy on the Lord Jesus, because [times] the Jews went

  1  on_the_cross-[?] and then-[?] carry to-Lord believe.
  2  Lord-Jézus and then-exist tie_up hand Lord-Jézus-Christ
  3  [bound] every to-of-Lord to-year-to [led] that* and then-exist Lord.
  4  go to-Jew head [before] and then-exist Lord
  5  go down on-to-mount and many [people] ~do
  6  Jew on-Lord-Jézus because Lord one scourged* beat
  7  [from] town* in_turn-two to-Lord to-house [and] third
  8  to-Lord [answered] from not-not of-somebody have_mercy Lord-Jézus
  9  and then-exist through [?]-+say through over-~exist Kidron
 10  and Lord grab-+say on-bridge go Lord-Jézus.
 11  but Lord on-bridge fall and to-Lord [struck] who.
 12  of-somebody have_mercy Lord-Jézus because Lord two [times] go Jew

## 038r — bound before Caiaphas

> [bound] they bound the Lord Jesus Christ; and then the Lord […] and dragged him out […]; no man had mercy on the Lord Jesus Christ. And then the Jews who the Lord would the Jews went […] one […] the Lord | Pilate; secondly […] to Caiaphas; and | when the Lord […] to Caiaphas the high priest. And then the Jews […] accused the Lord; and then the Lord […] before the high priest's house; and | when the Lord […] […] the Lord this […] and then the Lord […] into a house; and | when the Lord […] one […] […] | not at all the Lord Jesus Christ said. And then Peter, one

  1  [bound] who-chain-to Lord-Jézus-Christ and then-exist Lord
  2  exist and out-out draw [away] of-somebody have_mercy
  3  Lord-Jézus-Christ and_then Jew who Lord want
  4  Jew go say-+say one brought* Lord | to
  5  Pilate in_turn-two say brought-Lord to-Caiaphas and | then
  6  exist Lord brought-Lord to-Caiaphas high_priest and_then
  7  Jew would_say* Lord on-+three accuse and then-exist
  8  Lord to-[?] before NAME.priest high_priest house and | then
  9  exist Lord exist-+say inside-?brought Lord this high_priest.
 10  and then-exist Lord gate inside one house and | then
 11  exist Lord from-to-every one [answered] ~hour | not-not
 12  say Lord-Jézus-Christ and_then Peter one

## 038v — the first denial, and Caiaphas's counsel

> of the Jews, this Malchus whose ear was cut off […] Peter […] this Peter […] and this was the first denial of the Lord Jesus, because Peter said not the Lord, and denied him. And […] the Lord Jesus [was brought] to Caiaphas the high priest; and | when he said, the Lord went before Caiaphas; and there cried the Jews […] [expedient] this went believe this […] the Lord; and to the Lord […] of the apostles […] […] all the people against the Lord […] | and the second said: the Son of God; the third said: the king. Caiaphas said: it is written, it is good that one man should die rather than all […] […]; and […] […] the high priest […] in the house, among the apostles Christ [counsel]

  1  Jew this Malchus ear cut_off say.
  2  Peter [then] this-Peter and-to-Lord-to-Peter and this from
  3  first denial Lord-Jézus because say Peter not* Lord and-to-Lord-to
  4  and brought* Lord-Jézus to-Caiaphas high_priest and | then-exist
  5  say to-Lord go before Caiaphas and shout
  6  Jew this-Caiaphas-+say [expedient] go this believe
  7  this ~half-believe Lord and to-Lord SUBJ from apostle-exist-exist
  8  feed^ bread all^ people on-Lord [manna] | in_turn
  9  two say-+say say son God third say-+say king
 10  say say Caiaphas write SUBJ good one Lord-somebody
 11  die but-+who rather all^ world perish and then-?cup-+say [nation]
 12  apostle-high inside-?brought inside house among disciple^ Christ look_up leave^ [counsel]

## 039r — the second denial

> Saint Peter before the gate; and then Peter was seen by the maid at the Jews' gate. And then the maid [said] to Peter: art thou an apostle of this Jesus? Peter said […] and denied him. This was the second denial of the Lord Jesus, because Peter said […] the Lord | and denied him. And John […] […] was known to the high priest. Caiaphas said to Jesus: sayest thou the Son of God? And how dost thou truly preach? Jesus said to Caiaphas […] Caiaphas […] answered […] hear my preaching [denied] truly […] And then Caiaphas, this Caiaphas, and [gathered] in the Lord new Caiaphas but rather the Lord righteously the man; Caiaphas said […] the Lord […] […] to Caiaphas […]

  1  holy-Peter before ~gate and then-exist Peter exist
  2  show^ from-handmaid ~gate Jew and_then handmaid this-Peter
  3  disciple^ this Jézus say Peter this-?with and-to-Lord-to and.
  4  this the_rest^ denial Lord-Jézus because say Peter not* Lord | and.
  5  to-Lord-to in_turn John inside-[?] because-exist.
  6  acquaintance this high_priest say Caiaphas to-Jézus this-Lord say
  7  son God in_turn how? this righteous preach say Jézus
  8  to-Caiaphas from-judge-Caiaphas from say Lord-to.
  9  hear preach [denied] ~righteous preach.
 10  and_then Caiaphas this-Caiaphas and [gathered] inside Lord new
 11  Caiaphas-year but_rather* this-Lord righteously man^ say Caiaphas
 12  [?]-field Lord brought* to-~Pilate to-of-Caiaphas exist-exist

## 039v — before Pilate

> And this […] the two […]; and the Lord […] | Pilate; and they accused the Lord […] […] Pilate; the Lord went […] and | when he said: they have done nothing at all against the Lord. The Lord went before Pilate, because all his […] | the Lord […] and his holy face […] and | when the Lord […] said […] […] […]; no man had mercy on the Lord Jesus. And then the Lord said, and went to Pilate. And then the Jews [said] to Pilate: the Lord went […]; and the Lord […] | of the apostles […] […] all the people against the Lord […] The second said: he saith he is the Son of God. The third said:

  1  and this ~out two hour and Lord brought* | to
  2  Pilate and from Lord on-+three accuse and_then-+say
  3  he_said* Pilate go this-Lord half-believe and | then
  4  exist say many not-not on-Lord do
  5  go Lord before Pilate because every of-Lord [accusation] | on
  6  Lord from [spat] and of-Lord holy-face every [buffeted] and | then
  7  exist Lord exist say [nothing] to-?again [again] of-somebody
  8  have_mercy Lord-Jézus and then-exist Lord exist say go
  9  to-Pilate and_then Jew this Pilate say Lord
 10  go this-Lord half-believe and Lord SUBJ from | apostle-exist
 11  exist food bread every people on-Lord [manna]
 12  in_turn-two say say say son God third say say

## 040r — the third denial, and the cock

> he saith he is king. And then Peter went to a […] […] because […] […] […] […] […] […] said one of the Jews to him: […] art thou an apostle of this Jesus? Peter said know and denied him, and this was the third denial of the Lord Jesus; and at that moment the cock crew. And Peter said he who Peter went out: Master, he spoke, and sorrowfully with went out. And then Pilate righteously to Jesus: sayest thou that thou art the Son of God? And how dost thou preach? The Lord Jesus said to Pilate; Pilate answered […]: hear my preaching [denied] righteously preach. And Pilate [judged]; the Lord Jesus spoke

  1  king say and then-exist Peter go to-one
  2  bread [manna] because exist virgin-cut_off [sacrament] [worship]
  3  want with* [answered] say one Jew to
  4  with* this apostle [?]-~half-~believe this Jézus
  5  say Peter grab God this-Peter know
  6  and this three denial Lord-Jézus and time crow cock
  7  and say Peter this SUBJ out he_who* Peter Master
  8  speak and sad with* leave-to-leave and_then Pilate
  9  to-Jézus this Lord say son God in_turn how? this righteously
 10  preach say Lord-Jézus to-Pilate from-judge-Pilate
 11  from say and-+say Lord-to hear preach [denied]
 12  righteously preach and Pilate [judged] from speak Lord-Jézus

## 040v — two lines

> but the Lord said […] with his own mouth, that he is truly the Son of the living God.

  1  but say Lord this-~Pilate SUBJ mouth and-Lord this-Lord
  2  righteous son living God

## 041r — art thou the king of the Jews

> And then Pilate [said] to the Lord: speakest thou, Lord, king of the Jews? The Lord Jesus said to Pilate [asked] Pilate's mouth and that he is truly the Son of the living God and then Pilate […] truly this man; Pilate how [answered] in the Lord [nothing]; and there cried the Jews […] the Lord. Pilate: the cross! The Lord [is] accursed, this Pilate […] would say the Lord, say […] emperor truly condemned. And then […] [therefore] they took the Lord, saying; and the Lord brought Herod, Pilate's […]; and then […] […] the hour; and then the Lord brought that king; and then, and […] upon one

  1  and_then Pilate this Lord speak Lord king Jew
  2  say Lord-Jézus this Pilate SUBJ [asked] Pilate mouth
  3  and this-Lord righteous son living God and_then.
  4  Pilate this-Lord SUBJ righteous somebody this Pilate
  5  how? [answered] inside Lord [nothing] and shout
  6  Jew condemned* Lord Pilate on_the_cross Lord cursed this
  7  Pilate this-hide want say Lord say [release]
  8  emperor righteous condemned* and_then Pilate.
  9  [therefore] grab Lord say and Lord brought*
 10  ~Herod of-Pilate ~brother and then-exist ~out three.
 11  hour and then-exist Lord brought* that*
 12  king and then-exist and [?]-+say on-one

## 041v — sent to Herod, because he is of Galilee

> […] […]; and then all cried out, the four […] the Lord [accused] this brought the Lord […] this Jesus blasphemeth; and the Lord is out of Galilee, he cometh bread; all the people against the Lord [manna] And then the Lord […] many judged […] Herod the king, because […] the Jews would […] the Lord to Herod condemned; and the Lord […] Herod condemned; but [long] shone […] Herod, the Lord Jesus Christ; and then the Lord brought before Herod the king; and the Jews cried […] Herod said: the Lord went […]; and the Lord is out of Galilee, he cometh bread all

  1  love [answered] and then-exist from shout every two-two direction-~year-to
  2  Lord [accused] this brought* this-Lord ~begin-believe
  3  this blasphemer-Lord this Jézus and SUBJ Lord from Galilee
  4  protrude bread every people on-Lord [manna]
  5  and then-exist Lord to-?brought many ask^ before.
  6  Herod king because to-+Elizabeth Jew to-Lord want
  7  Herod condemned* and Lord emperor.
  8  Herod condemned* but [long] shine see.
  9  Herod Lord-Jézus-Christ and then-exist Lord brought* before
 10  Herod king and shout Jew this.
 11  Herod say Lord go this-Lord begin-believe and Lord SUBJ
 12  from Galilee protrude bread every

## 042r — four lines

> the people against the Lord [manna]; and the Lord said, the Son of God. And then the false […] said of the Lord, and the man, this temple destroy | he would the Lord, that he in three [days] all [would] do

  1  people on-Lord [manna] and Lord say son
  2  God and_then ~false °and_then-confess say Lord and
  3  man* this exist-chapter destroy | want
  4  Lord this-Lord in three_days every ~do

## 042v — Herod questions him

> and [of David] confessed it talent Herod; but […] Herod said: Lord — Herod [mock] God, that the Lord is the Son; and one said, spoke of the Lord Jesus against Herod; and Herod [mocked] Herod [derided] Herod the king […] the Lord […] Herod […] this death […] […] the Lord [sent back] Herod said to him, Herod said [again] to Herod: the Lord of the living God […]; Herod said [mock] God — that he is the Son; and not the Lord was named his Father […]. And then the Lord Jesus to Herod | that the Lord is truly the Son of the living God. The Lord Jesus said: the Lord goeth to his Father […] to judge the living and the dead; and Herod did so: he brought a stone and […]

  1  and [of_David] to-this confess talent Herod but say.
  2  Herod say Lord Herod [mock] God this Lord son and
  3  one say speak Lord-Jézus ~against Herod and
  4  Herod [mocked] Herod [derided] this-Herod king this-Herod.
  5  this-Lord can Herod [white] this die condemned* [garment]
  6  this-Lord [sent_back] Herod to say say Herod [again]
  7  to-Herod this Lord-to living God one-to say Herod [mock]
  8  God this-Lord son and not* Lord was_named*
  9  of-Lord father [believed] and_then Lord-Jézus to-Herod | this
 10  Lord righteous son living God say Lord-Jézus this-Lord go
 11  of-Lord father on-[?] judge living and die
 12  and do Herod carry stone and inside.

## 043r — Herod hoped to see a miracle

> a vessel of water, and brought various [stood] before the Lord Jesus; and the Lord was asked by Herod, when the Lord [stood] before him, to do a miracle; and they set a yoke before the Lord Jesus, and […] to do a miracle, because when [hoped] before Herod he did no miracle, though the Lord took […] condemned but Herod said brought the Lord [questioned] Pilate became Herod's brother […] who […] the Lord, because […] upon the Lord, Pilate did. And the Lord brought before Pilate, many judge And this was […] the sixth hour; and the Lord […] before Pilate. And then the Jews [said to] Pilate; Pilate said

  1  one vessel water and brought* various
  2  [stood] before Lord-Jézus and Lord ~ask
  3  Herod then-exist-Lord before miracle do
  4  and yoke Lord-Jézus before and understand-eat
  5  miracle do because then-exist [hoped] before
  6  Herod miracle do why?-Lord grab Herod.
  7  condemned* but say Herod brought* this Lord [questioned]
  8  Pilate to-of-Herod friend^ understand-understand-+who who
  9  [answered_nothing] this-Lord because on-Lord do Pilate
 10  and Lord brought* before Pilate many judge
 11  and this ~out six hour and Lord brought* before
 12  Pilate and_then Jew Pilate say this-Lord Pilate SUBJ

## 043v — the scourging

> Herod condemned; and Pilate if the Jews would the Lord. He said [wrote] inscription truly condemned And then Pilate […] the soldiers; the soldiers brought him [to] Pilate, the two [thieves] [with him]; and then Pilate said, bring the two [thieves] [with him]; and the Lord […] the gate […] […]; and Pilate took | two two soldiers to the Lord Jesus, and the Lord was scourged; and then the two [pillar] flogged the Lord Jesus; and a second time the Lord the second began, saying, to flog; and then the second, and the second said, […] flogged the Lord Jesus Christ; and | there came one soldier to the Lord Jesus; and then […] the Lord Jesus, because the Lord had many tie up

  1  Herod condemned* in_turn-who-Lord this Pilate if want Jew
  2  Lord say [wrote] ~emperor righteous condemned*
  3  and_then Pilate understand-eat soldier carry-soldier Pilate
  4  two [thieves] [with_him] and then-exist Pilate say carry
  5  two [thieves] [with_him] and Lord gate inside.
  6  understand-eat ~until and grab Pilate | two
  7  two soldier to Lord-Jézus and Lord exist whip and then-exist
  8  two from [pillar] flog Lord-Jézus in_turn-two Lord
  9  begin two say flog and then-exist two and from two say
 10  from [pillar] flog Lord-Jézus-Christ and | leave
 11  to-leave one soldier to Lord-Jézus and then-exist
 12  from one-+Wednesday Lord-Jézus because exist Lord many tie_up

## 044v — the purple robe and the crown of thorns

> And then the Lord collapse; they bowed before the Lord Jesus; and the Lord [scourged] again […]; and the Lord [mocked] […] a purple robe; and the Lord, thorns crown upon his head […] and they set the Lord upon a seat; and […] knelt before the Lord Jesus, and spoke: Hail, Jesus, this day! And […] […] […] the soldiers […] […] […] the Lord Jesus; and [sat] seat [judgment] the Lord Jesus; and then the Lord collapse bowed; and the Jews took the Lord, and the Jews led the Lord to Pilate, into the house.

  1  and then-exist Lord collapse = Lord-Jézus and
  2  Lord [scourged] again* raise-+say and Lord [mocked]
  3  ~ask-to understand-eat purple_robe and Lord
  4  thorn crown on-head conceive-+say
  5  and Lord sit on-understand-eat chair and
  6  then-[?] kneel before Lord-Jézus and
  7  speak healing Jézus today-this and leave-to-leave [hail]
  8  understand-eat soldier that* [gave] [blows] Lord-Jézus and
  9  [sat] from seat [judgment] Lord-Jézus and then-exist
 10  Lord collapse = and Lord grab Jew
 11  and Lord go Jew to Pilate inside house

## 045v — twelve legions of angels

> And the Lord sat […] in a judgment seat | in the midst […]; and then Pilate knelt before the Lord Jesus, and Pilate said: Hail, Lord, King of the Jews! And the Lord Jesus said to Pilate […] speakest thou that the Lord is King of the Jews? Because | when will his Father God, ye took the Lord prisoner; for if the Lord would, the Lord would ask of God his Father | twelve legions of angels […] the Lord, that ye took him prisoner; because if the Lord would, the Lord could […] you all

  1  and Lord sit say inside one throne | on
  2  middle ~until and then-exist kneel Pilate
  3  before Lord-Jézus and say Pilate healing Lord king
  4  Jew and say Lord-Jézus to-Pilate this-+the_Lord
  5  speak because this-Lord king Jew because | then
  6  exist will of-Lord God_the_Father you
  7  Lord capture because then-exist this-Lord want Lord
  8  this-Lord ask from of-Lord from-father God | six
  9  six an_army in_turn angel remain* this-Lord
 10  you grab capture because then-chapter
 11  this-Lord want this-Lord you every can

## 046r — Barabbas, and Behold the man

> the Lord die […]; and ye took the Lord prisoner. And Pilate said to Jesus: sayest thou, Lord, the Son of God? And one said [Behold] the Lord Jesus said to Pilate; and he released Barabbas scourged Jesus; and they beat the Lord, [from] town [outside] all his […] quaked; and Jesus said […] the soldier, Barabbas, truly the Lord spoke […] they beat him; the scribes spoke, it is written that; and [scourged] [again] they beat him. O! O! And so they did to the Lord. Pilate went out of the house, and cried, Pilate: Behold Jesus, Nazareth the King of the Jews!

  1  Lord die cross-die and you grab
  2  Lord capture and say Pilate to-Jézus this
  3  Lord say son God and one say
  4  [Behold] say Lord-Jézus to-Pilate and leave-chapter-leave
  5  Barabbas to-Jézus and Lord beat scourged*
  6  [from] town* [outside] every of-Lord holy-nine-+name
  7  quake and say Jézus this soldier Barabbas this righteous
  8  speak-Lord to-inside-Lord beat speak church_father
  9  write that* exist and [scourged] [again] beat
 10  chapter-oh chapter-oh and Lord do
 11  Pilate out go on-house and shout-to
 12  Pilate lo Jézus Nazareth king Jew

## 046v — crucify him, the second time

> […] and the angel […] Bethlehem […] And the Jews cried: the cross for the Lord! Pilate: the Lord is accursed, […] if ye will the Lord. He said enemy […] truly condemned; and Pilate said to the soldiers, lead the Lord into the house. And a second time the Lord afterward went into the house, and Pilate cried: Behold Jesus Nazareth the King of the Jews! […] and the angel | [to] Bethlehem […] and […] the Jews: the cross for the Lord! Pilate: the Lord is accursed, this Pilate, if ye will the Lord. He said enemy […] truly condemned; and Pilate said to the soldiers, lead the Lord

  1  [Caesar] in_turn angel Bethlehem city.
  2  and shout Jew on_the_cross Lord Pilate cursed Lord
  3  this-~Pilate if want Lord say enemy of-~emperor
  4  righteous condemned* and say Pilate to soldier go Lord
  5  inside house and two Lord ~do go on-house
  6  and shout Pilate lo Jézus Nazareth
  7  king Jew [Caesar] in_turn angel | to
  8  Bethlehem city and shout.
  9  Jew on_the_cross Lord Pilate cursed Lord this
 10  Pilate if want Lord say enemy of-~emperor
 11  righteous condemned* and say Pilate to soldier go Lord

## 047r — the third time, and Caesar

> into the house. And a third time the Lord afterward went into the house, and Pilate cried: Behold Jesus Nazareth the King of the Jews! [Caesar] and the angel [to] Bethlehem […]; and there cried the Jews: the cross for the Lord! Pilate: the Lord is accursed […] Pilate, if ye will the Lord. He said […] | Caesar truly condemned. And then the Jews [Behold] that the Lord is King of the Jews […] half […] the Lord, half […] one the Lord blasphemeth. And Pilate cried, Pilate, and how [cried] in the Lord [out] Pilate, that he is

  1  inside-house and three Lord ~do go on-house
  2  and shout Pilate lo Jézus Nazareth
  3  king Jew [Caesar] in_turn angel
  4  to-Bethlehem city and shout
  5  Jew on_the_cross Lord Pilate cursed Lord this.
  6  Pilate if want Lord say enemy | of.
  7  emperor righteous condemned* and_then Jew
  8  [Behold] this-Lord king Jew this-Lord.
  9  half one Lord half-believe one
 10  blasphemer-Lord and shout Pilate this Pilate
 11  and how? [cried] inside Lord [out] Pilate this-Lord SUBJ

## 047v — Pilate washes his hands

> truly this man. And then Pilate […] water in a basin, and […] […] brought it, and […] the two […]. And then Pilate […]: I am innocent of this Lord's blood. And then the Jews, because this was […] and […] the son; and Pilate cried: whom will ye | that I release, Barabbas or Jesus? And the Jews cried: release Pilate Barabbas, and Jesus to the cross! And then Pilate condemned the soldiers led the Lord up into the house; and then Pilate, the Lord went […] […] into the house; and Pilate cried |

  1  righteous man^ and_then Pilate carry-+say water
  2  inside one washdish and [?]-~Pilate exist.
  3  carry and high-wash-~Pilate of two why?-in_turn and_then
  4  Pilate this-~Pilate innocent from of-Lord blood and_then
  5  Jew because this exist on-+say and of-+say son
  6  and shout Pilate who want | Pilate
  7  to say release Barabbas in_turn Jézus and
  8  shout Jew release Pilate Barabbas
  9  in_turn Jézus on_the_cross condemned* and_then Pilate understand-eat
 10  soldier go divine_one^ up on-house and then-exist Pilate this-who
 11  divine_one^ go [went] up on-house and shout Pilate | from

## 048r — the Reproaches: O my people, what have I done to thee

> […] this man truly took […] because not want the Lord condemned; and the Lord afterward Pilate went out of the house down among [them] […] and the Lord Jesus cried: O my people, the Lord's people, the Jews, who he said afterward I loved this people cross afterward the people, the Lord's, the Jews, who […] this people, through sin [O my] I did good to this people [what] the Lord among this people did miracles. First, | this people went into Egypt [out of] as servants; over sea […] I divided

  1  SUBJ somebody righteous grab on-?condemned because SUBJ
  2  not_want Lord-to condemned* and Lord ~do
  3  Pilate out go on-house down among from [them]
  4  ~Jew and shout Lord-Jézus people-chapter
  5  of-Lord Jew who this-Lord he_said* ~do
  6  to-love this-people-chapter [cross] ~do people-chapter
  7  of-Lord Jew who this-Lord this-people-chapter commit sin
  8  [O_my] this-people-to good [what] then-exist-Lord this-Lord
  9  among this-people-to miracle do first | this
 10  people-chapter go on-Egypt [out_of] living-servant this
 11  over sea [?]-[?]-~exist divide

## 048v — forty years in the wilderness, and a cross for their Saviour

> in two parts, this people, over the sea; through struck the Lord led them by day, and from the beginning all […] to this people, the whole wide world | I kept this people alive forty years in the wilderness, and the angel bread to this people; [thou hast prepared] cross I did for the Lord's people, the Jews […]; they lifted up the Lord on Palm Sunday | they would make the Lord king, a crown, and […] would say his body lifted up upon the cross; and Pilate cried […] the Lord blind and the Lord take the Jews; and then he said

  1  on-two direction this-people-chapter over sea
  2  through struck* go-Lord day in_turn from head
  3  every sky to-of-people-chapter ~all_the_world | this
  4  people [fed] living-Lord forty inside field
  5  in_turn angel bread to-this-people-chapter
  6  [thou_hast_prepared] cross do people of-Lord
  7  Jew he_said* to-Lord-to raise on-Palm_Sunday | then
  8  chapter-Lord want king crown in_turn name-high
  9  would_say* of-Lord body on_the_cross raise-to
 10  and shout Pilate grab-+say Lord ~blind
 11  and Lord take* Jew and then-exist say

## 049r — the two thieves, and Mary Magdalene told

> They brought two thieves to the Lord Jesus, and set […] upon the Lord Jesus; and of the two thieves | […] […] the good one […] […] the Lord Jesus. And Saint John went up into Bethany, to Mary Magdalene: [sought] Master, the Lord liveth [early] to Mary Magdalene [appeared]; and he said […]; Mary Magdalene went with John […] at that time

  1  to-go say two ~thief to Lord-Jézus and put
  2  say cross on-Lord-Jézus in_turn from two ~thief | carry
  3  say who-[?] good from [sepulchre] [laid] Lord-Jézus
  4  and to-go up holy-John inside Bethany to
  5  two-Mary Magdalene good [sought] Master living Lord [early]
  6  to-Mary Magdalene [appeared] and say SUBJ
  7  understand-go Mary Magdalene John [stood] time

## 049v — over the Cedron, and Simon carries it

> The Lord went, he said, to the Cedron; and then the Lord went over the Cedron; and then down […] […] the Lord Jesus; and […] | fall down the Lord Jesus […]; and the Jews knelt before the Lord Jesus, and […] Hail, Jesus! […] And there came to the Lord | the Virgin Mary; and Simon carried it for the Lord; and | when the Jews […] within […] and […] cross upon the earth, and […] believed in the Lord Jesus […] […] [they parted] the Lord […] the Lord Jesus, and

  1  go this-Lord say exist Cedron and then-exist go Lord
  2  say over-exist Cedron and then-exist
  3  to-down [ground] to-°sick Lord-Jézus and collapse | from
  4  fall Lord-Jézus to-+cross and kneel Jew
  5  before Lord-Jézus and speak-+say healthy_man^
  6  Jézus Nazareth and leave-to-leave to-Lord | virgin
  7  Mary and Lord Simon cross carry and | then
  8  exist Jew [?]-+cross-[?] inside ~Eden
  9  and put-+say cross on-earth and
 10  take_off believe on-Lord-Jézus food [garments]
 11  [they_parted] Lord take_off-+say Lord-Jézus and

## 050r — laid upon the cross

> the Virgin Mary came to the Lord Jesus; and | [they bound] […] his bonds. And then the Lord Jesus […] his have said, […] […] this, in the commandment […] his apostles; and the Jews saw [the title] the whole wide world To his passion the Lord went; and [written] said, in the Lord believed; and they laid the Lord upon the cross, and the Lord […] one […] and the two [between] the cross, and could […] and […] […] and […] […]; and his feet could

  1  leave-to-leave virgin-Mary to-Lord-Jézus and | from
  2  [they_bound] of-exist-°first of-Lord handcuffs and_then
  3  Lord-Jézus name-[?]-~exist of-Lord have say
  4  trespass [wrote] this inside commandment this apostle-+one of-Lord apostle
  5  and see Jew [the_title] good all_the_world
  6  on-suffering-year go Lord and [written] say inside
  7  Lord believe and to-Lord set_on on_the_cross
  8  and Lord this-pierce-+say one why?-in_turn
  9  and two [between] on_the_cross and can
 10  take* and why?-in_turn chain-draw-+say
 11  and why?-in_turn pierce-+say and of-Lord foot can

## 050v — the title, and the ninth hour

> take and the feet […] and they pierced the feet; and all his […]; and | the Lord [three tongues] in the Lord […] in the Lord Jesus Christ. And Pilate wrote upon a tablet: Jesus Nazareth King of the Jews. And then the Jews: write that the Lord said he is King of the Jews. But the Lord's writing, Jesus Nazareth. And then Pilate: what I have written Pilate has written. And the two thieves; with the Lord they nailed them to the cross, and the Lord among the two thieves […] […]. And this was at the ninth hour. And then the Lord Jesus on the cross prayed to God his Father eternal

  1  take* ~and foot chain-draw-+say
  2  and foot pierce and every of-Lord [title] and | of
  3  Lord [three_tongues] inside Lord to-°trench-to-°trench inside Lord-Jézus-Christ
  4  and write Pilate on-one tablet Jézus
  5  Nazareth king Jew and_then Jew
  6  write Lord king Jew but Lord write
  7  Jézus Nazareth and_then Pilate write SUBJ
  8  who ~Pilate write and two ~thief to-Lord pierce
  9  on_the_cross and Lord call^ two ~thief one-[?]
 10  say and this out nine hour and_then Lord-Jézus
 11  on_the_cross from-father of-Lord God heaven* ask-Lord

## 051v — three nails, and the sponge on a stick

> remain Mary's woe; but his three nails, long, with which they nailed the Lord to the cross. And then the Lord Jesus […] the Lord; and | the Lord's apostles, when they bought […] sweet, and wine; the apostles took […] the Jews' chief; and the Lord […]; but […] […] and the Lord | took […] vinegar; and […]; and the Lord, they took wine upon a sponge on a stick, and held the sponge to the Lord's face […]; and the wine […] his mouth […] […]. And then | the Lord Jesus upon the cross [prayed to] God his Father in heaven […] […] his Father […] into his Father's hands.

  1  remain* of-Mary woe but of-Lord three_nails long this-who
  2  this-Lord pierce to-cross and_then Lord-Jézus thirst Lord and | of
  3  Lord apostle then-exist buy grape sweet and
  4  wine grab apostle high_priest = and
  5  Lord grab-+who but say-to pine in_turn Lord | grab
  6  say vinegar and [hyssop] and Lord
  7  wine grab say on-one sponge and
  8  then-exist-Lord sponge face wipe_off-+say and wine
  9  grab mouth little on-+pine and_then | Lord
 10  Jézus on_the_cross from-father of-Lord God heaven offer
 11  this-Lord this-father of-Lord commend* inside of-God_the_Father

## 052r — two lines

> […] and […] to the Lord Jesus, his […] […] Here ends the account Passion evangelist the Passion of the Lord Jesus.

  1  why?-in_turn and from to-Lord-Jézus of-Lord commend* give_up_the_ghost
  2  end this the_account* Passion evangelist* suffering Lord-Jézus

## 052v — the earthquake, and Longinus

> And then the Lord Jesus, his commend give up the ghost upon the cross; the earth quaked, the rocks and the stones rent; the sun and the moon were darkened; and all creatures among the people humbled themselves; and all creation mourned, when Christ the Lord was crucified. And there came one soldier from Jerusalem, blind; and that soldier was Longinus; and the Jews' spear pierced the Lord Jesus Christ; and [pierced] the spear […] the Lord Jesus Christ; and the soldier, the blood splashed from the Lord Jesus upon his eyes, and through it he saw, and the soldier was healed; and the soldier believed in the Lord Jesus Christ, and the soldier was baptized, and saw […]

  1  and then-exist Lord-Jézus of-Lord commend* give_up_the_ghost on_the_cross earth
  2  quake rock stone rent sun and moon
  3  this eclipse and every [...] among_the_people* this humble ~and every
  4  create mourn then-exist Christ crucified Lord and go say.
  5  one soldier on-Jerusalem blind and was_named* soldier
  6  exist Longinus and pierce Jew spear ~exist-from-in_turn
  7  Lord-Jézus-Christ and can [pierced] spear on
  8  ~exist-from-in_turn Lord-Jézus-Christ how? soldier [thieves] splash
  9  to-to-to Lord-Jézus on-place through see and healing soldier
 10  leave and grab soldier believe Lord-Jézus-Christ
 11  and soldier see-baptize and see ~Jew

## 053r — after the ninth hour

> […] the Lord Jesus Christ; and […] believed in the Lord, but many judged brought […] home. And the second said sorrowfully, accusing, because [darkness] [came] he said that they crucified, saying, the Son of God; and sorrowfully they went, saying […] home; and this [from] was the ninth hour, and four hours from that hour the Lord Jesus suffered upon the cross […] […] all […] home from [breast] [striking] and the apostles […] went, every one of the apostles […] | […] and one, and […]

  1  can Lord-Jézus-Christ and [many] inside Lord believe
  2  but many judge brought* [?]-+say home
  3  in_turn-two say sad accuse because [darkness] [came]
  4  say that* ~execute say son God and
  5  sad go say [?]-+say home and this
  6  [from] out nine ~hour and two-two from ~hour
  7  on_the_cross suffer Lord-Jézus and-+say go-?brought
  8  every [?]-°and_then home from [breast] [striking]
  9  in_turn apostle exist apart go-go every to-apostle [stood] | on
 10  Galilee and one and understand-eat

## 053v — Joseph and Nicodemus ask for the body

> the apostles […]; and then two […] Jerusalem, and was named was Joseph; and the second Nicodemus; and then the two asked of Pilate […] the Lord Jesus; and have the two, the sufferer […] the Lord Jesus; and then the two went [away] Christ was condemned; and the two went to many Jews; and the two were, that is, good and merciful men; and then the two saw the Virgin Mary, and […] Magdalene. Many people went out of Jerusalem, and were afraid, because the Jews would […] the Lord, all […] because

  1  apostle cut_off and then-exist two somebody-have_mercy Jerusalem ~one
  2  and was_named* exist Joseph in_turn-two
  3  ~Nicodemus and then-exist two ask from Pilate
  4  ~exist-[?] Lord-Jézus and have two sufferer
  5  ~exist-[?] Lord-Jézus and then-exist two go [away]
  6  exist Christ condemned* and go to two
  7  many Jew and two people that_is good people have_mercy
  8  and then-exist two see virgin-Mary and Mary.
  9  Magdalene go many people on-Jerusalem and ~through
 10  startle because to Lord want Jew every Lord [take_down] because

## 054r — taken down, and the tomb sealed

> this was […] | and […] went […] […] because Mary was […] fled […] the Jews; and in that place were these people, when the two Marys went to the people, and took Nicodemus the Lord Jesus from the cross, and the three nails, […] Saint John took […] saw | the Virgin Mary […] took the Virgin Mary into bosom and afterward Nicodemus, with his servants' [linen]; and the two covered the body, and […] [linen]; and Nicodemus laid the Lord Jesus within, and they closed the Lord within the tomb; and there stood, he said, four soldiers by the Lord […] were opened the chief of Jerusalem; and [the veil] went [part]. Here ends this holy gospel.

  1  this exist from | and [down] go down [from_the_cross]
  2  because exist-Mary on-+mount escape before.
  3  Jew and on-place exist this people then-exist
  4  from two-Mary to-people go-two-Mary and grab
  5  ~Nicodemus on_the_cross was_named* Lord-Jézus in_turn three three_nails
  6  seal-to grab holy-John then-+mouth-Mary see | virgin
  7  Mary then-~exist grab virgin-Mary inside bosom
  8  ~and ~do Nicodemus of-living-servant
  9  [linen] and cover two body and then-~exist [linen] and
 10  inside-put Nicodemus name-end-to Lord-Jézus and
 11  Lord inside tomb close and leave seal* say to-Lord two-two soldier from*
 12  were_opened* Jerusalem head ~and [the_veil] go [part] end this
 13  holy-gospel

## 054v — a rubric, naming Mark

> Here begins this holy gospel, written by Saint Mark.

  1  here_begins this holy_gospel write holy-Mark

## 055r — the three women at the tomb

> in the seven chapter of his writing: at that time, when they went the three Marys [bought] to the tomb of Christ, because they had prepared [spices] another [anoint] […] Jesus: Mary Salome, and Mary the mother of James, and Mary Magdalene. And then these Marys [and] these Marys among [Salome] […] […] the stone from the tomb; and then | Mary came to the tomb of Christ, and saw the three Marys [the sabbath] the tomb [rolled away]; and then the three Marys within this the three Marys and they went in the three Marys and remain saw […] Jesus; but they saw one

  1  inside seven chapter-leave of-write time then-exist
  2  go the_three_Marys [bought] tomb Christ because-exist prepare
  3  [spices] another this-cut_off [anoint] ~exist-[?] Jézus
  4  Mary Salome and Mary James mother and
  5  Mary Magdalene and then-exist this-two-Mary [and] this-two-Mary
  6  among [Salome] among-Mary-+the_three_Marys-[?]-+one-Mary
  7  from-?again from stone on-tomb and then-exist | go_on-+three
  8  Mary to-tomb Christ and see the_three_Marys [the_sabbath]
  9  SUBJ tomb from [rolled_away] and then-exist the_three_Marys inside this
 10  the_three_Marys and inside-to-go the_three_Marys and
 11  remain* see ~exist-[?] Jézus but see first^

## 055v — be not afraid, he is risen

> angel, sitting on the left side, from [a young man] within cover […] Jesus. And then Mary, through was afraid, because Mary supposed as a ghost. And then the angel: be not […] [be affrighted] the three Marys be not afraid. He is risen, whom ye mourn — the Lord Jesus, whom they crucified, is risen seek; but […] within Galilee and […] his apostles, and Peter […]. Here ends this holy gospel. And […] these women went […] from the tomb of Christ; and | Mary Magdalene went back to the tomb of Christ. At that time

  1  angel sit on-left direction from [a_young_man] inside exist
  2  cover ~exist-[?] Jézus and then-exist Mary through
  3  startle because rather-Mary supposed* SUBJ how? ghost
  4  and_then angel do_not ~have-+the_three_Marys [be_affrighted]
  5  the_three_Marys through startle rise mourn to-Lord from Jézus
  6  crucify^ rise seek* but go-+the_three_Marys
  7  inside Galilee and say-+the_three_Marys
  8  of-Lord disciple^ and Peter say-+the_three_Marys side^ this
  9  holy-gospel and [?]-+the_three_Marys go this woman
 10  head from this tomb Christ and | return
 11  return back Mary Magdalene to-tomb Christ time

## 056r — Mary Magdalene takes him for the gardener

> the Lord Jesus appeared to Mary Magdalene in the form of a gardener. And then this gardener, the Lord Jesus Christ, | [said to] this woman: why [came] woman, weepest thou for the Lord? He, Jesus, whom they crucified, is risen, because […] said […] […] […] light […] […] […] the tomb pierced, and the tomb light […]; and […] […] is risen. And the Lord Jesus stood before Mary Magdalene in that place; Mary [turning] that […] Master! And the Lord […] to Mary: go to the apostles. And Mary went to these two sisters, the women,

  1  appear Lord-Jézus Mary Magdalene inside form from one
  2  gardener and_then this gardener-Lord-Jézus-Christ | this
  3  woman who-shore [came] woman mourn to-Lord this from
  4  Jézus execute rise seek* because
  5  say who-before [risen] see-[?] light on-+heaven
  6  town-chapter-in_turn stooped_down* tomb pierce and tomb SUBJ
  7  light from-gate and verily can that rise
  8  and leave Lord-Jézus before Mary Magdalene
  9  on-to-place Mary [turning] on-reason that
 10  this-Lord Master and Lord SUBJ to-Mary-apostle go-Lord-apostle
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
  5  you of-Lord have_mercy somebody to and believe
  6  inside Lord and inside of-Lord from God_the_Father chapter-oh.
  7  chapter-oh amen and_then Lord-Jézus SUBJ
  8  the_three_Marys see-Mary inside tomb brother-chapter
  9  from Jézus execute and say Mary Magdalene that*
 10  Lord-Mary see-Mary rise on-die and
 11  leave Lord-Jézus-Christ among the_three_Marys this apostle holy-gospel

## 057v — an Old Testament prophecy, and Mark again

> Written by Saint […] the prophet, the prophet, in the Old Testament, truly, the sixth chapter of his writing, and Saint Mark seven it is written. Said Saint […] the prophet: because he saith […] it is found, in the Old Testament is truly written this word: the Lord shall rise from the dead. The King — thanks to the Lord [not]; and the Lord Christ destroyed the evil one; and […] […] the evil one […] Lucifer. This is written | Saint Mark, in the seven chapter of his writing: when the Lord Christ upon the cross breathed out his soul, the earth quaked, the rocks and stones rend; the sun and the moon

  1  write holy-NAME.prophet
  2  prophet Old_Testament righteous
  3  six chapter-leave of-write
  4  in_turn holy-Mark seven
  5  write say holy-NAME.prophet
  6  because say SUBJ exist find
  7  inside Old_Testament righteous write this word stand_up-Lord on-die-Lord
  8  king to-Lord thanks [not] and destroy Lord ~evil Christ and from
  9  [Adam] [bound] ~evil can Satan this_is write | to
 10  holy-Mark inside seven chapter-leave of-write then-exist Lord
 11  Christ on_the_cross of-Lord soul exhale earth quake
 12  rock stone this rend sun and moon this

## 058r — the harrowing of hell

> were darkened; and all creatures into the world humbled themselves; and all creation mourned when Christ was crucified. And four hours the Lord Jesus suffered upon the cross; and the Lord within the tomb | the apostles laid him, […] and then they laid the Lord within the tomb; and at that hour there came from God the Father in heaven, from the Father, an angel into […] the Lord Jesus; and rise […] and the angel within the tomb stay and the Lord went […], and destroyed the evil one; and he who the people who died within a hundred years, and within | five […] and within […] and […] all the prophets went into hell; and [brought out] three souls, all out the Lord went, and the three souls within the evil one's […] the Lord |

  1  eclipse and every [...] into_the_world* this humble and every create mourn
  2  then-exist Christ crucified and two-two hour
  3  on_the_cross suffer Lord-Jézus and Lord inside tomb | put-apostle
  4  Mary-angel and then-exist-Lord inside tomb lay Lord and
  5  hour time go from-father God heaven
  6  on-of-father angel inside ~exist-[?] Lord-Jézus and
  7  rise* from ~pray in_turn angel inside tomb stay
  8  in_turn to-Lord go-Lord on-~evil and ~evil destroy and he_who*
  9  people die inside one hundred-year and inside | five
 10  sit-~year and inside nine-[?] and nine-~year every prophet
 11  go on-netherworld and [brought_out] three soul every out go Lord
 12  in_turn three soul inside ~evil stay Lord | speak.

## 058v — Adam's soul kneels to the Virgin

> Saint Augustine the doctor: within many years, and one soul [counsel] went into the eternal land; but when the Lord went to the souls, the Lord, and [brought out] three souls [and then] out the Lord went to the souls; and the Lord appeared to the blessed Virgin Mary; and Adam's soul knelt before the blessed Virgin Mary; and the maiden […] prayed; and blessed the blessed Virgin Mary; and all the souls stood before the blessed Virgin Mary; and within Paradise the souls, the Lord, the souls; and the Lord went to the souls; and then twenty-five(?) hours; and this was […] the sixth hour.

  1  holy-Augustine-church_father inside many-to-year and one soul [counsel]
  2  ~go inside heaven = but then-exist to-Lord
  3  to-soul-soul-soul-soul-soul go Lord and [brought_out] three soul
  4  every* out to-go Lord soul and Lord appear Lord
  5  to-happy virgin-Mary and kneel ~Adam soul
  6  before to-happy virgin-Mary and girl SUBJ-have_mercy
  7  ask and bless-year to-happy virgin-Mary
  8  and to-soul-soul-soul every leave before to-happy
  9  virgin-Mary and inside Paradise soul Lord soul
 10  and go Lord soul and then-exist two-ten-ten five
 11  hour and this out thirty-[?] six hour

## 059r — one line

> And on the third day the Lord Jesus Christ rose from the dead.

  1  to-and on_the_third_day from die stand_up Lord-Jézus-Christ

## 059v — the road to Emmaus

> Here begins this holy gospel, written by Saint Luke, in the first [chapter] of his writing: at that time, when there went two apostles out of Jerusalem into a […] and | […] was Emmaus; and then the two apostles […] of the living Lord Jesus; and then the two spoke of how the Lord was truly a man, truly the Lord, preaching, and many miracles he did [spoke of]; the two apostles; the Jews' chief crucified him. At that time there appeared to the two apostles the Lord Jesus, in the form of a traveller; and then

  1  here_begins this holy_gospel
  2  write holy-Luke one
  3  of-write time
  4  then-exist go two
  5  apostle Jerusalem inside one
  6  in_turn-chapter-in_turn and | exist-chapter
  7  ~year-+name exist Emmaus and then-exist to-high-two-apostle from living
  8  Lord-Jézus and then-exist two talk^ how?-Lord this-Lord
  9  exist righteous somebody righteous Lord ~preach who-and-this-and
 10  wonder^ do [spoke_of] of-two-apostle Jew
 11  head crucify^ time appear
 12  two-apostle Lord-Jézus form traveller and then-exist

## 060r — the Lord asks the two what they are speaking of

> The two apostles [drew near] Lord Jesus, and the two apostles began to talk, and the Lord spoke from among them; and then Lord Jesus: O my two apostles, are you not saying, two apostles, Lord, how, saying among [into heaven] have, two apostles, because they said the Lord Jesus Christ apostle that the two men spoke of the Lord, this Lord, the two Lord's apostles; the third Lord; and then Luke this [named] the way, the man, this Lord, this good remain [sad] how [knowest not] the miracles in Jerusalem afterwards, and how the man […] said, the chief truly crucified this Jesus; and the Lord came into the world, went went preaching, and this and that miracle he did

  1  two-apostle [drew_near] Lord-Jézus and two-apostle talk and
  2  Lord from-speak and_then Lord-Jézus oh of-Lord
  3  two-apostle ~brother say two-apostle Lord how? say ~among
  4  [one_another] have two-apostle because say exist Lord-Jézus-Christ
  5  apostle that* two somebody from-Lord speak this-Lord two
  6  Lord apostle three Lord and_then Luke this [named]
  7  way somebody this Lord this good remain* [sad]
  8  how? [knowest_not] SUBJ miracle Jerusalem ~do how?-to
  9  somebody [?]-+say head righteous
 10  crucify^ this Jézus and the_Lord into_the_world* go-Lord
 11  go-+SUBJ preach-[?] who-and-this-and miracle do

## 060v — the miracles, and the women's news they did not believe

> the blind, through him light; the dead, through him […] […] lame the body, and the evil, those possessed by the evil one, healed and the Lord […] was from […] […] he rose, and one said, the one baptized, the Baptist, the chief the news was of the Lord up he rose; the news the two apostles [certain] believed, who from the Lord, from the dead rose; because he is the Lord's, to the brethren rot this pleasing, and who from the Lord, from the dead rose; and then Lord Jesus you the two […] the man, to hide, the two believing

  1  eye-eye ~blind SUBJ through light die SUBJ resurrect | lame
  2  lame body and evil^ possessed heal
  3  and Lord SUBJ exist from [the_third_day] up
  4  stand_up-Lord and say one ~woman ~head
  5  news exist-Lord up stand_up-Lord news two
  6  apostle [certain] believe who from Lord from die
  7  stand_up-Lord because he_is* of-Lord brother-to
  8  rot this pleasing who from Lord from
  9  die stand_up and_then Lord-Jézus you two
 10  ~exist-+baptize-to-~humble somebody to-hide believe-two

## 061r — O fools and slow of heart, and Cleopas is named

> Is it that these, to him, rise from the […] And then Lord Jesus left; the Son of God died more than these, rise from the, from the the Lord, from the eternal Father, and began, through Lord Jesus expounded from Adam, the trespass, written said; and then Cleopas, Luke, this Lord, to the two [foolish] the Lord wished good, said; and then Lord Jesus from Abel […] signified this Jesus crucified, how, in turn [slow of heart] died, the brother's he said and this Jesus died, the Lord's brother; and then Lord Jesus, the trespass Noah

  1  ~you-two this to-+SUBJ rise* from pray
  2  and_then Lord-Jézus leave exist die son God
  3  more_than_these* rise* from pray from pray
  4  the_Lord from God_the_Father heaven* and beginning^ through
  5  explain Lord-Jézus from ~Adam ~trespass scripture^
  6  say and_then Cleopas Luke this Lord to-two [foolish]
  7  want-Lord good say and_then Lord-Jézus from Abel
  8  Abel symbolize this Jézus execute how? | in_turn
  9  [slow_of_heart] die of-brother he_said* and this Jézus
 10  die of-Lord brother and_then Lord-Jézus trespass Noah

## 061v — Abraham as the figure of the crucifixion

> […] signified this Jesus crucified, he is […] redeemed every people in [the wood] this [Isaac] and on this Jesus crucified, saved every one, Adam gained; and then Lord Jesus, above; Abraham — Abraham's [deed] signified this Jesus crucified, and Lord Jesus said, said the Lord. Abraham, to the Lord's angel — Abraham gave his son […] and the Lord […] […] who did, Abraham on tie up the faggots […] in turn Abraham took sword who Isaac wished to slay

  1  ~Noah symbolize this Jézus execute he_is* ~Noah
  2  redeem every people* inside [the_wood] this [Isaac] and on-this Jézus
  3  execute be_saved every ~Adam gain and_then
  4  Lord-Jézus near^ Abraham Abraham symbolize this
  5  Jézus execute and say Lord-Jézus say exist Lord_God.
  6  Abraham on-~angel of-Lord_God Abraham take^
  7  of-son Isaac and Lord sacrifice.
  8  on-to-+offering who do Abraham on
  9  tie_up faggot on-+Isaac in_turn Abraham
 10  take^ sword who Isaac want slay

## 062r — the mount, the ram, and the angel

> And then he went on this, to the mount […] wished sacrifice and then Isaac O my father donkey and went far […] and a, and the ram, and a lamb the young men Isaac father sacrifice and said from father Abraham, from the brethren, the Lord […] offering and then tie up bundle of wood of Isaac living, the Lord wished to slay, and the Lord cried in the cloud to the angel go away Abraham, to the whole wide world, the Lord's love, this is

  1  and then-exist go on-this to-mount [?]-+Isaac
  2  want sacrifice and_then Isaac oh
  3  of-father donkey* and go far
  4  to_whom-+one and one and sheep and one
  5  lamb brethren* Isaac father sacrifice and say
  6  from-father Abraham from brethren* Lord_God ox.*
  7  offering and then-exist tie_up bundle_of_wood*
  8  of Isaac ~sheep-living want Lord slay and
  9  shout Lord_God in_the_cloud on-angel leave
 10  Abraham to-all_the_world SUBJ Lord of love this_is

## 062v — he made as though he would go further, and they constrained him

> Lord peace and then Lord Jesus, he is, was Isaac as he gave his father's [son], so this Jesus was crucified the Lord gave, his divine Father, and he rose the Lord from the […] because the Lord from the […] from the Father, eternal God; and then the Lord's apostles went, this in turn and then Lord Jesus went, the two apostles, you, because this Lord the Lord had a long way; and the Lord began, the two apostles persuaded; and then the Lord was, the two apostles persuaded, and the two the Lord's apostles went, and then the Lord's two apostles into the room went the Lord's two apostles, and the two apostles sat the Lord at the table, and

  1  Lord peace and_then Lord-Jézus he_is* exist Isaac
  2  to-grab of father this and this Jézus execute exist
  3  to-grab-Lord of-Lord God_the_Father and SUBJ rise*
  4  Lord from ~pray because-+the_Lord from ~pray from-father
  5  God heaven* and then-exist go-apostle-Lord this in_turn-chapter-in_turn
  6  and_then Lord-Jézus go-two-apostle you because this-Lord
  7  have-Lord long way and Lord beginning^ two apostle
  8  persuade and then-exist-Lord exist two-apostle persuade and | two
  9  apostle-Lord go and then-exist two-apostle-Lord on-+room | go
 10  two-apostle-Lord and sit-two-Lord-apostle to-throne and

## 063r — the breaking of bread, and he vanished out of their sight

> the two apostles carried cup water and wine. Lord Jesus took one cup and cup [he blessed] this, how, then [vanished] […] and from […] today's, and wine, and the cloud Lord Jesus blessed; and then the two apostles ate, the two apostles, and the two apostles drank, in the place, to the two apostles in the Holy Spirit, the farm, truly the Son of God to Lord Jesus; the two apostles, he left them, and go away among the two apostles, Lord Jesus Christ, the chapter answered to the Lord [vanished] the two apostles saw. Here ends this holy gospel.

  1  carry apostle the_rest^ cup ~water and wine and.
  2  grab Lord-Jézus one cup and cup
  3  [he_blessed] this how? then-exist [vanished] °alone-[?]
  4  and from bread and wine and cloud
  5  bless Lord-Jézus and then-exist the_rest^ apostle | eat-two
  6  apostle and drink-two-apostle on-place to-two-apostle
  7  on-spirit holy-farm SUBJ righteous son God
  8  to Lord-Jézus the_rest^ apostle of-to-leave-this and
  9  leave among the_rest^ apostle Lord-Jézus-Christ chapter-?answered
 10  Lord-to [vanished] see-two-apostle here_ends this holy_gospel

## 063v — Thomas was not with them

> Here begins this holy gospel written by holy John in the twentieth chapter of his writing. At that time the apostles were found in Jerusalem in one house, six in the Lord's house, where the Lord Lord Jesus, after supper; and then holy Thomas went Didymus one Saturday evening, to the apostles; and the apostles said, Thomas, apostle, we have seen the Lord. And holy Thomas said, I do not believe this at all; unless I hide this, unless Thomas believes […] not, unless he sees Thomas the Lord's end, and unless Thomas puts his finger in […]

  1  here_begins this holy_gospel
  2  write holy-John
  3  within^ two-ten-ten chapter-leave
  4  of-write time
  5  ~find disciple^ within^ Jerusalem
  6  within^ one house six
  7  within^ Lord house where Lord_God
  8  Lord-Jézus dinner ~do and then-exist go holy-Thomas Didymus*
  9  one Saturday evening to-apostle and say-apostle Thomas disciple^
 10  see Lord and say holy-Thomas this-Thomas this not believe
 11  every this this-hide this-Thomas this believe if not | see
 12  Thomas of-Lord side^ and of-Thomas finger not put within^ | of

## 009r — reach hither thy finger, and my Lord and my God

> the Lord's end, who from the Lord, rose from the dead; at that time Lord Jesus Christ left into the midst of the apostles closed and said, you have the commandment, and judge; he left the apostles in turn; Thomas began have and Lord Jesus said, Thomas, thou shalt go to put thy finger, Thomas, into the Lord's wound [blessed] see and believe; and [have not] Lord Jesus, the Lord's wound and Lord Jesus said, Thomas, blessed are they, and the man who sees and believes but and blessed are they, and the food he sees from believe. Here ends this holy gospel. And he kneeled, holy Thomas, before Lord Jesus, and holy Thomas said, Lord, Thomas's God; Thomas asked this of the Lord, have mercy on Thomas, who through sin against this Lord

  1  Lord side^ who from Lord from die stand_up time stand^ Lord-Jézus-Christ
  2  middle disciple^ closed and say peace^ you exist and judge stand^
  3  disciple^ in_turn Thomas begin have and say Lord-Jézus Thomas
  4  go-+name to put of-Thomas finger within^ of-Lord wound
  5  [blessed] see believe and [have_not] Lord-Jézus of-Lord wound
  6  and say Lord-Jézus Thomas happy-to from and somebody see
  7  and believe but and happy-to from and food see
  8  from* believe here_ends this holy_gospel and kneel
  9  holy-Thomas before Lord-Jézus and say holy-Thomas Lord
 10  of-Thomas God of-Thomas ask-Thomas this-Lord_God
 11  have_mercy Thomas who this-Thomas commit sin against this-Lord_God

## 009v — Thomas blesses him, and the Good Shepherd begins

> Thomas, this Lord, Thomas believed remain this Lord truly the Son of the living God. And then Thomas blessed Lord Jesus Christ. And have mercy on Thomas's sin. And Lord Jesus said, every [my] and [God] [my] from [that day] believing in Lord Jesus Christ, every gentile man and Jew […] have mercy on sin. Here ends this apostle's holy gospel; blessed be the Lord. Here ends this holy gospel. Written by holy John in the tenth chapter of his writing. At that time Lord Jesus said […] supper, apostles, to his Lord, this good Lord, before the son, in turn, you, from the apostles

  1  this-Thomas this-Lord believe-Thomas remain* this-Lord righteous
  2  son living God and then-exist Thomas exist bless Lord-Jézus-Christ.
  3  and sin Thomas find_mercy^ and say Lord-Jézus every [my] and [God] [my] from
  4  [that_day] on-believe to-Lord-Jézus-Christ every heathen man^ Jew
  5  above-pagan sin find_mercy^ side^ this apostle holy-gospel on-Lord_God bless
  6  here_ends this holy_gospel
  7  write holy-John
  8  inside ten chapter of-write
  9  time say Lord-Jézus
 10  on-who-+who-to dinner apostle
 11  of-Lord this-Lord good shepherd in_turn you from apostle

## 064r — the good shepherd and the hireling

> his sheep, and the Lord knows his sheep, and this Lord knows his sheep. And then Lord Jesus: then there was a king, and then he had two shepherds, one who kept the house well, a shepherd; the other in turn a hired shepherd. And then, of the two shepherds […] from one herd of sheep of this king; and then came the wolf to this sheep, and would carry this sheep away and this hired shepherd, of the shepherds leave this sheep; in turn the good shepherd, of the house, of the shepherds redeemed this sheep, and made the sheep ready in the herd and took it into the good keeping, and one carried away, and

  1  of-Lord sheep and Lord ~know of-Lord sheep and
  2  this-Lord ~know of-Lord sheep and_then Lord-Jézus | then
  3  exist one king and then-exist ~have two shepherd
  4  one ~who home good shepherd in_turn-two labourer
  5  shepherd and then-exist from two shepherd chapter-[?] from one
  6  herd sheep this king and then-exist go wolf
  7  this sheep and want this sheep from-~carry
  8  and this labourer shepherd from shepherd leave
  9  this sheep/a_female_person in_turn-this good shepherd home from shepherd
 10  redeem this sheep/a_female_person and sheep/a_female_person prepare inside herd
 11  and inside-good-exist-to give^ and one from-~carry and

## 064v — the good shepherd giveth his life, and other sheep I have

> in turn who […] out this herd, and went. The wolf, and the sheep carried away; and then Lord Jesus: he who is the good shepherd, of the shepherds, lays down his living for his sheep; and the Lord takes and one [fold] he who is the good shepherd, of the shepherds, is the gate of his sheep; and then they hear the voice of the Lord; the sheep […] the shepherd go; and then Lord Jesus, his apostles, one creature […] one sheep and these sheep I will bring to you blind and go you shall be every one, one shepherd, shepherds one; thanks to the Lord. Here ends this holy gospel.

  1  in_turn-who rebuke-trespass out this herd and go.
  2  wolf and sheep from-~carry and_then
  3  Lord-Jézus to-+he_who good shepherd from shepherd put
  4  down of-Lord living to-of-Lord sheep/a_female_person and grab-Lord
  5  and one [fold] he_who good shepherd from shepherd
  6  SUBJ ~gate of-Lord sheep and then-exist hear
  7  voice of-Lord_God sheep ~blind-Lord shepherd go and_then
  8  Lord-Jézus apostle of-Lord [...] [?]-°by_night one sheep/a_female_person
  9  and this-sheep want to-you ~blind go and
 10  you exist every one shepherd shepherd
 11  one to-Lord thanks Lord_God here_ends this holy_gospel

## 065r — beware of false prophets

> Here ends this holy gospel. Written by holy Matthew in the last of his writing. At that time, then the chapter of the day of Lord Jesus Christ, thirty, three days. At that time Lord Jesus said to his apostles, go, and to you lamb believe false prophets, pagan, evil [clothing] they are pagan evil, the Lord's trespass [ravening wolves] mouth the apostles, men, and the pagan evil believe, because they are false

  1  here_ends this holy_gospel
  2  write holy-Matthew
  3  inside seven of-write
  4  time | then-chapter
  5  day Lord-Jézus-Christ
  6  thirty three_days
  7  time say Lord-Jézus
  8  apostle of-Lord go to-you in_sheep's clothing
  9  false prophet pagan evil [clothing] exist pagan
 10  evil trespass Lord [ravening_wolves] mouth* apostle man^
 11  and pagan evil clothes^ because exist false | of

## 065v — by their fruits ye shall know them

> the Lord's name confess; and then Lord Jesus, to his apostles, verily verily this Lord spoke to you; and then Lord Jesus: do not pick figs from thistles, but rather from the fig, and […] food, grapes thornbush not from the grapevine, because he who is a good tree brings this good fruit; in turn likewise the evil tree brings this evil of hell. Because a good tree cannot bring forth the evil of hell, every good fruit it brings; in turn likewise the evil tree cannot bring good fruit, but every evil of hell it brings. And then Lord Jesus, many people were crying out against the judgment the Lord's year, to the Lord; this man's trespass; this the Lord preached, and Lord Jesus said

  1  Lord name confess and_then Lord-Jézus apostle of-Lord
  2  verily verily this-Lord you speak and_then
  3  Lord-Jézus pick_not fig on-thistle ~but on-fig and | pick_not
  4  food grape thornbush* ~but on-grapevine
  5  because he_who* good tree this good_fruit grab | in_turn
  6  ~if die-evil tree this die-evil-hell grab
  7  because good tree can die-evil-hell grab ~but
  8  every good_fruit grab ~if die-evil tree
  9  can good_fruit grab ~but every die-evil-hell
 10  grab and_then Lord-Jézus many people exist shout | on-judge
 11  year Lord to-Lord this man^ trespass this Lord preach and say Lord-Jézus

## 066r — the weeping and gnashing of teeth

> and […] the man who can speak of the Lord, go to the Lord, the Lord's heart the man, and the Lord saved every one, Adam gained, this man [shall enter] the year out, the man chapter of his Father, and this man every man [shall enter] into [many] the heavenly home of his Father; but every one goes, the man, to hell fire; there is seen the gnashing of teeth and crying for ever; in turn, and the man is [not] the man says, three, Lord upon Lord upon Lord, saved by the Lord, every people, this man every one goes into [many] the heavenly home of his Father; there is the man's judgment, to the Lord, and the angels, and his Lord Father God, for ever, amen. Here ends this holy gospel.

  1  and [whosoever] man^ can-say-Lord go Lord_God Lord heart | of
  2  man^ and be_saved Lord every ~Adam gain this man^
  3  [shall_enter] out-year man^ chapter* of-Lord God_the_Father and this man^
  4  everybody = [shall_enter] inside [many] heaven^ home of-Lord
  5  God_the_Father but every go man^ on-chapter-oh chapter-oh hell
  6  fire there exist see grinding tooth weep^
  7  chapter-oh chapter-oh in_turn and man^ exist [not] man^
  8  say three Lord-chapter-Lord-chapter-Lord be_saved Lord every people* this man^
  9  every go inside [many] heaven^ home of-Lord God_the_Father there
 10  exist man^ judge to-Lord and angel and of-Lord-father
 11  God chapter-oh chapter-oh amen here_ends this holy_gospel

## 066v — whatsoever ye shall ask the Father in my name

> Here begins this holy gospel written by holy John in the fourteenth chapter of his writing. At that time Lord Jesus said to his apostles, at the last supper, verily verily this the Lord spoke to you: love. Whatsoever ye shall ask of the Lord's Father in the Lord's name, ye shall all receive it saved from heaven, from this Lord Christ. And this Lord Jesus spoke, saying, on the way, to his apostles, and said, O the Lord's son.

  1  here_begins this holy_gospel
  2  write holy-John
  3  fourteen-+one chapter of-write
  4  time say Lord-Jézus
  5  apostle of-Lord at_the_Last_Supper =
  6  verily verily this-Lord you speak love
  7  whatever you exist ~ask from of-Lord-from God_the_Father
  8  inside of-Lord name every you be_saved grab
  9  from heavenly from this-Lord Christ and this say speak Lord-Jézus
 10  on-way apostle of-Lord and say oh of-Lord son.

## 067r — whose son is he, and thou art the Son of the living God

> Judge this: whose son is he? yours the apostles spoke to the Lord, and the apostles said, the apostles answered, this Lord believe that this Lord [sat] truly the Son of the living God. And Lord Jesus said, O the Lord's son, this Lord casts this out; if you believe this, it is to the Lord that this Lord is truly the Son of the living God […] and […] yours believe, believing, because this Lord who goes to the death, to the Lord's death […] ask this of you [shall be raised] in the Lord herd the apostles, because you are apostles, many sorrowing on the Lord you have, because you apostles, all the apostles [oh Lord] […] go and go mourn and to and one and

  1  ask^ this-Lord you whose? son | ~you
  2  yours to-Lord speak apostle and say apostle answered apostle this Lord
  3  believe that* this Lord [sat] righteous son living God and say
  4  Lord-Jézus oh of-Lord son this-Lord this exorcise
  5  if-to you this believe exist to-Lord
  6  this-Lord righteous son living God mouth-+who and [?]-+one | ~you
  7  yours believe ~brother because this-Lord who-go
  8  on-die to-Lord-die name-[?] ~ask this-Lord you [shall_be_raised]
  9  inside Lord herd apostle because you exist apostle many sad
 10  on-Lord have because you apostle every apostle | on-apostle-chapter
 11  [oh_Lord] [...] go-go mourn and to-and one and

## 067v — he that believeth and is baptized shall be saved

> one [died] and this Lord, on the third day, rose again. He stood up, and this Lord, believing in you, within belief, afterwards believe there is a leaving; for ever, amen. And the two men [sendeth] you, and the apostles are one God; the apostles believe, and the man who is outside this believe and one man is saved, but every man is damned and the man who believes in […] Christ, this whosoever shall be saved, because this is to the Lord, one God. Here ends this holy gospel. whatsoever the man has, he asks in Jesus' name he is saved, speaks holy Paul the apostle

  1  one [died] and this-Lord on_the_third_day one-?again.
  2  stand_up-to and this-Lord you ~brother inside
  3  believe ~do believe* exist
  4  leave-chapter-leave chapter-oh chapter-oh amen and two
  5  somebody [sendeth] you and exist apostle one
  6  God believe apostle and somebody exist out this believe
  7  and one somebody be_saved but everybody = be_damned
  8  ~to and somebody exist believe inside [?]-~Christ this
  9  whosoever* exist be_saved because this to-Lord one God
 10  here_ends this holy_gospel whatsoever* have somebody ask
 11  inside Jézus name be_saved speak holy-Paul apostle

## 068r — love the Lord, and thy neighbour as thyself

> this word, Paul's brethren; Paul the man has, he asks in Jesus' name; three things Paul the man asks; in turn the brethren, Paul the man would be saved first; he asks, the man, Paul: love the Lord most high with all the heart, and every man as his neighbour as the neighbour; and the man shall be saved. In turn the second he has, Paul the man asks, in Jesus' name go away believe; Paul the man asks of Lord Jesus, in his name. The third Paul the man has, he asks, in Jesus' name, saved by Lord Jesus, in his [believeth] name, and the man shall be saved. Here ends this apostle's holy gospel.

  1  this word brother of-Paul have somebody-Paul ask
  2  inside Jézus name three ask-somebody-Paul | in_turn
  3  brethren* want-somebody-Paul be_saved first | ask-somebody
  4  Paul love Lord_God highest all^ heart and everybody = how?-to neighbour
  5  to-+neighbour and exist somebody be_saved in_turn-two have
  6  somebody-Paul ask inside Jézus name leave
  7  believe ask somebody-Paul from Lord-Jézus inside of-Lord
  8  and-to-end-+name third have somebody-Paul ask | inside
  9  Jézus and-to-end-+name be_saved from Lord-Jézus inside of-Lord
 10  [believeth] and-to-end-+name and exist somebody be_saved end
 11  this apostle holy-gospel

## 068v — of sin, and of righteousness, and of judgment

> Here begins this holy gospel written by holy John, in the sixteenth chapter of his writing. At that time Lord Jesus said to his apostles, at the last supper: this Lord goes to his Father; you learn, he does, heaven and earth, that is, this Lord go away to the death; the Lord dies, and this Lord goes from you […] the day; in turn he who, this Lord, this dies for you go not away the Holy Spirit; the Lord dies, and this Lord, to you the Holy Spirit goes, and you shall see two judgments: first of sin; in turn the second of righteousness; the third, judgment

  1  here_begins this holy_gospel
  2  write holy-John inside
  3  ten-six chapter of-write
  4  time say Lord-Jézus
  5  apostle of-Lord on-last
  6  dinner this-Lord go-Lord of-Lord God_the_Father you learn
  7  do heavenly land that_is this-Lord leave*
  8  on-die Lord die and this-Lord you go | [the_Paraclete]
  9  day in_turn-who this-Lord this die to you go_not_away
 10  holy-spirit Lord die and this-Lord you
 11  go holy-spirit and you exist see-two
 12  judge first from sin in_turn-two from righteous third judge

## 069r — the Spirit, the tongues, and the signs

> And then this Holy Spirit goes to you, from the Spirit through it you receive humble every good thing, and there are apostles new who lift up tongues say [truly] you shall have many miracles say which the mouth speaks in the Old Testament word, and it lives goes before […] […] […] the day of judgment because there are many miracles afterwards. Here ends this holy gospel. Here begins this holy gospel written by holy Luke, in the tenth the last chapter of his writing. Said Lord Jesus to his apostles, at the last supper, this Lord grapevine his Father

  1  and then-exist you go this holy-spirit from-spirit
  2  through grab you humble every good and exist
  3  apostle new who-ascend language say [truly] you exist many
  4  miracle say which-mouth exist inside Old_Testament word and living exist
  5  go before [all_men] ~baptize [until] judge-~year
  6  because-exist many miracle ~do here_ends this holy_gospel
  7  here_begins this holy_gospel
  8  write holy-Luke inside | ten
  9  seven chapter of-write say
 10  Lord-Jézus apostle of-Lord | on
 11  last dinner this-Lord grapevine God_the_Father of-Lord SUBJ

## 069v — I am the vine, ye are the branches

> the vineyard; in turn you are the branches, and the Father, the Lord's vineyard, the angel […] this […] […] and without a name […] […] name he takes this and cuts it off, and vine branch out onto the way throw out and then Lord Jesus, and the man who is within the Lord, carried by the Lord, stays; and this Lord is within […]. And then Lord Jesus, to his apostles, O the Lord's son, this law and love the Lord carries; can the apostles [abide] understand what this Lord […] to you, speaking Lord; and the man who is in the Lord's commandment of love, the man carries, from the man who is within the Lord's law […] stays, and this Lord

  1  farm in_turn you vine_shoot and go
  2  God_the_Father of-Lord farm angel vine* this | name-Lord
  3  grapevine and without-+name vine_shoot | [nothing]
  4  name take^ this cut_off and vine_shoot out
  5  ~way cast_out and_then Lord-Jézus and man^ exist
  6  inside Lord-[?]-~carry-Lord stay and this-Lord exist
  7  inside him and_then Lord-Jézus apostle of-Lord oh | of
  8  Lord son this law-love-~carry-Lord can apostle [abide]
  9  understand who this-Lord you [bear_fruit] | speak
 10  Lord and man^ exist of-Lord commandment-love carry-somebody from
 11  man^ exist inside Lord-+law-[?] stay and this-Lord

## 070r — the branch that beareth not is cast into the fire

> the Lord is within [my Father's house]; Lord Jesus said, who afterwards to his Father, this […] […] is good grape takes this and that vine branch […] from the Father of the Lord, upon whom every grape carries; and the Lord's Father goes two evil vineyards, and this in turn what vine branch takes the evil vineyard, and throw out to the evil fire there is seen the gnashing of teeth and crying, for ever. And then Lord Jesus, he is from his Father the Lord loves, and this Lord loves you; and Lord Jesus said, O the Lord's son, and you love, because the apostles are in love

  1  exist-Lord inside him say Lord-Jézus who ~do
  2  to-God_the_Father of-Lord this vine_shoot [withered] exist | good
  3  grape grab this-and-this vine_shoot from-~blind from-God_the_Father
  4  of-Lord who-chapter every grape carry and go father of-Lord
  5  two evil farm and this in_turn-what vine_shoot
  6  grab evil farm and SUBJ cast_out on-~evil
  7  fire there exist see grinding tooth crying chapter-oh
  8  chapter-oh and_then Lord-Jézus he_is* from-God_the_Father of-Lord
  9  Lord love and this-Lord you love and say Lord-Jézus oh
 10  of-Lord son and you love because-exist disciple^ inside-love

## 070v — ask in my name, and Paul's three askings again

> in the commandment you are, the Lord's ten laws of love the apostles carry Lord Jesus said, and the man who carries [in my name] […] […] you first […] love the Lord, whatsoever it is ye shall ask of the Father, of the Lord's Father, in the Lord's name, ye shall all receive it saved. Here ends this holy gospel. whatsoever the man has, he asks in Jesus' name he is saved, speaks holy Paul the apostle this word; Paul's own; whosoever Paul asks in Jesus' name; three things Paul the man asks if Paul the man would be saved, first he asks

  1  inside commandment you exist of-Lord law-love-ten carry-apostle
  2  say Lord-Jézus and somebody exist carry [in_my_name] this-?Pharisees-+one
  3  [must] you first say Lord love whatever | ~you
  4  exist ~ask from-God_the_Father from of-Lord from-God_the_Father inside
  5  of-Lord name every you be_saved grab
  6  here_ends this holy_gospel whatsoever* have somebody ask
  7  inside-Jézus name be_saved speak holy-Paul apostle
  8  this word exist-exist of-Paul have ~somebody-Paul
  9  ask inside-Jézus name three ask somebody-Paul
 10  if want somebody-Paul be_saved first ask

## 071r — the great commandment, repeated

> Paul the man: love the Lord most high, literally with all the heart, and every man as the neighbour […] and the man shall be saved. In turn the second Paul the man has, he asks, in his […] and was named go away believe; Paul the man asks of Lord Jesus, in the Lord's name. The third he has, Paul the man asks in the Lord's name, saved by Lord Jesus, in the Lord's name; and the man shall be saved. Here ends this apostle's holy gospel [amen] Here begins this holy gospel, written by holy Luke, in […] of his writing. Lord Jesus said to his apostles at the last supper: you shall be driven out

  1  somebody Paul love Lord_God from literal every heart and everybody = | how?
  2  to neighbour [?]-from-°creature and exist somebody be_saved
  3  in_turn-two have somebody Paul ask inside of-Lord | and
  4  was_named* leave believe ask somebody Paul
  5  from Lord-Jézus inside of-Lord name third have
  6  somebody Paul ask inside of-Lord name be_saved
  7  from Lord-Jézus inside of-Lord name and exist
  8  somebody be_saved end this apostle holy-gospel [amen]
  9  here_begins this holy_gospel write
 10  holy-Luke inside [fourteen] | of
 11  write say Lord-Jézus apostle of-Lord
 12  at_the_Last_Supper = you | chase

## 071v — a woman when she is in travail hath sorrow

> cast out, for hearing; how one […] every for the Lord's name. And then you they will drive out, the apostles say; this is it: out, he who, apostle by apostle, Master spoke and the Lord, the Jews put to death; and you shall have much sorrow upon the Lord; in turn, one word, joy [shall be turned] your sorrow is […] until little how; then one woman, the chief, a son is born […] she has no more; in turn, then the son is born, and of that comes joy over the son and your sorrow, in turn, joy; much sorrow cast out, and that in the year of judgment; in turn your sorrow, much joy cast out, and that in the year of judgment. Here ends this holy gospel.

  1  say out on-hear how? one have_mercy-apostle-~believe every
  2  to-of-Lord name and then-exist you
  3  chase want apostle say this_is ~out he_who* apostle-apostle
  4  Master [spoke] and Lord Jew die and you
  5  exist many sad on-Lord have in_turn one say-exist
  6  joy [shall_be_turned] you sad exist and-ascend ~until
  7  little how? then-exist one baptize head
  8  son be_born remain* many not-not have in_turn | then
  9  exist be_born from-~exist on-son joy this-Peter
 10  and ~you sad in_turn-+say joy want many sad
 11  ~out and that* on-judge-year in_turn you sad many
 12  joy ~out and that* on-judge-year here_ends this holy_gospel

## 072r — after the crucifixion, they sit at meat in Jerusalem

> Here begins this holy gospel, written by […] in the twenty- fifth chapter of his writing. At that time, then, after the crucifixion of Lord Christ […] at that time then the apostles sat at table in Jerusalem, in the Lord's house, where the Lord Lord Jesus made the supper; at that time he appeared, the Lord Jesus, to his apostles, in […] name, the man; and he sat with the apostles at table and began to rebuke their unbelief

  1  begins this
  2  holy-gospel write
  3  holy_Mark inside | the_rest^
  4  ten-ten five chapter
  5  of-write time
  6  then-exist on-execute
  7  Lord-Christ [?]-~year time then-exist
  8  sit apostle at_table inside Jerusalem inside Lord house where Lord_God
  9  Lord-Jézus dinner do time appear | Lord
 10  Jézus apostle of-Lord inside ~brother-+name somebody and.
 11  sit to-apostle at_table and begin-admonish on-believe

## 072v — go ye into all the world, he that believeth and is baptized

> and Lord Jesus said, go ye, apostles, among the people, and baptize in the Lord's name; and the man who is baptized in the name of the Father and the Son and the Holy Spirit, and believes in the Lord, every such man shall be saved; and one is damned [shall perish] [but] and the man exist baptized, and believes in the Lord and one be saved but every man is damned [shall perish] [but] and the man who believes in the Lord shall do many miracles, all in the Lord's name; the man in the Lord's […] […] name: the blind through light, the dead see and rise up.

  1  and say Lord-Jézus you go teach^ among_the_people* and
  2  exist baptize inside of-Lord was_named* and somebody
  3  exist baptize inside name God_the_Father and son
  4  and holy-spirit and exist Lord-to believe
  5  everybody = be_saved and one be_damned [but]
  6  [-but] and somebody exist baptize and exist Lord-to
  7  believe and one be_saved but everybody =
  8  be_damned [but] [-but] and somebody exist Lord-to believe
  9  from exist many miracle do every inside of-Lord
 10  name exist somebody inside of-Lord | and-exist
 11  [?]-+name ~blind through light die from-see resurrect rise^

## 073r — and these signs shall follow them that believe

> the man in the Lord's name, the evil in the man casts out; he carries serpents in the hand, and the man cannot be bitten; the man, in the Lord's name deadly poison drink and whatever the man not ill the man, in the Lord's name, at the cup […] of the man, why in turn he puts […] the man is healed, all in the Lord's name; the man does many miracles, and Lord Jesus said, this Lord goes to his Father, to you the Lord, and the Lord goes, and this Lord, to you goes the Holy Spirit, and the apostles new lift up tongues

  1  exist somebody inside of-Lord name evil inside
  2  somebody exorcise exist serpent carry inside
  3  hand ~exist somebody can bite exist somebody inside
  4  of-Lord name poison drink and what-to
  5  who somebody ~exist well exist somebody inside of-Lord
  6  name on-cup-[?]-~year of-somebody why?-in_turn put
  7  this-°sat-+SUBJ exist somebody heal every inside of-Lord | and-exist-from
  8  ~year-+name exist somebody many miracle do and
  9  say Lord-Jézus this-Lord go to-of-Lord from-God_the_Father to-you
 10  Lord and Lord_God SUBJ Lord go and this-Lord you go-Lord
 11  holy-spirit and exist apostle new who-ascend language

## 073v — he went on the way, and each time he said the same

> say and Lord Jesus said to his apostles, go, apostles today the mount; this Lord would go out truly, and the whole wide world; from his Father; and he passed on, from the apostles; in turn the apostles knew the Lord went and then the Lord looked on the apostles and said, peace be unto you and then the Lord passed on the way; and a second time he looked on the apostles and said, peace be unto you; and then the Lord passed on the way; in turn the apostles knew the Lord; on the Monday; and a third time he looked on the apostles and said, peace be unto you; and then the Lord passed on the way; and a fourth time he looked on the apostles and said, peace be unto you […] and then the Lord passed on the way; and a fifth time the Lord looked on the apostles and said, this Lord, to you, the eye

  1  say and say Lord-Jézus apostle of-Lord go-apostle today*
  2  mount this-Lord want-Lord ~out righteous and all_the_world of-Lord | from
  3  God_the_Father and trespass go-Lord from apostle in_turn apostle know Lord go apostle
  4  and then-exist from-see-Lord on-apostle and say-Lord law you
  5  and then-exist trespass go-Lord ~way and two from-see-Lord on-apostle
  6  and say-Lord law you and then-exist trespass go-Lord | on
  7  ~way in_turn apostle know Lord Monday-apostle and three from-see-Lord on-apostle
  8  and say-Lord law you and then-exist trespass go-Lord
  9  ~way and two-two from-see-Lord on-apostle and say-Lord law | ~you
 10  yours and then-exist trespass go-Lord ~way and five | from
 11  see-Lord on-apostle and say-Lord this-Lord you law eye

## 074r — he was received up into glory

> to his sufferer, and to his Father, for ever amen; because Lord Jesus would have him confess before his Father, in the year of judgment; then the Father goes to judge the living and the dead, the man; and the Lord said to the apostles, ye shall hear; his mother, and Mary blessed upon all the apostles, and among this earth […] knew Lord Jesus, and […] Lord Jesus […] sun went sky and blessed all the whole wide world and the Lord was taken into eternal glory. At that time said holy Peter: Master, how does this Lord have apostles, as it were, saying

  1  to-sufferer of-Lord and of-Lord from-God_the_Father chapter-oh chapter-oh
  2  amen because want Lord-Jézus to-Lord confess have
  3  before from-God_the_Father of-Lord on-judge-year then-exist
  4  go God_the_Father judge living and die somebody and say-Lord apostle
  5  you exist hear of-Lord mother and
  6  Mary bless on-every apostle and among this earth
  7  [after] know Lord-Jézus and [taken_up] Lord-Jézus | remain*
  8  sun go sky and bless the_whole wide world
  9  and Lord take^ to-?heaven glory* time say | saint^
 10  Peter Master how? this-Lord have apostle pray say

## 074v — the Lord's Prayer

> Lord Jesus, this his son, as the Father of the man and the Lord, in the eternal holy name of the Father; the man goes into the Father's kingdom; the whole wide world is the Lord's, as in heaven so on earth bread of the man, every year the Lord gives the man this day's bread; this man's trespass forgive, as the man forgives his own; joy the man goes into pleasing redeem from evil. Amen. Written by holy Matthew in his gospel. And the second time said holy Peter: Master, Lord, when shall be pass the year of judgment? Lord Jesus Christ said or out and out

  1  Lord-Jézus this of-Lord son pray God_the_Father of-somebody
  2  and-Lord inside heaven* be_hallowed^ name of-God_the_Father go man^
  3  inside kingdom^ of-God_the_Father exist all_the_world of-Lord how? heaven
  4  this and ~earth bread of-somebody every day^
  5  grab-Lord man^ today’s day^ this-somebody trespass
  6  forgive^ how?-to man^ forgive^ of-somebody joy
  7  lead us into temptation redeem from evil amen
  8  write holy-Matthew inside of gospel and two say
  9  holy-Peter Master Lord when? exist pass
 10  judge-year say Lord-Jézus-Christ or out-out

## 075r — two men in white apparel

> In turn, out and out, two thousand years. And the third time said holy Peter: Master, how shall the apostles good news write of the Lord? Lord Jesus said, one year write, apostles, literally; in turn the second, figuratively. And then the eternal gate was to Lord Jesus; and then Lord Jesus went into heaven, into glory; and the Lord's light departed, because Lord Jesus would have it so; then the Lord shone on the apostles of God, upon this world; and then the two appeared, two angels, white […] believe and then the two angels, to you apostles, O men, how see ye the Lord's joy? Jairus

  1  in_turn out-to-out two-to-?thousand-year and three say holy-Peter
  2  Master how? apostle gospel Lord write say Lord-Jézus one
  3  year write apostle literal in_turn two metaphoric and then-exist
  4  heaven* gate exist-to Lord-Jézus and then-exist
  5  go Lord-Jézus heaven glory* and Lord light from
  6  ~leave because would_like^ Lord-Jézus then-exist Lord
  7  apostle God shine on-this world* and then-exist-two
  8  appear two angel-angel white | clothes
  9  believe* and_then two angel-angel you
 10  apostle-oh-DIV-chapter man how? Lord joy see Jairus

## 075v — he shall so come, to judge the quick and the dead

> he departed, from the eternal; in turn, to the end, this joy the Lord would go to […] judge the living and the dead, the man. And the two said, these two angels, go, apostles, into the apostles, O; and the Lord find the apostle-man. And […] they saw; the word was done by the two angels. Here ends this holy gospel. Love the Lord with all thy heart. The Lord spoke, the apostles, Lord Jesus Christ; then the apostles prayed, his son, this Father of the man

  1  ~leave from_heaven* in_turn-chapter-end-chapter this joy
  2  would_like^ Lord go on-[?] judge living and die
  3  man^ and say-two this two angel-angel go-apostle within^
  4  apostle-oh-DIV-chapter and Lord find apostle-somebody.
  5  and [gazing] see word do two | angel
  6  angel here_ends this holy_gospel the_Lord love Lord_God be_loved
  7  speak-Lord apostle Lord-Jézus-Christ
  8  then-exist apostle pray
  9  of-Lord son
 10  this Our_Father

## 076r — how oft shall my brother sin against me

> [afterward] to the apostles many said say written [holy Paul] apostolic letter in the first chapter of his writing. At that time, then, Lord Jesus Christ in the thirtieth year, and three days, and five months, and three days, at that time left the apostles, to Lord Jesus; and then holy Peter answered, would the most high, this Peter, have mercy [how often] Peter is […] and then Lord Jesus Christ: Peter, Peter, in turn the brethren, one […] […] one year, through the sin of a man against this Peter; have mercy, the man, if the man goes to mercy, asks mercy, the man receives sun goes […] the man of mercy; and cried to Lord Jesus Christ

  1  [afterward] to-apostle many say say write [holy_Paul] apostolic_letter
  2  inside one chapter of-write time then-exist Lord-Jézus-Christ
  3  inside thirty year and three_days and five moon and three_days inside
  4  time leave-to-leave apostle ~to Lord-Jézus and_then holy-Peter
  5  answered want-high this-Peter forgive^ [how_often] exist Peter
  6  [then] and_then Lord-Jézus-Christ Peter Peter | in_turn
  7  brethren* one-[?] dry* one year commit sin somebody
  8  against this-Peter forgive^ somebody SUBJ if go somebody-have_mercy
  9  ask-have_mercy-somebody SUBJ grab sun* go
 10  understand-+say somebody-have_mercy and shout-to Lord-Jézus-Christ

## 076v — the catalogue of sins

> he departed on the water of heaven [walked] Peter, Peter, if rather a man among the apostles sins against you witness from […] the man, the apostle, the sin […] […] the man, of the man's sin, leave it; but if a man's sins are many, in turn he who is a thief; in turn robber; in turn a shedder of blood, that is a killer of men; the man in turn [adulterer]; the man in turn from [thief] the man in turn proud; the man in turn a drinker; the man in turn many [proud]; the man in turn under many yokes; this Peter said Lord Jesus Christ, because Peter is [pride] in turn in humble the man, this be damned how then the man dies in turn

  1  ~leave on-water heaven [high] Peter Peter if-°but_rather
  2  SUBJ somebody among apostle you sin witness* from
  3  heathen* somebody apostle sin witness* publican* somebody | of
  4  somebody-~sin leave but if-exist many somebody-~sin in_turn
  5  thief-who in_turn robber in_turn blood murderer that_is
  6  people-die somebody in_turn [adulterer] somebody in_turn from [thief]
  7  somebody in_turn proud somebody in_turn drink somebody in_turn many
  8  [proud] somebody in_turn many yoke-chapter somebody this-on-Peter
  9  say Lord-Jézus-Christ because exist Peter [pride] in_turn inside humble
 10  somebody this be_damned* how? then-exist somebody die in_turn

## 077r — one sin, and whosoever sins is damned

> Adam the man penance have mercy; the man in turn from riches [forgiven] the man in turn penance truly; the man, or the man judges of whom holy Paul speaks apostolic letter said Lord Jesus Christ, this [forgive] the man sins one sin penance he is saved; and he who hides the man [seventy times seven] heavenly in sin, to Lord Jesus Christ one sin penance is saved; but every one, whosoever sins, is damned said Lord Jesus Christ: Peter, Peter [if he hear thee not] that is [church] whosoever sins exist the apostle, this whosoever sins, from heathen witness […] the man, of […] leaves […] the man [with one] the voice [two or three] the brethren, the man says, this man

  1  Adam man^ penance* have_mercy man^ in_turn from-rich-from [forgiven]
  2  man^ in_turn penance* true^ man^ or ~judge man^
  3  who speak holy-Paul apostolic_letter say Lord-Jézus-Christ this [forgive]
  4  man^ sin one sin penance* be_saved and who-hide
  5  man^ [seventy_times_seven] heavenly* on-sin to Lord-Jézus-Christ
  6  one sin penance* be_saved but every ~somebody-~sin be_damned
  7  say Lord-Jézus-Christ Peter Peter [if_he_hear_thee_not] that_is [church]
  8  ~somebody-~sin exist apostle-this-~somebody-~sin from heathen* witness*
  9  publican* man^ of-[?] leave [as_the_heathen]
 10  man^ [with_one] voice [two_or_three] brethren-exist man^ say man^ this

## 077v — go to him alone, then take two, then three

> he loves Lord Jesus Christ more than these. Lord Jesus Christ said to Peter: in turn […] the apostle-man among […]; the man who sins, go to Peter, […] the sin, to the house; and the man upon his sin rebuke, because this man who sins suffers; in turn, to whom this man suffers exist the apostle, this whosoever sins, from heathen publican he looks; of […] he leaves; but Peter goes, to Peter, two […] the sin; and the man upon his sin rebuke, because this whosoever sins suffers; in turn, to whom this man suffers exist the apostle, this whosoever sins from […] […] the man, of […] leaves; but Peter goes, to Peter, a third time […] the sin, and the man

  1  SUBJ love Lord-Jézus-Christ more_than_these* say Lord-Jézus-Christ to-Peter
  2  in_turn [rebuke] apostle-somebody among [alone] somebody-~sin go | to
  3  Peter [?]-~sin to-home and somebody-on-~sin
  4  rebuke^ because this somebody-~sin sufferer in_turn to-which this-somebody
  5  sufferer exist disciple^ this ~somebody-~sin from heathen* publican*
  6  from-see of-[?] leave but go-Peter to-Peter two
  7  [?]-~sin and somebody-on-~sin rebuke^ because this ~somebody-~sin
  8  sufferer in_turn to-which this-somebody sufferer exist disciple^ this ~somebody-~sin
  9  from heathen* publican* man^ of-[?] leave but
 10  go Peter to-Peter three [?]-~sin and man^

## 078r — judge righteous judgment

> upon his sin rebuke, because this whosoever sins suffers; in turn, to whom this man suffers, take him, whosoever sins take from [appearance] within why in turn? because this is truly, truly, to whosoever sins; because a false judge according to judges whosoever, truly judge but rather every [by appearance] false judgment; in turn the false judge the true man falsely judged is damned, in the evil for ever; in turn the true judge, every one to whom he judges truly according to the judge falsely judging, but rather to whom he judges truly; the Lord speaks, every writing and every prophet and every church father and every forefather and evangelist

  1  on-sin admonish because this ~somebody-~sin sufferer in_turn to-which this-somebody
  2  sufferer grab ~somebody-~sin take* from [appearance] inside
  3  why?-in_turn because this exist righteous righteous to-~somebody-~sin because
  4  false ~judge-somebody according_to* chapter-judge-~somebody righteous judge
  5  °but_rather-every [by_appearance] false judge in_turn false ~judge-somebody
  6  righteous man^ false from-judge be_damned SUBJ inside ~evil
  7  SUBJ chapter-oh chapter-oh in_turn righteous ~judge-somebody every
  8  to-which-chapter righteous judge according_to* judge-somebody false
  9  from-judge °but_rather-every to-which-chapter righteous judge Lord_God speak every write
 10  and every prophet and every church_father and every forefather and evangelist*

## 079r — the orders of angels, and one word

> among all peoples, to eternal glory, most high, all the angels, the orders of angels [answered] eat literally, from the one Lord, truly somebody speaks holy Paul apostolic letter Paul's own, this Lord truly […] Lord Jesus Christ this Lord judges all peoples by one word [idle] the word, every man [give account] of the man, truly, good, mercy, saying, love, doing; and the Lord takes; this Lord truly […] and the Lord, every man receives [mercy] from the Lord [reward] the man the firstborn is damned, to be [bosom] […] [rest] damned [torment] [everlasting] [fire] and nine [orders of angels]

  1  inside every people* to-?heaven glory* highest every angel angel angel order
  2  [answered] eat literal from one Lord righteous somebody* speak holy-Paul
  3  apostolic_letter exist-exist of-Paul this-Lord righteous ~judge-+somebody Lord-Jézus-Christ
  4  this-Lord exist judge every people* one word [idle] word every
  5  somebody [give_account] of-somebody righteous-good-have_mercy-say-love-do and
  6  grab Lord_God SUBJ this-Lord righteous ~judge-+somebody and Lord_God every
  7  somebody exist grab [mercy] exist from Lord_God [reward] somebody
  8  firstborn exist be_damned to-~brother [bosom] on-~Lazarus [rest]
  9  be_damned [torment] [everlasting] [fire] and nine [orders_of_angels]

## 080r — the Comforter, and the threefold reproof

> Before the gospel: written by holy John, in the sixteenth chapter of his writing. Then said the Lord Jesus to his apostles at the last supper: this Lord goes to his Father. You know that the heavenly kingdom, that is: this Lord goes away, to die; the Lord dies, and this Lord sends you the Holy Spirit. In turn, if this Lord did not die, did not go away, to you the Holy Spirit [would not come]. The Lord dies, and this Lord sends you the Holy Spirit, and you shall see two judgments: the first, of sin; the second, of righteousness; the third, judgment. And then you receive this Holy Spirit; from the Spirit, through him, he takes you.

  1  before gospel write holy-John inside ten-six chapter of-write
  2  already^ say Lord-Jézus teach^ of-Lord at_the_Last_Supper = this-Lord
  3  go-Lord of-Lord God_the_Father you learn do
  4  heavenly land that_is this-Lord leave* on-die Lord
  5  die and this-Lord you go holy-spirit | in_turn
  6  who this-Lord this die to you go_not_away holy-spirit
  7  Lord-die and this-Lord you go holy-spirit
  8  and you exist see-two judge first from sin
  9  in_turn-two from righteous third judge and then-exist you
 10  go this holy-spirit from-spirit through grab you

## 080v — the apostles wait in prayer with Mary

> humble every good thing; and the apostles new lift up language say [truly] ye shall have many miracles, says the mouth in the Old Testament word, and it lives; go before […] […] [until] the day of judgment. Here ends this teaching gospel. Here begins this holy gospel, written by holy Luke, in the second chapter of his writing. At that time, then, after the crucifixion of Lord Christ […] year; and then the Lord was […] year; at that time the apostles remained in prayer in the Lord's, until where the Lord, Lord Jesus, made the supper; out ten years; and then this went on ten years; at that time the apostles remained in prayer; and holy Peter left, to the Virgin Mary. And then

  1  humble every good and exist disciple^ new who-ascend language say
  2  [truly] you exist many miracle say which-mouth-chapter-year
  3  inside Old_Testament word and living-exist go before [continuing] ~baptize
  4  [until] judge-~year end this SUBJ learn holy-gospel begins
  5  this holy-gospel write holy-Luke inside two chapter of-write time
  6  then-exist on-execute Lord-~Christ [?]-year and | then
  7  Lord-exist [?]-year time stand^ disciple^ prayer^
  8  inside divine_one^ ~until where Lord_God Lord-Jézus dinner do on-~out
  9  ten-year and then-exist go_on this ten-year time stand^ disciple^ on
 10  prayer^ and leave-to-leave holy-Peter to virgin-Mary and_then

## 081r — the Spirit comes upon them

> holy Peter, the wife, to the apostles answered, speaking; understand, apostles, the Lord is from […] the Holy Spirit goes, to Peter the rock […] this is. And then the Virgin Mary, then the Father, from sky the Holy Spirit goes; father Abraham, and Abraham the spirit goes upon the eleven […] understand the spirit and the apostles, Mary, on high; go, upon this; said Lord Jesus, his Father, this Lord from sky goes, his own Holy Spirit and his mother. And then the Father, how, in what form would he go if he goes into God, the Son, the Spirit; the Lord, Father, Son, Holy Spirit […] this people crucified; and then the Father, holy

  1  holy-Peter wife apostle-to answered speak believe^ apostle exist-Lord
  2  from sky go holy-spirit rock-to Peter [?]-~year this
  3  exist and_then virgin-Mary then-exist God_the_Father from sky
  4  go holy-spirit father Abraham and Abraham
  5  spirit go on-ten-+one-[?] believe^ spirit
  6  and apostle-Mary to-high go on-this say say Lord-Jézus God_the_Father of-Lord
  7  this-Lord from sky go of-Lord exist-exist holy-spirit
  8  and of-Lord mother and_then God_the_Father how? form would_like^ go
  9  if go inside God-son-spirit-Lord father son holy-spirit
 10  not_suffer this people* on_the_cross crucify^ and_then God_the_Father | holy

## 081v — cloven tongues like as of fire

> the Spirit took, upon the spirit, the form of fire and the Spirit went out from the apostles, Mary, the Jews, and the man this Spirit [filled] the apostles, the Jews; and it took, upon the spirit, the Spirit, the form of holy fire, and the Spirit went out from the apostles, Mary, the Jews; and the man, the Spirit [filled] the apostles, Mary, the Jews, many […] [cloven tongues] many a wind, in that form dove in fire in that form; and the Jews saw this fire, that form, and it came down upon this house where the apostles and Mary were at prayer. And then the Jews said, the chief, that is

  1  spirit give^ on-spirit fire form
  2  and go spirit from somebody-apostle-Mary-Jew and somebody
  3  this spirit [filled] apostle-Jew and give^ on-spirit
  4  spirit holy-fire form and go-spirit
  5  from somebody-apostle-Mary-Jew and somebody spirit [filled]
  6  somebody-apostle-Mary-Jew many drink-~year [cloven_tongues]
  7  many sough inside form dove inside fire
  8  inside form and see Jew this fire.
  9  form and bow on-this house where apostle-Mary
 10  on-pray and_then-+say Jew ~head that_is

## 082r — the Jews see it, and three thousand are added

> the Lord; the apostles began to believe, every wind, and go to the Jews saw it, because […] the Jews […] every wind; and then the Jews were […] in the house where the apostles and Mary were at prayer, to sky from the apostles and Mary at prayer, they left the heavenly word; thanks, apostles and Mary, to the Lord; thanks to the Lord God; and various […] […] and then the Jews […] these apostles; the sons of Jerusalem saw how language say and then the apostles are apostles, Master, from sky the Holy Spirit goes [amazed] the apostles, the one who […] went from the people, the Jews, one […] the people received belief in Lord Jesus Christ, and every

  1  Lord ~begin-believe apostle every sough and go_to Jew
  2  on-see because ~exist-+name Jew [under_heaven] every sough and | then
  3  exist Jew go_to inside house where apostle-Mary | on
  4  prayer^ to sky from apostle-Mary on-pray ascension^
  5  heaven^ word thanks apostle-Mary to-Lord thanks Lord God and
  6  various language say and_then Jew ~blind-to.
  7  this-apostle Jerusalem son see how? language say and_then apostle
  8  SUBJ exist apostle Master from sky go holy-spirit [amazed]
  9  apostle one-who food go from ~people Jew three_thousand
 10  ~people grab believe Lord-Jézus-Christ and every

## 082v — three thousand added, and the Trinity begins

> man, Jew, apostle, Mary, received the Holy Spirit; and two years, three baptisms, from the Jews […] and […] baptism […] three thousand, and one […] son, seven sons; and from the son received holy Spirit […] upon the spirit, the Holy Spirit, every man, Jew, son […] received the Holy Spirit and believed in the Lord Jesus Christ proceed believing, the man would heaven in turn […] Here ends this holy gospel, this Holy Spirit. [proceedeth] from the Father, out and out, the Spirit proceeds; in turn the Son, this Son, from the Father, sitteth; see, he is this […] sun the Sun; this sun has three good things; first

  1  somebody-Jew-apostle-Mary grab holy-spirit and two-year ~baptize from
  2  Jew [received] and [baptized] ~baptize three_thousand and
  3  one-[?]-[?] ~son seven ~son and from ~son grab | holy
  4  soul^ proceed* on-spirit holy-spirit every | somebody-Jew
  5  ~son-[?] grab holy-spirit and believe | Lord
  6  Jézus-Christ proceed* on-believe somebody want one-can heaven
  7  ~land here_ends this holy_gospel this holy-spirit.
  8  [proceedeth] on-father out-out go_out-spirit in_turn son
  9  this-son from to-God_the_Father sit see he_is* this | remain*
 10  sun Sun this sun SUBJ three good first

## 083v — the sun, its light and its warmth

> is good first he who is light; in turn the second is good, warmth; the third is good from the Sun; the sun's light signifies the Son of God; in turn the warmth signifies the Holy Spirit; in turn the Sun itself signifies the Father; upon this Lord, from the Sun proceeds the light, proceeds the warmth, proceeds the Son from the Father, proceeds the Holy Spirit from the Father; he is the sun, one form; this is one God; in turn who is, this can have, how can heaven and earth quake, and in his [dwell] prepare heaven, in turn, and the earth

  1  SUBJ good [first] he_who* light in_turn-two SUBJ good warmth third SUBJ good
  2  from-Sun sun Sun light symbolize son God in_turn warmth
  3  symbolize holy-spirit in_turn from-Sun symbolize from-God_the_Father on-this-Lord from-Sun
  4  on-go_out light on-go_out warmth on-go_out son on-from-God_the_Father
  5  on-go_out holy-spirit on-from-God_the_Father he_is* sun
  6  one form | this
  7  SUBJ one God in_turn-who
  8  SUBJ this can have how?
  9  can heaven earth
 10  quake and inside of-Lord [dwell] prepare
 11  heaven in_turn-chapter-in_turn-from-in_turn and earth

## 084r — Augustine and the child on the seashore

> At that time, then, after the condemning of Lord Jesus Christ, in the sixtieth year, at that time holy Augustine went to the shore of the sea, because he would understand how it is that three, Lord, Lord, Lord, Father, Son, Spirit, are one God; and this is one [one day at] in the evening in the middle at the going down of the sun; and then he found one little child on the shore; this […] that day the little child sat […] and the child […] one pit […] and the child carried in his hand one spoon, and this that day the child scooped with this spoon into this pit, this child

  1  time then-exist
  2  on-?condemned Lord-Jézus
  3  Christ six-ten-year time
  4  go holy-Augustine shore
  5  sea because want
  6  understand ~if
  7  three Lord-Lord-Lord father
  8  son spirit one God and this exist one
  9  morning evening noon Sunday on-go_out and then-exist
 10  find one little son-Lord_God on-shore this
 11  ~sea sit son-Lord_God little [on_the_sand] and | of
 12  son-Lord_God [digging] one pit son* and | of
 13  son-Lord_God hand one spoon carry-son-Lord_God and this
 14  ~sea this spoon inside this pit scoop-son-Lord_God this son

## 084v — thou shalt sooner empty the sea

> And then holy Augustine, this little child, what does this child want? Said the child, this: that day into this pit I scoop. Said holy Augustine, this child, can this child do it? What child, this, that day, into this pit the child scoops said this […] child; first this child, can the child do it, and this Augustine, upon leaving and the child [cannot] saw the word afterwards, before holy Augustine; and he could tell many this [understand] in writing [the Trinity] but believe truly, this woman, one God, of the man, heaven and earth, that is, he has carries the law of God [and keep] sin, the man is saved the man answered, to many, he shall never die, for ever, amen; speaks holy James apostolic letter his own

  1  and_then holy-Augustine this little son-Lord_God
  2  who this want-son-Lord_God say want-son-Lord_God this.
  3  ~sea inside this pit scoop say holy-Augustine | this
  4  son-Lord_God this can-son-Lord_God do who | this
  5  son-Lord_God this ~sea inside this pit scoop-son-Lord_God
  6  say this little son-Lord_God first this-son this | can
  7  son-Lord_God do but-who this-Augustine on-chapter-leave-this
  8  and son-Lord_God [cannot] see word ~do before
  9  holy-Augustine and can to-many this [understand] on-write [the_Trinity]
 10  but believe righteous this-woman one God | of
 11  somebody-+SUBJ heaven land that_is have
 12  carry law God [not_commit] sin somebody be_saved
 13  somebody answered* to-many not-not-die chapter-oh chapter-oh
 14  amen speak holy_James apostolic_letter exist-exist of

## 085r — one commandment broken is all of them broken

> and among you, through transgressing one of God's laws, the commandment, every man [in one point] receives before face thanks to the Lord, because if a man one transgresses, how then is he a transgressor of every law? because it is the Lord's; he received it from his angel, in the Old Testament word, father Abraham […] ten and one commandment [guilty of all] this, more than these, go and be saved among men; the Lord of the Jews, Jesus, apostle to the gentiles, most high serpent the Son of the living God Lord Jesus Christ; and to the man from face and to the man the soul upon the cross […] and for the man his blood was shed, and the man the Lord redeemed from hell fire [stay] the man, to many, until the ten laws; believe truly, be baptized […] one God

  1  and among you through transgress one
  2  law God to-commandment all^ somebody-+SUBJ [in_one_point] grab before
  3  face to-Lord thanks Lord_God because and somebody one
  4  transgress how? then-exist all^ law ~transgress somebody | because
  5  SUBJ exist Lord_God grab on-angel of-Lord inside Old_Testament
  6  word father Abraham seventy and one-[?] commandment
  7  [guilty_of_all] this more_than_these* go be_saved among somebody divine_one^
  8  Jew Jézus apostle-pagan above-high serpent son living God
  9  Lord-Jézus-Christ and to-somebody from face and to-somebody soul
 10  ~on-+cross-[?] and to-somebody SUBJ of blood shed and somebody SUBJ
 11  redeem-Lord from hell fire [stay] somebody to-many from-until
 12  ten-+law believe righteous woman-[?] one God

## 085v — Elijah calls down fire

> of the man, heaven and earth, that is, he has carries the law of God [and keep] sin, the man is saved the man answered, to many, he shall never die, for ever, amen. Speaks holy Augustine, to many: believe, the man, in God for ever that God can, for ever. face this day, in the place, the man receives in his mouth; speaks holy Elijah the prophet, it is written. Holy the prophet, holy Moses, there was [called down] fire upon all peoples to heaven on high, because all peoples were destroyed; kneeled one holy Elijah the prophet. At that time, then, the Lord destroyed the earth; there was fire in one place, and […] from piercing [give account] to the Lord, in water; upon this the destroying was three

  1  of-somebody SUBJ heaven land that_is have
  2  carry law God [not_commit] sin somebody be_saved
  3  somebody answered* to-many not-not-die chapter-oh chapter-oh
  4  amen speak holy-Augustine to-many believe somebody inside
  5  God exist-exist-chapter that God can inside exist-exist-chapter.
  6  to-from face exist-today’s on-place grab somebody
  7  inside of-somebody mouth speak holy-Elijah prophet write.
  8  holy-NAME.prophet holy-Moses exist [called_down] fire on-every people*
  9  to-heaven high because-exist every people* destroy kneel one
 10  holy-Elijah prophet time then-exist Lord_God destroy-Lord
 11  earth exist fire inside one place and flame* | from
 12  pierce [give_account] to-to Lord_God inside water on-this destroy exist three

## 086r — the torch lit from heaven

> twenty years and six years; at that time holy Elijah kneeled and prayed; thanks to the Lord; and fire from the gate of God, the angel of heaven; and rather fire [from heaven] one [torch] [became] said the angel of God: Elijah, this signifies the Lord, the Lord of angels. And then holy Elijah took a torch, and the torch gave light; in turn this […] […] went to Elijah, from twenty twenty peoples, and every one […] the torch gave light; in turn holy Elijah [chariot] little and in Elijah, until until; and then holy Elijah, then, forty days. This is written by holy Moses in the Old Testament word.

  1  forty and six-year time kneel holy-Elijah
  2  and pray to-Lord thanks Lord_God to fire
  3  from-gate God angel heaven and from [but_rather]
  4  fire [from_heaven] one [torch] [became] say
  5  God angel Elijah this exist symbolize Lord_God Lord | of
  6  angel and then-exist grab holy-Elijah torch ~and torch
  7  light in_turn this [figure] flame* go to-Elijah from | two-two
  8  two-two ~people and every from-~people torch light in_turn
  9  holy-Elijah [chariot] little and inside Elijah from-until
 10  from-until and_then holy-Elijah then-exist | two-two-two-two
 11  ten-~year this_is write holy-Moses inside Old_Testament word

## 086v — the torch signifies the Virgin

> it signifies [figure] good news the angel from the Father, for ever to the blessed Virgin Mary, one son, the Lord [figure] signifies the man, for ever […] received, upon the Lord Jesus Christ; it signifies the torch, for ever, to the blessed Virgin Mary; then Mary conceived the Lord, and Jesus saved the whole wide world; and Christ […] of the man, and the Lord, the head […] heaven and earth [together] signifies, for ever, Lord Jesus Christ […] the fire signifies the Lord, and every one can […] God the Father Lord Jesus Christ, the angel, the Holy Spirit, Mary, the apostles, one [God] God [made] and this [unconsumed] is, until the crucifying of Lord Jesus Christ, at thirty, in the host the Lord's year, upon the whole wide world

  1  symbolize [figure] gospel exist angel from-father inside exist-exist-chapter
  2  to-happy virgin-Mary son one Lord_God [figure] symbolize
  3  somebody exist-exist-chapter gospel exist grab | on-Lord
  4  Jézus-Christ symbolize torch exist-exist-chapter to-happy | virgin
  5  Mary then-exist-Mary conceive Lord_God and Jézus be_saved every all_the_world
  6  world* and Christ ~woman of-somebody and Lord ~head-[?]-~son
  7  heaven and earth [together] symbolize exist-exist-chapter Lord-Jézus
  8  Christ [unconsumed] symbolize fire Lord_God and can every | father-God
  9  Lord-Jézus-Christ-angel-holy-spirit-Mary-apostle one [God]
 10  God [made] and this [unconsumed] exist from-until on-execute
 11  Lord-Jézus-Christ on-thirty inside the_host* Lord-year on-every all_the_world world*

## 087r — the torch and the light

> and the man who eats this day man the Son of God man every man shall be saved; and one man be damned Elijah signifies, for ever, the blessed Virgin Mary, how from Mary the torch gave light at his coming the Lord created of the man, and the cross could, to one man's death, but all peoples die; this one, one man could, God, everything, in his mouth receives, because the Lord […] for ever, but rather [the sun] God is many [the sun] and […] and from [the light] [the warmth] the earth [the sun] and heaven on high, and God is this can; then the Lord would have heaven and earth quake

  1  and somebody exist this exist-today’s eat man* son
  2  God man* everybody = be_saved and one
  3  somebody be_damned Elijah symbolize exist-exist-chapter to-happy
  4  virgin-Mary how? from-Mary torch light then-~be_born
  5  create-Lord of-somebody and can on_the_cross to-one
  6  somebody die but every people* die this-+one one somebody
  7  can God every inside of-somebody mouth grab because Lord_God
  8  ~have-[?] exist-exist-chapter but_rather [the_sun] God-+SUBJ
  9  many [the_sun] and high-Lord and from [the_light] [the_warmth]
 10  earth [the_sun] and heaven high and God-+SUBJ
 11  this can then-exist want-Lord heaven earth quake

## 087v — the poor man of God

> […] the gospel written by holy Matthew […] of his writing, who is whosoever is an apostle, this from this little the son to afterwards, in Jesus' name, one man is saved, one […] in heaven; in turn the day is not so; every man is damned, judged, the man, by Christ. Holy Matthew speaks [thus] this man says, this little the son, this little the man trespasses, the poor man of God, and the poor man of God, the man, and [riches] have the man in turn, this

  1  ~before gospel write
  2  holy-Matthew [eighteen]
  3  of-write who-exist-to
  4  ~somebody-apostle this from this
  5  little son to*
  6  ~do inside of-Jézus
  7  and-~body one
  8  somebody be_saved one man* inside heaven | in_turn-chapter
  9  ~year-exist ~but everybody = be_damned judge somebody Christ | holy
 10  Matthew speak [thus] this somebody say this little
 11  son this little somebody trespass poor_man_of_God = and
 12  poor_man_of_God = somebody and [riches] have somebody in_turn this

## 088r — the rich man, and the soul in purgatory

> the man is rich, he has wealth, he sees, blind he goes […] or sits, and blind asks of this man alms, in Jesus' name [alms] the blind, the high receives; the man is damned, the man, for ever riches […] judged and damned, the man upon the blind; in turn damned, whosoever is damned, the man, for ever [remember] saved; the man is damned, the man get conceived whosoever, in the evil bury [there] it is written, the man in the evil until the death of the man […] in turn upon death the soul is in purification […] until the day of judgment; in turn upon the day of judgment, and the soul, and for ever in the evil, for ever

  1  somebody rich have-somebody wealth see blind
  2  go name-somebody or sit and ~blind exist ask from this
  3  somebody alms inside Jézus and-~body [alms]
  4  blind high-grab somebody be_damned exist somebody chapter-oh
  5  chapter-oh riches* ~but-somebody from-judge be_damned somebody
  6  on-blind in_turn be_damned whosoever* be_damned exist somebody chapter-oh
  7  chapter-oh [remember] be_saved somebody be_damned exist somebody conceive
  8  whosoever* inside ~evil bury [there] write somebody
  9  inside ~evil until to-die of-somebody and-~body in_turn | on
 10  die soul inside purification fire until judge-~year in_turn | on
 11  judge-~year and soul and exist-exist-chapter inside ~evil chapter-oh chapter-oh

## 088v — there was a certain rich man, clothed in purple

> Here begins this holy gospel written by holy Luke in the sixth chapter of his writing. At that time Lord Jesus said to his apostles, and the Jewish people, there was a rich man, one rich man, and the rich man, every […] and purple the rich man wore, and the rich man from day to day made merry; and then that way came one Lazarus to the rich man's house; and Lazarus was all over head until toe covered wounds, Lazarus; at that time this rich man to table the rich man sat, the man, the Lord [fared sumptuously] the Lord king [in purple] this and that, the Lord; and then the rich man, this poor man asked

  1  here_begins this holy_gospel
  2  write holy-Luke inside
  3  six chapter of-write
  4  time say Lord-Jézus
  5  apostle of-Lord and Jew
  6  people-chapter exist-rich
  7  one rich-somebody
  8  and somebody-rich every [linen] and purple go-somebody-rich | and
  9  rich from day until day joy-rich and then-exist thus go
 10  one ~Lazarus to-house this-rich and ~Lazarus exist every from
 11  head until toe covered* wound ~Lazarus time this rich
 12  to table sit-rich man^ husband^ [fared_sumptuously] king-Lord [in_purple]
 13  who-and-this-and husband^ and then-exist rich exist this the_poor_man/woman* ask

## 089r — the dogs licked his sores, and angels carried him

> alms; and the poor man, alms take the rich man [desired] but the poor man he drove out; and then this poor man lay outside the gate of the rich man, alone, because the poor man was [full of sores] was [laid]; and then the poor man desired the crumbs that fell the dogs from the rich man's table […] the poor man […]; and then the rich man had many dogs, and the dogs came, this Lazarus and the dogs licked Lazarus […] and Lazarus more was of the dogs have mercy, this Lazarus; in turn from the rich man mercy […] lame mercy; and then this Lazarus died, went with angels to heaven, to glory, literally, from God the Father the Most High this Lazarus, and Lazarus the angels took, and carried Lazarus into the bosom of Abraham the forefather. And then this rich man saw this miracle, of this Lazarus

  1  alms and the_poor_man/woman* alms take rich [desired]
  2  but the_poor_man/woman* out chase and then-exist lie this
  3  the_poor_man/woman* out ~gate to-of-rich exist-+one because exist the_poor_man/woman* [full_of_sores]
  4  exist [laid] and then-exist want the_poor_man/woman* trespass from crumbs the_dogs*
  5  on-of-rich table^ [fell_from] the_poor_man/woman* take and then-exist | have
  6  rich many dog and go-dog this Lazarus ~and
  7  lick-dog of-Lazarus ~wound and Lazarus more
  8  exist from dog have have_mercy this Lazarus in_turn from-rich
  9  have_mercy ~believe-Lazarus lame have_mercy and then-exist this Lazarus
 10  die go angel heaven glory* literal from-father God the_Highest* this Lazarus and Lazarus
 11  grab-angel and Lazarus carry inside öl Abraham
 12  forefather and then-exist see this miracle this rich from this Lazarus

## 089v — in hell he lifted up his eyes

> who Lazarus did, the angels, the Father, heaven; and then this rich man died, and this rich man [also] in the evil was buried; and then he suffered in the evil, this rich man; he looked up and saw Lazarus in the bosom of father Abraham, and this rich man cried father Abraham, said the father, Lazarus, because this […] the poor man, of Lazarus, a little finger dip in water, and cool it on the rich man's tongue [cool] flame the soul of the rich man; and from […] for ever, of the rich man. And then father Abraham: this rich man, son of the Father, this rich man had good things [in thy lifetime] he is Lazarus was [evil things] [now] the people; in turn this rich man was rich blind [lifted up his eyes] this rich man, Lazarus took the crumbs that fell the dogs the rich man's table; the rich man took [fell from] the rich man, Lazarus take

  1  who do Lazarus angel father heaven and then-exist this
  2  rich die and this-~rich [also] inside ~evil bury and then-exist
  3  suffer inside ~evil this ~rich see ~trespass-~rich and see Lazarus
  4  inside öl father Abraham and shout this rich
  5  father Abraham say-father Lazarus because-this from-understand the_poor_man/woman* | of
  6  Lazarus little finger immerge water and cool
  7  on-of-rich tongue [cool] flame* soul of-rich and from
  8  [remember] exist-exist-chapter of-rich and_then father Abraham | this
  9  ~rich son of-God_the_Father this-~rich good [in_thy_lifetime] he_is*
 10  Lazarus exist [evil_things] [now] people* in_turn this-~rich exist
 11  rich ~blind [lifted_up_his_eyes] this-~rich grab-Lazarus trespass from crumbs
 12  the_dogs* [?]-~rich throne ~rich grab [fell_from] ~rich Lazarus take

## 090r — a great gulf fixed, and they have Moses and the prophets

> said father Abraham, take Lazarus [send] opposite the people. And then father Abraham: a great chasm between the rich man […] or […] this is the netherworld, most high, evil upon evil; who cries, this […] father Abraham; and Lazarus [may come] in the bosom of father Abraham; and a second time this rich man cried, father Abraham, send Lazarus [great gulf] opposite world the rich man has, the trespass, these two, of the rich man brethren, because the brethren […] of the rich man, how in this rich man's suffering because these brethren, the man sins, from [repent] then is damned the man, as the rich man, this rich man is damned. Said father Abraham, they have the brethren, the trespass, this prophet, and preaching, because this prophet preaches evil; the man, the brethren be damned and a third time he cried, this

  1  say father Abraham grab-Lazarus [send] opposite people* and_then
  2  father Abraham great^ chasm among-~rich-[?] or [pass_over]
  3  this_is netherworld highest ~evil on-~evil who-shout this-[?]
  4  father Abraham and Lazarus [may_come] inside öl father
  5  Abraham and two who-shout this-~rich our_father Abraham
  6  go Lazarus [great_gulf] opposite world have-~rich trespass this-two-two of-rich
  7  ~brother because ~brother say-Lazarus from-~rich how? inside this-rich suffer
  8  because this ~brother somebody sin from [repent] then-exist be_damned
  9  somebody how?-rich this-rich be_damned say our_father Abraham have
 10  exist-exist trespass this prophet and preach because this prophet preach
 11  evil somebody brother be_damned* and three who-shout this

## 090v — neither will they be persuaded, though one rose from the dead

> the rich man; father Abraham […] the prophet preaches, believe [fell from] [neither] good, the man Lazarus, believing and the body rose from the dead, the poor man. Said father Abraham, in turn who cannot the brethren, the prophet, let the brethren believe, and the preaching and good, from the man […] […] the brethren believe; and the body rose from the dead, the man Lazarus […] this holy day. Here ends this holy gospel. Here begins this holy gospel, written by holy John, in the second chapter of his writing. At that time Nicodemus came by night to Lord Jesus, because he feared the Jews; and not want to the Lord he came

  1  rich our_father Abraham name-°vanished-from prophet preach believe [fell_from]
  2  [neither] good somebody-Lazarus believe-exist-exist
  3  and body from die stand_up-somebody-~woman say our_father Abraham in_turn-who cannot*
  4  friend^ prophet believe-brother-somebody and preach
  5  and good from somebody-~baptize-[?] cannot* exist-exist believe and body
  6  from die stand_up-somebody-Lazarus [?]-this-holy-~year here_ends this holy_gospel
  7  here_begins this holy_gospel write
  8  holy-John inside second^ chapter | of
  9  write time go Nicodemus
 10  inside night to-Lord-Jézus
 11  because ~have Jew and
 12  not_want to-Lord go-this

## 091r — except a man be born again

> but by night to the Lord came Nicodemus. And then Nicodemus: O. Nicodemus answered, this Nicodemus, this Lord Nicodemus believes. that this Lord is truly the Son of the living God, because this Lord goes to heaven. In turn […] and the Lord, this Lord truly the Son of the living God. And then Lord Jesus, Nicodemus verily verily this Lord to you speaks: and the man cannot who believes in the Lord born again a second time is born into this world, that one man is saved; but every man is damned. Said Nicodemus, answering, how can this be, who a second time a second time from his mother goes, Nicodemus, and a second time is born into this world? For this, thanks. Said Lord Jesus, Nicodemus speak this Lord, this

  1  but inside night to-Lord go-Nicodemus and_then Nicodemus oh.
  2  of-Nicodemus answered this-Nicodemus this-Lord believe-Nicodemus.
  3  that this-Lord true^ son living God because this-Lord go on-heaven.
  4  ~land and-Lord this-Lord true^ son living God and_then.
  5  Lord-Jézus Nicodemus verily verily this-Lord you.
  6  speak and man^ cannot* exist to-Lord believe born_again* second^
  7  be_born on-this world* one man^ be_saved but every-somebody
  8  be_damned say Nicodemus answered how?-this can exist who to-two-before
  9  second^ from of mother go-Nicodemus and second^ be_born-Nicodemus on-this world.*
 10  this thanks say Lord-Jézus Nicodemus speak* this-Lord this-donkey-to

## 091v — born of water and of the Spirit, and God so loved the world

> this host, this Nicodemus, a second time born of his mother; but this Lord speaks: then, born a second time, the man Nicodemus, of water and of the Holy Spirit, that one man Nicodemus is saved; but every man Nicodemus is damned. Said Lord Jesus, Nicodemus, in turn then this Lord to you began, the Lord, to preach of heaven and earth, how you from […] left, Nicodemus the man; then can this world, Nicodemus, the man enter he left, the brethren; this Lord to you preached, said the Lord Jesus, Nicodemus: so did you love the Father, his God of heaven but the Father's only begotten Son, Jesus, that is, to the Lord, so did you love the Father, said Lord Jesus; and [water] and the man, the Lord

  1  this host this-Nicodemus again be_born from of-Nicodemus mother but
  2  this-Lord speak then second^ be_born-somebody-Nicodemus from water and
  3  from holy-spirit one somebody-Nicodemus be_saved but
  4  every-somebody-Nicodemus be_damned say Lord-Jézus Nicodemus in_turn | then
  5  exist this-Lord you begin-Lord preach from-heaven
  6  kingdom^ how? you from enter* | leave-Nicodemus
  7  man^ then-exist this world* can Nicodemus-somebody enter*
  8  leave-to-leave brethren* this-Lord you preach-Lord say | Lord
  9  Jézus Nicodemus [?]-+one you love father of-Lord God heaven
 10  but of-God_the_Father only son Jézus that_is to-Lord [?]-+one
 11  you love God_the_Father say Lord-Jézus and [water] and man^ Lord

## 092r — that whosoever believeth should not perish

> believes in the Son of the Father, the only begotten, Lord Jesus Christ, and one man Nicodemus is saved; but every man Nicodemus is damned. Said Lord Jesus, Nicodemus [answered] to the Lord goes the Father, his God of heaven; he loved this Lord; this people he judges, but rather to the Lord goes the Father, the brethren, this Lord saved this world by his death; and man is, to the Lord believes, this man Nicodemus, and his Father believes more than these; this one, one God. Said Lord Jesus [only begotten] one […] among you […] from the dog and [believeth in him] [already] [condemned] not; and said Lord Jesus, and the man Nicodemus who does evil among you

  1  believe son of-God_the_Father only Lord-Jézus-Christ and one
  2  somebody-Nicodemus be_saved but every-somebody-Nicodemus be_damned say
  3  Lord-Jézus Nicodemus [answered] to-Lord go father of-Lord God heaven
  4  love this-Lord this people* judge but_rather* to-Lord go God_the_Father brethren* this-Lord
  5  this world* be_saved on-of-Lord die and man* exist to-Lord
  6  believe this somebody-Nicodemus exist and of-Lord God_the_Father
  7  believe more_than_these* this one one God say Lord-Jézus [only_begotten]
  8  one ~exist-[?] among you [that_believeth] from
  9  dog and [believeth_in_him] [already] [condemned] not and say
 10  Lord-Jézus and SUBJ do_evil-somebody-Nicodemus among you

## 092v — men loved darkness rather than light

> from the man Nicodemus who will not come to the light, but loves the darkness, the man Nicodemus; said Lord Jesus, and the true man Nicodemus, from the man Nicodemus, the light, the man Nicodemus loves, and all come to the light the man Nicodemus. Here ends this holy gospel. The Lord, with all thy heart, Lord. Here begins this holy gospel written by holy Luke in the fourteenth […] in his writing. At that time Lord Jesus said to his apostles and to the Jewish people: then a rich lord made, one rich man, many dinner

  1  from somebody-Nicodemus not_want on-light go but darkness love
  2  somebody-Nicodemus say Lord-Jézus and SUBJ righteous-somebody-Nicodemus from
  3  somebody-Nicodemus light love-somebody-Nicodemus and every on-light | go
  4  somebody-Nicodemus here_ends this holy_gospel Lord_God be_loved Lord
  5  here_begins this holy_gospel
  6  write holy-Luke inside
  7  fourteen chapter inside | of
  8  write time
  9  say Lord-Jézus disciple^
 10  of-Lord and Jew
 11  people-chapter | then-exist
 12  rich-Lord_God do one rich man^ many dinner

## 093r — a certain man made a great supper, and bade many

> And then the rich lord, among the rich lord's, the redeemer's day, three […] upon this […] said this rich lord to his living servant, go […] speak this word, go, the man; at that time all is finished, say. This living servant, this […] man lo, the living servant. Go to the rich lord's living man […] then the lord […] of the lord […] said this first: not. […] because […] a piece of ploughland; I must man go and see it, and I must, the ploughland […] he asks […] to speak man he is to […] the lord; and said this second, lo. The living servant goes, the lord's living servant, this man

  1  and then-exist-rich-Lord_God among-rich-Lord_God redeemer-~year three friend.
  2  on-this dinner say this-rich-Lord_God of-Lord living-servant go-[?].
  3  this word speak-angel go-somebody time SUBJ every finished say.
  4  this-living-servant this ~one man* lo living-servant.
  5  go of-living-somebody-Lord_God this-?man then-chapter-Lord_God go-?man
  6  of-Lord_God dinner say this first this-?man not.
  7  can-?man because buy-?man plough | want
  8  man* SUBJ -anus-go see and want plough [prove_them.]
  9  ask this-~servant to-speak man* exist-to
 10  of-living-~servant Lord_God and say this two sense lo.
 11  living-servant go of-living-servant Lord_God this-somebody-sense

## 093v — I have bought five yoke of oxen

> then the lord; the man goes, of the lord dinner said this second man, this man cannot the man cannot, because the man has bought five yoke of oxen ox the man must the man goes in the field the man must […] thanks; he can […] […] [pray thee] [excused] believe; this living servant, to speak the man, before […] the lord said this third man, lo, the living servant goes, the lord's living servant the lord; this third man, then the lord, the man goes of the lord dinner said this third, this man

  1  then-chapter-Lord_God go-somebody-sense of-Lord_God dinner say this
  2  two somebody-sense this-somebody-sense not
  3  can-somebody-sense because buy-somebody-sense
  4  five yoke sense ox want-somebody-sense
  5  go-somebody-sense in_the_field* want-somebody-sense
  6  SUBJ ox thanks exist can ox | [try]
  7  [pray_thee] [excused] believe this-living-~servant to-speak
  8  somebody-sense before of-living-~servant Lord_God say
  9  this three somebody-thief lo living-servant go of-living-servant
 10  Lord_God this-somebody-thief then-chapter-Lord_God go-somebody-thief
 11  of-Lord_God dinner say this three thief this-somebody-thief

## 094r — go out into the highways and hedges

> the man cannot, and the man must go because the man must go, he has married; this man cannot the man cannot, and the man must go, and this and that the man [answered] said, to speak, the man is to of […] the lord; and then, and one goes, the man man upon this, to the supper, said this lord, that is, the people; and the people spoke of the lord dinner and the lord said to the living servant, go out into the roadside and the way and into the town, and to the town gate, and. […] within, the one-eyed, the blind, to be […] the body hungry, and […] within the one-eyed, and […]

  1  not can-somebody-thief and to-go-somebody-thief
  2  because to-go-somebody-thief marry this-somebody-thief not
  3  can somebody-thief and to-go-somebody-thief and this-and-this
  4  somebody-thief [answered] say to-speak somebody-thief exist-to
  5  of-[?] Lord_God and then-exist and one | go-somebody
  6  man* on-this to-dinner-to say this
  7  Lord_God that_is people-chapter and people-chapter from-speak of-Lord_God dinner
  8  and say of-Lord_God living-servant go on-roadside and on-way
  9  and on-town and on-gate town and.
 10  ~find-[?] inside only-~year-~exist blind-eye | to-exist-chapter
 11  [lame] body hunger and thirst inside only-~year-~exist and [?]-°first.

## 094v — blessed is he that shall eat bread in the kingdom of God

> man he found; every man went, the angel, into the lord's house said this living servant, the angel, Lord, it is done; and the mountain top, which the Lord said [the master] said this living servant, the angel servant one to the place, and to the place the living servant would go out and then there rose at the table one Jew, and cried out: blessed is he, from within the one-eyed, the blind, because the one-eyed, of the blind, heaven and earth; and said Lord Jesus truly, speaking to the Jew, more than these, within the one-eyed, heaven and earth. And then this rich man, the lord [supper] [bade many] many, to go, the mouth […] the thief upon the rich lord's dinner Here ends this holy gospel.

  1  man* find everybody = go-angel inside of-Lord_God house
  2  say this living-servant-angel Lord do and summit who-Lord
  3  say [the_master] say this living-servant-angel servant*
  4  one to-place and to-place want living-servant-angel on-out
  5  and then-exist rise to-throne one Jew and
  6  shout-to blessed^ from inside only-~year-~exist blind-eye because
  7  only-~year-~exist of-blind-eye heaven kingdom^ and say | Lord
  8  Jézus righteous speak-Jew more_than_these* inside only-~year-~exist heaven
  9  kingdom^ and_then this-rich somebody-Lord_God [supper] [bade_many]
 10  many to-go-mouth | man-[?]-somebody
 11  thief on-of-somebody-rich-Lord_God dinner here_ends this holy_gospel

## 095r — the bread blessed at the supper

> Here begins this holy gospel written by holy John in the sixth chapter of his writing. At that time Lord Jesus said to his apostles and the Jewish people: ye shall eat of his, for ever, and of his shall ye drink. And then Lord Jesus, with his apostles, at the last supper, this at the last supper; and Lord Jesus took, in turn, one baked cake, and Lord Jesus blessed this bread and bread before the Lord, Lord Jesus put it. And

  1  here_begins this holy_gospel
  2  write holy-John
  3  inside six chapter of-write
  4  time say Lord-Jézus
  5  apostle of-Lord and Jew
  6  people-chapter you
  7  exist of-Lord exist-exist-chapter
  8  eat and of-Lord to-to-this
  9  drink and_then Lord-Jézus apostle of-Lord last dinner-to this
 10  at_the_Last_Supper = and grab Lord-Jézus inside why?-in_turn one baked
 11  cake and blessed Lord-Jézus this bread.
 12  and bread before Lord place^ Lord-Jézus and.

## 095v — except ye eat my flesh and drink my blood

> Lord Jesus took wine, one cup, and water into the cup poured, and Lord Jesus blessed the wine and the water; and the wine and water before the Lord, Lord Jesus put. And then Lord Jesus: and the man who eats this bread, this man is called his own […] and the man exist who eats this bread and believes in the Lord every man is damned […] and the man who believes in the Lord and from the altar, from the thirty, the holy host eats and drink every man shall be living, for ever, amen. And then the Jews: how can this be, his own, to be eaten, and his

  1  give^ Lord-Jézus wine one cup and water inside cup
  2  pour and blessed Lord-Jézus wine and water and
  3  wine water before Lord put Lord-Jézus and_then | Lord
  4  Jézus and man^ exist this bread eat this man^
  5  exist of-Lord ~body ~eat and man^ exist
  6  this bread eat and Lord believe
  7  everybody = be_damned cut_off-[?] and man^ exist Lord believe
  8  and from altar exist from thirty holy-host
  9  eat and drink everybody = exist
 10  living chapter-oh chapter-oh amen and_then Jew
 11  how? exist-+say of-Lord ~body eat and of-Lord

## 096r — whoso eateth my flesh hath eternal life

> drink of this? This pleasing, which this Lord speaks, because food the Jews, who […] […] and his body to eat and to drink of it; which is hidden, said this Lord Jesus, who is the Lord strive but said Lord Jesus, believe; then the man believes in the Lord, to the Lord, he who is truly the Son of the living God. And then Lord Jesus: his own, this is truly to eat, and of his, this is truly to drink And then Lord Jesus: then the man who eats this bread is a man, an apostle [eateth] upon his, never [everlasting life] is from eating, how the bread of […]

  1  to-to-this drink this pleasing who this-Lord speak because eat^
  2  Jew who-[?] strive* and of-Lord body eat
  3  and to-to-this drink which-hide say this Lord-Jézus who-Lord-exist
  4  strive* but say Lord-Jézus to-believe then-exist
  5  believe-somebody inside Lord to-Lord this-?he_who indeed^ son
  6  living God and_then Lord-Jézus of-Lord ~body this_is
  7  indeed^ eat and of-Lord to-to-this this_is indeed^ drink
  8  and_then Lord-Jézus then-exist man^ this bread eat
  9  exist man^ apostle [eateth] on-of-Lord not-not [everlasting_life]
 10  exist from eat how? bread of-[?]

## 096v — I am the living bread which came down from heaven

> your fathers did eat in field because that is the bread of life; he who goes, the Lord, the Lord's bread; in turn he left the eternal town from that day, upon this world; and the man who eats this bread from him, the man shall live for ever, amen and this Lord, this […] because the Lord, this Lord goes the Lord from his Father, upon this world; and this Lord to his Father, the living Lord; and the man who in the Lord believes, from him the man lives to the Lord, for ever man and the man who is within the Lord's law of love, carried by the Lord, stays; and this Lord is

  1  you father eat inside field because that_is bread
  2  living he_who go-Lord ~bread in_turn ascension^ from_heaven* | town
  3  from-~year on-this world* and man^ exist this bread eat
  4  from man^ exist living chapter-oh chapter-oh amen
  5  and this-Lord this bread because-Lord this-Lord | go
  6  Lord from of-Lord from-God_the_Father on-this world* and this-Lord
  7  to-of-Lord from-father living-Lord and man^ exist Lord.
  8  believe from man^ exist to-Lord living chapter-oh
  9  chapter-oh man* and man^ exist
 10  inside Lord-+law-love-~carry-Lord stay and this-Lord exist

## 097r — he that dwelleth in me, and I in him

> within somebody and the man who carries his commandment, from the man who is in the Lord, from the Lord's law of love, carried by the Lord, stays; and this Lord is within somebody And then Lord Jesus [abideth in me] the man, and the man who is within the Lord, the Father, the Son, God, Jesus, the Holy Spirit, Mary, Christ, the apostles, the angels […] stays; the Lord, the Father, the Son, God would have Jesus, the Holy Spirit, Mary, Christ, the apostles, the angels go; and the man goes, the Lord, the Father, the Son, God, Jesus, the Holy Spirit, Mary, Christ, the apostles, the angels into the heavenly land. And then Lord Jesus, and this man would have the Lord, the Father, the Son, God, Jesus, the Holy Spirit, Mary, Christ, the apostles, the angels take his house, at the Lord's, the Father's, the Son's, God's, Jesus', the Holy Spirit's

  1  inside somebody and somebody exist of-Lord commandment carry from somebody
  2  exist inside Lord from Lord-+law-love-~carry-Lord stay and this-Lord exist
  3  inside somebody and_then Lord-Jézus [abideth_in_me] somebody and somebody exist
  4  inside Lord-God_the_Father-son-God-Jézus-holy-spirit-Mary-Christ-apostle-angel
  5  [?]-stay | want-Lord-God_the_Father-son-God
  6  Jézus-holy-spirit-Mary-Christ-apostle-angel go and somebody
  7  go-Lord-God_the_Father-son-God-Jézus-holy-spirit-Mary-Christ-apostle-angel
  8  inside heavenly land and_then Lord-Jézus and this somebody
  9  want-Lord-God_the_Father-son-God-Jézus-holy-spirit-Mary-Christ-apostle-angel
 10  house grab at | of-Lord-God_the_Father-son-God-Jézus-holy-spirit

## 097v — the whole company of heaven, and the host

> Mary, Christ, the apostles, the angels; from God the Father, hidden, through staying the man, for ever, amen. And then Lord Jesus, and the man who from the altar, from the thirty, the holy host eats [shall not die] from him the man lives, for ever, amen. Here ends this holy gospel. The Lord, with all thy heart. Here begins this holy gospel written by holy Luke, in the […] chapter of his writing. Then Lord Jesus, in the thirtieth day and in the first year; at that time he left

  1  Mary-Christ-apostle-angel from-father-God to-hide-exist through stay
  2  somebody chapter-oh chapter-oh amen and_then Lord-Jézus and
  3  somebody exist from altar from thirty holy-host
  4  eat [shall_not_die] from somebody exist living-somebody chapter-oh
  5  chapter-oh amen here_ends this holy_gospel Lord-+be_loved
  6  here_begins this holy_gospel
  7  write holy-Luke inside
  8  and chapter of-write
  9  then-exist Lord-Jézus inside
 10  thirty day and inside one
 11  year time leave-to-leave

## 098r — the light of the body is the eye

> Lord Jesus [preached] among the chief of the Jews, and his apostles And then Lord Jesus, to his apostles and the Jewish people [the lamp of the body] have mercy […] the eye […] […] of the apostles the man said, the eye. And then Lord Jesus, the eye of […] the man, this is the lamp of […] and the lamp of the apostles the man said, this is for ever, of […] and in turn, it is within […] for ever […] one the heart, sin protruding, is all of […] for ever darkness. And then Lord Jesus, in turn who [take heed] […] sins against the Lord, from God the Father, from the heart; he would, from the Father

  1  Lord-Jézus [preached] among high_priest = and of-Lord apostle
  2  and_then Lord-Jézus apostle of-Lord and Jew ~people [the_lamp_of_the_body]
  3  have_mercy-+SUBJ of-[?] eye-from [single] [lightsome] | of-apostle
  4  say-somebody eye-from and_then Lord-Jézus eye-from | of-[?]
  5  man^ this_is lamp of-[?] and lamp | of-apostle
  6  say-somebody this_is exist-exist-chapter of-[?] and
  7  in_turn exist inside of-[?] exist-exist-chapter remain* one
  8  heart sin protrude exist all^ of-[?] exist-exist-chapter
  9  darkness and_then Lord-Jézus in_turn-who [take_heed] heart-°alone
 10  sin against of-Lord from-father God from heart want from-father

## 098v — a candle set on a candlestick

> his scourges, various, of the ass. And then Lord Jesus, this hidden is within […] for ever; every […] is clean all of […] for ever, light. And then Lord Jesus, how then […] the lamp gives light, to the light; the lamp, a hundred, gives light, of […] for ever. Here ends this holy gospel. The Lord with all thy heart; the Lord have mercy; and truly speaks holy John: God can bear the sky and the earth; to this speaks holy John, the Lord God; and the man who bears the living man upon this world, and healing

  1  of-Lord whip-whip various from-donkey and_then Lord-Jézus this-hide
  2  exist inside of-[?] exist-exist-chapter all^ heart clean exist
  3  all^ of-[?] exist-exist-chapter light and_then Lord-Jézus
  4  how? then-exist [?]-[?] lamp light to-+SUBJ
  5  light lamp hundred exist light of-[?] exist-exist-chapter
  6  here_ends this holy_gospel Lord_God be_loved Lord_God SUBJ have_mercy and righteous
  7  speak holy-John God
  8  can carry sky
  9  and earth to-this
 10  speak holy-John Lord
 11  God and man^ carry living
 12  man^ on-this world* and healthy_man^

## 099r — he that dwelleth in love dwelleth in God

> the man receives, and God receives the man […] the man, God. To this the man has: the Lord God, Jesus Christ, the Son of God; and the Lord, the Lord's head, heaven and earth; and love his brother as thy neighbour. In turn [hath this world's goods] the holy man; the man has wealth, he sees; trespass, the poor of God; and the man [seeth not] has God, the man loves the holy man as thy neighbour. Of whosoever is holy, one, the kingdom of heaven, speaks holy Matthew; and the man […] says: this man loves God. In turn, of the holy man, his brother hateth loves the holy man, from [a liar]

  1  man^ grab and God man^ grab [abideth] man^ God | to
  2  this have man^ Lord_God Jézus Christ son of-God
  3  and Lord ~head heaven and earth
  4  and love of-somebody father son how?-to man^ neighbour
  5  in_turn [hath_this_world's_goods] ~rich man^ have man^ wealth see
  6  trespass poor_man_of_God = and man^ [seeth_not] have God man^
  7  SUBJ love-rich-somebody how?-to man^ neighbour exist | of
  8  ~somebody-rich-+one heaven land speak holy-~Matthew and
  9  man^ [a_liar] say this-somebody God love in_turn | of-rich.
 10  man^ father son hateth love-rich-somebody from [a_liar]

## 099v — if a man say, I love God, and hateth his brother, he is a liar

> he is a liar; how does this man love God, in turn, of his brother hateth loves God [his brother] the Most High, this he sees. the man, in turn, his brother he sees; whosoever hateth the son hateth the man loves; how does this man love God, this pleasing; in turn the rich man would love God; first love, of the rich man, his brother, as the holy man, the holy man's neighbour, God and good; the rich man is loved […] […] the eternal land, the evil […] the rich man sees, saved the rich man is, for ever, amen. In turn who is the rich man; the Lord, the apostles, love every man as the rich man

  1  first^ liar exist how? this man^ God love in_turn | of
  2  man^ father son hateth love God [his_brother] high-this see.
  3  man^ in_turn of-somebody father son see whosoever* hateth
  4  son hateth love-somebody how? this-somebody God love this
  5  godfearing^ in_turn want-rich-somebody God love first love | of-rich
  6  man^ father son how?-to rich-somebody rich-+neighbour God
  7  and good exist somebody-~rich love [?]-[?] heaven*
  8  land ~evil [cannot] see-rich-somebody | be_saved
  9  rich-somebody exist chapter-oh chapter-oh amen.
 10  in_turn-who-exist rich-somebody Lord apostle love everybody = how?-to rich-somebody

## 100r — Elijah taken up by fire, and the list of miracles

> the neighbour is of the holy man; the eternal kingdom [inheriteth] the holy man, from [taken up] the Lord, from the Father and the Son and the Holy Spirit. Elijah the prophet was taken, by fire, into heaven. Various miracles: afterward the blind eyes, through light [saw]; the dead were raised up; the lame [walked]; the body, and the possessed of the evil one, were healed. Elijah? Who? and this, and this miracle: did Elijah do it? writes the church father, the scholar pagan First writes the scholar pagan; the church father [concerning] Elijah.

  1  neighbour exist of-rich-somebody heaven = [inheriteth]
  2  rich somebody from [taken_up] Lord from God_the_Father and son and holy-spirit
  3  Elijah prophet take^
  4  fire on-+heaven
  5  various miracle
  6  ~do blind sight^
  7  SUBJ through light die SUBJ
  8  raised_up* lame
  9  body and evil^ possessed SUBJ heal Elijah | who-and-this
 10  and-this miracle do Elijah write church_father church_father^ pagan
 11  first write church_father^ pagan church_father [concerning] Elijah

## 100v — the fathers on the sepulchre, a chronology, and the temple of forty-six years

> the sepulchre; to heaven; on earth; on that, writes [in three days] […] the church father, on that, writes: the Most High hid himself, and from […] the scholar. pagan the church father, on that, writes the scholar pagan the Pharisees. And the church father writes this three; and Saint Augustine the church father: Elijah the Lord God [heart-Lord] first, but rather [heart-Lord] the sun and the moon, and there is living Elijah; to Elijah, two; then, from Adam [heart-Lord] fifty; and on this man […] seven people. Then is this man five hundred and thirty. In the thirtieth year, then: "destroy", the Lord; five towns; and then on this: "destroy", forty years and six years.

  1  tomb to-+heaven on-earth on-that_is write [in_three_days]
  2  pagan church_father on-that_is write high-hide-and-from scholar.
  3  pagan church_father on-that_is write scholar pagan Pharisees*
  4  and church_father this three write and Saint_Augustine_the_church_father Elijah
  5  Lord_God heart-Lord first but_rather heart-Lord sun and moon
  6  and exist living Elijah to Elijah two then-exist from
  7  Adam heart-Lord fifty and on-this somebody [and_six] seven
  8  people-chapter time exist this somebody five_hundred and
  9  thirty thirty-~year time destroy Lord_God five
 10  town and then-exist on-this destroy forty and six-year

## 101r — Elijah's fire, and Enoch and Elijah kept for Antichrist

> Then holy Elijah knelt down and prayed to the Lord God; to fire; and took; the angel of God said, the angel of God, to Elijah: this is the angel of the Lord; and this man from […] And Elijah, the man, from […] […] […] and Elijah, the man, was taken up into heaven […] and […]. Elijah, the man man from the day; Noah and Elijah shall bear the sword; the evil one […] and […] […] Noah and Elijah on the earth. [Antichrist] [of a harlot] shall be born; two; the chief evil, the evil one, and the son of the devil; and there is […] evil, who is Antichrist.

  1  time kneel holy-+Elijah and pray Lord_God | to
  2  fire and grab God angel say God angel Elijah
  3  this exist-of-angel Lord_God and this somebody from-exist
  4  and Elijah-somebody from-leave-to-leave [wished_to_die] [juniper] and
  5  Elijah-somebody be_caught_up heaven highest and gate/open | Elijah
  6  somebody [man] from-~year Noah Elijah sword carry
  7  ~evil one-+gate/open and [Enoch] leave-to-leave Noah Elijah on-earth
  8  [Antichrist] [of_a_harlot] through be_born two chief_devil =
  9  and son Satan and exist-[?] evil^ exist Antichrist

## 101v — the opening of a reading from Luke: Simeon

> Before the gospel, says holy Luke: thanks to the Lord, the Lord God, thanks be; of the Lord, holy mercy, Lord; this Lord, the gate, Lord; of the Lord, many homes. Before, many holy fathers before, many, writes church father the church father: heaven; the Lord's Son […] the Lord taken; to see one […] because many holy fathers wanted to see the Lord Jesus Christ [consolation of Israel] The Lord's chapter: many; how shall we see? In turn, Simeon; one, Simeon.

  1  before Word^ speak
  2  holy-Luke to-Lord glory^
  3  Lord God glory^ exist
  4  of-Lord holy-have_mercy Lord
  5  this Lord gate Lord
  6  of-Lord many home
  7  before many holy-father-before many write church_father church_father
  8  heaven Lord son SUBJ grab-Lord see one [?]-°sat
  9  because because many holy-father want see Lord-Jézus-Christ [consolation_of_Israel]
 10  Lord-chapter many how_shall_we* see but Simeon one-Simeon

## 102r — Simeon's arms, and the thirtieth year

> and shall be called; it is Simeon; for Simeon carried him in his bosom: the Lord Jesus Christ [took him]. The Lord saw the apostles and the Jewish people, and these apostles, the Jews, the Lord; all saw within […] of the name of the man. Then was the Lord Jesus within his thirtieth year. Then, from the woman, the Lord Jesus; and the Lord went from town to town, from temple to temple, from field to field; and the Lord's apostles went into the world; the gospel the Lord preached; various miracles the Lord did afterward: […] […] the Lord: through light [the blind saw]; the dead the Lord raised up; the lame [walked];

  1  and ~body exist Simeon because from Simeon carry bosom
  2  Lord-Jézus-Christ [took_him] Lord see apostle and Jew people-chapter and
  3  this apostle Jew Lord every see inside ~body somebody
  4  time then-exist Lord-Jézus inside thirty year time
  5  from-woman-woman Lord-Jézus and go-Lord from town
  6  until town from temple until temple from
  7  plough until plough and of-Lord apostle go-Lord into_the_world* gospel
  8  preach-Lord various miracle ~do-Lord | ~blind
  9  ~blind SUBJ-Lord through light-Lord die raised_up_(by_the_Lord)* lame*

## 102v — the Passion in short: the sun darkened, the rocks rent

> the body, and the possessed of the evil one, the Lord healed. And the Lord suffered for man's sin, the good of the whole world; the cross […]; and for man of the Lord; to the thief, who […]; and the Lord redeemed man from hell fire. And then the Lord, the cross […] […] […] and the moon, this darkened, before the sun darkened; and before the moon darkened, the face of the earth quaked; the rock, the stone rent; and at the sun's darkening every creature […] this humbled itself, and every creature mourned. Then Christ, the cross […]; and the Lord was put in the sepulchre.

  1  body and evil^ possessed heal-Lord and suffer SUBJ Lord to
  2  somebody-sin good all_the_world on_the_cross-[?] and to-somebody
  3  SUBJ of-Lord to-to-thief-who and somebody redeem-Lord from hell
  4  fire and then-exist-Lord on_the_cross-[?] | sun*
  5  Lord-+name and moon this eclipse before sun eclipse
  6  and before moon eclipse ~earth quake rock
  7  stone rent and on-sun eclipse all^
  8  [...] on-+world this humble and all^ create mourn
  9  then-exist Christ on_the_cross-[?] ~and Lord inside tomb | put

## 103r — the three days: where was the soul?

> said; and then the Lord lay in the sepulchre, the Lord; and the hour, then, went to the Father, God, heaven; to the Father's; the angel; the soul within […] the Lord Jesus, and rose from prayer(?). In turn: the devil in the sepulchre stayed; in turn, the Lord went to hell, and destroyed hell, and redeemed man; hell fire, because | he carried, the Lord, his cross on his shoulder; and man's soul […] of the Lord the Father, all the world, the people. And then the Lord Jesus, from the Father, the Lord God eternal; the soul […] of this Father, this soul

  1  say and then-exist-Lord inside tomb lay-Lord and hour time
  2  go from-father God heaven on-of-father angel soul inside
  3  ~exist-~before Lord-Jézus and rise* from pray
  4  in_turn angel inside tomb stayed in_turn to-Lord go-Lord on-hell
  5  and hell destroy and somebody redeem-Lord fire hell because | carry
  6  Lord of-Lord cross on-of-Lord shoulder and somebody soul-[?]
  7  of-Lord God_the_Father every all_the_world people* and_then Lord-Jézus | from
  8  father of-Lord God heaven* soul-[?] this-God_the_Father this soul

## 103v — the lost sheep, a doxology, and the names in one sign

> of the Lord; from the lost sheep this Lord's soul the Lord redeemed; the wolf; the face of the earth; this Father's soul; the lost sheep [gather] the Lord took; this Father's soul. redeem heavenly until the ages of ages, amen. From every ghost, and from [fared sumptuously] the Lord, from the heavenly, on this the people believe; woman, woman; and […] the Lord […] the angel. On […]-[…]-Mary-Jesus-God-Christ-angel-the-lost-sheep speaks Saint […], the church father. Holy Anne, this Anne, gave birth: [for ever] [and ever] [for ever] to mercy, the commandment; go, on everyone, the whole world.

  1  of-Lord from-+the_lost_sheep this-Lord soul redeem-Lord wolf ~earth
  2  this-God_the_Father soul the_lost_sheep [gather] grab-Lord this-God_the_Father soul
  3  redeem heavenly until chapter-oh chapter-oh
  4  amen from every ghost and from [fared_sumptuously] Lord from heavenly* on-this
  5  people* believe woman woman and [sent] Lord [his] angel | on
  6  [?]-[?]-Mary-Jézus-God-Christ-angel-+the_lost_sheep
  7  speak Saint_[a_church_father] church_father | holy
  8  Anne this Anne be_born
  9  [for_ever] [and] [for_ever] SUBJ
 10  to-have_mercy commandment go on-every all_the_world

## 104r — a creed, from Anne's daughter to the judgment

> the world, that is: then from Anne was born the blessed | Virgin Mary; from Mary the coming of the Lord Jesus Christ; and the Lord went into the world, preached the gospel, various miracles; afterward the Lord suffered for man's sin, for the whole world; the Lord was crucified, and for man the Lord shed his blood, and the Lord redeemed man from hell fire; and man, the Lord; there is the faith in the true Son of the living God: every man shall be saved; and one man shall be damned; and the Lord: he that believeth not, and [perish] one shall be saved; in turn, every man shall be damned.

  1  world* that_is then-exist from Anne be_born happy | virgin
  2  Mary from Mary ~be_born Lord-Jézus-Christ and from Lord go
  3  into_the_world* gospel preach various miracle ~do
  4  Lord and suffer to somebody sin all_the_world crucified Lord and
  5  to somebody SUBJ of-Lord shed_his_blood and somebody SUBJ redeem-Lord
  6  from hell fire and somebody Lord exist believe-chapter
  7  to righteous son living God everybody = be_saved and one
  8  somebody be_damned to and Lord not believe and [perish]
  9  one to be_saved ~but everybody = be_damned

## 104v — blessed are the eyes which see

> Begins this holy gospel, written by holy Luke, in the tenth chapter of his writing. Then said | the Lord Jesus to his apostles and the Jewish people: blessed the two eyes, the two eyes that see the Lord; and you [see] those things which | the apostles see. He said: for many holy fathers, many, writes the church father, many prophets, many kings, many emperors | would have liked, the fathers, church fathers, prophets, kings, emperors, to see this which you […] from […]; and there rose among these Jews one; another church father wanted

  1  here_begins this holy_gospel
  2  write holy-Luke inside
  3  ten chapter of-write
  4  time say | Lord
  5  Jézus disciple^ of-Lord
  6  and Jew people-chapter
  7  to-happy two from
  8  eye-from to-two eye-from this Lord see who you [those_things_which] | see-apostle
  9  say because many holy-father many write church_father many prophet many
 10  king many emperor | would_like_to-father-church_father-prophet-king-emperor
 11  this see who you [blessed_are] from-[?] and
 12  rise among this Jew one another church_father want

## 105r — the lawyer's question, and the great commandment

> tempted the Lord Jesus. And then this Jew answered, the lawyer […]: he who, says the scribe, must do; how? this […] to gain life for ever and ever. Said the Lord Jesus, this […]: [answered] he said: as the scripture is written, says this Jew, this scribe: as the scribe, the scripture is written, within the sixth chapter. Said the Lord Jesus, glad, this Lord, to this Jew: how readest thou the scripture? Right. And then this Jew, this reading, the scripture is written: love the Lord God most high with all thy heart, all thy soul, all thy might, all thy heart; and | thy neighbour as thyself, thy neighbour, the kingdom of heaven. And then the Lord Jesus spoke: right.

  1  tempt Lord-Jézus and_then this Jew answered learn-[?]
  2  he_who* say-church_father must do how? this-[?] gain
  3  living chapter-oh chapter-oh say Lord-Jézus this-[?]
  4  [answered] to-+say pray say the_scripture* write say this
  5  Jew this-church_father pray church_father the_scripture* write inside
  6  six chapter say Lord-Jézus joy this-Lord this-Jew how?
  7  read^ the_scripture* righteous and_then this Jew this read^
  8  the_scripture* write love Lord_God highest ~every heart all^ of-somebody
  9  soul all^ of-somebody might all^ of-somebody heart and | of
 10  somebody exist-exist how?-to somebody neighbour of-somebody SUBJ
 11  heaven land and_then Lord-Jézus righteous speak

## 105v — who is my neighbour? A certain man went down to Jericho

> the Jew: for whoever believes in one God, to […] literally, love thy neighbour as thyself, thy neighbour; of […] heaven; in turn […]; and the man's mouth went on; and then […] proud, this Jew. And then he answered: who is my neighbour? […] said the Lord Jesus [answered] and said, as he said, the scripture, right: and from there was a living servant; through sin whosoever, a man, the Lord God; and exorcised(?); on the Lord's mercy; and then whosoever, the man, went into the wilderness, to one place […] Jericho; in turn, in turn; from evening to build(?); and then went the servant, the man, into the wilderness; and then fell among robbers.

  1  Jew because and man^ believe one God to-cut_off-literal
  2  love man^ of-somebody ~brother how?-to man^ neighbour
  3  of-[?] heaven ~land and mouth man^
  4  leave-leave and then-[?] proud this Jew and_then
  5  answered who? exist of-+say [?]-~year-~exist-DIV say
  6  Lord-Jézus [answered] to-+say pray who-+say the_scripture* righteous
  7  and from exist living-~servant commit sin of-~somebody-~Adam
  8  Lord_God and exorcise on-of-Lord have_mercy and then-exist
  9  go-~somebody-~Adam on-~field to-one place °forgive-+SUBJ
 10  Jericho in_turn-chapter-in_turn evening-from-to build-to and then-exist go
 11  ~servant ~Adam on-~field and then-exist fell_among robber

## 106r — stripped, half dead; the priest and the Levite pass by

> And the robbers began, to the man; the holy(?) found; and then these robbers let the man go, having taken the booty; and the robbers beat the man, this man dying; and half dead and half alive. That way went one, a descendant of Abraham, a priest's son; the man; on seeing, the descendant of Abraham passed the man by, and | went. The descendant of Abraham went. Then, second, began a descendant of the scripture, a Levite's son; the man […] the descendant of the scripture passed the man by, and went […] the man could; the two, of Abraham, of the scripture, good, afterward, passed the man by; through went the two of Abraham, that way.

  1  and begin robber to-~Adam ~rich ~find
  2  and then-exist this robber remit ~Adam grab
  3  booty and ~Adam beat robber
  4  die-this ~Adam and half_dead and half_alive
  5  thus go ~on one descendant-Abraham who-to
  6  ~Adam on-see-descendant-Abraham long-~Adam and | go
  7  descendant-Abraham go ~on the_rest^ ~begin descendant_of_Moses who-to ~Adam
  8  [?]-descendant_of_Moses long-~Adam and go [by_chance]
  9  ~Adam can-two-Abraham-?the_scripture good ~do
 10  long-~Adam through go-two-Abraham thus

## 106v — the Samaritan binds his wounds and pays the host

> Went on one Samaritan, to Jerusalem, the Lord's living servant; and saw his face, found him, and had compassion on the man; afterward, for the Lord poured wine into the man's wounds, and had mercy; one; to the Lord long; in turn the Lord's faith; bound up the man's wounds, and the man | he put, the Lord, on his own shoulder; and the man he carried, to the Lord's lodging; and the man this innkeeper took. And the innkeeper took two [pence], two denarii; and then this innkeeper, this innkeeper, on the man take care; on this, that, whatever more on the man | […]

  1  go ~on one Samaritan on-Jerusalem of-Lord living-servant
  2  and face found and have_mercy to-~Adam
  3  ~do because pour-Lord wine of-~Adam
  4  wound and have_mercy one-to long-Lord in_turn of-Lord believe
  5  bound_up of-~Adam wound and ~Adam | place^
  6  Lord on-of-Lord shoulder and ~Adam from-carry to-Lord
  7  on-lodging and ~Adam grab this innkeeper
  8  and innkeeper grab two [pence] two denarius
  9  and_then this innkeeper this-innkeeper on-~Adam
 10  carry on-~exist-this who to-whatever on-~Adam | little

## 107r — which of these three was neighbour? Then Augustine begins

> the innkeeper; then, when I come again, everything this innkeeper I repay. And then the Lord Jesus asked, this Lord, this Jew: who was this good neighbour among | the […] of Abraham, the one of the scripture, the Samaritan? And then this Jew say: and this said, he spoke and said: he is [neighbour] the good neighbour, and […] did mercy to the man. And then the Lord Jesus, right, spoke to the Jew. And then the Lord Jesus, | this Jew brought(?); and he said: stay, do, said, it is, said he, the kingdom of heaven. The end of this holy gospel. Speaks holy Matthew: from the one denarius is signified

  1  innkeeper then-chapter go doomsday every this-innkeeper return^
  2  and_then Lord-Jézus judge this-Lord this-Jew who?
  3  SUBJ this good one-?heavenly-~year among | [?]-Abraham-+one-?the_scripture
  4  the_Samaritan and_then this Jew [say]
  5  and this-+say speak-+say he_is* [neighbour] good one-?heavenly-~year
  6  and name-[?] have_mercy to-~Adam do and_then
  7  Lord-Jézus righteous SUBJ speak-Jew and_then Lord-Jézus | this
  8  Jew brought* and he_said* stay do-+say
  9  exist of-+say heaven land end this
 10  holy-gospel speak holy-Matthew from one denarius symbolize

## 107v — the two pence, by Augustine; and the opening of the next reading

> the Old Testament faith; in turn the two denarii signify the birth and death of the Lord Christ, speaks Saint Augustine the church father, […] […]. little [the Old] [the New] says God, in turn, for ever; God swallow; from the thirty [years] [preached], from the high food. Before the gospel, says | the Lord Jesus to his apostles and the Jewish people: because see | he is [so] good; do what is pleasing, and thanks to the Lord, the Lord God. Begins this holy gospel, written

  1  Old_Testament believe in_turn-two denarius symbolize ~on-be_born
  2  and die Lord-Christ speak Saint_Augustine_the_church_father [two_pence] [Testaments.]
  3  little [the_Old] [the_New] say God but exist-exist-chapter
  4  God swallow on-from thirty [years] [preached] from to-high-food
  5  before gospel say | Lord
  6  Jézus apostle of-Lord and
  7  Jew people
  8  because see | ~you-chapter
  9  [so] good
 10  do pleasing
 11  and thanks to-Lord Lord_God here_begins this holy_gospel write

## 108r — ye are the salt of the earth, and a city set on a hill

> written by holy Matthew, in the fifth chapter of his writing. Then said the Lord Jesus to his apostles and the Jewish people: ye are the salt of this world. In turn, if this salt lose its taste, it is good for nothing, out, the salt is thrown out, and the people trample on the salt, because this is set on high. Do ye good. And then the Lord Jesus: a city on a high mount, and the city cannot be hid; the people see it; and then [trodden down] the people to the city. Chapter to chapter, this; and you, learn, you, do good; in turn whosoever is high, of the two, teach the people, and do; found among the people, a man, mercy.

  1  holy-Matthew inside five chapter of-write time say Lord-Jézus
  2  apostle of-Lord and Jew people you salt
  3  this world* in_turn lose_savour this salt good-apostle-God out-out
  4  salt cast_out and salt people trample
  5  because this exist high you good_deed = and_then
  6  Lord-Jézus and SUBJ city on-high to_the_mount and city [up]
  7  people see and then-+SUBJ [trodden_down] people to-+city.
  8  chapter-go-to-chapter this and you on-learn you
  9  good_deed = in_turn-who-exist high from-two people on-learn
 10  and do found among people man^ have_mercy

## 108v — the candle and the bushel, and the Father's house

> and love the Lord [candle]; whosoever loveth the Lord, and believeth in the Lord, and from the man receives; of you, of the Lord, in teaching [which] the Lord teacheth; this Lord taketh you; and from the man goes into the Lord's Father's house, | where is joy for ever and ever, amen. In turn, then, out, the building, to cut off, the man is the city from […]. And then the Lord Jesus: then a man giveth light, lighteth a man; to this [before men] light, who is a lamp on a candlestick put; a man doth, a man, to the pit(?), the bushel; a lamp on a candlestick a man putteth, who letteth it give light; all the people see, he who is in the house; and you,

  1  and love-Lord [candle] ~somebody-and love-Lord man^ and believe inside-Lord and from
  2  man^ grab from you of-Lord on-learn [which]
  3  learn-Lord this-Lord you grab-Lord and from man^ go
  4  inside of-Lord God_the_Father house | exist joy chapter-oh
  5  chapter-oh amen in_turn then-chapter out building to-cut_off man^
  6  exist city from-[?] and_then Lord-Jézus then-chapter man^
  7  giveth_light* light man^ to this [before_men] light who-exist lamp
  8  on-candlestick put man^ do man^ to-pit-~year but
  9  lamp on-candlestick put-somebody who-exist release^
 10  giveth_light* every people see he_who* inside house and you

## 109r — whosoever shall do and teach them

> the lamp of this world, that is: learn from the Lord Jesus and from the holy gospel. And then the Lord Jesus: many believe; there is a man who beareth the people until the day of judgment; and one believeth, the second is gone. In turn believe this Lord letteth you go. And then the Lord Jesus: and whosoever keepeth that which the scripture abound, and from the man is this rightly taught; in turn, and whosoever keepeth that which the scripture abound and from whosoever teacheth this not rightly. And then the Lord Jesus: and whosoever keepeth that which the scripture writeth, of the man good afterward; he shall see heaven, pleasing. In turn, and

  1  lamp this world* that_is learn from Lord-Jézus and from holy-gospel
  2  and_then Lord-Jézus great^ believe exist man^ carry people
  3  until judge-~year and one believe two exist
  4  leave-leave but believe* this-Lord you remit-Lord
  5  and_then Lord-Jézus and man^ exist carry he_who* the_scripture*
  6  abound* and from man^ exist this righteous on-learn
  7  in_turn and man^ exist carry he_who* the_scripture* abound*
  8  and from whosoever* is_not this righteous on-learn and_then Lord-Jézus
  9  and man^ exist carry he_who* the_scripture* write of-somebody
 10  good ~do exist see heaven pleasing in_turn and

## 109v — the end of the Matthew reading, and a new one from Luke

> the man keepeth not that which the scripture […] | of the man, good afterward, shall not see the pleasing things of the Lord, from the Father. The end of this holy gospel. The Lord God: love the Lord God. Begins this holy word, written by holy Luke, in the ninth chapter of his writing. Then went the Lord Jesus to Jerusalem; and then went the Lord Jesus to the mount of Olives, over against Jerusalem, in turn; and the Son of God saw down over Jerusalem, in turn; and cried out, | the Lord Jesus. And then: Jerusalem, Jerusalem! Then this Jerusalem [Bethphage] and this Jerusalem

  1  man^ is_not bring^ he_who* the_scripture* abound* | of
  2  man^ good ~do is_not show^ pleasing of-Lord
  3  from-God_the_Father here_ends this holy_gospel Lord_God love Lord_God
  4  here_begins this holy_gospel
  5  write holy-Luke
  6  inside nine chapter of-write
  7  time go Lord-Jézus
  8  Jerusalem and then-exist go
  9  Lord-Jézus of_the_olives mount highest Jerusalem in_turn-chapter-in_turn and
 10  show^ son God down Jerusalem in_turn-chapter-in_turn and cry_out | Lord
 11  Jézus and_then Jerusalem Jerusalem then-exist this-Jerusalem [Bethphage] and this-Jerusalem

## 110r — if thou hadst known; the army that shall compass thee

> […] because there is much misery upon this Jerusalem. Why? this | what […] who this […], said the man; the apostles | of the Lord said; and who this Lord preached, and this faith And then the Lord Jesus, then this Lord, the Son of God, weeping over this Jerusalem, because there shall come upon this Jerusalem […] an army; | this this shall sit about Jerusalem, and this Jerusalem [thine enemies] compass round; [straiten thee] and thou knewest not, man, the devil exist a man, the devil, out; and [stone] […] [visitation] among you taken captive, all of them, the cross, condemned, the man, the devil, and not, he said, of hunger shall die; and there is much misery upon this

  1  chapter-+new because exist many misery ~on-this Jerusalem why? this | what
  2  believe* who this faith* say-somebody apostle | of
  3  Lord say and who this-Lord preach and this faith*
  4  and_then Lord-Jézus then-exist this-Lord son God crying
  5  this-Jerusalem because exist on-this-Jerusalem [trench] an_army | this
  6  this to-sit Jerusalem and this-Jerusalem [thine_enemies] surround
  7  [straiten_thee] and you is_not somebody angel exist
  8  somebody angel out and [stone] name-Jerusalem but [visitation] among you
  9  capture every-+say on_the_cross condemned* somebody angel and
 10  ~exist-+say hunger? die and exist many misery ~on-this

## 110v — Jerusalem destroyed by Vespasian and Titus, and the temple cleansed

> Jerusalem; for this Jerusalem, all Jerusalem, the Roman destroyed, at their head | Vespasi- -anus, and his son Titus; […] stone upon stone | shall not be left; [them that sold] faith. And the Lord Jesus went into the Jerusalem temple; and then the Lord found within them that sold, the sellers of doves; and the Lord Jesus made of small cords a whip, and all of them [drove out] out, out, cast out the Lord. And then the Lord Jesus: this is the house of prayer, this house; make it pleasing to the Lord, of the Father. In turn ye, the house, have made, said he, a den of thieves. And from thence the Lord Jesus, from until Palm Sunday, until many […]. The end of this | holy gospel.

  1  Jerusalem because this-Jerusalem every-Jerusalem destroyed the_Roman on-head | Vespasi-
  2  -anus son Titus that stone on-stone | shall_not_be
  3  left [them_that_sold] believe and go Lord-Jézus
  4  within^ Jerusalem temple and then-exist Lord within^ found [them_that_sold]
  5  dove_seller and do Lord-Jézus of_cords
  6  cords scourge^ and every-+say [drove_out] out-out
  7  cast_out Lord and_then Lord-Jézus this_is prayer^
  8  house this house SUBJ do on-pleasing of-Lord from
  9  God_the_Father in_turn you house do-+say
 10  one thief house and from-exist Lord-Jézus from
 11  until Palm_Sunday until many Wednesday end this | holy
 12  gospel

## 111r — the five sorrows of the Son of God

> All the writings speak of five sorrows of the Son of God. The first sorrow of the Son of God: then the Lord God destroyed five, in turn; and not only sorrow of the Lord's eye, but rather greatly sad. The second sorrow, the writing speaks of the coming to the city of Bethlehem, because the Lord Jesus foresaw that he is, upon many, […] suffering | upon the coming of the Lord. The third sorrow, the writing speaks | of Palm Sunday: then he sat and saw, in turn, Jerusalem; not only the sorrow of the Lord Jesus for the house and for the building, literally, in the middle; in turn, the sorrow of the Lord Jesus for his own creature, who the Lord created for himself, [wept] because the Lord Jesus foresaw then

  1  every write speak five sorrow* son God first sorrow*
  2  son God then-exist destroy Lord_God five in_turn-chapter-in_turn
  3  and not_only sorrow* Lord eye but_rather* highest sad two sorrow* write
  4  speak on-~be_born Bethlehem city because
  5  foresee Lord-Jézus he_is* on-many [how_often] suffering | on
  6  ~be_born Lord third sorrow* write speak | on
  7  Palm_Sunday then-exist sit see on-in_turn-chapter-in_turn
  8  Jerusalem not_only sorrow* Lord-Jézus to-house and to-+building literal amid
  9  in_turn-chapter-in_turn but sorrow* Lord-Jézus to-of-Lord create he_who*
 10  create-Lord to-Lord [wept] because foresee Lord-Jézus then-exist SUBJ

## 111v — Jerusalem falls, and a mother eats her son

> the people shall go, all scattered. And then, at the execution of the Lord Christ: ten and ten, and four years; then took the Lord God power, the Roman, at their head; and at their head | there was by name Vespasian, and Titus; and these were father and son; and then the two, father and son, destroyed Jerusalem, all Jerusalem, [shall fall] even to the ground; and stone upon stone shall not be left. And | two, father and son, much misery upon them, did the son, the two, the father; because one said: of hunger they die. In turn the second said: how shall we, of hunger? [famine] In turn, of my son eat. The third said, they said, and they said, out, […] and […] head.

  1  say people go every scattered and then-exist on-execute Lord
  2  Christ one-ten-+one-ten and two-two-year time grab Lord_God
  3  can Roman on-head and on-head | and-exist
  4  exist-+name exist Vespasian and Titus and this exist
  5  from-father son and then-exist two-father-son destroyed Jerusalem every Jerusalem [shall_fall]
  6  until ground and stone on-stone shall_not_be_left and | two
  7  father-son many misery on-+say do-son-two-father
  8  because one say hunger die in_turn-two say how_shall_we-+say
  9  hunger [famine] but of-+say son eat third say
 10  say and-+say out [?]-+say and °take_heed-+say head

## 112r — thirty Jews for one penny, because Judas sold for thirty

> among them taken captive, all of them, the cross, executed, but […] and there is a head crucify [sold] a head; and they could a head [a penny] find; and there they were, executed, a head […] sold, a head thirty for one denarius; and they, | from sell a head let go; in turn, until, in turn, went take a head; and they, nine hundred for thirty denarii; and the head, more, they took; but it is. Judas, and they sold. The fourth sorrow, the writing speaks of Holy Tuesday: then Lazarus at the tomb, of the Lord; not only sorrow,

  1  among say capture every say on_the_cross execute °but_rather-[?] and
  2  exist head crucify* [sold] head and say can
  3  head [a_penny] on-find on-exist-+say-+SUBJ
  4  execute head [?]-+SUBJ vend head
  5  on-thirty to-one denarius and-+say SUBJ | from
  6  sell* head remit in_turn-chapter-in_turn ~until in_turn-chapter-in_turn go
  7  take* head and say nine hundred to-thirty denarius
  8  and head SUBJ more grab but_rather* exist.
  9  Judas and say vend in_turn-two-two sorrow* write
 10  speak on_Holy_Tuesday = then-chapter Lazarus on-tomb among-Lord not_only sorrow*

## 112v — the fourth and fifth sorrows: Lazarus, and Good Friday

> the eye of the Lord Jesus, | but rather greatly sad, because Lazarus […] […] among, out, at the tomb; because three days was Lazarus in the tomb; and Lazarus [was sick] health out, of the Lord. The fifth sorrow, the writing speaks of Good Friday: then Christ crucified, because […] [not only] man, the Lord died; not only sorrow of the eye of the Lord Jesus, but rather greatly sad, sad for the people […] in the Lord […] believe; because foresaw | the Lord Jesus […] that the people shall go, all scattered; because there is [looked up] the heavenly Jerusalem. The end of this teaching, the holy gospel. For on the day of judgment […] the angel divideth, the angel, the evil: how? one rejoiced […]; one […]

  1  eye Lord-Jézus | but_rather highest sad because Lazarus [was_sick] health among
  2  out on-tomb because three_days exist Lazarus inside tomb and Lazarus
  3  [was_sick] health out among-Lord fifth sorrow* write
  4  speak on_Good_Friday = then-chapter Christ crucified because to-°high-Lord
  5  [not_only] somebody die-Lord not_only sorrow* eye Lord-Jézus but_rather highest sad
  6  sad to people [groaned] inside-Lord [troubled] believe because foresee | Lord
  7  Jézus [?]-+SUBJ say people go every scattered because-exist
  8  say [looked_up] heaven Jerusalem end this learn holy-gospel
  9  because on-judge-year [?]-angel divide angel evil
 10  how? one rejoiced [wept] one [?]-+say

## 113r — the division at the judgment, and the opening of the Prodigal Son

> die; this is: in two divided, the firstborn rejoiced, let go; in turn this younger rejoiced, let go, this; and the man divideth on the day of judgment: one gate to the evil; in turn the second taketh within the kingdom of heaven, but the Lord; there are many speak joy. Begins this holy gospel, the writing, the holy gospel, written by holy Matthew, in the first chapter of his writing. Then said the Lord Jesus to his apostles and the Jewish people: there was one holy Lord God; and then the Lord God had two sons, the angel, the soul; and this younger son of the soul then asked for the soul's

  1  die this_is on-two divide firstborn rejoiced remit
  2  in_turn this younger rejoiced remit this and man^ divide
  3  on-judge-year one gate on-~evil in_turn-two give^ inside
  4  heaven land °but_rather-Lord exist many speak* joy
  5  here_begins this holy_gospel
  6  write holy-gospel
  7  write holy-Matthew inside one chapter
  8  of-write time
  9  say Lord-Jézus apostle of-Lord
 10  and Jew people exist
 11  one ~rich Lord_God and then-exist have Lord_God two son
 12  angel soul and this younger soul-son then-exist soul ask

## 113v — the younger son takes his portion and wastes it

> portion of the soul's son, of the Father; and then the son of the soul had much wealth, took it of the Father; because the son of the soul rightly [substance] took of the Father this, of the soul's son, of the Father. And the son of the soul went far, into a | city there was; and the son of the soul stayed in that land, and | began the soul's son to waste it all; the son of the soul stayed in that land, because | began the soul's son to live riotously; and then, many years, the son of the soul stayed there. | In turn it was; and there was left; he began to be hungry, this; and the son of the soul how shall he understand? for the […] son: the holy eye, speech, hearing, love, mercy, faith, righteousness: the five senses […] of the Father. And the son of the soul went to a swineherd, and

  1  divide of-soul-son God_the_Father and then-exist soul-son exist many ~rich
  2  grab God_the_Father because soul-son righteous [substance] grab God_the_Father this
  3  of-soul-son God_the_Father and go soul-son far inside | town
  4  exist and leave soul-son inside land and | begin-soul
  5  son from every prodigalize leave soul-son this land because | begin-soul
  6  son lived_riotously and then-exist many-year leave soul-son this | in_turn
  7  exist-exist and leave hunger this and soul-son
  8  how_shall_we* understand because remain-[?] | rich-eye-say-hear-love-have_mercy
  9  believe-righteous-+five-sense-[?]
 10  God_the_Father and go soul-son one pigman and

## 114r — the swine, the husks, and "I will arise and go to my father"

> son this swineherd, evil; and the son of the soul began of the evil swine son; and the son of the soul, how shall he be fed? In turn the son of the soul began […] […] […] he who | sinned, from […] understood; and the son of the soul began to speak: my | Father God has hired men and servants, goodly, left over, in turn; this son of the soul is left, and good bread they eat. Mercy, Lord God! The hired men, the servants, in turn; this son of the soul eateth. And then this younger son, this son of the soul, and the son of the soul went. The son of the soul would go to the Father [hired servants]; the son of the soul, humbled, would

  1  son* this pigman evil and begin-soul-son
  2  of-evil pig [...] and soul-son how_shall_we*
  3  food but begin-soul-son name-from-+name [husks] [swine] he_who* | sin
  4  [?]-from understand and begin-soul-son speak have | from-father
  5  DIV of-soul-son labourer and servant good ascension^
  6  but this-soul-son ascension^ and tasty bread eat have_mercy
  7  Lord_God labourer servant but this-soul-son eat and_then
  8  this the_younger_son this-soul-son and go-soul-son.
  9  of-soul-son from-God_the_Father want [hired_servants] soul-son ~humble want-soul-son

## 114v — the father sees him afar off; Father, I have sinned

> mercy, this; and this younger son went to his Father God. And the son of the soul saw afar off, this, his Father God; and the son of the soul began recognize that, rightly, of his Father God, the son of the soul; and the son of the soul recognize that, God, the son of the soul; and the son of the soul went, this son of the soul, before his Father God; and the son of the soul knelt down before his Father God; and the Father God began to pray, the Father God of the son of the soul asked, this son of the soul; this Father had mercy on the son of the soul, who, this son of the soul, through the sin of the soul against this Father and against the Lord God

  1  have_mercy this and go this the_younger_son to-of-soul-son
  2  God_the_Father and soul-son see far this of-soul-son
  3  God_the_Father and soul-son begin-soul-son recognize that* righteous
  4  of-God_the_Father soul-son and soul-son recognize that*
  5  God soul-son and go-soul-son this-soul-son before
  6  of-soul-son God_the_Father and kneel-soul-son before
  7  of-soul-son God_the_Father and God_the_Father begin pray God_the_Father
  8  of-soul-son ask this-soul-son this-father have_mercy-soul-son
  9  who this-soul-son through ~sin-soul against this-father and against Lord_God

## 115r — bring forth the best robe: of love, of mercy, of righteousness

> and the son of the soul, mercy, this Father, of the son of the soul, all of the son of the soul, through the sin he who left, through the sin […]. And then this Father God of the son of the soul, the hired men and the servants, the holy apostles, the teaching, and the angel went, the apostles, the teaching, the angel; and | they brought, the apostles, the teaching, the angel, the most beautiful robe: the Lord's robe, that is love, the Lord God; the Lord's robe, that is mercy, the Lord God; the Lord's robe, that is | the Lord God; the Lord's robe, that is righteousness, the Lord God. And the son of the soul, from | the Father, the apostles, the teaching, the angels, within the law, to the Lord's faith; and | the son of the soul went, the apostles, the teaching, the angels, into his Father God's house; there is

  1  and soul-son have_mercy this father of-soul-son every of-soul-son
  2  commit sin he_who* from-leave through ~sin-[?] and_then this
  3  of-soul-son from-God_the_Father labourer and servant holy-apostle-learn
  4  and angel go-apostle-learn-angel and | carry-apostle-learn
  5  angel fairest robe Lord believe SUBJ love Lord_God
  6  Lord believe SUBJ have_mercy Lord_God Lord believe SUBJ | Lord_God
  7  Lord believe SUBJ righteous Lord_God and soul-son from | father
  8  apostle-learn-angel-angel inside law to-Lord believe and | soul
  9  son go-apostle-learn-angel-angel inside of-God_the_Father house there exist

## 115v — the elder brother in the field hears the music

> joy for ever and ever, amen. And | among this. The Father of the son of the soul, the Father God, all of the Father God [elder son] [in the field] the neighbour; and the neighbour began to rejoice, the apostles, the Father God, the teaching, the angel, from […] the word […] and […] […]; and then was not this firstborn at home, because he was in the field. That is: within, the angel's joy; and he heard a sound, | of the son of the soul, of the Father God, the heavenly house, that is, within the heavenly city it is. And the son of the soul went, dying, this younger son, to his Father God's heavenly house; and the angel went,

  1  joy chapter-oh chapter-oh amen and | among-this.
  2  father of-soul-son from-God_the_Father every of-God_the_Father [elder_son] [in_the_field]
  3  one-?heavenly-~year and begin-[?] ~joy apostle-God_the_Father-learn-angel
  4  from-[?] word [music] and [dancing] [asked] and then-~exist this
  5  firstborn exist-exist home because-exist on-field
  6  that_is inside angel joy and hear voice | to-of
  7  soul-son from-God_the_Father heaven house that_is inside heaven | town
  8  exist and go-soul-die-son this the_younger_son | on
  9  of-soul-son from-God_the_Father heaven house and go-angel

## 116r — he was lost, and is found; the end of the gospel

> this angel, the firstborn, was, to his angel, of the Father God. And then his angel, of the Father God, of the Father God, his angel [hath this world's goods] this Father, the angel, took one, rejoiced, died; and one loaf of bread, love was, this angel, of the joy of his angel […]; in turn, on this the son of the soul, joy, the Father. And understanding he took from this Father: much wealth, the eye, speech, hearing, love, mercy, faith, righteousness, the five senses. And then this Father, of his angel, of the Father God, the son, of the Father God: lo, there is the son of the soul, who was lost, […] the servant; and the son of the soul was dead, and is risen from death, and is saved. The end of this holy gospel.

  1  this angel-firstborn exist-exist to-of-angel from-God_the_Father
  2  and_then of-angel from-God_the_Father from-God_the_Father of-angel [hath_this_world's_goods]
  3  this father angel grab one rejoiced die and
  4  one loaf bread love-exist this-angel
  5  from-joy of-angel one-+friend in_turn on-this soul-son joy
  6  father and understand grab from this father many ~rich | eye-say-hear
  7  love-have_mercy-believe-righteous-+five-sense and_then
  8  this father of-angel from-God_the_Father son of-God_the_Father lo
  9  exist soul-son was_lost | release-angel-[?]-[?]-labourer
 10  servant-and soul-son exist die and rise* on-die be_saved
 11  here_ends this holy_gospel

## 116v — John the Baptist, and the soldiers and publicans who came to him

> Before the gospel: written by holy John the Baptist; this word is written. Then it was, the Lord Jesus within his twentieth year and within the ninth year, within that time preached holy John the Baptist, on Carmel, on the mount; and he went. This John, the two [publicans], the soldiers, the Pharisees, the farmers, and the sinful people; because there went soldiers, Pharisees, farmers, and sinners, to be taught by John on Carmel; and first the people were, the soldiers,

  1  before gospel-+SUBJ
  2  write holy-John
  3  the_Baptist/woman this word write
  4  time then-exist
  5  Lord-Jézus inside | two-ten-ten
  6  year and inside nine year inside
  7  time preach
  8  holy-John the_Baptist/woman on-Carmel to-mount and go.
  9  this-who John two-two [publicans] soldier Pharisee farm and sin
 10  people because exist go soldier Pharisee farm and sin on-learn
 11  to-John on-Carmel on first people exist soldier

## 117r — John the Baptist answers the soldiers, and then the Pharisees

> people; in turn the second people are the Pharisees, the Jews; the third people are the farmers, the people; in turn the fourth people are the sinners. First said the soldiers, the people; the soldiers answered; the soldiers went to this John to be taught, in a dream(?) taught. The soldiers: how shall we be saved? they spoke. And to the soldiers, holy John the Baptist: the soldiers' holiness, and of the soldiers' faith: begin to give alms, soldiers, to God, [content] the poor of God, and be merciful, soldiers, and righteous, soldiers; that is, yours is the kingdom of heaven. Then said the Pharisees, the Jews, to John; the Pharisees answered; the Pharisees went to this John to be taught, in a dream taught. The Pharisees: how shall we be saved?

  1  people in_turn-two people exist Pharisee Jew third people exist
  2  farm people in_turn-two-two people exist sinners*
  3  first say soldier people answered-soldier go-soldier this-John
  4  on-learn on sleep learn exist soldier how_shall_we* be_saved | from
  5  speak and soldier holy-John the_Baptist/woman of-soldier ~rich and | of
  6  soldier believe on-begin donate soldier God [content] poor_man_of_God^
  7  and exist-soldier have_mercy-soldier and righteous-soldier exist | ~you
  8  yours heaven land time say the_Pharisees*
  9  Jew to-John answered-Pharisee go-Pharisee | this
 10  John on-learn on sleep learn exist the_Pharisees* how_shall_we* be_saved

## 117v — the Pharisees and the farmers get their answers

> they spoke. And to the Pharisees, holy John the Baptist: and have this, ye Pharisees, righteous people; preach, and teach the sinful; how is sin, from redeem. And be ye Pharisees merciful, ye Pharisees, and righteous, ye Pharisees; there is yours the kingdom of heaven. Then said the farmers, the people, to John; the farmers answered; the farmers went to this John to be taught, in a dream taught. The farmers: how shall we be saved? they spoke. And to the farmers, holy John the Baptist: and have this, ye farmers; you, farmers, farm, till the ground, and conceive, and rightly, of the farmers, not, living; and to the poor of God give alms; be ye farmers merciful, ye farmers, and righteous, ye farmers; yours is the kingdom of heaven.

  1  from-speak and the_Pharisees* holy-John the_Baptist/woman and have this the_Pharisees.*
  2  righteous people preach and sin learn how? exist sin | from
  3  redeem* and exist-Pharisee have_mercy-?the_Pharisees and righteous-?the_Pharisees exist
  4  you heaven land time say farm.
  5  people to-John answered-farm go-farm this-John
  6  on-learn on sleep learn exist farm how_shall_we* be_saved from-speak
  7  and farm holy-John the_Baptist/woman and have this-farm you
  8  farm farm plough? and conceive and righteous of-farm not-not
  9  living and poor_man_of_God = donate exist-farm have_mercy-farm
 10  and righteous-farm exist you heaven land

## 118r — and the sinners, who get the great commandment

> Then said the sinners; the sinners answered; there went the sinners to this John to be taught, in a dream taught. The sinners: how shall we be saved? they spoke. And to the sinners, holy John the Baptist: and have this, sinners; love the Lord God, lift up all your hearts, all your souls, all your might, all your heart; and your neighbour as thyself. Be ye sinners merciful, sinners, and righteous, sinners; and keep, sinners, the commandments of God; […] a hundred […] sins, and be saved, sinners, [with all thy strength], not, for ever and ever, amen; there is

  1  time say sinners* answered-?sinners | go
  2  sinners* this-John on-learn on sleep learn exist.
  3  sinners* how_shall_we* be_saved from-speak and sinners*
  4  holy-John the_Baptist/woman and have sinners* love Lord_God
  5  from-raise all^ heart all^ of-?sinners soul all^ of-?sinners
  6  might all^ of-?sinners heart and of-?sinners
  7  exist-exist how?-to somebody neighbour exist-?sinners | have_mercy
  8  sinners* and righteous-?sinners and carry sinners*
  9  commandment God ~exist-hundred-[?]-~sin be_saved sinners*
 10  [with_all_thy_strength] not-not chapter-oh chapter-oh amen exist

## 118v — the commandment summed up, and a new reading from Luke

> yours the kingdom of heaven. This teaching is [murmured] not love the Lord God most high with all thy heart; and the man who keepeth the commandments of God, his is the kingdom of heaven. And this is: this love, the commandment, take from […] to be saved; and the man who believeth in the Lord Jesus Christ, that he is the true Son of the living God, every man shall be saved; and one is not damned but: every man shall be saved. Begins this holy gospel, written by holy Luke, in the seventh chapter of his writing. Then was the Lord Jesus in his thirtieth year and one day; then went the Lord Jesus into the Pharisees' town; and there went to the Lord all these, and the sinners; this, who, the Lord Jesus, and

  1  you heaven land this learn exist [murmured] not* love | divine_one^
  2  DIV highest every heart and man^ and exist carry commandment God of-somebody
  3  SUBJ heaven land and this_is this love commandment grab
  4  from [?]-°again on-be_saved and man^ and exist believe
  5  inside Lord-Jézus-Christ he_is* righteous son living God everybody =
  6  be_saved and one is_not be_damned but everybody = be_saved
  7  here_begins this holy_gospel write holy-Luke inside seven chapter | of
  8  write time then-exist Lord-Jézus inside thirty one-~year
  9  time go Lord-Jézus inside Pharisee town and go
 10  to-Lord who-and-this-and sinners* this-who Lord-Jézus and

## 119r — the Lost Sheep

> […] Pharisees and the scribes murmured at the Lord Jesus, that the Lord spoke [as] the Son of God; and when the Lord was the Son of God | this Lord […] went, this […] […] the Lord Jesus | when What man is there among you | who has one hundred sheep in the wilderness, and if he lose one of them […] […] […] the man is […] the lost one […] and does he not leave the ninety sheep and nine in the wilderness, and go, the man […] nine, [after] the lost one to find it; and when he finds the lost one, and the man takes it up […] | upon

  1  begin-?the_Pharisees Pharisees* and church_father murmur on-Lord-Jézus this-Lord speak
  2  son God in_turn then-exist this-Lord exist son God | this
  3  Lord [leaveth] go this [in_the_desert] and_then Lord-Jézus | then
  4  exist one have call^ you | one
  5  hundred sheep inside wilderness^ and then-exist lose one
  6  call^ end* [layeth_it] [shoulders] man^ exist answered-hide-~year ~who-chapter-say
  7  and exist from-food-somebody from nine-ten sheep and nine
  8  inside wilderness^ and go-somebody ninety* nine the_lost_sheep
  9  find and then-exist the_lost_sheep find-somebody
 10  and the_lost_sheep grab-somebody man* | on

## 119v — the lost sheep found, and the woman with ten pieces of silver

> on his shoulder; and the man went to his friends and neighbours, and he is, with friend and neighbour; he said to them: I have found, my sheep, which [which was lost]; mine is this, this. Oh! And good, over the sheep, joy; in turn, over the ninety and nine sheep. And then the Lord Jesus: then one woman, the head, and she had ten drachmas; and then of these ten she loseth one. Eve; and there is light, Eve, the son of Mary, born, crucified, the lamp; and then Eve findeth this drachma, the kingdom of heaven; and there is good, over heaven, the kingdom, joy, Eve; over the Lord Christ's dying,

  1  of-somebody shoulder and go-somebody to-of-somebody friend and neighbours
  2  and exist and-friend-neighbor say-somebody say exist | found
  3  somebody sheep [which_was_lost] somebody exist this-this oh and
  4  good on-~sheep joy ~but on-nine-ten and nine sheep/a_female_person
  5  and_then Lord-Jézus then-exist one woman ~head
  6  and exist have ten silver^ and then-exist this ten loseth_one*
  7  Eve and exist light Eve | Mary-son
  8  be_born-+crucified lamp and then-exist find Eve
  9  this silver^ heaven land and exist good
 10  on-+heaven land joy Eve on-die-Lord-Christ

## 120r — the ninety-nine, and the nine orders of angels

> Eve's joy; in turn, over the feeding, the nine drachmas, the law. The end of this holy gospel. Then the Lord [telleth], the Lord Jesus [healeth], the sufferer. The gospel: said the Lord Jesus to his apostles and the Jewish people, this Lord: one Lord, this sheep; because to the Lord, this Lord abandon the Lord, the nine orders of angels within the kingdom of heaven. And then the Lord Jesus, then the Lord bowed down, from the Father God, heaven, into the kingdom of heaven, upon many angels, upon the angel whose name is Lucifer, and the second angel, and Lucifer, as he was; and forty thousand years

  1  Eve rejoice^ but on-food nine drachma law end
  2  this holy-gospel then-exist-Lord [telleth] Lord-Jézus [until] sufferer
  3  gospel say Lord-Jézus apostle of-Lord and Jew people this-Lord
  4  one Lord this sheep/a_female_person because to-Lord this-Lord | abandon
  5  Lord nine order angel inside heaven land
  6  and_then Lord-Jézus then-exist-Lord bow from-God_the_Father
  7  heaven on-heaven land on-many angel
  8  on angel name exist Satan and two
  9  angel and Satan ~pray and ten-ten-ten-ten-year

## 120v — the fall of Lucifer, and the order left empty

> and forty thousand, and night, which Lucifer, to Lucifer, into the kingdom of heaven, unto the evil redeem; there is one order, the day from; and then this Lord went from the Father God, of the Lord; from this the Lord would [the tenth] begin the order of angels; and from the leaving of the Lord until the day of judgment the Lord would, of the Lord, from the Father God, [the tenth] from the order, in the place [shall stand empty] there is the Lord; the Lord bowed down from the Father God, of the Lord, into the kingdom of heaven, unto the evil; then went the Lord, the Father God, the Son, God, Jesus, the Holy Spirit, Mary, Christ, the apostles, the angels judge living, and dying redeem [shall fill it]

  1  and ten-ten-ten-ten and night which-Satan to-Satan
  2  on-heaven land on-~evil redeem* SUBJ one
  3  order ~year-chapter from* and then-exist this-Lord go-Lord from-God_the_Father
  4  of-Lord from this-Lord want-Lord [the_tenth] ~begin order angel and from
  5  to-leave of-Lord ~until judge-year want-Lord of-Lord | from
  6  God_the_Father [the_tenth] from order on-place [shall_stand_empty] SUBJ | exist
  7  Lord bow-Lord from-God_the_Father of-Lord on-heaven land
  8  on-~evil then-exist | go-Lord-God_the_Father-son-God-Jézus-holy-spirit
  9  Mary-Christ-apostle-angel judge living and die redeem* [shall_fill_it]

## 121r — the tenth order, and the drachma that was lost

> This Lord is […] of the Lord, of the Father God, upon the sheep, the righteous people; and believe in the Lord, and in his Father God, many judge, and the neighbours, and the friends, the angels, and the apostles, for ever and ever, amen. And then the Lord Jesus, this […] […] baptized: this is his creature; you, the mother; she, from her, is she; she lost one drachma, one order, the order within the kingdom of heaven; because then he bowed down from the Father God, heaven, upon many angels, upon heaven, the kingdom, unto the evil. And then the Lord Jesus said: there is

  1  exist this-Lord judge-Lord of-Lord from-God_the_Father on-sheep
  2  righteous people and believe inside divine_one^ and inside of-Lord from-God_the_Father many
  3  judge and neighbours and friend angel and apostle chapter-oh chapter-oh
  4  amen and_then Lord-Jézus this one-~woman this_is of-Lord
  5  create you mother it from it SUBJ | exist
  6  it loseth_one-+it one silver^ one
  7  order order inside heaven land because then
  8  bow from-God_the_Father heaven on-many angel on-heaven.
  9  land on-~evil and_then Lord-Jézus say exist

## 121v — the Trinity: Father, Son and Spirit, and one God

> from the Father God, to the Son, goeth the Holy Spirit; Father, Son, heart, man. And then from the Father God the Holy Spirit; how the man was shaped he would, the Father, the Son, the Spirit, the heart. And then the Son, in his image [after our] [likeness]: man is, all one, to the Father, the Son, the Spirit. Father, Son and Spirit took man, and every living thing [creature]; the soul heard; Adam saw rightly; not many from the Father, from the Son; not many the Holy Spirit; in turn this Lord is all one God. And then the Lord Jesus went forth, Father, Son and Spirit, out, into the kingdom of heaven, into this world.

  1  from-God_the_Father to-son go holy-spirit father son heart man^
  2  and_then from-God_the_Father holy-spirit on-how? man^ image^
  3  would_like^ father son spirit heart and_then son | on-of
  4  image^ [after_our] [likeness] exist man^ every one | to
  5  father son spirit grab father son spirit man^
  6  every cattle^ [creature] soul hear man^ see righteous not
  7  many from-father from son not many holy-spirit but
  8  this Lord every one God and_then Lord-Jézus go_out-Lord
  9  father son spirit out on-heaven land on-this world*

## 122r — the Lord God forms Adam and breathes into him

> And out of Paradise the Lord God, Adam, the heart slime (of the earth) And then Adam was, the heart, as was said before [breathed] and became to one soul, the heart, breathed upon Adam; and he became living. And the Lord took Adam, the Father, the Son, the Spirit; and Adam went, the Lord, the Father, the Son, the Spirit, into Paradise; and every heart is Adam's, the heart, the Lord, the Father, the Son, the Spirit. And then the Lord Jesus said, from the Father, of the Lord God, heaven, Adam […] this Adam took all rightly [nor] hunger and thirst [nor] this Adam;

  1  and out Paradise Lord_God man^ heart slime_(of_the_earth)*
  2  and then-exist man^ exist heart aforesaid [breathed] and
  3  became* to-soul-+one heart breathe on-Adam and
  4  living leave and man^ take^ Lord-father son.
  5  spirit and man^ go Lord-father son spirit
  6  inside Paradise and every heart exist-to man^
  7  heart Lord-father son spirit and_then Lord-Jézus say from-father
  8  of-Lord God heaven man^ name-[?] this-Adam
  9  take^ every righteous [nor] hunger and thirsty [nor] this-Adam

## 122v — the commandment, the sleep, and the rib

> and one living thing dieth; there shall be sin, hunger, thirst, to him who. [afterward] the Lord took, this Adam, all rightly one: the law, this yoke, this Adam, by commandment: do not eat of this tree, evil, sin, thou shalt die. Likewise Adam did eat, in that place, and died. And then Adam slept, into Paradise; and then the throne, first, from the saying; and then went the Holy Spirit into Paradise. And then this, this the garden; and the Lord God took from Adam a rib; and she, the heart, and then the Lord Jesus: thou, mother. And then Adam

  1  and one living-die-sin have hunger thirsty to-to-this-who.
  2  [afterward] grab Lord this Adam every righteous one
  3  law this yoke this Adam command = do_not eat
  4  this to-~son evil-~sin thou_shalt_die* ~if Adam exist eat
  5  on-place die and then-exist Adam sleep inside into_Paradise
  6  and then-exist table first from saying and then-exist go holy-spirit
  7  inside Paradise and_then this SUBJ this the_garden and
  8  grab Lord_God Adam rib and it heart
  9  and_then Lord-Jézus you mother and then-exist Adam

## 123r — bone of my bones, and the serpent

> laughed; and then this: bone of my bones. In turn, the two souls, one […] by name. And then the Lord Jesus left, the Lord, the Father God, the Son, the Spirit, into the kingdom of heaven; and there went she into the Garden of Eden; and then Eve, Eve went to this tree which stood in the midst; it is the Lord God's, by the law; and she saw a serpent. And then this serpent: she, eat of this fruit. And then she: ye shall not eat, because she, Adam, answered by the commandment. And then this serpent: Eve, eat; she, Adam.

  1  from laugh and_then this bone bones in_turn two soul
  2  one ~brother-+name and_then Lord-Jézus leave Lord-God_the_Father
  3  son spirit on-heaven land and go
  4  it on-Eden and then-exist Eve
  5  Eve go to this tree what stood_in_the_midst*
  6  exist Lord_God through law and see one serpent and_then this serpent it
  7  eat this fruit and_then it shall_not_eat eat
  8  because it Adam answered command = and_then
  9  this serpent Eve eat it Adam

## 123v — she took of the fruit, and their eyes were opened

> this; in turn the fruit, it is; she, one, Adam did eat. Eve is, Adam; they knew evil and good, how to the Lord God it is known. And then she plucked, the serpent, this [beguiled], this serpent; and then she took, in turn she, the fruit, and gave to Adam; and then were opened, in that place, Adam, naked; she saw, Adam; and then she, Adam, was ashamed. And then the Lord Jesus: and this, unto death, the sin, to hide, they did; Lucifer, the Lord, the Father, the Son, the Spirit, of the Lord, the man, from the Father God,

  1  this in_turn fruit SUBJ exist it one Adam eat
  2  exist Eve Adam know evil and good | how?
  3  to Lord-God know and then-exist pluck serpent this
  4  [beguiled] this serpent and then-exist grab it
  5  in_turn it fruit grab Adam and then-exist
  6  were_opened* on-place Adam naked see it
  7  Adam and then-exist it Adam be_ashamed
  8  and_then Lord-Jézus and this on-die ~sin-hide do
  9  Satan Lord-father son Spirit_of_God^ of-Lord somebody from-God_the_Father

## 124r — Adam, where art thou?

> the son, Lucifer, is bowed down, the Father God, into heaven; in turn the day is unto hell. And then the Lord Jesus left, the Lord, the Father, the Son, the Spirit, into heaven; in turn […] within the Garden of Eden. And then the Lord Jesus, this second throne, from the saying; and then left, the Lord, the Father, the Son, the Spirit; left into the kingdom of heaven, into Paradise; he said: there is […] of […]. The Spirit to Adam: Adam, where art thou? And then Adam, which Adam; the Lord God said, the Lord, the Father, the Son, the Spirit, by mouth: Adam, which, said Adam,

  1  who-+SUBJ Satan exist ~bow God_the_Father on-heaven | in_turn-chapter
  2  ~year-exist on-hell and_then Lord-Jézus leave Lord-father son
  3  Spirit_of_God^ on-heaven ~land inside Eden
  4  and_then Lord-Jézus this table two from saying and then-exist
  5  leave Lord-father son Spirit_of_God^ leave on-heaven land
  6  inside into_Paradise say exist [down] | of-[?].
  7  Spirit_of_God^ to-Adam Adam why? and_then
  8  Adam which Adam Lord_God say | Lord-father-son
  9  Spirit_of_God^ who-mouth Adam which say Adam

## 124v — the woman gave me, and the serpent beguiled me

> who, this Adam answered and said to the Lord, the Father, the Son, the Spirit: where? Adam answered and said: the woman, Eve, Adam, she gave me to eat. Said the Lord, the Father, the Son, the Spirit: Eve, heavenly, said; Eve, which Eve, to this Lord said. The Lord, the Father, the Son, the Spirit: where art thou? she, which, who. Who? She answered and said to the Lord, the Father, the Son, the Spirit: where? Eve answered and said: she, the serpent, she gave her food. Said the Lord Jesus: there is, of the Lord, from the Father God, to Adam: Adam, to one

  1  who this-Adam answered* say Lord-father-son-spirit
  2  why? Adam answered* say ~Adam Eve
  3  Adam gave_to_eat say Lord-father-son-spirit Eve
  4  heavenly say Eve which Eve this-Lord-to say
  5  Lord-father-son-spirit why? it which who.
  6  who it answered* say Lord-father-son-spirit
  7  why? Eve answered* say it serpent
  8  it food say Lord-Jézus say exist of-Lord
  9  from-God_the_Father to-Adam Adam to-one

## 125r — to till the ground, and the sorrow

> the law; this Adam is […]; the commandment he kept; it is Adam, to him who, upon Adam; in turn, chapter, who. gates Adam is, the earth, to till the ground; he would, to the son, food take; in turn Eve this; Eve is through pining, and this Eve is painful, the coming, he hath; in turn this evil is [cursed] the earth, the serpent slideth, and a room for evil; this man was made, all of this; the serpent

  1  law this-Adam exist name-[?]-ten commandment carry exist
  2  Adam to-to-this-who on-of-Adam in_turn chapter-~who.
  3  gates* exist Adam earth to_till_the_ground
  4  want to-~son eat^ take^ in_turn Eve this
  5  Eve exist through pine and this Eve
  6  exist painful ~be_born have in_turn this evil
  7  exist [cursed] earth slide and
  8  room evil this man^ create every this serpent

## 125v — driven out, and the flaming sword

> dieth; and he departed from among Adam and Eve the Lord, the Father, the Son, God, the Spirit, from the Father God, Jesus, the angel, the Virgin Mary, Christ, and the apostles, and the Jews, and the man baptized, and all. [he drove out] and all the kingdom of heaven, the Lord, and the Lord's heart, all the earth, and the evil, and the kingdom of heaven; and there went the Lord God, the angel, the second, the earth, and […] fire, the sword, and | the earth; Adam slid out; from the Garden of Eden he was cast out.

  1  die and become^ among Adam_and_Eve
  2  of-Lord father son God spirit from-father God Jézus angel
  3  virgin-Mary Christ and apostle and Jew and man^ ~baptize and every.
  4  [he_drove_out] and every heaven land Lord and Lord-+heart
  5  every earth and ~evil and heaven land
  6  and go Lord_God angel two earth and.
  7  Eve flame^ sword and | ~earth
  8  slide out on-inside Eden exorcise

## 126r — the cherub at the gate, and the third saying

> And he set the angel with the sword at the gate, the cherub of the Garden of Eden; and one creature [cherubim] within the Garden of Eden; in turn, the angel. And then the Lord Jesus, this third throne, from the saying, said the Lord Jesus: this is this drachma; and it is lost, then, from the evil, the sin: they did eat, the two, Adam; and Eve and Adam slid out; cast out, the Lord, the Father, the Son, the Holy Spirit; and then hell, the evil; from […] the serpent took, from the good, one commandment of God; which chapter […] the serpent hath.

  1  and place^ angel sword on-gate cherub*
  2  Eden and one create can_be inside
  3  Eden but angel and_then Lord-Jézus
  4  this table three from saying say Lord-Jézus this SUBJ this
  5  silver^ and exist lose then from evil-~sin eat two
  6  ~Adam and Eve and ~Adam slide out
  7  exorcise Lord-father son holy-spirit and then-exist hell
  8  evil from [?]-slide take^ from good
  9  one commandment God which-chapter [?]-slide have

## 126v — the Lord seeks the drachma he lost

> The Lord, the Father, the Son, the Spirit, took what was lost; | the two, Adam, the serpent. Said the Lord Jesus: then therefore the two could find it. All, until this | redemption; therefore have mercy on the angel of the Lord, from the Father God; he could […] find, redemption, therefore. He was born of a mother, the Lord's love, and redemption; this Lord, of a mother [again] was born; and redemption, this Lord, the cross [thereon]; in turn […] […] the cross; from there he would find this drachma, this eternal kingdom […] there is, from […] the serpent; abandon Lucifer. And said the Lord Jesus: this Lord would take the trespass, and redeem, of the Lord, from the Father God, heaven.

  1  Lord-father son spirit exist grab lose | two-~Adam
  2  slide say Lord-Jézus then-~exist two can find.
  3  every ~until this | redemption ~exist have_mercy on-angel of-Lord
  4  from-God_the_Father can ~woman find redemption ~exist
  5  exist be_born mother of-Lord love and redemption this-Lord from mother
  6  [again] be_born and redemption this-Lord on_the_cross [thereon] in_turn
  7  [?]-[?] on_the_cross from want find this silver^ this heaven*
  8  land [?]-+SUBJ exist from [?]-slide
  9  abandon Satan and say Lord-Jézus this-Lord want-Lord
 10  trespass grab and ~redeem-Lord of-Lord from-God_the_Father heaven

## 127r — Hezekiah is told he shall die, and is given more years

> He said, in sleep, the angel of God, to holy Hezekiah the prophet; Hezekiah, the Lord God, this is, saith the Lord: within three days, this | one shall die. And then from laughter, holy Hezekiah began, Hezekiah, to be sad, holy Hezekiah, and cried out: who shall make ready? There went to Hezekiah […] and a second time said the angel of God: Hezekiah, the Lord God, this is, saith: I have had mercy on thee; it is until […] years thou shalt live; and mercy.

  1  say inside sleep God angel
  2  holy-Hezekiah
  3  prophet Hezekiah
  4  Lord_God this_is say-Lord
  5  until three_days | this
  6  SUBJ die and then-exist
  7  from laugh holy-Hezekiah
  8  beginning^ Hezekiah sad
  9  holy-Hezekiah and cry_out who-exist prepare-chapter-to-and
 10  go to-of-Hezekiah heart-Lord and the_rest^ say God angel
 11  Hezekiah Lord_God this_is say prolong_life-chapter-to-and exist
 12  until five-fourteen-?years living-chapter-to-and and prolong_life

## 127v — Hezekiah dies, and Paul sets his house in order

> Made ready, holy Hezekiah; and upon […] Hezekiah's soul breathed out; and then of Hezekiah the soul breathed out; then appeared the angel of God, and said to the servants: of Hezekiah, lay him. This is for ever, in the sepulchre; in turn the soul of Hezekiah, | this the angel would take; and the angel left, in turn, holy Hezekiah for ever in the sepulchre laid. The servants speak; holy Paul apostolic letter [writeth] the brethren of Paul […] and Paul made ready, of Paul, in his last year.

  1  prepare holy-Hezekiah and on-[?]
  2  of-Hezekiah soul give_out^ and then-exist-chapter-to-and
  3  of_Hezekiah soul give_out^ time appear.
  4  God angel and say servant of_Hezekiah put.
  5  this exist-exist-chapter inside tomb in_turn soul Hezekiah | this
  6  angel want-angel give^ and leave angel
  7  in_turn holy_Hezekiah exist-exist-chapter inside tomb put.
  8  servant speak holy-Paul apostolic_letter [writeth] brother of-Paul
  9  ~have-[?] and Paul prepare of-Paul last day^

## 128r — Paul's one only Son, and a new reading begins

> that he is, made ready, Hezekiah, holy Hezekiah the prophet; this [foretold] hath; and Paul, the man, made ready, he who, the Lord Jesus, the Son of God, of Paul, the man, the one only, who was; that man went, because he lost [the sheep] Begins this | holy gospel, written | by holy Luke, in the first chapter, in his writing. Then, when he was condemned, the Lord Christ, three days

  1  he_is* exist prepare-Hezekiah holy-Hezekiah
  2  prophet this [foretold] have and Paul-somebody prepare this-who
  3  Lord-Jézus son God of-Paul-somebody one only
  4  exist-exist go-this-somebody because lose [the_sheep]
  5  begins this | saint^
  6  gospel write | saint^
  7  Luke within^ one chapter within^
  8  of-write time
  9  then-exist on-?condemned
 10  Lord Christ three_days

## 128v — they were terrified, and believed not for joy

> another night; then appeared to his apostles, the gate. And then the Lord Jesus: the law, he is, [so] he is; and through, the apostles were startled, because the apostles believed that he is; how, for gladness? And then the Lord Jesus had the apostles; the Lord, this Lord, the apostles saw; within is for ever a man [a spirit] the angel, for ever; in turn, one, for gladness, could the apostles, the Lord, […] the Lord, who […] this Lord, to you, through be thirty days and three, and literally

  1  another* night time appear
  2  apostle of-Lord gate and_then Lord-Jézus law | ~you-chapter
  3  [so] exist and through startle apostle because
  4  believe apostle he_is* how? ghost and_then
  5  Lord-Jézus have-apostle Lord this-Lord see-apostle inside | exist
  6  exist-chapter somebody [a_spirit] angel exist-exist-chapter
  7  in_turn one ghost can apostle Lord
  8  because* Lord ~who-[?] this-Lord to-you
  9  through stay thirty day and three and literal

## 129r — receive ye the Holy Spirit, and go into all the world

> and the apostles could because the Lord Jesus, Christ, because therefore out, the Holy Spirit, mercy; and spake holy John: he breathed upon them, the apostles; and all the apostles received the Holy Spirit. And then the Lord Jesus to his apostles: go ye, apostles, into the world, and be ye his apostles; preach the gospel.

  1  and can apostle because* Lord-Jézus ~Christ-to because-~exist
  2  out holy-spirit have_mercy and speak holy-John | breathed
  3  upon_them on-apostle and every apostle grab holy-spirit
  4  and_then Lord-Jézus apostle of-Lord you go-apostle
  5  into_the_world* and exist-apostle of-Lord gospel preach
  6  and exist-apostle baptize inside of-Lord name
  7  and somebody exist Lord believe and exist
  8  baptize somebody inside name from-God_the_Father and son
  9  and holy-spirit everybody = be_saved if and somebody ~exist

## 129v — baptize them, and be brought before kings

> baptizing them in the name of the Father, and the Son, and the Holy Spirit. One man shall be saved; in turn, every man shall be damned. And said the Lord Jesus to his apostles: ye shall | go, said he, before kings, before emperors. | Therefore the apostles have, because this Lord is with you that therefore the apostles [teach] how shall they say? it is the apostles that speak. And then the Lord Jesus had these apostles from him; and a man, you, the apostles, for ever, to die rather, the apostles of the Lord God. Have, and the Lord, you, the apostles, the soul, and for ever

  1  baptize inside name from-God_the_Father and son and holy-spirit
  2  one man^ be_saved but everybody = be_damned and
  3  say Lord-Jézus teach^ of-Lord you exist | go
  4  say before king before emperor | ~exist
  5  teach^ have because this-Lord exist you that
  6  ~exist teach^ [teach] how? say exist speak-apostle and_then
  7  Lord-Jézus have this-apostle from and man^ you teach^
  8  exist-exist-chapter die rather somebody-apostle from Lord_God.
  9  have and-Lord you teach^ soul and exist-exist-chapter

## 130r — the apostles go out, and a new reading from John

> the dying of the Lord. And then the Lord Jesus: then went the apostles and preached, and began at Jerusalem; and the apostles preached in all the whole wide world. The end of this holy gospel; and the Lord Jesus departed from among the apostles. Begins this holy gospel, written by holy John, in the second chapter of his writing. Then said the Lord Jesus to his apostles, the Lord, at the last supper: this Lord goeth to his Father; he who, the Lord, goeth

  1  die-die-Lord and_then Lord-Jézus then go-apostle preach and
  2  ~begin from Jerusalem ~and preach teach^ on-every all_the_world world.*
  3  here_ends this holy_gospel and leave among teach^ Lord-Jézus
  4  begins this.
  5  holy-gospel write
  6  holy-John inside two chapter
  7  inside of-write time
  8  say Lord-Jézus teach^ | of
  9  Lord at_the_Last_Supper =.
 10  this-Lord go-Lord to-of-Lord from-God_the_Father he_who Lord go-Lord

## 130v — Thomas, and Philip: shew us the Father

> And then holy Thomas answered: goeth the Lord to his Father? Said | the Lord Jesus: Thomas, this Lord goeth to his Father, and the Lord goeth. And then | holy Philip answered: shew us, the apostles, thy Father. And then the Lord Jesus: Philip, the apostles, the Lord the apostles have seen; then this Lord did miracles, [works] miracles; one, the Lord; this Lord, to the Lord, the trespass did; but rather the Father, of the Lord, […] doeth them, the Lord's finger. And he began to rebuke the apostles for their unbelief. And then the | Lord Jesus: and a man, the Lord, the apostles have seen, these apostles, and of the Lord the Father have seen; and a man who believeth in the Lord, this is

  1  and_then holy-Thomas answered go-Lord to-of-Lord God_the_Father say | Lord
  2  Jézus Thomas this-Lord go-Lord to-of-Lord God_the_Father and SUBJ-Lord
  3  go-Lord and_then | holy-Philip answered shew apostle
  4  of-Lord from-God_the_Father and_then Lord-Jézus Philip SUBJ apostle
  5  Lord see-apostle then this-Lord miracle do [works] miracle
  6  one-Lord this-Lord to-Lord trespass do but_rather* God_the_Father
  7  of-Lord [?]-°down do of-Lord finger
  8  and apostle begin rebuke on-believe and_then | Lord
  9  Jézus and SUBJ man^ Lord see-apostle this-apostle SUBJ and of-Lord
 10  from-God_the_Father see and man^ exist Lord believe this exist

## 131r — the Sadducees and the resurrection

> and in the Lord's Father believe, because this is one God. And then the Lord Jesus: go ye, apostles, into land and land, among the Sadducees; and the Sadducees, preach ye, apostles, how this Lord from death stood up, and ate; how it is that the Sadducees, ye, apostles, believe, because God said, the mouth of the day, hear; and the Lord ye have seen, Sadducees. And then the Lord Jesus said: he is yours; how ye, apostles, are, the Sadducees, to believe: because the Sadducees, before you, the dead they bear, the Sadducees, to rise, resurrect; and this is

  1  and of-Lord from-God_the_Father believe because this one
  2  God and_then Lord-Jézus you go-apostle inside
  3  land land among the_Sadducees* and
  4  the_Sadducees* exist preach-apostle how? this-Lord from-die
  5  stand_up food how? exist from the_Sadducees* you
  6  apostle believe because God say mouth-~year hear and SUBJ
  7  Lord see the_Sadducees* and_then Lord-Jézus say-Lord | ~you
  8  yours how? you apostle exist the_Sadducees* | to
  9  believe* because-exist the_Sadducees* before you
 10  die carry-?the_Sadducees on-~stand_up resurrect and this | exist

## 131v — in my name, and he that believeth and is baptized

> the apostles say, these dead men offer; the apostles can, Jesus of Nazareth have; the dead again stand up, rise; in that place stand up, rise, the man, in his name. And then the Lord Jesus: and the man who believeth in the Lord, every such man shall be saved; and one man shall be damned. And then the Lord Jesus: and the man who therefore believeth the Lord, one man shall be saved; in turn every man shall be damned. And then the Lord Jesus: and the man who believeth the Lord, to be baptized with the second baptism, the Baptist's, in the name of the Father, and the Son, and the Holy Spirit: every such man shall be saved, and one man

  1  apostle say-apostle this-die-somebody offer apostle can Jézus Nazareth
  2  have die-somebody again* rise^ resurrect on-place rise^ resurrect
  3  somebody inside of-Lord name and_then Lord-Jézus and
  4  somebody exist Lord believe everybody = be_saved
  5  and one somebody be_damned and_then Lord-Jézus and
  6  somebody ~exist Lord believe one somebody
  7  be_saved but everybody = be_damned and_then Lord-Jézus
  8  and somebody exist Lord believe to exist | one-~woman
  9  the_Baptist/woman inside name from-God_the_Father and son and holy
 10  spirit everybody = be_saved and one somebody

## 132r — the signs that shall follow them that believe

> shall be damned. And then the Lord Jesus: and the man who believeth the Lord shall do many miracles, all in the Lord's name; | and there is […]; then the apostles saw him taken up into heaven, the kingdom, the light. And then the apostles answered: they saw, the apostles, the light, taken up into heaven; in turn […] said the Lord Jesus: lo, taken up; Lucifer could. And then the Lord Jesus: go ye, apostles, into the world; be ye apostles to the ass; heal ye, apostles; be ye apostles; the evil | upon the people cast ye out, apostles; the blind eyes, through light, apostles; the dead shall stand up, rise, apostles: all in the Lord's name.

  1  be_damned and_then Lord-Jézus and somebody exist Lord believe
  2  exist many miracle do every inside of-Lord | and
  3  exist-[?] time see apostle bow on-heaven
  4  land light and_then apostle answered see
  5  apostle light bow on-heaven ~land say
  6  Lord-Jézus lo bow can Satan and_then
  7  Lord-Jézus you-apostle go into_the_world* exist-apostle
  8  to-from-donkey heal-apostle exist-apostle evil | on
  9  people ~exorcise-apostle eye-blind through light-apostle
 10  die-somebody stand_up resurrect-apostle every inside of-Lord name

## 132v — the end of the reading, and the angel comes to Elijah

> and as the man, from the ass, go ye, apostles, all, from healing, apostles, in the Lord's name. The end of this holy gospel. Then appeared the angel of God to holy Elijah the prophet. Then

  1  and ~on-how? chapter-somebody | from-donkey go-apostle every chapter | from
  2  healing-apostle inside of-Lord name here_ends this holy_gospel
  3  time then-exist appear God angel
  4  holy-+Elijah prophet time then-exist

## 133r — Elijah's forty days, and the angel at Horeb

> From Adam […] until this […] five hundred years and thirty-six years. Then appeared the angel of God to holy Elijah the prophet. And then the angel of God: Elijah, the Lord God, this is, saith the Lord: it is this year, forty days go, Elijah, afar […]; and from […] by name it is Horeb. And then went Elijah upon this mount Horeb; and then Elijah lay down, to one tree; and a second time said the angel of God: Elijah, take, and Elijah found, and Elijah did eat, and Elijah was strengthened; and Elijah went [forty days], Elijah, upon this mount Horeb, the love of the Lord God.

  1  from ~Adam heart-Lord until this [thousand] | five_hundred
  2  day^ and thirty six-year time appear God
  3  angel holy-+Elijah prophet and_then God angel
  4  Elijah Lord_God this_is say-Lord exist this-year
  5  forty go-+Elijah on-far mount and ~body
  6  exist Horeb and then-exist go Elijah on-this mount
  7  Horeb and then-exist from Elijah lie | to
  8  one tree and second^ say God angel Elijah take^
  9  find-+Elijah eat-+Elijah exist-+Elijah strengthen
 10  and go-+Elijah [forty_days] Elijah on-this mount Horeb love Lord_God

## 133v — the cake and the cruse, and Elijah taken up

> This is this mount, the love of the Lord God most high, of every creature. And then went Elijah upon this mount Horeb, and before he went, in that place [under a juniper] lay down holy Elijah the prophet; and Elijah found one cake, and one cup of water; and he did eat, and drank, and was strengthened, upon this mount [of God] Elijah. And from that year, forty years; and these forty years, then, then he took Elijah, the two, Noah [wished to die] [a cake] and Elijah and Noah were caught up into heaven on high; and from Elijah man is Noah, Elijah, the sword shall bear; the evil […] and [Enoch] shall leave Noah and Elijah on the earth,

  1  this_is this mount love Lord_God highest every create and then-exist go Elijah
  2  on-this mount Horeb and before go from on-place [under_a_juniper]
  3  lie holy-+Elijah prophet exist find-+Elijah
  4  one a_cake and one cup water and
  5  eat and drink and strengthen on-this mount [of_God] Elijah
  6  and from this-year forty and this forty then-exist
  7  time grab to-+Elijah-two-?Noah [wished_to_die] [a_cake]
  8  and Elijah-?Noah be_caught_up heaven high and from
  9  Elijah man* exist ~Noah Elijah sword
 10  carry ~evil one-+gate/open and [Enoch] leave-to-leave Noah Elijah on-earth

## 134r — Antichrist, and a new reading: the king who took account

> [Antichrist] [of a harlot] through birth, the two, the chief evil, the evil one, and the son of the devil, by name evil; it is | Anti- christ. Before the gospel, said the Lord Jesus, leaving: a king, a man, from the king; hear all […] | of the kingdom. Begins this holy gospel, written by holy Matthew, in the […] chapter of his writing. Then said the Lord Jesus to his apostles and the Jewish people: there is, among the Lord God, the day of judgment, one king; all priest heavenly, the Lord, the man, before the Lord God the king; and then he had one heavenly

  1  [Antichrist] [of_a_harlot] through be_born two chief_devil = and
  2  son Satan name evil exist | Anti-
  3  baptize before gospel say
  4  Lord-Jézus leave-to-leave
  5  king somebody ~king
  6  hear every priest | of
  7  ~king kingdom^ begins
  8  this holy-gospel write
  9  holy-Matthew inside [eighteen] chapter of-write time say Lord-Jézus
 10  apostle of-Lord and Jew people exist among Lord_God judge-~year
 11  one king every priest heaven^ Lord somebody before
 12  Lord_God-king and then-exist have one heaven^

## 134v — ten thousand talents, and the servant sold

> a servant; and the lord's servant owed ten thousand talents; and there went this Lord God the king, this heavenly servant; and then the servant, the angel, went before this | Lord God the king, before the Lord Christ; and the servant began to believe, this […] whosoever, the king, of the Lord | […] to do good. And then the Lord God the king, | the law, love, mercy, righteousness, good deeds […] took. And then this Lord God the king sold the servant, the angel, to be lost, | of the man, his son, the sin; and the people, to the holy; and the man knelt down, this man, this heavenly servant, before this | Lord God

  1  somebody-servant and Lord servant exist debt^ ten_thousand talent
  2  and go this Lord_God-king this heaven^ servant and
  3  then-exist somebody-servant-angel go-angel before this | Lord_God
  4  king before Lord Christ and somebody-servant begin
  5  believe this [?]-~somebody-+king of-Lord | [forgave_the_debt]
  6  good-do and then-exist Lord_God-king | law-love-have_mercy
  7  righteous-good-do not-to-°high take^ and_then
  8  this Lord_God-king sold angel-somebody to_be_lost | of
  9  somebody ~son sin and people* ~rich-to and kneel-somebody
 10  this somebody this heaven^ servant before this | Lord_God

## 135r — the Unmerciful Servant

> A king, and the Lord God begins […] [fellowservant] [a hundred pence] […] […] […] would a man, the Lord God […] forgive the debt. And behold, the Lord God the king besought The servant of the Lord God the king humbled himself — the man-servant — and the man had mercy, the Lord God the king; and the man forgave all […] of the man's sin. And the man went […] to his home. And then, as the man went on, the fellow-servant of his household — and then he met one | God the man, this man, the fellow-servant; and the man was in debt hundred pence; and the man of God began to demand it.

  1  king and Lord_God begin ~pray [fellowservant] [a_hundred_pence]
  2  have law to somebody-~sin would_like^ somebody this Lord_God have_compassion
  3  remit debt^ ~and see this Lord_God-king besought*
  4  ~humble this servant of-Lord_God-king somebody-servant and
  5  somebody forgive^ this Lord_God-king and somebody forgive^ every ~exist-+one
  6  of-somebody sin and somebody go-angel of-somebody
  7  home and then-exist go_on-somebody this heavenly servant
  8  of-somebody home and then-exist come^ one | God
  9  somebody this somebody heavenly servant and somebody exist
 10  debt^ hundred* denarius and God-somebody begin ask

## 135v — the fellowservant cast into prison

> of the debt; and rather love he took; in turn he knelt down, the man of God, before this heavenly servant; and the servant began, as before […] […] to have the law, | to the man of God; the man of God would, this man, the heavenly servant, have compassion forgive the debt; and the man of God release in turn the man of God took him into prison; and the man of God, until, from […] he bowed the head upon the scaffold; and this saw, sadly, the second servant; this Lord God the king, the angel, had mercy, the one only Lord God; and the angel went, sorrowing, the angel, this this Lord God the king; and the Lord God the king said to the angel

  1  of-indebted and rather-love take^ but kneel God-somebody
  2  before this heavenly servant and somebody-servant
  3  begin ~pray [fellowservant] [a_hundred_pence] have law | to
  4  God-somebody want-God-somebody this somebody heavenly servant
  5  have_compassion remit debt^ and God-somebody release*
  6  but God-somebody take^ inside prison^ and God-somebody
  7  until-from bowed head inside scaffold and
  8  see this sad two servant this Lord_God-king angel forgive^
  9  one only Lord_God and go-angel sad-angel-this
 10  this Lord_God-king and Lord_God-king say angel

## 136r — the parable told a second time

> the Father of heaven, he who is king of all heaven and earth, and king of all on earth; and then of his mercy the servant believes in the Lord God, the one only Lord God [besought] This Lord God had mercy. The Lord: ten thousand talents appeared. One man of God; and whosoever was in debt a hundred denarii; and the man of God began to ask | for the debt, and rather with love he took him; in turn he knelt down, the man of God, before this heavenly servant; and the servant began, as before, [fellowservant] [a hundred pence] to have the law upon the man of God.

  1  from-father heaven he_who king every heaven land
  2  and on-earth every king and_then from forgive^ ~servant
  3  believe of-Lord_God one only Lord_God [besought]
  4  this Lord_God forgive^ Lord ten-?thousand talent appear.
  5  one God-somebody and whosoever* exist debt^ hundred*
  6  denarius and God-somebody begin ask | of
  7  debt^ and rather-love take^
  8  but kneel-God-somebody before this
  9  heavenly servant and somebody-servant begin ~pray
 10  [fellowservant] [a_hundred_pence] have law to God-somebody

## 136v — he would not forgive, and the king was wroth

> The man of God would not, this heavenly servant, have compassion, forgive the debt, and release the man; in turn the man of God took him into prison; and the man of God, from house to house, bowed his head upon the scaffold. This king, the Lord Christ, grew angry, and went upon this heavenly servant; and the servant went to die, before the angel, before this king, before the Lord Christ, the one only Lord God. And then this king, on this servant had mercy | of the Lord, the Father God; that servant hid himself; how the Lord [came] to him; and the king — that servant: "Lord have mercy, Lord have mercy" — that servant.

  1  want-God-somebody this heavenly servant have_compassion
  2  forgive^ debt^ and God somebody release*
  3  but God-somebody grab inside prison^ and God-somebody
  4  to-house-from bowed ~head inside scaffold
  5  grow_angry this king Lord Christ and go on-this
  6  heavenly servant and servant go die angel before
  7  this king before Lord Christ one only
  8  Lord_God and_then this king this servant forgive^ | of
  9  Lord from-father God to-hide that_servant ~how? Lord to and
 10  king that_servant have_mercy-Lord have_mercy-Lord that_servant

## 137r — the end of the reading

> Ten thousand talents. In turn this man, from the man of God [forgave thee] had mercy: a hundred denarii. And the man took this king, the Lord Christ; and then took of the Lord the king the evil out, the evil of hell; and then this king, the Lord Christ, all of it, until this: that the man suffer [shouldst not thou] [had compassion] [even as I] likewise the king: the debt of the sin of the man. And then this king remitted all of the man; and the man therefore had mercy. Here ends this holy gospel.

  1  ten_thousand talent in_turn this-somebody from God-somebody [forgave_thee]
  2  forgive^ hundred* denarius ~and somebody grab this
  3  king Lord Christ and then-exist grab of-Lord-king
  4  evil exorcise devil = and_then this king
  5  Lord Christ every until-from this that somebody suffering
  6  [shouldst_not_thou] [had_compassion] [even_as_I] ~if king debt^ sin
  7  somebody and_then this king this exist every forgive^
  8  somebody and somebody ~exist forgive^ here_ends this holy_gospel

## 137v — a prayer to the Virgin, with the author's colophon

> Hail, O Virgin. Through holy Mary, mother of God, gate into Paradise Queen Mary, […] Lady […] […] | thou Mary, the one and only virgin maiden — thou, Mary, didst conceive Jesus without [sin]. Born of Mary […]; and from the Lord the Redeemer, in the Lord | I, [author], we do not doubt, [author]; we […] | I, [author], we pray to thee, Mary, […] | of [author], that when there is […], our soul may be forgiven | of [author], we […]. End of chapter. Amen. This prayer must be [said]. […] have mercy. Hail Mary. […] have mercy […] | Lord

  1  healing-girl through holy-Mary mother God gate into_Paradise
  2  king-Mary heaven wife world* ascend-Mary | this
  3  Mary one only virgin-girl this-Mary ~conceive Jézus without sin
  4  be_born-Mary Lord-+heart and from Lord-redeemer inside Lord | this-NAME.author
  5  somebody doubt_not-NAME.author-somebody believe | this-NAME.author
  6  somebody this-Mary pray to-~sin | of-NAME.author
  7  somebody then-exist ascend soul remit | of-NAME.author
  8  somebody exist-exist-chapter amen this pray have
  9  hundred-year have_mercy healing Mary name-high have_mercy ~out-Mary | Lord

## 138r — the Hail Mary, twice

> … God: this Mary of God. Blessed Mary, this Mary among women; blessed is the son of Mary, he who went to the Lord | from above, of Mary. Here ends the chapter. Jesus Christ. Amen. Hail, maiden, holy Mary, who took hold of the virgin girl. (An earlier printing read the first sign as the healing of a girl; it is Király and Tokai's *Hail*, as at 137v:1.) N. believes, this N., that this Mary is; N. through the mercy of the virgin girl; and N. is [blessed art thou] […] this […] and in every saying, and | redeem Mary; N., on the day of wrath of Mary, through the day of wrath, through — O son of Mary, Lord of N. — Jesus Christ.

  1  DIV this-Mary-DIV blessed-Mary this-Mary ~among
  2  the_poor_man/woman* blessed-+SUBJ of-Mary son he_who go-Lord | from
  3  up of-Mary exist-exist-chapter Jézus Christ amen
  4  healing-girl through holy-Mary from grab-virgin-girl
  5  believe this-NAME.author-somebody this-Mary exist NAME.author-somebody
  6  through have_mercy-virgin-girl and exist NAME.author-somebody [blessed_art_thou]
  7  [among_women] this °sick-+name-Mary and inside every saying and | redeem
  8  Mary NAME.author-somebody grow_angry-~year of-Mary through grow_angry-~year
  9  through oh son of-Mary Lord of-somebody Jézus Christ

## 138v — Saint Augustine and the three Hail Marys

> Amen. This prayer has from [three] mercy. So speaks the holy church father of the happy virgin Mary […] above: this Mary is; believe Mary; from Mary the son, from the Lord Jesus Christ. Everyone who would take hold, says holy Augustine the church father. Saint Augustine prays this: three prayers to the happy virgin Mary, to her pleasure and to her thanks. There is — Saint Augustine — the man who must be lost, O chapter, O chapter; and upon the cloud destroyed; and by three prayers many sins of a man are taken away, the sins of a man, in […]

  1  amen this pray have from [three] have_mercy
  2  speak holy-NAME.father church_father from happy virgin-Mary who up
  3  exist this-Mary exist ~ask-Mary from of-Mary
  4  son from Lord-Jézus-Christ every want grab speak
  5  holy-Augustine-church_father pray-+Saint_Augustine this
  6  three pray happy virgin-Mary on-pleasing on-thanks
  7  ~exist-+Saint_Augustine-somebody have lose chapter-oh
  8  chapter-oh and on-+cloud destroy and on-+three pray
  9  from many somebody-sin go-somebody-sin inside ~heaven

## 139r — Mary shows her breast

> the earth. Because whoever prays to the happy virgin Mary, every man is saved and goes not into the fire of hell; because [whoever prays to] the happy virgin Mary every day, kneeling to Mary, there is of Mary | the son; she shows, of Mary, the breast, this breast, this of Mary, that nursed the Lord God — believe — "the lost and damned man: have mercy, Christ" | "the man lost and damned." And whoever prays to the mother of Christ, every man is saved, and not one is damned; in turn every man is saved, because a good servant, every [faithful] servant

  1  land because and somebody pray happy virgin-Mary
  2  everybody = be_saved not-go on-hell fire because
  3  happy virgin-Mary every day kneel-Mary exist-to
  4  of-Mary | son show of-Mary
  5  breast this breast this-Mary this-Lord_God nurse believe
  6  the_man-+lost_and_damned have_mercy Christ | the_man*
  7  lost_and_damned and somebody pray mother Christ every
  8  somebody be_saved and one be_damned but everybody =
  9  be_saved because good servant every [faithful] servant

## 139v — the curse and the blessing

> So speaks holy Moses to Aaron; of Moses it is: this people, the man, is cursed from every good. That is, therefore the man is saved; in turn, whoever is merciful, righteous, to the poor of God, and to his brother as to himself, to his own. There is heaven and earth; in turn, whoever is merciful, righteous to the poor of God, and to his brother: this man the Lord God would. Cursed from every good; and all he has, that is, all his riches who [cursed] what the man has is damned, and the rich man cursed. This

  1  speak holy-Moses Aaron of-Moses exist-exist
  2  exist this people man^ exist through cursed from every
  3  good that_is ~exist be_saved-somebody in_turn and man^ exist
  4  have_mercy-somebody righteous-somebody poor_man_of_God = and to of-somebody
  5  from-father son how?-to man^ himself of-somebody.
  6  exist heaven land in_turn and man^ exist
  7  find_mercy^ righteous-somebody to poor_man_of_God = and to of-somebody
  8  from-father son this man^ want Lord_God cursed from
  9  every good be_saved and every have that_is every ~rich who
 10  [cursed] have-somebody be_damned-somebody and ~rich cursed this

## 140r — cursed be thy herd and thy field

> the man. Of the Lord the herd, cursed; of the Lord the field; then the man's harvest, the field, cursed; of the Lord, his […] then the man's grape, harvest, […] cursed, this man of the Lord, within his house. There is this man [barn] [stores] damned, O chapter, O chapter; into hell the man falls; in turn, whoever is | merciful, righteous, the man, to the poor of God, this, to his brother as to himself, this man. Blessed of the Lord the herd; blessed of the Lord the field; then the man's field, harvest, blessed;

  1  somebody Lord_God of herd cursed Lord_God of field
  2  then-this-somebody harvest field cursed Lord_God of-somebody
  3  mount then-this-somebody grape harvest mount.
  4  cursed this-somebody Lord_God inside of-somebody home
  5  exist this-somebody [barn] [stores] be_damned-somebody chapter-oh
  6  chapter-oh inside hell somebody fall in_turn and somebody exist | have_mercy
  7  somebody righteous somebody to poor_man_of_God = this of-somebody
  8  from-father son how?-to somebody himself this-somebody.
  9  blessed Lord_God of herd blessed Lord_God of
 10  field then-this-somebody field harvest blessed

## 140v — write it, and pray to the virgin Mary

> of the Lord the mount; then the man's mount, grape. Harvest blessed, this man of the Lord, and within his | house in turn home and in every place [wide] the man is left, the man is saved, there is. O chapter, O chapter, amen. It is written, it is said: all the wide world, to the pleasure of the Father God, and the Son of the Father God. Pray to the virgin Mary, believe; to all who would, the Lord the Father God hears; all the wide people the Lord would, to his will do; and the Lord: whoever is righteous, believe, the man. This the apostles all wrote, because every man's sin goes to the virgin Mary for mercy. Believe, man.

  1  Lord_God of mount then-this-somebody mount grape.
  2  harvest blessed this-somebody Lord_God and inside of-somebody | ~home-in_turn
  3  home* and every to-place [wide] leave-somebody be_saved-somebody
  4  exist chapter-oh chapter-oh amen write speak
  5  every wide world pleasing from-God_the_Father in_turn son of-God_the_Father.
  6  pray from virgin-Mary believe to every want Lord
  7  from-God_the_Father hear every wide people* want Lord to-+will
  8  do and Lord somebody exist righteous believe
  9  somebody this SUBJ apostle every write because everybody = sin
 10  go-somebody to virgin-Mary have_mercy believe somebody.

## 141r — the fruit of Mary

> Because of this, pray to Mary: the fruit of Mary, the son, to all the wide world; because the Lord Christ made the law among men, among the Father God's, of the Lord, because they are many. Have mercy, Lord Christ, on every man's sin, speaks the holy church father; then this man is, from many a man's sin, [narrow] left, the man, of the man, the heart of the Lord, because this is the creature of the Lord: the sin, the mercy [fruit]; this is within the man's law, that is; and the man must carry the law of God, | as the scribes say, [bear] the sin; the man is saved through many sufferings.

  1  because this from Mary pray of-Mary fruit son
  2  to-every wide world* because Lord Christ law do among
  3  somebody among from-God_the_Father of-Lord because SUBJ many.
  4  have_mercy Lord Christ to-every somebody sin speak holy-NAME.father
  5  church_father then-exist this somebody exist from many somebody sin
  6  [narrow] leave-somebody of-somebody Lord-+heart because this_is.
  7  [...] Lord sin have_mercy [fruit] this exist inside law somebody
  8  that_is and have somebody carry law God | [...]
  9  [bear] sin somebody be_saved-somebody to-many suffering

## 141v — a woman in Rome

> O chapter, O chapter, amen. It is written by the name | of the man; in heaven and earth, until he dies; in turn upon death. Here ends the chapter. And the soul. O chapter, O chapter, amen. There was in Rome a woman, the head, and then, it is believed, the woman in Rome father every day two: God. Here ends the chapter. She took, and fasted […] […]; she fasted to […], the woman, many years; and the woman would give thanks; this [Lady] fasted one [received]; and the woman took this holy host, and then

  1  chapter-oh chapter-oh amen write SUBJ name | of
  2  somebody inside heaven land until die in_turn | on
  3  die exist-exist-chapter and soul chapter-oh chapter-oh amen
  4  exist inside Rome one
  5  woman the_Baptist/woman head and
  6  then-exist ~ask-+woman
  7  inside Rome [father]
  8  every day two God exist-exist-chapter
  9  grab and fast half* [forty_days] SUBJ fast ~baptize the_Baptist/woman
 10  many year and woman want thanks this [Lady] fast one
 11  [received] and woman grab this holy-host and then-exist

## 142r — the woman who lived on the host

> The woman took, and cried out; the woman was lost and died; and then she carried the host; and then the woman host was; she took it to the place; hungering, she left [nothing] this day's food. The woman ate many years [was fed]; the woman understood Christ in the high heavens, the Holy Spirit, spirit to spirit, from the woman; living […] […] there were two; the woman's head, in Rome; and then the woman, through sin, the woman went out; of the woman the Lord, who was a thief, did; and then the woman cast out; the Lord, upon the Lord, had mercy; and one sister went; and then, O, of

  1  woman grab and shout-to lose die-+woman the_Baptist/woman
  2  and then-exist carry host and then-exist woman the_Baptist/woman host exist
  3  grab on-place hunger? leave [nothing] exist-today’s
  4  eat woman the_Baptist/woman many year [was_fed] SUBJ woman the_Baptist/woman understand
  5  Christ on-heaven high holy-spirit to-spirit from woman
  6  living-[?] half* exist two woman the_Baptist/woman head inside Rome
  7  and then-exist woman the_Baptist/woman commit sin woman the_Baptist/woman out
  8  of-+woman the_Baptist/woman Lord thief-who do and then-exist
  9  woman the_Baptist/woman exorcise Lord on-of-Lord have_mercy and
 10  go one sister and_then oh | of

## 142v — the woman fasts and takes the host

> The woman: the father, to him in turn, who — this, to the wife — could do, how this woman could. The woman went into mercy, the woman; of the woman the Lord; and then would say this chapter, sister: to fast, the woman [prayed]; and God. Here ends the chapter. She carried the woman, within the woman's mouth; and the Lord is God. Here ends the chapter. She kissed the woman; the Lord would, this woman; mercy there is; and then the woman, the woman, to fast, and took God. Here ends the chapter. And she carried the woman, within the woman's

  1  woman the_Baptist/woman from-father to-to in_turn-who this to-to-wife can do
  2  how? this-+woman can woman the_Baptist/woman inside have_mercy go woman
  3  of-+woman the_Baptist/woman Lord and_then want say this chapter-+sister
  4  to-fast woman [prayed] and God exist-exist-chapter carry
  5  woman inside of-+woman the_Baptist/woman mouth and Lord exist
  6  God exist-exist-chapter kiss woman the_Baptist/woman want-Lord this
  7  woman the_Baptist/woman have_mercy exist and then-exist woman
  8  the_Baptist/woman to-fast and grab God exist-exist-chapter
  9  and carry woman the_Baptist/woman inside of-+woman the_Baptist/woman

## 143r — the face, the cloud, and the two grinding

> mouth; and the Lord would, to God. Here ends the chapter. She kissed; and the woman's face beat upon the place [cheek] outward. God. Here ends the chapter. And there was a miracle, a farm; and the Lord God cried out, in the cloud, to the angel | of the Lord, leaving. O, to […] the woman, of the Lord, the father, the daughter, to love. The Lord is a miracle; the farm; the woman must the woman [suffered] the woman [patiently] this Lord; this woman, the creature of the Lord: the sin, the mercy; and then this woman in turn, grinding as one — thou, Lord God, sayest

  1  mouth and Lord want to God exist-exist-chapter kiss
  2  and woman the_Baptist/woman face beat on-place [cheek]
  3  out God exist-exist-chapter and SUBJ exist ~miracle farm
  4  and shout-to Lord_God on-+cloud on-angel | of
  5  Lord leave oh ~baptize the_Baptist/woman of-Lord from-father daughter
  6  to-love Lord exist ~miracle farm woman the_Baptist/woman have
  7  woman the_Baptist/woman [suffered] woman the_Baptist/woman [patiently] this-Lord
  8  this woman the_Baptist/woman [...] Lord sin have_mercy and_then
  9  this woman the_Baptist/woman in_turn grinding-+one you Lord_God say

## 143v — crucified, and the sin that dies

> the Lord God, in the cloud, to the angel of the Lord, this Lord, from Jesus; | and the Lord was crucified. And then this wife, the Lord, of the wife, the Lord God, of the wife mercy, to […] the woman, the brethren, this wife, through sin against the Lord, could; and then the Lord God, this Lord, this woman's sin — have mercy, Lord [forgive] Lord, upon the sin. [cloud] This says: the Son of God, the king of the high day, would the Lord, heaven, earth [shall pass away] in turn one. A man's sin dies; that is, damned […] the man damned. The Lord God, in turn: this man to the Lord, among the Lord

  1  Lord_God in_the_cloud on-angel of-Lord this-Lord from Jézus | and-Lord
  2  SUBJ crucified and_then this wife Lord of-wife Lord God
  3  of-wife have_mercy to-~baptize the_Baptist/woman brethren* this-wife commit sin
  4  against of-Lord can and_then Lord_God this-Lord this
  5  woman the_Baptist/woman sin have_mercy Lord [forgive] Lord on-sin
  6  [cloud] this say SUBJ son God high-~year-+king want Lord
  7  heaven earth [shall_pass_away] but one
  8  somebody sin die that_is be_damned to-+little somebody
  9  be_damned Lord God but this somebody to-Lord among Lord

## 144r — Saint Augustine, and an image of the Virgin

> heavenly the people, the man, to the Lord God, this Lord — thou, creature of the Lord, the sin, the mercy, […]; this must the man carry: the commandment of God. The man is saved through many sufferings. O chapter, O chapter, amen. It is written by | holy Saint Augustine: there was a woman, and a Lady who prayed to the happy virgin Mary, outwardly, three years. In […] there was an image | of the virgin Mary; and then […] this image | of the virgin Mary; and she said this: from the Lady, hear, Lady — and the man

  1  heavenly* people somebody to-Lord_God this-Lord you [...]
  2  Lord sin have_mercy seal-from this have somebody carry
  3  commandment God be_saved somebody to-many suffering
  4  chapter-oh chapter-oh amen write SUBJ | holy
  5  Saint_Augustine exist one ~sheep and Lady
  6  SUBJ pray happy virgin-Mary on-~out three
  7  year inside mount exist one image | virgin
  8  Mary and then-exist [knelt_before] this image | virgin
  9  Mary and say this ~sheep hear-+Lady and somebody

## 144v — thou who holdest heaven and earth

> pray to the virgin Mary. The man would: "Good Queen, thou who holdest heaven and earth" — this Lady would, the Lady, pray. And she served one day; then Mary, every day, she took bread, and [ate] truly, at the day's beginning. Then, the year out, in time, the woman went to this image of the virgin Mary, and said this, the woman: | "Lord, […] thou who holdest heaven and earth, Lady, | virgin Mary." This Lady spoke from thence; and two said; the girl said:

  1  pray virgin-Mary want-somebody good queen grab heaven
  2  land this-+Lady want-+Lady pray
  3  and servant one day then-exist Mary every day
  4  grab bread and [ate] righteous ~begin-~year
  5  then-exist year ~out inside time go this sheep
  6  this image virgin-Mary and say this sheep | Lord
  7  queen grab heaven land Lady | virgin
  8  Mary this-+Lady from speak and two say girl say

## 145r — how shall we creatures speak?

> "Queen, thou who holdest heaven and earth, Lady virgin Mary" — this woman spoke thus: how shall we creatures speak? How can she speak? Said this woman, this woman, [said to] love: this Mary would; and then Mary, the woman, served, fasted, and prayed two healings of Mary, and truly at the day's beginning this day's; and [ate] she took; and then, two years out, in time, the woman went to this image of the virgin Mary, and said, this woman: "Queen, thou who holdest heaven and earth, Lady virgin Mary"

  1  queen grab heaven land Lady virgin-Mary
  2  this-~sheep from speak how? how_shall_we* [...] speak
  3  can speak say this sheep this-~sheep
  4  [said_to] love this Mary want and then-exist Mary sheep/a_female_person
  5  servant fast and two Hail_Mary pray and righteous begin-~year
  6  exist-today’s and [ate] grab and then-exist
  7  ~out two-year inside time go this sheep this
  8  image virgin-Mary and say this sheep queen
  9  grab heaven land Lady virgin-Mary

## 145v — three days, three Hail Marys

> This Lady spoke from thence; and two said, this woman: "Queen, thou who holdest heaven and earth, Lady virgin Mary." The Lady prayed this to Mary, outwardly, fasting, fasting. The girl, the Lady: "Queen, thou who holdest heaven and earth" — this girl, the Lady, spoke; this woman [said to] love, this Mary would; and then Mary, the woman, served three days out; and three Hail Marys she prayed; and truly at the day's beginning, this day's; and [ate] she took; and then, out, three days, in time, the woman went to this image of the virgin Mary and said, this woman: "Queen, thou who holdest heaven

  1  this-+Lady from speak and two say this sheep queen
  2  grab heaven land Lady virgin-Mary
  3  pray Lady this Mary on-~out fast fast
  4  girl Lady queen grab heaven land
  5  this-girl Lady speak this-~sheep [said_to] love
  6  this-Mary want and then-exist Mary sheep/a_female_person servant
  7  on-out three_days and three Hail_Mary pray and righteous begin-~year
  8  exist-today’s and [ate] grab and then-exist out.
  9  three_days inside time go this sheep this image
 10  virgin-Mary and say this sheep queen grab heaven

## 146r — the Lady speaks from the image

> and earth, Lady virgin Mary." This Lady spoke from thence; and two said, this woman: "Queen, thou who holdest heaven, | the town there is, Lady virgin Mary." This Lady spoke from thence. This woman grew angry. Forgive — the Lady went, of the Lady the Lord said, this woman, this Lady; and the Lady went. Forgive, this Lord. The Lady prayed, and the Lady served the virgin Mary three days out. This girl, the Lady: "Queen, thou who holdest heaven and earth" — this Lady; and | went the Lady. Forgive, this Lord said, this woman, this Lord.

  1  land Lady virgin-Mary this-+Lady from speak
  2  and two say this sheep queen grab heaven | town
  3  exist Lady virgin-Mary this-+Lady from speak
  4  grow_angry this sheep remit go-+Lady of-+Lady
  5  Lord say this sheep this-+Lady and go-+Lady
  6  remit this Lord pray Lady and servant Lady
  7  virgin-Mary on-out three_days this-girl Lady queen
  8  grab heaven land this-+Lady and | go
  9  Lady remit this Lord say this sheep this-Lord

## 146v — the nail, and the Virgin in the image

> The Lady went […], this Lord; this Lady the Lord would, in the place. The girl: "Queen, thou who holdest heaven and earth" heavenly this woman, of the Lady, the Lord; and the Lady took this Lord, one [a candle] [lit] upon the piercing. And one […] […]; and the Lady went, this, | from the woman; and then […] the Lady went, this woman; and many went. | In time appeared the Lady, the virgin Mary, within the image, the woman; and then happy the virgin Mary took the woman, to this | [a candle]

  1  go-+Lady from-Lord this-Lord this-+Lady want-Lord on-place
  2  girl queen grab heaven land heavenly*
  3  this sheep of-+Lady Lord and Lady grab
  4  this Lord one [a_candle] [lit] on-pierce and.
  5  one [placed] [before_it] and go-+Lady this | from
  6  sheep/a_female_person and then-[?] go-+Lady this sheep
  7  and go many | inside time appear
  8  Lady virgin-Mary inside image woman the_Baptist/woman and_then
  9  happy virgin-Mary grab woman the_Baptist/woman to this | [a_candle]

## 147r — the son, and the king

> [candle] from the son, in the name of the virgin Mary, said this woman, this Lady; and the girl prayed; and the Lady served Mary three outward, this living day. "Queen, thou who holdest heaven and earth" — Mary took the girl, the Lady; this son the Lady would, the son, to this […] put | and take; the girl, the Lady, the son; in turn the Lady took one know; and then the virgin Mary, the Lady, went again to the king; and the king took the Lady, this know; and the brethren, this Lady said; from the king, living, the Lady did.

  1  [candle] from son inside name virgin-Mary say this
  2  sheep this-+Lady pray girl and servant Lady
  3  Mary on-~out three this-~sheep queen grab heaven
  4  land Mary grab-girl Lady this son
  5  want-+Lady son to this [a_candle] put | grab
  6  girl Lady son but Lady grab one
  7  know* and_then virgin-Mary go-+Lady to-?again king
  8  and king grab Lady this know* and brethren*
  9  this Lady say ~king living-exist Lady do

## 147v — the Virgin seen by all the people

> And then the Lady went to this king; and from the […] king this […]; and took […] this woman; and | then there were Pharisees; they left the Lady; and then the Lady, the heavenly host say served the Lady. In time appeared the Lady, […] the virgin Mary, within the image, the woman, and upon all the people she was seen. And then happy the virgin Mary, this woman: this is it. This Lady, like her, loved the girl, | this Mary; this Lady, the man did, the girl. The Lady is good; the Lady therefore […] in turn

  1  and then-exist go-+Lady this king and from see-~king
  2  this know* and grab [led_away] this sheep and | then
  3  exist Pharisees* leave Lady and then-exist Lady heavenly
  4  host say servant Lady inside time appear
  5  Lady happy virgin-Mary inside image woman the_Baptist/woman
  6  on-every people see and_then happy virgin-Mary this
  7  sheep this_is this Lady like love-girl | this
  8  Mary this Lady somebody do girl
  9  exist-+Lady good Lady ~exist °derided-~exist in_turn

## 148r — Adam went down to Jericho

> the Lady is […]; she was lost, this Lady; and here ends the chapter. happy the virgin Mary, before the people, forgave. It is written of Adam. The son, Seth. And this is the word. It is written: Adam went, one man, to Jerusalem, into the town of Jericho; and then Adam went into the field; and then there appeared an evil one; and then Adam a year of chapters [fell among] the evil one in the field; and then

  1  exist-+Lady °derided-~exist lose this Lady and
  2  leave-chapter-leave happy virgin-Mary before remit people.
  3  write Adam.
  4  son Seth.
  5  and this word.
  6  write go-~Adam
  7  one man^ on-Jerusalem
  8  inside Jericho town
  9  and then-exist and go ~Adam on-~field and then-exist.
 10  come^ one deer and then-exist ~Adam
 11  chapter-year [fell_among] deer on-~field and then-exist

## 148v — the man in the pit, and the two mice

> The man fled across the field, and then the man | fell the man into a pit; and then hang cling the man onto a tree, because there was a branch sticking out [root]; and there came two mice, one black, the other white; and this tree the two mice began to eat. And then the man saw, and to the man he saw an evil one [dragon] and which cried out to the man: the man is lost [in the well] if the man goes back again; this man, this | can

  1  escape ~Adam on-~field and then-exist ~Adam | conceive
  2  ~Adam inside one pit and then-exist hang
  3  cling ~Adam on-one tree because exist
  4  protrude [outgrow] and go two mouse one black
  5  in_turn-two white and this tree ~begin two mouse
  6  to-eat and then-exist see ~Adam to-~Adam
  7  and see one dragon = and
  8  who-shout-to ~Adam lose-~Adam [in_the_well]
  9  if again* go-~Adam this ~Adam this | can

## 149r — the lance of the soldier

> the evil one dies, if cling the man bows down to this. The evil one [dragon] tears the man apart; and then the man […] startled the man, and | he went to the dying Lord Christ; one soldier of the Lord Jesus Christ who died [pierced the side] […] the suffering; and this | can the evil one at the beginning, through the death of the Lord Christ and the man took hold of this soldier of Christ who died, the chapter | of the soldier of the Lord Jesus Christ who died: the suffering, the lance. And then this soldier of the Lord Jesus Christ who died freed the man from this

  1  evil die if cling bow ~Adam this.
  2  dragon = ~Adam rend and then-exist ~Adam
  3  [blind] through startle ~Adam and | go-die-Lord
  4  Christ one soldier-Lord-Jézus-die-Christ [pierced_the_side]
  5  [his] suffering and this | can
  6  evil on-~begin through [the_death_of_the_Lord_Christ] and
  7  ~Adam grab this soldier-[?]-die-~Christ-chapter | of
  8  soldier-Lord-Jézus-die-Christ suffering lance and_then
  9  this soldier-Lord-Jézus-die-Christ escape-~Adam on-this

## 149v — pulled out of the pit

> the pit; the man was scattered, and then the man was with the Lord; the Lord took hold of the suffering and the lance of the soldier of the Lord Jesus Christ who died and the man out of this pit, the chapter of the soldier of Christ who died, took hold; and then this soldier of the Lord Jesus Christ who died, then this man therefore the Lord took out, upon this pit there was the man inside this pit; and the man died, because | this man, this the evil one can: he dies, that is, he is damned. There is, there is a man [is baptized] who is saved. the man; God is [condemned] [not] the man saw

  1  pit scatter ~Adam and then-exist ~Adam exist-Lord
  2  grab-Lord of-soldier-Lord-Jézus-die-Christ suffering lance
  3  and ~Adam ~out this pit soldier-[?]-die-~Christ-chapter
  4  grab and_then this soldier-Lord-Jézus-die-Christ then-exist
  5  this-~Adam ~exist out grab-Lord on-this pit exist
  6  ~Adam inside this pit and die-~Adam because-exist | this
  7  ~Adam this deer die that_is be_damned
  8  exist exist ~Adam [is_baptized] be_saved.
  9  ~Adam God-exist [baptized] [not] see ~Adam

## 150r — a certain man had two sons

> wrote the church father, to the heathen; first wrote […] | upon this this wrote the church father, the church father [two sons] upon that wrote [the younger] the church father, upon that, wrote the church father the Pharisees; and the church father [the gospel] the gospel: there was one man, and then this man had one. son; and this son was three(?); he sold | and bought from him; and the son […] wanted, the man could the son bought; and then the son went away [divided] among; this son, of the son, from the father, said this

  1  write church_father to-+pagan first write [a_certain_man] | on-this
  2  this write church_father church_father [two_sons] on-that_is write
  3  [the_younger] church_father on-that_is SUBJ write church_father
  4  Pharisees* and church_father [the_gospel] gospel exist one
  5  man^ and then-exist have man^ one.
  6  son and this son exist three sell | from-buy
  7  man^ and son two-two want-somebody can
  8  son from-buy and then-exist son go exorcise
  9  [divided] among this son of-son from-father say this

## 150v — the father kissed him

> the son; oh, of the son, from the father: the father kissed the son upon this last year; and then the son, the father kissed; and cursed [ran] and then that father was [fell upon his neck] a dog then this father was, the father, the son, the apostle, for good, therefore this son upon this went, to the son, in love the son went, speaking […] the church father, of the man, the church father, upon […] the name: Saint Augustine the church father spoke; it is of Saint Augustine; and the man believes in the Lord Jesus Christ; the man has this, of the man. the son, for good, the apostle: how […] dies, the good man.

  1  son oh of-son from-father kiss son father on-this
  2  last year and then-exist son father kiss and cursed
  3  [ran] and_then that_is father exist [fell_upon_his_neck] dog
  4  then-exist this-father exist father son apostle on-good ~exist
  5  this-son on-this go-~son on-love son go-~son speak-~baptize
  6  church_father of-somebody church_father on-[?]-+name Saint_Augustine_the_church_father
  7  speak ~brother of-+Saint_Augustine and somebody believe
  8  inside Lord-Jézus-Christ have-somebody this of-somebody.
  9  son on-good apostle how? ~you good-somebody.

## 151r — for the good, to the father

> […] dies, from the father, for good, the apostle of the father, this; and you the man, of the man, the son, for good, the apostle, this man, because seal and the son, therefore this man, for good, the apostle of the man the son wants […] from […] dies, at the coming, two the son's sin; and the son's sin, you are, you light upon you: take the forgiveness of sins, and you. Cursed […] the son's sin, upon […] said the Lord God, holy Hezekiah the king, the prophet, to the angel of the Lord; Hezekiah the king was; the man had three born from whosoever; and from three born

  1  ~you from-father on-good apostle-father this and you
  2  man^ of-somebody son on-good apostle-this-somebody so_that^
  3  seal* and son ~exist-somebody-this on-good apostle of-somebody
  4  son want-[?] from ~you on-~be_born the_rest^
  5  ~son-sin and son-sin you exist you
  6  light on-you grab-+forgiveness_of_sins and you.
  7  cursed [ran] ~son-sin on-[?] say Lord_God holy-Hezekiah
  8  prophet on-angel of-Lord Hezekiah exist man^ have
  9  three on-be_born from whosoever* and from three on-be_born

## 151v — the forgiveness of sins

> therefore […] and has; a) there is the son's sin; remit it; you, light, leave; and then the man sees the light, and there is the forgiveness of sins for you; go to the forgiveness of sins in the image [likeness] the heart; how one woman the forgiveness of sins; and there is the forgiveness of sins, […] the forgiveness of sins of the man, the son; the forgiveness of sins for you, son; the other, and the son from whosoever the son in turn, to and upon the son, to [not] the man is damned; if, and the son, to therefore the man, the apostle, for good; and upon the son, to, is damned | in turn

  1  ~exist ~exist-[?] and have but exist ~son-sin remit
  2  you light to-leave then-~exist somebody see light and
  3  exist forgiveness_of_sins to you go-+forgiveness_of_sins
  4  inside image [likeness] heart how? one a_female_person
  5  forgiveness_of_sins and exist-+forgiveness_of_sins [?]-+forgiveness_of_sins
  6  of-somebody son forgiveness_of_sins you son
  7  in_turn-two and SUBJ son from whosoever* son in_turn to-to
  8  and on-son to-to [not] somebody be_damned if and son to-to
  9  ~exist somebody apostle on-good and on-son to-to be_damned | in_turn

## 152r — saved or damned, and the litany

> the brother, the son, to; there is the man, the apostle, for good; there is the man saved; therefore the man is damned; the man, the third son; and from whosoever this, of the man, good do […] do; this the man can do, | upon out of darkness into the light goes the man of the Lord God; love the Lord God; have mercy, Lord God; righteous, Lord God; hope, Lord God; every one of the man [with his whole heart] Lord God; every one of the man, good the apostle, Lord God; of the man, fast, Lord God; of the man repentance; from town to town carry, Lord God; of the man, believe

  1  ~if son to-to exist somebody apostle on-good exist somebody
  2  be_saved somebody ~exist somebody be_damned somebody third
  3  son and SUBJ from whosoever* this of-somebody good_deed =
  4  [penance] do this somebody can do | on
  5  darkness out on-light go-somebody Lord_God SUBJ love Lord_God
  6  SUBJ have_mercy Lord_God SUBJ righteous Lord_God SUBJ hope Lord_God
  7  SUBJ every of-somebody [with_his_whole_heart] Lord_God SUBJ every of-somebody virtue^
  8  apostle Lord_God SUBJ of-somebody fast Lord_God SUBJ of-somebody
  9  repentance from_town_to_town* carry Lord_God SUBJ of-somebody believe

## 152v — God be merciful to me a sinner

> Lord God; every good deed, Lord God; of the man a good life; oh chapter, oh chapter, in heaven and earth in the gospel a man speaks the Lord Christ, the son of the Lord and then a man went into the temple. And the man knelt down inside. In the temple every man has this; he said to the Lord: thanks, Lord God, pleasing it is to the Lord; holy mercy, have mercy on the sinner because this is he who repents; every sinner, to the Lord, thanks

  1  Lord_God SUBJ every good_deed = Lord_God SUBJ of-somebody
  2  good living chapter-oh chapter-oh inside heaven land
  3  inside gospel man^ speak
  4  Lord-~Christ son of-Lord
  5  then-exist go man^
  6  inside temple and.
  7  kneel-somebody inside.
  8  temple everybody = have this say to-Lord thanks Lord_God
  9  godfearing^ exist of-Lord holy-have_mercy have_mercy somebody-sin
 10  because this who repentance every somebody-sin to-Lord thanks

## 153r — Lord, remember me

> Lord God, have mercy on the sinful man. Holy John speaks: how from the thief; and Christ was crucified, and the thief; and then the thief went up, he who from that day, the Lord Jesus, to the place […] that Lord Jesus righteous, the son of God, because he is; out, the thief, the Holy Spirit have mercy; and he cried to the cross, he answered | asking the thief; this thief, to this Lord: remember me, the thief. then to go with the Lord into the land of the Lord. And then these two thieves; and there was the Lord, the thief condemned. […] this […] then this Lord loved | can

  1  Lord_God find_mercy^ man^ sin speak holy-John how?
  2  from thief and Christ crucified thief and then-exist thief
  3  on-go who-from-~year Lord-Jézus on-place ~exist-this that Lord-Jézus
  4  righteous son God because-exist ~out thief holy-spirit
  5  find_mercy^ and shout-to on_the_cross answered | ask
  6  thief this-thief this-Lord remember on-thief
  7  then-to go-Lord inside of-Lord kingdom^ and_then
  8  this the_rest^ thief and exist Lord thief condemned.*
  9  [remember_me] this [thy_kingdom] then-exist this-Lord love | can

## 153v — today shalt thou be in paradise

> the Lord; this Lord is to redeem; and the thief, the thief, the one Lord and cried out, this thief, first, to this Lord: righteous the man; the two thieves, these die, they deserve it and turned toward the Lord Jesus, the head of the Lord, to the thief and then the Lord Jesus, the robe, the Lord believe the year until wherefore hidden; the thief is [said to the Lord] before, in Paradise and one said, from the thief: how shall we | upon the thief, the last year, heaven and earth it is written, in the days of Moses, righteous [due reward]

  1  Lord this-Lord exist to-Lord redeem and thief thief one-Lord
  2  and shout-to this thief first this-Lord SUBJ righteous
  3  man^ the_rest^ thief-thief this die from deserve
  4  and turn_to Lord-Jézus of-Lord head to-thief
  5  and_then Lord-Jézus robe the_Lord believe* day^ until
  6  why?-hide exist-thief [said_to_the_Lord] before inside into_Paradise
  7  and one say from thief how_shall_we* | on-of
  8  thief last year-heaven kingdom^
  9  write SUBJ inside Moses-~year righteous [due_reward]

## 154r — the fire of purgatory

> […] the fire of purification, rather than hell [torment] on the day [after] the soul goes out, into purification; this soul, joy because the soul goes before the face of the Lord Jesus Christ. The end of this holy gospel. […] the world, one year redeemed, a hundred years of suffering; heaven and earth; the other, the ways there is a man, for one day of repentance | atonement the man inside the fire of purification, a hundred years for one day in turn; and the man, righteous, to fast and repentance | atonement the man, of the man, heaven and earth, and

  1  from-°withered purification fire but_rather* hell [torment]
  2  ~year-to [after] soul go out on-purification this soul joy
  3  because go-soul before from face Lord-Jézus-Christ end
  4  this holy-gospel [?]-?world one year redeem hundred-year
  5  suffering heaven land in_turn-two ways*
  6  exist somebody to one day repentance | atone
  7  somebody inside purification fire hundred-year to-one
  8  day in_turn and somebody righteous to-fast and repentance | atone
  9  somebody of-somebody SUBJ heaven land and

## 154v — the captive and the king

> this man, repentance, leave; because the man, the righteous man the suffering of the Lord Christ; and the man | is saved. the man; oh chapter, oh chapter, amen; Lord God, with all thy heart wrote holy Elijah the prophet and holy Luke. And then he was taken prisoner, the robber, the […] son one, from the king of the world; and and then it is written, this […] son, of the […] […] the world […]; then the […] son bought

  1  this somebody repentance leave because somebody SUBJ righteous-somebody
  2  suffering Lord-Christ and somebody | be_saved.
  3  somebody chapter-oh chapter-oh amen Lord_God be_loved
  4  write holy-Elijah prophet
  5  and holy-Luke.
  6  then-exist capture
  7  robber ~baptize-son
  8  one from-?world-~king and
  9  then-exist write this ~baptize-son of-[?]
 10  [?]-?world-~king then-exist ~baptize-son from-buy

## 155r — held in bondage

> from the king of the world, in bondage; and the […] son could not get out […]; this humble, this […] son; and sadly the […] son left; and then […] this robber, the daughter, at the building, the daughter inside one house; and then for many years he led her out. This robber, upon this, until; and then | the daughter believed; the believing daughter went out, home and then the believing daughter went home, this from […] the […] son; and the believing daughter began to […]

  1  from-?world-~king on-bondage and ~baptize-son cannot
  2  out [bondage] this humble this ~baptize-son and
  3  sad ~baptize-son leave and then-exist [was_afraid]
  4  this robber daughter on-to-+building daughter inside
  5  one house and then-exist many year out lead.
  6  this robber on-this ~until and then-exist | daughter
  7  believe out go-daughter-believe to-home
  8  and then-exist go daughter-believe to-home this from-[?]
  9  ~baptize-son and begin-daughter-believe to-[?]

## 155v — he could not buy him back

> speak; and the daughter could not speak, because there was sadness; the […] son upon this, of the […], the […] world […] the brother, the […] son, could not buy him back, and | went the believing daughter from the […] son; and then the believing daughter, and the two, the believing daughter went; then the […] son, good, the whole wide world; and then to […] | the daughter believed, and began to talk; and the believing daughter, spoke to […], said to […] this. From the king of the world: if, how shall we ransom the believing daughter?

  1  speak and cannot daughter speak because exist
  2  sad ~baptize-son on-this of-[?] [?]-?world-~king
  3  brethren* ~baptize-son cannot from-buy and | from-go
  4  daughter-believe from* ~baptize-son and then-exist
  5  daughter-believe and two go-daughter-believe then-exist
  6  ~baptize-son good all_the_world and then-exist to-[?] | daughter
  7  believe begin_to_talk and daughter-believe.
  8  speak to-[?] say to-[?] this.
  9  from-?world-~king if how_shall_we* daughter-believe | redeem-daughter.

## 156r — how shall she be ransomed

> believe; the […] son, this believing; how is this believing daughter to be ransomed? this, the day on which, before the believing daughter | from the father the king of the world, the evil one; and then this believing daughter, this robber if the believing daughter wants […] to take | this to […] the […] son, the wife | this daughter believing, this […] the believing daughter wants to be ransomed; this, the day on which, said this to the son of the son, this from the king of the world, this […] wants […]

  1  believe to-[?] this hide-~year-which say this | daughter
  2  believe how?-exist this-daughter-believe redeem-daughter-believe
  3  this hide-~year-which before of-daughter-believe | from-father
  4  world-~king evil and_then this daughter-believe this robber
  5  if daughter-believe want-[?] grab | this
  6  to-[?] [?]-son wife | this-daughter
  7  believe this-[?] want-daughter-believe
  8  redeem this hide-~year-which say this to-son-son this
  9  from-?world-~king this-[?] want-[?]

## 156v — the escape by night

> this believing daughter has the […] son as husband and then this time; and then the believing daughter to […] in the night | fled, the daughter believing […]; and the rich | carried away the daughter believing […], the brother | the believing daughter to […] the rich could carry; and then […] to […] | to the woman the son, […] the world […]; and | […] the daughter believing, saw; and went, this of the […]

  1  this-daughter-believe have [?]-son wife
  2  then-exist this time and then-exist daughter-believe
  3  to-[?] inside night | escape-daughter
  4  believe-[?] and ~rich | from-carry-daughter
  5  believe-[?] brethren* | daughter-believe
  6  to-[?] ~rich can carry and then-exist
  7  [?]-to-[?] | to-of-+woman
  8  son [?]-?world-~king and | [?]-daughter
  9  believe see and go this of-[?]

## 157r — the virgin daughter

> […] the world […]; and sadly the father left; and then to […] the believing daughter went to […] | to of […] […] and then this from […] oh, of […], to […], oh, from […] love went to […] | judged from […] | this to […]; he is this virgin, the believing daughter, said this to […]: this is the believing daughter, from the robber he who is to […], the robber taken prisoner said this from […]: he is this believing daughter, this woman

  1  [?]-?world-~king and sad leave-father-[?] and then-exist
  2  to-[?] daughter-believe go-to-[?] | to
  3  of-[?] [?]-[?] and_then this from-[?]
  4  oh of-[?] to-[?] oh from-[?]
  5  SUBJ love go-to-[?] | judge from-[?] | this
  6  to-[?] he_is* this virgin-daughter-believe say
  7  this to-[?] this_is daughter-believe from robber
  8  he_who exist to-[?] capture-+robber
  9  say this from-[?] he_is* this-daughter-believe this woman

## 157v — she is led before the Father

> The believing daughter eloped; she was led before God the Father | of the daughter the Lord Christ. This is the daughter who believes in the Lord Christ, in unbelief […] of the daughter of the Lord Jesus Christ, from God the Father; and said this | the daughter of the Lord Jesus Christ, this from […] […] this believing daughter of the Lord Jesus Christ in unbelief […] of the believing daughter of the Lord Jesus Christ | from God the Father, because from God the Father, of the daughter of the Lord Jesus Christ, the wealth she has; remit […] […] […] in turn | then this king of the world was; every one of […] the rich | was sold from […] therefore there is, to […]: how shall we | from

  1  elope-daughter-believe lead before from-God_the_Father | of-daughter
  2  Lord-Christ this_is daughter-Lord-Christ-believe inside not_believe
  3  [the_mother] of-daughter-Lord-Jézus-Christ from-God_the_Father and say this | daughter-Lord
  4  Jézus-Christ this from-[?] [named] this-daughter-Lord-Jézus-Christ-believe
  5  inside not_believe [the_mother] of-daughter-Lord-Jézus-Christ-believe | from
  6  God_the_Father because from-God_the_Father of-daughter-Lord-Jézus-Christ wealth
  7  have remit man* [talent] [asked] in_turn | then
  8  exist this-from-?world-~king exist every of-[?] ~rich | sold
  9  from-[?] ~exist exist to-[?] how_shall_we* | from

## 158r — the buying and the selling

> buy this, in turn; and then to […] he wanted from […] to buy this; it is, it is, from […] from […] oh chapter, oh chapter; said this from […] of […] to […] this […] this | the daughter of the Lord Jesus Christ who believes, […] took | to scatter every one of […] the rich; and said this to […] of […] […] | this to […] this believing daughter of the Lord Jesus Christ | wanted

  1  buy-this in_turn then-exist to-[?] want-from-[?]
  2  from-buy-this exist exist from God-?seal from-[?]
  3  chapter-oh chapter-oh say this from-[?] of-[?]
  4  to-[?] this-[?] this | daughter-Lord-Jézus
  5  Christ-believe son* grab | to
  6  scatter every of-[?] ~rich and say this
  7  to-[?] of-[?] [?]-[?] | this
  8  to-[?] this daughter-Lord-Jézus-Christ-believe | want

## 158v — a wife, and the end of it

> to […] took; and then this time | to the woman the son, righteous, a wife; and the […] son, righteous. until the daughter of the Lord Jesus Christ who believes, and | the woman wanted the son of the believing daughter of the Lord Jesus Christ lived [happily] God, the whole wide world; oh chapter, oh chapter, amen; Lord God, with all thy heart. Before the gospel, written by holy Luke, in the twenty-second chapter | of the writing; the time | then the Lord Jesus was, in the thirtieth

  1  to-[?] grab then-exist this time | to-of-+woman
  2  son righteous wife and [?]-son righteous.
  3  ~until Lord-daughter-Jézus-believe-Christ and | want-+woman
  4  son-daughter-Lord-Jézus-Christ-believe living [happily] exist.
  5  God all_the_world chapter-oh chapter-oh amen Lord_God be_loved
  6  before Word^ write
  7  holy-Luke inside two-two chapter | of
  8  write time | then
  9  exist Lord-Jézus inside thirty

## 159r — two men with spirits

> and second year; the time; the Lord Jesus went to the shore; bread and then the Lord Jesus found the shore of the sea one hundred; the sin of this; and then he found, the Lord Jesus, the shore of the sea, among one mountain, two men with spirits; in the two men there were | six hundred and six hundred and sixty and six evil devils; and how the two men's hearts were found, the hearts of these two men aforesaid […] in turn […] the two men were, to take | the Lord

  1  two-year time go Lord-Jézus shore bread
  2  and then-exist meet^ Lord-Jézus shore sea
  3  one hundred* sin-this-from and then-exist meet^
  4  Lord-Jézus shore sea among one
  5  mount two somebody-spirit inside two man^ exist | six
  6  hundred* and six_hundred* and six-ten and six devil = and how?
  7  two man^ heart find-two-somebody this heart two man^
  8  aforesaid [tombs] in_turn [possessed] exist two man^ to-grab | Lord

## 159v — the devils ask to be sent into the swine

> Jesus Christ; and the two men went to the Lord Jesus, and began the two men to cry out; he answered [torment] and the Lord went before the time; he loved the two men; the evil suffering, the Lord, every died of many sufferings; and the two men began the devils to ask, into the leftover food; and then the two, whatsoever devils there were, were driven by the Lord Jesus into the leftover food, because […] the Lord Jesus scattered them from the leftover food in turn; and from the two men the woman's spirit, the Lord God redeemed

  1  Jézus Christ and go two somebody to-Lord-Jézus and begin
  2  two somebody shout-to answered [torment] and Lord go before
  3  time love two somebody devil^ suffering Lord all^
  4  die from* many suffering ~and begin two somebody
  5  devil^ ask inside leftovers food? and
  6  then-exist two whosoever* devil^ exist chase
  7  Lord-Jézus inside leftovers food? because name-°sat-~year
  8  Lord-Jézus from leftovers food? scatter
  9  in_turn from two somebody woman the_Baptist/woman spirit redeem Lord_God

## 160r — the herd runs into the sea

> and then the herdsmen saw this, and were startled, and fled to the herdsmen's home and the herdsmen said what they had seen of the Lord; and then they went from the Lord […] saying: Jesus of Nazareth. And every aforesaid herd of the herdsmen was destroyed in the sea; the Lord humbly spoke, and sadly they left […]. The end of this apostolic holy gospel. This holy gospel begins, written by holy Luke in the twenty-second chapter of the writing; the time the Lord Jesus sat by the sea; then, in his thirty-second year

  1  and then-exist see this-Lord this shepherd and through
  2  startle and escape to-of-shepherd home
  3  and say shepherd Lord-see of-shepherd and_then
  4  go-from-Lord [?]-from say Jézus Nazareth and every
  5  aforesaid of-shepherd herd inside sea perish^
  6  Lord ~humble-+say and sad leave-[?] end this
  7  apostle holy-gospel here_begins this holy_gospel write holy-Luke
  8  inside two-two chapter of-write time sit Lord-Jézus
  9  on-sea then-exist inside thirty two-year

## 160v — the Lord returns to Capharnaum

> Within, there was one of the Lord God, and through [preached] the Lord Jesus into one land […] into one […] [was in the house] the house; and then he was seen, the Lord Jesus going, and they began to cry out [the palsy], and the Lord went; this Lord would; he says from on high, of the rich [the roof] he made ready, and the Lord Jesus returned | into the middle of the Lord's town; and this town | was named Capharnaum; and he took to himself three apostles, Peter and Paul and

  1  inside one ~exist Lord_God and through [preached] Lord-Jézus inside
  2  one land [Capharnaum] inside one in_turn-chapter-in_turn
  3  [was_in_the_house] home and then-exist see-+say go-Lord-Jézus
  4  and begin-+say shout-to [the_palsy] and go-Lord
  5  this-Lord want-Lord say from-high of-+say ~rich [the_roof]
  6  prepare and-Lord return Lord-Jézus | inside-and
  7  amid-inside of-Lord town and this town | and
  8  was_named* exist Capharnaum and grab
  9  to-Lord three apostle Peter and Paul and

## 161r — the paralytic, and the four who carried him

> John; because then the Lord Christ would do a miracle, and every miracle the Lord had to confess; and then | he preached, the Lord, in Capharnaum; and many people made ready to him, and then they carried one upon an ass before the Lord Jesus, within | two by two, the men, at the head. Among them: faith, love, hope, mercy; and | they could not — the four friends of the paralytic — so instead, up onto the temple they went, the four friends; and the temple they pierced through, the four friends, to let him down

  1  John because then-exist Lord Christ miracle do want
  2  Lord-to every miracle confess have and then-exist | preach
  3  Lord inside Capharnaum and prepare to-Lord many people
  4  and then-[?] carry one from-donkey before
  5  Lord-Jézus inside | man^ two-two man head.
  6  among believe love hope forgive^ and | can
  7  the_four_bearers inside °but_rather-?again on-temple
  8  go the_four_bearers and temple
  9  through pierce the_four_bearers to-?again

## 161v — thy sins are forgiven thee

> onto the roof; and a man, with a rope, | let down faith, love, hope, mercy, to the Lord, before the Lord Jesus Christ; the Lord Jesus saw, and was saved the man; from the faith of the two and two, what and who, and a man had mercy, the Lord Jesus Christ; and then the Lord Jesus: son, of the Lord believing son, loving son, hoping son, | mercy; the son shall have health, the son; and then the Lord was there [their faith]; the Lord, the Jews, the Lord Jesus; and then the Lord Jesus […] | said: believe, man, love, hope, man, have mercy, man; there is [forgiven] a man, or rise, and go, man.

  1  on-roof and man^ rope | go-~ask-love-hope
  2  forgive^ Lord before Lord-Jézus-Christ see Lord-Jézus be_saved
  3  of-somebody believe from two-two what-+who and man^
  4  forgive^ Lord-Jézus-Christ and_then Lord-Jézus son of-Lord
  5  ~ask-son love-son hope-son | forgive^
  6  son exist have-son health son and
  7  then-exist-Lord exist [their_faith] Lord Jew Lord-Jézus
  8  and_then Lord-Jézus [thy_sins] | say-believe-somebody-love
  9  somebody-hope-somebody-have_mercy-somebody exist [forgiven]
 10  have-somebody or rise and* go-somebody

## 162r — rise, take up thy bed and walk

> The Jews said […] | said: believe, man, love, man, hope, man, have mercy, man; there is, therefore, a man, said the Lord Jesus truly; the Jews spoke, and then | the Lord Jesus took […] of the son | faith, love, hope, mercy, that day; and the stretcher he took, and put the son on the stretcher, upon the son's shoulder; and the man went, and the son was saved, the man's son, home to heaven. Here ends this holy gospel. The Lord Christ raised three dead, stood them up, the Lord | of

  1  say Jew [blaspheme] | say-believe-somebody-love-somebody
  2  hope-somebody-have_mercy-somebody exist therefore* have-somebody
  3  say Lord-Jézus righteous SUBJ speak Jew and_then | Lord
  4  Jézus grab-[?] of-son | ~ask-love-hope
  5  have_mercy-~year and stretcher
  6  take^ and put son stretcher
  7  on-of-son shoulder and go-somebody-son be_saved
  8  of-somebody son ~home heaven here_ends this holy_gospel
  9  Lord-Christ three die-somebody SUBJ rise^ resurrect-Lord | of

## 162v — the three whom the Lord raised

> the Lord, of the Father; first he could stand up and raise, the Lord Jesus, one chief man's daughter in Jerusalem; and the second | dead man he stood up and raised, the Lord Jesus: Lazarus, in Jerusalem; | and the third dead man he stood up and raised, the Lord Jesus, at Nain; [maiden] therefore stood up and raised the three dead to the Lord, the Lord Christ: rather, the daughter, Lazarus, the son; of the Father, of the Lord, he stood up and raised; of the Lord, why in turn, of the Lord the finger […] the miracle he did. | The Lord, Father, Son, God, Jesus, Holy Spirit, the Lord God, with all thy heart.

  1  Lord from-God_the_Father can first stand_up resurrect Lord-Jézus
  2  one head daughter inside Jerusalem in_turn-two | die
  3  man^ stand_up resurrect Lord-Jézus Lazarus inside Jerusalem | in_turn
  4  three die-somebody stand_up resurrect Lord-Jézus Nain
  5  [maiden] therefore* stand_up resurrect and three die-somebody to-Lord
  6  Lord-Christ but_rather* daughter Lazarus son from-God_the_Father
  7  of-Lord stand_up resurrect of-Lord why?-in_turn of-Lord
  8  finger [into] miracle do | Lord
  9  God_the_Father-son-God-Jézus-holy-spirit Lord_God be_loved

## 163r — the widow of Nain

> This holy gospel begins, written by holy Luke, in the […] chapter of the writing: the time, then, the Lord Jesus, in his thirty- | second year; the time he went, | the Lord Jesus, into one town; and this town's name was Nain; and the Lord went to the farm, and many people, and then to the Lord the seventy and the twelve apostles, and | then then the Lord Jesus kept going to this town, and then there died in this town the son of one widow woman.

  1  here_begins this holy_gospel
  2  write holy-Luke inside
  3  one-[?] chapter of-write
  4  time then-exist
  5  Lord-Jézus inside thirty | two
  6  day^ time go | Lord
  7  Jézus inside one town and this town name
  8  exist Nain and go farm Lord many people
  9  and then-exist to-Lord seventy and six-six disciple^ and | then
 10  then-exist go_on Lord-Jézus this town and then-exist
 11  die inside this town son one widow

## 163v — weep not

> and the son was carried; therefore the brethren of the son, the Lord God, the thief, therefore humble; the son was of the Lord God, therefore God had the son carried out of the town, two by two among the men, at the head, because they had him within. The word of the Old Testament: he was borne out of the town, to the aforesaid wide world; and there were to the son many people; and then they left behind an army, an army, among the gates, from the two peoples, the people, two; and they left [compassion]; and the Lord Jesus saw many sorrowing; and then this woman, the chief, remained a widow, sorrowing, this one; how then this? Said the Lord Jesus: stand up | this

  1  and son carry ~exist brethren-~son Lord_God thief ~exist humble
  2  son exist Lord_God ~exist God have-~son out on-town
  3  two-two among man head because have inside.
  4  Old_Testament word conceive out town to-from aforesaid all_the_world and exist
  5  to son many people and then-exist leave-to-leave an_army
  6  an_army among ~gate from-two people people two
  7  and stand^ [compassion] and see Lord-Jézus many
  8  sad and_then this woman = remain-~baptize
  9  sad this how? then-exist this say Lord-Jézus stand_up | this

## 164r — young man, I say to thee, arise

> the woman's son; and the Lord Jesus left off from the coffin, which within the coffin to the son, from the two by two men at the head; and the Lord Jesus touched, why in turn, from the coffin, which within the coffin lay dead, the son of this widow woman; and then | the Lord Jesus raised this son -- in this example, the son [arise] -- and he rose and sat up. How? As one prophet; and thus the Lord went; his descendant, to the pleasing of the Lord, the prophet foretold through this the Lord went; and then the Lord Jesus took the son, of the son | faith, love, hope […]; and | faith, love, hope

  1  woman of son and stand^ Lord-Jézus from coffin which inside coffin
  2  to-~son to-~son from two-two man head and
  3  touch Lord-Jézus of why?-in_turn from coffin which inside coffin
  4  lie die son this widow and_then | Lord
  5  Jézus rise this son example* son [arise] and rise
  6  on-sit how? one prophet and_then this_is
  7  go-Lord descendant to-pleasing-Lord prophet through predict this_is
  8  go-Lord and_then Lord-Jézus grab-~son of-son | believe
  9  love-hope-[?] and | believe-love-hope

## 164v — and he gave him to his mother

> mercy, the day; and they put the son, faith, love, hope, mercy, | upon the son's shoulder; and the son took, why in turn, the Lord Jesus; and then the son was; the Lord took the son's mother, and the son went to the temple, the mother; he was saved; the son's temple, the mother, home to heaven; much joy, in turn, one sorrow remitted. And in turn the two of them could see the Lord Jesus Christ; and the Lord, every thanks they gave him. Here ends this holy gospel. The Lord's love. Written by holy Luke in the […] chapter of the writing. This woman signifies the mother, the temple, faith, the three baptisms,

  1  have_mercy day and put son believe-love-hope-have_mercy | on-of
  2  son shoulder and son give^ on-why?-in_turn Lord-Jézus and
  3  then-exist son exist grab-Lord of-son mother and
  4  go son temple mother be_saved of-son temple mother
  5  ~home heaven great^ joy in_turn one sad remit
  6  in_turn-two see-somebody can Lord-Jézus-Christ and Lord
  7  every thanks grab-somebody here_ends this holy_gospel the_Lord love
  8  write holy-Luke inside one-[?] chapter of-write
  9  this woman symbolize mother temple believe ~baptize

## 165r — what the widow and her son signify

> the widow; the son signifies the soul of every man, that the Lord God, the Lord's heart, every man; this town signifies that, that he is saved, that […] the Lord Jesus Christ, all the wide world | this this is saved: every man who believes, the three baptisms, the widow [signifieth] the Lord saves, the Lord Jesus Christ, of the Father, of the Lord. In this gospel, as holy Luke writes, there went two by two men at the head, to the son; in this example the son [arise] and the son was dead; and the son they took and carried; therefore love | the Lord God. The thief, therefore, is humble; the Lord God, therefore, has

  1  the_Baptist/woman son symbolize soul everybody = that* Lord_God heart-Lord
  2  everybody = this town symbolize that* that* be_saved
  3  that* [signifieth] Lord-Jézus-Christ every all_the_world world | this
  4  this be_saved everybody = believe ~baptize the_Baptist/woman [signifieth]
  5  the_Lord be_saved Lord-Jézus-Christ from-God_the_Father of-Lord
  6  inside this gospel SUBJ write holy-Luke go two-two man
  7  head to-~son this example* son [arise] and son
  8  exist die and son grab and carry ~exist love | Lord
  9  DIV thief SUBJ ~exist exist humble Lord_God ~exist have

## 165v — the first of the four ways

> the Lord God; and this, therefore, repentance [confession] took this son, this widow woman; and the son was carried out, into belief. The three baptisms, the widow: that is, the son cast out, remitted, saved, the damned son. Chapter. Chapter. In the gospel written by holy Luke, this example: therefore love the most high Lord God | from the letter, with all the heart; rather, love, and this, and the heart, love the son, and therefore the brethren. Then the dead son goes to the son, and leaves; therefore love on the first way. In the gospel written by holy Luke, this example: there were many thieves, but by name the son

  1  Lord_God and this ~exist repentance [confession] grab this son this
  2  widow and son carry out on-believe.
  3  ~baptize the_Baptist/woman that_is cast_out son remit be_saved
  4  be_damned son chapter-oh chapter-oh inside gospel write
  5  holy-Luke this example* ~exist love high Lord_God | from
  6  literal every heart but_rather love-and-this-and heart love-son and ~exist brethren*
  7  then-chapter die-son go to-son and leave ~exist love
  8  on-one ways* inside gospel write holy-Luke
  9  this example* SUBJ exist many thief ~but-+name-to son

## 166r — the second, third and fourth ways

> in repentance took; then the dead son goes to the son. And the thief leaves, on the second way. In the gospel written by holy Luke, this example: therefore be humble, son, man; and the Lord God; then the dead son goes to the son, and leaves; therefore be humble, on the third way. In the gospel written by holy Luke, this example: therefore he has, the son, the Lord God, in all of the son's [whosoever sins dies] [dead] the son is within [whosoever sins dies] then the dead son goes to the son, and leaves; therefore he has

  1  on-repentance grab then-chapter die-son go to-son.
  2  and leave thief on-two ways* inside-gospel write
  3  holy-Luke this example* ~exist exist humble son
  4  somebody and Lord_God then-chapter die-son go to-son
  5  and leave ~exist exist humble on-+three ways* inside-gospel
  6  write holy-Luke this example* ~exist have
  7  son Lord_God inside every of-son [whosoever_sins_dies]
  8  [dead] SUBJ exist son inside [whosoever_sins_dies]
  9  then-chapter die-son go to-son and leave ~exist have

## 166v — the whole law in two commandments

> on the fourth way; and [between] the two by two men, and the son they took, the two by two men, and carried the son out the town gate of the town, into belief; the three baptisms, the widow; into damnation, then the son is carried into hell, damned. Chapter. Chapter. [with thy whole soul] therefore be saved. It is written in Moses, truly: love the Lord God most high with all thy heart, with all thy soul, with all thy might, with all thy heart; and of thy father's son, how a man loves his neighbour | of the man; heaven and earth. Here ends this holy gospel.

  1  on-two-two ways* and [between] two-two man and son
  2  grab two-two man and son carry out the_town_gate*
  3  town on-believe ~baptize the_Baptist/woman on-be_damned then-chapter
  4  son carry inside hell be_damned exist chapter-oh.
  5  chapter-oh [with_thy_whole_soul] ~exist be_saved write inside
  6  Moses true^ love Lord_God highest all^ heart all^ of-somebody
  7  soul all^ of-somebody might all^ of-somebody heart and
  8  of-somebody from-father son how?-to somebody neighbour | of
  9  somebody SUBJ heaven land here_ends this holy_gospel

## 167r — a certain rich man had a steward

> This holy gospel begins, written by holy Luke in the sixth chapter of the writing: the time the Lord Jesus said to the apostles of the Lord, and to the Jewish people: there was a certain rich man, who left in his sight, a steward over the rich man's goods | — sight, speech, life, hearing, soul, mind, reason, sense — all to manage; and the man began, the steward, this rich man's sight, speech, life, hearing, soul, mind, reason,

  1  here_begins this holy_gospel
  2  write holy-Luke
  3  inside six chapter of-write
  4  time say Lord-Jézus
  5  disciple^ of-Lord and Jew
  6  people exist one rich-~somebody who leave-from-rich-see
  7  steward^ on-of-Lord-rich-somebody | rich-see-say-living-hear
  8  soul-exist-exist-chapter-reason-sense every manage
  9  and begin-somebody-manager this rich of-Lord-rich-somebody
 10  see-say-living-hear-soul-exist-exist-chapter-reason

## 167v — the same was accused unto him

> sense to manage; and then he began, the man, and then a man came to accuse one servant before the steward; the man's lord spoke to the servant, this serving angel: all of the rich man's | […] soul, mind, reason, sense [give an account] sense, the word, he scattered; be humble, this rich Lord God | this rich man. The man, and then, to the account: therefore many of the rich man's, the steward; and he heard this, the steward, this said from the steward's rich lord […] and | sorrowing

  1  sense manage and then-exist SUBJ ~begin man* and then
  2  man^ exist accuse one servant before
  3  of-manager somebody-Lord say-~servant this angel-servant
  4  every of-Lord-rich-somebody | [?]-soul.
  5  exist-exist-chapter-reason-sense [give_an_account] sense
  6  word scatter humble this rich-rich-Lord_God | this-rich.
  7  man^ and_then to-?the_account many ~exist of-Lord-rich-somebody
  8  steward^ and hear this steward^ this say from
  9  of-manager Lord-rich-somebody [put_out] and | sad

## 168r — what shall I do?

> the steward, the steward left off; and then this steward, the weeping steward [dig] and [I am not able] [to beg] and […] [I am ashamed] the steward [thought]; and he found one accusation against the steward, and then this steward had two debtors | of the steward, a man of mercy and of alms; and | then there was, among the steward's, this one debtor of mercy; and this said, the steward: how much mercy dost thou owe the steward? [my lord] And then the debtor of mercy: a hundred measures of oil. And then this steward sat him down, the man of mercy,

  1  steward^ leave-manager and_then this steward^ crying-manager
  2  [dig] and [I_am_not_able] [to_beg] and °try-°pray_thee [I_am_ashamed]
  3  steward^ [thought] and one one-?heavenly-~year find-manager
  4  and then-exist have this steward^ two debtor^ | of
  5  steward^ man* find_mercy^ and alms and | then
  6  exist among-manager this one debtor^ find_mercy^ and say this
  7  steward^ how_much? find_mercy^ debtor^ of-manager [my_lord]
  8  and_then debtor^ have_mercy-somebody hundred* measure
  9  oil and_then this steward^ sit-have_mercy-somebody

## 168v — sit down quickly, and write fifty

> to write down fifty, in turn fifty | mercy, the man, down [another] this, and this [thy bill] of the steward's rich Lord God; and then these two, the steward | mercy, the man [a hundred] [quarters of wheat] divided into two parts, the steward of mercy, and among these, the steward, these two debtors | alms, the man; and this said, the steward: how much alms dost thou owe, to the steward's rich lord? And then the debtor of alms: a hundred measures of wheat. And then this steward | sat the man of alms down, to write down | from five,

  1  to-down and write fifty in_turn five-rich-ten | have_mercy
  2  somebody to-down [another] this and this [thy_bill] of-manager
  3  Lord_God-rich-somebody and_then this two steward^ | have_mercy
  4  somebody [a_hundred] [quarters_of_wheat] divide-two-manager-have_mercy-somebody
  5  ~and among this steward^ this two indebted | alms
  6  somebody and say this steward^ how_much? alms indebted
  7  of-manager Lord-rich-somebody and_then indebted alms
  8  hundred* food wheat and_then this steward^ | sit
  9  alms-somebody to-down and write from | five

## 169r — the lord commended the unjust steward

> thirty, in turn twenty, the man of alms, down [another] this, and these two [eighty] [thy bill] of the steward's rich Lord God; and in turn unjust steward he took, this, the steward's rich Lord God, because the steward was found accused; and then this steward, these two, the steward's men of alms […] […] | divided, the steward's two men of alms. And then the Lord Jesus: O, of the Lord, son; have, apostles, truly: the steward was have, apostles, found accused, because the Lord, this Lord, this rich Lord God, the man; the Lord took to you many riches,

  1  thirty in_turn two-ten-rich alms-somebody to-down [another]
  2  this and this two [eighty] [thy_bill] of-manager Lord_God-rich-somebody
  3  in_turn [unjust_steward] take^ this of-manager Lord_God-rich-somebody
  4  because steward^ one-?heavenly-~year find and_then this steward^
  5  this two-manager-alms-somebody [a_hundred] [quarters_of_wheat] | divide
  6  two-manager-alms-somebody and_then Lord-Jézus
  7  oh of-Lord son have-apostle righteous steward^ exist
  8  have-apostle one-?heavenly-~year find because-Lord this-Lord this
  9  rich-Lord_God-somebody grab-Lord you greatly^ rich

## 169v — the goods are the senses

> the Lord took to you sight, the Lord took to you speech, the Lord took to you life, the Lord took to you hearing, the Lord took to you soul, the Lord took | is he yours? The mind the Lord took to you, reason the Lord took to you, sense the Lord took. To you, all of the rich Lord God's | sight, speech, life, hearing, soul, mind, reason, sense; and the apostles and the Jews are, truly, stewards over | sight, speech, life, hearing, soul, mind, reason, sense, in turn, in this world; the rich man has these apostles and Jews found accused.

  1  grab-Lord you see grab-Lord you
  2  say grab-Lord you living grab-Lord you
  3  hear grab-Lord you soul grab-Lord | ~you
  4  yours exist-exist-chapter grab-Lord you reason
  5  grab-Lord you sense grab-Lord.
  6  you every of-Lord_God-rich-somebody | rich-see-say.
  7  living-hear-soul-exist-exist-chapter-reason-sense
  8  and exist-apostle-Jew righteous manager inside | rich-see-say
  9  living-hear-soul-exist-exist-chapter-reason-sense
 10  in_turn inside this world* rich have this-apostle-Jew one-?heavenly-~year find

## 170r — the account, and a new gospel begins

> Here ends this holy gospel, spoken by holy Luke. Have | this: the apostles, the Jews, the man, truly, are stewards of the man's father, the son; and among them the man has the son. He is found accused, because then the dead man is accused; the man is quieted; accused. Here ends this holy gospel. To the apostles, the Lord God, with all thy heart; the Lord God have mercy. This holy gospel begins, written by holy Matthew in the fifth chapter | of the writing; by holy Luke in the | twenty- second chapter; the holy chapter of Jerusalem, in the ninth chapter: the time, then, the Lord Jesus, in

  1  here_ends this holy_gospel speak holy-Luke have | this
  2  apostle-Jew-somebody righteous steward^ of-somebody father
  3  son and among somebody son have somebody.
  4  one-?heavenly-~year find because then-chapter die-somebody exist
  5  one-?heavenly-~year somebody grow_calm one-?heavenly-~year side^
  6  this holy-gospel on-apostle Lord_God be_loved Lord_God SUBJ-have_mercy
  7  here_begins this holy_gospel write
  8  holy-Matthew within^ five chapter | of
  9  write holy-Luke within^ | two-two
 10  two-two chapter holy-chapter-+one-Jerusalem within^ nine chapter
 11  time then-exist Lord-Jézus within^

## 170v — can the children of the bridegroom mourn?

> his thirtieth year; the time the Lord Jesus went into the temple at Jerusalem, and | then he was in the temple; the Lord Jesus went, and the Lord saw the son, much joy and much sorrow; and from afar off were the apostles of holy John the Baptist; and then the Lord Jesus left off; and then the apostles answered: the apostles fast, and the Pharisees fast; in turn, the Lord's apostles — why do thy apostles not fast? And then the Lord Jesus to the apostles: | in joy, in turn; then the apostles go in joy, keeping watch, while the apostles are two years; thus the apostles leave the Lord Jesus, from the chief man; and then the apostle Jairus: Jairus's daughter is dead; to the high priest, this one who answered; and he took this chief man.

  1  thirty years* time go Lord-Jézus inside Jerusalem temple and | then
  2  exist inside temple go Lord-Jézus and see-Lord who* many joy
  3  and many sad and from-to-far exist apostle holy-John
  4  ~baptize the_Baptist/woman and then-exist leave^ Lord-Jézus and_then apostle
  5  answered apostle fast-apostle and Pharisee fast in_turn of-Lord apostle
  6  ~exist fast-apostle and_then Lord-Jézus to apostle | on
  7  joy in_turn then-exist go apostle on-joy observe exist
  8  apostle two-year ~on-that_is leave^ apostle Lord-Jézus from head
  9  and_then apostle Jairus of-Jairus daughter SUBJ die to-high_priest
 10  this ~exist-who answered and take^ this head.

## 171r — the woman who touched the hem

> The Lord Jesus; and the Lord Jesus went with the chief man to this chief man's house; and this one went, the Lord, and many people; and there was among this people one woman, a chief woman, which chief woman had been twelve years in an issue of blood; and then this woman, the chief, then this woman: how shall we touch the woman? Why in turn? Of the Lord she believed: the hem — this woman, the woman's healing, the woman left off; and then she touched, believing, the Lord Jesus, | within the hour the woman was healed, the woman left off; and the Lord Jesus saw upon the people; the Lord's hand; there were many people; and then the Lord Jesus, this

  1  Lord-Jézus and go-Lord-head-Jézus this head
  2  house and go this-who Lord many people and exist
  3  among this people one woman = which
  4  woman = exist nine-year-six-six-year inside blood from-donkey
  5  and_then this woman = then-exist this-woman
  6  how_shall_we* touch of-woman why?-in_turn of-Lord believe-exist
  7  hem this-woman healing-woman leave-woman and
  8  then-exist touch believe-exist Lord-Jézus | inside
  9  hour healing-woman leave-woman and see Lord-Jézus
 10  on-people hand-Lord ~exist many people and_then Lord-Jézus this

## 171v — thy faith hath made thee whole

> woman: the woman's faith healed the woman. Afterward, which day the Lord Jesus said, this Lord, to this woman, the Lord healed her; but the Lord Jesus said to this woman: the woman's faith hath healing done. And | the Lord went, the chief man, the apostles, Jesus, the woman; this chief man's house said, and | then the Lord, the chief man […] Jesus, the woman, going in; and he saw, the Lord Jesus, much sorrow; and then the Lord Jesus [give place] therefore: this daughter is not a dead daughter, but rather the daughter sleeps. And then they laughed, said the Lord Jesus; and then he said: see, love | this

  1  woman of-woman believe healing-woman ~do
  2  who-~year say Lord-Jézus this-Lord this-woman heal-Lord but
  3  say Lord-Jézus this-woman of-woman believe healing
  4  do and | go-Lord-head-apostle-Jézus-woman
  5  say this head house and | then-exist-Lord
  6  ~head-[?]-Jézus-woman-+say inside-go and see
  7  Lord-Jézus many sad and_then Lord-Jézus [give_place]
  8  ~exist this daughter die-daughter but_rather to-sleep-daughter and then-exist
  9  say laugh Lord-Jézus and_then say see love | this

## 172r — damsel, arise

> the Lord [laughed him to scorn] spoke; and then the Lord Jesus, this chief man, cast this people out; and then, having cast out, the chief man, and with the Lord Jesus the daughter's father and mother; and then the Lord Jesus to the sky said, said, named this: servant, arise, servant daughter, among maidens; and | then the daughter stood up and sat; and then, lo, the Lord went, his descendant, to the pleasing of the Lord, the prophet foretold through; lo, the Lord went; and then the Lord Jesus had the father and mother bring wine and bread [walked] [give her to eat] and drink; and then the daughter

  1  Lord [laughed_him_to_scorn] speak and_then Lord-Jézus this head.
  2  cast_out this people out and then-exist out cast_out
  3  head and among Lord-Jézus of-daughter father
  4  and mother and_then Lord-Jézus sky say say name-this
  5  one-+servant rise servant daughter among virgin-girl and | then
  6  exist rise^ daughter on-sit and_then lo go-Lord
  7  descendant to-pleasing-Lord prophet through predict lo go-Lord
  8  and_then Lord-Jézus carry father mother wine and bread
  9  [walked] [give_her_to_eat] and drink and then-exist daughter

## 172v — the fame of it went abroad, and the talents begin

> drank; and the daughter […]; and then the Lord Jesus, this month, [the fame] therefore said; and the news went out into all the sky and earth. Here ends this holy gospel. The Lord God, with all thy heart. This holy gospel begins, written by holy Stephen the king; this word, written, the chief; this world, the Lord, the priest; and the high Magdalene day, the king, all the Lord […]; and the farm, the people; this word he speaks, from the king; there was a rich lord going a long way; and | then the Lord had three living servants; and then the servants

  1  drink and ~eat-daughter and_then Lord-Jézus this moon
  2  [the_fame] ~exist say ~and news ascension^ every sky
  3  earth here_ends this holy_gospel Lord_God be_loved
  4  here_begins this holy_gospel.
  5  write holy-Stephen kingdom^
  6  this word write head
  7  this world* Lord priest.
  8  and high-Magdalene-~year kingdom^ every
  9  Lord ~baptize and farm people this word speak-~king exist
 10  go-Lord one rich Lord long way and | then
 11  exist have-Lord three living-servant and then-exist living-servant

## 173r — one talent, three talents, five talents

> before the Lord; he was with the Lord; and then the Lord took one servant, one talent of gold; and in turn the Lord took three talents of gold; the third the Lord took, five talents of gold; and then this rich lord, all, until this [gave]: five senses, mercy, prayer, alms, faith [ability]; the servant's mouth, this Lord went to […]; be saved, how shall we, living servant; and the Lord took the priest, the high Magdalene day, the king, the Lord, to […], the farm, the people, the man, soul, soul, soul, soul. Here ends this holy gospel. The Lord's love.

  1  SUBJ before Lord exist ~among-Lord and then-exist grab-Lord
  2  one servant one gold* talent in_turn-two
  3  grab-Lord three gold* talent third grab-Lord
  4  five gold* talent and_then this rich-Lord every until
  5  this [gave] five sense find_mercy^ pray.
  6  alms believe [ability] servant mouth
  7  this-Lord go ~baptize be_saved how_shall_we* living-servant and Lord grab priest
  8  high-Magdalene-~year kingdom^ Lord ~baptize farm people man^
  9  soul soul soul soul here_ends this holy_gospel the_Lord love

## 173v — after a long time the lord came

> Many years passed; then this rich lord returned | to the lodging, because from the lodging the way of the people lay into the house of this rich lord; and from the people, the servant carried this rich lord; and then he went out | among the Lord's, this rich man and the Lord's living servants, the apostles, the angels; and then he did so among this rich lord's; the Lord's servant, before the rich lord […] the three servants stood; the Lord took | of the rich Lord; and then this rich lord, this one to whom the Lord had given five talents of gold — and then this rich lord reckoned with the servant: how shall the man

  1  many year exist then-exist return this rich-Lord | on
  2  lodging because from* lodging way people inside house this
  3  rich-Lord and from people servant bring^ this rich-Lord and
  4  then-exist go out on | among-Lord this rich
  5  and of-Lord living-servant-apostle-angel and then-exist do
  6  among this rich-Lord of-Lord servant before rich-Lord
  7  [after_a_long_time] three SUBJ servant exist-Lord grab-Lord | of
  8  Lord rich and_then this rich-Lord this one to_whom
  9  SUBJ exist-Lord grab-Lord five gold.*
 10  talent and_then this rich-Lord reckon_with* servant how_shall_we-somebody

## 174r — well done, good and faithful servant

> of the rich Lord? This servant said: how shall the man be pleasing to the Lord God? And he received the aforesaid five talents of gold; and then this rich lord: go, servant, into the Lord's house, to the Lord's Father, and to the Father; the man shall be a man of joy. Chapter. Chapter. Amen. And then, among the Lord's, this second, to whom the Lord had given three talents of gold; and then this rich lord reckoned with the servant: how shall the man | of the rich Lord? This servant said: how shall the man be pleasing to the Lord God? And he received the aforesaid three talents of gold; and then this rich lord:

  1  of-Lord rich say this servant how_shall_we-somebody to-pleasing Lord_God and
  2  receive* five gold* aforesaid talent and_then this rich Lord
  3  go-servant inside of-Lord to-house to-of-Lord from-God_the_Father and
  4  to-God_the_Father somebody exist joy-somebody chapter-oh
  5  chapter-oh amen and then-exist among-Lord this two
  6  to_whom SUBJ exist-Lord ~grab-Lord three gold* talent
  7  and_then this rich-Lord reckon_with* servant how_shall_we-somebody | of
  8  Lord rich say this servant how_shall_we-somebody to-pleasing Lord_God
  9  and receive* three gold* aforesaid talent and_then this rich Lord

## 174v — the third servant

> go, servant, into the Lord's house, to the Lord's Father, and | to the Father; the man shall be in joy. Chapter. Chapter. Amen. And then, among the Lord's, this third, to whom the Lord had given one talent of gold; and then this rich lord reckoned with the servant: how shall the man? Of the rich Lord, this servant said [hard] servant [thou reapest] [where] [thou hast not sown] [gatherest] there is love, there is riches [ability] servant, because this Lord [afraid] the servant has, because then this servant of the rich Lord lost the servant; this Lord is [hid in the earth]

  1  go servant inside of-Lord to-house to-of-Lord from-God_the_Father and | to
  2  God_the_Father man^ exist ~joy chapter-oh chapter-oh
  3  amen and then-exist among-Lord this three to_whom SUBJ
  4  exist-Lord grab-Lord one gold* talent
  5  and_then this rich Lord reckon_with* servant how_shall_we-somebody
  6  of-Lord rich say this servant [hard] servant [thou_reapest]
  7  [where] [thou_hast_not_sown] [gatherest] love-exist exist-rich [ability] servant
  8  because this-Lord [afraid] have servant because then-exist this-servant
  9  of-Lord rich lose ~servant this-Lord exist [hid_in_the_earth]

## 175r — take the talent from him

> upon the servant; the rich man has this Lord, and from extortion upon the servant he took; because this rich Lord God […] […] | […] said, the man; and he said; and then this rich lord: this unprofitable servant, high, this servant, this | servant's love is this: the eye sees the servant, the Lord's house is far off, this | love is: go, servant, into the Lord's house. And then this rich Lord's servant, the angel, took from this unprofitable servant this one talent; and the angel took the talent from him and gave it to the faithful servant, the servant who has ten talents. Here ends this holy gospel.

  1  on-~servant rich have this-Lord and from [extort] on-~servant
  2  grab because this-rich Lord_God [take_away] [talent] | [?]-+say
  3  man* and say and_then this-rich-Lord
  4  this unhelpful servant high this-servant this | ~servant-love
  5  exist this eye seem^ servant of-Lord to-house long this | love
  6  exist go-~servant inside of-Lord to-house and_then this rich
  7  of-Lord ~servant grab angel from this unhelpful ~servant
  8  this one talent and talent grab angel from
  9  believe ~servant servant talent ten have here_ends this holy_gospel

## 175v — the Lord goes from town to town

> This holy gospel begins, written by holy Luke in the sixth chapter of the writing: the time, then, the Lord Jesus, in his thirtieth year; the time the Lord Jesus went among the people, and the Lord's apostles, from town to town, town; from temple to temple, temple; from village to village, village; and the Lord's apostles; and they went

  1  here_begins this holy_gospel write holy-Luke
  2  inside six chapter of-write time
  3  then-exist Lord-Jézus inside thirty years*
  4  time go Lord-Jézus among_the_people* and of-Lord apostle from town
  5  from_town_to_town* town from temple from_town_to_town* temple from
  6  village from_town_to_town* village and of-Lord apostle and go

## 176r — the woman of Samaria at the well

> the Lord Jesus, to one well; and the Lord Jesus sat by this well, because there was [afraid]; the Lord was wearied; in turn the apostles went, the apostles, into the village for bread, and the living brethren, the mind, living; and then there came one chief woman | to this well; and then she dipped […] this well; and then the Lord Jesus was thirsty, and […] the Lord asked her for water; and then this woman of an alien nation: how is it, this Lord | dares, the Lord, to ask water of a pagan? This woman of an alien nation in turn: | this Lord is a Jew; she dipped for the Lord [give me] to drink, the Lord, and

  1  Lord-Jézus one well and sit Lord-Jézus to-this
  2  well because exist [afraid] tire-Lord in_turn disciple^ go-apostle
  3  inside village on-~bread ~and living ~if exist-exist-chapter
  4  living and then-exist go one woman = | to
  5  this well and then-exist dip-~woman this well and_then
  6  Lord-Jézus thirsty-Lord and [?]-~woman-+SUBJ exist-Lord water
  7  ~ask and_then this heathen how? this-Lord | dare
  8  Lord from pagan water ~ask this heathen in_turn | this
  9  Lord Jew dip-+the_Lord [give_me] on-drink Lord and

## 176v — the Lord begins to speak to the Gentiles

> he began to speak through the pagan, the Lord Jesus; and the woman of an alien nation | judged this; she had, to the pagan man; and of an alien nation the Lord began | to speak this: lift up, woman of an alien nation, do at home likewise, | do, pagan; she left off, the woman of an alien nation; and then this woman of an alien nation | upon the alien nation […] which; and from [five husbands] this Lord, this Lord's descendant, the Lord, to the pleasing of the Lord, the prophet foretold; and the apostles went to the Lord, and the apostles began; the miracle upon the Lord; the Lord's love; the Lord spoke this | one baptism, two baptisms, the chief; and this woman of an alien nation believed in the Lord Jesus; and the woman of an alien nation went to her own | […] from

  1  begin through talk^ pagan Lord-Jézus and heathen-+SUBJ | ~judge
  2  this ~have to-+pagan man and heathen begin-Lord | say
  3  this-raise heathen place^ do ~if | do
  4  pagan from-leave of-heathen and_then this heathen | on-of
  5  heathen °many-to which and from [five_husbands] this-Lord this-Lord descendant
  6  husband^ to-pleasing-Lord prophet predict and go disciple^ to-Lord
  7  and begin-apostle wonder^ on-Lord love-Lord speak-Lord this | ~woman
  8  one-~woman head and believe this heathen inside
  9  Lord-Jézus and go heathen to-of-heathen | [?]-from

## 177r — come, see a man who told me all things

> […] and then she went into the village, and the woman of an alien nation began to speak | this: this people, sit; one Lord at the well, and even more from the Lord, to the pleasing of the Lord, the prophet foretold through; because the alien woman's home he did; the love of the alien woman he did; the alien woman left off, the alien woman's all that she was and did […]; the alien woman said […]; and then this people believed in the Lord, the man, the people; and the people went to this well, because they would pray to the Lord; | then and the people were there, and the Lord preached one to two years.

  1  [the_woman] and then-exist go inside village and begin-heathen say | this
  2  this people sit one Lord to-well still_more from-Lord
  3  to-pleasing-Lord prophet through predict because of-heathen home
  4  do love-heathen do heathen from-leave
  5  of-heathen every ~do [all_things] heathen-+SUBJ say-[?] and
  6  then-exist this people inside Lord-somebody believe-people and
  7  go-people this well because-Lord want-people pray | then
  8  exist and people exist-Lord preach one to-two-year

## 177v — the gospel ends, and another begins

> and even more to the Lord Jesus; but the Lord went into Galilee, to the town. Here ends this holy gospel. The Lord God, with all thy heart. This holy gospel begins, written by holy Luke, in

  1  and still_more-to Lord-Jézus but to-go-Lord inside Galilee
  2  town here_ends this holy_gospel Lord_God be_loved.
  3  here_begins this holy_gospel
  4  write holy-Luke inside

## 178r — the ten lepers

> the fifth chapter of the writing: the time, then, the Lord Jesus, in his thirty- | first year; the time the Lord Jesus went into Jerusalem; and this one went, the Lord, and many people; and then the Lord Jesus went, the people, into the field, and there stood [stood] afar off ten leprous people; and the ten lepers began to cry out: son of David, king, have mercy — the ten lepers, son; and they cried to the Lord Jesus; go, ten lepers, and let the ten shew themselves to the priest; and the priest took the ten lepers, from all that was [shew yourselves] in the law of Moses; and then the ten lepers went | from

  1  five chapter of-write time then-exist Lord-Jézus inside thirty | one
  2  years* time go Lord-Jézus inside Jerusalem and go this-who Lord
  3  many people and then-exist go Lord-Jézus people on-~field-+one and
  4  leave stood away^ ten leper people and begin ten
  5  leper shout-to son David king have_mercy
  6  ten leper son and shout-to Lord-Jézus go ten
  7  ~leper and ten appear priest and
  8  priest grab ten leper from every-~exist [shew_yourselves]
  9  Moses law and then-exist go ten leper | from

## 178v — the priests dispute over them

> and they saw the lepers' minds; and then there were lepers, the mind, healing; and one Wednesday, ten […] [as they went] [were made clean]; and then the ten lepers went, the ten people, there to the chief men of the Jews, before the priest; and then the priests of the Jews: how are you people, ten | lepers? Chapter. Said [one of them] the lepers, from the people [went back] the lepers; the people were before the priest, among the priests, the Jews, the man; they cast the priest out; the Jews said to the priest; the Jews: who of you men is healed? | said the leper

  1  see of-leper exist-exist-chapter and then-exist exist
  2  leper exist-exist-chapter healing and one-+Wednesday ten how?-aforesaid-°alone
  3  [as_they_went] [were_made_clean] and then-exist ten leper go-ten-people-exist-to
  4  high_priest = before priest and_then
  5  priest Jew how? you people ten | leper
  6  chapter say [one_of_them] leper from-people [went_back] leper.
  7  people exist priest among priest Jew-somebody
  8  out cast_out priest Jew say priest.
  9  Jew who? you man^ heal | say-leper

## 179r — where are the nine?

> the ten people healed: son of David, king; said the chief men, the Jews, the priest [glorifying God]: you people, from the son have sinned; the Lord healed you; but you people were healed by Moses truly, because there is the word of the Old Testament, from the lepers; among the priests, the Jews, they cast them out, and then of the nine people a man believed the priests, the Jews; in turn the tenth man had faith, and returned back to the Lord Jesus; and the leper bowed down before the Lord's feet; and then the Lord's sister

  1  ten-people heal son David king say head
  2  Jew priest [glorifying_God] you people from son
  3  sin_against heal-Lord but you people-+SUBJ heal
  4  Moses righteous because-exist Old_Testament word from
  5  leper-+say among priest Jew out exorcise
  6  and then-exist from nine people somebody believe from priest
  7  Jew in_turn ten somebody faith* but return
  8  back against Lord-Jézus and bow leper
  9  before of-Lord foot and then-exist-Lord sister

## 179v — were not ten made clean?

> kissed, the tenth man, the Lord's feet; and the Lord was pleased, and the tenth man gave thanks; and then the Lord Jesus to the apostles | of the Lord, to all by name: and the people, were there not ten lepers? Which [were not ten] one, whosoever keeps the commandment; and whosoever keeps the commandment the Lord loves. And then the Lord Jesus to the apostles: of the Lord, good […] from | he is. Chapter. [so] the son, the man; there is the Lord; the alien nation's love. Here ends this holy gospel. The Lord God's love. Three things must be believed in the world: first, believe in the most high; and then the pagan day, and the Jews believe in this and this; believe, one man,

  1  kiss-ten-somebody of-Lord foot and Lord godfearing^
  2  and thanks grab-ten-somebody and_then Lord-Jézus apostle | of
  3  Lord name-every-to and people exist ten leper in_turn-+who
  4  SUBJ [were_not_ten] one ~somebody-commandment and ~somebody-commandment Lord love
  5  and_then Lord-Jézus apostle of-Lord good [the_nine] from | ~you-chapter
  6  [so] son somebody exist Lord heathen love end
  7  this holy-gospel Lord_God SUBJ love three believe have
  8  from world* first SUBJ believe above-high and °and_then-pagan-~year and Jew
  9  believe inside this-and-this believe one somebody

## 180r — one faith, one Church

> and the Jews, the pagan day, the most high; in turn, therefore, to be saved; and a man, therefore, believes, the man, in the Lord Jesus Christ; one man, therefore, is saved; but every man is damned; and secondly, believe the Church; and the Church's belief is good, because there is one Church; the Church, and in believing is salvation, because from the Church, the Church, one way, belief, the Church, the Church, in the Lord Jesus Christ, in his coming and in his death; then on the cross the Lord gave up the ghost; thirdly, believe in the coming of the Lord Christ; and through him escape.

  1  and Jew-pagan-~year above-high in_turn ~exist be_saved and somebody
  2  ~exist believe somebody inside Lord-Jézus-Christ one
  3  somebody ~exist be_saved but everybody = be_damned in_turn-two SUBJ
  4  believe church and church believe this_is good
  5  because one church church and inside believe be_saved
  6  because from church church one ways* believe
  7  church church inside Lord-Jézus-Christ inside ~be_born and inside
  8  die then-+SUBJ on_the_cross of-Lord soul give_up_the_ghost third
  9  SUBJ believe on-~be_born Lord-Christ and through escape

## 180v — a summary of the Lord's life

> The Lord Jesus, and the Lord Christ made ready the twelve apostles; and many wearied, the Lord Christ, who wearied; the Lord did it; he went into the world | of the Lord, the apostles; and many a miracle the Lord Christ, in love, did | upon the world; the Lord's apostles went; the blind of eye he gave light; the dead man he stood up and raised; the evil upon the people […] the Lord | love, and this and this; the cup […] that day; the Lord healed; and the holy host, the mind, the Lord Christ, the brethren; the Lord at thirty stayed, the Lord, within the host; and the Lord Christ was humble, because the Lord was humble in this world. The chief men took the Lord, and the Jews captured him [led away]

  1  Lord-Jézus and prepare Lord-Christ six-six apostle and many tire
  2  Lord-Christ who tire-+SUBJ do-Lord into_the_world* go-Lord | of
  3  Lord apostle and many miracle Lord-Christ love miracle-+SUBJ do | on
  4  world go of-Lord apostle eye-blind SUBJ through light Lord die somebody
  5  SUBJ stand_up resurrect-chapter-Lord evil SUBJ on-people ~before-to-+who-Lord | love-and
  6  this-and-this cup-[?]-~year heal-Lord and holy-+host God exist-exist-chapter
  7  Lord-Christ ~if Lord on-thirty stay-Lord inside host
  8  and humble Lord-Christ because-+the_Lord exist-Lord humble-Lord this world.*
  9  head grab-Lord and Jew SUBJ capture [led_away]

## 181r — Thomas was not with them

> […] and a crown of thorns upon his head | conceived, he said; and [trodden down] the Lord Christ died, and the Lord Christ rose, and the Lord Christ appeared to the Lord's apostles, one Saturday evening; and this evening it was; then the Lord appeared to the twelve apostles in the Lord's house, where the Lord God, the Lord Jesus, had made the supper; and | then holy Thomas came Didymus one Saturday evening to the apostles; and the apostles said: Thomas, the apostles have seen the Lord. And holy Thomas said, this Thomas: this I will not believe, all this, to whom | this; Thomas, this belief is blind [unless] unless Thomas sees

  1  [they_platted] and thorn crown on-head | conceive
  2  say and [trodden_down] die Lord-Christ and rise Lord-Christ and appear
  3  Lord-Christ disciple^ of-Lord one Saturday evening and this
  4  evening exist then-exist-Lord appear-Lord six-six disciple^
  5  within^ Lord house where Lord_God Lord-Jézus dinner-to do and | then
  6  exist go holy-Thomas Didymus* one Saturday evening
  7  to-apostle and say disciple^ Thomas disciple^ see Lord and say holy-Thomas
  8  this-Thomas this not believe every this to_whom | this
  9  Thomas this believe ~blind-[?] [unless] see-Thomas

## 181v — blessed are they that have not seen

> the Lord's wounds, and unless Thomas puts his finger into the Lord's wounds, who from the Lord, from death, stood up. The time the Lord Jesus Christ came, into the midst of the apostles, the doors being shut, and said: peace be to you; and the judgment year; the apostles; in turn Thomas began to have, and said | the Lord Jesus: Thomas, come by name [hither] put thy finger into the Lord's wound [blessed] see and believe; and [have not] the Lord Jesus, the Lord's wound; and the Lord Jesus said: Thomas, happy art thou from this; and the man who sees that day, believing; but also | blessed is the day, and the food; he sees, from believing. Here ends this holy gospel.

  1  of-Lord side^ and of-Thomas finger not put within^ of-Lord
  2  side^ who from Lord from die stand_up time stand^ Lord-Jézus-Christ
  3  middle disciple^ closed and say peace^ you exist
  4  and judge-year disciple^ in_turn Thomas begin have and say | Lord
  5  Jézus Thomas go-+name [hither] put of-Thomas finger
  6  within^ of-Lord wound [blessed] see believe and [have_not]
  7  Lord-Jézus of-Lord wound and say Lord-Jézus Thomas happy-to
  8  from and somebody see [?]-~year ~believe but and | blessed
  9  ~year-to and food see from* believe here_ends this holy_gospel

## 182r — the appearance at table, and the sending out

> The Lord God, with all thy heart. And this [upbraided] the man said, the Lord Jesus [hardness of heart] the man, the Lord, therefore, within that day […] the man; and then, after the Lord Christ was executed, in the […] year, the time the apostles sat at table in Jerusalem, in the Lord's house, | at the place where the Lord God, the Lord Jesus, had made the supper; the time the Lord Jesus appeared to the Lord's apostles, in the mind, the man; and he sat with the apostles, outside, and began to upbraid them | for their belief; and the Lord Jesus said: go, apostles, | into the world; and be baptized in the Lord's […]

  1  Lord_God be_loved and this [upbraided] somebody say Lord-Jézus [hardness_of_heart]
  2  somebody Lord ~exist inside-~year-[?] somebody and then-exist
  3  on-execute Lord-Christ [?]-year inside
  4  time sit apostle to-table inside Jerusalem inside Lord house | to
  5  [where] Lord_God Lord-Jézus dinner do time
  6  appear Lord-Jézus apostle of-Lord inside exist-exist-chapter somebody
  7  and sit to-apostle to-~out and begin admonish | on
  8  believe and say Lord-Jézus you go-apostle | on
  9  world* and exist one-~woman the_Baptist/woman inside of-Lord exist-[?]

## 182v — baptize them in the name of the Father

> and let a man be baptized in the name of the Father and of the Son and of the Holy Spirit; and let him be to the Lord | to believe; every such man is saved, and one is damned [shall perish] [but]; and let a man be baptized and be the Lord's; one is saved, but every man is damned. Here ends this holy gospel. The Lord God's love. Written by holy Luke in the second chapter of the writing: the time, then, after the execution

  1  and somebody exist one-~woman the_Baptist/woman inside name God_the_Father
  2  and son and holy-spirit and exist Lord-to | to
  3  believe* everybody = be_saved and one
  4  be_damned [but] [-but] and somebody exist one-~woman the_Baptist/woman
  5  and exist Lord-to one be_saved but
  6  everybody = be_damned here_ends this holy_gospel Lord_God SUBJ
  7  love write holy-Luke inside two
  8  chapter of-write time
  9  then-exist on-execute

## 183r — Chosroes carries off the Cross

> of the Lord Christ, twenty-six days; the time of sitting at Jerusalem. One of an alien nation there was, a man of substance, whose name was Chosroes; and then he seized upon Jerusalem, the tree of the Cross — the tree upon which Christ was executed — and the tree he carried off into the town of Ctesiphon, into one tower; and then there was war many years upon the Roman emperor, whose name was Heraclius; and then war went, this, to the pagan emperor.

  1  Lord-~Christ two-ten-ten six-~year time to-sit Jerusalem.
  2  one to-heathen ~emperor name
  3  exist Chosroes and then-exist grab on-Jerusalem
  4  cross tree ~on tree exist Christ
  5  execute and tree SUBJ from-carry inside
  6  Ctesiphon town inside one tower
  7  and then-exist exist many year war* on-Roman.
  8  emperor name exist Heraclius
  9  and then-exist war* go this to-heathen emperor

## 183v — the sign given to Heraclius

> This Roman emperor then had two wars to fight, sinned against; and then Heraclius the emperor had a small army; and then he believed, as much as he could | from the Lord, giving thanks; the Lord God heard, the Lord God, the emperor's prayer; and God's angel cried out upon the water; Heraclius had it; the Lord God heard Heraclius's prayer; and then God's angel, Heraclius, the daughter, had him write upon his armour the tree of the Cross, and

  1  this Roman emperor then-exist have two war*
  2  on-fight sin_against and then-exist.
  3  little an_army have Heraclius emperor
  4  and then-exist believe on-~pray can | from-to
  5  Lord to-thanks Lord_God hear Lord_God of-~emperor.
  6  pray and shout-to God angel on-water
  7  have Heraclius hear Lord_God of-Heraclius
  8  pray and_then God angel Heraclius daughter
  9  have write on-arms cross tree and

## 184r — the battle, and the tower at Ctesiphon

> the emperor won the fight, because the pagan emperor lost, the emperor; and then the two left, this pagan emperor and this Roman emperor; and then the two did battle | upon the chapter, within, to the Lord, the two; and the pagan people [fought] the people among [into heaven] died; in turn the Jewish people; and the pagan, to many [the bridge]; and then the pagan people died, and they began to pierce [overcame] [baptized] upon the pagan earth; and then Heraclius went into the town of Ctesiphon, to the place of this pagan emperor Chosroes, because the emperor sat in one

  1  win emperor on-fight because lose to-heathen
  2  emperor and then-exist two leave this to-heathen emperor
  3  this Roman emperor and then-exist-two fight | on-chapter-+one
  4  inside-to-Lord-two ~and to-heathen people [fought] people among [one_another]
  5  die in_turn Jew people and to-heathen SUBJ to-many [the_bridge] and
  6  then-exist people to-heathen die and begin pierce [overcame]
  7  [baptized] on-to-heathen earth and then-exist go Heraclius
  8  inside Ctesiphon town on-place to-this to-heathen
  9  emperor Chosroes because sit emperor inside one

## 184v — the tower of gold and precious stones

> tower; and the tower was all of gold, and built of precious stone, the tower, as though for one God; the emperor sat within, because he had set himself, the emperor, in one way, the emperor; and the emperor was all of gold, shedding blood; and in the second way the emperor had set the tree of the Cross, he himself, upon the gold; and then the emperor [of silver] the water went up again upon the tower; and lo, the emperor took the rain, the emperor […] the emperor would take, and then the emperor made it within the tower, the day […] and to […] and […] and among the tree of the Cross

  1  tower and tower exist every golden and gem stone build tower
  2  how? one God inside-sit emperor because exist put
  3  emperor on-one ways* emperor and emperor exist every
  4  golden shed_blood in_turn-two ways* put emperor cross tree
  5  he_is* exist on-golden and then-exist emperor [of_silver]
  6  water ascend again* on-tower and lo rain grab
  7  emperor [?]-+SUBJ want emperor grab
  8  and then-exist emperor do inside tower.
  9  ~year-[?] and to-[?] and [precious_stones] and among cross tree

## 185r — Chosroes sits between the cross and the cock

> of gold, among the cross, among the cock, the emperor sat, as though one [a cock] from [the other side] the emperor, to God he said, from, because there is the whole world [worshipped as God] and then Heraclius the emperor went to this pagan emperor in the tower; and then Heraclius the emperor believed, Heraclius's God, in turn, the whole wide world; this […] the chief; he said he must die, this | there was the emperor [slew]; and they took the emperor by the head, and then Heraclius the emperor did all

  1  golden among cross among cock sit emperor
  2  how? one [a_cock] from [the_other_side] emperor
  3  to-God ~pray-+say from because-exist every world* [worshipped_as_God]
  4  and then-exist Heraclius emperor go this to-heathen
  5  emperor inside tower and_then Heraclius emperor
  6  believe of-Heraclius God in_turn all_the_world this
  7  Heraclius ~head die say this | ~exist
  8  emperor [slew] and emperor behead and
  9  then-exist do Heraclius emperor every

## 185v — the Cross comes back to Jerusalem

> [from the] the tower he pierced; and the tower, God, he took up, and […] […] the son | from one woman; and the son the emperor left [behind] and he took the tree of the Cross, and carried it off into the town of Jerusalem; and then […] before | the army, the army; and then arrived Jerusalem; and at the gate God's angel, the gate of Jerusalem; and the angel cried out to Heraclius: thus the Lord Christ did not carry the tree of the Cross out to Jerusalem in pride, but carried it in humility; and then he sat down [upon an ass]

  1  [from_the] tower on-+pierce ~and tower God up grab
  2  ~and [of_Chosroes] [emperor] son | from
  3  ~woman and son emperor leave [behind] and
  4  grab cross tree and SUBJ from-carry inside
  5  Jerusalem town and then-exist [came] before | army
  6  army and then-exist arrived Jerusalem and to-gate God
  7  angel ~gate Jerusalem ~and shout-to angel Heraclius
  8  this-this Lord-Christ proud out on-Jerusalem carry cross tree
  9  but humble carry and then-exist sit down [upon_an_ass]

## 186r — the emperor takes off his robes

> and took off from the emperor his clothes; and then [put off his shoes] and with bowed head carried the tree of the Cross into Jerusalem; and then, from the gate, God's angel, the gate of Jerusalem; and the emperor, many [his purple] loved, he said, the tree of the Cross; and the emperor put the cross within Jerusalem, in the temple; and the emperor gave thanks to the Lord, the Lord God, the whole wide world; and there is a man who takes the holy tree of the Cross, the tree; and [set up the] the tree of the Cross; and the tree of the Cross, two by two, through the law, upon all

  1  and take_off on-~emperor of clothes [and_then]
  2  [put_off_his_shoes] and bowed head carry cross tree inside
  3  Jerusalem and then-exist from-gate God angel ~gate Jerusalem
  4  and emperor many [his_purple] [?]-love-+say cross
  5  tree and cross SUBJ put emperor inside Jerusalem
  6  temple and ~pray-~emperor to-Lord thanks Lord_God
  7  the_whole wide world and exist somebody to grab holy-cross
  8  tree and [set_up_the] cross tree
  9  and cross tree two-from-from through law on-every

## 186v — the holy Cross against the evil

> the wide world; because this holy tree of the Cross, this cross, of a man's [healed] and of a man's [miracles]; and this holy tree of the Cross, this, of a man's [witness] against [these things]; and believe: the evil, the evil one, the Lord God, that is, against the evil one, the evil. On the Sunday the Lord God created from the world and

  1  all_the_world world because this holy-cross tree this cross SUBJ of-somebody
  2  [healed] and of-somebody [miracles] and this holy-cross tree this
  3  SUBJ of-somebody [witness] against [these_things] and believe
  4  devil = Lord_God that_is against devil =
  5  inside Sunday
  6  create Lord_God
  7  from world
  8  and

## 187r — the Red Sea

> the angel, in the eternal land; thus the Lord God, on the Sunday, led them through, through dry the Red Sea, by Moses and by Aaron, the Jewish people, from the land of Egypt, from Pharaoh king's earth; and then Moses and Aaron went to the Red Sea; and then God's angel: Moses, hold out this rod over the Red Sea; and then he held it out over the Red Sea; and then | the Red Sea, in the Lord's name, left apart in two ways; and then the people went through, said Moses, Aaron, the angel, through the Red Sea.

  1  angel inside heaven = on-that_is Lord_God inside Sunday
  2  through go-Lord through dry* the_Red_Sea on-+Moses
  3  and on-Aaron Jew people on-Egypt land^
  4  on-Pharaoh king land^ and then-exist Moses
  5  and Aaron to-+the_Red_Sea go and_then
  6  be_glorified^ angel Moses hold_out this stick on-+the_Red_Sea
  7  and then-exist hold_out on-+the_Red_Sea and then-exist | the_Red_Sea
  8  Lord-+name apart leave on-two ways* and then-exist through go people
  9  say Moses Aaron angel through the_Red_Sea

## 187v — Pharaoh in the midst of the sea

> The time Pharaoh the king went into the Red Sea, the king, Pharaoh's army; and then the king went | into the middle of the Red Sea; the time God's angel said: Moses, hold out this rod over the Red Sea; and then he held it out; the time the Red Sea closed in upon Pharaoh the king; and then went Moses and Aaron [stretched out]; thus the Lord God, on the Sunday […] from the people, who was the Lord's, going | upon [from heaven] the earth; the Lord God took the heavenly manna from the eternal land; and this manna, this, is this day's

  1  time Pharaoh king inside the_Red_Sea go-king
  2  of-Pharaoh an_army and then-exist go-king | on
  3  middle^ the_Red_Sea time say God angel Moses hold_out
  4  this stick on-+the_Red_Sea and then-exist hold_out time
  5  the_Red_Sea shut_in Pharaoh king and then-exist to-go
  6  Moses and Aaron [stretched_out] on-that_is Lord_God
  7  inside Sunday [stretched_out] from people who exist-Lord on-go-Lord | on
  8  [from_heaven] earth grab Lord_God heavenly manna
  9  from_heaven* land and this manna this SUBJ exist-today’s

## 188r — the manna and the bread of this day

> the angel; and this is this day's living, the people said | […] the year; and how at table they ate of it, they ate of it, they left off; and then this manna take a bucket; and he said [his purple] brought [a vessel] from the manna, thanks and pleasing he did; in turn [came] Christ stayed, that day's [put into it] manna; and then the Lord Jesus, in his thirty- third year, the time the Lord Jesus said, at the last supper, he took within, why in turn, one baked cake, and the Lord Jesus said: and let a man eat this day's bread; and the Lord

  1  angel and this exist-today’s living people-+say | [?]-[?]-+one
  2  year and how? table-+say eat on-+say from eat SUBJ leave
  3  and then-exist this manna take* bucket and
  4  say [his_purple] brought* [a_vessel] from manna glory^
  5  and godfearing^ do-+say in_turn [came] Christ stay daily
  6  [put_into_it] manna and then-exist Lord-Jézus inside thirty half*
  7  three_days time say Lord-Jézus at_the_Last_Supper = grab
  8  inside why?-in_turn one baked cake and
  9  say Lord-Jézus and man^ exist this exist-today’s eat and Lord

## 188v — he that believeth not

> believeth not: every such man is damned […]; and a man who is the Lord's believes; and there is a man who from the altar from the thirty, eats the holy host and drinks; he that believeth not, that man lives. Chapter. Chapter. Amen. On the Sunday from [the flesh of] Christ came into this world; and before the Lord Christ's coming, nine months and two Sundays; on the Sunday the Lord was announced, to the understanding, by the angel; in | not the Sunday, in the mind, the happy virgin Mary, and | […] [holy] Joseph; on the Sunday the Lord was

  1  not_believe everybody = be_damned cut_off-[?] and man^ exist Lord
  2  believe and exist man^ from altar exist
  3  from thirty holy-host eat and drink who_believes_not*
  4  man^ exist living chapter-oh chapter-oh amen
  5  to Sunday from [the_flesh_of] Christ on-this world ~be_born
  6  and before Lord-Christ ~be_born nine moon and two Sunday inside
  7  Sunday the_Lord exist announce on-understand-chapter angel inside | not
  8  ~Sunday inside exist-exist-chapter happy virgin-Mary and | [the_holy_Trinity]
  9  [holy] Joseph inside Sunday the_Lord exist

## 189r — what was done on the Sundays

> announced, this angel, to the understanding, the angel; and then the Lord | into this world came; and then the Lord, in his thirty-first day, the time, on a Sunday, the Lord Jesus Christ made at the wedding water into wine; on a Sunday the Lord stood up and raised | the Lord Jesus Christ, the daughter of one chief man in Jerusalem; on a Sunday the Lord […] upon Carmel, to the mount, and the Holy Spirit appeared in the shape of a dove; and then this Lord, of the son, he who quieted the spirit, and the Lord took the Holy Spirit; and the Lord went into the field

  1  announce this angel on-understand-chapter angel and then-exist-Lord | on
  2  this world* ~be_born and then-exist-Lord inside thirty one-~year
  3  time inside Sunday create on-wedding Lord-Jézus-Christ
  4  water wine inside Sunday the_Lord stand_up resurrect | Lord
  5  Jézus-Christ daughter first^ head inside Jerusalem inside Sunday
  6  the_Lord from-[?]-[?] on-Carmel to-mount and
  7  appear holy-spirit inside ~form dove and_then
  8  this-Lord of son he_who spirit grow_calm and
  9  Lord grab holy-spirit and Lord go inside field

## 189v — Nain, the blind man, the cleansing of the temple

> to […] the Lord Jesus, that day; on a Sunday the Lord stood up and raised, the Lord Jesus Christ, in the town of Nain, the son of one widow; and before that, he himself | was the Lord; this widow's son the Lord raised; one blind man he gave light; on a Sunday the Lord Jesus Christ by the wayside the town of Jericho; then the Lord went into Jerusalem, and the Lord's apostles; on a Sunday the Lord cast out, in Jerusalem, from one man, hell, the mind; then the Lord, in his thirty-third year, on a Sunday the Lord | broke

  1  to-[?] Lord-Jézus [?]-~year inside Sunday the_Lord
  2  stand_up resurrect Lord-Jézus-Christ inside Nain town son
  3  one virgin-[?] the_Baptist/woman and before that_is he_is* | exist
  4  Lord this virgin-[?] the_Baptist/woman son stand_up resurrect-Lord one
  5  ~blind through light inside Sunday Lord-Jézus-Christ by_the_wayside*
  6  Jericho town then-chapter and go-Lord inside Jerusalem and
  7  of-Lord apostle inside Sunday the_Lord ~exorcise-Lord inside Jerusalem
  8  on-one somebody hell exist-chapter then-exist-Lord
  9  inside thirty half three inside Sunday the_Lord | break

## 190r — the week of the Passion, day by day

> the Lord, five loaves of this day's bread, for five thousand people; then the Lord, in his thirty-third year, from Galilee through the Red Sea to one mount; on a Sunday the Lord went to suffer in Jerusalem; then the Lord, in his thirty- third year, on the Monday the Lord preached many a miracle; in turn on the Tuesday the Lord stood up and raised Lazarus from the tomb; in turn on the Wednesday the Lord — but Judas sold him for thirty pieces of silver; in turn the wounded one made the supper, and they captured the Lord; in turn on the Friday the cross […]; and the evil one was bound; in turn on the Saturday, hell

  1  Lord five baked exist-today’s five-?thousand people
  2  then-exist-Lord inside thirty half three_days from Galilee
  3  through the_Red_Sea to-one to-mount inside Sunday
  4  the_Lord exist go-Lord on-suffer inside Jerusalem then-exist-Lord inside thirty
  5  half three_days inside Monday the_Lord many miracle preach-Lord in_turn
  6  Tuesday the_Lord Lazarus on-tomb stand_up resurrect-Lord in_turn Wednesday
  7  Lord-~but-+SUBJ exist Judas sold to-thirty silver
  8  in_turn wound dinner-to do-Lord and capture-Lord in_turn
  9  Friday on_the_cross-[?] and evil bound_up in_turn inside Saturday hell

## 190v — the five appearances, and Emmaus

> the Lord destroyed; on the Sunday the Lord rose from the dead; and to the apostles the Lord appeared. First the Lord appeared in Bethany | to the virgin Mary; secondly the Lord appeared at the tomb to Mary Magdalene; thirdly the Lord appeared on the way […] the people to Jerusalem; fourthly the Lord appeared to two apostles; then the two apostles went, on the Sunday, out of Jerusalem, into one […]; and the name of that […] was Emmaus; in turn the apostles | and the names of that day were Luke and Cleopas; and there was […] one apostle; this day's bread, and nine, and water; the Lord Jesus blessed; on the Sunday the Lord appeared a fifth time, in Jerusalem, to the ten apostles | of

  1  SUBJ destroy-Lord inside Sunday the_Lord rise on-die and apostle the_Lord
  2  appear-Lord first the_Lord appear inside Bethany | virgin
  3  Mary in_turn-two the_Lord appear to-tomb Mary Magdalene third
  4  the_Lord appear on-way [?]-[?] people
  5  on-Jerusalem in_turn-two-two the_Lord appear two apostle then two
  6  apostle and go inside Sunday on-Jerusalem inside one in_turn-chapter-in_turn and
  7  ~brother-+name in_turn-chapter-in_turn exist Emmaus in_turn apostle | and-exist-chapter
  8  ~year-+name exist Luke and Cleopas and ~exist-[?] one
  9  apostle exist-today’s and grape and water bless Lord-Jézus
 10  inside Sunday the_Lord five appear inside Jerusalem ten apostle | of

## 191r — the Ascension, and the two men in white

> the Lord, the gate; and then, after the Lord Christ's execution, in the twelfth year, the time the Lord Jesus appeared, on a Sunday, in Jerusalem, to the Lord's twelve apostles, to the whole wide world, and to Thomas; and then, after the Lord Christ's execution, | in the twentieth […] year, the time the apostles sat at table in Jerusalem, in the Lord's house where the Lord God, the Lord Jesus, made the supper; the time there appeared two, from the execution of the Lord Christ, from town to town | […] the year; and he left, to the Lord's Father, to the eternal town; and there appeared two angels in white clothes, and then the two angels: you, apostles,

  1  Lord gate and then-exist on-execute Lord-Christ six-two-year time
  2  appear Lord-Jézus inside Sunday inside Jerusalem six-six apostle of-Lord
  3  to-all_the_world Thomas and then-exist on-execute Lord-Christ | one-ten-+one-ten
  4  [?]-year time sit apostle at_table inside Jerusalem inside Lord house
  5  where Lord_God Lord-Jézus dinner do time appear
  6  two-?from execute Lord-Christ from_town_to_town* | [?]-[?]
  7  year and to-leave to-of-Lord from-God_the_Father from_heaven* town-chapter-in_turn
  8  and two appear two angel-angel white clothes
  9  and_then two angel-angel you apostle-oh-DIV-chapter

## 191v — why stand you looking up to heaven?

> which and how? The Lord, joy, see […]; he left, into heaven | the town; this joy is to be, the Lord would [shall come] on the judgment year, to judge whosoever liveth and the dead; this word, from the Lord, the living Lord; and in this world | the Lord went into heaven, in turn […] the Lord, with all thy heart, the Lord God, with all thy heart, pleasing and thanks. This holy gospel begins, written by holy Luke in the second chapter of the writing: the time, because the time the virgin Mary, at the coming of the Lord Jesus | […]

  1  what-+who how? Lord joy see [so_shall_he_come] leave-chapter-leave on-heaven | town
  2  exist-to this joy want-Lord [shall_come] on-+judge-year judge whosoever_liveth*
  3  and dead this word SUBJ from Lord living-Lord and on-this world* | from-go
  4  Lord on-heaven ~land Lord be_loved Lord_God be_loved pleasing and thanks
  5  here_begins this holy_gospel
  6  write holy-Luke
  7  within^ two chapter of-write
  8  time because time
  9  virgin-Mary on-~be_born
 10  Lord-Jézus | [?]-[?]

## 192r — Simeon in the temple

> the year; the time the virgin Mary carried, as a wife, in her lap, to the temple the Lord Jesus; because this girl would destroy — truly the Lord, but the girl would out [by the Spirit] the salvation of the Jews; and then the girl went to this temple; the time Simeon went into the temple, by the Holy Spirit, in mercy, and the virgin Mary appeared; and then Simeon, the virgin Mary, Simeon took this son, more than these, this son, Simeon; [into his arms] he carried the son within, Simeon, why in turn; and Simeon knelt down before the Lord Jesus, and asked the Lord for mercy; and then Simeon: Lord, dismiss thy servant in peace.

  1  year time carry wife virgin-Mary inside öl who temple
  2  Lord-Jézus because which this-girl destroy righteous Lord ~but want-girl
  3  out [by_the_Spirit] from-salvation Jew and then-exist girl go this temple
  4  time go Simeon inside temple on-holy-spirit find_mercy^
  5  and come^ virgin-Mary and_then Simeon virgin-Mary
  6  grab-Simeon this son more_than_these* this son Simeon
  7  [into_his_arms] son carry inside of-Simeon why?-in_turn and kneel
  8  Simeon before Lord-Jézus and Lord find_mercy^ ~ask
  9  and_then Simeon Lord dismiss^ servant of-Lord peace SUBJ

## 192v — mine eyes have seen thy salvation

> Simeon: for which two reasons? Simeon's two eyes have seen salvation | of Simeon; and holy Simeon blessed the Lord Jesus; and Simeon's sin the Lord had mercy on; and the Lord took him in his lap, and the Lord carried him into the temple at Jerusalem; and then into the temple went the Lord, Simeon and Mary; and Simeon raised the Lord Jesus within, Simeon, why in turn; and then Simeon: lo, from the Lamb; and the Lord went upon heaven and earth, upon this world, the Lord Jesus Christ; and from the Lord, the cross; and upon the Lord there is blessing, all the wide world; and blessing there is; he left. Chapter.

  1  Simeon who-two-why? see two of-Simeon eye-eye be_saved | of
  2  Simeon and bless Lord-Jézus holy-Simeon and sin
  3  Simeon have_mercy-Lord and Lord take^ inside öl
  4  and Lord carry inside Jerusalem temple and then-exist inside temple
  5  go-Lord-Simeon-Mary and raise Simeon Lord-Jézus
  6  inside of-Simeon why?-in_turn and_then Simeon ~lo from
  7  lamb and the_Lord go-Lord on-heaven land
  8  on-this world* Lord-Jézus-Christ and from Lord on_the_cross-[?] and on-Lord exist
  9  bless every ~all_the_world world* and bless exist leave^ chapter-oh

## 193r — Simeon carries the news to the fathers in hell

> Chapter. Amen. Here ends this holy gospel. The Lord God's love. This, out of high Moses, truly, in one chapter, he who is written, written: holy Simeon, three days from going out of this world, said: Christ, the apostles of the Lord, announce; Simeon, in the netherworld, to the holy fathers, | at the coming of the Lord: and see, you are saved, and many in judgment who are in the netherworld, from the holy fathers and the holy prophets. Written; and from the holy gospel, that is […] the Lord, this Lord, the holy gospel: this Lord, the nine, upon the water created; this Lord gave light to the blind; this Lord cast the evil out of the people; this Lord the dead raised and resurrected; and this and that; the leper the Lord healed; this Lord, the cross, the holy gospel.

  1  chapter-oh amen here_ends this holy_gospel Lord_God SUBJ love this EOL
  2  out high-Moses righteous inside one chapter he_who* exist write write EOL
  3  holy-Simeon three_days on-this world from-go-Simeon say Christ apostle EOL
  4  of-Lord announce SUBJ Simeon inside netherworld holy-from-father | on-+EOL
  5  ~be_born of-Lord and see be_saved you and many EOL
  6  judge-+SUBJ exist inside netherworld from father-holy and prophet-holy. EOL
  7  write and from holy-gospel that_is [?]-°down Lord this-Lord holy-gospel EOL
  8  this-Lord grape on-water create this-Lord blind through light EOL
  9  this-Lord evil on-people exorcise this-Lord dead EOL
 10  rise* ~resurrect who-and-this-and leper heal-Lord this-Lord cross holy-gospel

## 193v — the call of Matthew at the receipt of custom

> This holy gospel begins, written by holy Matthew, in the […] chapter of the writing: the time, then, the Lord Jesus, in his thirtieth year, the time he preached in | there was […] and then the Lord Jesus preached in Capharnaum, and left off, down, from preaching; and many people made ready to him; and then the Lord went into the town, and saw, the Lord Jesus, holy Matthew sitting at the receipt of custom; and then the Lord Jesus

  1  here_begins this holy_gospel
  2  write holy-Matthew inside and
  3  chapter of-write time
  4  then-exist Lord-Jézus inside
  5  thirty years* time
  6  preach inside | ~exist
  7  °afterward-+one and then-exist from-preach Lord-Jézus inside Capharnaum
  8  and leave to-down on-preach and follow^ to-Lord
  9  many people and then-exist go-Lord on-town and see
 10  Lord-Jézus on-publican sit holy-Matthew and_then Lord-Jézus

## 194r — he sat at meat in the house

> Matthew went to the Lord, to the food, to the place; holy Matthew rose, and Matthew went to the Lord Jesus; and the Lord went with Matthew to holy Matthew's house, and he made, out of many, out of [sat at meat] — how? Holy Luke speaks: he made, out of many, out of […] [sat at meat] and there went to the Lord the Jews, the Pharisees, and the tax collectors, the chief men; and together with the Lord Jesus they drank and ate, the sinners; and the Jews began, the Pharisees, to speak to the Lord's apostles: this, you answered, the salvation of sinners? In turn, then, this Lord is

  1  Matthew go to-Lord on-food to-place rise holy-~Matthew and
  2  go-Matthew to-Lord-Jézus and go-Lord-Matthew holy-~Matthew house
  3  and do from-many-to from-~out company how?
  4  speak holy-Luke do from-many-to from-~out.
  5  company and go to-Lord Jew pharisee and
  6  publican exist head and together Lord-Jézus drink
  7  and eat sinners* and begin Jew.
  8  pharisee speak disciple^ of-Lord this you answered
  9  sinners* from-salvation in_turn then-exist this-Lord exist

## 194v — they that are well need not a physician

> and the Lord said: this Lord is sin, therefore the Lord's salvation; and the blind to the Lord Jesus [they that are well] humble; and then the Lord Jesus [a physician] to the Lord: this Lord went not to the righteous man in this world, but to the sinner; and then the Lord Jesus: you, righteous man; and then the Lord Jesus: the healthy man needs no recovery, but rather he needs one sin — this is recovery. Here ends this holy gospel, written by holy Matthew in the […] chapter. Holy Paul speaks and says: | the Lord Jesus Christ, from the beginning of the world, from the creating of Adam, | to [healeth] the coming of the Lord Jesus Christ into this world [sinners]

  1  and Lord say this-Lord exist sinner^ ~exist from-salvation-Lord and
  2  ~blind-to Lord-Jézus [they_that_are_well] humble and_then Lord-Jézus [answered]
  3  to-Lord this-Lord go-Lord to-just_man on-this world* but to-sin
  4  and_then Lord-Jézus you just_man and_then
  5  Lord-Jézus need the_healthy healing but_rather need.
  6  one-sin ~exist-this health^ here_ends this holy_gospel
  7  write holy-Matthew inside and chapter holy-Paul speak say | Lord
  8  Jézus-Christ from* ~begin-to world* from* ~Adam create | to
  9  [until] ~be_born Lord-Jézus-Christ on-this world [then]

## 195r — from Adam to the coming of Christ

> truly, the man; and one prophet, and one forefather, and one holy father, holy living; and one | […] the father […] in the eternal land; but rather, then, at the coming of Christ into this world, and then, in his thirtieth day, the time […] the Lord Jesus upon Carmel, the mount; and then out, in his thirty-third year, the time he was crucified, and on the third day stood up from the dead; and many holy prophets and holy forefathers and holy fathers, holy living, out of the netherworld | to the Lord went; and then, that day, the time he left

  1  righteous somebody and one prophet and one forefather
  2  and one holy-father holy-living and one | [prophet]
  3  father-[?]-[?]-[?] inside heaven =
  4  °but_rather-+one then ~be_born Christ on-this world* and then-exist inside
  5  thirty day time from-[?]-[?] Lord-Jézus on-Carmel
  6  mount and then-exist out thirty ~begin-+three_days time
  7  crucified and on_the_third_day from die stand_up and many holy-prophet
  8  and holy-forefather and holy-father holy-living on-netherworld out | to
  9  go-Lord and then-exist [?]-~year time to-leave

## 195v — he shall come to judge the quick and the dead

> to the Lord's Father, upon heaven and earth; | the Lord sits at the Father's right hand, at the food; the Lord shall go to judge the living and the dead; and before going away he blessed all the wide world. This holy gospel begins, written by holy Matthew | […] the twenty-second chapter of the writing: the time, then, | the Lord Jesus, in his thirty-third year, the time the Lord Jesus said to the apostles; they answered: who shall be to the Lord, this Lord, the greatest in the eternal

  1  to-of-Lord from-God_the_Father on-heaven kingdom^ | from-sit
  2  Lord from-God_the_Father on-right from-food have-Lord go-Lord judge
  3  living-somebody and die-somebody and before leave bless every all_the_world
  4  world here_begins this holy_gospel.
  5  write holy-Matthew | [sixteen]
  6  two-two chapter of-write.
  7  time then-exist | Lord
  8  Jézus thirty ~begin-+three time say disciple^ Lord-Jézus.
  9  answered who? exist to-Lord this-Lord on-many inside heaven*

## 196r — except you become as little children

> land? Because this is the apostles' — he himself, the Lord, was crucified and on the third day stood up from the dead; and the Lord to these apostles, to judge who shall be to the Lord, this Lord, greatest in the eternal land; and the Lord Jesus took among them one little son, and the son the Lord Jesus set upon the head, of the Lord, why in turn; and then the Lord Jesus: whosoever therefore is humble | as this little son, that one therefore is saved. The time the Jews brought one | before | the Lord Jesus, from this emperor, to whom, and he was a pagan.

  1  kingdom^ because ~exist-this disciple^ he_is* Lord crucified and
  2  on_the_third_day from die stand_up and Lord to-this disciple^ judge
  3  who exist to-Lord this-Lord on-many inside heaven =
  4  and call^ Lord-Jézus one little son.
  5  and son SUBJ put_on Lord-Jézus on-head.
  6  of-Lord why?-in_turn and_then Lord-Jézus who-~exist this humble | how?
  7  SUBJ this little son one ~exist be_saved
  8  time carry Jew one | before | Lord
  9  Jézus from* this emperor to-+who-to and exist pagan.

## 196v — the keys, and whatsoever thou shalt bind

> Because he heard from every man, upon one | before; this was: the Lord Jesus took the key of salvation, holy Peter; said | the Lord Jesus: whom this Peter loose in this world, from a man there is loose and from the eternal land; in turn whom this one loose in this world, from a man there is loose and from the eternal land. And then the Lord Jesus: he who among many, the Lord, you, from the Lord — every one a servant; and then the Lord Jesus: whosoever therefore this apostle, from this little son, does

  1  because hear from everybody = on-one | before this exist
  2  give^ Lord-Jézus key be_saved holy-Peter say | Lord
  3  Jézus who this-Peter loose* on-this world from
  4  man^ exist loose* and from_heaven* kingdom^
  5  in_turn who this-?with loose* on-this world from
  6  man^ exist loose* and from_heaven* kingdom^
  7  and_then Lord-Jézus he_who on-many Lord you from
  8  the_Lord every servant and_then Lord-Jézus who-~exist this
  9  disciple^ this from little son to* do

## 197r — their angels always see the face of my Father

> in the Lord's name, that one therefore is saved; and then the Lord Jesus taught the Lord's, therefore, apostles; and one [despise not] [little ones] did; and then the Lord Jesus to the apostles of the Lord: happy are the people, and the angels see the face of the Lord's Father; it is the will, from the people; and the angels look upon the face of the Lord's Father. Here ends this holy gospel. This holy gospel begins, written by holy Matthew: the time | the Lord Jesus said to the Lord's apostles, and to the Jewish

  1  inside of-Lord ~brother-+name and one ~exist be_saved
  2  and_then Lord-Jézus learn of-Lord ~exist apostle and one
  3  [despise_not] [little_ones] do and_then Lord-Jézus apostle
  4  of-Lord happy from people and angel see face
  5  of-Lord from-God_the_Father will from-people and angel on-see.
  6  face of-Lord from-God_the_Father here_ends this holy_gospel
  7  here_begins this holy_gospel write
  8  holy-Matthew time say | Lord
  9  Jézus apostle of-Lord and Jew

## 197v — take up his cross and follow me

> people; and the apostles, the man, the Jews: whosoever would come after the Lord, let him | deny himself, and all that is his, and take his own cross upon his own shoulder, and let the man go after the Lord; and then the Lord Jesus: who is this man […] and this world | rich […] then this man took his own soul | to riches […] and then the Lord Jesus: good is it that this man release | of the man's soul; damned, but saved, because many a man; and the man is [in exchange] [for his soul] [shall render] saved, every man damned [according to] [his works] the man is, from the judgment, said,

  1  people and apostle-somebody-Jew want what Lord go | deny
  2  man^ of-somebody all_the_world and grab of-somebody
  3  ~cross on-of-somebody shoulder and go-somebody what
  4  Lord and_then Lord-Jézus who this man^ profit and this world | rich
  5  [for_what] then this man^ SUBJ grab of-somebody soul | to-rich
  6  [for_what] and_then Lord-Jézus good SUBJ this man^ release* | of
  7  man^ soul be_damned ~but be_saved because many man^
  8  and man^ exist [in_exchange] [for_his_soul] [shall_render] be_saved-somebody every
  9  man^ be_damned [according_to] [his_works] man^ exist from-judge say

## 198r — go into all the world

> to damnation; every man saved. And then the Lord Jesus: you, therefore, go from town to town, this believing; who this Lord, you, preach the Lord, every one, from town to town, this [look upon] and see, go into this world, from prayer, the Son of God, in the mind of man, on the judgment year, every one, from town to town, this […] believe; and then the Lord Jesus […] Peter, one among you; and the apostles | see, the apostles, from prayer, the Son of God, within […] the man, and the apostles are within; the apostles believe. Here ends this holy gospel.

  1  on-be_damned everybody = be_saved and_then Lord-Jézus you
  2  ~exist-+say every from_town_to_town* this-believe-+say who
  3  this-Lord you preach-Lord every from_town_to_town*
  4  this [look_upon] see-+say go on-this world from pray
  5  son God inside exist-exist-chapter somebody on-judge-year every from_town_to_town*
  6  this-[?] believe and_then Lord-Jézus [answered_him]
  7  Peter one among you and apostle | see
  8  apostle from pray son God inside ~exist-[?] somebody
  9  and apostle exist inside son ~ask-apostle end
 10  this holy-gospel

## 198v — write your names in the eternal land

> Said the Lord God to the angel | of the Lord, holy […] the prophet, and | holy Elijah the prophet […] | said the apostles, the man, to the Lord, this Lord: thou creature, Lord, have mercy on sin [fruit] this is in the commandment, the man, that is; and the man who bears the commandment of God […] the sinful man is saved, to many | not, not, not. Chapter. Chapter. Amen. Written are the names of men in the eternal land, in the house; he dies, in turn | upon death, the mind and the soul. Chapter. Chapter. Amen.

  1  say SUBJ Lord_God on-angel | of
  2  Lord holy-NAME.prophet prophet and | holy
  3  Elijah prophet [was_taken_up] | say
  4  apostle-somebody to-Lord this-Lord.
  5  you [...] Lord sin have_mercy [fruit] this exist
  6  inside commandment somebody that_is and have somebody ~carry commandment
  7  God [...] sin somebody be_saved to-many | not-not
  8  not chapter-oh chapter-oh amen write SUBJ name
  9  of-somebody inside heaven = to-house die in_turn | on
 10  die exist-exist-chapter and soul chapter-oh chapter-oh amen

## 199r — a man had a vineyard and two sons

> This holy gospel begins, written by holy Matthew | in the twentieth, in the fifth chapter of the writing: the time, then, the Lord Jesus, in his thirty-third year, the time the Lord Jesus preached in Jerusalem; and the Lord Jesus said to the apostles of the Lord, and to the Jewish people: the kingdom of heaven left a man and earth; and then the Lord Jesus: there was [a vineyard] one rich man, a vineyard; and then he had

  1  here_begins this holy_gospel
  2  write holy-Matthew | one
  3  ten-+one-ten inside five chapter
  4  of-write time
  5  then-exist Lord-Jézus inside
  6  thirty ~begin-+three_days
  7  time preach Lord-Jézus inside Jerusalem and say Lord-Jézus apostle
  8  of-Lord and Jew people leave king man^ heaven
  9  land and_then Lord-Jézus exist [a_vineyard]
 10  first^ rich-somebody vineyard and then-exist have

## 199v — go work today in my vineyard

> two sons, to the pagan and the Jew; and then this rich man | of the Lord, the man, the son, said […] he brought the son into | the Lord's man's vineyard, the farm; he said, brought the son to this, go, and then this rich man […] the second, to the son, […] the man, into the rich man's vineyard, the farm; and then he said, said the priest, and […] […] the man; and said the Lord Jesus to the chief men of the Jews and to the Lord's apostles: judge, Lord, this Lord, you: which of these did good? Say. Said the chief men of the Jews: which did good? He who

  1  two son to-+pagan Jew and_then this rich-somebody | of
  2  Lord-somebody son on-+say [go_work_today] brought-son inside | of-Lord-from
  3  man vineyard vinedresser^ say brought-son to-this ~go-+say
  4  and_then this rich-somebody [?]-[?] two to-~son
  5  [?]-somebody inside of-Lord-somebody vineyard vinedresser^ °and_then-say-say
  6  priest* and [?]-[?] [?]-somebody and say
  7  Lord-Jézus high_priest = and apostle of-Lord judge-Lord
  8  this-Lord you who? SUBJ-this good say.
  9  say high_priest = who? SUBJ good say he_who

## 200r — he let out the vineyard to husbandmen

> said, to the pagan, the priest; and whosoever would be named, in turn went to the pagan; and then the Lord Jesus spoke truly; and secondly the Lord Jesus said a parable, and said: there was one rich lord who let out on lease the Lord's vineyard to husbandmen, the farm, the Lord's vineyard; and then the vineyard, many years he bore it, to take, to remit the vineyard's lease; and then this rich lord | of the Lord's servants, prophets and angels, the prophets and angels went, this lease from them to ask, the prophets and angels; and | the prophets and angels, the lease they would not take from them, but rather

  1  say-to-+pagan priest* and name-+who-want in_turn go-to-+pagan
  2  and_then Lord-Jézus righteous-+say speak and the_rest^ say Lord-Jézus
  3  parable say exist take^ one rich-Lord on-lease
  4  of-Lord vinedresser vinedresser^ of-Lord vineyard and then-exist
  5  vineyard-+say many year carry-+say to-+say take^ release^
  6  vineyard lease and_then this rich-Lord | of
  7  Lord servant prophet and angel go-prophet-angel this lease
  8  from* say ask-prophet-angel and | prophet
  9  angel lease to-+say grab-+say but_rather

## 200v — last of all he sent his son

> they all died; and the Lord's son went; this rich lord said to this son: they will have, they would say, the lease the Lord will take; and then the Lord was; they saw, and went; and the son they said; and then, thus: the son from [the heir] the vineyard […] the son […]; and this son is the vineyard's heir; and then they carried him off to die, they said; and sent saying to the Lord; and the son died, they said; and then it was, from town to town [killed him] and the Jews, the chief men: how? he said; spoke the Lord Jesus; and thirdly the Lord Jesus said a parable,

  1  every kill^ and go-Lord of-Lord son this rich-Lord say this son
  2  exist-+say have would_say* lease Lord take^
  3  and then-exist-Lord exist-+say see and go and son.
  4  say* and_then-+say this_is son from [the_heir]
  5  SUBJ vineyard [?]-~son [cast_him_out] and this
  6  son exist vineyard carry and_then-+say go-die
  7  say and [sent] to-Lord and son die-+say and
  8  then-exist exist from_town_to_town* [killed_him] and Jew ~head
  9  how? he_said* speak Lord-Jézus and three say Lord-Jézus parable

## 201r — the marriage of the king's son

> and said: there was one king in a land, and then he had one son; and the king would make a wedding; and then, among this king's, all the Lord king's, in turn […] to this wedding; and | then, therefore, not one went to this wedding; this king grew angry; and then, thus, the people; and he spoke, the people of the Lord, out, in turn, the whole wide world, to the supper; and then the Lord Jesus: what did this king? He said to the Lord's servants: all, from the town, destroy with fire and with water; and then this king

  1  say exist one king inside kingdom^ and then-exist
  2  have one son and son would_like^ king
  3  wedding pray and then-exist call^ this king
  4  every of-Lord king ~land on-this wedding and | then
  5  ~exist one go on-this wedding grow_angry this
  6  king and_then that_is people and speak people
  7  of-Lord out in_turn all_the_world dinner-to and_then Lord-Jézus who do
  8  this king say of-Lord servant every from town.
  9  destroy fire and* water and_then this king

## 201v — go out into the highways

> said to the Lord's servants: go, and speak this word, to the understanding, to the hidden; leave them behind, and let them be among those at this wedding; and then this Lord king's servants went, to the blind, to the hidden, and the way, and to the town; and they found the poor of God, […] blind, and even more […] and the hungry and the thirsty, and [feeble] the poor of God, and [go ye] [into the highways] the servants found; all the servants went, filled into the Lord king's house; and then, out of the house, this king, the various heaven

  1  of-Lord servant go and this word speak-understand-hide exist
  2  leave-to-leave and exist call^ on-this wedding and_then
  3  this Lord-king of-Lord servant go-~blind-hide and
  4  way and on-town and find
  5  poor_man_of_God = ninety-~exist blind and still_more-[?]-to and
  6  hunger and thirst and [feeble] poor_man_of_God = and
  7  [go_ye] [into_the_highways] find servant every go-servant
  8  filled* inside of-Lord-king house and then-exist out
  9  house this king various heaven

## 202r — the man without a wedding garment

> Lord; and this king said, this king; and the king went into the Lord king's house; the king would go before, out of the Lord king's house; and then this king went into the Lord king's house; and this king saw one man of God in ragged clothes; and thus the king said: this friend […] which man [the king came in] the man went [a wedding garment] the man, friend, the wedding clothes, by name, which this man

  1  Lord and say this king this-king and go-king inside
  2  of-Lord-king house want-king to-before on-~out
  3  of-Lord-king house and then-exist ~go this king
  4  inside of-Lord-king house and see this king
  5  one God-somebody ragged clothes and
  6  say that_is king this friend name-°sat-to_whom-+one who man^
  7  [the_king_came_in] go-somebody [a_wedding_garment] man^ friend
  8  wedding clothes to-+name who this man^

## 202v — bind him hand and foot

> said, in the Lord God's house of heaven, that day; good, said this king, Gabriel, friend, brother by name, this most high […] the will; Gabriel spoke and said: bind the man's hands and feet, and cast the man out, the angel, outside [outer darkness] […] there is; see, the grinding of teeth, weeping. Chapter. Chapter. Here ends this holy gospel. The Lord God, with all thy heart. This holy gospel begins, written by holy Matthew, […] chapter | of the writing: the time, then, | the Lord Jesus, in his thirty-third year, the time

  1  say inside of-Lord_God heaven house [?]-~year good say this king
  2  Gabriel friend brother-+name this-high to-°sat will
  3  speak-~Gabriel say bind^ somebody hand and.
  4  foot and somebody cast_out angel on-out darkness
  5  [?]-~exist exist see grinding tooth weep^ chapter-oh
  6  chapter-oh here_ends this holy_gospel Lord_God be_loved
  7  here_begins this holy_gospel write.
  8  holy-Matthew [twenty_two] chapter | of.
  9  write time then-exist | Lord
 10  Jézus thirty ~begin-+three_days time

## 203r — is it lawful to give tribute to Caesar?

> The Lord Jesus preached in Jerusalem, and the Jews came to him, | to the Lord Jesus; and then they said, they answered [Master] [we know] truly the man; and truly the Lord is a prophet, because truly in God's way the Lord goes; and the Lord has the king and the emperor […] go; the Lord's name, to the apostles; how teachest thou? | Would the Lord take from what they would do? | […] He said: take from every man one drachma, the emperor, to the pagan; and they said: how teachest thou? Would the Lord take from what they would do? Said

  1  preach Lord-Jézus inside Jerusalem and to-leave Jew | to-Lord
  2  Jézus and_then say answered-+say [Master] [we_know] true^
  3  man^ and righteous-Lord prophet because true^ God way
  4  go-Lord and divine_one^ ~have king and emperor
  5  [teachest] go name-Lord on-apostle how? learn-+say-learn | want
  6  divine_one^ grab from would_say* do | [?]-[?]
  7  say grab from everybody = on-one drachma.
  8  emperor to-heathen and say-+say how? learn-+say-learn
  9  want-Lord grab from would_say* do say

## 203v — whose image and superscription?

> the Lord Jesus: bring the Lord the tax; and they brought it before the Lord Jesus; and then the Lord Jesus: whose is this image? Said the Jews: this is the inscription, the image. And then the Lord Jesus: whose is this writing? Said the Jews: this is the inscription, the writing. And then | the Lord Jesus: this is the inscription, the image; and the inscription, the writing; this inscription, from town to town, leave it. And then | the Lord Jesus: the brethren […] owe the inscription […] to the emperor, take it; in turn | love, they said, the apostles;

  1  Lord-Jézus carry-+say Lord tax and carry-+say
  2  before Lord-Jézus and_then Lord-Jézus whose?-+SUBJ this
  3  image^ say Jew this_is ~emperor image^
  4  and_then Lord-Jézus whose?-+SUBJ this write say
  5  Jew this_is ~emperor write and_then | Lord
  6  Jézus this_is ~emperor image^ and ~emperor
  7  write this ~emperor from_town_to_town* leave and_then | Lord
  8  Jézus brethren-[?] indebted ~emperor [whose_image]
  9  emperor grab-[?] in_turn | love-+say-apostle

## 204r — render to God the things that are God's

> the man owes God; this, God, take it. And then the Lord Jesus: he that believeth not […] the inscription, and God; and a man, from what he owes, as therefore he takes, likewise he owes. Here ends this holy gospel. Said the Lord Jesus: there is humble, the chief, the inscription, this world; and take it, the inscription, which he said; and he owes it, because this from the inscription, you [render to Caesar]

  1  somebody indebted God this God grab-[?]
  2  and_then Lord-Jézus exist ~believe-[?]
  3  ~emperor and God and somebody from indebted pray ~exist
  4  grab-[?] ~if indebted-[?]
  5  here_ends this holy_gospel say Lord-Jézus exist-[?]
  6  humble head [?]-~emperor-[?] this world* and
  7  grab-[?] [?]-~emperor-[?] who
  8  say-[?] and indebted-[?] because this
  9  from [?]-~emperor-[?] you [render]

## 204v — what a man owes the Church

> from the heavenly faith, baptized, a man remits; the alien nation, out; believe, baptized, a man; and | the apostles, the man; and the emperor, the king | humble, they said, the apostles; the man; and he owes the Church, this man, [shall be gathered] in turn, upon, to many churches; and of […] the Lord, the earth; in turn, before, secondly they said, he owes the Church, this man, upon [shall stand] before the man's spirit, from the Father; and the Father, this man, the way he makes before the Lord | the Father

  1  from heavenly* believe one-~woman somebody remit heathen
  2  out believe one-~woman somebody and | [?]-apostle
  3  somebody and [?]-~emperor-king | humble-+say-apostle.
  4  somebody and indebted-[?] church this somebody
  5  [shall_be_gathered] in_turn on on-many church and
  6  of-[?] Lord earth in_turn before two
  7  say-[?] indebted church this somebody on
  8  [shall_stand] before of-somebody spirit from-father and father this
  9  somebody way do before of-Lord | from-father

## 205r — fasting, the ten commandments, and thanks

> God; thirdly, they said, he owes, take | of the man's fast, and the man's prayer, and the ten commandments of the Lord's Father God; and he owes to kneel down before the Lord's Father God [shall be gathered] and the man owes the Lord prayer, at home, in humility, the Lord's pleasing and thanks afterward; and to the Lord all heaven and earth; and a man takes the chief, the Lord, from the emperor, the king, the world, he who owes; the man who believeth not, every Lord and every emperor and every king, every believer

  1  DIV third say-[?] indebted grab | of
  2  somebody-fast and of-somebody pray and ten commandment
  3  of-Lord from-God_the_Father and indebted-[?] kneel
  4  before of-Lord from-God_the_Father [shall_be_gathered] and
  5  indebted-somebody Lord pray ~humble Lord pleasing
  6  and give_thanks = and to-Lord every heaven land
  7  and somebody grab head Lord from emperor king
  8  world he_who* indebted somebody exist ~believe-somebody
  9  every Lord and every emperor and every king every believe

## 205v — Jericho

> baptized, the man [unto] of the Lord's Father God. Here ends this holy gospel, and to the apostles the holy gospel. The Lord God, with all thy heart. This holy gospel begins, written by holy Luke, in the ninth end of numeral chapter of the writing: the time, then, the Lord Jesus, thirty, in one day; the time | the Lord Jesus went into another town; and this town's name was Jericho; and then

  1  one-~woman man^ [unto] of-Lord from-God_the_Father
  2  here_ends this holy_gospel and on-apostle holy-gospel Lord_God be_loved
  3  here_begins this holy_gospel
  4  write holy-Luke inside
  5  nine end_of_numeral* chapter of-write
  6  time then-exist
  7  Lord-Jézus thirty inside one
  8  day time go | Lord
  9  Jézus inside one another town and this town
 10  name exist Jericho and then-exist

## 206r — Zacchaeus climbs the tree

> the Lord Jesus kept going, the town of Jericho; and then in Jericho there was one chief tax collector, and the man's name was Zacchaeus; and then he was seen, the Lord Jesus going into Jericho; and Zacchaeus could not see the Lord Jesus, but from [chief publican] Zacchaeus, this many people; and he climbed up one tree, because [little of stature] Zacchaeus […] the Lord Jesus went; and then the Lord Jesus came to this tree, and the Lord Jesus saw

  1  go_on Lord-Jézus Jericho town and then-exist inside
  2  Jericho one publican head and.
  3  ~brother-+name man^ exist Zacchaeus
  4  and then-exist Lord see-+say go Lord-Jézus inside Jericho
  5  and Lord can see Zacchaeus Lord-Jézus
  6  but from [chief_publican] Zacchaeus this many people
  7  and ascend one [...] because [little_of_stature]
  8  Zacchaeus [?]-go Lord-Jézus and then-exist
  9  go Lord-Jézus to-this [...] and see Lord-Jézus

## 206v — make haste and come down

> Zacchaeus sitting upon this tree; and then the Lord Jesus: Zacchaeus, come down, for this Lord must be today in Zacchaeus's house, that day, the Lord; and with joy he left, Zacchaeus; and he came down, this Zacchaeus; and the Lord and the apostles, Jesus, went into Zacchaeus's house; and | from the name of the Lord Jesus, that day, the Lord sat; and they began to murmur against the Lord Jesus, the chief men of the Jews, saying:

  1  Zacchaeus abide^ on-this [...]
  2  and_then Lord-Jézus Zacchaeus go to-down
  3  this-Lord today exist-Lord inside of-Zacchaeus
  4  house [?]-~year-Lord and joy leave-chapter-leave.
  5  Zacchaeus and go down this.
  6  Zacchaeus and go-Lord-apostle-Jézus inside
  7  Zacchaeus [?]-+who-to house and | from
  8  name Lord-Jézus [?]-~out-~year sit-Lord and begin-+say
  9  murmur on-Lord-Jézus high_priest = this-Lord say

## 207r — the half of my goods I give to the poor

> the Son of God, in turn, with one sinner, from one […] one extortioner; and he left afar | the name of Jerusalem, Zacchaeus; and then Zacchaeus: Master, this Zacchaeus takes the half, the half truly, of Zacchaeus's riches, to God, the poor in spirit, truly the half; in turn he left afar one among you, in turn, Jerusalem […] | take, Jerusalem, one denarius; upon the extortion, Jerusalem would, the man, to every one, two by two, take; and the Lord Jesus saw that he himself was

  1  son God in_turn one sinner^ from-one
  2  extorter* one extort and stand^ far | name-Jerusalem
  3  Zacchaeus and_then Zacchaeus
  4  Master this-Zacchaeus half grab
  5  half-righteous of-Zacchaeus ~rich God
  6  poor_in_spirit = righteous-half in_turn stand^ far one
  7  among you in_turn-chapter-Jerusalem [half_my_goods] | grab
  8  chapter-Jerusalem one denarius on-extort want-chapter-Jerusalem man^
  9  to-every two-two grab and see Lord-Jézus he_is*

## 207v — this day is salvation come to this house

> truly a son of father Abraham; and then the Lord Jesus: | Zacchaeus, Zacchaeus, have it, because this day, in Zacchaeus's house is salvation, Zacchaeus's; because the Lord, this Lord, truly the Son of the living God; and then the Lord Jesus to the chief men of the Jews: take the commandment; Zacchaeus, therefore, the Lord to this, this Lord went into this world, who is, this Lord, sin […] […] | but the Lord, this Lord went, who is, this Lord, sin; the Lord loves; and the Lord, the sinful man; and [this day] of the Lord, the sinful man is saved, and the Lord is pleased; and the sinful man gives thanks. Here ends this holy gospel. The Lord God,

  1  righteous son father Abraham and_then Lord-Jézus | Zacchaeus
  2  Zacchaeus have because this-[?]-+name today inside of-~Zacchaeus
  3  house be_saved of-~Zacchaeus because Lord this-Lord
  4  righteous son living God and_then Lord-Jézus high_priest =
  5  grab-+say commandment Zacchaeus ~exist-Lord to-this this-Lord
  6  go-Lord on-this world* who-exist this-Lord sin from-°sat [fourfold] | but
  7  Lord this-Lord go-Lord who-exist this-Lord sin love-Lord and Lord sin
  8  man* and [this_day] of-Lord be_saved sin-somebody exist
  9  and Lord godfearing^ and give_thanks = sin-somebody here_ends this holy_gospel Lord_God

## 208r — what Zacchaeus signifies

> with all thy heart. This Zacchaeus is every chief among sinners, and every tax collector, and every man who takes from the sinner, in mercy, the Lord God; and every sinful man, and the sinner in love, the Lord God; and every sinful man truly, and the sinner in truth, the Lord God, that is; and the sinner bears the law of God — this is truly the law of the Lord God; and this Zacchaeus is mercy to God's poor in spirit; and this Zacchaeus loves the Lord God most high, all creation, and every man, as a man his neighbour; and this Zacchaeus is in the truth, the law of the Lord God, that is, | bearing

  1  be_loved this Zacchaeus exist every sin-somebody head
  2  and every publican and everybody = from-grab somebody-sin inside have_mercy.
  3  Lord_God and every somebody-sin and somebody-sin inside love Lord_God and every
  4  somebody-sin righteous and somebody-sin inside righteous Lord_God that_is
  5  and somebody-sin carry law God this_is righteous law Lord_God
  6  and this Zacchaeus exist have_mercy God spiritually
  7  blind and this Zacchaeus love Lord_God high every create
  8  and everybody = how?-to somebody neighbour* and this.
  9  Zacchaeus exist inside righteous law Lord_God that_is | carry

## 208v — the first three commandments

> the commandment of God, he who is; take it, in the word of the Old Testament, | from father Abraham. The first commandment of God: believe, man, truly, baptized; one God saves a man, to many | not, not, not; the man's is heaven and earth. The second law, take it in the word of the Old Testament, from father Abraham: God's name take not in vain. The third law, take it in the word of the Old Testament, from father Abraham: a man shall, truly, baptized, the holy Sunday and the feast, this holy man, from the mother, the temple; let a man hear the preaching, of […]

  1  SUBJ-[?] commandment God he_who* exist take^ inside Old_Testament word | from
  2  father Abraham first God commandment believe somebody righteous
  3  one-~woman one God be_saved somebody to-many | not
  4  not-not of-somebody SUBJ heaven land the_rest^ law
  5  exist take^ inside Old_Testament word from-father Abraham God
  6  name in_vain grab three law exist take^
  7  inside Old_Testament word from-father Abraham shall somebody
  8  righteous one-~woman holy-~Sunday and feast holy-this-somebody from*
  9  mother temple preach hear-somebody of-[?].

## 209r — from Adam to Abraham to Moses

> heaven and earth; and these three laws the Lord God confirmed to Moses by the Lord's angel; the time, then, from Adam onward until Abraham, one hundred years and […] years; from Abraham out until Moses, three thousand and fifty; from Abraham until Moses, the time the Lord God first confirmed to Moses by the Lord's angel; and God's angel said: Moses, because of this, teach, Moses, this people the three laws of the Lord; because of this let the people believe in one

  1  heaven land and this three law confirm Lord_God Moses
  2  on-angel of-Lord time then-exist from ~Adam ~trespass.
  3  until Abraham one hundred-year and [?]-year from
  4  Abraham SUBJ ~out until Moses ~begin-+three_thousand
  5  and fifty from Abraham until Moses time
  6  first confirm Lord_God Moses on-angel of-Lord and say
  7  God angel Moses because-this on-learn this Moses this
  8  people three law of-Lord because-this people believe one

## 209v — the three laws, and what Zacchaeus kept

> God; second, take not God's name in vain; third, God's law: [to keep] the holy Sunday and the feast, this holy man, from the mother, the temple; let a man hear the preaching. This is God's law; and the law a man bears; every such man is saved. And this Zacchaeus [hear the] the word, loved, and bore these three laws of the Lord God. Here ends this teaching, the holy gospel. The Lord God, with all thy heart.

  1  God two God name in_vain grab three God law
  2  [to_keep] holy-~Sunday and feast holy-this-somebody from* mother temple
  3  preach hear-somebody this God law and law somebody exist
  4  carry everybody = exist be_saved and this Zacchaeus
  5  [hear_the] word love and carry this three law Lord_God end this
  6  learn holy-gospel Lord_God be_loved

## 210r — a man possessed brought before the Lord

> This holy gospel begins, written by holy Matthew, in the fourteenth […] chapter | of the writing: the time, then, the Lord Jesus, in his thirty-third year, the time | the Lord Jesus preached in Jerusalem; and then they brought one man before the Lord Jesus, in [the synagogue]; the man was evil, the evil one in him; and then the Jews: this Lord, by Lucifer, the help

  1  here_begins this holy_gospel
  2  write holy-Matthew inside
  3  fourteen-+one end_of_numeral* chapter | of
  4  write time
  5  then-exist Lord-Jézus
  6  inside thirty ~begin-+three_days time preach | Lord
  7  Jézus inside Jerusalem and then-exist brought* one man^
  8  before Lord-Jézus inside [the_synagogue] man^ exist devil =
  9  and_then Jew this-Lord hide-evil help

## 210v — the unclean spirit walks through dry places

> of the evil, from the people he casts out. And then the Lord Jesus: this Lord […] of the Lord's Father God; and this Lord, of the Father God, can do it, the Lord. And then the Lord Jesus: this, therefore, is pleasing; who is from the evil, he is pierced. And then the Lord Jesus: then he casts out from a man one unclean spirit, and the evil one goes to a dry place, and [walketh] to the Lord, the place, that is, to the virgin, from the people, and to the word, the people; and there is […] the evil one's lodging; and then this evil one, this evil

  1  evil inside from generation^ exorcise and_then Lord-Jézus this-Lord
  2  [by_the_finger_of_God] of-Lord from-God_the_Father and this-Lord of-God_the_Father can miracle
  3  do-Lord and_then Lord-Jézus this therefore-pleasing who-exist
  4  from evil exist pierce and_then Lord-Jézus then-exist.
  5  exorcise inside man^ one unclean
  6  ~spirit and go evil dry place and
  7  [walketh] to-Lord place that_is on-virgin-from generation^ and
  8  on-word generation^ and exist therefore-°not evil
  9  lodging-+and_then this evil this-evil

## 211r — seven other spirits worse than himself

> and the evil one goes [wicked] because from the evil, love, sin, the sinful man; and he takes [taketh with him] seven evil ones, from the evil, trespass, mourning; and there are […] seven evil ones; and | they go, the evil ones, all seven. And then the Lord Jesus: how then this man, the one aforesaid [swept] and every man, O, into the house goes, this; and there stood up again one […] chief among this people, the Jews; and then: blessed is the womb which bore this Lord, and blessed are the breasts which | this Lord did nurse. And then the Lord Jesus: blessed is the Lord's mother,

  1  and go-evil [wicked] because from evil^ love sin somebody-sin
  2  and exist grab [taketh_with_him] seven evil^ from evil^
  3  trespass mourn and exist [wicked] seven evil^ and | go
  4  evil^ every seven and_then Lord-Jézus how? then-chapter this man^
  5  first^ aforesaid [swept] and everybody = oh inside house
  6  go-this ~and stand_up-?again first^ ~woman head
  7  among this people Jew and_then blessed from womb
  8  which-+SUBJ this-Lord carry and blessed from breast which | this
  9  Lord nurse and_then Lord-Jézus blessed SUBJ of-Lord mother

## 211v — rather, blessed are they that hear the word of God

> the virgin Mary, which bore the Lord; and blessed are the breasts which did nurse the Lord; and even more blessed are the people, and God said: let a man hear, and say, and let a man bear it. Here ends this holy gospel. The Lord God, with all thy heart. This holy gospel begins, written by holy John

  1  virgin-Mary which-+SUBJ to-Lord carry and blessed from breast which
  2  to-Lord nurse still_more and blessed from people and God say.
  3  hear-somebody and say SUBJ carry-somebody end this
  4  holy-gospel Lord_God be_loved
  5  here_begins this holy_gospel
  6  write holy-John

## 212r — whence shall we buy bread?

> in the sixth chapter of the writing: the time, then, the Lord Jesus in his thirty-third year, the time the Lord Jesus sat | by the Red Sea [of Galilee]; and the Lord went through, the Lord Jesus went through the Red Sea to one mount; and the Lord Jesus sat upon this mount, and [lifted up] the Lord's two eyes to heaven [saw] and the Lord Jesus saw, upon every side, [a great multitude] people coming to the Lord; and they came; and then the Lord Jesus: Philip, this people | take, the Lord's apostle Philip, to eat. And then holy Philip answered:

  1  inside six chapter of-write time then-exist Lord-Jézus
  2  inside thirty ~begin-+three_days time sit Lord-Jézus | on
  3  the_Red_Sea [of_Galilee] and Lord through
  4  go-Lord Lord-Jézus through the_Red_Sea to-one
  5  to_the_mount and sit Lord-Jézus to-this to-mount
  6  and lifted_up of-Lord two eye heaven [high] and
  7  see Lord-Jézus on-every two-two [a_great_multitude] people to-Lord and
  8  go and_then Lord-Jézus Philip this people | grab
  9  apostle-Lord-Philip eat and_then holy-Philip answered

## 212v — five barley loaves and two fishes

> then two hundred pennyworth would not be enough, this day's bread to buy, therefore, for the people. And then holy Andrew answered: this [two hundred pennyworth] one [barley loaves] son; and the son has five loaves of barley bread, and two fishes. And the apostles brought these five loaves of barley bread and these two fishes before the Lord Jesus; and the Lord Jesus took this bread and these two fishes; and this bread and

  1  then-exist have two_hundred denarius who-exist people
  2  exist-today’s buy ~exist people enough and_then
  3  holy-Andrew answered SUBJ this [two_hundred_pennyworth] one.
  4  ~little boy^ and have boy^ five.
  5  loaves barley bread and two fish
  6  and carry disciple^ this loaves five barley
  7  bread and this two fish before Lord-Jézus
  8  and take^ Lord-Jézus this bread and
  9  this two fish and this bread and

## 213r — twelve baskets full

> these two fishes the Lord Jesus blessed; and then the Lord Jesus to the apostles of the Lord: apostles, sit this people down upon the grass; and the Lord Jesus divided this bread to the apostles, and these two fishes, in turn, the apostles to this people; and then the apostles, every apostle took his portion, and then the apostles to the whole wide world, upon eating; and then | the Lord Jesus to the Lord's apostles: go, apostles, and take this, of the leftovers; and into baskets the apostles, of the leftovers, twelve filled up; and then the Lord Jesus to the Lord's apostles: go out among this people; and then the apostles carried the twelve baskets filled up out

  1  this two fish bless* Lord-Jézus and_then Lord-Jézus disciple^
  2  of-Lord sit-apostle down this people on-grass and on-divide
  3  Lord-Jézus this bread disciple^ and this two fish in_turn disciple^ this
  4  people and then-exist disciple^ every apostle-[?] portion grab-apostle
  5  and then-exist apostle-[?] to all_the_world on eat and_then | Lord
  6  Jézus disciple^ of-Lord go-apostle and grab-apostle this from
  7  leftovers and on-basket disciple^ from leftovers six-six
  8  fill and_then Lord-Jézus disciple^ of-Lord go this out among
  9  people and then-exist disciple^ carry basket six-six fill out

## 213v — this is of a truth the prophet

> among this people, to the many; and this many people saw what the Lord Jesus could do, and all the people gave the Lord thanks; and this word they cried out, thanks: there is God, by the letter, the most high; and the Lord took a man by name, he could, and a man could do this miracle; and he left, among this people, the Lord Jesus. Here ends this holy gospel. The Lord God, with all thy heart. This holy gospel begins, written by holy John, in the eighth chapter of the writing: the time, then, the Lord Jesus, in his thirty- | third year, the time.

  1  among this people to-many and see this to-many people can Lord-Jézus
  2  and Lord every people give_thanks = and this word who-shout-to
  3  thanks exist God literal-on highest and the_Lord grab-somebody name-+one can
  4  and somebody can this miracle do and leave among
  5  this people Lord-Jézus here_ends this holy_gospel Lord_God be_loved.
  6  here_begins this holy_gospel
  7  write holy-John inside
  8  six-two chapter of-write
  9  time then-exist
 10  Lord-Jézus inside thirty | ~begin
 11  three_days time.

## 214r — he that is of God heareth the words of God

> The Lord Jesus preached in Jerusalem, and the Lord Jesus said to the Lord's apostles and to the Jewish people: he left behind one, afar, among you, apostles; and the Lord upbraided them for sin; and then the Lord Jesus: amen, amen, this Lord says to you, apostles, and […] from God: whosoever is of God heareth God's word; in turn whosoever, therefore, is not of God, whosoever, God's word he heareth not. And this […] from the two […]; and then the Jews: this Lord is a blasphemer; this Lord, Lucifer, the evil one, the evil, the Lord has; this Lord is one who began to believe

  1  preach Lord-Jézus inside Jerusalem and say Lord-Jézus apostle of-Lord and Jew
  2  people leave-leave one far among you-apostle
  3  and Lord on-sin admonish-chapter and_then Lord-Jézus verily^ verily^
  4  this-Lord you-apostle speak-Lord and [?]-+SUBJ from*
  5  God this ~somebody-[?] God say hear in_turn and ~somebody-[?] ~exist
  6  from* God this ~somebody-[?] God say ~exist hear and this
  7  [?]-+SUBJ from* two [hath_a_devil] and_then Jew
  8  this-Lord one blasphemer this-Lord Satan hide-evil
  9  devil^ have-Lord this-Lord one ~begin-believe

## 214v — before Abraham was made, I am

> and this Lord, on the holy feast, healed the sick. And then the Lord Jesus, in this [keep my word]: this Lord, through sin, this healing; you are sorrowful, love; this Lord, you, on the holy feast healed the sick. And then the Lord Jesus: amen, amen, this Lord says to you; and whosoever, therefore, believes the Lord, that one therefore, whosoever, is saved; but every man is damned who remains; and | the man, the apostles said, is the Lord's; believe, whosoever lives | whosoever, one, the apostles said. Chapter. Chapter. He shall not die. And then the Jews: Abraham of theirs, the black, believed God;

  1  and this-Lord on-holy-feast ill heal-Lord and_then Lord-Jézus inside
  2  this [keep_my_word] this-Lord commit sin this healthy_man^ SUBJ you sad
  3  love this-Lord you on-holy-feast ill heal-Lord
  4  and_then Lord-Jézus amen amen this-Lord you
  5  speak-Lord and ~somebody-[?] ~exist Lord believe and one
  6  ~exist-~somebody-[?] be_saved but everybody = be_damned remain* and | man^
  7  apostle-+say exist Lord believe from ~somebody-[?] exist | living-~somebody
  8  one-apostle-+say chapter-oh chapter-oh not die and_then
  9  Jew of-+say Abraham black SUBJ God believe

## 215r — Abraham saw my day

> and the black one, God's word he heard, Abraham, and still is dead in turn, this Lord shall not die. And then the Lord Jesus: this Lord saw the death of father Abraham. Said the Jews to the chief men: therefore this Lord is fifty, in turn this | two thousand years, likewise, of their father Abraham […] in turn | this Lord spoke [rejoiced] Abraham; the Lord saw; this, therefore, is pleasing; this Lord is a blasphemer. And then the Lord Jesus: the Lord is first; this Lord left, but rather your father Abraham, in this world [was made]

  1  and black SUBJ God say hear Abraham and still SUBJ is_dead*
  2  in_turn this-Lord not die and_then Lord-Jézus this-Lord see
  3  ~you from-father Abraham say Jew on-head
  4  ~exist this-Lord fifty in_turn-+SUBJ this | two-?thousand
  5  year ~if of-+say from-father Abraham is_dead* in_turn | this
  6  Lord speak-Lord [rejoiced] Abraham Lord see-Lord this ~exist pleasing
  7  this-Lord blasphemer and_then Lord-Jézus first-Lord this-Lord leave but_rather
  8  you from-father Abraham on-this world* [was_made]

## 215v — then they took up stones

> And then the Jews: this, therefore, is pleasing; this Lord is a blasphemer; and they carried stones, and would have stoned the Lord Jesus; and the Lord Jesus left from among them, and out | of the temple the Lord went, and the Lord's apostles. Here ends this holy gospel. The Lord God, with all thy heart. Because it is written in Moses, truly, in turn [the law] among you, if a man begin to blaspheme, and a man has stones, and out from among them [out of the temple] [passing through] spoke holy Elijah the prophet and holy Moses; therefore he said they could, because of […] the Lord, the Lord God created, of theirs

  1  and_then Jew this ~exist pleasing this-Lord one blasphemer
  2  and carry-+say stone and would_say* stone-stone-this
  3  Lord-Jézus and leave among-+say Lord-Jézus and out | on
  4  temple and go-Lord and of-Lord apostle here_ends this holy_gospel
  5  Lord_God be_loved because-exist inside Moses true^ write in_turn [the_law]
  6  among you ~begin somebody how? blasphemer and have
  7  somebody stone-stone-this and among-+say out [out_of_the_temple] [passing_through]
  8  speak holy-+Elijah prophet and holy-Moses ~exist he_said*
  9  can-+say because* of-[?] Lord create Lord_God of-+say

## 014r — the Lord went in humility

> the Lord God; because the Lord went in humility, in turn the king, there is heaven and earth, and many a miracle there was afterward, the Lord; and you, the Lord, | upon the cross died, and on the third day stood up from the dead, and appeared to many people, and the Lord was to you, through staying […] the year; and then this […] year […] see, they said, upon all the people; see, he left behind, into heaven and earth; and he left behind, they said that believe: he himself is truly the Son of the living God, and King of all kings, and Lord of all lords, the chief Lord of heaven and earth.

  1  Lord_God because go-Lord humble-Lord in_turn king exist heaven and ~earth
  2  and great^ miracle exist ~do-Lord and you Lord | on
  3  cross-die and on_the_third_day from die stand_up and appear great^ nation^
  4  and exist-Lord to-you through stay [?]-year
  5  and then-exist this [?]-year [King_of_kings] see
  6  say-[?] on-every nation^ see leave-leave inside heaven
  7  land and on-leave-leave exist-+say that* believe
  8  he_is* righteous son living God and king every king and
  9  Lord every Lord head Lord heaven and ~earth

## 014v — a new gospel begins

> This holy gospel begins, written by holy Matthew, in the twentieth, in the first chapter of the writing: the time | then

  1  here_begins this holy_gospel write holy-Matthew inside
  2  one-ten-+one-ten inside one chapter of-write time | then

## 011r — go into the village, and you shall find an ass

> the Lord Jesus was in his thirty-third year, the time | the Lord Jesus went to Bethany, into Jerusalem, and the twelve apostles; and then | the Lord went to the lodging [Bethphage] there was [mount Olivet] prayer, until, because the trespassing way of the people, the lodging; and the trespassing, through the night, the lodging of the Lord Jesus; and then the Lord Jesus sent two apostles down to Bethany, because the trespassing, they carried all [over against you] the way of the people, one ass; and then the Lord Jesus: in turn, brethren, you [immediately] therefore take it, they said, the two disciples, take it, the two disciples, the ass [tied] the apostles [a colt] love

  1  exist Lord-Jézus thirty ~begin-+three_days time go | Lord
  2  Jézus on-Bethany inside Jerusalem six-six disciple^ and then-exist | go
  3  Lord on-+lodging [Bethphage] exist [mount_Olivet] pray ~until because
  4  trespass way people lodging and trespass through night
  5  lodging Lord-Jézus and then-exist-Lord go Lord-Jézus two disciple^ down
  6  Bethany because trespass carry-+say every [over_against_you] way people
  7  one donkey and_then Lord-Jézus in_turn-?brethren you
  8  [immediately] ~exist-+say grab-+say say learn-two-learn
  9  grab-+say learn-two-learn donkey [tied] apostle-+SUBJ [a_colt] love

## 011v — they set him thereon

> [loose them] they answered, going [bring them] the ass, in the place, you, the ass, to say; and then the two disciples were […] one [laid their garments] the ass, to the ass, two asses, the ass; and then the apostles untied this ass, and [they did] this commandment; but [set him] and the Lord Jesus sat down upon the ass, he said; and the Lord had the apostles tie this, from the ass, the mother of this ass; and the Lord sat upon this ass, and the Lord went into Jerusalem; and then the Lord was; the Lord went upon the mount of Olives, the most high, Jerusalem, […]

  1  [loose_them] answered on-go [bring_them] donkey on-place you donkey to
  2  say and then-exist learn-two-learn exist [?]-[?].
  3  one [laid_their_garments] colt^ to-donkey the_rest^ donkey
  4  donkey and then-exist tie_up-apostle this donkey and
  5  [they_did] this commandment but [set_him] and sit down Lord-Jézus
  6  on-?he_said donkey and Lord tie_up disciple^ this from
  7  donkey mother this donkey and sit-Lord on-this
  8  from donkey and go-Lord inside Jerusalem and then-exist.
  9  exist-Lord go-Lord on-tasty-to mount highest Jerusalem in_turn-chapter-in_turn

## 012r — the multitude went before him

> and […] the Lord Jesus and the Lord's apostles, because they were taught [went before] and then the Lord Jesus to the Lord's apostles: go, you, [multitude] and in turn, brethren, you [cried out] there is judgment, who is it; and the apostles went, the apostles said, and the apostles went to the Lord, to answer; in turn, to the Lord, they went the two ways; and then the Lord was to the Lord [followed] many people, because they preached, this people [a great multitude] the Lord Jesus went; and an army went to the Lord Jesus; and then the Lord Jesus kept going to Jerusalem, and then the Lord was; he saw upon Jerusalem the people; and the Lord Jesus went

  1  and from-°sought-to Lord-Jézus and of-Lord apostle because learn exist [went_before]
  2  and_then Lord-Jézus apostle of-Lord go you
  3  [multitude] and in_turn-?brethren you [cried_out] exist judge
  4  who_is_it and go-apostle say-apostle and go-apostle to Lord to
  5  answered in_turn to-Lord go two way and then-exist-Lord
  6  exist to-Lord [followed] many people because [?]-+preach this
  7  people [a_great_multitude] go Lord-Jézus and and go an_army
  8  to Lord-Jézus and then-exist go_on Lord-Jézus to-Jerusalem
  9  and then-exist-Lord exist see on-Jerusalem people and go Lord-Jézus

## 012v — hosanna to the son of David

> into Jerusalem; and with much joy they cried out, this Lord; and the son came, David the king; and the Lord, with much joy, said, because one man, they said, of […] believed; mercy and love, they spread, the men, before the Lord Jesus; and secondly they said, the men, branches of trees | they cut off, they said, the men; and […] | […] the men, before the Lord Jesus; and they cried out | this Lord is the son of David the king; they brought the king a crown, they said; and the Jews spoke: this Lord

  1  inside Jerusalem and great^ joy shout-[?] this-Lord and go son
  2  David king ~and-Lord great^ joy say
  3  because one somebody-+say of-[?] clothes^
  4  have_mercy-love spread-+say-somebody before Lord-Jézus
  5  in_turn-two say-somebody bough-+SUBJ | cut_off
  6  say-somebody and [spread_their_garments] | [in_the_way]
  7  somebody before Lord-Jézus and shout-[?] | this
  8  Lord SUBJ son David king brought-[?].
  9  king crown-+say and speak Jew this-Lord

## 010r — my house shall be called the house of prayer

> is the king of the Jews. And this word they cried out: thanks to the Lord from all the people on earth, and the angels of the eternal height; and the Lord Jesus went into the temple at Jerusalem; and then the Lord found the money changers; and the Lord, all the money changers, out […] | cast out, the Lord; and then the Lord Jesus: this temple is a house of prayer, a house by name; you have made it a den of thieves. And then, from one little son they cried out: this Lord is […] the king. And then one of the Jews answered: see, the Lord, the brethren, this

  1  king Jew and this word shout-[?] thanks
  2  Lord every people on-earth and angel from_heaven* high and
  3  go Lord-Jézus inside temple Jerusalem and then-exist exist-Lord find
  4  moneychanger and-Lord every moneychanger out dove_seller* | exorcise
  5  Lord and_then Lord-Jézus this temple-+SUBJ prayer^ house
  6  name-+one house you say do one
  7  thief-+one-house and then-exist from one little son
  8  and shout-to this-Lord SUBJ [?]-+say king
  9  and_then one Jew answered see-Lord brethren* this

## 010v — out of the mouth of infants

> little son speaks [Hosanna] this Lord is their king. And then the Lord Jesus: then this, every one, this little son, therefore | speaks; the son, then, the earth is, and the rock and stone, all are, they cry out [son of David] this Lord is your king. Here ends this holy gospel. The Lord God, with all thy heart. And then the law of the Jews; and the Lord said: take, in this […] Jerusalem, one rather, but rather they said, they could cup this, they would, the chief, take; and then […] the lodging to find, the Lord's heart, heaven and earth, Lord of all lords,

  1  little son speak-~son [Hosanna] this-Lord of-+say king and_then
  2  Lord-Jézus then-exist this every this little son ~exist | speak
  3  ~son then exist earth and rock-stone every exist.
  4  shout-to [son_of_David] this-Lord you-+say king
  5  here_ends this holy_gospel Lord_God be_loved and then-[?]
  6  law Jew and say Lord grab inside this in_turn-chapter-in_turn Jerusalem
  7  one rather °but_rather-+say exist-+say can-+say cup* this
  8  would_say* head grab and then-exist [?]-Lord
  9  lodging find heart-Lord heaven and earth Lord every Lord

## 013r — the prophet foretold it

> King of all kings; spoke holy […] the prophet, and holy […] the prophet, therefore, could the lodging find, the Lord's heart; and the chief of heaven and earth, Lord of all lords, King of all kings; and out, the two, loving, foretold, the prophet, and holy […] the prophet; and the Lord Jesus went [lodged] into Bethany, this [remained there] went [with him] the two, above, hidden, the earth; and this, many thanks the Lord did; in turn [morning] the Lord [returning] much sorrow; and then the Lord Jesus: this is [hungry] every one, from a man; and a man is of the Lord's name among men; and out of the man, the good man does.

  1  king every king speak holy-NAME.prophet prophet and holy-NAME.prophet
  2  prophet ~exist can lodging find heart-Lord and head
  3  heaven and earth Lord every Lord king every king and
  4  ~out love-two-exist predict NAME.prophet prophet and holy-NAME.prophet
  5  prophet and go Lord-Jézus [lodged] inside Bethany this [remained_there]
  6  go [with_him] two above-hide earth and this many thanks Lord do
  7  in_turn [morning] Lord [returning] many sad and_then Lord-Jézus this
  8  exist [hungry] every from somebody and somebody exist of-Lord name
  9  among somebody and out-somebody good-somebody do

## 013v — the three tables of Moses

> Three tables Moses took, and the Lord God wrote by the Lord's angel.

  1  three tablet Moses give^ and write Lord_God on-angel of-Lord

## 218r — Gamaliel and Nicodemus, and a servant named Saul

> the second, this holy man remits; the mother, the temple; let a man hear the preaching, from the seeing; heaven and earth; and the time of prayer, the two church fathers at Jerusalem; three chiselled on tables of stone, because the Lord God had Moses chisel three tables of stone by the Lord's angel, and wrote three commandments. Thanks to the Lord God. The time, then, from Adam onward, seven […] and three thousand; and the time of these three tables of Moses, the prayer, two church fathers, two high priests at Jerusalem: Gamaliel the high priest and Nicodemus the high priest; and then two servants hired themselves to these two high priests, as apostles; one man there was, and his name was Saul,

  1  two holy-this-somebody remit mother temple preach hear-somebody
  2  of-from-see SUBJ heaven land and time pray two
  3  church_father on-Jerusalem three on-stone-tablet chisel because exist Lord_God Moses
  4  three stone-tablet chisel on-angel of-Lord and write three commandment
  5  to-Lord thanks Lord_God time then-exist from ~Adam ~trespass seven-[?] and
  6  ~begin-+three_thousand and time this three tablet Moses pray
  7  two church_father two high_priest-high_priest on-Jerusalem Gamaliel high_priest and Nicodemus
  8  high_priest and then-exist two servant hire_out on-apostle this two high_priest-high_priest
  9  one man^ exist and-~brother-+name Saul

## 218v — Stephen, the first martyr

> and the second apostle was holy Stephen, the Lord God's first martyr; and | then there were two servants, these two, two apostles, these two, two high priests; in turn these two, two apostles, the two of them from [Damascus] the two, in belief, of Christ; this was the time, then, the Lord Christ was crucified, and then the Jews wipe out down, believing Christ, the Jews, the chief men; and they were, they said find; and there was a man, to many [far countries]; a man by the name of Christ, every man suffering; in turn, a man rather, the chief | take, they said; and then holy Stephen [cried with a loud voice] confess the name

  1  in_turn-two apostle exist Saint_Stephen the_first_martyr and | then
  2  exist two servant two this-two two apostle this-two two high_priest-high_priest
  3  in_turn this-two two apostle exist-two from [Damascus] two on-believe
  4  [?]-~Christ this exist time then Lord-~Christ crucified
  5  and then-exist Jew wipe_out* to-down believe ~Christ Jew
  6  head and exist exist-+say find* and exist
  7  somebody to-many [far_countries] somebody name [?]-~Christ
  8  everybody = suffering in_turn somebody-°but_rather head | grab
  9  say and then-exist holy-Stephen [cried_with_a_loud_voice] confess name

## 217r — they brought him to suffer

> of Christ; and then the Jews, the chief men, made ready against this holy Stephen, the Lord God's first martyr; and then Stephen they brought, they said, to suffer, within the temple at Jerusalem, the two of them, among them; Stephen went […]; and this Saul to them; and Saul went, because therefore [consenting] many; and this Saul, and then Stephen, they said, was brought within the temple at Jerusalem, because they would stone Stephen, because it is written in Moses, truly, in turn [the law] among you, if a man begin to blaspheme, and a man has stones, and | among

  1  [?]-~Christ and then-exist prepare Jew ~head on-this
  2  Saint_Stephen the_first_martyr and then-exist Stephen
  3  exist-+say brought* on-suffering inside Jerusalem temple
  4  two-+say among-+say Stephen go-[?] and this Saul
  5  to-+say and go Saul because ~exist [consenting] many and this Saul
  6  and then-exist Stephen exist-+say to-?brought inside temple Jerusalem
  7  because Stephen would_say* stone-stone-this because-exist write inside
  8  righteous Moses in_turn [the_law] among you begin man^
  9  how? blasphemer and have man^ stone-stone-this and | among

## 217v — the heavens opened

> they said, out […] […] | and then holy Stephen knelt down; and | then Stephen prayed to the Lord, gave thanks to the Lord God, they said; and then Stephen prayed, redeemed, to the Lord, gave thanks to the Lord God; and Stephen lifted up Stephen's two eyes to heaven and earth, and to the Lord, to thanks, the Lord God; and this word holy Stephen said, to the Lord, to thanks, the Lord God, through offering, Stephen, this Stephen, this Lord, Stephen's soul within, the Lord's, why in turn; the time, then, the gate of heaven; and then Stephen saw one king sitting on a throne, and [the right hand of God] an army, an army

  1  say out [out_of_the_temple] [passing_through] | and then-exist kneel holy-Stephen and | then
  2  exist pray-Stephen to-Lord to-thanks Lord_God to-+say and then
  3  pray ~redeem Stephen to-Lord to-thanks Lord_God and raise-Stephen
  4  of-Stephen two-eye-eye heaven land and to-Lord to-thanks.
  5  Lord_God and this word say holy-Stephen to-Lord to-thanks Lord_God through
  6  offer Stephen this-Stephen this-Lord of-Stephen soul
  7  inside of-Lord why?-in_turn time then-exist from-gate
  8  heaven and then-exist-Stephen see-Stephen one king
  9  inside throne sit and [the_right_hand_of_God] an_army army

## 216r — they stopped their ears

> of angels; and holy Stephen cried out; Stephen saw […] | see, the gate of heaven and earth is opened, and Stephen saw one king, crowned, sitting on a throne, and [the right hand of God] an army, an army of angels. And then the Jews: this Stephen is a blasphemer, Stephen; and they took off from themselves their belief; and they left, the letter, the man, one son; and this son was this Saul; and the man was this belief; and the scribes would stone holy Stephen | the first martyr

  1  angel and shout-to holy-Stephen see-Stephen [looking_up] | see*
  2  gate/open heaven land and see-Stephen one
  3  king crown inside throne sit and [the_right_hand_of_God]
  4  an_army army angel and_then Jew
  5  this-Stephen-+SUBJ one blasphemer-Stephen and.
  6  take_off-+say on-+say of-+say clothes^ and.
  7  leave-+say literal man* one son and this son.
  8  exist this Saul and man* exist this clothes^
  9  and from [...] want stone-stone-this holy-Stephen | first-suffering

## 216v — Stephen prays for those who stone him

> of the Lord God [lay not this sin] and the scribes judged; they could stone Stephen; and the scribes were [fell asleep] in Stephen's death; and this, spoken, written; then, therefore, Stephen prayed for the scribes, and Stephen, the Lord God's first martyr, to the Lord, to thanks, the Lord God; the scribes were; they are damned; and then Stephen, they said, out of the town, stoned […] […]; and | then that day he was; he saw this suffering, this Saul, […] what the Jews did to holy Stephen; | the first, not, not, not; to the Lord, to thanks, the Lord God; and then | there were the scribes; through startling, this Saul, and trespassing, to the place

  1  Lord_God [lay_not_this_sin] and [...] can Stephen stone-stone-this
  2  and from [...] exist [fell_asleep] inside of-Stephen die and this speak
  3  write then-exist ~exist Stephen [...] pray-Stephen
  4  and Stephen first-suffering-Lord_God to-Lord to-thanks Lord_God
  5  [...] exist be_damned and then-exist Stephen exist-+say
  6  out on-town stone-stone [out_of_the_temple] [passing_through] and | then-chapter
  7  day exist see this suffering this Saul
  8  [a_great_persecution] do Jew on-holy-Stephen | first-not
  9  not-not to-Lord to-thanks Lord_God and then-exist | exist
 10  [...] through startle this Saul and trespass to-place

## 219r — Saul takes letters to Damascus

> and by the name of the brethren of the Lord Jesus Christ; and this Saul went to the chief men of the Jews, to Jerusalem; one from this Saul they took, the chief men, the scribes; they could, upon this man that believeth not, and the man who this Jesus, this Christ, believes; and [threatenings] the scribes, the mother, the scribes would, every one take prisoner, and whosoever, to many [bound] see, by the name of the brethren of the Lord, the scribes would, every man to you, this going; and then the scribes, they said, took a commission, many riches; and then the scribes were [letters] many servants on the commission.

  1  and-brother-+name Lord-Jézus-Christ and go this
  2  Saul to-head Jew on-in_turn-chapter-in_turn Jerusalem
  3  one-from this Saul grab-+say head [...]
  4  can on-this man^ not_believe and man^ this Jézus this
  5  Christ believe and [threatenings] [...] mother [...] SUBJ every
  6  capture and ~somebody-+SUBJ to-many [bound] see* and-brother-+name
  7  of-Lord [...] everybody = to-you this-go-this
  8  and then-exist [...] exist-+say grab mission many ~rich
  9  and then-exist [...] [letters] many servant on-mission

## 219v — a light from heaven

> And then, within | within Jerusalem, one […] a town there was, named Damascus, because, and within that they believed the Lord Jesus Christ; and then this one went, Saul, upon this town, many an army; and | then Saul said to the servants, at the beginning of the way, Saul and the servants going, the time; and this Saul went, the scribes' servant, and then there was a light [shined round] from heaven and earth, and then there was a light [fell to the earth] to the heavenly; he bowed down, and the Lord God cried out upon the water: Saul, Saul,

  1  and then-exist inside | inside Jerusalem one-in_turn-chapter-in_turn
  2  exist-[?] town exist Damascus because and
  3  inside that* believe Lord-Jézus Christ and then-exist go this-who
  4  Saul on-this town many an_army and | then-exist
  5  say-Saul-servant on-~begin way to-go-Saul-servant
  6  time and go this Saul ~before [...] servant
  7  and [...] exist light [shined_round] on-heaven land
  8  and [...] exist light [fell_to_the_earth] on-+heavenly-to bow
  9  and shout-to Lord_God on-water Saul Saul

## 220r — I am Jesus of Nazareth

> to the brethren of the Lord, through persecuting the scribes; and he cried out, this | Saul, the scribes [Saul] lie; in turn the Lord [whom thou persecutest] this Lord; and the Lord God cried out upon the water: this Lord is Jesus of Nazareth, the Lord, on the cross executed; and this Saul cried out: Lord, brethren, Saul, the Lord, afterward; and the Lord God cried out upon the water: go, scribes, into the […]; from the scribes, teach a man love; the scribes were; the scribes did it, the time, the hour, from the blinding of the scribes' eyes; and [led him by the hand] and then there were those who took Saul's servants; and Saul they carried,

  1  to-?brethren Lord through [...] and shout-to this | Saul
  2  [...] [Saul] lie in_turn Lord [whom_thou_persecutest] this-Lord and
  3  shout-to Lord_God on-water this-Lord from Jézus Nazareth
  4  the_Lord on_the_cross execute and shout-to this Saul
  5  Lord brethren* Saul Lord ~do and shout-to
  6  Lord_God on-water [...] inside in_turn-chapter-in_turn from [...] on-learn man^
  7  love [...] [...] time hour from
  8  [...] and [led_him_by_the_hand] and [...] exist
  9  grab of-Saul servant and Saul from-carry

## 220v — the house of Judas, and Ananias

> Saul, the servants, into the […]; and they put Saul, the servants, one man, Ananias; and a man, Ananias, was coming, Gamaliel, the […]; and this Saul, trespassing, the scribes were at the coming; and then there was this Saul, this Ananias put Saul, the servants, into one house; and then three days the scribes lay, this Saul, within this house, this Ananias, the man; and this man's name was Judas; and then one man within this […] could, the man said, to the high understanding; in turn the man's name was

  1  Saul servant inside in_turn-chapter-in_turn and Saul put servant
  2  one man* Ananias* and man^ Ananias* exist ~be_born
  3  Gamaliel in_turn-chapter-in_turn and this Saul trespass [...]
  4  on-~be_born and [...] exist this Saul this
  5  Ananias* put of-Saul servant inside one house
  6  and [...] three [...] this Saul inside
  7  this house this Ananias* man^ and this man^ and-~brother-+name
  8  exist Judas and then-exist one man^ inside this in_turn-to-in_turn
  9  can man^ say to-high-understand in_turn and-~brother-+name man^ exist

## 221r — a vessel to bear my name

> Ananias; and Paul, from Paul; and he bowed down, [hail] upon Paul [laid his hands]; and Ananias put the Lord's name upon Paul, because from Paul, Paul is | of the Lord; the name Paul bears into the wide world; Paul is | of the Lord; the name Paul confesses. And then holy Ananias: Lord, how is it, from Saul, of the Lord, the name | bears Saul, and Saul, of the Lord, the name, through persecuting, Saul? And secondly the Lord God said to holy Ananias: go, Ananias; the Lord's servant, in truth and love, drink

  1  Ananiah and Paul from-[?]-Paul and bow
  2  [hail] on-of-Paul [laid_his_hands] and put Ananiah of-Lord
  3  name on-Paul because from Paul exist-Paul | of
  4  Lord name carry Paul on-~all_the_world world* exist-Paul | of
  5  Lord name confess Paul and_then holy-Ananiah
  6  Lord how? exist from Saul of-Lord and-~brother-+name | carry
  7  Saul and Saul SUBJ of-Lord and-~brother-+name through
  8  persecute-Saul and two say Lord_God holy-Ananiah
  9  go Ananiah of-Lord servant inside righteous-love drink

## 221v — a table of earthquakes and eclipses

> Before the Spirit, on the Friday, the earth, one quake; on the Spirit, on the Wednesday, the moon eclipsed one hour; and from the year before God, on the Friday, the earth quaked, from the Spirit; the first year from God, the first year, in turn, on the fast | three days before the virgin Mary; on the Sunday the earth quaked; and this, and the day [a sign] [shall appear] upon heaven and earth, living, and confessing, to the letter; and a man [a sign] sees [darkened] [the sun] to, within [the holy church] […] in turn, two years [famine] from the Spirit [pestilence]

  1  before spirit inside Friday earth one
  2  quake on-spirit inside Wednesday moon eclipse
  3  one hour and from year before God
  4  inside Friday earth quake from spirit
  5  first year from God first year in_turn on-fast | three
  6  day before virgin-Mary inside ~Sunday earth
  7  quake and this and day [a_sign] [shall_appear] on-heaven
  8  land living and confess to-literal-to and somebody
  9  [a_sign] see [darkened] [the_sun] to inside [the_holy_church]
 10  °answered-to in_turn two-year [famine] from spirit [pestilence]

## 223r — more of the same table

> the day the earth quaked, out, the first Spirit, Friday; and the years and three days of God, from the Spirit, twenty-two years [a wind] from the Spirit [shall come] the earth quaked, and the moon in turn, upon; and the year, at the beginning, from the Father of a man [the kingdom] from [render to Caesar] whosoever; and [within] in truth believing, the Lord bears the man [shall be saved] believeth not; and this, every one, therefore have mercy, man [shall perish] and the man would, Christ, against, leave; the man, God, learn, the throne [shall be fulfilled] would, whosoever [shall sit] the Lord's throne [shall be saved] truly of the Lord.

  1  day SUBJ earth quake out first
  2  spirit Friday and years* and three_days God from spirit two-two-year
  3  [a_wind] from spirit [shall_come] earth quake and moon
  4  in_turn on and year SUBJ ~begin
  5  from-father of-somebody [heaven] from [render] whosoever* and
  6  [within] inside righteous believe carry-Lord somebody [shall_be_saved]
  7  not_believe and this every therefore-have_mercy somebody [shall_perish]
  8  and somebody want Christ against leave somebody God learn
  9  throne [shall_be_fulfilled] want whosoever* [shall_sit] Lord-throne [shall_be_saved] righteous
 10  Lord-of

## 223v — the date, and the age of the world

> From the leaving of the Lord Jesus Christ to the Lord's Father, out, a thousand years, five hundred and sixty years; and by name, that day, thus, the beginning of the year, written. Twenty-two sons. From [the beginning] then it was, that day, in turn, see; and then the son, Moses [five thousand one hundred and ninety nine] by name, the year, the first day, seven, in turn, from the seeing, two years [a thousand five hundred and sixty] from the understanding, the earth; understanding; the Lord Jesus Christ was born into this world, out, five thousand and a hundred days, and | ninety years, and nine years; and this signifies nine, from the understanding, the beginning of this world, until the Lord Jesus Christ was born into this world; in turn, and from, out, from the understanding, to the leaving of the Lord Jesus to the Lord's Father, eternal, in turn […] the time the apostles said to the Lord Jesus: Master, when shall the judgment day be? Said

  1  from* to-leave Lord-Jézus-Christ from-father of-Lord out
  2  thousand-year five_hundred and six-ten-year and from-+name-~year
  3  this_is begin-year write
  4  two-two-son
  5  from* [the_beginning] then-exist exist [?]-~year in_turn see* [and_then]
  6  son Moses [...] from-+name-year first-~year
  7  seven in_turn of-from-see two-year [a_numeral]
  8  from-understand earth understand be_born Lord-Jézus-Christ
  9  on-this world* ~out five_thousand and hundred-~year and | nine-ten
 10  year and nine-year and this symbolize nine ~hour from-understand begin this world.
 11  until be_born Lord-Jézus-Christ on-this world in_turn and ~hour ~out
 12  from-understand to-leave Lord-Jézus to-from-father of-Lord heaven* in_turn-~brother
 13  time say apostle Lord-Jézus Master when? exist understand judge-~year say

## 222r — when shall the judgment day be?

> [hallowed be] the name of the Lord, of the Lord's Father God. In turn, out [after] two thousand years, to this, the brother, of the chapter, one day; and he has from […] the judgment day; because anew, from the Son of God, judgment; the dead man, the sinful man damned, the sinful man; and saved, the light, said, said the Lord Jesus; this said the Lord's apostles; there is upon a man one, one, to the earth, water, sun, all [shall be shaken] the earth, the sun, Christ, [amen] the Lord God.

  1  [hallowed_be] name of-Lord of-Lord from-God_the_Father.
  2  in_turn-[?]-~out [after] two_thousand to-+this_is
  3  [?]-~brother of chapter one day and have
  4  from covered-+one judge-~year because new-from son God judge
  5  die man^ sin be_damned man^ sin and be_saved
  6  light say say Lord-Jézus this say disciple^ of-Lord exist on-somebody
  7  one one to-to earth water sun every [shall_be_shaken]
  8  earth sun Christ
  9  [amen] Lord_God

## 222v — a calendar, with the writer's own name in it

> [on the holy day] Monday, in the wound, he went, the writer of this book [I went] to the house, the brother, trespassing, he carried, the writer of this book [to the Lord's house] on the Friday, [and then] the writer of this book [to the Lord's house] on the Sunday he went, the writer of this book, to the seal [I went] remitted, at the beginning of the year [to the Lord's house] this, out, one holy Philip's year […] Monday, on the […] he took, the writer of this book, until the beginning of the year; in turn, from the beginning of the year, one in turn [reckoned] [I pray] [my sins] the Lord, have mercy; in turn [my soul] one [reckoned] in turn, in the middle, the man [to the Lord's house] more than these; this said […] the writer of this book [wrote] Friday [I fasted] [lunatic] the writer of this book; this, out, two; Sunday, by name, Sunday three, in turn, two by two; Sunday three, the Lord | Father, Son and Spirit; on the Monday there was [the Holy Spirit] conceived, to

  1  [on_the_holy_day] Monday inside wound go-+the_name_of_the_author-somebody [I_went] to-house
  2  brother-trespass carry-+the_name_of_the_author-somebody [to_the_Lord's_house] inside Friday
  3  [and_then] the_name_of_the_author-somebody [to_the_Lord's_house] inside Sunday go-+the_name_of_the_author-somebody seal-to
  4  [I_went] remit ~begin-year [to_the_Lord's_house] this out one
  5  holy-Philip-year [on_the_feast_of] Monday inside DATE grab-+the_name_of_the_author-somebody
  6  until ~begin-year in_turn from* ~begin-year one in_turn [reckoned]
  7  [I_pray] [my_sins] Lord have_mercy in_turn [my_soul] one [reckoned] in_turn amid
  8  somebody [to_the_Lord's_house] more_than_these* this say °gave-[?] the_name_of_the_author [wrote]
  9  Friday [I_fasted] [lunatic] the_name_of_the_author-somebody this out two Sunday name
 10  Sunday three in_turn-two-two SUBJ Sunday three Lord | father
 11  son-spirit inside Monday exist [the_Holy_Ghost] conceive to

## 224r — the last leaf but one

> ninety-six, little, one […] Michael, on the Saturday, of the woman [the angel] of Mark; he himself took, and [wrote] and two, from two, the mother, on the Saturday [and on] [the same week] on the Saturday, upon good [deed] more than these; upon a man there is, then, upon death, that day, upon the name [one year] [on the day of] [the feast] Matthew, on the Saturday; and lo, one, this is [likewise] Matthew [and on] [the same week] on the Saturday [likewise] [and on] [the same week] understanding, who [at the table] the cup by name; and from a man to this rich good [deed] and one [and a half] three, and one [and a half] three, believe upon this [a portion] [of wine] [a portion] […]

  1  nine-ten six little one-[?]
  2  Michael on-Saturday of-woman [the_angel]
  3  of Mark ~you grab and [wrote] and two from two mother
  4  on-Saturday [and_on] [the_same_week] on-Saturday
  5  on-good [deed] more_than_these* on-somebody exist then-+SUBJ
  6  on-die [?]-~year on-~brother-+name [one_year]
  7  [on_the_day_of] [the_feast] Matthew on-Saturday and lo
  8  one this SUBJ exist [likewise] Matthew [and_on]
  9  [the_same_week] on-Saturday [likewise] [and_on] [the_same_week]
 10  understand-who [at_the_table] cup-+name and from somebody to this rich good [deed]
 11  and one [and_a_half] three and one [and_a_half] three
 12  believe on-this [a_portion] [of_wine] [a_portion] °gave-year

## 224v — the end of the book

> the Lord Jesus Christ, saved; the Lord, wide, [I pray thee] the son, living, of he said; and this man, upon the food, to, in turn, living, the woman, Matthew [and on] on the Saturday, within the seal [this book] Lord have mercy, you, have mercy, of Christ; and through offering, you, have mercy, have mercy, Lord; in turn, the woman [and on] [the same week] and of [the saints] and all, from the leaving […] [the same week] on high; and [into heaven] there is, then, the soul from losing, from riches [at the last] there is [amen] [for ever] from the day, this why; and understanding, the man, the woman, this world, truly, two.

  1  Lord-Jézus-Christ be_saved Lord wide
  2  [I_pray_thee] ~son living-exist of
  3  say and this somebody on-food to-on in_turn
  4  living woman ~Matthew [and_on] on-Saturday inside
  5  seal-chapter [this_book] Lord have_mercy you have_mercy
  6  [?]-~Christ
  7  and through offer you have_mercy
  8  have_mercy Lord in_turn woman [and_on] [the_same_week]
  9  and of [the_saints] and every of-from-leave [...] [the_same_week]
 10  on high and SUBJ [into_heaven] exist then-+SUBJ soul from
 11  lose from-rich [at_the_last] exist [amen] [for_ever] from
 12  day this-why? and understand somebody woman
 13  this world righteous two
