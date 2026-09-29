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
| `word?` | a reading marked uncertain, by Király and Tokai or here; after how, why, who and the like it is the question word |
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
    read                               28532 (95.1%)
    read from one passage, marked *    447 (1.5%)
    restored, in brackets              981 (3.3%)
    dark, printed as an ellipsis       37 (0.1%)

    lines with every word read         3574 of 4372 (81.7%)
    lines complete including
      restorations                     4335 of 4372 (99.2%)

The evidence for every single word is in `harness/proposals.json`, one entry
per sign, with its tier and the argument in full. `harness/ktprov.py` prints
where each reading came from and whether the manuscript itself can ever refuse
it. `harness/ktnull.py` and `harness/ktrederive.py` are the controls,
including the two that failed.

**Brackets are the measure of what is left to do.** Every time a source text
enters the corpus, or a formula turns up twice, some of them become plain
words. There are 981 of them now.

---


## 004v — the beginning: heaven, the angels, Lucifer

> In the beginning there was the Lord God. created one [thing] on the sky, and the earth. The sun and the moon, [as] the scripture(?) [says]. Elijah the prophet. The angel of God said: [the forefather], before he created us. The Father [and] Adam the Lord created. God on the sky, in heaven; and the brethren. Many angels upon angels; and they were to the Father, God, holy angels. Upon the angels two hundred and fifty years and seven, before he created us. The Father, Adam, and an angel, a brother, named — he was Satan — and two angels. And the angel Satan prayed, forty days [and] forty nights which Satan to Satan: upon one heaven, upon, in turn, a brother, upon hell. And the second, said the angel to Elijah: Elijah, and then pray Lucifer, who did [this] — Lucifer, when he was the day he sat on the throne of the Father God; he went to the Father God.

  1  time then Lord God
  2  create one-on-sky and ~earth
  3  sun and moon write
  4  Elijah prophet say angel God
  5  [forefather] before create our
  6  the_father ~Adam create Lord
  7  God on-on-sky heaven in_turn-brother
  8  many ~angel on-~angel and exist to-the_father God on_Holy angel
  9  on-angel two-half-hundred-year seven before create our
 10  the_father ~Adam and angel brother-+name exist Satan and two ~angel
 11  and angel Satan pray and forty days forty nights
 12  which Satan to Satan on-+one-heaven on-in_turn-brother on-hell
 13  and two say angel to-Elijah Elijah and then pray
 14  Satan who do Satan then
 15  day sit on throne the_father God go the_father God

## 004r — the cup

> The angel of the Father said, the Father God, the angel said, that Satan hid the cup. above, of the Father, on the throne; and God said, the angel: Satan hid the cup. above the Lord on the throne; and then the cup Lucifer [stole]; the cup was hidden away above And then from Lucifer the angel returned to the Father. And the angel said: Lord, the cup: Satan [stole] the cup, hid it above; and the two went. God the Father; the angel of the Father [spoke] to Lucifer; Lucifer said: because the cup was hidden away. above with the Father, on the throne; and when Lucifer went to God the angel said: God; the angel; the cup was hidden away above the Lord on the throne; and when the cup Lucifer [stole]; the cup was hidden away above; and then from | hidden. The angel returned, the angel, to God the Father, because there was said Lucifer to the Lord: hidden. The Lord God's mother was born, born, to the Lord, to the Lord, this | hidden. The angel: [proud] Satan was on this throne; and God said, the angel, the Lord: The cup of Lucifer [steal] the cup was hidden away above said Lucifer to the Lord: hidden.

  1  angel of-father say the_father God angel say Satan that cup-to hide
  2  above* of-father on throne and_said God angel Satan cup-to hide
  3  above* Lord on throne and then cup ~Satan [steal] cup-to hide above*
  4  and then from Satan return angel to-father
  5  and_said angel Lord cup Satan [steal] cup-to hide above* and two go
  6  God_the_Father of-father angel to-Satan say Satan because cup-to hide
  7  above* on-of-father on throne and then to-Satan go God
  8  angel say God angel cup-to hide above* Lord on throne and then
  9  cup Satan [steal] cup-to hide above* and then from | hide
 10  angel return angel to-father God because-exist
 11  say Satan to-Lord hide Lord_God mother ~be_born be_born* to-Lord to-Lord this | hide
 12  angel [proud] Satan this on throne and_said God angel Lord
 13  cup Satan [steal] cup-to hide above* say Satan to-Lord hide

## 002r — Michael, the command to bow, and Lucifer's fall

> The mother of the Lord God was born; and Lucifer to the Lord, to the Lord; Lucifer [envied] Lucifer, this one, on the throne [set] of the Lord God; the Lord's finger There was the earth; and the Father, God of heaven, said to Michael: The angels, faithful servants, rose up; and when they had risen, the heavenly one said, the Father of heaven: go to Satan; and Lucifer bowed on the throne of the Lord; and then, within […] one, understand they bowed down — and of the angels every one — to whom Lucifer [would not] bow. And then the Father, God of heaven, saw, and cried out. The Father, God of heaven, left Satan the commandment, because every angel was to whom Satan should bow; and he [refused] to go, said the Father. From he left; this was the angel; he left, up, the year of judgement; and three, the angel said to Elijah the prophet, Elijah said: the Father is. To the Son came the Holy Spirit. The Father and the Son created somebody; and said the Father, the Holy Spirit: in what way? Somebody's form the Father wanted.

  1  Lord_God mother be_born and Satan to-Lord to-Lord Satan [envied]
  2  Satan this on throne [set] Lord_God of-Lord finger
  3  exist earth and_said the_father God heaven Michael
  4  angel believe servant stand_up up and then stand_up
  5  heavenly say the_Father heaven go to-Satan and
  6  Satan bow on throne of-Lord and then inside [?]-+one-understand
  7  bow and from angel every to-which Satan bow
  8  and then see* the_father God heaven and shout
  9  the_father God heaven leave Satan commandment because every exist angel
 10  to-which Satan bow and [refused] to-~go say the_Father from
 11  leave this exist angel leave up ~judge-year and three say angel
 12  to-Elijah prophet Elijah say SUBJ the_Father exist
 13  to-son go holy-spirit father son create somebody and_said
 14  the_Father holy-spirit on-how? somebody form want father

## 002v — the Trinity, and the making of Adam

> The Son, the Spirit, created; and the Son said: in the form, in the Lord. he created [a likeness]: man is, all one, to the Father, the Son, the Spirit. Father, Son and Spirit took man, and every living thing [creature] The soul heard. The man saw the living, truly, not many | Father and Son — not many; the Holy Spirit; but this Lord is all, one God. And God said, the angel, to Elijah the prophet. Elijah the prophet, when there were Father, Son and Spirit, going forth […] […] and the brethren, in this world, and […] | to Paradise the Lord God created man of the slime of the earth; and then man was created of the aforesaid slime of the earth, and became a soul, one. he created, breathed on Adam; and he became living, and the Lord God took the man, and the man went into Eden; and all [things] he created before man.

  1  son spirit create and_said son on-of form on-Lord
  2  create [likeness] exist man^ all^ one to-father son
  3  spirit grab father son spirit man^ all^ living [creature]
  4  soul hear man^ see living righteous not many | from
  5  father from son not many holy-spirit but this Lord all^
  6  one God and_said God angel Elijah prophet
  7  prophet Elijah then father son spirit to-go
  8  table from_the_eternal* in_turn-brother on-this world and out | to
  9  Paradise Lord_God man^ create slime_(of_the_earth)* and then
 10  man^ ~exist create aforesaid slime_(of_the_earth)* and became* to-soul-+one
 11  create breathe on-Adam and living leave and
 12  man^ grab Lord_God and man^ go inside
 13  Eden and all^ create before man^

## 003r — the commandment, and the sleep

> And the Lord God said: Adam, I the Lord take this Adam. every truly [nor] hunger, and thirst [nor] upon Adam; and one living [thing] dies. There shall be sin, hunger, thirst, to the girl … [afterward] the Lord took. To Adam, all truly one. the commandment, this yoke upon Adam, by commandment: do not eat. this to the son: the forbidden fruit — thou shalt die if Adam eats. […] Adam would die. And then Adam slept within | Paradise; and then upon this, fill, first, from the hour; and | then the Holy Spirit came within into Paradise, and said: this this the garden and the Lord God took Adam rib, and Eve he created. The angel said to you: mother. And then Adam, from laughter, said this |

  1  and_said Lord_God Adam I_the_Lord this-Adam grab
  2  every righteous [nor] hunger and thirsty [nor] this-Adam and
  3  one living die sin have hunger thirsty girl-to
  4  [afterward] grab-Lord this-Adam every righteous one
  5  commandment this yoke this-Adam command = not eat.
  6  this to-~son forbidden_fruit thou_shalt_die* ~if Adam exist eat.
  7  on-[?] die-Adam and then Adam sleep inside | to
  8  Paradise and then on-this fill ~first from hour and | then
  9  exist go holy-spirit inside into_Paradise and_said this
 10  SUBJ this the_garden and grab Lord_God Adam
 11  rib and Eve create say angel you
 12  mother and then Adam from laugh* and_said this | to

## 003v — the rib, Eve, and the serpent

> Bone of bone; and the two souls are one. | Before year, by name, and five said the angel. The Lord God departed from heaven | Chapter. year, was; and Eve went into Eden; and | when Eve went to this tree: what tree? was the Lord God's command; and [he] showed one the serpent on this tree: what tree is it? the Lord God commanded; and said this serpent to Eve: eat this fruit; and Eve said: we shall not eat, eat, because, Eve, Adam's Master commanded; and said this serpent: Eve ate, Eve [and] Adam. one this fruit; in turn the fruit was Eve['s]; one Adam ate; Eve [and] Adam knew

  1  bone bone in_turn two soul one | before
  2  ~year-+name and five say angel leave Lord_God from_heaven* | in_turn-chapter
  3  ~year-~exist and go Eve on-Eden and | then
  4  exist Eve go to-this tree what tree
  5  exist Lord_God command = and show^ one
  6  serpent on-this tree what tree exist
  7  Lord_God command = and_said this serpent Eve
  8  ~eat this fruit and_said Eve shall_not_eat eat
  9  because Eve Adam Master command = and_said
 10  this serpent Eve eat Eve Adam
 11  one this fruit in_turn fruit SUBJ exist Eve
 12  one Adam eat exist Eve Adam know

## 001r — good and evil, shame, and back to Elijah

> evil and good, as the Lord God knows. And then they plucked, the serpent, this fruit, this serpent; and | then the day Eve took; in turn Eve took the fruit. Adam. And then were opened immediately; Adam naked. Eve saw Adam; and then Eve [and] Adam was ashamed. And [chapter] six: the angel of God said to Elijah […] Elijah; and this [deadly sin] did Lucifer, the Father of heaven, whom Satan should bow down to | Father God from heaven, and the brethren, hell; and seven said the angel of God to Elijah the prophet: Elijah, the Lord God departed from heaven, land, within Eden, saying

  1  evil and good as Lord-God know and then pluck
  2  serpent this fruit this serpent and | then
  3  day grab Eve in_turn Eve fruit grab
  4  Adam and then were_opened* immediately Adam naked
  5  see Eve Adam and then Eve Adam
  6  be_ashamed and six say God angel to-Elijah prophet.
  7  Elijah and this [deadly_sin] ~do Satan
  8  the_father heaven who-+SUBJ Satan exist bow | father
  9  DIV from_heaven* in_turn-brother hell* and seven say
 10  God angel to-Elijah prophet Elijah leave Lord_God
 11  from_heaven* ~land inside Eden say

## 001v — where art thou

> The Lord God, upon the angel, this fill, two from the hour; and then departed. The Lord God from heaven within into Paradise; and the Lord God said: Adam, why? And Adam said: Adam hid from the Lord God. And the Lord God said: why, Adam, hide? And Adam said: who … this Adam naked? said the Lord God: why, Adam, naked? And Adam said: Eve [gave] Adam food. And said the Lord God: Eve, where? And Eve answered: I … And the Lord God said: why, Eve? Eve answered: who … Eve naked? And the Lord God said: why, Eve, naked? And Eve said: the serpent, Eve, food. And the Lord God said to Adam: to one commandment, this Adam … ten: the commandment observe.

  1  Lord_God on-angel this fill two from hour and then leave
  2  Lord_God from_heaven* inside into_Paradise and_said Lord_God DIV
  3  Adam why? and_said ~Adam hide-~Adam Lord_God
  4  and_said Lord_God why? ~Adam hide and_said ~Adam
  5  who this-~Adam naked say Lord_God why? ~Adam
  6  naked and_said Eve Adam food and_said.
  7  Lord_God Eve where? and_said answered* Eve I-to
  8  and_said Lord_God why? Eve answered* who Eve naked
  9  and_said Lord_God why? Eve naked and_said Eve
 10  serpent Eve food and_said Lord_God ~Adam
 11  to-one commandment this ~Adam name-[?]-ten commandment observe

## 007r — the curse, and the sword at the gate

> Adam was, the girl … Adam, in turn hands gates Adam was; the earth to till he wants food for the son, to take, in turn Eve, this Eve through yearning; and this Eve is in pain. [to be] born, has; in turn this evil — this evil is [cursed] the earth slide and room evil. Man was made, all of this. The serpent dies; and he departed from among Adam and Eve the Lord God; and there went the Lord God, the angel; Adam and Eve; flame, a sword; and Adam and Eve out | within Paradise. He drove them out, and set an angel sword

  1  exist ~Adam girl-to [?]-~Adam in_turn hands
  2  gates* exist ~Adam earth till_the_earth
  3  want to-~son food ~grab in_turn Eve this-Eve
  4  exist through pine and this-Eve exist painful
  5  ~be_born have in_turn this evil this-evil exist
  6  [cursed] earth slide ~and room
  7  evil this man^ create every this serpent die and
  8  leave among Adam_and_Eve Lord_God and go
  9  Lord_God angel Adam_and_Eve flame^
 10  sword and Adam_and_Eve out | on-inside
 11  Eden exorcise and put angel sword

## 007v — outside the garden: Cain, Abel, Seth, and Adam goes blind

> at the gate Eve, Eden; and one creature can be within Eden, but the angel. And the Lord God said, upon the angel, this fill, three from the hour, and from two-two-two-two said | to Elijah. The angel of God: Elijah, when the Lord God [drove] Adam out […] from Paradise; and then | Eve he dwelt in the field many years; and Adam had Eve offspring, these two sons. And the firstborn was Cain, and the second … named, was Abel. Third, by name, was Seth. And then Adam was blind from the eyes; and then Adam went into Paradise the son […]; and this son was [Cain] the son [Abel] Adam. And then Adam said: bring, Adam, from the tree.

  1  on-~gate Eve Eden and one create
  2  can_be inside Eden but angel and_said Lord_God
  3  on-angel this fill three from hour and from two-two-two-two say | to
  4  Elijah God angel Elijah then Lord_God ~Adam
  5  out cast_out on-Eden and then | two-+name-donkey
  6  Eve leave inside ~field many year and ~have ~Adam Eve
  7  descendant this-two to-son and firstborn exist Cain and two before-end-+name exist
  8  Abel third ~name exist Seth and then
  9  ~Adam from eyes blind and then go ~Adam inside Paradise
 10  son of-~Adam and this son exist [Cain] son [Abel]
 11  ~Adam and then say ~Adam bring ~Adam from tree.

## 006r — Seth goes to Paradise for the branch

> a branch. And then the branch to Adam he carries, immediately through seeing; and then through seeing, immediately, through the eye, blind Adam sees; and to heal Adam [sick]; and then Seth went | [to Paradise] the gate of Eden; and then to Seth appeared God's angel; and God's angel said: Seth [answered], and went; one said, Seth: the father Adam, Seth goes into Eden | then there was father Adam; Seth carried from the tree a branch on the tree of mercy was Adam, the father; [he] committed sin; and Adam said, Adam, then the seed Seth carried, immediately through seeing; and then through seeing, immediately, through the eye, the blind sees; and Adam was made whole. And the angel said: truly speak; and then the angel went into Paradise, and Seth carried the branch

  1  one ~branch and then branch to-~Adam carry immediately through
  2  seeing and then through seeing immediately through eye see blind ~Adam
  3  and be_healed = ~Adam [sick] and then Seth go | [to_Paradise]
  4  gate/open Eden and then Seth appear God
  5  angel and_said God angel Seth [answered] and go one say Seth
  6  the_father ~Adam Seth SUBJ go inside Eden | then
  7  exist father ~Adam carry Seth from tree branch
  8  on-+the_tree_of_mercy SUBJ exist father ~Adam commit sin and say ~Adam
  9  ~Adam then seed carry Seth immediately through
 10  seeing and then through seeing immediately through eye see blind ~and
 11  be_healed = ~Adam and_said angel righteous SUBJ speak and then
 12  go angel inside Eden and Seth carry branch

## 006v — the branch brought home, and a city

> out of Paradise, from tree […] Adam was, through sin. And then Seth took from the angel this branch; and then the branch Seth carried to Seth's father Adam. And then Seth went into a town, and the town was named Jericho, where Adam was, a house. And then he came [the way] recognize; and within, all from the town [the way] recognize; and then out of the town one [road]; and then Seth went, this [one, a name] and within [the way] recognize; and then Seth said, one the one Seth met oh, of Seth, the Father, the Spirit, the Father recognize Adam. And Adam's eyes were blind — Adam, whom the Lord God's, cast out out of Paradise by the angel; and then [the one, a name] from seeing the gospel; and found [the one, a name]; ten, two, two, ten years; and

  1  on-Eden from tree on-+tree exist ~Adam through
  2  sin and then Seth ~exist ~grab angel this branch
  3  and then branch Seth carry to-of-Seth father
  4  ~Adam and then Seth go inside one town
  5  and believe-end-+name town exist Jericho who exist ~Adam
  6  house and then arrive can [the_way] recognize and inside every from
  7  town can [the_way] recognize and then out town
  8  one [road] and then Seth exist go this NAME
  9  and inside can [the_way] recognize and then Seth say one
 10  NAME oh of-Seth the_father spirit father SUBJ recognize
 11  ~Adam and ~Adam exist eyes blind who ~Adam exist Lord
 12  God out cast_out on-Eden on-angel and then NAME
 13  from-see gospel and find NAME ten-two-two-ten-year and

## 008r — Noah and the ark

> seven And then three at that time the Lord God appeared to Noah; and then the Lord God said: Noah, sorrow, Lord, leave, who, somebody, of them, leave; that he had made them, because [flood] he who keeps his commandment. The Lord God would have all destroyed. And the Lord God said: Noah, make one … the Lord | […] was the Lord; it was forty cubits long; in turn three hundred broad, in turn five high; one hid. Noah took every creature two by two; and [inside] the ark. And then this [dove]: I, this Noah, go, Lord. And then Noah took every creature two by two, and went before the Lord God; and within was the Lord God, to the cup; and to the Lord lost, and [drunken] the Lord God; every four directions; the water dispersed, fifth, from heaven high and the rain came, forty; and five towns were destroyed. The Lord God; and the angel of God said [to] Elijah: the Lord God was [with] Noah; Noah remain all this [three] was; and the other [sons] departed; and this

  1  seven and then three time appear Lord_God Noah
  2  and then and_said Lord_God Noah sad-Lord leave who somebody on-of leave*
  3  create because [flood] this who carry of commandment ~exist Lord_God want every
  4  destroy and_said Lord_God Noah do one exist Lord | [...]
  5  ~exist Lord exist on-two-two-ten cubit long in_turn three_hundred*
  6  broad in_turn five high one-hide grab Noah every create two-DISTR-two and
  7  [inside] of-ark and then this [dove] I this-Noah go-Lord
  8  and then Noah grab every create two-DISTR-two and go before Lord_God
  9  and inside-~exist Lord_God to-cup and to-Lord lose* and [drunken]
 10  Lord_God every two-two direction water disperse fifth from_heaven* high
 11  and go rain forty and five town destroy
 12  Lord_God and_said God angel Elijah say exist Lord_God Noah
 13  Noah remain* every this [three] exist and two [sons] leave and this

## 008v — from Noah to Abraham

> the people were, until Abraham the forefather were pagans believed. From Noah it was, until Abraham, seven … And said the angel of God to Elijah the prophet: Elijah, among these believe. One man was saved in that time. The angel departed from before Elijah the prophet; and these said Elijah the prophet wrote; and [holy Enoch] […] within one chapter Elijah of the writing.

  1  people exist until Abraham forefather were_pagans* believe
  2  from Noah exist until Abraham seven-[?] and_said
  3  God angel to-Elijah prophet Elijah inside these
  4  believe one somebody ~be_saved inside time
  5  leave angel before Elijah prophet and these say
  6  SUBJ write Elijah prophet and [holy_Enoch] prophet.
  7  inside one chapter Elijah* of-write

## 005r — Abraham and Isaac

> […] and the son went [with] the father | the father; and a sheep, and a lamb. … the son; the father [would] sacrifice. And the father Abraham said: for love of the Lord, to hide, the Lord, the Lord God's offering. And then Isaac was tie up […] who was [ram] Isaac [instead] name Abraham sacrificed, and drew out […] […] […] […] Isaac he would slay; and the Lord God cried out from the cloud, by the angel of the Lord God, Stop, Abraham! … will this. Abraham. The Lord God. Love the Lord. this is peace to the Lord. And then he looked up and saw, Abraham, and saw […] a lamb in a thornbush.

  1  donkey* and go-son-father | son*
  2  father and one sheep and one lamb
  3  who-~exist son father sacrifice and_said father Abraham
  4  from love Lord to-hide-Lord Lord_God offering and then Isaac
  5  exist tie_up on-+pierce who exist [ram] Isaac [instead]
  6  name Abraham sacrifice and take_out on-+name
  7  understand-girl-chapter sword who Isaac want slay
  8  and shout Lord_God on-cloud on-angel of-Lord_God
  9  stop Abraham-to will SUBJ who this.
 10  Abraham Lord_God love Lord
 11  this_is to-Lord peace
 12  and then from see look_up
 13  Abraham and see
 14  understand-eat ~lamb
 15  on-understand-eat bush

## 005v — the ram, and a prophecy of Christ

> And then, from the lamb sacrifice, the Lord God said from the cloud, from the angel of the Lord, to Abraham: born within of Isaac one holy Mary; from the Virgin Mary a son born, to whom The son is the body, Jesus; and the Lord went among the people He preached the gospel, did many various miracles, and the Lord suffered crucified; and on the third day rose from the dead. And the Lord God said, from the angel, to Abraham: and from seeing, the Lord's chapter is believe truly [in] the Son of the living God; every man is saved […] One man […]; but every man is saved [from] the yoke; and man […] the Lord […] believes; and one […] […] but every man was damned, from Adam, trespass, table, until Abraham, a hundred years and twenty years; from Abraham [until] Moses one thousand five hundred and fifty from Abraham until

  1  and then from lamb sacrifice and_said Lord_God on-cloud
  2  on-angel of-Lord Abraham say ~be_born inside of Isaac
  3  one holy-Mary from virgin-Mary on-be_born son to_whom
  4  son exist ~body Jesus and go Lord among_the_people*
  5  exist gospel preach many various miracle ~do
  6  and suffer Lord crucified and on_the_third_day from die stand_up-Lord
  7  and_said Lord_God on-angel Abraham and from-and-see chapter-Lord exist
  8  believe righteous son living God everybody = be_saved and.
  9  one somebody not_damned but everybody = be_saved yoke and
 10  somebody Lord not believe and one not be_saved.
 11  but everybody = be_damned from ~Adam ~trespass table until Abraham
 12  one hundred-year and ten-ten-year from Abraham SUBJ table [until]
 13  Moses half-+three_thousand and fifty from Abraham until

## 015r — David the king

> did; David the king humbled himself against the Lord God. The king began repentance, did; anointed king [of] the Lord God. have mercy; and the king's sin — have mercy. At that time there appeared to the king the angel of God; and the angel of God said [to] David the king: the Lord God The king sin, have mercy. The king keeps the Lord's commandment; and the Lord confirmed the king on the king's throne; and the king proclaimed [it to] the people. [the Lord] there shall be born say a son [of David]; the son shall be the Son of God. And the angel departed from before David […] From David the king until the Virgin Mary, born, years: … out, half … and … hundred years, and one hundred years out, nine hundred and one hundred years | two, two, two ten years and five, from David the king until the Virgin Mary

  1  ~do David king humble against Lord_God.
  2  repentance begin king ~do anointed king Lord_God.
  3  have_mercy and sin king have_mercy time appear king
  4  God angel and_said God angel David king Lord_God
  5  king SUBJ sin have_mercy carry-king of-Lord commandment and
  6  confirm-Lord king SUBJ on-of-king throne and announce king people
  7  [the_Lord] on-be_born host say son [of_David] son exist son
  8  God and leave angel before David king.
  9  from David king until Virgin_Mary be_born-~year
 10  ~out-half-to-[?] and [?]-hundred-~year and one hundred-~year
 11  ~out nine_hundred and one hundred-~year | two-two-two
 12  ten-~year and five from David king until Virgin_Mary

## 015v — the count of years

> the years: from Adam's trespass, out, until the Virgin Mary | was born, years: five thousand and one hundred years and fifty and four years, and four years.

  1  be_born-~year from Adam ~trespass ~out until Virgin_Mary | be_born
  2  day five_thousand and one hundred-~year and fifty
  3  and two-two-year and two-two-year

## 016r — Saint Luke

> Saint Luke writes, the sixth throne of his writing, from, remain, kiss(?). exist […] they gave thanks, and prayed to the Lord God.

  1  write holy-Luke six-throne of-write from remain* kiss?.
  2  exist* holy-in_turn-+one-[?] give_thanks = and pray to-Lord_God

## 016v — Joachim's offering is refused

> And Saint Anne …; of the two of them, all their riches divided in three parts: one division they gave to the people of the temple; a second division to the Lord's way-people; the third division Joachim and his household lived on. And all Joachim's household gave thanks, thanks, to the Lord God; in turn had | Joachim his household, born thirty years; and he prepared the offering. it is the chapter: every one of … creatures; and then, and from Joachim he brought his offering; and at Joachim looked the chief the Jews; and this high priest said [to] Saint Joachim: food, this Joachim, [the temple], who … Joachim goes among the neighbours; the food of the offering, [the temple], one [portion] and Joachim [is] cast out of this temple; and sorrowfully Joachim departed, and went into the field, into the forest, … from the shepherd and from the sheep, the shepherd, and on one mount, one

  1  and holy-Anne mouth-~year from-two from_both every of-rich divide on-+three part
  2  one division grab to_the_people_of_the_temple = second division
  3  from-Lord way people third division Joachim-+one-+his_household living.
  4  and every Joachim's_household thanks thanks Lord_God in_turn have | Joachim
  5  his_household ~be_born thirty year and prepare offering
  6  exist-chapter every of-in_turn-+one-[?] creature and then and from Joachim
  7  carry of offering and to-Joachim see from head
  8  Jew and_said this high_priest = holy-Joachim
  9  food this-Joachim [the_temple] who Joachim* go
 10  among of neighbor food of offering [the_temple] one [portion]
 11  and out Joachim cast_out on-this temple and sad
 12  Joachim leave and go inside field inside forest chapter-of from shepherd
 13  and from sheep shepherd and on-one mount one

## 017r — the angel comes to Joachim

> a lamb sacrifice; and then the lamb sacrifice [rejected] At that time, when Joachim was appear God [in the desert] And the angel of God said: Joachim, … heard [the Lord God] … prayer; and the angel of God said: Joachim, this [hath had mercy] The Lord God has had mercy. Go home, Joachim; and at the golden gate — this Joachim departed — Joachim's wife Anne, and conceived one: the Virgin Mary. And then she is born, and [shall conceive] The Virgin Mary is Mary; and Mary remits, bears a son, whose The son shall be, by name, Jesus; and the Lord went among the people He preached the gospel, did many various miracles, and suffered, the Lord crucified; and on the third day rose from the dead; and ascend shall be saved, every one in all the world; and the man who believes in the Lord. And the angel departed from before Saint Joachim; and at that time the angel appear

  1  lamb sacrifice and then lamb sacrifice [rejected]
  2  time then Joachim exist appear God [in_the_desert]
  3  and_said God angel Joachim have hear [the_Lord_God]
  4  of-~pray and_said God angel Joachim this [hath_had_mercy]
  5  Lord_God have_mercy go Joachim to-home and on-golden
  6  gate this Joachim leave of-Joachim wife Anne and conceived*
  7  one Virgin_Mary and then ~be_born and [shall_conceive]
  8  Virgin_Mary exist Mary and remit Mary on-be_born son whose.
  9  son exist ~name Jesus and go-Lord among_the_people.*
 10  exist gospel preach many various miracle do and suffer
 11  Lord crucified and on_the_third_day from die stand_up-Lord and ascend* be_saved
 12  every all_the_world world and somebody Lord exist believe and leave angel
 13  before holy-Joachim and time then angel appear

## 017v — the golden gate, and Mary carried nine months

> the angel of God [to] Saint Anne: […] this Anne, […] the Lord God has had mercy, has heard the Lord God, Anne's prayer. Go home, Anne; and at the golden gate Anne left the Lord's Joachim, and conceived one: the Virgin Mary. And then was born the body, the Virgin Mary — she is Mary; and Mary remits, bears a son, to whom the son is, and the body, Jesus; and the Lord went among the people; he preached the gospel, [did] many various miracles; and the Lord suffered crucified; and on the third day from death the Lord rose; and ascended; saved every one in all the world; and the man who is the Lord's believes. And the angel departed from before Saint Anne; and she conceived the blessed Virgin Mary. And Mary carried the child nine months, in turn ten, the child was born; and this out, two months; and on out, five; and at six years out, from Adam's trespass until the Virgin Mary was conceived and born: five thousand and one hundred and fifty and

  1  God angel holy-Anne have this Anne SUBJ Lord_God have_mercy hear
  2  Lord_God of-Anne ~pray go Anne to home and
  3  on-golden gate leave Anne of-Lord Joachim and conceive one
  4  Virgin_Mary and then be_born body Virgin_Mary exist Mary
  5  and remit Mary be_born son to_whom son exist and-body
  6  Jesus and go Lord among_the_people* exist gospel preach many various
  7  miracle do and suffer Lord crucified and on_the_third_day from die
  8  stand_up-Lord and ascend* be_saved every all_the_world world and somebody Lord exist
  9  believe and leave ~angel before holy-Anne and conceive happy
 10  Virgin_Mary and from Mary foetus carry nine moon in_turn ten foetus be_born and this
 11  out two moon and on-out five and on-six-year-to
 12  ~out from Adam ~trespass until Virgin_Mary conceive and on-be_born.
 13  five_thousand and one hundred and fifty and

## 018r — Gabriel: Hail, full of grace

> [Five] months, until the offering in the temple, the blessed Virgin Mary. And then Mary was [at] three [years] in the temple; from the beginning she went and hid in the temple. […] and said […] that Mary would keep her virginity | Of Mary, created. For ever and ever, amen. And then Mary was twelve, the feast, and … three days; and at that time opened the Father of heaven, because he saw hidden every world, darkness, the sky. And at that time the Father of heaven opened, and went. the Lord's angel Gabriel, in the temple, to the blessed Virgin Mary. Saint Luke writes chapter in his writing: at that time the angel said, Gabriel: Hail, this Virgin Mary, full of grace! Out, the Lord God, Mary. And said this Virgin Mary: How can this be, this maiden knowing not … this maiden? … this maiden wants, the Virgin Mary, to keep … of the maiden, created … For ever and ever, amen. And the angel Gabriel said [to] Mary:

  1  half-ten moon until offering inside temple blessed^ Virgin_Mary
  2  and then Mary exist inside three from begin go-hide-this inside temple
  3  [?]-+one and say [?]-+one this-Mary want virgin-carry | of
  4  Mary create for_ever_and_ever = amen and then Mary
  5  exist six-six feast and [?]-+three and time open
  6  the_Father heaven because see hide every world darkness sky.
  7  and time open the_Father heaven and go.
  8  of-Lord angel Gabriel inside temple blessed the_Virgin_Mary*
  9  write holy-Luke chapter* of-write time say angel
 10  Gabriel healing this-Virgin_Mary full_of_grace out Lord_God-Mary and_said
 11  this Virgin_Mary how? this exist can this-girl not_know this-girl
 12  half-be_damned this-girl want Virgin_Mary carry of-girl create-[?]
 13  for_ever_and_ever = amen and_said angel Gabriel Mary

## 018v — the Holy Spirit, and Elizabeth six months gone

> has wanted, to the girl, this: the Holy Spirit goes; to every [one] mercy [full of grace] This maiden shall conceive a son; and the son's body is Jesus. And the Virgin Mary said, blessed, to one: this, say it; and blessed be the will from the Lord God. this [power] the Lord, this overshadow; and then the maiden [answered] the Virgin Mary; the word of command to the Lord; Mary hid, this overshadowed, which maiden the angel said; at this he said: God the Father pours out on the Virgin Mary | the Holy Spirit; in turn to the Lord [came upon] one; went the Lord Jesus Christ, conceived, the Lord Christ. And then [departed from] the Virgin Mary. And the angel Gabriel said: [to] Mary: Behold, thy kinswoman is six months gone | Elizabeth, who conceived; Mary; the son, Saint John [barren] within the chapter […] chapter; the Lord God's mercy to this […]; from John shall be the way done [for] the Lord Jesus Christ, that is, the Lord [according to thy word] this Mary bore; and from the Lord went the Lord on the world; [he] is the Word, preaching

  1  have want to-girl this go holy-spirit to-every have_mercy [full_of_grace]
  2  this-girl conceive son and ~son ~body exist Jesus.
  3  and_said Virgin_Mary blessed one-to this say and blessed want from Lord_God.
  4  this [power] SUBJ Lord this overshadow* ~and then girl [answered.]
  5  Virgin_Mary commandment word to-Lord-hide Mary hide this overshadow* who girl
  6  exist angel say on-this say pour_out God_the_Father Virgin_Mary | holy
  7  spirit in_turn to-Lord [came_upon] one go Lord-Jesus-Christ conceive Lord
  8  Christ and then [departed_from] Virgin_Mary and_said angel Gabriel
  9  Mary have lo out six month^ of-girl relative | holy-+name-chapter
 10  Elizabeth who conceive Mary son holy-John [barren] inside chapter SUBJ
 11  go chapter Lord_God of have_mercy to-this have from John exist way
 12  do Lord-Jesus-Christ that_is Lord [according_to_thy_word] this
 13  Mary be_born and from Lord go Lord on-+world exist Word^ preach

## 019r — Joseph

> various miracles done; and the Lord suffered; the Jews crucified [him]; and the man who believes in the Lord, that [he is] the righteous the Son of the living God — every man be saved; and one man is damned; and the Lord not believe; and one be saved but who believes not a man is damned. Here ends this holy gospel. And at that time the angel was appear; the angel of God aged Joseph; and the angel of God said: aged Joseph. Go, aged one Joseph in the temple, Joachim, the girl Mary, and this aged Joseph was [already] aged […] of the son, well-pleasing, from Mary, on being born; and then the son shall be born and the body; the son is Jesus; and from the Lord went among the people; is the gospel preached, various miracles done, and the Lord suffered [death]

  1  various miracle ~do and suffer Lord Jew
  2  crucified and somebody to-Lord exist believe that righteous
  3  son living God everybody = be_saved and one somebody
  4  be_damned to and Lord not believe and one to
  5  be_saved but who_believes_not* somebody be_damned here_ends this holy_gospel
  6  and time then angel exist appear God angel
  7  aged Joseph and_said God angel aged
  8  Joseph go aged Joseph.
  9  inside temple Joachim* girl Mary and this aged.
 10  Joseph exist [already] aged Joseph-+cross-girl-+mouth
 11  from son to-pleasing from Mary on-~be_born and then ~son on-be_born
 12  and-~body ~son exist Jesus and from Lord go among_the_people* exist
 13  gospel preach various miracle do and suffer Lord [death]

## 019v — the census of Augustus

> the Jews crucified; and the man who believes in the Lord, that truly the Son of the living God — every man is saved; and the first man is damned; and the Lord not believes; and the first be saved but who believes not a man is damned. Here ends this holy gospel. And then out, the blessed Virgin Mary was sixteen years, at that time. There was a decree, before […] the Lord Jesus Christ, twenty and | two years; and on the birth, the first day, the Lord Jesus Christ; and. At that time Augustus the emperor commanded that all the world should be enrolled. And then the commandment of Augustus the emperor: all the world go back, the commandment, to the town. And | then it was, the two of them, Mary and aged Joseph, went | home And then the two, Mary and aged Joseph, took the first ox and the first

  1  Jew crucified and somebody to-Lord exist ~believe that.
  2  righteous son living God everybody = be_saved and first^
  3  somebody be_damned to and Lord not believe and first^
  4  to be_saved but who_believes_not* somebody be_damned here_ends this holy_gospel
  5  and then out happy Virgin_Mary ten-six-year time.
  6  exist commandment before ~be_born Lord-Jesus-Christ ten-ten and | two
  7  two-year and on-~be_born first^ day^ Lord-Jesus-Christ and.
  8  time command Augustus emperor that
  9  all^ world exist enrol and then commandment Augustus
 10  emperor all^ world back go commandment town and | then
 11  exist and from two Mary aged Joseph go | to
 12  home* and then two Mary aged Joseph
 13  exist grab first^ ox and first^

## 020r — no room, and a manger

> donkey; because this they took, aged Joseph the ox, the two of them — aged Joseph and Mary exist remain [together] the two of them, the aged […] remain and the donkey was aged Joseph's; he took her who would bear this son | Mary and aged Joseph took her away on the donkey; and then the two. aged Joseph, when he arrived | the aged Mary and Joseph, [at] Bethlehem town; and […] aged Mary and Joseph can [not] find lodging. none; but the two of them, Mary and aged Joseph, lodged within the first barn; and [manger] […] the first manger; and then bought, the aged [one]. Joseph hay; and then the ox

  1  donkey because this exist grab aged Joseph
  2  from ox who two aged Joseph Mary
  3  exist remain* [together] who two aged Joseph.
  4  remain* exist in_turn donkey exist aged Joseph
  5  grab who this son on-be_born want | aged-Mary
  6  Joseph on-donkey take_away and then two.
  7  aged Joseph exist from arrive | aged
  8  Mary-Joseph Bethlehem town and [arrived]
  9  can aged-Mary-Joseph lodging find
 10  but leave two aged-Mary-Joseph inside first^
 11  barn and [manger] aged-?Joseph-Mary-+mouth.
 12  first^ manger and then buy aged.
 13  Joseph hay and then two ox

## 020v — the birth, the star, and the angel's news

> and the donkey; he laid the hay; and then the aged | the girl … a fire, the light begins; and then shoulder … half. in the night the son was born; and the son was and the body, Jesus. At that time sky star light through Bethlehem town; and then a star the shepherds saw; and from the sheep, the shepherd; and then at the star, a miracle. At that time the angel Gabriel said: great joy! A king is born, a king born in Bethlehem town, within barn, in a donkey's manger. [the ox], the donkey, love; hay within [the manger] [laid] Christ, Mary's son. And then […] went [to] Bethlehem; and then the sheep knelt, and every one of them knelt before the shepherds [hastened] to go another and […]

  1  donkey exist hay put and then aged | Joseph*
  2  girl-+mouth ~fire begin-light ~and then shoulder-to half.
  3  night time on-be_born son and son exist
  4  and-~body Jesus time then sky star
  5  through bright^ Bethlehem town and then star
  6  see the_shepherds and from sheep shepherd and then
  7  on-star miracle time say angel Gabriel great
  8  joy be_born king king SUBJ be_born inside
  9  ~Bethlehem town inside barn inside donkey manger
 10  [ox] donkey love hay inside [manger] [laid]
 11  Christ Mary son and then the_shepherds go Bethlehem
 12  and then sheep kneel and every this exist kneel
 13  before from the_shepherds [hastened] to go another and to-Lord.

## 021r — the reckoning of years

> gave thanks, and gave thanks. Here ends this holy gospel [amen] Saint Luke writes, in one [then] of his writing, chapter [of the book] [the reading] out, from Adam's trespass, until the birth of the Lord Jesus Christ. five thousand and one hundred years and sixty years and six years, until the birth of the Lord Jesus Christ.

  1  thanks and give_thanks = here_ends this holy_gospel [amen]
  2  write holy-Luke inside one [then] of-write chapter [of_the_book] [the_reading]
  3  out from Adam ~trespass until be_born Lord-Jesus-Christ.
  4  five_thousand and one hundred-year and sixty
  5  and six-year until be_born Lord-Jesus-Christ

## 021v — the flight into Egypt, and the eighth day

> At that time then, a fast, on the birth of the Lord Jesus Christ, three, at that time the angel Gabriel said to the aged Joseph: Rise up, and take this son and his mother, this son […] and flee into Egypt, and go, all this, begin [by night]; out of Egypt [into] this; the angel [appeared] said day [Herod] Here ends this holy gospel. At that time rose up the aged | Joseph [arise] and took the Lord Jesus Christ and his mother, and five days passed; then | [the Son, and the aged Joseph, and the holy mother Mary] year, Joseph, chapter; [they] went into Jerusalem town, that is, when was born the Lord Jesus Christ; on the eighth year, at that time, the son was circumcised, and the son was named Jesus. And this Lord Jesus first man, the Lord's blood shed; and then the Lord. circumcised the Lord Jesus in the Jerusalem temple; and fled Mary his mother the Holy Spirit and Joseph

  1  time then fast on-be_born Lord-Jesus-Christ three
  2  time say angel Gabriel aged Joseph
  3  stand_up up and take^ this son and of this son mother.
  4  and escape inside Egypt and go every this begin [by_night]
  5  out-out Egypt [into] this this angel [appeared] say day [Herod] end
  6  this holy-gospel time stand_up up the_aged | Joseph
  7  [arise] ~and take^ Lord-Jesus-Christ and of mother and five
  8  day^ pass then | [the_son_and_the_aged_Joseph_and_the_holy_mother_Mary]
  9  ~year-+Joseph-chapter go inside Jerusalem ~town that_is on-be_born
 10  Lord-Jesus-Christ on-six-two-year time circumcise son
 11  and son exist and-from-~year-exist-+name Jesus and this Lord-Jesus first
 12  man* of-Lord blood shed and then Lord.
 13  circumcise Lord-Jesus inside Jerusalem temple and escape
 14  Mary_his_mother_the_Holy_Spirit_and_Joseph*

## 022r — Egypt, and the twelve

> into the land of Egypt; and [dwelt]; and the Lord went Joseph in the land of Egypt, into every city [idols] […] evil fell, bowed down; and | … mother … Joseph. [arise]; die … from Joseph; they remained in Egypt twelve years. at that time the angel Gabriel said Joseph Flee into the land of Egypt, into Nazareth city. And … mother … Joseph … left for Nazareth. [in that] town twelve years; and five; and this [returned] table twenty, two, nine years. Here ends this holy gospel. One day; he called twelve apostles; and three years preached; and | who, this and this miracle did: the blind eye the Lord, through light; the dead the Lord resurrects; the evil among the people the Lord drives out.

  1  inside Egypt earth and [dwelt] and go Lord Joseph
  2  on-Egypt earth inside every town [idols] hell.
  3  fall* evil bow_down and | [?]-mother-?Joseph.
  4  [arise] die from Joseph leave inside Egypt six-six-year
  5  time say ~Gabriel angel Joseph.
  6  escape on-Egypt earth inside Nazareth town
  7  and [?]-mother-+Joseph-chapter leave Nazareth.
  8  town six-six-year and five and this [returned] table
  9  ten-ten-two-nine-year here_ends this holy_gospel one
 10  day call six-six apostle and three_years preach and | who-this
 11  and-this miracle ~do eye blind SUBJ Lord through
 12  light die SUBJ Lord resurrect evil inside people exorcise-Lord

## 022v — the signs, numbered

> Before, that is, the Lord made wine of water; after these the Lord broke five loaves of bread [for] five thousand people. The second-two sign the Lord Jesus showed, when | in Nain. before the town he raised up, from a widow, the son. The fifth sign the Lord Jesus showed, when he raised up the girl, lost. within Jerusalem. The sixth sign the Lord Jesus showed within the first town, when the Jews brought the first sick man before the Lord Jesus: a sick man, and a sick man, and a sick man, and a paralytic; and the sick, the sick, the sick, the paralytic — the Lord Jesus healed; in turn, seven The sign the Lord Jesus showed within Capharnaum, because [he] raised from the dead two servants of the first soldier; and the soldier was named: the centurion The eighth sign the Lord Jesus showed within Tyre town: the girl, the first woman, a head.

  1  before that_is SUBJ Lord wine made water after_these SUBJ Lord
  2  break five loaves bread five_thousand people
  3  second-two can show Lord-Jesus then | in_Nain.
  4  before town resurrect from virgin-~woman son fifth
  5  can show Lord-Jesus then resurrect girl lose*
  6  within^ Jerusalem in_turn-six can show Lord-Jesus within^ first^
  7  town then Jew carry first^ ill
  8  before Lord-Jesus sick_man and sick_man and sick_man and paralytic
  9  and sick_man sick_man sick_man paralytic heal Lord-Jesus in_turn-+seven
 10  can show Lord-Jesus within^ Capharnaum because raise_from_the_dead =
 11  two servant first^ soldier and name soldier.
 12  exist the_centurion in_turn-six-two can show Lord-Jesus
 13  within^ Tyrus town girl first^ ~woman head

## 023r — the ninth, tenth and eleventh signs

> a pagan; and within the girl was a devil; and the evil [one] the Lord drove out. The ninth sign the Lord Jesus showed in | … a proud man paralytic because the man […] did. The tenth sign the Lord Jesus showed in Galilee: a king's son, because he was at the point of death; and the son […] did. And [the next] sign the Lord Jesus showed in Jerusalem: the evil spirit, when the Lord cast a devil out of one man. First, before the birth of the Lord Jesus Christ, the Son of God cannot a prophet, a forefather, this […] did as Christ did; and by miracle they confessed that the Lord Jesus is truly the Son of God. five confessed […] the Lord Jesus that the Lord Jesus is truly the Son of God. First confessed … the Lord Jesus: Moses and Elijah. The second confessed

  1  one pagan and inside girl exist devil = and evil^
  2  out exorcise-Lord in_turn-nine can show Lord-Jesus inside | exist.
  3  proud on-one paralytic man^ because man^ healing.
  4  do in_turn-ten can show Lord-Jesus inside Galilee
  5  one king son because exist on-die and son healing.
  6  ~do in_turn-and can show Lord-Jesus inside Jerusalem evil^
  7  then Lord inside one man^ devil = exorcise
  8  first before be_born Lord-Jesus-Christ son God cannot.
  9  one prophet one forefather this miracle.
 10  ~do as Christ ~do and miracle confess
 11  that Lord-Jesus righteous son God five confess ~have.
 12  Lord-Jesus that Lord-Jesus righteous son God first confess
 13  ~have Lord-Jesus Moses and Elijah second confess

## 023v — who confessed him, and the Transfiguration

> … the Lord Jesus: the Father of the Lord. The third confessed the devils, that the Lord Jesus is truly the Son of God. The second-two confessed the Lord Jesus — the angel, that the Lord Jesus is truly the Son of God. Fifth They confessed […]; and the earth, the sun, the moon, that the Lord Jesus is truly the Son of God; and all this confessed. that the Lord Jesus is truly the Son of God. First confessed it Saint Peter, Moses and Elijah. Saint Luke writes that when the Lord Jesus was thirty years, at that time the Lord Jesus went […] [to] Mount Tabor with his apostles; and he was transfigured; and the disciples saw Moses and Elijah [in] white clothes, and they saw the light [from heaven]; and then there stopped | the Lord Jesus, and Moses and Elijah; and then the apostles, through took fright, down [fell], bowed; and then the disciples, the voice.

  1  ~have Lord-Jesus the_Father of-Lord third confess devil =
  2  that* Lord-Jesus righteous son God second-two confess ~have
  3  Lord-Jesus angel that Lord-Jesus righteous son God fifth
  4  confess sky and earth sun and.
  5  moon that Lord-Jesus righteous son God and this every confess.
  6  that Lord-Jesus righteous son God first confess holy-Peter
  7  Moses and Elijah write holy-Luke then
  8  Lord-Jesus inside thirty years* time go Lord-Jesus on.
  9  Tabor and of disciple^ and be_glorified ~and
 10  see disciple^ Moses and Elijah white clothes
 11  and see light [from_heaven] and then stop | Lord
 12  Jesus and Moses and Elijah and then disciple^ through
 13  take_fright and down [fell] bow and then disciple^ voice.

## 024r — Tabor and Carmel, and the baptism

> heard this word spoken [beloved] of the Son; and the Father mouth [voice] […] and then home [alone] not the apostles, and not every […] but to the Lord Jesus. Here ends this holy gospel. The second confessed … the Lord Jesus, the Father of the Lord: first on Mount Tabor, second on Mount Carmel. Because then the Lord Jesus, at thirty- one years, at that time the Lord Jesus went to be baptized [by] Saint John, […] to Mount Carmel; and then the Lord went | [to] Saint John. The Lord Jesus said: John […]. The Lord said | Saint John: Master, and […] [came] baptize. And the Lord Jesus said, John baptize the Lord; and […] is baptize Saint John baptized; he saw baptized the Lord Jesus. Then the Lord was thirty years old; and appear the Holy Spirit

  1  hear this word say [beloved] of son and father mouth* [voice] spoon-+name
  2  and then home [alone] not apostle and not every see.
  3  but to-Lord-Jesus here_ends this holy_gospel second confess
  4  ~have Lord-Jesus the_father of-Lord first on-Tabor
  5  second on-Carmel to-mount because then Lord-Jesus inside thirty
  6  one-~year time go Lord-Jesus to baptize holy-John
  7  baptize on-Carmel to-mount and then Lord go | to
  8  holy-John say Lord-Jesus John baptize Lord say | holy
  9  John Master and this-~John [came] baptize and say Lord-Jesus
 10  John baptize Lord and mouth-~John exist baptize.
 11  holy-John baptize see-baptize Lord-Jesus then
 12  to-Lord inside thirty year and appear holy-spirit

## 024v — the dove

> in the form of a dove, and said: He is of the Son. he who the Spirit came to rest; and the Lord took the Holy Spirit; and the Lord went into field the Lord Jesus fasted forty days. The third confessed

  1  inside ~form dove and_said he of son
  2  he_who spirit grow_calm and Lord grab
  3  holy-spirit and Lord go inside field
  4  fast Lord-Jesus forty_days third confess

## 025r — the devils confess him

> the devils that the Lord Jesus is truly the Son of God. Because when the Lord Jesus was thirty years old, at that time the Lord Jesus went into | [afterward] the town; and then he went into Capharnaum. At that time a man knelt down before the Lord Jesus, and said, Lord, the man's mouth: I have one son, and in [him] a devil [cast out]. The man's son — his apostles son could not heal [him]. That he begged the Lord to heal this, our son. Said the Lord Jesus: have mercy, gain [lunatic] son; [he] can, from the year, [be] a healthy man. And then the son came before the Lord Jesus; and […] he was made whole; and this three confessed — the devils that the Lord Jesus is truly the Son of God, because by miracle they confessed. The second-two confessed […] the Lord Jesus — the angels, at the birth of the Lord Jesus Christ. Because then the Lord Jesus was born [in] Bethlehem

  1  devil = that Lord-Jesus righteous son God because exist
  2  Lord-Jesus inside thirty year time go Lord-Jesus inside | exist
  3  [afterward] town and then go inside Capharnaum time
  4  then kneel one man^ before Lord-Jesus
  5  and_said Lord mouth man^ have one son and inside-+SUBJ
  6  devil = [cast_out] man^ son of disciple^ to-hide-to son can
  7  heal that* ask heal this Lord our son say
  8  Lord-Jesus have_mercy gain [lunatic] son can from-~year healthy_man^
  9  and then son go before Lord-Jesus and ~way.
 10  be_healed = and this three confess devil = that
 11  Lord-Jesus righteous son God because miracle confess second-two
 12  confess have Lord-Jesus angel on-be_born Lord-Jesus
 13  Christ because then Lord-Jesus be_born Bethlehem

## 025v — the Nativity told again

> town; and first, before the birth, one hour was […] a star, light through Bethlehem town; and | then the star; the shepherd saw it; and from the sheep, the shepherd. and then at the star, a miracle. At that time the angel said [shepherds] great joy! A king is born, a king born in Bethlehem town, in a barn, in a donkey's manger [ox] the donkey, in the hay, in [manger] [laid] Christ, Mary's son. And | then the shepherd went [to] Bethlehem; and then […] knelt down, and every one of them knelt | and [and then] from the shepherd [hastened] to go another and [the Most High Lord] gave thanks, and gave thanks. Here ends this holy gospel. […] confessed […] the Lord Jesus […]

  1  town and first before be_born one hour exist
  2  sky star through light Bethlehem town and | then
  3  exist star see shepherd and from sheep shepherd.
  4  and then on-star miracle time say angel [shepherds]
  5  great joy be_born king king SUBJ
  6  be_born inside ~Bethlehem town inside barn inside donkey
  7  manger [ox] donkey inside hay inside
  8  [manger] [laid] Christ Mary son and | then
  9  exist* shepherd go Bethlehem and then.
 10  rejoiced kneel and every this ~exist kneel | ~exist
 11  [and_then] from shepherd [hastened] to go another and
 12  [the_Most_High_Lord] thanks and give_thanks = here_ends this holy_gospel
 13  fifth confess ~have Lord-Jesus sky

## 026r — the earth quakes

> and the earth, to the Lord […] and the moon, because because when the Lord Christ crucified the earth quaked, the rocks and the stones split.

  1  and earth to-Lord-year and moon because
  2  because then Lord-Christ crucified.
  3  earth quake-rock stone split

## 026v — the sun darkened, and Abraham's confession

> The sun and the moon were darkened; and all tree into the world humbled themselves; and all creation mourn when Christ crucified; and all this five confessed, in sorrow that, that the Lord Jesus is truly the Son of God; and by miracle they confessed that the Lord Jesus is truly the Son of God, because […] miracle did; and the Lord suffered; the Jews crucified. and to whom, the year, the Lord, the Lord God announced [to] Abraham | the patriarch holy year arrived then; said, was said the Lord God [to] Abraham by the angel; and this the Lord God said to the blessed Virgin Mary by Gabriel the angel; and | Saint very old Joseph; and the man who believes in the Lord, that he is truly the Son of the living God — every man is saved; and one a man is damned; and the Lord not believes; and [perish] one is saved, but who believes not, a man is damned; and | this thus he said. First confessed it Abraham the forefather | This one confessed …; after these confessed holy Anne

  1  sun and moon this eclipse and every tree into_the_world* this humble and every
  2  create mourn then Christ crucified and this every five confess
  3  inside-to-sad that Lord-Jesus righteous son God and miracle confess
  4  that Lord-Jesus righteous son God because various.
  5  miracle ~do and suffer Lord Jew crucified
  6  and to-+who-~year the_Lord Lord_God announce Abraham | patriarch
  7  holy-~year arrive then* say exist say Lord_God Abraham on-angel and this
  8  say say Lord_God happy Virgin_Mary by_Gabriel angel and | holy
  9  aged Joseph and somebody to-Lord exist believe
 10  that righteous son living God everybody = be_saved and one.
 11  somebody be_damned to and Lord not believe and [perish]
 12  one to be_saved but who_believes_not* somebody be_damned and | this
 13  and-this say confess first Abraham forefather | on-this
 14  this confess holy-in_turn-+one-[?] after_these confess holy_Anne

## 027r — Mary's confession

> the mother, the blessed Virgin Mary. After these confessed the blessed | Virgin Mary. The angel of God said: at that time the Lord was; the Lord God went; the Lord's angel [to] the blessed Virgin Mary; then out, from … to the house of the Virgin Mary; she conceived, and bore; and [on the eighth] … five thousand years and one hundred and sixty years, and five, and, and the moon. at that time the Father of heaven opened, because he saw hidden every world, darkness, the sky. At that time the Father in heaven; and the Lord's angel Gabriel went […] to the blessed Virgin Mary, and these said. Saint Luke writes chapter in his writing; and the man who believes in the Lord, that he is truly the Son of the living God — every man is saved; and one man is damned; and the Lord not believes; and one is saved; but every man

  1  mother happy Virgin_Mary after_these confess happy | virgin
  2  Mary say angel God time exist Lord go Lord_God of-Lord
  3  angel happy Virgin_Mary then ~out from want-year to-house
  4  Virgin_Mary conceive and be_born and [on_the_eighth] five_thousand-~year
  5  and one hundred and six-ten-year and five and and moon.
  6  time open the_Father heaven because see hide every
  7  world darkness sky time open the_Father
  8  heaven and go of-Lord angel Gabriel inside exist-chapter
  9  blessed Virgin_Mary and these say write holy-Luke
 10  chapter* of-write and somebody to-Lord exist believe
 11  that righteous son living God everybody = be_saved and
 12  one somebody be_damned to and Lord not.
 13  believe and one to be_saved but everybody =

## 027v — Joseph's confession, and "there are not many gods"

> is damned. And these said, confessed Saint Joseph the aged | [understand] the angel of God said, because the Lord God spoke by the angel Gabriel: and the man who is the Lord's believe, that truly the Son of the living God — every man is saved; and one man is damned; and the Lord […] […]; and | […] … is saved, but every man is damned; and | this and this said, said the Lord Jesus on Maundy Thursday; then the Lord went | on to his death; and then the Lord went … the apostles in Jerusalem. At that time knelt the Lord Jesus before the blessed Virgin Mary; and the Lord Jesus said: there are not many gods, but rather one God. And the Lord Jesus said: […] and the Lord […] […] in the Lord Jesus Christ; and one is saved, but every man is damned; and Mary blessed the Lord Jesus, on every apostle — the blessed Virgin Mary.

  1  be_damned and these say confess holy-aged | Joseph
  2  [understand] say angel God because exist say Lord_God on-angel
  3  Gabriel and somebody to-Lord exist believe that righteous
  4  son living God everybody = be_saved and one
  5  somebody be_damned to and Lord not believe and | one
  6  chapter to be_saved but every somebody be_damned and | this-and
  7  this say say Lord-Jesus on_Maundy_Thursday = then Lord go | on
  8  die and then-Lord ~go-[?] apostle inside Jerusalem time kneel
  9  Lord-Jesus before happy Virgin_Mary and say Lord-Jesus is_not
 10  many God but_rather* one God and_said Lord-Jesus
 11  to and Lord not believe inside Lord-Jesus-Christ and
 12  one to be_saved but everybody = be_damned
 13  and Mary bless Lord-Jesus on-every apostle happy Virgin_Mary

## 028r — the Passover lamb, and the twelfth sign

> And then Mary, the Lord, kissed the Lord Jesus, the Lord's mother, the blessed Virgin Mary; and then Mary was, and from Mary. Mary's son, the Lord Jesus Christ, kissed [her]; and from Mary went away the Lord Jesus Bethany the apostles in Jerusalem, because the apostles […] Before the Lord went into Jerusalem, who, the apostles, ate the supper. the apostles prepared a lamb, because at that time was the feast of the Jews, the Passover. this is There began the suffering of the Lord Jesus Christ, Son of God; because the Lord is truly the Son of God. And then the Lord, the Jews crucified; and then the Lord, the apostles, the mother; within the tomb put; and on the third day from death the Lord stood up. And from | six six, the sign the Lord Jesus showed, when he rose from pray the Lord and the apostles appear in Jerusalem; and the thirteenth sign the Lord Jesus showed

  1  and then-Mary exist-Lord kiss Lord-Jesus of-Lord mother
  2  happy Virgin_Mary and then-Mary exist and from Mary.
  3  kiss of-Mary son Lord-Jesus-Christ and from Mary go_away
  4  Lord-Jesus Bethany apostle inside Jerusalem because SUBJ apostle exist.
  5  before Lord go inside Jerusalem who apostle dinner eat.
  6  prepare-apostle one lamb because time
  7  holiday exist Jew Easter this_is begin suffering
  8  Lord-Jesus-Christ son God because SUBJ Lord righteous son God
  9  and then Lord Jew crucified and then Lord apostle
 10  mother inside tomb put and on_the_third_day from die stand_up-Lord and from | six
 11  six can show Lord-Jesus then rise*
 12  from pray Lord and apostle appear inside Jerusalem and six-+seven can show Lord-Jesus

## 028v — the Ascension

> then [among] [one another]; one mount; two men and two men drove out six hundred and six thousand and sixty and six devils and the two men healed, did; the fourteenth sign showed the Lord Jesus; then Holy Thursday; then [he] left to the Lord's God the Father | on heaven's land, to sit, the Lord; the Father God, on the right.

  1  then [among] [one_another] one mount two somebody and two somebody
  2  exorcise six-hundred and six-?thousand and six-ten and six devil =
  3  and two somebody healing ~do fourteen can show
  4  Lord-Jesus then Holy_Thursday then leave to-of-Lord God_the_Father | on
  5  heaven ~land from-sit-Lord the_Father God on-right

## 029r — the Passion begins: "Here begins"

> Here begins the account Passion of our Creator Lord, the writing of the Passion, [the Passion], [of] Saint Matthew and Saint John, of the Passion | of somebody, the Creator Lord. At that time The Lord Jesus went to Bethany Jerusalem, because from far … to the Lord, the supper done, because the Lord was [there]. Before, the Lord went, the apostles, into Jerusalem, and the Lord Jesus said to the apostles: prepare from the Passover lamb, who, the Lord, the apostles, the supper eat, and I go to you. And then the Lord went to the apostles in Jerusalem; and sat at the table, the Lord [with] the disciples. At that time the apostles prepared the Passover lamb; and the lamb

  1  begins this begin the_account*
  2  Passion our Creator_Lord
  3  write Passion = [the_Passion]
  4  holy-Matthew and holy-John
  5  from suffering | of.
  6  somebody Creator_Lord time.
  7  go Lord-Jesus to_Bethany
  8  Jerusalem because from far-to-Lord dinner ~do because exist Lord.
  9  before Lord go apostle inside Jerusalem and_said Lord-Jesus exist apostle.
 10  prepare from Easter lamb who Lord apostle dinner.
 11  eat and I to you go and then Lord go.
 12  to-apostle inside Jerusalem and sit to-throne Lord [with] to_the_disciples time
 13  exist apostle prepare from Easter lamb and lamb

## 029v — the supper, and the washing of feet

> the apostles brought to the table; and the Lord Jesus said: brothers of the Lord, from the lamb, the Lord wants you to eat this Passover lamb. Therefore the Lord asks you: do not, apostles, be offended in the Lord, because I go to death — the Lord dies; and I | on the third day up rise, the Lord; and I appear to you. And the Lord Jesus stood up from the table, and took off, the Lord, | the Lord's clothes. And the Lord Jesus said: one apostle among seventy apostles, and among seven apostles, and the body an apostle was Titus; in turn [he] carried one bucket [of] water and a washing-dish; and then water into the dish poured; and the Lord Jesus went to Saint Peter; in turn Titus, in turn brought the water in the dish to the Lord Jesus; and Saint Peter said:

  1  carry apostle on table and_said Lord-Jesus brother of-Lord from
  2  lamb* want Lord to you eat this Passover.
  3  lamb therefore ask-Lord you do_not apostle
  4  inside Lord take_offence because I go on-die Lord die and I | on
  5  three_days up rise-Lord and I you appear
  6  and stand_up to-throne Lord-Jesus and take_off-Lord | on
  7  Lord of-Lord clothes and_said Lord-Jesus one apostle
  8  among seven-ten apostle and among seven apostle and ~body
  9  apostle exist Titus-in_turn carry one bucket water
 10  and one washdish and then water inside washdish
 11  pour and go Lord-Jesus to holy-Peter in_turn Titus-in_turn
 12  carry inside washdish water to Lord-Jesus and_said holy-Peter

## 030r — Peter objects

> Master, do not let this Peter, who he, Peter, have his feet washed. And the Lord Jesus said: Peter, if I this Peter's feet washed […] […] [part] within heaven, land And Saint Peter said: Master … this Peter, this … trespass; he a sufferer … Peter … [part], he in heaven's land | … this Peter, he … [hands and] head. washed; and all Peter's body washed; and | then Peter's feet the Lord washed; and the feet with the garment, the towel; and the rest of the apostles stood in the middle; every one he washed; and the feet garment [wiped] and the Lord Jesus took the Lord's clothes, and

  1  Master not_let this-Peter who he Peter foot wash
  2  and_said Lord-Jesus Peter if I this-Peter foot
  3  wash understand-+one this-cut_off-[?] [part] inside heaven ~land
  4  and_said holy-Peter Master sky* this-Peter this
  5  love-to-+high-[?] trespass he sufferer who-to-+high-[?]
  6  Peter cut_off-?be_born [part] he inside heaven ~land | love-cut_off.
  7  this-Peter he grab-cut_off-to [hands_and] head.
  8  wash and every of-Peter ~body wash and | then
  9  exist Peter SUBJ foot exist-Lord wash and foot
 10  SUBJ garment* towel and the_rest from stand apostle middle every
 11  wash and foot SUBJ garment* [wiped] and
 12  grab Lord-Jesus on-Lord of-Lord clothes and

## 030v — the bread, and the cup with water and wine

> The Lord Jesus sat at table with the apostles; and the Lord Jesus said: see, apostles, the Lord; see how I you pray, from rather and you understand, eat; two; pray; and took the Lord Jesus [took] in his hands one baked cake, and blessed the Lord Jesus this bread and bread the Lord set it before them; and the Lord Jesus took wine in a cup, and poured water into the cup; and blessed the Lord Jesus, the wine and the water; and the wine and water the Lord Jesus set before them; and the Lord Jesus said: and somebody whoever eats of this […], that man shall be | the the Lord's body eats; and somebody [who does] not this bread

  1  sit Lord-Jesus to-throne to-apostle and_said Lord-Jesus see SUBJ apostle
  2  to-Lord see how? I you pray from rather*
  3  and you understand-eat two pray and grab
  4  Lord-Jesus inside hands one baked cake
  5  and blessed Lord-Jesus this bread and bread
  6  before Lord put Lord-Jesus and grab Lord-Jesus
  7  wine one cup and water inside cup pour and blessed
  8  Lord-Jesus wine and water and wine water
  9  before Lord put Lord-Jesus and_said Lord-Jesus and somebody.
 10  exist this bread eat this somebody exist | of
 11  Lord ~body ~eat and somebody not this bread

## 031r — one of you shall betray me

> eats and believes in the Lord […]; every man is damned […] and the man who believes in the Lord and is from […] they ate the holy Host […] drank […] that man shall live, for ever and ever, amen. And said The Lord Jesus know: one among you and […] the Lord […] one of the apostles shall betray him. And the apostles looked among the apostles; Saint Peter said: Master, who is it? and struck … the Lord Jesus said; and [leaning] [breast] the Lord Jesus Peter and John; and [Peter] said: O, Peter's brother, ask the Master, who is it? And then he leaned Saint John on the side of the Lord Jesus, and said: Master | … These [words] said the Lord Jesus: to whom I give the bite

  1  eat and Lord believe everybody = be_damned cut_off-[?]
  2  and somebody exist Lord believe and exist from
  3  thirty holy-host eat and drink every.
  4  somebody exist living for_ever_and_ever = amen and_said
  5  Lord-Jesus know* SUBJ one among you
  6  and [?]-+SUBJ Lord name-+one from apostle betray and see-apostle among
  7  apostle say holy-Peter Master who_is_it and struck-to.
  8  say Lord-Jesus and [leaning] [breast] Lord-Jesus
  9  Peter and ~John and say oh of-Peter ~brother
 10  ask Master who_is_it? and then lean_on
 11  holy-~John on-end Lord-Jesus and_said Master | name-+one.
 12  these say Lord-Jesus to_whom I give^ bite

## 031v — Satan enters into Judas

> bread. So it is. And then holy John slept on the side of the Lord Jesus; and this the Lord Jesus gave. Nicodemus(?) saw the Lord Jesus [the morsel] this bread And then bread Judas Iscariot gave; and then the bread, Judas immediately the devil entered into Judas. And the Lord Jesus said: apostles, weeping, from a man, and this gave from the Son of God. And the Lord Jesus said: Judas, do what thou doest. And then the apostles misunderstood how he said: Master, speak. But the apostles did not understand what Judas said. bread [he should] buy, who … the shepherd, to eat, because to feed the apostles … because this was the Jews' Passover.

  1  bread so_it_is and then sleep holy-~John
  2  on-end Lord-Jesus and give^ this Lord-Jesus.
  3  Nicodemus? and see* Lord-Jesus [the_morsel] this
  4  bread and then bread exist-Lord Judas
  5  Iscariot give^ and then bread Judas
  6  immediately = devil = inside Judas enter
  7  and_said Lord-Jesus apostle crying from man^ and give^ this
  8  from son God and_said Lord-Jesus Judas do
  9  who-exist do and then misunderstand apostle how?
 10  say Master speak but understand apostle how? say Judas
 11  bread buy who-exist shepherd ~eat because
 12  feed apostle ~exist judge because this exist Jew Easter

## 032r — Wednesday, and the silver

> and […] Judas; and he went [to] the Jews' chief in Jerusalem; because the Lord was […]. On Wednesday one of the apostles betrayed him — Judas — because he took for the Lord thirty silver. And the Lord Jesus said: brothers of the Lord, I go to God the Father of the Lord; and I [send] you the Holy Spirit shall come; and you shall […] … that is, I go to death; the Lord dies, because the Jews crucify the Lord; and I on the third day up stand, the Lord. Therefore the Lord asks you: do not, apostles, stumble in the Lord, because the hour comes, the hour of the Lord God the Father [willed] the Lord crucified. And [Peter] said:

  1  and rise Judas and go Jew
  2  head inside Jerusalem because Lord exist inside Wednesday from apostle
  3  betray Judas because exist to-Lord grab thirty
  4  silver and_said Lord-Jesus brother of-Lord I
  5  go of-Lord God_the_Father and I you
  6  go holy-spirit and you exist see-two
  7  judge that_is I go on-die Lord die because
  8  Lord Jew crucified and I on_the_third_day
  9  up stand_up-Lord therefore ask Lord you
 10  do_not apostle inside Lord stumble because come hour
 11  of-Lord God_the_Father [willed] hour SUBJ Lord crucified and_said

## 032v — Peter will deny him

> Peter: Master, this Peter wants … the Lord; he dies. And the Lord Jesus said: Peter, before the cock crows, this Peter will deny the Lord three times. And Peter said, Peter … And the Lord Jesus said: Peter, this this […] Therefore the Lord asks you: do not […] be offended in the Lord; because the apostles were very sorrowful for the Lord; and one of the Jews was a judge; and the mouth could the Lord; said the Lord Jesus: but rise; and the Lord went on the way, because the Lord Jesus had then known, the Lord, Judas, in the house of the high priest; and many miracles and much preaching did the Lord Jesus on the way.

  1  Peter Master this-Peter want food Lord he die
  2  and_said Lord-Jesus Peter first than crow cock
  3  this-Peter Lord-to three exist deny and Peter say Peter
  4  emperor and_said Lord-Jesus Peter this SUBJ this
  5  ~out therefore ask Lord you do_not apostle.
  6  inside Lord stumble because exist apostle many sad on-Lord have
  7  in_turn one Jew exist judge and mouth
  8  can Lord say Lord-Jesus but rise and go Lord
  9  on-way because have Lord-Jesus then Lord know
 10  Judas inside house ~high_priest and many miracle
 11  and many ~preach ~do Lord-Jesus on-way

## 033r — over the brook Cedron, into the garden

> And Saint John tells of many miracles and much preaching did the Lord Jesus, the way; but within [it is] not written down. And then the Lord and the twelve apostles […] […] There was a brook Kidron; and of the apostles the rest of the apostles; the third apostle; the Lord gave Peter, and. John, and James, and […] over Kidron; and up into the mount; and […], because there was a garden on this, to the mount beyond Jerusalem town; and then the Lord went on Jerusalem; and into Jerusalem, behold, the Lord […] to the Lord Jesus and his apostles, because [Judas] wanted to give the Lord Jesus in the garden to arrest. as our father Adam [on the tree] [the tree]

  1  and speak holy-John many miracle and many ~preach
  2  ~do Lord-Jesus ~way but inside write not
  3  write and then Lord six-six apostle [?]-~year this.
  4  exist one brook Kidron and from apostle
  5  rest apostle third apostle Lord give^ Peter and.
  6  John and James and [?]-[?].
  7  over Kidron and to-up inside to_the_mount
  8  and [?]-+one-[?] because-exist garden on-this to_the_mount
  9  trespass Jerusalem town and then-+SUBJ go-Lord on-Jerusalem and inside
 10  Jerusalem lo Lord [?]-Lord-apostle to Lord-Jesus and of-Lord apostle
 11  because want-Lord give^ Lord-Jesus inside-garden arrest
 12  as our father ~Adam [on_the_tree] [tree.]

## 033v — a stone's cast, and the prayer

> committed sin; this wanted the Lord Jesus, to somebody [on the tree] [tree] suffering, not to; and then from, to the Lord the apostles in the garden; in turn the Lord went to pray, speaks Saint John: the Lord went away from the apostles, [answered], then about a stone's throw pray; his Father; and he knelt down, the Lord Jesus, and said: Father of the Lord, God of heaven, from […] take, Father, from the Lord this suffering; nevertheless if it is pleasing. And the Lord Jesus rose; and the Lord went to the apostles, but the apostles were asleep; and the Lord Jesus said: rise and […] woke them; and the Lord Jesus went […] Peter the peak of the mountain, to see this people, because all the people were

  1  commit sin this want Lord-Jesus to-somebody [on_the_tree]
  2  [tree] suffering not-to and then from-to Lord
  3  apostle inside garden in_turn to-Lord go on-~pray speak
  4  holy-John go_away-Lord trespass from apostle [answered] then
  5  a_stone's_throw = pray father of-Lord and kneel
  6  Lord-Jesus and_said father of-Lord God heaven.
  7  from ~grab-father from Lord this suffering in_turn
  8  SUBJ pleasing and rise Lord-Jesus and go-Lord
  9  to apostle but apostle to-sleep and_said Lord-Jesus rise
 10  and ~have-apostle awake and go Lord-Jesus Peter
 11  peak of_the_mountain to see this ~people because exist every people

## 034r — the second prayer, and the sweat

> And a second time the Lord went to pray, before, and the Lord Jesus knelt, and said: God the Father of heaven, from […] take, Father, from the Lord this suffering; if it is pleasing. And then blood, sweat, through the Lord Jesus, because [in an agony] the Lord Jesus, how, first, the Lord's suffering […]. And the Lord went to the apostles […]; the apostles were asleep And the Lord Jesus said: rise, and, apostles, be awake. At that time Saint Peter went, and said: on the third, the army, be afraid. and a third time the Lord went, prayed [to] God the Father of the Lord, and knelt | the Lord Jesus, and said: God the Father of the Lord, of heaven, from | do not take Father, take from the Lord this suffering; nevertheless as it pleases thee; nevertheless [thy will] pleasing, because this, God the Father, fulfil on the Lord the will | of

  1  and two go Lord on-°pray-before and kneel Lord-Jesus and_said
  2  God_the_Father heaven from ~grab-father from Lord this suffering
  3  if SUBJ pleasing and then blood sweat through
  4  Lord-Jesus because [in_an_agony] Lord-Jesus how?-°first Lord suffering
  5  not-chapter and go Lord to-apostle but apostle to-sleep
  6  and_said Lord-Jesus rise and ~have-apostle awake
  7  time go holy-Peter and_say on-+three army be_afraid
  8  and three go Lord ~pray God_the_Father of-Lord and kneel | Lord
  9  Jesus and_said God_the_Father of-Lord heaven from | not_take
 10  father from Lord this suffering in_turn SUBJ pleasing in_turn
 11  [thy_will] pleasing because this-God_the_Father fulfil on-Lord will | of

## 034v — the angel from heaven

> the Father. And an angel went from heaven high, the Father's, and said: Lord, do not have … this, the Lord, this suffering drink. And the angel said: this is it, he offers, the Father: the Lord's lot, of God the Father; the Son Jesus Nazareth every world redeem. And the angel departed from before the Lord Jesus; because every night the angel went not from the Father high to the Lord Jesus; because the angel bore for the Lord all his suffering, written; and [spoken] righteously; fulfil, who, from the prophet. written. And the Lord went to the apostles, and the Lord Jesus said: […] his […]; and the Lord and the apostles had one […] not, not, first; and then [he rose] [from prayer]; and then the apostles | to

  1  father and go angel from_heaven* high the_Father and_said
  2  Lord do_not ~have this the_Lord this suffering drink
  3  and_said angel this_is he offer the_Father.
  4  of-Lord fate of-God_the_Father son Jesus Nazareth
  5  every world redeem and leave angel before
  6  Lord-Jesus because every night not_go angel high the_Father
  7  to-Lord-Jesus because Lord carry angel every of-Lord suffering
  8  write and [spoken] righteous fulfil who from-prophet.
  9  write and go-Lord to-apostle and_said Lord-Jesus
 10  brother of-Lord and have-Lord-apostle one little
 11  not-?not-°first and then [he_rose] [from_prayer] and then apostle | to

## 035r — the sign, and the kiss

> slept. And the Lord Jesus could not sleep; but the Lord laid a stone at his head; and the Lord Jesus could not sleep; but rise And the Lord said: apostles, stand up, apostles, up, have, apostles, [a sign]: serpent because from know came the Jews [betray] the Son of Man recognized, to capture [him]. And then the Lord and the apostles went on the way, and saw | the Lord Jesus a great people going; and among the Jews was Judas, he whose father died, and mother, [while] they slept. [Came] Judas and the Jews. He asked a sign to tell the Lord from James, John, Peter: a kiss. so that Judas […] the Jews might take the Lord. And then Judas went up to the Lord Jesus; and […] Judas, the Lord's hand; because to the Jews [he] asked a sign,

  1  sleep and can sleep Lord-Jesus but Lord-put one stone
  2  to-head and can sleep Lord-Jesus but rise
  3  and_said Lord apostle stand_up apostle to-up ~have-apostle [a_sign]
  4  serpent* because from know* go Jew [betray]
  5  Son_of_Man = recognize* capture and then
  6  Lord apostle and apostle go-Lord-and-apostle on-way and see | Lord
  7  Jesus great^ people go and among Jew exist Judas
  8  he_who the_father die and mother [while] sleep [came] Judas and Jew
  9  ask_a_sign distinguish Lord James John Peter kiss
 10  Judas from Lord capture Jew and then
 11  go Judas against Lord-Jesus and kiss.
 12  ~Judas of-Lord hand because to-Jew ask_a_sign

## 035v — "Whom seek ye?" and they fell backward

> because John was like the Lord Jesus. And he cried out, | the Lord Jesus: Whom seek ye? The people, the Lord's — the Jews. And they cried, the Jews shouted, the Jews answered: Jesus of Nazareth. And cried the Lord Jesus: from I, if [it is] the Lord ye seek, Jews. And every Jew fell backward. And the Lord Jesus said: rise, Jews, up. [Swords] the Jews hid, of the club; and the Jews rose up; and the Jews' club the Jews took in their hands, because the Lord Jesus prayed did; God his Father, to the Jewish people; and The Jews rose up; and a second time the Lord Jesus cried: whom seek ye, the people, the Lord's — the Jews. And they cried […] The Jews answered: Jesus of Nazareth. And cried the Lord Jesus: from I, if [it is] the Lord ye seek, Jews; and

  1  because exist similar John to-Lord-Jesus ~and shout | Lord
  2  Jesus who? search people of-Lord Jew and shout
  3  Jew Jews answered Jesus Nazareth and shout
  4  Lord-Jesus from I if Lord search Jew and every
  5  Jew fall_back = and_said Lord-Jesus rise-Jew up
  6  [swords] Jews hide of-club and rise-Jews up and of-Jew
  7  club grab-Jews inside hands because Lord-Jesus pray
  8  do God_the_Father of-Lord to-Jew people and
  9  rise-Jew to-up and two shout Lord-Jesus whom search
 10  people of-Lord Jew and shout Jew.
 11  Jews answered Jesus Nazareth and shout
 12  Lord-Jesus from I if Lord search Jew and

## 036r — the third cry, and Jesus of Nazareth

> every Jew fell backward. And the Lord Jesus said: rise, Jews, up. He said: hide, of the club; and the Jews rose up; and the Jews' club the Jews took in their hands, because | the Lord Jesus prayed, did, [to] God his Father, to the Jews people; and the Jews rose up; and a third time he cried | the Lord Jesus: Whom seek ye? The Lord's whom the Jews; and the Jews shouted, the Jews answered: Jesus of Nazareth. And the Lord Jesus cried: from I, if [it is] the Lord ye seek, Jews. And said, cried, the Lord Jesus: Take the Lord, Jews, because [I] go, the hour, to God my Father. And then the Jews arrested the Lord Jesus [backward].

  1  every Jew fall_back = and_said Lord-Jesus rise-Jew up
  2  he_said* hide of-club and rise-Jews up and of
  3  Jew club grab-Jews inside hands because | Lord
  4  Jesus pray ~do God_the_Father of-Lord to Jew
  5  people ~and rise-Jew to-up and three shout | Lord
  6  Jesus whom search of-Lord Jew
  7  and shout Jew Jews answered
  8  Jesus Nazareth and shout Lord-Jesus from I
  9  if Lord search Jew and_said shout Lord-Jesus
 10  grab Jew Lord because go ~hour of-Lord God_the_Father
 11  and then ~Jew arrest Jew Lord-Jesus [backward]

## 036v — Malchus, and the ear put back

> Peter cut off with the sword the ear of one of the Jews, and the Jew's name was Malchus. And said the Lord Jesus: Peter, Peter, blind, cut off [with the] sword; because and the man Peter sword cut off from sword struck, somebody die. And the Lord Jesus gave [back] this ear and put it back in its place, and the ear was made whole. And from the Lord Jesus a miracle done on the pagan. And the Jews believed in the Lord; but the Lord's clothes | the Lord take off; and one of the Jews fled, to the Lord, believe the Lord Jesus; and from [fear] to the Lord [fled] the Lord Jesus all the Jews [forsook] [him]; to the Jews went; and then … from little [if] And then the Lord could have fled — the Lord did not flee, but good [will] to somebody, apostle, Jew, pagans, above on high.

  1  cut_off Peter sword ear one Jew
  2  and name Jew exist Malchus and_said
  3  Lord-Jesus Peter Peter ~blind cut_off sword because and
  4  somebody Peter sword cut_off from sword.
  5  struck* somebody-+SUBJ die and give^ Lord-Jesus this ear
  6  and ear-+SUBJ put on-place and healing ear
  7  leave and from Lord-Jesus on-pagan miracle ~do
  8  and and Jews inside Lord believe but of-Lord clothes | on
  9  Lord take_off and escape one Jew
 10  to-Lord believe Lord-Jesus and from [fear] to-Lord [fled] Lord-Jesus
 11  every Jews [forsook] to Jew go and then-[?] from little
 12  [if] and then Lord want escape exist Lord not escape
 13  but good [will] to-somebody apostle Jew pagans above-high

## 037r — bound, and struck

> On the cross … and then … carried the Lord's clothes. the Lord Jesus; and then tie up the hands of the Lord Jesus Christ [bound] all to the Lord, to the year [led] that; and then the Lord. they went to the chief of the Jews [before]; and then the Lord went down from the mountain; and many [people] did the Jews on the Lord Jesus, because the Lord one [struck] in the face [from] the town; the second, to the Lord's house; [and] the third to the Lord [answered] from the suffering. Our mercy, the Lord Jesus! And then through … the Jews, through, over Kidron; and the Jews took the Lord on the bridge; went the Lord Jesus. but the Lord on the bridge fell; and to the Lord [struck] who. Our mercy, the Lord Jesus! because the Lord two [times] went [among] the Jews.

  1  on_the_cross-[?] and then-[?] carry to-Lord clothes.
  2  Lord-Jesus and then tie_up hand Lord-Jesus-Christ
  3  [bound] every to-of-Lord to-year-to [led] that* and then Lord.
  4  go to-Jew head [before] and then Lord
  5  go down on-to-mount and many [people] ~do
  6  Jew on-Lord-Jesus because Lord one face beat
  7  [from] town* second to-Lord to-house [and] third
  8  to-Lord [answered] from suffering our have_mercy Lord-Jesus
  9  and then through [?]-Jews through over Kidron
 10  and Lord grab-Jews on-bridge go Lord-Jesus.
 11  but Lord on-bridge fall and to-Lord [struck] who.
 12  our have_mercy Lord-Jesus because Lord two [times] go Jew

## 038r — bound before Caiaphas

> [bound] they bound the Lord Jesus Christ; and then the Lord … and dragged out, out, [away]. Our mercy, the Lord Jesus Christ! And the Jews said: where does the Lord want [to go]? the Jews went, the Jews said: one brought the Lord | to Pilate. The second said: bring the Lord to Caiaphas. And | then the Lord was brought to Caiaphas the high priest. And said the Jews […] accused the Lord; and then the Lord […] before the high priest's house; and | when the Lord was [there]; the Jews … brought the Lord [to] this high priest. and then the Lord […] into a house; and | when the Lord, from every one, one [answered], the hour | of the suffering. The Jews, the Lord Jesus Christ. And Peter said, one

  1  [bound] who-chain-to Lord-Jesus-Christ and then Lord
  2  exist and out-out draw [away] our have_mercy
  3  Lord-Jesus-Christ and_said Jew where? Lord want
  4  Jew go say-Jews one brought* Lord | to
  5  Pilate second say brought-Lord to-Caiaphas and | then
  6  exist Lord brought-Lord to-Caiaphas high_priest and_said
  7  Jew would_say* Lord on-+three accuse and then
  8  Lord to-[?] before NAME.priest high_priest house and | then
  9  exist Lord exist-Jews inside-?brought Lord this high_priest.
 10  and then Lord gate inside one house and | then
 11  exist Lord from-to-every one [answered] ~hour | suffering
 12  Jews Lord-Jesus-Christ and_said Peter one

## 038v — the first denial, and Caiaphas's counsel

> of the Jews, this Malchus whose ear was cut off […] Peter [then], this Peter knew not, Peter; and this was from the first denial of the Lord Jesus, because Peter said: I know not the Lord. And […] the Lord Jesus [was brought] to Caiaphas the high priest; and | when the Jews went to the Lord before Caiaphas, and shouted the Jews, this Caiaphas, the Jews: [it is expedient] [he] go; this believe, this heretic Lord; and the Lord is from Galilee; he fed with bread all the people, the Lord, [manna] | in turn the second, the Jews said, said: the Son of God; the third, the Jews said: the king. Caiaphas said: it is written, it is good that one man should die, rather than all the world perish. And then … the Jews, [the nation]. the high priest […] in the house, among the apostles Christ [counsel]

  1  Jew this Malchus ear cut_off say.
  2  Peter [then] this-Peter not_know-Peter and this from
  3  first denial Lord-Jesus because say Peter not* Lord not_know
  4  and brought* Lord-Jesus to-Caiaphas high_priest and | then
  5  Jews to-Lord go before Caiaphas and shout
  6  Jew this-Caiaphas-Jews [expedient] go this believe
  7  this heretic Lord and to-Lord SUBJ from Galilee
  8  feed bread all^ people on-Lord [manna] | in_turn
  9  two say-Jews say son God third say-Jews king
 10  say say Caiaphas write SUBJ good one Lord-somebody
 11  die than rather all^ world perish and then-?cup-Jews [nation]
 12  apostle-high inside-?brought inside house among disciple^ Christ look_up leave^ [counsel]

## 039r — the second denial

> Saint Peter before the gate; and then Peter was seen by the handmaid at the Jews' gate. And the handmaid said: this Peter [is] a disciple of this Jesus. Peter said: this Peter knows [him] not. This [was] the other denial of the Lord Jesus, because Peter said not the Lord | and. and denied him. And John […] […] was known to the high priest. Caiaphas said to Jesus: he says the Son of God? And how dost thou truly preach? Jesus said to Caiaphas, judge Caiaphas, from the Jews, to the Lord. hear my preaching [denied] truly […] And then Caiaphas, this Caiaphas, and [gathered] in the Lord new Caiaphas that year, but rather he righteously the man, said Caiaphas. […] field the Lord was brought to Pilate, to Caiaphas's brother.

  1  holy-Peter before ~gate and then Peter exist
  2  show^ from-handmaid ~gate Jew and_said handmaid this-Peter
  3  disciple^ this Jesus say Peter this-Peter not_know and.
  4  this the_rest^ denial Lord-Jesus because say Peter not* Lord | and.
  5  to-Lord-to in_turn John inside-[?] because-exist.
  6  acquaintance this high_priest say Caiaphas to-Jesus he say
  7  son God in_turn how? this righteous preach say Jesus
  8  to-Caiaphas from-judge-Caiaphas from Jews Lord-to.
  9  hear preach [denied] ~righteous preach.
 10  and_said Caiaphas this-Caiaphas and [gathered] inside Lord new
 11  Caiaphas-year but_rather* he righteously man^ say Caiaphas
 12  [?]-field Lord brought* to-~Pilate to-of-Caiaphas brother

## 039v — before Pilate

> And this out, two hours; and the Lord brought | to Pilate; and from the Lord, on three [counts], they accused; and then the Jews said to Pilate: he goes, he, the heretic; and | then many Jews were, [bringing] suffering on the Lord. The Lord went before Pilate, because all the Lord's [accusation] | on the Lord from [spat]; and the Lord's holy face all [buffeted]; and | when the Lord was; the Jews were; [nothing] up [again]; our mercy, the Lord Jesus! And then the Lord was [with] the Jews; went to Pilate. And then the Jews [said to] this Pilate: the Lord goes, he, the heretic; and the Lord from | the apostles was food, bread, [for] all the people, on the Lord [manna] The second, the Jews said: the Son of God. The third, the Jews said:

  1  and this ~out two hour and Lord brought* | to
  2  Pilate and from Lord on-+three accuse and_said-Jews
  3  he_said* Pilate go he heretic and | then
  4  exist Jews many suffering on-Lord do
  5  go Lord before Pilate because every of-Lord [accusation] | on
  6  Lord from [spat] and of-Lord holy-face every [buffeted] and | then
  7  exist Lord exist Jews [nothing] to-up [again] our
  8  have_mercy Lord-Jesus and then Lord exist Jews go
  9  to-Pilate and_said Jew this Pilate Jews Lord
 10  go he heretic and Lord SUBJ from | apostle-exist
 11  exist food bread every people on-Lord [manna]
 12  second say Jews say son God third say Jews

## 040r — the third denial, and the cock

> he saith he is king. And then Peter went to a bread [manna]; because is virgin, cut off [sacrament] [worship] Peter wanted; [answered], said one Jew to [him]: Peter, this apostle, he half believes this Jesus. Peter said know and denied him, and this was the third denial of the Lord Jesus; and at that moment the cock crew. And Peter said: this out, who, Peter: Master, he spoke; and sorrowfully Peter went out. And then Pilate to Jesus: this Lord, sayest thou the Son of God? In turn, how? this righteously. preach? The Lord Jesus said to Pilate; Pilate from the Jews, and the Jews; the Lord: hear my preaching [denied] righteously preach. And Pilate [judged]; the Lord Jesus spoke

  1  king say and then Peter go to-one
  2  bread [manna] because exist virgin-cut_off [sacrament] [worship]
  3  want Peter [answered] say one Jew to
  4  Peter this apostle he-~half-~believe this Jesus
  5  say Peter grab God this-Peter know
  6  and this three denial Lord-Jesus and time crow cock
  7  and say Peter this SUBJ out who Peter Master
  8  speak and sad Peter leave and_said Pilate
  9  to-Jesus this Lord say son God in_turn how? this righteously
 10  preach say Lord-Jesus to-Pilate from-judge-Pilate
 11  from Jews and-Jews Lord-to hear preach [denied]
 12  righteously preach and Pilate [judged] from speak Lord-Jesus

## 040v — two lines

> but the Lord said to this Pilate, with his mouth, and the Lord: I truly the Son of the living God.

  1  but say Lord this-~Pilate SUBJ mouth and-Lord I
  2  righteous son living God

## 041r — art thou the king of the Jews

> And then Pilate [said] to this Lord: speakest thou, Lord, king of the Jews? The Lord Jesus said to Pilate [asked] Pilate's mouth and I [am] truly the Son of the living God. And then Pilate: he truly somebody, this [man]; this Pilate how [answered] in the Lord [nothing]; and there cried the Jews: crucify the Lord! Pilate: on the cross the Lord [is] cursed, this Pilate. If the Jews want the Lord, the Jews [release him]. The emperor truly crucifies. And then Pilate [therefore] the Jews took the Lord; and the Lord was brought Herod, Pilate's brother; and then out, three. the hour; and then the Lord was brought [to] Herod the king; and then, and [the Jews] […] on one

  1  and_said Pilate this Lord speak Lord king Jew
  2  say Lord-Jesus this Pilate SUBJ [asked] Pilate mouth
  3  and I righteous son living God and_said.
  4  Pilate he SUBJ righteous somebody this Pilate
  5  how? [answered] inside Lord [nothing] and shout
  6  Jew crucify Lord Pilate on_the_cross Lord cursed this
  7  Pilate if want Jews Lord Jews [release]
  8  emperor righteous crucify and_said Pilate.
  9  [therefore] grab Lord Jews and Lord brought*
 10  ~Herod of-Pilate ~brother and then ~out three.
 11  hour and then Lord brought* Herod
 12  king and then and [?]-Jews on-one

## 041v — sent to Herod, because he is of Galilee

> love [answered]; and then from [them] shouted every [one], four directions, year, to the Lord [accused]; this he brought: he, the heretic this Jesus blasphemeth; and the Lord is out of Galilee, he fed with bread all the people, on the Lord [manna]. And then the Lord was brought; many asked before. Herod the king, because […] the Jews would […] the Lord Herod, crucify! and the Lord, the emperor. Herod, crucify! but [long] shining, see. Herod, the Lord Jesus Christ; and then the Lord brought before Herod the king; and the Jews cried […] Herod, the Jews: the Lord goes, he, the heretic; and the Lord is from Galilee; he fed with bread every

  1  love [answered] and then from shout every two-two direction-~year-to
  2  Lord [accused] this brought* he heretic
  3  this blasphemer-Lord this Jesus and SUBJ Lord from Galilee
  4  feed bread every people on-Lord [manna]
  5  and then Lord to-?brought many ask^ before.
  6  Herod king because to-+Elizabeth Jew to-Lord want
  7  Herod crucify and Lord emperor.
  8  Herod crucify but [long] shine see.
  9  Herod Lord-Jesus-Christ and then Lord brought* before
 10  Herod king and shout Jew this.
 11  Herod Jews Lord go he heretic and Lord SUBJ
 12  from Galilee feed bread every

## 042r — four lines

> the people against the Lord [manna]; and the Lord said, the Son God. And then the false [witnesses] confessed, said the Lord, and the man, this temple destroy | he wants, the Lord: I in three days all [shall] do.

  1  people on-Lord [manna] and Lord say son
  2  God and_said ~false °and_then-confess say Lord and
  3  man* this temple destroy | want
  4  Lord I in three_days every ~do

## 042v — Herod questions him

> and [of David] confessed it talent Herod; but […] Herod said: Lord — Herod [mock] God, that the Lord is the Son; and one said, spoke of the Lord Jesus against Herod; and Herod [mocked] Herod [derided] Herod the king […] he could, Herod, [white], this dying, crucify [garment] he [sent back]; Herod said to [him]; Herod said [again] to Herod: the Lord of the living God […]; Herod said [mock] God, he [is] the Son; and not the Lord's name his Father [believed]. And then the Lord Jesus [said] to Herod | this: the Lord is truly the Son of the living God. The Lord Jesus said: I go to my Father; on doomsday [I] judge the living and the dead. and Herod did so: he brought a stone and […]

  1  and [of_David] to-this confess talent Herod but say.
  2  Herod say Lord Herod [mock] God this Lord son and
  3  one say speak Lord-Jesus ~against Herod and
  4  Herod [mocked] Herod [derided] this-Herod king this-Herod.
  5  he can Herod [white] this die crucify [garment]
  6  he [sent_back] Herod to say say Herod [again]
  7  to-Herod this Lord-to living God one-to say Herod [mock]
  8  God he son and not* Lord name
  9  of-Lord father [believed] and_said Lord-Jesus to-Herod | this
 10  Lord righteous son living God say Lord-Jesus I go
 11  of-Lord father on_doomsday judge living and die
 12  and do Herod carry stone and inside.

## 043r — Herod hoped to see a miracle

> a vessel of water, and brought various [stood] before the Lord Jesus; and the Lord was asked Herod: then the Lord before [him], a miracle do. and they set a yoke before the Lord Jesus, and […] to do a miracle, because when [hoped] before Herod he did no miracle, though the Lord took […] crucify! but Herod said: bring this Lord [questioned] Pilate [became] Herod's friend; understand, understand, who, who [he answered nothing], because on the Lord Pilate did. And the Lord brought before Pilate, many judge And this was out, the sixth hour; and the Lord [was] brought before Pilate. And then the Jews [said to] Pilate; he said, Pilate

  1  one vessel water and brought* various
  2  [stood] before Lord-Jesus and Lord ~ask
  3  Herod then-Lord before miracle do
  4  and yoke Lord-Jesus before and understand-eat
  5  miracle do because then [hoped] before
  6  Herod miracle do why?-Lord grab Herod.
  7  crucify but say Herod brought* this Lord [questioned]
  8  Pilate to-of-Herod friend^ understand-understand-+who who
  9  [answered_nothing] he because on-Lord do Pilate
 10  and Lord brought* before Pilate many judge
 11  and this ~out six hour and Lord brought* before
 12  Pilate and_said Jew Pilate say he Pilate SUBJ

## 043v — the scourging

> Herod, crucify, if the Lord … this Pilate, if the Jews want. the Lord. The Jews [wrote]: the emperor truly crucifies. And then Pilate understood; the soldiers carried [him]; the soldiers, Pilate. the two [thieves] [with him]; and then Pilate: Jews, carry. the two [thieves] [with him]; and the Lord, the gate, within. understood, the house; and Pilate took | two two soldiers to the Lord Jesus, and the Lord was scourged; and then two from the [pillar] flogged the Lord Jesus; second, the Lord began; two Jews flogged; and then two, and from two Jews. […] flogged the Lord Jesus Christ; and | there came one soldier to the Lord Jesus; and then […] the Lord Jesus, because the Lord had many tie up

  1  Herod crucify if-Lord this Pilate if want Jew
  2  Lord Jews [wrote] ~emperor righteous crucify
  3  and_said Pilate understand-eat soldier carry-soldier Pilate
  4  two [thieves] [with_him] and then Pilate Jews carry
  5  two [thieves] [with_him] and Lord gate inside.
  6  understand-eat house and grab Pilate | two
  7  two soldier to Lord-Jesus and Lord exist whip and then
  8  two from [pillar] flog Lord-Jesus second Lord
  9  begin two Jews flog and then two and from two Jews
 10  from [pillar] flog Lord-Jesus-Christ and | leave
 11  to-leave one soldier to Lord-Jesus and then
 12  from one-+Wednesday Lord-Jesus because exist Lord many tie_up

## 044v — the purple robe and the crown of thorns

> And then the Lord collapsed, the Lord Jesus; and the Lord [scourged]; they raised him up; and the Lord [mocked] clothes; understood, a purple robe; and the Lord the crown of thorns on his head, the Jews [put]. and they set the Lord upon a seat; and […] knelt before the Lord Jesus, and spoke: Healing, Jesus of Nazareth! And they left [hail]. understood, the soldiers, that [gave] [blows] [to] the Lord Jesus; and [sat] seat [judgment] the Lord Jesus; and then the Lord collapsed; and the Jews took the Lord, and the Jews led the Lord to Pilate, into the house.

  1  and then Lord collapse = Lord-Jesus and
  2  Lord [scourged] up raise-Jews and Lord [mocked]
  3  clothes understand-eat purple_robe and Lord
  4  thorn crown on-head conceive-Jews
  5  and Lord sit on-understand-eat chair and
  6  then-[?] kneel before Lord-Jesus and
  7  speak healing Jesus Nazareth and leave [hail]
  8  understand-eat soldier that* [gave] [blows] Lord-Jesus and
  9  [sat] from seat [judgment] Lord-Jesus and then
 10  Lord collapse = and Lord grab Jew
 11  and Lord go Jew to Pilate inside house

## 045v — twelve legions of angels

> And the Lord [was] seated [by] the Jews, within one throne | on the middle of the house; and then Pilate knelt. before the Lord Jesus, and Pilate said: Hail, Lord, King of the Jews! And the Lord Jesus said to Pilate […] speakest thou that I am king of the Jews? Because | then will his Father God, ye the Lord captured, because then I want, the Lord, I ask from my Father God | six six armies in turn of angels remain [with] me, that you seize [and] capture, because then I want; I [could] you all.

  1  and Lord seat Jews inside one throne | on
  2  middle house and then kneel Pilate
  3  before Lord-Jesus and say Pilate healing Lord king
  4  Jew and say Lord-Jesus to-Pilate this-+the_Lord
  5  speak because I king Jew because | then
  6  exist will of-Lord God_the_Father you
  7  Lord capture because then I want Lord
  8  I ask from of-Lord the_father God | six
  9  six an_army in_turn angel remain* I
 10  you grab capture because then
 11  I want I you every can

## 046r — Barabbas, and Behold the man

> the Lord die […]; and ye took the Lord captured. And Pilate said to Jesus: this sayest thou, Lord, the Son of God? And one said [Behold], said the Lord Jesus to Pilate; and he let go Barabbas; to Jesus, and they beat the Lord's face. [from] town [outside], all the Lord's holy, nine […] name quaked; and Jesus said […] the soldier, Barabbas, truly the Lord spoke […] they beat him; the church father spoke, it is written that; and [scourged] [again] they beat him. For ever and ever. And so they did to the Lord. Pilate went out of the house, and cried, Pilate: Behold Jesus, Nazareth the King of the Jews!

  1  Lord die cross-die and you grab
  2  Lord capture and say Pilate to-Jesus this
  3  Lord say son God and one say
  4  [Behold] say Lord-Jesus to-Pilate and leave
  5  Barabbas to-Jesus and Lord beat face
  6  [from] town* [outside] every of-Lord holy-nine-+name
  7  quake and say Jesus this soldier Barabbas this righteous
  8  speak-Lord to-inside-Lord beat speak church_father
  9  write that* exist and [scourged] [again] beat
 10  for_ever_and_ever = and Lord do
 11  Pilate out go on-house and shout-to
 12  Pilate lo Jesus Nazareth king Jew

## 046v — crucify him, the second time

> [Caesar]; in turn, the angel, Bethlehem town. And the Jews cried: the cross for the Lord! Pilate: the Lord is accursed, this Pilate: if the Jews want the Lord, enemy of the emperor. truly crucify! And Pilate said to the soldiers: go, Lord. into the house. And a second time the Lord did [so], went into the house, and Pilate cried: Behold Jesus Nazareth the King of the Jews! [Caesar] and the angel | Bethlehem town; and they shouted. the Jews: the cross for the Lord! Pilate: the Lord is accursed, this Pilate: if the Jews want the Lord, enemy of the emperor. truly crucify! And Pilate said to the soldiers: go, Lord.

  1  [Caesar] in_turn angel Bethlehem town.
  2  and shout Jew on_the_cross Lord Pilate cursed Lord
  3  this-~Pilate if want Lord Jews enemy of-~emperor
  4  righteous crucify and say Pilate to soldier go Lord
  5  inside house and two Lord ~do go on-house
  6  and shout Pilate lo Jesus Nazareth
  7  king Jew [Caesar] in_turn angel | to
  8  Bethlehem town and shout.
  9  Jew on_the_cross Lord Pilate cursed Lord this
 10  Pilate if want Lord Jews enemy of-~emperor
 11  righteous crucify and say Pilate to soldier go Lord

## 047r — the third time, and Caesar

> into the house. And a third time the Lord did [so], went into the house, and Pilate cried: Behold Jesus Nazareth the King of the Jews! [Caesar] and the angel to Bethlehem town; and they shouted. the Jews: the cross for the Lord! Pilate: the Lord is accursed […] Pilate: if the Jews want the Lord, enemy | of the emperor, truly crucify! And then the Jews [Behold], he, the king of the Jews, he. half [said]: one, the Lord; [half]: heretic, one. the Lord blasphemeth. And Pilate cried, Pilate, and how [cried] in the Lord [out] Pilate: he

  1  inside-house and three Lord ~do go on-house
  2  and shout Pilate lo Jesus Nazareth
  3  king Jew [Caesar] in_turn angel
  4  to-Bethlehem town and shout
  5  Jew on_the_cross Lord Pilate cursed Lord this.
  6  Pilate if want Lord Jews enemy | of.
  7  emperor righteous crucify and_said Jew
  8  [Behold] he king Jew he.
  9  half one Lord heretic one
 10  blasphemer-Lord and shout Pilate this Pilate
 11  and how? [cried] inside Lord [out] Pilate he SUBJ

## 047v — Pilate washes his hands

> truly the man. And then Pilate: Jews, carry water in one washdish; and then Pilate was [there]. carry; and Pilate washed high his two hands. And then Pilate: this Pilate [is] innocent of the Lord's blood. And then the Jews: because this is on the Jews, and on the Jews' son. and Pilate cried: whom will ye | to the Jews, release Barabbas or Jesus? And the Jews cried: release Pilate Barabbas, or Jesus? On the cross, crucify! And then Pilate understood; the soldiers led the divine one up to the house; and then Pilate, to the divine one went [went] up into the house; and Pilate shouted | from

  1  righteous man^ and_said Pilate carry-Jews water
  2  inside one washdish and then-~Pilate exist.
  3  carry and high-wash-~Pilate of two hands and_said
  4  Pilate this-~Pilate innocent from of-Lord blood and_said
  5  Jew because this exist on-Jews and of-Jews son
  6  and shout Pilate who want | Pilate
  7  to Jews release Barabbas in_turn Jesus and
  8  shout Jew release Pilate Barabbas
  9  in_turn Jesus on_the_cross crucify and_said Pilate understand-eat
 10  soldier go divine_one^ up on-house and then Pilate to
 11  divine_one^ go [went] up on-house and shout Pilate | from

## 048r — the Reproaches: O my people, what have I done to thee

> the man truly took to crucify, because [he did] not want the Lord crucified; and the Lord did [so]. Pilate went out of the house down among [them] the Jews; and the Lord Jesus shouted: people, the Lord's Jews, who I, he said, did, why? this people [cross], did, people, the Lord's Jews, who, this people, I; commit sin. [O my] this people, good [what] then the Lord I among this people did miracles. First, | people went into Egypt [out of] living servants; this over the sea, the sea I divided

  1  SUBJ somebody righteous grab on-crucify because SUBJ
  2  not_want Lord-to crucify and Lord ~do
  3  Pilate out go on-house down among from [them]
  4  ~Jew and shout Lord-Jesus people
  5  of-Lord Jew who I he_said* ~do
  6  why? this-people [cross] ~do people
  7  of-Lord Jew who I this-people commit sin
  8  [O_my] this-people-to good [what] then-Lord I
  9  among this-people-to miracle do first | this
 10  people go on-Egypt [out_of] living-servant this
 11  over sea sea divide

## 048v — forty years in the wilderness, and a cross for their Saviour

> in two directions, this people, over the sea. through struck the Lord led them by day, and from the beginning every sky to the people, all the world | this people [fed], living, the Lord, forty, in the field, in turn the angel, bread to this people. [thou hast prepared] cross I did for the Lord's people, the Jews, he said, to the Lord; raised [him] on Palm Sunday | then they would make the Lord king, a crown, and […] would say, the Lord's body on the cross lifted up. and Pilate shouted; the Jews took the Lord, blind[folded] and the Lord taken, the Jews; and then the Jews

  1  on-two direction this-people over sea
  2  through struck* go-Lord day in_turn from head
  3  every sky to-of-people ~all_the_world | this
  4  people [fed] living-Lord forty inside field
  5  in_turn angel bread to-this-people
  6  [thou_hast_prepared] cross do people of-Lord
  7  Jew he_said* to-Lord-to raise on-Palm_Sunday | then
  8  chapter-Lord want king crown in_turn name-high
  9  would_say* of-Lord body on_the_cross lift_up
 10  and shout Pilate grab-Jews Lord ~blind
 11  and Lord take* Jew and then Jews

## 049r — the two thieves, and Mary Magdalene told

> the Jews went; two thieves to the Lord Jesus, and put the Jews, the cross on the Lord Jesus; in turn, from two thieves | carried the Jews; who […] good; from the [sepulchre] [laid] the Lord Jesus. And Saint John went up into Bethany, to Mary Magdalene: [sought] Master, the Lord liveth [early] to Mary Magdalene [appeared]; and the Jews understood, went; Mary Magdalene, John [stood]; at that time

  1  to-go Jews two ~thief to Lord-Jesus and put
  2  Jews cross on-Lord-Jesus in_turn from two ~thief | carry
  3  Jews who-[?] good from [sepulchre] [laid] Lord-Jesus
  4  and to-go up holy-John inside Bethany to
  5  two-Mary Magdalene good [sought] Master living Lord [early]
  6  to-Mary Magdalene [appeared] and Jews SUBJ
  7  understand-go Mary Magdalene John [stood] time

## 049v — over the Cedron, and Simon carries it

> I go, the Jews were [at] the Kidron; and then the Lord went the Jews, over the Kidron; and then down [to the ground], to the sick, the Lord Jesus; and collapsed | from fall down the Lord Jesus […]; and the Jews knelt before the Lord Jesus; and the Jews spoke: healthy man, Jesus of Nazareth! And there came to the Lord | the Virgin Mary; and Simon carried it for the Lord; and | when the Jews […] cross […] within Eden and the Jews put the cross on the earth, and took off [his clothes]; believe on the Lord Jesus; food [garments] [they parted] the Lord; the Jews took off the Lord Jesus [his clothes], and

  1  go I Jews exist Kidron and then go Lord
  2  Jews over Kidron and then
  3  down [ground] to-°sick Lord-Jesus and collapse | from
  4  fall Lord-Jesus to-+cross and kneel Jew
  5  before Lord-Jesus and speak-Jews healthy_man^
  6  Jesus Nazareth and leave to-Lord | virgin
  7  Mary and Lord Simon cross carry and | then
  8  exist Jew [?]-+cross-[?] inside ~Eden
  9  and put-Jews cross on-earth and
 10  take_off believe on-Lord-Jesus food [garments]
 11  [they_parted] Lord take_off-Jews Lord-Jesus and

## 050r — laid upon the cross

> the Virgin Mary came to the Lord Jesus; and | from [they bound] the first … the Lord's handcuffs. And then the Lord Jesus, name […] of the Lord, have, the Jews trespass [wrote] this, within the commandment, this one apostle, the Lord's apostle; and the Jews saw [the title] the whole wide world in the year of suffering the Lord went; and [written], the Jews, within the Lord believed; and they laid the Lord upon the cross, and the Lord, the Jews nailed one hand. and the two [between] the cross, and could took, and the hand the Jews drew with the chain. and the hand the Jews nailed; and the Lord's foot could

  1  leave Virgin_Mary to-Lord-Jesus and | from
  2  [they_bound] of-exist-°first of-Lord handcuffs and_said
  3  Lord-Jesus name-[?]-~exist of-Lord have Jews
  4  trespass [wrote] this inside commandment this apostle-+one of-Lord apostle
  5  and see Jew [the_title] good all_the_world
  6  on-suffering-year go Lord and [written] Jews inside
  7  Lord believe and to-Lord set_on on_the_cross
  8  and Lord nail-Jews one hands
  9  and two [between] on_the_cross and can
 10  take* and hands chain-draw-Jews
 11  and hands nail-Jews and of-Lord foot can

## 050v — the title, and the ninth hour

> take, and the foot the Jews drew with the chain. and they pierced the feet; and all the Lord's [title]; and | of the Lord [three tongues] in the Lord, to, trench, to, trench, in the Lord Jesus Christ. And Pilate wrote upon a tablet: Jesus Nazareth, king of the Jews. And then the Jews write that the Lord said he is King of the Jews. But the Lord's writing, Jesus of Nazareth. And then Pilate: I have written, Pilate has written. And the two thieves; with the Lord they nailed them on the cross; and the Lord called two thieves, one […] the Jews; and this was out [at] the ninth hour. And then the Lord Jesus on the cross asked the Father, the Lord God of heaven.

  1  take* ~and foot chain-draw-Jews
  2  and foot pierce and every of-Lord [title] and | of
  3  Lord [three_tongues] inside Lord to-°trench-to-°trench inside Lord-Jesus-Christ
  4  and write Pilate on-one tablet Jesus
  5  Nazareth king Jew and_said Jew
  6  write Lord king Jew but Lord write
  7  Jesus Nazareth and_said Pilate write SUBJ
  8  who ~Pilate write and two ~thief to-Lord pierce
  9  on_the_cross and Lord call^ two ~thief one-[?]
 10  Jews and this out nine hour and_said Lord-Jesus
 11  on_the_cross the_father of-Lord God heaven ask-Lord

## 051v — three nails, and the sponge on a stick

> remained Mary's woe, than the Lord's three nails, long, [with which] I was pierced to the cross. And then the Lord Jesus: I thirst, the Lord; and | of Lord's apostles, when they bought grape, sweet, and wine; the apostles took [it to] the high priest; and the Lord; [somebody] took, but to the Jews [to] drink; in turn the Lord | took the Jews: vinegar, and [hyssop]; and the Lord. wine the Jews took on one sponge, and then the Lord's face; the Jews wiped the sponge; and the wine he took [into] his mouth, a little, on the [pine]. And then | the Lord Jesus on the cross offered [to] the Father, the Lord God of heaven I this Father, the Lord's soul into God the Father's

  1  remain* of-Mary woe than of-Lord three_nails long to
  2  I pierce to-cross and_said Lord-Jesus thirst Lord and | of
  3  Lord apostle then buy grape sweet and
  4  wine grab apostle high_priest = and
  5  Lord grab-+who but Jews-to drink in_turn Lord | grab
  6  Jews vinegar and [hyssop] and Lord
  7  wine grab Jews on-one sponge and
  8  then-Lord sponge face wipe_off-Jews and wine
  9  grab mouth little on-+pine and_said | Lord
 10  Jesus on_the_cross the_father of-Lord God heaven offer
 11  I this-father of-Lord soul inside of-God_the_Father

## 052r — two lines

> hands; and from the Lord Jesus, the Lord's soul, gave up the ghost. Here ends this Passion: the evangelist's suffering of the Lord Jesus.

  1  hands and from to-Lord-Jesus of-Lord soul give_up_the_ghost
  2  end this Passion = evangelist* suffering Lord-Jesus

## 052v — the earthquake, and Longinus

> And then the Lord Jesus, his soul, gave up the ghost on the cross; the earth quaked, the rocks and the stones rent; the sun and the moon this eclipse; and every tree among the people humbled itself; and all creation mourned, when Christ the Lord was crucified. And the Jews went. one soldier to Jerusalem, blind; and the soldier's name was Longinus; and the Jew's spear pierced the side the Lord Jesus Christ; and [pierced] the spear side of the Lord Jesus Christ; how the soldier [thieves] splash[ed] the Lord Jesus's blood on the place; through [it] he saw, and the soldier was healed; and the soldier believed in the Lord Jesus Christ, and the soldier saw, baptized, and saw, Jew

  1  and then Lord-Jesus of-Lord soul give_up_the_ghost on_the_cross earth
  2  quake rock stone rent sun and moon
  3  this eclipse and every tree among_the_people* this humble ~and every
  4  create mourn then Christ crucified Lord and go Jews.
  5  one soldier on-Jerusalem blind and name soldier
  6  exist Longinus and pierce Jew spear side
  7  Lord-Jesus-Christ and can [pierced] spear on
  8  side Lord-Jesus-Christ how? soldier [thieves] splash
  9  blood Lord-Jesus on-place through see and healing soldier
 10  leave and grab soldier believe Lord-Jesus-Christ
 11  and soldier see-baptize and see ~Jew

## 053r — after the ninth hour

> the power of the Lord Jesus Christ; and [many] believed in the Lord, but many [in] joy brought […], the Jews, home. The second Jews sadly accused, because [darkness] [came] the Jews, that they put to death, the Jews, the Son of God; and sadly went the Jews, […] the Jews, home; and this [from] was the ninth hour, and four hours from that hour on the cross suffered the Lord Jesus; and the Jews went [and] brought all […] home from [breast] [striking] in turn the apostles were apart; every one returned to the apostles; [stood] | on […] and one, and […]

  1  power Lord-Jesus-Christ and [many] inside Lord believe
  2  but many joy brought* [?]-Jews home
  3  second Jews sad accuse because [darkness] [came]
  4  Jews that* ~execute Jews son God and
  5  sad go Jews [?]-Jews home and this
  6  [from] out nine ~hour and two-two from ~hour
  7  on_the_cross suffer Lord-Jesus and-Jews go-?brought
  8  every [?]-°and_then home from [breast] [striking]
  9  in_turn apostle exist apart return every to-apostle [stood] | on
 10  Galilee and one and understand-eat

## 053v — Joseph and Nicodemus ask for the body

> the apostles cut off; and then two, somebody, have mercy, Jerusalem, one and his name was Joseph; the second Nicodemus; and then the two asked of Pilate was before the Lord Jesus; and the two had suffered. was before the Lord Jesus; and then the two went [away] Christ was crucified; and the two went to many Jews; and the two were, that is, good and merciful men; and then the two saw the Virgin Mary, and Mary. Magdalene. Many people went out of Jerusalem, and were afraid, because the Jews wanted to the Lord, every Lord [take down], because

  1  apostle cut_off and then two somebody-have_mercy Jerusalem ~one
  2  and name exist Joseph second
  3  ~Nicodemus and then two ask from Pilate
  4  ~exist-before Lord-Jesus and have two sufferer
  5  ~exist-before Lord-Jesus and then two go [away]
  6  exist Christ crucify and go to two
  7  many Jew and two people that_is good people have_mercy
  8  and then two see Virgin_Mary and Mary.
  9  Magdalene go many people on-Jerusalem and ~through
 10  startle because to Lord want Jew every Lord [take_down] because

## 054r — taken down, and the tomb sealed

> this was from | and [down] went down [from the cross] because Mary was […] fled […] the Jews; and in that place were these people, when the two Marys went to the people, and took Nicodemus [took] from the cross [by] name the Lord Jesus; in turn the three nails, […] Saint John took […] saw | the Virgin Mary; then [he] took the Virgin Mary into [his] bosom and did Nicodemus, of the living servant [linen]; and the two covered the body; and then [linen]; and Nicodemus put in, [by] name, at the end, the Lord Jesus; and they closed the Lord within the tomb; and they left a seal, the Jews; to the Lord four soldiers from were opened the chief of Jerusalem; and [the veil] went [part]. Here ends this holy gospel.

  1  this exist from | and [down] go down [from_the_cross]
  2  because exist-Mary on-+mount escape before.
  3  Jew and on-place exist this people then
  4  from two-Mary to-people go-two-Mary and grab
  5  ~Nicodemus on_the_cross name Lord-Jesus in_turn three three_nails
  6  seal-to grab holy-John then-+mouth-Mary see | virgin
  7  Mary then grab Virgin_Mary inside bosom
  8  ~and ~do Nicodemus of-living-servant
  9  [linen] and cover two body and then [linen] and
 10  put_in Nicodemus name-end-to Lord-Jesus and
 11  Lord inside tomb close and leave seal* Jews to-Lord two-two soldier from*
 12  were_opened* Jerusalem head ~and [the_veil] go [part] end this
 13  holy-gospel

## 054v — a rubric, naming Mark

> Here begins this holy gospel, written by Saint Mark.

  1  here_begins this holy_gospel write holy-Mark

## 055r — the three women at the tomb

> in the seventh chapter of his writing: at that time, when they went the three Marys [bought] to the tomb of Christ, because they had prepared [spices] another [anoint] […] Jesus: Mary Salome, and Mary the mother of James, and Mary Magdalene. And then these Marys [and] these Marys among [Salome] […] lifted up the stone from the tomb; and then | went on, the three [Marys] Mary came to the tomb of Christ, and saw the three Marys [the sabbath] the tomb [rolled away]; and then the three Marys within this the three Marys, and the three Marys entered; and remain, saw […] Jesus; but saw the first

  1  inside seven chapter of-write time then
  2  go the_three_Marys [bought] tomb Christ because-exist prepare
  3  [spices] another this-cut_off [anoint] ~exist-[?] Jesus
  4  Mary Salome and Mary James mother and
  5  Mary Magdalene and then this-two-Mary [and] this-two-Mary
  6  among [Salome] among-Mary-+the_three_Marys-[?]-+one-Mary
  7  lift_up from stone on-tomb and then | go_on-+three
  8  Mary to-tomb Christ and see the_three_Marys [the_sabbath]
  9  SUBJ tomb from [rolled_away] and then the_three_Marys inside this
 10  the_three_Marys and enter the_three_Marys and
 11  remain* see ~exist-[?] Jesus but see first^

## 055v — be not afraid, he is risen

> angel, sitting on the left side, from [a young man] within cover […] Jesus. And then Mary, through was afraid, because Mary supposed as a ghost. And then the angel: do not have [fear], the three Marys, [be affrighted] the three Marys be not afraid. He is risen, whom ye mourn — the Lord Jesus, whom they crucified, is risen seek; but […] within Galilee and […] the Lord's disciples and Peter, said the three Marys, [at the] side. This holy gospel. And then the three Marys went, this woman head, from this tomb of Christ; and | return Mary Magdalene went back to the tomb of Christ. At that time

  1  angel sit on-left direction from [a_young_man] inside exist
  2  cover ~exist-[?] Jesus and then Mary through
  3  startle because rather-Mary supposed* SUBJ how? ghost
  4  and_said angel do_not ~have-+the_three_Marys [be_affrighted]
  5  the_three_Marys through startle rise mourn to-Lord from Jesus
  6  crucify^ rise seek* but go-+the_three_Marys
  7  inside Galilee and say-+the_three_Marys
  8  of-Lord disciple^ and Peter say-+the_three_Marys side^ this
  9  holy-gospel and then-+the_three_Marys go this woman
 10  head from this tomb Christ and | return
 11  return back Mary Magdalene to-tomb Christ time

## 056r — Mary Magdalene takes him for the gardener

> the Lord Jesus appeared to Mary Magdalene in the form of a gardener. And then this gardener, the Lord Jesus Christ, | [said to] this woman: that [came], woman, mourning for the Lord; this, from Jesus, whom they crucified, is risen, because said the shepherd: [risen]; see, the shepherd, light in heaven town, chapter, in turn [she] stooped down [into] the tomb, bowed down; and the tomb light, open; and verily [he] could, that [he] rose. And the Lord Jesus stood before Mary Magdalene in that place; Mary [turning] that he: Master! And the Lord to Mary, [to] the apostles: go, the Lord, [to] the apostles. And Mary went to these two sisters, the women,

  1  appear Lord-Jesus Mary Magdalene inside form from one
  2  gardener and_said this gardener-Lord-Jesus-Christ | this
  3  woman that [came] woman mourn to-Lord this from
  4  Jesus execute rise seek* because
  5  say shepherd [risen] see-shepherd light on-+heaven
  6  town-chapter-in_turn stooped_down* tomb bow_down and tomb SUBJ
  7  light open and verily can that rise
  8  and leave Lord-Jesus before Mary Magdalene
  9  on-to-place Mary [turning] on-reason that
 10  he Master and Lord SUBJ to-Mary-apostle go-Lord-apostle
 11  and go-Mary to this two sister wife

## 056v — two lines

> and then Mary went with these women, and Mary would tell […]

  1  and then Mary understand-go-Mary this woman
  2  and want say Mary from

## 057r — he stands among them

> Magdalene saw the Master in the form of a gardener. At that time the Lord Jesus Christ stood in the midst, living, among the three Marys, the Lord, among these sisters Jerusalem. And then the Lord Jesus: the commandment of God among you: his mercy to whoever believes in the Lord, and in the Lord, from God the Father, ever. ever, amen. And then the Lord Jesus the three Marys; Mary saw within the tomb […] […] Jesus whom they crucified; and Mary Magdalene said […] Mary saw the Lord risen from the dead; and the Lord Jesus Christ stood among the three Marys […] the apostles. This holy gospel.

  1  Magdalene see-Magdalene Master inside image from gardener
  2  time leave Lord-Jesus-Christ middle living
  3  among the_three_Marys Lord among this sister
  4  Jerusalem and_said Lord-Jesus commandment God among
  5  you of-Lord have_mercy somebody to and believe
  6  inside Lord and inside of-Lord from God_the_Father ever.
  7  ever amen and_said Lord-Jesus SUBJ
  8  the_three_Marys see-Mary inside tomb brother-chapter
  9  from Jesus execute and say Mary Magdalene that*
 10  Lord-Mary see-Mary rise on-die and
 11  leave Lord-Jesus-Christ among the_three_Marys this apostle holy-gospel

## 057v — an Old Testament prophecy, and Mark again

> Written by Saint […] the prophet, the prophet, in the Old Testament, truly, the sixth chapter of his writing, and Saint Mark seven it is written. Said Saint […] the prophet: because he saith […] it is found, in the Old Testament is truly written this word: the Lord shall rise from the dead. the King; to the Lord thanks [not]; and the Lord destroyed hell, Christ; and from [Adam] [bound]: hell could [not], Satan. This is written | to Saint Mark, in the seventh chapter of his writing: when the Lord Christ upon the cross breathed out his soul, the earth quaked, the rocks and stones rend; the sun and the moon

  1  write holy-NAME.prophet
  2  prophet Old_Testament righteous
  3  six chapter of-write
  4  in_turn holy-Mark seven
  5  write say holy-NAME.prophet
  6  because say SUBJ exist find
  7  inside Old_Testament righteous write this word stand_up-Lord on-die-Lord
  8  king to-Lord thanks [not] and destroy Lord hell Christ and from
  9  [Adam] [bound] hell can Satan this_is write | to
 10  holy-Mark inside seven chapter of-write then Lord
 11  Christ on_the_cross of-Lord soul exhale earth quake
 12  rock stone this rend sun and moon this

## 058r — the harrowing of hell

> eclipse; and every tree into the world humbled itself; and all creation mourned when Christ was crucified. And four hours the Lord Jesus suffered upon the cross; and the Lord within the tomb | the apostles laid him, Mary, the angel; and then the Lord within the tomb they laid, the Lord; and at that hour, at that time, came from the Father God in heaven, from the Father, an angel within, before the Lord Jesus; and rise, from prayer; in turn the angel within the tomb stay in turn to the Lord; the Lord went to hell, and destroyed hell; and who the people who died within a hundred years, and within | five sat, year; and within nine […]; and nine years; all the prophets went into hell; and [brought out] three souls, all out the Lord went, in turn three souls within hell stayed; the Lord | spoke.

  1  eclipse and every tree into_the_world* this humble and every create mourn
  2  then Christ crucified and two-two hour
  3  on_the_cross suffer Lord-Jesus and Lord inside tomb | put-apostle
  4  Mary-angel and then-Lord inside tomb lay Lord and
  5  hour time go the_father God heaven
  6  on-of-father angel inside ~exist-before Lord-Jesus and
  7  rise* from ~pray in_turn angel inside tomb stay
  8  in_turn to-Lord go-Lord on-hell and hell destroy and who
  9  people die inside one hundred-year and inside | five
 10  sit-~year and inside nine-[?] and nine-~year every prophet
 11  go on-netherworld and [brought_out] three soul every out go Lord
 12  in_turn three soul inside hell stay Lord | speak.

## 058v — Adam's soul kneels to the Virgin

> Saint Augustine: within many years, and one soul [counsel] went into heaven; but then to the Lord went to the souls, the Lord, and [brought out] three souls every [one] out the Lord went to the souls; and the Lord appeared the blessed Virgin Mary; and Adam's soul knelt before the blessed Virgin Mary; and the girl had mercy, asked, and blessed the blessed Virgin Mary; and all the souls, soul upon soul, left before the blessed Virgin Mary; and within Paradise the souls, the Lord, the souls; and the Lord went to the souls; and then twenty-five hours; and this was […] the sixth hour.

  1  Saint_Augustine inside many-to-year and one soul [counsel]
  2  ~go inside heaven = but then to-Lord
  3  to-soul-soul-soul-soul-soul go Lord and [brought_out] three soul
  4  every* out to-go Lord soul and Lord appear Lord
  5  blessed Virgin_Mary and kneel ~Adam soul
  6  before blessed Virgin_Mary and girl SUBJ-have_mercy
  7  ask and bless blessed Virgin_Mary
  8  and to-soul-soul-soul every leave before blessed
  9  Virgin_Mary and inside Paradise soul Lord soul
 10  and go Lord soul and then two-ten-ten five
 11  hour and this out thirty-[?] six hour

## 059r — one line

> And on the third day the Lord Jesus Christ rose from the dead.

  1  to-and on_the_third_day from die stand_up Lord-Jesus-Christ

## 059v — the road to Emmaus

> Here begins this holy gospel, written by Saint Luke, in the first [chapter] of his writing: at that time, when there went two apostles out of Jerusalem into a town; and | was, the chapter year, by name, was Emmaus; and then the two apostles found [him] from the living Lord Jesus; and then the two talked of how the Lord, he was truly somebody, truly the Lord, preaching various [things] miracles he did [spoke of]; the two apostles; the Jews' chief crucified him. At that time there appeared to the two apostles the Lord Jesus, in the form of a traveller; and then

  1  here_begins this holy_gospel
  2  write holy-Luke one
  3  of-write time
  4  then go two
  5  apostle Jerusalem inside one
  6  town and | exist-chapter
  7  ~year-+name exist Emmaus and then find-two-apostle from living
  8  Lord-Jesus and then two talk^ how?-Lord he
  9  exist righteous somebody righteous Lord ~preach various
 10  wonder^ do [spoke_of] of-two-apostle Jew
 11  head crucify^ time appear
 12  two-apostle Lord-Jesus form traveller and then

## 060r — the Lord asks the two what they are speaking of

> The two apostles [drew near] Lord Jesus, and the two apostles began to talk, and the Lord talked. And then the Lord Jesus: O, of the Lord two apostles, brother, saying, two apostles, Lord, how, saying among [one another] have, two apostles, because they said the Lord Jesus Christ apostle, that the two men spoke of the Lord; I, the two Lord's apostles, three [with] the Lord. And then Luke, this [named] the way, the man, this Lord, this good remain [sad] how [knowest not] the miracles [in] Jerusalem, done as somebody [the Jews] […], the head, truly crucified this Jesus; and the Lord came into the world, went went, preaching […], various miracles he did.

  1  two-apostle [drew_near] Lord-Jesus and two-apostle talk and
  2  Lord talk and_said Lord-Jesus oh of-Lord
  3  two-apostle ~brother say two-apostle Lord how? say ~among
  4  [one_another] have two-apostle because say exist Lord-Jesus-Christ
  5  apostle that* two somebody from-Lord speak I two
  6  Lord apostle three Lord and_said Luke this [named]
  7  way somebody this Lord this good remain* [sad]
  8  how? [knowest_not] SUBJ miracle Jerusalem ~do as
  9  somebody [?]-Jews head righteous
 10  crucify^ this Jesus and the_Lord into_the_world* go-Lord
 11  go-+SUBJ preach-[?] various miracle do

## 060v — the miracles, and the women's news they did not believe

> the eyes of the blind, through [him] light; the dead, resurrected; | the lame lame the body, and the evil, those possessed by the evil one, healed and the Lord was from [the third day] up he rose, the Lord; and said one woman, the head the news was of the Lord up he rose; the news the two apostles [certain] believed, who from the Lord, from the dead the Lord stood up, because as the Lord's brother, to rot this pleasing, and who from the Lord, from the the dead stood up. And then the Lord Jesus: you two […] the man, to hide, the two believing

  1  eyes ~blind SUBJ through light die SUBJ resurrect | lame
  2  lame body and evil^ possessed heal
  3  and Lord SUBJ exist from [the_third_day] up
  4  stand_up-Lord and say one ~woman ~head
  5  news exist-Lord up stand_up-Lord news two
  6  apostle [certain] believe who from Lord from die
  7  stand_up-Lord because as of-Lord brother-to
  8  rot this pleasing who from Lord from
  9  die stand_up and_said Lord-Jesus you two
 10  ~exist-+baptize-to-~humble somebody to-hide believe-two

## 061r — O fools and slow of heart, and Cleopas is named

> You two, this, to, rise from prayer And then the Lord Jesus left; the Son of God was dead. more than these, rise from prayer, from prayer the Lord, from God the Father in heaven; and the beginning, through the Lord Jesus expounded, from Adam, the trespass, the scripture said. And then Cleopas, Luke, this Lord, to the two [foolish] the Lord wanted good, said. And then the Lord Jesus, from Abel […] signified this Jesus crucified, how, in turn [slow of heart] died, the brother's he said and this Jesus died, the Lord's brother. And then the Lord Jesus, from Noah

  1  ~you-two this to-+SUBJ rise* from pray
  2  and_said Lord-Jesus leave exist die son God
  3  more_than_these* rise* from pray from pray
  4  the_Lord from God_the_Father heaven and beginning^ through
  5  explain Lord-Jesus from ~Adam ~trespass scripture^
  6  say and_said Cleopas Luke this Lord to-two [foolish]
  7  want-Lord good say and_said Lord-Jesus from Abel
  8  Abel symbolize this Jesus execute how? | in_turn
  9  [slow_of_heart] die of-brother he_said* and this Jesus
 10  die of-Lord brother and_said Lord-Jesus from Noah

## 061v — Abraham as the figure of the crucifixion

> Noah symbolized this Jesus put to death, as Noah redeemed all the world; in [the wood] this [Isaac], and on this Jesus put to death, every [one] is saved; Adam gained. And then the Lord Jesus, about Abraham: Abraham symbolized this Jesus crucified, and Lord Jesus said, said the Lord. Abraham, to the angel of the Lord God — Abraham took his son […] and the Lord […] […] who did, Abraham on tie up the faggots […] in turn Abraham took sword who Isaac wished to slay

  1  ~Noah symbolize this Jesus execute as ~Noah
  2  redeem every world inside [the_wood] this [Isaac] and on-this Jesus
  3  execute be_saved every ~Adam gain and_said
  4  Lord-Jesus about Abraham Abraham symbolize this
  5  Jesus execute and say Lord-Jesus say exist Lord_God.
  6  Abraham on-~angel of-Lord_God Abraham take^
  7  of-son Isaac and Lord sacrifice.
  8  on-to-+offering who do Abraham on
  9  tie_up faggot on-+Isaac in_turn Abraham
 10  take^ sword who Isaac want slay

## 062r — the mount, the ram, and the angel

> And then he went on this, to the mount […] wanted a sacrifice. And then Isaac: O, my father donkey and went far […] and a, and the ram, and a the lamb, who? Isaac's father, sacrifice; and said the father Abraham: from whom the Lord God [gives] the ox. offering and then tie up bundle of wood of Isaac, sheep, living, the Lord wanted to slay, and the Lord God shouted in the cloud to the angel: stop! Abraham, to the whole wide world, the Lord's love, this is

  1  and then go on-this to-mount [?]-+Isaac
  2  want sacrifice and_said Isaac oh
  3  of-father donkey* and go far
  4  to_whom-+one and one and sheep and one
  5  lamb who Isaac father sacrifice and say
  6  the_father Abraham from who Lord_God ox.*
  7  offering and then tie_up bundle_of_wood*
  8  of Isaac ~sheep-living want Lord slay and
  9  shout Lord_God in_the_cloud on-angel stop
 10  Abraham to-all_the_world SUBJ Lord of love this_is

## 062v — he made as though he would go further, and they constrained him

> the Lord's peace. And then the Lord Jesus: as was Isaac, as he gave his father's [son], so this Jesus was crucified the Lord gave, his divine Father, and he rose the Lord, from prayer, because the Lord, from prayer, the Father, God of heaven. And then the apostles of the Lord went, this town. And then the Lord Jesus: go, two apostles, you, because I the Lord had a long way; and the Lord began, the two apostles persuaded; and then the Lord was [there]; the two apostles persuaded, and | the two the Lord's apostles went, and then the Lord's two apostles into the room went the Lord's two apostles, and the two apostles sat the Lord at the table, and

  1  Lord peace and_said Lord-Jesus as exist Isaac
  2  to-grab of father this and this Jesus execute exist
  3  to-grab-Lord of-Lord God_the_Father and SUBJ rise*
  4  Lord from ~pray because-+the_Lord from ~pray the_father
  5  God heaven and then go-apostle-Lord this town
  6  and_said Lord-Jesus go-two-apostle you because I
  7  have-Lord long way and Lord beginning^ two apostle
  8  persuade and then-Lord exist two-apostle persuade and | two
  9  apostle-Lord go and then two-apostle-Lord on-+room | go
 10  two-apostle-Lord and sit-two-Lord-apostle to-throne and

## 063r — the breaking of bread, and he vanished out of their sight

> the apostles carried, the rest, cup, water and wine, and. Lord Jesus took one cup and cup [he blessed] this, how, then [vanished] alone […] and from […] today's, and wine, and the cloud the Lord Jesus blessed; and then the other apostles | ate, the two apostles; and the two apostles drank in the place; the two apostles recognized [him]. in the Holy Spirit, the farm, truly the Son of God to the Lord Jesus; the other apostles, of, to leave this, and left among the other apostles, the Lord Jesus Christ, the chapter answered to the Lord [vanished] the two apostles saw. Here ends this holy gospel.

  1  carry apostle the_rest^ cup ~water and wine and.
  2  grab Lord-Jesus one cup and cup
  3  [he_blessed] this how? then [vanished] °alone-[?]
  4  and from bread and wine and cloud
  5  bless Lord-Jesus and then the_rest^ apostle | eat-two
  6  apostle and drink-two-apostle on-place recognize-two-apostle
  7  on-spirit holy-farm SUBJ righteous son God
  8  to Lord-Jesus the_rest^ apostle of-to-leave-this and
  9  leave among the_rest^ apostle Lord-Jesus-Christ chapter-?answered
 10  Lord-to [vanished] see-two-apostle here_ends this holy_gospel

## 063v — Thomas was not with them

> Here begins this holy gospel written by holy John within the twentieth chapter of his writing. At that time the disciples met within Jerusalem in one house, six in the Lord's house, where the Lord Lord Jesus, after supper; and then holy Thomas went Didymus one Saturday evening, to the apostles; and the apostles said, Thomas, apostle, we have seen the Lord. And holy Thomas said, I do not believe this every [one]; if this, if Thomas believes this, if not | see Thomas, the Lord's side; and unless Thomas puts his finger within | of

  1  here_begins this holy_gospel
  2  write holy-John
  3  within^ two-ten-ten chapter
  4  of-write time
  5  meet disciple^ within^ Jerusalem
  6  within^ one house six
  7  within^ Lord house where Lord_God
  8  Lord-Jesus dinner ~do and then go holy-Thomas Didymus*
  9  one Saturday evening to-apostle and say-apostle Thomas disciple^
 10  see Lord and say holy-Thomas this-Thomas this not believe
 11  every this if this-Thomas this believe if not | see
 12  Thomas of-Lord side^ and of-Thomas finger not put within^ | of

## 009r — reach hither thy finger, and my Lord and my God

> the Lord's side, who from the Lord, rose from the dead; at that time stood the Lord Jesus Christ in the midst of the disciples, closed, and said: peace [be] you; and in joy [they] stood. the apostles in turn; Thomas began have and Lord Jesus said, Thomas, thou shalt go to put thy finger, Thomas, into the Lord's wound [blessed] see and believe; and [have not] Lord Jesus, the Lord's wound And the Lord Jesus said: Thomas, happy from, and somebody sees and believes; but and happy from, and not see, but believe. Here ends this holy gospel. And he knelt, holy Thomas, before Lord Jesus, and holy Thomas said, Lord, Thomas's God; Thomas asked the divine one: have mercy on Thomas, who, this Thomas, committed sin against the divine one.

  1  Lord side^ who from Lord from die stand_up time stand^ Lord-Jesus-Christ
  2  middle disciple^ closed and say peace^ you exist and joy stand^
  3  disciple^ in_turn Thomas begin have and say Lord-Jesus Thomas
  4  go-+name to put of-Thomas finger within^ of-Lord wound
  5  [blessed] see believe and [have_not] Lord-Jesus of-Lord wound
  6  and say Lord-Jesus Thomas happy from and somebody see
  7  and believe but and happy from and not see
  8  but believe here_ends this holy_gospel and kneel
  9  holy-Thomas before Lord-Jesus and say holy-Thomas Lord
 10  of-Thomas God of-Thomas ask-Thomas he-DIV
 11  have_mercy Thomas who this-Thomas commit sin against he-DIV

## 009v — Thomas blesses him, and the Good Shepherd begins

> this Thomas, he believed; Thomas remained; he truly the Son of the living God. And then Thomas was blessing the Lord Jesus Christ. And Thomas's sin find mercy. And the Lord Jesus said: every [my] and [God] [my] from [that day] on believing in the Lord Jesus Christ, every heathen man, Jew, pagans' sin find mercy [on his] side. This apostle's holy gospel; bless the Lord God. Here ends this holy gospel. Written by holy John in the tenth chapter of his writing. At that time Lord Jesus said […] supper, apostles, of the Lord: I, the good shepherd; in turn you, from the apostles

  1  this-Thomas he believe-Thomas remain* he righteous
  2  son living God and then Thomas exist bless Lord-Jesus-Christ.
  3  and sin Thomas find_mercy^ and say Lord-Jesus every [my] and [God] [my] from
  4  [that_day] on-believe to-Lord-Jesus-Christ every heathen man^ Jew
  5  pagans sin find_mercy^ side^ this apostle holy-gospel on-Lord_God bless
  6  here_ends this holy_gospel
  7  write holy-John
  8  inside ten chapter of-write
  9  time say Lord-Jesus
 10  on-who-+who-to dinner apostle
 11  of-Lord I good shepherd in_turn you from apostle

## 064r — the good shepherd and the hireling

> his sheep, and the Lord knows his sheep, and I know the Lord's sheep. And then the Lord Jesus: | then there was a king, and then he had two shepherds, one who [kept] the home well, the shepherd; the second, a labourer. shepherd. And then, of the two shepherds […] from one herd of sheep of this king; and then came the wolf to this sheep, and would carry this sheep away and this hired shepherd, of the shepherds leave this sheep; in turn this good shepherd, the home, from the shepherd redeemed this sheep; and the sheep follow within the herd. and within, good, before, [he] gives; and one carries away; and

  1  of-Lord sheep and Lord ~know of-Lord sheep and
  2  I ~know of-Lord sheep and_said Lord-Jesus | then
  3  exist one king and then ~have two shepherd
  4  one ~who home good shepherd second labourer
  5  shepherd and then from two shepherd chapter-[?] from one
  6  herd sheep this king and then go wolf
  7  this sheep and want this sheep from-~carry
  8  and this labourer shepherd from shepherd leave
  9  this sheep in_turn-this good shepherd home from shepherd
 10  redeem this sheep and sheep follow inside herd
 11  and inside-good-before give^ and one carry_away and

## 064v — the good shepherd giveth his life, and other sheep I have

> if [he does] not leave, out [of] this herd, and go. The wolf, and the sheep carried away. And then Lord Jesus: he who is the good shepherd, of the shepherds, lays down the Lord's life for the Lord's sheep; and the Lord takes and one [fold] he who is the good shepherd, of the shepherds, the gate of the Lord's sheep; and then [they] hear the voice of the Lord God; the sheep, blind, the Lord, the shepherd, go. And then the Lord Jesus, the Lord's apostles, […] by night, one sheep and these sheep I will bring to you blind and go you shall be every one, one shepherd, shepherds one; thanks to the Lord. Here ends this holy gospel.

  1  if not_leave out this herd and go.
  2  wolf and sheep carry_away and_said
  3  Lord-Jesus to-+he_who good shepherd from shepherd put
  4  down of-Lord life to-of-Lord sheep and grab-Lord
  5  and one [fold] he_who good shepherd from shepherd
  6  SUBJ gate of-Lord sheep and then hear
  7  voice of-Lord_God sheep ~blind-Lord shepherd go and_said
  8  Lord-Jesus apostle of-Lord [...] [?]-°by_night one sheep
  9  and this-sheep want to-you ~blind go and
 10  you exist every one shepherd shepherd
 11  one to-Lord thanks Lord_God here_ends this holy_gospel

## 065r — beware of false prophets

> Here ends this holy gospel. Written by holy Matthew in the last of his writing. time | then of the day of Lord Jesus Christ, thirty-three [years]. At that time Lord Jesus said to the Lord's apostles: [they] go to you in sheep's clothing false prophets, pagan, evil [clothing] they are pagan evil, the Lord's trespass [ravening wolves] mouth the apostles, men, and pagan, evil clothes, because they are false | of

  1  here_ends this holy_gospel
  2  write holy-Matthew
  3  inside seven of-write
  4  time | then
  5  day Lord-Jesus-Christ
  6  thirty three
  7  time say Lord-Jesus
  8  apostle of-Lord go to-you in_sheep's clothing
  9  false prophet pagan evil [clothing] exist pagan
 10  evil trespass Lord [ravening_wolves] mouth* apostle man^
 11  and pagan evil clothes^ because exist false | of

## 065v — by their fruits ye shall know them

> confess the Lord's name. And then the Lord Jesus, the Lord's apostles: verily verily I speak to you. And then the Lord Jesus: do not pick figs from thistles, but on the fig; and | do not pick food, grapes from the thornbush, but on the grapevine, because who [is] a good tree takes this good fruit; | in turn if dying, the evil tree takes this bad fruit. Because a good tree can take bad fruit, but every good fruit it takes; if a bad tree can take good fruit, but every bad fruit it takes. And then the Lord Jesus: many people were shouting | on the judgment the Lord's year, to the Lord; this man's trespass; this the Lord preached, and Lord Jesus said

  1  Lord name confess and_said Lord-Jesus apostle of-Lord
  2  verily verily I you speak and_said
  3  Lord-Jesus pick_not fig on-thistle ~but on-fig and | pick_not
  4  food grape thornbush* ~but on-grapevine
  5  because who good tree this good_fruit grab | in_turn
  6  ~if die-evil tree this bad_fruit grab
  7  because good tree can bad_fruit grab ~but
  8  every good_fruit grab ~if bad tree
  9  can good_fruit grab ~but every bad_fruit
 10  grab and_said Lord-Jesus many people exist shout | on-judge
 11  year Lord to-Lord this man^ trespass this Lord preach and say Lord-Jesus

## 066r — the weeping and gnashing of teeth

> and [whosoever], the man, can say: Lord, go, Lord God; the Lord creates | of the man, and the Lord saved every one, Adam gained, this man [shall enter] the year out, the man chapter of his Father, and this man everybody [shall enter] into [many] heavenly homes of the Lord, God the Father; but every [one] goes, the man, to ever-ever hell fire; there is seen the grinding of teeth, weeping, for ever and ever; in turn, and the man is [not] the man [who] says three [times]: Lord, Lord, Lord; saved [by] the Lord, all the world; this man every [one] goes into [many] heavenly homes of the Lord, God the Father; there is the man's joy, to the Lord, and the angels, and the Lord's Father God, for ever and ever, amen. Here ends this holy gospel.

  1  and [whosoever] man^ can-say-Lord go Lord_God Lord create | of
  2  man^ and be_saved Lord every ~Adam gain this man^
  3  [shall_enter] out-year man^ chapter* of-Lord God_the_Father and this man^
  4  everybody = [shall_enter] inside [many] heavenly home of-Lord
  5  God_the_Father but every go man^ on-ever ever hell
  6  fire there exist see grinding tooth weep
  7  for_ever_and_ever = in_turn and man^ exist [not] man^
  8  say three Lord-chapter-Lord-chapter-Lord be_saved Lord every world this man^
  9  every go inside [many] heavenly home of-Lord God_the_Father there
 10  exist man^ joy to-Lord and angel and of-Lord-father
 11  God for_ever_and_ever = amen here_ends this holy_gospel

## 066v — whatsoever ye shall ask the Father in my name

> Here begins this holy gospel written by holy John in the fourteen-and-one chapter of his writing. At that time Lord Jesus said to his apostles, at the last supper, verily verily I speak to you: love. Whatsoever ye shall ask of the Lord's Father in the Lord's name, ye shall all receive it saved from heaven, from I, Christ. And this said, spoke the Lord Jesus: on the way, to his apostles, and said, O the Lord's son.

  1  here_begins this holy_gospel
  2  write holy-John
  3  fourteen-+one chapter of-write
  4  time say Lord-Jesus
  5  apostle of-Lord at_the_Last_Supper =
  6  verily verily I you speak love
  7  whatever you exist ~ask from of-Lord-from God_the_Father
  8  inside of-Lord name every you be_saved grab
  9  from heavenly from I Christ and this say speak Lord-Jesus
 10  on-way apostle of-Lord and say oh of-Lord son.

## 067r — whose son is he, and thou art the Son of the living God

> I ask you: whose son? | you yours. To the Lord spoke the apostles, and the apostles said: Master, the apostle, this Lord believe that this Lord [sat] truly the Son of the living God. And the Lord Jesus: O the Lord's son, I cast this out. if you believe this, it is to the Lord I [am] truly the Son of the living God; mouth, who […] one | you yours, believe, brother, because I who go to death, to the Lord's death, name […]; I ask you [shall be raised] in the Lord herd the apostles, because you are apostles, many sorrowing you have on the Lord, because you apostles, all the apostles | learn, chapter [oh Lord] […] return, mourn, and to and one and

  1  ask^ I you whose? son | ~you
  2  yours to-Lord speak apostle and say apostle Master apostle this Lord
  3  believe that* this Lord [sat] righteous son living God and say
  4  Lord-Jesus oh of-Lord son I this exorcise
  5  if-to you this believe exist to-Lord
  6  I righteous son living God mouth-+who and [?]-+one | ~you
  7  yours believe ~brother because I who-go
  8  on-die to-Lord-die name-[?] ~ask I you [shall_be_raised]
  9  inside Lord herd apostle because you exist apostle many sad
 10  on-Lord have because you apostle every apostle | learn-chapter
 11  [oh_Lord] [...] return mourn and to-and one and

## 067v — he that believeth and is baptized shall be saved

> one [died]; and I on the third day up. stood up; and I, you, brother, within belief did; believe there is leave for ever and ever, amen. And the two men [sendeth] you, and the apostles are one God; the apostles believe, and the man who is outside this believe and one man is saved, but every man is damned and the man who believes in […] Christ, this somebody is saved, because this [is] to the Lord, one God. Here ends this holy gospel. whatsoever the man has, he asks in Jesus' name he is saved, speaks holy Paul the apostle

  1  one [died] and I on_the_third_day up.
  2  stand_up and I you ~brother inside
  3  believe ~do believe* exist
  4  leave for_ever_and_ever = amen and two
  5  somebody [sendeth] you and exist apostle one
  6  God believe apostle and somebody exist out this believe
  7  and one somebody be_saved but everybody = be_damned
  8  ~to and somebody exist believe inside [?]-~Christ this
  9  somebody exist be_saved because this to-Lord one God
 10  here_ends this holy_gospel whatsoever* have somebody ask
 11  inside Jesus name be_saved speak holy-Paul apostle

## 068r — love the Lord, and thy neighbour as thyself

> this word, Paul's brethren; Paul the man has, he asks in Jesus' name; three things Paul the man asks; in turn who wants, somebody, Paul, to be saved first; | somebody asks Paul: love the Lord God highest [above] all creation, and everybody as the neighbour as the neighbour; and somebody is saved. The second has, Paul the man asks, in Jesus' name go away believe; Paul the man asks of Lord Jesus, in his name. The third Paul the man has, he asks, in Jesus' name, saved by Lord Jesus, in his [believeth] name, and the man shall be saved. Here ends this apostle's holy gospel.

  1  this word brother of-Paul have somebody-Paul ask
  2  inside Jesus name three ask-somebody-Paul | in_turn
  3  who want-somebody-Paul be_saved first | ask-somebody
  4  Paul love Lord_God highest all^ create and everybody = as neighbour
  5  to-+neighbour and exist somebody be_saved second have
  6  somebody-Paul ask inside Jesus name leave
  7  believe ask somebody-Paul from Lord-Jesus inside of-Lord
  8  and-to-end-+name third have somebody-Paul ask | inside
  9  Jesus and-to-end-+name be_saved from Lord-Jesus inside of-Lord
 10  [believeth] and-to-end-+name and exist somebody be_saved end
 11  this apostle holy-gospel

## 068v — of sin, and of righteousness, and of judgment

> Here begins this holy gospel written by holy John, in the sixteenth chapter of his writing. At that time Lord Jesus said to his apostles, at the last dinner: I go, the Lord, to the Lord's God the Father; you learn, do, the heavenly land; that is, I leave to death; the Lord dies; and I go [from] you | [the Paraclete] the day; if I do not die, to you [he] does not go away the Holy Spirit. The Lord dies, and I [send to] you the Holy Spirit goes, and you shall see two judgment: first, of sin; second, of righteousness; third, of judgment.

  1  here_begins this holy_gospel
  2  write holy-John inside
  3  ten-six chapter of-write
  4  time say Lord-Jesus
  5  apostle of-Lord on-last
  6  dinner I go-Lord of-Lord God_the_Father you learn
  7  do heavenly land that_is I leave*
  8  on-die Lord die and I you go | [the_Paraclete]
  9  day if I does_not die to you go_not_away
 10  holy-spirit Lord die and I you
 11  go holy-spirit and you exist see-two
 12  judge first from sin second from righteous third judge

## 069r — the Spirit, the tongues, and the signs

> And then this Holy Spirit goes to you, from the Spirit through it you receive humble every good thing, and there are the apostles, new, new tongues say [truly]; you [shall] be many miracles say which the mouth speaks in the Old Testament word, and it lives goes before [all men]; baptize [until] doomsday. because there are many miracles done. Here ends this holy gospel. Here begins this holy gospel written by holy Luke, in the tenth the last chapter of his writing. Said Lord Jesus to his apostles, at the last dinner: I [am] the grapevine; God the Father of the Lord

  1  and then you go this holy-spirit from-spirit
  2  through grab you humble every good and exist
  3  apostle new new language say [truly] you exist many
  4  miracle say which-mouth exist inside Old_Testament word and living exist
  5  go before [all_men] ~baptize [until] doomsday
  6  because-exist many miracle ~do here_ends this holy_gospel
  7  here_begins this holy_gospel
  8  write holy-Luke inside | ten
  9  seven chapter of-write say
 10  Lord-Jesus apostle of-Lord | on
 11  last dinner I grapevine God_the_Father of-Lord SUBJ

## 069v — I am the vine, ye are the branches

> the vineyard; in turn you are the branches, and God the Father, the Lord's vineyard, the angel, the vine, this | name, Lord the grapevine; and without the vine shoot | [nothing] name he takes this and cuts it off, and vine branch out on the way cast out. And then the Lord Jesus: and the man who is within the Lord, […] carried by the Lord, stays; and I am within him. And then the Lord Jesus, the Lord's apostles: O | of the Lord's son, this keeping of the commandment of love; the apostles can [abide] understand, who, I, you, [bear fruit] | speak Lord; and the man who is in the Lord's commandment of love, the man carries, from the man who is within the Lord's commandment […] stays, and I

  1  farm in_turn you vine_shoot and go
  2  God_the_Father of-Lord farm angel vine* this | name-Lord
  3  grapevine and without vine_shoot | [nothing]
  4  name take^ this cut_off and vine_shoot out
  5  ~way cast_out and_said Lord-Jesus and man^ exist
  6  inside Lord-[?]-~carry-Lord stay and I exist
  7  inside him and_said Lord-Jesus apostle of-Lord oh | of
  8  Lord son this keeping_the_commandment_of_love can apostle [abide]
  9  understand who I you [bear_fruit] | speak
 10  Lord and man^ exist of-Lord commandment-love carry-somebody from
 11  man^ exist inside Lord-commandment-[?] stay and I

## 070r — the branch that beareth not is cast into the fire

> the Lord is within him; the Lord Jesus said: who did to God the Father of the Lord, this vine shoot [withered] is | good the grape takes these vine shoots from the blind; the Father of the Lord, so that every grape carries; and the Lord's Father goes two evil vineyards, and this in turn what vine branch takes the evil farm, and casts [it] out into hell fire; there is seen the grinding of teeth, crying, ever ever. And then the Lord Jesus: as the Father of the Lord the Lord loves, and I love you. And the Lord Jesus said: O the Lord's son, and you love, because the disciples are loving

  1  exist-Lord inside him say Lord-Jesus who ~do
  2  to-God_the_Father of-Lord this vine_shoot [withered] exist | good
  3  grape grab these vine_shoot from-~blind the_Father
  4  of-Lord so_that every grape carry and go father of-Lord
  5  two evil farm and this in_turn-what vine_shoot
  6  grab evil farm and SUBJ cast_out on-hell
  7  fire there exist see grinding tooth crying ever
  8  ever and_said Lord-Jesus as the_Father of-Lord
  9  Lord love and I you love and say Lord-Jesus oh
 10  of-Lord son and you love because-exist disciple^ love

## 070v — ask in my name, and Paul's three askings again

> within the commandment you are; the Lord's commandment of love the apostles carry Lord Jesus said, and the man who carries [in my name] […] [must] you first say: love the Lord, whatever | you [ye] shall ask the Father, from the Lord's Father, in the Lord's name, ye shall all receive it saved. Here ends this holy gospel. whatsoever the man has, he asks in Jesus' name saved, speaks holy Paul the apostle this word; Paul's brother has, somebody, Paul asks in Jesus' name; three [things] asks somebody, Paul: if Paul the man would be saved, first he asks

  1  inside commandment you exist of-Lord the_commandment_of_love carry-apostle
  2  say Lord-Jesus and somebody exist carry [in_my_name] this-?Pharisees-+one
  3  [must] you first say Lord love whatever | ~you
  4  exist ~ask the_Father from of-Lord the_Father inside
  5  of-Lord name every you be_saved grab
  6  here_ends this holy_gospel whatsoever* have somebody ask
  7  inside-Jesus name be_saved speak holy-Paul apostle
  8  this word brother of-Paul have somebody-Paul
  9  ask inside-Jesus name three ask somebody-Paul
 10  if want somebody-Paul be_saved first ask

## 071r — the great commandment, repeated

> somebody, Paul: love the Lord God, from the literal, [above] every creature, and everybody | how? the neighbour […] and the man shall be saved. The second has somebody, Paul, asks within the Lord's | and name: leave, believe; asks somebody, Paul: of Lord Jesus, in the Lord's name. The third he has, Paul the man asks in the Lord's name, saved by Lord Jesus, in the Lord's name; and the man shall be saved. Here ends this apostle's holy gospel [amen] Here begins this holy gospel, written by holy Luke, in [fourteen] of his writing. Lord Jesus said to his apostles at the last supper: you shall be driven out

  1  somebody Paul love Lord_God from literal every create and everybody = | how?
  2  to neighbour [?]-from-°creature and exist somebody be_saved
  3  second have somebody Paul ask inside of-Lord | and
  4  name leave believe ask somebody Paul
  5  from Lord-Jesus inside of-Lord name third have
  6  somebody Paul ask inside of-Lord name be_saved
  7  from Lord-Jesus inside of-Lord name and exist
  8  somebody be_saved end this apostle holy-gospel [amen]
  9  here_begins this holy_gospel write
 10  holy-Luke inside [fourteen] | of
 11  write say Lord-Jesus apostle of-Lord
 12  at_the_Last_Supper = you | chase

## 071v — a woman when she is in travail hath sorrow

> the Jews out, on hearing; how one had mercy, the apostle believes, every for the Lord's name. And then you they want to chase, the apostles say; this is it: out, who, apostle [by] apostle Master spoke and the Lord, the Jews put to death; and you shall be many sad on the Lord, have; in turn, one, the Jews are joy [shall be turned]; your sorrow is, and ascends until little, how? then one woman, the head, a son is born, remains many sufferings, has; in turn, | then the son is born, and of that comes joy over the son and you sad; in turn the Jews joy want; many sad cast out, and that in the year of judgment; in turn your sorrow, much joy cast out, and that in the year of judgment. Here ends this holy gospel.

  1  Jews out on-hear how? one have_mercy-apostle-~believe every
  2  to-of-Lord name and then you
  3  chase want apostle say this_is ~out who apostle-apostle
  4  Master [spoke] and Lord Jew die and you
  5  exist many sad on-Lord have in_turn one Jews-exist
  6  joy [shall_be_turned] you sad exist and-ascend ~until
  7  little how? then one woman head
  8  son be_born remain* many suffering have in_turn | then
  9  exist be_born from-~exist on-son joy this-Peter
 10  and ~you sad in_turn-Jews joy want many sad
 11  ~out and that* on-judge-year in_turn you sad many
 12  joy ~out and that* on-judge-year here_ends this holy_gospel

## 072r — after the crucifixion, they sit at meat in Jerusalem

> Here begins this holy gospel, written by holy Mark, within | the other twenty-fifth chapter of his writing. At that time, then, after the crucifixion of Lord Christ […] at that time then the apostles sat at table in Jerusalem, in the Lord's house, where the Lord Lord Jesus made the supper; at that time he appeared, the Lord Jesus, to his apostles, within, by name, somebody; and. he sat with the apostles at table and began to rebuke their unbelief

  1  begins this
  2  holy-gospel write
  3  holy_Mark inside | the_rest^
  4  ten-ten five chapter
  5  of-write time
  6  then on-execute
  7  Lord-Christ [?]-~year time then
  8  sit apostle at_table inside Jerusalem inside Lord house where Lord_God
  9  Lord-Jesus dinner do time appear | Lord
 10  Jesus apostle of-Lord inside ~brother-+name somebody and.
 11  sit to-apostle at_table and begin-admonish on-believe

## 072v — go ye into all the world, he that believeth and is baptized

> and Lord Jesus said, go ye, apostles, among the people, and is baptized in the Lord's name; and somebody who is baptized in the name of the Father and the Son and the Holy Spirit, and believes in the Lord, every such man shall be saved; and one is damned [but] [but] and somebody [is] not baptized, and is [for] the Lord and one be saved but every man is damned [but] [but]; and the man who believes in the Lord shall do many miracles, all in the Lord's name; the man in the Lord's […] […] name: the blind through light; the dead, somebody resurrects, rise.

  1  and say Lord-Jesus you go teach^ among_the_people* and
  2  exist baptize inside of-Lord name and somebody
  3  exist baptize inside name God_the_Father and son
  4  and holy-spirit and exist Lord-to believe
  5  everybody = be_saved and one be_damned [but]
  6  [-but] and somebody not baptize and exist Lord-to
  7  believe and one be_saved but everybody =
  8  be_damned [but] [-but] and somebody exist Lord-to believe
  9  from exist many miracle do every inside of-Lord
 10  name exist somebody inside of-Lord | and-exist
 11  [?]-+name ~blind through light die somebody resurrect rise^

## 073r — and these signs shall follow them that believe

> the man in the Lord's name, the evil in the man casts out; he carries serpents in the hand, is somebody not bitten; is somebody in the Lord's name deadly poison drink and whatever who, somebody, is well; is somebody within the Lord's name, on the cup […] year, our hands put this, sat, is somebody healed, all in the Lord's name; the man does many miracles, and The Lord Jesus said: I go to the Lord's Father, to you the Lord, and the Lord God the Lord goes, and I go to you, the Lord the Holy Spirit; and the apostles are new, new tongues.

  1  exist somebody inside of-Lord name evil inside
  2  somebody exorcise exist serpent carry inside
  3  hand ~exist somebody not bite exist somebody inside
  4  of-Lord name poison drink and what-to
  5  who somebody ~exist well exist somebody inside of-Lord
  6  name on-cup-[?]-~year our hands put
  7  this-°sat-+SUBJ exist somebody heal every inside of-Lord | and-exist-from
  8  ~year-+name exist somebody many miracle do and
  9  say Lord-Jesus I go to-of-Lord the_Father to-you
 10  Lord and Lord_God SUBJ Lord go and I you go-Lord
 11  holy-spirit and exist apostle new new language

## 073v — he went on the way, and each time he said the same

> say and Lord Jesus said to his apostles, go, apostles today the mount; I want, the Lord, out truly, and all the world, the Lord's | from God the Father; and passing, the Lord went from the apostles; in turn the apostles to the Lord went, the apostles and then, from seeing, the Lord [said to the] learners, and said, the Lord: peace [be] you and then passing, the Lord went [on] the way; and a second time, from seeing, the Lord [said to the] learners and said, the Lord: peace [be] you; and then passing, the Lord went | on the way; in turn the apostles to the Lord, on Monday, the apostles; and a third time, from seeing, the Lord [said to the] learners and said, the Lord: peace [be] you; and then passing, the Lord went the way; and a fourth time, from seeing, the Lord [said to the] learners, and said, the Lord: peace | you […] and then the Lord passed on the way; and a fifth time seeing, the Lord [said to the] learners, and said, the Lord: I [give] you peace; the eye

  1  say and say Lord-Jesus apostle of-Lord go-apostle today*
  2  mount I want-Lord ~out righteous and all_the_world of-Lord | from
  3  God_the_Father and trespass go-Lord from apostle in_turn apostle to Lord go apostle
  4  and then from-see-Lord learn and say-Lord peace you
  5  and then trespass go-Lord ~way and two from-see-Lord learn
  6  and say-Lord peace you and then trespass go-Lord | on
  7  ~way in_turn apostle to Lord Monday-apostle and three from-see-Lord learn
  8  and say-Lord peace you and then trespass go-Lord
  9  ~way and two-two from-see-Lord learn and say-Lord peace | ~you
 10  yours and then trespass go-Lord ~way and five | from
 11  see-Lord learn and say-Lord I you peace eye

## 074r — he was received up into glory

> to the Lord's sufferer, and the Lord's Father, for ever and ever. amen; because Lord Jesus would have him confess before the Father of the Lord, in the year of judgment; then the Father goes to judge the living and the dead, the man; and the Lord said to the apostles, ye shall hear; his mother, and Mary blessed upon all the apostles, and among this earth [after] to the Lord Jesus; and [taken up] the Lord Jesus | remained sun went sky and blessed all the whole wide world and the Lord was taken to heaven's glory. At that time said | Saint Peter: Master, how has he apostles pray, say

  1  to-sufferer of-Lord and of-Lord the_Father for_ever_and_ever =
  2  amen because want Lord-Jesus to-Lord confess have
  3  before the_Father of-Lord on-judge-year then
  4  go God_the_Father judge living and die somebody and say-Lord apostle
  5  you exist hear of-Lord mother and
  6  Mary bless on-every apostle and among this earth
  7  [after] to Lord-Jesus and [taken_up] Lord-Jesus | remain*
  8  sun go sky and bless the_whole wide world
  9  and Lord take^ to-heaven glory* time say | saint^
 10  Peter Master how? he have apostle pray say

## 074v — the Lord's Prayer

> the Lord Jesus, this the Lord's son: pray, God the Father, ours and the Lord in heaven, hallowed [be] the name of God the Father; the man goes into the Father's kingdom; the whole wide world is the Lord's, as in heaven this, and on earth, our bread every day the Lord takes, man, today's day [for] us; trespass forgive, as the man forgives our debtors. lead us into temptation; redeem from evil. Amen. Written by holy Matthew in his gospel. And the second time said holy Peter: Master, Lord, when shall be pass the year of judgment? Lord Jesus Christ said or out and out

  1  Lord-Jesus this of-Lord son pray God_the_Father our
  2  and-Lord inside heaven be_hallowed^ name of-God_the_Father go man^
  3  inside kingdom^ of-God_the_Father exist all_the_world of-Lord how? heaven
  4  this and ~earth bread our every day^
  5  grab-Lord man^ today’s day^ us trespass
  6  forgive^ as man^ forgive^ our debtors
  7  lead us into temptation redeem from evil amen
  8  write holy-Matthew inside of gospel and two say
  9  holy-Peter Master Lord when? exist pass
 10  judge-year say Lord-Jesus-Christ or out-out

## 075r — two men in white apparel

> in turn not fulfilled, two thousand years. And the third said holy Peter: Master, how shall the apostles good news write of the Lord? Lord Jesus said, one year write, apostles, literally; in turn the second, figuratively. And then the gate of heaven before the Lord Jesus; and then the Lord Jesus went into heaven's glory; and the Lord bright from left, because the Lord Jesus would like; then the Lord the apostles glorified, shining on this world; and then the two appeared, two angels, white […] believe. And then the two angels, angel [and] angel: you men of Galilee, how see ye the Lord's joy? Jairus

  1  in_turn not_fulfilled two-to-?thousand-year and three say holy-Peter
  2  Master how? apostle gospel Lord write say Lord-Jesus one
  3  year write apostle literal in_turn two metaphoric and then
  4  heaven gate before Lord-Jesus and then
  5  go Lord-Jesus heaven glory* and Lord bright from
  6  ~leave because would_like^ Lord-Jesus then Lord
  7  apostle be_glorified shine on-this world and then-two
  8  appear two angel-angel white | clothes
  9  believe* and_said two angel-angel you
 10  Galilee man how? Lord joy see Jairus

## 075v — he shall so come, to judge the quick and the dead

> left from heaven, land, this joy. the Lord would like to go on doomsday, to judge the living and the dead. the man. And the two said, these two angels, go, apostles, into Galilee; and the Lord met the apostle somebody. And [gazing] they saw; the word was done by the two angels. Here ends this holy gospel. Love the Lord with all thy heart. The Lord spoke, the apostles, Lord Jesus Christ; then the apostles prayed, his son, this Our Father

  1  ~leave from_heaven* land this joy
  2  would_like^ Lord go on_doomsday judge living and die
  3  man^ and say-two this two angel-angel go-apostle within^
  4  Galilee and Lord meet apostle-somebody.
  5  and [gazing] see word do two | angel
  6  angel here_ends this holy_gospel the_Lord love Lord_God be_loved
  7  speak-Lord apostle Lord-Jesus-Christ
  8  then apostle pray
  9  of-Lord son
 10  this Our_Father

## 076r — how oft shall my brother sin against me

> [afterward] to the apostles many said say written [holy Paul] apostolic letter in the first chapter of his writing. At that time, then, the Lord Jesus Christ at thirty years and three, and five months, and three [days], at time, the apostles left, under the Lord Jesus; and then holy Peter: Master, the high will this Peter forgive [how often]? is Peter [then]. And then the Lord Jesus Christ: Peter, Peter, | in turn who one […] dry, one year, commits sin, somebody against this Peter; forgive, the man, if the man goes to mercy, asks mercy, the man receives sun goes […] the man of mercy; and cried to Lord Jesus Christ

  1  [afterward] to-apostle many say say write [holy_Paul] apostolic_letter
  2  inside one chapter of-write time then Lord-Jesus-Christ
  3  inside thirty year and three and five moon and three inside
  4  time leave apostle under Lord-Jesus and_said holy-Peter
  5  Master want-high this-Peter forgive^ [how_often] exist Peter
  6  [then] and_said Lord-Jesus-Christ Peter Peter | in_turn
  7  who one-[?] dry* one year commit sin somebody
  8  against this-Peter forgive^ somebody SUBJ if go somebody-have_mercy
  9  ask-have_mercy-somebody SUBJ grab sun* go
 10  understand-+say somebody-have_mercy and shout-to Lord-Jesus-Christ

## 076v — the catalogue of sins

> stopped on the water of heaven [high] Peter, Peter, if, but rather a man among the apostles sins against you witness from […] the man, the apostle, the sin […] […] the man, of somebody's sin, leave [it]; but if many [are] somebody's sins, in turn a thief; in turn a robber; in turn a blood murderer; that is, a killer of men; the man in turn [adulterer]; the man in turn from [thief] the man in turn proud; the man in turn a drinker; the man in turn many [proud]; the man in turn under many yokes; this Peter said Lord Jesus Christ, because Peter is [pride] in turn in humble the man, this be damned how then the man dies in turn

  1  stop on-water heaven [high] Peter Peter if-°but_rather
  2  SUBJ somebody among apostle you sin witness* from
  3  heathen* somebody apostle sin witness* publican* somebody | of
  4  somebody-~sin leave but if many somebody-~sin in_turn
  5  thief in_turn robber in_turn blood murderer that_is
  6  people-die somebody in_turn [adulterer] somebody in_turn from [thief]
  7  somebody in_turn proud somebody in_turn drink somebody in_turn many
  8  [proud] somebody in_turn many yoke-chapter somebody this-on-Peter
  9  say Lord-Jesus-Christ because exist Peter [pride] in_turn inside humble
 10  somebody this be_damned* how? then somebody die in_turn

## 077r — one sin, and whosoever sins is damned

> Adam the man penance have mercy; the man in turn from riches [forgiven] the man in turn penance truly; the man, or the man judges of whom holy Paul speaks apostolic letter said Lord Jesus Christ, this [forgive] the man sins one sin penance he is saved; and he who hides the man [seventy times seven] heavenly in sin, to Lord Jesus Christ one sin, penance, saved; but every sinner is damned. said Lord Jesus Christ: Peter, Peter [if he hear thee not] that is [church] a sinner, not an apostle, this sinner, from a heathen witness publican, the man, of […] leaves [as the heathen] the man [with one] voice [two or three]; who is the man, says the man, this

  1  Adam man^ penance* have_mercy man^ in_turn from-rich-from [forgiven]
  2  man^ in_turn penance* true^ man^ or ~judge man^
  3  who speak holy-Paul apostolic_letter say Lord-Jesus-Christ this [forgive]
  4  man^ sin one sin penance* be_saved and who-hide
  5  man^ [seventy_times_seven] heavenly* on-sin to Lord-Jesus-Christ
  6  one sin penance* be_saved but every sinner be_damned
  7  say Lord-Jesus-Christ Peter Peter [if_he_hear_thee_not] that_is [church]
  8  sinner not apostle-this-sinner from heathen* witness*
  9  publican* man^ of-[?] leave [as_the_heathen]
 10  man^ [with_one] voice [two_or_three] who-exist man^ say man^ this

## 077v — go to him alone, then take two, then three

> he loves Lord Jesus Christ more than these. Lord Jesus Christ said to Peter: in turn [rebuke] the apostle-man among [alone]; the man who sins, go to Peter, […] the sin, to the house; and the man upon his sin rebuke, because this somebody's sin, sufferer; in turn, to which, us, sufferer, not a disciple, this sinner, from a heathen publican. from seeing the sinner, leave [him]; but Peter goes, to Peter, two […] sin; and somebody on sin rebuke, because this sinner, sufferer; in turn, to which, us, sufferer, not a disciple, this sinner from a heathen publican, the man; of the sinner leave [him]; but Peter goes, to Peter, a third time […] the sin, and the man

  1  SUBJ love Lord-Jesus-Christ more_than_these* say Lord-Jesus-Christ to-Peter
  2  in_turn [rebuke] apostle-somebody among [alone] somebody-~sin go | to
  3  Peter [?]-~sin to-home and somebody-on-~sin
  4  rebuke^ because this somebody-~sin sufferer in_turn to-which us
  5  sufferer not disciple^ this sinner from heathen* publican*
  6  from-see of-sinner leave but go-Peter to-Peter two
  7  [?]-~sin and somebody-on-~sin rebuke^ because this sinner
  8  sufferer in_turn to-which us sufferer not disciple^ this sinner
  9  from heathen* publican* man^ of-sinner leave but
 10  go Peter to-Peter three [?]-~sin and man^

## 078r — judge righteous judgment

> on sin admonish, because this sinner, sufferer; in turn, to which, us, sufferer, take the sinner; take from [appearance] within the hands; because this is right, right, to the sinner; because the false judge, according to [the law], judges somebody; the righteous judge but rather every [by appearance] false judgment; in turn the false judge the righteous man falsely judged is damned; in hell for ever and ever; in turn the righteous judge, every to whom he judges truly according to the judge falsely judging, but rather every [one] to which, righteous judge; the Lord God speaks every writing and every prophet and every church father and every forefather and evangelist

  1  on-sin admonish because this sinner sufferer in_turn to-which us
  2  sufferer grab sinner take* from [appearance] inside
  3  hands because this exist righteous righteous to-sinner because
  4  false ~judge-somebody according_to* chapter-judge-somebody righteous judge
  5  °but_rather-every [by_appearance] false judge in_turn false ~judge-somebody
  6  righteous man^ false judge be_damned SUBJ inside hell
  7  SUBJ for_ever_and_ever = in_turn righteous ~judge-somebody every
  8  to-which-chapter righteous judge according_to* judge-somebody false
  9  judge °but_rather-every to-which-chapter righteous judge Lord_God speak every write
 10  and every prophet and every church_father and every forefather and evangelist*

## 079r — the orders of angels, and one word

> within all the world, to heaven's glory, highest, every angel, angel, angel, order [answered] eat literally, from the one Lord, truly somebody speaks holy Paul the apostolic letter, the brother of Paul: he, the righteous judge, the Lord Jesus Christ he is judging all the world; one word [idle], word, every somebody [give account] our righteousness, good, mercy, saying, love, doing; and the Lord God takes; he, the righteous judge, and the Lord God every man receives [mercy] from the Lord [reward] the man the firstborn is damned, to the brother [bosom], on Lazarus [rest] damned [torment] [everlasting] [fire] and nine [orders of angels]

  1  inside every world to-heaven glory* highest every angel angel angel order
  2  [answered] eat literal from one Lord righteous somebody* speak holy-Paul
  3  apostolic_letter brother of-Paul he righteous ~judge-+somebody Lord-Jesus-Christ
  4  he exist judge every world one word [idle] word every
  5  somebody [give_account] our righteous-good-have_mercy-say-love-do and
  6  grab Lord_God SUBJ he righteous ~judge-+somebody and Lord_God every
  7  somebody exist grab [mercy] exist from Lord_God [reward] somebody
  8  firstborn exist be_damned to-~brother [bosom] on-~Lazarus [rest]
  9  be_damned [torment] [everlasting] [fire] and nine [orders_of_angels]

## 080r — the Comforter, and the threefold reproof

> Before the gospel: written by holy John, in the sixteenth chapter of his writing. Already said the Lord Jesus [to] the Lord's disciples at the Last Supper: I goes to his Father. You know that the heavenly land; that is, I leave, to die; the Lord dies, and I go [from] you [to send] the Holy Spirit. | In turn, who, I; if [I] do not die, to you the Holy Spirit does not go away. The Lord dies, and I go [from] you [to send] the Holy Spirit. and you shall see two judgments: the first, of sin; the second, of righteousness; the third, judgment. And then you receive this Holy Spirit; from the Spirit, through him, he takes you.

  1  before gospel write holy-John inside ten-six chapter of-write
  2  already^ say Lord-Jesus teach^ of-Lord at_the_Last_Supper = I
  3  go-Lord of-Lord God_the_Father you learn do
  4  heavenly land that_is I leave* on-die Lord
  5  die and I you go holy-spirit | in_turn
  6  who I does_not die to you go_not_away holy-spirit
  7  Lord-die and I you go holy-spirit
  8  and you exist see-two judge first from sin
  9  second from righteous third judge and then you
 10  go this holy-spirit from-spirit through grab you

## 080v — the apostles wait in prayer with Mary

> humble every good; and the disciples are new, new tongues say [truly] ye shall have many miracles, says the mouth in the Old Testament word, and it lives; go before [continuing], baptize [until] doomsday. Here ends this apostle's holy gospel. Begins this holy gospel, written by holy Luke, in the second chapter of his writing. At that time, then, on the putting to death of the Lord Christ, forty years; and | then the Lord was forty years; at that time the disciples stood [in] prayer in the divine one's house, where the Lord God, the Lord Jesus, did the dinner; out ten years; and then this went on ten years; at that time the apostles remained in prayer; and holy Peter left, to the Virgin Mary. And then

  1  humble every good and exist disciple^ new new language say
  2  [truly] you exist many miracle say which-mouth-chapter-year
  3  inside Old_Testament word and living-exist go before [continuing] ~baptize
  4  [until] doomsday end this SUBJ apostle holy-gospel begins
  5  this holy-gospel write holy-Luke inside two chapter of-write time
  6  then on-execute Lord-~Christ forty_years and | then
  7  Lord-exist forty_years time stand^ disciple^ prayer^
  8  inside divine_one^ house where Lord_God Lord-Jesus dinner do on-~out
  9  ten-year and then go_on this ten-year time stand^ disciple^ on
 10  prayer^ and leave holy-Peter to Virgin_Mary and_said

## 081r — the Spirit comes upon them

> holy Peter, the wife, to the apostles: Master, speak to the apostles; the Lord is from the sky goes the Holy Spirit; and Peter […] year, this is. And then the Virgin Mary: then God the Father from the sky the Holy Spirit goes; father Abraham, and Abraham the spirit goes on the eleven, forty years, to the spirit and the apostles, Mary, find, go on this; said, said the Lord Jesus, God the Father of the Lord: I from the sky go, the Lord's brother, the Holy Spirit and the Lord's mother. And then God the Father: how, in what form would he like to go if he goes into God, the Son, the Spirit; the Lord, Father, Son, Holy Spirit not suffer this world on the cross crucified. And then God the Father, | holy

  1  holy-Peter wife apostle-to Master speak to apostle exist-Lord
  2  from sky go holy-spirit and Peter [?]-~year this
  3  exist and_said Virgin_Mary then God_the_Father from sky
  4  go holy-spirit father Abraham and Abraham
  5  spirit go on-ten-+one-forty_years to spirit
  6  and apostle-Mary find go on-this say say Lord-Jesus God_the_Father of-Lord
  7  I from sky go of-Lord brother holy-spirit
  8  and of-Lord mother and_said God_the_Father how? form would_like^ go
  9  if go inside God-son-spirit-Lord father son holy-spirit
 10  not_suffer this world on_the_cross crucify^ and_said God_the_Father | holy

## 081v — cloven tongues like as of fire

> the Spirit gave, on the spirit, the form of fire and the Spirit went out from the apostles, Mary, the Jews, and the man this Spirit [filled] the apostles, the Jews; and it gave, on the spirit, the Spirit, the form of holy fire, and the Spirit went out from the apostles, Mary, the Jews; and the man, the Spirit [filled] the apostles, Mary, the Jews, many; drink, year [cloven tongues] many a wind, in that form dove in fire in that form; and the Jews saw this fire, that form, and it bowed on this house where the apostles and Mary at prayer. And then the Jews [said], the Jews, the head, that is,

  1  spirit give^ on-spirit fire form
  2  and go spirit from somebody-apostle-Mary-Jew and somebody
  3  this spirit [filled] apostle-Jew and give^ on-spirit
  4  spirit holy-fire form and go-spirit
  5  from somebody-apostle-Mary-Jew and somebody spirit [filled]
  6  somebody-apostle-Mary-Jew many drink-~year [cloven_tongues]
  7  many sough inside form dove inside fire
  8  inside form and see Jew this fire.
  9  form and bow on-this house where apostle-Mary
 10  on-pray and_said-Jews Jew ~head that_is

## 082r — the Jews see it, and three thousand are added

> the Lord, heretic; the apostles, every sough, and go to the Jews saw it, because, by name, the Jews [under heaven], every sough; and | then the Jews were […] in the house where the apostles and Mary were at prayer to the sky, from the apostles and Mary at prayer; ascension the heavenly word; thanks, apostles and Mary, to the Lord; thanks, Lord God; and various tongues say. And then the Jews [were] blind to [it]. these apostles; the sons of Jerusalem see how [they] tongues say. And then the apostles are apostles, Master, from sky the Holy Spirit goes [amazed] the apostles, one who [gave] food, went from the people; the Jews, three thousand the people received belief in Lord Jesus Christ, and every

  1  Lord heretic apostle every sough and go_to Jew
  2  on-see because ~exist-+name Jew [under_heaven] every sough and | then
  3  exist Jew go_to inside house where apostle-Mary | on
  4  prayer^ to sky from apostle-Mary on-pray ascension^
  5  heavenly word thanks apostle-Mary to-Lord thanks Lord God and
  6  various language say and_said Jew ~blind-to.
  7  this-apostle Jerusalem son see how? language say and_said apostle
  8  SUBJ exist apostle Master from sky go holy-spirit [amazed]
  9  apostle one-who food go from ~people Jew three_thousand
 10  ~people grab believe Lord-Jesus-Christ and every

## 082v — three thousand added, and the Trinity begins

> man, Jew, apostle, Mary, received the Holy Spirit; and two years, baptized, from the Jews [received], and [baptized], baptized, three thousand, and one […] son, seven sons; and from the son received holy the soul proceeds on the spirit, the Holy Spirit, every | man, Jew, son […] received the Holy Spirit and believed in the Lord Jesus Christ proceeds, on believing, somebody wants, one can, heaven land. Here ends this holy gospel, this Holy Spirit. [proceedeth] from the Father, out and out, the Spirit proceeds; in turn the Son, this Son, from, to God the Father sits; see, as this | remained sun the Sun; this sun has three good things; first

  1  somebody-Jew-apostle-Mary grab holy-spirit and two-year ~baptize from
  2  Jew [received] and [baptized] ~baptize three_thousand and
  3  one-[?]-[?] ~son seven ~son and from ~son grab | holy
  4  soul^ proceed* on-spirit holy-spirit every | somebody-Jew
  5  ~son-[?] grab holy-spirit and believe | Lord
  6  Jesus-Christ proceed* on-believe somebody want one-can heaven
  7  ~land here_ends this holy_gospel this holy-spirit.
  8  [proceedeth] on-father out-out go_out-spirit in_turn son
  9  this-son from to-God_the_Father sit see as this | remain*
 10  sun Sun this sun SUBJ three good first

## 083v — the sun, its light and its warmth

> good [first], who [is] light; second, good, warmth; third, good from the Sun; the sun's light signifies the Son of God; in turn the warmth symbolizes the Holy Spirit; in turn from the Sun, it symbolizes the Father; on him, from the Sun goes out the light, goes out the warmth, goes out the Son from the Father, goes out the Holy Spirit from the Father; as the sun, one form; this one God; if is, this can have, how can heaven and earth quake, and in his [dwell] prepare heaven, town, from, in turn, and the earth

  1  SUBJ good [first] who light second SUBJ good warmth third SUBJ good
  2  from-Sun sun Sun light symbolize son God in_turn warmth
  3  symbolize holy-spirit in_turn from-Sun symbolize the_Father on-he from-Sun
  4  on-go_out light on-go_out warmth on-go_out son on-the_Father
  5  on-go_out holy-spirit on-the_Father as sun
  6  one form | this
  7  SUBJ one God if
  8  SUBJ this can have how?
  9  can heaven earth
 10  quake and inside of-Lord [dwell] prepare
 11  heaven town-from-in_turn and earth

## 084r — Augustine and the child on the seashore

> At that time, then, on the crucifying of the Lord Jesus Christ, in the sixtieth year, at that time holy Augustine went to the shore of the sea, because he would understand, if that three, Lord, Lord, Lord, Father, Son, Spirit, are one God; and this is one morning, evening, noon, Sunday, on going out; and then he found one little child on the shore; this [by the] sea sat the little son of the Lord God [on the sand]; and | of the son of the Lord God [digging] one pit, son, and | of the child carried in his hand one spoon, and this [at the] sea, this spoon into this pit, scooped the son of the Lord God, this son

  1  time then
  2  on-crucify Lord-Jesus
  3  Christ six-ten-year time
  4  go holy-Augustine shore
  5  sea because want
  6  understand ~if
  7  three Lord-Lord-Lord father
  8  son spirit one God and this exist one
  9  morning evening noon Sunday on-go_out and then
 10  find one little son-Lord_God on-shore this
 11  ~sea sit son-Lord_God little [on_the_sand] and | of
 12  son-Lord_God [digging] one pit son* and | of
 13  son-Lord_God hand one spoon carry-son-Lord_God and this
 14  ~sea this spoon inside this pit scoop-son-Lord_God this son

## 084v — thou shalt sooner empty the sea

> And then holy Augustine: this little son of the Lord God, what does this child want? Said the child, this: [at the] sea, into this pit I scoop. Said holy Augustine: | this child, can this child do it? What child, this, [at the] sea, into this pit the child scoops said this […] child; first this child, can the son of the Lord God does [it], rather than this Augustine, on leaving the chapter, this and the child [cannot] see the word, did, before holy Augustine; and [he] can many this [understand] on writing [the Trinity], but believe truly, Christian, one God, | of the man, heaven and earth, that is, he has carries the commandment of God, [does not commit] sin; somebody is saved. somebody answered: many mortal sufferings, for ever and ever, amen; speaks holy James, the apostolic letter, brother of

  1  and_said holy-Augustine this little son-Lord_God
  2  who this want-son-Lord_God say want-son-Lord_God this.
  3  ~sea inside this pit scoop say holy-Augustine | this
  4  son-Lord_God this can-son-Lord_God do who | this
  5  son-Lord_God this ~sea inside this pit scoop-son-Lord_God
  6  say this little son-Lord_God first this-son this | can
  7  son-Lord_God do than this-Augustine on-chapter-leave-this
  8  and son-Lord_God [cannot] see word ~do before
  9  holy-Augustine and can many this [understand] on-write [the_Trinity]
 10  than believe righteous Christian one God | of
 11  somebody-+SUBJ heaven land that_is have
 12  carry commandment God [not_commit] sin somebody be_saved
 13  somebody answered* many mortal_suffering for_ever_and_ever =
 14  amen speak holy_James apostolic_letter brother of

## 085r — one commandment broken is all of them broken

> and among you, through transgressing one commandment of God; to the commandment, all; somebody [in one point] takes before face thanks to the Lord, because if a man one transgresses; how then all commandments transgresses somebody? | because it is the Lord's; he received it from his angel, in the Old Testament word, father Abraham […] ten and one commandment [guilty of all] this, more than these, go and be saved among men; the Lord of the Jews, Jesus, apostle to the gentiles, most high serpent the Son of the living God Lord Jesus Christ; and to the man from face and to the man the soul upon the cross […] and for the man his blood was shed, and the man the Lord redeemed from hell fire; [stay] somebody, many; stay the ten commandments; believe truly, Christian, one God

  1  and among you through transgress one
  2  commandment God to-commandment all^ somebody-+SUBJ [in_one_point] grab before
  3  face to-Lord thanks Lord_God because and somebody one
  4  transgress how? then all^ commandment ~transgress somebody | because
  5  SUBJ exist Lord_God grab on-angel of-Lord inside Old_Testament
  6  word father Abraham seventy and one-[?] commandment
  7  [guilty_of_all] this more_than_these* go be_saved among somebody divine_one^
  8  Jew Jesus apostle-pagan above-high serpent son living God
  9  Lord-Jesus-Christ and to-somebody from face and to-somebody soul
 10  ~on-+cross-[?] and to-somebody SUBJ of blood shed and somebody SUBJ
 11  redeem-Lord from hell fire [stay] somebody many stay
 12  ten-commandment believe righteous Christian one God

## 085v — Elijah calls down fire

> our heaven [and] land, that is, has carries the commandment of God, [does not commit] sin; somebody is saved. somebody answered: many mortal sufferings, for ever and ever, amen. Speaks holy Augustine: many believe; somebody within God's body, that God can within the body. to, from, face, bread in the place somebody takes within our mouth. Speaks holy Elijah the prophet, writes. Holy prophet, holy Moses; there was [called down] fire on all the world, to heaven on high, because all the world was destroyed; knelt one holy Elijah the prophet. At that time, then, the Lord destroyed the earth; there was fire in one place, and flame | from piercing [give account], girl, Lord God, within water; on this the destroying was three

  1  our SUBJ heaven land that_is have
  2  carry commandment God [not_commit] sin somebody be_saved
  3  somebody answered* many mortal_suffering for_ever_and_ever =
  4  amen speak holy-Augustine many believe somebody inside
  5  God body that God can inside body.
  6  to-from face bread on-place grab somebody
  7  inside our mouth speak holy-Elijah prophet write.
  8  holy-NAME.prophet holy-Moses exist [called_down] fire on-every world
  9  to-heaven high because-exist every world destroy kneel one
 10  holy-Elijah prophet time then Lord_God destroy-Lord
 11  earth exist fire inside one place and flame* | from
 12  pierce [give_account] girl Lord_God inside water on-this destroy exist three

## 086r — the torch lit from heaven

> forty and six years; at that time holy Elijah knelt and prayed; thanks to the Lord; and fire God opened, the angel of heaven; and from [but rather] fire [from heaven] one [torch] [became] said the angel of God: Elijah, this signifies the Lord, the Lord of angels. And then holy Elijah took a torch, and the torch light; in turn this [figure], flame, went to Elijah from | four four peoples; and every one from the people, the torch gave light; in turn holy Elijah [chariot] little and in Elijah, until stay. And then holy Elijah, then | two, two, two, two ten years. This is written by holy Moses in the Old Testament word.

  1  forty and six-year time kneel holy-Elijah
  2  and pray to-Lord thanks Lord_God to fire
  3  open God angel heaven and from [but_rather]
  4  fire [from_heaven] one [torch] [became] say
  5  God angel Elijah this exist symbolize Lord_God Lord | of
  6  angel and then grab holy-Elijah torch ~and torch
  7  light in_turn this [figure] flame* go to-Elijah from | two-two
  8  two-two ~people and every from-~people torch light in_turn
  9  holy-Elijah [chariot] little and inside Elijah from-until
 10  stay and_said holy-Elijah then | two-two-two-two
 11  ten-~year this_is write holy-Moses inside Old_Testament word

## 086v — the torch signifies the Virgin

> symbolizes [figure]: the gospel is, the angel [of] the Father, within the body the blessed Virgin Mary, one son, the Lord God [figure] symbolizes somebody, body; the gospel is, takes | on the Lord Jesus Christ; symbolizes the torch, the body, the blessed | Virgin Mary; then Mary conceived the Lord God, and Jesus saved all the whole world; and Christ, woman, ours; and the Lord, head […] son heaven and earth [together] symbolizes the body of the Lord Jesus Christ [unconsumed] the fire symbolizes the Lord God, and every one can | God the Father the Lord Jesus Christ, angel, Holy Spirit, Mary, apostle, one [God] God [made]; and this [unconsumed] is, stays, on the putting to death [of] the Lord Jesus Christ, at thirty, within the Host, on all the whole world

  1  symbolize [figure] gospel exist angel the_father inside body
  2  blessed Virgin_Mary son one Lord_God [figure] symbolize
  3  somebody body gospel exist grab | on-Lord
  4  Jesus-Christ symbolize torch body blessed | virgin
  5  Mary then-Mary conceive Lord_God and Jesus be_saved every all_the_world
  6  world and Christ ~woman our and Lord ~head-[?]-~son
  7  heaven and earth [together] symbolize body Lord-Jesus
  8  Christ [unconsumed] symbolize fire Lord_God and can every | father-God
  9  Lord-Jesus-Christ-angel-holy-spirit-Mary-apostle one [God]
 10  God [made] and this [unconsumed] exist stay on-execute
 11  Lord-Jesus-Christ on-thirty inside the_host = on-every all_the_world world

## 087r — the torch and the light

> and somebody is [who] eats this bread, the man, the son of God man every man shall be saved; and one somebody not damned; Elijah symbolizes the body, the blessed Virgin Mary; how from Mary the torch [gave] light, when [he] was born our Creator Lord; and [he] can, on the cross, to one somebody die; but all the world dies; this one, one somebody, can, God, everything; within our mouth takes, because the Lord God has the Lord God [in] the body, rather than [the sun], God many [the sun] and […] and from [the light] [the warmth] the earth [the sun] and heaven on high, and God is this can; then the Lord would have heaven and earth quake

  1  and somebody exist this bread eat man* son
  2  God man* everybody = be_saved and one
  3  somebody not_damned Elijah symbolize body blessed
  4  Virgin_Mary how? from-Mary torch light then-~be_born
  5  Creator_Lord our and can on_the_cross to-one
  6  somebody die but every world die this-+one one somebody
  7  can God every inside our mouth grab because Lord_God
  8  ~have-Lord_God body than [the_sun] God-+SUBJ
  9  many [the_sun] and high-Lord and from [the_light] [the_warmth]
 10  earth [the_sun] and heaven high and God-+SUBJ
 11  this can then want-Lord heaven earth quake

## 087v — the poor man of God

> before, the gospel written by holy Matthew [eighteen] of his writing, who [is] not somebody, an apostle, this from this little the son to done, in Jesus' and the body, one man is saved, one […] in heaven; in turn the year is not so; but every man is damned, judged, the man, by Christ. | Holy Matthew speaks [thus] this man says, this little the son, this little the man trespasses, the poor man of God, and the poor man of God, the man, and [riches] have the man in turn, this

  1  ~before gospel write
  2  holy-Matthew [eighteen]
  3  of-write who_not
  4  somebody-apostle this from this
  5  little son to*
  6  ~do inside of-Jesus
  7  and-~body one
  8  somebody be_saved one man* inside heaven | in_turn-chapter
  9  ~year-exist ~but everybody = be_damned judge somebody Christ | holy
 10  Matthew speak [thus] this somebody say this little
 11  son this little somebody trespass poor_man_of_God = and
 12  poor_man_of_God = somebody and [riches] have somebody in_turn this

## 088r — the rich man, and the soul in purgatory

> the man is rich, he has wealth, he sees, blind he goes […] or sits, and blind asks of this man alms, in Jesus and the body [alms] the blind does not take; somebody is damned; somebody is, ever ever riches, but somebody judged, damned; somebody on the blind; in turn damned, somebody is damned; somebody is, ever ever [remember], saved; somebody is damned; somebody is conceived somebody within hell buried; [there] it writes; somebody within hell until the death of ours and the body; in turn | on death, the soul within purification fire until doomsday; in turn | on doomsday, both soul and body within hell for ever and ever.

  1  somebody rich have-somebody wealth see blind
  2  go name-somebody or sit and ~blind exist ask from this
  3  somebody alms inside Jesus and-~body [alms]
  4  blind not_take somebody be_damned exist somebody ever
  5  ever riches* ~but-somebody judge be_damned somebody
  6  on-blind in_turn be_damned somebody be_damned exist somebody ever
  7  ever [remember] be_saved somebody be_damned exist somebody conceive
  8  somebody inside hell bury [there] write somebody
  9  inside hell until to-die our and-~body in_turn | on
 10  die soul inside purification fire until doomsday in_turn | on
 11  doomsday and soul and body inside hell for_ever_and_ever =

## 088v — there was a certain rich man, clothed in purple

> Here begins this holy gospel written by holy Luke in the sixth chapter of his writing. At that time Lord Jesus said to his apostles, and the Jewish people, there was a rich [man] one rich man, and the rich man, every […] and purple the rich man wore, and the rich [man] from day to day caroused; and then thus [he] went one Lazarus to the rich man's house; and Lazarus was all over head until toe covered wounds, Lazarus; at that time this rich man to table sat the rich man, husband [fared sumptuously], king, Lord [in purple] various husbands; and then the rich [man] was [there]; this poor man asked

  1  here_begins this holy_gospel
  2  write holy-Luke inside
  3  six chapter of-write
  4  time say Lord-Jesus
  5  apostle of-Lord and Jew
  6  people exist-rich
  7  one rich-somebody
  8  and somebody-rich every [linen] and purple go-somebody-rich | and
  9  rich from day until day carouse and then thus go
 10  one ~Lazarus to-house this-rich and ~Lazarus exist every from
 11  head until toe covered* wound ~Lazarus time this rich
 12  to table sit-rich man^ husband^ [fared_sumptuously] king-Lord [in_purple]
 13  various husband^ and then rich exist this poor_man ask

## 089r — the dogs licked his sores, and angels carried him

> alms; and the poor man the alms did not take; the rich [man] [desired] but the poor man he chased out; and then this [one] lay, the poor man, out at the rich man's gate, alone, because the poor man was [full of sores] was [laid]; and then the poor man wanted [what] passed from the crumbs; the dogs on the rich man's table [fell from]; the poor man did not take; and then | have the rich man had many dogs, and the dogs came, this Lazarus and the dogs licked Lazarus […] and Lazarus more was of the dogs have mercy, this Lazarus; in turn from the rich man mercy; believe, Lazarus; lame; have mercy; and then this Lazarus died; the angels went, heaven's glory, the most high, the Father, God the Highest; this Lazarus, and Lazarus the angels took, and carried Lazarus into the bosom of Abraham. the forefather. And then this rich man saw this miracle, of this Lazarus

  1  alms and poor_man alms not_take rich [desired]
  2  but poor_man out chase and then lie this
  3  poor_man out gate to-of-rich exist-+one because exist poor_man [full_of_sores]
  4  exist [laid] and then want poor_man trespass from crumbs the_dogs*
  5  on-of-rich table^ [fell_from] poor_man not_take and then | have
  6  rich many dog and go-dog this Lazarus ~and
  7  lick-dog of-Lazarus ~wound and Lazarus more
  8  exist from dog have have_mercy this Lazarus in_turn from-rich
  9  have_mercy believe-Lazarus lame have_mercy and then this Lazarus
 10  die go angel heaven glory* most_high the_father God the_Highest* this Lazarus and Lazarus
 11  grab-angel and Lazarus carry inside bosom Abraham
 12  forefather and then see this miracle this rich from this Lazarus

## 089v — in hell he lifted up his eyes

> who Lazarus did, the angels, the Father, heaven; and then this the rich man died, and this rich man [also] was buried within hell; and then he suffered within hell, this rich man; he saw, the rich man's trespass, and saw Lazarus within the bosom of father Abraham; and this rich man shouted: father Abraham, said the father, Lazarus; because this, let the poor man | of Lazarus, a little finger dip in water, and cool it on the rich man's tongue [cool] flame the soul of the rich man; and from [remember], the body of the rich man. And then father Abraham: | this rich man, son of God the Father, this rich man [had] good [things] [in thy lifetime], as Lazarus was [evil things]; [now] the world; in turn this rich man is rich blind [lifted up his eyes] this rich man, Lazarus took the crumbs that fell the dogs […] the rich man's table; the rich man took [fell from]; the rich man; Lazarus did not take.

  1  who do Lazarus angel father heaven and then this
  2  rich die and this-~rich [also] inside hell bury and then
  3  suffer inside hell this ~rich see ~trespass-~rich and see Lazarus
  4  inside bosom father Abraham and shout this rich
  5  father Abraham say-father Lazarus because-this let poor_man | of
  6  Lazarus little finger immerge water and cool
  7  on-of-rich tongue [cool] flame* soul of-rich and from
  8  [remember] body of-rich and_said father Abraham | this
  9  ~rich son of-God_the_Father this-~rich good [in_thy_lifetime] as
 10  Lazarus exist [evil_things] [now] world in_turn this-~rich exist
 11  rich ~blind [lifted_up_his_eyes] this-~rich grab-Lazarus trespass from crumbs
 12  the_dogs* [?]-~rich table ~rich grab [fell_from] ~rich Lazarus not_take

## 090r — a great gulf fixed, and they have Moses and the prophets

> said father Abraham: take Lazarus, [send] up [to] the world. And then father Abraham: a great chasm between the rich man […] or [pass over] this is the netherworld, highest, hell on hell; who shouts, this […] father Abraham; and Lazarus [may come] within the bosom of father Abraham; and a second time this rich man cried, father Abraham, go, Lazarus, [great gulf], up [to] the world; the rich man has trespass; these four, of the rich man brethren, because the brethren […] of the rich man, how in this rich man's suffering because these brethren, the man sins, from [repent] then is damned the man, as the rich man, this rich man is damned. Said father Abraham, they have brothers; trespass; this prophet, and preach, in order that this prophet preach hear, somebody, brother, be damned; and a third [time] who shouts, this

  1  say father Abraham grab-Lazarus [send] up world and_said
  2  father Abraham great^ chasm among-~rich-[?] or [pass_over]
  3  this_is netherworld highest hell on-hell who-shout this-[?]
  4  father Abraham and Lazarus [may_come] inside bosom father
  5  Abraham and two who-shout this-~rich our_father Abraham
  6  go Lazarus [great_gulf] up world have-~rich trespass this-two-two of-rich
  7  ~brother because ~brother say-Lazarus from-~rich how? inside this-rich suffer
  8  because this ~brother somebody sin from [repent] then be_damned
  9  somebody how?-rich this-rich be_damned say our_father Abraham have
 10  brother trespass this prophet and preach in_order_that this prophet preach
 11  hear somebody brother be_damned* and three who-shout this

## 090v — neither will they be persuaded, though one rose from the dead

> the rich man; our father Abraham, name vanished from; the prophet preaches, believe [fell from] [neither] good; somebody, Lazarus; believe, brother and the body from the dead stood up, somebody, woman. Said our father Abraham: if not the friend, the prophet, let the brethren believe, and the preaching and good from somebody baptized […] not; the brother believes; and the body rose from the dead, the man Lazarus […] this holy day. Here ends this holy gospel. Here begins this holy gospel, written by holy John, in the second chapter of his writing. At that time Nicodemus came by night to Lord Jesus, because he feared the Jews; and not want to the Lord he came

  1  rich our_father Abraham name-°vanished-from prophet preach believe [fell_from]
  2  [neither] good somebody-Lazarus believe-brother
  3  and body from die stand_up-somebody-woman say our_father Abraham if not
  4  friend^ prophet believe-brother-somebody and preach
  5  and good from somebody-baptize-[?] not brother believe and body
  6  from die stand_up-somebody-Lazarus [?]-this-holy-~year here_ends this holy_gospel
  7  here_begins this holy_gospel write
  8  holy-John inside second^ chapter | of
  9  write time go Nicodemus
 10  inside night to-Lord-Jesus
 11  because ~have Jew and
 12  not_want to-Lord go-this

## 091r — except a man be born again

> but in the night to the Lord went Nicodemus. And then Nicodemus: O, Nicodemus's Master, this Nicodemus: he, Nicodemus believes, that he [is] the true Son of the living God, because he goes to heaven. land, and the Lord, he [is] the true Son of the living God. And then the Lord Jesus: Nicodemus, verily verily I [say to] you, speak: and the man is not to the Lord believing, born again a second [time], is born into this world, that one man is saved; but every man is damned. Said Nicodemus: Master, how can this be, who to two before a second time from his mother goes, Nicodemus, and a second time is born into this world? this, thanks. Said the Lord Jesus: Nicodemus, I speak this, donkey, to

  1  but inside night to-Lord go-Nicodemus and_said Nicodemus oh.
  2  of-Nicodemus Master this-Nicodemus he believe-Nicodemus.
  3  that he true^ son living God because he go on-heaven.
  4  ~land and-Lord he true^ son living God and_said.
  5  Lord-Jesus Nicodemus verily verily I you.
  6  speak and man^ not exist to-Lord believe born_again* second^
  7  be_born on-this world one man^ be_saved but every-somebody
  8  be_damned say Nicodemus Master how?-this can exist who to-two-before
  9  second^ from of mother go-Nicodemus and second^ be_born-Nicodemus on-this world.
 10  this thanks say Lord-Jesus Nicodemus speak* I this-donkey-to

## 091v — born of water and of the Spirit, and God so loved the world

> this, that this Nicodemus again is born from Nicodemus's mother; but I speak: then a second [time] born, somebody, Nicodemus, from water and of the Holy Spirit, that one man Nicodemus is saved; but every man Nicodemus is damned. Said Lord Jesus, Nicodemus, in turn then I [have] begun to you, the Lord, to preach from heaven and earth, how you from […] left, Nicodemus the man; then can this world, Nicodemus, the man enter leave, who, I, to you the Lord preached, said | the Lord Jesus, Nicodemus: so did you love the Father, his God of heaven but the Father's only begotten Son, Jesus, that is, to the Lord, so did you love the Father, said Lord Jesus; and [water] and the man, the Lord

  1  this that this-Nicodemus again be_born from of-Nicodemus mother but
  2  I speak then second^ be_born-somebody-Nicodemus from water and
  3  from holy-spirit one somebody-Nicodemus be_saved but
  4  every-somebody-Nicodemus be_damned say Lord-Jesus Nicodemus in_turn | then
  5  exist I you begin-Lord preach from-heaven
  6  kingdom^ how? you from enter* | leave-Nicodemus
  7  man^ then this world can Nicodemus-somebody enter*
  8  leave who I you preach-Lord say | Lord
  9  Jesus Nicodemus [?]-+one you love father of-Lord God heaven
 10  but of-God_the_Father only son Jesus that_is to-Lord [?]-+one
 11  you love God_the_Father say Lord-Jesus and [water] and man^ Lord

## 092r — that whosoever believeth should not perish

> believes in the Son of the Father, the only begotten, Lord Jesus Christ, and one man Nicodemus is saved; but every man Nicodemus is damned. Said Lord Jesus, Nicodemus [answered] to the Lord goes the Father, his God of heaven; I love this world, [not to] judge [it], but rather to the Lord goes God the Father; who, I saved this world by his death; and man is, to the Lord believes, this man Nicodemus, and his Father believes more than these; this one, one God. Said Lord Jesus [only begotten] one […] among you [that believeth] from darkness; and [believeth in him] [already] [condemned] not; and said Lord Jesus, and the man Nicodemus who does evil among you

  1  believe son of-God_the_Father only Lord-Jesus-Christ and one
  2  somebody-Nicodemus be_saved but every-somebody-Nicodemus be_damned say
  3  Lord-Jesus Nicodemus [answered] to-Lord go father of-Lord God heaven
  4  love I this world judge but_rather* to-Lord go God_the_Father who I
  5  this world be_saved on-of-Lord die and man* exist to-Lord
  6  believe this somebody-Nicodemus exist and of-Lord God_the_Father
  7  believe more_than_these* this one one God say Lord-Jesus [only_begotten]
  8  one ~exist-[?] among you [that_believeth] from
  9  darkness and [believeth_in_him] [already] [condemned] not and say
 10  Lord-Jesus and SUBJ do_evil-somebody-Nicodemus among you

## 092v — men loved darkness rather than light

> from the man Nicodemus who will not come to the light, but loves the darkness, somebody, Nicodemus; said the Lord Jesus: and practises righteousness from somebody, Nicodemus; the light [he] loves, and every [one] | goes to the light the man Nicodemus. Here ends this holy gospel. The Lord, with all thy heart, Lord. Here begins this holy gospel written by holy Luke in the fourteenth […] in his writing. At that time Lord Jesus said to his apostles and to the Jewish people: | then a rich lord made, one rich man, many dinner

  1  from somebody-Nicodemus not_want on-light go but darkness love
  2  somebody-Nicodemus say Lord-Jesus and SUBJ practise_righteousness from
  3  somebody-Nicodemus light love and every on-light | go
  4  somebody-Nicodemus here_ends this holy_gospel Lord_God be_loved Lord
  5  here_begins this holy_gospel
  6  write holy-Luke inside
  7  fourteen chapter inside | of
  8  write time
  9  say Lord-Jesus disciple^
 10  of-Lord and Jew
 11  people | then
 12  rich-Lord_God do one rich man^ many dinner

## 093r — a certain man made a great supper, and bade many

> And then the rich Lord God, among the rich Lord God['s], redeemer's year, three friends. upon this […] said this rich lord to his living servant, go […] speak this word, go, the man; at that time all is finished, say. This living servant, this […] man lo, the living servant. go, of the living Lord God, this man; then the Lord God, the man goes of the Lord God's dinner, said this first: I not. cannot, because [I have] bought a plough; | want the man go out, see; and want the plough [to prove them]. asked this servant to speak, the man, before […] the lord; and said this second, lo. The living servant goes, the lord's living servant, this man

  1  and then-rich-Lord_God among-rich-Lord_God redeemer-~year three friend.
  2  on-this dinner say this-rich-Lord_God of-Lord living-servant go-[?].
  3  this word speak-angel go-somebody time SUBJ every finished say.
  4  this-living-servant this ~one man* lo living-servant.
  5  go of-the_living-Lord_God this-?man then-Lord_God go-?man
  6  of-Lord_God dinner say this first I not.
  7  cannot because bought plough | want
  8  man* SUBJ go_out see and want plough [prove_them.]
  9  ask this-~servant to-speak man* before
 10  of-living-~servant Lord_God and say this two sense lo.
 11  living-servant go of-living-servant Lord_God this-somebody-sense

## 093v — I have bought five yoke of oxen

> then the Lord God; somebody goes […] of the Lord God's dinner; said this second somebody: us […] not the man cannot, because the man has bought five yoke of oxen ox the man must the man goes in the field the man must the ox, thanks; is, can, the ox | [try] [pray thee] [excused], asked this living servant to speak the man, before […] the lord said this third man, lo, the living servant goes, the lord's living servant the Lord God; this somebody, thief; then the Lord God, somebody goes, thief, of the Lord God's dinner; said this third, thief: us, thief,

  1  then-Lord_God go-somebody-sense of-Lord_God dinner say this
  2  two somebody-sense us-sense not
  3  can-somebody-sense because buy-somebody-sense
  4  five yoke sense ox want-somebody-sense
  5  go-somebody-sense in_the_field* want-somebody-sense
  6  SUBJ ox thanks exist can ox | [try]
  7  [pray_thee] [excused] ask this-living-~servant to-speak
  8  somebody-sense before of-living-~servant Lord_God say
  9  this three somebody-thief lo living-servant go of-living-servant
 10  Lord_God this-somebody-thief then-Lord_God go-somebody-thief
 11  of-Lord_God dinner say this three thief us-thief

## 094r — go out into the highways and hedges

> the man cannot, and the man must go because to go, somebody, thief, marry; us, thief, not can somebody, thief; and to go, somebody, thief, and these somebody, thief, [answered], said to speak; somebody, thief, before of […] the lord; and then, and one goes, the man the man on this dinner said this Lord God, that is, the people; and the people spoke of the Lord God's dinner and the lord said to the living servant, go out into the roadside and the way and into the town, and to the town gate, and. find […] within the spirit poor | to be, the chapter [lame], body hunger and thirst within the spirit, and […] first.

  1  not can-somebody-thief and to-go-somebody-thief
  2  because to-go-somebody-thief marry us-thief not
  3  can somebody-thief and to-go-somebody-thief and these
  4  somebody-thief [answered] say to-speak somebody-thief before
  5  of-[?] Lord_God and then and one | go-somebody
  6  man* on-this dinner say this
  7  Lord_God that_is people and people speak of-Lord_God dinner
  8  and say of-Lord_God living-servant go on-roadside and on-way
  9  and on-town and on-gate town and.
 10  ~find-[?] inside spirit poor | to-exist-chapter
 11  [lame] body hunger and thirst inside spirit and [?]-°first.

## 094v — blessed is he that shall eat bread in the kingdom of God

> man he found; every man went, the angel, into the lord's house said this living servant, the angel, Lord, it is done; and the mountain top, which the Lord said [the master] said this living servant, the angel servant one to the place, and to the place the living servant would go out and then there rose at the table one Jew, and shouted to: blessed from within the spirit poor, because the spirit of the poor, heaven's kingdom; and said | the Lord Jesus truly, speaking [to the] Jew, more than these, within the spirit heaven kingdom. And then this rich somebody, the Lord God, [supper] [bade many] many, to go, the mouth […] thief, on our rich Lord God's dinner. Here ends this holy gospel.

  1  man* find everybody = go-angel inside of-Lord_God house
  2  say this living-servant-angel Lord do and summit who-Lord
  3  say [the_master] say this living-servant-angel servant*
  4  one to-place and to-place want living-servant-angel on-out
  5  and then rise to-throne one Jew and
  6  shout-to blessed^ from inside spirit poor because
  7  spirit of_the_poor heaven kingdom^ and say | Lord
  8  Jesus righteous speak-Jew more_than_these* inside spirit heaven
  9  kingdom^ and_said this-rich somebody-Lord_God [supper] [bade_many]
 10  many to-go-mouth | man-[?]-somebody
 11  thief on-our-rich-Lord_God dinner here_ends this holy_gospel

## 095r — the bread blessed at the supper

> Here begins this holy gospel written by holy John in the sixth chapter of his writing. At that time Lord Jesus said to his apostles and the Jewish people: you are the Lord's body eat, and the Lord's blood drink. And then the Lord Jesus, the Lord's apostles, to the last dinner, this at the Last Supper; and the Lord Jesus took within [his] hands one baked cake, and Lord Jesus blessed this bread and bread before the Lord, Lord Jesus put it. And

  1  here_begins this holy_gospel
  2  write holy-John
  3  inside six chapter of-write
  4  time say Lord-Jesus
  5  apostle of-Lord and Jew
  6  people you
  7  exist of-Lord body
  8  eat and of-Lord blood
  9  drink and_said Lord-Jesus apostle of-Lord last dinner-to this
 10  at_the_Last_Supper = and grab Lord-Jesus inside hands one baked
 11  cake and blessed Lord-Jesus this bread.
 12  and bread before Lord place^ Lord-Jesus and.

## 095v — except ye eat my flesh and drink my blood

> the Lord Jesus gave wine, one cup, and water into the cup poured, and Lord Jesus blessed the wine and the water; and the wine [and] water before the Lord the Lord Jesus put. And then | the Lord Jesus: and the man who eats this bread, this man is the Lord's body eaten, and the man not who eats this bread and believes in the Lord every man is damned […] and the man who believes in the Lord and from the altar, from the thirty, the holy host eats and drink every man shall be living, for ever and ever, amen. And then the Jews: how is it, the Jews, the Lord's body eaten, and the Lord's

  1  give^ Lord-Jesus wine one cup and water inside cup
  2  pour and blessed Lord-Jesus wine and water and
  3  wine water before Lord put Lord-Jesus and_said | Lord
  4  Jesus and man^ exist this bread eat this man^
  5  exist of-Lord ~body ~eat and man^ not
  6  this bread eat and Lord believe
  7  everybody = be_damned cut_off-[?] and man^ exist Lord believe
  8  and from altar exist from thirty holy-host
  9  eat and drink everybody = exist
 10  living for_ever_and_ever = amen and_said Jew
 11  how? exist-Jews of-Lord ~body eat and of-Lord

## 096r — whoso eateth my flesh hath eternal life

> blood drunk? This pleasing, who he speaks, because eaten the Jews, who […] […] and his body to eat and blood drunk, which [is] hidden, said this Lord Jesus, who is the Lord strive but said Lord Jesus, believe; then somebody believes in the Lord, to the Lord, this who [is] indeed the Son of the living God. And then the Lord Jesus: the Lord's body, this is indeed eaten, and the Lord's blood, this is indeed drunk. And then the Lord Jesus: then the man [who] eats this bread is a man, apostle, [eateth] on the Lord's suffering [everlasting life] is from eating, how the bread of […]

  1  blood drink this pleasing who he speak because eat^
  2  Jew who-[?] strive* and of-Lord body eat
  3  and blood drink which-hide say this Lord-Jesus who-Lord-exist
  4  strive* but say Lord-Jesus to-believe then
  5  believe-somebody inside Lord to-Lord this-who indeed^ son
  6  living God and_said Lord-Jesus of-Lord ~body this_is
  7  indeed^ eat and of-Lord blood this_is indeed^ drink
  8  and_said Lord-Jesus then man^ this bread eat
  9  exist man^ apostle [eateth] on-of-Lord suffering [everlasting_life]
 10  exist from eat how? bread of-[?]

## 096v — I am the living bread which came down from heaven

> your fathers did eat in field because that is the bread of life; he who goes, the Lord, bread; in turn the ascension from heaven | town from that day, upon this world; and the man who eats this bread from the man, living, for ever and ever, amen and I [am] this bread, because the Lord, I | go the Lord from the Lord's Father on this world; and I to the Lord's Father, the living Lord; and the man is [in] the Lord, believes; from the man living to the Lord, ever ever, the man; and the man who is within the Lord's keeping of the commandment of love stays; and I am

  1  you father eat inside field because that_is bread
  2  living he_who go-Lord ~bread in_turn ascension^ from_heaven* | town
  3  from-~year on-this world and man^ exist this bread eat
  4  from man^ exist living for_ever_and_ever = amen
  5  and I this bread because-Lord I | go
  6  Lord from of-Lord the_Father on-this world and I
  7  to-of-Lord the_father living-Lord and man^ exist Lord.
  8  believe from man^ exist to-Lord living ever
  9  ever man* and man^ exist
 10  inside Lord-keeping_the_commandment_of_love stay and I exist

## 097r — he that dwelleth in me, and I in him

> within somebody and the man who carries his commandment, from the man is within the Lord, from the Lord's keeping of the commandment of love stays; and I am within somebody. And then the Lord Jesus: [abideth in me] somebody; and somebody is within the Lord, God the Father, the Son, God, Jesus, the Holy Spirit, Mary, Christ, the apostles, the angels, keeping the commandment of love, stays; | wants the Lord, God the Father, the Son, God, Jesus, the Holy Spirit, Mary, Christ, the apostles, the angels to go; and somebody goes, the Lord, God the Father, the Son, God, Jesus, the Holy Spirit, Mary, Christ, the apostles, the angels, into the heavenly land. And then the Lord Jesus: and this somebody wants the Lord, God the Father, the Son, God, Jesus, the Holy Spirit, Mary, Christ, the apostles, the angels to take the house, at | the Lord's, God the Father's, the Son's, God's, Jesus', the Holy Spirit's,

  1  inside somebody and somebody exist of-Lord commandment carry from somebody
  2  exist inside Lord from Lord-keeping_the_commandment_of_love stay and I exist
  3  inside somebody and_said Lord-Jesus [abideth_in_me] somebody and somebody exist
  4  inside Lord-God_the_Father-son-God-Jesus-holy-spirit-Mary-Christ-apostle-angel
  5  keeping_the_commandment_of_love-stay | want-Lord-God_the_Father-son-God
  6  Jesus-holy-spirit-Mary-Christ-apostle-angel go and somebody
  7  go-Lord-God_the_Father-son-God-Jesus-holy-spirit-Mary-Christ-apostle-angel
  8  inside heavenly land and_said Lord-Jesus and this somebody
  9  want-Lord-God_the_Father-son-God-Jesus-holy-spirit-Mary-Christ-apostle-angel
 10  house grab at | of-Lord-God_the_Father-son-God-Jesus-holy-spirit

## 097v — the whole company of heaven, and the host

> Mary's, Christ's, the apostles', the angels'; the Father God there, through staying, somebody, for ever and ever, amen. And then the Lord Jesus: and the man who from the altar, from the thirty, the holy host eats [shall not die]; from somebody, the living, ever ever, amen. Here ends this holy gospel. The Lord, be loved. Here begins this holy gospel written by holy Luke, in the […] chapter of his writing. Then the Lord Jesus, within the thirtieth day and in the first year; at that time he left

  1  Mary-Christ-apostle-angel the_father-God there through stay
  2  somebody for_ever_and_ever = amen and_said Lord-Jesus and
  3  somebody exist from altar from thirty holy-host
  4  eat [shall_not_die] from somebody exist the_living ever
  5  ever amen here_ends this holy_gospel Lord-+be_loved
  6  here_begins this holy_gospel
  7  write holy-Luke inside
  8  and chapter of-write
  9  then Lord-Jesus inside
 10  thirty day and inside one
 11  year time leave

## 098r — the light of the body is the eye

> the Lord Jesus [preached] among the high priest, and the Lord's apostles And then the Lord Jesus, the Lord's apostles and the Jews, the people: [the lamp of the body] have mercy […] the eye [single] [lightsome] | of the apostles the Jews, somebody, the eye. And then the Lord Jesus: the eye | of […] the man, this is the lamp of […] and the lamp of the apostles the Jews, somebody: this is the body of […], and in turn is within the body of […]; remained, one heart, sin protruding, is all the body of […] darkness. And then the Lord Jesus: if [take heed], the heart alone sins against the Lord's Father, God, from the heart; wants the Father

  1  Lord-Jesus [preached] among high_priest = and of-Lord apostle
  2  and_said Lord-Jesus apostle of-Lord and Jew ~people [the_lamp_of_the_body]
  3  have_mercy-+SUBJ of-[?] eye [single] [lightsome] | of-apostle
  4  Jews-somebody eye and_said Lord-Jesus eye | of-[?]
  5  man^ this_is lamp of-[?] and lamp | of-apostle
  6  Jews-somebody this_is body of-[?] and
  7  in_turn exist inside of-[?] body remain* one
  8  heart sin protrude exist all^ of-[?] body
  9  darkness and_said Lord-Jesus if [take_heed] heart-°alone
 10  sin against of-Lord the_father God from heart want the_father

## 098v — a candle set on a candlestick

> the Lord's flogging, various, from the donkey. And then the Lord Jesus: if [it] is within the body of […], the whole heart is clean, all the body of […] bright. And then the Lord Jesus: how then […] the lamp gives light, to the light; the lamp, a hundred, is light of the body of […] Here ends this holy gospel. The Lord with all thy heart; the Lord have mercy; and truly speaks holy John: God can bear the sky and the earth; to this speaks holy John, the Lord God; and the man who bears the living man upon this world, and the healthy man

  1  of-Lord flog various from-donkey and_said Lord-Jesus if
  2  exist inside of-[?] body all^ heart clean exist
  3  all^ of-[?] body bright and_said Lord-Jesus
  4  how? then [?]-[?] lamp light to-+SUBJ
  5  light lamp hundred exist light of-[?] body
  6  here_ends this holy_gospel Lord_God be_loved Lord_God SUBJ have_mercy and righteous
  7  speak holy-John God
  8  can carry sky
  9  and earth to-this
 10  speak holy-John Lord
 11  God and man^ carry living
 12  man^ on-this world and healthy_man^

## 099r — he that dwelleth in love dwelleth in God

> the man receives, and God receives the man [abideth] the man, God. | To this the man has: the Lord God, Jesus Christ, the Son of God; and the Lord, the Lord's head, heaven and earth; and love our father's son as the man [his] neighbour. In turn [hath this world's goods] the rich man; the man has wealth, sees; trespass, the poor of God; and the man [seeth not] has God, the man loves the rich somebody as the man [his] neighbour; is | of somebody rich, one, the heavenly land, speaks holy Matthew; and the man [a liar] says: us, God, love; in turn | of the rich. man, his brother hateth, loves the rich somebody, from [a liar]

  1  man^ grab and God man^ grab [abideth] man^ God | to
  2  this have man^ Lord_God Jesus Christ son of-God
  3  and Lord ~head heaven and earth
  4  and love our father son as man^ neighbour
  5  in_turn [hath_this_world's_goods] ~rich man^ have man^ wealth see
  6  trespass poor_man_of_God = and man^ [seeth_not] have God man^
  7  SUBJ love-rich-somebody as man^ neighbour exist | of
  8  somebody-rich-+one heaven land speak holy-~Matthew and
  9  man^ [a_liar] say us God love in_turn | of-rich.
 10  man^ father son hateth love-rich-somebody from [a_liar]

## 099v — if a man say, I love God, and hateth his brother, he is a liar

> the man, in turn, our father's son sees; somebody hateth the man, father, son, as the rich somebody, the rich neighbour, God land; hell [cannot] see the rich somebody | saved the rich somebody is, for ever and ever, amen. If the rich somebody is, the Lord, the apostles, love everybody as the rich somebody he is a liar; how does this man love God, in turn, of his brother hateth loves God [his brother] the Most High, this he sees. the man, in turn, our father's son sees; somebody hateth the son hateth the man loves; how does this man love God, this godfearing; in turn the rich somebody wants to love God; first love | of the rich the man, father, son, as the rich somebody, the rich neighbour, God and good; the rich somebody is loved […] heaven land; hell [cannot] see the rich somebody | saved the rich somebody is, for ever and ever, amen. If the rich somebody is, the Lord, the apostles, love everybody as the rich somebody

  1  first^ liar exist how? this man^ God love in_turn | of
  2  man^ father son hateth love God [his_brother] high-this see.
  3  man^ in_turn our father son see somebody hateth
  4  son hateth love-somebody how? this-somebody God love this
  5  godfearing^ in_turn want-rich-somebody God love first love | of-rich
  6  man^ father son as rich-somebody rich-+neighbour God
  7  and good exist somebody-~rich love [?]-[?] heaven
  8  land hell [cannot] see-rich-somebody | be_saved
  9  rich-somebody exist for_ever_and_ever = amen.
 10  if-exist rich-somebody Lord apostle love everybody = as rich-somebody

## 100r — Elijah taken up by fire, and the list of miracles

> the neighbour is of the rich somebody; heaven [inheriteth] the rich somebody, from [taken up] the Lord, from the Father and the Son and the Holy Spirit. Elijah the prophet was taken, by fire, into heaven. Various miracles: did; the blind sight, through light [saw]; the dead were raised up; the lame [walked]; the body, and the possessed of the evil one, were healed. Elijah? Who? and this, and this miracle did Elijah do; writes the church father, the church father, [the] pagan. First writes the church father, [the] pagan; the church father [concerning] Elijah.

  1  neighbour exist of-rich-somebody heaven = [inheriteth]
  2  rich somebody from [taken_up] Lord from God_the_Father and son and holy-spirit
  3  Elijah prophet take^
  4  fire on-+heaven
  5  various miracle
  6  ~do blind sight^
  7  SUBJ through light die SUBJ
  8  raised_up* lame
  9  body and evil^ possessed SUBJ heal Elijah | who-and-this
 10  and-this miracle do Elijah write church_father church_father pagan
 11  first write church_father pagan church_father [concerning] Elijah

## 100v — the fathers on the sepulchre, a chronology, and the temple of forty-six years

> the tomb, to heaven; on earth; after these writes [in three days] the pagan church father; after these writes: high, hide, and from the scholar. the pagan church father; after these writes the pagan scholar, the Pharisees. And the church father writes this three; and Saint Augustine the church father: Elijah the Lord God, the Creator Lord, first; than the Creator Lord, the sun and the moon, and there is living Elijah; to Elijah, two; then, from Adam; the Creator Lord fifty; and on this somebody [and six] seven people. At that time was this somebody five hundred and thirty. In the thirtieth year, then: "destroy", the Lord; five towns; and then on this: "destroy", forty and six years.

  1  tomb to-+heaven on-earth after_these write [in_three_days]
  2  pagan church_father after_these write high-hide-and-from scholar.
  3  pagan church_father after_these write scholar pagan Pharisees*
  4  and church_father this three write and Saint_Augustine_the_church_father Elijah
  5  Lord_God Creator_Lord first than Creator_Lord sun and moon
  6  and exist living Elijah to Elijah two then from
  7  Adam Creator_Lord fifty and on-this somebody [and_six] seven
  8  people time exist this somebody five_hundred and
  9  thirty thirty-~year time destroy Lord_God five
 10  town and then on-this destroy forty and six-year

## 101r — Elijah's fire, and Enoch and Elijah kept for Antichrist

> Then holy Elijah knelt down and prayed to the Lord God; to fire; and took; the angel of God said, the angel of God, to Elijah: this is the angel of the Lord; and this man from […] And Elijah, somebody, from leaving, [wished to die] [juniper]; and Elijah, the man, was taken up into heaven […] and […]. Elijah, the man [man] from the year; Noah and Elijah shall bear the sword; hell, one gate open; and [Enoch] left; Noah, Elijah on the earth. [Antichrist] [of a harlot] shall be born; two; the chief devil, and the son, Satan; and there is […] evil, who is Antichrist.

  1  time kneel holy-+Elijah and pray Lord_God | to
  2  fire and grab God angel say God angel Elijah
  3  this exist-of-angel Lord_God and this somebody from-exist
  4  and Elijah-somebody from-leave [wished_to_die] [juniper] and
  5  Elijah-somebody be_caught_up heaven highest and gate/open | Elijah
  6  somebody [man] from-~year Noah Elijah sword carry
  7  hell one-+gate/open and [Enoch] leave Noah Elijah on-earth
  8  [Antichrist] [of_a_harlot] through be_born two chief_devil =
  9  and son Satan and exist-[?] evil^ exist Antichrist

## 101v — the opening of a reading from Luke: Simeon

> Before the Word, says holy Luke: glory to the Lord, the Lord God, glory be; of the Lord, holy mercy, Lord; this Lord, the gate, Lord; of the Lord, many homes. Before, many holy fathers before, many, writes church father the church father: heaven; the Lord's Son […] the Lord taken; to see one […] because many holy fathers wanted to see the Lord Jesus Christ [consolation of Israel] The Lord's chapter: many; how shall we see? In turn, Simeon; one, Simeon.

  1  before Word^ speak
  2  holy-Luke to-Lord glory^
  3  Lord God glory^ exist
  4  of-Lord holy-have_mercy Lord
  5  this Lord gate Lord
  6  of-Lord many home
  7  before many holy-father-before many write church_father church_father
  8  heaven Lord son SUBJ grab-Lord see one [?]-°sat
  9  because because many holy-father want see Lord-Jesus-Christ [consolation_of_Israel]
 10  Lord-chapter many how_shall_we* see but Simeon one-Simeon

## 102r — Simeon's arms, and the thirtieth year

> and the body; it is Simeon; for Simeon carried him in his bosom: the Lord Jesus Christ [took him]. The Lord saw the apostles and the Jews, the people, and these apostles, the Jews, the Lord; all saw within the body, somebody. At that time then the Lord Jesus [was] within his thirtieth year. At that time from the woman, the Lord Jesus; and the Lord went from town to town, from temple to temple, from town until town; and the Lord's apostles went, the Lord, into the world; the gospel the Lord preached; various miracles the Lord did: | the blind the blind the Lord, through light, the Lord; the dead the Lord raised; the lame

  1  and ~body exist Simeon because from Simeon carry bosom
  2  Lord-Jesus-Christ [took_him] Lord see apostle and Jew people and
  3  this apostle Jew Lord every see inside ~body somebody
  4  time then Lord-Jesus inside thirty year time
  5  from-woman-woman Lord-Jesus and go-Lord from town
  6  until town from temple until temple from
  7  town until town and of-Lord apostle go-Lord into_the_world* gospel
  8  preach-Lord various miracle ~do-Lord | ~blind
  9  ~blind SUBJ-Lord through light-Lord die raise-Lord lame

## 102v — the Passion in short: the sun darkened, the rocks rent

> the body, and the possessed of the evil one, the Lord healed. And the Lord suffered for man's sin, the good of the whole world; the cross […]; and for man the Lord's shed blood; and somebody the Lord redeemed from hell fire. And then the Lord, on the cross […] | the sun […] and the moon, this darkened, before the sun darkened; and before the moon darkened, the face of the earth quaked; the rock, the stone rent; and at the sun's darkening every tree in the world, this humbled itself, and all creation mourned. Then Christ, the cross […]; and the Lord was put in the sepulchre.

  1  body and evil^ possessed heal-Lord and suffer SUBJ Lord to
  2  somebody-sin good all_the_world on_the_cross-[?] and to-somebody
  3  SUBJ of-Lord shed_blood and somebody redeem-Lord from hell
  4  fire and then-Lord on_the_cross-[?] | sun*
  5  Lord-+name and moon this eclipse before sun eclipse
  6  and before moon eclipse ~earth quake rock
  7  stone rent and on-sun eclipse all^
  8  tree on-+world this humble and all^ create mourn
  9  then Christ on_the_cross-[?] ~and Lord inside tomb | put

## 103r — the three days: where was the soul?

> the Jews; and then the Lord lay within the tomb, the Lord; and the hour, at that time, went the Father, God of heaven; from the Father, the angel; the soul within was before the Lord Jesus, and rose from prayer. In turn the angel stayed in the tomb; in turn, the Lord went to hell, and destroyed hell, and redeemed man; hell fire, because | he carried, the Lord, his cross on his shoulder; and man's soul […] of the Lord, God the Father, all the whole world. And then the Lord Jesus | from the Father, the Lord God of heaven; the soul […] of this God the Father, this soul

  1  Jews and then-Lord inside tomb lay-Lord and hour time
  2  go the_father God heaven on-of-father angel soul inside
  3  ~exist-~before Lord-Jesus and rise* from pray
  4  in_turn angel inside tomb stayed in_turn to-Lord go-Lord on-hell
  5  and hell destroy and somebody redeem-Lord fire hell because | carry
  6  Lord of-Lord cross on-of-Lord shoulder and somebody soul-[?]
  7  of-Lord God_the_Father every all_the_world world and_said Lord-Jesus | from
  8  father of-Lord God heaven soul-[?] this-God_the_Father this soul

## 103v — the lost sheep, a doxology, and the names in one sign

> of the Lord's sheep: I [the] soul, the Lord redeemed; the wolf; the earth this God the Father's soul; the sheep [gather] the Lord took; this God the Father's soul redeem heavenly, until for ever and ever. amen. From every ghost, and from [fared sumptuously] the Lord, from the heavenly, on this the world believe, woman, woman; and [sent] the Lord [his] angel. | On […]-[…]-Mary-Jesus-God-Christ-angel-sheep speaks Saint […], the church father. Holy Anne, this Anne, gave birth: [for ever] [and ever] [for ever] to mercy, the commandment; go, on everyone, the whole world.

  1  of-Lord sheep I soul redeem-Lord wolf ~earth
  2  this-God_the_Father soul sheep [gather] grab-Lord this-God_the_Father soul
  3  redeem heavenly until for_ever_and_ever =
  4  amen from every ghost and from [fared_sumptuously] Lord from heavenly* on-this
  5  world believe woman woman and [sent] Lord [his] angel | on
  6  [?]-[?]-Mary-Jesus-God-Christ-angel-sheep
  7  speak Saint_[a_church_father] church_father | holy
  8  Anne this Anne be_born
  9  [for_ever] [and] [for_ever] SUBJ
 10  to-have_mercy commandment go on-every all_the_world

## 104r — a creed, from Anne's daughter to the judgment

> the world, that is: then from Anne was born the blessed | Virgin Mary; from Mary was born the Lord Jesus Christ; and the Lord went into the world, preached the gospel, various miracles did; the Lord suffered for man's sin, for the whole world; the Lord was crucified, and for man the Lord shed his blood, and the Lord redeemed man from hell fire; and somebody, the Lord, is believed that [he is] truly the Son of the living God: everybody is saved; and one man shall be damned; and the Lord: he that believeth not, and [perish] one shall be saved; in turn, every man shall be damned.

  1  world that_is then from Anne be_born happy | virgin
  2  Mary from Mary ~be_born Lord-Jesus-Christ and from Lord go
  3  into_the_world* gospel preach various miracle ~do
  4  Lord and suffer to somebody sin all_the_world crucified Lord and
  5  to somebody SUBJ of-Lord shed_his_blood and somebody SUBJ redeem-Lord
  6  from hell fire and somebody Lord exist believe
  7  that righteous son living God everybody = be_saved and one
  8  somebody be_damned to and Lord not believe and [perish]
  9  one to be_saved ~but everybody = be_damned

## 104v — blessed are the eyes which see

> Begins this holy gospel, written by holy Luke, in the tenth chapter of his writing. Then said | the Lord Jesus to his apostles and the Jews, the people: blessed the two, from the eye, the two eyes; this the Lord sees, who you [those things which] | the apostles see. the Jews: because many holy fathers, many, writes the church father, many prophets, many kings, many emperors | would have liked, the fathers, church fathers, prophets, kings, emperors, to see this which you [blessed are] from […]; and there rose among these Jews one; another church father wanted

  1  here_begins this holy_gospel
  2  write holy-Luke inside
  3  ten chapter of-write
  4  time say | Lord
  5  Jesus disciple^ of-Lord
  6  and Jew people
  7  blessed two from
  8  eye to-two eye this Lord see who you [those_things_which] | see-apostle
  9  Jews because many holy-father many write church_father many prophet many
 10  king many emperor | would_like_to-father-church_father-prophet-king-emperor
 11  this see who you [blessed_are] from-[?] and
 12  rise among this Jew one another church_father want

## 105r — the lawyer's question, and the great commandment

> tempted the Lord Jesus. And then this Jew: Master, learning […] who, the Jews' church father, must do; how? this […] gain life for ever and ever. Said the Lord Jesus, this […]: [answered] to the Jews: pray, Jews, Moses writes, says this Jew, this church father: pray, church father, Moses writes within the sixth chapter. Said the Lord Jesus, [with] joy, I, this Jew: how readest thou Moses? Rightly. And then this Jew, this reading: Moses writes: love the Lord God highest [above] every creature, all our soul, all our might, all our heart; and | of somebody, brother, as somebody [his] neighbour, ours the heavenly land. And then the Lord Jesus, rightly, spoke.

  1  tempt Lord-Jesus and_said this Jew Master learn-[?]
  2  who Jews-church_father must do how? this-[?] gain
  3  living for_ever_and_ever = say Lord-Jesus this-[?]
  4  [answered] to-Jews pray Jews Moses write say this
  5  Jew this-church_father pray church_father Moses write inside
  6  six chapter say Lord-Jesus joy I this-Jew how?
  7  read Moses righteous and_said this Jew this read
  8  Moses write love Lord_God highest ~every create all^ our
  9  soul all^ our might all^ our heart and | of
 10  somebody brother as somebody neighbour our SUBJ
 11  heaven land and_said Lord-Jesus righteous speak

## 105v — who is my neighbour? A certain man went down to Jericho

> the Jew: for whoever believes in one God, to […] literally, love the man, our brother, as the man [his] neighbour; of […] heaven, land; and the man's mouth left; and then […] proud, this Jew. And then Master, who is of the Jews […]? said the Lord Jesus [answered] to the Jews: pray, who, Jews, Moses rightly and from was a living servant; committed sin; of somebody, Adam, the Lord God; and cast out; on the Lord's mercy; and then went somebody, Adam, into the field, to one place, forgive […] Jericho town; evening, from, to build; and then went the servant, Adam, into the field; and then met robbers.

  1  Jew because and man^ believe one God to-cut_off-literal
  2  love man^ our ~brother as man^ neighbour
  3  of-[?] heaven ~land and mouth man^
  4  leave and then-[?] proud this Jew and_said
  5  Master who? exist of-Jews [?]-~year-~exist-DIV say
  6  Lord-Jesus [answered] to-Jews pray who-Jews Moses righteous
  7  and from exist living-~servant commit sin of-somebody-~Adam
  8  Lord_God and exorcise on-of-Lord have_mercy and then
  9  go-somebody-~Adam on-~field to-one place °forgive-+SUBJ
 10  Jericho town evening-from-to build and then go
 11  ~servant ~Adam on-~field and then meet robber

## 106r — stripped, half dead; the priest and the Levite pass by

> And the robbers began, to the man; the holy(?) found; and then these robbers let the man go, having taken the booty; and the robbers beat the man, this man dying; and half dead and half alive. Thus went on one descendant of Abraham, who to [him] the man; on seeing, the descendant of Abraham passed the man by, and | went. The descendant of Abraham went on; the rest, half, a descendant of Moses, who to Adam […] the descendant of Moses passed the man by, and went [by chance] Adam could; the two, Abraham [and] Moses, good [they] did. passed the man by; through went the two of Abraham, that way.

  1  and begin robber to-~Adam ~rich ~find
  2  and then this robber remit ~Adam grab
  3  booty and ~Adam beat robber
  4  die-this ~Adam and half_dead and half_alive
  5  thus go ~on one descendant_of_Abraham who-to
  6  ~Adam on-see-descendant-Abraham long-~Adam and | go
  7  descendant_of_Abraham go ~on the_rest^ half descendant_of_Moses who-to ~Adam
  8  [?]-descendant_of_Moses long-~Adam and go [by_chance]
  9  ~Adam can-two-Abraham-Moses good ~do
 10  long-~Adam through go-two-Abraham thus

## 106v — the Samaritan binds his wounds and pays the host

> Went on one Samaritan, to Jerusalem, the Lord's living servant; and saw his face, found him, and had compassion on the man; did, for the Lord poured wine into the man's wound, and had mercy; one to the long Lord; in turn, the Lord's clothes bound up the man's wounds, and the man | he put, the Lord, on the Lord's shoulder; and Adam [he] took away to the Lord lodging; and the man this innkeeper took. And the innkeeper took two [pence], two denarii; And then this innkeeper, this innkeeper, on Adam take care; on this, that, whatever more on the man | […]

  1  go ~on one Samaritan on-Jerusalem of-Lord living-servant
  2  and face found and have_mercy to-~Adam
  3  ~do because pour-Lord wine of-~Adam
  4  wound and have_mercy one-to long-Lord in_turn of-Lord clothes
  5  bound_up of-~Adam wound and ~Adam | place^
  6  Lord on-of-Lord shoulder and ~Adam take_away to-Lord
  7  on-lodging and ~Adam grab this innkeeper
  8  and innkeeper grab two [pence] two denarius
  9  and_said this innkeeper this-innkeeper on-~Adam
 10  carry on-~exist-this who to-whatever on-~Adam | little

## 107r — which of these three was neighbour? Then Augustine begins

> the innkeeper: then [I] go; on doomsday all this, innkeeper, [I] give back. And then the Lord Jesus: I judge, this Jew, who this good friend among | the […] Abraham, one, Moses, the Samaritan? And then this Jew [say]: and this, the Jews spoke, as [neighbour] a good friend, and name […] had mercy to Adam, did. And then the Lord Jesus rightly spoke [to] the Jew. And then the Lord Jesus | this Jew brought; and he said: similarly do, Jews. is, of the Jews, the heavenly land. End [of] this holy gospel. Speaks holy Matthew: from the one denarius is signified

  1  innkeeper then go doomsday every this-innkeeper give_back
  2  and_said Lord-Jesus judge I this-Jew who?
  3  SUBJ this good friend among | [?]-Abraham-+one-Moses
  4  the_Samaritan and_said this Jew [say]
  5  and this-Jews speak-Jews as [neighbour] good friend
  6  and name-[?] have_mercy to-~Adam do and_said
  7  Lord-Jesus righteous SUBJ speak-Jew and_said Lord-Jesus | this
  8  Jew brought* and he_said* similarly do-Jews
  9  exist of-Jews heaven land end this
 10  holy-gospel speak holy-Matthew from one denarius symbolize

## 107v — the two pence, by Augustine; and the opening of the next reading

> Old Testament belief; the second denarius symbolizes on being born. and death of the Lord Christ, speaks Saint Augustine the church father, [two pence] [Testaments]. little [the Old] [the New] says God, but the body God swallow; on, from thirty [years] [preached], from the priest. Before the gospel, says | the Lord Jesus to his apostles and the Jewish people: because see | he is [so] good; do what is pleasing, and thanks to the Lord, the Lord God. Begins this holy gospel, written

  1  Old_Testament believe second denarius symbolize ~on-be_born
  2  and die Lord-Christ speak Saint_Augustine_the_church_father [two_pence] [Testaments.]
  3  little [the_Old] [the_New] say God but body
  4  God swallow on-from thirty [years] [preached] from priest
  5  before gospel say | Lord
  6  Jesus apostle of-Lord and
  7  Jew people
  8  because see | ~you-chapter
  9  [so] good
 10  do pleasing
 11  and thanks to-Lord Lord_God here_begins this holy_gospel write

## 108r — ye are the salt of the earth, and a city set on a hill

> written by holy Matthew, in the fifth chapter of his writing. Then said the Lord Jesus to his apostles and the Jewish people: ye are the salt of this world. In turn, if this salt lose its taste, it is good for nothing, out, the salt is thrown out, and the people trample on the salt, because this is high; you, good deed. And then the Lord Jesus: and a town on high, to the mount; and the town up the people see; and then [trodden down] the people, to the town. escape this; and you learn; you good deed; if [he] is high, from two, on the people learning and do; found among the people, a man, mercy.

  1  holy-Matthew inside five chapter of-write time say Lord-Jesus
  2  apostle of-Lord and Jew people you salt
  3  this world in_turn lose_savour this salt good-apostle-God out-out
  4  salt cast_out and salt people trample
  5  because this exist high you good_deed = and_said
  6  Lord-Jesus and SUBJ town on-high to_the_mount and town up
  7  people see and then-+SUBJ [trodden_down] people to-town.
  8  escape this and you learn you
  9  good_deed = if-exist high from-two people on-learn
 10  and do found among people man^ have_mercy

## 108v — the candle and the bushel, and the Father's house

> and love the Lord [candle]; somebody, and loves the Lord, the man; and believes in the Lord, and from the man receives; of you, of the Lord, in teaching [which] learns, the Lord; I take you, the Lord; and from the man goes into the Lord's God the Father's house | is joy ever ever, amen. In turn, then, out, the building, to cut off, the man is the town from […]. And then the Lord Jesus: then a man the lamp, light, a man, to this [before men], light, who [is] the lamp on a candlestick put; a man doth, a man, to the pit, year; but a lamp on a candlestick somebody puts, who releases the lamp; every people see who [is] within the house; and you

  1  and love-Lord [candle] somebody-and love-Lord man^ and believe inside-Lord and from
  2  man^ grab from you of-Lord on-learn [which]
  3  learn-Lord I you grab-Lord and from man^ go
  4  inside of-Lord God_the_Father house | exist joy ever
  5  ever amen in_turn then out building to-cut_off man^
  6  exist town from-[?] and_said Lord-Jesus then man^
  7  lamp light man^ to this [before_men] light who lamp
  8  on-candlestick put man^ do man^ to-pit-~year but
  9  lamp on-candlestick put-somebody who release^
 10  lamp every people see who inside house and you

## 109r — whosoever shall do and teach them

> the lamp of this world, that is: learn from the Lord Jesus and from the holy gospel. And then the Lord Jesus: great belief; there is a man [who] carries the people until doomsday; and one believes, two is leave; but believe: I remit you, the Lord. And then the Lord Jesus: and the man who is carrying, who, Moses abound; and from the man is this righteous teaching; in turn, and the man is carrying, who, Moses abound and from somebody is not this righteous learning. And then the Lord Jesus: and the man is carrying, who, Moses writes, our good did; he shall see heaven, pleasing. In turn, and

  1  lamp this world that_is learn from Lord-Jesus and from holy-gospel
  2  and_said Lord-Jesus great^ believe exist man^ carry people
  3  until doomsday and one believe two exist
  4  leave but believe* I you remit-Lord
  5  and_said Lord-Jesus and man^ exist carry who Moses
  6  abound* and from man^ exist this righteous teaching
  7  in_turn and man^ exist carry who Moses abound*
  8  and from somebody is_not this righteous on-learn and_said Lord-Jesus
  9  and man^ exist carry who Moses write our
 10  good ~do exist see heaven pleasing in_turn and

## 109v — the end of the Matthew reading, and a new one from Luke

> the man is not bringing, who, Moses abound | of the man, good did, does not show the pleasing things of the Lord, the Father. Here ends this holy gospel. The Lord God: love the Lord God. Begins this holy gospel, written by holy Luke, in the ninth chapter of his writing. Then went the Lord Jesus to Jerusalem; and then went the Lord Jesus, of the olives, the mount, highest, Jerusalem town; and the Son of God showed down [over] Jerusalem town; and cried out | the Lord Jesus. And then: Jerusalem, Jerusalem! Then this Jerusalem [Bethphage] and this Jerusalem

  1  man^ is_not bring^ who Moses abound* | of
  2  man^ good ~do is_not show^ pleasing of-Lord
  3  the_Father here_ends this holy_gospel Lord_God love Lord_God
  4  here_begins this holy_gospel
  5  write holy-Luke
  6  inside nine chapter of-write
  7  time go Lord-Jesus
  8  Jerusalem and then go
  9  Lord-Jesus of_the_olives mount highest Jerusalem town and
 10  show^ son God down Jerusalem town and cry_out | Lord
 11  Jesus and_said Jerusalem Jerusalem then this-Jerusalem [Bethphage] and this-Jerusalem

## 110r — if thou hadst known; the army that shall compass thee

> […] because there is much misery upon this Jerusalem. Why? this | what believe, who, this faith, the Jews, somebody, the apostles | of the Lord said; and who I preached, and this faith. And then the Lord Jesus: then I, the Son of God, crying over this Jerusalem, because there shall come upon this Jerusalem [trench], an army; | this this shall sit about Jerusalem, and this Jerusalem [thine enemies] compass round; [straiten thee] and thou art not, somebody, the angel, is somebody, the angel, out; and [stone], name, Jerusalem; but [visitation] among you captured, all the Jews, on the cross crucified, somebody, the angel, and the Jews are, by hunger(?) die; and there is much misery on this

  1  chapter-+new because exist many misery ~on-this Jerusalem why? this | what
  2  believe* who this faith* Jews-somebody apostle | of
  3  Lord say and who I preach and this faith*
  4  and_said Lord-Jesus then I son God crying
  5  this-Jerusalem because exist on-this-Jerusalem [trench] an_army | this
  6  this to-sit Jerusalem and this-Jerusalem [thine_enemies] surround
  7  [straiten_thee] and you is_not somebody angel exist
  8  somebody angel out and [stone] name-Jerusalem but [visitation] among you
  9  capture every-Jews on_the_cross crucify somebody angel and
 10  ~exist-Jews hunger? die and exist many misery ~on-this

## 110v — Jerusalem destroyed by Vespasian and Titus, and the temple cleansed

> Jerusalem; because this Jerusalem, all Jerusalem, destroyed the Roman general | Vespasi- -anus, and his son Titus; […] stone upon stone | shall not be left; [them that sold] faith. And the Lord Jesus went into the Jerusalem temple; and then the Lord found within them that sold, the sellers of doves; and the Lord Jesus made of small cords a scourge, and all the Jews [drove out], out. cast out, the Lord. And then the Lord Jesus: this is [the house of] prayer this house; make it pleasing to the Lord, of God the Father; in turn you, the house, did, the Jews. a den of thieves. And from thence the Lord Jesus, from until Palm Sunday, until many […]. The end of this | holy gospel.

  1  Jerusalem because this-Jerusalem every-Jerusalem destroyed the_Roman general | Vespasi-
  2  -anus son Titus that stone on-stone | shall_not_be
  3  left [them_that_sold] believe and go Lord-Jesus
  4  within^ Jerusalem temple and then Lord within^ found [them_that_sold]
  5  dove_seller and do Lord-Jesus of_cords
  6  cords scourge and every-Jews [drove_out] out
  7  cast_out Lord and_said Lord-Jesus this_is prayer^
  8  house this house SUBJ do on-pleasing of-Lord from
  9  God_the_Father in_turn you house do-Jews
 10  one thief house and from-exist Lord-Jesus from
 11  until Palm_Sunday until many Wednesday end this | holy
 12  gospel

## 111r — the five sorrows of the Son of God

> All the writings speak of five weepings of the Son of God. The first weeping of the Son of God: then the Lord God destroyed five towns; and not only the weeping of the Lord's eye, but rather highest sad. The second weeping, the writing speaks of the birth at Bethlehem town, because the Lord Jesus foresaw, as on Holy […] [how often] suffering | on the birth of the Lord. The third weeping, the writing speaks | on Palm Sunday: then he sat, saw on the town, Jerusalem; not only the weeping of the Lord Jesus for the house and for the building, literally, amid the town, but the weeping of the Lord Jesus for the Lord's creation, who the Lord created for the Lord, [wept], because the Lord Jesus foresaw then

  1  every write speak five weep son God first weep
  2  son God then destroy Lord_God five town
  3  and not_only weep Lord eye but_rather* highest sad two weep write
  4  speak on-~be_born Bethlehem town because
  5  foresee Lord-Jesus as on_Holy [how_often] suffering | on
  6  ~be_born Lord third weep write speak | on
  7  Palm_Sunday then sit see on-town
  8  Jerusalem not_only weep Lord-Jesus to-house and to-+building literal amid
  9  town but weep Lord-Jesus to-of-Lord create who
 10  create-Lord to-Lord [wept] because foresee Lord-Jesus then SUBJ

## 111v — Jerusalem falls, and a mother eats her son

> the Jews, the people, go, all scattered. And then, on the putting to death of the Lord, Christ: ten and ten, and four years; then took the Lord God power, the Roman general; and the general | and was by name Vespasian, and Titus; and these were the father [and] son; and then the two, father [and] son, destroyed Jerusalem, all Jerusalem, [shall fall] even to the ground; and stone upon stone shall not be left. And | two, father [and] son, many miseries on the Jews did, the son, the two, the father; because one of the Jews [said]: of hunger [we] die. The second of the Jews: how shall we, Jews, hunger? [famine]; but of the Jews [the] son eat. The third of the Jews and the Jews, out […] Jews, and take heed, the Jews, the head.

  1  Jews people go every scattered and then on-execute Lord
  2  Christ one-ten-+one-ten and two-two-year time grab Lord_God
  3  power Roman general and general | and-exist
  4  exist-+name exist Vespasian and Titus and this exist
  5  the_father son and then two-father-son destroyed Jerusalem every Jerusalem [shall_fall]
  6  until ground and stone on-stone shall_not_be_left and | two
  7  father-son many misery on-Jews do-son-two-father
  8  because one Jews hunger die second Jews how_shall_we-Jews
  9  hunger [famine] but of-Jews son eat third Jews
 10  Jews and-Jews out [?]-Jews and °take_heed-Jews head

## 112r — thirty Jews for one penny, because Judas sold for thirty

> among the Jews captured, all the Jews on the cross put to death, but rather […] and is the head crucified [sold] the head; and the Jews could the head [a penny] on finding; on it the Jews put to death; the head […] sold, the head at thirty to one denarius; and the Jews | from sold the head, remitted, town until town, went. took the head; and the Jews, nine hundred to thirty denarii; and the head more took, than was. Judas; and the Jews sold. The fourth weeping, the writing speaks on Holy Tuesday: then Lazarus at the tomb called; not only the weeping,

  1  among Jews capture every Jews on_the_cross execute °but_rather-[?] and
  2  exist head crucify* [sold] head and Jews can
  3  head [a_penny] on-find on-exist-Jews-+SUBJ
  4  execute head [?]-+SUBJ sell head
  5  on-thirty to-one denarius and-Jews SUBJ | from
  6  sell* head remit town ~until town go
  7  take* head and Jews nine hundred to-thirty denarius
  8  and head SUBJ more grab than exist.
  9  Judas and Jews sell second-two weep write
 10  speak on_Holy_Tuesday = then Lazarus on-tomb called not_only weep

## 112v — the fourth and fifth sorrows: Lazarus, and Good Friday

> the eye of the Lord Jesus, | than highest sad, because Lazarus [was sick], health among out, at the tomb; because three days was Lazarus in the tomb; and Lazarus [was sick], health out, called. The fifth weeping, the writing speaks on Good Friday: then Christ crucified, because to the high Lord [not only] somebody, the Lord died; not only the weeping of the eye of the Lord Jesus, but highest sad, sad for the people [groaned] in the Lord [troubled] believe; because foresaw | the Lord Jesus: then the Jews, the people, go, all scattered, because is the Jews [looked up], heaven, Jerusalem. End [of] this apostle's holy gospel. For on the day of judgment […] the angel divideth, the angel, the evil: how? one sheep [wept]; one […] Jews

  1  eye Lord-Jesus | than highest sad because Lazarus [was_sick] health among
  2  out on-tomb because three_days exist Lazarus inside tomb and Lazarus
  3  [was_sick] health out called fifth weep write
  4  speak on_Good_Friday = then Christ crucified because to-°high-Lord
  5  [not_only] somebody die-Lord not_only weep eye Lord-Jesus but highest sad
  6  sad to people [groaned] inside-Lord [troubled] believe because foresee | Lord
  7  Jesus then-+SUBJ Jews people go every scattered because-exist
  8  Jews [looked_up] heaven Jerusalem end this apostle holy-gospel
  9  because on-judge-year [?]-angel divide angel evil
 10  how? one sheep [wept] one [?]-Jews

## 113r — the division at the judgment, and the opening of the Prodigal Son

> die; this is: in two divided, the firstborn sheep remitted; in turn this younger sheep remitted; this and the man divides in the year of judgment: one gate into hell; the second gives within the kingdom of heaven, but the Lord; there are many speak joy. Begins this holy gospel, the writing, the holy gospel, written by holy Matthew, in the first chapter of his writing. Then said the Lord Jesus to his apostles and the Jewish people: there was one rich Lord God; and then the Lord God had two sons, the angel, the soul; and this younger son of the soul then asked for the soul's

  1  die this_is on-two divide firstborn sheep remit
  2  in_turn this younger sheep remit this and man^ divide
  3  on-judge-year one gate on-hell second give^ inside
  4  heaven land °but_rather-Lord exist many speak* joy
  5  here_begins this holy_gospel
  6  write holy-gospel
  7  write holy-Matthew inside one chapter
  8  of-write time
  9  say Lord-Jesus apostle of-Lord
 10  and Jew people exist
 11  one ~rich Lord_God and then have Lord_God two son
 12  angel soul and this younger soul-son then soul ask

## 113v — the younger son takes his portion and wastes it

> portion of the soul's son, of the Father; and then the son of the soul had much wealth, took it of the Father; because the son of the soul rightly [substance] took of the Father this, of the soul's son, of the Father. And the son of the soul went far, into a | city there was; and the son of the soul stayed in that land, and | began the soul's son to waste it all; the son of the soul stayed in that land, because | began the soul's son to live riotously; and then, many years, the son of the soul stayed there. | In turn brother; and left; hunger this; and the soul-son how shall we eat? because remained […] | rich, eye, say, hear, love, have mercy faith, righteousness: the five senses […] of the Father. And the son of the soul went to a swineherd, and

  1  divide of-soul-son God_the_Father and then soul-son exist many ~rich
  2  grab God_the_Father because soul-son righteous [substance] grab God_the_Father this
  3  of-soul-son God_the_Father and go soul-son far inside | town
  4  exist and leave soul-son inside land and | begin-soul
  5  son from every prodigalize leave soul-son this land because | begin-soul
  6  son lived_riotously and then many-year leave soul-son this | in_turn
  7  brother and leave hunger this and soul-son
  8  how_shall_we* eat because remain-[?] | rich-eye-say-hear-love-have_mercy
  9  believe-righteous-+five-sense-[?]
 10  God_the_Father and go soul-son one pigman and

## 114r — the swine, the husks, and "I will arise and go to my father"

> son this swineherd, evil; and the son of the soul began of the evil pig shepherded; and the soul-son, how shall we food? but the soul-son began, name from name, [husks], [swine], who | sinned […] from, understood; and the soul-son began to speak: have | the Father God has labourers and servants, good, ascension, than this soul-son; ascension, and tasty bread [they] eat. Have mercy, Lord God! The labourers, the servants, than this soul-son, eat. And then this younger son, this son of the soul, and the son of the soul went. the soul-son's Father; want [hired servants]; the soul-son, humbled, wants, the soul-son

  1  son* this pigman evil and begin-soul-son
  2  of-evil pig shepherded and soul-son how_shall_we*
  3  food but begin-soul-son name-from-+name [husks] [swine] who | sin
  4  [?]-from understand and begin-soul-son speak have | the_father
  5  DIV of-soul-son labourer and servant good ascension^
  6  than this-soul-son ascension^ and tasty bread eat have_mercy
  7  Lord_God labourer servant than this-soul-son eat and_said
  8  this the_younger_son this-soul-son and go-soul-son.
  9  of-soul-son the_Father want [hired_servants] soul-son ~humble want-soul-son

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

> and the son of the soul, mercy, this Father, of the son of the soul, all of the son of the soul, committed sin, who became through sin […]. And then this soul-son's Father: labourers and servants, holy apostles, learning, and the angel went, the apostles, the teaching, the angel; and | they brought, the apostles, the teaching, the angel: fairest belief, the Lord's clothes, love, the Lord God; the Lord's clothes, have mercy, the Lord God; the Lord's clothes | the Lord God; the Lord's clothes, righteous, the Lord God. And the soul-son from | the Father, apostles, learning, angels, angels, within the commandment to the Lord's clothes; and | the soul- of the soul went, the apostles, the teaching, the angels, into his Father God's house; there is

  1  and soul-son have_mercy this father of-soul-son every of-soul-son
  2  commit sin who become through ~sin-[?] and_said this
  3  of-soul-son the_Father labourer and servant holy-apostle-learn
  4  and angel go-apostle-learn-angel and | carry-apostle-learn
  5  angel fairest believe Lord clothes SUBJ love Lord_God
  6  Lord clothes SUBJ have_mercy Lord_God Lord clothes SUBJ | Lord_God
  7  Lord clothes SUBJ righteous Lord_God and soul-son from | father
  8  apostle-learn-angel-angel inside commandment to-Lord clothes and | soul
  9  son go-apostle-learn-angel-angel inside of-God_the_Father house there exist

## 115v — the elder brother in the field hears the music

> joy for ever and ever, amen. And | among this. The father of the soul-son, the Father, all of God the Father's [elder son] [in the field] friend; and began […] joy, the apostles, God the Father, learning, the angel. from […] the word [music] and [dancing] [asked]; and then was this the firstborn brother [at] home, because [he] was in the field. That is: within, the angel's joy; and he heard a sound, | of the soul-son, the Father, heaven's house, that is, within heaven's | town it is. And the son of the soul went, dying, this younger son, to the soul-son's Father, heaven's house; and the angel went,

  1  joy for_ever_and_ever = amen and | among-this.
  2  father of-soul-son the_Father every of-God_the_Father [elder_son] [in_the_field]
  3  friend and begin-[?] ~joy apostle-God_the_Father-learn-angel
  4  from-[?] word [music] and [dancing] [asked] and then-~exist this
  5  firstborn brother home because-exist on-field
  6  that_is inside angel joy and hear voice | to-of
  7  soul-son the_Father heaven house that_is inside heaven | town
  8  exist and go-soul-die-son this the_younger_son | on
  9  of-soul-son the_Father heaven house and go-angel

## 116r — he was lost, and is found; the end of the gospel

> this angel, the firstborn brother, to the angel's Father. And then the angel's Father, the Father, of the angel [hath this world's goods] this father, the angel, took one sheep, [it] died; and one loaf of bread, love was, this angel, rejoice, the angel's friend; in turn on this the soul-son, joy, the Father. And understanding he took from this Father: much wealth, the eye, speech, hearing, love, mercy, belief, righteousness, the five senses. And then this father, of the angel, the Father, the son of God the Father: lo, there is the soul-son [who] was lost | released, the angel, God the Father […] labourer the servant; and the son of the soul was dead, and is risen from death, and is saved. The end of this holy gospel.

  1  this angel-firstborn brother to-of-angel the_Father
  2  and_said of-angel the_Father the_Father of-angel [hath_this_world's_goods]
  3  this father angel grab one sheep die and
  4  one loaf bread love-exist this-angel
  5  rejoice of-angel friend in_turn on-this soul-son joy
  6  father and understand grab from this father many ~rich | eye-say-hear
  7  love-have_mercy-believe-righteous-+five-sense and_said
  8  this father of-angel the_Father son of-God_the_Father lo
  9  exist soul-son was_lost | release-angel-God_the_Father-[?]-labourer
 10  servant-and soul-son exist die and rise* on-die be_saved
 11  here_ends this holy_gospel

## 116v — John the Baptist, and the soldiers and publicans who came to him

> Before the gospel: written by holy John the Baptist; this word writes. Then it was, the Lord Jesus within his twentieth year and within the ninth year, within that time preached holy John the Baptist, on Carmel, to the mount; and he went. To John four [peoples]: [publicans], soldiers, Pharisees, farmers, and sin people; because there went soldiers, Pharisees, farmers, and sinners, to be taught by John on Carmel; and first the people were, the soldiers,

  1  before gospel-+SUBJ
  2  write holy-John
  3  the_Baptist this word write
  4  time then
  5  Lord-Jesus inside | two-ten-ten
  6  year and inside nine year inside
  7  time preach
  8  holy-John the_Baptist on-Carmel to-mount and go.
  9  to John two-two [publicans] soldier Pharisee farm and sin
 10  people because exist go soldier Pharisee farm and sin on-learn
 11  to-John on-Carmel on first people exist soldier

## 117r — John the Baptist answers the soldiers, and then the Pharisees

> people; the second people are the Pharisees, the Jews; the third people are the farmers, the people; the fourth people are the sinners. First said the soldiers, the people: Master, the soldiers went to this John to learn on what? learning, are the soldiers: how shall we be saved? | from [they] spoke. And to the soldiers, holy John the Baptist: of the soldiers' riches, and | of the soldiers' clothes, begin to give, soldiers, to God, [content], the poor man of God. and be merciful, soldiers, and righteous, soldiers; that is, yours is the heavenly land. At that time said the Pharisees, the Jews, to John: Master, the Pharisees went [to] | this John to learn on what? learning, are the Pharisees: how shall we be saved?

  1  people second people exist Pharisee Jew third people exist
  2  farm people second-two people exist sinners*
  3  first say soldier people Master-soldier go-soldier this-John
  4  learn on what? learn exist soldier how_shall_we* be_saved | from
  5  speak and soldier holy-John the_Baptist of-soldier ~rich and | of
  6  soldier clothes on-begin donate soldier God [content] poor_man_of_God^
  7  and exist-soldier have_mercy-soldier and righteous-soldier exist | ~you
  8  yours heaven land time say Pharisee
  9  Jew to-John Master-Pharisee go-Pharisee | this
 10  John on-learn on what? learn exist Pharisee how_shall_we* be_saved

## 117v — the Pharisees and the farmers get their answers

> [they] spoke. And to the Pharisees, holy John the Baptist: and have this, Pharisees. righteous people; preach, and teach the sinful; how is sin, from redeem; and be, Pharisees, merciful, Pharisees, and righteous, Pharisees; there is yours the kingdom of heaven. Then said the farmers, the people, to John: Master, the farmers went [to] this John to learn on what? learning, are the farmers: how shall we be saved? [they] spoke. And to the farmers, holy John the Baptist: and have this, farmers; you farmers, farm, plough? and sow? and rightly, of the farmers, suffering living; and to the poor of God give alms; be ye farmers merciful, ye farmers, and righteous, ye farmers; yours is the kingdom of heaven.

  1  speak and Pharisee holy-John the_Baptist and have this Pharisee.
  2  righteous people preach and sin learn how? exist sin | from
  3  redeem* and exist-Pharisee have_mercy-Pharisee and righteous-Pharisee exist
  4  you heaven land time say farm.
  5  people to-John Master-farm go-farm this-John
  6  on-learn on what? learn exist farm how_shall_we* be_saved speak
  7  and farm holy-John the_Baptist and have this-farm you
  8  farm farm plough? and sow? and righteous of-farm suffering
  9  living and poor_man_of_God = donate exist-farm have_mercy-farm
 10  and righteous-farm exist you heaven land

## 118r — and the sinners, who get the great commandment

> At that time said the sinners: Master, the sinners | went the sinners [to] this John to learn on what? learning, are the sinners: how shall we be saved? [they] spoke. And to the sinners holy John the Baptist: and have, sinners; love the Lord God most high [with] all [your] hearts, all the sinners' souls, all the sinners' might, all your heart; and your brother as somebody [his] neighbour; be, sinners, | merciful sinners, and righteous, sinners; and keep, sinners, the commandments of God; […] a hundred […] sins, and be saved, sinners, [with all thy strength], suffering, for ever and ever, amen; there is

  1  time say sinners* Master-?sinners | go
  2  sinners* this-John on-learn on what? learn exist.
  3  sinners* how_shall_we* be_saved speak and sinners*
  4  holy-John the_Baptist and have sinners* love Lord_God
  5  most_high all^ create all^ of-?sinners soul all^ of-?sinners
  6  might all^ of-?sinners heart and of-?sinners
  7  brother as somebody neighbour exist-?sinners | have_mercy
  8  sinners* and righteous-?sinners and carry sinners*
  9  commandment God ~exist-hundred-[?]-~sin be_saved sinners*
 10  [with_all_thy_strength] suffering for_ever_and_ever = amen exist

## 118v — the commandment summed up, and a new reading from Luke

> yours the kingdom of heaven. This teaching is [murmured] not love the Lord the divine one highest [above] every creature; and the man is keeping the commandments of God, ours, is the kingdom of heaven. And this is: this love, the commandment, take from […] to be saved; and the man who believeth in the Lord Jesus Christ, as the true Son of the living God, everybody shall be saved; and one is not damned but: every man shall be saved. Begins this holy gospel, written by holy Luke, in the seventh chapter of his writing. At that time the Lord Jesus [was] within [his] thirty-first year; then went the Lord Jesus into the Pharisees' town; and there went to the Lord various sinners, to the Lord Jesus; and

  1  you heaven land this learn exist [murmured] not* love | divine_one^
  2  DIV highest every create and man^ and exist carry commandment God our
  3  SUBJ heaven land and this_is this love commandment grab
  4  from [?]-°again on-be_saved and man^ and exist believe
  5  inside Lord-Jesus-Christ as righteous son living God everybody =
  6  be_saved and one is_not be_damned but everybody = be_saved
  7  here_begins this holy_gospel write holy-Luke inside seven chapter | of
  8  write time then Lord-Jesus inside thirty one-~year
  9  time go Lord-Jesus inside Pharisee town and go
 10  to-Lord various sinners* to Lord-Jesus and

## 119r — the Lost Sheep

> the Pharisees began, the Pharisees and the church fathers, to murmur on the Lord Jesus, [that] he spoke [as] the Son of God; in turn then he is the Son of God | this the Lord [leaveth], goes, this [in the desert]. And then the Lord Jesus | then there is one [who] has, call you | one hundred sheep in the wilderness, and if he lose one call, end, [layeth it] [shoulders]; the man is, answered, hide, year, who, chapter, say and does he not leave the ninety sheep and nine in the wilderness; and somebody goes, ninety-nine sheep, find; and then somebody finds the sheep, and somebody takes the sheep, the man | on

  1  begin-Pharisee Pharisees* and church_father murmur on-Lord-Jesus he speak
  2  son God in_turn then he exist son God | this
  3  Lord [leaveth] go this [in_the_desert] and_said Lord-Jesus | then
  4  exist one have call^ you | one
  5  hundred sheep inside wilderness^ and then lose one
  6  call^ end* [layeth_it] [shoulders] man^ exist answered-hide-~year ~who-chapter-say
  7  and exist from-food-somebody from nine-ten sheep and nine
  8  inside wilderness^ and go-somebody ninety* nine sheep
  9  find and then sheep find-somebody
 10  and sheep grab-somebody man* | on

## 119v — the lost sheep found, and the woman with ten pieces of silver

> our shoulder; and somebody goes to our friends and neighbours, and he is, with friend and neighbour; he said to them: I have found, somebody's sheep [which was lost]; somebody is this, this; wish; and good on the sheep, joy; but on the ninety-nine sheep. And then the Lord Jesus: then one woman, the head, and is having ten silver [coins]; and then of these ten, lost Eve; and there is light, Eve, the son of Mary, born, crucified, the lamp; and then Eve findeth this silver [coin], the heavenly land; and there is good, over heaven, the kingdom, joy, Eve; over the Lord Christ's dying,

  1  our shoulder and go-somebody to-our friend and neighbours
  2  and exist and-friend-neighbor say-somebody say exist | found
  3  somebody sheep [which_was_lost] somebody exist this-this wish and
  4  good on-sheep joy ~but on-nine-ten and nine sheep
  5  and_said Lord-Jesus then one woman ~head
  6  and exist have ten silver and then this ten lost
  7  Eve and exist light Eve | Mary-son
  8  be_born-+crucified lamp and then find Eve
  9  this silver heaven land and exist good
 10  on-+heaven land joy Eve on-die-Lord-Christ

## 120r — the ninety-nine, and the nine orders of angels

> Eve rejoices, than on food nine drachmas; commandment. End [of] this holy gospel. Then the Lord [telleth], the Lord Jesus [until] the sufferer. The gospel: said the Lord Jesus [to] the Lord's apostles and the Jews, the people: I one Lord, this sheep; because to the Lord, I | abandon the Lord, the nine orders of angels within the kingdom of heaven. And then the Lord Jesus: then the Lord created, the Father, heaven; on the heavenly land, on the Holy angels, upon the angel whose name is Lucifer, and the second angel, and Lucifer prayed; and forty years

  1  Eve rejoice^ than on-food nine drachma commandment end
  2  this holy-gospel then-Lord [telleth] Lord-Jesus [until] sufferer
  3  gospel say Lord-Jesus apostle of-Lord and Jew people I
  4  one Lord this sheep because to-Lord I | abandon
  5  Lord nine order angel inside heaven land
  6  and_said Lord-Jesus then-Lord create the_Father
  7  heaven on-heaven land on_Holy angel
  8  on angel name exist Satan and two
  9  angel and Satan ~pray and ten-ten-ten-ten-year

## 120v — the fall of Lucifer, and the order left empty

> and forty, and night, which Lucifer, to Lucifer, on the heavenly land, on hell, redeem one order, the year, the chapter, from; and then I went, the Lord, the Father, of the Lord; from I, the Lord wanted [the tenth] half order of angels; and from the ascension of the Lord until the year of judgment wanted the Lord, of the Lord | from the Father God, [the tenth] from the order, in the place [shall stand empty] there is the Lord, the Lord bowed down, the Father of the Lord, on the heavenly land, on hell; then | went the Lord, God the Father, the Son, God, Jesus, the Holy Spirit, Mary, Christ, the apostles, the angels judge living, and dying redeem [shall fill it]

  1  and ten-ten-ten-ten and night which-Satan to-Satan
  2  on-heaven land on-hell redeem* SUBJ one
  3  order ~year-chapter from* and then I go-Lord the_Father
  4  of-Lord from I want-Lord [the_tenth] half order angel and from
  5  ascension of-Lord ~until judge-year want-Lord of-Lord | from
  6  God_the_Father [the_tenth] from order on-place [shall_stand_empty] SUBJ | exist
  7  Lord bow-Lord the_Father of-Lord on-heaven land
  8  on-hell then | go-Lord-God_the_Father-son-God-Jesus-holy-spirit
  9  Mary-Christ-apostle-angel judge living and die redeem* [shall_fill_it]

## 121r — the tenth order, and the drachma that was lost

> I am judging, the Lord, of the Lord the Father, on the sheep, the righteous people; and believe in the divine one, and in the Lord's Father, many judge, and the neighbours, and the friends, the angels, and the apostles, for ever and ever, amen. And then the Lord Jesus: this woman, this is of the Lord's creation; you, mother Eve; from Eve | is Eve lost one; Eve, one silver [coin], one order, the order within the kingdom of heaven; because then bowed, the Father, heaven, on the Holy angels, on heaven. land, on hell. And then the Lord Jesus said: there is

  1  exist I judge-Lord of-Lord the_Father on-sheep
  2  righteous people and believe inside divine_one^ and inside of-Lord the_Father many
  3  judge and neighbours and friend angel and apostle for_ever_and_ever =
  4  amen and_said Lord-Jesus this woman this_is of-Lord
  5  create you mother Eve from Eve SUBJ | exist
  6  Eve loseth_one-Eve one silver one
  7  order order inside heaven land because then
  8  bow the_Father heaven on_Holy angel on-heaven.
  9  land on-hell and_said Lord-Jesus say exist

## 121v — the Trinity: Father, Son and Spirit, and one God

> from the Father to the Son goes the Holy Spirit; Father, Son, creation, man. And then the Father, the Holy Spirit: on how the man [was] imaged [they] would like, Father, Son, Spirit, create. And then the Son | on the image [after our] [likeness]: man is, all one, to the Father, the Son, the Spirit. Father, Son and Spirit took man, and every cattle [creature]; the soul heard; the man saw rightly; not many [in] the Father, from the Son; not many the Holy Spirit; but this Lord is all one God. And then the Lord Jesus went out, the Lord. Father, Son and Spirit, out, into the kingdom of heaven, into this world.

  1  the_Father to-son go holy-spirit father son create man^
  2  and_said the_Father holy-spirit on-how? man^ image^
  3  would_like^ father son spirit create and_said son | on-of
  4  image^ [after_our] [likeness] exist man^ every one | to
  5  father son spirit grab father son spirit man^
  6  every cattle^ [creature] soul hear man^ see righteous not
  7  many the_father from son not many holy-spirit but
  8  this Lord every one God and_said Lord-Jesus go_out-Lord
  9  father son spirit out on-heaven land on-this world

## 122r — the Lord God forms Adam and breathes into him

> And out of Paradise the Lord God, the man, created, slime (of the earth) And then the man was, created, aforesaid, [breathed], and became one soul, created; breathed on Adam; and he became living. And the Lord, the Father, the Son took the man. the Spirit; and the man went, the Lord, the Father, the Son, the Spirit, within Paradise; and every creation before the man, created, Lord, Father, Son, Spirit. And then the Lord Jesus said: the Father of the Lord God, heaven, the man, name […] this Adam took all rightly [nor] hunger and thirst [nor] this Adam;

  1  and out Paradise Lord_God man^ create slime_(of_the_earth)*
  2  and then man^ exist create aforesaid [breathed] and
  3  became* to-soul-+one create breathe on-Adam and
  4  living leave and man^ take^ Lord-father son.
  5  spirit and man^ go Lord-father son spirit
  6  inside Paradise and every create before man^
  7  create Lord-father son spirit and_said Lord-Jesus say the_father
  8  of-Lord God heaven man^ name-[?] this-Adam
  9  take^ every righteous [nor] hunger and thirsty [nor] this-Adam

## 122v — the commandment, the sleep, and the rib

> and one living [thing] dies, sins, has hunger, thirsty, to the girl. [afterward] the Lord took, this Adam, all rightly one: the commandment, this yoke, this Adam, command: do not eat this [fruit] of the son, the forbidden fruit; thou shalt die. If Adam is eating, in that place, and died. And then Adam slept, into Paradise; and then the first table, from the hour; and then went the Holy Spirit within Paradise. And then this this, the garden; and the Lord God took from Adam a rib; and Eve created. And then the Lord Jesus: you, mother. And then Adam

  1  and one living-die-sin have hunger thirsty girl-to.
  2  [afterward] grab Lord this Adam every righteous one
  3  commandment this yoke this Adam command = do_not eat
  4  this to-~son forbidden_fruit thou_shalt_die* ~if Adam exist eat
  5  on-place die and then Adam sleep inside into_Paradise
  6  and then table first from hour and then go holy-spirit
  7  inside Paradise and_said this SUBJ this the_garden and
  8  grab Lord_God Adam rib and Eve create
  9  and_said Lord-Jesus you mother and then Adam

## 123r — bone of my bones, and the serpent

> from laughing; and then this: bone of bones. In turn, two souls, one brother by name. And then the Lord Jesus left, the Lord God the Father. the Son, the Spirit, into the kingdom of heaven; and there went Eve in Eden; and then Eve, Eve went to this tree, what tree; it is the Lord God's through commandment; and [she] saw a serpent. And then this serpent: Eve, eat this fruit. And then Eve: [we] shall not eat, eat, because Eve, Adam, Master, command. And then this serpent: Eve, eat; Eve, Adam.

  1  from laugh and_said this bone bones in_turn two soul
  2  one ~brother-+name and_said Lord-Jesus leave Lord-God_the_Father
  3  son spirit on-heaven land and go
  4  Eve on-Eden and then Eve
  5  Eve go to this tree what tree
  6  exist Lord_God through commandment and see one serpent and_said this serpent Eve
  7  eat this fruit and_said Eve shall_not_eat eat
  8  because Eve Adam Master command = and_said
  9  this serpent Eve eat Eve Adam

## 123v — she took of the fruit, and their eyes were opened

> this; in turn the fruit is; Eve, one; Adam eats. Eve is, Adam; they knew evil and good, how to the Lord God it is known. And then she plucked, the serpent, this [beguiled], this serpent; and then Eve took, in turn Eve, the fruit; Adam took [it]; and then were opened in the place: Adam naked; Eve saw Adam; and then Eve [and] Adam were ashamed. And then the Lord Jesus: and this, on dying, sin, hiding, did. Satan; the Lord, Father, Son, the Spirit of God, of the Lord, somebody, the Father

  1  this in_turn fruit SUBJ exist Eve one Adam eat
  2  exist Eve Adam know evil and good | how?
  3  to Lord-God know and then pluck serpent this
  4  [beguiled] this serpent and then grab Eve
  5  in_turn Eve fruit grab Adam and then
  6  were_opened* on-place Adam naked see Eve
  7  Adam and then Eve Adam be_ashamed
  8  and_said Lord-Jesus and this on-die ~sin-hide do
  9  Satan Lord-father son Spirit_of_God^ of-Lord somebody the_Father

## 124r — Adam, where art thou?

> who Satan is, put off [by] God the Father from heaven; | in turn, chapter, the year is on hell. And then the Lord Jesus left, the Lord, Father, Son, the Spirit of God, into heaven, land, within Eden. And then the Lord Jesus: this second table, from the hour; and then left, the Lord, the Father, the Son, the Spirit; left into the kingdom of heaven, into Paradise; he said: there is [down] | of […]. the Spirit of God to Adam: Adam, why? And then Adam hid; Adam; the Lord God said, | the Lord, Father, Son, the Spirit of God: why, Adam, hide? said Adam

  1  who-+SUBJ Satan exist put_off God_the_Father on-heaven | in_turn-chapter
  2  ~year-exist on-hell and_said Lord-Jesus leave Lord-father son
  3  Spirit_of_God^ on-heaven ~land inside Eden
  4  and_said Lord-Jesus this table two from hour and then
  5  leave Lord-father son Spirit_of_God^ leave on-heaven land
  6  inside into_Paradise say exist [down] | of-[?].
  7  Spirit_of_God^ to-Adam Adam why? and_said
  8  Adam hide Adam Lord_God say | Lord-father-son
  9  Spirit_of_God^ why? Adam hide say Adam

## 124v — the woman gave me, and the serpent beguiled me

> who, this Adam, naked, said [to] the Lord, Father, Son, Spirit: why? Adam naked said: Adam, Eve, Adam, she gave me to eat. Said the Lord, the Father, the Son, the Spirit: Eve, where? said; Eve, which Eve, to me said. The Lord, Father, Son, Spirit: why? Eve, which, who. who? Eve naked said [to] the Lord, Father, Son, Spirit: why? Eve naked said: Eve, the serpent, Eve, food. Said the Lord Jesus, said: there is, of the Lord, the Father, to Adam: Adam, to one

  1  who this-Adam naked say Lord-father-son-spirit
  2  why? Adam naked say ~Adam Eve
  3  Adam gave_to_eat say Lord-father-son-spirit Eve
  4  where? say Eve which Eve I-to say
  5  Lord-father-son-spirit why? Eve which who.
  6  who Eve naked say Lord-father-son-spirit
  7  why? Eve naked say Eve serpent
  8  Eve food say Lord-Jesus say exist of-Lord
  9  the_Father to-Adam Adam to-one

## 125r — to till the ground, and the sorrow

> commandment; this Adam is, name […] ten commandments carry, is Adam, to the girl, on Adam's; in turn, chapter, who. gates Adam is, the earth, to till the ground; wanted to take food to the son; in turn Eve this; Eve is through pining, and this Eve is painful, born, he hath; in turn this evil is [cursed] the earth, the serpent slideth, and a room for evil; this man was made, all of this; the serpent

  1  commandment this-Adam exist name-[?]-ten commandment carry exist
  2  Adam girl-to on-of-Adam in_turn chapter-~who.
  3  gates* exist Adam earth to_till_the_ground
  4  want to-~son food take^ in_turn Eve this
  5  Eve exist through pine and this Eve
  6  exist painful ~be_born have in_turn this evil
  7  exist [cursed] earth slide and
  8  room evil this man^ create every this serpent

## 125v — driven out, and the flaming sword

> dieth; and [it] became among Adam and Eve of the Lord, Father, Son, God, Spirit, the Father God, Jesus, the angel, the Virgin Mary, Christ, and the apostles, and the Jews, and the man baptized, and all. [he drove out]; and all the heavenly land, the Lord, and the Lord's creation, all the earth, and hell, and the heavenly land; and there went the Lord God, the angel, the second, the earth, and Eve, flame, the sword, and | earth [were] out; from the Garden of Eden they were cast out.

  1  die and become^ among Adam_and_Eve
  2  of-Lord father son God spirit the_father God Jesus angel
  3  Virgin_Mary Christ and apostle and Jew and man^ ~baptize and every.
  4  [he_drove_out] and every heaven land Lord and Lord-create
  5  every earth and hell and heaven land
  6  and go Lord_God angel two earth and.
  7  Eve flame^ sword and | ~earth
  8  slide out on-inside Eden exorcise

## 126r — the cherub at the gate, and the third saying

> And [he] placed the angel with the sword at the gate; Eve, of Eden; and one creature can be within Eden; but the angel. And then the Lord Jesus: this third table, from the hour, said the Lord Jesus: this this silver [coin]; and it is lost then, from the forbidden fruit, [which] the two ate. Adam; and Eve and Adam slid out; cast out, the Lord, the Father, the Son, the Holy Spirit; and then hell, the evil; from Adam and Eve taken, from the good, one commandment of God; which chapter Adam and Eve had.

  1  and place^ angel sword on-gate Eve
  2  Eden and one create can_be inside
  3  Eden but angel and_said Lord-Jesus
  4  this table three from hour say Lord-Jesus this SUBJ this
  5  silver and exist lose then from forbidden_fruit eat two
  6  ~Adam and Eve and ~Adam slide out
  7  exorcise Lord-father son holy-spirit and then hell
  8  evil from Adam_and_Eve take^ from good
  9  one commandment God which-chapter Adam_and_Eve have

## 126v — the Lord seeks the drachma he lost

> The Lord, the Father, the Son, the Spirit, took what was lost; | Adam slide. Said the Lord Jesus: then the two could not find. Every house this | redemption; not have mercy on the angel of the Lord, the Father; could, woman, find redemption? not. [He] was born [of a] mother, of the Lord's love, and redemption; I, from a mother, [again] was born; and redemption, I, on the cross [thereon]; in turn then […] on the cross; from [there] want to find this silver [coin], this heaven kingdom […] there is, from Adam and Eve; abandon Satan. And said the Lord Jesus: I want, the Lord, to take the trespass and redeem, the Lord, of the Lord's Father in heaven.

  1  Lord-father son spirit exist grab lose | two-~Adam
  2  slide say Lord-Jesus then-not two can find.
  3  every house this | redemption not have_mercy on-angel of-Lord
  4  the_Father can ~woman find redemption not
  5  exist be_born mother of-Lord love and redemption I from mother
  6  [again] be_born and redemption I on_the_cross [thereon] in_turn
  7  then-[?] on_the_cross from want find this silver this heaven
  8  land [?]-+SUBJ exist from Adam_and_Eve
  9  abandon Satan and say Lord-Jesus I want-Lord
 10  trespass grab and ~redeem-Lord of-Lord the_Father heaven

## 127r — Hezekiah is told he shall die, and is given more years

> said within a dream God's angel to holy Hezekiah the prophet; Hezekiah, the Lord God, this is, saith the Lord: within three days, this | one shall die. And then from laughter, holy Hezekiah began, Hezekiah, to be sad, holy Hezekiah; and cried out: who [will] prepare, chapter, to, and there went to Hezekiah the Creator Lord; and the rest said God's angel: Hezekiah, the Lord God, this is, says: prolong life, chapter, to, and is until five [and] fourteen years(?) living, chapter, to, and; and prolong life.

  1  say inside dream God angel
  2  holy-Hezekiah
  3  prophet Hezekiah
  4  Lord_God this_is say-Lord
  5  until three_days | this
  6  SUBJ die and then
  7  from laugh holy-Hezekiah
  8  beginning^ Hezekiah sad
  9  holy-Hezekiah and cry_out who prepare-chapter-to-and
 10  go to-of-Hezekiah Creator_Lord and the_rest^ say God angel
 11  Hezekiah Lord_God this_is say prolong_life-chapter-to-and exist
 12  until five-fourteen-?years living-chapter-to-and and prolong_life

## 127v — Hezekiah dies, and Paul sets his house in order

> Made ready, holy Hezekiah; and upon […] Hezekiah's soul gave out; and then, chapter, to, and Hezekiah's soul gave out; at that time appeared. the angel of God, and said to the servants: of Hezekiah, lay him. this body within the tomb; in turn the soul of Hezekiah | this the angel wanted, the angel, to give; and the angel left, in turn holy Hezekiah's body within the tomb put. The servants speak; holy Paul apostolic letter [writeth] the brethren of Paul […] and Paul made ready, of Paul, the last day.

  1  prepare holy-Hezekiah and on-[?]
  2  of-Hezekiah soul give_out and then-chapter-to-and
  3  of_Hezekiah soul give_out time appear.
  4  God angel and say servant of_Hezekiah put.
  5  this body inside tomb in_turn soul Hezekiah | this
  6  angel want-angel give^ and leave angel
  7  in_turn holy_Hezekiah body inside tomb put.
  8  servant speak holy-Paul apostolic_letter [writeth] brother of-Paul
  9  ~have-[?] and Paul prepare of-Paul last day^

## 128r — Paul's one only Son, and a new reading begins

> as is prepared, Hezekiah, holy Hezekiah the prophet; this [foretold] has; and Paul, somebody, prepared, to the Lord Jesus, the Son of God, of Paul, the man, the one only, brother went, this somebody, because [he] lost [the sheep] Begins this | holy gospel, written | by holy Luke, in the first chapter, in his writing. Then, then on crucifying, the Lord Christ, three days

  1  as exist prepare-Hezekiah holy-Hezekiah
  2  prophet this [foretold] have and Paul-somebody prepare to
  3  Lord-Jesus son God of-Paul-somebody one only
  4  brother go-this-somebody because lose [the_sheep]
  5  begins this | saint^
  6  gospel write | saint^
  7  Luke within^ one chapter within^
  8  of-write time
  9  then on-crucify
 10  Lord Christ three_days

## 128v — they were terrified, and believed not for joy

> another night; then appeared the Lord's apostles, the gate. And then the Lord Jesus: the commandment | you, chapter [so] he is; and through, the apostles were startled, because the apostles believed as how? a ghost. And then the Lord Jesus had the apostles; the Lord, he; the apostles saw within | is is, chapter, somebody [a spirit], the angel, body. in turn, one ghost; could the apostles, the Lord, because the Lord, who I, I to you, through be thirty days and three, and literally

  1  another* night time appear
  2  apostle of-Lord gate and_said Lord-Jesus commandment | ~you-chapter
  3  [so] exist and through startle apostle because
  4  believe apostle as how? ghost and_said
  5  Lord-Jesus have-apostle Lord he see-apostle inside | exist
  6  exist-chapter somebody [a_spirit] angel body
  7  in_turn one ghost can apostle Lord
  8  because* Lord ~who-I I to-you
  9  through stay thirty day and three and literal

## 129r — receive ye the Holy Spirit, and go into all the world

> and the apostles can, because the Lord Jesus, Christ, to, because not out, the Holy Spirit, mercy; and spake holy John: he breathed upon them, learning; and all the apostles took the Holy Spirit. And then the Lord Jesus, the Lord's apostles: you go, apostles, into the world, and be ye his apostles; preach the gospel. baptize somebody in the name of the Father and the Son and the Holy Spirit; everybody is saved; if, and somebody not

  1  and can apostle because* Lord-Jesus ~Christ-to because-not
  2  out holy-spirit have_mercy and speak holy-John | breathed
  3  upon_them learn and every apostle grab holy-spirit
  4  and_said Lord-Jesus apostle of-Lord you go-apostle
  5  into_the_world* and exist-apostle of-Lord gospel preach
  6  and exist-apostle baptize inside of-Lord name
  7  and somebody exist Lord believe and exist
  8  baptize somebody inside name the_Father and son
  9  and holy-spirit everybody = be_saved if and somebody not

## 129v — baptize them, and be brought before kings

> baptize in the name of the Father and the Son and the Holy Spirit. One man shall be saved; in turn, every man shall be damned. And said the Lord Jesus to his apostles: ye shall | go, the Jews, before kings, before emperors. | Not the disciples have, because I am [with] you that not the disciples [teach]; how say? it is the apostles speak. And then the Lord Jesus had these apostles from him; and a man, you, the apostles, body die, rather somebody, apostle, from the Lord God. have, and the Lord you, disciples, soul and body

  1  baptize inside name the_Father and son and holy-spirit
  2  one man^ be_saved but everybody = be_damned and
  3  say Lord-Jesus teach^ of-Lord you exist | go
  4  Jews before king before emperor | not
  5  teach^ have because I exist you that
  6  not teach^ [teach] how? say exist speak-apostle and_said
  7  Lord-Jesus have this-apostle from and man^ you teach^
  8  body die rather somebody-apostle from Lord_God.
  9  have and-Lord you teach^ soul and body

## 130r — the apostles go out, and a new reading from John

> destroy. And then the Lord Jesus: then went the apostles, preached, and began from Jerusalem; and the disciples preached on all the whole world. The end of this holy gospel; and the Lord Jesus departed from among the apostles. Begins this holy gospel, written by holy John, in the second chapter of his writing. Then said the Lord Jesus to his apostles, the Lord, at the last supper: I go, the Lord, to the Lord's Father; he who, the Lord, goes, the Lord,

  1  destroy and_said Lord-Jesus then go-apostle preach and
  2  begin from Jerusalem ~and preach teach^ on-every all_the_world world.
  3  here_ends this holy_gospel and leave among teach^ Lord-Jesus
  4  begins this.
  5  holy-gospel write
  6  holy-John inside two chapter
  7  inside of-write time
  8  say Lord-Jesus teach^ | of
  9  Lord at_the_Last_Supper =.
 10  I go-Lord to-of-Lord the_Father he_who Lord go-Lord

## 130v — Thomas, and Philip: shew us the Father

> And then holy Thomas: Master, goes the Lord to the Lord's God the Father? Said | the Lord Jesus: Thomas, I go, the Lord, to the Lord's God the Father; and the Lord goes, the Lord. And then | holy Philip: Master, show the apostles the Lord's Father. And then the Lord Jesus: Philip, the apostles the Lord the apostles saw; then I did miracles, [works], miracles; one Lord; I to the Lord by doing; but rather God the Father, of the Lord, […] doeth them, the Lord's finger. And the apostles [he] began to rebuke on belief. And then the | Lord Jesus: and a man, the Lord, the apostles have seen, these apostles, and of the Lord the Father saw; and the man is believing the Lord; this is

  1  and_said holy-Thomas Master go-Lord to-of-Lord God_the_Father say | Lord
  2  Jesus Thomas I go-Lord to-of-Lord God_the_Father and SUBJ-Lord
  3  go-Lord and_said | holy-Philip Master show apostle
  4  of-Lord the_Father and_said Lord-Jesus Philip SUBJ apostle
  5  Lord see-apostle then I miracle do [works] miracle
  6  one-Lord I to-Lord by do but_rather* God_the_Father
  7  of-Lord [?]-°down do of-Lord finger
  8  and apostle begin rebuke on-believe and_said | Lord
  9  Jesus and SUBJ man^ Lord see-apostle this-apostle SUBJ and of-Lord
 10  the_Father see and man^ exist Lord believe this exist

## 131r — the pagans and the resurrection

> and the Lord's Father believe, because this one God. And then the Lord Jesus: you go, apostles, within land [and] land, among the pagans; and the pagans; preach, apostles, how I from death stood up, up; how it is from the pagans, you apostles, believe, because God said, the mouth, year; hear; and the Lord see, pagans. And then the Lord Jesus said: the Lord | you yours; how you apostles are, the pagans | to believe: because the pagans are before you, the dead carry, the pagans, on standing up, resurrect; and this | is

  1  and of-Lord the_Father believe because this one
  2  God and_said Lord-Jesus you go-apostle inside
  3  land land among pagan and
  4  pagan exist preach-apostle how? I from-die
  5  stand_up up how? exist from pagan you
  6  apostle believe because God say mouth-~year hear and SUBJ
  7  Lord see pagan and_said Lord-Jesus say-Lord | ~you
  8  yours how? you apostle exist pagan | to
  9  believe* because-exist pagan before you
 10  die carry-pagan on-~stand_up resurrect and this | exist

## 131v — in my name, and he that believeth and is baptized

> the apostles say, the apostles: this, the dead, offer; the apostles can, Jesus of Nazareth have; the dead up, rise, resurrect; in the place rise, resurrect, somebody, in the Lord's name. And then the Lord Jesus: and the man who believeth in the Lord, every such man shall be saved; and one somebody is damned. And then the Lord Jesus: and somebody [does] not believe the Lord; one somebody is saved, but everybody is damned. And then the Lord Jesus: and the man who believeth the Lord, to be | one woman baptize in the name of the Father and the Son and the Holy Spirit: every such man shall be saved, and one man

  1  apostle say-apostle this-the_dead offer apostle can Jesus Nazareth
  2  have the_dead up rise^ resurrect on-place rise^ resurrect
  3  somebody inside of-Lord name and_said Lord-Jesus and
  4  somebody exist Lord believe everybody = be_saved
  5  and one somebody be_damned and_said Lord-Jesus and
  6  somebody not Lord believe one somebody
  7  be_saved but everybody = be_damned and_said Lord-Jesus
  8  and somebody exist Lord believe to exist | one-~woman
  9  baptize inside name the_Father and son and holy
 10  spirit everybody = be_saved and one somebody

## 132r — the signs that shall follow them that believe

> is damned. And then the Lord Jesus: and somebody is believing the Lord shall do many miracles, all in the Lord's name; | and there is […]; at that time the apostles saw [him] bow on heaven, land, light. And then the apostles: Master, [we] saw the apostles, the light, bowed on heaven; land; said the Lord Jesus: lo, bowed, could Satan. And then the Lord Jesus: go ye, apostles, into the world; be ye apostles to the ass; heal ye, apostles; be ye apostles; the evil | upon the people cast ye out, apostles; the blind eyes, through light, apostles; the dead stand up, resurrect, apostles, all in the Lord's name.

  1  be_damned and_said Lord-Jesus and somebody exist Lord believe
  2  exist many miracle do every inside of-Lord | and
  3  exist-[?] time see apostle bow on-heaven
  4  land light and_said apostle Master see
  5  apostle light bow on-heaven ~land say
  6  Lord-Jesus lo bow can Satan and_said
  7  Lord-Jesus you-apostle go into_the_world* exist-apostle
  8  to-from-donkey heal-apostle exist-apostle evil | on
  9  people ~exorcise-apostle eye-blind through light-apostle
 10  the_dead stand_up resurrect-apostle every inside of-Lord name

## 132v — the end of the reading, and the angel comes to Elijah

> and on how, chapter, somebody | ill; go, apostles, every chapter | from healing, apostles, in the Lord's name. The end of this holy gospel. Then appeared the angel of God to holy Elijah the prophet. Then

  1  and ~on-how? chapter-somebody | ill go-apostle every chapter | from
  2  healing-apostle inside of-Lord name here_ends this holy_gospel
  3  time then appear God angel
  4  holy-+Elijah prophet time then

## 133r — Elijah's forty days, and the angel at Horeb

> From Adam [to] the Creator Lord, until this [thousand] | five hundred day, and thirty [and] six years. At that time appeared God['s angel] angel [to] holy Elijah the prophet. And then God's angel: Elijah, the Lord God, this is, says the Lord: fast. forty; go, Elijah, afar [to the] mount; and the body it is Horeb. And then went Elijah upon this mount Horeb; and then Elijah lay down, to one tree; and a second time said the angel of God: Elijah, take, and Elijah found, and Elijah did eat, and Elijah was strengthened; and Elijah went [forty days], Elijah, upon this mount Horeb, the love of the Lord God.

  1  from ~Adam Creator_Lord until this [thousand] | five_hundred
  2  day^ and thirty six-year time appear God
  3  angel holy-+Elijah prophet and_said God angel
  4  Elijah Lord_God this_is say-Lord exist fast
  5  forty go-+Elijah on-far mount and ~body
  6  exist Horeb and then go Elijah on-this mount
  7  Horeb and then from Elijah lie | to
  8  one tree and second^ say God angel Elijah take^
  9  find-+Elijah eat-+Elijah exist-+Elijah strengthen
 10  and go-+Elijah [forty_days] Elijah on-this mount Horeb love Lord_God

## 133v — the cake and the cruse, and Elijah taken up

> This is this mount, the love of the Lord God most high, of every creature. And then went Elijah upon this mount Horeb, and before he went, in that place [under a juniper] lay down holy Elijah the prophet; and Elijah found one cake, and one cup of water; and he did eat, and drank, and was strengthened, upon this mount [of God] Elijah. And from the fast, forty; and this forty, then, at that time took Elijah, the two, Noah; [wished to die]; [a cake] and Elijah [and] Noah were caught up into heaven on high; and from Elijah man is Noah, Elijah, the sword carry; hell, one gate open; and [Enoch] left; Noah, Elijah on the earth.

  1  this_is this mount love Lord_God highest every create and then go Elijah
  2  on-this mount Horeb and before go from on-place [under_a_juniper]
  3  lie holy-+Elijah prophet exist find-+Elijah
  4  one a_cake and one cup water and
  5  eat and drink and strengthen on-this mount [of_God] Elijah
  6  and from fast forty and this forty then
  7  time grab to-+Elijah-two-Noah [wished_to_die] [a_cake]
  8  and Elijah-Noah be_caught_up heaven high and from
  9  Elijah man* exist ~Noah Elijah sword
 10  carry hell one-+gate/open and [Enoch] leave Noah Elijah on-earth

## 134r — Antichrist, and a new reading: the king who took account

> [Antichrist] [of a harlot] through birth, the two, the chief evil, the evil one, and the son of the devil, by name evil; it is | Anti- christ. Before the gospel, said the Lord Jesus left: a king, a man, king; hear all […] | of the kingdom. Begins this holy gospel, written by holy Matthew, in the [eighteen] chapter of his writing. Then said the Lord Jesus the Lord's apostles and the Jews, the people: there is, among the Lord God, doomsday, one king; all priest heavenly, the Lord, the man, before the Lord God the king; and then he had one heavenly

  1  [Antichrist] [of_a_harlot] through be_born two chief_devil = and
  2  son Satan name evil exist | Anti-
  3  baptize before gospel say
  4  Lord-Jesus leave
  5  king somebody ~king
  6  hear every priest | of
  7  ~king kingdom^ begins
  8  this holy-gospel write
  9  holy-Matthew inside [eighteen] chapter of-write time say Lord-Jesus
 10  apostle of-Lord and Jew people exist among Lord_God doomsday
 11  one king every priest heaven^ Lord somebody before
 12  Lord_God-king and then have one heaven^

## 134v — ten thousand talents, and the servant sold

> a servant; and the lord's servant owed ten thousand talents; and there went this Lord God the king, this heavenly servant; and then the servant, the angel, went before this | Lord God the king, before the Lord Christ; and the servant began asked this Lord God, somebody, the king, of the Lord | [forgave the debt] to do good. And then the Lord God, the king: | commandment, love, mercy, righteousness, good deeds, not to the high, take. And then this Lord God, the king, sold the angel-somebody, damned | of somebody, son, sin; and the world to the rich; and somebody knelt, this man, this heavenly servant, before this | Lord God

  1  somebody-servant and Lord servant exist debt^ ten_thousand talent
  2  and go this Lord_God-king this heaven^ servant and
  3  then somebody-servant-angel go-angel before this | Lord_God
  4  king before Lord Christ and somebody-servant begin
  5  ask this Lord_God-somebody-+king of-Lord | [forgave_the_debt]
  6  good-do and then Lord_God-king | commandment-love-have_mercy
  7  righteous-good-do not-to-°high take^ and_said
  8  this Lord_God-king sell angel-somebody be_damned | of
  9  somebody ~son sin and world ~rich-to and kneel-somebody
 10  this somebody this heaven^ servant before this | Lord_God

## 135r — the Unmerciful Servant

> A king, and the Lord God begins, prays [fellowservant] [a hundred pence] have the commandment to somebody's sin; would like, somebody, this Lord God, to have compassion. forgive the debt. And behold, the Lord God the king besought The servant of the Lord God the king humbled himself — the man-servant — and the man forgave, this Lord God the king; and the man forgave all, one our sin; and somebody went, the angel, our home. And then, as the man went on, the fellow-servant our home; and then came one | God the man, this man, the fellow-servant; and the man was in debt hundred pence; and the man of God began to demand it.

  1  king and Lord_God begin ~pray [fellowservant] [a_hundred_pence]
  2  have commandment to somebody-~sin would_like^ somebody this Lord_God have_compassion
  3  remit debt^ ~and see this Lord_God-king besought*
  4  ~humble this servant of-Lord_God-king somebody-servant and
  5  somebody forgive^ this Lord_God-king and somebody forgive^ every ~exist-+one
  6  our sin and somebody go-angel our
  7  home and then go_on-somebody this heavenly servant
  8  our home and then come one | God
  9  somebody this somebody heavenly servant and somebody exist
 10  debt^ hundred denarius and God-somebody begin ask

## 135v — the fellowservant cast into prison

> of the debt; and rather love he took; in turn he knelt down, the man of God, before this heavenly servant; and the servant began, prayed, [fellowservant] [a hundred pence], have the commandment | to the man of God; the man of God would, this man, the heavenly servant, have compassion forgive the debt; and the man of God release but God's somebody took [him] into prison; and God's somebody, until, from […] he bowed the head upon the scaffold; and saw this, sad, the other servant; this Lord God, the king, the angel, forgave. the one only Lord God; and the angel went, sorrowing, the angel, this this Lord God the king; and the Lord God the king said to the angel

  1  of-indebted and rather-love take^ but kneel God-somebody
  2  before this heavenly servant and somebody-servant
  3  begin ~pray [fellowservant] [a_hundred_pence] have commandment | to
  4  God-somebody want-God-somebody this somebody heavenly servant
  5  have_compassion remit debt^ and God-somebody release*
  6  but God-somebody take^ inside prison and God-somebody
  7  until-from bowed head inside scaffold and
  8  see this sad other servant this Lord_God-king angel forgive^
  9  one only Lord_God and go-angel sad-angel-this
 10  this Lord_God-king and Lord_God-king say angel

## 136r — the parable told a second time

> the Father of heaven, he who [is] king of all heaven [and] land, and on earth king of all. And then from forgiving, the servant believes in the Lord God, the one only Lord God [besought] This Lord God forgave. The Lord: ten thousand(?) talents appeared. One of God's somebody; and somebody was in debt a hundred denarii; and the man of God began to ask | for the debt, and rather with love he took him; in turn he knelt down, the man of God, before this heavenly servant; and the servant began, prayed, [fellowservant] [a hundred pence], have the commandment to God's somebody.

  1  the_father heaven he_who king every heaven land
  2  and on-earth every king and_said from forgive^ ~servant
  3  believe of-Lord_God one only Lord_God [besought]
  4  this Lord_God forgive^ Lord ten-?thousand talent appear.
  5  one God-somebody and somebody exist debt^ hundred
  6  denarius and God-somebody begin ask | of
  7  debt^ and rather-love take^
  8  but kneel-God-somebody before this
  9  heavenly servant and somebody-servant begin ~pray
 10  [fellowservant] [a_hundred_pence] have commandment to God-somebody

## 136v — he would not forgive, and the king was wroth

> The man of God would not, this heavenly servant, have compassion, forgive the debt, and release the man; but God's somebody took [him] into prison; and God's somebody, from house to house, bowed his head upon the scaffold. This king, the Lord Christ, grew angry, and went upon this heavenly servant; and the servant went to die, before the angel, before this king, before the Lord Christ, the one only the Lord God. And then this king, this servant forgave | of the Lord, the Father God; to hide that servant; like the Lord to; and the king — that servant: "Lord have mercy, Lord have mercy" — that servant.

  1  want-God-somebody this heavenly servant have_compassion
  2  forgive^ debt^ and God somebody release*
  3  but God-somebody grab inside prison and God-somebody
  4  to-house-from bowed ~head inside scaffold
  5  grow_angry this king Lord Christ and go on-this
  6  heavenly servant and servant go die angel before
  7  this king before Lord Christ one only
  8  Lord_God and_said this king this servant forgive^ | of
  9  Lord the_father God to-hide that_servant like Lord to and
 10  king that_servant have_mercy-Lord have_mercy-Lord that_servant

## 137r — the end of the reading

> Ten thousand talents. In turn this man, from the man of God [forgave thee] forgave: a hundred denarii. And the man took this king, the Lord Christ; and then took of the Lord the king evil, cast out the devil. And then this king, the Lord Christ, all of it, until this: that the man suffer [shouldst not thou] [had compassion] [even as I]; if the king, the debt of the sin somebody. And then this king, this is, forgave all somebody; and somebody did not forgive. Here ends this holy gospel.

  1  ten_thousand talent in_turn this-somebody from God-somebody [forgave_thee]
  2  forgive^ hundred denarius ~and somebody grab this
  3  king Lord Christ and then grab of-Lord-king
  4  evil exorcise devil = and_said this king
  5  Lord Christ every until-from this that somebody suffering
  6  [shouldst_not_thou] [had_compassion] [even_as_I] ~if king debt^ sin
  7  somebody and_said this king this exist every forgive^
  8  somebody and somebody not forgive^ here_ends this holy_gospel

## 137v — a prayer to the Virgin, with the author's colophon

> Hail, O Virgin. Through holy Mary, mother of God, gate into Paradise Queen Mary, heaven, wife, world; Mary ascends | this Mary, the one only Virgin Mary, you conceived Jesus without sin. Born of Mary, the Creator Lord; and from the Lord, the Redeemer, within the Lord | this N. [the author] we do not doubt, [author]; we […] | I, [author], somebody, you pray to, sin, | of N. [the author] that then our soul ascends, remitted | of N. [the author] somebody, the body. Amen. This prayer have. a hundred years, have mercy; healing, Mary; name high, have mercy; out, Mary | Lord

  1  healing-girl through holy-Mary mother God gate into_Paradise
  2  king-Mary heaven wife world ascend-Mary | this
  3  Mary one only Virgin_Mary you ~conceive Jesus without sin
  4  be_born-Mary Creator_Lord and from Lord-redeemer inside Lord | this-NAME.author
  5  somebody doubt_not-NAME.author-somebody believe | this-NAME.author
  6  somebody you pray to-~sin | of-NAME.author
  7  somebody then ascend soul remit | of-NAME.author
  8  somebody body amen this pray have
  9  hundred-year have_mercy healing Mary name-high have_mercy ~out-Mary | Lord

## 138r — the Hail Mary, twice

> … the divine one, you, divine one, blessed Mary, you among women; blessed Mary's son, he who went, the Lord, | from up, Mary's body. Jesus Christ. Amen. Healing, girl, through holy Mary, from, took the Virgin Mary. (An earlier printing read this as "Hail, maiden"; the signs read healing and girl here.) believe, this N. [the author], somebody, you are; N. [the author], somebody, through the mercy of the Virgin Mary; and is N. [the author], somebody [blessed art thou] [among women] this […] name, Mary; and within every hour; and | redeem Mary; N. [the author], somebody, in the year of wrath of Mary, through the year of wrath, through, wish, the son of Mary, our Lord Jesus Christ.

  1  DIV you-DIV blessed-Mary you ~among
  2  woman blessed-+SUBJ of-Mary son he_who go-Lord | from
  3  up of-Mary body Jesus Christ amen
  4  healing-girl through holy-Mary from grab-Virgin_Mary
  5  believe this-NAME.author-somebody you exist NAME.author-somebody
  6  through have_mercy-Virgin_Mary and exist NAME.author-somebody [blessed_art_thou]
  7  [among_women] this °sick-+name-Mary and inside every hour and | redeem
  8  Mary NAME.author-somebody grow_angry-~year of-Mary through grow_angry-~year
  9  through wish son of-Mary Lord our Jesus Christ

## 138v — Saint Augustine and the three Hail Marys

> Amen. This prayer has from [three] mercy. speaks the holy father, the church father, of the happy Virgin Mary, who [is] up: you are; ask Mary, from Mary the son, from the Lord Jesus Christ. Everyone who would take hold, says holy Augustine the church father. Saint Augustine prays this: three prayers [to] the happy Virgin Mary, on pleasing, on thanks. not; Saint Augustine: somebody has lost, ever ever; and on the cloud destroyed; and on three prayers many sins of a man are taken away, the sins of a man, in heaven

  1  amen this pray have from [three] have_mercy
  2  speak holy-NAME.father church_father from happy Virgin_Mary who up
  3  exist you exist ~ask-Mary from of-Mary
  4  son from Lord-Jesus-Christ every want grab speak
  5  holy-Augustine-church_father pray-+Saint_Augustine this
  6  three pray happy Virgin_Mary on-pleasing on-thanks
  7  not-+Saint_Augustine-somebody have lose ever
  8  ever and on-+cloud destroy and on-+three pray
  9  from many somebody-sin go-somebody-sin inside ~heaven

## 139r — Mary shows her breast

> land. Because, and somebody prays [to] the happy Virgin Mary every man is saved and goes not into the fire of hell; because the happy Virgin Mary every day, kneeling [to] Mary before of Mary | the son; she shows, of Mary, the breast, this breast, this of Mary, [that] he, the divine one, was nursed; believe. "the lost and damned man: have mercy, Christ" | "the man lost and damned." And whoever prays to the mother of Christ, every man is saved, and one is damned; but every man is saved, because a good servant, every [faithful] servant

  1  land because and somebody pray happy Virgin_Mary
  2  everybody = be_saved not-go on-hell fire because
  3  happy Virgin_Mary every day kneel-Mary before
  4  of-Mary | son show of-Mary
  5  breast this breast this-Mary he-DIV nurse believe
  6  the_man-+lost_and_damned have_mercy Christ | the_man*
  7  lost_and_damned and somebody pray mother Christ every
  8  somebody be_saved and one be_damned but everybody =
  9  be_saved because good servant every [faithful] servant

## 139v — the curse and the blessing

> speaks holy Moses [to] Aaron, Moses's brother: this people, the man, is cursed from every good. That is, somebody is not saved; in turn, and the man is merciful, righteous, to the poor man of God, and to our father's son as the man himself, ours. There is heaven land; in turn, and the man [who is] not finding mercy, righteous, to the poor man of God, and to our father's son, this man the Lord God wants cursed from every good; and all he has, that is, all his riches who [cursed] what the man has is damned, and the rich man cursed. This

  1  speak holy-Moses Aaron of-Moses brother
  2  exist this people man^ exist through cursed from every
  3  good that_is not be_saved-somebody in_turn and man^ exist
  4  have_mercy-somebody righteous-somebody poor_man_of_God = and to our
  5  the_father son as man^ himself our.
  6  exist heaven land in_turn and man^ not
  7  find_mercy^ righteous-somebody to poor_man_of_God = and to our
  8  the_father son this man^ want Lord_God cursed from
  9  every good be_saved and every have that_is every ~rich who
 10  [cursed] have-somebody be_damned-somebody and ~rich cursed this

## 140r — cursed be thy herd and thy field

> the man. Of the Lord the herd, cursed; of the Lord the field; then this somebody's harvest, field, cursed, [by] the Lord God, our mount; then this man's grape, harvest, mount. cursed, this somebody, [by] the Lord God, within our home. Not this somebody [barn] [stores]; somebody is damned, ever ever; into hell somebody falls; in turn, and somebody is | merciful, somebody righteous, somebody, to the poor man of God, this our father's son as somebody himself, this somebody. Blessed of the Lord the herd; blessed of the Lord the field; then the man's field, harvest, blessed;

  1  somebody Lord_God of herd cursed Lord_God of field
  2  then-this-somebody harvest field cursed Lord_God our
  3  mount then-this-somebody grape harvest mount.
  4  cursed this-somebody Lord_God inside our home
  5  not this-somebody [barn] [stores] be_damned-somebody ever
  6  ever inside hell somebody fall in_turn and somebody exist | have_mercy
  7  somebody righteous somebody to poor_man_of_God = this our
  8  the_father son as somebody himself this-somebody.
  9  blessed Lord_God of herd blessed Lord_God of
 10  field then-this-somebody field harvest blessed

## 140v — write it, and pray to the virgin Mary

> of the Lord God, the mount; then this man's mount, grape. Harvest blessed, this somebody, [by] the Lord God, and within our | home, in turn home and in every place [wide] the man is left, the man is saved, is, for ever and ever, amen. Writes, speaks: all the whole world, pleasing the Father; in turn the son of God the Father. Pray from the Virgin Mary, believe, to all [who] want the Lord the Father hears; all the whole world wants the Lord to [his] will do; and the Lord: whoever is righteous, believe, the man. This the apostles all wrote, because every man's sin somebody goes to the Virgin Mary; have mercy, asks somebody.

  1  Lord_God of mount then-this-somebody mount grape.
  2  harvest blessed this-somebody Lord_God and inside our | ~home-in_turn
  3  home* and every to-place [wide] leave-somebody be_saved-somebody
  4  exist for_ever_and_ever = amen write speak
  5  every all_the_world world pleasing the_Father in_turn son of-God_the_Father.
  6  pray from Virgin_Mary believe to every want Lord
  7  the_Father hear every all_the_world world want Lord to-+will
  8  do and Lord somebody exist righteous believe
  9  somebody this SUBJ apostle every write because everybody = sin
 10  go-somebody to Virgin_Mary have_mercy ask somebody.

## 141r — the fruit of Mary

> Because of this, pray to Mary: the fruit of Mary, the son, to all the whole world, because the Lord Christ did the commandment among somebody, among the Father of the Lord, because many. Have mercy, Lord Christ, on every man's sin, speaks the holy church father; then this man is, from many a man's sin, [narrow] left somebody, our Lord's creation, because this is. […] the Lord, sin, mercy [fruit]; this is within the commandment of somebody, that is; and somebody has to carry the commandment of God, | […] [bear] sin; somebody is saved, somebody, [through] many sufferings.

  1  because this from Mary pray of-Mary fruit son
  2  to-every all_the_world world because Lord Christ commandment do among
  3  somebody among the_Father of-Lord because SUBJ many.
  4  have_mercy Lord Christ to-every somebody sin speak holy-NAME.father
  5  church_father then this somebody exist from many somebody sin
  6  [narrow] leave-somebody our Lord-create because this_is.
  7  [...] Lord sin have_mercy [fruit] this exist inside commandment somebody
  8  that_is and have somebody carry commandment God | [...]
  9  [bear] sin somebody be_saved-somebody many suffering

## 141v — a woman in Rome

> for ever and ever, amen. Writes the name | of the man; in heaven and earth, until he dies; in turn upon die, the body and the soul, for ever and ever, amen. There was in Rome a woman, baptize, head, and then asked the woman in Rome father every day two, God, body. took, and fasted, half [forty days]; fasted; baptize, baptize. many years; and the woman would give thanks; this [Lady] fasted one [received]; and the woman took this holy host, and then

  1  for_ever_and_ever = amen write SUBJ name | of
  2  somebody inside heaven land until die in_turn | on
  3  die body and soul for_ever_and_ever = amen
  4  exist inside Rome one
  5  woman baptize head and
  6  then ~ask-+woman
  7  inside Rome [father]
  8  every day two God body
  9  grab and fast half* [forty_days] SUBJ fast ~baptize baptize
 10  many year and woman want thanks this [Lady] fast one
 11  [received] and woman grab this holy-host and then

## 142r — the woman who lived on the host

> The woman took, and shouted to; lost, died, the woman, baptize. and then carried the host; and then the woman, baptize, the host was. took in the place; hunger(?); left [nothing]; bread eat, the woman, baptize, many years [was fed]; the woman, baptize, fed. Christ in the high heavens, the Holy Spirit, spirit to spirit, from the woman; living […] half; there were two; the woman, baptize, head, within Rome; and then the woman, baptize, committed sin; the woman, baptize, out; of the woman, baptize, the Lord, thief, who did; and then the woman, baptize, cast out; the Lord, on the Lord's, had mercy; and went one sister. And then: oh, | of

  1  woman grab and shout-to lose die-+woman baptize
  2  and then carry host and then woman baptize host exist
  3  grab on-place hunger? leave [nothing] bread
  4  eat woman baptize many year [was_fed] SUBJ woman baptize feed
  5  Christ on-heaven high holy-spirit to-spirit from woman
  6  living-[?] half* exist two woman baptize head inside Rome
  7  and then woman baptize commit sin woman baptize out
  8  of-+woman baptize Lord thief-who do and then
  9  woman baptize exorcise Lord on-of-Lord have_mercy and
 10  go one sister and_said oh | of

## 142v — the woman fasts and takes the host

> The woman, baptize, the father, girl, if only this girl, wife, can do, how this woman can. The woman, baptize, went into mercy; the woman of the woman, baptize, the Lord; and then wanted to say this sister: to fast, the woman [prayed]; and God, body, carry the woman, within the woman's, baptize, mouth; and the Lord is God, body. Kissed the woman, baptize; the Lord wanted this woman, baptize; mercy is; and then the woman, baptize, to fast, and took God, body. And carried the woman, baptize, within the woman's, baptize,

  1  woman baptize the_father girl if_only this girl-wife can do
  2  how? this-+woman can woman baptize inside have_mercy go woman
  3  of-+woman baptize Lord and_said want say this sister
  4  to-fast woman [prayed] and God body carry
  5  woman inside of-+woman baptize mouth and Lord exist
  6  God body kiss woman baptize want-Lord this
  7  woman baptize have_mercy exist and then woman
  8  baptize to-fast and grab God body
  9  and carry woman baptize inside of-+woman baptize

## 143r — the face, the cloud, and the two grinding

> mouth; and the Lord wanted, to God, body. Kissed; and the woman, baptize, face beat on the place [cheek] out. God, body. And was a miracle, a farm; and the Lord God cried out, in the cloud, to the angel | of the Lord left. Oh, baptize, baptize, of the Lord, the father, the daughter, to love. The Lord is a miracle; the farm; the woman, baptize, has the woman, baptize, [suffered]; the woman, baptize, [patiently]; I this woman, baptize, […] the Lord, sin, mercy. And then this woman, baptize, in turn, grinding, one: you, Lord God, say

  1  mouth and Lord want to God body kiss
  2  and woman baptize face beat on-place [cheek]
  3  out God body and SUBJ exist ~miracle farm
  4  and shout-to Lord_God on-+cloud on-angel | of
  5  Lord leave oh ~baptize baptize of-Lord the_father daughter
  6  to-love Lord exist ~miracle farm woman baptize have
  7  woman baptize [suffered] woman baptize [patiently] I
  8  this woman baptize [...] Lord sin have_mercy and_said
  9  this woman baptize in_turn grinding-+one you Lord_God say

## 143v — crucified, and the sin that dies

> the Lord God in the cloud to the angel of the Lord: I from Jesus; | and the Lord crucified. And then this wife: Lord of the wife, Lord God, of the wife have mercy, to, baptize, baptize, who, this wife, committed sin against the Lord's, could. And then the Lord God: I this woman, baptize, sin: have mercy, Lord, [forgive], Lord, on sin. [cloud] This says the Son of God, the king of the high year; wanted the Lord, heaven, earth [shall pass away], than one. A man's sin dies; that is, damned […] the man damned. The Lord God, in turn: this man to the Lord, among the Lord

  1  Lord_God in_the_cloud on-angel of-Lord I from Jesus | and-Lord
  2  SUBJ crucified and_said this wife Lord of-wife Lord God
  3  of-wife have_mercy to-~baptize baptize who this-wife commit sin
  4  against of-Lord can and_said Lord_God I this
  5  woman baptize sin have_mercy Lord [forgive] Lord on-sin
  6  [cloud] this say SUBJ son God high-~year-+king want Lord
  7  heaven earth [shall_pass_away] than one
  8  somebody sin die that_is be_damned to-+little somebody
  9  be_damned Lord God but this somebody to-Lord among Lord

## 144r — Saint Augustine, and an image of the Virgin

> heavenly people, somebody, to the Lord God: I, you […] of the Lord, the sin, the mercy, […]; this must the man carry: the commandment of God; saved, somebody, [through] many sufferings. For ever and ever, amen. Writes | holy Saint Augustine: there was one woman and [a] Lady prayed [to] the happy Virgin Mary, on out, three years. In […] there was an image | of the virgin Mary; and then [knelt before] this image | of the virgin Mary; and said this: Lady, hear, Lady; and somebody

  1  heavenly* people somebody to-Lord_God I you [...]
  2  Lord sin have_mercy seal-from this have somebody carry
  3  commandment God be_saved somebody many suffering
  4  for_ever_and_ever = amen write SUBJ | holy
  5  Saint_Augustine exist one woman and Lady
  6  SUBJ pray happy Virgin_Mary on-~out three
  7  year inside mount exist one image | virgin
  8  Mary and then [knelt_before] this image | virgin
  9  Mary and say this Lady hear-+Lady and somebody

## 144v — thou who holdest heaven and earth

> pray [to] the Virgin Mary; wanted somebody: good queen, [who] took heaven and earth" — this Lady would, the Lady, pray. And she served one day; then Mary, every day, took bread, and [ate] truly, half year. then, the year out, within time, went this woman [to] this image of the Virgin Mary, and said this woman: | Lord, […] thou who holdest heaven and earth, Lady, | virgin Mary." This Lady spoke from thence; and two said; the girl said:

  1  pray Virgin_Mary want-somebody good queen grab heaven
  2  land this-+Lady want-+Lady pray
  3  and servant one day then Mary every day
  4  grab bread and [ate] righteous half-~year
  5  then year ~out inside time go this woman
  6  this image Virgin_Mary and say this woman | Lord
  7  queen grab heaven land Lady | virgin
  8  Mary this-+Lady from speak and two say girl say

## 145r — how shall we creatures speak?

> queen, [who] took heaven [and] land, Lady Virgin Mary. This Lady, from speaking, how? how shall we, tree, speak? can speak? said this woman, this woman, [said to] love: this Mary wanted; and then Mary, woman, served, fasted, and prayed two Hail Marys, and truly at the year's beginning bread; and [ate], took; and then, out, two years, within time, went this woman [to] this image of the Virgin Mary, and said this woman: queen, [who] took heaven [and] land, Lady Virgin Mary.

  1  queen grab heaven land Lady Virgin_Mary
  2  this-Lady from speak how? how_shall_we* tree speak
  3  can speak say this woman this-woman
  4  [said_to] love this Mary want and then Mary woman
  5  servant fast and two Hail_Mary pray and righteous begin-~year
  6  bread and [ate] grab and then
  7  ~out two-year inside time go this woman this
  8  image Virgin_Mary and say this woman queen
  9  grab heaven land Lady Virgin_Mary

## 145v — three days, three Hail Marys

> This Lady from speaking; and two said this woman: queen, [who] took heaven [and] land, Lady Virgin Mary. The Lady prayed this to Mary, outwardly, fasting, fasting. The girl, the Lady: "Queen, thou who holdest heaven and earth" — this girl, the Lady, spoke; this woman [said to] love: you want; and then Mary, woman, servant, three days out; and three Hail Marys she prayed; and truly at the year's beginning, bread; and [ate], took; and then out. three days, within time, went this woman [to] this image of the Virgin Mary, and said this woman: queen, [who] took heaven

  1  this-+Lady from speak and two say this woman queen
  2  grab heaven land Lady Virgin_Mary
  3  pray Lady this Mary on-~out fast fast
  4  girl Lady queen grab heaven land
  5  this-girl Lady speak this-woman [said_to] love
  6  you want and then Mary woman servant
  7  on-out three_days and three Hail_Mary pray and righteous begin-~year
  8  bread and [ate] grab and then out.
  9  three_days inside time go this woman this image
 10  Virgin_Mary and say this woman queen grab heaven

## 146r — the Lady speaks from the image

> land, Lady Virgin Mary. This Lady from speaking; and two said this woman: queen, [who] took heaven, | town is, Lady Virgin Mary. This Lady from speaking. This woman grew angry; remit; went the Lady, of the Lady the Lord said, this woman, this Lady; and the Lady went. Forgive, this Lord. The Lady prayed, and the Lady served the Virgin Mary, on out, three days; this girl, the Lady: queen, thou who holdest heaven and earth" — this Lady; and | went Lady. Remit, this Lord said, this woman, he.

  1  land Lady Virgin_Mary this-+Lady from speak
  2  and two say this woman queen grab heaven | town
  3  exist Lady Virgin_Mary this-+Lady from speak
  4  grow_angry this woman remit go-+Lady of-+Lady
  5  Lord say this woman this-+Lady and go-+Lady
  6  remit this Lord pray Lady and servant Lady
  7  Virgin_Mary on-out three_days this-girl Lady queen
  8  grab heaven land this-+Lady and | go
  9  Lady remit this Lord say this woman he

## 146v — the nail, and the Virgin in the image

> The Lady went from the Lord; I; this Lady the Lord wanted in the place. The girl: "Queen, thou who holdest heaven and earth" heavenly this woman, of the Lady, the Lord; and the Lady took this Lord, one [a candle] [lit] upon the piercing. And one [placed] [before it]; and the Lady went, this, | from the woman; and then […] went the Lady, this woman; and many went. | In time appeared the Lady, the Virgin Mary, within the image; the woman, baptize. And then happy the Virgin Mary took the woman, baptize, to this | [a candle]

  1  go-+Lady from-Lord I this-+Lady want-Lord on-place
  2  girl queen grab heaven land heavenly*
  3  this woman of-+Lady Lord and Lady grab
  4  this Lord one [a_candle] [lit] on-pierce and.
  5  one [placed] [before_it] and go-+Lady this | from
  6  woman and then-[?] go-+Lady this woman
  7  and go many | inside time appear
  8  Lady Virgin_Mary inside image woman baptize and_said
  9  happy Virgin_Mary grab woman baptize to this | [a_candle]

## 147r — the son, and the king

> [candle] from the son, in the name of the Virgin Mary, said this woman, this Lady; the girl prayed; and servant, Lady Mary, on out, three; this woman: queen, [who] took heaven and earth" — Mary took the girl, the Lady; this son the Lady would, the son, to this [a candle] put | and take; the girl, the Lady, the son; in turn the Lady took one know. And then the Virgin Mary went, the Lady, up to the king; and the king took the Lady, this know; and who this Lady said, king, living, the Lady did.

  1  [candle] from son inside name Virgin_Mary say this
  2  woman this-+Lady pray girl and servant Lady
  3  Mary on-~out three this-woman queen grab heaven
  4  land Mary grab-girl Lady this son
  5  want-+Lady son to this [a_candle] put | grab
  6  girl Lady son but Lady grab one
  7  know* and_said Virgin_Mary go-+Lady to-up king
  8  and king grab Lady this know* and who
  9  this Lady say ~king living-exist Lady do

## 147v — the Virgin seen by all the people

> And then the Lady went to this king; and from seeing the king this know; and took [led away] this woman; and | then there were Pharisees; they left the Lady; and then the Lady, the heavenly host say served the Lady. In time appeared the Lady, happy Virgin Mary, within the image; the woman, baptize, on all the people seen. And then happy the Virgin Mary [to] this woman: this is. This Lady, like, loved the girl, | this Mary; this Lady, the man did, the girl. the Lady is good; the Lady not derided; in turn

  1  and then go-+Lady this king and from see-~king
  2  this know* and grab [led_away] this woman and | then
  3  exist Pharisees* leave Lady and then Lady heavenly
  4  host say servant Lady inside time appear
  5  Lady happy Virgin_Mary inside image woman baptize
  6  on-every people see and_said happy Virgin_Mary this
  7  woman this_is this Lady like love-girl | this
  8  Mary this Lady somebody do girl
  9  exist-+Lady good Lady not °derided-~exist in_turn

## 148r — Adam went down to Jericho

> the Lady is derided; she was lost, this Lady; and left. Happy the Virgin Mary, before, remitted the people. It is written of Adam. The son, Seth. And this is the word. It is written: Adam went, one man, to Jerusalem, into the town of Jericho; and then, and Adam went into the field; and then came one deer; and then Adam a year of chapters [fell among] a deer in the field; and then

  1  exist-+Lady °derided-~exist lose this Lady and
  2  leave happy Virgin_Mary before remit people.
  3  write Adam.
  4  son Seth.
  5  and this word.
  6  write go-~Adam
  7  one man^ on-Jerusalem
  8  inside Jericho town
  9  and then and go ~Adam on-~field and then.
 10  come one deer and then ~Adam
 11  chapter-year [fell_among] deer on-~field and then

## 148v — the man in the pit, and the two mice

> Adam escaped across the field, and then Adam | bowed down the man into a pit; and then hang cling the man onto a tree, because there was a branch sticking out [outgrow]; and there came two mice, one black, the second white; and this tree, half, two mice to eat. And then the man saw, and to the man he saw a dragon, and which cried out to the man: the man is lost [in the well] if Adam goes up, this Adam, this | can

  1  escape ~Adam on-~field and then ~Adam | bow_down
  2  ~Adam inside one pit and then hang
  3  cling ~Adam on-one tree because exist
  4  protrude [outgrow] and go two mouse one black
  5  second white and this tree half two mouse
  6  to-eat and then see ~Adam to-~Adam
  7  and see one dragon = and
  8  who-shout-to ~Adam lose-~Adam [in_the_well]
  9  if up go-~Adam this ~Adam this | can

## 149r — the lance of the soldier

> the evil dies, if cling the man bows down to this. The dragon rends the man; and then the man [blind] through startled the man, and | he went to the dying Lord Christ; one soldier of the Lord Jesus Christ who died [pierced the side] [his] suffering; and this | can evil, on half, through [the death of the Lord Christ] and the man took hold of this soldier of Christ who died, the chapter | of the soldier of the Lord Jesus Christ who died: suffering, lance. And then this soldier of the Lord Jesus Christ who died: Adam escaped on this

  1  evil die if cling bow ~Adam this.
  2  dragon = ~Adam rend and then ~Adam
  3  [blind] through startle ~Adam and | go-die-Lord
  4  Christ one soldier-Lord-Jesus-die-Christ [pierced_the_side]
  5  [his] suffering and this | can
  6  evil on-half through [the_death_of_the_Lord_Christ] and
  7  ~Adam grab this soldier-[?]-die-~Christ-chapter | of
  8  soldier-Lord-Jesus-die-Christ suffering lance and_said
  9  this soldier-Lord-Jesus-die-Christ escape-~Adam on-this

## 149v — pulled out of the pit

> the pit; the man was scattered, and then the man was with the Lord; the Lord took the suffering [and] lance of the soldier of the Lord Jesus Christ who died. and the man out of this pit, the chapter of the soldier of Christ who died, took. And then this soldier of the Lord Jesus Christ who died: then this Adam not out, the Lord took, on this pit there was the man inside this pit; and the man died, because | this man, this deer dies, that is, he is damned. There is, there is a man [is baptized] who is saved. the man; God is [baptized] [not] the man saw

  1  pit scatter ~Adam and then ~Adam exist-Lord
  2  grab-Lord of-soldier-Lord-Jesus-die-Christ suffering lance
  3  and ~Adam ~out this pit soldier-[?]-die-~Christ-chapter
  4  grab and_said this soldier-Lord-Jesus-die-Christ then
  5  this-~Adam not out grab-Lord on-this pit exist
  6  ~Adam inside this pit and die-~Adam because-exist | this
  7  ~Adam this deer die that_is be_damned
  8  exist exist ~Adam [is_baptized] be_saved.
  9  ~Adam God-exist [baptized] [not] see ~Adam

## 150r — a certain man had two sons

> writes the church father, pagan; first writes [a certain man] | on this this writes the church father, the church father [two sons]; after these writes [the younger]; the church father, after these, writes the church father the Pharisees; and the church father [the gospel] the gospel: there was one man, and then this man had one. son; and this son was three; sold | redeemed the man; and the son, four, wanted; the man could the son redeemed; and then the son went, cast out [divided] among; this son, of the son, the father said this

  1  write church_father pagan first write [a_certain_man] | on-this
  2  this write church_father church_father [two_sons] after_these write
  3  [the_younger] church_father after_these SUBJ write church_father
  4  Pharisees* and church_father [the_gospel] gospel exist one
  5  man^ and then have man^ one.
  6  son and this son exist three sell | redeem
  7  man^ and son two-two want-somebody can
  8  son redeem and then son go exorcise
  9  [divided] among this son of-son the_father say this

## 150v — the father kissed him

> son; oh, of the son, the father: the father kissed the son on this last year; and then the son, the father kissed; and cursed [ran]. And then, that is, the father was [fell upon his neck]; darkness? then this father was, father, son, apostle, on good, not this son upon this went, to the son, in love the son went, speaking, baptize the church father, our church father, on [his] brother, by name Saint Augustine the church father spoke, the brother of Saint Augustine; and the man believes in the Lord Jesus Christ; somebody has this, ours. the son, on good, the apostle: how you, the good man.

  1  son oh of-son the_father kiss son father on-this
  2  last year and then son father kiss and cursed
  3  [ran] and_said that_is father exist [fell_upon_his_neck] darkness?
  4  then this-father exist father son apostle on-good not
  5  this-son on-this go-~son on-love son go-~son speak-~baptize
  6  church_father our church_father on-brother-+name Saint_Augustine_the_church_father
  7  speak ~brother of-+Saint_Augustine and somebody believe
  8  inside Lord-Jesus-Christ have-somebody this our.
  9  son on-good apostle how? ~you good-somebody.

## 151r — for the good, to the father

> you; the father, on good, the apostle, the father, this; and you the man, our son, on good, the apostle, this somebody, so that seal; and the son, not somebody, this, on good, our apostle the son wants […] from you, on the birth, the rest the son's sin; and the son's sin, you are, you light upon you: take the forgiveness of sins, and you. Cursed [ran], the son's sin, on doomsday, said the Lord God, holy Hezekiah, the prophet, to the angel of the Lord; Hezekiah the king was; the man had three born from whosoever; and from three born

  1  ~you the_father on-good apostle-father this and you
  2  man^ our son on-good apostle-this-somebody so_that^
  3  seal* and son not-somebody-this on-good apostle our
  4  son want-[?] from ~you on-~be_born the_rest^
  5  ~son-sin and son-sin you exist you
  6  light on-you grab-+forgiveness_of_sins and you.
  7  cursed [ran] ~son-sin on_doomsday say Lord_God holy-Hezekiah
  8  prophet on-angel of-Lord Hezekiah exist man^ have
  9  three on-be_born from whosoever* and from three on-be_born

## 151v — the forgiveness of sins

> not was […] and has; but there is the son's sin; remit you, light, to leave; then not somebody sees the light, and there is the forgiveness of sins for you; go to the forgiveness of sins within the image [likeness] created; how one Lady the forgiveness of sins; and there is the forgiveness of sins, […] the forgiveness of sins our son; the forgiveness of sins [to] you, son; the second, and the son, from whosoever, the son, in turn, girl and on the son, girl, [not] somebody is damned; if, and the son, girl, not somebody, the apostle, on good; and on the son, girl, is damned | in turn

  1  not ~exist-[?] and have but exist ~son-sin remit
  2  you light to-leave then-not somebody see light and
  3  exist forgiveness_of_sins to you go-+forgiveness_of_sins
  4  inside image [likeness] create how? one Lady
  5  forgiveness_of_sins and exist-+forgiveness_of_sins [?]-+forgiveness_of_sins
  6  our son forgiveness_of_sins you son
  7  second and SUBJ son from whosoever* son in_turn girl
  8  and on-son girl [not] somebody be_damned if and son girl
  9  not somebody apostle on-good and on-son girl be_damned | in_turn

## 152r — saved or damned, and the litany

> if the son, girl, is somebody, apostle, on good; is somebody saved; not somebody is damned; somebody, the third son; and from whosoever this our good deed [penance] do; this the man can do, | upon out of darkness into the light goes the man of the Lord God; love the Lord God; have mercy, Lord God; righteous, Lord God; hope, Lord God; every our [with his whole heart] Lord God; every our virtue, the apostle, Lord God; our fast, Lord God; our repentance until carry, Lord God; our belief,

  1  ~if son girl exist somebody apostle on-good exist somebody
  2  be_saved somebody not somebody be_damned somebody third
  3  son and SUBJ from whosoever* this our good_deed =
  4  [penance] do this somebody can do | on
  5  darkness out on-light go-somebody Lord_God SUBJ love Lord_God
  6  SUBJ have_mercy Lord_God SUBJ righteous Lord_God SUBJ hope Lord_God
  7  SUBJ every our [with_his_whole_heart] Lord_God SUBJ every our virtue^
  8  apostle Lord_God SUBJ our fast Lord_God SUBJ our
  9  repentance until carry Lord_God SUBJ our believe

## 152v — God be merciful to me a sinner

> Lord God; every good deed, Lord God; our good life, for ever and ever, within heaven land. in the gospel a man speaks the Lord Christ, the son of the Lord and then a man went into the temple. And the man knelt down inside. In the temple every man has this; he said to the Lord: thanks, Lord God, godfearing it is, of the Lord; holy mercy, have mercy on the sinner because this is he who repents; every sinner, to the Lord, thanks

  1  Lord_God SUBJ every good_deed = Lord_God SUBJ our
  2  good living for_ever_and_ever = inside heaven land
  3  inside gospel man^ speak
  4  Lord-~Christ son of-Lord
  5  then go man^
  6  inside temple and.
  7  kneel-somebody inside.
  8  temple everybody = have this say to-Lord thanks Lord_God
  9  godfearing^ exist of-Lord holy-have_mercy have_mercy somebody-sin
 10  because this who repentance every somebody-sin to-Lord thanks

## 153r — Lord, remember me

> Lord God, find mercy, the sinful man. Holy John speaks: how from the thief; and Christ was crucified, and the thief; and then the thief going on, who from the year, the Lord Jesus, in the place recognized that Lord Jesus righteous, the son of God, because he is; out, the thief, the Holy Spirit find mercy; and shouted to [him] on the cross: Master | ask the thief; this thief: he, remember [him], on the thief. then [when] the Lord goes into the Lord's kingdom. And then this [was] the rest thief; and there was the Lord, the thief crucified. [remember me] this [thy kingdom]; then he loves | can

  1  Lord_God find_mercy^ man^ sin speak holy-John how?
  2  from thief and Christ crucified thief and then thief
  3  on-go who-from-~year Lord-Jesus on-place recognize that Lord-Jesus
  4  righteous son God because-exist ~out thief holy-spirit
  5  find_mercy^ and shout-to on_the_cross Master | ask
  6  thief this-thief he remember on-thief
  7  then go-Lord inside of-Lord kingdom^ and_said
  8  this the_rest^ thief and exist Lord thief crucify.
  9  [remember_me] this [thy_kingdom] then he love | can

## 153v — today shalt thou be in paradise

> the Lord; he is to the Lord [to] redeem; and the thief, the thief, one Lord and shouted to [him], this thief, first: he righteous the man; the other thieves, these die; they deserve it and turned toward the Lord Jesus, the head of the Lord, to the thief And then the Lord Jesus: believe, the Lord, believe, the day until wherefore hidden; the thief is [said to the Lord] before, in Paradise and one said, from the thief: how shall we | upon the thief, the last year, heaven and earth it is written, in the days of Moses, righteous [due reward]

  1  Lord he exist to-Lord redeem and thief thief one-Lord
  2  and shout-to this thief first he SUBJ righteous
  3  man^ the_rest^ thief-thief this die from deserve
  4  and turn_to Lord-Jesus of-Lord head to-thief
  5  and_said Lord-Jesus believe the_Lord believe* day^ until
  6  why?-hide exist-thief [said_to_the_Lord] before inside into_Paradise
  7  and one say from thief how_shall_we* | on-of
  8  thief last year-heaven kingdom^
  9  write SUBJ inside Moses-~year righteous [due_reward]

## 154r — the fire of purgatory

> from [the] withered, the fire of purification, rather than hell [torment] the year [after] the soul goes out, into purification; this soul, joy because the soul goes before the face of the Lord Jesus Christ. The end this holy gospel. […] the world, one year redeemed, a hundred years suffering; heaven land; second way there is a man, for one day of repentance | atonement the man inside the fire of purification, a hundred years for one day in turn; and the man, righteous, to fast and repentance | atonement somebody, our heaven land, and

  1  from-°withered purification fire but_rather* hell [torment]
  2  ~year-to [after] soul go out on-purification this soul joy
  3  because go-soul before from face Lord-Jesus-Christ end
  4  this holy-gospel [?]-world one year redeem hundred-year
  5  suffering heaven land second way
  6  exist somebody to one day repentance | atone
  7  somebody inside purification fire hundred-year to-one
  8  day in_turn and somebody righteous to-fast and repentance | atone
  9  somebody our SUBJ heaven land and

## 154v — the captive and the king

> this man, repentance, leave; because the man, the righteous man the suffering of the Lord Christ; and the man | is saved. somebody, for ever and ever, amen. The Lord God, be loved. wrote holy Elijah the prophet and holy Luke. And then he was taken prisoner, the robber, the baptized son one, from the world's king, and and then it is written, this baptized son, of […] the father, the world's king; then the baptized son redeemed

  1  this somebody repentance leave because somebody SUBJ righteous-somebody
  2  suffering Lord-Christ and somebody | be_saved.
  3  somebody for_ever_and_ever = amen Lord_God be_loved
  4  write holy-Elijah prophet
  5  and holy-Luke.
  6  then capture
  7  robber ~baptize-son
  8  one from-world-~king and
  9  then write this ~baptize-son of-[?]
 10  the_father-world-~king then ~baptize-son redeem

## 155r — held in bondage

> from the world's king, on bondage; and the baptized son cannot out [of] [bondage]; this humble, this baptized son; and sadly the baptized son left; and then [was afraid] this robber, the daughter, at the building, the daughter inside one house; and then for many years he led her out. this robber on this house; and then | the daughter believed; the believing daughter went out, home and then the believing daughter went home, this from […] the baptized son; and the believing daughter began to […]

  1  from-world-~king on-bondage and ~baptize-son cannot
  2  out [bondage] this humble this ~baptize-son and
  3  sad ~baptize-son leave and then [was_afraid]
  4  this robber daughter on-to-+building daughter inside
  5  one house and then many year out lead.
  6  this robber on-this house and then | daughter
  7  believe out go-daughter-believe to-home
  8  and then go daughter-believe to-home this from-[?]
  9  ~baptize-son and begin-daughter-believe to-[?]

## 155v — he could not buy him back

> speak; and the daughter could not speak, because there was sad, the baptized son on this, of […], the father, the world's king who, the baptized son, cannot redeem; and | went away the believing daughter from the baptized son; and then the believing daughter, and the two, the believing daughter went; then the baptized son, good, all the world; and then to […] | the daughter believed, and began to talk; and the believing daughter, spoke to […], said to […] this. From the world's king: if, how shall we [do]? The daughter believes; | redeem the daughter.

  1  speak and cannot daughter speak because exist
  2  sad ~baptize-son on-this of-[?] the_father-world-~king
  3  who ~baptize-son cannot redeem and | go_away
  4  daughter-believe from* ~baptize-son and then
  5  daughter-believe and two go-daughter-believe then
  6  ~baptize-son good all_the_world and then to-[?] | daughter
  7  believe begin_to_talk and daughter-believe.
  8  speak to-[?] say to-[?] this.
  9  from-world-~king if how_shall_we* daughter-believe | redeem-daughter.

## 156r — how shall she be ransomed

> believe, to […] this bondage, said this | daughter believing; how is this believing daughter to be ransomed? this bondage before the daughter's belief | the father the world's king, evil. And then this daughter, believing, this robber if the believing daughter wants […] to take | this to […] the […] son, the wife | this daughter believing, this […] the believing daughter wants redeem this bondage; said this to the son's son, this from the world's king, this […] wants […]

  1  believe to-[?] this bondage say this | daughter
  2  believe how?-exist this-daughter-believe redeem-daughter-believe
  3  this bondage before of-daughter-believe | the_father
  4  world-~king evil and_said this daughter-believe this robber
  5  if daughter-believe want-[?] grab | this
  6  to-[?] [?]-son wife | this-daughter
  7  believe this-[?] want-daughter-believe
  8  redeem this bondage say this to-son-son this
  9  from-world-~king this-[?] want-[?]

## 156v — the escape by night

> this believing daughter has the […] son as husband and then this time; and then the believing daughter to […] in the night | fled, the daughter believing […]; and the rich | carried away the daughter believe […] who | the daughter believes to […] the rich could carry; and then […] to […] | to the woman son, the father, the world's king; and | […] daughter believing, saw; and went, this of the […]

  1  this-daughter-believe have [?]-son wife
  2  then this time and then daughter-believe
  3  to-[?] inside night | escape-daughter
  4  believe-[?] and ~rich | from-carry-daughter
  5  believe-[?] who | daughter-believe
  6  to-[?] ~rich can carry and then
  7  [?]-to-[?] | to-of-+woman
  8  son the_father-world-~king and | [?]-daughter
  9  believe see and go this of-[?]

## 157r — the virgin daughter

> the father, the world's king; and sad left the father […]; and then to […] the believing daughter went to […] | to of […], the father […]. And then this from […] oh, of […], to […], wish, from […] love went to […] | judged from […] | this to […], as this virgin, the daughter, believes, said this to […]: this is the believing daughter, from the robber he who is to […], the robber taken prisoner said this from […]: as this daughter believes, this woman

  1  the_father-world-~king and sad leave-father-[?] and then
  2  to-[?] daughter-believe go-to-[?] | to
  3  of-[?] the_father-[?] and_said this from-[?]
  4  oh of-[?] to-[?] wish from-[?]
  5  SUBJ love go-to-[?] | judge from-[?] | this
  6  to-[?] as this virgin-daughter-believe say
  7  this to-[?] this_is daughter-believe from robber
  8  he_who exist to-[?] capture-+robber
  9  say this from-[?] as this-daughter-believe this woman

## 157v — she is led before the Father

> The believing daughter eloped; led before the Father | of the daughter the Lord Christ. This is the daughter who believes in the Lord Christ, in unbelief [the mother] of the daughter of the Lord Jesus Christ, the Father; and said this | the daughter of the Lord Jesus Christ, this from […], [named] this daughter of the Lord Jesus Christ, believing within unbelief [the mother] of the daughter of the Lord Jesus Christ, believing | from God the Father, because the Father, of the daughter of the Lord Jesus Christ, the wealth she has; remit, the man, [talent] [asked]; in turn | then was this, from the world's king; was every […] rich | sold from […] not is, to […]: how shall we | from

  1  elope-daughter-believe lead before the_Father | of-daughter
  2  Lord-Christ this_is daughter-Lord-Christ-believe inside not_believe
  3  [the_mother] of-daughter-Lord-Jesus-Christ the_Father and say this | daughter-Lord
  4  Jesus-Christ this from-[?] [named] this-daughter-Lord-Jesus-Christ-believe
  5  inside not_believe [the_mother] of-daughter-Lord-Jesus-Christ-believe | from
  6  God_the_Father because the_Father of-daughter-Lord-Jesus-Christ wealth
  7  have remit man* [talent] [asked] in_turn | then
  8  exist this-from-world-~king exist every of-[?] ~rich | sell
  9  from-[?] not exist to-[?] how_shall_we* | from

## 158r — the buying and the selling

> buy this, in turn; and then to […] he wanted from […] redeem this; is, is, from God, seal, from […] for ever and ever; said this from […] of […] to […] this […] this | the daughter of the Lord Jesus Christ who believes, […] took | to scatter every one of […] the rich; and said this to […] of […] the father […] | this to […] this daughter of the Lord Jesus Christ, believing | wanted

  1  buy-this in_turn then to-[?] want-from-[?]
  2  redeem-this exist exist from God-?seal from-[?]
  3  for_ever_and_ever = say this from-[?] of-[?]
  4  to-[?] this-[?] this | daughter-Lord-Jesus
  5  Christ-believe son* grab | to
  6  scatter every of-[?] ~rich and say this
  7  to-[?] of-[?] the_father-[?] | this
  8  to-[?] this daughter-Lord-Jesus-Christ-believe | want

## 158v — a wife, and the end of it

> to […] took; and then this time | to the woman the son, righteous, a wife; and the […] son, righteous. until the Lord's daughter, Jesus, believing, Christ, and | the woman wanted the son of the daughter of the Lord Jesus Christ, believing, living [happily] was. God, all the world, for ever and ever, amen. The Lord God, be loved. Before the Word, written by holy Luke, in the fourth chapter | of the writing; the time | then the Lord Jesus was, in the thirtieth

  1  to-[?] grab then this time | to-of-+woman
  2  son righteous wife and [?]-son righteous.
  3  ~until Lord-daughter-Jesus-believe-Christ and | want-+woman
  4  son-daughter-Lord-Jesus-Christ-believe living [happily] exist.
  5  God all_the_world for_ever_and_ever = amen Lord_God be_loved
  6  before Word^ write
  7  holy-Luke inside two-two chapter | of
  8  write time | then
  9  exist Lord-Jesus inside thirty

## 159r — two men with spirits

> and second year; the time; the Lord Jesus went to the shore; bread and then the Lord Jesus met the shore of the sea one hundred pigs; and then [he] met the Lord Jesus, the shore of the sea, among one mountain, two men with spirits; in the two men there were | six thousand and six hundred and sixty and six devils; and how two men, created, found two somebodies; these created two men aforesaid [tombs]; in turn [possessed] the two men were, to take | the Lord

  1  two-year time go Lord-Jesus shore bread
  2  and then meet^ Lord-Jesus shore sea
  3  one hundred pig and then meet^
  4  Lord-Jesus shore sea among one
  5  mount two somebody-spirit inside two man^ exist | six
  6  hundred and six_hundred* and six-ten and six devil = and how?
  7  two man^ create find-two-somebody this create two man^
  8  aforesaid [tombs] in_turn [possessed] exist two man^ to-grab | Lord

## 159v — the devils ask to be sent into the swine

> Jesus Christ; and the two men went to the Lord Jesus, and began two somebodies shouted to [him]: Master [torment]; and the Lord went before the time; he loved the two men; the devils' suffering, the Lord, all died of many sufferings; and the two men began the devils to ask, into the leftover food(?); and then [from] the two somebodies the devils were chased by the Lord Jesus into the leftover food(?), because, name, sat, year the Lord Jesus scattered them from the leftover food(?) in turn from two somebodies the woman, baptize, spirit; the Lord God redeemed.

  1  Jesus Christ and go two somebody to-Lord-Jesus and begin
  2  two somebody shout-to Master [torment] and Lord go before
  3  time love two somebody devil^ suffering Lord all^
  4  die from* many suffering ~and begin two somebody
  5  devil^ ask inside leftovers food? and
  6  then two somebody devil^ exist chase
  7  Lord-Jesus inside leftovers food? because name-°sat-~year
  8  Lord-Jesus from leftovers food? scatter
  9  in_turn from two somebody woman baptize spirit redeem Lord_God

## 160r — the herd runs into the sea

> and then he saw this, the shepherd, and through startled, and fled to the herdsmen's home and said the shepherd: the Lord seen of the shepherd. And then they went from the Lord […] saying: Jesus of Nazareth. And every aforesaid herd of the herdsmen perished in the sea; the Lord humble, the Jews; and sad [they] left […]. End [of] this apostolic holy gospel. This holy gospel begins, written by holy Luke in the fourth chapter of the writing; the time the Lord Jesus sat by the sea; then, in his thirty-second year

  1  and then see he this shepherd and through
  2  startle and escape to-of-shepherd home
  3  and say shepherd Lord-see of-shepherd and_said
  4  go-from-Lord [?]-from say Jesus Nazareth and every
  5  aforesaid of-shepherd herd inside sea perish^
  6  Lord ~humble-Jews and sad leave-[?] end this
  7  apostle holy-gospel here_begins this holy_gospel write holy-Luke
  8  inside two-two chapter of-write time sit Lord-Jesus
  9  on-sea then inside thirty two-year

## 160v — the Lord returns to Capharnaum

> Within, there was one of the Lord God, and through [preached] the Lord Jesus into one land [Capharnaum] within one town [was in the house] the home; and then the Jews saw the Lord Jesus go, and the Jews began to shout to [him] [the palsy]; and the Lord went; he wanted, the Lord, the Jews from high, of the Jews' rich [the roof] he made ready, and the Lord Jesus returned | into the middle of the Lord's town; and this town | name was Capharnaum; and took to himself three apostles, Peter and Paul and

  1  inside one ~exist Lord_God and through [preached] Lord-Jesus inside
  2  one land [Capharnaum] inside one town
  3  [was_in_the_house] home and then see-Jews go-Lord-Jesus
  4  and begin-Jews shout-to [the_palsy] and go-Lord
  5  he want-Lord Jews from-high of-Jews ~rich [the_roof]
  6  prepare and-Lord return Lord-Jesus | inside-and
  7  amid-inside of-Lord town and this town | and
  8  name exist Capharnaum and grab
  9  to-Lord three apostle Peter and Paul and

## 161r — the paralytic, and the four who carried him

> John; because then the Lord Christ would do a miracle, and every miracle the Lord had to confess; and then | he preached, the Lord, in Capharnaum; and many people followed the Lord, and then […] carried one ill before the Lord Jesus, within | a man, four men, at the head. Among them: faith, love, hope, forgiveness; and | they could not the four bearers within, but rather up on the temple they went, the four bearers; and the temple through pierced, the four bearers, to up

  1  John because then Lord Christ miracle do want
  2  Lord-to every miracle confess have and then | preach
  3  Lord inside Capharnaum and follow to-Lord many people
  4  and then-[?] carry one ill before
  5  Lord-Jesus inside | man^ two-two man head.
  6  among believe love hope forgive^ and | can
  7  the_four_bearers inside °but_rather-up on-temple
  8  go the_four_bearers and temple
  9  through pierce the_four_bearers to-up

## 161v — thy sins are forgiven thee

> onto the roof; and a man, [with] a rope, | let down, asking, love, hope, forgiveness, to the Lord, before the Lord Jesus Christ; the Lord Jesus saw, and was saved our belief, from four men, and the man forgave, the Lord Jesus Christ. And then the Lord Jesus: son of the Lord asking son, loving son, hoping son, | forgiveness; the son shall have health, the son; and then the Lord was [there] [their faith]; the Lord, the Jew, the Lord Jesus; And then the Lord Jesus: [thy sins] | say, believe, somebody, love hope, man, have mercy, man; there is [forgiven] a man, or rise, and go, man.

  1  on-roof and man^ rope | go-~ask-love-hope
  2  forgive^ Lord before Lord-Jesus-Christ see Lord-Jesus be_saved
  3  our believe from two-two man and man^
  4  forgive^ Lord-Jesus-Christ and_said Lord-Jesus son of-Lord
  5  ~ask-son love-son hope-son | forgive^
  6  son exist have-son health son and
  7  then-Lord exist [their_faith] Lord Jew Lord-Jesus
  8  and_said Lord-Jesus [thy_sins] | say-believe-somebody-love
  9  somebody-hope-somebody-have_mercy-somebody exist [forgiven]
 10  have-somebody or rise and* go-somebody

## 162r — rise, take up thy bed and walk

> The Jews said [blaspheme] | said: believe, man, love, man, hope, man, have mercy, man; there is, therefore, a man, said the Lord Jesus rightly; spoke the Jew. And then | the Lord Jesus took […] of the son | asking, love, hope, mercy, the year; and the stretcher he took, and put the son on the stretcher, upon the son's shoulder; and the man went, and the son was saved, our son, home, heaven. Here ends this holy gospel. The Lord Christ, three dead rise, the Lord resurrected | of

  1  say Jew [blaspheme] | say-believe-somebody-love-somebody
  2  hope-somebody-have_mercy-somebody exist therefore* have-somebody
  3  say Lord-Jesus righteous SUBJ speak Jew and_said | Lord
  4  Jesus grab-[?] of-son | ~ask-love-hope
  5  have_mercy-~year and stretcher
  6  take^ and put son stretcher
  7  on-of-son shoulder and go-somebody-son be_saved
  8  our son ~home heaven here_ends this holy_gospel
  9  Lord-Christ three the_dead SUBJ rise^ resurrect-Lord | of

## 162v — the three whom the Lord raised

> the Lord, the Father can; first stand up, resurrect, the Lord Jesus, one head's daughter within Jerusalem; second | died man he stood up and raised, the Lord Jesus: Lazarus, in Jerusalem; | and the three dead stand up, resurrect, the Lord Jesus, Nain; [maiden] therefore stand up, resurrect; and three dead to the Lord, the Lord Christ: but rather the daughter, Lazarus, the son, the Father, of the Lord stand up, resurrect, of the Lord's hands, of the Lord. the finger [into]; the miracle he did. | The Lord, God the Father, Son, God, Jesus, Holy Spirit; the Lord God, be loved.

  1  Lord the_Father can first stand_up resurrect Lord-Jesus
  2  one head daughter inside Jerusalem second | die
  3  man^ stand_up resurrect Lord-Jesus Lazarus inside Jerusalem | in_turn
  4  three the_dead stand_up resurrect Lord-Jesus Nain
  5  [maiden] therefore* stand_up resurrect and three the_dead to-Lord
  6  Lord-Christ but_rather* daughter Lazarus son the_Father
  7  of-Lord stand_up resurrect of-Lord hands of-Lord
  8  finger [into] miracle do | Lord
  9  God_the_Father-son-God-Jesus-holy-spirit Lord_God be_loved

## 163r — the widow of Nain

> This holy gospel begins, written by holy Luke, in the […] chapter of the writing: the time, then, the Lord Jesus, in his thirty- | second year; the time he went, | the Lord Jesus, into one town; and this town's name was Nain; and many people went to the Lord, and then to the Lord the seventy and the twelve apostles, and | then then the Lord Jesus kept going to this town, and then there died in this town the son of one widow woman.

  1  here_begins this holy_gospel
  2  write holy-Luke inside
  3  one-[?] chapter of-write
  4  time then
  5  Lord-Jesus inside thirty | two
  6  day^ time go | Lord
  7  Jesus inside one town and this town name
  8  exist Nain and go to Lord many people
  9  and then to-Lord seventy and six-six disciple^ and | then
 10  then go_on Lord-Jesus this town and then
 11  die inside this town son one widow

## 163v — weep not

> and the son carried; not who, son, Lord God, thief; not humble; the son was the Lord God's; not God had the son out [of] the town, four among the men, at the head, because they had him within. The Old Testament word: thrown out, out [of the] town, to, from, aforesaid, all the world; and there were to the son many people; and then left an army, an army, among the gate, from two peoples, people, two; and they stood [compassion]; and the Lord Jesus saw many sad. And then this woman remained, baptize, sorrowing, this one; how then this? Said the Lord Jesus: stand up | this

  1  and son carry not who-~son Lord_God thief not humble
  2  son exist Lord_God not God have-~son out on-town
  3  two-two among man head because have inside.
  4  Old_Testament word throw_out out town to-from aforesaid all_the_world and exist
  5  to son many people and then leave an_army
  6  an_army among gate from-two people people two
  7  and stand^ [compassion] and see Lord-Jesus many
  8  sad and_said this woman = remain-baptize
  9  sad this how? then this say Lord-Jesus stand_up | this

## 164r — young man, I say to thee, arise

> the woman's son; and the Lord Jesus stood from the coffin, which within the coffin to the son, to the son, from the four men at the head; and the Lord Jesus touched with [his] hands from the coffin, which within the coffin lay dead, the son of this widow. And then | the Lord Jesus raised this son -- in this example, the son [arise] -- and he rose on sitting; how? one prophet. And then: this is the Lord went; his descendant, to the pleasing of the Lord, the prophet foretold through this went the Lord. And then the Lord Jesus took the son, of the son | believe love, hope […]; and | faith, love, hope

  1  woman of son and stand^ Lord-Jesus from coffin which inside coffin
  2  to-~son to-~son from two-two man head and
  3  touch Lord-Jesus of hands from coffin which inside coffin
  4  lie die son this widow and_said | Lord
  5  Jesus rise this son example* son [arise] and rise
  6  on-sit how? one prophet and_said this_is
  7  go-Lord descendant to-pleasing-Lord prophet through predict this_is
  8  go-Lord and_said Lord-Jesus grab-~son of-son | believe
  9  love-hope-[?] and | believe-love-hope

## 164v — and he gave him to his mother

> mercy, the day; and put the son, the stretcher, | on the son's shoulder; and the son gave [himself] into the hands of the Lord Jesus; and then the son was; the Lord took the son's mother, and the son went to the temple, the mother; he was saved; the son's temple, the mother, home to heaven; much joy, in turn, one sorrow remitted. The second somebody saw, can, the Lord Jesus Christ; and the Lord every thanks they gave him. Here ends this holy gospel. The Lord's love. Written by holy Luke in the […] chapter of the writing. This woman signifies the mother, the temple, faith, baptize,

  1  have_mercy day and put son stretcher | on-of
  2  son shoulder and son give^ on-hands Lord-Jesus and
  3  then son exist grab-Lord of-son mother and
  4  go son temple mother be_saved of-son temple mother
  5  ~home heaven great^ joy in_turn one sad remit
  6  second see-somebody can Lord-Jesus-Christ and Lord
  7  every thanks grab-somebody here_ends this holy_gospel the_Lord love
  8  write holy-Luke inside one-[?] chapter of-write
  9  this woman symbolize mother temple believe ~baptize

## 165r — what the widow and her son signify

> baptize; the son symbolizes the soul of everybody, that the Lord God, the Creator Lord, every man; this town signifies that, that he is saved, that [signifieth] the Lord Jesus Christ, all the whole world | this this is saved: everybody [who] believes, baptize, baptize [signifieth] the Lord saved, the Lord Jesus Christ, the Father of the Lord. In this gospel, as holy Luke writes, there went four men at the head, to the son; in this example the son [arise] and the son was dead; and the son [they] took and carried; not love | the Lord the divine one; the thief is not humble; the Lord God not have

  1  baptize son symbolize soul everybody = that* Lord_God Creator_Lord
  2  everybody = this town symbolize that* that* be_saved
  3  that* [signifieth] Lord-Jesus-Christ every all_the_world world | this
  4  this be_saved everybody = believe ~baptize baptize [signifieth]
  5  the_Lord be_saved Lord-Jesus-Christ the_Father of-Lord
  6  inside this gospel SUBJ write holy-Luke go two-two man
  7  head to-~son this example* son [arise] and son
  8  exist die and son grab and carry not love | Lord
  9  DIV thief SUBJ not exist humble Lord_God not have

## 165v — the first of the four ways

> the Lord God; and this not repentance [confession] took this son, this widow woman; and the son was carried out, into belief. baptize, baptize: that is, cast out, the son remitted, saved, the damned son, for ever and ever. Within the gospel writes holy Luke this example: not love the most high Lord God | from the literal, every creature, than various creatures; love the son, and not who. Then the dead son goes to the son, and leaves; not love, on the first way. Within the gospel writes holy Luke: this example: there were many thieves, but by name the son

  1  Lord_God and this not repentance [confession] grab this son this
  2  widow and son carry out on-believe.
  3  ~baptize baptize that_is cast_out son remit be_saved
  4  be_damned son for_ever_and_ever = inside gospel write
  5  holy-Luke this example* not love most_high Lord_God | from
  6  literal every create than various create love-son and not who
  7  then die-son go to-son and leave not love
  8  on-one way inside gospel write holy-Luke
  9  this example* SUBJ exist many thief ~but-+name-to son

## 166r — the second, third and fourth ways

> on repentance took; then the dead son goes to the son. And the thief leaves, on the second way. Within the gospel writes holy Luke this example: not being humble, son, somebody, and the Lord God; then the dead son goes to the son, and leaves; not being humble, on the third way. Within the gospel writes holy Luke this example: not having, the son, the Lord God, in all of the son's [whosoever sins dies] [dead] the son is within [whosoever sins dies] then the dead son goes to the son, and leaves; not having,

  1  on-repentance grab then die-son go to-son.
  2  and leave thief on-two way inside-gospel write
  3  holy-Luke this example* not exist humble son
  4  somebody and Lord_God then die-son go to-son
  5  and leave not exist humble on-+three way inside-gospel
  6  write holy-Luke this example* not have
  7  son Lord_God inside every of-son [whosoever_sins_dies]
  8  [dead] SUBJ exist son inside [whosoever_sins_dies]
  9  then die-son go to-son and leave not have

## 166v — the whole law in two commandments

> on the fourth way; and [between] four men and the son they took, the four men, and carried the son out the town gate town, on belief; baptize, baptize; on damnation, then the son is carried into hell, damned, is ever ever. [with thy whole soul] not saved. Writes within Moses, truly: love the Lord God highest [above] all creation, all our soul, all our might, all our heart; and our father's son, as somebody [his] neighbour | of the man; heaven and earth. Here ends this holy gospel.

  1  on-two-two way and [between] two-two man and son
  2  grab two-two man and son carry out the_town_gate*
  3  town on-believe ~baptize baptize on-be_damned then
  4  son carry inside hell be_damned exist ever.
  5  ever [with_thy_whole_soul] not be_saved write inside
  6  Moses true^ love Lord_God highest all^ create all^ our
  7  soul all^ our might all^ our heart and
  8  our the_father son as somebody neighbour | of
  9  somebody SUBJ heaven land here_ends this holy_gospel

## 167r — a certain rich man had a steward

> This holy gospel begins, written by holy Luke in the sixth chapter of the writing: the time the Lord Jesus said to the apostles of the Lord, and to the Jewish people: there was a rich somebody, who left, from the rich [man's] sight, a steward over the rich man's goods | — sight, speech, life, hearing, soul, body, reason, sense, all to manage; and the man began, the steward, this rich man's sight, speech, life, hearing, soul, body, reason,

  1  here_begins this holy_gospel
  2  write holy-Luke
  3  inside six chapter of-write
  4  time say Lord-Jesus
  5  disciple^ of-Lord and Jew
  6  people exist one rich-somebody who leave-from-rich-see
  7  steward^ on-of-Lord-rich-somebody | rich-see-say-living-hear
  8  soul-body-reason-sense every manage
  9  and begin-somebody-manager this rich of-Lord-rich-somebody
 10  see-say-living-hear-soul-body-reason

## 167v — the same was accused unto him

> sense to manage; and then began, the man, and then a man came to accuse one servant before the steward; the man's lord spoke to the servant, this serving angel: all of the rich man's | […] soul, body, reason, sense [give an account] sense, the word scattered; got angry, this rich, rich Lord God | this rich. The man. And then to the account: many not of the Lord, rich somebody, the steward; and he heard this, the steward, this said from the steward's rich lord [put out] and | sorrowing

  1  sense manage and then SUBJ begin man* and then
  2  man^ exist accuse one servant before
  3  of-manager somebody-Lord say-~servant this angel-servant
  4  every of-Lord-rich-somebody | [?]-soul.
  5  body-reason-sense [give_an_account] sense
  6  word scatter get_angry this rich-rich-Lord_God | this-rich.
  7  man^ and_said to-?the_account many not of-Lord-rich-somebody
  8  steward^ and hear this steward^ this say from
  9  of-manager Lord-rich-somebody [put_out] and | sad

## 168r — what shall I do?

> the steward, the manager left. And then this steward, the crying manager, [dig] and [I am not able] [to beg] and try, pray thee [I am ashamed] the steward [thought]; and the manager found one friend. and then this steward had two debtors | of the steward, a man of mercy and of alms; and | then there was, among the steward's, this one debtor of mercy; and this said, the steward: how much mercy dost thou owe the steward? [my lord] And then the debtor, have mercy, somebody: a hundred measures of oil. And then this steward sat [him] [down], have mercy, somebody,

  1  steward^ leave-manager and_said this steward^ crying-manager
  2  [dig] and [I_am_not_able] [to_beg] and °try-°pray_thee [I_am_ashamed]
  3  steward^ [thought] and one friend find-manager
  4  and then have this steward^ two debtor^ | of
  5  steward^ man* find_mercy^ and alms and | then
  6  exist among-manager this one debtor^ find_mercy^ and say this
  7  steward^ how_much? find_mercy^ debtor^ of-manager [my_lord]
  8  and_said debtor^ have_mercy-somebody hundred measure
  9  oil and_said this steward^ sit-have_mercy-somebody

## 168v — sit down quickly, and write fifty

> down, and write fifty; in turn five, rich, ten | have mercy somebody, down [another] this, and this [thy bill] of the manager's Lord God, rich somebody. And then these two, the steward | have mercy the man [a hundred] [quarters of wheat] divided into two parts, the steward of mercy, and among these, the steward, these two debtors | alms, the man; and this said, the steward: how much alms dost thou owe, to the manager's Lord, rich somebody? And then the indebted, alms: a hundred measures of wheat. And then this steward | sat the alms-somebody down, and write from | five

  1  down and write fifty in_turn five-rich-ten | have_mercy
  2  somebody down [another] this and this [thy_bill] of-manager
  3  Lord_God-rich-somebody and_said this two steward^ | have_mercy
  4  somebody [a_hundred] [quarters_of_wheat] divide-two-manager-have_mercy-somebody
  5  ~and among this steward^ this two indebted | alms
  6  somebody and say this steward^ how_much? alms indebted
  7  of-manager Lord-rich-somebody and_said indebted alms
  8  hundred measure wheat and_said this steward^ | sit
  9  alms-somebody down and write from | five

## 169r — the lord commended the unjust steward

> thirty; in turn twenty, rich, alms-somebody, down [another] this, and these two [eighty] [thy bill] of the steward's rich Lord God; and in turn unjust steward he took, this, the steward's rich Lord God, because the steward found a friend. And then this steward these two, the steward's men of alms [a hundred] [quarters of wheat] | divided, two managers, alms-somebody. And then the Lord Jesus: O, of the Lord, son; have, apostles, truly: the steward was have, apostles, friend find; because the Lord, I, this rich Lord God, the man; the Lord took to you many riches,

  1  thirty in_turn two-ten-rich alms-somebody down [another]
  2  this and this two [eighty] [thy_bill] of-manager Lord_God-rich-somebody
  3  in_turn [unjust_steward] take^ this of-manager Lord_God-rich-somebody
  4  because steward^ friend find and_said this steward^
  5  this two-manager-alms-somebody [a_hundred] [quarters_of_wheat] | divide
  6  two-manager-alms-somebody and_said Lord-Jesus
  7  oh of-Lord son have-apostle righteous steward^ exist
  8  have-apostle friend find because-Lord I this
  9  rich-Lord_God-somebody grab-Lord you greatly^ rich

## 169v — the goods are the senses

> the Lord took to you sight, the Lord took to you speech, the Lord took to you life, the Lord took to you hearing, the Lord took to you soul, the Lord took | is he yours; the body the Lord took [from] you, reason the Lord took to you, sense the Lord took. To you, all of the rich Lord God's | sight, speech, life, hearing, soul, body, reason, sense; and the apostles and the Jews are, truly, stewards over | sight, speech, life, hearing, soul, body, reason, sense, in turn within this world, rich have these apostles [and] Jews friend find.

  1  grab-Lord you see grab-Lord you
  2  say grab-Lord you living grab-Lord you
  3  hear grab-Lord you soul grab-Lord | ~you
  4  yours body grab-Lord you reason
  5  grab-Lord you sense grab-Lord.
  6  you every of-Lord_God-rich-somebody | rich-see-say.
  7  living-hear-soul-body-reason-sense
  8  and exist-apostle-Jew righteous manager inside | rich-see-say
  9  living-hear-soul-body-reason-sense
 10  in_turn inside this world rich have this-apostle-Jew friend find

## 170r — the account, and a new gospel begins

> Here ends this holy gospel, spoken by holy Luke. Have | this: the apostles, Jews, somebody, righteous stewards [of] our father, the son; and among them the man has the son. friend find, because then the dead are friend; somebody grows calm; friend [at his] side. this holy gospel. Learning. The Lord God, be loved; the Lord God have mercy. This holy gospel begins, written by holy Matthew in the fifth chapter | of the writing; by holy Luke within | four four chapter; the holy chapter of Jerusalem, within the ninth chapter: time; then the Lord Jesus within

  1  here_ends this holy_gospel speak holy-Luke have | this
  2  apostle-Jew-somebody righteous steward^ our father
  3  son and among somebody son have somebody.
  4  friend find because then the_dead exist
  5  friend somebody grow_calm friend side^
  6  this holy-gospel learn Lord_God be_loved Lord_God SUBJ-have_mercy
  7  here_begins this holy_gospel write
  8  holy-Matthew within^ five chapter | of
  9  write holy-Luke within^ | two-two
 10  two-two chapter holy-chapter-+one-Jerusalem within^ nine chapter
 11  time then Lord-Jesus within^

## 170v — can the children of the bridegroom mourn?

> his thirtieth year; the time the Lord Jesus went into the temple at Jerusalem, and | then he was in the temple; the Lord Jesus went, and the Lord saw who, much joy and much sorrow; and from afar off were the apostles of holy John baptize, baptize; and then the Lord Jesus left. And then the apostles: Master, the apostles fast, the apostles; and the Pharisees fast; in turn the Lord's apostles not fast, the apostles. And then the Lord Jesus to the apostles: | on joy, in turn; then the apostles go in joy, keeping watch, while the apostles fast, on, that is, the apostles leave the Lord Jesus; from the head And then the apostle Jairus: Jairus's daughter died, to the high priest, this was who: Master; and he took this head.

  1  thirty years* time go Lord-Jesus inside Jerusalem temple and | then
  2  exist inside temple go Lord-Jesus and see-Lord who* many joy
  3  and many sad and from-to-far exist apostle holy-John
  4  ~baptize baptize and then leave^ Lord-Jesus and_said apostle
  5  Master apostle fast-apostle and Pharisee fast in_turn of-Lord apostle
  6  not fast-apostle and_said Lord-Jesus to apostle | on
  7  joy in_turn then go apostle on-joy observe exist
  8  apostle fast ~on-that_is leave^ apostle Lord-Jesus from head
  9  and_said apostle Jairus of-Jairus daughter SUBJ die to-high_priest
 10  this ~exist-who Master and take^ this head.

## 171r — the woman who touched the hem

> the Lord Jesus; and went the Lord, the head, Jesus, this head's house; and many people went to the Lord; and there was among this people one woman, which a woman [who] was nine years, twelve years, within blood ill; And then this woman, then Christian: how shall we touch? of the woman, hands, of the Lord, clothes; the hem; Christian; healing, woman, the woman left; and then [she] touched the clothes of the Lord Jesus, | within the hour the woman was healed, the woman left off; and the Lord Jesus saw on the people; the hand of the Lord; there were many people. And then the Lord Jesus: this

  1  Lord-Jesus and go-Lord-head-Jesus this head
  2  house and go to Lord many people and exist
  3  among this people one woman = which
  4  woman = exist nine-year-six-six-year inside blood ill
  5  and_said this woman = then Christian
  6  how_shall_we* touch of-woman hands of-Lord clothes
  7  hem Christian healing-woman leave-woman and
  8  then touch clothes Lord-Jesus | inside
  9  hour healing-woman leave-woman and see Lord-Jesus
 10  on-people hand-Lord ~exist many people and_said Lord-Jesus this

## 171v — thy faith hath made thee whole

> woman: the woman's faith healed the woman. Did, who, year, said the Lord Jesus: I [said to] this woman, the Lord healed; but the Lord Jesus said to this woman: the woman's faith hath healing done. And | went the Lord, the head, the apostles, Jesus, the woman, the Jews, [to] this head's house; and | then the Lord, the head […], Jesus, the woman, the Jews entered; and saw the Lord Jesus much sadness. And then the Lord Jesus [give place]: not this daughter [is] dead, the daughter, but rather the daughter sleeps. And then the Jews laughed [at] the Lord Jesus. And then the Jews: see, love | this

  1  woman of-woman believe healing-woman ~do
  2  who-~year say Lord-Jesus I this-woman heal-Lord but
  3  say Lord-Jesus this-woman of-woman believe healing
  4  do and | go-Lord-head-apostle-Jesus-woman
  5  Jews this head house and | then-Lord
  6  ~head-[?]-Jesus-woman-Jews enter and see
  7  Lord-Jesus many sad and_said Lord-Jesus [give_place]
  8  not this daughter die-daughter but_rather to-sleep-daughter and then
  9  Jews laugh Lord-Jesus and_said Jews see love | this

## 172r — damsel, arise

> the Lord [laughed him to scorn] spoke. And then the Lord Jesus [to] this head. cast this people out; and then, having cast out, the chief man, and with the Lord Jesus the daughter's father and mother. And then the Lord Jesus [to] the sky said, said, named this: one servant, rise, servant, daughter, among [the] Virgin Mary; and | then the daughter rose, sat up. And then, lo, the Lord went, his descendant, to the pleasing of the Lord, the prophet foretold through; lo, the Lord went; And then the Lord Jesus [had] the father [and] mother carry wine and bread [walked] [give her to eat] and drink; and then the daughter

  1  Lord [laughed_him_to_scorn] speak and_said Lord-Jesus this head.
  2  cast_out this people out and then out cast_out
  3  head and among Lord-Jesus of-daughter father
  4  and mother and_said Lord-Jesus sky say say name-this
  5  one-+servant rise servant daughter among Virgin_Mary and | then
  6  exist rise^ daughter on-sit and_said lo go-Lord
  7  descendant to-pleasing-Lord prophet through predict lo go-Lord
  8  and_said Lord-Jesus carry father mother wine and bread
  9  [walked] [give_her_to_eat] and drink and then daughter

## 172v — the fame of it went abroad, and the talents begin

> drink; and the daughter ate. And then the Lord Jesus, this moon, [the fame] not say; and the news went up [to] every sky. and earth. Here ends this holy gospel. The Lord God, with all thy heart. This holy gospel begins, written by holy Stephen, the kingdom; this word, written, the chief; this world, the Lord, the priest; and the high Magdalene year, the kingdom, all the Lord, baptize; and the farm, the people; this word he speaks, king; there was a rich lord going a long way; and | then the Lord had three living servants; and then the servants

  1  drink and ~eat-daughter and_said Lord-Jesus this moon
  2  [the_fame] not say ~and news ascension^ every sky
  3  earth here_ends this holy_gospel Lord_God be_loved
  4  here_begins this holy_gospel.
  5  write holy-Stephen kingdom^
  6  this word write head
  7  this world Lord priest.
  8  and high-Magdalene-~year kingdom^ every
  9  Lord ~baptize and farm people this word speak-~king exist
 10  go-Lord one rich Lord long way and | then
 11  exist have-Lord three living-servant and then living-servant

## 173r — one talent, three talents, five talents

> before the Lord; he was with the Lord; and then the Lord took one servant one gold talent; the second the Lord took three talents of gold; the third the Lord took, five gold talents. And then this rich Lord, all, until this [gave]: five senses, mercy, prayer, alms, faith [ability]; the servant's mouth, I go, baptize; how shall we be saved, living servant? And the Lord took the priest, the high Magdalene year, the kingdom, the Lord, baptize, the farm, the people, the man, soul, soul, soul, soul. Here ends this holy gospel. The Lord's love.

  1  SUBJ before Lord exist ~among-Lord and then grab-Lord
  2  one servant one gold* talent second
  3  grab-Lord three gold* talent third grab-Lord
  4  five gold* talent and_said this rich-Lord every until
  5  this [gave] five sense find_mercy^ pray.
  6  alms believe [ability] servant mouth
  7  I go ~baptize be_saved how_shall_we* living-servant and Lord grab priest
  8  high-Magdalene-~year kingdom^ Lord ~baptize farm people man^
  9  soul soul soul soul here_ends this holy_gospel the_Lord love

## 173v — after a long time the lord came

> Many years passed; then this rich lord returned | to the lodging, because from the lodging the way of the people lay into the house of this rich lord; and from the people, the servant carried this rich lord; and then went out on | called this rich and the Lord's living servants, the apostles, the angels; and then he did so among this rich lord's; the Lord's servant, before the rich lord [after a long time] the three servants stood; the Lord took | of the rich Lord. And then this rich Lord, this one to whom the Lord had given five talents of gold — talent. And then this rich Lord reckoned with the servant: how shall we, somebody

  1  many year exist then return this rich-Lord | on
  2  lodging because from* lodging way people inside house this
  3  rich-Lord and from people servant bring^ this rich-Lord and
  4  then go out on | called this rich
  5  and of-Lord living-servant-apostle-angel and then do
  6  among this rich-Lord of-Lord servant before rich-Lord
  7  [after_a_long_time] three SUBJ servant exist-Lord grab-Lord | of
  8  Lord rich and_said this rich-Lord this one to_whom
  9  SUBJ exist-Lord grab-Lord five gold.*
 10  talent and_said this rich-Lord reckon_with* servant how_shall_we-somebody

## 174r — well done, good and faithful servant

> of the rich Lord? This servant said: how shall the man be pleasing to the Lord God? And received the aforesaid five gold talents. And then this rich Lord: go, servant, into the Lord's house, to the Lord's Father, and to God the Father; somebody is a joy-somebody ever ever, amen. And then called this second, to whom the Lord had given three talents of gold; And then this rich Lord reckoned with the servant: how shall we, somebody | of the rich Lord? This servant said: how shall the man be pleasing to the Lord God? And [he] received the aforesaid three gold talents. And then this rich Lord:

  1  of-Lord rich say this servant how_shall_we-somebody to-pleasing Lord_God and
  2  receive* five gold* aforesaid talent and_said this rich Lord
  3  go-servant inside of-Lord house to-of-Lord the_Father and
  4  to-God_the_Father somebody exist joy-somebody ever
  5  ever amen and then called this two
  6  to_whom SUBJ exist-Lord ~grab-Lord three gold* talent
  7  and_said this rich-Lord reckon_with* servant how_shall_we-somebody | of
  8  Lord rich say this servant how_shall_we-somebody to-pleasing Lord_God
  9  and receive* three gold* aforesaid talent and_said this rich Lord

## 174v — the third servant

> go, servant, into the Lord's house, to the Lord's Father, and | to God the Father; the man is in joy for ever and ever, amen. And then called this third, to whom the Lord had given one talent of gold; And then this rich Lord reckoned with the servant: how shall we, somebody? Of the rich Lord, this servant said [hard] servant [thou reapest] [where] [thou hast not sown] [gatherest] there is love, there is riches [ability] servant, because he [afraid] had the servant; because then this servant of the rich Lord lost, the servant; he is [hid in the earth]

  1  go servant inside of-Lord house to-of-Lord the_Father and | to
  2  God_the_Father man^ exist ~joy for_ever_and_ever =
  3  amen and then called this three to_whom SUBJ
  4  exist-Lord grab-Lord one gold* talent
  5  and_said this rich Lord reckon_with* servant how_shall_we-somebody
  6  of-Lord rich say this servant [hard] servant [thou_reapest]
  7  [where] [thou_hast_not_sown] [gatherest] love-exist exist-rich [ability] servant
  8  because he [afraid] have servant because then this-servant
  9  of-Lord rich lose ~servant he exist [hid_in_the_earth]

## 175r — take the talent from him

> on the servant; the rich [Lord] has he, and from [extort] on the servant took; because this rich Lord God [take away] [talent] | […] the Jews the man; and said. And then this rich Lord: this unprofitable servant, high, this servant, this | servant's love is this: the eye seems, servant; the Lord's house long; this | love is: go, servant, into the Lord's house. And then this rich Lord's servant, the angel, took from this unprofitable servant this one talent; and the angel took the talent from him and gave it to the faithful servant, the servant who has ten talents. Here ends this holy gospel.

  1  on-~servant rich have he and from [extort] on-~servant
  2  grab because this-rich Lord_God [take_away] [talent] | [?]-Jews
  3  man* and say and_said this-rich-Lord
  4  this unhelpful servant high this-servant this | ~servant-love
  5  exist this eye seem^ servant of-Lord house long this | love
  6  exist go-~servant inside of-Lord house and_said this rich
  7  of-Lord ~servant grab angel from this unhelpful ~servant
  8  this one talent and talent grab angel from
  9  believe ~servant servant talent ten have here_ends this holy_gospel

## 175v — the Lord goes from town to town

> This holy gospel begins, written by holy Luke in the sixth chapter of the writing: the time, then the Lord Jesus within thirty years; the time the Lord Jesus went among the people, and the Lord's apostles, from town until town; from temple until temple; from village until village; and the Lord's apostles; and went

  1  here_begins this holy_gospel write holy-Luke
  2  inside six chapter of-write time
  3  then Lord-Jesus inside thirty years*
  4  time go Lord-Jesus among_the_people* and of-Lord apostle from town
  5  until town from temple until temple from
  6  village until village and of-Lord apostle and go

## 176r — the woman of Samaria at the well

> the Lord Jesus, to one well; and the Lord Jesus sat by this well, because there was [afraid]; the Lord was wearied; in turn the apostles went, into the village for bread; and living; if the body living; and then there came one woman | to this well; and then the woman dipped [at] this well. And then the Lord Jesus [was] thirsty, the Lord; and then the woman was; the Lord [asked] water; asked. And then this heathen: how he | dare the Lord, to ask water of a pagan? This heathen [woman] in turn: | this Lord is a Jew; she dipped for the Lord [give me] to drink, the Lord, and

  1  Lord-Jesus one well and sit Lord-Jesus to-this
  2  well because exist [afraid] tire-Lord in_turn disciple^ go-apostle
  3  inside village on-~bread ~and living ~if body
  4  living and then go one woman = | to
  5  this well and then dip-~woman this well and_said
  6  Lord-Jesus thirsty-Lord and then-~woman-+SUBJ exist-Lord water
  7  ~ask and_said this heathen how? he | dare
  8  Lord from pagan water ~ask this heathen in_turn | this
  9  Lord Jew dip-+the_Lord [give_me] on-drink Lord and

## 176v — the Lord begins to speak to the Gentiles

> he began to speak through the pagan, the Lord Jesus; and the heathen | judged this; had; pagan man; and the heathen began, the Lord, | to say this: raise, heathen [woman], the place, do; if | do, pagan; divorce of the heathen. And then this heathen | on the heathen, many to which; and from [five husbands]; he, he, descendant husband; to the pleasing of the Lord, the prophet foretold; and the disciples went to the Lord, and the apostles began; the wonder upon the Lord; the Lord's love; the Lord spoke this | woman, one woman, the head; and this heathen [woman] believed in the Lord Jesus; and the heathen [woman] went to her own | […] from

  1  begin through talk^ pagan Lord-Jesus and heathen-+SUBJ | ~judge
  2  this ~have pagan man and heathen begin-Lord | say
  3  this-raise heathen place^ do ~if | do
  4  pagan divorce of-heathen and_said this heathen | on-of
  5  heathen °many-to which and from [five_husbands] he he descendant
  6  husband^ to-pleasing-Lord prophet predict and go disciple^ to-Lord
  7  and begin-apostle wonder^ on-Lord love-Lord speak-Lord this | ~woman
  8  one-~woman head and believe this heathen inside
  9  Lord-Jesus and go heathen to-of-heathen | [?]-from

## 177r — come, see a man who told me all things

> [the woman] and then went into the village, and the heathen [woman] began to speak | this: this people, sit; one Lord at the well, and even more from the Lord, to the pleasing of the Lord, the prophet foretold through; because the heathen's home did; the heathen's love did; the heathen divorced; the heathen's every deed [all things]; the heathen said […]; and then this people believed in the Lord, the man, the people; and the people went to this well, because they would pray to the Lord; | then and the people were there, and the Lord preached one to two years.

  1  [the_woman] and then go inside village and begin-heathen say | this
  2  this people sit one Lord to-well still_more from-Lord
  3  to-pleasing-Lord prophet through predict because of-heathen home
  4  do love-heathen do heathen divorce
  5  of-heathen every ~do [all_things] heathen-+SUBJ say-[?] and
  6  then this people inside Lord-somebody believe-people and
  7  go-people this well because-Lord want-people pray | then
  8  exist and people exist-Lord preach one to-two-year

## 177v — the gospel ends, and another begins

> and even more to the Lord Jesus; but the Lord went into Galilee, to the town. Here ends this holy gospel. The Lord God, with all thy heart. This holy gospel begins, written by holy Luke, in

  1  and still_more-to Lord-Jesus but to-go-Lord inside Galilee
  2  town here_ends this holy_gospel Lord_God be_loved.
  3  here_begins this holy_gospel
  4  write holy-Luke inside

## 178r — the ten lepers

> the fifth chapter of the writing: at that time, then, the Lord Jesus, within thirty | one years: at that time the Lord Jesus went into Jerusalem; and went to the Lord and many people; and then the Lord Jesus went, the people, into the field, and left, stood far away, ten leper people; and began the ten lepers began to cry out: son of David, king, have mercy — the ten lepers, son; and they cried to the Lord Jesus; go, ten lepers, and let the ten shew themselves to the priest; and the priest took the ten lepers, from all that was [shew yourselves] the commandment of Moses; and then the ten lepers went | from

  1  five chapter of-write time then Lord-Jesus inside thirty | one
  2  years* time go Lord-Jesus inside Jerusalem and go to Lord
  3  many people and then go Lord-Jesus people on-~field-+one and
  4  leave stood far_away ten leper people and begin ten
  5  leper shout-to son David king have_mercy
  6  ten leper son and shout-to Lord-Jesus go ten
  7  ~leper and ten appear priest and
  8  priest grab ten leper from every-~exist [shew_yourselves]
  9  Moses commandment and then go ten leper | from

## 178v — the priests dispute over them

> saw the lepers' body; and then were the lepers' body healing; and one Wednesday, ten, how, aforesaid, alone [as they went] [were made clean]; and then the ten lepers went, the ten people, before the high priest, before the priest. And then the priests of the Jews: how are you people, ten | lepers? Chapter. Said [one of them] the lepers, from the people [went back] the lepers; the people were before the priest, among the priests, the Jews, the man; they cast the priest out; the Jews said to the priest; the Jews: who of you men is healed? | said the leper

  1  see of-leper body and then exist
  2  leper body healing and one-+Wednesday ten how?-aforesaid-°alone
  3  [as_they_went] [were_made_clean] and then ten leper go-ten-people-before
  4  high_priest = before priest and_said
  5  priest Jew how? you people ten | leper
  6  chapter say [one_of_them] leper from-people [went_back] leper.
  7  people exist priest among priest Jew-somebody
  8  out cast_out priest Jew say priest.
  9  Jew who? you man^ heal | say-leper

## 179r — where are the nine?

> the ten people healed: son of David, king; said the chief men, the Jews, the priest [glorifying God]: you people, from the son have sinned; the Lord healed you; but you people were healed by Moses truly, because there is the word of the Old Testament, from the lepers, the Jews; among the priests, the Jews, out, cast out, and then of the nine people a man believed the priests, the Jews; in turn the tenth man had faith, and returned back to the Lord Jesus; and the leper bowed down before the Lord's feet; and then the Lord's sister

  1  ten-people heal son David king say head
  2  Jew priest [glorifying_God] you people from son
  3  sin_against heal-Lord but you people-+SUBJ heal
  4  Moses righteous because-exist Old_Testament word from
  5  leper-Jews among priest Jew out exorcise
  6  and then from nine people somebody believe from priest
  7  Jew in_turn ten somebody faith* but return
  8  back against Lord-Jesus and bow leper
  9  before of-Lord foot and then-Lord sister

## 179v — were not ten made clean?

> kissed, the tenth man, the Lord's feet; and the Lord, godfearing, and thanks took the tenth somebody. And then the Lord Jesus, the apostles | of the Lord, to all by name: and the people, were there not ten lepers? Which [were not ten] one somebody, commandment; and somebody, commandment, the Lord loves. And then the Lord Jesus, the Lord's apostles: good [the nine] from | you, chapter [so] the son, the man; there is the Lord; the heathen's love. Here ends this holy gospel. The Lord God's love. Three things must be believed from the world: first believe above, high; and then the pagans, and the Jews believe within these; believe one somebody

  1  kiss-ten-somebody of-Lord foot and Lord godfearing^
  2  and thanks grab-ten-somebody and_said Lord-Jesus apostle | of
  3  Lord name-every-to and people exist ten leper in_turn-+who
  4  SUBJ [were_not_ten] one somebody-commandment and somebody-commandment Lord love
  5  and_said Lord-Jesus apostle of-Lord good [the_nine] from | ~you-chapter
  6  [so] son somebody exist Lord heathen love end
  7  this holy-gospel Lord_God SUBJ love three believe have
  8  from world first SUBJ believe above-high and °and_then-pagans and Jew
  9  believe inside these believe one somebody

## 180r — one faith, one Church

> and the Jews, the pagans, above high; in turn not saved; and somebody not believe, somebody, in the Lord Jesus Christ; one somebody not saved, but everybody damned; second believe the Church; and the Church's belief is good, because there is one Church; the Church, and in believing is salvation, because from the church, the church, one way, belief, the Church, the Church, in the Lord Jesus Christ, in his coming and in his death; then on the cross the Lord gave up the ghost; thirdly, believe in the coming of the Lord Christ; and through him escape.

  1  and Jew-pagans above-high in_turn not be_saved and somebody
  2  not believe somebody inside Lord-Jesus-Christ one
  3  somebody not be_saved but everybody = be_damned second SUBJ
  4  believe church and church believe this_is good
  5  because one church church and inside believe be_saved
  6  because from church church one way believe
  7  church church inside Lord-Jesus-Christ inside ~be_born and inside
  8  die then-+SUBJ on_the_cross of-Lord soul give_up_the_ghost third
  9  SUBJ believe on-~be_born Lord-Christ and through escape

## 180v — a summary of the Lord's life

> the Lord Jesus; and the twelve apostles followed the Lord Christ; and many tired, the Lord Christ, who wearied; the Lord did it; he went into the world | of the Lord, the apostles; and many a miracle the Lord Christ, in love, did | upon the world; the Lord's apostles went; the blind of eye he gave light; the dead man he stood up and raised; the evil upon the people, before, to who, the Lord | love, and these ill the Lord healed; and the holy Host, God's body, the Lord Christ; if the Lord at thirty stayed, the Lord, within the host; and the Lord Christ was humble, because the Lord was humble in this world. The chief men took the Lord, and the Jews captured him [led away]

  1  Lord-Jesus and follow Lord-Christ six-six apostle and many tire
  2  Lord-Christ who tire-+SUBJ do-Lord into_the_world* go-Lord | of
  3  Lord apostle and many miracle Lord-Christ love miracle-+SUBJ do | on
  4  world go of-Lord apostle eye-blind SUBJ through light Lord die somebody
  5  SUBJ stand_up resurrect-chapter-Lord evil SUBJ on-people ~before-to-+who-Lord | love-and
  6  these ill heal-Lord and holy-+host God body
  7  Lord-Christ ~if Lord on-thirty stay-Lord inside host
  8  and humble Lord-Christ because-+the_Lord exist-Lord humble-Lord this world.
  9  head grab-Lord and Jew SUBJ capture [led_away]

## 181r — Thomas was not with them

> [they platted] and a crown of thorns upon his head | conceived, the Jews; and [trodden down]; died the Lord Christ, and rose the Lord Christ, and appeared to the Lord's apostles, one Saturday evening; and this evening it was; then the Lord appeared, the Lord, [to] the twelve disciples in the Lord's house, where the Lord God, the Lord Jesus, had made the supper; and | then holy Thomas came Didymus one Saturday evening to the apostles; and the apostles said: Thomas, the apostles have seen the Lord. And holy Thomas said, this Thomas: this not believe, all this; then | this Thomas: this believe, if [unless] Thomas sees

  1  [they_platted] and thorn crown on-head | conceive
  2  Jews and [trodden_down] die Lord-Christ and rise Lord-Christ and appear
  3  Lord-Christ disciple^ of-Lord one Saturday evening and this
  4  evening exist then-Lord appear-Lord six-six disciple^
  5  within^ Lord house where Lord_God Lord-Jesus dinner-to do and | then
  6  exist go holy-Thomas Didymus* one Saturday evening
  7  to-apostle and say disciple^ Thomas disciple^ see Lord and say holy-Thomas
  8  this-Thomas this not believe every this then | this
  9  Thomas this believe if [unless] see-Thomas

## 181v — blessed are they that have not seen

> the Lord's side, and unless Thomas puts his finger into the Lord's side, who from the Lord, from death, stood up. At that time the Lord Jesus Christ stood into the midst of the apostles, the doors being shut, and said: peace be to you; and the judgment year; the apostles; in turn Thomas began to have, and said | the Lord Jesus: Thomas, come by name [hither] put thy finger into the Lord's wound [blessed] see and believe; and [have not] the Lord Jesus, the Lord's wound; and said the Lord Jesus: Thomas, happy from; and somebody sees and believes; but and | blessed year to; and not see, but believe. Here ends this holy gospel.

  1  of-Lord side^ and of-Thomas finger not put within^ of-Lord
  2  side^ who from Lord from die stand_up time stand^ Lord-Jesus-Christ
  3  middle disciple^ closed and say peace^ you exist
  4  and judge-year disciple^ in_turn Thomas begin have and say | Lord
  5  Jesus Thomas go-+name [hither] put of-Thomas finger
  6  within^ of-Lord wound [blessed] see believe and [have_not]
  7  Lord-Jesus of-Lord wound and say Lord-Jesus Thomas happy
  8  from and somebody see and ~believe but and | blessed
  9  ~year-to and not see but believe here_ends this holy_gospel

## 182r — the appearance at table, and the sending out

> The Lord God, with all thy heart. And this [upbraided] the man said, the Lord Jesus [hardness of heart] somebody, the Lord, not within, year […] somebody; and then after the Lord Christ was executed, in the […] year, the time the apostles sat at table in Jerusalem, in the Lord's house, | at the place where the Lord God, the Lord Jesus, had made the supper; the time the Lord Jesus appeared [to] the Lord's apostles within the body, somebody; and he sat with the apostles, outside, and began to upbraid them | for their belief; and the Lord Jesus said: go, apostles, | into the world; and is one woman baptized in the Lord's, is […]

  1  Lord_God be_loved and this [upbraided] somebody say Lord-Jesus [hardness_of_heart]
  2  somebody Lord not inside-~year-[?] somebody and then
  3  on-execute Lord-Christ [?]-year inside
  4  time sit apostle to-table inside Jerusalem inside Lord house | to
  5  [where] Lord_God Lord-Jesus dinner do time
  6  appear Lord-Jesus apostle of-Lord inside body somebody
  7  and sit to-apostle to-~out and begin admonish | on
  8  believe and say Lord-Jesus you go-apostle | on
  9  world and exist one-~woman baptize inside of-Lord exist-[?]

## 182v — baptize them in the name of the Father

> and somebody is one woman baptized in the name of God the Father and of the Son and of the Holy Spirit; and let him be to the Lord | to believe; every such man is saved, and one is damned [but] [but]; and somebody not one woman baptized and not to the Lord; one saved, but every man is damned. Here ends this holy gospel. The Lord God's love. Written by holy Luke in the second chapter of the writing: the time, then, after the execution

  1  and somebody exist one-~woman baptize inside name God_the_Father
  2  and son and holy-spirit and exist Lord-to | to
  3  believe* everybody = be_saved and one
  4  be_damned [but] [-but] and somebody not one-~woman baptize
  5  and not Lord-to one be_saved but
  6  everybody = be_damned here_ends this holy_gospel Lord_God SUBJ
  7  love write holy-Luke inside two
  8  chapter of-write time
  9  then on-execute

## 183r — Chosroes carries off the Cross

> the Lord Christ, twenty-six years; at that time occupied Jerusalem. One heathen emperor, name was Chosroes; and then he seized upon Jerusalem, the tree of the Cross — the tree upon which Christ executed; and the tree took away into the town of Ctesiphon, into one tower; and then there was war many years upon the Roman emperor, whose name was Heraclius; and then war went [between] this heathen emperor

  1  Lord-~Christ two-ten-ten six-~year time occupy Jerusalem.
  2  one heathen ~emperor name
  3  exist Chosroes and then grab on-Jerusalem
  4  cross tree ~on tree exist Christ
  5  execute and tree SUBJ take_away inside
  6  Ctesiphon town inside one tower
  7  and then exist many year war* on-Roman.
  8  emperor name exist Heraclius
  9  and then war* go this heathen emperor

## 183v — the sign given to Heraclius

> This Roman emperor then had two wars on fighting against each other; and then. Heraclius the emperor had a small army; and then asked, on prayer, can | from, to the Lord, thanks; the Lord God heard, the Lord God, the emperor's prayer; and God's angel cried out upon the water; Heraclius had it; the Lord God heard Heraclius's prayer. And then God's angel [to] Heraclius, daughter, had him write upon his armour the tree of the Cross, and

  1  this Roman emperor then have two war*
  2  on-fight against_each_other and then.
  3  little an_army have Heraclius emperor
  4  and then ask on-~pray can | from-to
  5  Lord thanks Lord_God hear Lord_God of-~emperor.
  6  pray and shout-to God angel on-water
  7  have Heraclius hear Lord_God of-Heraclius
  8  pray and_said God angel Heraclius daughter
  9  have write on-arms cross tree and

## 184r — the battle, and the tower at Ctesiphon

> the emperor won the fight, because the heathen lost, the emperor; and then the two left, this heathen emperor [and] this Roman emperor; and then the two fought | on, chapter, one within, to the Lord, the two; and the heathen people [fought] the people among [one another] died; in turn the Jews, the people; and the heathen to many [the bridge]; and then the heathen people died; and began to pierce [overcame] [baptized] on the heathen earth; and then went Heraclius into Ctesiphon town, to the place, to this heathen emperor Chosroes, because the emperor dwelt within one

  1  win emperor on-fight because lose heathen
  2  emperor and then two leave this heathen emperor
  3  this Roman emperor and then-two fight | on-chapter-+one
  4  inside-to-Lord-two ~and heathen people [fought] people among [one_another]
  5  die in_turn Jew people and heathen SUBJ to-many [the_bridge] and
  6  then people heathen die and begin pierce [overcame]
  7  [baptized] on-heathen earth and then go Heraclius
  8  inside Ctesiphon town on-place to-this heathen
  9  emperor Chosroes because dwell emperor inside one

## 184v — the tower of gold and precious stones

> tower; and the tower was all of gold, and built of precious stone, the tower, how? one God; the emperor sat within, because [he] was put the emperor, on one way, a cock; and the cock was all golden, pouring; the second way the emperor put the cross tree as [it] was on the golden; and then the emperor [of silver] the water ascended up on the tower; and lo, the rain took, the emperor, then wanted the emperor to take, and then the emperor made it within the tower, the year […] and to […] and [precious stones] and among the tree of the Cross

  1  tower and tower exist every golden and gem stone build tower
  2  how? one God sit_inside emperor because exist put
  3  emperor on-one way cock and cock exist every
  4  golden pour second way put emperor cross tree
  5  as exist on-golden and then emperor [of_silver]
  6  water ascend up on-tower and lo rain grab
  7  emperor then-+SUBJ want emperor grab
  8  and then emperor do inside tower.
  9  ~year-[?] and to-[?] and [precious_stones] and among cross tree

## 185r — Chosroes sits between the cross and the cock

> of gold, among the cross, among the cock, the emperor sat, as though one [a cock] from [the other side] the emperor, to God prayed, the Jews, from, because is every world [worshipped as God] and then Heraclius the emperor went [to] this heathen emperor within the tower. And then Heraclius the emperor believed, Heraclius's God, in turn, the whole wide world; this Heraclius, the head; die, he said, this | there was the emperor [slew]; and they beheaded the emperor, and then Heraclius the emperor did all

  1  golden among cross among cock sit emperor
  2  how? one [a_cock] from [the_other_side] emperor
  3  to-God ~pray-Jews from because-exist every world [worshipped_as_God]
  4  and then Heraclius emperor go this heathen
  5  emperor inside tower and_said Heraclius emperor
  6  believe of-Heraclius God in_turn all_the_world this
  7  Heraclius ~head die say this | ~exist
  8  emperor [slew] and emperor behead and
  9  then do Heraclius emperor every

## 185v — the Cross comes back to Jerusalem

> [from the] the tower he pierced; and the tower, God, he took up, and [of Chosroes] [emperor] the son | from one woman; and the son the emperor left [behind] and took the cross tree, and took away into the town of Jerusalem; and then [came] before | the army, the army; and then arrived Jerusalem; and at the gate God's angel, gate, Jerusalem; and the angel shouted to Heraclius: thus the Lord Christ did not carry the tree of the Cross out to Jerusalem in pride, but carried it in humility; and then he sat down [upon an ass]

  1  [from_the] tower on-+pierce ~and tower God up grab
  2  ~and [of_Chosroes] [emperor] son | from
  3  ~woman and son emperor leave [behind] and
  4  grab cross tree and SUBJ take_away inside
  5  Jerusalem town and then [came] before | army
  6  army and then arrived Jerusalem and to-gate God
  7  angel gate Jerusalem ~and shout-to angel Heraclius
  8  this-this Lord-Christ proud out on-Jerusalem carry cross tree
  9  but humble carry and then sit down [upon_an_ass]

## 186r — the emperor takes off his robes

> and took off from the emperor his clothes; and then [put off his shoes] and with bowed head carried the tree of the Cross into Jerusalem; and then God's angel opened the gate of Jerusalem; and the emperor, many [his purple], […] love, the Jews, the cross Cross; and the emperor put the cross within Jerusalem, in the temple; and the emperor prayed, to the Lord thanks, the Lord God, the whole wide world; and there is a man who takes the holy tree of the Cross, the tree; and [set up the] the tree of the Cross; and the cross tree, a feast, through the commandment, on all

  1  and take_off on-~emperor of clothes [and_then]
  2  [put_off_his_shoes] and bowed head carry cross tree inside
  3  Jerusalem and then open God angel gate Jerusalem
  4  and emperor many [his_purple] [?]-love-Jews cross
  5  tree and cross SUBJ put emperor inside Jerusalem
  6  temple and ~pray-~emperor to-Lord thanks Lord_God
  7  the_whole wide world and exist somebody to grab holy-cross
  8  tree and [set_up_the] cross tree
  9  and cross tree feast through commandment on-every

## 186v — the holy Cross against the evil

> the whole world; because this holy cross tree, this cross, our [healed], and our [miracles]; and this holy cross tree, this our [witness] against [these things]; and believe: the devil, the Lord God, that is, against the devil. On the Sunday the Lord God created from the world and

  1  all_the_world world because this holy-cross tree this cross SUBJ our
  2  [healed] and our [miracles] and this holy-cross tree this
  3  SUBJ our [witness] against [these_things] and believe
  4  devil = Lord_God that_is against devil =
  5  inside Sunday
  6  create Lord_God
  7  from world
  8  and

## 187r — the Red Sea

> the angel, within heaven; after these the Lord God, within Sunday, led them through, through dry the Red Sea, by Moses and by Aaron, the Jewish people, from the land of Egypt, from Pharaoh king's earth; and then Moses and Aaron went to the Red Sea. And then glorified, the angel: Moses, hold out this rod over the Red Sea; and then he held it out over the Red Sea; and then | the Red Sea, in the Lord's name, apart left, on two ways; and then through went the people, the Jews, Moses, Aaron, the angel, through the Red Sea.

  1  angel inside heaven = after_these Lord_God inside Sunday
  2  through go-Lord through dry* the_Red_Sea on-+Moses
  3  and on-Aaron Jew people on-Egypt land^
  4  on-Pharaoh king land^ and then Moses
  5  and Aaron to-+the_Red_Sea go and_said
  6  be_glorified^ angel Moses hold_out this stick on-+the_Red_Sea
  7  and then hold_out on-+the_Red_Sea and then | the_Red_Sea
  8  Lord-+name apart leave on-two way and then through go people
  9  Jews Moses Aaron angel through the_Red_Sea

## 187v — Pharaoh in the midst of the sea

> The time Pharaoh the king went into the Red Sea, the king, Pharaoh's army; and then the king went | into the middle of the Red Sea; the time God's angel said: Moses, hold out this rod over the Red Sea; and then he held it out; the time the Red Sea closed in upon Pharaoh the king; and then went Moses and Aaron [stretched out]; after these the Lord God, on the Sunday [stretched out] from the people, who was the Lord's, going | upon [from heaven] the earth; the Lord God took the heavenly manna from heaven, land; and this manna, this bread

  1  time Pharaoh king inside the_Red_Sea go-king
  2  of-Pharaoh an_army and then go-king | on
  3  middle^ the_Red_Sea time say God angel Moses hold_out
  4  this stick on-+the_Red_Sea and then hold_out time
  5  the_Red_Sea shut_in Pharaoh king and then to-go
  6  Moses and Aaron [stretched_out] after_these Lord_God
  7  inside Sunday [stretched_out] from people who exist-Lord on-go-Lord | on
  8  [from_heaven] earth grab Lord_God heavenly manna
  9  from_heaven* land and this manna this SUBJ bread

## 188r — the manna and the bread of this day

> the angel; and this living bread, the people, the Jews | forty years; and how? at table the Jews ate; on the Jews, from eating, left; and then this manna take a bucket; and the Jews [his purple] brought [a vessel] from the manna, glory and godfearing did, the Jews; in turn [came] Christ, stayed, daily [put into it] manna; and then the Lord Jesus within thirty [and a] half three [years]; the time the Lord Jesus said, at the last supper, he took within [his] hands one baked cake, and said the Lord Jesus: and the man [who does] not this bread eat; and the Lord

  1  angel and this bread living people-Jews | forty
  2  year and how? table-Jews eat on-Jews from eat SUBJ leave
  3  and then this manna take* bucket and
  4  Jews [his_purple] brought* [a_vessel] from manna glory^
  5  and godfearing^ do-Jews in_turn [came] Christ stay daily
  6  [put_into_it] manna and then Lord-Jesus inside thirty half*
  7  three time say Lord-Jesus at_the_Last_Supper = grab
  8  inside hands one baked cake and
  9  say Lord-Jesus and man^ not this bread eat and Lord

## 188v — he that believeth not

> believeth not: every such man is damned […]; and a man who is the Lord's believes; and there is a man who from the altar from the thirty, eats the holy host and drinks; he that believeth not, the man is living, for ever and ever, amen. On the Sunday from [the flesh of] Christ came into this world; and before the Lord Christ's coming, nine months and two Sundays; on the Sunday the Lord was announced by the angel Gabriel; within | not Sunday, within the body of the happy Virgin Mary, and | [the holy Trinity] [holy] Joseph; on the Sunday the Lord was

  1  not_believe everybody = be_damned cut_off-[?] and man^ exist Lord
  2  believe and exist man^ from altar exist
  3  from thirty holy-host eat and drink who_believes_not*
  4  man^ exist living for_ever_and_ever = amen
  5  to Sunday from [the_flesh_of] Christ on-this world ~be_born
  6  and before Lord-Christ ~be_born nine moon and two Sunday inside
  7  Sunday the_Lord exist announce by_Gabriel angel inside | not
  8  ~Sunday inside body happy Virgin_Mary and | [the_holy_Trinity]
  9  [holy] Joseph inside Sunday the_Lord exist

## 189r — what was done on the Sundays

> announced, this angel, by the angel Gabriel; and then the Lord | on this world was born; and then the Lord within [his] thirty-first year the time, on a Sunday, the Lord Jesus Christ made at the wedding water into wine; on a Sunday the Lord stood up and raised | the Lord Jesus Christ [raised] the daughter of the first head in Jerusalem, within Sunday the Lord […] upon Carmel, to the mount, and appeared the Holy Spirit within the form of a dove. And then he, of the son, he who the spirit grew calm, and the Lord took the Holy Spirit; and the Lord went into the field

  1  announce this angel by_Gabriel angel and then-Lord | on
  2  this world ~be_born and then-Lord inside thirty one-~year
  3  time inside Sunday create on-wedding Lord-Jesus-Christ
  4  water wine inside Sunday the_Lord stand_up resurrect | Lord
  5  Jesus-Christ daughter first^ head inside Jerusalem inside Sunday
  6  the_Lord from-[?]-[?] on-Carmel to-mount and
  7  appear holy-spirit inside ~form dove and_said
  8  he of son he_who spirit grow_calm and
  9  Lord grab holy-spirit and Lord go inside field

## 189v — Nain, the blind man, the cleansing of the temple

> the Lord Jesus fasted forty days; within Sunday the Lord stood up and raised, the Lord Jesus Christ, in the town of Nain, the son one virgin […] woman; and before, that is, as | was the Lord; this virgin […] woman's son stood up, the Lord resurrected; one blind man he gave light; on a Sunday the Lord Jesus Christ by the wayside Jericho town; then, and the Lord went into Jerusalem, and the Lord's apostles; on a Sunday the Lord cast out, in Jerusalem, on one somebody, hell, evil; then the Lord, in his thirty-third year, on a Sunday the Lord | broke

  1  fast Lord-Jesus forty_days inside Sunday the_Lord
  2  stand_up resurrect Lord-Jesus-Christ inside Nain town son
  3  one virgin-[?] woman and before that_is as | exist
  4  Lord this virgin-[?] woman son stand_up resurrect-Lord one
  5  ~blind through light inside Sunday Lord-Jesus-Christ by_the_wayside*
  6  Jericho town then and go-Lord inside Jerusalem and
  7  of-Lord apostle inside Sunday the_Lord ~exorcise-Lord inside Jerusalem
  8  on-one somebody hell evil then-Lord
  9  inside thirty half three inside Sunday the_Lord | break

## 190r — the week of the Passion, day by day

> the Lord, five baked bread, five thousand people; then the Lord within thirty-three and a half [years], from Galilee through the Red Sea to one mount; on a Sunday the Lord was going, the Lord, to suffer within Jerusalem; then the Lord within thirty- three and a half [years]; on the Monday the Lord preached many a miracle; in turn on the Tuesday the Lord stood up and raised Lazarus from the tomb; in turn on the Wednesday the Lord, but was Judas, sold for thirty silver [pieces]; in turn Thursday, the dinner, the Lord did; and captured the Lord; in turn Friday the cross […]; and the evil one was bound; in turn on the Saturday, hell

  1  Lord five baked bread five_thousand people
  2  then-Lord inside thirty half three from Galilee
  3  through the_Red_Sea to-one to-mount inside Sunday
  4  the_Lord exist go-Lord on-suffer inside Jerusalem then-Lord inside thirty
  5  half three inside Monday the_Lord many miracle preach-Lord in_turn
  6  Tuesday the_Lord Lazarus on-tomb stand_up resurrect-Lord in_turn Wednesday
  7  Lord-~but-+SUBJ exist Judas sell to-thirty silver
  8  in_turn Thursday dinner-to do-Lord and capture-Lord in_turn
  9  Friday on_the_cross-[?] and evil bound_up in_turn inside Saturday hell

## 190v — the five appearances, and Emmaus

> the Lord destroyed; on the Sunday the Lord rose from the dead; and to the apostles the Lord appeared. First the Lord appeared in Bethany | to the virgin Mary; second, the Lord appeared at the tomb [to] Mary Magdalene; third the Lord appeared on the way […] the people at Jerusalem; fourth, the Lord appeared [to] two apostles; then the two apostles, and went, within Sunday, at Jerusalem, into one town; and the name of the town was Emmaus; in turn the apostles | and is, chapter, by name of the year were Luke and Cleopas; and was I one apostle; bread and grape and water; blessed the Lord Jesus; on the Sunday the Lord appeared a fifth time, in Jerusalem, to the ten apostles | of

  1  SUBJ destroy-Lord inside Sunday the_Lord rise on-die and apostle the_Lord
  2  appear-Lord first the_Lord appear inside Bethany | virgin
  3  Mary second the_Lord appear to-tomb Mary Magdalene third
  4  the_Lord appear on-way [?]-[?] people
  5  on-Jerusalem second-two the_Lord appear two apostle then two
  6  apostle and go inside Sunday on-Jerusalem inside one town and
  7  ~brother-+name town exist Emmaus in_turn apostle | and-exist-chapter
  8  ~year-+name exist Luke and Cleopas and ~exist-I one
  9  apostle bread and grape and water bless Lord-Jesus
 10  inside Sunday the_Lord five appear inside Jerusalem ten apostle | of

## 191r — the Ascension, and the two men in white

> the Lord, the gate; and then, after the Lord Christ's execution, in the eighth year, the time the Lord Jesus appeared, on a Sunday, in Jerusalem, to the Lord's twelve apostles, to the whole wide world, and to Thomas; and then, after the Lord Christ's execution, | in the twentieth […] year, the time the apostles sat at table in Jerusalem, in the Lord's house where the Lord God, the Lord Jesus, made the supper; the time there appeared two, from the putting to death of the Lord Christ until | […] […] year; and to leave to the Lord's Father, from heaven, town, chapter, in turn; and there appeared two angels in white clothes, And then the two angels, angel [and] angel: you [of] Galilee,

  1  Lord gate and then on-execute Lord-Christ six-two-year time
  2  appear Lord-Jesus inside Sunday inside Jerusalem six-six apostle of-Lord
  3  to-all_the_world Thomas and then on-execute Lord-Christ | one-ten-+one-ten
  4  [?]-year time sit apostle at_table inside Jerusalem inside Lord house
  5  where Lord_God Lord-Jesus dinner do time appear
  6  two-?from execute Lord-Christ until | [?]-[?]
  7  year and to-leave to-of-Lord the_Father from_heaven* town-chapter-in_turn
  8  and two appear two angel-angel white clothes
  9  and_said two angel-angel you Galilee

## 191v — why stand you looking up to heaven?

> men, how? the Lord's joy see [so shall he come]; left on heaven | town before this joy wants the Lord [shall come] on the year of judgment, to judge the living and the dead; this word from the Lord, the living Lord; and on this world | went away went into heaven, in turn […] the Lord, with all thy heart, the Lord God, with all thy heart, pleasing and thanks. This holy gospel begins, written by holy Luke in the second chapter of the writing: the time, because the time the Virgin Mary, on the birth of the Lord Jesus | […]

  1  man how? Lord joy see [so_shall_he_come] leave on-heaven | town
  2  before this joy want-Lord [shall_come] on-+judge-year judge the_living
  3  and dead this word SUBJ from Lord living-Lord and on-this world | go_away
  4  Lord on-heaven ~land Lord be_loved Lord_God be_loved pleasing and thanks
  5  here_begins this holy_gospel
  6  write holy-Luke
  7  within^ two chapter of-write
  8  time because time
  9  Virgin_Mary on-~be_born
 10  Lord-Jesus | [?]-[?]

## 192r — Simeon in the temple

> year; at that time the wife, the Virgin Mary, carried within [her] bosom into the temple the Lord Jesus; because not this girl [to] destroy, truly the Lord; but wanted the girl out [by the Spirit] the salvation of the Jews; and then the girl went to this temple; the time Simeon went into the temple, by the Holy Spirit, in mercy, and came the Virgin Mary. And then Simeon, the Virgin Mary, Simeon took this son, more than these, this son, Simeon; [into his arms] carried the son within Simeon's hands; and knelt before the Lord Jesus, and asked the Lord for mercy; And then Simeon: Lord, dismiss the Lord's servant in peace

  1  year time carry wife Virgin_Mary inside bosom in temple
  2  Lord-Jesus because not this-girl destroy righteous Lord ~but want-girl
  3  out [by_the_Spirit] from-salvation Jew and then girl go this temple
  4  time go Simeon inside temple on-holy-spirit find_mercy^
  5  and come Virgin_Mary and_said Simeon Virgin_Mary
  6  grab-Simeon this son more_than_these* this son Simeon
  7  [into_his_arms] son carry inside of-Simeon hands and kneel
  8  Simeon before Lord-Jesus and Lord find_mercy^ ~ask
  9  and_said Simeon Lord dismiss^ servant of-Lord peace SUBJ

## 192v — mine eyes have seen thy salvation

> Simeon, because see two, Simeon's eyes, saved | of Simeon; and holy Simeon blessed the Lord Jesus; and Simeon's Simeon the Lord had mercy; and the Lord took [him] within [his] bosom and the Lord carried him into the temple at Jerusalem; and then into the temple went the Lord, Simeon and Mary; and Simeon raised the Lord Jesus within Simeon's hands. And then Simeon: lo, from the Lamb; and the Lord went upon heaven and earth, on this world the Lord Jesus Christ; and from the Lord, on the cross […]; and on the Lord is blessing, all the whole world; and blessing is; left ever

  1  Simeon because see two of-Simeon eyes be_saved | of
  2  Simeon and bless Lord-Jesus holy-Simeon and sin
  3  Simeon have_mercy-Lord and Lord take^ inside bosom
  4  and Lord carry inside Jerusalem temple and then inside temple
  5  go-Lord-Simeon-Mary and raise Simeon Lord-Jesus
  6  inside of-Simeon hands and_said Simeon ~lo from
  7  lamb and the_Lord go-Lord on-heaven land
  8  on-this world Lord-Jesus-Christ and from Lord on_the_cross-[?] and on-Lord exist
  9  bless every ~all_the_world world and bless exist leave^ ever

## 193r — Simeon carries the news to the fathers in hell

> ever, amen. Here ends this holy gospel. The Lord God love this. out [of] Moses, truly, within one chapter, who is written, written: holy Simeon, three on this world, Simeon went away, said: Christ, the apostles of the Lord announce; Simeon within the netherworld, the holy fathers, | on the coming of the Lord: and see, you are saved, and many judge are within the netherworld, from the forefathers and the holy prophets. Written; and from the holy gospel, that is, […] down, the Lord; I, the holy gospel: I [the] grape on the water created; I [gave] the blind light through; I cast the evil out of the people; I [raised] the dead, rise, resurrect; various lepers the Lord healed; I, the cross, the holy gospel.

  1  ever amen here_ends this holy_gospel Lord_God SUBJ love this EOL
  2  out Moses righteous inside one chapter who exist write write EOL
  3  holy-Simeon three on-this world go_away-Simeon say Christ apostle EOL
  4  of-Lord announce SUBJ Simeon inside netherworld holy-the_father | on-+EOL
  5  ~be_born of-Lord and see be_saved you and many EOL
  6  judge-+SUBJ exist inside netherworld from forefather and prophet-holy. EOL
  7  write and from holy-gospel that_is [?]-°down Lord I holy-gospel EOL
  8  I grape on-water create I blind through light EOL
  9  I evil on-people exorcise I dead EOL
 10  rise* ~resurrect various leper heal-Lord I cross holy-gospel

## 193v — the call of Matthew at the receipt of custom

> This holy gospel begins, written by holy Matthew, in the […] chapter of the writing: the time, then the Lord Jesus within thirtieth year, the time he preached in | there was afterward, one; and then the Lord Jesus [was] teaching in Capharnaum, and left, down, on preaching; and [many] followed the Lord. to him; and then the Lord went into the town, and saw, the Lord Jesus, at the publican's [place], sat holy Matthew. And then the Lord Jesus

  1  here_begins this holy_gospel
  2  write holy-Matthew inside and
  3  chapter of-write time
  4  then Lord-Jesus inside
  5  thirty years* time
  6  preach inside | ~exist
  7  °afterward-+one and then teaching Lord-Jesus inside Capharnaum
  8  and leave down on-preach and follow^ to-Lord
  9  many people and then go-Lord on-town and see
 10  Lord-Jesus on-publican sit holy-Matthew and_said Lord-Jesus

## 194r — he sat at meat in the house

> Matthew went to the Lord, to the food, to the place; holy Matthew rose, and Matthew went to the Lord Jesus; and the Lord went with Matthew to holy Matthew's house, and did, from many, to the table company; how? Speaks holy Luke: did, from many, to the table. company; and there went to the Lord the Jews, the Pharisees, and the tax collectors, the chief men; and together with the Lord Jesus they drank and ate, the sinners; and the Jews began, the Pharisees spoke [to] the Lord's disciples: this you, Master, save sinners? In turn, then, he is

  1  Matthew go to-Lord on-food to-place rise holy-~Matthew and
  2  go-Matthew to-Lord-Jesus and go-Lord-Matthew holy-~Matthew house
  3  and do from-many-to table company how?
  4  speak holy-Luke do from-many-to table.
  5  company and go to-Lord Jew pharisee and
  6  publican exist head and together Lord-Jesus drink
  7  and eat sinners* and begin Jew.
  8  pharisee speak disciple^ of-Lord this you Master
  9  sinners* save in_turn then he exist

## 194v — they that are well need not a physician

> and the Lord said: he is a sinner, not from the Lord's salvation; and the blind to the Lord Jesus [they that are well] got angry. And then the Lord Jesus [answered] to the Lord: I go, the Lord, to the just man on this world, but to sin. And then the Lord Jesus: you, just man. And then the Lord Jesus: need, the healthy, healing; but rather need. one sin, is this health. Here ends this holy gospel. written by holy Matthew in the […] chapter. Holy Paul speaks and says: | the Lord Jesus Christ, from the beginning of the world, from Adam's creation, | to [until] the coming of the Lord Jesus Christ into this world [then]

  1  and Lord say he exist sinner^ not from-salvation-Lord and
  2  ~blind-to Lord-Jesus [they_that_are_well] get_angry and_said Lord-Jesus [answered]
  3  to-Lord I go-Lord to-just_man on-this world but to-sin
  4  and_said Lord-Jesus you just_man and_said
  5  Lord-Jesus need the_healthy healing but_rather need.
  6  one-sin ~exist-this health here_ends this holy_gospel
  7  write holy-Matthew inside and chapter holy-Paul speak say | Lord
  8  Jesus-Christ from* beginning world from* ~Adam create | to
  9  [until] ~be_born Lord-Jesus-Christ on-this world [then]

## 195r — from Adam to the coming of Christ

> truly, the man; and one prophet, and one forefather, and one holy father, holy living; and one | [prophet] the father […] in heaven; but rather, then, at the coming of Christ into this world, and then, in his thirtieth day, the time […] the Lord Jesus upon Carmel, the mount; and then out, thirty-three and a half [years]; at that time he was crucified, and on the third day stood up from the dead; and many holy prophets and holy forefathers and holy fathers, holy living, out of the netherworld | to the Lord went; and then, forty days; at that time to leave

  1  righteous somebody and one prophet and one forefather
  2  and one holy-father holy-living and one | [prophet]
  3  father-[?]-[?]-[?] inside heaven =
  4  °but_rather-+one then ~be_born Christ on-this world and then inside
  5  thirty day time from-[?]-[?] Lord-Jesus on-Carmel
  6  mount and then out thirty half-three time
  7  crucified and on_the_third_day from die stand_up and many holy-prophet
  8  and holy-forefather and holy-father holy-living on-netherworld out | to
  9  go-Lord and then forty_days time to-leave

## 195v — he shall come to judge the quick and the dead

> to the Lord's Father, on the heavenly kingdom; | sat down the Lord, the Father, on the right; from there has the Lord [to] go, the Lord, to judge the living and the dead; and before the ascension he blessed all the whole world. This holy gospel begins, written by holy Matthew | [sixteen] the fourth chapter of the writing: the time, then, | the Lord Jesus, thirty-three and a half [years]; at that time said the disciples [to] the Lord Jesus: Master, who is to the Lord, he, on Holy, within heaven's

  1  to-of-Lord the_Father on-heaven kingdom^ | sit_down
  2  Lord the_Father on-right from_there have-Lord go-Lord judge
  3  the_living and the_dead and before ascension bless every all_the_world
  4  world here_begins this holy_gospel.
  5  write holy-Matthew | [sixteen]
  6  two-two chapter of-write.
  7  time then | Lord
  8  Jesus thirty half-+three time say disciple^ Lord-Jesus.
  9  Master who? exist to-Lord he on_Holy inside heaven

## 196r — except you become as little children

> kingdom? because the disciples recognized as the Lord crucified; and on the third day stood up from the dead; and the Lord to these apostles, to judge who is to the Lord, he, on Holy, within heaven; and the Lord Jesus called one little son, and the son the Lord Jesus set upon the head, the Lord's hands. And then the Lord Jesus: who [is] not this humble | how this little son, one [is] not saved. The time the Jews brought one | before | the Lord Jesus, from this emperor, to whom, and he was a pagan.

  1  kingdom^ because recognize disciple^ as Lord crucified and
  2  on_the_third_day from die stand_up and Lord to-this disciple^ judge
  3  who? exist to-Lord he on_Holy inside heaven =
  4  and call^ Lord-Jesus one little son.
  5  and son SUBJ put_on Lord-Jesus on-head.
  6  of-Lord hands and_said Lord-Jesus who-not this humble | how?
  7  SUBJ this little son one not be_saved
  8  time carry Jew one | before | Lord
  9  Jesus from* this emperor to-+who-to and exist pagan.

## 196v — the keys, and whatsoever thou shalt bind

> Because he heard from every man, upon one | before; this was: the Lord Jesus gave the key of salvation [to] holy Peter; said | the Lord Jesus: who[m] this Peter binds on this world, from the man is bound, and from heaven's kingdom; in turn who[m] this Peter absolves on this world, from the man is absolved, and from heaven's kingdom. And then the Lord Jesus: he who [is] on Holy, the Lord, you from the Lord, every [one] a servant. And then the Lord Jesus: who [does] not this apostle, from this little son, does

  1  because hear from everybody = on-one | before this exist
  2  give^ Lord-Jesus key be_saved holy-Peter say | Lord
  3  Jesus who this-Peter bind on-this world from
  4  man^ exist bind and from_heaven* kingdom^
  5  in_turn who this-Peter absolve on-this world from
  6  man^ exist absolve and from_heaven* kingdom^
  7  and_said Lord-Jesus he_who on_Holy Lord you from
  8  the_Lord every servant and_said Lord-Jesus who-not this
  9  disciple^ this from little son to* do

## 197r — their angels always see the face of my Father

> within the Lord's name, [by] name, and one [is] not saved. And then the Lord Jesus, the Lord's apostles, not apostles, and one [despise not] [little ones] do. And then the Lord Jesus [to the] apostles: of the Lord: happy are the people, and the angels see the face of the Lord's Father, the will, from the people; and the angels on seeing the face of the Lord's Father. Here ends this holy gospel. This holy gospel begins, written by holy Matthew: the time | the Lord Jesus said to the Lord's apostles, and to the Jewish

  1  inside of-Lord ~brother-+name and one not be_saved
  2  and_said Lord-Jesus apostle of-Lord not apostle and one
  3  [despise_not] [little_ones] do and_said Lord-Jesus apostle
  4  of-Lord happy from people and angel see face
  5  of-Lord the_Father will from-people and angel on-see.
  6  face of-Lord the_Father here_ends this holy_gospel
  7  here_begins this holy_gospel write
  8  holy-Matthew time say | Lord
  9  Jesus apostle of-Lord and Jew

## 197v — take up his cross and follow me

> people; and the apostles, somebody, the Jews: [who] want to go to the Lord | deny the man, our all the world; and take our cross on our shoulder; and go, somebody, to the Lord. And then the Lord Jesus: who [is] this man, profit, and this world | rich [for what] then this man takes our soul | to riches [for what]. And then the Lord Jesus: good this man releases | of the man's soul; damned, but saved, because many a man; and the man is [in exchange] [for his soul] [shall render] saved, every the man damned [according to] [his works]; the man is judged, the Jews

  1  people and apostle-somebody-Jew want to Lord go | deny
  2  man^ our all_the_world and grab our
  3  ~cross on-our shoulder and go-somebody to
  4  Lord and_said Lord-Jesus who this man^ profit and this world | rich
  5  [for_what] then this man^ SUBJ grab our soul | to-rich
  6  [for_what] and_said Lord-Jesus good SUBJ this man^ release* | of
  7  man^ soul be_damned ~but be_saved because many man^
  8  and man^ exist [in_exchange] [for_his_soul] [shall_render] be_saved-somebody every
  9  man^ be_damned [according_to] [his_works] man^ exist judge Jews

## 198r — go into all the world

> to damnation; everybody saved. And then the Lord Jesus: you not, Jews, every until this belief, Jews, who I you, preach the Lord, every until this [look upon]; the Jews see, go on this world, from prayer, the Son of God within the body, somebody, in the year of judgment, every until this […] believe. And then the Lord Jesus [answered him] Peter, one among you; and the apostles | see, the apostles, from prayer, the Son of God, within […] the man, and the apostles are within the son; the apostles ask. Here ends this holy gospel.

  1  on-be_damned everybody = be_saved and_said Lord-Jesus you
  2  not-Jews every until this-believe-Jews who
  3  I you preach-Lord every until
  4  this [look_upon] see-Jews go on-this world from pray
  5  son God inside body somebody on-judge-year every until
  6  this-[?] believe and_said Lord-Jesus [answered_him]
  7  Peter one among you and apostle | see
  8  apostle from pray son God inside ~exist-[?] somebody
  9  and apostle exist inside son ~ask-apostle end
 10  this holy-gospel

## 198v — write your names in the eternal land

> Said the Lord God to the angel | of the Lord, holy […] the prophet, and | holy Elijah the prophet [was taken up] | the Jews the apostles, somebody, to the Lord: I. you […], Lord, have mercy on sin [fruit] this is within the commandment, somebody, that is; and has somebody observing the commandment of God, does not commit sin; somebody is saved, many | sufferings not, for ever and ever, amen. Writes the names ours within heaven, to the house; dies, in turn | on death, the body and the soul, for ever and ever, amen.

  1  say SUBJ Lord_God on-angel | of
  2  Lord holy-NAME.prophet prophet and | holy
  3  Elijah prophet [was_taken_up] | Jews
  4  apostle-somebody to-Lord I.
  5  you [...] Lord sin have_mercy [fruit] this exist
  6  inside commandment somebody that_is and have somebody observe commandment
  7  God not_commit sin somebody be_saved many | suffering
  8  not for_ever_and_ever = amen write SUBJ name
  9  our inside heaven = to-house die in_turn | on
 10  die body and soul for_ever_and_ever = amen

## 199r — a man had a vineyard and two sons

> This holy gospel begins, written by holy Matthew | in the twentieth, in the fifth chapter of the writing: the time, then the Lord Jesus within thirty-three and a half [years], the time the Lord Jesus preached in Jerusalem; and the Lord Jesus said to the apostles of the Lord, and to the Jewish people: the kingdom of heaven left a man land. And then the Lord Jesus: there was [a vineyard] one rich man, a vineyard; and then he had

  1  here_begins this holy_gospel
  2  write holy-Matthew | one
  3  ten-+one-ten inside five chapter
  4  of-write time
  5  then Lord-Jesus inside
  6  thirty half-three
  7  time preach Lord-Jesus inside Jerusalem and say Lord-Jesus apostle
  8  of-Lord and Jew people leave king man^ heaven
  9  land and_said Lord-Jesus exist [a_vineyard]
 10  first^ rich-somebody vineyard and then have

## 199v — go work today in my vineyard

> two sons, the pagan [and] the Jew. And then this rich somebody | of the Lord, somebody, son, on the Jews [go work today], brought the son into | the Lord's, from the man's vineyard to cultivate; said, brought the son to this: go, Jews. And then this rich somebody […] […] the second, to the son, […] somebody, into the Lord's somebody's vineyard, vinedresser. And then the priest, and […] […] the man; and said the Lord Jesus to the high priest and to the Lord's apostles: judge, Lord, I [ask] you: who this good? Say. Said the high priest: which good? He who

  1  two son pagan Jew and_said this rich-somebody | of
  2  Lord-somebody son on-Jews [go_work_today] brought-son inside | of-Lord-from
  3  man vineyard cultivate say brought-son to-this ~go-Jews
  4  and_said this rich-somebody [?]-[?] two to-~son
  5  [?]-somebody inside of-Lord-somebody vineyard vinedresser^ and_said
  6  priest* and [?]-[?] [?]-somebody and say
  7  Lord-Jesus high_priest = and apostle of-Lord judge-Lord
  8  I you who? SUBJ-this good say.
  9  say high_priest = who? SUBJ good say he_who

## 200r — he let out the vineyard to husbandmen

> said, to the pagan, the priest; and whosoever would be named, in turn went to the pagan; And then the Lord Jesus, rightly, the Jews spoke; and the rest said the Lord Jesus a parable, and said: there was, taken, one rich lord, on lease the Lord's vinedresser, the vinedresser, the Lord's vineyard; and then the vineyard, the Jews, many years carried, the Jews, to the Jews to take, to release the vineyard lease. And then this rich Lord | of the Lord's servants, prophets and angels, the prophets and angels went, this lease from the Jews to ask, the prophets, the angels; and | the prophets, the angels, the lease to the Jews, the Jews took, than

  1  say-to-+pagan priest* and name-+who-want in_turn go-to-+pagan
  2  and_said Lord-Jesus righteous-Jews speak and the_rest^ say Lord-Jesus
  3  parable say exist take^ one rich-Lord on-lease
  4  of-Lord vinedresser vinedresser^ of-Lord vineyard and then
  5  vineyard-Jews many year carry-Jews to-Jews take^ release^
  6  vineyard lease and_said this rich-Lord | of
  7  Lord servant prophet and angel go-prophet-angel this lease
  8  from* Jews ask-prophet-angel and | prophet
  9  angel lease to-Jews grab-Jews than

## 200v — last of all he sent his son

> they killed all; and the Lord's son went; this rich lord said to this son: are, the Jews, having, would say, the lease the Lord takes; and then the Lord was, the Jews saw, and went; and the son. said. And then the Jews: this is the son from [the heir] the vineyard, the father's son [cast him out]; and this son is the vineyard; carry. And then the Jews: go, die. the Jews; and [sent] to the Lord; and the son died, the Jews; and then was until [killed him]; and the Jews, the head: how? he said; spoke the Lord Jesus; and thirdly the Lord Jesus said a parable,

  1  every kill^ and go-Lord of-Lord son this rich-Lord say this son
  2  exist-Jews have would_say* lease Lord take^
  3  and then-Lord exist-Jews see and go and son.
  4  say* and_said-Jews this_is son from [the_heir]
  5  SUBJ vineyard the_father-~son [cast_him_out] and this
  6  son exist vineyard carry and_said-Jews go-die
  7  Jews and [sent] to-Lord and son die-Jews and
  8  then exist until [killed_him] and Jew ~head
  9  how? he_said* speak Lord-Jesus and three say Lord-Jesus parable

## 201r — the marriage of the king's son

> and said: there was one king in a land, and then he had one son; and the king would make a wedding; prayed; and then [he] called, this king, all the Lord king's, land, to this wedding; and | then, not one went on this wedding. Grew angry this king. And then, that is, the people; and excused [themselves], the people, of the Lord's table; in turn all the world, to dinner. And then the Lord Jesus: who did this king? He said to the Lord's servants: all, from the town, destroy [with] fire and water. And then this king

  1  say exist one king inside kingdom^ and then
  2  have one son and son would_like^ king
  3  wedding pray and then call^ this king
  4  every of-Lord king ~land on-this wedding and | then
  5  not one go on-this wedding grow_angry this
  6  king and_said that_is people and excused people
  7  of-Lord table in_turn all_the_world dinner-to and_said Lord-Jesus who do
  8  this king say of-Lord servant every from town.
  9  destroy fire and* water and_said this king

## 201v — go out into the highways

> said to the Lord's servants: go, and speak this word, to the understanding, to the hidden; leave; and is called on this wedding. And then this Lord king's servants went, to the blind, to the hidden, and the way, and to the town; and they found the poor man of God, ninety, blind, and still more […] and the hungry and the thirsty, and [feeble] the poor of God, and [go ye] [into the highways] the servants found; all the servants went, filled within the Lord king's house; and then filled the house, this king, the various heaven

  1  of-Lord servant go and this word speak-understand-hide exist
  2  leave and exist call^ on-this wedding and_said
  3  this Lord-king of-Lord servant go-~blind-hide and
  4  way and on-town and find
  5  poor_man_of_God = ninety-~exist blind and still_more-[?]-to and
  6  hunger and thirst and [feeble] poor_man_of_God = and
  7  [go_ye] [into_the_highways] find servant every go-servant
  8  filled* inside of-Lord-king house and then fill
  9  house this king various heaven

## 202r — the man without a wedding garment

> Lord; and this king said, this king; and the king went into the Lord king's house; the king would go before, out of the Lord king's house; and then this king went into the Lord king's house; and this king saw one man of God in ragged clothes; and thus the king said: this friend, name, sat, to whom, one, which man [the king came in] the man went [a wedding garment] the man, friend, the wedding clothes, by name, which this man

  1  Lord and say this king this-king and go-king inside
  2  of-Lord-king house want-king to-before on-~out
  3  of-Lord-king house and then ~go this king
  4  inside of-Lord-king house and see this king
  5  one God-somebody ragged clothes and
  6  say that_is king this friend name-°sat-to_whom-+one who man^
  7  [the_king_came_in] go-somebody [a_wedding_garment] man^ friend
  8  wedding clothes to-+name who this man^

## 202v — bind him hand and foot

> said, within the Lord God's heaven house, found, the year; good, said this king, Gabriel, friend, brother by name, this most high, to, sat, the will; Gabriel spoke and said: bind the man's hands and feet, and cast the man out, the angel, outside, darkness there is seen the grinding of teeth, weeping, ever ever. Here ends this holy gospel. The Lord God, be loved. This holy gospel begins, written by holy Matthew, [twenty-two] chapter | of the writing: the time, then, | the Lord Jesus, thirty-three and a half [years]; at that time

  1  say inside of-Lord_God heaven house find-~year good say this king
  2  Gabriel friend brother-+name this-high to-°sat will
  3  speak-~Gabriel say bind^ somebody hand and.
  4  foot and somebody cast_out angel on-out darkness
  5  there exist see grinding tooth weep ever
  6  ever here_ends this holy_gospel Lord_God be_loved
  7  here_begins this holy_gospel write.
  8  holy-Matthew [twenty_two] chapter | of.
  9  write time then | Lord
 10  Jesus thirty half-three time

## 203r — is it lawful to give tribute to Caesar?

> The Lord Jesus preached in Jerusalem, and the Jews came to him, | to the Lord Jesus. And then the Jews: Master, the Jews [Master] [we know] true the man; and truly the Lord is a prophet, because truly in God's way the Lord goes; and the Lord has the king and the emperor [teachest]; go, the Lord's name, learn; how? learn, the Jews, learn | want the Lord take from what they would do? | […] the Jews: take from everybody one drachma [for] the heathen emperor? And said the Jews: how? learn, the Jews, learn. Would the Lord take from what they would do? Said

  1  preach Lord-Jesus inside Jerusalem and to-leave Jew | to-Lord
  2  Jesus and_said Jews Master-Jews [Master] [we_know] true^
  3  man^ and righteous-Lord prophet because true^ God way
  4  go-Lord and divine_one^ ~have king and emperor
  5  [teachest] go name-Lord learn how? learn-Jews-learn | want
  6  divine_one^ grab from would_say* do | [?]-[?]
  7  Jews grab from everybody = on-one drachma.
  8  emperor heathen and say-Jews how? learn-Jews-learn
  9  want-Lord grab from would_say* do say

## 203v — whose image and superscription?

> the Lord Jesus: carry, Jews, [to] the Lord the tax; and the Jews carried before the Lord Jesus. And then the Lord Jesus: whose this image? Said the Jews: this is the emperor's image. And then the Lord Jesus: whose this writing? Said the Jews: this is the emperor's writing. And then | the Lord Jesus: this is the emperor's image; and the emperor's writing; this emperor['s] until leave. And then | the Lord Jesus: who […] indebted [to the] emperor [whose image] [to] the emperor, take […]; in turn | love, the Jews, the apostle.

  1  Lord-Jesus carry-Jews Lord tax and carry-Jews
  2  before Lord-Jesus and_said Lord-Jesus whose?-+SUBJ this
  3  image^ say Jew this_is ~emperor image^
  4  and_said Lord-Jesus whose?-+SUBJ this write say
  5  Jew this_is ~emperor write and_said | Lord
  6  Jesus this_is ~emperor image^ and ~emperor
  7  write this ~emperor until leave and_said | Lord
  8  Jesus who-[?] indebted ~emperor [whose_image]
  9  emperor grab-[?] in_turn | love-Jews-apostle

## 204r — render to God the things that are God's

> the man owes God; this, God, take it. And then the Lord Jesus: is believing […] the emperor, and God; and somebody, from being indebted, pray not he takes […]; if he owes […] Here ends this holy gospel. Said the Lord Jesus: there is humble head, the Lord God, the emperor […], this world; and take […], the Lord God, the emperor […], who the Jews […], and indebted […], because this from the Lord God, the emperor […], you [render]

  1  somebody indebted God this God grab-[?]
  2  and_said Lord-Jesus exist ~believe-[?]
  3  ~emperor and God and somebody from indebted pray not
  4  grab-[?] ~if indebted-[?]
  5  here_ends this holy_gospel say Lord-Jesus exist-[?]
  6  humble head Lord_God-~emperor-[?] this world and
  7  grab-[?] Lord_God-~emperor-[?] who
  8  Jews-[?] and indebted-[?] because this
  9  from Lord_God-~emperor-[?] you [render]

## 204v — what a man owes the Church

> from heavenly belief, baptized, somebody remits; the heathen out; believe, baptized, somebody; and | […] the apostles somebody; and the Lord God, the emperor, king | humble, the Jews, the apostle. the man; and he owes the Church, this man, [shall be gathered]; in turn, on, on Holy church; and of […] the Lord, the earth; in turn, before, secondly the Jews […] indebted [to] the church, this somebody, on [shall stand] before our spirit, the Father; and the Father, this somebody makes [his] way before the Lord's | Father

  1  from heavenly* believe baptize somebody remit heathen
  2  out believe baptize somebody and | [?]-apostle
  3  somebody and Lord_God-~emperor-king | humble-Jews-apostle.
  4  somebody and indebted-[?] church this somebody
  5  [shall_be_gathered] in_turn on on_Holy church and
  6  of-[?] Lord earth in_turn before two
  7  Jews-[?] indebted church this somebody on
  8  [shall_stand] before our spirit the_father and father this
  9  somebody way do before of-Lord | the_father

## 205r — fasting, the ten commandments, and thanks

> the divine one; third, the Jews […] indebted, take | of somebody['s] fast, and our prayer, and the ten commandments of the Lord's Father; and indebted […] to kneel before the Lord's Father [shall be gathered] and the man owes the Lord prayer, humble, the Lord's pleasing and gives thanks; and to the Lord all heaven and earth; and somebody does not take the head, the Lord, from the emperor, the king, the world, who [is] indebted; somebody is believing, somebody, every Lord and every emperor and every king, every believer

  1  DIV third Jews-[?] indebted grab | of
  2  somebody-fast and our pray and ten commandment
  3  of-Lord the_Father and indebted-[?] kneel
  4  before of-Lord the_Father [shall_be_gathered] and
  5  indebted-somebody Lord pray ~humble Lord pleasing
  6  and give_thanks = and to-Lord every heaven land
  7  and somebody not_take head Lord from emperor king
  8  world who indebted somebody exist ~believe-somebody
  9  every Lord and every emperor and every king every believe

## 205v — Jericho

> baptized, the man [unto] the Lord's Father. Here ends this holy gospel; and learning, the holy gospel. The Lord God, be loved. This holy gospel begins, written by holy Luke, in the ninth end of numeral chapter of the writing: the time, then, the Lord Jesus, thirty, in one day; the time | the Lord Jesus went into another town; and this town's name was Jericho; and then

  1  baptize man^ [unto] of-Lord the_Father
  2  here_ends this holy_gospel and learn holy-gospel Lord_God be_loved
  3  here_begins this holy_gospel
  4  write holy-Luke inside
  5  nine end_of_numeral* chapter of-write
  6  time then
  7  Lord-Jesus thirty inside one
  8  day time go | Lord
  9  Jesus inside one another town and this town
 10  name exist Jericho and then

## 206r — Zacchaeus climbs the tree

> the Lord Jesus kept going, the town of Jericho; and then in Jericho there was one chief tax collector, and the man's name was Zacchaeus; and then the Jews saw the Lord; the Lord Jesus went into Jericho; and Zacchaeus could not see the Lord Jesus, but from [chief publican] Zacchaeus, this many people; and [he] climbed one tree, because [little of stature] Zacchaeus […] the Lord Jesus went; and then the Lord Jesus went to this tree, and the Lord Jesus saw

  1  go_on Lord-Jesus Jericho town and then inside
  2  Jericho one publican head and.
  3  ~brother-+name man^ exist Zacchaeus
  4  and then Lord see-Jews go Lord-Jesus inside Jericho
  5  and Lord can see Zacchaeus Lord-Jesus
  6  but from [chief_publican] Zacchaeus this many people
  7  and ascend one tree because [little_of_stature]
  8  Zacchaeus [?]-go Lord-Jesus and then
  9  go Lord-Jesus to-this tree and see Lord-Jesus

## 206v — make haste and come down

> Zacchaeus abiding on this tree; And then the Lord Jesus: Zacchaeus, go down, I today [must] be, the Lord, within Zacchaeus's house, table, year, the Lord; and [with] joy left. Zacchaeus; and he came down, this Zacchaeus; and went the Lord, the apostles, Jesus, into Zacchaeus's house; and | from name of the Lord Jesus, […] out, year, the Lord sat; and the Jews began to murmur on the Lord Jesus, the high priest; he said:

  1  Zacchaeus abide^ on-this tree
  2  and_said Lord-Jesus Zacchaeus go down
  3  I today exist-Lord inside of-Zacchaeus
  4  house table-~year-Lord and joy leave.
  5  Zacchaeus and go down this.
  6  Zacchaeus and go-Lord-apostle-Jesus inside
  7  Zacchaeus [?]-+who-to house and | from
  8  name Lord-Jesus [?]-~out-~year sit-Lord and begin-Jews
  9  murmur on-Lord-Jesus high_priest = he say

## 207r — the half of my goods I give to the poor

> the Son of God, in turn, with one sinner, from one an extorter, one extorts; and [he] stood up | name, Jerusalem, Zacchaeus. And then Zacchaeus: Master, this Zacchaeus takes the half, unrighteously of Zacchaeus's riches, God, the poor in spirit, undeservedly; in turn [he] stood up, one among you, in turn, chapter, Jerusalem [half my goods] | take, Zacchaeus, one denarius; on extorting, want, chapter, Jerusalem, the man, to every [one] four take. And the Lord Jesus saw, as

  1  son God in_turn one sinner^ from-one
  2  extorter* one extort and stand^ up | name-Jerusalem
  3  Zacchaeus and_said Zacchaeus
  4  Master this-Zacchaeus half grab
  5  unrighteously of-Zacchaeus ~rich God
  6  poor_in_spirit = undeservedly in_turn stand^ up one
  7  among you in_turn-chapter-Jerusalem [half_my_goods] | grab
  8  Zacchaeus one denarius on-extort want-chapter-Jerusalem man^
  9  to-every two-two grab and see Lord-Jesus as

## 207v — this day is salvation come to this house

> a righteous son of father Abraham. And then the Lord Jesus: | Zacchaeus, Zacchaeus, have it, because this day, in Zacchaeus's house is saved, Zacchaeus's; because the Lord, I [am] truly the Son of the living God. And then the Lord Jesus [to] the high priest: the Jews take the commandment; Zacchaeus not; the Lord to this, I went, the Lord, on this world, who, I, sin, from sat [fourfold] | but the Lord, I went, the Lord, who, I, sin; the Lord loves; and the Lord, sin man; and [this day] of the Lord, the sinful man is saved, and the Lord, godfearing; and the sinful man gives thanks. Here ends this holy gospel. The Lord God,

  1  righteous son father Abraham and_said Lord-Jesus | Zacchaeus
  2  Zacchaeus have because this-[?]-+name today inside of-~Zacchaeus
  3  house be_saved of-~Zacchaeus because Lord I
  4  righteous son living God and_said Lord-Jesus high_priest =
  5  grab-Jews commandment Zacchaeus not-Lord to-this I
  6  go-Lord on-this world who I sin from-°sat [fourfold] | but
  7  Lord I go-Lord who I sin love-Lord and Lord sin
  8  man* and [this_day] of-Lord be_saved sin-somebody exist
  9  and Lord godfearing^ and give_thanks = sin-somebody here_ends this holy_gospel Lord_God

## 208r — what Zacchaeus signifies

> with all thy heart. This Zacchaeus is every chief among sinners, and every tax collector, and every man who takes from the sinner, in mercy, the Lord God; and every sinful man, and the sinner in love, the Lord God; and every sinful man truly, and the sinner in truth, the Lord God, that is; and somebody, sin, carries the commandment of God; this is the righteous commandment of the Lord God; and this Zacchaeus is mercy to God's poor in blind; and this Zacchaeus loves the Lord God most high, every creation, and everybody as somebody [his] neighbour; and this. Zacchaeus is within the righteous commandment of the Lord God, that is, | carrying

  1  be_loved this Zacchaeus exist every sin-somebody head
  2  and every publican and everybody = from-grab somebody-sin inside have_mercy.
  3  Lord_God and every somebody-sin and somebody-sin inside love Lord_God and every
  4  somebody-sin righteous and somebody-sin inside righteous Lord_God that_is
  5  and somebody-sin carry commandment God this_is righteous commandment Lord_God
  6  and this Zacchaeus exist have_mercy God spiritually
  7  blind and this Zacchaeus love Lord_God most_high every create
  8  and everybody = as somebody neighbour* and this.
  9  Zacchaeus exist inside righteous commandment Lord_God that_is | carry

## 208v — the first three commandments

> […] the commandment of God, who is; taken within the word of the Old Testament, | from father Abraham. The first commandment of God: believe, man, truly, baptize; one God; somebody saved, many | not sufferings; ours heaven land. The rest commandment is taken within the word of the Old Testament, the father Abraham: God's name in vain not take. The third commandment is taken within the word of the Old Testament, the father Abraham: shall somebody truly baptize, holy Sunday and feast, holy this somebody, from the mother, the temple; let a man hear the preaching, of […]

  1  SUBJ-[?] commandment God who exist take^ inside Old_Testament word | from
  2  father Abraham first God commandment believe somebody righteous
  3  baptize one God be_saved somebody many | not
  4  suffering our SUBJ heaven land the_rest^ commandment
  5  exist take^ inside Old_Testament word the_father Abraham God
  6  name in_vain not_take three commandment exist take^
  7  inside Old_Testament word the_father Abraham shall somebody
  8  righteous baptize holy-~Sunday and feast holy-this-somebody from*
  9  mother temple preach hear-somebody of-[?].

## 209r — from Adam to Abraham to Moses

> heaven land; and these three commandments the Lord God confirmed [to] Moses by the Lord's angel; the time, then, from Adam, trespass. until Abraham, one hundred years and […] years; from Abraham out until Moses, [fifteen hundred] and fifty; from Abraham until Moses, the time the Lord God first confirmed to Moses by the Lord's angel; and God's angel said: Moses, because of this, teach, Moses, this people the three commandments of the Lord; because this, the people believe one

  1  heaven land and this three commandment confirm Lord_God Moses
  2  on-angel of-Lord time then from ~Adam ~trespass.
  3  until Abraham one hundred-year and [?]-year from
  4  Abraham SUBJ ~out until Moses half-+three_thousand
  5  and fifty from Abraham until Moses time
  6  first confirm Lord_God Moses on-angel of-Lord and say
  7  God angel Moses because-this on-learn this Moses this
  8  people three commandment of-Lord because-this people believe one

## 209v — the three laws, and what Zacchaeus kept

> God; two, God's name in vain not take; three, God's commandment: [to keep] the holy Sunday and the feast, this holy man, from the mother, the temple; preaching hear, somebody; this [is] God's commandment; and the commandment somebody is bears; every such man is saved. And this Zacchaeus [hear the] word, love, and carry these three commandments of the Lord God. End [of] this apostle's holy gospel. The Lord God, be loved.

  1  God two God name in_vain not_take three God commandment
  2  [to_keep] holy-~Sunday and feast holy-this-somebody from* mother temple
  3  preach hear-somebody this God commandment and commandment somebody exist
  4  carry everybody = exist be_saved and this Zacchaeus
  5  [hear_the] word love and carry this three commandment Lord_God end this
  6  apostle holy-gospel Lord_God be_loved

## 210r — a man possessed brought before the Lord

> This holy gospel begins, written by holy Matthew, in the fourteen-and-one chapter | of the writing: the time, then the Lord Jesus within thirty-three and a half [years]; at that time preaching | the Lord Jesus preached in Jerusalem; and then they brought one man before the Lord Jesus, in [the synagogue]; the man was [with] a devil; And then the Jews: he [by] the prince of devils, the help

  1  here_begins this holy_gospel
  2  write holy-Matthew inside
  3  fourteen-+one end_of_numeral* chapter | of
  4  write time
  5  then Lord-Jesus
  6  inside thirty half-three time preach | Lord
  7  Jesus inside Jerusalem and then brought* one man^
  8  before Lord-Jesus inside [the_synagogue] man^ exist devil =
  9  and_said Jew he prince_of_devils help

## 210v — the unclean spirit walks through dry places

> of the evil within, from the generation, casts out. And then the Lord Jesus: I [by the finger of God], of the Lord's Father; and I, of God the Father, can miracles do, the Lord. And then the Lord Jesus: this not pious, who from evil is expelled. And then the Lord Jesus: then. he casts out from a man one unclean spirit, and the evil one goes to a dry place, and [walketh] to the Lord, the place, that is, to the virgin, from the generation, and to the word, the generation; and there is, therefore not, the evil lodging. And then this evil, this evil

  1  evil inside from generation^ exorcise and_said Lord-Jesus I
  2  [by_the_finger_of_God] of-Lord the_Father and I of-God_the_Father can miracle
  3  do-Lord and_said Lord-Jesus this not_pious who
  4  from evil exist expel and_said Lord-Jesus then.
  5  exorcise inside man^ one unclean
  6  ~spirit and go evil dry place and
  7  [walketh] to-Lord place that_is on-virgin-from generation^ and
  8  on-word generation^ and exist therefore-°not evil
  9  lodging-and_said this evil this-evil

## 211r — seven other spirits worse than himself

> and the evil one goes [wicked] because from the evil, love, sin, the sinful man; and he takes [taketh with him] seven evil ones, from the evil, trespass, mourning; and there are [wicked] seven evil ones; and | they go, the evil ones, all seven. And then the Lord Jesus: how then this man, the first aforesaid [swept]; and everybody, wish, into the house goes, this; and stood up, up, the first woman, the head, among this people, the Jews. And then: blessed from the womb which carried him, and blessed from the breasts which | this Lord nursed. And then the Lord Jesus: blessed the Lord's mother,

  1  and go-evil [wicked] because from evil^ love sin somebody-sin
  2  and exist grab [taketh_with_him] seven evil^ from evil^
  3  trespass mourn and exist [wicked] seven evil^ and | go
  4  evil^ every seven and_said Lord-Jesus how? then this man^
  5  first^ aforesaid [swept] and everybody = wish inside house
  6  go-this ~and stand_up-up first^ ~woman head
  7  among this people Jew and_said blessed from womb
  8  which-+SUBJ he carry and blessed from breast which | this
  9  Lord nurse and_said Lord-Jesus blessed SUBJ of-Lord mother

## 211v — rather, blessed are they that hear the word of God

> the Virgin Mary, which carried the Lord; and blessed from the breasts which did nurse the Lord; and even more blessed are the people, and God said: let a man hear, and say, and let a man bear it. Here ends this holy gospel. The Lord God, with all thy heart. This holy gospel begins, written by holy John

  1  Virgin_Mary which-+SUBJ to-Lord carry and blessed from breast which
  2  to-Lord nurse still_more and blessed from people and God say.
  3  hear-somebody and say SUBJ carry-somebody end this
  4  holy-gospel Lord_God be_loved
  5  here_begins this holy_gospel
  6  write holy-John

## 212r — whence shall we buy bread?

> within the sixth chapter of the writing: at that time, then, the Lord Jesus within thirty-three and a half [years]; at that time sat the Lord Jesus | on the Red Sea [of Galilee]; and the Lord went through, the Lord Jesus went through the Red Sea to one mount; and the Lord Jesus sat upon this mount, and lifted up the Lord's two eyes to heaven [high] and the Lord Jesus saw, on all four [sides], [a great multitude] people coming to the Lord; and went. And then the Lord Jesus: Philip, this people | take the Lord's apostle Philip, to eat. And then holy Philip: Master,

  1  inside six chapter of-write time then Lord-Jesus
  2  inside thirty half-three time sit Lord-Jesus | on
  3  the_Red_Sea [of_Galilee] and Lord through
  4  go-Lord Lord-Jesus through the_Red_Sea to-one
  5  to_the_mount and sit Lord-Jesus to-this to-mount
  6  and lifted_up of-Lord two eye heaven [high] and
  7  see Lord-Jesus on-every two-two [a_great_multitude] people to-Lord and
  8  go and_said Lord-Jesus Philip this people | grab
  9  apostle-Lord-Philip eat and_said holy-Philip Master

## 212v — five barley loaves and two fishes

> then [we] have two hundred denarii; who, the people, buy bread? not enough [for] the people. And then holy Andrew: Master, this [two hundred pennyworth] one. a little boy; and the boy has five loaves of barley bread, and two fishes. And the apostles brought these five loaves of barley bread and these two fishes before the Lord Jesus; and the Lord Jesus took this bread and these two fishes; and this bread and

  1  then have two_hundred denarius who people
  2  bread buy not people enough and_said
  3  holy-Andrew Master SUBJ this [two_hundred_pennyworth] one.
  4  ~little boy^ and have boy^ five.
  5  loaves barley bread and two fish
  6  and carry disciple^ this loaves five barley
  7  bread and this two fish before Lord-Jesus
  8  and take^ Lord-Jesus this bread and
  9  this two fish and this bread and

## 213r — twelve baskets full

> these two fish the Lord Jesus blessed. And then the Lord Jesus [to] the disciples of the Lord: apostles, sit this people down upon the grass; and the Lord Jesus divided this bread to the apostles, and these two fishes, in turn, the apostles to this people; and then the apostles, every apostle took his portion, and then the apostles […] to all the world, on eating. And then | the Lord Jesus to the Lord's apostles: go, apostles, and take this, of the leftovers; and into baskets the apostles, of the leftovers, twelve filled. And then the Lord Jesus [to] the Lord's disciples: go, this out, among this people; and then the apostles carried the twelve baskets filled up out

  1  this two fish bless* Lord-Jesus and_said Lord-Jesus disciple^
  2  of-Lord sit-apostle down this people on-grass and on-divide
  3  Lord-Jesus this bread disciple^ and this two fish in_turn disciple^ this
  4  people and then disciple^ every apostle-[?] portion grab-apostle
  5  and then apostle-[?] to all_the_world on eat and_said | Lord
  6  Jesus disciple^ of-Lord go-apostle and grab-apostle this from
  7  leftovers and on-basket disciple^ from leftovers six-six
  8  fill and_said Lord-Jesus disciple^ of-Lord go this out among
  9  people and then disciple^ carry basket six-six fill out

## 213v — this is of a truth the prophet

> among this people, many; and saw this many people the power of the Lord Jesus. and all the people gave the Lord thanks; and this word they cried out, thanks: there is God, most high, highest; and the Lord took somebody, by name, one, can, and a man could do this miracle; and he left, among this people, the Lord Jesus. Here ends this holy gospel. The Lord God, with all thy heart. This holy gospel begins, written by holy John, in the eighth chapter of the writing: the time, then, the Lord Jesus within thirty | [and a] half three [years], the time.

  1  among this people many and see this many people power Lord-Jesus
  2  and Lord every people give_thanks = and this word who-shout-to
  3  thanks exist God most_high highest and the_Lord grab-somebody name-+one can
  4  and somebody can this miracle do and leave among
  5  this people Lord-Jesus here_ends this holy_gospel Lord_God be_loved.
  6  here_begins this holy_gospel
  7  write holy-John inside
  8  six-two chapter of-write
  9  time then
 10  Lord-Jesus inside thirty | half
 11  three time.

## 214r — he that is of God heareth the words of God

> The Lord Jesus preached in Jerusalem, and the Lord Jesus said to the Lord's apostles and to the Jewish people: left one up among you, apostles; and the Lord admonished on sin. And then the Lord Jesus: verily verily I speak to you, apostles, the Lord; and […] from God: this somebody […] God's word hears; in turn, and somebody […] not from God, this somebody […] God's word does not hear. And this […] from two [hath a devil]. And then the Jews: he [is] a blasphemer; he [has] Satan, the prince of devils, devils has the Lord; he [is] a heretic

  1  preach Lord-Jesus inside Jerusalem and say Lord-Jesus apostle of-Lord and Jew
  2  people leave one up among you-apostle
  3  and Lord on-sin admonish and_said Lord-Jesus verily verily
  4  I you-apostle speak-Lord and [?]-+SUBJ from*
  5  God this somebody-[?] God say hear in_turn and somebody-[?] not
  6  from* God this somebody-[?] God say not hear and this
  7  [?]-+SUBJ from* two [hath_a_devil] and_said Jew
  8  he one blasphemer he Satan prince_of_devils
  9  devil^ have-Lord he one heretic

## 214v — before Abraham was made, I am

> and he on the holy feast healed the ill. And then the Lord Jesus within this [keep my word]: I committed sin, this healing? you [are] sad, love; I [for] you on the holy feast healed the ill. And then the Lord Jesus: amen, amen, I [say to] you, speaks the Lord; and somebody […] not believing the Lord, and one not somebody […] saved, but everybody damned, remains; and | the man, the apostles, the Jews, is the Lord; believe from somebody […] is | living somebody one, the apostles, the Jews: for ever and ever not die. And then the Jews: of the Jews Abraham [is] black; believed God;

  1  and he on-holy-feast ill heal-Lord and_said Lord-Jesus inside
  2  this [keep_my_word] I commit sin this healing SUBJ you sad
  3  love I you on-holy-feast ill heal-Lord
  4  and_said Lord-Jesus amen amen I you
  5  speak-Lord and somebody-[?] not Lord believe and one
  6  not-somebody-[?] be_saved but everybody = be_damned remain* and | man^
  7  apostle-Jews exist Lord believe from somebody-[?] exist | living-somebody
  8  one-apostle-Jews for_ever_and_ever = not die and_said
  9  Jew of-Jews Abraham black SUBJ God believe

## 215r — Abraham saw my day

> and the black one, God's word he heard, Abraham, and still is dead in turn he not die. And then the Lord Jesus: I saw you, the father Abraham. Said the Jews on the head: not he fifty; in turn this | two thousand(?) years; if of the Jews the father Abraham is dead; in turn | this the Lord spoke, the Lord [rejoiced] Abraham; the Lord saw, the Lord; this [is] not pleasing; he [is] a blasphemer. And then the Lord Jesus: before I leave, than you, the father Abraham, on this world [was made]

  1  and black SUBJ God say hear Abraham and still SUBJ is_dead*
  2  in_turn he not die and_said Lord-Jesus I see
  3  ~you the_father Abraham say Jew on-head
  4  not he fifty in_turn-+SUBJ this | two-?thousand
  5  year ~if of-Jews the_father Abraham is_dead* in_turn | this
  6  Lord speak-Lord [rejoiced] Abraham Lord see-Lord this not pleasing
  7  he blasphemer and_said Lord-Jesus before I leave than
  8  you the_father Abraham on-this world [was_made]

## 215v — then they took up stones

> And then the Jews: this [is] not pleasing; he [is] a blasphemer; and the Jews carried stones, and would say: stone, stone this Lord Jesus; and left among the Jews the Lord Jesus, and out | on the temple the Lord went, and the Lord's apostles. Here ends this holy gospel. The Lord God, with all thy heart. Because it is written in Moses, truly, in turn [the law] among you half somebody, how? a blasphemer, and has somebody stone, stone this; and among the Jews out [out of the temple] [passing through] spoke holy Elijah the prophet and holy Moses; not he said the Jews can, because of […] the Lord created, the Lord God, of the Jews

  1  and_said Jew this not pleasing he one blasphemer
  2  and carry-Jews stone and would_say* stone-stone-this
  3  Lord-Jesus and leave among-Jews Lord-Jesus and out | on
  4  temple and go-Lord and of-Lord apostle here_ends this holy_gospel
  5  Lord_God be_loved because-exist inside Moses true^ write in_turn [the_law]
  6  among you half somebody how? blasphemer and have
  7  somebody stone-stone-this and among-Jews out [out_of_the_temple] [passing_through]
  8  speak holy-+Elijah prophet and holy-Moses not he_said*
  9  can-Jews because* of-[?] Lord create Lord_God of-Jews

## 014r — the Lord went in humility

> the Lord God; because the Lord went in humility, in turn the king, there is heaven and earth, and many a miracle there was afterward, the Lord; and you, the Lord, | upon the cross died, and on the third day stood up from the dead, and appeared to a great nation, and the Lord was to you through staying forty years; and then these forty years [King of kings] see, the Jews […] on every nation see; left within heaven land; and on leaving are the Jews that believe as the true Son of the living God, and king of every king, and Lord of all lords, the chief Lord of heaven and earth.

  1  Lord_God because go-Lord humble-Lord in_turn king exist heaven and ~earth
  2  and great^ miracle exist ~do-Lord and you Lord | on
  3  cross-die and on_the_third_day from die stand_up and appear great^ nation^
  4  and exist-Lord to-you through stay forty_years
  5  and then this forty_years [King_of_kings] see
  6  Jews-[?] on-every nation^ see leave inside heaven
  7  land and on-leave exist-Jews that* believe
  8  as righteous son living God and king every king and
  9  Lord every Lord head Lord heaven and ~earth

## 014v — a new gospel begins

> This holy gospel begins, written by holy Matthew, in the twentieth, in the first chapter of the writing: the time | then

  1  here_begins this holy_gospel write holy-Matthew inside
  2  one-ten-+one-ten inside one chapter of-write time | then

## 011r — go into the village, and you shall find an ass

> was the Lord Jesus thirty-three and a half [years]; at that time went | the Lord Jesus went to Bethany, into Jerusalem, and the twelve apostles; and then | the Lord went to the lodging [Bethphage] there was [mount Olivet] prayer, until, because the trespassing way of the people, the lodging; and the trespassing, through the night, the lodging of the Lord Jesus; and then the Lord went, the Lord Jesus, two disciples down Bethany, because trespass, the Jews carried every [over against you] way, the people, one donkey. And then the Lord Jesus: if you [immediately] not, the Jews, take, the Jews, said the learners, two learners, take, the Jews, the learners, two learners, the donkey [tied]; the apostles [a colt] love

  1  exist Lord-Jesus thirty half-three time go | Lord
  2  Jesus on-Bethany inside Jerusalem six-six disciple^ and then | go
  3  Lord on-+lodging [Bethphage] exist [mount_Olivet] pray ~until because
  4  trespass way people lodging and trespass through night
  5  lodging Lord-Jesus and then-Lord go Lord-Jesus two disciple^ down
  6  Bethany because trespass carry-Jews every [over_against_you] way people
  7  one donkey and_said Lord-Jesus if you
  8  [immediately] not-Jews grab-Jews say learn-two-learn
  9  grab-Jews learn-two-learn donkey [tied] apostle-+SUBJ [a_colt] love

## 011v — they set him thereon

> [loose them]: Master, on going [bring them] the donkey, in the place, you, the donkey, to the Jews; and then the learners, two learners, were […] […]. one [laid their garments] the colt, to the donkey, the other donkey, the ass; and then the apostles untied this ass, and [they did] this commandment; but [set him] and the Lord Jesus sat down on the, he said, donkey; and the Lord loosed, the disciples, this, from the ass, the mother of this ass; and the Lord sat upon this from the donkey; and the Lord went into Jerusalem; and then. the Lord was; the Lord went on the tasty to mount, highest, Jerusalem town

  1  [loose_them] Master on-go [bring_them] donkey on-place you donkey to
  2  Jews and then learn-two-learn exist [?]-[?].
  3  one [laid_their_garments] colt^ to-donkey the_rest^ donkey
  4  donkey and then tie_up-apostle this donkey and
  5  [they_did] this commandment but [set_him] and sit down Lord-Jesus
  6  on-?he_said donkey and Lord loose disciple^ this from
  7  donkey mother this donkey and sit-Lord on-this
  8  from donkey and go-Lord inside Jerusalem and then.
  9  exist-Lord go-Lord on-tasty-to mount highest Jerusalem town

## 012r — the multitude went before him

> and from sought, to the Lord Jesus and the Lord's apostles, because the apostles were [went before] And then the Lord Jesus [to] the Lord's apostles: go, you, [multitude]; and if you [cried out], is judge, who is it; and the apostles went, the apostles said, and the apostles went to the Lord, to Master; in turn to the Lord went two ways; and then the Lord was to the Lord [followed] many people, because they preached, this people [a great multitude] the Lord Jesus went; and an army went to the Lord Jesus; and then the Lord Jesus kept going to Jerusalem, and then the Lord was; saw on Jerusalem the people; and went the Lord Jesus

  1  and from-°sought-to Lord-Jesus and of-Lord apostle because apostle exist [went_before]
  2  and_said Lord-Jesus apostle of-Lord go you
  3  [multitude] and if you [cried_out] exist judge
  4  who_is_it and go-apostle say-apostle and go-apostle to Lord to
  5  Master in_turn to-Lord go two way and then-Lord
  6  exist to-Lord [followed] many people because [?]-+preach this
  7  people [a_great_multitude] go Lord-Jesus and and go an_army
  8  to Lord-Jesus and then go_on Lord-Jesus to-Jerusalem
  9  and then-Lord exist see on-Jerusalem people and go Lord-Jesus

## 012v — hosanna to the son of David

> into Jerusalem; and [with] great joy the Jews shouted: he, and the son goes, David the king; and the Lord, great joy, the Jews, because one somebody, the Jews, of […] clothes; mercy [and] love; spread the Jews, somebody, before the Lord Jesus; second, the Jews, somebody, the bough | cut off the Jews, somebody; and [spread their garments] | [in the way] somebody before the Lord Jesus; and the Jews shouted | this Lord is the son of David the king; they brought the king's crown, the Jews; and the Jew spoke: he

  1  inside Jerusalem and great^ joy shouted-Jews he and go son
  2  David king ~and-Lord great^ joy Jews
  3  because one somebody-Jews of-[?] clothes^
  4  have_mercy-love spread-Jews-somebody before Lord-Jesus
  5  second Jews-somebody bough-+SUBJ | cut_off
  6  Jews-somebody and [spread_their_garments] | [in_the_way]
  7  somebody before Lord-Jesus and shouted-Jews | this
  8  Lord SUBJ son David king brought-[?].
  9  king crown-Jews and speak Jew he

## 010r — my house shall be called the house of prayer

> [is] king of the Jews. And this word the Jews shouted: thanks to the Lord from all the people on earth, and the angels from heaven high; and the Lord Jesus went into the temple at Jerusalem; and then the Lord found the moneychangers; and the Lord, all the moneychangers, out, the dove sellers | cast out, the Lord. And then the Lord Jesus: this temple [is] a house of prayer, one house by name; you Jews did one den of thieves. And then from one little son and shouted to: he […] the Jews' king. And then one Jew: Master, see, Lord, who this

  1  king Jew and this word shouted-Jews thanks
  2  Lord every people on-earth and angel from_heaven* high and
  3  go Lord-Jesus inside temple Jerusalem and then exist-Lord find
  4  moneychanger and-Lord every moneychanger out dove_seller* | exorcise
  5  Lord and_said Lord-Jesus this temple-+SUBJ prayer^ house
  6  name-+one house you Jews do one
  7  den_of_thieves and then from one little son
  8  and shout-to he SUBJ [?]-Jews king
  9  and_said one Jew Master see-Lord who this

## 010v — out of the mouth of infants

> little son speaks, the son [Hosanna]: he [is] the Jews' king. And then the Lord Jesus: then this every, this little son not | speak the son, then, the earth is, and the rock and stone, all are, shouted to [son of David]: I [am] your, Jews, king. Here ends this holy gospel. The Lord God, with all thy heart. And then the commandment of the Jews; and the Jews, the Lord: take within this town Jerusalem one cup, but rather the Jews, are, the Jews can cup this, they would, the chief, take; and then […] the Lord the lodging find, the Creator Lord, heaven and earth, Lord of every lord,

  1  little son speak-~son [Hosanna] he of-Jews king and_said
  2  Lord-Jesus then this every this little son not | speak
  3  ~son then exist earth and rock-stone every exist.
  4  shout-to [son_of_David] I you-Jews king
  5  here_ends this holy_gospel Lord_God be_loved and then-[?]
  6  commandment Jew and Jews Lord grab inside this town Jerusalem
  7  one cup °but_rather-Jews exist-Jews can-Jews cup* this
  8  would_say* head grab and then [?]-Lord
  9  lodging find Creator_Lord heaven and earth Lord every Lord

## 013r — the prophet foretold it

> King of all kings; spoke holy […] the prophet, and holy […] the prophet not can the lodging find, the Creator Lord; and the head of heaven and earth, Lord of all lords, King of all kings; and out, the two, loving, foretold, the prophet, and holy […] the prophet; and the Lord Jesus went [lodged] into Bethany, this [remained there] went [with him] the two, above, hidden, the earth; and this, many thanks the Lord did; in turn [morning] the Lord [returning], much sad. And then the Lord Jesus: this is [hungry] every one, from a man; and a man is of the Lord's name among men; and out of the man, the good man does.

  1  king every king speak holy-NAME.prophet prophet and holy-NAME.prophet
  2  prophet not can lodging find Creator_Lord and head
  3  heaven and earth Lord every Lord king every king and
  4  ~out love-two-exist predict NAME.prophet prophet and holy-NAME.prophet
  5  prophet and go Lord-Jesus [lodged] inside Bethany this [remained_there]
  6  go [with_him] two above-hide earth and this many thanks Lord do
  7  in_turn [morning] Lord [returning] many sad and_said Lord-Jesus this
  8  exist [hungry] every from somebody and somebody exist of-Lord name
  9  among somebody and out-somebody good-somebody do

## 013v — the three tables of Moses

> Three tablets Moses gave, and the Lord God wrote by the Lord's angel.

  1  three tablet Moses give^ and write Lord_God on-angel of-Lord

## 218r — Gamaliel and Nicodemus, and a servant named Saul

> the second, this holy man remits; the mother, the temple; let a man hear the preaching, from the seeing; heaven and earth; and the time of prayer, the two church fathers at Jerusalem; three chiselled on tables of stone, because the Lord God had Moses chisel three tables of stone by the Lord's angel, and wrote three commandments. Thanks to the Lord God. The time, then, from Adam, trespass, seven […] and fifteen hundred; and the time of these three tablets of Moses, prayer, two church fathers, two high priests at Jerusalem: Gamaliel the high priest and Nicodemus the high priest; and then two servants hired out, learning, these two high priests; one man there was, and his name was Saul,

  1  two holy-this-somebody remit mother temple preach hear-somebody
  2  of-from-see SUBJ heaven land and time pray two
  3  church_father on-Jerusalem three on-stone-tablet chisel because exist Lord_God Moses
  4  three stone-tablet chisel on-angel of-Lord and write three commandment
  5  to-Lord thanks Lord_God time then from ~Adam ~trespass seven-[?] and
  6  half-+three_thousand and time this three tablet Moses pray
  7  two church_father two high_priest-high_priest on-Jerusalem Gamaliel high_priest and Nicodemus
  8  high_priest and then two servant hire_out learn this two high_priest-high_priest
  9  one man^ exist and-~brother-+name Saul

## 218v — Stephen, the first martyr

> The second apostle was Saint Stephen, the first martyr; and | then there were two servants, these two, two apostles, these two, two high priests; in turn these two, two apostles, the two of them from [Damascus] the two, in belief, of Christ; this was the time, then, the Lord Christ was crucified, and then the Jews wiped out, down, the faith of Christ, the Jews, the head; and was, were, the Jews, found; and there was somebody, many [far countries]; somebody, name […] Christ, every man suffering; in turn, a man rather, the chief | take, the Jews; and then holy Stephen [cried with a loud voice]: confess the name

  1  second apostle exist Saint_Stephen the_first_martyr and | then
  2  exist two servant two this-two two apostle this-two two high_priest-high_priest
  3  in_turn this-two two apostle exist-two from [Damascus] two on-believe
  4  [?]-~Christ this exist time then Lord-~Christ crucified
  5  and then Jew wipe_out* down faith ~Christ Jew
  6  head and exist exist-Jews find* and exist
  7  somebody many [far_countries] somebody name [?]-~Christ
  8  everybody = suffering in_turn somebody-°but_rather head | grab
  9  Jews and then holy-Stephen [cried_with_a_loud_voice] confess name

## 217r — they brought him to suffer

> […] Christ. And then the Jews, the head, followed on this Saint Stephen, the first martyr; and then Stephen the Jews were brought on suffering within the Jerusalem temple, two Jews among the Jews; Stephen went […]; and this Saul to the Jews; and Saul went, because not [consenting] many; and this Saul, and then Stephen was, the Jews, brought within the temple, Jerusalem, because they would stone Stephen, because it is written in Moses, truly, in turn [the law] among you, if a man begin to blaspheme, and a man has stones, and | among

  1  [?]-~Christ and then follow Jew ~head on-this
  2  Saint_Stephen the_first_martyr and then Stephen
  3  exist-Jews brought* on-suffering inside Jerusalem temple
  4  two-Jews among-Jews Stephen go-[?] and this Saul
  5  to-Jews and go Saul because not [consenting] many and this Saul
  6  and then Stephen exist-Jews to-?brought inside temple Jerusalem
  7  because Stephen would_say* stone-stone-this because-exist write inside
  8  righteous Moses in_turn [the_law] among you begin man^
  9  how? blasphemer and have man^ stone-stone-this and | among

## 217v — the heavens opened

> the Jews, out [out of the temple] [passing through] | and then holy Stephen knelt; and | then was praying, Stephen, to the Lord, thanks [to] the Lord God, to the Jews; and then Stephen prayed, redeem, to the Lord, thanks [to] the Lord God; and Stephen raised Stephen's two eyes [to] heaven land, and to the Lord, thanks. the Lord God; and this word said holy Stephen: to the Lord thanks, the Lord God, through offering Stephen, this Stephen, he, Stephen's soul, within the Lord's hands. At that time, then, opened heaven; and then Stephen saw, Stephen, one king sitting on a throne, and [the right hand of God] an army, an army

  1  Jews out [out_of_the_temple] [passing_through] | and then kneel holy-Stephen and | then
  2  exist pray-Stephen to-Lord thanks Lord_God to-Jews and then
  3  pray ~redeem Stephen to-Lord thanks Lord_God and raise-Stephen
  4  of-Stephen two-eyes heaven land and to-Lord thanks.
  5  Lord_God and this word say holy-Stephen to-Lord thanks Lord_God through
  6  offer Stephen this-Stephen he of-Stephen soul
  7  inside of-Lord hands time then open
  8  heaven and then-Stephen see-Stephen one king
  9  inside throne sit and [the_right_hand_of_God] an_army army

## 216r — they stopped their ears

> of angels; and holy Stephen cried out; Stephen saw [looking up] | see, the gate of heaven and earth is opened, and Stephen saw one king, crowned, sitting on a throne, and [the right hand of God] an army, an army of angels. And then the Jews this Stephen is a blasphemer, Stephen; and took off, the Jews, on the Jews, the Jews' clothes; and. left, the Jews, literal, the man, one son; and this son. was this Saul; and the man was [with] these clothes; and from […] want [to] stone, stone this, holy Stephen, | the first martyr

  1  angel and shout-to holy-Stephen see-Stephen [looking_up] | see*
  2  gate/open heaven land and see-Stephen one
  3  king crown inside throne sit and [the_right_hand_of_God]
  4  an_army army angel and_said Jew
  5  this-Stephen-+SUBJ one blasphemer-Stephen and.
  6  take_off-Jews on-Jews of-Jews clothes^ and.
  7  leave-Jews literal man* one son and this son.
  8  exist this Saul and man* exist this clothes^
  9  and from [...] want stone-stone-this holy-Stephen | first_martyr

## 216v — Stephen prays for those who stone him

> of the Lord God [lay not this sin]; and […] could stone Stephen, stone this; and from […] were [fell asleep] in Stephen's death; and this, spoken, written; then not Stephen […] Stephen prayed, and Stephen, the first martyr, to the Lord, thanks [to] the Lord God; […] are damned; and then Stephen was, the Jews, out on the town, stoned [out of the temple] [passing through]; and | then that day he was; he saw this suffering, this Saul, [a great persecution] the Jews did to holy Stephen; | the first, not, suffering; to the Lord thanks [to] the Lord God; and then | was […] through startling, this Saul, and trespassing, to the place

  1  Lord_God [lay_not_this_sin] and [...] can Stephen stone-stone-this
  2  and from [...] exist [fell_asleep] inside of-Stephen die and this speak
  3  write then not Stephen [...] pray-Stephen
  4  and Stephen first_martyr to-Lord thanks Lord_God
  5  [...] exist be_damned and then Stephen exist-Jews
  6  out on-town stone [out_of_the_temple] [passing_through] and | then
  7  day exist see this suffering this Saul
  8  [a_great_persecution] do Jew on-holy-Stephen | first-not
  9  suffering to-Lord thanks Lord_God and then | exist
 10  [...] through startle this Saul and trespass to-place

## 219r — Saul takes letters to Damascus

> and by the name of the brethren of the Lord Jesus Christ; and this Saul to the head of the Jews, on the town Jerusalem; one from this Saul, the Jews took, the head […]; they could, upon this man that believeth not, and the man who this Jesus, this Christ, believes; and [threatenings] […], the mother, […] every capture; and somebody many [bound] see; and by name brother of the Lord, […], every man to you, this going; and then […] was, the Jews, took a mission, many riches; and then […] [letters], many servants on the commission.

  1  and-brother-+name Lord-Jesus-Christ and go this
  2  Saul to-head Jew on-town Jerusalem
  3  one-from this Saul grab-Jews head [...]
  4  can on-this man^ not_believe and man^ this Jesus this
  5  Christ believe and [threatenings] [...] mother [...] SUBJ every
  6  capture and somebody-+SUBJ many [bound] see* and-brother-+name
  7  of-Lord [...] everybody = to-you this-go-this
  8  and then [...] exist-Jews grab mission many ~rich
  9  and then [...] [letters] many servant on-mission

## 219v — a light from heaven

> And then within | within Jerusalem one town a town there was, named Damascus, because, and within that [they] believe the Lord Jesus Christ; and then went to Saul, upon this town, many an army; and | then the Jews, Saul, the servants, on half the way, to go, Saul, the servants, the time; and this Saul went, before […], servant, and […] there was a light [shined round] from heaven and earth, and […] there was a light [fell to the earth] to the heavenly; he bowed, and the Lord God cried out upon the water: Saul, Saul,

  1  and then inside | inside Jerusalem one-town
  2  exist-[?] town exist Damascus because and
  3  inside that* believe Lord-Jesus Christ and then go to
  4  Saul on-this town many an_army and | then
  5  Jews-Saul-servant on-half way to-go-Saul-servant
  6  time and go this Saul ~before [...] servant
  7  and [...] exist light [shined_round] on-heaven land
  8  and [...] exist light [fell_to_the_earth] on-+heavenly-to bow
  9  and shout-to Lord_God on-water Saul Saul

## 220r — I am Jesus of Nazareth

> why? the Lord through […]; and shouted to this | Saul, […] [Saul] lie; in turn the Lord [whom thou persecutest] he; and shouted to the Lord God on the water: I, from Jesus of Nazareth, the Lord, on the cross executed; and this Saul cried out: Lord, who, Saul, the Lord, did; and shouted to the Lord God on the water: […] into the town; from […] on learning, the man love; […] […], the time, the hour, from […]; and [led him by the hand]; and […] there were took Saul's servant; and Saul [they] took away,

  1  why? Lord through [...] and shout-to this | Saul
  2  [...] [Saul] lie in_turn Lord [whom_thou_persecutest] he and
  3  shout-to Lord_God on-water I from Jesus Nazareth
  4  the_Lord on_the_cross execute and shout-to this Saul
  5  Lord who Saul Lord ~do and shout-to
  6  Lord_God on-water [...] inside town from [...] on-learn man^
  7  love [...] [...] time hour from
  8  [...] and [led_him_by_the_hand] and [...] exist
  9  grab of-Saul servant and Saul take_away

## 220v — the house of Judas, and Ananias

> Saul, servant, into the town; and Saul put, servant, one man, Ananias; and a man, Ananias, was born, Gamaliel, town; and this Saul, trespass, […] at the birth; and […] there was this Saul, this Ananias put Saul, the servants, into one house; and […] three […], this Saul, within this house, this Ananias, the man; and this man's name was Judas; and then one man within this town can, the man said, find, understand; in turn, and by name, brother, the man was

  1  Saul servant inside town and Saul put servant
  2  one man* Ananias* and man^ Ananias* exist ~be_born
  3  Gamaliel town and this Saul trespass [...]
  4  on-~be_born and [...] exist this Saul this
  5  Ananias* put of-Saul servant inside one house
  6  and [...] three [...] this Saul inside
  7  this house this Ananias* man^ and this man^ and-~brother-+name
  8  exist Judas and then one man^ inside this town
  9  can man^ say find-understand in_turn and-~brother-+name man^ exist

## 221r — a vessel to bear my name

> Ananias; and Paul, from Paul; and he bowed down, [hail] upon Paul [laid his hands]; and Ananias put the Lord's name upon Paul, because from Paul, Paul is | of the Lord's name carries Paul on all the whole world; is Paul | of the Lord's name, confesses Paul. And then holy Ananias: Lord, how is it, from Saul, of the Lord, the name | bears Saul, and Saul, of the Lord, the name, through persecuting, Saul? And secondly the Lord God said to holy Ananias: go, Ananias; the Lord's servant, in truth and love, drink

  1  Ananiah and Paul from-[?]-Paul and bow
  2  [hail] on-of-Paul [laid_his_hands] and put Ananiah of-Lord
  3  name on-Paul because from Paul exist-Paul | of
  4  Lord name carry Paul on-all_the_world world exist-Paul | of
  5  Lord name confess Paul and_said holy-Ananiah
  6  Lord how? exist from Saul of-Lord and-~brother-+name | carry
  7  Saul and Saul SUBJ of-Lord and-~brother-+name through
  8  persecute-Saul and two say Lord_God holy-Ananiah
  9  go Ananiah of-Lord servant inside righteous-love drink

## 221v — a table of earthquakes and eclipses

> Before the Spirit, on the Friday, the earth, one quake; on the Spirit, on the Wednesday, the moon eclipsed one hour; and from the year before God, on the Friday, the earth quaked, from the Spirit; the first year from God, the first year, in turn, on the fast | three day before the Virgin Mary; within Sunday the earth quaked; and this, and the day [a sign] [shall appear] upon heaven and earth, living, and confessing, to the letter; and a man [a sign] sees [darkened] [the sun] to, within [the holy church] answered, to; in turn, two years [famine] from the Spirit [pestilence]

  1  before spirit inside Friday earth one
  2  quake on-spirit inside Wednesday moon eclipse
  3  one hour and from year before God
  4  inside Friday earth quake from spirit
  5  first year from God first year in_turn on-fast | three
  6  day before Virgin_Mary inside ~Sunday earth
  7  quake and this and day [a_sign] [shall_appear] on-heaven
  8  land living and confess to-literal-to and somebody
  9  [a_sign] see [darkened] [the_sun] to inside [the_holy_church]
 10  °answered-to in_turn two-year [famine] from spirit [pestilence]

## 223r — more of the same table

> the day the earth quaked, out, the first Spirit, Friday; and the years and three of God, from the Spirit, four years [a wind] from the Spirit [shall come] the earth quaked, and the moon in turn on; and the year half the father, our [heaven] from [render] somebody; and [within] in truth believing, the Lord bears the man [shall be saved] believeth not; and this, every one, therefore have mercy, man [shall perish] and the man would, Christ, against, leave; the man, God, learn, the throne [shall be fulfilled] wants somebody [shall sit], the Lord's throne [shall be saved], righteous of the Lord.

  1  day SUBJ earth quake out first
  2  spirit Friday and years* and three God from spirit two-two-year
  3  [a_wind] from spirit [shall_come] earth quake and moon
  4  in_turn on and year SUBJ half
  5  the_father our [heaven] from [render] somebody and
  6  [within] inside righteous believe carry-Lord somebody [shall_be_saved]
  7  not_believe and this every therefore-have_mercy somebody [shall_perish]
  8  and somebody want Christ against leave somebody God learn
  9  throne [shall_be_fulfilled] want somebody [shall_sit] Lord-throne [shall_be_saved] righteous
 10  Lord-of

## 223v — the date, and the age of the world

> From the ascension of the Lord Jesus Christ [to] the Father of the Lord, out, a thousand years, five hundred and sixty years; and by name, that day, thus, the beginning of the year, written. Four sons. From [the beginning] then was forty days; in turn see [and then] the son, Moses [five thousand one hundred and ninety nine] by name, the year, the first year, seven, in turn, from the seeing, two years [a numeral] from the earth until the Lord Jesus Christ was born into this world, out, five thousand and a hundred years, and | ninety years, and nine years; and this symbolizes nine hours from the beginning of this world. until the Lord Jesus Christ was born into this world; in turn, and the hour, out, from the ascension of the Lord Jesus to the Lord's Father, heaven; in turn, brother the time the apostles said [to] the Lord Jesus: Master, when is doomsday passing? Said

  1  from* ascension Lord-Jesus-Christ the_father of-Lord out
  2  thousand-year five_hundred and six-ten-year and from-+name-~year
  3  this_is begin-year write
  4  two-two-son
  5  from* [the_beginning] then exist forty_days in_turn see* [and_then]
  6  son Moses [...] from-+name-year first-~year
  7  seven in_turn of-from-see two-year [a_numeral]
  8  from earth until be_born Lord-Jesus-Christ
  9  on-this world ~out five_thousand and hundred-~year and | nine-ten
 10  year and nine-year and this symbolize nine ~hour from begin this world.
 11  until be_born Lord-Jesus-Christ on-this world in_turn and ~hour ~out
 12  from ascension Lord-Jesus to-the_father of-Lord heaven in_turn-~brother
 13  time say apostle Lord-Jesus Master when? exist pass doomsday say

## 222r — when shall the judgment day be?

> [hallowed be] the name of the Lord, of the Lord's Father. In turn, out [after] two thousand years, to this, the brother, of the chapter, one day; and he has from covered, one, the judgment year; because anew, from the Son of God, judgment; the dead man, the sinful man damned, the sinful man; and saved, the light, said, said the Lord Jesus; this said the Lord's apostles; there is upon a man one, one, girl, earth, water, sun, all [shall be shaken] the earth, the sun, Christ, [amen] the Lord God.

  1  [hallowed_be] name of-Lord of-Lord the_Father.
  2  in_turn-[?]-~out [after] two_thousand to-+this_is
  3  [?]-~brother of chapter one day and have
  4  from covered-+one judge-~year because new-from son God judge
  5  die man^ sin be_damned man^ sin and be_saved
  6  light say say Lord-Jesus this say disciple^ of-Lord exist on-somebody
  7  one one girl earth water sun every [shall_be_shaken]
  8  earth sun Christ
  9  [amen] Lord_God

## 222v — a calendar, with the writer's own name in it

> [on the holy day] Monday, within Thursday, went somebody [of] the name of the author [I went] to the house, the brother, trespassing, he carried, the writer of this book [to the Lord's house] on the Friday, [and then] the writer of this book [to the Lord's house] on the Sunday he went, the writer of this book, to the seal [I went] remitted, half year [to the Lord's house] this, out, one holy Philip's year [on the feast of] Monday, within [a date] he took, the writer of this book, until half year; in turn from half year one, in turn [reckoned] [I pray] [my sins] the Lord, have mercy; in turn [my soul] one [reckoned] in turn, in the middle, the man [to the Lord's house] more than these; this said, gave […], the writer of this book [wrote] Friday [I fasted] [lunatic] the writer of this book; this, out, two; Sunday, by name, Sunday three, fourth Sunday three, the Lord | Father, Son and Spirit; on the Monday there was [the Holy Spirit] conceived, to

  1  [on_the_holy_day] Monday inside Thursday go-+the_name_of_the_author-somebody [I_went] to-house
  2  brother-trespass carry-+the_name_of_the_author-somebody [to_the_Lord's_house] inside Friday
  3  [and_then] the_name_of_the_author-somebody [to_the_Lord's_house] inside Sunday go-+the_name_of_the_author-somebody seal-to
  4  [I_went] remit half-year [to_the_Lord's_house] this out one
  5  holy-Philip-year [on_the_feast_of] Monday inside DATE grab-+the_name_of_the_author-somebody
  6  until half-year in_turn from* half-year one in_turn [reckoned]
  7  [I_pray] [my_sins] Lord have_mercy in_turn [my_soul] one [reckoned] in_turn amid
  8  somebody [to_the_Lord's_house] more_than_these* this say °gave-[?] the_name_of_the_author [wrote]
  9  Friday [I_fasted] [lunatic] the_name_of_the_author-somebody this out two Sunday name
 10  Sunday three second-two SUBJ Sunday three Lord | father
 11  son-spirit inside Monday exist [the_Holy_Ghost] conceive to

## 224r — the last leaf but one

> ninety-six, little, one […] Michael, on the Saturday, of the woman [the angel] of Mark; you took, and [wrote] and two, from two, the mother, on the Saturday [and on] [the same week] on the Saturday, upon good [deed] more than these; upon a man there is, then, upon death, that day, upon the name [one year] [on the day of] [the feast] Matthew, on the Saturday; and lo, one, this is [likewise] Matthew [and on] [the same week] on the Saturday [likewise] [and on] [the same week] understanding, who [at the table] the cup by name; and from a man to this rich good [deed] and one [and a half] three, and one [and a half] three, believe upon this [a portion] [of wine] [a portion], gave, year

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

> the Lord Jesus Christ saved; the Lord, all the world, [I pray thee] the son, living, of he said; and this man, upon the food, to, in turn, living, the woman, Matthew [and on] on the Saturday, within the seal [this book] Lord have mercy, you, have mercy, of Christ; and through offering, you, have mercy, have mercy, Lord; in turn, the woman [and on] [the same week] and of [the saints] and all, from the leaving […] [the same week] on high; and [into heaven] there is, then, the soul from losing, from riches [at the last] there is [amen] [for ever] from the day, this why; and understanding, the man, the woman, this world, truly, two.

  1  Lord-Jesus-Christ be_saved Lord all_the_world
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
