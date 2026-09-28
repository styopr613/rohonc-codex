# The Rohonc Codex — a working translation

Translated from `rohonc_reading_full.txt`, which is Király and Tokai's
dictionary laid over their transcription, plus the composed readings gated in
`ktname.py` and `ktsegment.py`. Their page order.

**How to read this.** English first. The gloss it was made from is underneath
in a code span, so every choice can be checked. A word in `[…]` had no reading
at all. A word in `[like this?]` is my guess at an unread word from context. A
`(?)` marks a sense choice I am not confident in. A `|` in the gloss is a gap
or a margin break in the manuscript.

**What this is not.** It is not Király and Tokai's translation, which is
unpublished. Where their published reading of a line exists it is noted and
compared. Every gloss is theirs. The sentence-making is mine and is the part
most likely to be wrong.

**Confidence.** The dictionary reaches 78.8% of the words. Context cannot pick
between senses (measured: `ktsense.py`, `ktgrammar.py`), so I picked them, and
a blind test of that skill earlier in the project scored one to two right out
of six. Treat any single line as a proposal. The story-level reading — what
book this is — rests on many lines agreeing and is much firmer than any one of
them.

**Corrected 2026-09-28.** The gloss was proofed word by word against the
dictionary and decided by hand in context. 2,185 lines on 429 folios changed
their gloss, and each of those lines was rewritten by hand to follow the new
gloss. On those lines the code span is now the reader's-edition gloss, in its
own wording, not the older raw gloss. Earlier English on them was wrong where
it differs: it carried words the signs do not give (a Sasanian king, "an alien
nation", "render to Caesar", "the scribes" for dark signs) and misread sets
such as *poor man* (Lazarus), *woman* (Augustine's widow, 144r–147v) and
*Jesus*.

---

## What the book turns out to be

The opening is not a gospel. Folios 004v through 001v tell the **Life of Adam
and Eve**: the fall of Lucifer, the creation of Adam, the breath of life,
Paradise, the rib, Eve, the serpent, the fruit, the shame, and God walking in
the garden asking where Adam is. That is the apocryphal *Vita Adae et Evae*,
not Genesis. An earlier version said the distinguishing episode was here, God
commanding the angels to bow to Adam and Lucifer refusing; that was wrong. The
bowing on 002r comes before Adam is made on 002v, at the birth of the mother of
the Lord God, and the gloss has Lucifer bow, with the refusal supplied.

It is framed as a revelation. The angel of God speaks to **Elijah the
prophet**, and Elijah is addressed by name at the start of sections. Chapter
ends are marked in the text with the word Király and Tokai gloss "chapter".

---

## Recurring unread words, guessed from context

These are guesses, not readings. Listed so they can be checked against every
occurrence, which is the test that would make any of them real.

| code | times | guess | why |
|---|---|---|---|
| `EAE0` | 217 | **day** | K&T mark it a variant of a code they gloss "day". Sits between "forty" and "forty night" at 004v:11. |
| `E4A2 E4A0 E4A4` | 337 | **and then / thereupon** | Always clause-initial, usually before a name or a speech verb. One glyph from their code for "and". |
| `E540 E60B` | ~76 | an auxiliary, **did / would** | One glyph from their "will, want, future auxiliary". Sits beside eat, take, give all through the Eden pages. |
| `E060 E060 E443 E520` | many | an epithet of God | Follows "God the Father" almost every time it appears. |
| `E520 E3F0 E950 E1F2` | 3 here | **gave / ate** | 001v:5, 8, 9, in the interrogation of Eve. |

**Numerals.** The parts add, and a `ten` after a group multiplies that group
by ten. Four readings confirm it against a known number in the source:

| written | value | where | check |
|---|---|---|---|
| `ten-ten-ten-ten` | 40 | 004v:11 | forty days and forty nights |
| `two-two-ten` | 40 | 008r:11 | the rain fell forty days |
| `six-two` | 8 | 021v:10 | circumcised on the eighth day, Luke 2:21 |
| `nine-ten` + `nine` | 99 | 119r:7 | the ninety and nine sheep, Luke 15:4 |
| `six-six` | 12 | 022r:10 | the twelve apostles |
| `ten-six` | 16 | 019v:5 | Mary's age at the Annunciation |

Király and Tokai gloss one very common code "place-value delimiter in
numerals", so they had already seen that the system has place value.

**Numerals that resolved.** Their numbers are written as sums of their parts.
`two-<distributive infix>-two` at 008r:6 and 008r:8 is **two by two**, of
every creature into the ark.

---

## 004v — the beginning: heaven, the angels, Lucifer

**1**  In the beginning there was the Lord God.
`time then-exist Lord God`

**2**  created one [thing] on the sky, and the earth.
`create one-on-sky and ~earth`

**3**  The sun and the moon, [as] the scripture(?) [says].
`sun and moon write`

**4**  Elijah the prophet. The angel of God said:
`Elijah prophet say angel God`

**5**  [the forefather], before he created us.
`[forefather] before create our`

**6**  The Father [and] Adam the Lord created.
`the_father ~Adam create Lord`

**7**  God on the sky, in heaven; and the brethren.
`God on-on-sky heaven in_turn-brother`

**8**  Many angels upon angels; and they were to the Father, God, holy angels.
`many ~angel on-~angel and exist to-the_father God on_Holy angel`

**9**  Upon the angels two hundred and fifty years and seven, before he created us.
`on-angel two-half-hundred-year seven before create our`

**10**  The Father, Adam, and an angel, a brother, named — he was Satan — and two angels.
`the_father ~Adam and angel brother-+name exist Satan and two ~angel`

**11**  And the angel Satan prayed, forty days [and] forty nights
`and angel Satan pray and forty days forty nights`

**12**  which Satan to Satan: upon one heaven, upon, in turn, a brother, upon hell.
`which Satan to Satan on-+one-heaven on-in_turn-brother on-hell`

**13**  And the second, said the angel to Elijah: Elijah, and then pray
`and two say angel to-Elijah Elijah and then pray`

**14**  Lucifer, who did [this] — Lucifer, when he was
`hide_oneself-angel who do, hide_oneself-angel then-exist`

**15**  the day he sat on the throne of the Father God; he went to the Father God.
`day sit on throne the_father God go the_father God`

> Lucifer's name is a compound: their code for "hide oneself" followed by
> their sign for angel, Satan, Lucifer. It is the code this project spent ten
> failed attempts trying to guess as a single word.

## 004r — the cup

A formula repeats six times in thirteen lines. I have kept the repetition
rather than smoothing it, because it is the shape of the page.

**1**  The angel of the Father said, the Father God, the angel said, that Satan hid the cup.
`angel of-father say the_father God angel say Satan that cup-to hide`

**2**  above, of the Father, on the throne; and God said, the angel: Satan hid the cup.
`above* of-father on throne and_said God angel Satan cup-to hide`

**3**  above the Lord on the throne; and then the cup Lucifer [stole]; the cup was hidden away above
`above* Lord on throne and then cup ~Satan [steal] cup-to hide above*`

**4**  And then from Lucifer the angel returned to the Father.
`and then from Satan return angel to-father`

**5**  And the angel said: Lord, the cup: Satan [stole] the cup, hid it above; and the two went.
`and_said angel Lord cup Satan [steal] cup-to hide above* and two go`

**6**  God the Father; the angel of the Father [spoke] to Lucifer; Lucifer said: because the cup was hidden away.
`father-<divine> <of>-father angel to-hide_oneself-angel say hide_oneself-angel because cup-to hide_oneself`

**7**  above with the Father, on the throne; and when Lucifer went to God
`[?] on-<of>-father on throne and then-exist to-hide_oneself-angel go God`

**8**  the angel said: God; the angel; the cup was hidden away above the Lord on the throne; and when
`angel say God angel cup-to hide_oneself [?] Lord on throne and then-exist`

**9**  the cup Lucifer [stole]; the cup was hidden away above; and then from | hidden.
`cup Satan [steal] cup-to hide above* and then from | hide`

**10**  The angel returned, the angel, to God the Father, because there was
`angel return angel to-father God because-exist`

**11**  said Lucifer to the Lord: hidden. The Lord God's mother was born, born, to the Lord, to the Lord, this | hidden.
`say Satan to-Lord hide Lord_God mother ~be_born be_born* to-Lord to-Lord this | hide`

**12**  The angel: [proud] Satan was on this throne; and God said, the angel, the Lord:
`angel [proud] Satan this on throne and_said God angel Lord`

**13**  The cup of Lucifer [steal] the cup was hidden away above said Lucifer to the Lord: hidden.
`cup hide_oneself-angel [?] cup-to hide_oneself [?] say hide_oneself-angel to-Lord hide_oneself`

## 002r — Michael, the command to bow, and Lucifer's fall

**1**  The mother of the Lord God was born; and Lucifer to the Lord, to the Lord; Lucifer [envied]
`Lord_God mother be_born and Satan to-Lord to-Lord Satan [envied]`

**2**  Lucifer, this one, on the throne [set] of the Lord God; the Lord's finger
`Satan this on throne [set] Lord_God of-Lord finger`

**3**  There was the earth; and the Father, God of heaven, said to Michael:
`exist earth and_said the_father God heaven Michael`

**4**  The angels, faithful servants, rose up; and when they had risen,
`angel believe servant stand_up up and then-exist stand_up`

**5**  the heavenly one said, the Father of heaven: go to Satan; and
`heavenly say the_Father heaven go to-Satan and`

**6**  Lucifer bowed on the throne of the Lord; and then, within […] one, understand
`Satan bow on throne of-Lord and then inside [?]-+one-understand`

**7**  they bowed down — and of the angels every one — to whom Lucifer [would not] bow.
`bow_down and from angel each,_every to-which hide_oneself-angel bow_down`

**8**  And then the Father, God of heaven, saw, and cried out.
`and then see* the_father God heaven and shout`

**9**  The Father, God of heaven, left Satan the commandment, because every angel was
`the_father God heaven leave Satan commandment because every exist angel`

**10**  to whom Satan should bow; and he [refused] to go, said the Father. From
`to-which Satan bow and [refused] to-~go say the_Father from`

**11**  he left; this was the angel; he left, up, the year of judgement; and three, the angel said
`leave this exist angel leave up ~judge-year and three say angel`

**12**  to Elijah the prophet, Elijah said: the Father is.
`to-Elijah prophet Elijah say SUBJ the_Father exist`

**13**  To the Son came the Holy Spirit. The Father and the Son created somebody; and said
`to-son go holy-spirit father son create somebody and_said`

**14**  the Father, the Holy Spirit: in what way? Somebody's form the Father wanted.
`the_Father holy-spirit on-how? somebody form want father`

> The angels bow on this page, and Lucifer is sent away by the Father's
> command. Adam is not made until 002v, so this is not the *Life of Adam and
> Eve*'s command to bow to Adam; it opens with the birth of the mother of the
> Lord God. The signs say Lucifer bowed (lines 7, 10); *would not* and
> *refused* are supplied. An earlier note here called it the distinguishing
> episode of the *Life of Adam and Eve*, which was wrong.

## 002v — the Trinity, and the making of Adam

**1**  The Son, the Spirit, created; and the Son said: in the form, in the Lord.
`son spirit create and_said son on-of form on-Lord`

**2**  he created [a likeness]: man is, all one, to the Father, the Son,
`create [likeness] exist man^ all^ one to-father son`

**3**  the Spirit. Father, Son and Spirit took man, and every living thing [creature]
`spirit grab father son spirit somebody each,_every living [?]`

**4**  The soul heard. The man saw the living, truly, not many |
`soul hear man^ see living righteous not many | from`

**5**  Father and Son — not many; the Holy Spirit; but this Lord is all,
`father from son not many holy-spirit a) this Lord each,_every`

**6**  one God. And God said, the angel, to Elijah the prophet.
`one God and_said God angel Elijah prophet`

**7**  Elijah the prophet, when there were Father, Son and Spirit, going forth
`prophet Elijah then-exist father son spirit to-go`

**8**  […] […] and the brethren, in this world, and […] |
`table [?] in_turn-brother on-this world and [?] | to`

**9**  to Paradise the Lord God created man of the slime of the earth; and then
`Paradise Lord_God man^ create slime_(of_the_earth)* and then`

**10**  man was created of the aforesaid slime of the earth, and became a soul, one.
`man^ ~exist create aforesaid slime_(of_the_earth)* and became* to-soul-+one`

**11**  he created, breathed on Adam; and he became living, and
`create breathe on-Adam and living leave and`

**12**  the Lord God took the man, and the man went into
`man^ grab Lord_God and man^ go inside`

**13**  Eden; and all [things] he created before man.
`Eden and all^ create before man^`

> Line 11 is Genesis 2:7 — the breath, and the man becoming a living being.
> Line 5 is a Trinity formula: Father and Son, not many, one God.

## 003r — the commandment, and the sleep

**1**  And the Lord God said: Adam, I the Lord take this Adam.
`and_said Lord_God Adam I_the_Lord this-Adam grab`

**2**  every truly [nor] hunger, and thirst [nor] upon Adam; and
`each,_every righteous(ly) [?] be_hungry and thirsty [?] this-Adam and`

**3**  one living [thing] dies. There shall be sin, hunger, thirst, to the girl …
`one living die sin have hunger thirsty girl-to`

**4**  [afterward] the Lord took. To Adam, all truly one.
`[?] grab-Lord this-Adam each,_every righteous(ly) one`

**5**  the commandment, this yoke upon Adam, by commandment: do not eat.
`commandment this yoke this-Adam command = not eat.`

**6**  this to the son: the forbidden fruit — thou shalt die if Adam eats.
`this to-~son forbidden_fruit thou_shalt_die* ~if Adam exist eat.`

**7**  […] Adam would die. And then Adam slept within |
`[?] die-Adam and then-exist Adam sleep inside | to`

**8**  Paradise; and then upon this, fill, first, from the hour; and | then
`Paradise and then on-this fill ~first from hour and | then`

**9**  the Holy Spirit came within into Paradise, and said: this
`exist go holy-spirit inside into_Paradise and_said this`

**10**  <subject marker> this the garden and the Lord God took Adam
`[?] this [?] and grab Lord-<divine> Adam`

**11**  rib, and Eve he created. The angel said to you:
`rib and Eve create say angel you`

**12**  mother. And then Adam, from laughter, said this |
`mother and then Adam from laugh* and_said this | to`

## 003v — the rib, Eve, and the serpent

**1**  Bone of bone; and the two souls are one. | Before
`bone bone in_turn two soul one | before`

**2**  year, by name, and five said the angel. The Lord God departed from heaven | Chapter.
`~year-+name and five say angel leave Lord_God from_heaven* | in_turn-chapter`

**3**  year, was; and Eve went into Eden; and | when
`~year-~exist and go Eve on-Eden and | then`

**4**  Eve went to this tree: what tree?
`exist Eve go to-this tree what tree`

**5**  was the Lord God's command; and [he] showed one
`exist Lord_God command = and show^ one`

**6**  the serpent on this tree: what tree is it?
`serpent on-this tree what tree exist`

**7**  the Lord God commanded; and said this serpent to Eve:
`Lord_God command = and_said this serpent Eve`

**8**  eat this fruit; and Eve said: we shall not eat, eat,
`~eat this fruit and_said Eve shall_not_eat eat`

**9**  because, Eve, Adam's Master commanded; and said
`because Eve Adam Master command = and_said`

**10**  this serpent: Eve ate, Eve [and] Adam.
`this serpent Eve eat Eve Adam`

**11**  one this fruit; in turn the fruit <subject marker> was Eve['s];
`one this fruit in_turn fruit SUBJ exist Eve`

**12**  one Adam ate; Eve [and] Adam knew
`one Adam eat exist Eve Adam know`

> Genesis 3:2-3, Eve's answer to the serpent. Király & Tokai read *not
> [eat]* at line 8 and *Master* at line 9, where they note "? God (in the
> Garden of Eden)". Corrected 2026-09-26: Book One had Eve eat against a
> commandment laid on Adam; here she refuses because of it.

## 001r — good and evil, shame, and back to Elijah

**1**  evil and good, as the Lord God knows. And then they plucked,
`evil and good as Lord-God know and then pluck`

**2**  the serpent, this fruit, this serpent; and | then
`serpent this fruit this serpent and | then`

**3**  the day Eve took; in turn Eve took the fruit.
`day grab Eve in_turn Eve fruit grab`

**4**  Adam. And then were opened immediately; Adam naked.
`Adam and then were_opened* immediately Adam naked`

**5**  Eve saw Adam; and then Eve [and] Adam
`see Eve Adam and then Eve Adam`

**6**  was ashamed. And [chapter] six: the angel of God said to Elijah […]
`be_ashamed_of_sg and six say God angel to-Elijah [?]`

**7**  Elijah; and this [deadly sin] did Lucifer,
`Elijah and this [deadly_sin] ~do Satan`

**8**  the Father of heaven, whom Satan should bow down to | Father
`the_father heaven who-+SUBJ Satan exist bow | father`

**9**  God from heaven, and the brethren, hell; and seven said
`DIV from_heaven* in_turn-brother hell* and seven say`

**10**  the angel of God to Elijah the prophet: Elijah, the Lord God departed
`God angel to-Elijah prophet Elijah leave Lord-<divine>`

**11**  from heaven, land, within Eden, saying
`from_heaven* ~land inside Eden say`

## 001v — where art thou

**1**  The Lord God, upon the angel, this fill, two from the hour; and then departed.
`Lord_God on-angel this fill two from hour and then leave`

**2**  The Lord God from heaven within into Paradise; and the Lord God said:
`Lord_God from_heaven* inside into_Paradise and_said Lord_God DIV`

**3**  Adam, why? And Adam said: Adam hid from the Lord God.
`Adam why? and_said ~Adam hide-~Adam Lord_God`

**4**  And the Lord God said: why, Adam, hide? And Adam said:
`and_said Lord_God why? ~Adam hide and_said ~Adam`

**5**  who … this Adam naked? said the Lord God: why, Adam,
`who this-~Adam naked say Lord_God why? ~Adam`

**6**  naked? And Adam said: Eve [gave] Adam food. And said
`naked and_said Eve Adam food and_said.`

**7**  the Lord God: Eve, where? And Eve answered: I …
`Lord_God Eve where? and_said answered* Eve I-to`

**8**  And the Lord God said: why, Eve? Eve answered: who … Eve naked?
`and_said Lord_God why? Eve answered* who Eve naked`

**9**  And the Lord God said: why, Eve, naked? And Eve said:
`and_said Lord_God why? Eve naked and_said Eve`

**10**  the serpent, Eve, food. And the Lord God said to Adam:
`serpent Eve food and_said Lord_God ~Adam`

**11**  to one commandment, this Adam … ten: the commandment observe.
`to-one commandment this ~Adam name-[?]-ten commandment observe`

> Genesis 3:9, "Where art thou?", and 3:13, "What is this that thou hast
> done?" — here as a repeated *Why, Eve?*

## 137v — a prayer to the Virgin, with the author's colophon

This is the page Király and Tokai published a reading of, so it is the one
place the work can be scored against theirs. Their published line is line 3,
and it matches.

**1**  Hail, O Virgin. Through holy Mary, mother of God, gate into Paradise
`healing-girl through holy-Mary mother God [?] [?]`

**2**  Queen Mary, heaven, wife, world; Mary ascends | this
`king-Mary heaven wife world ascend-Mary | this`

**3**  Mary, the one only Virgin Mary, you conceived Jesus without sin.
`Mary one only Virgin_Mary you ~conceive Jesus without sin`

**4**  Born of Mary, the Creator Lord; and from the Lord, the Redeemer, within the Lord | this N. [the author]
`be_born-Mary Creator_Lord and from Lord-redeemer inside Lord | this-NAME.author`

**5**  we do not doubt, [author]; we […] | I, [author],
`somebody do_not_doubt-<author>-somebody [?] | this-<author>`

**6**  somebody, you pray to, sin, | of N. [the author]
`somebody you pray to-~sin | of-NAME.author`

**7**  that then our soul ascends, remitted | of N. [the author]
`somebody then ascend soul remit | of-NAME.author`

**8**  somebody, the body. Amen. This prayer have.
`somebody body amen this pray have`

**9**  a hundred years, have mercy; healing, Mary; name high, have mercy; out, Mary | Lord
`hundred-year have_mercy healing Mary name-high have_mercy ~out-Mary | Lord`

> Király and Tokai's published reading of line 3 is *sin, without, Jesus,
> conceive, you-Mary*. That is the same line, in their order.
>
> The right-hand margin is a colophon: the author's own name sign repeated
> down the side of the page, once with "I" and twice with the genitive. The
> codex does not inflect, so a name sign standing where a pronoun would stand
> is how it says "I".

---

## 007r — the curse, and the sword at the gate

**1**  Adam was, the girl … Adam, in turn hands
`exist ~Adam girl-to [?]-~Adam in_turn hands`

**2**  gates Adam was; the earth to till
`[?] exist ~Adam earth [?]`

**3**  he wants food for the son, to take, in turn Eve, this Eve
`want to-~son food ~grab in_turn Eve this-Eve`

**4**  through yearning; and this Eve is in pain.
`exist through pine and this-Eve exist painful`

**5**  [to be] born, has; in turn this evil — this evil is
`~be_born have in_turn this evil this-evil exist`

**6**  [cursed] the earth slide and room
`[?] earth [?] ~and [?]`

**7**  evil. Man was made, all of this. The serpent dies; and
`evil this somebody create each,_every this serpent die and`

**8**  he departed from among Adam and Eve the Lord God; and there went
`leave among [?] Lord-<divine> and go`

**9**  the Lord God, the angel; Adam and Eve; flame,
`Lord_God angel Adam_and_Eve flame^`

**10**  a sword; and Adam and Eve out | within
`sword and Adam_and_Eve out | on-inside`

**11**  Paradise. He drove them out, and set an angel sword
`Garden_of_Eden exorcise and put angel [?]`

> Genesis 3:24 — the angel and the flaming sword set at the gate.
> *To till the earth*, line 2, is Király & Tokai's expression, cited here and
> at 125r03 (Genesis 3:23). Corrected 2026-09-26: Book One read it as
> "made from the earth, and to the earth he would return".

> The same passage is written again at 125r, and that copy reads a good
> deal further; read the two together (`ktdouble.py --show 007r`).

## 007v — outside the garden: Cain, Abel, Seth, and Adam goes blind

**1**  at the gate Eve, Eden; and one creature
`on-~gate Eve Eden and one create`

**2**  can be within Eden, but the angel. And the Lord God said,
`can_be inside Eden but angel and_said Lord_God`

**3**  upon the angel, this fill, three from the hour, and from two-two-two-two said | to
`on-angel this fill three from hour and from two-two-two-two say | to`

**4**  Elijah. The angel of God: Elijah, when the Lord God [drove] Adam
`Elijah God angel Elijah then-exist Lord-<divine> ~Adam`

**5**  out […] from Paradise; and then |
`out(ward) [?] on-Garden_of_Eden and then-exist | [?]`

**6**  Eve he dwelt in the field many years; and Adam had Eve
`[?] leave inside ~field many year and ~have ~Adam [?]`

**7**  offspring, these two sons. And the firstborn was Cain, and the second … named, was
`descendant this-two to-son and firstborn exist Cain and two before-end-+name exist`

**8**  Abel. Third, by name, was Seth. And then
`Abel third ~name exist Seth and then`

**9**  Adam was blind from the eyes; and then Adam went into Paradise
`~Adam from eyes blind and then go ~Adam inside Paradise`

**10**  the son […]; and this son was [Cain] the son [Abel]
`son [?] and this son exist [?] son [?]`

**11**  Adam. And then Adam said: bring, Adam, from the tree.
`~Adam and then say ~Adam bring ~Adam from tree.`

## 006r — Seth goes to Paradise for the branch

**1**  a branch. And then the branch to Adam he carries, immediately through
`one ~branch and then branch to-~Adam carry immediately through`

**2**  seeing; and then through seeing, immediately, through the eye, blind Adam sees;
`seeing and then through seeing immediately through eye see blind ~Adam`

**3**  and to heal Adam [sick]; and then Seth went | [to Paradise]
`and be_healed = ~Adam [sick] and then Seth go | [to_Paradise]`

**4**  the gate of Eden; and then to Seth appeared God's
`gate/open Eden and then Seth appear God`

**5**  angel; and God's angel said: Seth [answered], and went; one said, Seth:
`angel and_said God angel Seth [answered] and go one say Seth`

**6**  the father Adam, Seth <subject marker> goes into Eden | then
`the_father ~Adam Seth SUBJ go inside Eden | then`

**7**  there was father Adam; Seth carried from the tree a branch
`exist father ~Adam carry Seth from tree branch`

**8**  on the tree of mercy <subject marker> was Adam, the father; [he] committed sin; and Adam said,
`on-+the_tree_of_mercy SUBJ exist father ~Adam commit sin and say ~Adam`

**9**  Adam, then the seed Seth carried, immediately through
`~Adam then seed carry Seth immediately through`

**10**  seeing; and then through seeing, immediately, through the eye, the blind sees; and
`seeing and then through seeing immediately through eye see blind ~and`

**11**  Adam was made whole. And the angel said: truly <subject marker> speak; and then
`be_healed = ~Adam and_said angel righteous SUBJ speak and then`

**12**  the angel went into Paradise, and Seth carried the branch
`go angel inside Garden_of_Eden and Seth carry branch`

> This is the Legend of the Rood, in the *Life of Adam and Eve*: blind, dying
> Adam sends Seth back to Paradise, and Seth returns with a branch. The codex
> tells it twice over, lines 1–3 and 9–12, in nearly the same words.

## 006v — the branch brought home, and a city

**1**  out of Paradise, from tree […] Adam was, through
`on-Garden_of_Eden from [?] [?] exist ~Adam through`

**2**  sin. And then Seth took from the angel this branch;
`sin and then Seth ~exist ~grab angel this branch`

**3**  and then the branch Seth carried to Seth's father
`and then branch Seth carry to-of-Seth father`

**4**  Adam. And then Seth went into a town,
`~Adam and then Seth go inside one town`

**5**  and the town was named Jericho, where Adam was,
`and believe-end-+name town exist Jericho who exist ~Adam`

**6**  a house. And then he came [the way] recognize; and within, all from
`house and then-exist arrive can [?] [?] and inside each,_every from`

**7**  the town [the way] recognize; and then out of the town
`town can [the_way] recognize and then out town`

**8**  one [road]; and then Seth went, this [one, a name]
`one [road] and then Seth exist go this NAME`

**9**  and within [the way] recognize; and then Seth said, one
`and inside can [?] [?] and then-exist Seth say one`

**10**  <someone Seth meets> oh, of Seth, the Father, the Spirit, the Father <subject marker> recognize
`NAME oh of-Seth the_father spirit father SUBJ recognize`

**11**  Adam. And Adam's eyes were blind — Adam, whom the Lord
`~Adam and ~Adam exist eyes blind who ~Adam exist Lord`

**12**  God's, cast out out of Paradise by the angel; and then [the one, a name]
`God out cast_out on-Eden on-angel and then NAME`

**13**  from seeing the gospel; and found [the one, a name]; ten, two, two, ten years; and
`from-see gospel and find NAME ten-two-two-ten-year and`

## 008r — Noah and the ark

**1**  seven And then three at that time the Lord God appeared to Noah;
`[?] and then-exist [?] time appear Lord-<divine> Noah`

**2**  and then the Lord God said: Noah, sorrow, Lord, leave, who, somebody, of them, leave;
`and then and_said Lord_God Noah sad-Lord leave who somebody on-of leave*`

**3**  that he had made them, because [flood] he who keeps his commandment. The Lord God would have all
`create because [?] this who carry <of> commandment ~exist Lord-<divine> want each,_every`

**4**  destroyed. And the Lord God said: Noah, make one … the Lord | […]
`destroy and_said Lord_God Noah do one exist Lord | [...]`

**5**  was the Lord; it was forty cubits long; in turn three hundred
`~exist Lord exist on-two-two-ten cubit long in_turn three_hundred*`

**6**  broad, in turn five high; one hid. Noah took every creature two by two; and
`broad in_turn five high one-hide grab Noah every create two-DISTR-two and`

**7**  [inside] the ark. And then this [dove]: I, this Noah, go, Lord.
`[inside] of-ark and then this [dove] I this-Noah go-Lord`

**8**  And then Noah took every creature two by two, and went before the Lord God;
`and then Noah grab every create two-DISTR-two and go before Lord_God`

**9**  and within was the Lord God, to the cup; and to the Lord lost, and [drunken]
`and inside-~exist Lord_God to-cup and to-Lord lose* and [drunken]`

**10**  the Lord God; every four directions; the water dispersed, fifth, from heaven high
`Lord_God every two-two direction water disperse fifth from_heaven* high`

**11**  and the rain came, forty; and five towns were destroyed.
`and go rain forty and five town destroy`

**12**  The Lord God; and the angel of God said [to] Elijah: the Lord God was [with] Noah;
`Lord_God and_said God angel Elijah say exist Lord_God Noah`

**13**  Noah remain all this [three] was; and the other [sons] departed; and this
`[?] [?] each,_every this [?] exist and two [?] leave and this`

## 008v — from Noah to Abraham

**1**  the people were, until Abraham the forefather were pagans believed.
`people exist until Abraham forefather [?] believe`

**2**  From Noah it was, until Abraham, seven … And said
`from Noah exist until Abraham seven-[?] and_said`

**3**  the angel of God to Elijah the prophet: Elijah, among these
`God angel to-Elijah prophet Elijah inside these`

**4**  believe. One man was saved in that time.
`believe one somebody ~be_saved inside time`

**5**  The angel departed from before Elijah the prophet; and these said
`leave angel before Elijah prophet and these say`

**6**  <subject marker> Elijah the prophet wrote; and [holy Enoch] […]
`[?] write Elijah prophet and [?] [?]`

**7**  within one chapter Elijah of the writing.
`inside [?] chapter [?] <of>-write`

## 005r — Abraham and Isaac

**1**  […] and the son went [with] the father |
`[?] and go-son-father | [?]`

**2**  the father; and a sheep, and a lamb.
`father and one sheep and one lamb`

**3**  … the son; the father [would] sacrifice. And the father Abraham said:
`who-~exist son father sacrifice and_said father Abraham`

**4**  for love of the Lord, to hide, the Lord, the Lord God's offering. And then Isaac
`from love Lord to-hide-Lord Lord_God offering and then Isaac`

**5**  was tie up […] who was [ram] Isaac [instead]
`exist [?] [?] who exist [?] Isaac [?]`

**6**  name Abraham sacrificed, and drew out […]
`[?] Abraham sacrifice and take_out [?]`

**7**  […] […] […] Isaac he would slay;
`understand-girl-chapter [?] [?] Isaac want slay`

**8**  and the Lord God cried out from the cloud, by the angel of the Lord God,
`and shout Lord-<divine> on-cloud on-angel <of>-Lord-<divine>`

**9**  Stop, Abraham! … will <subject marker> this.
`stop Abraham-to will SUBJ who this.`

**10**  Abraham. The Lord God. Love the Lord.
`Abraham Lord-<divine> love Lord`

**11**  this is peace to the Lord.
`[?] to-Lord peace`

**12**  And then he looked up and saw,
`and then-exist from see look_up`

**13**  Abraham, and saw
`Abraham and see`

**14**  […] a lamb
`understand-eat ~lamb`

**15**  in a thornbush.
`on-understand-eat (thorn)bush`

> Genesis 22:13, the ram caught in the thicket. The page is laid out in short
> lines, which is why the last four are three or four words each.

## 005v — the ram, and a prophecy of Christ

**1**  And then, from the lamb sacrifice, the Lord God said from the cloud,
`and then from lamb sacrifice and_said Lord_God on-cloud`

**2**  from the angel of the Lord, to Abraham: born within of Isaac
`on-angel of-Lord Abraham say ~be_born inside of Isaac`

**3**  one holy Mary; from the Virgin Mary a son born, to whom
`one holy-Mary from virgin-Mary on-be_born son to_whom`

**4**  The son is the body, Jesus; and the Lord went among the people
`son exist ~body Jesus and go Lord among_the_people*`

**5**  He preached the gospel, did many various miracles,
`exist gospel preach many various miracle ~do`

**6**  and the Lord suffered crucified; and on the third day rose from the dead.
`and suffer Lord [?] and [?] from die stand_up-Lord`

**7**  And the Lord God said, from the angel, to Abraham: and from seeing, the Lord's chapter is
`and_said Lord_God on-angel Abraham and from-and-see chapter-Lord exist`

**8**  believe truly [in] the Son of the living God; every man is saved […]
`believe righteous(ly) son living God each,_every somebody be_saved [?]`

**9**  One man […]; but every man is saved [from] the yoke; and
`one somebody [?] a) each,_every somebody be_saved yoke and`

**10**  man […] the Lord […] believes; and one […] […]
`somebody Lord [?] believe and one [?] [?]`

**11**  but every man was damned, from Adam, trespass, table, until Abraham,
`but everybody = be_damned from ~Adam ~trespass table until Abraham`

**12**  a hundred years and twenty years; from Abraham <subject marker> [until]
`one hundred-year and ten-ten-year from Abraham [?] table [?]`

**13**  Moses one thousand five hundred and fifty from Abraham until
`Moses half-+three_thousand and fifty from Abraham until`

> Line 13 first read as three blanks. The numerals are five strokes and a
> thousand sign, five strokes and a ten sign, read by Király & Tokai's rule
> that the sign after a group of strokes multiplies it (2026-09-20).

> The angel gives Abraham the whole gospel in advance: a virgin's son named
> Jesus, who preaches, works miracles, suffers, and rises. Then the book
> starts counting years between the patriarchs, which is what a world
> chronicle does.

---

## 015r — David the king

**1**  did; David the king humbled himself against the Lord God.
`~do David king humble against Lord_God.`

**2**  The king began repentance, did; anointed king [of] the Lord God.
`repentance begin king ~do anointed king Lord_God.`

**3**  have mercy; and the king's sin — have mercy. At that time there appeared to the king
`have_mercy and sin king have_mercy time appear king`

**4**  the angel of God; and the angel of God said [to] David the king: the Lord God
`God angel and_said God angel David king Lord_God`

**5**  The king <subject marker> sin, have mercy. The king keeps the Lord's commandment; and
`king [?] sin have_mercy carry-king <of>-Lord commandment and`

**6**  the Lord confirmed the king <subject marker> on the king's throne; and the king proclaimed [it to] the people.
`confirm-Lord king SUBJ on-of-king throne and announce king people`

**7**  [the Lord] there shall be born say a son [of David]; the son shall be the Son
`[?] on-be_born host [?] son [?] son exist son`

**8**  of God. And the angel departed from before David […]
`God and leave angel before David [?]`

**9**  From David the king until the Virgin Mary, born, years:
`from David king until Virgin_Mary be_born-~year`

**10**  … out, half … and … hundred years, and one hundred years
`~out-half-to-[?] and [?]-hundred-~year and one hundred-~year`

**11**  out, nine hundred and one hundred years | two, two, two
`~out nine_hundred and one hundred-~year | two-two-two`

**12**  ten years and five, from David the king until the Virgin Mary
`ten-~year and five from David king until Virgin_Mary`

## 015v — the count of years

**1**  the years: from Adam's trespass, out, until the Virgin Mary | was born,
`be_born-~year from Adam ~trespass ~out until Virgin_Mary | be_born`

**2**  years: five thousand and one hundred years and fifty
`+day +five_thousand and one hundred-+day and +fifty`

> Lines 1 and 2 first read as blanks. The sign now read Adam is one Király &
> Tokai's own entry lists as a spelling of Adam at 100v; the numerals are
> five strokes + thousand and five strokes + ten. So the book dates the
> Virgin's birth from Adam at 5,158 years, and the birth of Christ on 021r
> follows the same formula (2026-09-20).

**3**  and four years, and four years.
`and two-two-year and two-two-year`

## 016r — Saint Luke

**1**  Saint Luke writes, the sixth throne of his writing, from, remain, kiss(?).
`write holy-Luke six-throne of-write from remain* kiss?.`

**2**  exist […] they gave thanks, and prayed to the Lord God.
`[?] [?] thanks grab and pray to-Lord-<divine>`

## 016v — Joachim's offering is refused

**1**  And Saint Anne …; of the two of them, all their riches divided in three parts:
`and holy-Anne mouth-~year from-two from_both every of-rich divide on-+three part`

**2**  one division they gave to the people of the temple; a second division
`one division grab to_the_people_of_the_temple = second division`

**3**  to the Lord's way-people; the third division Joachim and his household lived on.
`from-Lord way people third division Joachim-+one-+his_household living.`

**4**  And all Joachim's household gave thanks, thanks, to the Lord God; in turn had | Joachim
`and every Joachim's_household thanks thanks Lord_God in_turn have | Joachim`

**5**  his household, born thirty years; and he prepared the offering.
`his_household ~be_born thirty year and prepare offering`

**6**  it is the chapter: every one of … creatures; and then, and from Joachim
`exist-chapter every of-in_turn-+one-[?] creature and then and from Joachim`

**7**  he brought his offering; and at Joachim looked the chief
`carry <of> offering and to-Joachim see from head`

**8**  the Jews; and this high priest said [to] Saint Joachim:
`Jew and_said this high_priest = holy-Joachim`

**9**  food, this Joachim, [the temple], who … Joachim goes
`food this-Joachim [the_temple] who Joachim* go`

**10**  among the neighbours; the food of the offering, [the temple], one [portion]
`among of neighbor food of offering [the_temple] one [portion]`

**11**  and Joachim [is] cast out of this temple; and sorrowfully
`and out Joachim cast_out on-this temple and sad`

**12**  Joachim departed, and went into the field, into the forest, … from the shepherd
`Joachim leave and go inside field inside forest chapter-of from shepherd`

**13**  and from the sheep, the shepherd, and on one mount, one
`and from sheep shepherd and on-one mount one`

> The Protevangelium and the Golden Legend: Joachim divides his substance in
> portions, the high priest refuses his offering because he is childless, and
> he goes off into the wilderness.

## 017r — the angel comes to Joachim

**1**  a lamb sacrifice; and then the lamb sacrifice [rejected]
`lamb [?] and then-exist lamb [?] [?]`

**2**  At that time, when Joachim was appear God [in the desert]
`time then-exist Joachim exist [?] God [?]`

**3**  And the angel of God said: Joachim, … heard [the Lord God]
`and_said God angel Joachim have hear [the_Lord_God]`

**4**  … prayer; and the angel of God said: Joachim, this [hath had mercy]
`of-~pray and_said God angel Joachim this [hath_had_mercy]`

**5**  The Lord God has had mercy. Go home, Joachim; and at the golden
`Lord-<divine> have_mercy go Joachim to-home and on-golden`

**6**  gate — this Joachim departed — Joachim's wife Anne, and conceived
`gate this Joachim leave <of>-Joachim wife Anne and [?]`

**7**  one: the Virgin Mary. And then she is born, and [shall conceive]
`one Virgin_Mary and then ~be_born and [shall_conceive]`

**8**  The Virgin Mary is Mary; and Mary remits, bears a son, whose
`Virgin_Mary exist Mary and remit Mary on-be_born son whose.`

**9**  The son shall be, by name, Jesus; and the Lord went among the people
`son exist ~name Jesus and go-Lord among_the_people.*`

**10**  He preached the gospel, did many various miracles, and suffered,
`exist gospel preach many various miracle do and suffer`

**11**  the Lord crucified; and on the third day rose from the dead; and ascend shall be saved,
`Lord [?] and [?] from die stand_up-Lord and [?] be_saved`

**12**  every one in all the world; and the man who believes in the Lord. And the angel departed
`every all_the_world world and somebody Lord exist believe and leave angel`

**13**  from before Saint Joachim; and at that time the angel appear
`before holy-Joachim and time then-exist angel [?]`

## 017v — the golden gate, and Mary carried nine months

**1**  the angel of God [to] Saint Anne: […] this Anne, […] the Lord God has had mercy, has heard
`God angel holy-Anne have this Anne [?] Lord-<divine> have_mercy hear`

**2**  the Lord God, Anne's prayer. Go home, Anne; and
`Lord_God of-Anne ~pray go Anne to home and`

**3**  at the golden gate Anne left the Lord's Joachim, and conceived one:
`on-golden gate leave Anne of-Lord Joachim and conceive one`

**4**  the Virgin Mary. And then was born the body, the Virgin Mary — she is Mary;
`Virgin_Mary and then be_born body Virgin_Mary exist Mary`

**5**  and Mary remits, bears a son, to whom the son is, and the body,
`and remit Mary be_born son to_whom son exist and-body`

**6**  Jesus; and the Lord went among the people; he preached the gospel, [did] many various
`Jesus and go Lord among_the_people* exist gospel preach many various`

**7**  miracles; and the Lord suffered crucified; and on the third day from death
`miracle do, and suffer Lord [?] and [?] from die`

**8**  the Lord rose; and ascended; saved every one in all the world; and the man who is the Lord's
`stand_up-Lord and ascend* be_saved every all_the_world world and somebody Lord exist`

**9**  believes. And the angel departed from before Saint Anne; and she conceived the blessed
`believe and leave ~angel before holy-Anne and conceive happy`

**10**  Virgin Mary. And Mary carried the child nine months, in turn ten, the child was born; and this
`Virgin_Mary and from Mary foetus carry nine moon in_turn ten foetus be_born and this`

**11**  out, two months; and on out, five; and at six years
`out two moon and on-out five and on-six-year-to`

**12**  out, from Adam's trespass until the Virgin Mary was conceived and born:
`~out from Adam ~trespass until Virgin_Mary conceive and on-be_born.`

**13**  five thousand and one hundred and fifty and
`+five_thousand and one hundred and +fifty and`

> Lines 12 and 13 first read as blanks; the same Adam-to-Mary count as 015v
> (2026-09-20).

> The meeting at the Golden Gate, and the conception of Mary. Line 10 is the
> kind of detail no paraphrase invents: nine months carried, born in the tenth.

## 018r — Gabriel: Hail, full of grace

**1**  Five months, until the offering in the temple, the blessed Virgin Mary.
`half-ten moon until offering inside temple blessed^ Virgin_Mary`

**2**  And then Mary was in [the temple] three days; from the beginning she went and hid in the temple.
`and then Mary exist inside three_days from begin go-hide-this inside temple`

**3**  […] and said […] that Mary would keep her virginity |
`[?] and say [?] this-Mary want virgin-carry | <of>`

**4**  Of Mary, created. For ever and ever, amen. And then Mary
`Mary create for_ever_and_ever = amen and then Mary`

**5**  was twelve, the feast, and … three days; and at that time opened
`exist six-six feast and [?]-+three_days and time open`

**6**  the Father of heaven, because he saw hidden every world, darkness, the sky.
`the_Father heaven because see hide every world darkness sky.`

**7**  And at that time the Father of heaven opened, and went.
`and time open the_Father heaven and go.`

**8**  the Lord's angel Gabriel, in the temple, to the blessed Virgin Mary.
`of-Lord angel Gabriel inside temple blessed the_Virgin_Mary*`

**9**  Saint Luke writes chapter in his writing: at that time the angel said,
`write holy-Luke [?] <of>-write time say angel`

**10**  Gabriel: Hail, this Virgin Mary, full of grace! Out, the Lord God, Mary. And said
`Gabriel healing this-Virgin_Mary full_of_grace out Lord_God-Mary and_said`

**11**  this Virgin Mary: How can this be, this maiden knowing not … this maiden?
`this Virgin_Mary how? this exist can this-girl not_know this-girl`

**12**  … this maiden wants, the Virgin Mary, to keep … of the maiden, created …
`half-be_damned this-girl want Virgin_Mary carry of-girl create-[?]`

**13**  For ever and ever, amen. And the angel Gabriel said [to] Mary:
`for_ever_and_ever = amen and_said angel Gabriel Mary`

> Luke 1:28 and 1:34, in order, and the codex names Luke as its source two
> lines earlier.

## 018v — the Holy Spirit, and Elizabeth six months gone

**1**  has wanted, to the girl, this: the Holy Spirit goes; to every [one] mercy [full of grace]
`have want to-girl this go holy-spirit to-every have_mercy [full_of_grace]`

**2**  This maiden shall conceive a son; and the son's body is Jesus.
`this-girl conceive son and ~son ~body exist Jesus.`

**3**  And the Virgin Mary said, blessed, to one: this, say it; and blessed be the will from the Lord God.
`and_said Virgin_Mary blessed one-to this say and blessed want from Lord_God.`

**4**  this [power] <subject marker> the Lord, this overshadow; and then the maiden [answered]
`this [?] [?] Lord this [?] ~and then-exist girl [?]`

**5**  the Virgin Mary; the word of command to the Lord; Mary hid, this overshadowed, which maiden
`Virgin_Mary commandment word to-Lord-hide Mary hide this overshadow* who girl`

**6**  the angel said; at this he said: God the Father pours out on the Virgin Mary | the Holy
`exist angel say on-this say pour_out God_the_Father Virgin_Mary | holy`

**7**  Spirit; in turn to the Lord [came upon] one; went the Lord Jesus Christ, conceived, the Lord
`spirit in_turn to-Lord [came_upon] one go Lord-Jesus-Christ conceive Lord`

**8**  Christ. And then [departed from] the Virgin Mary. And the angel Gabriel said:
`Christ and then [departed_from] Virgin_Mary and_said angel Gabriel`

**9**  [to] Mary: Behold, thy kinswoman is six months gone |
`Mary have lo out(ward) six moon <of>-girl relative | [?]`

**10**  Elizabeth, who conceived; Mary; the son, Saint John [barren] within the chapter <subject marker>
`Elizabeth who conceive Mary son holy-John [barren] inside chapter SUBJ`

**11**  […] chapter; the Lord God's mercy to this […]; from John shall be the way
`go chapter Lord-<divine> <of> have_mercy to-this have from John exist way`

**12**  done [for] the Lord Jesus Christ, that is, the Lord [according to thy word] this
`do Lord-Jesus-Christ that_is Lord [according_to_thy_word] this`

**13**  Mary bore; and from the Lord went the Lord on the world; [he] is the Word, preaching
`Mary be_born and from Lord go Lord on-+world exist Word^ preach`

> Luke 1:35 and 1:36. John the Baptist is "the way made for the Lord Jesus
> Christ", which is the codex paraphrasing rather than quoting.

---

## A refrain, repeated word for word

One passage recurs verbatim at 005v:3–8, 017r:8–12 and 017v:5–8, spoken each
time by an angel to a different person — to Abraham, to Joachim, to Anne:

> a virgin shall bear a son, and the son shall be Jesus; he shall preach the
> gospel and do many miracles; the Lord shall suffer, and rise from the dead;
> and every man who believes shall be saved.

The same words in the same order, three times, hundreds of lines apart. That
is a formula, and it is the kind of internal repetition that can be checked
without any dictionary at all.

---

## 019r — Joseph

**1**  various miracles done; and the Lord suffered; the Jews
`various miracle ~do and suffer Lord Jew`

**2**  crucified [him]; and the man who believes in the Lord, that [he is] the righteous
`crucified and somebody to-Lord exist believe that righteous`

**3**  the Son of the living God — every man be saved; and one man
`son living God each,_every somebody [?] and one somebody`

**4**  is damned; and the Lord not believe; and one
`be_damned to and Lord [?] [?] and one to`

**5**  be saved but who believes not a man is damned. Here ends this holy gospel.
`[?] a) [?] somebody be_damned end this holy-gospel`

**6**  And at that time the angel was appear; the angel of God
`and time then-exist angel exist [?] God angel`

**7**  aged Joseph; and the angel of God said: aged
`aged Joseph and_said God angel aged`

**8**  Joseph. Go, aged one Joseph
`Joseph go very_old [?]`

**9**  in the temple, Joachim, the girl Mary, and this aged
`inside temple Joachim* girl Mary and this aged.`

**10**  Joseph was [already] aged […]
`Joseph exist [?] very_old [?]`

**11**  of the son, well-pleasing, from Mary, on being born; and then the son shall be born
`from son to-pleasing from Mary on-~be_born and then ~son on-be_born`

**12**  and the body; the son is Jesus; and from the Lord went among the people; is
`and-~body ~son exist Jesus and from Lord go among_the_people* exist`

**13**  the gospel preached, various miracles done, and the Lord suffered [death]
`gospel preach various miracle do and suffer Lord [death]`

> "The aged" is Joseph's standing epithet all through these pages, which is
> how medieval art paints him.

## 019v — the census of Augustus

**1**  the Jews crucified; and the man who believes in the Lord, that
`Jew crucified and somebody to-Lord exist ~believe that.`

**2**  truly the Son of the living God — every man is saved; and the first
`righteous son living God everybody = be_saved and first^`

**3**  man is damned; and the Lord not believes; and the first
`somebody be_damned to and Lord not believe and first^`

**4**  be saved but who believes not a man is damned. Here ends this holy gospel.
`to [?] a) [?] somebody be_damned end this holy-gospel`

**5**  And then out, the blessed Virgin Mary was sixteen years, at that time.
`and then out happy Virgin_Mary ten-six-year time.`

**6**  There was a decree, before […] the Lord Jesus Christ, twenty and | two
`exist commandment before [?] Lord-Jézus-Christ ten-ten and | two`

**7**  years; and on the birth, the first day, the Lord Jesus Christ; and.
`two-year and on-~be_born first^ day^ Lord-Jesus-Christ and.`

**8**  At that time Augustus the emperor commanded that
`time command Augustus emperor that`

**9**  all the world should be enrolled. And then the commandment of Augustus
`all^ world exist enrol and then commandment Augustus`

**10**  the emperor: all the world go back, the commandment, to the town. And | then
`emperor all^ world back go commandment town and | then`

**11**  it was, the two of them, Mary and aged Joseph, went |
`exist and from two Mary very_old Joseph go | to`

**12**  home And then the two, Mary and aged Joseph,
`[?] and then-exist two Mary very_old Joseph`

**13**  took the first ox and the first
`exist grab first^ ox and first^`

> Luke 2:1, the decree that all the world should be taxed.

## 020r — no room, and a manger

**1**  donkey; because this they took, aged Joseph
`donkey because this exist grab very_old Joseph`

**2**  the ox, the two of them — aged Joseph and Mary
`from ox who two very_old Joseph Mary`

**3**  exist remain [together] the two of them, the aged […]
`[?] [?] [?] who two very_old [?]`

**4**  remain and the donkey was aged Joseph's;
`[?] exist in_turn donkey exist very_old Joseph`

**5**  he took her who would bear this son | Mary and aged
`grab who this son on-be_born want | very_old-Mary`

**6**  Joseph took her away on the donkey; and then the two.
`Joseph on-donkey take_away and then two.`

**7**  aged Joseph, when he arrived | the aged
`very_old Joseph exist from arrive | very_old`

**8**  Mary and Joseph, [at] Bethlehem town; and […]
`Mary-Joseph Bethlehem town and [?]`

**9**  aged Mary and Joseph can [not] find lodging.
`can aged-Mary-Joseph lodging find`

**10**  none; but the two of them, Mary and aged Joseph, lodged within the first
`but leave two aged-Mary-Joseph inside first^`

**11**  barn; and [manger] […]
`barn and [?] [?]`

**12**  the first manger; and then bought, the aged [one].
`first^ manger and then buy aged.`

**13**  Joseph hay; and then the ox
`Joseph hay and then two ox`

> Luke 2:7 — no room, and the manger. The ox and the ass are not in Luke.
> They come from Isaiah by way of the Nativity plays.

## 020v — the birth, the star, and the angel's news

**1**  and the donkey; he laid the hay; and then the aged |
`donkey exist hay put and then-exist very_old | [?]`

**2**  the girl … a fire, the light begins; and then shoulder … half.
`girl-+mouth ~fire begin-light ~and then shoulder-to half.`

**3**  in the night the son was born; and the son was
`night time on-be_born son and son exist`

**4**  and the body, Jesus. At that time sky star
`and-~body Jesus time then sky star`

**5**  light through Bethlehem town; and then a star
`through light Bethlehem town and then-exist star`

**6**  the shepherds saw; and from the sheep, the shepherd; and then
`see the_shepherds and from sheep shepherd and then`

**7**  at the star, a miracle. At that time the angel Gabriel said: great
`on-star miracle time say angel Gabriel great`

**8**  joy! A king is born, a king <subject marker> born in
`joy be_born king king [?] be_born inside`

**9**  Bethlehem town, within barn, in a donkey's manger.
`~Bethlehem town inside [?] inside donkey manger`

**10**  [the ox], the donkey, love; hay within [the manger] [laid]
`[ox] donkey love hay inside [manger] [laid]`

**11**  Christ, Mary's son. And then […] went [to] Bethlehem;
`Christ Mary son and then-exist [?] go Bethlehem`

**12**  and then the sheep knelt, and every one of them knelt
`and then sheep kneel and every this exist kneel`

**13**  before the shepherds [hastened] to go another and […]
`before from [?] [?] to go [?] and [?]`

> Luke 2:10–11, the angel's "tidings of great joy" and the child born in the
> city of David.

## 021r — the reckoning of years

**1**  gave thanks, and gave thanks. Here ends this holy gospel [amen]
`thanks and thanks grab end this holy-gospel [?]`

**2**  Saint Luke writes, in one [then] of his writing, chapter [of the book] [the reading]
`write holy-Luke inside [?] [?] <of>-write chapter [?] [?]`

**3**  out, from Adam's trespass, until the birth of the Lord Jesus Christ.
`out from Adam ~trespass until be_born Lord-Jesus-Christ.`

> Line 3 first read as blanks; the same Adam-to-Christ formula as 015v and
> 017v, now that the Adam sign is read (2026-09-20).

**4**  five thousand and one hundred years and sixty years
`[?] and [?] hundred-year and two-two-two-ten-year`

**5**  and six years, until the birth of the Lord Jesus Christ.
`and six-year until be_born Lord-Jézus-Christ`

## 021v — the flight into Egypt, and the eighth day

**1**  At that time then, a fast, on the birth of the Lord Jesus Christ, three days,
`time then fast on-be_born Lord-Jesus-Christ three_days`

**2**  at that time the angel Gabriel said to the aged Joseph:
`time say angel Gabriel aged Joseph`

**3**  Rise up, and take this son and his mother, this son […]
`stand_up up and take^ this son and of this son mother.`

**4**  and flee into Egypt, and go, all this, begin [by night];
`and escape inside Egypt and go every this begin [by_night]`

**5**  out of Egypt [into] this; the angel [appeared] said day [Herod] Here ends
`out(ward)-out(ward) Egypt [?] this this angel [?] say [?] [?] end`

**6**  this holy gospel. At that time rose up the aged | Joseph
`this holy-gospel time stand_up up the_aged | Joseph`

**7**  [arise] and took the Lord Jesus Christ and his mother, and five
`[?] ~and grab Lord-Jézus-Christ and <of> mother and [?]`

**8**  days passed; then | [the Son, and the aged Joseph, and the holy mother Mary]
`day^ pass then | [the_son_and_the_aged_Joseph_and_the_holy_mother_Mary]`

**9**  year, Joseph, chapter; [they] went into Jerusalem town, that is, when was born
`~year-+Joseph-chapter go inside Jerusalem ~town that_is on-be_born`

**10**  the Lord Jesus Christ; on the eighth year, at that time, the son was circumcised,
`Lord-Jesus-Christ on-six-two-year time circumcise son`

**11**  and the son was named Jesus. And this Lord Jesus first
`and son exist [?] Jézus and this Lord-Jézus first`

**12**  man, the Lord's blood shed; and then the Lord.
`man* of-Lord blood shed and then Lord.`

**13**  circumcised the Lord Jesus in the Jerusalem temple; and fled
`circumcise Lord-Jesus inside Jerusalem temple and escape`

**14**  Mary his mother the Holy Spirit and Joseph
`[?]`

> Matthew 2:13 and Luke 2:21. Line 10 dates the circumcision to the eighth
> day, which is what Luke says, and lines 11–12 call it the first shedding of
> Christ's blood — a medieval devotional idea, not a gospel one.

---

## 022r — Egypt, and the twelve

**1**  into the land of Egypt; and [dwelt]; and the Lord went Joseph
`inside Egypt earth and [?] and go Lord [?]`

**2**  in the land of Egypt, into every city [idols] […]
`on-Egypt earth inside each,_every town [?] [?]`

**3**  evil fell, bowed down; and | … mother … Joseph.
`fall* evil bow_down and | [?]-mother-?Joseph.`

**4**  [arise]; die … from Joseph; they remained in Egypt twelve years.
`[arise] die from Joseph leave inside Egypt six-six-year`

**5**  at that time the angel Gabriel said Joseph
`time say ~Gabriel angel [?]`

**6**  Flee into the land of Egypt, into Nazareth city.
`escape on-Egypt earth inside [?] town`

**7**  And … mother … Joseph … left for Nazareth.
`and [?]-mother-+Joseph-chapter leave Nazareth.`

**8**  [in that] town twelve years; and five; and this [returned] table
`town six-six-year and five and this [returned] table`

**9**  twenty, two, nine years. Here ends this holy gospel. One
`ten-ten-two-nine-year here_ends this holy_gospel one`

**10**  day; he called twelve apostles; and three days preached; and | who, this
`day call six-six apostle and three_days preach and | who-this`

**11**  and this miracle did: the blind eye <subject marker> the Lord, through
`and-this miracle ~do eye blind SUBJ Lord through`

**12**  light; the dead <subject marker> the Lord resurrects; the evil among the people the Lord drives out.
`light die SUBJ Lord resurrect evil inside people exorcise-Lord`

## 022v — the signs, numbered

**1**  Before, that is, <subject marker> the Lord made wine of water; after these <subject marker> the Lord
`before that_is SUBJ Lord wine made water after_these SUBJ Lord`

**2**  broke five loaves of bread [for] five thousand people.
`break five loaves bread five_thousand people`

**3**  The second-two sign the Lord Jesus showed, when | in Nain.
`second-two can show Lord-Jesus then | in_Nain.`

**4**  before the town he raised up, from a widow, the son. The fifth
`before town resurrect from virgin-~woman son fifth`

**5**  sign the Lord Jesus showed, when he raised up the girl, lost.
`can show Lord-Jesus then resurrect girl lose*`

**6**  within Jerusalem. The sixth sign the Lord Jesus showed within the first
`within^ Jerusalem in_turn-six can show Lord-Jesus within^ first^`

**7**  town, when the Jews brought the first sick man
`town then Jew carry first^ ill`

**8**  before the Lord Jesus: a sick man, and a sick man, and a sick man, and a paralytic;
`before Lord-Jézus <sick_man> and <sick_man> and <sick_man> and paralytic`

**9**  and the sick, the sick, the sick, the paralytic — the Lord Jesus healed; in turn, seven
`and sick_man sick_man sick_man paralytic heal Lord-Jesus in_turn-+seven`

**10**  The sign the Lord Jesus showed within Capharnaum, because [he] raised from the dead
`can show Lord-Jesus within^ Capharnaum because raise_from_the_dead =`

**11**  two servants of the first soldier; and the soldier was named:
`two servant first^ soldier and name soldier.`

**12**  the centurion The eighth sign the Lord Jesus showed
`exist [?] in_turn-six-two can show Lord-Jézus`

**13**  within Tyre town: the girl, the first woman, a head.
`within^ Tyrus town girl first^ ~woman head`

> First the water into wine at Cana, John 2:11, which the gospel itself calls
> the first of the signs. Then the centurion's servant at Capernaum, Matthew
> 8:5, and the Syro-Phoenician woman at Tyre, Mark 7:24 — both named by the
> right place. The fourth is the widow's son at Nain, Luke 7:11, which is
> Király & Tokai's reading of lines 3-4. Corrected 2026-09-26: the earlier
> printing, and Book One, left the place and the widow out.

## 023r — the ninth, tenth and eleventh signs

**1**  a pagan; and within the girl was a devil; and the evil [one]
`one pagan and inside girl exist devil = and evil^`

**2**  the Lord drove out. The ninth sign the Lord Jesus showed in | …
`out exorcise-Lord in_turn-nine can show Lord-Jesus inside | exist.`

**3**  a proud man paralytic because the man […]
`proud on-one [?] somebody because somebody [?]`

**4**  did. The tenth sign the Lord Jesus showed in Galilee:
`do in_turn-ten can show Lord-Jesus inside Galilee`

**5**  a king's son, because he was at the point of death; and the son […]
`one king son because exist on-die and son [?]`

**6**  did. And [the next] sign the Lord Jesus showed in Jerusalem: the evil
`~do in_turn-and can show Lord-Jesus inside Jerusalem evil^`

**7**  spirit, when the Lord cast a devil out of one man.
`then Lord inside one man^ devil = exorcise`

**8**  First, before the birth of the Lord Jesus Christ, the Son of God cannot
`first before be_born Lord-Jézus-Christ son God [?]`

**9**  a prophet, a forefather, this […]
`one prophet one forefather this [?]`

**10**  did as Christ did; and by miracle they confessed
`~do as Christ ~do and miracle confess`

**11**  that the Lord Jesus is truly the Son of God. five confessed […]
`[?] Lord-Jézus righteous(ly) son God [?] confess [?]`

**12**  the Lord Jesus that the Lord Jesus is truly the Son of God. First confessed
`Lord-Jézus [?] Lord-Jézus righteous(ly) son God first confess`

**13**  … the Lord Jesus: Moses and Elijah. The second confessed
`~have Lord-Jesus Moses and Elijah second confess`

> The king's son at the point of death is John 4:46–54, and "at the point of
> death" is the gospel's own phrase.

## 023v — who confessed him, and the Transfiguration

**1**  … the Lord Jesus: the Father of the Lord. The third confessed the devils,
`~have Lord-Jesus the_Father of-Lord third confess devil =`

**2**  that the Lord Jesus is truly the Son of God. The second-two confessed
`that* Lord-Jesus righteous son God second-two confess ~have`

**3**  the Lord Jesus — the angel, that the Lord Jesus is truly the Son of God. Fifth
`Lord-Jesus angel that Lord-Jesus righteous son God fifth`

**4**  They confessed […]; and the earth, the sun,
`confess [?] and earth sun [?]`

**5**  the moon, that the Lord Jesus is truly the Son of God; and all this confessed.
`moon that Lord-Jesus righteous son God and this every confess.`

**6**  that the Lord Jesus is truly the Son of God. First confessed it Saint Peter,
`[?] Lord-Jézus righteous(ly) son God first confess holy-Peter`

**7**  Moses and Elijah. Saint Luke writes that when
`[?] and Elijah write holy-Luke then-exist`

**8**  the Lord Jesus was thirty years, at that time the Lord Jesus went […]
`Lord-Jézus inside thirty [?] time go Lord-Jézus [?]`

**9**  [to] Mount Tabor with his apostles; and he was transfigured; and
`Mount_Tabor and <of> apostle and be_glorified ~and`

**10**  the disciples saw Moses and Elijah [in] white clothes,
`see disciple^ Moses and Elijah white clothes`

**11**  and they saw the light [from heaven]; and then there stopped | the Lord
`and see light [from_heaven] and then stop | Lord`

**12**  Jesus, and Moses and Elijah; and then the apostles, through
`Jézus and [?] and Elijah and then-exist apostle through`

**13**  took fright, down [fell], bowed; and then the disciples, the voice.
`take_fright and down [fell] bow and then disciple^ voice.`

> Peter's confession, Matthew 16:16, "Thou art the Christ, the Son of the
> living God" — and the codex names him. Then the Transfiguration on Tabor
> with Elias, and Matthew 17:6, "they fell on their face, and were sore
> afraid."

## 024r — Tabor and Carmel, and the baptism

**1**  heard this word spoken [beloved] of the Son; and the Father mouth [voice] […]
`hear this word say [?] <of> son and father [?] [?] [?]`

**2**  and then home [alone] not the apostles, and not every […]
`and then-exist home [?] not apostle and not each,_every [?]`

**3**  but to the Lord Jesus. Here ends this holy gospel. The second confessed
`but to-Lord-Jesus here_ends this holy_gospel second confess`

**4**  … the Lord Jesus, the Father of the Lord: first on Mount Tabor,
`~have Lord-Jesus the_father of-Lord first on-Tabor`

**5**  second on Mount Carmel. Because then the Lord Jesus, at thirty-
`second on-Carmel to-mount because then Lord-Jesus inside thirty`

**6**  one years, at that time the Lord Jesus went to be baptized [by] Saint John,
`one-~year time go Lord-Jesus to baptize holy-John`

**7**  […] to Mount Carmel; and then the Lord went |
`[?] on-Carmel to-mount and then-exist Lord go | to`

**8**  [to] Saint John. The Lord Jesus said: John […]. The Lord said | Saint
`holy-John say Lord-Jézus John [?] Lord say | holy`

**9**  John: Master, and […] [came] baptize. And the Lord Jesus said,
`John Master and [?] [?] [?] and say Lord-Jézus`

**10**  John baptize the Lord; and […] is baptize
`John [?] Lord and [?] exist [?]`

**11**  Saint John baptized; he saw baptized the Lord Jesus. Then
`holy-John baptize see-baptize Lord-Jesus then`

**12**  the Lord was thirty years old; and appear the Holy Spirit
`to-Lord inside thirty year and [?] holy-spirit`

## 024v — the dove

**1**  in the form of a dove, and said: He is of the Son.
`inside ~form dove and_said he of son`

**2**  he who the Spirit came to rest; and the Lord took
`[?] spirit calm_down and Lord grab`

**3**  the Holy Spirit; and the Lord went into field
`holy-spirit and Lord go inside [?]`

**4**  the Lord Jesus fasted forty days. The third confessed
`fast Lord-Jesus forty_days third confess`

> Matthew 3:16–17 — the Spirit descending like a dove, and the voice naming
> the Son.

## 025r — the devils confess him

**1**  the devils that the Lord Jesus is truly the Son of God. Because when
`hell evil [?] Lord-Jézus righteous(ly) son God because exist`

**2**  the Lord Jesus was thirty years old, at that time the Lord Jesus went into |
`Lord-Jézus inside thirty year time go Lord-Jézus inside | exist`

**3**  [afterward] the town; and then he went into Capharnaum. At that time
`[afterward] town and then go inside Capharnaum time`

**4**  a man knelt down before the Lord Jesus,
`then-exist kneel_(down) one somebody before Lord-Jézus`

**5**  and said, Lord, the man's mouth: I have one son, and in [him]
`and_said Lord mouth man^ have one son and inside-+SUBJ`

**6**  a devil [cast out]. The man's son — his apostles son could not
`hell evil [?] somebody son <of> apostle to-hide_oneself-to [?] can`

**7**  heal [him]. That he begged the Lord to heal this, our son. Said
`heal that* ask heal this Lord our son say`

**8**  the Lord Jesus: have mercy, gain [lunatic] son; [he] can, from the year, [be] a healthy man.
`Lord-Jesus have_mercy gain [lunatic] son can from-~year healthy_man^`

**9**  And then the son came before the Lord Jesus; and […]
`and then-exist son go before Lord-Jézus and [?]`

**10**  he was made whole; and this three confessed — the devils that
`healing leave-to-leave and this [?] confess hell evil [?]`

**11**  the Lord Jesus is truly the Son of God, because by miracle they confessed. The second-two
`Lord-Jesus righteous son God because miracle confess second-two`

**12**  confessed […] the Lord Jesus — the angels, at the birth of the Lord Jesus
`confess have Lord-Jézus angel on-be_born Lord-Jézus`

**13**  Christ. Because then the Lord Jesus was born [in] Bethlehem
`Christ because then Lord-Jesus be_born Bethlehem`

> Matthew 17:14–18: the father kneels, the disciples could not cure the boy,
> and Jesus does.

## 025v — the Nativity told again

This page repeats 020v almost word for word, as the proof that the angels
confessed him.

**1**  town; and first, before the birth, one hour was
`town and first before be_born one hour exist`

**2**  […] a star, light through Bethlehem town; and | then
`[?] star through light Bethlehem town and | then`

**3**  the star; the shepherd saw it; and from the sheep, the shepherd.
`exist star see shepherd and from sheep shepherd.`

**4**  and then at the star, a miracle. At that time the angel said [shepherds]
`and then-exist on-star miracle time say angel [?]`

**5**  great joy! A king is born, a king <subject marker>
`[?] joy be_born king king [?]`

**6**  born in Bethlehem town, in a barn, in a donkey's
`be_born inside ~Bethlehem town inside barn inside donkey`

**7**  manger [ox] the donkey, in the hay, in
`manger [?] donkey inside hay inside`

**8**  [manger] [laid] Christ, Mary's son. And | then
`[manger] [laid] Christ Mary son and | then`

**9**  the shepherd went [to] Bethlehem; and then
`exist* shepherd go Bethlehem and then.`

**10**  […] knelt down, and every one of them knelt | and
`[?] kneel_(down) and each,_every this ~exist kneel_(down) | ~exist`

**11**  [and then] from the shepherd [hastened] to go another and
`[and_then] from shepherd [hastened] to go another and`

**12**  [the Most High Lord] gave thanks, and gave thanks. Here ends this holy gospel.
`[?] thanks and thanks grab end this holy-gospel`

**13**  […] confessed […] the Lord Jesus […]
`[?] confess ~have Lord-Jézus [?]`

---

## A grammar rule read out of the text

The codex counts its items with a list marker in front of the numeral.
Király and Tokai gloss that marker "introducing the next item in a list", and
it is the same word they also gloss "in turn, nor, or, but". Put in front of
a number it makes an ordinal:

    marker + two            secondly
    marker + two-two        fourthly
    marker + six            sixthly
    marker + six-two        eighthly
    marker + nine           ninthly
    marker + ten            tenthly
    marker + and            eleventhly

That last one works because the code they gloss "and, but, then" is also the
one they gloss "eleven". So the book contains two long numbered lists: the
signs the Lord Jesus showed, and the witnesses who confessed him Son of God.
Both run in order, and the order is what makes the numerals checkable.

**Twelve confirmed.** `six-six` at 022r:10 is the number of apostles called,
so `six-six` is twelve, and the same word four lines earlier says the Holy
Family stayed twelve years in Egypt.

---

## 026r — the earth quakes

**1**  and the earth, to the Lord […] and the moon, because
`and earth to-Lord-year and moon because`

**2**  because when the Lord Christ crucified
`because then-exist Lord-Christ [?]`

**3**  the earth quaked, the rocks and the stones split.
`earth quake-rock stone split`

> Matthew 27:51, "the earth did quake, and the rocks rent".

## 026v — the sun darkened, and Abraham's confession

**1**  The sun and the moon were darkened; and all tree into the world humbled themselves; and all
`sun and moon this eclipse and each,_every [?] [?] this humble and each,_every`

**2**  creation mourn when Christ crucified; and all this five confessed,
`create [?] then-exist Christ [?] and this each,_every [?] confess`

**3**  in sorrow that, that the Lord Jesus is truly the Son of God; and by miracle they confessed
`inside-to-sad(ly) [?] Lord-Jézus righteous(ly) son God and miracle confess`

**4**  that the Lord Jesus is truly the Son of God, because […]
`[?] Lord-Jézus righteous(ly) son God because [?]`

**5**  miracle did; and the Lord suffered; the Jews crucified.
`miracle ~do and suffer Lord Jew crucified`

**6**  and to whom, the year, the Lord, the Lord God announced [to] Abraham | the patriarch
`and to-+who-~year the_Lord Lord_God announce Abraham | patriarch`

**7**  holy year arrived then; said, was said the Lord God [to] Abraham by the angel; and this
`holy-~year arrive then* say exist say Lord_God Abraham on-angel and this`

**8**  the Lord God said to the blessed Virgin Mary by Gabriel the angel; and | Saint
`say say Lord_God happy Virgin_Mary by_Gabriel angel and | holy`

**9**  very old Joseph; and the man who believes in the Lord,
`[?] [?] and somebody to-Lord exist believe`

**10**  that he is truly the Son of the living God — every man is saved; and one
`that righteous son living God everybody = be_saved and one.`

**11**  a man is damned; and the Lord not believes; and [perish]
`somebody be_damned to and Lord [?] believe and [?]`

**12**  one is saved, but who believes not, a man is damned; and | this
`one to be_saved but who_believes_not* somebody be_damned and | this`

**13**  thus he said. First confessed it Abraham the forefather |
`and-this say confess first Abraham forefather | on-this`

**14**  This one confessed …; after these confessed holy Anne
`this confess holy-in_turn-+one-[?] after_these confess holy_Anne`

## 027r — Mary's confession

**1**  the mother, the blessed Virgin Mary. After these confessed the blessed | Virgin
`mother happy Virgin_Mary after_these confess happy | virgin`

**2**  Mary. The angel of God said: at that time the Lord was; the Lord God went; the Lord's
`Mary say angel God time exist Lord go Lord-<divine> <of>-Lord`

**3**  angel [to] the blessed Virgin Mary; then out, from … to the house
`angel happy Virgin_Mary then ~out from want-year to-house`

**4**  of the Virgin Mary; she conceived, and bore; and [on the eighth] … five thousand years
`Virgin_Mary conceive and be_born and [on_the_eighth] five_thousand-~year`

**5**  and one hundred and sixty years, and five, and, and the moon.
`and one hundred and six-ten-year and five and and moon.`

**6**  at that time the Father of heaven opened, because he saw hidden every
`time open the_Father heaven because see hide every`

**7**  world, darkness, the sky. At that time the Father
`world darkness sky time open the_Father`

**8**  in heaven; and the Lord's angel Gabriel went […]
`heaven and go <of>-Lord angel Gabriel inside exist-chapter`

**9**  to the blessed Virgin Mary, and these said. Saint Luke writes
`blessed Virgin_Mary and these say write holy-Luke`

**10**  chapter in his writing; and the man who believes in the Lord,
`[?] <of>-write and somebody to-Lord exist believe`

**11**  that he is truly the Son of the living God — every man is saved; and
`that righteous son living God everybody = be_saved and`

**12**  one man is damned; and the Lord not
`one somebody be_damned to and Lord [?]`

**13**  believes; and one is saved; but every man
`believe and one to be_saved a) each,_every somebody`

## 027v — Joseph's confession, and "there are not many gods"

**1**  is damned. And these said, confessed Saint Joseph the aged |
`be_damned and these say confess holy-aged | Joseph`

**2**  [understand] the angel of God said, because the Lord God spoke by the angel
`[?] say angel God because exist say Lord-<divine> on-angel`

**3**  Gabriel: and the man who is the Lord's believe, that truly
`Gabriel and somebody to-Lord exist believe that righteous`

**4**  the Son of the living God — every man is saved; and one
`son living God each,_every somebody be_saved and one`

**5**  man is damned; and the Lord […] […]; and | […]
`somebody be_damned to and Lord [?] [?] and | [?]`

**6**  … is saved, but every man is damned; and | this and
`chapter to be_saved but every somebody be_damned and | this-and`

**7**  this said, said the Lord Jesus on Maundy Thursday; then the Lord went | on
`this say say Lord-Jesus on_Maundy_Thursday = then Lord go | on`

**8**  to his death; and then the Lord went … the apostles in Jerusalem. At that time knelt
`die and then-Lord ~go-[?] apostle inside Jerusalem time kneel`

**9**  the Lord Jesus before the blessed Virgin Mary; and the Lord Jesus said: there are not
`Lord-Jesus before happy Virgin_Mary and say Lord-Jesus is_not`

**10**  many gods, but rather one God. And the Lord Jesus said:
`many God but_rather* one God and_said Lord-Jesus`

**11**  […] and the Lord […] […] in the Lord Jesus Christ; and
`to and Lord [?] [?] inside Lord-Jézus-Christ and`

**12**  one is saved, but every man is damned;
`one to be_saved a) each,_every somebody be_damned`

**13**  and Mary blessed the Lord Jesus, on every apostle — the blessed Virgin Mary.
`and Mary bless Lord-Jesus on-every apostle happy Virgin_Mary`

## 028r — the Passover lamb, and the twelfth sign

**1**  And then Mary, the Lord, kissed the Lord Jesus, the Lord's mother,
`and then-Mary exist-Lord kiss Lord-Jesus of-Lord mother`

**2**  the blessed Virgin Mary; and then Mary was, and from Mary.
`happy Virgin_Mary and then-Mary exist and from Mary.`

**3**  Mary's son, the Lord Jesus Christ, kissed [her]; and from Mary went away
`kiss of-Mary son Lord-Jesus-Christ and from Mary go_away`

**4**  the Lord Jesus Bethany the apostles in Jerusalem, because <subject marker> the apostles […]
`Lord-Jézus [?] apostle inside Jerusalem because [?] apostle [?]`

**5**  Before the Lord went into Jerusalem, who, the apostles, ate the supper.
`before Lord go inside Jerusalem who apostle dinner eat.`

**6**  the apostles prepared a lamb, because at that time
`prepare-apostle one lamb because time`

**7**  was the feast of the Jews, the Passover. this is There began the suffering
`holiday exist Jew(ish) Easter [?] begin suffering`

**8**  of the Lord Jesus Christ, Son of God; because <subject marker> the Lord is truly the Son of God.
`Lord-Jézus-Christ son God because [?] Lord righteous(ly) son God`

**9**  And then the Lord, the Jews crucified; and then the Lord, the apostles,
`and then-exist Lord Jew(ish) [?] and then-exist Lord apostle`

**10**  the mother; within the tomb put; and on the third day from death the Lord stood up. And from | six
`mother inside tomb put and on_the_third_day from die stand_up-Lord and from | six`

**11**  six, the sign the Lord Jesus showed, when he rose
`six can show Lord-Jesus then rise*`

**12**  from pray the Lord and the apostles appear in Jerusalem; and the thirteenth sign the Lord Jesus showed
`from [?] Lord and apostle [?] inside Jerusalem and [?] can show Lord-Jézus`

## 028v — the Ascension

**1**  then [among] [one another]; one mount; two men and two men
`then [among] [one_another] one mount two somebody and two somebody`

**2**  drove out six hundred and six thousand and sixty and six devils
`exorcise six-hundred and six-?thousand and six-ten and six devil =`

**3**  and the two men healed, did; the fourteenth sign showed
`and two somebody healing ~do fourteen can show`

**4**  the Lord Jesus; then Holy Thursday; then [he] left to the Lord's God the Father | on
`Lord-Jesus then Holy_Thursday then leave to-of-Lord God_the_Father | on`

**5**  heaven's land, to sit, the Lord; the Father God, on the right.
`heaven ~land from-sit-Lord the_Father God on-right`

> The last line is the creed: he ascended into heaven, and sitteth at the
> right hand of God the Father.

## 029r — the Passion begins: "Here begins"

**1**  Here begins the account
`begins this begin [?]`

**2**  Passion of our Creator Lord,
`Passion our Creator_Lord`

**3**  the writing of the Passion, [the Passion],
`write Passion = [the_Passion]`

**4**  [of] Saint Matthew and Saint John,
`holy-Matthew and holy-John`

**5**  of the Passion |
`from suffering | [?]`

**6**  of somebody, the Creator Lord. At that time
`somebody Creator_Lord time.`

**7**  The Lord Jesus went to Bethany
`go Lord-Jézus [?]`

**8**  Jerusalem, because from far … to the Lord, the supper done, because the Lord was [there].
`Jerusalem because from far-to-Lord dinner ~do because exist Lord.`

**9**  Before, the Lord went, the apostles, into Jerusalem, and the Lord Jesus said to the apostles:
`before Lord go apostle inside Jerusalem and_said Lord-Jesus exist apostle.`

**10**  prepare from the Passover lamb, who, the Lord, the apostles, the supper
`prepare from Easter lamb who Lord apostle dinner.`

**11**  eat, and I go to you. And then the Lord went
`eat and I to you go and then Lord go.`

**12**  to the apostles in Jerusalem; and sat at the table, the Lord [with] the disciples. At that time
`to-apostle inside Jerusalem and sit to-throne Lord [with] to_the_disciples time`

**13**  the apostles prepared the Passover lamb; and the lamb
`exist apostle prepare from Easter lamb and lamb`

> The codex names its own sources for the Passion: Saint Matthew and Saint
> John. Line 1 is a rubric, "Here begins", of the kind a scribe writes.

## 029v — the supper, and the washing of feet

**1**  the apostles brought to the table; and the Lord Jesus said: brothers of the Lord, from
`carry apostle on table and_said Lord-Jesus brother of-Lord from`

**2**  the lamb, the Lord wants you to eat this Passover
`lamb* want Lord to you eat this Passover.`

**3**  lamb. Therefore the Lord asks you: do not, apostles,
`lamb that_is_why ask_(for)-Lord you do_not apostle`

**4**  be offended in the Lord, because I go to death — the Lord dies; and I |
`inside Lord take_offence because I go on-die Lord die and I | on`

**5**  on the third day up rise, the Lord; and I appear to you.
`three_days up rise-Lord and I you appear`

**6**  And the Lord Jesus stood up from the table, and took off, the Lord, |
`and stand_up to-throne Lord-Jesus and take_off-Lord | on`

**7**  the Lord's clothes. And the Lord Jesus said: one apostle
`Lord of-Lord clothes and_said Lord-Jesus one apostle`

**8**  among seventy apostles, and among seven apostles, and the body
`among seven-ten apostle and among seven apostle and ~body`

**9**  an apostle was Titus; in turn [he] carried one bucket [of] water
`apostle exist Titus-in_turn carry one bucket water`

**10**  and a washing-dish; and then water into the dish
`and one washdish and then-exist water inside washdish`

**11**  poured; and the Lord Jesus went to Saint Peter; in turn Titus, in turn
`pour and go Lord-Jesus to holy-Peter in_turn Titus-in_turn`

**12**  brought the water in the dish to the Lord Jesus; and Saint Peter said:
`carry inside washdish water to Lord-Jesus and_said holy-Peter`

> John 13:4–6, in order: he rose from supper, laid aside his garments, poured
> water into a basin, and came to Simon Peter. Luke 22:15 is at line 2, and
> Matthew 26:31, "all ye shall be offended", at line 4.

---

## 030r — Peter objects

**1**  Master, do not let this Peter, who he, Peter, have his feet washed.
`Master not_let this-Peter who he Peter foot wash`

**2**  And the Lord Jesus said: Peter, if I this Peter's feet
`and_said Lord-Jesus Peter if I this-Peter foot`

**3**  washed […] […] [part] within heaven, land
`wash understand-+one this-cut_off-[?] [part] inside heaven ~land`

**4**  And Saint Peter said: Master … this Peter, this
`and_said holy-Peter Master sky* this-Peter this`

**5**  … trespass; he a sufferer …
`love-to-+high-[?] trespass he sufferer who-to-+high-[?]`

**6**  Peter … [part], he in heaven's land | …
`Peter cut_off-?be_born [part] he inside heaven ~land | love-cut_off.`

**7**  this Peter, he … [hands and] head.
`this-Peter he grab-cut_off-to [hands_and] head.`

**8**  washed; and all Peter's body washed; and | then
`wash and every of-Peter ~body wash and | then`

**9**  Peter's feet the Lord washed; and the feet
`exist Peter SUBJ foot exist-Lord wash and foot`

**10**  <subject marker> with the garment, the towel; and the rest of the apostles stood in the middle; every one
`SUBJ garment* towel and the_rest from stand apostle middle every`

**11**  he washed; and the feet <subject marker> garment [wiped] and
`wash and foot [?] [?] [?] and`

**12**  the Lord Jesus took the Lord's clothes, and
`grab Lord-Jesus on-Lord of-Lord clothes and`

> John 13:8, Peter's "thou shalt never wash my feet".

## 030v — the bread, and the cup with water and wine

**1**  The Lord Jesus sat at table with the apostles; and the Lord Jesus said: see, <subject marker> apostles,
`sit Lord-Jesus to-throne to-apostle and_said Lord-Jesus see SUBJ apostle`

**2**  the Lord; see how I you pray, from rather
`to-Lord see how? I you pray from rather*`

**3**  and you understand, eat; two; pray; and took
`and you understand-eat two pray and grab`

**4**  the Lord Jesus [took] in his hands one baked cake,
`Lord-Jesus inside hands one baked cake`

**5**  and blessed the Lord Jesus this bread and bread
`and [?] Lord-Jézus this [?] and [?]`

**6**  the Lord set it before them; and the Lord Jesus took
`before Lord put Lord-Jézus and grab Lord-Jézus`

**7**  wine in a cup, and poured water into the cup; and blessed
`wine one cup and water inside cup pour and [?]`

**8**  the Lord Jesus, the wine and the water; and the wine and water
`Lord-Jézus wine and water and wine water`

**9**  the Lord Jesus set before them; and the Lord Jesus said: and somebody
`before Lord put Lord-Jesus and_said Lord-Jesus and somebody.`

**10**  whoever eats of this […], that man shall be | the
`exist this [?] eat this somebody exist | <of>`

**11**  the Lord's body eats; and somebody [who does] not this bread
`Lord ~body ~eat and somebody not this bread`

> Water poured into the wine is not in the gospels. It is the mixed chalice
> of the Mass, so the page is describing the rite as much as the supper.

## 031r — one of you shall betray me

**1**  eats and believes in the Lord […]; every man is damned […]
`eat and Lord believe each,_every somebody be_damned [?]`

**2**  and the man who believes in the Lord and is from
`and somebody exist Lord believe [?] exist from`

**3**  […] they ate the holy Host […] drank […]
`thirty holy-host eat [?] drink [?]`

**4**  that man shall live, for ever and ever, amen. And said
`somebody exist living for_ever_and_ever = amen and_said`

**5**  The Lord Jesus know <subject marker>: one among you
`Lord-Jézus [?] [?] one among you`

**6**  and […] the Lord […] one of the apostles shall betray him. And the apostles looked among
`and [?] Lord [?] from apostle betray and see-apostle among`

**7**  the apostles; Saint Peter said: Master, who is it? and struck …
`apostle say holy-Peter Master who_is_it and struck-to.`

**8**  the Lord Jesus said; and [leaning] [breast] the Lord Jesus
`say Lord-Jézus and [?] [?] Lord-Jézus`

**9**  Peter and John; and [Peter] said: O, Peter's brother,
`Peter and ~John and say oh of-Peter ~brother`

**10**  ask the Master, who is it? And then he leaned
`ask Master who_is_it? and then lean_on`

**11**  Saint John on the side of the Lord Jesus, and said: Master | …
`holy-~John on-end Lord-Jesus and_said Master | name-+one.`

**12**  These [words] said the Lord Jesus: to whom I give the bite
`these say Lord-Jesus to_whom I give^ bite`

> John 13:25, "Lord, who is it?", with John leaning on him, and 13:26, the
> sop. The dictionary has a word for "Who is it?" as a single code.

## 031v — Satan enters into Judas

**1**  bread. So it is. And then holy John slept
`bread so_it_is and then sleep holy-~John`

**2**  on the side of the Lord Jesus; and this the Lord Jesus gave.
`on-end Lord-Jesus and give^ this Lord-Jesus.`

**3**  Nicodemus(?) saw the Lord Jesus [the morsel] this
`Nicodemus? and see* Lord-Jesus [the_morsel] this`

**4**  bread And then bread Judas
`[?] and then-exist [?] exist-Lord Judas`

**5**  Iscariot gave; and then the bread, Judas
`Iscariot give^ and then bread Judas`

**6**  immediately the devil entered into Judas.
`immediately = devil = inside Judas enter`

**7**  And the Lord Jesus said: apostles, weeping, from a man, and this gave
`and_said Lord-Jesus apostle crying from man^ and give^ this`

**8**  from the Son of God. And the Lord Jesus said: Judas, do
`from son God and_said Lord-Jesus Judas do`

**9**  what thou doest. And then the apostles misunderstood how
`who-exist do and then misunderstand apostle how?`

**10**  he said: Master, speak. But the apostles did not understand what Judas said.
`say Master speak a) understand apostle how? say Judas`

**11**  bread [he should] buy, who … the shepherd, to eat, because
`bread buy who-exist shepherd ~eat because`

**12**  to feed the apostles … because this was the Jews' Passover.
`feed apostle ~exist judge because this exist Jew Easter`

> John 13:27, "Satan entered into him", and 13:28, "no man at the table knew
> for what intent he spake this unto him."

## 032r — Wednesday, and the silver

**1**  and […] Judas; and he went [to] the Jews'
`and [?] Judas and go Jew(ish)`

**2**  chief in Jerusalem; because the Lord was […]. On Wednesday one of the apostles
`head inside Jerusalem because Lord exist inside Wednesday from apostle`

**3**  betrayed him — Judas — because he took for the Lord thirty
`betray Judas because exist to-Lord grab [?]`

**4**  silver. And the Lord Jesus said: brothers of the Lord, I
`silver and_said Lord-Jesus brother of-Lord I`

**5**  go to God the Father of the Lord; and I [send] you
`go of-Lord God_the_Father and I you`

**6**  the Holy Spirit shall come; and you shall […]
`go holy-spirit and you exist see-two`

**7**  … that is, I go to death; the Lord dies, because
`judge that_is I go on-die Lord die because`

**8**  the Jews crucify the Lord; and I on the third day
`Lord Jew crucified and I on_the_third_day`

**9**  up stand, the Lord. Therefore the Lord asks you:
`up stand_up-Lord therefore ask Lord you`

**10**  do not, apostles, stumble in the Lord, because the hour comes,
`do_not apostle inside Lord stumble because come hour`

**11**  the hour of the Lord God the Father [willed] <subject marker> the Lord crucified. And [Peter] said:
`of-Lord God_the_Father [willed] hour SUBJ Lord crucified and_said`

> The codex dates the betrayal to a Wednesday, which is the traditional day
> and not stated in any gospel.

## 032v — Peter will deny him

**1**  Peter: Master, this Peter wants … the Lord; he dies.
`Peter Master this-Peter want food Lord he die`

**2**  And the Lord Jesus said: Peter, before the cock crows,
`and_said Lord-Jesus Peter first than crow cock`

**3**  this Peter will deny the Lord three times. And Peter said, Peter
`this-Peter Lord-to three exist deny and Peter say Peter`

**4**  … And the Lord Jesus said: Peter, this <subject marker> this
`emperor and_said Lord-Jesus Peter this SUBJ this`

**5**  […] Therefore the Lord asks you: do not […]
`~out(ward) that_is_why ask_(for) Lord you do_not [?]`

**6**  be offended in the Lord; because the apostles were very sorrowful for the Lord;
`inside Lord stumble because exist apostle many sad(ly) on-Lord have`

**7**  and one of the Jews was a judge; and the mouth
`in_turn one Jew(ish) exist judge and mouth`

**8**  could the Lord; said the Lord Jesus: but rise; and the Lord went
`can Lord say Lord-Jesus but rise and go Lord`

**9**  on the way, because the Lord Jesus had then known, the Lord,
`on-way because have Lord-Jesus then Lord know`

**10**  Judas, in the house of the high priest; and many miracles
`Judas inside house ~high_priest and many miracle`

**11**  and much preaching did the Lord Jesus on the way.
`and many ~preach ~do Lord-Jesus on-way`

---

## 033r — over the brook Cedron, into the garden

**1**  And Saint John tells of many miracles and much preaching
`and speak holy-John many miracle and many ~preach`

**2**  did the Lord Jesus, the way; but within [it is] not written
`~do Lord-Jesus ~way but inside write not`

**3**  down. And then the Lord and the twelve apostles […] […]
`write and then-exist Lord six-six apostle [?] [?]`

**4**  There was a brook Kidron; and of the apostles
`exist one brook [?] and from apostle`

**5**  the rest of the apostles; the third apostle; the Lord gave Peter, and.
`rest apostle third apostle Lord give^ Peter and.`

**6**  John, and James, and […]
`John and [?] and [?]`

**7**  over Kidron; and up into the mount;
`over Kidron and to-up inside to_the_mount`

**8**  and […], because there was a garden on this, to the mount
`and [?]-+one-[?] because-exist garden on-this to_the_mount`

**9**  beyond Jerusalem town; and then <subject marker> the Lord went on Jerusalem; and into
`trespass Jerusalem town and then-+SUBJ go-Lord on-Jerusalem and inside`

**10**  Jerusalem, behold, the Lord […] to the Lord Jesus and his apostles,
`Jerusalem lo Lord [?] to Lord-Jézus and <of>-Lord apostle`

**11**  because [Judas] wanted to give the Lord Jesus in the garden to arrest.
`because want-Lord give^ Lord-Jesus inside-garden arrest`

**12**  as our father Adam [on the tree] [the tree]
`as our father ~Adam [on_the_tree] [tree.]`

> Line 2 is John 21:25, the many other things Jesus did that are not written.
> Lines 4–8 are John 18:1: over the brook Cedron, where there was a garden.
> The codex has the brook by name.

## 033v — a stone's cast, and the prayer

**1**  committed sin; this wanted the Lord Jesus, to somebody [on the tree]
`commit sin this want Lord-Jesus to-somebody [on_the_tree]`

**2**  [tree] suffering, not to; and then from, to the Lord
`[tree] suffering not-to and then from-to Lord`

**3**  the apostles in the garden; in turn the Lord went to pray, speaks
`apostle inside garden in_turn to-Lord go on-~pray speak`

**4**  Saint John: the Lord went away from the apostles, [answered], then
`holy-John go_away-Lord trespass from apostle [answered] then`

**5**  about a stone's throw pray; his Father; and he knelt down,
`stone to-throw [?] father <of>-Lord and kneel_(down)`

**6**  the Lord Jesus, and said: Father of the Lord, God of heaven,
`Lord-Jesus and_said father of-Lord God heaven.`

**7**  from […] take, Father, from the Lord this suffering; nevertheless
`from ~grab-father from Lord this suffering in_turn`

**8**  <subject marker> if it is pleasing. And the Lord Jesus rose; and the Lord went
`SUBJ pleasing and rise Lord-Jesus and go-Lord`

**9**  to the apostles, but the apostles were asleep; and the Lord Jesus said: rise
`to apostle but apostle to-sleep and_said Lord-Jesus rise`

**10**  and […] woke them; and the Lord Jesus went […] Peter
`and [?] awake and go Lord-Jézus Peter`

**11**  the peak of the mountain, to see this people, because all the people were
`peak of_the_mountain to see this ~people because exist every people`

> Luke 22:41, "withdrawn from them about a stone's cast, and kneeled down,
> and prayed". The codex has the stone's cast.

## 034r — the second prayer, and the sweat

**1**  And a second time the Lord went to pray, before, and the Lord Jesus knelt, and said:
`and two go Lord on-°pray-before and kneel Lord-Jesus and_said`

**2**  God the Father of heaven, from […] take, Father, from the Lord this suffering;
`God_the_Father heaven from ~grab-father from Lord this suffering`

**3**  if <subject marker> it is pleasing. And then blood, sweat, through
`if SUBJ pleasing and then blood sweat through`

**4**  the Lord Jesus, because [in an agony] the Lord Jesus, how, first, the Lord's suffering
`Lord-Jesus because [in_an_agony] Lord-Jesus how?-°first Lord suffering`

**5**  […]. And the Lord went to the apostles […]; the apostles were asleep
`not-chapter and go Lord to-apostle [?] apostle to-sleep`

**6**  And the Lord Jesus said: rise, and, apostles, be awake.
`and_said Lord-Jesus rise and ~have-apostle awake`

**7**  At that time Saint Peter went, and said: on the third, the army, be afraid.
`time go holy-Peter and_say on-+three army be_afraid`

**8**  and a third time the Lord went, prayed [to] God the Father of the Lord, and knelt | the Lord
`and three go Lord ~pray God_the_Father of-Lord and kneel | Lord`

**9**  Jesus, and said: God the Father of the Lord, of heaven, from | do not take
`Jesus and_said God_the_Father of-Lord heaven from | not_take`

**10**  Father, take from the Lord this suffering; nevertheless <subject marker> as it pleases thee; nevertheless
`father from Lord this suffering in_turn [?] pleasing in_turn`

**11**  [thy will] pleasing, because this, God the Father, fulfil on the Lord the will | of
`[thy_will] pleasing because this-God_the_Father fulfil on-Lord will | of`

> Luke 22:44, the sweat. Three prayers in the garden, as in Matthew 26, and
> the second and third are worded almost identically here.

## 034v — the angel from heaven

**1**  the Father. And an angel went from heaven high, the Father's, and said:
`father and go angel from_heaven* high the_Father and_said`

**2**  Lord, do not have … this, the Lord, this suffering drink.
`Lord do_not ~have this the_Lord this suffering drink`

**3**  And the angel said: this is it, he offers, the Father:
`and_said angel this_is he offer the_Father.`

**4**  the Lord's lot, of God the Father; the Son Jesus Nazareth
`<of>-Lord fate <of>-father-<divine> son Jézus [?]`

**5**  every world redeem. And the angel departed from before
`every world redeem and leave angel before`

**6**  the Lord Jesus; because every night the angel went not from the Father high
`Lord-Jesus because every night not_go angel high the_Father`

**7**  to the Lord Jesus; because the angel bore for the Lord all his suffering,
`to-Lord-Jézus because Lord carry angel each,_every <of>-Lord suffering`

**8**  written; and [spoken] righteously; fulfil, who, from the prophet.
`write and [spoken] righteous fulfil who from-prophet.`

**9**  written. And the Lord went to the apostles, and the Lord Jesus said:
`write and go-Lord to-apostle and_said Lord-Jesus`

**10**  […] his […]; and the Lord and the apostles had one […]
`[?] <of>-Lord and have-Lord-apostle one [?]`

**11**  not, not, first; and then [he rose] [from prayer]; and then the apostles | to
`not-?not-°first and then [he_rose] [from_prayer] and then apostle | to`

> Luke 22:43, the angel from heaven strengthening him.

## 035r — the sign, and the kiss

**1**  slept. And the Lord Jesus could not sleep; but the Lord laid a stone
`sleep and can sleep Lord-Jézus a) Lord-put one stone`

**2**  at his head; and the Lord Jesus could not sleep; but rise
`to-head and can sleep Lord-Jézus a) [?]`

**3**  And the Lord said: apostles, stand up, apostles, up, have, apostles, [a sign]:
`and_said Lord apostle stand_up apostle to-up ~have-apostle [a_sign]`

**4**  serpent because from know came the Jews [betray]
`[?] because from [?] go Jew(ish) [?]`

**5**  the Son of Man recognized, to capture [him]. And then
`Son_of_Man = recognize* capture and then`

**6**  the Lord and the apostles went on the way, and saw | the Lord
`Lord apostle and apostle go-Lord-and-apostle on-way and see | Lord`

**7**  Jesus a great people going; and among the Jews was Judas,
`Jesus great^ people go and among Jew exist Judas`

**8**  he whose father died, and mother, [while] they slept. [Came] Judas and the Jews.
`he_who the_father die and mother [while] sleep [came] Judas and Jew`

**9**  He asked a sign to tell the Lord from James, John, Peter: a kiss.
`ask_a_sign distinguish Lord James John Peter kiss`

**10**  so that Judas […] the Jews might take the Lord. And then
`Judas from Lord capture Jew(ish) and then-exist`

**11**  Judas went up to the Lord Jesus; and […]
`go Judas against Lord-Jézus and [?]`

**12**  Judas, the Lord's hand; because to the Jews [he] asked a sign,
`~Judas of-Lord hand because to-Jew ask_a_sign`

> Matthew 26:48, "he gave them a sign". The codex adds the reason the sign
> was needed, on the next page.

## 035v — "Whom seek ye?" and they fell backward

**1**  because John was like the Lord Jesus. And he cried out, | the Lord
`because exist similar John to-Lord-Jézus ~and shout | Lord`

**2**  Jesus: Whom seek ye? The people, the Lord's — the Jews. And they cried,
`Jézus who(m)? search people <of>-Lord Jew(ish) and shout`

**3**  the Jews shouted, the Jews answered: Jesus of Nazareth. And cried
`Jew Jews answered Jesus Nazareth and shout`

**4**  the Lord Jesus: from I, if [it is] the Lord ye seek, Jews. And every
`Lord-Jesus from I if Lord search Jew and every`

**5**  Jew fell backward. And the Lord Jesus said: rise, Jews, up.
`Jew fall_back = and_said Lord-Jesus rise-Jew up`

**6**  [Swords] the Jews hid, of the club; and the Jews rose up; and the Jews'
`[swords] Jews hide of-club and rise-Jews up and of-Jew`

**7**  club the Jews took in their hands, because the Lord Jesus prayed
`club grab-Jews inside hands because Lord-Jesus pray`

**8**  did; God his Father, to the Jewish people; and
`do, father-<divine> <of>-Lord to-Jew(ish) people and`

**9**  The Jews rose up; and a second time the Lord Jesus cried: whom seek ye,
`rise-Jew to-up and two shout Lord-Jesus whom search`

**10**  the people, the Lord's — the Jews. And they cried […]
`people <of>-Lord Jew(ish) and shout [?]`

**11**  The Jews answered: Jesus of Nazareth. And cried
`Jews answered Jesus Nazareth and shout`

**12**  the Lord Jesus: from I, if [it is] the Lord ye seek, Jews; and
`Lord-Jesus from I if Lord search Jew and`

> John 18:4–8, and it is unmistakable. He asks "Whom seek ye?", they answer,
> he says "I am he", and they go backward and fall to the ground — and then
> the whole exchange repeats, exactly as it does in John. The codex also
> explains why Judas needed to identify him: John looked like him.

---

# Two parables, found mechanically

These two folios were not reached by translating in page order. `ktverse.py`
scored every line of the codex against the reference corpus and ranked them,
and these came out near the top on their own. They are the clearest known
plaintext in the book, and both are confirmed by something outside my reading
of them.

## 135r — the Unmerciful Servant

**1**  A king, and the Lord God begins, prays [fellowservant] [a hundred pence]
`king and Lord_God begin ~pray [fellowservant] [a_hundred_pence]`

**2**  have the commandment to somebody's sin; would like, somebody, this Lord God, to have compassion.
`have commandment to somebody-~sin would_like^ somebody this Lord_God have_compassion`

**3**  forgive the debt. And behold, the Lord God the king besought
`remit indebted ~and see this Lord-<divine>-king [?]`

**4**  The servant of the Lord God the king humbled himself — the man-servant — and
`~humble this servant <of>-Lord-<divine>-king somebody-servant and`

**5**  the man forgave, this Lord God the king; and the man forgave all, one
`somebody forgive^ this Lord_God-king and somebody forgive^ every ~exist-+one`

**6**  our sin; and somebody went, the angel, our
`our sin and somebody go-angel our`

**7**  home. And then, as the man went on, the fellow-servant
`home and then-exist keep_going-somebody this heavenly servant`

**8**  our home; and then came one | God
`our home and then come one | God`

**9**  the man, this man, the fellow-servant; and the man was
`somebody this somebody heavenly servant and somebody exist`

**10**  in debt hundred pence; and the man of God began to demand it.
`indebted [?] denarius and God-somebody begin ask_(for)`

> Matthew 18:23–35. The king who forgives a great debt, the servant who
> worships him, and the fellow-servant who owed a hundred pence.
>
> **This one does not rest on my reading at all.** Király and Tokai's own
> dictionary contains a code they gloss "adjective of the unmerciful servant",
> and it is the word standing at lines 7 and 9 where the fellow-servant
> stands. They had identified this parable already. Their dictionary also
> contains *denarius*, which is the coin of this parable and of almost
> nothing else.

## 119r — the Lost Sheep

**1**  the Pharisees began, the Pharisees and the church fathers, to murmur on the Lord Jesus, [that] he spoke
`begin-Pharisee Pharisees* and church_father murmur on-Lord-Jesus he speak`

**2**  [as] the Son of God; in turn then he is the Son of God | this
`son God in_turn then he exist son God | this`

**3**  the Lord [leaveth], goes, this [in the desert]. And then the Lord Jesus | then
`Lord [leaveth] go this [in_the_desert] and_said Lord-Jesus | then`

**4**  there is one [who] has, call you | one
`exist one have call^ you | one`

**5**  hundred sheep in the wilderness, and if he lose one
`hundred sheep inside field and then-exist lose one`

**6**  call, end, [layeth it] [shoulders]; the man is, answered, hide, year, who, chapter, say
`call^ end* [layeth_it] [shoulders] man^ exist answered-hide-~year ~who-chapter-say`

**7**  and does he not leave the ninety sheep and nine
`and exist from-food-somebody from nine-ten sheep and nine`

**8**  in the wilderness; and somebody goes, ninety-nine sheep,
`inside wilderness^ and go-somebody ninety* nine sheep`

**9**  find; and then somebody finds the sheep,
`find and then sheep find-somebody`

**10**  and somebody takes the sheep, the man | on
`and sheep grab-somebody man* | on`

> Luke 15:2–5 and Matthew 18:12–13. The scribes murmuring, "what man of
> you, having an hundred sheep, if he lose one of them, doth not leave the
> ninety and nine in the wilderness", and laying it on his shoulders.
>
> **Two things confirm this without my reading.** The codex writes *ninety
> and nine* the way Luke does, as ninety followed by nine, and it writes
> ninety as nine-ten, which is the same rule the other numerals follow. And
> the unread code marked `[?lost]` above occurs four times in the whole book:
> three of them are here, in the three places the lost sheep belongs, and the
> fourth is at 103v:2 beside the word *soul*. "Lost" works in all four. That
> is Király and Tokai's own method — carry a guess to every occurrence and
> keep it only if it survives — and this guess survives.

---

*From here on, words marked `+word` in the gloss are this project's own
readings from `harness/proposals.json`, not Király and Tokai's.*

## 036r — the third cry, and Jesus of Nazareth

**1**  every Jew fell backward. And the Lord Jesus said: rise, Jews, up.
`every Jew fall_back = and_said Lord-Jesus rise-Jew up`

**2**  He said: hide, of the club; and the Jews rose up; and the
`he_said* hide of-club and rise-Jews up and of`

**3**  Jews' club the Jews took in their hands, because | the Lord
`Jew club grab-Jews inside hands because | Lord`

**4**  Jesus prayed, did, [to] God his Father, to the Jews
`Jesus pray ~do God_the_Father of-Lord to Jew`

**5**  people; and the Jews rose up; and a third time he cried | the Lord
`people ~and rise-Jew to-up and three shout | Lord`

**6**  Jesus: Whom seek ye? The Lord's whom the Jews;
`Jézus [?] search <of>-Lord Jew(ish)`

**7**  and the Jews shouted, the Jews answered:
`and shout Jew Jews answered`

**8**  Jesus of Nazareth. And the Lord Jesus cried: from I,
`Jesus Nazareth and shout Lord-Jesus from I`

**9**  if [it is] the Lord ye seek, Jews. And said, cried, the Lord Jesus:
`if Lord search Jew and_said shout Lord-Jesus`

**10**  Take the Lord, Jews, because [I] go, the hour, to God my Father.
`grab Jew Lord because go ~hour of-Lord God_the_Father`

**11**  And then the Jews arrested the Lord Jesus [backward].
`and then ~Jew arrest Jew Lord-Jesus [backward]`

> The exchange runs three times here, and John 18 gives it twice with the
> third cry implied. "Jesus of Nazareth" is the answer, and it is the sign
> this project read as Nazareth on its six occurrences.

## 036v — Malchus, and the ear put back

**1**  Peter cut off with the sword the ear of one of the Jews,
`cut_off Peter sword ear one Jew`

**2**  and the Jew's name was Malchus. And said
`and name Jew exist Malchus and_said`

**3**  the Lord Jesus: Peter, Peter, blind, cut off [with the] sword; because and
`Lord-Jesus Peter Peter ~blind cut_off sword because and`

**4**  the man Peter sword cut off from sword
`somebody Peter [?] cut_off from [?]`

**5**  struck, somebody <subject marker> die. And the Lord Jesus gave [back] this ear
`struck* somebody-+SUBJ die and give^ Lord-Jesus this ear`

**6**  and put it back in its place, and the ear was made
`and [?] put on-place and healing ear`

**7**  whole. And from the Lord Jesus a miracle done on the pagan.
`leave and from Lord-Jesus on-pagan miracle ~do`

**8**  And the Jews believed in the Lord; but the Lord's clothes |
`and and Jews inside Lord believe but of-Lord clothes | on`

**9**  the Lord take off; and one of the Jews fled,
`Lord [?] and escape one Jew(ish)`

**10**  to the Lord, believe the Lord Jesus; and from [fear] to the Lord [fled] the Lord Jesus
`to-Lord believe Lord-Jesus and from [fear] to-Lord [fled] Lord-Jesus`

**11**  all the Jews [forsook] [him]; to the Jews went; and then … from little
`every Jews [forsook] to Jew go and then-[?] from little`

**12**  [if] And then the Lord could have fled — the Lord did not flee,
`[?] and then-exist Lord want escape exist Lord not escape`

**13**  but good [will] to somebody, apostle, Jew, pagans, above on high.
`but good [will] to-somebody apostle Jew pagans above-high`

> John 18:10 names the servant Malchus, and Luke 22:51 has Jesus touch the
> ear and heal it. The codex has both, and adds that the bystanders believed
> because of it.

## 037r — bound, and struck

**1**  On the cross … and then … carried the Lord's clothes.
`on_the_cross-[?] and then-[?] carry to-Lord clothes.`

**2**  the Lord Jesus; and then tie up the hands of the Lord Jesus Christ
`Lord-Jézus and then-exist [?] hand Lord-Jézus-Christ`

**3**  [bound] all to the Lord, to the year [led] that; and then the Lord.
`[bound] every to-of-Lord to-year-to [led] that* and then Lord.`

**4**  they went to the chief of the Jews [before]; and then the Lord
`go to-Jew(ish) head [?] and then-exist Lord`

**5**  went down from the mountain; and many [people] did
`go down on-to-mount and many [people] ~do`

**6**  the Jews on the Lord Jesus, because the Lord one [struck] in the face
`Jew on-Lord-Jesus because Lord one face beat`

**7**  [from] the town; the second, to the Lord's house; [and] the third
`[from] town* second to-Lord to-house [and] third`

**8**  to the Lord [answered] from the suffering. Our mercy, the Lord Jesus!
`to-Lord [answered] from suffering our have_mercy Lord-Jesus`

**9**  And then through … the Jews, through, over Kidron;
`and then through [?]-Jews through over Kidron`

**10**  and the Jews took the Lord on the bridge; went the Lord Jesus.
`and Lord grab-Jews on-bridge go Lord-Jesus.`

**11**  but the Lord on the bridge fell; and to the Lord [struck] who.
`but Lord on-bridge fall and to-Lord [struck] who.`

**12**  Our mercy, the Lord Jesus! because the Lord two [times] went [among] the Jews.
`our have_mercy Lord-Jesus because Lord two [times] go Jew`

## 038r — bound before Caiaphas

**1**  [bound] they bound the Lord Jesus Christ; and then the Lord
`[?] who-chain-to Lord-Jézus-Christ and then-exist Lord`

**2**  … and dragged out, out, [away]. Our mercy,
`exist and out-out draw [away] our have_mercy`

**3**  the Lord Jesus Christ! And the Jews said: where does the Lord want [to go]?
`Lord-Jesus-Christ and_said Jew where? Lord want`

**4**  the Jews went, the Jews said: one brought the Lord | to
`Jew go say-Jews one brought* Lord | to`

**5**  Pilate. The second said: bring the Lord to Caiaphas. And | then
`Pilate second say brought-Lord to-Caiaphas and | then`

**6**  the Lord was brought to Caiaphas the high priest. And said
`exist Lord brought-Lord to-Caiaphas high_priest and_said`

**7**  the Jews […] accused the Lord; and then
`Jew(ish) [?] Lord [?] accuse and then-exist`

**8**  the Lord […] before the high priest's house; and | when
`Lord [?] before <priest> high_priest house and | then`

**9**  the Lord was [there]; the Jews … brought the Lord [to] this high priest.
`exist Lord exist-Jews inside-?brought Lord this high_priest.`

**10**  and then the Lord […] into a house; and | when
`and then-exist Lord [?] inside one house and | then`

**11**  the Lord, from every one, one [answered], the hour | of the suffering.
`exist Lord from-to-every one [answered] ~hour | suffering`

**12**  The Jews, the Lord Jesus Christ. And Peter said, one
`Jews Lord-Jesus-Christ and_said Peter one`

## 038v — the first denial, and Caiaphas's counsel

**1**  of the Jews, this Malchus whose ear was cut off […]
`Jew(ish) this Malchus ear cut_off [?]`

**2**  Peter [then], this Peter knew not, Peter; and this was from
`Peter [then] this-Peter not_know-Peter and this from`

**3**  the first denial of the Lord Jesus, because Peter said: I know not the Lord.
`first denial Lord-Jesus because say Peter not* Lord not_know`

**4**  And […] the Lord Jesus [was brought] to Caiaphas the high priest; and | when
`and [?] Lord-Jézus to-Caiaphas high_priest and | then-exist`

**5**  the Jews went to the Lord before Caiaphas, and shouted
`Jews to-Lord go before Caiaphas and shout`

**6**  the Jews, this Caiaphas, the Jews: [it is expedient] [he] go; this believe,
`Jew this-Caiaphas-Jews [expedient] go this believe`

**7**  this heretic Lord; and the Lord is from Galilee;
`this heretic Lord and to-Lord SUBJ from Galilee`

**8**  he fed with bread all the people, the Lord, [manna] | in turn
`feed bread all^ people on-Lord [manna] | in_turn`

**9**  the second, the Jews said, said: the Son of God; the third, the Jews said: the king.
`two say-Jews say son God third say-Jews king`

**10**  Caiaphas said: it is written, it is good that one man
`say say Caiaphas write +<subject_marker> good one Lord-somebody`

**11**  should die, rather than all the world perish. And then … the Jews, [the nation].
`die than rather all^ world perish and then-?cup-Jews [nation]`

**12**  the high priest […] in the house, among the apostles Christ [counsel]
`apostle-high [?] inside house among apostle Christ look_up leave [?]`

> Line 10 is John 11:50 and 18:14 — Caiaphas's counsel that it was expedient
> that one man should die for the people. The denials are numbered as the
> signs of Christ were: first, second, third.

## 039r — the second denial

**1**  Saint Peter before the gate; and then Peter was
`holy-Peter before ~gate and then-exist Peter exist`

**2**  seen by the handmaid at the Jews' gate. And the handmaid said: this Peter
`show^ from-handmaid ~gate Jew and_said handmaid this-Peter`

**3**  [is] a disciple of this Jesus. Peter said: this Peter knows [him] not.
`disciple^ this Jesus say Peter this-Peter not_know and.`

**4**  This [was] the other denial of the Lord Jesus, because Peter said not the Lord | and.
`this the_rest^ denial Lord-Jesus because say Peter not* Lord | and.`

**5**  and denied him. And John […] […]
`to-Lord-to in_turn John [?] [?]`

**6**  was known to the high priest. Caiaphas said to Jesus: he says
`acquaintance this high_priest say Caiaphas to-Jesus he say`

**7**  the Son of God? And how dost thou truly preach? Jesus said
`son God in_turn how? this righteous(ly) preach say Jézus`

**8**  to Caiaphas, judge Caiaphas, from the Jews, to the Lord.
`to-Caiaphas from-judge-Caiaphas from Jews Lord-to.`

**9**  hear my preaching [denied] truly […]
`hear preach [?] ~righteous(ly) [?]`

**10**  And then Caiaphas, this Caiaphas, and [gathered] in the Lord new
`and_said Caiaphas this-Caiaphas and [gathered] inside Lord new`

**11**  Caiaphas that year, but rather he righteously the man, said Caiaphas.
`Caiaphas-year but_rather* he righteously man^ say Caiaphas`

**12**  […] field the Lord was brought to Pilate, to Caiaphas's brother.
`[?]-field Lord brought* to-~Pilate to-of-Caiaphas brother`

> John 18:15–17: the maid at the door, the other disciple known to the high
> priest, and Peter's denial. The codex names the disciple John.

## 039v — before Pilate

**1**  And this out, two hours; and the Lord brought | to
`and this ~out two hour and Lord brought* | to`

**2**  Pilate; and from the Lord, on three [counts], they accused; and then the Jews
`Pilate and from Lord on-+three accuse and_said-Jews`

**3**  said to Pilate: he goes, he, the heretic; and | then
`he_said* Pilate go he heretic and | then`

**4**  many Jews were, [bringing] suffering on the Lord.
`exist Jews many suffering on-Lord do`

**5**  The Lord went before Pilate, because all the Lord's [accusation] | on
`go Lord before Pilate because every of-Lord [accusation] | on`

**6**  the Lord from [spat]; and the Lord's holy face all [buffeted]; and | when
`Lord from [spat] and of-Lord holy-face every [buffeted] and | then`

**7**  the Lord was; the Jews were; [nothing] up [again]; our
`exist Lord exist Jews [nothing] to-up [again] our`

**8**  mercy, the Lord Jesus! And then the Lord was [with] the Jews; went
`have_mercy Lord-Jesus and then Lord exist Jews go`

**9**  to Pilate. And then the Jews [said to] this Pilate: the Lord
`to-Pilate and_said Jew this Pilate Jews Lord`

**10**  goes, he, the heretic; and the Lord <subject marker> from | the apostles
`go he heretic and Lord SUBJ from | apostle-exist`

**11**  was food, bread, [for] all the people, on the Lord [manna]
`exist food bread every people on-Lord [manna]`

**12**  The second, the Jews said: the Son of God. The third, the Jews said:
`second say Jews say son God third say Jews`

## 040r — the third denial, and the cock

**1**  he saith he is king. And then Peter went to a
`king say and then-exist Peter go to-one`

**2**  bread [manna]; because is virgin, cut off [sacrament] [worship]
`bread [manna] because exist virgin-cut_off [sacrament] [worship]`

**3**  Peter wanted; [answered], said one Jew to [him]:
`want Peter [answered] say one Jew to`

**4**  Peter, this apostle, he half believes this Jesus.
`Peter this apostle he-~half-~believe this Jesus`

**5**  Peter said know and denied him,
`say Peter grab God this-Peter [?]`

**6**  and this was the third denial of the Lord Jesus; and at that moment the cock crew.
`and this +three denial Lord-Jézus and time crow cock`

**7**  And Peter said: this <subject marker> out, who, Peter: Master,
`and say Peter this SUBJ out who Peter Master`

**8**  he spoke; and sorrowfully Peter went out. And then Pilate
`speak and sad Peter leave and_said Pilate`

**9**  to Jesus: this Lord, sayest thou the Son of God? In turn, how? this righteously.
`to-Jesus this Lord say son God in_turn how? this righteously`

**10**  preach? The Lord Jesus said to Pilate; Pilate
`preach say Lord-Jézus to-Pilate from-judge-Pilate`

**11**  from the Jews, and the Jews; the Lord: hear my preaching [denied]
`from Jews and-Jews Lord-to hear preach [denied]`

**12**  righteously preach. And Pilate [judged]; the Lord Jesus spoke
`[?] preach and Pilate [?] from speak Lord-Jézus`

## 040v — two lines

**1**  but the Lord said to this Pilate, <subject marker> with his mouth, and the Lord: I
`but say Lord this-~Pilate SUBJ mouth and-Lord I`

**2**  truly the Son of the living God.
`righteous(ly) son living God`

## 041r — art thou the king of the Jews

**1**  And then Pilate [said] to this Lord: speakest thou, Lord, king of the Jews?
`and_said Pilate this Lord speak Lord king Jew`

**2**  The Lord Jesus said to Pilate [asked] Pilate's mouth
`say Lord-Jézus this Pilate +<subject_marker> [?] Pilate mouth`

**3**  and I [am] truly the Son of the living God. And then
`and I righteous son living God and_said.`

**4**  Pilate: he <subject marker> truly somebody, this [man]; this Pilate
`Pilate he SUBJ righteous somebody this Pilate`

**5**  how [answered] in the Lord [nothing]; and there cried
`how? [?] inside Lord [?] and shout`

**6**  the Jews: crucify the Lord! Pilate: on the cross the Lord [is] cursed, this
`Jew crucify Lord Pilate on_the_cross Lord cursed this`

**7**  Pilate. If the Jews want the Lord, the Jews [release him].
`Pilate if want Jews Lord Jews [release]`

**8**  The emperor truly crucifies. And then Pilate
`emperor righteous crucify and_said Pilate.`

**9**  [therefore] the Jews took the Lord; and the Lord was brought
`[therefore] grab Lord Jews and Lord brought*`

**10**  Herod, Pilate's brother; and then out, three.
`~Herod of-Pilate ~brother and then ~out three.`

**11**  the hour; and then the Lord was brought [to] Herod
`hour and then Lord brought* Herod`

**12**  the king; and then, and [the Jews] […] on one
`king and then and [?]-Jews on-one`

## 041v — sent to Herod, because he is of Galilee

**1**  love [answered]; and then from [them] shouted every [one], four directions, year, to
`love [answered] and then from shout every two-two direction-~year-to`

**2**  the Lord [accused]; this he brought: he, the heretic
`Lord [accused] this brought* he heretic`

**3**  this Jesus blasphemeth; and the Lord is out of Galilee,
`this blasphemer-Lord this Jézus and +<subject_marker> Lord from Galilee`

**4**  he fed with bread all the people, on the Lord [manna].
`feed bread every people on-Lord [manna]`

**5**  And then the Lord was brought; many asked before.
`and then Lord to-?brought many ask^ before.`

**6**  Herod the king, because […] the Jews would […] the Lord
`Herod king because [?] Jew(ish) to-Lord want`

**7**  Herod, crucify! and the Lord, the emperor.
`Herod crucify and Lord emperor.`

**8**  Herod, crucify! but [long] shining, see.
`Herod crucify but [long] shine see.`

**9**  Herod, the Lord Jesus Christ; and then the Lord brought before
`Herod Lord-Jézus-Christ and then-exist Lord [?] before`

**10**  Herod the king; and the Jews cried […]
`Herod king and shout Jew(ish) [?]`

**11**  Herod, the Jews: the Lord goes, he, the heretic; and the Lord <subject marker>
`Herod Jews Lord go he heretic and Lord SUBJ`

**12**  is from Galilee; he fed with bread every
`from Galilee feed bread every`

> Luke 23:6–7 — Pilate hears Galilee and sends him to Herod.

## 042r — four lines

**1**  the people against the Lord [manna]; and the Lord said, the Son
`people on-Lord [?] and Lord say son`

**2**  God. And then the false [witnesses] confessed, said the Lord, and
`God and_said ~false °and_then-confess say Lord and`

**3**  the man, this temple destroy | he wants,
`man* this temple destroy | want`

**4**  the Lord: I in three days all [shall] do.
`Lord I in three_days every ~do`

> Matthew 26:61, the false witnesses: *This man said, I am able to destroy the
> temple of God, and after three days to rebuild it.* Király & Tokai read
> *false testimony* at line 2, *temple* and *will* at line 3, and *in three
> days* at line 4. Corrected 2026-09-26: the earlier printing left the temple
> unread, and Book One turned the charge into a promise that he would rise.

## 042v — Herod questions him

**1**  and [of David] confessed it talent Herod; but […]
`and [?] to-this confess [?] Herod a) [?]`

**2**  Herod said: Lord — Herod [mock] God, that the Lord is the Son; and
`Herod say Lord Herod [?] God this Lord son and`

**3**  one said, spoke of the Lord Jesus against Herod; and
`one say speak Lord-Jézus ~against Herod and`

**4**  Herod [mocked] Herod [derided] Herod the king […]
`Herod [?] Herod [?] this-Herod king [?]`

**5**  he could, Herod, [white], this dying, crucify [garment]
`he can Herod [white] this die crucify [garment]`

**6**  he [sent back]; Herod said to [him]; Herod said [again]
`he [sent_back] Herod to say say Herod [again]`

**7**  to Herod: the Lord of the living God […]; Herod said [mock]
`to-Herod this Lord-to living God [?] say Herod [?]`

**8**  God, he [is] the Son; and not the Lord's name
`God he son and not* Lord name`

**9**  his Father [believed]. And then the Lord Jesus [said] to Herod | this:
`of-Lord father [believed] and_said Lord-Jesus to-Herod | this`

**10**  the Lord is truly the Son of the living God. The Lord Jesus said: I go
`Lord righteous son living God say Lord-Jesus I go`

**11**  to my Father; on doomsday [I] judge the living and the dead.
`of-Lord father on_doomsday judge living and die`

**12**  and Herod did so: he brought a stone and […]
`and do, Herod carry stone and [?]`

> Line 11 is the creed again: he shall come to judge the quick and the dead.

## 043r — Herod hoped to see a miracle

**1**  a vessel of water, and brought various
`one vessel water and [?] various`

**2**  [stood] before the Lord Jesus; and the Lord was asked
`[?] before Lord-Jézus and Lord ~ask_(for)`

**3**  Herod: then the Lord before [him], a miracle do.
`Herod then-Lord before miracle do`

**4**  and they set a yoke before the Lord Jesus, and […]
`and yoke Lord-Jézus before and understand-eat`

**5**  to do a miracle, because when [hoped] before
`miracle do, because then-exist [?] before`

**6**  Herod he did no miracle, though the Lord took […]
`miracle do, why?-Lord grab [?]`

**7**  crucify! but Herod said: bring this Lord [questioned]
`crucify but say Herod brought* this Lord [questioned]`

**8**  Pilate [became] Herod's friend; understand, understand, who, who
`Pilate to-of-Herod friend^ understand-understand-+who who`

**9**  [he answered nothing], because on the Lord Pilate did.
`[answered_nothing] he because on-Lord do Pilate`

**10**  And the Lord brought before Pilate, many judge
`and Lord [?] before Pilate many [?]`

**11**  And this was out, the sixth hour; and the Lord [was] brought before
`and this ~out six hour and Lord brought* before`

**12**  Pilate. And then the Jews [said to] Pilate; he said, Pilate <subject marker>
`Pilate and_said Jew Pilate say he Pilate SUBJ`

> Luke 23:8, Herod hoped to see a miracle, and 23:12, Pilate and Herod were
> made friends that same day — here "Pilate became Herod's brother". John
> 19:14 puts the judgment at the sixth hour, and line 11 has it.

## 043v — the scourging

**1**  Herod, crucify, if the Lord … this Pilate, if the Jews want.
`Herod crucify if-Lord this Pilate if want Jew`

**2**  the Lord. The Jews [wrote]: the emperor truly crucifies.
`Lord Jews [wrote] ~emperor righteous crucify`

**3**  And then Pilate understood; the soldiers carried [him]; the soldiers, Pilate.
`and_said Pilate understand-eat soldier carry-soldier Pilate`

**4**  the two [thieves] [with him]; and then Pilate: Jews, carry.
`two [thieves] [with_him] and then Pilate Jews carry`

**5**  the two [thieves] [with him]; and the Lord, the gate, within.
`two [thieves] [with_him] and Lord gate inside.`

**6**  understood, the house; and Pilate took | two
`understand-eat house and grab Pilate | two`

**7**  two soldiers to the Lord Jesus, and the Lord was scourged; and then
`two soldier to Lord-Jézus and Lord exist whip and then-exist`

**8**  two from the [pillar] flogged the Lord Jesus; second, the Lord
`two from [pillar] flog Lord-Jesus second Lord`

**9**  began; two Jews flogged; and then two, and from two Jews.
`begin two Jews flog and then two and from two Jews`

**10**  […] flogged the Lord Jesus Christ; and | there came
`from [?] flog Lord-Jézus-Christ and | leave`

**11**  one soldier to the Lord Jesus; and then
`to-leave one soldier to Lord-Jézus and then-exist`

**12**  […] the Lord Jesus, because the Lord had many tie up
`from [?] Lord-Jézus because exist Lord many [?]`

## 044v — the purple robe and the crown of thorns

**1**  And then the Lord collapsed, the Lord Jesus; and
`and then Lord collapse = Lord-Jesus and`

**2**  the Lord [scourged]; they raised him up; and the Lord [mocked]
`Lord [scourged] up raise-Jews and Lord [mocked]`

**3**  clothes; understood, a purple robe; and the Lord
`clothes understand-eat purple_robe and Lord`

**4**  the crown of thorns on his head, the Jews [put].
`thorn crown on-head conceive-Jews`

**5**  and they set the Lord upon a seat; and
`and Lord sit on-understand-eat chair and`

**6**  […] knelt before the Lord Jesus, and
`[?] kneel_(down) before Lord-Jézus and`

**7**  spoke: Healing, Jesus of Nazareth! And they left [hail].
`speak healing Jesus Nazareth and leave [hail]`

**8**  understood, the soldiers, that [gave] [blows] [to] the Lord Jesus; and
`understand-eat soldier that* [gave] [blows] Lord-Jesus and`

**9**  [sat] seat [judgment] the Lord Jesus; and then
`[?] from [?] [?] Lord-Jézus and then-exist`

**10**  the Lord collapsed; and the Jews took the Lord,
`Lord collapse = and Lord grab Jew`

**11**  and the Jews led the Lord to Pilate, into the house.
`and Lord go Jew(ish) to Pilate inside house`

> John 19:2–3: the purple robe, the crown of thorns, and Hail, King of the
> Jews, with the kneeling. The codex keeps the mockery of the kneeling.

## 045v — twelve legions of angels

**1**  And the Lord [was] seated [by] the Jews, within one throne | on
`and Lord seat Jews inside one throne | on`

**2**  the middle of the house; and then Pilate knelt.
`middle house and then kneel Pilate`

**3**  before the Lord Jesus, and Pilate said: Hail, Lord, King
`before Lord-Jézus and say Pilate healing Lord king`

**4**  of the Jews! And the Lord Jesus said to Pilate […]
`Jew(ish) and say Lord-Jézus to-Pilate [?]`

**5**  speakest thou that I am king of the Jews? Because | then
`speak because I king Jew because | then`

**6**  will his Father God, ye
`exist [?] <of>-Lord father-<divine> you`

**7**  the Lord captured, because then I want, the Lord,
`Lord capture because then I want Lord`

**8**  I ask from my Father God | six
`I ask from of-Lord the_father God | six`

**9**  six armies in turn of angels remain [with] me,
`six an_army in_turn angel remain* I`

**10**  that you seize [and] capture, because then
`you grab capture because then`

**11**  I want; I [could] you all.
`I want I you every can`

> Matthew 26:53 — "more than twelve legions of angels". The twelve is
> written six and six across the margin break, the same way the twelve
> apostles are written at 022r:10.

## 046r — Barabbas, and Behold the man

**1**  the Lord die […]; and ye took
`Lord die [?] and you grab`

**2**  the Lord captured. And Pilate said to Jesus: this
`Lord capture and say Pilate to-Jesus this`

**3**  sayest thou, Lord, the Son of God? And one said
`Lord say son God and one say`

**4**  [Behold], said the Lord Jesus to Pilate; and he let go
`[Behold] say Lord-Jesus to-Pilate and leave`

**5**  Barabbas; to Jesus, and they beat the Lord's face.
`Barabbas to-Jesus and Lord beat face`

**6**  [from] town [outside], all the Lord's holy, nine […] name
`[from] town* [outside] every of-Lord holy-nine-+name`

**7**  quaked; and Jesus said […] the soldier, Barabbas, truly
`quake and say Jézus this soldier Barabbas this righteous(ly)`

**8**  the Lord spoke […] they beat him; the church father spoke,
`speak-Lord to-inside-Lord beat speak church_father`

**9**  it is written that; and [scourged] [again] they beat him.
`write [?] exist and [?] [?] beat`

**10**  For ever and ever. And so they did to the Lord.
`for_ever_and_ever = and Lord do`

**11**  Pilate went out of the house, and cried,
`Pilate out(ward) go on-house and shout-to`

**12**  Pilate: Behold Jesus, Nazareth the King of the Jews!
`Pilate lo Jézus [?] king Jew(ish)`

> John 19:14, "Behold your King!", and Barabbas from all four gospels.

## 046v — crucify him, the second time

**1**  [Caesar]; in turn, the angel, Bethlehem town.
`[Caesar] in_turn angel Bethlehem town.`

**2**  And the Jews cried: the cross for the Lord! Pilate: the Lord is accursed,
`and shout Jew(ish) +cross Lord Pilate cursed Lord`

**3**  this Pilate: if the Jews want the Lord, enemy of the emperor.
`this-~Pilate if want Lord Jews enemy of-~emperor`

**4**  truly crucify! And Pilate said to the soldiers: go, Lord.
`righteous crucify and say Pilate to soldier go Lord`

**5**  into the house. And a second time the Lord did [so], went into the house,
`inside house and two Lord ~do go on-house`

**6**  and Pilate cried: Behold Jesus Nazareth
`and shout Pilate lo Jézus [?]`

**7**  the King of the Jews! [Caesar] and the angel |
`king Jew [Caesar] in_turn angel | to`

**8**  Bethlehem town; and they shouted.
`Bethlehem town and shout.`

**9**  the Jews: the cross for the Lord! Pilate: the Lord is accursed, this
`Jew(ish) +cross Lord Pilate cursed Lord this`

**10**  Pilate: if the Jews want the Lord, enemy of the emperor.
`Pilate if want Lord Jews enemy of-~emperor`

**11**  truly crucify! And Pilate said to the soldiers: go, Lord.
`righteous crucify and say Pilate to soldier go Lord`

## 047r — the third time, and Caesar

**1**  into the house. And a third time the Lord did [so], went into the house,
`inside-house and three Lord ~do go on-house`

**2**  and Pilate cried: Behold Jesus Nazareth
`and shout Pilate lo Jézus [?]`

**3**  the King of the Jews! [Caesar] and the angel
`king Jew(ish) [?] in_turn angel`

**4**  to Bethlehem town; and they shouted.
`to-Bethlehem town and shout`

**5**  the Jews: the cross for the Lord! Pilate: the Lord is accursed […]
`Jew(ish) +cross Lord Pilate cursed Lord [?]`

**6**  Pilate: if the Jews want the Lord, enemy | of
`Pilate if want Lord Jews enemy | of.`

**7**  the emperor, truly crucify! And then the Jews
`emperor righteous crucify and_said Jew`

**8**  [Behold], he, the king of the Jews, he.
`[Behold] he king Jew he.`

**9**  half [said]: one, the Lord; [half]: heretic, one.
`half one Lord heretic one`

**10**  the Lord blasphemeth. And Pilate cried, Pilate,
`blasphemer-Lord and shout Pilate this Pilate`

**11**  and how [cried] in the Lord [out] Pilate: he <subject marker>
`and how? [cried] inside Lord [out] Pilate he SUBJ`

> John 19:12, Caesar. The Ecce Homo is put three times, first second third,
> the way the codex numbers everything.

## 047v — Pilate washes his hands

**1**  truly the man. And then Pilate: Jews, carry water
`righteous man^ and_said Pilate carry-Jews water`

**2**  in one washdish; and then Pilate was [there].
`inside one washdish and then-~Pilate exist.`

**3**  carry; and Pilate washed high his two hands. And then
`carry and high-wash-~Pilate of two hands and_said`

**4**  Pilate: this Pilate [is] innocent of the Lord's blood. And then
`Pilate this-~Pilate innocent from of-Lord blood and_said`

**5**  the Jews: because this is on the Jews, and on the Jews' son.
`Jew because this exist on-Jews and of-Jews son`

**6**  and Pilate cried: whom will ye |
`and shout Pilate who want | [?]`

**7**  to the Jews, release Barabbas or Jesus? And
`to Jews release Barabbas in_turn Jesus and`

**8**  the Jews cried: release Pilate Barabbas,
`shout Jew(ish) release [?] Barabbas`

**9**  or Jesus? On the cross, crucify! And then Pilate understood;
`in_turn Jesus on_the_cross crucify and_said Pilate understand-eat`

**10**  the soldiers led the divine one up to the house; and then Pilate, to
`soldier go divine_one^ up on-house and then Pilate to`

**11**  the divine one went [went] up into the house; and Pilate shouted | from
`divine_one^ go [went] up on-house and shout Pilate | from`

> Matthew 27:24, the basin and "I am innocent of the blood of this just
> person", with the choice of Barabbas right after it.

## 048r — the Reproaches: O my people, what have I done to thee

**1**  <subject marker> the man truly took to crucify, because <subject marker>
`SUBJ somebody righteous grab on-crucify because SUBJ`

**2**  [he did] not want the Lord crucified; and the Lord did [so].
`not_want Lord-to crucify and Lord ~do`

**3**  Pilate went out of the house down among [them]
`Pilate out(ward) go on-house [?] among from [?]`

**4**  the Jews; and the Lord Jesus shouted: people,
`~Jew and shout Lord-Jesus people`

**5**  the Lord's Jews, who I, he said, did,
`of-Lord Jew who I he_said* ~do`

**6**  why? this people [cross], did, people,
`why? this-people [cross] ~do people`

**7**  the Lord's Jews, who, this people, I; commit sin.
`of-Lord Jew who I this-people commit sin`

**8**  [O my] this people, good [what] then the Lord I
`[O_my] this-people-to good [what] then-Lord I`

**9**  among this people did miracles. First, |
`among this-people-to miracle do, first | this`

**10**  people went into Egypt [out of] living servants; this
`people go on-Egypt [out_of] living-servant this`

**11**  over the sea, the sea I divided
`over sea sea divide`

## 048v — forty years in the wilderness, and a cross for their Saviour

**1**  in two directions, this people, over the sea.
`on-two direction this-people over sea`

**2**  through struck the Lord led them by day, and from the beginning
`through [?] go-Lord +day in_turn from head`

**3**  every sky to the people, all the world | this
`every sky to-of-people ~all_the_world | this`

**4**  people [fed], living, the Lord, forty, in the field,
`people [fed] living-Lord forty inside field`

**5**  in turn the angel, bread to this people.
`in_turn angel bread to-this-people`

**6**  [thou hast prepared] cross I did for the Lord's people,
`[?] [?] do, people <of>-Lord`

**7**  the Jews, he said, to the Lord; raised [him] on Palm Sunday | then
`Jew he_said* to-Lord-to raise on-Palm_Sunday | then`

**8**  they would make the Lord king, a crown, and […]
`chapter-Lord want king crown in_turn [?]`

**9**  would say, the Lord's body on the cross lifted up.
`would_say* of-Lord body on_the_cross lift_up`

**10**  and Pilate shouted; the Jews took the Lord, blind[folded]
`and shout Pilate grab-Jews Lord ~blind`

**11**  and the Lord taken, the Jews; and then the Jews
`and Lord take* Jew and then Jews`

> This is the Improperia, the Reproaches sung on Good Friday: *O my people,
> what have I done unto thee? I brought thee out of Egypt, I divided the
> sea, I led thee forty years through the wilderness, and thou hast
> prepared a cross for thy Saviour.* It is liturgy, not gospel, and the
> codex has it in order, with forty written the way it is written of the
> flood.

## 049r — the two thieves, and Mary Magdalene told

**1**  the Jews went; two thieves to the Lord Jesus, and put
`to-go Jews two ~thief to Lord-Jesus and put`

**2**  the Jews, the cross on the Lord Jesus; in turn, from two thieves | carried
`Jews cross on-Lord-Jesus in_turn from two ~thief | carry`

**3**  the Jews; who […] good; from the [sepulchre] [laid] the Lord Jesus.
`Jews who-[?] good from [sepulchre] [laid] Lord-Jesus`

**4**  And Saint John went up into Bethany, to
`and to-go up holy-John inside Bethany to`

**5**  Mary Magdalene: [sought] Master, the Lord liveth [early]
`two-Mary Magdalene good [?] Master living Lord [?]`

**6**  to Mary Magdalene [appeared]; and the Jews <subject marker>
`to-Mary Magdalene [appeared] and Jews SUBJ`

**7**  understood, went; Mary Magdalene, John [stood]; at that time
`understand-go Mary Magdalene John [stood] time`

## 049v — over the Cedron, and Simon carries it

**1**  I go, the Jews were [at] the Kidron; and then the Lord went
`go I Jews exist Kidron and then go Lord`

**2**  the Jews, over the Kidron; and then
`Jews over Kidron and then`

**3**  down [to the ground], to the sick, the Lord Jesus; and collapsed | from
`down [ground] to-°sick Lord-Jesus and collapse | from`

**4**  fall down the Lord Jesus […]; and the Jews knelt
`[?] Lord-Jézus [?] and kneel_(down) Jew(ish)`

**5**  before the Lord Jesus; and the Jews spoke: healthy man,
`before Lord-Jesus and speak-Jews healthy_man^`

**6**  Jesus of Nazareth! And there came to the Lord | the Virgin
`Jesus Nazareth and leave to-Lord | virgin`

**7**  Mary; and Simon carried it for the Lord; and | when
`Mary and Lord Simon [?] carry and | then`

**8**  the Jews […] cross […] within Eden
`exist Jew [?]-+cross-[?] inside ~Eden`

**9**  and the Jews put the cross on the earth, and
`and put-Jews cross on-earth and`

**10**  took off [his clothes]; believe on the Lord Jesus; food [garments]
`take_off believe on-Lord-Jesus food [garments]`

**11**  [they parted] the Lord; the Jews took off the Lord Jesus [his clothes], and
`[they_parted] Lord take_off-Jews Lord-Jesus and`

> Simon of Cyrene, Matthew 27:32.

## 050r — laid upon the cross

**1**  the Virgin Mary came to the Lord Jesus; and | from
`leave Virgin_Mary to-Lord-Jesus and | from`

**2**  [they bound] the first … the Lord's handcuffs. And then
`[they_bound] of-exist-°first of-Lord handcuffs and_said`

**3**  the Lord Jesus, name […] of the Lord, have, the Jews
`Lord-Jesus name-[?]-~exist of-Lord have Jews`

**4**  trespass [wrote] this, within the commandment, this one apostle, the Lord's apostle;
`trespass [wrote] this inside commandment this apostle-+one of-Lord apostle`

**5**  and the Jews saw [the title] the whole wide world
`and see Jew(ish) [?] good the_whole_wide_world`

**6**  in the year of suffering the Lord went; and [written], the Jews, within
`on-suffering-year go Lord and [written] Jews inside`

**7**  the Lord believed; and they laid the Lord upon the cross,
`Lord believe and to-Lord place_onto +cross`

**8**  and the Lord, the Jews nailed one hand.
`and Lord nail-Jews one hands`

**9**  and the two [between] the cross, and could
`and two [?] +cross and can`

**10**  took, and the hand the Jews drew with the chain.
`take* and hands chain-draw-Jews`

**11**  and the hand the Jews nailed; and the Lord's foot could
`and hands nail-Jews and of-Lord foot can`

## 050v — the title, and the ninth hour

**1**  take, and the foot the Jews drew with the chain.
`take* ~and foot chain-draw-Jews`

**2**  and they pierced the feet; and all the Lord's [title]; and | of
`and foot pierce and every of-Lord [title] and | of`

**3**  the Lord [three tongues] in the Lord, to, trench, to, trench, in the Lord Jesus Christ.
`Lord [three_tongues] inside Lord to-°trench-to-°trench inside Lord-Jesus-Christ`

**4**  And Pilate wrote upon a tablet: Jesus
`and write Pilate on-one tablet Jézus`

**5**  Nazareth, king of the Jews. And then the Jews
`Nazareth king Jew and_said Jew`

**6**  write that the Lord said he is King of the Jews. But the Lord's writing,
`write Lord king Jew(ish) a) Lord write`

**7**  Jesus of Nazareth. And then Pilate: I have written, <subject marker>
`Jesus Nazareth and_said Pilate write SUBJ`

**8**  Pilate has written. And the two thieves; with the Lord they nailed them
`[?] ~Pilate write and two ~thief to-Lord pierce`

**9**  on the cross; and the Lord called two thieves, one […]
`on_the_cross and Lord call^ two ~thief one-[?]`

**10**  the Jews; and this was out [at] the ninth hour. And then the Lord Jesus
`Jews and this out nine hour and_said Lord-Jesus`

**11**  on the cross asked the Father, the Lord God of heaven.
`on_the_cross the_father of-Lord God heaven ask-Lord`

> John 19:19–22, the title and "what I have written I have written", and
> Matthew 27:46, the ninth hour.

## 051v — three nails, and the sponge on a stick

**1**  remained Mary's woe, than the Lord's three nails, long, [with which]
`remain* of-Mary woe than of-Lord three_nails long to`

**2**  I was pierced to the cross. And then the Lord Jesus: I thirst, the Lord; and | of
`I pierce to-cross and_said Lord-Jesus thirst Lord and | of`

**3**  Lord's apostles, when they bought grape, sweet, and
`Lord apostle then buy grape sweet and`

**4**  wine; the apostles took [it to] the high priest; and
`wine grab apostle high_priest = and`

**5**  the Lord; [somebody] took, but to the Jews [to] drink; in turn the Lord | took
`Lord grab-+who but Jews-to drink in_turn Lord | grab`

**6**  the Jews: vinegar, and [hyssop]; and the Lord.
`Jews vinegar and [hyssop] and Lord`

**7**  wine the Jews took on one sponge, and
`wine grab Jews on-one sponge and`

**8**  then the Lord's face; the Jews wiped the sponge; and the wine
`then-Lord sponge face wipe_off-Jews and wine`

**9**  he took [into] his mouth, a little, on the [pine]. And then | the Lord
`grab mouth little on-+pine and_said | Lord`

**10**  Jesus on the cross offered [to] the Father, the Lord God of heaven
`Jesus on_the_cross the_father of-Lord God heaven offer`

**11**  I this Father, the Lord's soul into God the Father's
`I this-father of-Lord soul inside of-God_the_Father`

> John 19:29, the sponge on hyssop, and Luke 23:46, "Father, into thy hands".

## 052r — two lines

**1**  hands; and from the Lord Jesus, the Lord's soul, gave up the ghost.
`hands and from to-Lord-Jesus of-Lord soul give_up_the_ghost`

**2**  Here ends this Passion: the evangelist's suffering of the Lord Jesus.
`end this Passion = evangelist* suffering Lord-Jesus`

## 052v — the earthquake, and Longinus

**1**  And then the Lord Jesus, his soul, gave up the ghost on the cross; the earth
`and then Lord-Jesus of-Lord soul give_up_the_ghost on_the_cross earth`

**2**  quaked, the rocks and the stones rent; the sun and the moon
`quake rock stone [?] sun and moon`

**3**  this eclipse; and every tree among the people humbled itself; and all
`this eclipse and every tree among_the_people* this humble ~and every`

**4**  creation mourned, when Christ the Lord was crucified. And the Jews went.
`create mourn then Christ crucified Lord and go Jews.`

**5**  one soldier to Jerusalem, blind; and the soldier's name
`one soldier on-Jerusalem blind and name soldier`

**6**  was Longinus; and the Jew's spear pierced the side
`exist Longinus and pierce Jew spear side`

**7**  the Lord Jesus Christ; and [pierced] the spear
`Lord-Jézus-Christ and can [?] spear on`

**8**  side of the Lord Jesus Christ; how the soldier [thieves] splash[ed]
`side Lord-Jesus-Christ how? soldier [thieves] splash`

**9**  the Lord Jesus's blood on the place; through [it] he saw, and the soldier was healed;
`blood Lord-Jesus on-place through see and healing soldier`

**10**  and the soldier believed in the Lord Jesus Christ,
`leave and grab soldier believe Lord-Jézus-Christ`

**11**  and the soldier saw, baptized, and saw, Jew
`and soldier see-baptize and see ~Jew`

> Longinus, the blind soldier whose sight is restored by the blood from the
> spear wound, is not in any gospel. He is the Golden Legend, and Király and
> Tokai's dictionary has a code glossed for him by name.

## 053r — after the ninth hour

**1**  the power of the Lord Jesus Christ; and [many] believed in the Lord,
`power Lord-Jesus-Christ and [many] inside Lord believe`

**2**  but many [in] joy brought […], the Jews, home.
`but many joy brought* [?]-Jews home`

**3**  The second Jews sadly accused, because [darkness] [came]
`second Jews sad accuse because [darkness] [came]`

**4**  the Jews, that they put to death, the Jews, the Son of God; and
`Jews that* ~execute Jews son God and`

**5**  sadly went the Jews, […] the Jews, home; and this
`sad go Jews [?]-Jews home and this`

**6**  [from] was the ninth hour, and four hours from that hour
`[?] out(ward) nine ~hour and two-two from ~hour`

**7**  on the cross suffered the Lord Jesus; and the Jews went [and] brought
`on_the_cross suffer Lord-Jesus and-Jews go-?brought`

**8**  all […] home from [breast] [striking]
`each,_every [?] home from [?] [?]`

**9**  in turn the apostles were apart; every one returned to the apostles; [stood] | on
`in_turn apostle exist apart return every to-apostle [stood] | on`

**10**  […] and one, and […]
`[?] and one and understand-eat`

## 053v — Joseph and Nicodemus ask for the body

**1**  the apostles cut off; and then two, somebody, have mercy, Jerusalem, one
`apostle cut_off and then two somebody-have_mercy Jerusalem ~one`

**2**  and his name was Joseph; the second
`and name exist Joseph second`

**3**  Nicodemus; and then the two asked of Pilate
`~Nicodemus and then-exist two ask_(for) from Pilate`

**4**  was before the Lord Jesus; and the two had suffered.
`~exist-before Lord-Jesus and have two sufferer`

**5**  was before the Lord Jesus; and then the two went [away]
`~exist-before Lord-Jesus and then two go [away]`

**6**  Christ was crucified; and the two went to
`exist Christ crucify and go to two`

**7**  many Jews; and the two were, that is, good and merciful men;
`many Jew(ish) and two people that_is good people have_mercy`

**8**  and then the two saw the Virgin Mary, and Mary.
`and then two see Virgin_Mary and Mary.`

**9**  Magdalene. Many people went out of Jerusalem, and
`Magdalene go many people on-Jerusalem and ~through`

**10**  were afraid, because the Jews wanted to the Lord, every Lord [take down], because
`startle because to Lord want Jew every Lord [take_down] because`

## 054r — taken down, and the tomb sealed

**1**  this was from | and [down] went down [from the cross]
`this exist from | and [down] go down [from_the_cross]`

**2**  because Mary was […] fled […]
`because exist-Mary [?] escape [?]`

**3**  the Jews; and in that place were these people, when
`Jew(ish) and on-place exist this people then-exist`

**4**  the two Marys went to the people, and took
`from two-Mary to-people go-two-Mary and grab`

**5**  Nicodemus [took] from the cross [by] name the Lord Jesus; in turn the three nails,
`~Nicodemus on_the_cross name Lord-Jesus in_turn three three_nails`

**6**  […] Saint John took […] saw | the Virgin
`[?] grab holy-John [?] see | virgin`

**7**  Mary; then [he] took the Virgin Mary into [his] bosom
`Mary then grab Virgin_Mary inside bosom`

**8**  and did Nicodemus, of the living servant
`~and ~do Nicodemus of-living-servant`

**9**  [linen]; and the two covered the body; and then [linen]; and
`[linen] and cover two body and then [linen] and`

**10**  Nicodemus put in, [by] name, at the end, the Lord Jesus; and
`put_in Nicodemus name-end-to Lord-Jesus and`

**11**  they closed the Lord within the tomb; and they left a seal, the Jews; to the Lord four soldiers from
`Lord inside tomb close and leave seal* Jews to-Lord two-two soldier from*`

**12**  were opened the chief of Jerusalem; and [the veil] went [part]. Here ends this
`[?] Jerusalem head ~and [?] go [?] end this`

**13**  holy gospel.
`holy-gospel`

## 054v — a rubric, naming Mark

**1**  Here begins this holy gospel, written by Saint Mark.
`begins this holy-gospel write holy-Mark`

> The fourth evangelist the codex names for itself, after Luke, Matthew and
> John. What follows is Mark 16, and it follows it closely.

## 055r — the three women at the tomb

**1**  in the seventh chapter of his writing: at that time, when
`inside seven chapter of-write time then`

**2**  they went the three Marys [bought] to the tomb of Christ, because they had prepared
`go [?] [?] burial_chamber Christ because-exist prepare`

**3**  [spices] another [anoint] […] Jesus:
`[?] [?] this-cut_off [?] [?] Jézus`

**4**  Mary Salome, and Mary the mother of James, and
`Mary Salome and Mary James mother and`

**5**  Mary Magdalene. And then these Marys [and] these Marys
`Mary Magdalene and then-exist this-two-Mary [?] this-two-Mary`

**6**  among [Salome] […]
`among [?] [?]`

**7**  lifted up the stone from the tomb; and then | went on, the three [Marys]
`lift_up from stone on-tomb and then | go_on-+three`

**8**  Mary came to the tomb of Christ, and saw the three Marys [the sabbath]
`Mary to-burial_chamber Christ and see [?] [?]`

**9**  the tomb [rolled away]; and then the three Marys within this
`+<subject_marker> burial_chamber from [?] and then-exist [?] inside this`

**10**  the three Marys, and the three Marys entered; and
`the_three_Marys and enter the_three_Marys and`

**11**  remain, saw […] Jesus; but saw the first
`remain* see ~exist-[?] Jesus but see first^`

> Mark 16:1 names exactly these three: Mary Magdalene, Mary the mother of
> James, and Salome. The codex has all three, and the stone rolled away.

## 055v — be not afraid, he is risen

**1**  angel, sitting on the left side, from [a young man] within
`angel sit on-left_(side) direction from [?] inside exist`

**2**  cover […] Jesus. And then Mary, through
`[?] [?] Jézus and then-exist Mary through`

**3**  was afraid, because Mary supposed as a ghost.
`startle because rather-Mary [?] +<subject_marker> how? ghost`

**4**  And then the angel: do not have [fear], the three Marys, [be affrighted]
`and_said angel do_not ~have-+the_three_Marys [be_affrighted]`

**5**  the three Marys be not afraid. He is risen, whom ye mourn — the Lord Jesus,
`[?] through startle +rise mourn to-Lord from Jézus`

**6**  whom they crucified, is risen seek; but […]
`execute +rise [?] a) [?]`

**7**  within Galilee and […]
`inside [?] and [?]`

**8**  the Lord's disciples and Peter, said the three Marys, [at the] side. This
`of-Lord disciple^ and Peter say-+the_three_Marys side^ this`

**9**  holy gospel. And then the three Marys went, this woman
`holy-gospel and then-+the_three_Marys go this woman`

**10**  head, from this tomb of Christ; and | return
`head from this tomb Christ and | return`

**11**  Mary Magdalene went back to the tomb of Christ. At that time
`[?] back Mary Magdalene to-burial_chamber Christ time`

> Mark 16:5–7, including "tell his disciples and Peter", which is Mark's
> detail and no one else's. The codex puts the angel on the left; Mark says
> the right.

## 056r — Mary Magdalene takes him for the gardener

**1**  the Lord Jesus appeared to Mary Magdalene in the form of a
`appear Lord-Jézus Mary Magdalene inside shape,_form from one`

**2**  gardener. And then this gardener, the Lord Jesus Christ, | [said to] this
`gardener and_said this gardener-Lord-Jesus-Christ | this`

**3**  woman: that [came], woman, mourning for the Lord; this, from
`woman that [came] woman mourn to-Lord this from`

**4**  Jesus, whom they crucified, is risen, because
`Jézus execute +rise [?] because`

**5**  said the shepherd: [risen]; see, the shepherd, light in heaven
`say shepherd [risen] see-shepherd light on-+heaven`

**6**  town, chapter, in turn [she] stooped down [into] the tomb, bowed down; and the tomb <subject marker>
`town-chapter-in_turn stooped_down* tomb bow_down and tomb SUBJ`

**7**  light, open; and verily [he] could, that [he] rose.
`light open and verily can that rise`

**8**  And the Lord Jesus stood before Mary Magdalene
`and leave Lord-Jézus before Mary Magdalene`

**9**  in that place; Mary [turning] that
`on-to-place Mary [?] on-reason [?]`

**10**  he: Master! And the Lord <subject marker> to Mary, [to] the apostles: go, the Lord, [to] the apostles.
`he Master and Lord SUBJ to-Mary-apostle go-Lord-apostle`

**11**  And Mary went to these two sisters, the women,
`and go-Mary to this two sister wife`

> John 20:15, where she supposes him to be the gardener, and 20:17, go to my
> brethren. The codex explains the mistake by saying he appeared in that
> form.

## 056v — two lines

**1**  and then Mary went with these women,
`and then-exist Mary understand-go-Mary this woman`

**2**  and Mary would tell […]
`and want say Mary from`

## 057r — he stands among them

**1**  Magdalene saw the Master in the form of a gardener.
`Magdalene see-Magdalene Master inside [?] from gardener`

**2**  At that time the Lord Jesus Christ stood in the midst, living,
`time leave Lord-Jézus-Christ middle living`

**3**  among the three Marys, the Lord, among these sisters
`among +the_three_Marys Lord among this sister`

**4**  Jerusalem. And then the Lord Jesus: the commandment of God among
`Jerusalem and_said Lord-Jesus commandment God among`

**5**  you: his mercy to whoever believes
`you <of>-Lord have_mercy somebody to and believe`

**6**  in the Lord, and in the Lord, from God the Father, ever.
`inside Lord and inside of-Lord from God_the_Father ever.`

**7**  ever, amen. And then the Lord Jesus <subject marker>
`ever amen and_said Lord-Jesus SUBJ`

**8**  the three Marys; Mary saw within the tomb […]
`+the_three_Marys see-Mary inside burial_chamber brother-chapter`

**9**  […] Jesus whom they crucified; and Mary Magdalene said […]
`from Jézus execute and say Mary Magdalene [?]`

**10**  Mary saw the Lord risen from the dead; and
`Lord-Mary see-Mary +rise on-die and`

**11**  the Lord Jesus Christ stood among the three Marys […] the apostles. This holy gospel.
`leave Lord-Jézus-Christ among +the_three_Marys this apostle holy-gospel`

## 057v — an Old Testament prophecy, and Mark again

**1**  Written by Saint […] the prophet,
`write holy-<prophet>`

**2**  the prophet, in the Old Testament, truly,
`prophet <Old_Testament> righteous(ly)`

**3**  the sixth chapter of his writing,
`six chapter of-write`

**4**  and Saint Mark seven
`in_turn holy-Mark [?]`

**5**  it is written. Said Saint […] the prophet:
`write say holy-<prophet>`

**6**  because he saith […] it is found,
`because say +<subject_marker> exist find`

**7**  in the Old Testament is truly written this word: the Lord shall rise from the dead.
`inside <Old_Testament> righteous(ly) write this word stand_up-Lord on-die-Lord`

**8**  the King; to the Lord thanks [not]; and the Lord destroyed hell, Christ; and from
`king to-Lord thanks [not] and destroy Lord hell Christ and from`

**9**  [Adam] [bound]: hell could [not], Satan. This is written | to
`[Adam] [bound] hell can Satan this_is write | to`

**10**  Saint Mark, in the seventh chapter of his writing: when the Lord
`holy-Mark inside seven chapter of-write then Lord`

**11**  Christ upon the cross breathed out his soul, the earth quaked,
`Christ +cross <of>-Lord soul breathe_out earth quake`

**12**  the rocks and stones rend; the sun and the moon
`rock stone this [?] sun and moon this`

## 058r — the harrowing of hell

**1**  eclipse; and every tree into the world humbled itself; and all creation mourned
`eclipse and every tree into_the_world* this humble and every create mourn`

**2**  when Christ was crucified. And four hours
`then-exist Christ +crucified and two-two hour`

**3**  the Lord Jesus suffered upon the cross; and the Lord within the tomb | the apostles laid him,
`+cross suffer Lord-Jézus and Lord inside burial_chamber | put-apostle`

**4**  Mary, the angel; and then the Lord within the tomb they laid, the Lord; and
`Mary-angel and then-Lord inside tomb lay Lord and`

**5**  at that hour, at that time, came from the Father God in heaven,
`hour time go the_father God heaven`

**6**  from the Father, an angel within, before the Lord Jesus; and
`on-of-father angel inside ~exist-before Lord-Jesus and`

**7**  rise, from prayer; in turn the angel within the tomb stay
`rise* from ~pray in_turn angel inside tomb stay`

**8**  in turn to the Lord; the Lord went to hell, and destroyed hell; and who
`in_turn to-Lord go-Lord on-hell and hell destroy and who`

**9**  the people who died within a hundred years, and within | five
`people die inside one hundred-year and inside | +five`

**10**  sat, year; and within nine […]; and nine years; all the prophets
`sit-~year and inside nine-[?] and nine-~year every prophet`

**11**  went into hell; and [brought out] three souls, all out the Lord went,
`go on-netherworld and [?] +three soul each,_every [?] go Lord`

**12**  in turn three souls within hell stayed; the Lord | spoke.
`in_turn three soul inside hell stay Lord | speak.`

## 058v — Adam's soul kneels to the Virgin

**1**  Saint Augustine: within many years, and one soul [counsel]
`Saint_Augustine inside many-to-year and one soul [counsel]`

**2**  went into heaven; but then to the Lord
`~go inside heaven = but then to-Lord`

**3**  went to the souls, the Lord, and [brought out] three souls
`to-soul-soul-soul-soul-soul go Lord and [?] +three soul`

**4**  every [one] out the Lord went to the souls; and the Lord appeared
`every* out to-go Lord soul and Lord appear Lord`

**5**  the blessed Virgin Mary; and Adam's soul knelt
`blessed Virgin_Mary and kneel ~Adam soul`

**6**  before the blessed Virgin Mary; and the girl <subject marker> had mercy,
`before blessed Virgin_Mary and girl SUBJ-have_mercy`

**7**  asked, and blessed the blessed Virgin Mary;
`ask and bless blessed Virgin_Mary`

**8**  and all the souls, soul upon soul, left before the blessed
`and to-soul-soul-soul every leave before blessed`

**9**  Virgin Mary; and within Paradise the souls, the Lord, the souls;
`Virgin_Mary and inside Paradise soul Lord soul`

**10**  and the Lord went to the souls; and then twenty-five
`and go Lord soul and then two-ten-ten five`

**11**  hours; and this was […] the sixth hour.
`hour and this out(ward) [?] six hour`

> The descent into hell, from the Gospel of Nicodemus, with Augustine cited
> by name. Adam's soul kneeling to the Virgin is later devotional material,
> not the Gospel of Nicodemus.

## 059r — one line

**1**  And on the third day the Lord Jesus Christ rose from the dead.
`to-and +on_the_third_day from die stand_up Lord-Jézus-Christ`

## 059v — the road to Emmaus

**1**  Here begins this holy gospel,
`begins this holy-gospel`

**2**  written by Saint Luke, in the first
`write holy-Luke +one`

**3**  [chapter] of his writing: at that time,
`<of>-write time`

**4**  when there went two
`then-exist go two`

**5**  apostles out of Jerusalem into a
`apostle Jerusalem inside one`

**6**  town; and | was, the chapter
`town and | exist-chapter`

**7**  year, by name, was Emmaus; and then the two apostles found [him] from the living
`~year-+name exist Emmaus and then find-two-apostle from living`

**8**  Lord Jesus; and then the two talked of how the Lord, he
`Lord-Jesus and then two talk^ how?-Lord he`

**9**  was truly somebody, truly the Lord, preaching various [things]
`exist righteous somebody righteous Lord ~preach various`

**10**  miracles he did [spoke of]; the two apostles; the Jews'
`miracle do, [?] <of>-two-apostle Jew(ish)`

**11**  chief crucified him. At that time there appeared
`head execute time appear`

**12**  to the two apostles the Lord Jesus, in the form of a traveller; and then
`two-apostle Lord-Jézus shape,_form traveller and then-exist`

> Luke 24:13–21, and the codex names Emmaus. As with the gardener, it
> explains why they did not know him: he appeared in the form of a traveller.

## 060r — the Lord asks the two what they are speaking of

**1**  The two apostles [drew near] Lord Jesus, and the two apostles began to talk, and
`two-apostle [?] Lord-Jézus and two-apostle (begin_to)_talk and`

**2**  the Lord talked. And then the Lord Jesus: O, of the Lord
`Lord talk and_said Lord-Jesus oh of-Lord`

**3**  two apostles, brother, saying, two apostles, Lord, how, saying among
`two-apostle ~brother say two-apostle Lord how? say ~among`

**4**  [one another] have, two apostles, because they said the Lord Jesus Christ
`[one_another] have two-apostle because say exist Lord-Jesus-Christ`

**5**  apostle, that the two men spoke of the Lord; I, the two
`apostle that* two somebody from-Lord speak I two`

**6**  Lord's apostles, three [with] the Lord. And then Luke, this [named]
`Lord apostle three Lord and_said Luke this [named]`

**7**  the way, the man, this Lord, this good remain [sad]
`way somebody this Lord this good [?] [?]`

**8**  how [knowest not] <subject marker> the miracles [in] Jerusalem, done as
`how? [knowest_not] SUBJ miracle Jerusalem ~do as`

**9**  somebody [the Jews] […], the head, truly
`somebody [?]-Jews head righteous`

**10**  crucified this Jesus; and the Lord came into the world, went
`execute this Jézus and +the_Lord ?into_the_world go-Lord`

**11**  went, <subject marker> preaching […], various miracles he did.
`go-+SUBJ preach-[?] various miracle do`

> Luke 24:17–20. The codex keeps the two apostles' complaint that the chief
> priests crucified him, and names Luke as one of the two, which the gospel
> does not.

## 060v — the miracles, and the women's news they did not believe

**1**  the eyes of the blind, <subject marker> through [him] light; the dead, <subject marker> resurrected; | the lame
`eyes ~blind SUBJ through light die SUBJ resurrect | lame`

**2**  lame the body, and the evil, those possessed by the evil one, healed
`[?] body and evil obsessed_by_the_evil from-healing`

**3**  and the Lord <subject marker> was from [the third day] up
`and Lord SUBJ exist from [the_third_day] up`

**4**  he rose, the Lord; and said one woman, the head
`stand_up-Lord and say one ~woman ~head`

**5**  the news was of the Lord up he rose; the news the two
`news exist-Lord [?] stand_up-Lord news two`

**6**  apostles [certain] believed, who from the Lord, from the dead
`apostle [?] believe who from Lord from die`

**7**  the Lord stood up, because as the Lord's brother, to
`stand_up-Lord because as of-Lord brother-to`

**8**  rot this pleasing, and who from the Lord, from the
`[?] this pleasing who from Lord from`

**9**  the dead stood up. And then the Lord Jesus: you two
`die stand_up and_said Lord-Jesus you two`

**10**  […] the man, to hide, the two believing
`[?] somebody to-hide_oneself believe-two`

> Luke 24:21–24, the report of the women at the tomb that the two did not
> believe.

## 061r — O fools and slow of heart, and Cleopas is named

**1**  You two, this, to <subject marker>, rise from prayer
`~you-two this to-+SUBJ rise* from pray`

**2**  And then the Lord Jesus left; the Son of God was dead.
`and_said Lord-Jesus leave exist die son God`

**3**  more than these, rise from prayer, from prayer
`more_than_these* rise* from pray from pray`

**4**  the Lord, from God the Father in heaven; and the beginning, through
`the_Lord from God_the_Father heaven and beginning^ through`

**5**  the Lord Jesus expounded, from Adam, the trespass, the scripture
`explain Lord-Jesus from ~Adam ~trespass scripture^`

**6**  said. And then Cleopas, Luke, this Lord, to the two [foolish]
`say and_said Cleopas Luke this Lord to-two [foolish]`

**7**  the Lord wanted good, said. And then the Lord Jesus, from Abel
`want-Lord good say and_said Lord-Jesus from Abel`

**8**  […] signified this Jesus crucified, how, in turn
`[?] symbolize this Jézus execute how? | in_turn`

**9**  [slow of heart] died, the brother's he said and this Jesus
`[?] die <preposition_of_genitive>-brother [?] and this Jézus`

**10**  died, the Lord's brother. And then the Lord Jesus, from Noah
`die of-Lord brother and_said Lord-Jesus from Noah`

> Luke 24:25–27, *beginning at Moses and all the prophets, he expounded unto
> them.* The codex begins further back, at Adam's trespass. **Cleopas is
> named on line 6**, which is Luke 24:18, and the codex makes Luke the other
> of the two.

## 061v — Abraham as the figure of the crucifixion

**1**  Noah symbolized this Jesus put to death, as Noah
`~Noah symbolize this Jesus execute as ~Noah`

**2**  redeemed all the world; in [the wood] this [Isaac], and on this Jesus
`redeem every world inside [the_wood] this [Isaac] and on-this Jesus`

**3**  put to death, every [one] is saved; Adam gained. And then
`execute be_saved every ~Adam gain and_said`

**4**  the Lord Jesus, about Abraham: Abraham symbolized this
`Lord-Jesus about Abraham Abraham symbolize this`

**5**  Jesus crucified, and Lord Jesus said, said the Lord.
`Jézus execute and say Lord-Jézus say exist Lord-<suffix_of_divine_name>.`

**6**  Abraham, to the angel of the Lord God — Abraham took
`Abraham on-~angel of-Lord_God Abraham take^`

**7**  his son […] and the Lord […]
`<preposition_of_genitive>-son [?] and Lord [?].`

**8**  […] who did, Abraham on
`[?] who do, Abraham on`

**9**  tie up the faggots […] in turn Abraham
`[?] faggot [?] in_turn Abraham`

**10**  took sword who Isaac wished to slay
`grab [?] who [?] want slay`

> The typology is the standard one, and line 4 has to be read with the
> codex's own pronoun rule, where a name sign written twice is the name and
> then a pronoun for it. It is not saying Abraham is the figure of Christ.
> What signifies the crucifixion is the sacrifice: **Abraham gives his son**
> (lines 6–7), as God the Father gives his, which is what 062v:2–3 then says
> outright. Isaac is the figure of Christ and Abraham of the Father. The
> faggots on line 9 are the wood Isaac carries, Genesis 22:6, read by
> medieval commentary as the cross.

## 062r — the mount, the ram, and the angel

**1**  And then he went on this, to the mount […]
`and then-exist go on-this to-mount [?]`

**2**  wanted a sacrifice. And then Isaac: O,
`want sacrifice and_said Isaac oh`

**3**  my father donkey and went far
`<preposition_of_genitive>-father [?] and go far`

**4**  […] and a, and the ram, and a
`[?] and a and sheep and a`

**5**  the lamb, who? Isaac's father, sacrifice; and said
`lamb who Isaac father sacrifice and say`

**6**  the father Abraham: from whom the Lord God [gives] the ox.
`the_father Abraham from who Lord_God ox.*`

**7**  offering and then tie up bundle of wood
`[?] and then-exist [?] [?]`

**8**  of Isaac, sheep, living, the Lord wanted to slay, and
`of Isaac ~sheep-living want Lord slay and`

**9**  the Lord God shouted in the cloud to the angel: stop!
`shout Lord_God in_the_cloud on-angel stop`

**10**  Abraham, to the whole wide world, the Lord's love, this is
`Abraham to-the_whole_wide_world +<subject_marker> Lord <preposition_of_genitive> love +this_is`

> Genesis 22. *My father* on line 3 is Isaac's question, the ram caught for
> the sacrifice is on line 4, the young men left behind with the ass on
> line 5, and the angel stops the hand on line 9.

## 062v — he made as though he would go further, and they constrained him

**1**  the Lord's peace. And then the Lord Jesus: as was Isaac,
`Lord peace and_said Lord-Jesus as exist Isaac`

**2**  as he gave his father's [son], so this Jesus was crucified
`to-give <preposition_of_genitive> father so and so Jézus execute exist`

**3**  the Lord gave, his divine Father, and he rose
`to-give-Lord <preposition_of_genitive>-Lord father-<suffix_of_divine_name> and +<subject_marker> ?rise`

**4**  the Lord, from prayer, because the Lord, from prayer, the Father,
`Lord from ~pray because-+the_Lord from ~pray the_father`

**5**  God of heaven. And then the apostles of the Lord went, this town.
`God heaven and then go-apostle-Lord this town`

**6**  And then the Lord Jesus: go, two apostles, you, because I
`and_said Lord-Jesus go-two-apostle you because I`

**7**  the Lord had a long way; and the Lord began, the two apostles
`have-Lord long way and Lord begin two apostle`

**8**  persuaded; and then the Lord was [there]; the two apostles persuaded, and | the two
`persuade and then-Lord exist two-apostle persuade and | two`

**9**  the Lord's apostles went, and then the Lord's two apostles into the room went
`apostle-Lord go and then-exist two-apostle-Lord on-+room | go`

**10**  the Lord's two apostles, and the two apostles sat the Lord at the table, and
`two-apostle-Lord and sit-two-Lord-apostle to-throne and`

> Lines 2–3 close the Abraham figure and state it plainly: as Abraham gave
> his son, so God the Father gave his, and Jesus was crucified and rose.
> Abraham stands for the Father, not for Christ. From line 5 the folio
> returns to the road, and lines 6–9 are Luke 24:28–29, *he made as though he
> would have gone further, but they constrained him*: the long way, the
> persuading, and the sitting down at table.

## 063r — the breaking of bread, and he vanished out of their sight

**1**  the apostles carried, the rest, cup, water and wine, and.
`carry apostle the_rest^ cup ~water and wine and.`

**2**  Lord Jesus took one cup and cup
`grab Lord-Jézus one [?] and [?]`

**3**  [he blessed] this, how, then [vanished] alone […]
`[he_blessed] this how? then [vanished] °alone-[?]`

**4**  and from […] today's, and wine, and the cloud
`and from [?]-today’s and wine and cloud`

**5**  the Lord Jesus blessed; and then the other apostles | ate, the two
`bless Lord-Jesus and then the_rest^ apostle | eat-two`

**6**  apostles; and the two apostles drank in the place; the two apostles recognized [him].
`apostle and drink-two-apostle on-place recognize-two-apostle`

**7**  in the Holy Spirit, the farm, truly the Son of God
`on-spirit holy-farm +<subject_marker> righteous(ly) son God`

**8**  to the Lord Jesus; the other apostles, of, to leave this, and
`to Lord-Jesus the_rest^ apostle of-to-leave-this and`

**9**  left among the other apostles, the Lord Jesus Christ, the chapter answered
`leave among the_rest^ apostle Lord-Jesus-Christ chapter-?answered`

**10**  to the Lord [vanished] the two apostles saw. Here ends this holy gospel.
`Lord-to [?] see-two-apostle end this holy-gospel`

> Luke 24:30–31: *he took bread, and blessed it, and brake, and gave to them.
> And their eyes were opened, and they knew him; and he vanished out of their
> sight.* Line 8 has the leaving. The daily bread of line 4 is the same word
> the codex uses in the Our Father.

## 063v — Thomas was not with them

**1**  Here begins this holy gospel
`begins this holy-gospel`

**2**  written by holy John
`write holy-John`

**3**  within the twentieth chapter
`within^ two-ten-ten chapter`

**4**  of his writing. At that time
`<preposition_of_genitive>-write time`

**5**  the disciples met within Jerusalem
`meet disciple^ within^ Jerusalem`

**6**  in one house, six
`inside [?] house six`

**7**  in the Lord's house, where the Lord
`inside Lord house where Lord-<suffix_of_divine_name>`

**8**  Lord Jesus, after supper; and then holy Thomas went Didymus
`Lord-Jézus dinner ?afterward and then-exist go holy-Thomas [?]`

**9**  one Saturday evening, to the apostles; and the apostles said, Thomas, apostle,
`one Saturday evening to-apostle and say-apostle Thomas apostle`

**10**  we have seen the Lord. And holy Thomas said, I do not believe this
`see Lord and say holy-Thomas this-Thomas this not believe`

**11**  every [one]; if this, if Thomas believes this, if not | see
`every this if this-Thomas this believe if not | see`

**12**  Thomas, the Lord's side; and unless Thomas puts his finger within | of
`Thomas of-Lord side^ and of-Thomas finger not put within^ | of`

> John 20:24–25. *Except I shall see in his hands the print of the nails, and
> put my finger into the print of the nails, I will not believe.*

## 009r — reach hither thy finger, and my Lord and my God

**1**  the Lord's side, who from the Lord, rose from the dead; at that time stood the Lord Jesus Christ
`Lord side^ who from Lord from die stand_up time stand^ Lord-Jesus-Christ`

**2**  in the midst of the disciples, closed, and said: peace [be] you; and in joy [they] stood.
`middle disciple^ closed and say peace^ you exist and joy stand^`

**3**  the apostles in turn; Thomas began have and Lord Jesus said, Thomas,
`apostle in_turn Thomas begin [?] and say Lord-Jézus Thomas`

**4**  thou shalt go to put thy finger, Thomas, into the Lord's wound
`go-?shall to put <preposition_of_genitive>-Thomas finger inside <preposition_of_genitive>-Lord wound`

**5**  [blessed] see and believe; and [have not] Lord Jesus, the Lord's wound
`[?] see believe and [?] Lord-Jézus <preposition_of_genitive>-Lord wound`

**6**  And the Lord Jesus said: Thomas, happy from, and somebody sees
`and say Lord-Jesus Thomas happy from and somebody see`

**7**  and believes; but and happy from, and not see,
`and believe but and happy from and not see`

**8**  but believe. Here ends this holy gospel. And he knelt,
`but believe here_ends this holy_gospel and kneel`

**9**  holy Thomas, before Lord Jesus, and holy Thomas said, Lord,
`holy-Thomas before Lord-Jézus and say holy-Thomas Lord`

**10**  Thomas's God; Thomas asked the divine one:
`of-Thomas God of-Thomas ask-Thomas he-DIV`

**11**  have mercy on Thomas, who, this Thomas, committed sin against the divine one.
`have_mercy Thomas who this-Thomas commit sin against he-DIV`

> John 20:26–29. Line 4 is *reach hither thy finger*, line 6 is *blessed are
> they that have not seen, and yet have believed*, and lines 9–10 are *My Lord
> and my God*, which the codex renders as Thomas's Lord and Thomas's God
> because of the rule that a name sign stands in for the pronoun.

## 009v — Thomas blesses him, and the Good Shepherd begins

**1**  this Thomas, he believed; Thomas remained; he truly
`this-Thomas he believe-Thomas remain* he righteous`

**2**  the Son of the living God. And then Thomas was blessing the Lord Jesus Christ.
`son living God and then Thomas exist bless Lord-Jesus-Christ.`

**3**  And Thomas's sin find mercy. And the Lord Jesus said: every [my] and [God] [my] from
`and sin Thomas find_mercy^ and say Lord-Jesus every [my] and [God] [my] from`

**4**  [that day] on believing in the Lord Jesus Christ, every heathen man, Jew,
`[that_day] on-believe to-Lord-Jesus-Christ every heathen man^ Jew`

**5**  pagans' sin find mercy [on his] side. This apostle's holy gospel; bless the Lord God.
`pagans sin find_mercy^ side^ this apostle holy-gospel on-Lord_God bless`

**6**  Here ends this holy gospel.
`end this holy-gospel`

**7**  Written by holy John
`write holy-John`

**8**  in the tenth chapter of his writing.
`inside ten chapter <preposition_of_genitive>-write`

**9**  At that time Lord Jesus said
`time say Lord-Jézus`

**10**  […] supper, apostles,
`[?] dinner apostle`

**11**  of the Lord: I, the good shepherd; in turn you, from the apostles
`of-Lord I good shepherd in_turn you from apostle`

> Thomas's confession, *my Lord and my God*, John 20:28, then the book turns
> to John 10, the Good Shepherd.

## 064r — the good shepherd and the hireling

**1**  his sheep, and the Lord knows his sheep, and
`<preposition_of_genitive>-Lord sheep and Lord ~know <preposition_of_genitive>-Lord sheep and`

**2**  I know the Lord's sheep. And then the Lord Jesus: | then
`I ~know of-Lord sheep and_said Lord-Jesus | then`

**3**  there was a king, and then he had two shepherds,
`exist one king and then-exist ~have two ?sons`

**4**  one who [kept] the home well, the shepherd; the second, a labourer.
`one ~who home good shepherd second labourer`

**5**  shepherd. And then, of the two shepherds […] from one
`?sons and then-exist from two ?sons chapter-[?] from one`

**6**  herd of sheep of this king; and then came the wolf
`herd sheep this king and then-exist go wolf`

**7**  to this sheep, and would carry this sheep away
`this sheep and want this sheep from-~carry`

**8**  and this hired shepherd, of the shepherds leave
`and this farm_hand ?sons from ?sons [?]`

**9**  this sheep; in turn this good shepherd, the home, from the shepherd
`this sheep in_turn-this good shepherd home from shepherd`

**10**  redeemed this sheep; and the sheep follow within the herd.
`redeem this sheep and sheep follow inside herd`

**11**  and within, good, before, [he] gives; and one carries away; and
`and inside-good-before give^ and one carry_away and`

> John 10:11–13, told as a parable of a king with two shepherds, one his own
> and one hired. The wolf comes, the hireling flees, the good shepherd
> redeems the sheep.

## 064v — the good shepherd giveth his life, and other sheep I have

**1**  if [he does] not leave, out [of] this herd, and go.
`if not_leave out this herd and go.`

**2**  The wolf, and the sheep carried away. And then
`wolf and sheep carry_away and_said`

**3**  Lord Jesus: he who is the good shepherd, of the shepherds, lays
`Lord-Jézus to-+he_who good ?sons from ?sons put`

**4**  down the Lord's life for the Lord's sheep; and the Lord takes
`down of-Lord life to-of-Lord sheep and grab-Lord`

**5**  and one [fold] he who is the good shepherd, of the shepherds,
`and one [?] +he_who good ?sons from ?sons`

**6**  <subject marker> the gate of the Lord's sheep; and then [they] hear
`SUBJ gate of-Lord sheep and then hear`

**7**  the voice of the Lord God; the sheep, blind, the Lord, the shepherd, go. And then
`voice of-Lord_God sheep ~blind-Lord shepherd go and_said`

**8**  the Lord Jesus, the Lord's apostles, […] by night, one sheep
`Lord-Jesus apostle of-Lord [...] [?]-°by_night one sheep`

**9**  and these sheep I will bring to you blind and go
`and this-sheep will to-you [?] go and`

**10**  you shall be every one, one shepherd, shepherds
`you exist each,_every one ?sons ?sons`

**11**  one; thanks to the Lord. Here ends this holy gospel.
`one to-Lord thanks Lord-<suffix_of_divine_name> end this holy-gospel`

> John 10:11–16. Line 3 is *the good shepherd giveth his life for the sheep*,
> line 6 is *I am the door of the sheep*, line 7 is *they hear his voice*, and
> lines 8–10 are *other sheep I have... and there shall be one fold, and one
> shepherd*.

## 065r — beware of false prophets

**1**  Here ends this holy gospel.
`end this holy-gospel`

**2**  Written by holy Matthew
`write holy-Matthew`

**3**  in the last of his writing.
`inside ?the_last <preposition_of_genitive>-write`

**4**  time | then
`time | then`

**5**  of the day of Lord Jesus Christ,
`+day Lord-Jézus-Christ`

**6**  thirty, three days.
`thirty +three_days`

**7**  At that time Lord Jesus said
`time say Lord-Jézus`

**8**  to the Lord's apostles: [they] go to you in sheep's clothing
`apostle of-Lord go to-you in_sheep's clothing`

**9**  false prophets, pagan, evil [clothing] they are pagan
`false prophet pagan evil [?] exist pagan`

**10**  evil, the Lord's trespass [ravening wolves] mouth the apostles, men,
`evil trespass Lord [?] [?] apostle somebody`

**11**  and pagan, evil clothes, because they are false | of
`and pagan evil clothes^ because exist false | of`

> Matthew 7:15, *beware of false prophets, which come to you in sheep's
> clothing.* The codex has put it straight after the Good Shepherd, which is
> where the sheep's clothing belongs.

## 065v — by their fruits ye shall know them

**1**  confess the Lord's name. And then the Lord Jesus, the Lord's apostles:
`Lord name confess and_said Lord-Jesus apostle of-Lord`

**2**  verily verily I speak to you. And then
`verily verily I you speak and_said`

**3**  the Lord Jesus: do not pick figs from thistles, but on the fig; and | do not pick
`Lord-Jesus pick_not fig on-thistle ~but on-fig and | pick_not`

**4**  food, grapes from the thornbush, but on the grapevine,
`food grape thornbush* ~but on-grapevine`

**5**  because who [is] a good tree takes this good fruit; | in turn
`because who good tree this good_fruit grab | in_turn`

**6**  if dying, the evil tree takes this bad fruit.
`~if die-evil tree this bad_fruit grab`

**7**  Because a good tree can take bad fruit, but
`because good tree can bad_fruit grab ~but`

**8**  every good fruit it takes; if a bad tree
`every good_fruit grab ~if bad tree`

**9**  can take good fruit, but every bad fruit
`can good_fruit grab ~but every bad_fruit`

**10**  it takes. And then the Lord Jesus: many people were shouting | on the judgment
`grab and_said Lord-Jesus many people exist shout | on-judge`

**11**  the Lord's year, to the Lord; this man's trespass; this the Lord preached, and Lord Jesus said
`year Lord to-Lord this somebody trespass this Lord preach and say Lord-Jézus`

> Matthew 7:16–20. *Do men gather grapes of thorns, or figs of thistles?* on
> lines 3–4, and the good tree and the corrupt tree on lines 5–9, in the same
> order as the gospel.

## 066r — the weeping and gnashing of teeth

**1**  and [whosoever], the man, can say: Lord, go, Lord God; the Lord creates | of
`and [whosoever] man^ can-say-Lord go Lord_God Lord create | of`

**2**  the man, and the Lord saved every one, Adam gained, this man
`somebody and +be_saved Lord each,_every ~Adam gain this somebody`

**3**  [shall enter] the year out, the man chapter of his Father, and this man
`[?] out(ward)-year somebody [?] <preposition_of_genitive>-Lord father-<suffix_of_divine_name> and this somebody`

**4**  everybody [shall enter] into [many] heavenly homes of the Lord,
`everybody = [shall_enter] inside [many] heavenly home of-Lord`

**5**  God the Father; but every [one] goes, the man, to ever-ever hell
`God_the_Father but every go man^ on-ever ever hell`

**6**  fire; there is seen the grinding of teeth, weeping,
`fire there exist see grinding tooth weep`

**7**  for ever and ever; in turn, and the man is [not] the man
`for_ever_and_ever = in_turn and man^ exist [not] man^`

**8**  [who] says three [times]: Lord, Lord, Lord; saved [by] the Lord, all the world; this man
`say three Lord-chapter-Lord-chapter-Lord be_saved Lord every world this man^`

**9**  every [one] goes into [many] heavenly homes of the Lord, God the Father; there
`every go inside [many] heavenly home of-Lord God_the_Father there`

**10**  is the man's joy, to the Lord, and the angels, and the Lord's Father
`exist man^ joy to-Lord and angel and of-Lord-father`

**11**  God, for ever and ever, amen. Here ends this holy gospel.
`God for_ever_and_ever = amen here_ends this holy_gospel`

> Matthew 8:12, *there shall be weeping and gnashing of teeth*, set against
> *in my Father's house are many mansions*, John 14:2, which is where the
> next folio begins.

## 066v — whatsoever ye shall ask the Father in my name

**1**  Here begins this holy gospel
`begins this holy-gospel`

**2**  written by holy John
`write holy-John`

**3**  in the fourteen-and-one chapter of his writing.
`fourteen-+one chapter of-write`

**4**  At that time Lord Jesus said
`time say Lord-Jézus`

**5**  to his apostles, at the last supper,
`apostle <preposition_of_genitive>-Lord on-last dinner`

**6**  verily verily I speak to you: love.
`verily verily I you speak love`

**7**  Whatsoever ye shall ask of the Lord's Father
`whatever you exist ~ask_(for) from <preposition_of_genitive>-Lord-from father-<suffix_of_divine_name>`

**8**  in the Lord's name, ye shall all receive it saved
`inside <preposition_of_genitive>-Lord +name each,_every you +be_saved grab`

**9**  from heaven, from I, Christ. And this said, spoke the Lord Jesus:
`from heavenly from I Christ and this say speak Lord-Jesus`

**10**  on the way, to his apostles, and said, O the Lord's son.
`on-way apostle <preposition_of_genitive>-Lord and say oh <preposition_of_genitive>-Lord son.`

> John 14:13–14, *whatsoever ye shall ask in my name, that will I do*, placed
> at the last supper as the gospel places it.

## 067r — whose son is he, and thou art the Son of the living God

**1**  I ask you: whose son? | you
`ask^ I you whose? son | ~you`

**2**  yours. To the Lord spoke the apostles, and the apostles said: Master, the apostle, this Lord
`yours to-Lord speak apostle and say apostle Master apostle this Lord`

**3**  believe that this Lord [sat] truly the Son of the living God. And
`believe [?] this Lord [?] righteous(ly) son living God and say`

**4**  the Lord Jesus: O the Lord's son, I cast this out.
`Lord-Jesus oh of-Lord son I this exorcise`

**5**  if you believe this, it is to the Lord
`if-to you this believe exist to-Lord`

**6**  I [am] truly the Son of the living God; mouth, who […] one | you
`I righteous son living God mouth-+who and [?]-+one | ~you`

**7**  yours, believe, brother, because I who go
`yours believe ~brother because I who-go`

**8**  to death, to the Lord's death, name […]; I ask you [shall be raised]
`on-die to-Lord-die name-[?] ~ask I you [shall_be_raised]`

**9**  in the Lord herd the apostles, because you are apostles, many sorrowing
`inside Lord [?] apostle because you exist apostle many sad(ly)`

**10**  you have on the Lord, because you apostles, all the apostles | learn, chapter
`on-Lord have because you apostle every apostle | learn-chapter`

**11**  [oh Lord] […] return, mourn, and to and one and
`[oh_Lord] [...] return mourn and to-and one and`

> Matthew 22:42, *what think ye of Christ? whose son is he?*, answered with
> Peter's confession from Matthew 16:16, *thou art the Christ, the Son of the
> living God*.

## 067v — he that believeth and is baptized shall be saved

**1**  one [died]; and I on the third day up.
`one [died] and I on_the_third_day up.`

**2**  stood up; and I, you, brother, within
`stand_up and I you ~brother inside`

**3**  belief did; believe there is
`believe ~do believe* exist`

**4**  leave for ever and ever, amen. And the two
`leave for_ever_and_ever = amen and two`

**5**  men [sendeth] you, and the apostles are one
`somebody [?] you and exist apostle one`

**6**  God; the apostles believe, and the man who is outside this believe
`God believe apostle and somebody exist out(ward) this [?]`

**7**  and one man is saved, but every man is damned
`and one somebody be_saved a) each,_every somebody be_damned`

**8**  and the man who believes in […] Christ, this
`~to and somebody exist believe inside [?]-~Christ this`

**9**  somebody is saved, because this [is] to the Lord, one God.
`somebody exist be_saved because this to-Lord one God`

**10**  Here ends this holy gospel. whatsoever the man has, he asks
`end this holy-gospel [?] have somebody ask_(for)`

**11**  in Jesus' name he is saved, speaks holy Paul the apostle
`inside Jézus +name be_saved speak holy-Paul apostle`

> Mark 16:16, *he that believeth and is baptized shall be saved; but he that
> believeth not shall be damned*, on lines 7–9, then the book turns to Paul.

## 068r — love the Lord, and thy neighbour as thyself

**1**  this word, Paul's brethren; Paul the man has, he asks
`this word brother <preposition_of_genitive>-Paul have somebody-Paul ask_(for)`

**2**  in Jesus' name; three things Paul the man asks; in turn
`inside Jézus +name +three ask_(for)-somebody-Paul | in_turn`

**3**  who wants, somebody, Paul, to be saved first; | somebody asks
`who want-somebody-Paul be_saved first | ask-somebody`

**4**  Paul: love the Lord God highest [above] all creation, and everybody as the neighbour
`Paul love Lord_God highest all^ create and everybody = as neighbour`

**5**  as the neighbour; and somebody is saved. The second has,
`to-+neighbour and exist somebody be_saved second have`

**6**  Paul the man asks, in Jesus' name go away
`somebody-Paul ask_(for) inside Jézus +name [?]`

**7**  believe; Paul the man asks of Lord Jesus, in his
`believe ask_(for) somebody-Paul from Lord-Jézus inside <preposition_of_genitive>-Lord`

**8**  name. The third Paul the man has, he asks, in
`and-to-end-+name +third have somebody-Paul ask_(for) | inside`

**9**  Jesus' name, saved by Lord Jesus, in his
`Jézus and-to-end-+name be_saved from Lord-Jézus inside <preposition_of_genitive>-Lord`

**10**  [believeth] name, and the man shall be saved. Here ends
`[?] and-to-end-+name and exist somebody be_saved end`

**11**  this apostle's holy gospel.
`this apostle holy-gospel`

> The great commandment, Matthew 22:37–39, attributed here to Paul and set
> out as three things asked in Jesus' name. The sign read here as *neighbour*
> was read from exactly this frame.

## 068v — of sin, and of righteousness, and of judgment

**1**  Here begins this holy gospel
`begins this holy-gospel`

**2**  written by holy John, in
`write holy-John inside`

**3**  the sixteenth chapter of his writing.
`ten-six chapter <preposition_of_genitive>-write`

**4**  At that time Lord Jesus said
`time say Lord-Jézus`

**5**  to his apostles, at the last
`apostle <preposition_of_genitive>-Lord on-last`

**6**  dinner: I go, the Lord, to the Lord's God the Father; you learn,
`dinner I go-Lord of-Lord God_the_Father you learn`

**7**  do, the heavenly land; that is, I leave
`do heavenly land that_is I leave*`

**8**  to death; the Lord dies; and I go [from] you | [the Paraclete]
`on-die Lord die and I you go | [the_Paraclete]`

**9**  the day; if I do not die, to you [he] does not go away
`day if I does_not die to you go_not_away`

**10**  the Holy Spirit. The Lord dies, and I [send to] you
`holy-spirit Lord die and I you`

**11**  the Holy Spirit goes, and you shall see two
`go holy-spirit and you exist see-two`

**12**  judgment: first, of sin; second, of righteousness; third, of judgment.
`judge first from sin second from righteous third judge`

> John 16:7–8, *it is expedient for you that I go away... and when he is
> come, he will reprove the world of sin, and of righteousness, and of
> judgment.* Line 12 has the three in the gospel's order, counted with the
> codex's own ordinals. Line 7 is Király & Tokai's *heavenly* (they cite
> 068v07), the same words as 080r04. Corrected 2026-09-26: the earlier
> printing, and Book One, read *heaven and earth* here.

## 069r — the Spirit, the tongues, and the signs

**1**  And then this Holy Spirit goes to you, from the Spirit
`and then-exist you go this holy-spirit from-spirit`

**2**  through it you receive humble every good thing, and there are
`through grab you [?] each,_every good and exist`

**3**  the apostles, new, new tongues say [truly]; you [shall] be many
`apostle new new language say [truly] you exist many`

**4**  miracles say which the mouth speaks in the Old Testament word, and it lives
`miracle [?] which-mouth exist inside <pertaining_to_the_Old_Testament> word and living exist`

**5**  goes before [all men]; baptize [until] doomsday.
`go before [all_men] ~baptize [until] doomsday`

**6**  because there are many miracles done. Here ends this holy gospel.
`because-exist many miracle ~do here_ends this holy_gospel`

**7**  Here begins this holy gospel
`begins this holy-gospel`

**8**  written by holy Luke, in the tenth
`write holy-Luke inside | ten`

**9**  the last chapter of his writing. Said
`?the_last chapter <preposition_of_genitive>-write say`

**10**  Lord Jesus to his apostles, at
`Lord-Jézus apostle <preposition_of_genitive>-Lord | on`

**11**  the last dinner: I [am] the grapevine; God the Father of the Lord <subject marker>
`last dinner I grapevine God_the_Father of-Lord SUBJ`

> Acts 2, the tongues and the signs, joined to the promise of the Spirit at
> the supper.

## 069v — I am the vine, ye are the branches

**1**  the vineyard; in turn you are the branches, and
`farm in_turn you vine_branch and go`

**2**  God the Father, the Lord's vineyard, the angel, the vine, this | name, Lord
`God_the_Father of-Lord farm angel vine* this | name-Lord`

**3**  the grapevine; and without the vine shoot | [nothing]
`grapevine and without vine_shoot | [nothing]`

**4**  name he takes this and cuts it off, and vine branch out
`[?] grab this cut_off and [?] out(ward)`

**5**  on the way cast out. And then the Lord Jesus: and the man who is
`~way cast_out and_said Lord-Jesus and man^ exist`

**6**  within the Lord, […] carried by the Lord, stays; and I am
`inside Lord-[?]-~carry-Lord stay and I exist`

**7**  within him. And then the Lord Jesus, the Lord's apostles: O | of
`inside him and_said Lord-Jesus apostle of-Lord oh | of`

**8**  the Lord's son, this keeping of the commandment of love; the apostles can [abide]
`Lord son this keeping_the_commandment_of_love can apostle [abide]`

**9**  understand, who, I, you, [bear fruit] | speak
`understand who I you [bear_fruit] | speak`

**10**  Lord; and the man who is in the Lord's commandment of love, the man carries, from
`Lord and somebody exist <preposition_of_genitive>-Lord commandment-love carry-somebody from`

**11**  the man who is within the Lord's commandment […] stays, and I
`man^ exist inside Lord-commandment-[?] stay and I`

> John 15:1–5. *I am the true vine, and my Father is the husbandman... ye are
> the branches... abide in me.* The vineyard is the codex's word for the
> husbandman's ground, and the cutting off on line 4 is John 15:2.

## 070r — the branch that beareth not is cast into the fire

**1**  the Lord is within him; the Lord Jesus said: who did
`exist-Lord inside him say Lord-Jesus who ~do`

**2**  to God the Father of the Lord, this vine shoot [withered] is | good
`to-God_the_Father of-Lord this vine_shoot [withered] exist | good`

**3**  the grape takes these vine shoots from the blind; the Father
`grape grab these vine_shoot from-~blind the_Father`

**4**  of the Lord, so that every grape carries; and the Lord's Father goes
`of-Lord so_that every grape carry and go father of-Lord`

**5**  two evil vineyards, and this in turn what vine branch
`two evil farm and this in_turn-what [?]`

**6**  takes the evil farm, and <subject marker> casts [it] out into hell
`grab evil farm and SUBJ cast_out on-hell`

**7**  fire; there is seen the grinding of teeth, crying, ever
`fire there exist see grinding tooth crying ever`

**8**  ever. And then the Lord Jesus: as the Father of the Lord
`ever and_said Lord-Jesus as the_Father of-Lord`

**9**  the Lord loves, and I love you. And the Lord Jesus said: O
`Lord love and I you love and say Lord-Jesus oh`

**10**  the Lord's son, and you love, because the disciples are loving
`of-Lord son and you love because-exist disciple^ love`

> John 15:6, *if a man abide not in me, he is cast forth as a branch... and
> men gather them, and cast them into the fire*, with the codex's own
> gnashing of teeth attached, then John 15:9, *as the Father hath loved me,
> so have I loved you.*

## 070v — ask in my name, and Paul's three askings again

**1**  within the commandment you are; the Lord's commandment of love the apostles carry
`inside commandment you exist of-Lord the_commandment_of_love carry-apostle`

**2**  Lord Jesus said, and the man who carries [in my name] […]
`say Lord-Jézus and somebody exist carry [?] [?]`

**3**  [must] you first say: love the Lord, whatever | you
`[must] you first say Lord love whatever | ~you`

**4**  [ye] shall ask the Father, from the Lord's Father, in
`exist ~ask the_Father from of-Lord the_Father inside`

**5**  the Lord's name, ye shall all receive it saved.
`<preposition_of_genitive>-Lord +name each,_every you be_saved grab`

**6**  Here ends this holy gospel. whatsoever the man has, he asks
`end this holy-gospel [?] have somebody ask_(for)`

**7**  in Jesus' name saved, speaks holy Paul the apostle
`inside-Jesus name be_saved speak holy-Paul apostle`

**8**  this word; Paul's brother has, somebody, Paul
`this word brother of-Paul have somebody-Paul`

**9**  asks in Jesus' name; three [things] asks somebody, Paul:
`ask inside-Jesus name three ask somebody-Paul`

**10**  if Paul the man would be saved, first he asks
`if want somebody-Paul +be_saved first ask_(for)`

> The ten commandments of love on line 1, then John 14:13 again, then the
> **same Paul passage as 068r, repeated almost word for word**. The codex
> reuses whole pericopes, which is what a preaching or lectionary collection
> does rather than a continuous narrative.

## 071r — the great commandment, repeated

**1**  somebody, Paul: love the Lord God, from the literal, [above] every creature, and everybody | how?
`somebody Paul love Lord_God from literal every create and everybody = | how?`

**2**  the neighbour […] and the man shall be saved.
`to +neighbour [?] and exist somebody +be_saved`

**3**  The second has somebody, Paul, asks within the Lord's | and
`second have somebody Paul ask inside of-Lord | and`

**4**  name: leave, believe; asks somebody, Paul:
`name leave believe ask somebody Paul`

**5**  of Lord Jesus, in the Lord's name. The third he has,
`from Lord-Jézus inside <preposition_of_genitive>-Lord +name +third have`

**6**  Paul the man asks in the Lord's name, saved
`somebody Paul ask_(for) inside <preposition_of_genitive>-Lord +name +be_saved`

**7**  by Lord Jesus, in the Lord's name; and
`from Lord-Jézus inside <preposition_of_genitive>-Lord +name and exist`

**8**  the man shall be saved. Here ends this apostle's holy gospel [amen]
`somebody +be_saved end this apostle holy-gospel [?]`

**9**  Here begins this holy gospel, written by
`begins this holy-gospel write`

**10**  holy Luke, in [fourteen] of
`holy-Luke inside [fourteen] | of`

**11**  his writing. Lord Jesus said to his apostles
`write say Lord-Jézus apostle <preposition_of_genitive>-Lord`

**12**  at the last supper: you shall be driven out
`on-last dinner you | chase`

> The second copy of the great commandment, running straight on from 070v.

## 071v — a woman when she is in travail hath sorrow

**1**  the Jews out, on hearing; how one had mercy, the apostle believes, every
`Jews out on-hear how? one have_mercy-apostle-~believe every`

**2**  for the Lord's name. And then you
`to-<preposition_of_genitive>-Lord +name and then-exist you`

**3**  they want to chase, the apostles say; this is it: out, who, apostle [by] apostle
`chase want apostle say this_is ~out who apostle-apostle`

**4**  Master spoke and the Lord, the Jews put to death; and you
`Master [?] and Lord Jew(ish) die and you`

**5**  shall be many sad on the Lord, have; in turn, one, the Jews are
`exist many sad on-Lord have in_turn one Jews-exist`

**6**  joy [shall be turned]; your sorrow is, and ascends until
`joy [shall_be_turned] you sad exist and-ascend ~until`

**7**  little, how? then one woman, the head,
`little how? then one woman head`

**8**  a son is born, remains many sufferings, has; in turn, | then
`son be_born remain* many suffering have in_turn | then`

**9**  the son is born, and of that comes joy over the son
`exist be_born from-~exist on-son joy this-Peter`

**10**  and you sad; in turn the Jews joy want; many sad
`and ~you sad in_turn-Jews joy want many sad`

**11**  cast out, and that in the year of judgment; in turn your sorrow, much
`~out(ward) and [?] on-judge-year in_turn you sad(ly) many`

**12**  joy cast out, and that in the year of judgment. Here ends this holy gospel.
`joy ~out(ward) and [?] on-judge-year end this holy-gospel`

> John 16:2, *they shall put you out of the synagogues*, then John 16:21,
> *a woman when she is in travail hath sorrow... but as soon as she is
> delivered of the child, she remembereth no more the anguish, for joy that a
> man is born into the world.* Lines 7–10 have the whole figure.

## 072r — after the crucifixion, they sit at meat in Jerusalem

**1**  Here begins this
`begins this`

**2**  holy gospel, written by
`holy-gospel write`

**3**  holy Mark, within | the other
`holy_Mark inside | the_rest^`

**4**  twenty-fifth chapter
`ten-ten five chapter`

**5**  of his writing. At that time,
`<preposition_of_genitive>-write time`

**6**  then, after the crucifixion
`then-exist on-execute`

**7**  of Lord Christ […] at that time then
`Lord-Christ [?]-+day time then-exist`

**8**  the apostles sat at table in Jerusalem, in the Lord's house, where the Lord
`sit apostle [?] inside Jerusalem inside Lord house where Lord-<suffix_of_divine_name>`

**9**  Lord Jesus made the supper; at that time he appeared, the Lord
`Lord-Jézus dinner do, time appear | Lord`

**10**  Jesus, to his apostles, within, by name, somebody; and.
`Jesus apostle of-Lord inside ~brother-+name somebody and.`

**11**  he sat with the apostles at table and began to rebuke their unbelief
`sit to-apostle [?] and begin-admonish on-believe`

> Mark 16:14, *afterward he appeared unto the eleven as they sat at meat, and
> upbraided them with their unbelief.*

## 072v — go ye into all the world, he that believeth and is baptized

**1**  and Lord Jesus said, go ye, apostles, among the people, and
`and say Lord-Jézus you go apostle ?among_the_people and`

**2**  is baptized in the Lord's name; and somebody
`exist baptize inside of-Lord name and somebody`

**3**  who is baptized in the name of the Father and the Son
`exist baptize inside +name father-<suffix_of_divine_name> and son`

**4**  and the Holy Spirit, and believes in the Lord,
`and holy-spirit and exist Lord-to believe`

**5**  every such man shall be saved; and one is damned [but]
`everybody = be_saved and one be_damned [but]`

**6**  [but] and somebody [is] not baptized, and is [for] the Lord
`[-but] and somebody not baptize and exist Lord-to`

**7**  and one be saved but every man
`believe and one [?] a) each,_every somebody`

**8**  is damned [but] [but]; and the man who believes in the Lord
`be_damned [but] [-but] and somebody exist Lord-to believe`

**9**  shall do many miracles, all in the Lord's
`from exist many miracle do, each,_every inside <preposition_of_genitive>-Lord`

**10**  name; the man in the Lord's […]
`+name exist somebody inside <preposition_of_genitive>-Lord | and-exist`

**11**  […] name: the blind through light; the dead, somebody resurrects, rise.
`[?]-+name ~blind through light die somebody resurrect rise^`

> Mark 16:15–16, *go ye into all the world... he that believeth and is
> baptized shall be saved; but he that believeth not shall be damned*, with
> the baptismal formula of Matthew 28:19 folded into it.

## 073r — and these signs shall follow them that believe

**1**  the man in the Lord's name, the evil in
`exist somebody inside <preposition_of_genitive>-Lord +name evil inside`

**2**  the man casts out; he carries serpents in
`somebody exorcise exist serpent carry inside`

**3**  the hand, is somebody not bitten; is somebody in
`hand ~exist somebody not bite exist somebody inside`

**4**  the Lord's name deadly poison drink and whatever
`<preposition_of_genitive>-Lord +name [?] [?] and what-to`

**5**  who, somebody, is well; is somebody within the Lord's
`who somebody ~exist well exist somebody inside of-Lord`

**6**  name, on the cup […] year, our hands put
`name on-cup-[?]-~year our hands put`

**7**  this, sat, <subject marker> is somebody healed, all in the Lord's
`this-°sat-+SUBJ exist somebody heal every inside of-Lord | and-exist-from`

**8**  name; the man does many miracles, and
`+day-+name exist somebody many miracle do, and`

**9**  The Lord Jesus said: I go to the Lord's Father, to you
`say Lord-Jesus I go to-of-Lord the_Father to-you`

**10**  the Lord, and the Lord God <subject marker> the Lord goes, and I go to you, the Lord
`Lord and Lord_God SUBJ Lord go and I you go-Lord`

**11**  the Holy Spirit; and the apostles are new, new tongues.
`holy-spirit and exist apostle new new language`

> Mark 16:17–18, sign for sign and in order: *in my name shall they cast out
> devils; they shall speak with new tongues; they shall take up serpents; and
> if they drink any deadly thing, it shall not hurt them; they shall lay
> hands on the sick, and they shall recover.* The cup on line 6 is the deadly
> draught.

## 073v — he went on the way, and each time he said the same

**1**  say and Lord Jesus said to his apostles, go, apostles today
`[?] and say Lord-Jézus apostle <preposition_of_genitive>-Lord go-apostle [?]`

**2**  the mount; I want, the Lord, out truly, and all the world, the Lord's | from
`mount I want-Lord ~out righteous and all_the_world of-Lord | from`

**3**  God the Father; and passing, the Lord went from the apostles; in turn the apostles to the Lord went, the apostles
`God_the_Father and trespass go-Lord from apostle in_turn apostle to Lord go apostle`

**4**  and then, from seeing, the Lord [said to the] learners, and said, the Lord: peace [be] you
`and then from-see-Lord learn and say-Lord peace you`

**5**  and then passing, the Lord went [on] the way; and a second time, from seeing, the Lord [said to the] learners
`and then trespass go-Lord ~way and two from-see-Lord learn`

**6**  and said, the Lord: peace [be] you; and then passing, the Lord went | on
`and say-Lord peace you and then trespass go-Lord | on`

**7**  the way; in turn the apostles to the Lord, on Monday, the apostles; and a third time, from seeing, the Lord [said to the] learners
`~way in_turn apostle to Lord Monday-apostle and three from-see-Lord learn`

**8**  and said, the Lord: peace [be] you; and then passing, the Lord went
`and say-Lord peace you and then trespass go-Lord`

**9**  the way; and a fourth time, from seeing, the Lord [said to the] learners, and said, the Lord: peace | you
`~way and two-two from-see-Lord learn and say-Lord peace | ~you`

**10**  […] and then the Lord passed on the way; and a fifth time
`[?] and then-exist trespass go-Lord on-~way and +five | from`

**11**  seeing, the Lord [said to the] learners, and said, the Lord: I [give] you peace; the eye
`see-Lord learn and say-Lord I you peace eye`

> A numbered sequence of five, each ending in the same formula, counted with
> the codex's own ordinals: second, third, fourth, fifth. This is the shape of
> a devotional list rather than a gospel passage, and the repeated greeting
> reads as *peace be unto you*.

## 074r — he was received up into glory

**1**  to the Lord's sufferer, and the Lord's Father, for ever and ever.
`to-sufferer of-Lord and of-Lord the_Father for_ever_and_ever =`

**2**  amen; because Lord Jesus would have him confess
`amen because want Lord-Jézus to-Lord confess have`

**3**  before the Father of the Lord, in the year of judgment; then
`before the_Father of-Lord on-judge-year then`

**4**  the Father goes to judge the living and the dead, the man; and the Lord said to the apostles,
`go father-<suffix_of_divine_name> judge living and die somebody and say-Lord apostle`

**5**  ye shall hear; his mother, and
`you exist hear <preposition_of_genitive>-Lord mother and`

**6**  Mary blessed upon all the apostles, and among this earth
`Mary bless on-each,_every apostle and among this [?]`

**7**  [after] to the Lord Jesus; and [taken up] the Lord Jesus | remained
`[after] to Lord-Jesus and [taken_up] Lord-Jesus | remain*`

**8**  sun went sky and blessed all the whole wide world
`[?] go [?] and bless each,_every the_whole_wide_world ?world`

**9**  and the Lord was taken to heaven's glory. At that time said | Saint
`and Lord take^ to-heaven glory* time say | saint^`

**10**  Peter: Master, how has he apostles pray, say
`Peter Master how? he have apostle pray say`

> Mark 16:19, *he was received up into heaven*, with the creed's *judge the
> quick and the dead* on line 4.

## 074v — the Lord's Prayer

**1**  the Lord Jesus, this the Lord's son: pray, God the Father, ours
`Lord-Jesus this of-Lord son pray God_the_Father our`

**2**  and the Lord in heaven, hallowed [be] the name of God the Father; the man goes
`and-Lord inside heaven be_hallowed^ name of-God_the_Father go man^`

**3**  into the Father's kingdom; the whole wide world is the Lord's, as in heaven
`inside king <preposition_of_genitive>-father-<suffix_of_divine_name> exist the_whole_wide_world <preposition_of_genitive>-Lord how? +heaven`

**4**  this, and on earth, our bread every day
`this and ~earth bread our every day^`

**5**  the Lord takes, man, today's day [for] us; trespass
`grab-Lord man^ today’s day^ us trespass`

**6**  forgive, as the man forgives our debtors.
`forgive^ as man^ forgive^ our debtors`

**7**  lead us into temptation; redeem from evil. Amen.
`lead us into temptation redeem from evil amen`

**8**  Written by holy Matthew in his gospel. And the second time said
`write holy-Matthew inside <preposition_of_genitive> gospel and two say`

**9**  holy Peter: Master, Lord, when shall be pass
`holy-Peter Master Lord when? exist [?]`

**10**  the year of judgment? Lord Jesus Christ said or out and out
`judge-year say Lord-Jézus-Christ [?] out(ward)-out(ward)`

> **The Lord's Prayer**, Matthew 6:9–13, and the codex says so on line 8.
> Hallowed be thy name, thy kingdom come, thy will be done in earth as it is
> in heaven, give us this day our daily bread, and forgive us our trespasses
> as we forgive them that trespass against us, and deliver us from evil.
> Amen. The word rendered *year* on lines 4–5 is the same root the dictionary
> gives as day or year, so *this day's bread* is the daily bread.

## 075r — two men in white apparel

**1**  in turn not fulfilled, two thousand years. And the third said holy Peter:
`in_turn not_fulfilled two-to-?thousand-year and three say holy-Peter`

**2**  Master, how shall the apostles good news write of the Lord? Lord Jesus said, one
`Master how? apostle [?] Lord write say Lord-Jézus one`

**3**  year write, apostles, literally; in turn the second, figuratively. And then
`year write apostle literal in_turn two metaphoric and then-exist`

**4**  the gate of heaven before the Lord Jesus; and then
`heaven gate before Lord-Jesus and then`

**5**  the Lord Jesus went into heaven's glory; and the Lord bright from
`go Lord-Jesus heaven glory* and Lord bright from`

**6**  left, because the Lord Jesus would like; then the Lord
`~leave because would_like^ Lord-Jesus then Lord`

**7**  the apostles glorified, shining on this world; and then the two
`apostle be_glorified shine on-this world and then-two`

**8**  appeared, two angels, white […]
`appear two angel-angel white | [?]`

**9**  believe. And then the two angels, angel [and] angel: you
`believe* and_said two angel-angel you`

**10**  men of Galilee, how see ye the Lord's joy? Jairus
`Galilee man how? Lord joy see Jairus`

> Acts 1:10, *behold, two men stood by them in white apparel.* Lines 2–3 are
> a note on how the apostles are to write: one literally, the other
> figuratively, which is a commentator's remark, not a gospel verse.

## 075v — he shall so come, to judge the quick and the dead

**1**  left from heaven, land, this joy.
`~leave from_heaven* land this joy`

**2**  the Lord would like to go on doomsday, to judge the living and the dead.
`would_like^ Lord go on_doomsday judge living and die`

**3**  the man. And the two said, these two angels, go, apostles, into
`somebody and say-two this two angel-angel go-apostle inside`

**4**  Galilee; and the Lord met the apostle somebody.
`Galilee and Lord meet apostle-somebody.`

**5**  And [gazing] they saw; the word was done by the two
`and [gazing] see word do two | angel`

**6**  angels. Here ends this holy gospel. Love the Lord with all thy heart.
`angel end this holy-gospel +the_Lord love Lord-<suffix_of_divine_name> ?with_all_thy_heart`

**7**  The Lord spoke, the apostles, Lord Jesus Christ;
`speak-Lord apostle Lord-Jézus-Christ`

**8**  then the apostles prayed,
`then-exist apostle pray`

**9**  his son,
`<preposition_of_genitive>-Lord son`

**10**  this Our Father
`this Our_Father`

> Acts 1:11, *this same Jesus... shall so come in like manner*, with the
> creed's *judge the quick and the dead* on line 2.

## 076r — how oft shall my brother sin against me

**1**  [afterward] to the apostles many said say written [holy Paul] apostolic letter
`[?] to-apostle many say [?] write [?] [?]`

**2**  in the first chapter of his writing. At that time, then, the Lord Jesus Christ
`inside one chapter of-write time then Lord-Jesus-Christ`

**3**  in the thirtieth year, and three days, and five months, and three days, at
`inside thirty year and +three_days and +five moon and +three_days inside`

**4**  time, the apostles left, under the Lord Jesus; and then holy Peter:
`time leave apostle under Lord-Jesus and_said holy-Peter`

**5**  Master, the high will this Peter forgive [how often]? is Peter
`Master want-high this-Peter forgive^ [how_often] exist Peter`

**6**  [then]. And then the Lord Jesus Christ: Peter, Peter, | in turn
`[then] and_said Lord-Jesus-Christ Peter Peter | in_turn`

**7**  who one […] dry, one year, commits sin, somebody
`who one-[?] dry* one year commit sin somebody`

**8**  against this Peter; forgive, the man <subject marker>, if the man goes to mercy,
`against this-Peter forgive^ somebody SUBJ if go somebody-have_mercy`

**9**  asks mercy, the man receives sun goes
`ask_(for)-have_mercy-somebody +<subject_marker> grab [?] go`

**10**  […] the man of mercy; and cried to Lord Jesus Christ
`[?] somebody-have_mercy and shout-to Lord-Jézus-Christ`

> Matthew 18:21, *Lord, how oft shall my brother sin against me, and I
> forgive him?* The dating on line 3 is the codex's own, not the gospel's.

## 076v — the catalogue of sins

**1**  stopped on the water of heaven [high] Peter, Peter, if, but rather
`stop on-water heaven [high] Peter Peter if-°but_rather`

**2**  a man among the apostles sins against you witness from
`+<subject_marker> somebody among apostle you sin [?] from`

**3**  […] the man, the apostle, the sin […] […] the man, of
`[?] somebody apostle +sin [?] [?] somebody | <preposition_of_genitive>`

**4**  somebody's sin, leave [it]; but if many [are] somebody's sins, in turn
`somebody-~sin leave but if many somebody-~sin in_turn`

**5**  a thief; in turn a robber; in turn a blood murderer; that is,
`thief in_turn robber in_turn blood murderer that_is`

**6**  a killer of men; the man in turn [adulterer]; the man in turn from [thief]
`people-die somebody in_turn [?] somebody in_turn from [?]`

**7**  the man in turn proud; the man in turn a drinker; the man in turn many
`somebody in_turn proud somebody in_turn drink somebody in_turn many`

**8**  [proud]; the man in turn under many yokes; this Peter
`[?] somebody in_turn many yoke-chapter somebody this-on-Peter`

**9**  said Lord Jesus Christ, because Peter is [pride] in turn in humble
`say Lord-Jézus-Christ because exist Peter [?] in_turn inside [?]`

**10**  the man, this be damned how then the man dies in turn
`somebody this [?] how? then-exist somebody die in_turn`

> A list of sins built on the repeated *in turn*: thief, shedder of blood,
> manslayer, proud, drunkard. Catalogues like this belong to the confessional
> handbook rather than to the gospel.

## 077r — one sin, and whosoever sins is damned

**1**  Adam the man penance have mercy; the man in turn from riches [forgiven]
`[?] somebody [?] have_mercy somebody in_turn from-rich-from [?]`

**2**  the man in turn penance truly; the man, or the man judges
`somebody in_turn [?] righteous(ly) somebody or ~judge somebody`

**3**  of whom holy Paul speaks apostolic letter said Lord Jesus Christ, this [forgive]
`who speak holy-Paul [?] say Lord-Jézus-Christ this [?]`

**4**  the man sins one sin penance he is saved; and he who hides
`somebody sin one +sin [?] be_saved and who-hide_oneself`

**5**  the man [seventy times seven] heavenly in sin, to Lord Jesus Christ
`somebody [?] [?] on-sin to Lord-Jézus-Christ`

**6**  one sin, penance, saved; but every sinner is damned.
`one sin penance* be_saved but every sinner be_damned`

**7**  said Lord Jesus Christ: Peter, Peter [if he hear thee not] that is [church]
`say Lord-Jézus-Christ Peter Peter [?] that_is [?]`

**8**  a sinner, not an apostle, this sinner, from a heathen witness
`sinner not apostle-this-sinner from heathen* witness*`

**9**  publican, the man, of […] leaves [as the heathen]
`publican* man^ of-[?] leave [as_the_heathen]`

**10**  the man [with one] voice [two or three]; who is the man, says the man, this
`man^ [with_one] voice [two_or_three] who-exist man^ say man^ this`

> Still Matthew 18, the sin of a brother and the forgiving of it.

## 077v — go to him alone, then take two, then three

**1**  he loves Lord Jesus Christ more than these. Lord Jesus Christ said to Peter:
`+<subject_marker> love Lord-Jézus-Christ ?more_than_these say Lord-Jézus-Christ to-Peter`

**2**  in turn [rebuke] the apostle-man among [alone]; the man who sins, go to
`in_turn [rebuke] apostle-somebody among [alone] somebody-~sin go | to`

**3**  Peter, […] the sin, to the house; and the man upon his sin
`Peter [?]-+sin to-home and somebody-on-+sin`

**4**  rebuke, because this somebody's sin, sufferer; in turn, to which, us,
`rebuke^ because this somebody-~sin sufferer in_turn to-which us`

**5**  sufferer, not a disciple, this sinner, from a heathen publican.
`sufferer not disciple^ this sinner from heathen* publican*`

**6**  from seeing the sinner, leave [him]; but Peter goes, to Peter, two
`from-see of-sinner leave but go-Peter to-Peter two`

**7**  […] sin; and somebody on sin rebuke, because this sinner,
`[?]-~sin and somebody-on-~sin rebuke^ because this sinner`

**8**  sufferer; in turn, to which, us, sufferer, not a disciple, this sinner
`sufferer in_turn to-which us sufferer not disciple^ this sinner`

**9**  from a heathen publican, the man; of the sinner leave [him]; but
`from heathen* publican* man^ of-sinner leave but`

**10**  Peter goes, to Peter, a third time […] the sin, and the man
`go Peter to-Peter +three [?]-+sin and somebody`

> Matthew 18:15–17, and the codex counts the three steps with its own
> ordinals: go alone first, then take two, then a third time. Line 1 is
> *lovest thou me more than these*, John 21:15, put in front of it.

## 078r — judge righteous judgment

**1**  on sin admonish, because this sinner, sufferer; in turn, to which, us,
`on-sin admonish because this sinner sufferer in_turn to-which us`

**2**  sufferer, take the sinner; take from [appearance] within
`sufferer grab sinner take* from [appearance] inside`

**3**  the hands; because this is right, right, to the sinner; because
`hands because this exist righteous righteous to-sinner because`

**4**  the false judge, according to [the law], judges somebody; the righteous judge
`false ~judge-somebody according_to* chapter-judge-somebody righteous judge`

**5**  but rather every [by appearance] false judgment; in turn the false judge
`?but_rather-each,_every [?] false judge in_turn false ~judge-somebody`

**6**  the righteous man falsely judged is damned; <subject marker> in hell
`righteous man^ false judge be_damned SUBJ inside hell`

**7**  <subject marker> for ever and ever; in turn the righteous judge, every
`SUBJ for_ever_and_ever = in_turn righteous ~judge-somebody every`

**8**  to whom he judges truly according to the judge falsely
`to-which-chapter righteous(ly) judge [?] judge-somebody false`

**9**  judging, but rather every [one] to which, righteous judge; the Lord God speaks every writing
`judge °but_rather-every to-which-chapter righteous judge Lord_God speak every write`

**10**  and every prophet and every church father and every forefather and evangelist
`and each,_every prophet and each,_every church_father and each,_every forefather and [?]`

> John 7:24, *judge not according to the appearance, but judge righteous
> judgment*, worked out at length against the false judge.

## 079r — the orders of angels, and one word

**1**  within all the world, to heaven's glory, highest, every angel, angel, angel, order
`inside every world to-heaven glory* highest every angel angel angel order`

**2**  [answered] eat literally, from the one Lord, truly somebody speaks holy Paul
`[?] eat literal from one Lord righteous(ly) [?] speak holy-Paul`

**3**  the apostolic letter, the brother of Paul: he, the righteous judge, the Lord Jesus Christ
`apostolic_letter brother of-Paul he righteous ~judge-+somebody Lord-Jesus-Christ`

**4**  he is judging all the world; one word [idle], word, every
`he exist judge every world one word [idle] word every`

**5**  somebody [give account] our righteousness, good, mercy, saying, love, doing; and
`somebody [give_account] our righteous-good-have_mercy-say-love-do and`

**6**  the Lord God takes <subject marker>; he, the righteous judge, and the Lord God every
`grab Lord_God SUBJ he righteous ~judge-+somebody and Lord_God every`

**7**  man receives [mercy] from the Lord [reward] the man
`somebody exist grab [?] exist from Lord-<suffix_of_divine_name> [?] somebody`

**8**  the firstborn is damned, to the brother [bosom], on Lazarus [rest]
`firstborn exist be_damned to-~brother [bosom] on-~Lazarus [rest]`

**9**  damned [torment] [everlasting] [fire] and nine [orders of angels]
`be_damned [?] [?] [?] and nine [?]`

> The nine orders of angels on line 1, which is Pseudo-Dionysius by way of
> every medieval preaching book, and the judgment of all peoples by one word.

## 080r — the Comforter, and the threefold reproof

**1**  Before the gospel: written by holy John, in the sixteenth chapter of his writing.
`before gospel write holy-John inside ten-six chapter <of>-write`

**2**  Already said the Lord Jesus [to] the Lord's disciples at the Last Supper: I
`already^ say Lord-Jesus teach^ of-Lord at_the_Last_Supper = I`

**3**  goes to his Father. You know that
`go-Lord <of>-Lord father-<divine> you learn do,`

**4**  the heavenly land; that is, I leave, to die; the Lord
`heavenly land that_is I leave* on-die Lord`

**5**  dies, and I go [from] you [to send] the Holy Spirit. | In turn,
`die and I you go holy-spirit | in_turn`

**6**  who, I; if [I] do not die, to you the Holy Spirit does not go away.
`who I does_not die to you go_not_away holy-spirit`

**7**  The Lord dies, and I go [from] you [to send] the Holy Spirit.
`Lord-die and I you go holy-spirit`

**8**  and you shall see two judgments: the first, of sin;
`and you exist see-two judge first from +sin`

**9**  the second, of righteousness; the third, judgment. And then you
`second from righteous third judge and then you`

**10**  receive this Holy Spirit; from the Spirit, through him, he takes you.
`go this holy-spirit from-spirit through grab you`

> John 16:7-13: "if I go not away, the Comforter will not come unto you; but
> if I depart, I will send him unto you. And when he is come, he will reprove
> the world of sin, and of righteousness, and of judgment ... he will guide
> you into all truth." The citation on line 1 is right. The two readings
> marked here, *go away* and *go not away*, sit where Király & Tokai's own
> apparatus puts a negated *go* on these very lines.

## 080v — the apostles wait in prayer with Mary

**1**  humble every good; and the disciples are new, new tongues say
`humble every good and exist disciple^ new new language say`

**2**  [truly] ye shall have many miracles, says the mouth
`[?] you exist many miracle say which-mouth-chapter-year`

**3**  in the Old Testament word, and it lives; go before [continuing], baptize
`inside Old_Testament word and living-exist go before [continuing] ~baptize`

**4**  [until] doomsday. Here ends this apostle's holy gospel. Begins
`[until] doomsday end this SUBJ apostle holy-gospel begins`

**5**  this holy gospel, written by holy Luke, in the second chapter of his writing. At that time,
`this holy-gospel write holy-Luke inside two chapter <preposition_of_genitive>-write time`

**6**  then, on the putting to death of the Lord Christ, forty years; and | then
`then on-execute Lord-~Christ forty_years and | then`

**7**  the Lord was forty years; at that time the disciples stood [in] prayer
`Lord-exist forty_years time stand^ disciple^ prayer^`

**8**  in the divine one's house, where the Lord God, the Lord Jesus, did the dinner; out
`inside divine_one^ house where Lord_God Lord-Jesus dinner do on-~out`

**9**  ten years; and then this went on ten years; at that time the apostles remained in
`ten-year and then-exist keep_going this ten-year time leave apostle on`

**10**  prayer; and holy Peter left, to the Virgin Mary. And then
`prayer^ and leave holy-Peter to Virgin_Mary and_said`

> Acts 1:14, *these all continued with one accord in prayer and supplication,
> with Mary the mother of Jesus.* The upper room is named as the place where
> the supper was made.

## 081r — the Spirit comes upon them

**1**  holy Peter, the wife, to the apostles: Master, speak to the apostles; the Lord is
`holy-Peter wife apostle-to Master speak to apostle exist-Lord`

**2**  from the sky goes the Holy Spirit; and Peter […] year, this
`from sky go holy-spirit and Peter [?]-~year this`

**3**  is. And then the Virgin Mary: then God the Father from the sky
`exist and_said Virgin_Mary then God_the_Father from sky`

**4**  the Holy Spirit goes; father Abraham, and Abraham
`go holy-spirit father Abraham and Abraham`

**5**  the spirit goes on the eleven, forty years, to the spirit
`spirit go on-ten-+one-forty_years to spirit`

**6**  and the apostles, Mary, find, go on this; said, said the Lord Jesus, God the Father of the Lord:
`and apostle-Mary find go on-this say say Lord-Jesus God_the_Father of-Lord`

**7**  I from the sky go, the Lord's brother, the Holy Spirit
`I from sky go of-Lord brother holy-spirit`

**8**  and the Lord's mother. And then God the Father: how, in what form would he like to go
`and of-Lord mother and_said God_the_Father how? form would_like^ go`

**9**  if he goes into God, the Son, the Spirit; the Lord, Father, Son, Holy Spirit
`if go inside God-son-spirit-Lord father son holy-spirit`

**10**  not suffer this world on the cross crucified. And then God the Father, | holy
`not_suffer this world on_the_cross crucify^ and_said God_the_Father | holy`

> Pentecost, Acts 2, with the eleven named on line 5 and the Trinity set out
> on line 9.

## 081v — cloven tongues like as of fire

**1**  the Spirit gave, on the spirit, the form of fire
`spirit give^ on-spirit fire form`

**2**  and the Spirit went out from the apostles, Mary, the Jews, and the man
`and go spirit from somebody-apostle-Mary-Jew(ish) and somebody`

**3**  this Spirit [filled] the apostles, the Jews; and it gave, on the spirit,
`this spirit [filled] apostle-Jew and give^ on-spirit`

**4**  the Spirit, the form of holy fire, and the Spirit went
`spirit holy-fire shape,_form and go-spirit`

**5**  out from the apostles, Mary, the Jews; and the man, the Spirit [filled]
`from somebody-apostle-Mary-Jew(ish) and somebody spirit [?]`

**6**  the apostles, Mary, the Jews, many; drink, year [cloven tongues]
`somebody-apostle-Mary-Jew many drink-~year [cloven_tongues]`

**7**  many a wind, in that form dove in fire
`many sough inside shape,_form [?] inside fire`

**8**  in that form; and the Jews saw this fire,
`inside shape,_form and see Jew(ish) this fire.`

**9**  that form, and it bowed on this house where the apostles and Mary
`form and bow on-this house where apostle-Mary`

**10**  at prayer. And then the Jews [said], the Jews, the head, that is,
`on-pray and_said-Jews Jew ~head that_is`

> Acts 2:2–3, *a rushing mighty wind... and there appeared unto them cloven
> tongues like as of fire, and it sat upon each of them.* The wind is on line
> 7 and the descent on the house on line 9.

## 082r — the Jews see it, and three thousand are added

**1**  the Lord, heretic; the apostles, every sough, and go to the Jews
`Lord heretic apostle every sough and go_to Jew`

**2**  saw it, because, by name, the Jews [under heaven], every sough; and | then
`on-see because ~exist-+name Jew [under_heaven] every sough and | then`

**3**  the Jews were […] in the house where the apostles and Mary were at
`exist Jew(ish) [?] inside house where apostle-Mary | on`

**4**  prayer to the sky, from the apostles and Mary at prayer; ascension
`prayer^ to sky from apostle-Mary on-pray ascension^`

**5**  the heavenly word; thanks, apostles and Mary, to the Lord; thanks, Lord God; and
`heavenly word thanks apostle-Mary to-Lord thanks Lord God and`

**6**  various tongues say. And then the Jews [were] blind to [it].
`various language say and_said Jew ~blind-to.`

**7**  these apostles; the sons of Jerusalem see how [they] tongues say. And then the apostles
`this-apostle Jerusalem son see how? language say and_said apostle`

**8**  are apostles, Master, from sky the Holy Spirit goes [amazed]
`+<subject_marker> exist apostle Master from [?] go holy-spirit [?]`

**9**  the apostles, one who [gave] food, went from the people; the Jews, three thousand
`apostle one-who food go from ~people Jew three_thousand`

**10**  the people received belief in Lord Jesus Christ, and every
`people-+day grab believe Lord-Jézus-Christ and each,_every`

> Acts 2:6–12, the crowd hearing them, and then Acts 2:41, *and the same day
> there were added unto them about three thousand souls*, which the next
> folio counts.

## 082v — three thousand added, and the Trinity begins

**1**  man, Jew, apostle, Mary, received the Holy Spirit; and two years, baptized, from
`somebody-Jew-apostle-Mary grab holy-spirit and two-year ~baptize from`

**2**  the Jews [received], and [baptized], baptized, three thousand, and
`Jew [received] and [baptized] ~baptize three_thousand and`

**3**  one […] son, seven sons; and from the son received holy
`+one-[?]-[?] ~son +seven ~son and from ~son grab | holy`

**4**  the soul proceeds on the spirit, the Holy Spirit, every | man, Jew,
`soul^ proceed* on-spirit holy-spirit every | somebody-Jew`

**5**  son […] received the Holy Spirit and believed in the Lord
`~son-[?] grab holy-spirit and believe | Lord`

**6**  Jesus Christ proceeds, on believing, somebody wants, one can, heaven
`Jesus-Christ proceed* on-believe somebody want one-can heaven`

**7**  land. Here ends this holy gospel, this Holy Spirit.
`~land here_ends this holy_gospel this holy-spirit.`

**8**  [proceedeth] from the Father, out and out, the Spirit proceeds; in turn the Son,
`[?] on-father out(ward)-out(ward) go_out-spirit in_turn son`

**9**  this Son, from, to God the Father sits; see, as this | remained
`this-son from to-God_the_Father sit see as this | remain*`

**10**  sun the Sun; this sun has three good things; first
`[?] Sun this sun +<subject_marker> +three good first`

> The three thousand of Acts 2:41 on line 2, then the folio turns to the
> procession of the Spirit and sets up the sun analogy for the Trinity.

## 083v — the sun, its light and its warmth

**1**  <subject marker> good [first], who [is] light; second, <subject marker> good, warmth; third, <subject marker> good
`SUBJ good [first] who light second SUBJ good warmth third SUBJ good`

**2**  from the Sun; the sun's light signifies the Son of God; in turn the warmth
`from-Sun sun Sun light symbolize son God in_turn warmth`

**3**  symbolizes the Holy Spirit; in turn from the Sun, it symbolizes the Father; on him, from the Sun
`symbolize holy-spirit in_turn from-Sun symbolize the_Father on-he from-Sun`

**4**  goes out the light, goes out the warmth, goes out the Son from the Father,
`on-go_out light on-go_out warmth on-go_out son on-the_Father`

**5**  goes out the Holy Spirit from the Father; as the sun,
`on-go_out holy-spirit on-the_Father as sun`

**6**  one form; this
`one shape,_form | this`

**7**  <subject marker> one God; if
`SUBJ one God if`

**8**  is, this can have, how
`+<subject_marker> this can have how?`

**9**  can heaven and earth
`can heaven earth`

**10**  quake, and in his [dwell] prepare
`quake and inside <preposition_of_genitive>-Lord [?] prepare`

**11**  heaven, town, from, in turn, and the earth
`heaven town-from-in_turn and earth`

> The sun analogy for the Trinity: the sun itself is the Father, its light
> the Son, its warmth the Spirit, and all three are one sun. Standard
> patristic teaching, set out here as a numbered list.

## 084r — Augustine and the child on the seashore

**1**  At that time, then,
`time then-exist`

**2**  on the crucifying of the Lord Jesus
`on-crucify Lord-Jesus`

**3**  Christ, in the sixtieth year, at that time
`Christ six-ten-year time`

**4**  holy Augustine went to the shore
`go holy-Augustine shore`

**5**  of the sea, because he would
`sea because want`

**6**  understand, if
`understand ~if`

**7**  that three, Lord, Lord, Lord, Father,
`+three Lord-Lord-Lord father`

**8**  Son, Spirit, are one God; and this is one
`son spirit one God and this exist one`

**9**  morning, evening, noon, Sunday, on going out; and then
`morning evening noon Sunday on-go_out and then`

**10**  he found one little child on the shore; this
`find one little son-Lord-<suffix_of_divine_name> on-shore this`

**11**  [by the] sea sat the little son of the Lord God [on the sand]; and | of
`~sea sit son-Lord_God little [on_the_sand] and | of`

**12**  the son of the Lord God [digging] one pit, son, and | of
`son-Lord_God [digging] one pit son* and | of`

**13**  the child carried in his hand one spoon, and this
`son-Lord-<suffix_of_divine_name> hand one spoon carry-son-Lord-<suffix_of_divine_name> and this`

**14**  [at the] sea, this spoon into this pit, scooped the son of the Lord God, this son
`~sea this spoon inside this pit scoop-son-Lord_God this son`

> **The legend of Saint Augustine and the child on the seashore**, who is
> emptying the sea into a hole with a spoon, and tells Augustine that he will
> sooner do that than understand the Trinity. It is in the Golden Legend,
> which is in this project's reference corpus, and it follows directly from
> the sun analogy on the folio before.

## 084v — thou shalt sooner empty the sea

**1**  And then holy Augustine: this little son of the Lord God,
`and_said holy-Augustine this little son-Lord_God`

**2**  what does this child want? Said the child, this:
`who this want-son-Lord-<suffix_of_divine_name> say want-son-Lord-<suffix_of_divine_name> this.`

**3**  [at the] sea, into this pit I scoop. Said holy Augustine: | this
`~sea inside this pit scoop say holy-Augustine | this`

**4**  child, can this child do it? What
`son-Lord-<suffix_of_divine_name> this can-son-Lord-<suffix_of_divine_name> do, who | this`

**5**  child, this, [at the] sea, into this pit the child scoops
`son-Lord_God this ~sea inside this pit scoop-son-Lord_God`

**6**  said this […] child; first this child, can
`say this [?] son-Lord-<suffix_of_divine_name> first this-son this | can`

**7**  the son of the Lord God does [it], rather than this Augustine, on leaving the chapter, this
`son-Lord_God do than this-Augustine on-chapter-leave-this`

**8**  and the child [cannot] see the word, did, before
`and son-Lord_God [cannot] see word ~do before`

**9**  holy Augustine; and [he] can many this [understand] on writing [the Trinity],
`holy-Augustine and can many this [understand] on-write [the_Trinity]`

**10**  but believe truly, Christian, one God, | of
`than believe righteous Christian one God | of`

**11**  the man, heaven and earth, that is, he has
`somebody-+<subject_marker> heaven land that_is have`

**12**  carries the commandment of God, [does not commit] sin; somebody is saved.
`carry commandment God [not_commit] sin somebody be_saved`

**13**  somebody answered: many mortal sufferings, for ever and ever,
`somebody answered* many mortal_suffering for_ever_and_ever =`

**14**  amen; speaks holy James, the apostolic letter, brother of
`amen speak holy_James apostolic_letter brother of`

> The child tells Augustine he will sooner empty the sea into the pit than
> understand the Trinity, and Augustine goes away and writes of it.

## 085r — one commandment broken is all of them broken

**1**  and among you, through transgressing one
`and among you through transgress one`

**2**  commandment of God; to the commandment, all; somebody <subject marker> [in one point] takes before
`commandment God to-commandment all^ somebody-+SUBJ [in_one_point] grab before`

**3**  face thanks to the Lord, because if a man one
`[?] to-Lord thanks Lord-<suffix_of_divine_name> because and somebody one`

**4**  transgresses; how then all commandments transgresses somebody? | because
`transgress how? then all^ commandment ~transgress somebody | because`

**5**  it is the Lord's; he received it from his angel, in the Old
`+<subject_marker> exist Lord-<suffix_of_divine_name> grab on-angel <preposition_of_genitive>-Lord inside <pertaining_to_the_Old_Testament>`

**6**  Testament word, father Abraham […] ten and one commandment
`word father Abraham [?]-ten and +one-[?] commandment`

**7**  [guilty of all] this, more than these, go and be saved among men; the Lord
`[?] this ?more_than_these go be_saved among somebody Lord`

**8**  of the Jews, Jesus, apostle to the gentiles, most high serpent the Son of the living God
`Jew(ish) Jézus apostle-pagan ?above-high [?] son living God`

**9**  Lord Jesus Christ; and to the man from face and to the man the soul
`Lord-Jézus-Christ and to-somebody from [?] and to-somebody soul`

**10**  upon the cross […] and for the man his blood was shed, and the man
`~on-+cross-[?] and to-somebody +<subject_marker> <preposition_of_genitive> blood shed and somebody +<subject_marker>`

**11**  the Lord redeemed from hell fire; [stay] somebody, many; stay
`redeem-Lord from hell fire [stay] somebody many stay`

**12**  the ten commandments; believe truly, Christian, one God
`ten-commandment believe righteous Christian one God`

> James 2:10, *whosoever shall keep the whole law, and yet offend in one
> point, he is guilty of all*, set against the ten commandments.

## 085v — Elijah calls down fire

**1**  our <subject marker> heaven [and] land, that is, has
`our SUBJ heaven land that_is have`

**2**  carries the commandment of God, [does not commit] sin; somebody is saved.
`carry commandment God [not_commit] sin somebody be_saved`

**3**  somebody answered: many mortal sufferings, for ever and ever,
`somebody answered* many mortal_suffering for_ever_and_ever =`

**4**  amen. Speaks holy Augustine: many believe; somebody within
`amen speak holy-Augustine many believe somebody inside`

**5**  God's body, that God can within the body.
`God body that God can inside body.`

**6**  to, from, face, bread in the place somebody takes
`to-from face bread on-place grab somebody`

**7**  within our mouth. Speaks holy Elijah the prophet, writes.
`inside our mouth speak holy-Elijah prophet write.`

**8**  Holy prophet, holy Moses; there was [called down] fire on all the world,
`holy-NAME.prophet holy-Moses exist [called_down] fire on-every world`

**9**  to heaven on high, because all the world was destroyed; knelt one
`to-heaven high because-exist every world destroy kneel one`

**10**  holy Elijah the prophet. At that time, then, the Lord destroyed
`holy-Elijah prophet time then-exist Lord-<suffix_of_divine_name> destroy-Lord`

**11**  the earth; there was fire in one place, and flame | from
`earth exist fire inside one place and flame* | from`

**12**  piercing [give account], girl, Lord God, within water; on this the destroying was three
`pierce [give_account] girl Lord_God inside water on-this destroy exist three`

> 1 Kings 18:36–38, Elijah at Carmel, the water poured over the altar and the
> fire of the Lord falling.

## 086r — the torch lit from heaven

**1**  forty and six years; at that time holy Elijah knelt
`forty and six-year time kneel holy-Elijah`

**2**  and prayed; thanks to the Lord; and fire
`and pray to-Lord thanks Lord-<suffix_of_divine_name> to fire`

**3**  God opened, the angel of heaven; and from [but rather]
`open God angel heaven and from [but_rather]`

**4**  fire [from heaven] one [torch] [became] said
`fire [?] one [?] [?] say`

**5**  the angel of God: Elijah, this signifies the Lord, the Lord of
`God angel Elijah this exist symbolize Lord-<suffix_of_divine_name> Lord | <preposition_of_genitive>`

**6**  angels. And then holy Elijah took a torch, and the torch
`angel and then-exist grab holy-Elijah torch ~and torch`

**7**  light; in turn this [figure], flame, went to Elijah from | four
`light in_turn this [figure] flame* go to-Elijah from | two-two`

**8**  four peoples; and every one from the people, the torch gave light; in turn
`two-two ~people and every from-~people torch light in_turn`

**9**  holy Elijah [chariot] little and in Elijah, until
`holy-Elijah [?] [?] and inside Elijah from-until`

**10**  stay. And then holy Elijah, then | two, two, two, two
`stay and_said holy-Elijah then | two-two-two-two`

**11**  ten years. This is written by holy Moses in the Old Testament word.
`ten-~year this_is write holy-Moses inside Old_Testament word`

> The fire from heaven becomes a torch, and the torch a figure, which the
> next folio applies to the Virgin.

## 086v — the torch signifies the Virgin

**1**  symbolizes [figure]: the gospel is, the angel [of] the Father, within the body
`symbolize [figure] gospel exist angel the_father inside body`

**2**  the blessed Virgin Mary, one son, the Lord God [figure] symbolizes
`blessed Virgin_Mary son one Lord_God [figure] symbolize`

**3**  somebody, body; the gospel is, takes | on the Lord
`somebody body gospel exist grab | on-Lord`

**4**  Jesus Christ; symbolizes the torch, the body, the blessed | Virgin
`Jesus-Christ symbolize torch body blessed | virgin`

**5**  Mary; then Mary conceived the Lord God, and Jesus saved all the whole
`Mary then-Mary conceive Lord_God and Jesus be_saved every all_the_world`

**6**  world; and Christ, woman, ours; and the Lord, head […] son
`world and Christ ~woman our and Lord ~head-[?]-~son`

**7**  heaven and earth [together] symbolizes the body of the Lord Jesus
`heaven and earth [together] symbolize body Lord-Jesus`

**8**  Christ [unconsumed] the fire symbolizes the Lord God, and every one can | God the Father
`Christ [unconsumed] symbolize fire Lord_God and can every | father-God`

**9**  the Lord Jesus Christ, angel, Holy Spirit, Mary, apostle, one [God]
`Lord-Jesus-Christ-angel-holy-spirit-Mary-apostle one [God]`

**10**  God [made]; and this [unconsumed] is, stays, on the putting to death
`God [made] and this [unconsumed] exist stay on-execute`

**11**  [of] the Lord Jesus Christ, at thirty, within the Host, on all the whole world
`Lord-Jesus-Christ on-thirty inside the_host = on-every all_the_world world`

> The torch lit but not consumed is read as the Virgin, which is the same
> figure the burning bush usually carries. Typology of this kind is why the
> book keeps saying *signifies*.

## 087r — the torch and the light

**1**  and somebody is [who] eats this bread, the man, the son
`and somebody exist this bread eat man* son`

**2**  of God man every man shall be saved; and one
`God [?] each,_every somebody +be_saved and one`

**3**  somebody not damned; Elijah symbolizes the body, the blessed
`somebody not_damned Elijah symbolize body blessed`

**4**  Virgin Mary; how from Mary the torch [gave] light, when [he] was born
`Virgin_Mary how? from-Mary torch light then-~be_born`

**5**  our Creator Lord; and [he] can, on the cross, to one
`Creator_Lord our and can on_the_cross to-one`

**6**  somebody die; but all the world dies; this one, one somebody,
`somebody die but every world die this-+one one somebody`

**7**  can, God, everything; within our mouth takes, because the Lord God
`can God every inside our mouth grab because Lord_God`

**8**  has the Lord God [in] the body, rather than [the sun], God <subject marker>
`~have-Lord_God body than [the_sun] God-+SUBJ`

**9**  many [the sun] and […] and from [the light] [the warmth]
`many [?] and [?] and from [?] [?]`

**10**  the earth [the sun] and heaven on high, and God is
`earth [?] and heaven high and God-+<subject_marker>`

**11**  this can; then the Lord would have heaven and earth quake
`this can then-exist want-Lord heaven earth quake`

> The torch figure carried through to the Nativity and the cross.

## 087v — the poor man of God

**1**  before, the gospel written
`~before gospel write`

**2**  by holy Matthew [eighteen]
`holy-Matthew [eighteen]`

**3**  of his writing, who [is] not
`of-write who_not`

**4**  somebody, an apostle, this from this
`somebody-apostle this from this`

**5**  little the son to
`[?] son [?]`

**6**  done, in Jesus'
`~do inside of-Jesus`

**7**  and the body, one
`and-~body one`

**8**  man is saved, one […] in heaven; in turn
`somebody +be_saved one [?] inside heaven | in_turn-chapter`

**9**  the year is not so; but every man is damned, judged, the man, by Christ. | Holy
`~year-exist ~but everybody = be_damned judge somebody Christ | holy`

**10**  Matthew speaks [thus] this man says, this little
`Matthew speak [?] this somebody say this [?]`

**11**  the son, this little the man trespasses, the poor man of God, and
`son this [?] somebody trespass blind God and`

**12**  the poor man of God, the man, and [riches] have the man in turn, this
`blind God somebody and [?] [?] somebody in_turn this`

> A sermon on sinning against a little one, the poor man of God, leading into
> the rich man of the next folio. *Poor man of God* is Király & Tokai's set
> phrase, and 087v11 is the line they cite for it. Corrected 2026-09-26: the
> earlier printing read the two signs one by one, as *blind to God*.

## 088r — the rich man, and the soul in purgatory

**1**  the man is rich, he has wealth, he sees, blind
`somebody rich have-somebody wealth see blind`

**2**  he goes […] or sits, and blind asks of this
`go [?] or sit and [?] exist ask_(for) from this`

**3**  man alms, in Jesus and the body [alms]
`somebody alms inside Jesus and-~body [alms]`

**4**  the blind does not take; somebody is damned; somebody is, ever
`blind not_take somebody be_damned exist somebody ever`

**5**  ever riches, but somebody judged, damned; somebody
`ever riches* ~but-somebody judge be_damned somebody`

**6**  on the blind; in turn damned, somebody is damned; somebody is, ever
`on-blind in_turn be_damned somebody be_damned exist somebody ever`

**7**  ever [remember], saved; somebody is damned; somebody is conceived
`ever [remember] be_saved somebody be_damned exist somebody conceive`

**8**  somebody within hell buried; [there] it writes; somebody
`somebody inside hell bury [there] write somebody`

**9**  within hell until the death of ours and the body; in turn | on
`inside hell until to-die our and-~body in_turn | on`

**10**  death, the soul within purification fire until doomsday; in turn | on
`die soul inside purification fire until doomsday in_turn | on`

**11**  doomsday, both soul and body within hell for ever and ever.
`doomsday and soul and body inside hell for_ever_and_ever =`

> Purgatory is named outright on line 10, which is a doctrine of the Latin
> church and not a gospel text.

## 088v — there was a certain rich man, clothed in purple

**1**  Here begins this holy gospel
`begins this holy-gospel`

**2**  written by holy Luke in
`write holy-Luke inside`

**3**  the sixth chapter of his writing.
`six [?] <preposition_of_genitive>-write`

**4**  At that time Lord Jesus said
`time say Lord-Jézus`

**5**  to his apostles, and the Jewish
`apostle <preposition_of_genitive>-Lord and Jew(ish)`

**6**  people, there was a rich [man]
`people exist-rich`

**7**  one rich man,
`one rich-somebody`

**8**  and the rich man, every […] and purple the rich man wore, and
`and somebody-rich each,_every [?] and purple go-somebody-rich | and`

**9**  the rich [man] from day to day caroused; and then thus [he] went
`rich from day until day carouse and then thus go`

**10**  one Lazarus to the rich man's house; and Lazarus was all over
`one ~Lazarus to-house this-rich and ~Lazarus exist each,_every from`

**11**  head until toe covered wounds, Lazarus; at that time this rich man
`[?] until [?] [?] wound ~Lazarus time this rich`

**12**  to table sat the rich man, husband [fared sumptuously], king, Lord [in purple]
`to table sit-rich man^ husband^ [fared_sumptuously] king-Lord [in_purple]`

**13**  various husbands; and then the rich [man] was [there]; this poor man asked
`various husband^ and then rich exist this poor_man ask`

> Luke 16:19–20, *there was a certain rich man, which was clothed in purple
> and fine linen, and fared sumptuously every day: and there was a certain
> beggar named Lazarus, which was laid at his gate, full of sores.*

## 089r — the dogs licked his sores, and angels carried him

**1**  alms; and the poor man the alms did not take; the rich [man] [desired]
`alms and poor_man alms not_take rich [desired]`

**2**  but the poor man he chased out; and then this [one] lay,
`but poor_man out chase and then lie this`

**3**  the poor man, out at the rich man's gate, alone, because the poor man was [full of sores]
`poor_man out gate to-of-rich exist-+one because exist poor_man [full_of_sores]`

**4**  was [laid]; and then the poor man wanted [what] passed from the crumbs; the dogs
`exist [laid] and then want poor_man trespass from crumbs the_dogs*`

**5**  on the rich man's table [fell from]; the poor man did not take; and then | have
`on-of-rich table^ [fell_from] poor_man not_take and then | have`

**6**  the rich man had many dogs, and the dogs came, this Lazarus and
`rich many dog and go-dog this [?] ~and`

**7**  the dogs licked Lazarus […] and Lazarus more
`lick-dog <preposition_of_genitive>-Lazarus [?] and Lazarus more`

**8**  was of the dogs have mercy, this Lazarus; in turn from the rich man
`exist from dog [?] have_mercy this Lazarus in_turn from-rich`

**9**  mercy; believe, Lazarus; lame; have mercy; and then this Lazarus
`have_mercy believe-Lazarus lame have_mercy and then this Lazarus`

**10**  died; the angels went, heaven's glory, the most high, the Father, God the Highest; this Lazarus, and Lazarus
`die go angel heaven glory* most_high the_father God the_Highest* this Lazarus and Lazarus`

**11**  the angels took, and carried Lazarus into the bosom of Abraham.
`grab-angel and Lazarus carry inside bosom Abraham`

**12**  the forefather. And then this rich man saw this miracle, of this Lazarus
`forefather and then-exist see this miracle this rich from this Lazarus`

> Luke 16:21–22, *the dogs came and licked his sores... the beggar died, and
> was carried by the angels into Abraham's bosom.* The word for bosom is
> Kiraly and Tokai's own Hungarian gloss, *öl*, left as they give it.

## 089v — in hell he lifted up his eyes

**1**  who Lazarus did, the angels, the Father, heaven; and then this
`[?] do, Lazarus angel father heaven and then-exist this`

**2**  the rich man died, and this rich man [also] was buried within hell; and then
`rich die and this-~rich [also] inside hell bury and then`

**3**  he suffered within hell, this rich man; he saw, the rich man's trespass, and saw Lazarus
`suffer inside hell this ~rich see ~trespass-~rich and see Lazarus`

**4**  within the bosom of father Abraham; and this rich man shouted:
`inside bosom father Abraham and shout this rich`

**5**  father Abraham, said the father, Lazarus; because this, let the poor man | of
`father Abraham say-father Lazarus because-this let poor_man | of`

**6**  Lazarus, a little finger dip in water, and cool it
`Lazarus little [?] immerge water and cool`

**7**  on the rich man's tongue [cool] flame the soul of the rich man; and from
`on-<preposition_of_genitive>-rich tongue [?] [?] soul <preposition_of_genitive>-rich and from`

**8**  [remember], the body of the rich man. And then father Abraham: | this
`[remember] body of-rich and_said father Abraham | this`

**9**  rich man, son of God the Father, this rich man [had] good [things] [in thy lifetime], as
`~rich son of-God_the_Father this-~rich good [in_thy_lifetime] as`

**10**  Lazarus was [evil things]; [now] the world; in turn this rich man is
`Lazarus exist [evil_things] [now] world in_turn this-~rich exist`

**11**  rich blind [lifted up his eyes] this rich man, Lazarus took the crumbs that fell
`rich [?] [?] this-~rich grab-Lazarus trespass from crumbs`

**12**  the dogs […] the rich man's table; the rich man took [fell from]; the rich man; Lazarus did not take.
`the_dogs* [?]-~rich table ~rich grab [fell_from] ~rich Lazarus not_take`

> Luke 16:23–25, *in hell he lift up his eyes... send Lazarus, that he may
> dip the tip of his finger in water, and cool my tongue... Son, remember
> that thou in thy lifetime receivedst thy good things.*

## 090r — a great gulf fixed, and they have Moses and the prophets

**1**  said father Abraham: take Lazarus, [send] up [to] the world. And then
`say father Abraham grab-Lazarus [send] up world and_said`

**2**  father Abraham: a great chasm between the rich man […] or [pass over]
`father Abraham great^ chasm among-~rich-[?] or [pass_over]`

**3**  this is the netherworld, highest, hell on hell; who shouts, this […]
`this_is netherworld highest hell on-hell who-shout this-[?]`

**4**  father Abraham; and Lazarus [may come] within the bosom of father
`father Abraham and Lazarus [may_come] inside bosom father`

**5**  Abraham; and a second time this rich man cried, father Abraham,
`Abraham and two who-shout this-~rich father-<suffix_of_divine_name> Abraham`

**6**  go, Lazarus, [great gulf], up [to] the world; the rich man has trespass; these four, of the rich man
`go Lazarus [great_gulf] up world have-~rich trespass this-two-two of-rich`

**7**  brethren, because the brethren […] of the rich man, how in this rich man's suffering
`~exist-exist because ~exist-exist [?] from-~rich how? inside this-rich suffer`

**8**  because these brethren, the man sins, from [repent] then is damned
`because this ~exist-exist somebody sin from [?] then-exist be_damned`

**9**  the man, as the rich man, this rich man is damned. Said father Abraham, they have
`somebody how?-rich this-rich be_damned say father-<suffix_of_divine_name> Abraham have`

**10**  brothers; trespass; this prophet, and preach, in order that this prophet preach
`brother trespass this prophet and preach in_order_that this prophet preach`

**11**  hear, somebody, brother, be damned; and a third [time] who shouts, this
`hear somebody brother be_damned* and three who-shout this`

> Luke 16:26–29, *between us and you there is a great gulf fixed... I have
> five brethren... they have Moses and the prophets.* The codex counts the
> rich man's three cries with its own ordinals, second on line 5 and third on
> line 11.

## 090v — neither will they be persuaded, though one rose from the dead

**1**  the rich man; our father Abraham, name vanished from; the prophet preaches, believe [fell from]
`rich our_father Abraham name-°vanished-from prophet preach believe [fell_from]`

**2**  [neither] good; somebody, Lazarus; believe, brother
`[neither] good somebody-Lazarus believe-brother`

**3**  and the body from the dead stood up, somebody, woman. Said our father Abraham: if not
`and body from die stand_up-somebody-woman say our_father Abraham if not`

**4**  the friend, the prophet, let the brethren believe, and the preaching
`friend^ prophet believe-brother-somebody and preach`

**5**  and good from somebody baptized […] not; the brother believes; and the body
`and good from somebody-baptize-[?] not brother believe and body`

**6**  rose from the dead, the man Lazarus […] this holy day. Here ends this holy gospel.
`from die stand_up-somebody-Lazarus [?]-this-holy-+day end this holy-gospel`

**7**  Here begins this holy gospel, written by
`begins this holy-gospel write`

**8**  holy John, in the second chapter of
`holy-John inside two chapter | <preposition_of_genitive>`

**9**  his writing. At that time Nicodemus came
`write time go Nicodemus`

**10**  by night to Lord Jesus,
`inside night to-Lord-Jézus`

**11**  because he feared the Jews; and
`because ~have Jew(ish) and`

**12**  not want to the Lord he came
`[?] to-Lord go-this`

> Luke 16:31, *neither will they be persuaded, though one rose from the
> dead*, which the codex reads back onto Lazarus. Then Nicodemus. **The
> citation on line 8 says John chapter two and the passage is John 3; it is
> the one miss in the citation test.**

## 091r — except a man be born again

**1**  but in the night to the Lord went Nicodemus. And then Nicodemus: O,
`but inside night to-Lord go-Nicodemus and_said Nicodemus oh.`

**2**  Nicodemus's Master, this Nicodemus: he, Nicodemus believes,
`of-Nicodemus Master this-Nicodemus he believe-Nicodemus.`

**3**  that he [is] the true Son of the living God, because he goes to heaven.
`that he true^ son living God because he go on-heaven.`

**4**  land, and the Lord, he [is] the true Son of the living God. And then
`~land and-Lord he true^ son living God and_said.`

**5**  the Lord Jesus: Nicodemus, verily verily I [say to] you,
`Lord-Jesus Nicodemus verily verily I you.`

**6**  speak: and the man is not to the Lord believing, born again a second [time],
`speak and man^ not exist to-Lord believe born_again* second^`

**7**  is born into this world, that one man is saved; but every man
`be_born on-this ?world one somebody be_saved a) each,_every-somebody`

**8**  is damned. Said Nicodemus: Master, how can this be, who to two before
`be_damned say Nicodemus Master how?-this can exist who to-two-before`

**9**  a second time from his mother goes, Nicodemus, and a second time is born into this world?
`two from <preposition_of_genitive> mother go-Nicodemus and two be_born-Nicodemus on-this ?world.`

**10**  this, thanks. Said the Lord Jesus: Nicodemus, I speak this, donkey, to
`this thanks say Lord-Jesus Nicodemus speak* I this-donkey-to`

> John 3:3–4, *except a man be born again, he cannot see the kingdom of God.
> How can a man be born when he is old? can he enter the second time into his
> mother's womb, and be born?*

## 091v — born of water and of the Spirit, and God so loved the world

**1**  this, that this Nicodemus again is born from Nicodemus's mother; but
`this that this-Nicodemus again be_born from of-Nicodemus mother but`

**2**  I speak: then a second [time] born, somebody, Nicodemus, from water and
`I speak then second^ be_born-somebody-Nicodemus from water and`

**3**  of the Holy Spirit, that one man Nicodemus is saved; but
`from holy-spirit one somebody-Nicodemus be_saved a)`

**4**  every man Nicodemus is damned. Said Lord Jesus, Nicodemus, in turn then
`each,_every-somebody-Nicodemus be_damned say Lord-Jézus Nicodemus in_turn | then`

**5**  I [have] begun to you, the Lord, to preach from heaven
`exist I you begin-Lord preach from-heaven`

**6**  and earth, how you from […] left, Nicodemus
`land how? you from [?] | leave-Nicodemus`

**7**  the man; then can this world, Nicodemus, the man enter
`somebody then-exist this ?world can Nicodemus-somebody [?]`

**8**  leave, who, I, to you the Lord preached, said | the Lord
`leave who I you preach-Lord say | Lord`

**9**  Jesus, Nicodemus: so did you love the Father, his God of heaven
`Jézus Nicodemus [?]-+one you love father <preposition_of_genitive>-Lord God heaven`

**10**  but the Father's only begotten Son, Jesus, that is, to the Lord, so
`a) <preposition_of_genitive>-father-<suffix_of_divine_name> only_one son Jézus that_is to-Lord [?]-+one`

**11**  did you love the Father, said Lord Jesus; and [water] and the man, the Lord
`you love father-<suffix_of_divine_name> say Lord-Jézus and [?] and somebody Lord`

> John 3:5, *except a man be born of water and of the Spirit*, then John
> 3:16, *God so loved the world, that he gave his only begotten Son*, which
> line 10 gives with the word *only begotten* intact.

## 092r — that whosoever believeth should not perish

**1**  believes in the Son of the Father, the only begotten, Lord Jesus Christ, and one
`believe son <preposition_of_genitive>-father-<suffix_of_divine_name> only_one Lord-Jézus-Christ and one`

**2**  man Nicodemus is saved; but every man Nicodemus is damned. Said
`somebody-Nicodemus be_saved a) each,_every-somebody-Nicodemus be_damned say`

**3**  Lord Jesus, Nicodemus [answered] to the Lord goes the Father, his God of heaven;
`Lord-Jézus Nicodemus [?] to-Lord go father <preposition_of_genitive>-Lord God heaven`

**4**  I love this world, [not to] judge [it], but rather to the Lord goes God the Father; who, I
`love I this world judge but_rather* to-Lord go God_the_Father who I`

**5**  saved this world by his death; and man is, to the Lord
`this ?world be_saved on-<preposition_of_genitive>-Lord die and [?] exist to-Lord`

**6**  believes, this man Nicodemus, and his Father
`believe this somebody-Nicodemus exist and <preposition_of_genitive>-Lord father-<suffix_of_divine_name>`

**7**  believes more than these; this one, one God. Said Lord Jesus [only begotten]
`believe ?more_than_these this +one one God say Lord-Jézus [?]`

**8**  one […] among you [that believeth] from
`one ~exist-[?] among you [that_believeth] from`

**9**  darkness; and [believeth in him] [already] [condemned] not; and said
`darkness and [believeth_in_him] [already] [condemned] not and say`

**10**  Lord Jesus, and the man Nicodemus who does evil among you
`Lord-Jézus and +<subject_marker> do_evil-somebody-Nicodemus among you`

> John 3:16–18, *that whosoever believeth in him should not perish... he that
> believeth not is condemned already.*

## 092v — men loved darkness rather than light

**1**  from the man Nicodemus who will not come to the light, but loves the darkness,
`from somebody-Nicodemus not_want on-light go a) darkness love`

**2**  somebody, Nicodemus; said the Lord Jesus: and <subject marker> practises righteousness from
`somebody-Nicodemus say Lord-Jesus and SUBJ practise_righteousness from`

**3**  somebody, Nicodemus; the light [he] loves, and every [one] | goes to the light
`somebody-Nicodemus light love and every on-light | go`

**4**  the man Nicodemus. Here ends this holy gospel. The Lord, with all thy heart, Lord.
`somebody-Nicodemus end this holy-gospel Lord-<suffix_of_divine_name> ?with_all_thy_heart Lord`

**5**  Here begins this holy gospel
`begins this holy-gospel`

**6**  written by holy Luke in
`write holy-Luke inside`

**7**  the fourteenth […] in his
`14 [?] inside | <preposition_of_genitive>`

**8**  writing. At that time
`write time`

**9**  Lord Jesus said to his apostles
`say Lord-Jézus apostle`

**10**  and to the Jewish
`<preposition_of_genitive>-Lord and Jew(ish)`

**11**  people: | then
`people | then`

**12**  a rich lord made, one rich man, many dinner
`rich-Lord-<suffix_of_divine_name> do, one rich somebody many [?]`

> John 3:19–21, *men loved darkness rather than light.* Then the citation on
> line 7 says **Luke chapter fourteen**, and what follows is the Great
> Supper, Luke 14:16. That citation checks out.

## 093r — a certain man made a great supper, and bade many

**1**  And then the rich Lord God, among the rich Lord God['s], redeemer's year, three friends.
`and then-rich-Lord_God among-rich-Lord_God redeemer-~year three friend.`

**2**  upon this […] said this rich lord to his living servant, go […]
`on-this [?] say this-rich-Lord-<suffix_of_divine_name> <preposition_of_genitive>-Lord living-servant go-[?].`

**3**  speak this word, go, the man; at that time all is finished, say.
`this word speak-angel go-somebody time +<subject_marker> each,_every finished say.`

**4**  This living servant, this […] man lo, the living servant.
`this-living-servant this [?] [?] lo living-servant.`

**5**  go, of the living Lord God, this man; then the Lord God, the man goes
`go of-the_living-Lord_God this-?man then-Lord_God go-?man`

**6**  of the Lord God's dinner, said this first: I not.
`of-Lord_God dinner say this first I not.`

**7**  cannot, because [I have] bought a plough; | want
`cannot because bought plough | want`

**8**  the man <subject marker> go out, see; and want the plough [to prove them].
`man* SUBJ go_out see and want plough [prove_them.]`

**9**  asked this servant to speak, the man, before
`ask this-~servant to-speak man* before`

**10**  […] the lord; and said this second, lo.
`[?] Lord-<suffix_of_divine_name> and say this two sense lo.`

**11**  The living servant goes, the lord's living servant, this man
`living-servant go <preposition_of_genitive>-living-servant Lord-<suffix_of_divine_name> this-somebody-sense`

> Luke 14:16–19, *a certain man made a great supper, and bade many... and
> they all with one consent began to make excuse. The first said unto him, I
> have bought a piece of ground, and I must needs go and see it.* The codex
> counts the excuses first, second, as the gospel does.

## 093v — I have bought five yoke of oxen

**1**  then the Lord God; somebody goes […] of the Lord God's dinner; said this
`then-Lord_God go-somebody-sense of-Lord_God dinner say this`

**2**  second somebody: us […] not
`two somebody-sense us-sense not`

**3**  the man cannot, because the man has bought
`can-somebody-sense because buy-somebody-sense`

**4**  five yoke of oxen ox the man must
`+five yoke sense [?] want-somebody-sense`

**5**  the man goes in the field the man must
`go-somebody-sense [?] want-somebody-sense`

**6**  <subject marker> the ox, thanks; is, can, the ox | [try]
`SUBJ ox thanks exist can ox | [try]`

**7**  [pray thee] [excused], asked this living servant to speak
`[pray_thee] [excused] ask this-living-~servant to-speak`

**8**  the man, before […] the lord said
`somebody-sense before [?] Lord-<suffix_of_divine_name> say`

**9**  this third man, lo, the living servant goes, the lord's living servant
`this +three somebody-thief lo living-servant go <preposition_of_genitive>-living-servant`

**10**  the Lord God; this somebody, thief; then the Lord God, somebody goes, thief,
`Lord_God this-somebody-thief then-Lord_God go-somebody-thief`

**11**  of the Lord God's dinner; said this third, thief: us, thief,
`of-Lord_God dinner say this three thief us-thief`

> Luke 14:19, *I have bought five yoke of oxen, and I go to prove them.* The
> codex counts the three excuse-makers with its own ordinals.

## 094r — go out into the highways and hedges

**1**  the man cannot, and the man must go
`not can-somebody-thief and to-go-somebody-thief`

**2**  because to go, somebody, thief, marry; us, thief, not
`because to-go-somebody-thief marry us-thief not`

**3**  can somebody, thief; and to go, somebody, thief, and these
`can somebody-thief and to-go-somebody-thief and these`

**4**  somebody, thief, [answered], said to speak; somebody, thief, before
`somebody-thief [answered] say to-speak somebody-thief before`

**5**  of […] the lord; and then, and one goes, the man
`<preposition_of_genitive>-[?] Lord-<suffix_of_divine_name> and then-exist and one | go-somebody`

**6**  the man on this dinner said this
`man* on-this dinner say this`

**7**  Lord God, that is, the people; and the people spoke of the Lord God's dinner
`Lord_God that_is people and people speak of-Lord_God dinner`

**8**  and the lord said to the living servant, go out into the roadside and the way
`and say <preposition_of_genitive>-Lord-<suffix_of_divine_name> living-servant go on-(on_the)_roadside and on-way`

**9**  and into the town, and to the town gate, and.
`and on-town and on-gate town and.`

**10**  find […] within the spirit poor | to be, the chapter
`~find-[?] inside spirit poor | to-exist-chapter`

**11**  [lame], body hunger and thirst within the spirit, and […] first.
`[lame] body hunger and thirst inside spirit and [?]-°first.`

> Luke 14:21–23, *go out quickly into the streets and lanes of the city, and
> bring in hither the poor, and the maimed, and the halt, and the blind...
> go out into the highways and hedges.*

## 094v — blessed is he that shall eat bread in the kingdom of God

**1**  man he found; every man went, the angel, into the lord's house
`[?] find each,_every somebody go-angel inside <preposition_of_genitive>-Lord-<suffix_of_divine_name> house`

**2**  said this living servant, the angel, Lord, it is done; and the mountain top, which the Lord
`say this living-servant-angel Lord do, and mountain_peak who-Lord`

**3**  said [the master] said this living servant, the angel servant
`say [?] say this living-servant-angel [?]`

**4**  one to the place, and to the place the living servant would go out
`one to-place and to-place want living-servant-angel on-out(ward)`

**5**  and then there rose at the table one Jew, and
`and then-exist +rise to-throne one Jew(ish) and`

**6**  shouted to: blessed from within the spirit poor, because
`shout-to blessed^ from inside spirit poor because`

**7**  the spirit of the poor, heaven's kingdom; and said | the Lord
`spirit of_the_poor heaven kingdom^ and say | Lord`

**8**  Jesus truly, speaking [to the] Jew, more than these, within the spirit heaven
`Jesus righteous speak-Jew more_than_these* inside spirit heaven`

**9**  kingdom. And then this rich somebody, the Lord God, [supper] [bade many]
`kingdom^ and_said this-rich somebody-Lord_God [supper] [bade_many]`

**10**  many, to go, the mouth […]
`many to-go-mouth | [?]`

**11**  thief, on our rich Lord God's dinner. Here ends this holy gospel.
`thief on-our-rich-Lord_God dinner here_ends this holy_gospel`

> Luke 14:15, *blessed is he that shall eat bread in the kingdom of God*,
> which the gospel puts in the mouth of one that sat at meat, exactly as
> line 5 does here.

## 095r — the bread blessed at the supper

**1**  Here begins this holy gospel
`begins this holy-gospel`

**2**  written by holy John
`write holy-John`

**3**  in the sixth chapter of his writing.
`inside six chapter <preposition_of_genitive>-write`

**4**  At that time Lord Jesus said
`time say Lord-Jézus`

**5**  to his apostles and the Jewish
`apostle <preposition_of_genitive>-Lord and Jew(ish)`

**6**  people: you
`people you`

**7**  are the Lord's body
`exist of-Lord body`

**8**  eat, and the Lord's blood
`eat and of-Lord blood`

**9**  drink. And then the Lord Jesus, the Lord's apostles, to the last dinner, this
`drink and_said Lord-Jesus apostle of-Lord last dinner-to this`

**10**  at the Last Supper; and the Lord Jesus took within [his] hands one baked
`at_the_Last_Supper = and grab Lord-Jesus inside hands one baked`

**11**  cake, and Lord Jesus blessed this bread
`„cake” and +blessed Lord-Jézus this +bread.`

**12**  and bread before the Lord, Lord Jesus put it. And
`and [?] before Lord put Lord-Jézus and.`

> **John chapter six is what the page says, and John 6 is the Bread of Life.
> That citation checks out.** The word for the loaf is Kiraly and Tokai's
> own, left in their quotation marks.

## 095v — except ye eat my flesh and drink my blood

**1**  the Lord Jesus gave wine, one cup, and water into the cup
`give^ Lord-Jesus wine one cup and water inside cup`

**2**  poured, and Lord Jesus blessed the wine and the water; and
`pour and +blessed Lord-Jézus wine and water and`

**3**  the wine [and] water before the Lord the Lord Jesus put. And then | the Lord
`wine water before Lord put Lord-Jesus and_said | Lord`

**4**  Jesus: and the man who eats this bread, this man
`Jézus and somebody exist this +bread eat this somebody`

**5**  is the Lord's body eaten, and the man not
`exist of-Lord ~body ~eat and man^ not`

**6**  who eats this bread and believes in the Lord
`this +bread eat [?] Lord believe`

**7**  every man is damned […] and the man who believes in the Lord
`each,_every somebody be_damned cut_off-[?] and somebody exist Lord believe`

**8**  and from the altar, from the thirty, the holy host
`[?] from altar(table) exist from thirty holy-host`

**9**  eats and drink every man shall be
`eat [?] [?] each,_every somebody exist`

**10**  living, for ever and ever, amen. And then the Jews:
`living for_ever_and_ever = amen and_said Jew`

**11**  how is it, the Jews, the Lord's body eaten, and the Lord's
`how? exist-Jews of-Lord ~body eat and of-Lord`

> John 6:52–54, *how can this man give us his flesh to eat?... except ye eat
> the flesh of the Son of man, and drink his blood, ye have no life in you.*
> The wine mixed with water on line 1 is the liturgy, not the gospel.

## 096r — whoso eateth my flesh hath eternal life

**1**  blood drunk? This pleasing, who he speaks, because eaten
`blood drink this pleasing who he speak because eat^`

**2**  the Jews, who […] […] and his body to eat
`Jew(ish) who-[?] [?] and <preposition_of_genitive>-Lord body eat`

**3**  and blood drunk, which [is] hidden, said this Lord Jesus, who is the Lord
`and blood drink which-hide say this Lord-Jesus who-Lord-exist`

**4**  strive but said Lord Jesus, believe; then
`[?] a) say Lord-Jézus to-believe then-exist`

**5**  somebody believes in the Lord, to the Lord, this who [is] indeed the Son
`believe-somebody inside Lord to-Lord this-who indeed^ son`

**6**  of the living God. And then the Lord Jesus: the Lord's body, this is
`living God and_said Lord-Jesus of-Lord ~body this_is`

**7**  indeed eaten, and the Lord's blood, this is indeed drunk.
`indeed^ eat and of-Lord blood this_is indeed^ drink`

**8**  And then the Lord Jesus: then the man [who] eats this bread
`and_said Lord-Jesus then man^ this bread eat`

**9**  is a man, apostle, [eateth] on the Lord's suffering [everlasting life]
`exist man^ apostle [eateth] on-of-Lord suffering [everlasting_life]`

**10**  is from eating, how the bread of […]
`exist from eat how? +bread <preposition_of_genitive>-[?]`

> John 6:55, *my flesh is meat indeed, and my blood is drink indeed*, which
> line 7 gives in both halves.

## 096v — I am the living bread which came down from heaven

**1**  your fathers did eat in field because that is the bread
`you father eat inside [?] because that_is +bread`

**2**  of life; he who goes, the Lord, bread; in turn the ascension from heaven | town
`living he_who go-Lord ~bread in_turn ascension^ from_heaven* | town`

**3**  from that day, upon this world; and the man who eats this bread
`from-+day on-this ?world and somebody exist this +bread eat`

**4**  from the man, living, for ever and ever, amen
`from man^ exist living for_ever_and_ever = amen`

**5**  and I [am] this bread, because the Lord, I | go
`and I this bread because-Lord I | go`

**6**  the Lord from the Lord's Father on this world; and I
`Lord from of-Lord the_Father on-this world and I`

**7**  to the Lord's Father, the living Lord; and the man is [in] the Lord,
`to-of-Lord the_father living-Lord and man^ exist Lord.`

**8**  believes; from the man living to the Lord, ever
`believe from man^ exist to-Lord living ever`

**9**  ever, the man; and the man who is
`ever man* and man^ exist`

**10**  within the Lord's keeping of the commandment of love stays; and I am
`inside Lord-keeping_the_commandment_of_love stay and I exist`

> John 6:49–51, *your fathers did eat manna in the wilderness, and are dead.
> This is the bread which cometh down from heaven... I am the living bread.*

## 097r — he that dwelleth in me, and I in him

**1**  within somebody and the man who carries his commandment, from the man
`inside [?] and somebody exist <preposition_of_genitive>-Lord commandment carry from somebody`

**2**  is within the Lord, from the Lord's keeping of the commandment of love stays; and I am
`exist inside Lord from Lord-keeping_the_commandment_of_love stay and I exist`

**3**  within somebody. And then the Lord Jesus: [abideth in me] somebody; and somebody is
`inside somebody and_said Lord-Jesus [abideth_in_me] somebody and somebody exist`

**4**  within the Lord, God the Father, the Son, God, Jesus, the Holy Spirit, Mary, Christ, the apostles, the angels,
`inside Lord-God_the_Father-son-God-Jesus-holy-spirit-Mary-Christ-apostle-angel`

**5**  keeping the commandment of love, stays; | wants the Lord, God the Father, the Son, God,
`keeping_the_commandment_of_love-stay | want-Lord-God_the_Father-son-God`

**6**  Jesus, the Holy Spirit, Mary, Christ, the apostles, the angels to go; and somebody
`Jesus-holy-spirit-Mary-Christ-apostle-angel go and somebody`

**7**  goes, the Lord, God the Father, the Son, God, Jesus, the Holy Spirit, Mary, Christ, the apostles, the angels,
`go-Lord-God_the_Father-son-God-Jesus-holy-spirit-Mary-Christ-apostle-angel`

**8**  into the heavenly land. And then the Lord Jesus: and this somebody
`inside heavenly land and_said Lord-Jesus and this somebody`

**9**  wants the Lord, God the Father, the Son, God, Jesus, the Holy Spirit, Mary, Christ, the apostles, the angels
`want-Lord-God_the_Father-son-God-Jesus-holy-spirit-Mary-Christ-apostle-angel`

**10**  to take the house, at | the Lord's, God the Father's, the Son's, God's, Jesus', the Holy Spirit's,
`house grab at | of-Lord-God_the_Father-son-God-Jesus-holy-spirit`

> John 6:56, *he that eateth my flesh, and drinketh my blood, dwelleth in me,
> and I in him.* The long chains on lines 4, 7 and 9 are one sign written as
> a single compound naming the whole of heaven at once, which is how the
> codex does a litany.

## 097v — the whole company of heaven, and the host

**1**  Mary's, Christ's, the apostles', the angels'; the Father God there, through staying,
`Mary-Christ-apostle-angel the_father-God there through stay`

**2**  somebody, for ever and ever, amen. And then the Lord Jesus: and
`somebody for_ever_and_ever = amen and_said Lord-Jesus and`

**3**  the man who from the altar, from the thirty, the holy host
`somebody exist from altar(table) from thirty holy-host`

**4**  eats [shall not die]; from somebody, the living, ever
`eat [shall_not_die] from somebody exist the_living ever`

**5**  ever, amen. Here ends this holy gospel. The Lord, be loved.
`ever amen here_ends this holy_gospel Lord-+be_loved`

**6**  Here begins this holy gospel
`begins this holy-gospel`

**7**  written by holy Luke, in
`write holy-Luke inside`

**8**  the […] chapter of his writing.
`and chapter <preposition_of_genitive>-write`

**9**  Then the Lord Jesus, within
`then Lord-Jesus inside`

**10**  the thirtieth day and in the first
`thirty +day and inside +one`

**11**  year; at that time he left
`year time leave`

> The altar, the thirty and the holy host on line 3 are the mass, not the
> gospel.

## 098r — the light of the body is the eye

**1**  the Lord Jesus [preached] among the high priest, and the Lord's apostles
`Lord-Jesus [preached] among high_priest = and of-Lord apostle`

**2**  And then the Lord Jesus, the Lord's apostles and the Jews, the people: [the lamp of the body]
`and_said Lord-Jesus apostle of-Lord and Jew ~people [the_lamp_of_the_body]`

**3**  have mercy <subject marker> […] the eye [single] [lightsome] | of the apostles
`have_mercy-+SUBJ of-[?] eye [single] [lightsome] | of-apostle`

**4**  the Jews, somebody, the eye. And then the Lord Jesus: the eye | of […]
`Jews-somebody eye and_said Lord-Jesus eye | of-[?]`

**5**  the man, this is the lamp of […] and the lamp of the apostles
`somebody +this_is lamp <preposition_of_genitive>-[?] and lamp | <preposition_of_genitive>-apostle`

**6**  the Jews, somebody: this is the body of […], and
`Jews-somebody this_is body of-[?] and`

**7**  in turn is within the body of […]; remained, one
`in_turn exist inside of-[?] body remain* one`

**8**  heart, sin protruding, is all the body of […]
`heart sin protrude exist all^ of-[?] body`

**9**  darkness. And then the Lord Jesus: if [take heed], the heart alone
`darkness and_said Lord-Jesus if [take_heed] heart-°alone`

**10**  sins against the Lord's Father, God, from the heart; wants the Father
`sin against of-Lord the_father God from heart want the_father`

> Luke 11:34, *the light of the body is the eye: therefore when thine eye is
> single, thy whole body also is full of light; but when thine eye is evil,
> thy body also is full of darkness.*

## 098v — a candle set on a candlestick

**1**  the Lord's flogging, various, from the donkey. And then the Lord Jesus: if
`of-Lord flog various from-donkey and_said Lord-Jesus if`

**2**  [it] is within the body of […], the whole heart is clean,
`exist inside of-[?] body all^ heart clean exist`

**3**  all the body of […] bright. And then the Lord Jesus:
`all^ of-[?] body bright and_said Lord-Jesus`

**4**  how then […] the lamp gives light, to
`how? then-exist [?]-[?] lamp light to-+<subject_marker>`

**5**  the light; the lamp, a hundred, is light of the body of […]
`light lamp hundred exist light of-[?] body`

**6**  Here ends this holy gospel. The Lord with all thy heart; the Lord have mercy; and truly
`end this holy-gospel Lord-<suffix_of_divine_name> ?with_all_thy_heart Lord-<suffix_of_divine_name> +<subject_marker> have_mercy and righteous(ly)`

**7**  speaks holy John: God
`speak holy-John God`

**8**  can bear the sky
`can carry sky`

**9**  and the earth; to this
`and earth to-this`

**10**  speaks holy John, the Lord
`speak holy-John Lord`

**11**  God; and the man who bears the living
`God and somebody carry living`

**12**  man upon this world, and the healthy man
`man^ on-this world and healthy_man^`

> Luke 11:33, *no man, when he hath lighted a candle, putteth it in a secret
> place... but on a candlestick, that they which come in may see the light.*

## 099r — he that dwelleth in love dwelleth in God

**1**  the man receives, and God receives the man [abideth] the man, God. | To
`man^ grab and God man^ grab [abideth] man^ God | to`

**2**  this the man has: the Lord God, Jesus Christ, the Son of God;
`this have somebody Lord-<divine> Jézus Christ son <of>-God`

**3**  and the Lord, the Lord's head, heaven and earth;
`and Lord ~head-Lord +heaven and earth`

**4**  and love our father's son as the man [his] neighbour.
`and love our father son as man^ neighbour`

**5**  In turn [hath this world's goods] the rich man; the man has wealth, sees;
`in_turn [hath_this_world's_goods] ~rich man^ have man^ wealth see`

**6**  trespass, the poor of God; and the man [seeth not] has God, the man
`trespass blind God and somebody [?] have God somebody`

**7**  <subject marker> loves the rich somebody as the man [his] neighbour; is | of
`SUBJ love-rich-somebody as man^ neighbour exist | of`

**8**  somebody rich, one, the heavenly land, speaks holy Matthew; and
`somebody-rich-+one heaven land speak holy-~Matthew and`

**9**  the man [a liar] says: us, God, love; in turn | of the rich.
`man^ [a_liar] say us God love in_turn | of-rich.`

**10**  man, his brother hateth, loves the rich somebody, from [a liar]
`man^ father son hateth love-rich-somebody from [a_liar]`

> 1 John 4:15-21: "Whosoever shall confess that Jesus is the Son of God, God
> dwelleth in him ... he that loveth not his brother whom he hath seen, how
> can he love God whom he hath not seen? ... he who loveth God love his
> brother also." *Father son* is the book's word for brother, "my father's
> son", by Király & Tokai's own entry, which cites lines 4 and 10 here.

## 099v — if a man say, I love God, and hateth his brother, he is a liar

**3**  the man, in turn, our father's son sees; somebody hateth
`man^ in_turn our father son see somebody hateth`

**6**  the man, father, son, as the rich somebody, the rich neighbour, God
`man^ father son as rich-somebody rich-+neighbour God`

**8**  land; hell [cannot] see the rich somebody | saved
`land hell [cannot] see-rich-somebody | be_saved`

**9**  the rich somebody is, for ever and ever, amen.
`rich-somebody exist for_ever_and_ever = amen.`

**10**  If the rich somebody is, the Lord, the apostles, love everybody as the rich somebody
`if-exist rich-somebody Lord apostle love everybody = as rich-somebody`

> Corrected 2026-09-20: lines 2, 3 and 6 first read "the father, the son".
> Király & Tokai's entry for *son* says the pair *father son* is the book's
> word for brother, "my father's son", and cites these very lines. So
> 1 John 4:20-21 stands here word for word: he that loveth God love his
> brother also.

**1**  he is a liar; how does this man love God, in turn, of
`one liar exist how? this somebody God love in_turn | <preposition_of_genitive>`

**2**  his brother hateth loves God [his brother] the Most High, this he sees.
`somebody father son [?] love God [?] high-this see.`

**3**  the man, in turn, our father's son sees; somebody hateth
`man^ in_turn our father son see somebody hateth`

**4**  the son hateth the man loves; how does this man love God, this
`son [?] love-somebody how? this-somebody God love this`

**5**  godfearing; in turn the rich somebody wants to love God; first love | of the rich
`godfearing^ in_turn want-rich-somebody God love first love | of-rich`

**6**  the man, father, son, as the rich somebody, the rich neighbour, God
`man^ father son as rich-somebody rich-+neighbour God`

**7**  and good; the rich somebody is loved […] heaven
`and good exist somebody-~rich love [?]-[?] heaven`

**8**  land; hell [cannot] see the rich somebody | saved
`land hell [cannot] see-rich-somebody | be_saved`

**9**  the rich somebody is, for ever and ever, amen.
`rich-somebody exist for_ever_and_ever = amen.`

**10**  If the rich somebody is, the Lord, the apostles, love everybody as the rich somebody
`if-exist rich-somebody Lord apostle love everybody = as rich-somebody`

> **1 John 4:20**, *if a man say, I love God, and hateth his brother, he is a
> liar: for he that loveth not his brother whom he hath seen, how can he love
> God whom he hath not seen?* Lines 1–4 have both halves of it, and the
> answer on line 6 is the great commandment again.

## 100r — Elijah taken up by fire, and the list of miracles

**1**  the neighbour is of the rich somebody; heaven [inheriteth]
`neighbour exist of-rich-somebody heaven = [inheriteth]`

**2**  the rich somebody, from [taken up] the Lord, from the Father and the Son and the Holy Spirit.
`rich somebody from [taken_up] Lord from God_the_Father and son and holy-spirit`

**3**  Elijah the prophet was taken,
`+Elijah prophet grab`

**4**  by fire, into heaven.
`fire on-+heaven`

**5**  Various miracles:
`various miracle`

**6**  did; the blind sight,
`~do blind sight^`

**7**  through light [saw]; the dead
`+<subj> through light die +<subj>`

**8**  were raised up; the lame [walked];
`?raised_up +lame`

**9**  the body, and the possessed of the evil one, were healed. Elijah? Who? and this,
`body and evil obsessed_by_the_evil +<subj> from-healing +Elijah | who-and-this`

**10**  and this miracle did Elijah do; writes the church father, the church father, [the] pagan.
`and-this miracle do Elijah write church_father church_father pagan`

**11**  First writes the church father, [the] pagan; the church father [concerning] Elijah.
`first write church_father pagan church_father [concerning] Elijah`

> 2 Kings 2:11 on lines 3-4, then the Matthew 11:5 list: the blind receive
> their sight, the dead are raised up, the lame walk, the sick are healed.
> The sign read Elijah here was read *Enoch* until today; it is Király &
> Tokai's own Elijah with one glyph swapped, and the Horeb pages at 133r
> settle it. *Lame* and *raised up* stand where their apparatus cites their
> own lame and resurrect signs on these lines. Lines 9-11 are a scholastic
> question, whether Elijah did these, answered from the fathers.

## 100v — the fathers on the sepulchre, a chronology, and the temple of forty-six years

**1**  the tomb, to heaven; on earth; after these writes [in three days]
`tomb to-+heaven on-earth after_these write [in_three_days]`

**2**  the pagan church father; after these writes: high, hide, and from the scholar.
`pagan church_father after_these write high-hide-and-from scholar.`

**3**  the pagan church father; after these writes the pagan scholar, the Pharisees.
`pagan church_father after_these write scholar pagan Pharisees*`

**4**  And the church father writes this three; and Saint Augustine the church father: Elijah
`and church_father this +three write and +Saint_Augustine_the_church_father +Elijah`

**5**  the Lord God, the Creator Lord, first; than the Creator Lord, the sun and the moon,
`Lord_God Creator_Lord first than Creator_Lord sun and moon`

**6**  and there is living Elijah; to Elijah, two; then, from
`and exist living +Elijah to +Elijah two then-exist from`

**7**  Adam; the Creator Lord fifty; and on this somebody [and six] seven
`Adam Creator_Lord fifty and on-this somebody [and_six] seven`

**8**  people. At that time was this somebody five hundred and
`people time exist this somebody five_hundred and`

**9**  thirty. In the thirtieth year, then: "destroy", the Lord; five
`thirty thirty-+day time destroy Lord-<divine> +five`

**10**  towns; and then on this: "destroy", forty and six years.
`town and then on-this destroy forty and six-year`

> Lines 9-10 are John 2:19-20, "Destroy this temple ... Forty and six years
> was this temple in building", set in the thirtieth year of Jesus, which is
> the sense Király & Tokai give this *thirty* sign. Saint Augustine is named
> on line 4 by their own entry. The sign rendered *heart-Lord* on lines 5
> and 7 is a cut, heart + Lord, and it does not read; it stands three times
> where "made" would stand (the Lord made first ... the sun and moon; Adam
> ... fifty) and at 010v:9 before "heaven and earth". Flagged, not read.

## 101r — Elijah's fire, and Enoch and Elijah kept for Antichrist

**1**  Then holy Elijah knelt down and prayed to the Lord God; to
`time kneel_(down) holy-+Elijah and pray Lord-<divine> | to`

**2**  fire; and took; the angel of God said, the angel of God, to Elijah:
`fire and grab God angel say God angel +Elijah`

**3**  this is the angel of the Lord; and this man from […]
`this exist-<of>-angel Lord-<divine> and this somebody from-exist`

**4**  And Elijah, somebody, from leaving, [wished to die] [juniper]; and
`and Elijah-somebody from-leave [wished_to_die] [juniper] and`

**5**  Elijah, the man, was taken up into heaven […] and […]. Elijah,
`+Elijah-somebody get_raptured heaven [?] and [?] | +Elijah`

**6**  the man [man] from the year; Noah and Elijah shall bear the sword;
`somebody [man] from-~year Noah Elijah sword carry`

**7**  hell, one gate open; and [Enoch] left; Noah, Elijah on the earth.
`hell one-+gate/open and [Enoch] leave Noah Elijah on-earth`

**8**  [Antichrist] [of a harlot] shall be born; two; the chief devil,
`[Antichrist] [of_a_harlot] through be_born two chief_devil =`

**9**  and the son, Satan; and there is […] evil, who is Antichrist.
`and son Satan and exist-[?] evil^ exist Antichrist`

> 1 Kings 18:36-38 on lines 1-2, Elijah's prayer and the fire; then the
> Gospel of Nicodemus, chapter 20: Enoch and Elijah, kept alive, return at
> the coming of Antichrist, fight him and are slain by him. *Sword* is a
> spelling Király & Tokai's own sword entry cites at this line. The sign
> beside Elijah on lines 6 and 7 is their Noah sign, and this passage
> repeats word for word at 133v-134r, where they mark the same sign as a
> variant of Noah. In every source it is Enoch who stands here, and Noah is
> never taken up to heaven (133v:8). Their reading stays on the page; the
> doubt is recorded.

## 101v — the opening of a reading from Luke: Simeon

**1**  Before the Word, says
`before Word^ speak`

**2**  holy Luke: glory to the Lord,
`holy-Luke to-Lord glory^`

**3**  the Lord God, glory be;
`Lord God glory^ exist`

**4**  of the Lord, holy mercy, Lord;
`<of>-Lord holy-have_mercy Lord`

**5**  this Lord, the gate, Lord;
`this Lord gate Lord`

**6**  of the Lord, many homes.
`<of>-Lord many home`

**7**  Before, many holy fathers before, many, writes church father the church father:
`before many holy-father-before many write [?] church_father`

**8**  heaven; the Lord's Son […] the Lord taken; to see one […]
`+heaven Lord son +<subj> grab-Lord see one [?]`

**9**  because many holy fathers wanted to see the Lord Jesus Christ [consolation of Israel]
`because because many holy-father want see Lord-Jézus-Christ [?]`

**10**  The Lord's chapter: many; how shall we see? In turn, Simeon; one, Simeon.
`Lord-chapter many ?how_shall_we see a) Simeon one-Simeon`

> Luke 2:25-32, Simeon, who was promised he should not see death before he
> had seen the Lord's Christ, and Luke 10:24, "many prophets and kings have
> desired to see those things which ye see". The reading continues on 102r.

## 102r — Simeon's arms, and the thirtieth year

**1**  and the body; it is Simeon; for Simeon carried him in his bosom:
`and ~body exist Simeon because from Simeon carry bosom`

**2**  the Lord Jesus Christ [took him]. The Lord saw the apostles and the Jews, the people, and
`Lord-Jesus-Christ [took_him] Lord see apostle and Jew people and`

**3**  these apostles, the Jews, the Lord; all saw within the body, somebody.
`this apostle Jew Lord every see inside ~body somebody`

**4**  At that time then the Lord Jesus [was] within his thirtieth year. At that time
`time then Lord-Jesus inside thirty year time`

**5**  from the woman, the Lord Jesus; and the Lord went from town
`from-woman-woman Lord-Jézus and go-Lord from town`

**6**  to town, from temple to temple, from
`+until town from temple +until temple from`

**7**  town until town; and the Lord's apostles went, the Lord, into the world; the gospel
`town until town and of-Lord apostle go-Lord into_the_world* gospel`

**8**  the Lord preached; various miracles the Lord did: | the blind
`preach-Lord various miracle ~do-Lord | ~blind`

**9**  the blind <subject marker> the Lord, through light, the Lord; the dead the Lord raised; the lame
`~blind SUBJ-Lord through light-Lord die raise-Lord lame`

> Luke 2:28, "then took he him up in his arms", where *bosom* is a spelling
> Király & Tokai's own bosom entry cites at this line; Luke 3:23 for the
> thirtieth year, which is the sense they give this *thirty* sign; then the
> ministry and the Matthew 11:5 list, as on 100r. *Until* is the "to" of
> "from town to town", and was read too narrowly from this line alone before.

## 102v — the Passion in short: the sun darkened, the rocks rent

**1**  the body, and the possessed of the evil one, the Lord healed. And the Lord suffered for
`body and evil obsessed_by_the_evil from-healing-Lord and suffer +<subj> Lord to`

**2**  man's sin, the good of the whole world; the cross […]; and for man
`somebody-sin good the_whole_wide_world +cross-[?] and to-somebody`

**3**  <subject marker> the Lord's shed blood; and somebody the Lord redeemed from hell
`SUBJ of-Lord shed_blood and somebody redeem-Lord from hell`

**4**  fire. And then the Lord, on the cross […] | the sun
`fire and then-Lord on_the_cross-[?] | sun*`

**5**  […] and the moon, this darkened, before the sun darkened;
`[?] and moon this eclipse before sun eclipse`

**6**  and before the moon darkened, the face of the earth quaked; the rock,
`and before moon eclipse face-~Adam quake rock`

**7**  the stone rent; and at the sun's darkening every
`stone +rent and on-sun eclipse each,_every`

**8**  tree in the world, this humbled itself, and all creation mourned.
`tree on-+world this humble and all^ create mourn`

**9**  Then Christ, the cross […]; and the Lord was put in the sepulchre.
`then-exist Christ +cross-[?] ~and Lord inside burial_chamber | put`

> Matthew 27:45 and 27:51, the darkness and the rocks rent, with Luke 23:43
> for the thief. *Rent* is Király & Tokai's split-the-rock sign in a second
> spelling their entry cites at this line and at 052v:2, where the same
> sentence stands in the long Passion. Their quake, rock, stone, humble and
> mourn are all cited by them on these lines.

## 103r — the three days: where was the soul?

**1**  the Jews; and then the Lord lay within the tomb, the Lord; and the hour, at that time,
`Jews and then-Lord inside tomb lay-Lord and hour time`

**2**  went the Father, God of heaven; from the Father, the angel; the soul within
`go the_father God heaven on-of-father angel soul inside`

**3**  was before the Lord Jesus, and rose from prayer.
`~exist-~before Lord-Jesus and rise* from pray`

**4**  In turn the angel stayed in the tomb; in turn, the Lord went to hell,
`in_turn angel inside tomb stayed in_turn to-Lord go-Lord on-hell`

**5**  and destroyed hell, and redeemed man; hell fire, because | he carried,
`and hell destroy and somebody redeem-Lord fire hell because | carry`

**6**  the Lord, his cross on his shoulder; and man's soul […]
`Lord <of>-Lord +cross on-<of>-Lord shoulder and somebody soul-[?]`

**7**  of the Lord, God the Father, all the whole world. And then the Lord Jesus | from
`of-Lord God_the_Father every all_the_world world and_said Lord-Jesus | from`

**8**  the Father, the Lord God of heaven; the soul […] of this God the Father, this soul
`father of-Lord God heaven soul-[?] this-God_the_Father this soul`

> The question the fathers asked of the three days: did the soul stay in the
> sepulchre, or go down to hell? Line 4 puts both, with *stayed*, which is
> Király & Tokai's stay sign in a spelling they cite at this line. The word
> rendered angel on lines 2 and 4 is their angel/Satan/Lucifer sign; on line
> 4 the devil is meant.

## 103v — the lost sheep, a doxology, and the names in one sign

**1**  of the Lord's sheep: I [the] soul, the Lord redeemed; the wolf; the earth
`of-Lord sheep I soul redeem-Lord wolf ~earth`

**2**  this God the Father's soul; the sheep [gather] the Lord took; this God the Father's soul
`this-God_the_Father soul sheep [gather] grab-Lord this-God_the_Father soul`

**3**  redeem heavenly, until for ever and ever.
`redeem heavenly until for_ever_and_ever =`

**4**  amen. From every ghost, and from [fared sumptuously] the Lord, from the heavenly, on this
`amen from each,_every ghost and from [?] Lord from ?heavenly on-this`

**5**  the world believe, woman, woman; and [sent] the Lord [his] angel. | On
`world believe woman woman and [sent] Lord [his] angel | on`

**6**  […]-[…]-Mary-Jesus-God-Christ-angel-sheep
`[?]-[?]-Mary-Jesus-God-Christ-angel-sheep`

**7**  speaks Saint […], the church father. Holy
`speak +Saint_[a_church_father] church_father | holy`

**8**  Anne, this Anne, gave birth:
`Anne this Anne be_born`

**9**  [for ever] [and ever] [for ever]
`[?] [?] [?] +<subj>`

**10**  to mercy, the commandment; go, on everyone, the whole world.
`to-have_mercy commandment go on-each,_every the_whole_wide_world`

> The close of the previous reading, with "until the ages of ages, amen" on
> lines 3-4 as at 099v:9, then a new one opening with the birth of the Virgin
> from Anne, as on 104r. Line 6 is one compound sign carrying six names, a
> litany packed into a word, as at 097. Line 7's father is named by a stem
> Király & Tokai mark "name of a church father" and cite here, so the name is
> theirs to give; it cannot be read from the sign.

## 104r — a creed, from Anne's daughter to the judgment

**1**  the world, that is: then from Anne was born the blessed | Virgin
`?world that_is then-exist from Anne be_born happy | virgin`

**2**  Mary; from Mary was born the Lord Jesus Christ; and the Lord went
`Mary from Mary ~be_born Lord-Jesus-Christ and from Lord go`

**3**  into the world, preached the gospel, various miracles did;
`into_the_world* gospel preach various miracle ~do`

**4**  the Lord suffered for man's sin, for the whole world; the Lord was crucified, and
`Lord and suffer to somebody +sin the_whole_wide_world +crucified Lord and`

**5**  for man the Lord shed his blood, and the Lord redeemed man
`to somebody +<subj> <of>-Lord +shed_his_blood and somebody +<subj> redeem-Lord`

**6**  from hell fire; and somebody, the Lord, is believed
`from hell fire and somebody Lord exist believe`

**7**  that [he is] truly the Son of the living God: everybody is saved; and one
`that righteous son living God everybody = be_saved and one`

**8**  man shall be damned; and the Lord: he that believeth not, and [perish]
`somebody be_damned to and Lord +not believe and [?]`

**9**  one shall be saved; in turn, every man shall be damned.
`one to be_saved ~a) each,_every somebody be_damned`

> The summary creed the book gives more than once: the Virgin's birth, the
> ministry, the Passion, the harrowing, then Mark 16:16, "he that believeth
> and is baptized shall be saved; but he that believeth not shall be damned".
> *Shed his blood* is Király & Tokai's own expression, cited by them at line
> 5. Line 8 is word for word the line at 026v:11, gap included.

## 104v — blessed are the eyes which see

**1**  Begins this holy gospel,
`begins this holy-gospel`

**2**  written by holy Luke, in
`write holy-Luke inside`

**3**  the tenth chapter of his writing.
`ten chapter <of>-write`

**4**  Then said | the Lord
`time say | Lord`

**5**  Jesus to his apostles
`Jézus apostle <of>-Lord`

**6**  and the Jews, the people:
`and Jew people`

**7**  blessed the two, from
`blessed two from`

**8**  the eye, the two eyes; this the Lord sees, who you [those things which] | the apostles see.
`eye to-two eye this Lord see who you [those_things_which] | see-apostle`

**9**  the Jews: because many holy fathers, many, writes the church father, many prophets, many
`Jews because many holy-father many write church_father many prophet many`

**10**  kings, many emperors | would have liked, the fathers, church fathers, prophets, kings, emperors,
`king many emperor | would_like_to-father-church_father-prophet-king-emperor`

**11**  to see this which you [blessed are] from […]; and
`this see who you [blessed_are] from-[?] and`

**12**  there rose among these Jews one; another church father wanted
`+rise among this Jew(ish) one +another church_father want`

> Luke 10:23-24: "Blessed are the eyes which see the things that ye see: for
> I tell you, that many prophets and kings have desired to see those things
> which ye see, and have not seen them." The citation, Luke chapter ten, is
> right. Line 10 packs father, church father, prophet, king and emperor into
> one compound sign after listing them one by one on lines 9-10.

## 105r — the lawyer's question, and the great commandment

**1**  tempted the Lord Jesus. And then this Jew: Master, learning […]
`tempt Lord-Jesus and_said this Jew Master learn-[?]`

**2**  who, the Jews' church father, must do; how? this […] gain
`who Jews-church_father must do how? this-[?] gain`

**3**  life for ever and ever. Said the Lord Jesus, this […]:
`living for_ever_and_ever = say Lord-Jesus this-[?]`

**4**  [answered] to the Jews: pray, Jews, Moses writes, says this
`[answered] to-Jews pray Jews Moses write say this`

**5**  Jew, this church father: pray, church father, Moses writes within
`Jew this-church_father pray church_father Moses write inside`

**6**  the sixth chapter. Said the Lord Jesus, [with] joy, I, this Jew: how
`six chapter say Lord-Jesus joy I this-Jew how?`

**7**  readest thou Moses? Rightly. And then this Jew, this reading:
`read Moses righteous and_said this Jew this read`

**8**  Moses writes: love the Lord God highest [above] every creature, all our
`Moses write love Lord_God highest ~every create all^ our`

**9**  soul, all our might, all our heart; and | of
`soul all^ our might all^ our heart and | of`

**10**  somebody, brother, as somebody [his] neighbour, ours <subject marker>
`somebody brother as somebody neighbour our SUBJ`

**11**  the heavenly land. And then the Lord Jesus, rightly, spoke.
`heaven land and_said Lord-Jesus righteous speak`

> Luke 10:25-28. "What is written in the law? how readest thou?" and the
> answer from Deuteronomy 6:5, which is what "within the sixth chapter" on
> line 6 points at. The sign rendered *contain* on line 7 is Király &
> Tokai's, and here it carries "readest".

## 105v — who is my neighbour? A certain man went down to Jericho

**1**  the Jew: for whoever believes in one God, to […] literally,
`Jew(ish) because and somebody believe one God to-cut_off-literal`

**2**  love the man, our brother, as the man [his] neighbour;
`love man^ our ~brother as man^ neighbour`

**3**  of […] heaven, land; and the man's mouth
`of-[?] heaven ~land and mouth man^`

**4**  left; and then […] proud, this Jew. And then
`leave and then-[?] proud this Jew and_said`

**5**  Master, who is of the Jews […]? said
`Master who? exist of-Jews [?]-~year-~exist-DIV say`

**6**  the Lord Jesus [answered] to the Jews: pray, who, Jews, Moses rightly
`Lord-Jesus [answered] to-Jews pray who-Jews Moses righteous`

**7**  and from was a living servant; committed sin; of somebody, Adam,
`and from exist living-~servant commit sin of-somebody-~Adam`

**8**  the Lord God; and cast out; on the Lord's mercy; and then
`Lord_God and exorcise on-of-Lord have_mercy and then`

**9**  went somebody, Adam, into the field, to one place, forgive […]
`go-somebody-~Adam on-~field to-one place °forgive-+SUBJ`

**10**  Jericho town; evening, from, to build; and then went
`Jericho town evening-from-to build and then go`

**11**  the servant, Adam, into the field; and then met robbers.
`~servant ~Adam on-~field and then meet robber`

> Luke 10:29-30. *Fell among* is Király & Tokai's meet sign in a spelling
> they cite at this line. The word rendered *Adam* on these pages is their
> Adam-or-man sign in the sense man, and I render it "the man" throughout
> the parable.

## 106r — stripped, half dead; the priest and the Levite pass by

**1**  And the robbers began, to the man; the holy(?) found;
`and begin robber to-~Adam ~rich ~find`

**2**  and then these robbers let the man go, having taken
`and then-exist this robber remit ~Adam grab`

**3**  the booty; and the robbers beat the man,
`booty and ~Adam beat robber`

**4**  this man dying; and half dead and half alive.
`die-this ~Adam and +half_dead and +half_alive`

**5**  Thus went on one descendant of Abraham, who to [him]
`thus go ~on one descendant_of_Abraham who-to`

**6**  the man; on seeing, the descendant of Abraham passed the man by, and | went.
`~Adam on-see-descendant-Abraham long-~Adam and | go`

**7**  The descendant of Abraham went on; the rest, half, a descendant of Moses, who to Adam
`descendant_of_Abraham go ~on the_rest^ half descendant_of_Moses who-to ~Adam`

**8**  […] the descendant of Moses passed the man by, and went [by chance]
`[?]-descendant_of_Moses long-~Adam and go [by_chance]`

**9**  Adam could; the two, Abraham [and] Moses, good [they] did.
`~Adam can-two-Abraham-Moses good ~do`

**10**  passed the man by; through went the two of Abraham, that way.
`long-~Adam through go-two-Abraham that_way`

> Luke 10:30-32. *Half dead* and *half alive* are one unread glyph joined to
> Király & Tokai's die and their living, each with their man; the pair reads
> each other. The book writes the priest as "descendant of Abraham" and the
> Levite as "descendant of Moses" (Király & Tokai's reading; an earlier
> printing had "descendant of the scripture", a reading of ours, which was
> wrong).

## 106v — the Samaritan binds his wounds and pays the host

**1**  Went on one Samaritan, to Jerusalem, the Lord's living servant;
`go ~on one Samaritan on-Jerusalem <of>-Lord living-servant`

**2**  and saw his face, found him, and had compassion on the man;
`and face +found and have_mercy to-~Adam`

**3**  did, for the Lord poured wine into the man's
`~do because pour-Lord wine of-~Adam`

**4**  wound, and had mercy; one to the long Lord; in turn, the Lord's clothes
`wound and have_mercy one-to long-Lord in_turn of-Lord clothes`

**5**  bound up the man's wounds, and the man | he put,
`+bound_up <of>-~Adam wound and ~Adam | put`

**6**  the Lord, on the Lord's shoulder; and Adam [he] took away to the Lord
`Lord on-of-Lord shoulder and ~Adam take_away to-Lord`

**7**  lodging; and the man this innkeeper took.
`on-lodging and ~Adam grab this innkeeper`

**8**  And the innkeeper took two [pence], two denarii;
`and innkeeper grab two [?] two denarius`

**9**  And then this innkeeper, this innkeeper, on Adam
`and_said this innkeeper this-innkeeper on-~Adam`

**10**  take care; on this, that, whatever more on the man | […]
`carry on-~exist-this who to-whatever on-~Adam | [?]`

> Luke 10:33-35. *Found* and *bound up* are both spellings Király & Tokai's
> own entries cite at these lines, the second one also at 190r:9 where it
> binds Satan. The book puts the wounded man on the Samaritan's shoulder,
> not his beast, the same word it uses for the cross at 103r:6.

## 107r — which of these three was neighbour? Then Augustine begins

**1**  the innkeeper: then [I] go; on doomsday all this, innkeeper, [I] give back.
`innkeeper then go doomsday every this-innkeeper give_back`

**2**  And then the Lord Jesus: I judge, this Jew, who
`and_said Lord-Jesus judge I this-Jew who?`

**3**  <subject marker> this good friend among | the […] Abraham, one, Moses,
`SUBJ this good friend among | [?]-Abraham-+one-Moses`

**4**  the Samaritan? And then this Jew [say]:
`the_Samaritan and_said this Jew [say]`

**5**  and this, the Jews spoke, as [neighbour] a good friend,
`and this-Jews speak-Jews as [neighbour] good friend`

**6**  and name […] had mercy to Adam, did. And then
`and name-[?] have_mercy to-~Adam do and_said`

**7**  the Lord Jesus rightly <subject marker> spoke [to] the Jew. And then the Lord Jesus | this
`Lord-Jesus righteous SUBJ speak-Jew and_said Lord-Jesus | this`

**8**  Jew brought; and he said: similarly do, Jews.
`Jew brought* and he_said* similarly do-Jews`

**9**  is, of the Jews, the heavenly land. End [of] this
`exist of-Jews heaven land end this`

**10**  holy gospel. Speaks holy Matthew: from the one denarius is signified
`holy-gospel speak holy-Matthew from one denarius symbolize`

> Luke 10:36-37, "He that shewed mercy on him. Then said Jesus unto him,
> Go, and do thou likewise", and the reading ends on line 9. *The
> Samaritan* on line 4 is Király & Tokai's Samaritan, which their entry
> cites here "in aggregate". The sign rendered *was accused* on lines 3
> and 5 is their gloss; the slot wants "neighbour" both times, and it is
> left as their word. Line 10 opens the exposition.

## 107v — the two pence, by Augustine; and the opening of the next reading

**1**  Old Testament belief; the second denarius symbolizes on being born.
`Old_Testament believe second denarius symbolize ~on-be_born`

**2**  and death of the Lord Christ, speaks Saint Augustine the church father, [two pence] [Testaments].
`and die Lord-Christ speak Saint_Augustine_the_church_father [two_pence] [Testaments.]`

**3**  little [the Old] [the New] says God, but the body
`little [the_Old] [the_New] say God but body`

**4**  God swallow; on, from thirty [years] [preached], from the priest.
`God swallow on-from thirty [years] [preached] from priest`

**5**  Before the gospel, says | the Lord
`before gospel say | Lord`

**6**  Jesus to his apostles and
`Jézus apostle <of>-Lord and`

**7**  the Jewish people:
`Jew(ish) people`

**8**  because see | he is
`because see | ?is_he-chapter`

**9**  [so] good;
`[?] good`

**10**  do what is pleasing,
`do, pleasing`

**11**  and thanks to the Lord, the Lord God. Begins this holy gospel, written
`and thanks to-Lord Lord-<divine> begins this holy-gospel write`

> The allegory of the two pence as the two Testaments, or as the birth and
> death of Christ, is Augustine's on the Good Samaritan (Quaestiones
> Evangeliorum II.19), and the book names him. Line 4 carries a priest sign
> Király & Tokai mark doubtful at this line; the line does not read.

## 108r — ye are the salt of the earth, and a city set on a hill

**1**  written by holy Matthew, in the fifth chapter of his writing. Then said the Lord Jesus
`holy-Matthew inside +five chapter <of>-write time say Lord-Jézus`

**2**  to his apostles and the Jewish people: ye are the salt
`apostle <of>-Lord and Jew(ish) people you salt`

**3**  of this world. In turn, if this salt lose its taste, it is good for nothing, out,
`this ?world in_turn lose_taste this salt good-apostle-God out(ward)-out(ward)`

**4**  the salt is thrown out, and the people trample on the salt,
`salt throw_out and salt people trample_on`

**5**  because this is high; you, good deed. And then
`because this exist high you good_deed = and_said`

**6**  the Lord Jesus: and <subject marker> a town on high, to the mount; and the town up
`Lord-Jesus and SUBJ town on-high to_the_mount and town up`

**7**  the people see; and then <subject marker> [trodden down] the people, to the town.
`people see and then-+SUBJ [trodden_down] people to-town.`

**8**  escape this; and you learn; you
`escape this and you learn you`

**9**  good deed; if [he] is high, from two, on the people learning
`good_deed = if-exist high from-two people on-learn`

**10**  and do; found among the people, a man, mercy.
`and do, +found among people somebody have_mercy`

> Matthew 5:13-14. The citation is right. This is the page that corrected
> two of this project's readings earlier: the sign on line 6 is *mount*, not
> *the Mount of Olives*, because Matthew wants a hill here, and the *city*
> beside it is the reading that came out of the same line.

## 108v — the candle and the bushel, and the Father's house

**1**  and love the Lord [candle]; somebody, and loves the Lord, the man; and believes in the Lord, and from
`and love-Lord [candle] somebody-and love-Lord man^ and believe inside-Lord and from`

**2**  the man receives; of you, of the Lord, in teaching [which]
`somebody grab from you <of>-Lord on-learn [?]`

**3**  learns, the Lord; I take you, the Lord; and from the man goes
`learn-Lord I you grab-Lord and from man^ go`

**4**  into the Lord's God the Father's house | is joy ever
`inside of-Lord God_the_Father house | exist joy ever`

**5**  ever, amen. In turn, then, out, the building, to cut off, the man
`ever amen in_turn then out building to-cut_off man^`

**6**  is the town from […]. And then the Lord Jesus: then a man
`exist town from-[?] and_said Lord-Jesus then man^`

**7**  the lamp, light, a man, to this [before men], light, who [is] the lamp
`lamp light man^ to this [before_men] light who lamp`

**8**  on a candlestick put; a man doth, a man, to the pit, year; but
`on-candlestick put man^ do man^ to-pit-~year but`

**9**  a lamp on a candlestick somebody puts, who releases
`lamp on-candlestick put-somebody who release^`

**10**  the lamp; every people see who [is] within the house; and you
`lamp every people see who inside house and you`

> Matthew 5:15-16, the candle, the bushel and the candlestick, with Király &
> Tokai's own candlestick sign on lines 8 and 9 and their bushel on line 8.
> Line 4 is John 14:2, the Father's house, brought in as the reward.

## 109r — whosoever shall do and teach them

**1**  the lamp of this world, that is: learn from the Lord Jesus and from the holy gospel.
`lamp this ?world that_is learn from Lord-Jézus and from holy-gospel`

**2**  And then the Lord Jesus: great belief; there is a man [who] carries the people
`and_said Lord-Jesus great^ believe exist man^ carry people`

**3**  until doomsday; and one believes, two is
`until doomsday and one believe two exist`

**4**  leave; but believe: I remit you, the Lord.
`leave but believe* I you remit-Lord`

**5**  And then the Lord Jesus: and the man who is carrying, who, Moses
`and_said Lord-Jesus and man^ exist carry who Moses`

**6**  abound; and from the man is this righteous teaching;
`abound* and from man^ exist this righteous teaching`

**7**  in turn, and the man is carrying, who, Moses abound
`in_turn and man^ exist carry who Moses abound*`

**8**  and from somebody is not this righteous learning. And then the Lord Jesus:
`and from somebody is_not this righteous on-learn and_said Lord-Jesus`

**9**  and the man is carrying, who, Moses writes, our
`and man^ exist carry who Moses write our`

**10**  good did; he shall see heaven, pleasing. In turn, and
`good ~do exist see heaven pleasing in_turn and`

> Matthew 5:19, "whosoever shall do and teach them, the same shall be called
> great in the kingdom of heaven", set against the one who teacheth not
> rightly. The negated *is not* on line 8 is Király & Tokai's own negated
> copula, which their entry cites at this very line.

## 109v — the end of the Matthew reading, and a new one from Luke

**1**  the man is not bringing, who, Moses abound | of
`man^ is_not bring^ who Moses abound* | of`

**2**  the man, good did, does not show the pleasing things of the Lord,
`man^ good ~do is_not show^ pleasing of-Lord`

**3**  the Father. Here ends this holy gospel. The Lord God: love the Lord God.
`the_Father here_ends this holy_gospel Lord_God love Lord_God`

**4**  Begins this holy gospel,
`here_begins this holy_gospel`

**5**  written by holy Luke,
`write holy-Luke`

**6**  in the ninth chapter of his writing.
`inside nine chapter <of>-write`

**7**  Then went the Lord Jesus
`time go Lord-Jézus`

**8**  to Jerusalem; and then went
`Jerusalem and then-exist go`

**9**  the Lord Jesus, of the olives, the mount, highest, Jerusalem town; and
`Lord-Jesus of_the_olives mount highest Jerusalem town and`

**10**  the Son of God showed down [over] Jerusalem town; and cried out | the Lord
`show^ son God down Jerusalem town and cry_out | Lord`

**11**  Jesus. And then: Jerusalem, Jerusalem! Then this Jerusalem [Bethphage] and this Jerusalem
`Jesus and_said Jerusalem Jerusalem then this-Jerusalem [Bethphage] and this-Jerusalem`

> Line 6 says Luke chapter nine, and the passage that follows is Luke 19:29
> onward, the mount of Olives and the weeping over Jerusalem. It is recorded
> as off. Line 7 does match Luke 9:51, "he stedfastly set his face to go to
> Jerusalem", so the compiler may have opened there and run on; that is a
> guess, and the citation stands as a miss either way. *Mount* and *of the
> olives* are both Király & Tokai's, cited by them at this line.

## 110r — if thou hadst known; the army that shall compass thee

**1**  […] because there is much misery upon this Jerusalem. Why? this | what
`[?] because exist many misery ~on-this Jerusalem why? this | what`

**2**  believe, who, this faith, the Jews, somebody, the apostles | of
`believe* who this faith* Jews-somebody apostle | of`

**3**  the Lord said; and who I preached, and this faith.
`Lord say and who I preach and this faith*`

**4**  And then the Lord Jesus: then I, the Son of God, crying
`and_said Lord-Jesus then I son God crying`

**5**  over this Jerusalem, because there shall come upon this Jerusalem [trench], an army; | this
`this-Jerusalem because exist on-this-Jerusalem [trench] an_army | this`

**6**  this shall sit about Jerusalem, and this Jerusalem [thine enemies] compass round;
`this to-sit Jerusalem and this-Jerusalem [?] surround`

**7**  [straiten thee] and thou art not, somebody, the angel, is
`[straiten_thee] and you is_not somebody angel exist`

**8**  somebody, the angel, out; and [stone], name, Jerusalem; but [visitation] among you
`somebody angel out and [stone] name-Jerusalem but [visitation] among you`

**9**  captured, all the Jews, on the cross crucified, somebody, the angel, and
`capture every-Jews on_the_cross crucify somebody angel and`

**10**  the Jews are, by hunger(?) die; and there is much misery on this
`~exist-Jews hunger? die and exist many misery ~on-this`

> Luke 19:41-44. "And when he was come near, he beheld the city, and wept
> over it ... For the days shall come upon thee, that thine enemies shall
> cast a trench about thee, and compass thee round, and keep thee in on
> every side ... because thou knewest not the time of thy visitation."
> *An army* on line 5 and *knewest not* on line 7 are both Király & Tokai's
> own signs, cited by them at these lines.

## 110v — Jerusalem destroyed by Vespasian and Titus, and the temple cleansed

**1**  Jerusalem; because this Jerusalem, all Jerusalem, destroyed the Roman general | Vespasi-
`Jerusalem because this-Jerusalem every-Jerusalem destroyed the_Roman general | Vespasi-`

**2**  -anus, and his son Titus; […] stone upon stone | shall not be
`+-anus son Titus +[?] stone on-stone | +shall_not_be`

**3**  left; [them that sold] faith. And the Lord Jesus went
`+left [?] believe and go Lord-Jézus`

**4**  into the Jerusalem temple; and then the Lord found within them that sold,
`inside Jerusalem temple and then-exist Lord inside +found ?them_that_sold`

**5**  the sellers of doves; and the Lord Jesus made of small
`seller_of_doves and do, Lord-Jézus +of_cords`

**6**  cords a scourge, and all the Jews [drove out], out.
`cords scourge and every-Jews [drove_out] out`

**7**  cast out, the Lord. And then the Lord Jesus: this is [the house of] prayer
`cast_out Lord and_said Lord-Jesus this_is prayer^`

**8**  this house; make it pleasing to the Lord, of
`house this house +<subj> do, on-pleasing <of>-Lord from`

**9**  God the Father; in turn you, the house, did, the Jews.
`God_the_Father in_turn you house do-Jews`

**10**  a den of thieves. And from thence the Lord Jesus, from
`one thief house and from-exist Lord-Jézus from`

**11**  until Palm Sunday, until many […]. The end of this | holy
`+until +Palm_Sunday +until many [?] end this | holy`

**12**  gospel.
`gospel`

> Luke 19:45-46 and John 2:15, "a scourge of small cords", "my house is the
> house of prayer: but ye have made it a den of thieves". Lines 1-3 name the
> Roman destruction of AD 70 with both emperors: Vespasian's name is written
> across the line break, and Király & Tokai's own entries give the name, the
> Roman, the destroying, and the "there shall not be left one stone upon
> another" of Matthew 24:2, which is also written across a line break.
> *Palm Sunday* on line 11 is theirs too. The reading ends there.

## 111r — the five sorrows of the Son of God

**1**  All the writings speak of five weepings of the Son of God. The first weeping
`every write speak five weep son God first weep`

**2**  of the Son of God: then the Lord God destroyed five towns;
`son God then destroy Lord_God five town`

**3**  and not only the weeping of the Lord's eye, but rather highest sad. The second weeping, the writing
`and not_only weep Lord eye but_rather* highest sad two weep write`

**4**  speaks of the birth at Bethlehem town, because
`speak on-~be_born Bethlehem town because`

**5**  the Lord Jesus foresaw, as on Holy […] [how often] suffering | on
`foresee Lord-Jesus as on_Holy [how_often] suffering | on`

**6**  the birth of the Lord. The third weeping, the writing speaks | on
`~be_born Lord third weep write speak | on`

**7**  Palm Sunday: then he sat, saw on the town,
`Palm_Sunday then sit see on-town`

**8**  Jerusalem; not only the weeping of the Lord Jesus for the house and for the building, literally, amid
`Jerusalem not_only weep Lord-Jesus to-house and to-+building literal amid`

**9**  the town, but the weeping of the Lord Jesus for the Lord's creation, who
`town but weep Lord-Jesus to-of-Lord create who`

**10**  the Lord created for the Lord, [wept], because the Lord Jesus foresaw then <subject marker>
`create-Lord to-Lord [wept] because foresee Lord-Jesus then SUBJ`

> The five weepings of Christ, a standing list in medieval preaching: at the
> Nativity, over Jerusalem on Palm Sunday, at the grave of Lazarus, on the
> cross. The codex gives all five across 111r-112v, numbering them. Palm
> Sunday on line 7 is Király & Tokai's own sign, cited by them at this line.

## 111v — Jerusalem falls, and a mother eats her son

**1**  the Jews, the people, go, all scattered. And then, on the putting to death of the Lord,
`Jews people go every scattered and then on-execute Lord`

**2**  Christ: ten and ten, and four years; then took the Lord God
`Christ +one-ten-+one-ten and two-two-year time grab Lord-<divine>`

**3**  power, the Roman general; and the general | and was
`power Roman general and general | and-exist`

**4**  by name Vespasian, and Titus; and these were
`exist-+name exist +Vespasian and Titus and this exist`

**5**  the father [and] son; and then the two, father [and] son, destroyed Jerusalem, all Jerusalem, [shall fall]
`the_father son and then two-father-son destroyed Jerusalem every Jerusalem [shall_fall]`

**6**  even to the ground; and stone upon stone shall not be left. And | two,
`until ground and stone on-stone +shall_not_be_left and | two`

**7**  father [and] son, many miseries on the Jews did, the son, the two, the father;
`father-son many misery on-Jews do-son-two-father`

**8**  because one of the Jews [said]: of hunger [we] die. The second of the Jews: how shall we, Jews,
`because one Jews hunger die second Jews how_shall_we-Jews`

**9**  hunger? [famine]; but of the Jews [the] son eat. The third of the Jews
`hunger [famine] but of-Jews son eat third Jews`

**10**  and the Jews, out […] Jews, and take heed, the Jews, the head.
`Jews and-Jews out [?]-Jews and °take_heed-Jews head`

> Lines 1-6 are the Roman siege, with both emperors named and the "stone upon
> stone" of Matthew 24:2 written across a line break. Lines 8-9 are the
> mother who ate her own child in the famine, from Josephus by way of the
> Golden Legend and the *Siege of Jerusalem* that every preacher carried.
> The count on line 2 is ten and ten and four; the tradition puts the fall
> forty-two years after the Passion, so the reading of the numeral does not
> match the tradition and is left as it stands.

## 112r — thirty Jews for one penny, because Judas sold for thirty

**1**  among the Jews captured, all the Jews on the cross put to death, but rather […] and
`among Jews capture every Jews on_the_cross execute °but_rather-[?] and`

**2**  is the head crucified [sold] the head; and the Jews could
`exist head crucify* [sold] head and Jews can`

**3**  the head [a penny] on finding; on it the Jews <subject marker>
`head [a_penny] on-find on-exist-Jews-+SUBJ`

**4**  put to death; the head […] <subject marker> sold, the head
`execute head [?]-+SUBJ sell head`

**5**  at thirty to one denarius; and the Jews <subject marker> | from
`on-thirty to-one denarius and-Jews SUBJ | from`

**6**  sold the head, remitted, town until town, went.
`sell* head remit town ~until town go`

**7**  took the head; and the Jews, nine hundred to thirty denarii;
`take* head and Jews nine hundred to-thirty denarius`

**8**  and the head <subject marker> more took, than was.
`and head SUBJ more grab than exist.`

**9**  Judas; and the Jews sold. The fourth weeping, the writing
`Judas and Jews sell second-two weep write`

**10**  speaks on Holy Tuesday: then Lazarus at the tomb called; not only the weeping,
`speak on_Holy_Tuesday = then Lazarus on-tomb called not_only weep`

> The legend that Titus sold thirty Jews for one penny because Judas sold
> Christ for thirty pence. It is in the Golden Legend's account of the
> destruction of Jerusalem, and line 9 names Judas and the selling in the
> same breath. Király & Tokai's denarius sign stands on lines 5 and 7, and
> their Holy Tuesday on line 10.

## 112v — the fourth and fifth sorrows: Lazarus, and Good Friday

**1**  the eye of the Lord Jesus, | than highest sad, because Lazarus [was sick], health among
`eye Lord-Jesus | than highest sad because Lazarus [was_sick] health among`

**2**  out, at the tomb; because three days was Lazarus in the tomb; and Lazarus
`out(ward) on-burial_chamber because +three_days exist +Lazarus inside burial_chamber and +Lazarus`

**3**  [was sick], health out, called. The fifth weeping, the writing
`[was_sick] health out called fifth weep write`

**4**  speaks on Good Friday: then Christ crucified, because to the high Lord
`speak on_Good_Friday = then Christ crucified because to-°high-Lord`

**5**  [not only] somebody, the Lord died; not only the weeping of the eye of the Lord Jesus, but highest sad,
`[not_only] somebody die-Lord not_only weep eye Lord-Jesus but highest sad`

**6**  sad for the people [groaned] in the Lord [troubled] believe; because foresaw | the Lord
`sad to people [groaned] inside-Lord [troubled] believe because foresee | Lord`

**7**  Jesus: then <subject marker> the Jews, the people, go, all scattered, because is
`Jesus then-+SUBJ Jews people go every scattered because-exist`

**8**  the Jews [looked up], heaven, Jerusalem. End [of] this apostle's holy gospel.
`Jews [looked_up] heaven Jerusalem end this apostle holy-gospel`

**9**  For on the day of judgment […] the angel divideth, the angel, the evil:
`because on-judge-year [?]-angel divide angel evil`

**10**  how? one sheep [wept]; one […] Jews
`how? one sheep [wept] one [?]-Jews`

> John 11:35, "Jesus wept", is the fourth sorrow, and Good Friday the fifth.
> Lazarus is named four times across these two folios in two spellings, both
> Király & Tokai's, cited by them at these very lines. Two words stand
> beside Lazarus on lines 1 and 3 that their apparatus cites here for a sign
> they gloss doubtfully as "recovery or health"; which of the two they meant
> cannot be told, so both are left unread.

## 113r — the division at the judgment, and the opening of the Prodigal Son

**1**  die; this is: in two divided, the firstborn sheep remitted;
`die this_is on-two divide firstborn sheep remit`

**2**  in turn this younger sheep remitted; this and the man divides
`in_turn this younger sheep remit this and man^ divide`

**3**  in the year of judgment: one gate into hell; the second gives within
`on-judge-year one gate on-hell second give^ inside`

**4**  the kingdom of heaven, but the Lord; there are many speak joy.
`heaven land ?but_rather-Lord exist many [?] joy`

**5**  Begins this holy gospel,
`begins this holy-gospel`

**6**  the writing, the holy gospel,
`write holy-gospel`

**7**  written by holy Matthew, in the first chapter
`write holy-Matthew inside +one chapter`

**8**  of his writing. Then
`<of>-write time`

**9**  said the Lord Jesus to his apostles
`say Lord-Jézus apostle <of>-Lord`

**10**  and the Jewish people: there was
`and Jew(ish) people exist`

**11**  one rich Lord God; and then the Lord God had two sons,
`one ~rich Lord_God and then have Lord_God two son`

**12**  the angel, the soul; and this younger son of the soul then asked for the soul's
`angel soul and this younger soul-son then-exist soul ask_(for)`

> Line 7 says Matthew, first chapter, and what follows is the Prodigal Son,
> Luke 15:11. It is recorded as off. The parable is told allegorically from
> the first line: the two sons are named the angel and the soul.

## 113v — the younger son takes his portion and wastes it

**1**  portion of the soul's son, of the Father; and then the son of the soul had much wealth,
`divide_into_parts <of>-soul-son father-<divine> and then-exist soul-son exist many ~rich`

**2**  took it of the Father; because the son of the soul rightly [substance] took of the Father this,
`grab father-<divine> because soul-son righteous(ly) [?] grab father-<divine> this`

**3**  of the soul's son, of the Father. And the son of the soul went far, into a | city
`<of>-soul-son father-<divine> and go soul-son far inside | town`

**4**  there was; and the son of the soul stayed in that land, and | began the soul's
`exist and leave soul-son inside land and | begin-soul`

**5**  son to waste it all; the son of the soul stayed in that land, because | began the soul's
`son from each,_every prodigalize leave soul-son this land because | begin-soul`

**6**  son to live riotously; and then, many years, the son of the soul stayed there. | In turn
`son +lived_riotously and then-exist many-year leave soul-son this | in_turn`

**7**  brother; and left; hunger this; and the soul-son
`brother and leave hunger this and soul-son`

**8**  how shall we eat? because remained […] | rich, eye, say, hear, love, have mercy
`how_shall_we* eat because remain-[?] | rich-eye-say-hear-love-have_mercy`

**9**  faith, righteousness: the five senses […]
`faith-true-+five-sense-[?]`

**10**  of the Father. And the son of the soul went to a swineherd, and
`father-<divine> and go soul-son one pigman and`

> Luke 15:12-15. *Lived riotously* and *be hungry* are both Király &
> Tokai's, each cited by them at exactly these lines. Lines 8-9 give the
> standard allegory: the substance the son wastes is the five senses, listed
> one by one and then named as five in a single compound sign.

## 114r — the swine, the husks, and "I will arise and go to my father"

**1**  son this swineherd, evil; and the son of the soul began
`[?] this pigman evil and begin-soul-son`

**2**  of the evil pig shepherded; and the soul-son, how shall we
`of-evil pig shepherded and soul-son how_shall_we*`

**3**  food? but the soul-son began, name from name, [husks], [swine], who | sinned
`food but begin-soul-son name-from-+name [husks] [swine] who | sin`

**4**  […] from, understood; and the soul-son began to speak: have | the Father
`[?]-from understand and begin-soul-son speak have | the_father`

**5**  God has labourers and servants, good, ascension,
`DIV of-soul-son labourer and servant good ascension^`

**6**  than this soul-son; ascension, and tasty bread [they] eat. Have mercy,
`than this-soul-son ascension^ and tasty bread eat have_mercy`

**7**  Lord God! The labourers, the servants, than this soul-son, eat. And then
`Lord_God labourer servant than this-soul-son eat and_said`

**8**  this younger son, this son of the soul, and the son of the soul went.
`this +the_younger_son this-soul-son and go-soul-son.`

**9**  the soul-son's Father; want [hired servants]; the soul-son, humbled, wants, the soul-son
`of-soul-son the_Father want [hired_servants] soul-son ~humble want-soul-son`

> Luke 15:15-18, the husks the swine did eat, and "how many hired servants
> of my father's have bread enough and to spare, and I perish with hunger!
> I will arise and go to my father." Király & Tokai's own hired-hand sign
> stands on lines 5 and 7, cited by them at these lines.

## 114v — the father sees him afar off; Father, I have sinned

**1**  mercy, this; and this younger son went to his
`have_mercy this and go this +the_younger_son to-<of>-soul-son`

**2**  Father God. And the son of the soul saw afar off, this, his
`father-<divine> and soul-son see far this <of>-soul-son`

**3**  Father God; and the son of the soul began recognize that, rightly,
`father-<divine> and soul-son begin-soul-son [?] +that righteous(ly)`

**4**  of his Father God, the son of the soul; and the son of the soul recognize that,
`<of>-father-<divine> soul-son and soul-son [?] +that`

**5**  God, the son of the soul; and the son of the soul went, this son of the soul, before
`God soul-son and go-soul-son this-soul-son before`

**6**  his Father God; and the son of the soul knelt down before
`<of>-soul-son father-<divine> and kneel_(down)-soul-son before`

**7**  his Father God; and the Father God began to pray, the Father God
`<of>-soul-son father-<divine> and father-<divine> begin pray father-<divine>`

**8**  of the son of the soul asked, this son of the soul; this Father had mercy on the son of the soul,
`<of>-soul-son ask_(for) this-soul-son this-father have_mercy-soul-son`

**9**  who, this son of the soul, through the sin of the soul against this Father and against the Lord God
`who this-soul-son through +sin-soul against this-father and against Lord-<divine>`

> Luke 15:20-21, "when he was yet a great way off, his father saw him, and
> had compassion", and "Father, I have sinned against heaven, and in thy
> sight". The parable is told with the son named "the son of the soul"
> almost every line, which is the allegory the page opened with on 113r.

## 115r — bring forth the best robe: of love, of mercy, of righteousness

**1**  and the son of the soul, mercy, this Father, of the son of the soul, all of the son of the soul,
`and soul-son have_mercy this father <of>-soul-son each,_every <of>-soul-son`

**2**  committed sin, who became through sin […]. And then this
`commit sin who become through ~sin-[?] and_said this`

**3**  soul-son's Father: labourers and servants, holy apostles, learning,
`of-soul-son the_Father labourer and servant holy-apostle-learn`

**4**  and the angel went, the apostles, the teaching, the angel; and | they brought, the apostles, the teaching,
`and angel go-apostle-learn-angel and | carry-apostle-learn`

**5**  the angel: fairest belief, the Lord's clothes, <subject marker> love, the Lord God;
`angel fairest believe Lord clothes SUBJ love Lord_God`

**6**  the Lord's clothes, <subject marker> have mercy, the Lord God; the Lord's clothes <subject marker> | the Lord God;
`Lord clothes SUBJ have_mercy Lord_God Lord clothes SUBJ | Lord_God`

**7**  the Lord's clothes, <subject marker> righteous, the Lord God. And the soul-son from | the Father,
`Lord clothes SUBJ righteous Lord_God and soul-son from | father`

**8**  apostles, learning, angels, angels, within the commandment to the Lord's clothes; and | the soul-
`apostle-learn-angel-angel inside commandment to-Lord clothes and | soul`

**9**  of the soul went, the apostles, the teaching, the angels, into his Father God's house; there is
`son go-apostle-learn-angel-angel inside <of>-father-<divine> house there exist`

> Luke 15:22, "bring forth the best robe, and put it on him", read
> allegorically: the robe is love, mercy and righteousness. Király & Tokai's
> own sign for "the most beautiful", which they gloss with the verse, stands
> on line 5, and the word after it is their clothes sign. That sign is a
> homograph in their dictionary, faith and clothes both, and they cite the
> clothes sense at lines 5 to 8. The rendering prints faith there; the robe
> is what the passage wants, and it is their reading either way.

## 115v — the elder brother in the field hears the music

**1**  joy for ever and ever, amen. And | among this.
`joy for_ever_and_ever = amen and | among-this.`

**2**  The father of the soul-son, the Father, all of God the Father's [elder son] [in the field]
`father of-soul-son the_Father every of-God_the_Father [elder_son] [in_the_field]`

**3**  friend; and began […] joy, the apostles, God the Father, learning, the angel.
`friend and begin-[?] ~joy apostle-God_the_Father-learn-angel`

**4**  from […] the word [music] and [dancing] [asked]; and then was this
`from-[?] word [music] and [dancing] [asked] and then-~exist this`

**5**  the firstborn brother [at] home, because [he] was in the field.
`firstborn brother home because-exist on-field`

**6**  That is: within, the angel's joy; and he heard a sound, | of
`that_is inside angel joy and hear voice,_sound | to-<of>`

**7**  the soul-son, the Father, heaven's house, that is, within heaven's | town
`soul-son the_Father heaven house that_is inside heaven | town`

**8**  it is. And the son of the soul went, dying, this younger son, to
`exist and go-soul-die-son this +the_younger_son on`

**9**  the soul-son's Father, heaven's house; and the angel went,
`of-soul-son the_Father heaven house and go-angel`

> Luke 15:25, "now his elder son was in the field: and as he came and drew
> nigh to the house, he heard musick and dancing". Király & Tokai cite their
> own field sign at line 5 with the verse named.

## 116r — he was lost, and is found; the end of the gospel

**1**  this angel, the firstborn brother, to the angel's Father.
`this angel-firstborn brother to-of-angel the_Father`

**2**  And then the angel's Father, the Father, of the angel [hath this world's goods]
`and_said of-angel the_Father the_Father of-angel [hath_this_world's_goods]`

**3**  this father, the angel, took one sheep, [it] died; and
`this father angel grab one sheep die and`

**4**  one loaf of bread, love was, this angel,
`one loaf +bread love-exist this-angel`

**5**  rejoice, the angel's friend; in turn on this the soul-son, joy,
`rejoice of-angel friend in_turn on-this soul-son joy`

**6**  the Father. And understanding he took from this Father: much wealth, the eye, speech, hearing,
`father and understand grab from this father many ~rich eye-say-hear`

**7**  love, mercy, belief, righteousness, the five senses. And then
`love-have_mercy-believe-righteous-+five-sense and_said`

**8**  this father, of the angel, the Father, the son of God the Father: lo,
`this father of-angel the_Father son of-God_the_Father lo`

**9**  there is the soul-son [who] was lost | released, the angel, God the Father […] labourer
`exist soul-son was_lost | release-angel-God_the_Father-[?]-labourer`

**10**  the servant; and the son of the soul was dead, and is risen from death, and is saved.
`servant-and soul-son exist die and ?rise on-die +be_saved`

**11**  The end of this holy gospel.
`end this holy-gospel`

> Luke 15:24 and 32, "this my son was dead, and is alive again; he was lost,
> and is found". *Was lost* is Király & Tokai's, cited by them at line 9,
> where the only other unread word is a compound ending in their hired-hand
> sign, which they cite at the same line. Lines 6-7 close the allegory by
> listing the five senses again, as 113v did.

## 116v — John the Baptist, and the soldiers and publicans who came to him

**1**  Before the gospel:
`before gospel-+<subj>`

**2**  written by holy John
`write holy-John`

**3**  the Baptist; this word writes.
`the_Baptist this word write`

**4**  Then it was,
`time then-exist`

**5**  the Lord Jesus within his twentieth
`Lord-Jézus inside two-ten-ten`

**6**  year and within the ninth year, within
`year and inside nine year inside`

**7**  that time preached
`time preach`

**8**  holy John the Baptist, on Carmel, to the mount; and he went.
`holy-John the_Baptist on-Carmel to-mount and go.`

**9**  To John four [peoples]: [publicans], soldiers, Pharisees, farmers, and sin
`to John two-two [publicans] soldier Pharisee farm and sin`

**10**  people; because there went soldiers, Pharisees, farmers, and sinners, to be taught
`people because exist go soldier Pharisee farm and sin on-learn`

**11**  by John on Carmel; and first the people were, the soldiers,
`to-John on-Carmel on first people exist soldier`

> Luke 3:12-14: "then came also publicans to be baptized ... and the
> soldiers likewise demanded of him, saying, And what shall we do?" The
> reading is ascribed on lines 2-3 to John the Baptist himself rather than
> to an evangelist and a chapter, which is not the book's usual formula.
> Carmel is Király & Tokai's gloss and it is Elijah's mountain, not the
> Jordan; that stands as the book has it. Lines 5-6 put the Lord in his
> twenty-ninth year, where Luke 3:23 says about thirty.

## 117r — John the Baptist answers the soldiers, and then the Pharisees

**1**  people; the second people are the Pharisees, the Jews; the third people are
`people second people exist Pharisee Jew third people exist`

**2**  the farmers, the people; the fourth people are the sinners.
`farm people second-two people exist sinners*`

**3**  First said the soldiers, the people: Master, the soldiers went to this John
`first say soldier people Master-soldier go-soldier this-John`

**4**  to learn on what? learning, are the soldiers: how shall we be saved? | from
`learn on what? learn exist soldier how_shall_we* be_saved | from`

**5**  [they] spoke. And to the soldiers, holy John the Baptist: of the soldiers' riches, and | of
`speak and soldier holy-John the_Baptist of-soldier ~rich and | of`

**6**  the soldiers' clothes, begin to give, soldiers, to God, [content], the poor man of God.
`soldier clothes on-begin donate soldier God [content] poor_man_of_God^`

**7**  and be merciful, soldiers, and righteous, soldiers; that is,
`and exist-soldier have_mercy-soldier and righteous(ly)-soldier exist ?is_he`

**8**  yours is the heavenly land. At that time said the Pharisees,
`yours heaven land time say Pharisee`

**9**  the Jews, to John: Master, the Pharisees went [to] | this
`Jew to-John Master-Pharisee go-Pharisee | this`

**10**  John to learn on what? learning, are the Pharisees: how shall we be saved?
`John on-learn on what? learn exist Pharisee how_shall_we* be_saved`

> Luke 3:10-14, "and the people asked him, saying, What shall we do then?",
> expanded into four questions and four answers, one for each of four
> estates: soldiers, Pharisees, farmers, sinners. Their give-alms sign
> stands on line 6, cited by them at that line. The pair after it is Király
> & Tokai's set phrase "poor man of God" (the pious poor, a beggar). An
> earlier version read it sign by sign as "God blind" here and at 099r,
> 117v, 139v, 140r and 201v; that was wrong.

## 117v — the Pharisees and the farmers get their answers

**1**  [they] spoke. And to the Pharisees, holy John the Baptist: and have this, Pharisees.
`speak and Pharisee holy-John the_Baptist and have this Pharisee.`

**2**  righteous people; preach, and teach the sinful; how is sin, from
`righteous(ly) people preach and sin learn how? exist sin from`

**3**  redeem; and be, Pharisees, merciful, Pharisees, and righteous, Pharisees; there is
`redeem* and exist-Pharisee have_mercy-Pharisee and righteous-Pharisee exist`

**4**  yours the kingdom of heaven. Then said the farmers,
`you +heaven land time say farm.`

**5**  the people, to John: Master, the farmers went [to] this John
`people to-John Master-farm go-farm this-John`

**6**  to learn on what? learning, are the farmers: how shall we be saved? [they] spoke.
`on-learn on what? learn exist farm how_shall_we* be_saved speak`

**7**  And to the farmers, holy John the Baptist: and have this, farmers; you
`and farm holy-John the_Baptist and have this-farm you`

**8**  farmers, farm, plough? and sow? and rightly, of the farmers, suffering
`farm farm plough? and sow? and righteous of-farm suffering`

**9**  living; and to the poor of God give alms; be ye farmers merciful, ye farmers,
`living and God blind donate exist-farm have_mercy-farm`

**10**  and righteous, ye farmers; yours is the kingdom of heaven.
`and righteous(ly)-farm exist you +heaven land`

> Line 8 is Luke 3:13 turned into a farmer's rule, and line 9 repeats the
> alms of 117r:6. The closing formula is identical in all four answers, and
> it is that repetition which proves the pronoun read *yours* on 117r:8: the
> other three write Király & Tokai's own word for "you" in the same slot.

## 118r — and the sinners, who get the great commandment

**1**  At that time said the sinners: Master, the sinners | went
`time say sinners* Master-?sinners | go`

**2**  the sinners [to] this John to learn on what? learning, are
`sinners* this-John on-learn on what? learn exist.`

**3**  the sinners: how shall we be saved? [they] spoke. And to the sinners
`sinners* how_shall_we* be_saved speak and sinners*`

**4**  holy John the Baptist: and have, sinners; love the Lord God
`holy-John the_Baptist and have sinners* love Lord_God`

**5**  most high [with] all [your] hearts, all the sinners' souls, all the sinners'
`most_high all^ create all^ of-?sinners soul all^ of-?sinners`

**6**  might, all your heart; and your
`might each,_every <of>-?sinners heart and <of>-?sinners`

**7**  brother as somebody [his] neighbour; be, sinners, | merciful
`brother as somebody neighbour exist-?sinners | have_mercy`

**8**  sinners, and righteous, sinners; and keep, sinners,
`?sinners and righteous(ly)-?sinners and carry ?sinners`

**9**  the commandments of God; […] a hundred […] sins, and be saved, sinners,
`commandment God ~exist-hundred-[?]-+sin be_saved ?sinners`

**10**  [with all thy strength], suffering, for ever and ever, amen; there is
`[with_all_thy_strength] suffering for_ever_and_ever = amen exist`

> The fourth answer is the great commandment, Deuteronomy 6:5 and Luke
> 10:27, with the Sursum corda of line 5, "lift up your hearts", which is
> where that phrase was first read in this project.

## 118v — the commandment summed up, and a new reading from Luke

**1**  yours the kingdom of heaven. This teaching is [murmured] not love the Lord
`you +heaven land this learn exist [?] [?] love Lord`

**2**  the divine one highest [above] every creature; and the man is keeping the commandments of God, ours,
`DIV highest every create and man^ and exist carry commandment God our`

**3**  is the kingdom of heaven. And this is: this love, the commandment, take
`+<subj> +heaven land and +this_is this love commandment grab`

**4**  from […] to be saved; and the man who believeth
`from [?] on-be_saved and somebody and exist believe`

**5**  in the Lord Jesus Christ, as the true Son of the living God, everybody
`inside Lord-Jesus-Christ as righteous son living God everybody =`

**6**  shall be saved; and one is not damned but: every man shall be saved.
`+be_saved and one +is_not be_damned [?] each,_every somebody +be_saved`

**7**  Begins this holy gospel, written by holy Luke, in the seventh chapter of
`begins this holy-gospel write holy-Luke inside +seven chapter <of>`

**8**  his writing. At that time the Lord Jesus [was] within [his] thirty-first year;
`write time then Lord-Jesus inside thirty one-~year`

**9**  then went the Lord Jesus into the Pharisees' town; and there went
`time go Lord-Jézus inside Pharisee town and go`

**10**  to the Lord various sinners, to the Lord Jesus; and
`to-Lord various sinners* to Lord-Jesus and`

> Lines 9-10 are Luke 15:1-2, "then drew near unto him all the publicans and
> sinners ... and the Pharisees and scribes murmured", which is the setting
> of the Lost Sheep on 119r. Line 7 cites Luke chapter seven, and the
> passage is Luke 15. It is recorded as off. Line 6 is Mark 16:16.

## 119v — the lost sheep found, and the woman with ten pieces of silver

**1**  our shoulder; and somebody goes to our friends and neighbours,
`our shoulder and go-somebody to-our friend and neighbours`

**2**  and he is, with friend and neighbour; he said to them: I have found,
`and exist and-friend-neighbor say-somebody say exist +found`

**3**  somebody's sheep [which was lost]; somebody is this, this; wish; and
`somebody sheep [which_was_lost] somebody exist this-this wish and`

**4**  good on the sheep, joy; but on the ninety-nine sheep.
`good on-sheep joy ~but on-nine-ten and nine sheep`

**5**  And then the Lord Jesus: then one woman, the head,
`and_said Lord-Jesus then one woman ~head`

**6**  and is having ten silver [coins]; and then of these ten, lost
`and exist have ten silver and then this ten lost`

**7**  Eve; and there is light, Eve, the son of Mary,
`Eve and exist light Eve Mary-son`

**8**  born, crucified, the lamp; and then Eve findeth
`be_born-+crucified lamp and then-exist find Eve`

**9**  this silver [coin], the heavenly land; and there is good,
`this silver heaven land and exist good`

**10**  over heaven, the kingdom, joy, Eve; over the Lord Christ's dying,
`on-+heaven land joy Eve on-die-Lord-Christ`

> Luke 15:6, "rejoice with me; for I have found my sheep which was lost",
> then Luke 15:8, the woman with ten pieces of silver who lights a candle
> and sweeps the house. *Found*, *neighbours* and the exclamation *oh* are
> all Király & Tokai's, each cited by them at exactly these lines. The
> woman is read as Eve and the candle as Christ born and crucified, which
> is the standard allegory of that parable.

## 120r — the ninety-nine, and the nine orders of angels

**1**  Eve rejoices, than on food nine drachmas; commandment. End
`Eve rejoice^ than on-food nine drachma commandment end`

**2**  [of] this holy gospel. Then the Lord [telleth], the Lord Jesus [until] the sufferer.
`this holy-gospel then-Lord [telleth] Lord-Jesus [until] sufferer`

**3**  The gospel: said the Lord Jesus [to] the Lord's apostles and the Jews, the people: I
`gospel say Lord-Jesus apostle of-Lord and Jew people I`

**4**  one Lord, this sheep; because to the Lord, I | abandon
`one Lord this sheep because to-Lord I | abandon`

**5**  the Lord, the nine orders of angels within the kingdom of heaven.
`Lord nine order angel inside +heaven land`

**6**  And then the Lord Jesus: then the Lord created, the Father,
`and_said Lord-Jesus then-Lord create the_Father`

**7**  heaven; on the heavenly land, on the Holy angels,
`heaven on-heaven land on_Holy angel`

**8**  upon the angel whose name is Lucifer, and the second
`on angel +name exist hide_oneself-angel and two`

**9**  angel, and Lucifer prayed; and forty years
`angel and Satan ~pray and ten-ten-ten-ten-year`

> The ninety-nine sheep left in the wilderness are read as the nine orders
> of angels, the one lost sheep as mankind: the standard exposition of Luke
> 15:4, and the reason the codex keeps the number nine through both
> parables. Lines 8-9 turn to the fall of Lucifer. His name is two signs
> that Király and Tokai read together as one word, *Satan, Lucifer* (004v10);
> an earlier printing here called him "the hidden angel", which was wrong.

## 120v — the fall of Lucifer, and the order left empty

**1**  and forty, and night, which Lucifer, to Lucifer,
`and ten-ten-ten-ten and night which-Satan to-Satan`

**2**  on the heavenly land, on hell, redeem <subject marker> one
`on-heaven land on-hell redeem* SUBJ one`

**3**  order, the year, the chapter, from; and then I went, the Lord, the Father,
`order ~year-chapter from* and then I go-Lord the_Father`

**4**  of the Lord; from I, the Lord wanted [the tenth] half order of angels; and from
`of-Lord from I want-Lord [the_tenth] half order angel and from`

**5**  the ascension of the Lord until the year of judgment wanted the Lord, of the Lord | from
`ascension of-Lord ~until judge-year want-Lord of-Lord | from`

**6**  the Father God, [the tenth] from the order, in the place [shall stand empty] there is
`father-<divine> [?] from order on-place [?] +<subj> exist`

**7**  the Lord, the Lord bowed down, the Father of the Lord, on the heavenly land,
`Lord bow-Lord the_Father of-Lord on-heaven land`

**8**  on hell; then | went the Lord, God the Father, the Son, God, Jesus, the Holy Spirit,
`on-hell then | go-Lord-God_the_Father-son-God-Jesus-holy-spirit`

**9**  Mary, Christ, the apostles, the angels judge living, and dying redeem [shall fill it]
`Mary-Christ-apostle-angel [?] living and die [?] [?]`

> Lucifer falls and his order stands empty until the judgment; the lost
> sheep of 119r-120r is man, brought in to fill it. That is why the codex
> keeps the number nine through both parables. Király & Tokai's own
> "[angelic] order" sign stands on lines 3, 4 and 6, cited by them at each.

## 121r — the tenth order, and the drachma that was lost

**1**  I am judging, the Lord, of the Lord the Father, on the sheep,
`exist I judge-Lord of-Lord the_Father on-sheep`

**2**  the righteous people; and believe in the divine one, and in the Lord's Father, many
`righteous people and believe inside divine_one^ and inside of-Lord the_Father many`

**3**  judge, and the neighbours, and the friends, the angels, and the apostles, for ever and ever,
`judge and neighbours and friend angel and apostle for_ever_and_ever =`

**4**  amen. And then the Lord Jesus: this woman, this is of the Lord's
`amen and_said Lord-Jesus this woman this_is of-Lord`

**5**  creation; you, mother Eve; from Eve <subject marker> | is
`create you mother Eve from Eve SUBJ | exist`

**6**  Eve lost one; Eve, one silver [coin], one
`Eve loseth_one-Eve one silver one`

**7**  order, the order within the kingdom of heaven; because then
`order order inside heaven land because then`

**8**  bowed, the Father, heaven, on the Holy angels, on heaven.
`bow the_Father heaven on_Holy angel on-heaven.`

**9**  land, on hell. And then the Lord Jesus said: there is
`land on-hell and_said Lord-Jesus say exist`

> The woman of Luke 15:8 who loses one of ten pieces of silver is read as
> God losing one of ten orders: nine of angels and the tenth of men. It is
> the standard exposition, and it is why 120r counted nine orders.

## 121v — the Trinity: Father, Son and Spirit, and one God

**1**  from the Father to the Son goes the Holy Spirit; Father, Son, creation, man.
`the_Father to-son go holy-spirit father son create man^`

**2**  And then the Father, the Holy Spirit: on how the man [was] imaged
`and_said the_Father holy-spirit on-how? man^ image^`

**3**  [they] would like, Father, Son, Spirit, create. And then the Son | on the
`would_like^ father son spirit create and_said son | on-of`

**4**  image [after our] [likeness]: man is, all one, to
`shape,_form [?] [?] exist somebody each,_every one to`

**5**  the Father, the Son, the Spirit. Father, Son and Spirit took man,
`father son spirit grab father son spirit somebody`

**6**  and every cattle [creature]; the soul heard; the man saw rightly; not
`every cattle^ [creature] soul hear man^ see righteous not`

**7**  many [in] the Father, from the Son; not many the Holy Spirit; but
`many the_father from son not many holy-spirit but`

**8**  this Lord is all one God. And then the Lord Jesus went out, the Lord.
`this Lord every one God and_said Lord-Jesus go_out-Lord`

**9**  Father, Son and Spirit, out, into the kingdom of heaven, into this world.
`father son spirit out(ward) on-heaven land on-this ?world`

> Genesis 1:26, "let us make man in our image", with the Trinity formula the
> book repeats: not many, one God. This page is the same passage as 002v,
> written a second time, and it reads further than 002v does.

## 122r — the Lord God forms Adam and breathes into him

**1**  And out of Paradise the Lord God, the man, created, slime (of the earth)
`and out Paradise Lord_God man^ create slime_(of_the_earth)*`

**2**  And then the man was, created, aforesaid, [breathed], and
`and then man^ exist create aforesaid [breathed] and`

**3**  became one soul, created; breathed on Adam; and
`became* to-soul-+one create breathe on-Adam and`

**4**  he became living. And the Lord, the Father, the Son took the man.
`living leave and man^ take^ Lord-father son.`

**5**  the Spirit; and the man went, the Lord, the Father, the Son, the Spirit,
`spirit and man^ go Lord-father son spirit`

**6**  within Paradise; and every creation before the man,
`inside Paradise and every create before man^`

**7**  created, Lord, Father, Son, Spirit. And then the Lord Jesus said: the Father
`create Lord-father son spirit and_said Lord-Jesus say the_father`

**8**  of the Lord God, heaven, the man, name […] this Adam
`of-Lord God heaven man^ name-[?] this-Adam`

**9**  took all rightly [nor] hunger and thirst [nor] this Adam;
`grab each,_every righteous(ly) [?] be_hungry and thirsty [?] this-Adam`

> Genesis 2:7, "the LORD God formed man ... and breathed into his nostrils
> the breath of life; and man became a living soul", then Genesis 2:15, "the
> LORD God took the man, and put him into the garden of Eden". These lines
> are word for word the same as 002v:9-12, which was translated earlier and
> read much less far. The sign rendered *heart* stands five times here where
> Genesis wants dust, breath and life, and that use of it was already
> flagged as unexplained when the sign was read; more of it is on the record
> now and it is still unexplained.

## 122v — the commandment, the sleep, and the rib

**1**  and one living [thing] dies, sins, has hunger, thirsty, to the girl.
`and one living-die-sin have hunger thirsty girl-to.`

**2**  [afterward] the Lord took, this Adam, all rightly one:
`[?] grab Lord this Adam each,_every righteous(ly) one`

**3**  the commandment, this yoke, this Adam, command: do not eat
`commandment this yoke this Adam command = do_not eat`

**4**  this [fruit] of the son, the forbidden fruit; thou shalt die. If Adam is eating,
`this to-~son forbidden_fruit thou_shalt_die* ~if Adam exist eat`

**5**  in that place, and died. And then Adam slept, into Paradise;
`on-place die and then-exist Adam sleep inside +into_Paradise`

**6**  and then the first table, from the hour; and then went the Holy Spirit
`and then table first from hour and then go holy-spirit`

**7**  within Paradise. And then this <subject marker> this, the garden; and
`inside Paradise and_said this SUBJ this the_garden and`

**8**  the Lord God took from Adam a rib; and Eve created.
`grab Lord_God Adam rib and Eve create`

**9**  And then the Lord Jesus: you, mother. And then Adam
`and_said Lord-Jesus you mother and then Adam`

> Genesis 2:17 and 2:21-22. *Do not*, *the garden* and *rib* are all Király
> & Tokai's, each cited by them at this line and at the matching line of the
> first copy on 003r. The whole page is the second copy of 003r.

## 123r — bone of my bones, and the serpent

**1**  from laughing; and then this: bone of bones. In turn, two souls,
`from laugh and_said this bone bones in_turn two soul`

**2**  one brother by name. And then the Lord Jesus left, the Lord God the Father.
`one ~brother-+name and_said Lord-Jesus leave Lord-God_the_Father`

**3**  the Son, the Spirit, into the kingdom of heaven; and there went
`son spirit on-heaven land and go`

**4**  Eve in Eden; and then Eve,
`Eve on-Eden and then Eve`

**5**  Eve went to this tree, what tree;
`Eve go to this tree what tree`

**6**  it is the Lord God's through commandment; and [she] saw a serpent. And then this serpent: Eve,
`exist Lord_God through commandment and see one serpent and_said this serpent Eve`

**7**  eat this fruit. And then Eve: [we] shall not eat, eat,
`eat this fruit and_said Eve shall_not_eat eat`

**8**  because Eve, Adam, Master, command. And then
`because Eve Adam Master command = and_said`

**9**  this serpent: Eve, eat; Eve, Adam.
`this serpent Eve eat Eve Adam`

> Genesis 2:23 and 3:1-6. *Laugh* and *bone* are Király & Tokai's, cited by
> them at this line and at 003r:12 and 003v:1, the matching lines of the
> first copy. The tree that stood in the midst is Genesis 3:3, and the
> answer on line 7 is Eve's, "ye shall not eat of it, neither shall ye touch
> it, lest ye die".

## 123v — she took of the fruit, and their eyes were opened

**1**  this; in turn the fruit <subject marker> is; Eve, one; Adam eats.
`this in_turn fruit SUBJ exist Eve one Adam eat`

**2**  Eve is, Adam; they knew evil and good, how
`exist Eve Adam know evil and good how?`

**3**  to the Lord God it is known. And then she plucked, the serpent, this
`to Lord-God know and then-exist pluck serpent this`

**4**  [beguiled], this serpent; and then Eve took,
`[beguiled] this serpent and then grab Eve`

**5**  in turn Eve, the fruit; Adam took [it]; and then
`in_turn Eve fruit grab Adam and then`

**6**  were opened in the place: Adam naked; Eve saw
`were_opened* on-place Adam naked see Eve`

**7**  Adam; and then Eve [and] Adam were ashamed.
`Adam and then Eve Adam be_ashamed`

**8**  And then the Lord Jesus: and this, on dying, sin, hiding, did.
`and_said Lord-Jesus and this on-die ~sin-hide do`

**9**  Satan; the Lord, Father, Son, the Spirit of God, of the Lord, somebody, the Father
`Satan Lord-father son Spirit_of_God^ of-Lord somebody the_Father`

> Genesis 3:6-7, "she took of the fruit thereof, and did eat, and gave also
> unto her husband ... and the eyes of them both were opened, and they knew
> that they were naked". The same sentences stand at 001r and 003v, which
> the repeat-finder pairs with this page.

## 124r — Adam, where art thou?

**1**  who <subject marker> Satan is, put off [by] God the Father from heaven; | in turn, chapter,
`who-+SUBJ Satan exist put_off God_the_Father on-heaven | in_turn-chapter`

**2**  the year is on hell. And then the Lord Jesus left, the Lord, Father, Son,
`~year-exist on-hell and_said Lord-Jesus leave Lord-father son`

**3**  the Spirit of God, into heaven, land, within Eden.
`Spirit_of_God^ on-heaven ~land inside Eden`

**4**  And then the Lord Jesus: this second table, from the hour; and then
`and_said Lord-Jesus this table two from hour and then`

**5**  left, the Lord, the Father, the Son, the Spirit; left into the kingdom of heaven,
`leave Lord-father son spirit leave on-heaven land`

**6**  into Paradise; he said: there is [down] | of […].
`inside into_Paradise say exist [down] | of-[?].`

**7**  the Spirit of God to Adam: Adam, why? And then
`Spirit_of_God^ to-Adam Adam why? and_said`

**8**  Adam hid; Adam; the Lord God said, | the Lord, Father, Son,
`Adam hide Adam Lord_God say | Lord-father-son`

**9**  the Spirit of God: why, Adam, hide? said Adam
`Spirit_of_God^ why? Adam hide say Adam`

> Genesis 3:9, "And the LORD God called unto Adam, and said unto him, Where
> art thou?" The book gives the question with the Trinity as the speaker,
> as it has all through the creation.

## 124v — the woman gave me, and the serpent beguiled me

**1**  who, this Adam, naked, said [to] the Lord, Father, Son, Spirit:
`who this-Adam naked say Lord-father-son-spirit`

**2**  why? Adam naked said: Adam, Eve,
`why? Adam naked say ~Adam Eve`

**3**  Adam, she gave me to eat. Said the Lord, the Father, the Son, the Spirit: Eve,
`+Adam +gave_to_eat say Lord-father-son-spirit Eve`

**4**  where? said; Eve, which Eve, to me said.
`where? say Eve which Eve I-to say`

**5**  The Lord, Father, Son, Spirit: why? Eve, which, who.
`Lord-father-son-spirit why? Eve which who.`

**6**  who? Eve naked said [to] the Lord, Father, Son, Spirit:
`who Eve naked say Lord-father-son-spirit`

**7**  why? Eve naked said: Eve, the serpent,
`why? Eve naked say Eve serpent`

**8**  Eve, food. Said the Lord Jesus, said: there is, of the Lord,
`Eve food say Lord-Jesus say exist of-Lord`

**9**  the Father, to Adam: Adam, to one
`the_Father to-Adam Adam to-one`

> Genesis 3:12-13, "The woman whom thou gavest to be with me, she gave me of
> the tree, and I did eat" and "The serpent beguiled me, and I did eat".
> *Adam* and *gave me to eat* on line 3 are Király & Tokai's own, both cited
> by them at that line.

## 125r — to till the ground, and the sorrow

**1**  commandment; this Adam is, name […] ten commandments carry, is
`commandment this-Adam exist name-[?]-ten commandment carry exist`

**2**  Adam, to the girl, on Adam's; in turn, chapter, who.
`Adam girl-to on-of-Adam in_turn chapter-~who.`

**3**  gates Adam is, the earth, to till the ground;
`[?] exist Adam earth +to_till_the_ground`

**4**  wanted to take food to the son; in turn Eve this;
`want to-~son food take^ in_turn Eve this`

**5**  Eve is through pining, and this Eve
`[?] exist through +pine and this [?]`

**6**  is painful, born, he hath; in turn this evil
`exist painful ~be_born have in_turn this evil`

**7**  is [cursed] the earth, the serpent slideth, and
`exist [?] earth slide and`

**8**  a room for evil; this man was made, all of this; the serpent
`+room evil this somebody create each,_every this serpent`

> Genesis 3:17-19 and 3:23, "in sorrow shalt thou eat of it all the days of
> thy life ... to till the ground from whence he was taken". *To till the
> ground* is Király & Tokai's own expression, which they cite at line 3, and
> *pine* is their second sense of thirst, cited at line 5. This page is the
> second copy of 007r, and it reads a good deal further than 007r does.

## 125v — driven out, and the flaming sword

**1**  dieth; and [it] became among Adam and Eve
`die and become^ among Adam_and_Eve`

**2**  of the Lord, Father, Son, God, Spirit, the Father God, Jesus, the angel,
`of-Lord father son God spirit the_father God Jesus angel`

**3**  the Virgin Mary, Christ, and the apostles, and the Jews, and the man baptized, and all.
`Virgin_Mary Christ and apostle and Jew and man^ ~baptize and every.`

**4**  [he drove out]; and all the heavenly land, the Lord, and the Lord's creation,
`[he_drove_out] and every heaven land Lord and Lord-create`

**5**  all the earth, and hell, and the heavenly land;
`every earth and hell and heaven land`

**6**  and there went the Lord God, the angel, the second, the earth, and
`and go Lord-<divine> angel two earth and.`

**7**  Eve, flame, the sword, and | earth
`Eve flame^ sword and | ~earth`

**8**  [were] out; from the Garden of Eden they were cast out.
`slide out(ward) on-inside Garden_of_Eden exorcise`

> Genesis 3:24, the flaming sword. *Sword* is Király & Tokai's, in a
> spelling their entry cites at this line and the next page's. The sign
> that runs from line 7 into line 8 is Király & Tokai's aggregate *two +
> Adam + Eve*, Adam and Eve, which they cite here and at 007r10. Corrected
> 2026-09-26: the earlier printing had the serpent here, and the correction
> made the same day read the sign as Adam alone, sliding out; both were wrong.
> Other reading: the aggregate is split here by the line break, and the sign
> heading line 8 is, on its own, Király & Tokai's *slide [snake]* (which they
> cite only at 007r06 and 125r07). Read that way, line 8 says the serpent
> slid out and was cast from the garden.

## 126r — the cherub at the gate, and the third saying

**1**  And [he] placed the angel with the sword at the gate; Eve,
`and place^ angel sword on-gate Eve`

**2**  of Eden; and one creature can be within
`Eden and one create can_be inside`

**3**  Eden; but the angel. And then the Lord Jesus:
`Eden but angel and_said Lord-Jesus`

**4**  this third table, from the hour, said the Lord Jesus: this <subject marker> this
`this table three from hour say Lord-Jesus this SUBJ this`

**5**  silver [coin]; and it is lost then, from the forbidden fruit, [which] the two ate.
`silver and exist lose then from forbidden_fruit eat two`

**6**  Adam; and Eve and Adam slid out;
`~Adam and [?] and ~Adam slide out(ward)`

**7**  cast out, the Lord, the Father, the Son, the Holy Spirit; and then hell,
`exorcise Lord-father son holy-spirit and then-exist hell`

**8**  the evil; from Adam and Eve taken, from the good,
`evil from Adam_and_Eve take^ from good`

**9**  one commandment of God; which chapter Adam and Eve had.
`one commandment God which-chapter Adam_and_Eve have`

> Genesis 3:24, "he placed at the east of the garden of Eden Cherubims, and
> a flaming sword which turned every way". Line 5 ties the whole Adam
> narrative back to the lost drachma of Luke 15:8, which the book expounded
> on 121r: the coin God lost is man, lost here. This page is the second copy
> of 007v. The sign printed *the serpent* on lines 8 and 9 is the aggregate
> *two + Adam + Eve* that Király & Tokai parse at 007r and 125v. Corrected
> 2026-09-26: the earlier printing, and Book One, read the serpent.
> Other reading: *slide [snake]* is the last part of the sign; read as the
> serpent, line 8 says the serpent took Adam and Eve from the good.

## 126v — the Lord seeks the drachma he lost

**1**  The Lord, the Father, the Son, the Spirit, took what was lost; | Adam
`Lord-father son spirit exist grab lose | two-~Adam`

**2**  slide. Said the Lord Jesus: then the two could not find.
`slide say Lord-Jesus then-not two can find.`

**3**  Every house this | redemption; not have mercy on the angel of the Lord,
`every house this | redemption not have_mercy on-angel of-Lord`

**4**  the Father; could, woman, find redemption? not.
`the_Father can ~woman find redemption not`

**5**  [He] was born [of a] mother, of the Lord's love, and redemption; I, from a mother,
`exist be_born mother of-Lord love and redemption I from mother`

**6**  [again] was born; and redemption, I, on the cross [thereon]; in turn
`[again] be_born and redemption I on_the_cross [thereon] in_turn`

**7**  then […] on the cross; from [there] want to find this silver [coin], this heaven
`then-[?] on_the_cross from want find this silver this heaven`

**8**  kingdom […] there is, from Adam and Eve;
`land [?]-+SUBJ exist from Adam_and_Eve`

**9**  abandon Satan. And said the Lord Jesus: I want, the Lord,
`abandon Satan and say Lord-Jesus I want-Lord`

**10**  to take the trespass and redeem, the Lord, of the Lord's Father in heaven.
`trespass grab and ~redeem-Lord of-Lord the_Father heaven`

> The lost coin of Luke 15:8 expounded a third time: God lost it in Eden,
> and finds it by the Incarnation and the cross. *Redemption* and *find* are
> both Király & Tokai's, and their entries cite lines 2 to 7 here one by one.
> Lines 1-2 and 8 hold the aggregate *two + Adam + Eve* (Király & Tokai, at
> 007r and 125v). Corrected 2026-09-26: the earlier printing, and Book One,
> read it as the serpent. Other reading: on lines 1-2 the line break splits
> the aggregate, and line 2 opens with *slide [snake]* on its own; read so,
> what was lost was lost through the serpent.

## 127r — Hezekiah is told he shall die, and is given more years

**1**  said within a dream God's angel
`say inside dream God angel`

**2**  to holy Hezekiah
`holy-Hezekiah`

**3**  the prophet; Hezekiah,
`prophet Hezekiah`

**4**  the Lord God, this is, saith the Lord:
`Lord-<divine> +this_is say-Lord`

**5**  within three days, this | one
`until +three_days | this`

**6**  shall die. And then
`+<subj> die and then-exist`

**7**  from laughter, holy Hezekiah
`from +laugh holy-Hezekiah`

**8**  began, Hezekiah, to be sad,
`begin Hezekiah sad(ly)`

**9**  holy Hezekiah; and cried out: who [will] prepare, chapter, to, and
`holy-Hezekiah and cry_out who prepare-chapter-to-and`

**10**  there went to Hezekiah the Creator Lord; and the rest said God's angel:
`go to-of-Hezekiah Creator_Lord and the_rest^ say God angel`

**11**  Hezekiah, the Lord God, this is, says: prolong life, chapter, to, and is
`Hezekiah Lord_God this_is say prolong_life-chapter-to-and exist`

**12**  until five [and] fourteen years(?) living, chapter, to, and; and prolong life.
`until five-fourteen-?years living-chapter-to-and and prolong_life`

> Isaiah 38 and 2 Kings 20:1-6: "Set thine house in order: for thou shalt
> die, and not live ... I have heard thy prayer, I have seen thy tears:
> behold, I will add unto thy days fifteen years." The numeral on line 12
> does not resolve to fifteen: it is five strokes, then Király & Tokai's
> sign for fourteen, then one more stroke and the year terminator. It is
> recorded as unresolved rather than forced to fit the verse.

## 127v — Hezekiah dies, and Paul sets his house in order

**1**  Made ready, holy Hezekiah; and upon […]
`prepare holy-Hezekiah and on-[?]`

**2**  Hezekiah's soul gave out; and then, chapter, to, and
`of-Hezekiah soul give_out and then-chapter-to-and`

**3**  Hezekiah's soul gave out; at that time appeared.
`of_Hezekiah soul give_out time appear.`

**4**  the angel of God, and said to the servants: of Hezekiah, lay him.
`God angel and say servant +of_Hezekiah put.`

**5**  this body within the tomb; in turn the soul of Hezekiah | this
`this body inside tomb in_turn soul Hezekiah | this`

**6**  the angel wanted, the angel, to give; and the angel left,
`angel want-angel give^ and leave angel`

**7**  in turn holy Hezekiah's body within the tomb put.
`in_turn holy_Hezekiah body inside tomb put.`

**8**  The servants speak; holy Paul apostolic letter [writeth] the brethren of Paul
`servant speak holy-Paul [?] [?] brother <of>-Paul`

**9**  […] and Paul made ready, of Paul, the last day.
`~have-[?] and Paul prepare of-Paul last day^`

> Three spellings of Hezekiah's name stand on this page, all of them Király
> & Tokai's with one glyph changed. Paul comes in on line 8 as the second
> example: the man who set his house in order at the end, 2 Timothy 4:6-7.

## 128r — Paul's one only Son, and a new reading begins

**1**  as is prepared, Hezekiah, holy Hezekiah
`as exist prepare-Hezekiah holy-Hezekiah`

**2**  the prophet; this [foretold] has; and Paul, somebody, prepared, to
`prophet this [foretold] have and Paul-somebody prepare to`

**3**  the Lord Jesus, the Son of God, of Paul, the man, the one only,
`Lord-Jézus son God <of>-Paul-somebody one only_one`

**4**  brother went, this somebody, because [he] lost [the sheep]
`brother go-this-somebody because lose [the_sheep]`

**5**  Begins this | holy
`begins this | holy`

**6**  gospel, written | by holy
`gospel write | holy`

**7**  Luke, in the first chapter, in
`Luke inside +one chapter inside`

**8**  his writing. Then,
`<of>-write time`

**9**  then on crucifying,
`then on-crucify`

**10**  the Lord Christ, three days
`Lord Christ +three_days`

> Line 7 cites Luke, first chapter, and the reading that follows is the
> appearance in the upper room after the resurrection, which is Luke 24.
> It is recorded as off.

## 128v — they were terrified, and believed not for joy

**1**  another night; then appeared
`[?] night time appear`

**2**  the Lord's apostles, the gate. And then the Lord Jesus: the commandment | you, chapter
`apostle of-Lord gate and_said Lord-Jesus commandment | ~you-chapter`

**3**  [so] he is; and through, the apostles were startled, because
`[?] exist and through startle apostle because`

**4**  the apostles believed as how? a ghost. And then
`believe apostle as how? ghost and_said`

**5**  the Lord Jesus had the apostles; the Lord, he; the apostles saw within | is
`Lord-Jesus have-apostle Lord he see-apostle inside | exist`

**6**  is, chapter, somebody [a spirit], the angel, body.
`exist-chapter somebody [a_spirit] angel body`

**7**  in turn, one ghost; could the apostles, the Lord,
`in_turn one ghost can apostle Lord`

**8**  because the Lord, who I, I to you,
`because* Lord ~who-I I to-you`

**9**  through be thirty days and three, and literally
`[?] stay thirty +day and +three and literal`

> Luke 24:36-41: "they were terrified and affrighted, and supposed that they
> had seen a spirit ... and while they yet believed not for joy, and
> wondered". Line 4 gives "believed not for joy" almost word for word.

## 129r — receive ye the Holy Spirit, and go into all the world

**1**  and the apostles can, because the Lord Jesus, Christ, to, because not
`and can apostle because* Lord-Jesus ~Christ-to because-not`

**2**  out, the Holy Spirit, mercy; and spake holy John: he breathed
`out(ward) holy-spirit have_mercy and speak holy-John +breathed`

**3**  upon them, learning; and all the apostles took the Holy Spirit.
`upon_them learn and every apostle grab holy-spirit`

**4**  And then the Lord Jesus, the Lord's apostles: you go, apostles,
`and_said Lord-Jesus apostle of-Lord you go-apostle`

**5**  into the world, and be ye his apostles; preach the gospel.
`?into_the_world and exist-apostle <of>-Lord gospel preach`

**8**  baptize somebody in the name of the Father and the Son
`baptize somebody inside name the_Father and son`

**9**  and the Holy Spirit; everybody is saved; if, and somebody not
`and holy-spirit everybody = be_saved if and somebody not`

> John 20:22, "he breathed on them, and saith unto them, Receive ye the Holy
> Ghost", named to John on line 2, then Mark 16:15. Király & Tokai's breathe
> sign is written across the line break here, half on line 2 and half on
> line 3, and their entry cites it at line 3.

## 129v — baptize them, and be brought before kings

**1**  baptize in the name of the Father and the Son and the Holy Spirit.
`baptize inside name the_Father and son and holy-spirit`

**2**  One man shall be saved; in turn, every man shall be damned. And
`one somebody +be_saved a) each,_every somebody be_damned and`

**3**  said the Lord Jesus to his apostles: ye shall | go,
`say Lord-Jézus apostle <of>-Lord you exist | go`

**4**  the Jews, before kings, before emperors. | Not
`Jews before king before emperor | not`

**5**  the disciples have, because I am [with] you that
`teach^ have because I exist you that`

**6**  not the disciples [teach]; how say? it is the apostles speak. And then
`not teach^ [teach] how? say exist speak-apostle and_said`

**7**  the Lord Jesus had these apostles from him; and a man, you, the apostles,
`Lord-Jézus have this-apostle from and somebody you apostle`

**8**  body die, rather somebody, apostle, from the Lord God.
`body die rather somebody-apostle from Lord_God.`

**9**  have, and the Lord you, disciples, soul and body
`have and-Lord you teach^ soul and body`

> Matthew 28:19 on line 1 and Mark 16:16 on line 2, then Matthew 10:18-20,
> "ye shall be brought before governors and kings for my sake ... take no
> thought how or what ye shall speak ... for it is not ye that speak, but
> the Spirit of your Father". Line 6 gives that last clause. *Rather* on
> line 8 is Király & Tokai's, cited by them at that line.

## 130r — the apostles go out, and a new reading from John

**1**  destroy. And then the Lord Jesus: then went the apostles, preached, and
`destroy and_said Lord-Jesus then go-apostle preach and`

**2**  began from Jerusalem; and the disciples preached on all the whole world.
`begin from Jerusalem ~and preach teach^ on-every all_the_world world.`

**3**  The end of this holy gospel; and the Lord Jesus departed from among the apostles.
`end this holy-gospel and leave among apostle Lord-Jézus`

**4**  Begins this
`begins this.`

**5**  holy gospel, written
`holy-gospel write`

**6**  by holy John, in the second chapter
`holy-John inside two chapter`

**7**  of his writing. Then
`inside <of>-write time`

**8**  said the Lord Jesus to his apostles,
`say Lord-Jézus apostle <of>`

**9**  the Lord, at the last supper:
`Lord on-last dinner-to.`

**10**  I go, the Lord, to the Lord's Father; he who, the Lord, goes, the Lord,
`I go-Lord to-of-Lord the_Father he_who Lord go-Lord`

> Luke 24:47, "beginning at Jerusalem", on line 2. Line 6 cites John, second
> chapter, and what follows is John 14, Thomas and Philip at the last
> supper. It is recorded as off, and it is the sixth miss.

## 130v — Thomas, and Philip: shew us the Father

**1**  And then holy Thomas: Master, goes the Lord to the Lord's God the Father? Said | the Lord
`and_said holy-Thomas Master go-Lord to-of-Lord God_the_Father say | Lord`

**2**  Jesus: Thomas, I go, the Lord, to the Lord's God the Father; and <subject marker> the Lord
`Jesus Thomas I go-Lord to-of-Lord God_the_Father and SUBJ-Lord`

**3**  goes, the Lord. And then | holy Philip: Master, show the apostles
`go-Lord and_said | holy-Philip Master show apostle`

**4**  the Lord's Father. And then the Lord Jesus: Philip, <subject marker> the apostles
`of-Lord the_Father and_said Lord-Jesus Philip SUBJ apostle`

**5**  the Lord the apostles saw; then I did miracles, [works], miracles;
`Lord see-apostle then I miracle do [works] miracle`

**6**  one Lord; I to the Lord by doing; but rather God the Father,
`one-Lord I to-Lord by do but_rather* God_the_Father`

**7**  of the Lord, […] doeth them, the Lord's finger.
`<of>-Lord [?] do, <of>-Lord +finger`

**8**  And the apostles [he] began to rebuke on belief. And then the | Lord
`and apostle begin rebuke on-believe and_said | Lord`

**9**  Jesus: and a man, the Lord, the apostles have seen, these apostles, and of the Lord
`Jézus and +<subj> somebody Lord see-apostle this-apostle +<subj> and <of>-Lord`

**10**  the Father saw; and the man is believing the Lord; this is
`the_Father see and man^ exist Lord believe this exist`

> John 14:5-11, Thomas's "we know not whither thou goest" and Philip's
> "Lord, shew us the Father", answered with "he that hath seen me hath seen
> the Father ... the Father that dwelleth in me, he doeth the works". *Shew*
> is Király & Tokai's sign, which they gloss with the verse and cite here,
> and *rebuke* on line 8 is theirs, glossed with Mark 16:14, the unbelief of
> the apostles. Their *finger* stands on line 7.

## 131r — the pagans and the resurrection

**1**  and the Lord's Father believe, because this one
`and of-Lord the_Father believe because this one`

**2**  God. And then the Lord Jesus: you go, apostles, within
`God and_said Lord-Jesus you go-apostle inside`

**3**  land [and] land, among the pagans; and
`land land among pagan and`

**4**  the pagans; preach, apostles, how I from death
`pagan exist preach-apostle how? I from-die`

**5**  stood up, up; how it is from the pagans, you
`stand_up up how? exist from pagan you`

**6**  apostles, believe, because God said, the mouth, year; hear; and <subject marker>
`apostle believe because God say mouth-~year hear and SUBJ`

**7**  the Lord see, pagans. And then the Lord Jesus said: the Lord | you
`Lord see pagan and_said Lord-Jesus say-Lord | ~you`

**8**  yours; how you apostles are, the pagans | to
`yours how? you apostle exist pagan | to`

**9**  believe: because the pagans are before you,
`believe* because-exist pagan before you`

**10**  the dead carry, the pagans, on standing up, resurrect; and this | is
`die carry-pagan on-~stand_up resurrect and this | exist`

> An earlier printing read the sign on lines 3–10 as "the Sadducees"
> (Matthew 22:23), a reading of ours, and set line 5 against Luke 24:43,
> where the risen Lord eats before the apostles. Both were wrong: Király &
> Tokai read the sign "pagan", and line 5 has no eating. The page sends the
> apostles to preach the rising of the dead among the pagans. Király &
> Tokai's rise sign stands on line 10, cited by them.

## 131v — in my name, and he that believeth and is baptized

**1**  the apostles say, the apostles: this, the dead, offer; the apostles can, Jesus of Nazareth
`apostle say-apostle this-the_dead offer apostle can Jesus Nazareth`

**2**  have; the dead up, rise, resurrect; in the place rise, resurrect,
`have the_dead up rise^ resurrect on-place rise^ resurrect`

**3**  somebody, in the Lord's name. And then the Lord Jesus: and
`somebody inside of-Lord name and_said Lord-Jesus and`

**4**  the man who believeth in the Lord, every such man shall be saved;
`somebody exist Lord believe each,_every somebody +be_saved`

**5**  and one somebody is damned. And then the Lord Jesus: and
`and one somebody be_damned and_said Lord-Jesus and`

**6**  somebody [does] not believe the Lord; one somebody
`somebody not Lord believe one somebody`

**7**  is saved, but everybody is damned. And then the Lord Jesus:
`be_saved but everybody = be_damned and_said Lord-Jesus`

**8**  and the man who believeth the Lord, to be | one woman
`and somebody exist Lord believe to exist | one-~woman`

**9**  baptize in the name of the Father and the Son and the Holy
`baptize inside name the_Father and son and holy`

**10**  Spirit: every such man shall be saved, and one man
`spirit each,_every somebody +be_saved and one somebody`

> Acts 3:6, "in the name of Jesus Christ of Nazareth rise up and walk", then
> Mark 16:16 three times over with its two halves in different orders.

## 132r — the signs that shall follow them that believe

**1**  is damned. And then the Lord Jesus: and somebody is believing the Lord
`be_damned and_said Lord-Jesus and somebody exist Lord believe`

**2**  shall do many miracles, all in the Lord's name; | and
`exist many miracle do, each,_every inside <of>-Lord | and`

**3**  there is […]; at that time the apostles saw [him] bow on heaven,
`exist-[?] time see apostle bow on-heaven`

**4**  land, light. And then the apostles: Master, [we] saw
`land light and_said apostle Master see`

**5**  the apostles, the light, bowed on heaven; land; said
`apostle light bow on-heaven ~land say`

**6**  the Lord Jesus: lo, bowed, could Satan. And then
`Lord-Jesus lo bow can Satan and_said`

**7**  the Lord Jesus: go ye, apostles, into the world; be ye apostles
`Lord-Jézus you-apostle go ?into_the_world exist-apostle`

**8**  to the ass; heal ye, apostles; be ye apostles; the evil | upon
`to-from-donkey from-healing-apostle exist-apostle evil | on`

**9**  the people cast ye out, apostles; the blind eyes, through light, apostles;
`people +cast_out-apostle eye-blind through light-apostle`

**10**  the dead stand up, resurrect, apostles, all in the Lord's name.
`the_dead stand_up resurrect-apostle every inside of-Lord name`

> Mark 16:17-18, the signs that shall follow, which the book gives sign for
> sign a second time here; it gave them once already at 042v-043r. Lines 3-6
> are the Ascension.

## 132v — the end of the reading, and the angel comes to Elijah

**1**  and on how, chapter, somebody | ill; go, apostles, every chapter | from
`and ~on-how? chapter-somebody | ill go-apostle every chapter | from`

**2**  healing, apostles, in the Lord's name. The end of this holy gospel.
`healing-apostle inside <of>-Lord +name end this holy-gospel`

**3**  Then appeared the angel of God
`time then-exist appear God angel`

**4**  to holy Elijah the prophet. Then
`holy-+Elijah prophet time then-exist`

## 133r — Elijah's forty days, and the angel at Horeb

**1**  From Adam [to] the Creator Lord, until this [thousand] | five hundred
`from ~Adam Creator_Lord until this [thousand] | five_hundred`

**2**  day, and thirty [and] six years. At that time appeared God['s angel]
`day^ and thirty six-year time appear God`

**3**  angel [to] holy Elijah the prophet. And then God's angel:
`angel holy-+Elijah prophet and_said God angel`

**4**  Elijah, the Lord God, this is, says the Lord: fast.
`Elijah Lord_God this_is say-Lord exist fast`

**5**  forty; go, Elijah, afar [to the] mount; and the body
`forty go-+Elijah on-far mount and ~body`

**6**  it is Horeb. And then went Elijah upon this mount
`exist Horeb and then-exist go +Elijah on-this [?]`

**7**  Horeb; and then Elijah lay down, to
`+Horeb and then-exist from +Elijah lie to`

**8**  one tree; and a second time said the angel of God: Elijah, take,
`one tree and two say God angel +Elijah grab`

**9**  and Elijah found, and Elijah did eat, and Elijah was strengthened;
`find-+Elijah eat-+Elijah exist-+Elijah strengthen`

**10**  and Elijah went [forty days], Elijah, upon this mount Horeb, the love of the Lord God.
`and go-+Elijah [?] +Elijah on-this mount Horeb love Lord-<divine>`

> 1 Kings 19:4-8: Elijah under the juniper tree, the angel touching him
> twice, and the forty days' journey to Horeb the mount of God. Király &
> Tokai gloss Horeb at four lines on these two folios; the fourth spelling
> on line 7 is theirs too, cited by them at that line. This is the page that
> proved the sign read Enoch is Elijah.

## 133v — the cake and the cruse, and Elijah taken up

**1**  This is this mount, the love of the Lord God most high, of every creature. And then went Elijah
`+this_is this mount love Lord-<divine> most_high each,_every create and then-exist go +Elijah`

**2**  upon this mount Horeb, and before he went, in that place [under a juniper]
`on-this mount Horeb and before go from on-place [?]`

**3**  lay down holy Elijah the prophet; and Elijah found
`lie holy-+Elijah prophet exist find-+Elijah`

**4**  one cake, and one cup of water; and
`one +a_cake and one cup water and`

**5**  he did eat, and drank, and was strengthened, upon this mount [of God] Elijah.
`eat and drink and strengthen on-this mount [?] +Elijah`

**6**  And from the fast, forty; and this forty, then,
`and from fast forty and this forty then`

**7**  at that time took Elijah, the two, Noah; [wished to die]; [a cake]
`time grab to-+Elijah-two-Noah [wished_to_die] [a_cake]`

**8**  and Elijah [and] Noah were caught up into heaven on high; and from
`and Elijah-Noah be_caught_up heaven high and from`

**9**  Elijah man is Noah, Elijah, the sword
`+Elijah [?] exist ~Noah +Elijah +sword`

**10**  carry; hell, one gate open; and [Enoch] left; Noah, Elijah on the earth.
`carry hell one-+gate/open and [Enoch] leave Noah Elijah on-earth`

> 1 Kings 19:6, "there was a cake baken on the coals, and a cruse of water
> at his head", where *a cake* is Király & Tokai's own sign for that kind of
> bread, cited by them at this line, and the cup beside it is theirs. Lines
> 7-10 are the Gospel of Nicodemus again: the two men kept alive who return
> at the coming of Antichrist and are slain by the sword. This is the second
> copy of 101r, and the doubt recorded there stands: the companion is
> written with their Noah sign, and in every source it is Enoch.

## 134r — Antichrist, and a new reading: the king who took account

**1**  [Antichrist] [of a harlot] through birth, the two, the chief evil, the evil one, and
`[?] [?] through be_born two ~head-evil ~evil and`

**2**  the son of the devil, by name evil; it is | Anti-
`son hide_oneself-angel +name evil exist | +Anti-`

**3**  christ. Before the gospel, said
`baptize before gospel say`

**4**  the Lord Jesus left:
`Lord-Jesus leave`

**5**  a king, a man, king;
`king somebody ~king`

**6**  hear all […] | of
`hear each,_every [?] | <of>`

**7**  the kingdom. Begins
`from-+king land begins`

**8**  this holy gospel, written
`this holy-gospel write`

**9**  by holy Matthew, in the [eighteen] chapter of his writing. Then said the Lord Jesus
`holy-Matthew inside [eighteen] chapter of-write time say Lord-Jesus`

**10**  the Lord's apostles and the Jews, the people: there is, among the Lord God, doomsday,
`apostle of-Lord and Jew people exist among Lord_God doomsday`

**11**  one king; all priest heavenly, the Lord, the man, before
`one king each,_every [?] heavenly Lord somebody before`

**12**  the Lord God the king; and then he had one heavenly
`Lord-<divine>-king and then-exist have one heavenly`

> Antichrist on lines 2-3 is Király & Tokai's own compound, written across
> the line break, and its second half is the same sign the book reads as
> baptize. The chapter numeral on line 9 does not read: it is nine signs,
> four of their 080 then a sign that occurs nowhere else in the book then
> four more 080. The passage is the Unmerciful Servant, Matthew 18:23. If
> the outer groups are fours and the middle sign is ten, it says eighteen
> and the citation is right, but that is a guess and the numeral is recorded
> as unresolved. It is the only chapter citation so far that is not written
> in the book's ordinary numerals.

## 134v — ten thousand talents, and the servant sold

**1**  a servant; and the lord's servant owed ten thousand talents;
`somebody-servant and Lord servant exist indebted +ten_thousand talent`

**2**  and there went this Lord God the king, this heavenly servant; and
`and go this Lord-<divine>-king this heavenly servant and`

**3**  then the servant, the angel, went before this | Lord God
`then-exist somebody-servant-angel go-angel before this | Lord-<divine>`

**4**  the king, before the Lord Christ; and the servant began
`king before Lord Christ and somebody-servant begin`

**5**  asked this Lord God, somebody, the king, of the Lord | [forgave the debt]
`ask this Lord_God-somebody-+king of-Lord | [forgave_the_debt]`

**6**  to do good. And then the Lord God, the king: | commandment, love, mercy,
`good-do and then Lord_God-king | commandment-love-have_mercy`

**7**  righteousness, good deeds, not to the high, take. And then
`righteous-good-do not-to-°high take^ and_said`

**8**  this Lord God, the king, sold the angel-somebody, damned | of
`this Lord_God-king sell angel-somebody be_damned | of`

**9**  somebody, son, sin; and the world to the rich; and somebody knelt,
`somebody ~son sin and world ~rich-to and kneel-somebody`

**10**  this man, this heavenly servant, before this | Lord God
`this somebody this heavenly servant before this | Lord-<divine>`

> Matthew 18:23-26. *Ten thousand* is their ten and their thousand joined,
> standing directly before their own talent sign, which they gloss with the
> verse. *Sold* and *to be lost* are both theirs, cited at line 8, which is
> "his lord commanded him to be sold".

## 135v — the fellowservant cast into prison

**1**  of the debt; and rather love he took; in turn he knelt down, the man of God,
`<of>-indebted and rather-love grab a) kneel_(down) God-somebody`

**2**  before this heavenly servant; and the servant
`before this heavenly servant and somebody-servant`

**3**  began, prayed, [fellowservant] [a hundred pence], have the commandment | to
`begin ~pray [fellowservant] [a_hundred_pence] have commandment | to`

**4**  the man of God; the man of God would, this man, the heavenly servant,
`God-somebody want-God-somebody this somebody heavenly servant`

**5**  have compassion forgive the debt; and the man of God release
`[?] remit indebted and God-somebody [?]`

**6**  but God's somebody took [him] into prison; and God's somebody,
`but God-somebody take^ inside prison and God-somebody`

**7**  until, from […] he bowed the head upon the scaffold; and
`until-from +bowed head inside scaffold and`

**8**  saw this, sad, the other servant; this Lord God, the king, the angel, forgave.
`see this sad other servant this Lord_God-king angel forgive^`

**9**  the one only Lord God; and the angel went, sorrowing, the angel, this
`one only_one Lord-<divine> and go-angel sad(ly)-angel-this`

**10**  this Lord God the king; and the Lord God the king said to the angel
`this Lord-<divine>-king and Lord-<divine>-king say angel`

> Matthew 18:28-32, the fellowservant who owed a hundred pence, cast into
> prison, and the other servants who told their lord. Király & Tokai's
> scaffold sign stands on line 7 and their bow-down at the word before it.

## 136r — the parable told a second time

**1**  the Father of heaven, he who [is] king of all heaven [and] land,
`the_father heaven he_who king every heaven land`

**2**  and on earth king of all. And then from forgiving, the servant
`and on-earth every king and_said from forgive^ ~servant`

**3**  believes in the Lord God, the one only Lord God [besought]
`believe <of>-Lord-<divine> one only_one Lord-<divine> [?]`

**4**  This Lord God forgave. The Lord: ten thousand(?) talents appeared.
`this Lord_God forgive^ Lord ten-?thousand talent appear.`

**5**  One of God's somebody; and somebody was in debt a hundred
`one God-somebody and somebody exist debt^ hundred`

**6**  denarii; and the man of God began to ask | for
`denarius and God-somebody begin ask_(for) | <of>`

**7**  the debt, and rather with love he took him;
`indebted and rather-love grab`

**8**  in turn he knelt down, the man of God, before this
`a) kneel_(down)-God-somebody before this`

**9**  heavenly servant; and the servant began, prayed,
`heavenly servant and somebody-servant begin ~pray`

**10**  [fellowservant] [a hundred pence], have the commandment to God's somebody.
`[fellowservant] [a_hundred_pence] have commandment to God-somebody`

> Matthew 18:28-29 a second time. The book writes this whole passage twice:
> lines 5 to 10 here are word for word 135r:10 to 135v:3. The second copy is
> what read the first copy's gaps.

## 136v — he would not forgive, and the king was wroth

**1**  The man of God would not, this heavenly servant, have compassion,
`want-God-somebody this heavenly servant +have_compassion`

**2**  forgive the debt, and release the man;
`remit indebted and God somebody ?release`

**3**  but God's somebody took [him] into prison; and God's somebody,
`but God-somebody grab inside prison and God-somebody`

**4**  from house to house, bowed his head upon the scaffold.
`to-house-from +bowed ~head-chapter inside scaffold`

**5**  This king, the Lord Christ, grew angry, and went upon this
`get_angry this king Lord Christ and go on-this`

**6**  heavenly servant; and the servant went to die, before the angel,
`heavenly servant and +servant go die angel before`

**7**  before this king, before the Lord Christ, the one only
`this king before Lord Christ one only_one`

**8**  the Lord God. And then this king, this servant forgave | of
`Lord_God and_said this king this servant forgive^ | of`

**9**  the Lord, the Father God; to hide that servant; like the Lord to; and
`Lord the_father God to-hide that_servant like Lord to and`

**10**  the king — that servant: "Lord have mercy, Lord have mercy" — that servant.
`king +that_servant have_mercy-Lord have_mercy-Lord +that_servant`

> Matthew 18:30-34. Lines 9 and 10 are loose; the words are read but the
> sentence is not, and nothing here settles who hides from whom.

## 137r — the end of the reading

**1**  Ten thousand talents. In turn this man, from the man of God [forgave thee]
`+ten_thousand talent in_turn this-somebody from God-somebody [?]`

**2**  forgave: a hundred denarii. And the man took this
`forgive^ hundred denarius ~and somebody grab this`

**3**  king, the Lord Christ; and then took of the Lord the king
`king Lord Christ and then-exist grab <of>-Lord-king`

**4**  evil, cast out the devil. And then this king,
`evil exorcise devil = and_said this king`

**5**  the Lord Christ, all of it, until this: that the man suffer
`Lord Christ each,_every +until-from this +that somebody suffering`

**6**  [shouldst not thou] [had compassion] [even as I]; if the king, the debt of the sin
`[shouldst_not_thou] [had_compassion] [even_as_I] ~if king debt^ sin`

**7**  somebody. And then this king, this is, forgave all
`somebody and_said this king this exist every forgive^`

**8**  somebody; and somebody did not forgive. Here ends this holy gospel.
`somebody and somebody not forgive^ here_ends this holy_gospel`

> Matthew 18:32-35. Line 6 has three unread words together and cannot be
> assigned; it is left as it stands. *Cast out* on line 4 is Király & Tokai's
> own exorcise, written with its two halves in the other order, which their
> entry records at this very line.

## 138r — the Hail Mary, twice

**1**  … the divine one, you, divine one, blessed Mary, you among
`DIV you-DIV blessed-Mary you ~among`

**2**  women; blessed <subject marker> Mary's son, he who went, the Lord, | from
`woman blessed-+SUBJ of-Mary son he_who go-Lord | from`

**3**  up, Mary's body. Jesus Christ. Amen.
`up of-Mary body Jesus Christ amen`

**4**  Healing, girl, through holy Mary, from, took the Virgin Mary. (An earlier printing read this as "Hail, maiden"; the signs read healing and girl here.)
`healing-girl through holy-Mary from grab-Virgin_Mary`

**5**  believe, this N. [the author], somebody, you are; N. [the author], somebody,
`believe this-NAME.author-somebody you exist NAME.author-somebody`

**6**  through the mercy of the Virgin Mary; and is N. [the author], somebody [blessed art thou]
`through have_mercy-Virgin_Mary and exist NAME.author-somebody [blessed_art_thou]`

**7**  [among women] this […] name, Mary; and within every hour; and | redeem
`[among_women] this °sick-+name-Mary and inside every hour and | redeem`

**8**  Mary; N. [the author], somebody, in the year of wrath of Mary, through the year of wrath,
`Mary NAME.author-somebody grow_angry-~year of-Mary through grow_angry-~year`

**9**  through, wish, the son of Mary, our Lord Jesus Christ.
`through wish son of-Mary Lord our Jesus Christ`

> The Hail Mary, running across the page turn: Király & Tokai's own entry for
> the greeting gives "Hail Mary, full of grace, the Lord is with you" at
> 137v09-138r01, and their entry for *bless* gives the spelling on lines 1 and
> 2 here, which is how *blessed* was read. *Woman* on line 2 is theirs too,
> cited at this line; the same sign is *the poor man* through the whole Dives
> and Lazarus block at 088v-089v, and their dictionary numbers it as two
> words. "N." is their sign for the name of whoever is saying the prayer.

## 138v — Saint Augustine and the three Hail Marys

**1**  Amen. This prayer has from [three] mercy.
`amen this pray have from [?] have_mercy`

**2**  speaks the holy father, the church father, of the happy Virgin Mary, who [is] up:
`speak holy-NAME.father church_father from happy Virgin_Mary who up`

**3**  you are; ask Mary, from Mary
`exist you exist ~ask-Mary from of-Mary`

**4**  the son, from the Lord Jesus Christ. Everyone who would take hold, says
`son from Lord-Jézus-Christ each,_every want grab speak`

**5**  holy Augustine the church father. Saint Augustine prays this:
`holy-Augustine-church_father pray-+Saint_Augustine this`

**6**  three prayers [to] the happy Virgin Mary, on pleasing, on thanks.
`three pray happy Virgin_Mary on-pleasing on-thanks`

**7**  not; Saint Augustine: somebody has lost, ever
`not-+Saint_Augustine-somebody have lose ever`

**8**  ever; and on the cloud destroyed; and on three prayers
`ever and on-+cloud destroy and on-+three pray`

**9**  many sins of a man are taken away, the sins of a man, in heaven
`from many somebody-sin go-somebody-sin inside ~heaven`

> The devotion of the three Hail Marys, said in Augustine's name. *Lose* on
> line 7 and *Saint Augustine* on lines 5 and 7 are both Király & Tokai's own
> spellings, cited at these lines; *cloud* on line 8 is theirs with their own
> two question marks on it. Line 1 is an indulgence formula and 137v:9 has
> the same one with a figure in it, "a hundred years of mercy".

## 139r — Mary shows her breast

**1**  land. Because, and somebody prays [to] the happy Virgin Mary
`land because and somebody pray happy Virgin_Mary`

**2**  every man is saved and goes not into the fire of hell; because
`each,_every somebody +be_saved not-go on-hell fire because`

**3**  the happy Virgin Mary every day, kneeling [to] Mary before
`happy Virgin_Mary every day kneel-Mary before`

**4**  of Mary | the son; she shows, of Mary,
`<of>-Mary | son +show <of>-Mary`

**5**  the breast, this breast, this of Mary, [that] he, the divine one, was nursed; believe.
`breast this breast this-Mary he-DIV nurse believe`

**6**  "the lost and damned man: have mercy, Christ" | "the man
`?the_man-+lost_and_damned have_mercy Christ | ?the_man`

**7**  lost and damned." And whoever prays to the mother of Christ, every
`+lost_and_damned and somebody pray mother Christ each,_every`

**8**  man is saved, and one is damned; but every
`somebody be_saved and one be_damned but everybody =`

**9**  man is saved, because a good servant, every [faithful] servant
`+be_saved because good servant each,_every [?] servant`

> Mary pleading with her son by the breast that fed him, the commonest image
> in a medieval Marian intercession. *Show* on line 4 and *lost and damned* on
> lines 6 and 7 are Király & Tokai's, cited at these exact lines; *lost and
> damned* is written as one word on line 6 and split across the line break
> from line 6 to line 7, which is how the two halves were read.

## 139v — the curse and the blessing

**1**  speaks holy Moses [to] Aaron, Moses's brother:
`speak holy-Moses Aaron of-Moses brother`

**2**  this people, the man, is cursed from every
`exist this people somebody exist through cursed from each,_every`

**3**  good. That is, somebody is not saved; in turn, and the man is
`good that_is not be_saved-somebody in_turn and man^ exist`

**4**  merciful, righteous, to the poor man of God, and to our
`have_mercy-somebody righteous-somebody poor_man_of_God = and to our`

**5**  father's son as the man himself, ours.
`the_father son as man^ himself our.`

**6**  There is heaven land; in turn, and the man [who is] not
`exist heaven land in_turn and man^ not`

**7**  finding mercy, righteous, to the poor man of God, and to our
`find_mercy^ righteous-somebody to poor_man_of_God = and to our`

**8**  father's son, this man the Lord God wants cursed from
`the_father son this man^ want Lord_God cursed from`

**9**  every good; and all he has, that is, all his riches who
`each,_every good +be_saved and each,_every have that_is each,_every ~rich [?]`

**10**  [cursed] what the man has is damned, and the rich man cursed. This
`[?] have-somebody be_damned-somebody and ~rich cursed this`

> Deuteronomy 28, the blessings and the curses, which run from here to
> 140v. *Brother* on lines 5 and 8 is Király & Tokai's own father+son, and
> *himself* on line 5 is theirs too, cited at this line. Lines 3 to 8 are one
> formula said twice. Read sign by sign it says "to God blind", and an
> earlier version left it unexplained; it is Király & Tokai's set phrase
> "poor man of God", the pious poor (see 117r).

## 140r — cursed be thy herd and thy field

**1**  the man. Of the Lord the herd, cursed; of the Lord the field;
`somebody Lord-<divine> <of> herd cursed Lord-<divine> <of> field`

**2**  then this somebody's harvest, field, cursed, [by] the Lord God, our
`then-this-somebody harvest field cursed Lord_God our`

**3**  mount; then this man's grape, harvest, mount.
`mount then-this-somebody grape harvest mount.`

**4**  cursed, this somebody, [by] the Lord God, within our home.
`cursed this-somebody Lord_God inside our home`

**5**  Not this somebody [barn] [stores]; somebody is damned, ever
`not this-somebody [barn] [stores] be_damned-somebody ever`

**6**  ever; into hell somebody falls; in turn, and somebody is | merciful,
`ever inside hell somebody fall in_turn and somebody exist | have_mercy`

**7**  somebody righteous, somebody, to the poor man of God, this our
`somebody righteous somebody to poor_man_of_God = this our`

**8**  father's son as somebody himself, this somebody.
`the_father son as somebody himself this-somebody.`

**9**  Blessed of the Lord the herd; blessed of the Lord the
`+blessed Lord-<divine> <of> herd +blessed Lord-<divine> <of>`

**10**  field; then the man's field, harvest, blessed;
`field then-this-somebody field harvest +blessed`

> Deuteronomy 28:17-18 and then 28:3-5, the curse and the blessing in the same
> words with one word changed, which is how *blessed* was read: Király &
> Tokai's own entry gives that spelling here, and the curse standing opposite
> it says the same thing twice over. *Grape* on line 3 is theirs, cited at
> this line; it had been cut into their "exist" and their numeral "nine",
> because the rule that makes it a variant is written in their prose and not
> as a variant code.

## 140v — write it, and pray to the virgin Mary

**1**  of the Lord God, the mount; then this man's mount, grape.
`Lord_God of mount then-this-somebody mount grape.`

**2**  Harvest blessed, this somebody, [by] the Lord God, and within our | home, in turn
`harvest blessed this-somebody Lord_God and inside our | ~home-in_turn`

**3**  home and in every place [wide] the man is left, the man is saved,
`[?] and each,_every to-place [?] leave-somebody +be_saved-somebody`

**4**  is, for ever and ever, amen. Writes, speaks:
`exist for_ever_and_ever = amen write speak`

**5**  all the whole world, pleasing the Father; in turn the son of God the Father.
`every all_the_world world pleasing the_Father in_turn son of-God_the_Father.`

**6**  Pray from the Virgin Mary, believe, to all [who] want the Lord
`pray from Virgin_Mary believe to every want Lord`

**7**  the Father hears; all the whole world wants the Lord to [his] will
`the_Father hear every all_the_world world want Lord to-+will`

**8**  do; and the Lord: whoever is righteous, believe,
`do, and Lord somebody exist righteous(ly) +believe`

**9**  the man. This the apostles all wrote, because every man's sin
`somebody this +<subject> apostle each,_every write because each,_every somebody sin`

**10**  somebody goes to the Virgin Mary; have mercy, asks somebody.
`go-somebody to Virgin_Mary have_mercy ask somebody.`

> *Wide* on lines 5 and 7 is Király & Tokai's, cited at both, and they gloss
> the phrase it stands in as "the whole wide world"; *will* on line 7 is
> theirs with two question marks on it.

## 141r — the fruit of Mary

**1**  Because of this, pray to Mary: the fruit of Mary, the son,
`because this from Mary pray <of>-Mary +fruit son`

**2**  to all the whole world, because the Lord Christ did the commandment among
`to-every all_the_world world because Lord Christ commandment do among`

**3**  somebody, among the Father of the Lord, because <subject marker> many.
`somebody among the_Father of-Lord because SUBJ many.`

**4**  Have mercy, Lord Christ, on every man's sin, speaks the holy church
`have_mercy Lord Christ to-each,_every somebody sin speak holy-<church_father>`

**5**  father; then this man is, from many a man's sin,
`church_father then-exist this somebody exist from many somebody sin`

**6**  [narrow] left somebody, our Lord's creation, because this is.
`[narrow] leave-somebody our Lord-create because this_is.`

**7**  […] the Lord, sin, mercy [fruit]; this is within the commandment of somebody,
`[...] Lord sin have_mercy [fruit] this exist inside commandment somebody`

**8**  that is; and somebody has to carry the commandment of God, | […]
`that_is and have somebody carry commandment God | [...]`

**9**  [bear] sin; somebody is saved, somebody, [through] many sufferings.
`[bear] sin somebody be_saved-somebody many suffering`

> *Fruit* on line 1 is Király & Tokai's own, and they gloss the whole phrase
> at this line: "Mary's fruit, her son".

## 141v — a woman in Rome

**1**  for ever and ever, amen. Writes <subject marker> the name | of
`for_ever_and_ever = amen write SUBJ name | of`

**2**  the man; in heaven and earth, until he dies; in turn upon
`somebody inside heaven land until die in_turn | on`

**3**  die, the body and the soul, for ever and ever, amen.
`die body and soul for_ever_and_ever = amen`

**4**  There was in Rome a
`exist inside +Rome one`

**5**  woman, baptize, head, and
`woman baptize head and`

**6**  then asked the woman
`then ~ask-+woman`

**7**  in Rome father
`inside +Rome [?]`

**8**  every day two, God, body.
`every day two God body`

**9**  took, and fasted, half [forty days]; <subject marker> fasted; baptize, baptize.
`grab and fast half* [forty_days] SUBJ fast ~baptize baptize`

**10**  many years; and the woman would give thanks; this [Lady] fasted one
`many year and +woman want thanks this [?] fast one`

**11**  [received]; and the woman took this holy host, and then
`[?] and +woman grab this holy-host and then-exist`

> A correction, and a large one. This block was reading "baptism" and "the
> Baptist" and it is a woman. Király & Tokai's entry for *woman* cites
> 141v06, 10, 11, 142r01, 142v02, 02, 04, 05 for the first sign, and says the
> pair of signs across folios 141 to 147 is *woman* as well. Both words are
> reduplications of their 060131, which alone is *woman*, and their own
> Baptist entry writes "but cp." at the collision. The Baptist reading is
> right where the sign stands after Saint John at 116v-118r, which is where
> they cite it, and it was wrong everywhere else. *Rome* on lines 4 and 7 is
> theirs, cited at both, with their question mark on it.

## 142r — the woman who lived on the host

**1**  The woman took, and shouted to; lost, died, the woman, baptize.
`woman grab and shout-to lose die-+woman baptize`

**2**  and then carried the host; and then the woman, baptize, the host was.
`and then carry host and then woman baptize host exist`

**3**  took in the place; hunger(?); left [nothing]; bread
`grab on-place hunger? leave [nothing] bread`

**4**  eat, the woman, baptize, many years [was fed]; <subject marker> the woman, baptize, fed.
`eat woman baptize many year [was_fed] SUBJ woman baptize feed`

**5**  Christ in the high heavens, the Holy Spirit, spirit to spirit, from the woman;
`Christ on-heaven +high holy-spirit to-spirit from +woman`

**6**  living […] half; there were two; the woman, baptize, head, within Rome;
`living-[?] half* exist two woman baptize head inside Rome`

**7**  and then the woman, baptize, committed sin; the woman, baptize, out;
`and then woman baptize commit sin woman baptize out`

**8**  of the woman, baptize, the Lord, thief, who did; and then
`of-+woman baptize Lord thief-who do and then`

**9**  the woman, baptize, cast out; the Lord, on the Lord's, had mercy; and
`woman baptize exorcise Lord on-of-Lord have_mercy and`

**10**  went one sister. And then: oh, | of
`go one sister and_said oh | of`

> A woman who fasts for years and lives on the host. *High* on line 5 is
> Király & Tokai's, in their own phrase "the high heavens" cited at this
> line; *lose* on line 1 and *sister* on line 10 are theirs too, both cited
> here, and the sister carries their "?? nun". The words on this page are
> read and the story is not: whose thief, and who casts out whom, is not
> settled by anything on the page.

## 142v — the woman fasts and takes the host

**1**  The woman, baptize, the father, girl, if only this girl, wife, can do,
`woman baptize the_father girl if_only this girl-wife can do`

**2**  how this woman can. The woman, baptize, went into mercy; the woman
`how? this-+woman can woman baptize inside have_mercy go woman`

**3**  of the woman, baptize, the Lord; and then wanted to say this sister:
`of-+woman baptize Lord and_said want say this sister`

**4**  to fast, the woman [prayed]; and God, body, carry
`to-fast woman [prayed] and God body carry`

**5**  the woman, within the woman's, baptize, mouth; and the Lord is
`woman inside of-+woman baptize mouth and Lord exist`

**6**  God, body. Kissed the woman, baptize; the Lord wanted this
`God body kiss woman baptize want-Lord this`

**7**  woman, baptize; mercy is; and then the woman,
`woman baptize have_mercy exist and then woman`

**8**  baptize, to fast, and took God, body.
`baptize to-fast and grab God body`

**9**  And carried the woman, baptize, within the woman's, baptize,
`and carry woman baptize inside of-+woman baptize`

> *Kiss* on line 6 is Király & Tokai's, cited at this line and at 143r01 and
> 150v01, 02, which are its four occurrences in the book. The woman carries
> God in her mouth: the host. The words are read; the story is not settled.

## 143r — the face, the cloud, and the two grinding

**1**  mouth; and the Lord wanted, to God, body. Kissed;
`mouth and Lord want to God body kiss`

**2**  and the woman, baptize, face beat on the place [cheek]
`and woman baptize face beat on-place [cheek]`

**3**  out. God, body. And <subject marker> was a miracle, a farm;
`out God body and SUBJ exist ~miracle farm`

**4**  and the Lord God cried out, in the cloud, to the angel | of
`and shout-to Lord-<divine> on-+cloud on-angel | <of>`

**5**  the Lord left. Oh, baptize, baptize, of the Lord, the father, the daughter,
`Lord leave oh ~baptize baptize of-Lord the_father daughter`

**6**  to love. The Lord is a miracle; the farm; the woman, baptize, has
`to-love Lord exist ~miracle farm woman baptize have`

**7**  the woman, baptize, [suffered]; the woman, baptize, [patiently]; I
`woman baptize [suffered] woman baptize [patiently] I`

**8**  this woman, baptize, […] the Lord, sin, mercy. And then
`this woman baptize [...] Lord sin have_mercy and_said`

**9**  this woman, baptize, in turn, grinding, one: you, Lord God, say
`this woman baptize in_turn grinding-+one you Lord_God say`

> *Mouth*, *kiss*, *face*, *cloud* and *daughter* on this page are all Király
> & Tokai's own spellings, and every one of them is cited by them at the line
> it stands on. Line 9 is Matthew 24:41, the two women grinding at the mill,
> which is the first thing on these folios to put a verse behind the woman.

## 143v — crucified, and the sin that dies

**1**  the Lord God in the cloud to the angel of the Lord: I from Jesus; | and the Lord
`Lord_God in_the_cloud on-angel of-Lord I from Jesus | and-Lord`

**2**  <subject marker> crucified. And then this wife: Lord of the wife, Lord God,
`SUBJ crucified and_said this wife Lord of-wife Lord God`

**3**  of the wife have mercy, to, baptize, baptize, who, this wife, committed sin
`of-wife have_mercy to-~baptize baptize who this-wife commit sin`

**4**  against the Lord's, could. And then the Lord God: I this
`against of-Lord can and_said Lord_God I this`

**5**  woman, baptize, sin: have mercy, Lord, [forgive], Lord, on sin.
`woman baptize sin have_mercy Lord [forgive] Lord on-sin`

**6**  [cloud] This says <subject marker> the Son of God, the king of the high year; wanted the Lord,
`[cloud] this say SUBJ son God high-~year-+king want Lord`

**7**  heaven, earth [shall pass away], than one.
`heaven earth [shall_pass_away] than one`

**8**  A man's sin dies; that is, damned […] the man
`somebody sin die that_is be_damned [?] somebody`

**9**  damned. The Lord God, in turn: this man to the Lord, among the Lord
`be_damned Lord God a) this somebody to-Lord among Lord`

> The cloud on line 1 is the same formula as 143r:4 and 062r:9, the Lord God
> crying out in the cloud to the angel; only 143r:4 carries the spelling
> Király & Tokai cite, so the other two are read from the parallel.

## 144r — Saint Augustine, and an image of the Virgin

**1**  heavenly people, somebody, to the Lord God: I, you […]
`heavenly* people somebody to-Lord_God I you [...]`

**2**  of the Lord, the sin, the mercy, […]; this must the man carry:
`Lord +sin have_mercy [?] this have somebody carry`

**3**  the commandment of God; saved, somebody, [through] many sufferings.
`commandment God be_saved somebody many suffering`

**4**  For ever and ever, amen. Writes <subject marker> | holy
`for_ever_and_ever = amen write SUBJ | holy`

**5**  Saint Augustine: there was one woman and [a] Lady
`Saint_Augustine exist one woman and Lady`

**6**  <subject marker> prayed [to] the happy Virgin Mary, on out, three
`SUBJ pray happy Virgin_Mary on-~out three`

**7**  years. In […] there was an image | of the virgin
`year inside [?] exist one +image | virgin`

**8**  Mary; and then [knelt before] this image | of the virgin
`Mary and then [knelt_before] this image | virgin`

**9**  Mary; and said this: Lady, hear, Lady; and somebody
`Mary and say this Lady hear-+Lady and somebody`

> *Image* is Király & Tokai's, cited at lines 7 and 8 here and at 144v06,
> 145r08, 145v09, 146v08, 147v05 and 151v04, and for these folios alone they
> add the sense "? statue". *Lady* is their "<a female person>", which they
> put across 144v-148r; this project's word for it is Lady, because on these
> pages it stands as a title before the Virgin's name.

## 144v — thou who holdest heaven and earth

**1**  pray [to] the Virgin Mary; wanted somebody: good queen, [who] took heaven
`pray Virgin_Mary want-somebody good queen grab heaven`

**2**  and earth" — this Lady would, the Lady, pray.
`land this-+Lady want-+Lady pray`

**3**  And she served one day; then Mary, every day,
`and servant one +day then-exist Mary each,_every +day`

**4**  took bread, and [ate] truly, half year.
`grab bread and [ate] righteous half-~year`

**5**  then, the year out, within time, went this woman
`then year ~out inside time go this woman`

**6**  [to] this image of the Virgin Mary, and said this woman: | Lord,
`this image Virgin_Mary and say this woman | Lord`

**7**  […] thou who holdest heaven and earth, Lady, | virgin
`[?] grab heaven land +Lady | virgin`

**8**  Mary." This Lady spoke from thence; and two said; the girl said:
`Mary this-+Lady from speak and two say girl say`

> The sheep sign on lines 5 and 6 is Király & Tokai's own homograph: their
> entry gives sense (1) sheep, which is the Good Shepherd and the Lost Sheep
> at 064 and 119-120, and sense (2) "<a female person>" for 144v-147v, which
> is here. The page renders their first sense and the block means the woman.

## 145r — how shall we creatures speak?

**1**  queen, [who] took heaven [and] land, Lady Virgin Mary.
`queen grab heaven land Lady Virgin_Mary`

**2**  This Lady, from speaking, how? how shall we, tree, speak?
`this-Lady from speak how? how_shall_we* tree speak`

**3**  can speak? said this woman, this woman,
`can speak say this woman this-woman`

**4**  [said to] love: this Mary wanted; and then Mary, woman,
`[said_to] love this Mary want and then Mary woman`

**5**  served, fasted, and prayed two Hail Marys, and truly at the year's beginning
`servant fast and two Hail_Mary pray and righteous begin-~year`

**6**  bread; and [ate], took; and then,
`bread and [ate] grab and then`

**7**  out, two years, within time, went this woman [to] this
`~out two-year inside time go this woman this`

**8**  image of the Virgin Mary, and said this woman: queen,
`image Virgin_Mary and say this woman queen`

**9**  [who] took heaven [and] land, Lady Virgin Mary.
`grab heaven land Lady Virgin_Mary`

> The same scene as 144v, a year later: the woman comes back to the image and
> says the same prayer. *A female person* on line 2 is Király & Tokai's,
> cited at this line. "Two healings of Mary" on line 5 is their Hail-Mary
> greeting sign counted, as the three Hail Marys were counted at 138v:6.

## 145v — three days, three Hail Marys

**1**  This Lady from speaking; and two said this woman: queen,
`this-+Lady from speak and two say this woman queen`

**2**  [who] took heaven [and] land, Lady Virgin Mary.
`grab heaven land Lady Virgin_Mary`

**3**  The Lady prayed this to Mary, outwardly, fasting, fasting.
`pray +Lady this Mary on-~out(ward) fast fast`

**4**  The girl, the Lady: "Queen, thou who holdest heaven and earth" —
`girl +Lady +queen grab heaven land`

**5**  this girl, the Lady, spoke; this woman [said to] love:
`this-girl Lady speak this-woman [said_to] love`

**6**  you want; and then Mary, woman, servant,
`you want and then Mary woman servant`

**7**  three days out; and three Hail Marys she prayed; and truly at the year's beginning,
`on-out three_days and three Hail_Mary pray and righteous begin-~year`

**8**  bread; and [ate], took; and then out.
`bread and [ate] grab and then out.`

**9**  three days, within time, went this woman [to] this image
`three_days inside time go this woman this image`

**10**  of the Virgin Mary, and said this woman: queen, [who] took heaven
`Virgin_Mary and say this woman queen grab heaven`

> The third visit to the image, and the count has gone from one to two to
> three. Király & Tokai cite this line for the woman sign.

## 146r — the Lady speaks from the image

**1**  land, Lady Virgin Mary. This Lady from speaking;
`land Lady Virgin_Mary this-+Lady from speak`

**2**  and two said this woman: queen, [who] took heaven, | town
`and two say this woman queen grab heaven | town`

**3**  is, Lady Virgin Mary. This Lady from speaking.
`exist Lady Virgin_Mary this-+Lady from speak`

**4**  This woman grew angry; remit; went the Lady, of the Lady
`grow_angry this woman remit go-+Lady of-+Lady`

**5**  the Lord said, this woman, this Lady; and the Lady went.
`Lord say this woman this-+Lady and go-+Lady`

**6**  Forgive, this Lord. The Lady prayed, and the Lady served
`remit this Lord pray +Lady and servant +Lady`

**7**  the Virgin Mary, on out, three days; this girl, the Lady: queen,
`Virgin_Mary on-out three_days this-girl Lady queen`

**8**  thou who holdest heaven and earth" — this Lady; and | went
`grab heaven land this-+Lady and | go`

**9**  Lady. Remit, this Lord said, this woman, he.
`Lady remit this Lord say this woman he`

> The prayer is said four times on this folio in the same words, which is what
> makes the page readable at all: every slot in it is filled from a copy of
> itself.

## 146v — the nail, and the Virgin in the image

**1**  The Lady went from the Lord; I; this Lady the Lord wanted in the place.
`go-+Lady from-Lord I this-+Lady want-Lord on-place`

**2**  The girl: "Queen, thou who holdest heaven and earth" heavenly
`girl +queen grab heaven land [?]`

**3**  this woman, of the Lady, the Lord; and the Lady took
`this woman of-+Lady Lord and Lady grab`

**4**  this Lord, one [a candle] [lit] upon the piercing. And
`this Lord one [?] [?] on-pierce and.`

**5**  one [placed] [before it]; and the Lady went, this, | from
`one [placed] [before_it] and go-+Lady this | from`

**6**  the woman; and then […] went the Lady, this woman;
`woman and then-[?] go-+Lady this woman`

**7**  and many went. | In time appeared
`and go many | inside time appear`

**8**  the Lady, the Virgin Mary, within the image; the woman, baptize. And then
`Lady Virgin_Mary inside image woman baptize and_said`

**9**  happy the Virgin Mary took the woman, baptize, to this | [a candle]
`happy Virgin_Mary grab woman baptize to this | [a_candle]`

## 147r — the son, and the king

**1**  [candle] from the son, in the name of the Virgin Mary, said this
`[candle] from son inside name Virgin_Mary say this`

**2**  woman, this Lady; the girl prayed; and servant, Lady
`woman this-+Lady pray girl and servant Lady`

**3**  Mary, on out, three; this woman: queen, [who] took heaven
`Mary on-~out three this-woman queen grab heaven`

**4**  and earth" — Mary took the girl, the Lady; this son
`land Mary grab-girl +Lady this son`

**5**  the Lady would, the son, to this [a candle] put | and take;
`want-+Lady son to this [a_candle] put | grab`

**6**  the girl, the Lady, the son; in turn the Lady took one
`girl +Lady son a) +Lady grab one`

**7**  know. And then the Virgin Mary went, the Lady, up to the king;
`know* and_said Virgin_Mary go-+Lady to-up king`

**8**  and the king took the Lady, this know; and who
`and king grab Lady this know* and who`

**9**  this Lady said, king, living, the Lady did.
`this Lady say ~king living-exist Lady do`

## 147v — the Virgin seen by all the people

**1**  And then the Lady went to this king; and from seeing the king
`and then go-+Lady this king and from see-~king`

**2**  this know; and took [led away] this woman; and | then
`this know* and grab [led_away] this woman and | then`

**3**  there were Pharisees; they left the Lady; and then the Lady, the heavenly
`exist ?Pharisees leave +Lady and then-exist +Lady heavenly`

**4**  host say served the Lady. In time appeared
`host [?] servant +Lady inside time appear`

**5**  the Lady, happy Virgin Mary, within the image; the woman, baptize,
`Lady happy Virgin_Mary inside image woman baptize`

**6**  on all the people seen. And then happy the Virgin Mary [to] this
`on-every people see and_said happy Virgin_Mary this`

**7**  woman: this is. This Lady, like, loved the girl, | this
`woman this_is this Lady like love-girl | this`

**8**  Mary; this Lady, the man did, the girl.
`Mary this +Lady somebody do, girl`

**9**  the Lady is good; the Lady not derided; in turn
`exist-+Lady good Lady not °derided-~exist in_turn`

> *Like* on line 7 is Király & Tokai's, cited at this line as a variant of
> their "as, like".

## 148r — Adam went down to Jericho

**1**  the Lady is derided; she was lost, this Lady; and
`exist-+Lady °derided-~exist lose this Lady and`

**2**  left. Happy the Virgin Mary, before, remitted the people.
`leave happy Virgin_Mary before remit people.`

**3**  It is written of Adam.
`write +Adam.`

**4**  The son, Seth.
`son +Seth.`

**5**  And this is the word.
`and this word.`

**6**  It is written: Adam went,
`write go-~Adam`

**7**  one man, to Jerusalem,
`one somebody on-Jerusalem`

**8**  into the town of Jericho;
`inside +Jericho town`

**9**  and then, and Adam went into the field; and then
`and then and go ~Adam on-~field and then.`

**10**  came one deer; and then Adam
`come one deer and then ~Adam`

**11**  a year of chapters [fell among] a deer in the field; and then
`chapter-year [fell_among] deer on-~field and then`

> The Good Samaritan again, and this time with the allegory made explicit:
> the man who went down from Jerusalem to Jericho is Adam. *Adam*, *Seth*,
> *Jericho* and *lose* on this page are four of Király & Tokai's own
> spellings, each cited by them at the line it stands on, and their Jericho
> entry names the verse, Luke 10:30. The book already told this parable
> straight at 095v-097r; here it tells it as the fall of man.

## 148v — the man in the pit, and the two mice

The Good Samaritan allegory of 148r runs straight on: the same word for the
man, Király & Tokai's *Adam*, carries over the page turn. Then the book
changes figure and tells the apologue of the Man in the Well — the man who
flees, falls into a pit, catches at a tree, and does not see that two mice
are gnawing the root of it. It is the best-travelled parable in medieval
Europe, from *Barlaam and Ioasaph*, and the two mice are day and night.

**1**  Adam escaped across the field, and then Adam | bowed down
`escape ~Adam on-~field and then ~Adam | bow_down`

**2**  the man into a pit; and then hang
`~Adam inside one pit and then-exist [?]`

**3**  cling the man onto a tree, because there was
`[?] ~Adam on-one +tree because exist`

**4**  a branch sticking out [outgrow]; and there came two mice, one black,
`protrude [outgrow] and go two mouse one black`

**5**  the second white; and this tree, half, two mice
`second white and this tree half two mouse`

**6**  to eat. And then the man saw, and to the man
`to-eat and then-exist see ~Adam to-~Adam`

**7**  he saw a dragon, and
`and see one dragon = and`

**8**  which cried out to the man: the man is lost [in the well]
`who-shout-to ~Adam +lose-~Adam [?]`

**9**  if Adam goes up, this Adam, this | can
`if up go-~Adam this ~Adam this | can`

> The apologue of the Man in the Well, from *Barlaam and Ioasaph*. The
> source was fetched on 2026-09-20 (`data/ref/rohonc/barlaam.txt`) and it
> matches this page point for point: *a man flying before the face of a
> rampant unicorn ... he fell into a great pit; and as he fell, he stretched
> forth his hands, and laid hold on a tree ... he looked and descried two
> mice, the one white, the other black, that never ceased to gnaw the root
> of the tree whereon he hung ... he looked down to the bottom of the pit
> and espied below a dragon, breathing fire.* The codex has the flight, the
> pit, the tree, the two mice with their colours, and on line 7 the evil one
> below that cries out. *Mouse*, *black*, *white*, *tree* and *pit* are
> Király & Tokai's own words, so the match is between their dictionary and
> the source, not between two guesses of mine.
>
> The detail that settles *the man* is in the apologue's own moral: *the
> unicorn is the type of death, ever in eager pursuit to overtake the race
> of **Adam**.* That is why the codex writes him with Király & Tokai's
> *Adam* sign here, and why 148r, the page before, says outright that the
> man going down to Jericho is Adam. The book uses Adam for mankind exactly
> as its source does.
>
> The passage was found by a person reading the text. An attempt to place
> folios in named sources automatically is written up in ROHONC.md as the
> nineteenth attempt; it failed its own test four times and nothing here
> rests on it.

## 149r — the lance of the soldier

**1**  the evil dies, if cling the man bows down to this.
`evil die if cling bow ~Adam this.`

**2**  The dragon rends the man; and then the man
`dragon = ~Adam rend and then ~Adam`

**3**  [blind] through startled the man, and | he went to the dying Lord
`[blind] through startle ~Adam and | go-die-Lord`

**4**  Christ; one soldier of the Lord Jesus Christ who died [pierced the side]
`Christ one soldier-Lord-Jesus-die-Christ [pierced_the_side]`

**5**  [his] suffering; and this | can
`[his] suffering and this | can`

**6**  evil, on half, through [the death of the Lord Christ] and
`evil on-half through [the_death_of_the_Lord_Christ] and`

**7**  the man took hold of this soldier of Christ who died, the chapter | of
`~Adam grab this soldier-[?]-die-~Christ-chapter | <preposition_of_genitive>`

**8**  the soldier of the Lord Jesus Christ who died: suffering, lance. And then
`soldier-Lord-Jesus-die-Christ suffering lance and_said`

**9**  this soldier of the Lord Jesus Christ who died: Adam escaped on this
`this soldier-Lord-Jesus-die-Christ escape-~Adam on-this`

> The soldier with the lance is Longinus, who pierced Christ's side, and
> *lance* and *soldier* are Király & Tokai's. The man in the pit is pulled
> out by taking hold of the lance — the Passion itself as the thing that
> saves. The compound written for him, *soldier of the Lord Jesus Christ who
> died*, is the book's own; it is not a dictionary entry but every piece of
> it is.

## 149v — pulled out of the pit

**1**  the pit; the man was scattered, and then the man was with the Lord;
`pit scatter ~Adam and then-exist ~Adam exist-Lord`

**2**  the Lord took the suffering [and] lance of the soldier of the Lord Jesus Christ who died.
`grab-Lord of-soldier-Lord-Jesus-die-Christ suffering lance`

**3**  and the man out of this pit, the chapter of the soldier of Christ who died,
`and ~Adam ~out(ward) this pit soldier-[?]-die-~Christ-chapter`

**4**  took. And then this soldier of the Lord Jesus Christ who died: then
`grab and_said this soldier-Lord-Jesus-die-Christ then`

**5**  this Adam not out, the Lord took, on this pit there was
`this-~Adam not out grab-Lord on-this pit exist`

**6**  the man inside this pit; and the man died, because | this
`~Adam inside this pit and die-~Adam because-exist | this`

**7**  man, this deer dies, that is, he is damned.
`~Adam this deer die that_is be_damned`

**8**  There is, there is a man [is baptized] who is saved.
`exist exist ~Adam [?] +be_saved.`

**9**  the man; God is [baptized] [not] the man saw
`~Adam God-exist [baptized] [not] see ~Adam`

> The moral, and it is the ordinary one: the pit is death and damnation,
> and what lifts the man out of it is the Passion. Lines 7 and 8 set the two
> ends against each other in the book's standing formula, *damned* against
> *saved*, which it uses at 072v and 152r for Mark 16:16.

## 150r — a certain man had two sons

**1**  writes the church father, pagan; first writes [a certain man] | on this
`write church_father pagan first write [a_certain_man] | on-this`

**2**  this writes the church father, the church father [two sons]; after these writes
`this write church_father church_father [two_sons] after_these write`

**3**  [the younger]; the church father, after these, <subject marker> writes the church father
`[the_younger] church_father after_these SUBJ write church_father`

**4**  the Pharisees; and the church father [the gospel] the gospel: there was one
`?Pharisees and church_father [?] +good_news exist one`

**5**  man, and then this man had one.
`somebody and then-exist have somebody one.`

**6**  son; and this son was three; sold | redeemed
`son and this son exist three sell | redeem`

**7**  the man; and the son, four, wanted; the man could
`man^ and son two-two want-somebody can`

**8**  the son redeemed; and then the son went, cast out
`son redeem and then son go exorcise`

**9**  [divided] among; this son, of the son, the father said this
`[divided] among this son of-son the_father say this`

> Luke 15:11, *A certain man had two sons*. The parable of the prodigal son
> runs from here to 151r. The opening lines are a preacher's frame — a
> church father writing to the heathen — of the kind the book puts in front
> of a parable on 144r and 150v, where the father is named as Augustine.

## 150v — the father kissed him

**1**  son; oh, of the son, the father: the father kissed the son on this
`son oh of-son the_father kiss son father on-this`

**2**  last year; and then the son, the father kissed; and cursed
`last year and then-exist son father +kiss and cursed`

**3**  [ran]. And then, that is, the father was [fell upon his neck]; darkness?
`[ran] and_said that_is father exist [fell_upon_his_neck] darkness?`

**4**  then this father was, father, son, apostle, on good, not
`then this-father exist father son apostle on-good not`

**5**  this son upon this went, to the son, in love the son went, speaking, baptize
`this-son on-this go-~son on-love son go-~son speak-~baptize`

**6**  the church father, our church father, on [his] brother, by name Saint Augustine the church father
`church_father our church_father on-brother-+name Saint_Augustine_the_church_father`

**7**  spoke, the brother of Saint Augustine; and the man believes
`speak ~brother of-+Saint_Augustine and somebody believe`

**8**  in the Lord Jesus Christ; somebody has this, ours.
`inside Lord-Jesus-Christ have-somebody this our.`

**9**  the son, on good, the apostle: how you, the good man.
`son on-good apostle how? ~you good-somebody.`

> Luke 15:20, *and his father saw him, and had compassion, and ran, and fell
> on his neck, and kissed him*. The kiss is on the page twice. Saint
> Augustine is named on line 6 and again on line 7, as he is on 144r and
> 145v; the book keeps returning to him.

## 151r — for the good, to the father

**1**  you; the father, on good, the apostle, the father, this; and you
`~you the_father on-good apostle-father this and you`

**2**  the man, our son, on good, the apostle, this somebody, so that
`man^ our son on-good apostle-this-somebody so_that^`

**3**  seal; and the son, not somebody, this, on good, our apostle
`seal* and son not-somebody-this on-good apostle our`

**4**  the son wants […] from you, on the birth, the rest
`son want-[?] from ~you on-~be_born the_rest^`

**5**  the son's sin; and the son's sin, you are, you
`~son-sin and son-sin you exist you`

**6**  light upon you: take the forgiveness of sins, and you.
`light on-you grab-+forgiveness_of_sins and you.`

**7**  Cursed [ran], the son's sin, on doomsday, said the Lord God, holy Hezekiah,
`cursed [ran] ~son-sin on_doomsday say Lord_God holy-Hezekiah`

**8**  the prophet, to the angel of the Lord; Hezekiah the king was; the man had
`prophet on-angel <preposition_of_genitive>-Lord Hezekiah_<king> exist somebody have`

**9**  three born from whosoever; and from three born
`+three on-be_born from [?] and from +three on-be_born`

> The parable is applied: the sin of the son, and the forgiveness of sins.
> *Forgiveness of sins* on line 6 is a reading of this project's, checked at
> every occurrence. Hezekiah on lines 7 and 8 is Király & Tokai's own sign,
> and the turn to him is abrupt; 2 Kings 20 and Isaiah 38 are the Hezekiah
> the book uses elsewhere, the sickness and the added years.

## 151v — the forgiveness of sins

**1**  not was […] and has; but there is the son's sin; remit
`not ~exist-[?] and have but exist ~son-sin remit`

**2**  you, light, to leave; then not somebody sees the light, and
`you light to-leave then-not somebody see light and`

**3**  there is the forgiveness of sins for you; go to the forgiveness of sins
`exist +forgiveness_of_sins to you go-+forgiveness_of_sins`

**4**  within the image [likeness] created; how one Lady
`inside image [likeness] create how? one Lady`

**5**  the forgiveness of sins; and there is the forgiveness of sins, […] the forgiveness of sins
`+forgiveness_of_sins and exist-+forgiveness_of_sins [?]-+forgiveness_of_sins`

**6**  our son; the forgiveness of sins [to] you, son;
`our son forgiveness_of_sins you son`

**7**  the second, and <subject marker> the son, from whosoever, the son, in turn, girl
`second and SUBJ son from whosoever* son in_turn girl`

**8**  and on the son, girl, [not] somebody is damned; if, and the son, girl,
`and on-son girl [not] somebody be_damned if and son girl`

**9**  not somebody, the apostle, on good; and on the son, girl, is damned | in turn
`not somebody apostle on-good and on-son girl be_damned | in_turn`

> The prodigal son applied, still: the sin of the son and the forgiveness of
> it. *Forgiveness of sins* is a reading of this project's and it stands six
> times on this page alone.

## 152r — saved or damned, and the litany

**1**  if the son, girl, is somebody, apostle, on good; is somebody
`~if son girl exist somebody apostle on-good exist somebody`

**2**  saved; not somebody is damned; somebody, the third
`be_saved somebody not somebody be_damned somebody third`

**3**  son; and <subject marker> from whosoever this our good deed
`son and SUBJ from whosoever* this our good_deed =`

**4**  [penance] do; this the man can do, | upon
`[penance] do this somebody can do | on`

**5**  out of darkness into the light goes the man of the Lord God; love the Lord God;
`darkness out(ward) on-light go-somebody Lord-<suffix_of_divine_name> +<subject_marker> love Lord-<suffix_of_divine_name>`

**6**  have mercy, Lord God; righteous, Lord God; hope, Lord God;
`+<subject_marker> have_mercy Lord-<suffix_of_divine_name> +<subject_marker> righteous(ly) Lord-<suffix_of_divine_name> +<subject_marker> hope Lord-<suffix_of_divine_name>`

**7**  <subject marker> every our [with his whole heart] Lord God; <subject marker> every our virtue,
`SUBJ every our [with_his_whole_heart] Lord_God SUBJ every our virtue^`

**8**  the apostle, Lord God; <subject marker> our fast, Lord God; <subject marker> our
`apostle Lord_God SUBJ our fast Lord_God SUBJ our`

**9**  repentance until carry, Lord God; <subject marker> our belief,
`repentance until carry Lord_God SUBJ our believe`

> Lines 5 to 9 are a litany, the same shape repeated with a new virtue each
> time: love, mercy, righteousness, hope, fasting, repentance, belief. Line 2
> sets *saved* against *damned* in the book's standing formula from Mark
> 16:16. *Out of darkness into the light* on line 5 is 1 Peter 2:9.

## 152v — God be merciful to me a sinner

**1**  Lord God; <subject marker> every good deed, Lord God; <subject marker> our
`Lord_God SUBJ every good_deed = Lord_God SUBJ our`

**2**  good life, for ever and ever, within heaven land.
`good living for_ever_and_ever = inside heaven land`

**3**  in the gospel a man speaks
`inside gospel somebody speak`

**4**  the Lord Christ, the son of the Lord
`Lord-~Christ son <preposition_of_genitive>-Lord`

**5**  and then a man went
`then-exist go somebody`

**6**  into the temple. And
`inside temple and.`

**7**  the man knelt down inside.
`kneel_(down)-somebody inside.`

**8**  In the temple every man has this; he said to the Lord: thanks, Lord God,
`temple each,_every somebody have this say to-Lord thanks Lord-<suffix_of_divine_name>`

**9**  godfearing it is, of the Lord; holy mercy, have mercy on the sinner
`godfearing^ exist of-Lord holy-have_mercy have_mercy somebody-sin`

**10**  because this is he who repents; every sinner, to the Lord, thanks
`because this who repentance each,_every somebody-sin to-Lord thanks`

> Luke 18:10-13, the Pharisee and the publican: *two men went up into the
> temple to pray*, and *God be merciful to me a sinner*. Both halves are on
> the page — the thanks of the one on line 8, the mercy asked by the other on
> line 9 — and the book takes the publican's side on line 10.

## 153r — Lord, remember me

**1**  Lord God, find mercy, the sinful man. Holy John speaks: how
`Lord_God find_mercy^ man^ sin speak holy-John how?`

**2**  from the thief; and Christ was crucified, and the thief; and then the thief
`from thief and Christ +crucified thief and then-exist thief`

**3**  going on, who from the year, the Lord Jesus, in the place recognized that Lord Jesus
`on-go who-from-~year Lord-Jesus on-place recognize that Lord-Jesus`

**4**  righteous, the son of God, because he is; out, the thief, the Holy Spirit
`righteous(ly) son God because-exist ~out(ward) thief holy-spirit`

**5**  find mercy; and shouted to [him] on the cross: Master | ask
`find_mercy^ and shout-to on_the_cross Master | ask`

**6**  the thief; this thief: he, remember [him], on the thief.
`thief this-thief he remember on-thief`

**7**  then [when] the Lord goes into the Lord's kingdom. And then
`then go-Lord inside of-Lord kingdom^ and_said`

**8**  this [was] the rest thief; and there was the Lord, the thief crucified.
`this the_rest^ thief and exist Lord thief crucify.`

**9**  [remember me] this [thy kingdom]; then he loves | can
`[remember_me] this [thy_kingdom] then he love | can`

> Luke 23:39-42, the two thieves, and on line 6 the good thief's own words:
> *Lord, remember me when thou comest into thy kingdom*. The codex's phrase
> on line 7, *to go with the Lord into the land of the Lord*, is the kingdom.
> *Thief* stands nine times in nine lines.

## 153v — today shalt thou be in paradise

**1**  the Lord; he is to the Lord [to] redeem; and the thief, the thief, one Lord
`Lord he exist to-Lord redeem and thief thief one-Lord`

**2**  and shouted to [him], this thief, first: he <subject marker> righteous
`and shout-to this thief first he SUBJ righteous`

**3**  the man; the other thieves, these die; they deserve it
`man^ the_rest^ thief-thief this die from deserve`

**4**  and turned toward the Lord Jesus, the head of the Lord, to the thief
`and turn_toward Lord-Jézus <preposition_of_genitive>-Lord head to-thief`

**5**  And then the Lord Jesus: believe, the Lord, believe, the day until
`and_said Lord-Jesus believe the_Lord believe* day^ until`

**6**  wherefore hidden; the thief is [said to the Lord] before, in Paradise
`why?-hide_oneself exist-thief [?] before inside +into_Paradise`

**7**  and one said, from the thief: how shall we | upon
`and one say from thief ?how_shall_we | on-<preposition_of_genitive>`

**8**  the thief, the last year, heaven and earth
`thief last year-heaven land`

**9**  it is written, in the days of Moses, righteous [due reward]
`write +<subject_marker> inside +Moses-+day righteous(ly) [?]`

> Luke 23:41-43. Line 3 is the good thief's *we receive the due reward of our
> deeds*, and line 6 is *To day shalt thou be with me in paradise*. *Into
> Paradise* is Király & Tokai's own sign, cited by them at this line.

## 154r — the fire of purgatory

**1**  from [the] withered, the fire of purification, rather than hell [torment]
`from-°withered purification fire but_rather* hell [torment]`

**2**  the year [after] the soul goes out, into purification; this soul, joy
`~year-to [after] soul go out on-purification this soul joy`

**3**  because the soul goes before the face of the Lord Jesus Christ. The end
`because go-soul before from +face Lord-Jézus-Christ end`

**4**  this holy gospel. […] the world, one year redeemed, a hundred years
`this holy-gospel [?]-world one year redeem hundred-year`

**5**  suffering; heaven land; second way
`suffering heaven land second way`

**6**  there is a man, for one day of repentance | atonement
`exist somebody to one +day repentance | atone`

**7**  the man inside the fire of purification, a hundred years for one
`somebody inside purification fire ?hundred-year to-one`

**8**  day in turn; and the man, righteous, to fast and repentance | atonement
`+day in_turn and somebody righteous(ly) to-fast and repentance | atone`

**9**  somebody, our <subject marker> heaven land, and
`somebody our SUBJ heaven land and`

> Purgatory, and an indulgence reckoned in the usual medieval currency: one
> day of penance here against a hundred years of the fire. The book does the
> same arithmetic at 145v, where three Hail Marys buy a hundred years. No
> gospel is behind this page; it is the devotional literature the compilation
> is made of.

## 154v — the captive and the king

The page turns from purgatory to a story, and the story runs to 157v. A
robber takes a son captive; a king holds him in bondage; a daughter comes to
believe; she is ransomed, and at the end she is a bride. One sign stands
eleven times in four folios for the captive — *the […] son* — and it is not
in Király & Tokai's dictionary, so the person is not named here.

**1**  this man, repentance, leave; because the man, the righteous man
`this somebody repentance leave because somebody +<subject_marker> righteous(ly)-somebody`

**2**  the suffering of the Lord Christ; and the man | is saved.
`suffering Lord-Christ and somebody | +be_saved.`

**3**  somebody, for ever and ever, amen. The Lord God, be loved.
`somebody for_ever_and_ever = amen Lord_God be_loved`

**4**  wrote holy Elijah the prophet
`write holy-Elijah prophet`

**5**  and holy Luke.
`and holy-Luke.`

**6**  And then he was taken prisoner,
`then-exist take_prisoner`

**7**  the robber, the baptized son
`robber ~baptize-son`

**8**  one, from the world's king, and
`one from-world-~king and`

**9**  and then it is written, this baptized son, of […]
`then write this ~baptize-son of-[?]`

**10**  the father, the world's king; then the baptized son redeemed
`the_father-world-~king then ~baptize-son redeem`

> Lines 1 to 3 close the purgatory passage of 154r. From line 6 a new story
> begins. *Taken prisoner*, *robber*, *bondage* and *redeem* are Király &
> Tokai's own words, and they carry the whole of what follows.

## 155r — held in bondage

**1**  from the world's king, on bondage; and the baptized son cannot
`from-world-~king on-bondage and ~baptize-son cannot`

**2**  out [of] [bondage]; this humble, this baptized son; and
`out [bondage] this humble this ~baptize-son and`

**3**  sadly the baptized son left; and then [was afraid]
`sad ~baptize-son leave and then [was_afraid]`

**4**  this robber, the daughter, at the building, the daughter inside
`this +robber daughter on-to-+building daughter inside`

**5**  one house; and then for many years he led her out.
`one house and then-exist many year out(ward) lead.`

**6**  this robber on this house; and then | the daughter
`this robber on-this house and then | daughter`

**7**  believed; the believing daughter went out, home
`believe out(ward) go-daughter-believe to-home`

**8**  and then the believing daughter went home, this from […]
`and then-exist go daughter-believe to-home this from-[?]`

**9**  the baptized son; and the believing daughter began to […]
`~baptize-son and begin-daughter-believe to-[?]`

> The daughter of the house comes to believe. *Believing daughter* is one
> compound written without a space, and it stands more than twenty times in
> these four folios; the book uses it as her name.

## 155v — he could not buy him back

**1**  speak; and the daughter could not speak, because there was
`speak and can_not daughter speak because exist`

**2**  sad, the baptized son on this, of […], the father, the world's king
`sad ~baptize-son on-this of-[?] the_father-world-~king`

**3**  who, the baptized son, cannot redeem; and | went away
`who ~baptize-son cannot redeem and | go_away`

**4**  the believing daughter from the baptized son; and then
`daughter-believe from* ~baptize-son and then`

**5**  the believing daughter, and the two, the believing daughter went; then
`daughter-believe and two go-daughter-believe then-exist`

**6**  the baptized son, good, all the world; and then to […] | the daughter
`~baptize-son good all_the_world and then to-[?] | daughter`

**7**  believed, and began to talk; and the believing daughter,
`believe +begin_to_talk and daughter-believe.`

**8**  spoke to […], said to […] this.
`speak to-[?] say to-[?] this.`

**9**  From the world's king: if, how shall we [do]? The daughter believes; | redeem the daughter.
`from-world-~king if how_shall_we* daughter-believe | redeem-daughter.`

> The dumb daughter begins to talk on line 7: *began to talk* is Király &
> Tokai's own word, and the book puts it immediately after she believes.
> Line 9 asks the question the rest of the story answers.

## 156r — how shall she be ransomed

**1**  believe, to […] this bondage, said this | daughter
`believe to-[?] this bondage say this | daughter`

**2**  believing; how is this believing daughter to be ransomed?
`believe how?-exist this-daughter-believe redeem-daughter-believe`

**3**  this bondage before the daughter's belief | the father
`this bondage before of-daughter-believe | the_father`

**4**  the world's king, evil. And then this daughter, believing, this robber
`world-~king evil and_said this daughter-believe this robber`

**5**  if the believing daughter wants […] to take | this
`if daughter-believe want-[?] grab | this`

**6**  to […] the […] son, the wife | this daughter
`to-[?] [?]-son +wife | this-daughter`

**7**  believing, this […] the believing daughter wants
`believe this-[?] want-daughter-believe`

**8**  redeem this bondage; said this to the son's son, this
`redeem this bondage say this to-son-son this`

**9**  from the world's king, this […] wants […]
`from-world-~king this-[?] want-[?]`

> The king of the world is called *the evil one* on line 4, which is the
> book's word for the devil throughout. The daughter is to be ransomed and
> to be a wife. Whether the book means this as a story or as the standing
> allegory of the soul redeemed from the devil, it does not say here.

## 156v — the escape by night

**1**  this believing daughter has the […] son as husband
`this-daughter-believe have [?]-son wife`

**2**  and then this time; and then the believing daughter
`then-exist this time and then-exist daughter-believe`

**3**  to […] in the night | fled, the daughter
`to-[?] inside night | escape-daughter`

**4**  believing […]; and the rich | carried away the daughter
`believe-[?] and ~rich | from-carry-daughter`

**5**  believe […] who | the daughter believes
`believe-[?] who | daughter-believe`

**6**  to […] the rich could carry; and then
`to-[?] ~rich can carry and then-exist`

**7**  […] to […] | to the woman
`[?]-to-[?] | to-<preposition_of_genitive>-+woman`

**8**  son, the father, the world's king; and | […] daughter
`son the_father-world-~king and | [?]-daughter`

**9**  believing, saw; and went, this of the […]
`believe see and go this <preposition_of_genitive>-[?]`

> The escape, at night. The page is the most broken of the six: four of the
> nine lines carry a hole this project cannot fill, and the *[…] son* sign
> is one of them.

## 157r — the virgin daughter

**1**  the father, the world's king; and sad left the father […]; and then
`the_father-world-~king and sad leave-father-[?] and then`

**2**  to […] the believing daughter went to […] | to
`to-[?] daughter-believe go-to-[?] | to`

**3**  of […], the father […]. And then this from […]
`of-[?] the_father-[?] and_said this from-[?]`

**4**  oh, of […], to […], wish, from […]
`oh of-[?] to-[?] wish from-[?]`

**5**  love went to […] | judged from […] | this
`+<subject_marker> love go-to-[?] | judge from-[?] | this`

**6**  to […], as this virgin, the daughter, believes, said
`to-[?] as this virgin-daughter-believe say`

**7**  this to […]: this is the believing daughter, from the robber
`this to-[?] +this_is daughter-believe from +robber`

**8**  he who is to […], the robber taken prisoner
`+he_who exist to-[?] take_prisoner-+robber`

**9**  said this from […]: as this daughter believes, this woman
`say this from-[?] as this-daughter-believe this woman`

> She is called a virgin on line 6, and the robber is himself taken prisoner
> on line 8. The story is not finished here; 157v continues it.

## 157v — she is led before the Father

**1**  The believing daughter eloped; led before the Father | of the daughter
`elope-daughter-believe lead before the_Father | of-daughter`

**2**  the Lord Christ. This is the daughter who believes in the Lord Christ, in unbelief
`Lord-Christ +this_is daughter-Lord-Christ-believe inside +not_believe`

**3**  [the mother] of the daughter of the Lord Jesus Christ, the Father; and said this | the daughter of the Lord
`[the_mother] of-daughter-Lord-Jesus-Christ the_Father and say this | daughter-Lord`

**4**  Jesus Christ, this from […], [named] this daughter of the Lord Jesus Christ, believing
`Jesus-Christ this from-[?] [named] this-daughter-Lord-Jesus-Christ-believe`

**5**  within unbelief [the mother] of the daughter of the Lord Jesus Christ, believing | from
`inside not_believe [the_mother] of-daughter-Lord-Jesus-Christ-believe | from`

**6**  God the Father, because the Father, of the daughter of the Lord Jesus Christ, the wealth
`God_the_Father because the_Father of-daughter-Lord-Jesus-Christ wealth`

**7**  she has; remit, the man, [talent] [asked]; in turn | then
`have remit man* [talent] [asked] in_turn | then`

**8**  was this, from the world's king; was every […] rich | sold
`exist this-from-world-~king exist every of-[?] ~rich | sell`

**9**  from […] not is, to […]: how shall we | from
`from-[?] not exist to-[?] how_shall_we* | from`

> Her name has grown across the story: she is *the believing daughter* on
> 155r, and from here she is *the believing daughter of the Lord Jesus
> Christ*, one compound of five pieces written without a space. Every piece
> of it is read; the compound is the book's own.

## 158r — the buying and the selling

**1**  buy this, in turn; and then to […] he wanted from […]
`buy-this in_turn then-exist to-[?] want-from-[?]`

**2**  redeem this; is, is, from God, seal, from […]
`redeem-this exist exist from God-?seal from-[?]`

**3**  for ever and ever; said this from […] of […]
`for_ever_and_ever = say this from-[?] of-[?]`

**4**  to […] this […] this | the daughter of the Lord Jesus
`to-[?] this-[?] this | daughter-Lord-Jesus`

**5**  Christ who believes, […] took | to
`Christ-believe [?] grab | to`

**6**  scatter every one of […] the rich; and said this
`scatter each,_every <preposition_of_genitive>-[?] ~rich and say this`

**7**  to […] of […] the father […] | this
`to-[?] of-[?] the_father-[?] | this`

**8**  to […] this daughter of the Lord Jesus Christ, believing | wanted
`to-[?] this daughter-Lord-Jesus-Christ-believe | want`

> The most broken page of the legend: six of the eight lines carry a hole,
> and the same unread sign stands for whoever is being addressed. The sense
> is a ransom paid and goods scattered, but the actors cannot be named.

## 158v — a wife, and the end of it

**1**  to […] took; and then this time | to the woman
`to-[?] grab then-exist this time | to-<preposition_of_genitive>-+woman`

**2**  the son, righteous, a wife; and the […] son, righteous.
`son righteous(ly) wife and [?]-son righteous(ly).`

**3**  until the Lord's daughter, Jesus, believing, Christ, and | the woman wanted
`~until Lord-daughter-Jesus-believe-Christ and | want-+woman`

**4**  the son of the daughter of the Lord Jesus Christ, believing, living [happily] was.
`son-daughter-Lord-Jesus-Christ-believe living [happily] exist.`

**5**  God, all the world, for ever and ever, amen. The Lord God, be loved.
`God all_the_world for_ever_and_ever = amen Lord_God be_loved`

**6**  Before the Word, written
`before Word^ write`

**7**  by holy Luke, in the fourth chapter | of
`holy-Luke inside two-two chapter | of`

**8**  the writing; the time | then
`write time | then`

**9**  the Lord Jesus was, in the thirtieth
`exist Lord-Jézus inside thirty`

> The legend ends with a marriage and a son, and closes on the book's
> standing formula. Then a new gospel is announced. The chapter number the
> codex gives, four (two-two; an earlier printing read it as twenty-two, which
> was wrong), is its own; the passage that follows is the Gadarene demoniacs,
> which is Luke 8 and Matthew 8.

## 159r — two men with spirits

**1**  and second year; the time; the Lord Jesus went to the shore; bread
`two-year time go Lord-Jézus shore bread`

**2**  and then the Lord Jesus met the shore of the sea
`and then meet^ Lord-Jesus shore sea`

**3**  one hundred pigs; and then [he] met
`one hundred pig and then meet^`

**4**  the Lord Jesus, the shore of the sea, among one
`Lord-Jézus shore sea among one`

**5**  mountain, two men with spirits; in the two men there were | six
`mount two somebody-spirit inside two somebody exist | six`

**6**  thousand and six hundred and sixty and six devils; and how
`hundred and six_hundred* and six-ten and six devil = and how?`

**7**  two men, created, found two somebodies; these created two men
`two man^ create find-two-somebody this create two man^`

**8**  aforesaid [tombs]; in turn [possessed] the two men were, to take | the Lord
`aforesaid [tombs] in_turn [possessed] exist two man^ to-grab | Lord`

> Matthew 8:28, *there met him two possessed with devils, coming out of the
> tombs, exceeding fierce* — Matthew has TWO, where Mark and Luke have one,
> and the codex follows Matthew. The devils are counted on lines 5 and 6:
> six thousand six hundred and sixty-six, Király & Tokai's count (159r05-06,
> reading the sign on line 6 as *thousand*), which is the book's own number
> for them at 028v too. Corrected 2026-09-26: the earlier printing read six
> hundred and sixty-six. The
> gospels call them Legion.

## 159v — the devils ask to be sent into the swine

**1**  Jesus Christ; and the two men went to the Lord Jesus, and began
`Jézus Christ and go two somebody to-Lord-Jézus and begin`

**2**  two somebodies shouted to [him]: Master [torment]; and the Lord went before
`two somebody shout-to Master [torment] and Lord go before`

**3**  the time; he loved the two men; the devils' suffering, the Lord, all
`time love two somebody devil^ suffering Lord all^`

**4**  died of many sufferings; and the two men began
`die ?from many suffering ~and begin two somebody`

**5**  the devils to ask, into the leftover food(?); and
`devil^ ask inside leftovers food? and`

**6**  then [from] the two somebodies the devils were chased
`then two somebody devil^ exist chase`

**7**  by the Lord Jesus into the leftover food(?), because, name, sat, year
`Lord-Jesus inside leftovers food? because name-°sat-~year`

**8**  the Lord Jesus scattered them from the leftover food(?)
`Lord-Jesus from leftovers food? scatter`

**9**  in turn from two somebodies the woman, baptize, spirit; the Lord God redeemed.
`in_turn from two somebody woman baptize spirit redeem Lord_God`

> Matthew 8:31, *if thou cast us out, suffer us to go away into the herd of
> swine*. The book has no word for swine and uses Király & Tokai's
> *leftover food* — the swill the herd is fed — three times for them. The
> devils ask, and are sent.

## 160r — the herd runs into the sea

**1**  and then he saw this, the shepherd, and through
`and then see he this shepherd and through`

**2**  startled, and fled to the herdsmen's home
`startle and escape to-<preposition_of_genitive>-shepherd home`

**3**  and said the shepherd: the Lord seen of the shepherd. And then
`and say shepherd Lord-see of-shepherd and_said`

**4**  they went from the Lord […] saying: Jesus of Nazareth. And every
`go-from-Lord [?]-from say Jézus +Nazareth and each,_every`

**5**  aforesaid herd of the herdsmen perished in the sea;
`aforesaid of-shepherd herd inside sea perish^`

**6**  the Lord humble, the Jews; and sad [they] left […]. End [of] this
`Lord ~humble-Jews and sad leave-[?] end this`

**7**  apostolic holy gospel. This holy gospel begins, written by holy Luke
`apostle holy-gospel begins this holy-gospel write holy-Luke`

**8**  in the fourth chapter of the writing; the time the Lord Jesus sat
`inside two-two chapter of-write time sit Lord-Jesus`

**9**  by the sea; then, in his thirty-second year
`on-sea then-exist inside thirty two-year`

> Matthew 8:32-34: *the whole herd of swine ran violently down a steep place
> into the sea, and perished in the waters. And they that kept them fled,
> and went their ways into the city, and told every thing*. Both halves are
> here in order. The book dates the miracle to Jesus's thirty-second year,
> which is its own reckoning and no gospel's.

## 160v — the Lord returns to Capharnaum

**1**  Within, there was one of the Lord God, and through [preached] the Lord Jesus into
`inside one ~exist Lord-<divine> and through [?] Lord-Jézus inside`

**2**  one land [Capharnaum] within one town
`one land [Capharnaum] inside one town`

**3**  [was in the house] the home; and then the Jews saw the Lord Jesus go,
`[was_in_the_house] home and then see-Jews go-Lord-Jesus`

**4**  and the Jews began to shout to [him] [the palsy]; and the Lord went;
`and begin-Jews shout-to [the_palsy] and go-Lord`

**5**  he wanted, the Lord, the Jews from high, of the Jews' rich [the roof]
`he want-Lord Jews from-high of-Jews ~rich [the_roof]`

**6**  he made ready, and the Lord Jesus returned | into
`prepare and-Lord return Lord-Jézus | inside-and`

**7**  the middle of the Lord's town; and this town |
`in_the_middle-inside <of>-Lord town and this town |`

**8**  name was Capharnaum; and took
`name exist Capharnaum and grab`

**9**  to himself three apostles, Peter and Paul and
`to-Lord three apostle Peter and Paul and`

> Mark 2:1: *And again he entered into Capharnaum after some days, and it was
> heard that he was in the house.* The codex names the town outright on line 8
> and the next folio names it again.

## 161r — the paralytic, and the four who carried him

**1**  John; because then the Lord Christ would do a miracle,
`John because then-exist Lord Christ miracle do, want`

**2**  and every miracle the Lord had to confess; and then | he preached,
`Lord-to each,_every miracle confess have and then-exist | preach`

**3**  the Lord, in Capharnaum; and many people followed the Lord,
`Lord inside Capharnaum and follow to-Lord many people`

**4**  and then […] carried one ill before
`and then-[?] carry one ill before`

**5**  the Lord Jesus, within | a man, four men, at the head.
`Lord-Jesus inside | man^ two-two man head.`

**6**  Among them: faith, love, hope, forgiveness; and | they could not
`among believe love hope forgive^ and | can`

**7**  the four bearers within, but rather up on the temple
`the_four_bearers inside °but_rather-up on-temple`

**8**  they went, the four bearers; and the temple
`go the_four_bearers and temple`

**9**  through pierced, the four bearers, to up
`through pierce the_four_bearers to-up`

> Luke 5:18-19, Douay: *behold, men brought in a bed a man who had the palsy:
> and they sought means to bring him in... And not finding by what way they
> might bring him in, because of the multitude, they went up upon the roof,
> and let him down through the tiles with his bed.* The four bearers are the
> codex's own count and not the gospel's -- and Kiraly and Tokai's dictionary
> already carries a sign glossed "the four friends of the paralytic man in
> Luke 5:17ff", so the identification of this page is theirs, not this
> project's.

## 161v — thy sins are forgiven thee

**1**  onto the roof; and a man, [with] a rope, | let down, asking, love, hope,
`on-roof and man^ rope | go-~ask-love-hope`

**2**  forgiveness, to the Lord, before the Lord Jesus Christ; the Lord Jesus saw, and was saved
`forgive^ Lord before Lord-Jesus-Christ see Lord-Jesus be_saved`

**3**  our belief, from four men, and the man
`our believe from two-two man and man^`

**4**  forgave, the Lord Jesus Christ. And then the Lord Jesus: son of the Lord
`forgive^ Lord-Jesus-Christ and_said Lord-Jesus son of-Lord`

**5**  asking son, loving son, hoping son, | forgiveness;
`~ask-son love-son hope-son | forgive^`

**6**  the son shall have health, the son; and
`son exist have-son health son and`

**7**  then the Lord was [there] [their faith]; the Lord, the Jew, the Lord Jesus;
`then-Lord exist [their_faith] Lord Jew Lord-Jesus`

**8**  And then the Lord Jesus: [thy sins] | say, believe, somebody, love
`and_said Lord-Jesus [thy_sins] | say-believe-somebody-love`

**9**  hope, man, have mercy, man; there is [forgiven]
`somebody-hope-somebody-have_mercy-somebody exist [?]`

**10**  a man, or rise, and go, man.
`have-somebody or +rise ?and go-somebody`

> Luke 5:20, Douay: *Whose faith when he saw, he said: Man, thy sins are
> forgiven thee.* The codex keeps its own four-word chain -- faith, love, hope,
> mercy -- through the whole scene, which is a devotional gloss on the verse
> rather than the verse.

## 162r — rise, take up thy bed and walk

**1**  The Jews said [blaspheme] | said: believe, man, love, man,
`say Jew [blaspheme] | say-believe-somebody-love-somebody`

**2**  hope, man, have mercy, man; there is, therefore, a man,
`hope-somebody-have_mercy-somebody exist ?therefore have-somebody`

**3**  said the Lord Jesus rightly; <subject marker> spoke the Jew. And then | the Lord
`say Lord-Jesus righteous SUBJ speak Jew and_said | Lord`

**4**  Jesus took […] of the son | asking, love, hope,
`Jesus grab-[?] of-son | ~ask-love-hope`

**5**  mercy, the year; and the stretcher
`have_mercy-~year and stretcher`

**6**  he took, and put the son on the stretcher,
`grab and put son stretcher`

**7**  upon the son's shoulder; and the man went, and the son was saved,
`on-<of>-son shoulder and go-somebody-son be_saved`

**8**  our son, home, heaven. Here ends this holy gospel.
`our son ~home heaven here_ends this holy_gospel`

**9**  The Lord Christ, three dead <subject marker> rise, the Lord resurrected | of
`Lord-Christ three the_dead SUBJ rise^ resurrect-Lord | of`

> Luke 5:24-25: *Arise, take up thy bed, and go into thy house. And
> immediately rising up before them, he took up the bed on which he lay: and
> he went away to his own house, glorifying God.* The stretcher is read; the
> shoulder is the codex's own detail.

## 162v — the three whom the Lord raised

**1**  the Lord, the Father can; first stand up, resurrect, the Lord Jesus,
`Lord the_Father can first stand_up resurrect Lord-Jesus`

**2**  one head's daughter within Jerusalem; second | died
`one head daughter inside Jerusalem second | die`

**3**  man he stood up and raised, the Lord Jesus: Lazarus, in Jerusalem; | and the
`somebody stand_up resurrect Lord-Jézus Lazarus inside Jerusalem | in_turn`

**4**  three dead stand up, resurrect, the Lord Jesus, Nain;
`three the_dead stand_up resurrect Lord-Jesus Nain`

**5**  [maiden] therefore stand up, resurrect; and three dead to the Lord,
`[maiden] therefore* stand_up resurrect and three the_dead to-Lord`

**6**  the Lord Christ: but rather the daughter, Lazarus, the son, the Father,
`Lord-Christ but_rather* daughter Lazarus son the_Father`

**7**  of the Lord stand up, resurrect, of the Lord's hands, of the Lord.
`of-Lord stand_up resurrect of-Lord hands of-Lord`

**8**  the finger [into]; the miracle he did. | The Lord,
`finger [into] miracle do | Lord`

**9**  God the Father, Son, God, Jesus, Holy Spirit; the Lord God, be loved.
`God_the_Father-son-God-Jesus-holy-spirit Lord_God be_loved`

> The three raisings in the gospels are exactly these three: the daughter of
> Jairus (Mark 5:41), Lazarus (John 11:43), and the widow's son at Nain
> (Luke 7:14). The codex lists them in that order and names all three. This is
> a page of its own reckoning, not a gospel passage, and it is the kind of
> summary a preacher's handbook carries.

## 163r — the widow of Nain

**1**  This holy gospel begins,
`begins this holy-gospel`

**2**  written by holy Luke, in
`write holy-Luke inside`

**3**  the […] chapter of the writing:
`one-[?] chapter <of>-write`

**4**  the time, then,
`time then-exist`

**5**  the Lord Jesus, in his thirty- | second
`Lord-Jézus inside thirty | two`

**6**  year; the time he went, | the Lord
`year time go | Lord`

**7**  Jesus, into one town; and this town's name
`Jézus inside one town and this town name`

**8**  was Nain; and many people went to the Lord,
`exist Nain and go to Lord many people`

**9**  and then to the Lord the seventy and the twelve apostles, and | then
`and then-exist to-Lord seventy and six-six apostle and | then`

**10**  then the Lord Jesus kept going to this town, and then
`then-exist keep_going Lord-Jézus this town and then-exist`

**11**  there died in this town the son of one widow woman.
`die inside this town son one virgin-woman`

> Luke 7:11-12, Douay: *he went into a city that is called Naim; and there
> went with him his disciples, and a great multitude. And when he came nigh to
> the gate of the city, behold a dead man was carried out, the only son of his
> mother: and she was a widow.* The codex names Nain outright, and its
> seventy is Luke 10:1, which it has folded in.

## 163v — weep not

**1**  and the son carried; not who, son, Lord God, thief; not humble;
`and son carry not who-~son Lord_God thief not humble`

**2**  the son was the Lord God's; not God had the son out [of] the town,
`son exist Lord_God not God have-~son out on-town`

**3**  four among the men, at the head, because they had him within.
`two-two among man head because have inside.`

**4**  The Old Testament word: thrown out, out [of the] town, to, from, aforesaid, all the world; and there were
`Old_Testament word throw_out out town to-from aforesaid all_the_world and exist`

**5**  to the son many people; and then left an army,
`to son many people and then leave an_army`

**6**  an army, among the gate, from two peoples, people, two;
`an_army among gate from-two people people two`

**7**  and they stood [compassion]; and the Lord Jesus saw many
`and stand^ [compassion] and see Lord-Jesus many`

**8**  sad. And then this woman remained, baptize,
`sad and_said this woman = remain-baptize`

**9**  sorrowing, this one; how then this? Said the Lord Jesus: stand up | this
`sad(ly) this how? then-exist this say Lord-Jézus stand_up | this`

> Luke 7:13: *Whom when the Lord had seen, being moved with mercy towards her,
> he said to her: Weep not.* The codex has the seeing and the sorrow in the
> right order, and it makes the crowd at the gate an "army", which is its own
> word for a multitude and is read at three other places in the book.

## 164r — young man, I say to thee, arise

**1**  the woman's son; and the Lord Jesus stood from the coffin, which within the coffin
`woman of son and stand^ Lord-Jesus from coffin which inside coffin`

**2**  to the son, to the son, from the four men at the head; and
`to-~son to-~son from two-two man head and`

**3**  the Lord Jesus touched with [his] hands from the coffin, which within the coffin
`touch Lord-Jesus of hands from coffin which inside coffin`

**4**  lay dead, the son of this widow. And then | the Lord
`lie die son this widow and_said | Lord`

**5**  Jesus raised this son -- in this example, the son [arise] -- and he rose
`Jézus +rise this son ?example son [?] and +rise`

**6**  on sitting; how? one prophet. And then: this is
`on-sit how? one prophet and_said this_is`

**7**  the Lord went; his descendant, to the pleasing of the Lord, the prophet foretold through this
`go-Lord descendant to-pleasing-Lord prophet through predict this_is`

**8**  went the Lord. And then the Lord Jesus took the son, of the son | believe
`go-Lord and_said Lord-Jesus grab-~son of-son | believe`

**9**  love, hope […]; and | faith, love, hope
`love-hope-[?] and | believe-love-hope`

> Luke 7:14-16, Douay: *And he came near and touched the bier. And they that
> carried it, stood still. And he said: Young man, I say to thee, arise. And
> he that was dead, sat up, and began to speak... And there came a fear on
> them all: and they glorified God, saying: A great prophet is risen up among
> us.* The touching of the bier, the sitting up, and the prophet are all here
> in the gospel's order.

## 164v — and he gave him to his mother

**1**  mercy, the day; and put the son, the stretcher, | on the
`have_mercy day and put son stretcher | on-of`

**2**  son's shoulder; and the son gave [himself] into the hands of the Lord Jesus; and
`son shoulder and son give^ on-hands Lord-Jesus and`

**3**  then the son was; the Lord took the son's mother, and
`then-exist son exist grab-Lord <of>-son mother and`

**4**  the son went to the temple, the mother; he was saved; the son's temple, the mother,
`go son temple mother be_saved <of>-son temple mother`

**5**  home to heaven; much joy, in turn, one sorrow remitted.
`~home heaven many joy in_turn one sad(ly) remit`

**6**  The second somebody saw, can, the Lord Jesus Christ; and the Lord
`second see-somebody can Lord-Jesus-Christ and Lord`

**7**  every thanks they gave him. Here ends this holy gospel. The Lord's love.
`each,_every thanks grab-somebody end this holy-gospel the_Lord love`

**8**  Written by holy Luke in the […] chapter of the writing.
`write holy-Luke inside one-[?] chapter <of>-write`

**9**  This woman signifies the mother, the temple, faith, baptize,
`this woman symbolize mother temple believe ~baptize`

> Luke 7:15: *and he gave him to his mother.* The last line turns the page
> round: from here to 166v the codex stops telling the story and expounds it,
> saying what each figure in it signifies. That is the shape of a sermon on a
> pericope, and it is why the same formula -- "as Saint Luke writes in this
> example" -- runs down the next three folios.

## 165r — what the widow and her son signify

**1**  baptize; the son symbolizes the soul of everybody, that the Lord God, the Creator Lord,
`baptize son symbolize soul everybody = that* Lord_God Creator_Lord`

**2**  every man; this town signifies that, that he is saved,
`each,_every somebody this town symbolize ?that ?that +be_saved`

**3**  that [signifieth] the Lord Jesus Christ, all the whole world | this
`that* [signifieth] Lord-Jesus-Christ every all_the_world world | this`

**4**  this is saved: everybody [who] believes, baptize, baptize [signifieth]
`this be_saved everybody = believe ~baptize baptize [signifieth]`

**5**  the Lord saved, the Lord Jesus Christ, the Father of the Lord.
`the_Lord be_saved Lord-Jesus-Christ the_Father of-Lord`

**6**  In this gospel, as holy Luke writes, there went four men
`inside this gospel SUBJ write holy-Luke go two-two man`

**7**  at the head, to the son; in this example the son [arise] and the son
`head to-~son this ?example son [?] and son`

**8**  was dead; and the son [they] took and carried; not love | the Lord
`exist die and son grab and carry not love | Lord`

**9**  the divine one; the thief <subject marker> is not humble; the Lord God not have
`DIV thief SUBJ not exist humble Lord_God not have`

> The allegory is the standard one of the period: the dead young man is the
> soul in sin, the widowed mother is the Church, the town is the world, and
> the bearers are the things that carry a soul to burial. Nothing on this
> folio is a gospel verse; all of it is exposition.

## 165v — the first of the four ways

**1**  the Lord God; and this not repentance [confession] took this son, this
`Lord_God and this not repentance [confession] grab this son this`

**2**  widow woman; and the son was carried out, into belief.
`virgin-woman and son carry out(ward) on-believe.`

**3**  baptize, baptize: that is, cast out, the son remitted, saved,
`~baptize baptize that_is cast_out son remit be_saved`

**4**  the damned son, for ever and ever. Within the gospel writes
`be_damned son for_ever_and_ever = inside gospel write`

**5**  holy Luke this example: not love the most high Lord God | from
`holy-Luke this example* not love most_high Lord_God | from`

**6**  the literal, every creature, than various creatures; love the son, and not who.
`literal every create than various create love-son and not who`

**7**  Then the dead son goes to the son, and leaves; not love,
`then die-son go to-son and leave not love`

**8**  on the first way. Within the gospel writes holy Luke:
`on-one way inside gospel write holy-Luke`

**9**  this example: there were many thieves, but by name the son
`this ?example <subject> exist many thief +but-+name-to son`

> The four ways are the folio's own structure: the first is love, the second
> the thief, the third humility, the fourth what the son has. Each is
> introduced with the identical formula -- "in the gospel written by holy
> Luke, this example, therefore..." -- which is what fixed the reading of the
> sign rendered *example* here (six occurrences, 164r to 166r).

## 166r — the second, third and fourth ways

**1**  on repentance took; then the dead son goes to the son.
`on-repentance grab then die-son go to-son.`

**2**  And the thief leaves, on the second way. Within the gospel writes
`and leave thief on-two way inside-gospel write`

**3**  holy Luke this example: not being humble, son,
`holy-Luke this example* not exist humble son`

**4**  somebody, and the Lord God; then the dead son goes to the son,
`somebody and Lord_God then die-son go to-son`

**5**  and leaves; not being humble, on the third way. Within the gospel
`and leave not exist humble on-+three way inside-gospel`

**6**  writes holy Luke this example: not having,
`write holy-Luke this example* not have`

**7**  the son, the Lord God, in all of the son's [whosoever sins dies]
`son Lord-<divine> inside each,_every <of>-son [?]`

**8**  [dead] the son is within [whosoever sins dies]
`[?] <subject> exist son inside [?]`

**9**  then the dead son goes to the son, and leaves; not having,
`then die-son go to-son and leave not have`

## 166v — the whole law in two commandments

**1**  on the fourth way; and [between] four men and the son
`on-two-two way and [between] two-two man and son`

**2**  they took, the four men, and carried the son out the town gate
`grab two-two man and son carry out the_town_gate*`

**3**  town, on belief; baptize, baptize; on damnation, then
`town on-believe ~baptize baptize on-be_damned then`

**4**  the son is carried into hell, damned, is ever
`son carry inside hell be_damned exist ever.`

**5**  ever. [with thy whole soul] not saved. Writes within
`ever [with_thy_whole_soul] not be_saved write inside`

**6**  Moses, truly: love the Lord God highest [above] all creation, all our
`Moses true^ love Lord_God highest all^ create all^ our`

**7**  soul, all our might, all our heart; and
`soul all^ our might all^ our heart and`

**8**  our father's son, as somebody [his] neighbour | of
`our the_father son as somebody neighbour | of`

**9**  the man; heaven and earth. Here ends this holy gospel.
`somebody <subject> heaven land end this holy-gospel`

> Deuteronomy 6:5 by way of Mark 12:30-31, Douay: *Thou shalt love the Lord thy
> God with thy whole heart, and with thy whole soul, and with thy whole mind,
> and with thy whole strength... Thou shalt love thy neighbour as thyself.*
> The codex attributes it to Moses, which is right -- it is Deuteronomy -- and
> it keeps all four "with all thy" clauses.

## 167r — a certain rich man had a steward

**1**  This holy gospel begins,
`begins this holy-gospel`

**2**  written by holy Luke
`write holy-Luke`

**3**  in the sixth chapter of the writing:
`inside six chapter <of>-write`

**4**  the time the Lord Jesus said
`time say Lord-Jézus`

**5**  to the apostles of the Lord, and to the Jewish
`apostle <of>-Lord and Jew(ish)`

**6**  people: there was a rich somebody, who left, from the rich [man's] sight,
`people exist one rich-somebody who leave-from-rich-see`

**7**  a steward over the rich man's goods | — sight, speech, life, hearing,
`manager on-<of>-Lord-rich-somebody | rich-see-say-living-hear`

**8**  soul, body, reason, sense, all to manage;
`soul-body-reason-sense every manage`

**9**  and the man began, the steward, this rich man's
`and begin-somebody-manager this rich <of>-Lord-rich-somebody`

**10**  sight, speech, life, hearing, soul, body, reason,
`see-say-living-hear-soul-body-reason`

> Luke 16:1, Douay: *There was a certain rich man who had a steward: and the
> same was accused unto him, that he had wasted his goods.* The codex names
> the goods, and they are not goods: sight, speech, life, hearing, soul, mind,
> reason, sense. It is expounding the parable as a man's stewardship of his
> own faculties, which is how the preachers of the period read it, and it
> repeats the same eight-word chain four times over the next three folios.

## 167v — the same was accused unto him

**1**  sense to manage; and then <subject marker> began, the man, and then
`sense manage and then SUBJ begin man* and then`

**2**  a man came to accuse one servant before
`somebody exist accuse one servant before`

**3**  the steward; the man's lord spoke to the servant, this serving angel:
`<of>-manager somebody-Lord say-~servant this angel-servant`

**4**  all of the rich man's | […] soul,
`each,_every <of>-Lord-rich-somebody | [?]-soul.`

**5**  body, reason, sense [give an account] sense,
`body-reason-sense [give_an_account] sense`

**6**  the word scattered; got angry, this rich, rich Lord God | this rich.
`word scatter get_angry this rich-rich-Lord_God | this-rich.`

**7**  The man. And then to the account: many not of the Lord, rich somebody,
`man^ and_said to-?the_account many not of-Lord-rich-somebody`

**8**  the steward; and he heard this, the steward, this said from
`manager and hear this manager this say from`

**9**  the steward's rich lord [put out] and | sorrowing
`of-manager Lord-rich-somebody [put_out] and | sad`

> Luke 16:2: *Give an account of thy stewardship, for now thou canst be
> steward no longer.* The account is already read as a sign of K&T's, and the
> scattering of the goods is Luke's *dissipasset*.

## 168r — what shall I do?

**1**  the steward, the manager left. And then this steward, the crying manager,
`steward^ leave-manager and_said this steward^ crying-manager`

**2**  [dig] and [I am not able] [to beg] and try, pray thee [I am ashamed]
`[dig] and [I_am_not_able] [to_beg] and °try-°pray_thee [I_am_ashamed]`

**3**  the steward [thought]; and the manager found one friend.
`steward^ [thought] and one friend find-manager`

**4**  and then this steward had two debtors | of
`and then-exist have this manager two indebted | <of>`

**5**  the steward, a man of mercy and of alms; and | then
`manager ?man have_mercy and alms and | then`

**6**  there was, among the steward's, this one debtor of mercy; and this said,
`exist among-manager this one indebted have_mercy and say this`

**7**  the steward: how much mercy dost thou owe the steward? [my lord]
`manager how_much? have_mercy indebted <of>-manager [?]`

**8**  And then the debtor, have mercy, somebody: a hundred measures
`and_said debtor^ have_mercy-somebody hundred measure`

**9**  of oil. And then this steward sat [him] [down], have mercy, somebody,
`oil and_said this steward^ sit-have_mercy-somebody`

> Luke 16:3-6, Douay: *And the steward said within himself: What shall I do...
> To dig I am not able; to beg I am ashamed... Therefore calling together
> every one of his lord's debtors, he said to the first: How much dost thou
> owe my lord? But he said: An hundred barrels of oil. And he said to him:
> Take thy bill and sit down quickly, and write fifty.* The sitting down is
> here, and the hundred is here. The codex has renamed the two debtors mercy
> and alms, which is its exposition again.

## 168v — sit down quickly, and write fifty

**1**  down, and write fifty; in turn five, rich, ten | have mercy
`down and write fifty in_turn five-rich-ten | have_mercy`

**2**  somebody, down [another] this, and this [thy bill] of the manager's
`somebody down [another] this and this [thy_bill] of-manager`

**3**  Lord God, rich somebody. And then these two, the steward | have mercy
`Lord_God-rich-somebody and_said this two steward^ | have_mercy`

**4**  the man [a hundred] [quarters of wheat] divided into two parts, the steward of mercy,
`somebody [?] [?] divide_into_parts-two-manager-have_mercy-somebody`

**5**  and among these, the steward, these two debtors | alms,
`~and among this manager this two indebted | alms`

**6**  the man; and this said, the steward: how much alms dost thou owe,
`somebody and say this manager how_much? alms indebted`

**7**  to the manager's Lord, rich somebody? And then the indebted, alms:
`of-manager Lord-rich-somebody and_said indebted alms`

**8**  a hundred measures of wheat. And then this steward | sat
`hundred measure wheat and_said this steward^ | sit`

**9**  the alms-somebody down, and write from | five
`alms-somebody down and write from | five`

> Luke 16:7: *Then he said to another: And how much dost thou owe? Who said:
> An hundred quarters of wheat. He said to him: Take thy bill, and write
> eighty.* The codex's two debtors owe oil and wheat in Luke's order, and the
> hundred is written with its own numerals both times.

## 169r — the lord commended the unjust steward

**1**  thirty; in turn twenty, rich, alms-somebody, down [another]
`thirty in_turn two-ten-rich alms-somebody down [another]`

**2**  this, and these two [eighty] [thy bill] of the steward's rich Lord God;
`this and this two [?] [?] <of>-manager Lord-<divine>-rich-somebody`

**3**  and in turn unjust steward he took, this, the steward's rich Lord God,
`in_turn [?] grab this <of>-manager Lord-<divine>-rich-somebody`

**4**  because the steward found a friend. And then this steward
`because steward^ friend find and_said this steward^`

**5**  these two, the steward's men of alms [a hundred] [quarters of wheat] | divided,
`this two-manager-alms-somebody [a_hundred] [quarters_of_wheat] | divide`

**6**  two managers, alms-somebody. And then the Lord Jesus:
`two-manager-alms-somebody and_said Lord-Jesus`

**7**  O, of the Lord, son; have, apostles, truly: the steward was
`oh <of>-Lord son have-apostle righteous(ly) manager exist`

**8**  have, apostles, friend find; because the Lord, I, this
`have-apostle friend find because-Lord I this`

**9**  rich Lord God, the man; the Lord took to you many riches,
`rich-Lord-<divine>-somebody grab-Lord you many rich`

> Luke 16:8: *And the lord commended the unjust steward, forasmuch as he had
> done wisely.* The eighty of the gospel is written here as thirty and twenty
> and five, which is the codex's own arithmetic and not Luke's.

## 169v — the goods are the senses

**1**  the Lord took to you sight, the Lord took to you
`grab-Lord you see grab-Lord you`

**2**  speech, the Lord took to you life, the Lord took to you
`say grab-Lord you living grab-Lord you`

**3**  hearing, the Lord took to you soul, the Lord took | is he
`hear grab-Lord you soul grab-Lord | ?is_he`

**4**  yours; the body the Lord took [from] you, reason
`yours body grab-Lord you reason`

**5**  the Lord took to you, sense the Lord took.
`grab-Lord you sense grab-Lord.`

**6**  To you, all of the rich Lord God's | sight, speech,
`you each,_every <of>-Lord-<divine>-rich-somebody | rich-see-say.`

**7**  life, hearing, soul, body, reason, sense;
`living-hear-soul-body-reason-sense`

**8**  and the apostles and the Jews are, truly, stewards over | sight, speech,
`and exist-apostle-Jew(ish) righteous(ly) manager inside | rich-see-say`

**9**  life, hearing, soul, body, reason, sense,
`living-hear-soul-body-reason-sense`

**10**  in turn within this world, rich have these apostles [and] Jews friend find.
`in_turn inside this world rich have this-apostle-Jew friend find`

> This is the page the whole parable was being told for. The rich man is God,
> the goods are the eight faculties the codex has been listing since 167r, and
> every man is the steward who will be called to account for them. The
> eight-word chain is written out in full four times on this folio alone, which
> is why the signs in it are among the best attested in the book.

## 170r — the account, and a new gospel begins

**1**  Here ends this holy gospel, spoken by holy Luke. Have | this:
`end this holy-gospel speak holy-Luke have | this`

**2**  the apostles, Jews, somebody, righteous stewards [of] our father,
`apostle-Jew-somebody righteous steward^ our father`

**3**  the son; and among them the man has the son.
`son and among somebody son have somebody.`

**4**  friend find, because then the dead are
`friend find because then the_dead exist`

**5**  friend; somebody grows calm; friend [at his] side.
`friend somebody grow_calm friend side^`

**6**  this holy gospel. Learning. The Lord God, be loved; the Lord God <subject marker> have mercy.
`this holy-gospel learn Lord_God be_loved Lord_God SUBJ-have_mercy`

**7**  This holy gospel begins, written by
`begins this holy-gospel write`

**8**  holy Matthew in the fifth chapter | of
`holy-Matthew inside five chapter | <of>`

**9**  the writing; by holy Luke within | four
`write holy-Luke within^ | two-two`

**10**  four chapter; the holy chapter of Jerusalem, within the ninth chapter:
`two-two chapter holy-chapter-+one-Jerusalem within^ nine chapter`

**11**  time; then the Lord Jesus within
`time then Lord-Jesus within^`

> The codex gives its own chapter references on lines 8 to 10, and the story
> that follows is Matthew 9 and Luke 8: the question about fasting, then
> Jairus, then the woman with the issue of blood. Its numbering is not the
> numbering of a printed Bible, which is worth saying plainly -- it has the
> right books in the right order and its own chapter count.

## 170v — can the children of the bridegroom mourn?

**1**  his thirtieth year; the time the Lord Jesus went into the temple at Jerusalem, and | then
`thirty years* time go Lord-Jézus inside Jerusalem temple and | then`

**2**  he was in the temple; the Lord Jesus went, and the Lord saw who, much joy
`exist inside temple go Lord-Jesus and see-Lord who* many joy`

**3**  and much sorrow; and from afar off were the apostles of holy John
`and many sad(ly) and from-to-far exist apostle holy-John`

**4**  baptize, baptize; and then the Lord Jesus left. And then the apostles:
`~baptize baptize and then leave^ Lord-Jesus and_said apostle`

**5**  Master, the apostles fast, the apostles; and the Pharisees fast; in turn the Lord's apostles
`Master apostle fast-apostle and Pharisee fast in_turn of-Lord apostle`

**6**  not fast, the apostles. And then the Lord Jesus to the apostles: | on
`not fast-apostle and_said Lord-Jesus to apostle | on`

**7**  joy, in turn; then the apostles go in joy, keeping watch, while
`joy in_turn then-exist go apostle on-joy observe exist`

**8**  the apostles fast, on, that is, the apostles leave the Lord Jesus; from the head
`apostle fast ~on-that_is leave^ apostle Lord-Jesus from head`

**9**  And then the apostle Jairus: Jairus's daughter <subject marker> died, to the high priest,
`and_said apostle Jairus of-Jairus daughter SUBJ die to-high_priest`

**10**  this was who: Master; and he took this head.
`this ~exist-who Master and take^ this head.`

> Matthew 9:14-15, Douay: *Then came to him the disciples of John, saying: Why
> do we and the Pharisees fast often, but thy disciples do not fast? And Jesus
> said to them: Can the children of the bridegroom mourn, as long as the
> bridegroom is with them?* Then 9:18: *Behold a certain ruler came up, and
> adored him, saying: Lord, my daughter is even now dead.* The codex names
> Jairus outright, which is Mark's and Luke's name for that ruler, not
> Matthew's -- so the compiler is working from more than one gospel at once.

## 171r — the woman who touched the hem

**1**  the Lord Jesus; and went the Lord, the head, Jesus, this head's
`Lord-Jesus and go-Lord-head-Jesus this head`

**2**  house; and many people went to the Lord; and there was
`house and go to Lord many people and exist`

**3**  among this people one woman, which
`among this people one woman = which`

**4**  a woman [who] was nine years, twelve years, within blood ill;
`woman = exist nine-year-six-six-year inside blood ill`

**5**  And then this woman, then Christian:
`and_said this woman = then Christian`

**6**  how shall we touch? of the woman, hands, of the Lord, clothes;
`how_shall_we* touch of-woman hands of-Lord clothes`

**7**  the hem; Christian; healing, woman, the woman left; and
`hem Christian healing-woman leave-woman and`

**8**  then [she] touched the clothes of the Lord Jesus, | within
`then touch clothes Lord-Jesus | inside`

**9**  the hour the woman was healed, the woman left off; and the Lord Jesus saw
`hour healing-woman leave-woman and see Lord-Jézus`

**10**  on the people; the hand of the Lord; there were many people. And then the Lord Jesus: this
`on-people hand-Lord ~exist many people and_said Lord-Jesus this`

> Mark 5:25-29, Douay: *a woman who was under an issue of blood twelve years...
> came in the crowd behind him, and touched his garment. For she said: If I
> shall touch but his garment, I shall be whole. And forthwith the fountain of
> her blood was dried up.* The twelve years, the touching from behind, and the
> instant healing are all here.

## 171v — thy faith hath made thee whole

**1**  woman: the woman's faith healed the woman. Did,
`woman of-woman believe healing-woman ~do`

**2**  who, year, said the Lord Jesus: I [said to] this woman, the Lord healed; but
`who-~year say Lord-Jesus I this-woman heal-Lord but`

**3**  the Lord Jesus said to this woman: the woman's faith hath healing
`say Lord-Jézus this-woman <of>-woman believe healing`

**4**  done. And | went the Lord, the head, the apostles, Jesus, the woman,
`do and | go-Lord-head-apostle-Jesus-woman`

**5**  the Jews, [to] this head's house; and | then the Lord,
`Jews this head house and | then-Lord`

**6**  the head […], Jesus, the woman, the Jews entered; and saw
`~head-[?]-Jesus-woman-Jews enter and see`

**7**  the Lord Jesus much sadness. And then the Lord Jesus [give place]:
`Lord-Jesus many sad and_said Lord-Jesus [give_place]`

**8**  not this daughter [is] dead, the daughter, but rather the daughter sleeps. And then
`not this daughter die-daughter but_rather to-sleep-daughter and then`

**9**  the Jews laughed [at] the Lord Jesus. And then the Jews: see, love | this
`Jews laugh Lord-Jesus and_said Jews see love | this`

> Matthew 9:22-24, Douay: *Be of good heart, daughter, thy faith hath made
> thee whole... Give place, for the girl is not dead, but sleepeth. And they
> laughed him to scorn.* Both sayings are here, in order, with the laughing.

## 172r — damsel, arise

**1**  the Lord [laughed him to scorn] spoke. And then the Lord Jesus [to] this head.
`Lord [laughed_him_to_scorn] speak and_said Lord-Jesus this head.`

**2**  cast this people out; and then, having cast out,
`cast_out this people out(ward) and then-exist out(ward) cast_out`

**3**  the chief man, and with the Lord Jesus the daughter's father
`head and among Lord-Jézus <of>-daughter father`

**4**  and mother. And then the Lord Jesus [to] the sky said, said, named this:
`and mother and_said Lord-Jesus sky say say name-this`

**5**  one servant, rise, servant, daughter, among [the] Virgin Mary; and | then
`one-+servant rise servant daughter among Virgin_Mary and | then`

**6**  the daughter rose, sat up. And then, lo, the Lord went,
`exist rise^ daughter on-sit and_said lo go-Lord`

**7**  his descendant, to the pleasing of the Lord, the prophet foretold through; lo, the Lord went;
`descendant to-pleasing-Lord prophet through predict lo go-Lord`

**8**  And then the Lord Jesus [had] the father [and] mother carry wine and bread
`and_said Lord-Jesus carry father mother wine and bread`

**9**  [walked] [give her to eat] and drink; and then the daughter
`[?] [?] and drink and then-exist daughter`

> Mark 5:40-43, Douay: *having put them all out, he taketh the father and the
> mother of the damsel... and saith to her: Talitha cumi, which is, being
> interpreted: Damsel (I say to thee) arise... And he bid them give her to
> eat.* The putting out, the two parents kept back, the rising and the food
> are all here in Mark's order. The wine and the bread are the codex's own.

## 172v — the fame of it went abroad, and the talents begin

**1**  drink; and the daughter ate. And then the Lord Jesus, this moon,
`drink and ~eat-daughter and_said Lord-Jesus this moon`

**2**  [the fame] not say; and the news went up [to] every sky.
`[the_fame] not say ~and news ascension^ every sky`

**3**  and earth. Here ends this holy gospel. The Lord God, with all thy heart.
`earth end this holy-gospel Lord-<divine> ?with_all_thy_heart`

**4**  This holy gospel begins,
`begins this holy-gospel.`

**5**  written by holy Stephen, the kingdom;
`write holy-Stephen kingdom^`

**6**  this word, written, the chief;
`this word write head`

**7**  this world, the Lord, the priest;
`this world Lord priest.`

**8**  and the high Magdalene year, the kingdom, all
`and high-Magdalene-~year kingdom^ every`

**9**  the Lord, baptize; and the farm, the people; this word he speaks, king; there was
`Lord ~baptize and farm people this word speak-~king exist`

**10**  a rich lord going a long way; and | then
`go-Lord one rich Lord long way and | then`

**11**  the Lord had three living servants; and then the servants
`exist have-Lord three living-servant and then-exist living-servant`

> Matthew 9:26: *And the fame hereof went abroad into all that country.* Then
> a new reading begins and it is the Talents, Matthew 25:14-15: *For even as a
> man going into a far country, called his servants, and delivered to them his
> goods.* The codex gives three servants, as Matthew does. The attribution on
> line 5 to "holy Stephen the king" is the codex's own and belongs to no
> gospel; Stephen is Hungary's first king and its patron, which is the
> strongest hint of provenance anywhere in the book.

## 173r — one talent, three talents, five talents

**1**  before the Lord; he was with the Lord; and then the Lord took
`<subject> before Lord exist ~among-Lord and then-exist grab-Lord`

**2**  one servant one gold talent; the second
`one servant one gold* talent second`

**3**  the Lord took three talents of gold; the third the Lord took,
`grab-Lord three gold* talent third grab-Lord`

**4**  five gold talents. And then this rich Lord, all, until
`five gold* talent and_said this rich-Lord every until`

**5**  this [gave]: five senses, mercy, prayer,
`this [?] five sense have_mercy pray.`

**6**  alms, faith [ability]; the servant's mouth,
`alms believe [?] servant mouth`

**7**  I go, baptize; how shall we be saved, living servant? And the Lord took the priest,
`I go ~baptize be_saved how_shall_we* living-servant and Lord grab priest`

**8**  the high Magdalene year, the kingdom, the Lord, baptize, the farm, the people, the man,
`high-Magdalene-~year kingdom^ Lord ~baptize farm people man^`

**9**  soul, soul, soul, soul. Here ends this holy gospel. The Lord's love.
`soul soul soul soul end this holy-gospel the_Lord love`

> Matthew 25:15: *And to one he gave five talents, and to another two, and to
> another one.* The codex gives five, three and one. Line 5 does to this
> parable what 167r did to the Unjust Steward: the talents are glossed as the
> five senses, mercy, prayer, alms and faith.

## 173v — after a long time the lord came

**1**  Many years passed; then this rich lord returned | to
`many year exist then-exist return this rich-Lord | on`

**2**  the lodging, because from the lodging the way of the people lay into the house of this
`lodging because from* lodging way people inside house this`

**3**  rich lord; and from the people, the servant carried this rich lord; and
`rich-Lord and from people servant carry this rich-Lord and`

**4**  then went out on | called this rich
`then go out on | called this rich`

**5**  and the Lord's living servants, the apostles, the angels; and then he did so
`and <of>-Lord living-servant-apostle-angel and then-exist do,`

**6**  among this rich lord's; the Lord's servant, before the rich lord
`among this rich-Lord <of>-Lord servant before rich-Lord`

**7**  [after a long time] the three servants stood; the Lord took | of
`[after_a_long_time] three SUBJ servant exist-Lord grab-Lord | of`

**8**  the rich Lord. And then this rich Lord, this one to whom
`Lord rich and_said this rich-Lord this one to_whom`

**9**  the Lord had given five talents of gold —
`<subject> exist-Lord grab-Lord five gold.* talent`

**10**  talent. And then this rich Lord reckoned with the servant: how shall we, somebody
`talent and_said this rich-Lord reckon_with* servant how_shall_we-somebody`

> Matthew 25:19, Douay: *But after a long time the lord of those servants came,
> and reckoned with them.* The reckoning formula stands on three consecutive
> folios, 173v:10, 174r:7 and 174v:5, always in the same words, which is what
> fixed the reading of that sign.

## 174r — well done, good and faithful servant

**1**  of the rich Lord? This servant said: how shall the man be pleasing to the Lord God? And
`<of>-Lord rich say this servant how_shall_we-somebody to-pleasing Lord-<divine> and`

**2**  received the aforesaid five gold talents. And then this rich Lord:
`receive* five gold* aforesaid talent and_said this rich Lord`

**3**  go, servant, into the Lord's house, to the Lord's Father, and
`go-servant inside of-Lord house to-of-Lord the_Father and`

**4**  to God the Father; somebody is a joy-somebody ever
`to-God_the_Father somebody exist joy-somebody ever`

**5**  ever, amen. And then called this second,
`ever amen and then called this two`

**6**  to whom the Lord had given three talents of gold;
`to_whom <subject> exist-Lord grab-Lord three gold* talent`

**7**  And then this rich Lord reckoned with the servant: how shall we, somebody | of
`and_said this rich-Lord reckon_with* servant how_shall_we-somebody | of`

**8**  the rich Lord? This servant said: how shall the man be pleasing to the Lord God?
`Lord rich say this servant how_shall_we-somebody to-pleasing Lord-<divine>`

**9**  And [he] received the aforesaid three gold talents. And then this rich Lord:
`and receive* three gold* aforesaid talent and_said this rich Lord`

> Matthew 25:21: *Well done, good and faithful servant... enter thou into the
> joy of thy lord.* The codex renders the joy of the lord as going into the
> Lord's house, to the Father, and adds its own Amen.

## 174v — the third servant

**1**  go, servant, into the Lord's house, to the Lord's Father, and | to
`go servant inside of-Lord house to-of-Lord the_Father and | to`

**2**  God the Father; the man is in joy for ever and ever,
`God_the_Father man^ exist ~joy for_ever_and_ever =`

**3**  amen. And then called this third, to whom <subject marker>
`amen and then called this three to_whom SUBJ`

**4**  the Lord had given one talent of gold;
`exist-Lord grab-Lord one gold* talent`

**5**  And then this rich Lord reckoned with the servant: how shall we, somebody?
`and_said this rich Lord reckon_with* servant how_shall_we-somebody`

**6**  Of the rich Lord, this servant said [hard] servant [thou reapest]
`<of>-Lord rich say this servant [?] servant [?]`

**7**  [where] [thou hast not sown] [gatherest] there is love, there is riches [ability] servant,
`[?] [?] [?] love-exist exist-rich [?] servant`

**8**  because he [afraid] had the servant; because then this servant
`because he [afraid] have servant because then this-servant`

**9**  of the rich Lord lost, the servant; he is [hid in the earth]
`of-Lord rich lose ~servant he exist [hid_in_the_earth]`

> Matthew 25:24-25, Douay: *But he that had received the one talent, came and
> said: Lord, I know that thou art a hard man; thou reapest where thou hast
> not sown... and being afraid I went and hid thy talent in the earth.*

## 175r — take the talent from him

**1**  on the servant; the rich [Lord] has he, and from [extort] on the servant
`on-~servant rich have he and from [extort] on-~servant`

**2**  took; because this rich Lord God [take away] [talent] | […] the Jews
`grab because this-rich Lord_God [take_away] [talent] | [?]-Jews`

**3**  the man; and said. And then this rich Lord:
`man* and say and_said this-rich-Lord`

**4**  this unprofitable servant, high, this servant, this | servant's love
`this unhelpful servant high this-servant this | ~servant-love`

**5**  is this: the eye seems, servant; the Lord's house long; this | love
`exist this eye seem^ servant of-Lord house long this | love`

**6**  is: go, servant, into the Lord's house. And then this rich
`exist go-~servant inside of-Lord house and_said this rich`

**7**  Lord's servant, the angel, took from this unprofitable servant
`<of>-Lord ~servant grab angel from this unhelpful ~servant`

**8**  this one talent; and the angel took the talent from him
`this one talent and talent grab angel from`

**9**  and gave it to the faithful servant, the servant who has ten talents. Here ends this holy gospel.
`believe ~servant servant talent ten have end this holy-gospel`

> Matthew 25:28-30, Douay: *Take ye away therefore the talent from him, and
> give it to him that hath ten talents... And the unprofitable servant cast ye
> out into the exterior darkness.* The codex has the unprofitable servant, the
> taking away, and the ten talents; the angel doing the taking is its own.

## 175v — the Lord goes from town to town

**1**  This holy gospel begins, written by holy Luke
`begins this holy-gospel write holy-Luke`

**2**  in the sixth chapter of the writing: the time,
`inside six chapter <of>-write time`

**3**  then the Lord Jesus within thirty years;
`then Lord-Jesus inside thirty years*`

**4**  the time the Lord Jesus went among the people, and the Lord's apostles, from town
`time go Lord-Jézus among_the_people* and <of>-Lord apostle from town`

**5**  until town; from temple until temple; from
`until town from temple until temple from`

**6**  village until village; and the Lord's apostles; and went
`village until village and of-Lord apostle and go`

> Luke 8:1, Douay: *And it came to pass afterwards, that he travelled through
> the cities and towns, preaching and evangelizing the kingdom of God; and the
> twelve with him.* K&T's own dictionary carries a sign glossed "from town to
> town", and the codex uses it three times in two lines.

## 176r — the woman of Samaria at the well

**1**  the Lord Jesus, to one well; and the Lord Jesus sat by this
`Lord-Jézus one well and sit Lord-Jézus to-this`

**2**  well, because there was [afraid]; the Lord was wearied; in turn the apostles went,
`well because exist [?] get_tired-Lord in_turn apostle go-apostle`

**3**  into the village for bread; and living; if the body
`inside village on-~bread ~and living ~if body`

**4**  living; and then there came one woman | to
`living and then go one woman = | to`

**5**  this well; and then the woman dipped [at] this well. And then
`this well and then dip-~woman this well and_said`

**6**  the Lord Jesus [was] thirsty, the Lord; and then the woman <subject marker> was; the Lord [asked] water;
`Lord-Jesus thirsty-Lord and then-~woman-+SUBJ exist-Lord water`

**7**  asked. And then this heathen: how he | dare
`~ask and_said this heathen how? he | dare`

**8**  the Lord, to ask water of a pagan? This heathen [woman] in turn: | this
`Lord from pagan water ~ask this heathen in_turn | this`

**9**  Lord is a Jew; she dipped for the Lord [give me] to drink, the Lord, and
`Lord Jew(ish) dip-+the_Lord [?] on-drink Lord and`

> John 4:6-9, Douay: *Now Jacob's well was there. Jesus therefore being wearied
> with his journey, sat thus on the well... There cometh a woman of Samaria, to
> draw water. Jesus saith to her: Give me to drink... Then that Samaritan woman
> saith to him: How dost thou, being a Jew, ask of me to drink, who am a
> Samaritan woman?* The wearying, the sitting, the disciples gone for food, the
> asking and the objection are all here in John's order.

## 176v — the Lord begins to speak to the Gentiles

**1**  he began to speak through the pagan, the Lord Jesus; and the heathen <subject marker> | judged
`begin through talk^ pagan Lord-Jesus and heathen-+SUBJ | ~judge`

**2**  this; had; pagan man; and the heathen began, the Lord, | to say
`this ~have pagan man and heathen begin-Lord | say`

**3**  this: raise, heathen [woman], the place, do; if | do,
`this-raise heathen place^ do ~if | do`

**4**  pagan; divorce of the heathen. And then this heathen | on the
`pagan divorce of-heathen and_said this heathen | on-of`

**5**  heathen, many to which; and from [five husbands]; he, he, descendant
`heathen °many-to which and from [five_husbands] he he descendant`

**6**  husband; to the pleasing of the Lord, the prophet foretold; and the disciples went to the Lord,
`husband^ to-pleasing-Lord prophet predict and go disciple^ to-Lord`

**7**  and the apostles began; the wonder upon the Lord; the Lord's love; the Lord spoke this | woman,
`and begin-apostle wonder^ on-Lord love-Lord speak-Lord this | ~woman`

**8**  one woman, the head; and this heathen [woman] believed in
`one-~woman head and believe this heathen inside`

**9**  the Lord Jesus; and the heathen [woman] went to her own | […] from
`Lord-Jesus and go heathen to-of-heathen | [?]-from`

> John 4:16-19 and 4:28: *Go, call thy husband, and come hither... The woman
> saith to him: Sir, I perceive that thou art a prophet... The woman therefore
> left her waterpot, and went her way into the city.* The prophet and the
> leaving and the going into the town are all here.

## 177r — come, see a man who told me all things

**1**  [the woman] and then went into the village, and the heathen [woman] began to speak | this:
`[the_woman] and then go inside village and begin-heathen say | this`

**2**  this people, sit; one Lord at the well, and even more from the Lord,
`this people sit one Lord to-well even_more from-Lord`

**3**  to the pleasing of the Lord, the prophet foretold through; because the heathen's home
`to-pleasing-Lord prophet through predict because of-heathen home`

**4**  did; the heathen's love did; the heathen divorced;
`do love-heathen do heathen divorce`

**5**  the heathen's every deed [all things]; the heathen <subject marker> said […]; and
`of-heathen every ~do [all_things] heathen-+SUBJ say-[?] and`

**6**  then this people believed in the Lord, the man, the people; and
`then-exist this people inside Lord-somebody believe-people and`

**7**  the people went to this well, because they would pray to the Lord; | then
`go-people this well because-Lord want-people pray | then`

**8**  and the people were there, and the Lord preached one to two years.
`exist and people exist-Lord preach one to-two-year`

> John 4:29, Douay: *Come, and see a man who has told me all things whatsoever
> I have done. Is not he the Christ?* And 4:40: *So when the Samaritans were
> come to him, they desired that he would tarry there. And he abode there two
> days.* The codex's two days have become two years, which is its own
> reckoning, but the tarrying is right.

## 177v — the gospel ends, and another begins

**1**  and even more to the Lord Jesus; but the Lord went into Galilee,
`and even_more-to Lord-Jézus a) to-go-Lord inside Galilee`

**2**  to the town. Here ends this holy gospel. The Lord God, with all thy heart.
`town end this holy-gospel Lord-<divine> ?with_all_thy_heart.`

**3**  This holy gospel begins,
`begins this holy-gospel`

**4**  written by holy Luke, in
`write holy-Luke inside`

## 178r — the ten lepers

**1**  the fifth chapter of the writing: at that time, then, the Lord Jesus, within thirty | one
`five chapter of-write time then Lord-Jesus inside thirty | one`

**2**  years: at that time the Lord Jesus went into Jerusalem; and went to the Lord
`years* time go Lord-Jesus inside Jerusalem and go to Lord`

**3**  and many people; and then the Lord Jesus went, the people, into the field, and
`many people and then-exist go Lord-Jézus people on-+field-+one and`

**4**  left, stood far away, ten leper people; and began the ten
`leave stood far_away ten leper people and begin ten`

**5**  lepers began to cry out: son of David, king, have mercy —
`leper shout-to son David king have_mercy`

**6**  the ten lepers, son; and they cried to the Lord Jesus; go, ten
`ten leper son and shout-to Lord-Jézus go ten`

**7**  lepers, and let the ten shew themselves to the priest; and
`~leper and ten appear priest and`

**8**  the priest took the ten lepers, from all that was [shew yourselves]
`priest grab ten leper from each,_every-~exist [?]`

**9**  the commandment of Moses; and then the ten lepers went | from
`Moses commandment and then go ten leper | from`

> Luke 17:12-14, Douay: *there met him ten men that were lepers, who stood afar
> off; and lifted up their voice, saying: Jesus, master, have mercy on us. Whom
> when he saw, he said: Go, shew yourselves to the priests.* The codex has the
> standing afar off, the crying out, the ten, and the sending to the priest,
> and it adds the law of Moses, which is where the shewing comes from
> (Leviticus 14).

## 178v — the priests dispute over them

**1**  saw the lepers' body; and then were
`see of-leper body and then exist`

**2**  the lepers' body healing; and one Wednesday, ten, how, aforesaid, alone
`leper body healing and one-+Wednesday ten how?-aforesaid-°alone`

**3**  [as they went] [were made clean]; and then the ten lepers went, the ten people, before
`[as_they_went] [were_made_clean] and then ten leper go-ten-people-before`

**4**  the high priest, before the priest. And then
`high_priest = before priest and_said`

**5**  the priests of the Jews: how are you people, ten | lepers?
`priest Jew(ish) how? you people ten | leper`

**6**  Chapter. Said [one of them] the lepers, from the people [went back] the lepers;
`chapter say [?] leper from-people [?] leper.`

**7**  the people were before the priest, among the priests, the Jews, the man;
`people exist priest among priest Jew(ish)-somebody`

**8**  they cast the priest out; the Jews said to the priest;
`out(ward) cast_out priest Jew(ish) say priest.`

**9**  the Jews: who of you men is healed? | said the leper
`Jew(ish) who? you somebody from-healing | say-leper`

> Luke 17:14: *And it came to pass, as they went, they were made clean.* The
> dispute before the priests is not in Luke; the codex has built it out of the
> same materials as the dispute in John 9 over the man born blind, which is the
> kind of borrowing this compiler does throughout.

## 179r — where are the nine?

**1**  the ten people healed: son of David, king; said the chief men,
`ten-people from-healing son David king say head`

**2**  the Jews, the priest [glorifying God]: you people, from the son
`Jew(ish) priest [?] you people from son`

**3**  have sinned; the Lord healed you; but you people were healed
`sin_against from-healing-Lord a) you people-+<subject> from-healing`

**4**  by Moses truly, because there is the word of the Old Testament, from
`Moses righteous(ly) because-exist <OT> word from`

**5**  the lepers, the Jews; among the priests, the Jews, out, cast out,
`leper-Jews among priest Jew out exorcise`

**6**  and then of the nine people a man believed the priests,
`and then-exist from nine people somebody believe from priest`

**7**  the Jews; in turn the tenth man had faith, and returned
`Jew(ish) in_turn ten somebody faith* a) return`

**8**  back to the Lord Jesus; and the leper bowed down
`back against Lord-Jézus and bow_down leper`

**9**  before the Lord's feet; and then the Lord's sister
`before of-Lord foot and then-Lord sister`

> Luke 17:15-16, Douay: *And one of them, when he saw that he was made clean,
> went back, with a loud voice glorifying God. And he fell on his face before
> his feet, giving thanks.* The going back and the falling at the feet are
> here; the nine who did not are counted on line 6.

## 179v — were not ten made clean?

**1**  kissed, the tenth man, the Lord's feet; and the Lord, godfearing,
`kiss-ten-somebody of-Lord foot and Lord godfearing^`

**2**  and thanks took the tenth somebody. And then the Lord Jesus, the apostles | of
`and thanks grab-ten-somebody and_said Lord-Jesus apostle | of`

**3**  the Lord, to all by name: and the people, were there not ten lepers? Which
`Lord name-each,_every-to and people exist ten leper in_turn-+who`

**4**  <subject marker> [were not ten] one somebody, commandment; and somebody, commandment, the Lord loves.
`SUBJ [were_not_ten] one somebody-commandment and somebody-commandment Lord love`

**5**  And then the Lord Jesus, the Lord's apostles: good [the nine] from | you, chapter
`and_said Lord-Jesus apostle of-Lord good [the_nine] from | ~you-chapter`

**6**  [so] the son, the man; there is the Lord; the heathen's love. Here ends
`[so] son somebody exist Lord heathen love end`

**7**  this holy gospel. The Lord God's love. Three things must be believed
`this holy-gospel Lord-<divine> <subject> love three believe have`

**8**  from the world: first <subject marker> believe above, high; and then the pagans, and the Jews
`from world first SUBJ believe above-high and °and_then-pagans and Jew`

**9**  believe within these; believe one somebody
`believe inside these believe one somebody`

> Luke 17:17-18: *Were not ten made clean? And where are the nine? There is no
> one found to return and give glory to God, but this stranger.* The codex's
> "heathen" (printed earlier as "alien nation") is the Samaritan of that verse, and the folio turns from the
> story into doctrine on line 7.

## 180r — one faith, one Church

**1**  and the Jews, the pagans, above high; in turn not saved; and somebody
`and Jew-pagans above-high in_turn not be_saved and somebody`

**2**  not believe, somebody, in the Lord Jesus Christ; one
`not believe somebody inside Lord-Jesus-Christ one`

**3**  somebody not saved, but everybody damned; second <subject marker>
`somebody not be_saved but everybody = be_damned second SUBJ`

**4**  believe the Church; and the Church's belief is good,
`believe <church> and <church> believe this_is good`

**5**  because there is one Church; the Church, and in believing is salvation,
`because one <church> <church> and inside believe be_saved`

**6**  because from the church, the church, one way, belief,
`because from church church one way believe`

**7**  the Church, the Church, in the Lord Jesus Christ, in his coming and in
`<church> <church> inside Lord-Jézus-Christ inside coming* and inside`

**8**  his death; then on the cross the Lord gave up the ghost; thirdly,
`die then-+<subject> cross <of>-Lord soul give_up_the_ghost third`

**9**  believe in the coming of the Lord Christ; and through him escape.
`<subject> believe on-?coming Lord-Christ and through escape`

> Ephesians 4:5 by way of the creed: *One Lord, one faith, one baptism.* K&T
> gloss the sign used four times on this folio as "a Christian or related
> church or denomination", so the page is theirs to the extent that the word
> is; the argument built on it is the codex's own.

## 180v — a summary of the Lord's life

**1**  the Lord Jesus; and the twelve apostles followed the Lord Christ; and many tired,
`Lord-Jesus and follow Lord-Christ six-six apostle and many tire`

**2**  the Lord Christ, who wearied; the Lord did it; he went into the world | of
`Lord-Christ who get_tired-+<subject> do,-Lord into_the_world* go-Lord | <of>`

**3**  the Lord, the apostles; and many a miracle the Lord Christ, in love, did | upon
`Lord apostle and many miracle Lord-Christ love miracle-+<subject> do, | on`

**4**  the world; the Lord's apostles went; the blind of eye he gave light; the dead man
`world go <of>-Lord apostle eye-blind <subject> through light Lord die somebody`

**5**  he stood up and raised; the evil upon the people, before, to who, the Lord | love, and
`SUBJ stand_up resurrect-chapter-Lord evil SUBJ on-people ~before-to-+who-Lord | love-and`

**6**  these ill the Lord healed; and the holy Host, God's body,
`these ill heal-Lord and holy-+host God body`

**7**  the Lord Christ; if the Lord at thirty stayed, the Lord, within the host;
`Lord-Christ ~if Lord on-thirty stay-Lord inside host`

**8**  and the Lord Christ was humble, because the Lord was humble in this world.
`and humble Lord-Christ because-+the_Lord exist-Lord humble-Lord this world.`

**9**  The chief men took the Lord, and the Jews captured him [led away]
`head grab-Lord and Jew(ish) <subject> capture [?]`

## 181r — Thomas was not with them

**1**  [they platted] and a crown of thorns upon his head | conceived,
`[they_platted] and thorn crown on-head | conceive`

**2**  the Jews; and [trodden down]; died the Lord Christ, and rose the Lord Christ, and appeared
`Jews and [trodden_down] die Lord-Christ and rise Lord-Christ and appear`

**3**  to the Lord's apostles, one Saturday evening; and this
`Lord-Christ apostle <of>-Lord one Saturday evening and this`

**4**  evening it was; then the Lord appeared, the Lord, [to] the twelve disciples
`evening exist then-Lord appear-Lord six-six disciple^`

**5**  in the Lord's house, where the Lord God, the Lord Jesus, had made the supper; and | then
`inside Lord house where Lord-<divine> Lord-Jézus dinner-to do, and | then`

**6**  holy Thomas came Didymus one Saturday evening
`exist go holy-Thomas [?] one Saturday evening`

**7**  to the apostles; and the apostles said: Thomas, the apostles have seen the Lord. And holy Thomas said,
`to-apostle and say apostle Thomas apostle see Lord and say holy-Thomas`

**8**  this Thomas: this not believe, all this; then | this
`this-Thomas this not believe every this then | this`

**9**  Thomas: this believe, if [unless] Thomas sees
`Thomas this believe if [unless] see-Thomas`

> John 20:24-25, Douay: *Now Thomas, one of the twelve, was not with them when
> Jesus came. The other disciples therefore said to him: We have seen the Lord.
> But he said to them: Except I shall see in his hands the print of the nails,
> and put my finger into the place of the nails, and put my hand into his side,
> I will not believe.*

## 181v — blessed are they that have not seen

**1**  the Lord's side, and unless Thomas puts his finger into the Lord's
`of-Lord side^ and of-Thomas finger not put within^ of-Lord`

**2**  side, who from the Lord, from death, stood up. At that time the Lord Jesus Christ stood
`side^ who from Lord from die stand_up time stand^ Lord-Jesus-Christ`

**3**  into the midst of the apostles, the doors being shut, and said: peace be to you;
`middle apostle closed and say commandment you exist`

**4**  and the judgment year; the apostles; in turn Thomas began to have, and said | the Lord
`and judge-year apostle in_turn Thomas begin have and say | Lord`

**5**  Jesus: Thomas, come by name [hither] put thy finger
`Jézus Thomas go-+name [?] put <of>-Thomas finger`

**6**  into the Lord's wound [blessed] see and believe; and [have not]
`inside <of>-Lord wound [?] see believe and [?]`

**7**  the Lord Jesus, the Lord's wound; and said the Lord Jesus: Thomas, happy
`Lord-Jesus of-Lord wound and say Lord-Jesus Thomas happy`

**8**  from; and somebody sees and believes; but and | blessed
`from and somebody see and ~believe but and | blessed`

**9**  year to; and not see, but believe. Here ends this holy gospel.
`~year-to and not see but believe here_ends this holy_gospel`

> John 20:26-29, Douay: *the doors being shut, and stood in the midst, and
> said: Peace be to you... Put in thy finger hither, and see my hands... and be
> not faithless, but believing... Blessed are they that have not seen, and have
> believed.* The shut doors, the midst, the peace, the finger and the blessing
> are all here in John's order.

## 182r — the appearance at table, and the sending out

**1**  The Lord God, with all thy heart. And this [upbraided] the man said, the Lord Jesus [hardness of heart]
`Lord-<divine> ?with_all_thy_heart and this [?] somebody say Lord-Jézus [?]`

**2**  somebody, the Lord, not within, year […] somebody; and then
`somebody Lord not inside-~year-[?] somebody and then`

**3**  after the Lord Christ was executed, in the […] year,
`on-execute Lord-Christ [?]-year inside`

**4**  the time the apostles sat at table in Jerusalem, in the Lord's house, | at
`time sit apostle to-table inside Jerusalem inside Lord house | to`

**5**  the place where the Lord God, the Lord Jesus, had made the supper; the time
`where* Lord-<divine> Lord-Jézus dinner do, time`

**6**  the Lord Jesus appeared [to] the Lord's apostles within the body, somebody;
`appear Lord-Jesus apostle of-Lord inside body somebody`

**7**  and he sat with the apostles, outside, and began to upbraid them | for
`and sit to-apostle to-+out and begin admonish | on`

**8**  their belief; and the Lord Jesus said: go, apostles, | into
`believe and say Lord-Jézus you go-apostle | on`

**9**  the world; and is one woman baptized in the Lord's, is […]
`world and exist one-~woman baptize inside of-Lord exist-[?]`

> Mark 16:14, Douay: *At length he appeared to the eleven as they were at
> table: and he upbraided them with their incredulity.* This is the verse that
> proved the Douay was the right corpus to work from: the sign here read as
> *at table* was fixed years-worth of occurrences ago from Kiraly and Tokai's
> own citations at 072r08, 072r11 and 191r04, while a King James pool was
> still offering *at meat* for this verse. The upbraiding is on line 7.

## 182v — baptize them in the name of the Father

**1**  and somebody is one woman baptized in the name of God the Father
`and somebody exist one-~woman baptize inside name God_the_Father`

**2**  and of the Son and of the Holy Spirit; and let him be to the Lord | to
`and son and holy-spirit and exist Lord-to | to`

**3**  believe; every such man is saved, and one
`believe* each,_every somebody be_saved and one`

**4**  is damned [but] [but]; and somebody not one woman baptized
`be_damned [but] [-but] and somebody not one-~woman baptize`

**5**  and not to the Lord; one saved, but
`and not Lord-to one be_saved but`

**6**  every man is damned. Here ends this holy gospel. The Lord God's
`each,_every somebody be_damned end this holy-gospel Lord-<divine> <subject>`

**7**  love. Written by holy Luke in the second
`love write holy-Luke inside two`

**8**  chapter of the writing: the time,
`chapter <of>-write time`

**9**  then, after the execution
`then-exist on-execute`

> Matthew 28:19 and Mark 16:16, Douay: *Going therefore, teach ye all nations;
> baptizing them in the name of the Father, and of the Son, and of the Holy
> Ghost... He that believeth and is baptized, shall be saved: but he that
> believeth not shall be condemned.* Both halves, in order.

## 183r — Chosroes carries off the Cross

**1**  the Lord Christ, twenty-six years; at that time occupied Jerusalem.
`Lord-~Christ two-ten-ten six-~year time occupy Jerusalem.`

**2**  One heathen emperor, name
`one heathen ~emperor name`

**3**  was Chosroes; and then he seized upon Jerusalem,
`exist Khosrow_(Chosroes)_<Sasanian_king> and then-exist grab on-Jerusalem`

**4**  the tree of the Cross — the tree upon which Christ
`cross tree ~on tree exist Christ`

**5**  executed; and the tree <subject marker> took away into
`execute and tree SUBJ take_away inside`

**6**  the town of Ctesiphon, into one tower;
`Ctesiphon_<city_in_Persia> town inside one tower`

**7**  and then there was war many years upon the Roman
`and then-exist exist many year war* on-Roman.`

**8**  emperor, whose name was Heraclius;
`emperor name exist Heraclius_<Byzantine_emperor>`

**9**  and then war went [between] this heathen emperor
`and then war* go this heathen emperor`

> The Exaltation of the Cross, as the Golden Legend tells it: Chosroes II of
> Persia takes Jerusalem in 614 and carries off the relic of the True Cross;
> the emperor Heraclius wars on him and brings it back in 628. Kiraly and
> Tokai's own dictionary carries glosses for **Chosroes**, **Ctesiphon** and
> **Heraclius**, so the identification of these folios is theirs. This is the
> strongest non-biblical anchor in the book.

## 183v — the sign given to Heraclius

**1**  This Roman emperor then had two wars
`this Roman emperor then-exist have two war*`

**2**  on fighting against each other; and then.
`on-fight against_each_other and then.`

**3**  Heraclius the emperor had a small army;
`little an_army have Heraclius_<Byzantine_emperor> emperor`

**4**  and then asked, on prayer, can | from, to
`and then ask on-~pray can | from-to`

**5**  the Lord, thanks; the Lord God heard, the Lord God, the emperor's
`Lord thanks Lord_God hear Lord_God of-~emperor.`

**6**  prayer; and God's angel cried out upon the water;
`as* and shout-to God angel on-water`

**7**  Heraclius had it; the Lord God heard Heraclius's
`have Heraclius_<Byzantine_emperor> hear Lord-<divine> <of>-Heraclius_<Byzantine_emperor>`

**8**  prayer. And then God's angel [to] Heraclius, daughter,
`pray and_said God angel Heraclius daughter`

**9**  had him write upon his armour the tree of the Cross, and
`have write on-<armor> cross tree and`

> The Constantine motif -- *in hoc signo vinces* -- transferred to Heraclius:
> the sign of the Cross put on the armour before the battle. K&T gloss the
> sign on line 9 as a kind of armour or weapon.

## 184r — the battle, and the tower at Ctesiphon

**1**  the emperor won the fight, because the heathen lost,
`win emperor on-fight because lose heathen`

**2**  the emperor; and then the two left, this heathen emperor
`emperor and then two leave this heathen emperor`

**3**  [and] this Roman emperor; and then the two fought | on, chapter, one
`this Roman emperor and then-two fight | on-chapter-+one`

**4**  within, to the Lord, the two; and the heathen people [fought] the people among [one another]
`inside-to-Lord-two ~and heathen people [fought] people among [one_another]`

**5**  died; in turn the Jews, the people; and the heathen <subject marker> to many [the bridge]; and
`die in_turn Jew people and heathen SUBJ to-many [the_bridge] and`

**6**  then the heathen people died; and began to pierce [overcame]
`then people heathen die and begin pierce [overcame]`

**7**  [baptized] on the heathen earth; and then went Heraclius
`[baptized] on-heathen earth and then go Heraclius`

**8**  into Ctesiphon town, to the place, to this heathen
`inside Ctesiphon town on-place to-this heathen`

**9**  emperor Chosroes, because the emperor dwelt within one
`emperor Chosroes because dwell emperor inside one`

> The Golden Legend has Heraclius and Chosroes' son fight in single combat on
> a bridge over the Danube. The codex has the two leaving the armies and
> fighting, which is the same story.

## 184v — the tower of gold and precious stones

**1**  tower; and the tower was all of gold, and built of precious stone, the tower,
`tower and tower exist each,_every golden and precious_stone stone build tower`

**2**  how? one God; the emperor sat within, because [he] was put
`how? one God sit_inside emperor because exist put`

**3**  the emperor, on one way, a cock; and the cock was all
`emperor on-one way cock and cock exist every`

**4**  golden, pouring; the second way the emperor put the cross tree
`golden pour second way put emperor cross tree`

**5**  as [it] was on the golden; and then the emperor [of silver]
`as exist on-golden and then emperor [of_silver]`

**6**  the water ascended up on the tower; and lo, the rain took,
`water ascend up on-tower and lo rain grab`

**7**  the emperor, then <subject marker> wanted the emperor to take,
`emperor then-+SUBJ want emperor grab`

**8**  and then the emperor made it within the tower,
`and then-exist emperor do, inside tower.`

**9**  the year […] and to […] and [precious stones] and among the tree of the Cross
`~year-[?] and to-[?] and [precious_stones] and among cross tree`

> The Golden Legend: Chosroes *had made himself a tower of gold and silver,
> shining with gems, and had set therein images of the sun and moon and
> stars... and he caused water to be conveyed by hidden pipes, that he might
> as God make rain.* The gold, the precious stones, the sitting within, and
> the rain are all here, which fixes the source beyond argument.

## 185r — Chosroes sits between the cross and the cock

**1**  of gold, among the cross, among the cock, the emperor sat,
`golden among cross among cock sit emperor`

**2**  as though one [a cock] from [the other side] the emperor,
`how? one [?] from [?] emperor`

**3**  to God prayed, the Jews, from, because is every world [worshipped as God]
`to-God ~pray-Jews from because-exist every world [worshipped_as_God]`

**4**  and then Heraclius the emperor went [to] this heathen
`and then Heraclius emperor go this heathen`

**5**  emperor within the tower. And then Heraclius the emperor
`emperor inside tower and_said Heraclius emperor`

**6**  believed, Heraclius's God, in turn, the whole wide world; this
`believe <of>-Heraclius_<Byzantine_emperor> God in_turn the_whole_wide_world this`

**7**  Heraclius, the head; die, he said, this | there was
`Heraclius ~head die say this | ~exist`

**8**  the emperor [slew]; and they beheaded the emperor, and
`emperor [slew] and emperor behead and`

**9**  then Heraclius the emperor did all
`then-exist do, Heraclius_<Byzantine_emperor> emperor each,_every`

> The Golden Legend: Chosroes set the wood of the Cross on one side of his
> throne and a cock on the other, and would be worshipped as the Father. The
> cross and the cock are both on line 1.

## 185v — the Cross comes back to Jerusalem

**1**  [from the] the tower he pierced; and the tower, God, he took up,
`[?] tower on-+pierce ~and tower God up grab`

**2**  and [of Chosroes] [emperor] the son | from
`~and [of_Chosroes] [emperor] son | from`

**3**  one woman; and the son the emperor left [behind] and
`one-woman and son emperor leave [?] and`

**4**  took the cross tree, and <subject marker> took away into
`grab cross tree and SUBJ take_away inside`

**5**  the town of Jerusalem; and then [came] before | the army,
`Jerusalem town and then [came] before | army`

**6**  the army; and then arrived Jerusalem; and at the gate God's
`army and then-exist [?] Jerusalem and to-gate God`

**7**  angel, gate, Jerusalem; and the angel shouted to Heraclius:
`angel gate Jerusalem ~and shout-to angel Heraclius`

**8**  thus the Lord Christ did not carry the tree of the Cross out to Jerusalem in pride,
`this-this Lord-Christ proud out(ward) on-Jerusalem carry cross tree`

**9**  but carried it in humility; and then he sat down [upon an ass]
`but humble carry and then-exist sit down [?]`

> The Golden Legend again: Heraclius, riding in triumph with the Cross,
> finds the gate of Jerusalem shut by an angel, who tells him the King of
> heaven passed that way in humility. The gate, the angel and the rebuke are
> all here.

## 186r — the emperor takes off his robes

**1**  and took off from the emperor his clothes; and then
`and take_off on-+emperor <of> clothes and_then*`

**2**  [put off his shoes] and with bowed head carried the tree of the Cross into
`[?] and bowed head carry cross tree inside`

**3**  Jerusalem; and then God's angel opened the gate of Jerusalem;
`Jerusalem and then open God angel gate Jerusalem`

**4**  and the emperor, many [his purple], […] love, the Jews, the cross
`and emperor many [his_purple] [?]-love-Jews cross`

**5**  Cross; and the emperor put the cross within Jerusalem,
`tree and cross <subject> put emperor inside Jerusalem`

**6**  in the temple; and the emperor prayed, to the Lord thanks, the Lord God,
`temple and ~pray-~emperor to-Lord thanks Lord_God`

**7**  the whole wide world; and there is a man who takes the holy tree of the Cross,
`each,_every the_whole_wide_world world* and exist somebody to grab holy-cross`

**8**  the tree; and [set up the] the tree of the Cross;
`tree and [?] cross tree`

**9**  and the cross tree, a feast, through the commandment, on all
`and cross tree feast through commandment on-every`

> The legend ends as it always does: the emperor puts off his purple and his
> shoes, carries the Cross barefoot, and the gate opens. This is the feast of
> the Exaltation of the Cross, 14 September, and its place here -- between the
> gospels and the Old Testament readings that follow -- is where a missal or
> a breviary would put it.

## 186v — the holy Cross against the evil

**1**  the whole world; because this holy cross tree, this cross, <subject marker> our
`all_the_world world because this holy-cross tree this cross SUBJ our`

**2**  [healed], and our [miracles]; and this holy cross tree, this
`[healed] and our [miracles] and this holy-cross tree this`

**3**  <subject marker> our [witness] against [these things]; and believe:
`SUBJ our [witness] against [these_things] and believe`

**4**  the devil, the Lord God, that is, against the devil.
`devil = Lord_God that_is against devil =`

**5**  On the Sunday
`inside Sunday`

**6**  the Lord God created
`create Lord-<divine>`

**7**  from the world
`from world`

**8**  and
`and`

## 187r — the Red Sea

**1**  the angel, within heaven; after these the Lord God, within Sunday,
`angel inside heaven = after_these Lord_God inside Sunday`

**2**  led them through, through dry the Red Sea, by Moses
`through go-Lord through [?] the_Red_Sea on-+Moses`

**3**  and by Aaron, the Jewish people, from the land of Egypt,
`and on-Aaron Jew(ish) people on-Egypt earth`

**4**  from Pharaoh king's earth; and then Moses
`on-Pharaoh king earth and then-exist Moses`

**5**  and Aaron went to the Red Sea. And then
`and Aaron to-+the_Red_Sea go and_said`

**6**  glorified, the angel: Moses, hold out this rod over the Red Sea;
`be_glorified^ angel Moses hold_out this stick on-+the_Red_Sea`

**7**  and then he held it out over the Red Sea; and then | the Red Sea,
`and then-exist hold_out on-+the_Red_Sea and then-exist | the_Red_Sea`

**8**  in the Lord's name, apart left, on two ways; and then through went the people,
`Lord-+name apart leave on-two way and then through go people`

**9**  the Jews, Moses, Aaron, the angel, through the Red Sea.
`Jews Moses Aaron angel through the_Red_Sea`

> Exodus 14:16 and 14:21-22, Douay: *lift up thy rod, and stretch forth thy
> hand over the sea, and divide it: that the children of Israel may go through
> the midst of the sea on dry ground... And the children of Israel went in
> through the midst of the sea dried up.* Kiraly and Tokai's dictionary
> carries the Red Sea as a sign of its own, and it is on this folio five
> times.

## 187v — Pharaoh in the midst of the sea

**1**  The time Pharaoh the king went into the Red Sea, the king,
`time Pharaoh king inside the_Red_Sea go-king`

**2**  Pharaoh's army; and then the king went | into
`<of>-Pharaoh an_army and then-exist go-king | on`

**3**  the middle of the Red Sea; the time God's angel said: Moses, hold out
`half the_Red_Sea time say God angel Moses hold_out`

**4**  this rod over the Red Sea; and then he held it out; the time
`this stick on-+the_Red_Sea and then-exist hold_out time`

**5**  the Red Sea closed in upon Pharaoh the king; and then went
`the_Red_Sea close_in Pharaoh king and then-exist to-go`

**6**  Moses and Aaron [stretched out]; after these the Lord God,
`Moses and Aaron [stretched_out] after_these Lord_God`

**7**  on the Sunday [stretched out] from the people, who was the Lord's, going | upon
`inside Sunday [stretched_out] from people who exist-Lord on-go-Lord | on`

**8**  [from heaven] the earth; the Lord God took the heavenly manna
`[?] earth grab Lord-<divine> heavenly manna`

**9**  from heaven, land; and this manna, this <subject marker> bread
`from_heaven* land and this manna this SUBJ bread`

> Exodus 14:27-28 and then Exodus 16:15. The manna on line 8 runs straight
> into the daily bread of the Our Father on the next folio, which is the
> standard typological pairing and is why the two stand together here.

## 188r — the manna and the bread of this day

**1**  the angel; and this living bread, the people, the Jews | forty
`angel and this bread living people-Jews | forty`

**2**  years; and how? at table the Jews ate; on the Jews, from eating, <subject marker> left;
`year and how? table-Jews eat on-Jews from eat SUBJ leave`

**3**  and then this manna take a bucket; and
`and then-exist this manna [?] bucket and`

**4**  the Jews [his purple] brought [a vessel] from the manna, glory
`Jews [his_purple] brought* [a_vessel] from manna glory^`

**5**  and godfearing did, the Jews; in turn [came] Christ, stayed, daily
`and godfearing^ do-Jews in_turn [came] Christ stay daily`

**6**  [put into it] manna; and then the Lord Jesus within thirty [and a] half
`[put_into_it] manna and then Lord-Jesus inside thirty half*`

**7**  three [years]; the time the Lord Jesus said, at the last supper, he took
`three time say Lord-Jézus on-last dinner-to grab`

**8**  within [his] hands one baked cake, and
`inside hands one baked cake and`

**9**  said the Lord Jesus: and the man [who does] not this bread eat; and the Lord
`say Lord-Jesus and man^ not this bread eat and Lord`

> Exodus 16 read into the Last Supper. The manna, the bucket in which it was
> kept (Exodus 16:33), and then the bread of the supper. K&T gloss the sign
> on line 8 as a baked cake, in their own quotation marks.

## 188v — he that believeth not

**1**  believeth not: every such man is damned […]; and a man who is the Lord's
`not_believe each,_every somebody be_damned cut_off-[?] and somebody exist Lord`

**2**  believes; and there is a man who from the altar
`believe and exist somebody from altar(table) exist`

**3**  from the thirty, eats the holy host and drinks; he that believeth not,
`from thirty holy-host eat and drink who_believes_not*`

**4**  the man is living, for ever and ever, amen.
`man^ exist living for_ever_and_ever = amen`

**5**  On the Sunday from [the flesh of] Christ came into this world;
`to Sunday from [?] Christ on-this world coming*`

**6**  and before the Lord Christ's coming, nine months and two Sundays; on the
`and before Lord-Christ coming* nine moon and two Sunday inside`

**7**  Sunday the Lord was announced by the angel Gabriel; within | not
`Sunday the_Lord exist announce by_Gabriel angel inside | not`

**8**  Sunday, within the body of the happy Virgin Mary, and | [the holy Trinity]
`~Sunday inside body happy Virgin_Mary and | [the_holy_Trinity]`

**9**  [holy] Joseph; on the Sunday the Lord was
`[?] Joseph inside Sunday the_Lord exist`

> John 6:53-54 and the Annunciation. From here to 190v the codex keeps a
> concordance of Sundays: what the Lord did on each one. That is the shape of
> a preacher's handbook, not of a gospel.

## 189r — what was done on the Sundays

**1**  announced, this angel, by the angel Gabriel; and then the Lord | on
`announce this angel by_Gabriel angel and then-Lord | on`

**2**  this world was born; and then the Lord within [his] thirty-first year
`this world ~be_born and then-Lord inside thirty one-~year`

**3**  the time, on a Sunday, the Lord Jesus Christ made at the wedding
`time inside Sunday create on-wedding Lord-Jézus-Christ`

**4**  water into wine; on a Sunday the Lord stood up and raised | the Lord
`water wine inside Sunday the_Lord stand_up resurrect | Lord`

**5**  Jesus Christ [raised] the daughter of the first head in Jerusalem, within Sunday
`Jesus-Christ daughter first^ head inside Jerusalem inside Sunday`

**6**  the Lord […] upon Carmel, to the mount, and
`the_Lord from-[?]-[?] on-Carmel to-mount and`

**7**  appeared the Holy Spirit within the form of a dove. And then
`appear holy-spirit inside ~form dove and_said`

**8**  he, of the son, he who the spirit grew calm, and
`he of son he_who spirit grow_calm and`

**9**  the Lord took the Holy Spirit; and the Lord went into the field
`Lord grab holy-spirit and Lord go inside field`

> Cana (John 2:1-11), Jairus's daughter, and the baptism at the Jordan with
> the Spirit descending as a dove (Matthew 3:16). K&T's own dictionary carries
> Carmel as "a hill where John the Baptist baptizes", which is the codex's
> own geography and not any gospel's.

## 189v — Nain, the blind man, the cleansing of the temple

**1**  the Lord Jesus fasted forty days; within Sunday the Lord
`fast Lord-Jesus forty_days inside Sunday the_Lord`

**2**  stood up and raised, the Lord Jesus Christ, in the town of Nain, the son
`stand_up resurrect Lord-Jézus-Christ inside Nain town son`

**3**  one virgin […] woman; and before, that is, as | was
`one virgin-[?] woman and before that_is as | exist`

**4**  the Lord; this virgin […] woman's son stood up, the Lord resurrected; one
`Lord this virgin-[?] woman son stand_up resurrect-Lord one`

**5**  blind man he gave light; on a Sunday the Lord Jesus Christ by the wayside
`~blind through light inside Sunday Lord-Jézus-Christ [?]`

**6**  Jericho town; then, and the Lord went into Jerusalem, and
`Jericho town then and go-Lord inside Jerusalem and`

**7**  the Lord's apostles; on a Sunday the Lord cast out, in Jerusalem,
`<of>-Lord apostle inside Sunday the_Lord cast_out-Lord inside Jerusalem`

**8**  on one somebody, hell, evil; then the Lord,
`on-one somebody hell evil then-Lord`

**9**  in his thirty-third year, on a Sunday the Lord | broke
`inside thirty half three inside Sunday the_Lord | break`

## 190r — the week of the Passion, day by day

**1**  the Lord, five baked bread, five thousand people;
`Lord five baked bread five_thousand people`

**2**  then the Lord within thirty-three and a half [years], from Galilee
`then-Lord inside thirty half three from Galilee`

**3**  through the Red Sea to one mount; on a Sunday
`through the_Red_Sea to-one to-mount inside Sunday`

**4**  the Lord was going, the Lord, to suffer within Jerusalem; then the Lord within thirty
`the_Lord exist go-Lord on-suffer inside Jerusalem then-Lord inside thirty`

**5**  [and a] half, three [years]; on the Monday the Lord preached many a miracle; in turn on the
`half three inside Monday the_Lord many miracle preach-Lord in_turn`

**6**  Tuesday the Lord stood up and raised Lazarus from the tomb; in turn on the Wednesday
`Tuesday the_Lord Lazarus on-burial_chamber stand_up resurrect-Lord in_turn Wednesday`

**7**  the Lord, but <subject marker> was Judas, sold for thirty silver [pieces];
`Lord-~but-+SUBJ exist Judas sell to-thirty silver`

**8**  in turn Thursday, the dinner, the Lord did; and captured the Lord; in turn
`in_turn Thursday dinner-to do-Lord and capture-Lord in_turn`

**9**  Friday the cross […]; and the evil one was bound; in turn on the Saturday, hell
`Friday cross-[?] and evil bound_up in_turn inside Saturday hell`

> The whole Holy Week in nine lines: Palm Sunday, the preaching on Monday,
> Lazarus on Tuesday, Judas and the thirty pieces on Wednesday, the supper and
> the arrest on Thursday, the cross on Friday, the harrowing of hell on
> Saturday. The five loaves and five thousand are on line 1 and the
> Transfiguration on the mount on line 3.

## 190v — the five appearances, and Emmaus

**1**  the Lord destroyed; on the Sunday the Lord rose from the dead; and to the apostles the Lord
`<subject> destroy-Lord inside Sunday the_Lord rise on-die and apostle the_Lord`

**2**  appeared. First the Lord appeared in Bethany | to the virgin
`appear-Lord first the_Lord appear inside Bethany | virgin`

**3**  Mary; second, the Lord appeared at the tomb [to] Mary Magdalene; third
`Mary second the_Lord appear to-tomb Mary Magdalene third`

**4**  the Lord appeared on the way […] the people
`the_Lord appear on-way [?]-[?] people`

**5**  at Jerusalem; fourth, the Lord appeared [to] two apostles; then the two
`on-Jerusalem second-two the_Lord appear two apostle then two`

**6**  apostles, and went, within Sunday, at Jerusalem, into one town; and
`apostle and go inside Sunday on-Jerusalem inside one town and`

**7**  the name of the town was Emmaus; in turn the apostles | and is, chapter,
`~brother-+name town exist Emmaus in_turn apostle | and-exist-chapter`

**8**  by name of the year were Luke and Cleopas; and was I one
`~year-+name exist Luke and Cleopas and ~exist-I one`

**9**  apostle; bread and grape and water; blessed the Lord Jesus;
`apostle bread and grape and water bless Lord-Jesus`

**10**  on the Sunday the Lord appeared a fifth time, in Jerusalem, to the ten apostles | of
`inside Sunday the_Lord five appear inside Jerusalem ten apostle | <of>`

> Luke 24:13-18, Douay: *two of them went, the same day, to a town which was
> sixty furlongs from Jerusalem, named Emmaus... And one of them, whose name
> was Cleophas, answered.* Kiraly and Tokai's dictionary carries both Emmaus
> and Cleopas. Luke names only Cleopas; the codex names the second traveller
> as Luke himself, which is the old tradition and not the gospel.

## 191r — the Ascension, and the two men in white

**1**  the Lord, the gate; and then, after the Lord Christ's execution, in the eighth year, the time
`Lord gate and then on-execute Lord-Christ six-two-year time`

**2**  the Lord Jesus appeared, on a Sunday, in Jerusalem, to the Lord's twelve apostles,
`appear Lord-Jézus inside Sunday inside Jerusalem six-six apostle <of>-Lord`

**3**  to the whole wide world, and to Thomas; and then, after the Lord Christ's execution, | in the twentieth
`to-the_whole_wide_world Thomas and then-exist on-execute Lord-Christ | one-ten-+one-ten`

**4**  […] year, the time the apostles sat at table in Jerusalem, in the Lord's house
`[?]-year time sit apostle at_table inside Jerusalem inside Lord house`

**5**  where the Lord God, the Lord Jesus, made the supper; the time there appeared
`where Lord-<divine> Lord-Jézus dinner do, time appear`

**6**  two, from the putting to death of the Lord Christ until | […] […]
`two-?from execute Lord-Christ until | [?]-[?]`

**7**  year; and to leave to the Lord's Father, from heaven, town, chapter, in turn;
`year and to-leave to-of-Lord the_Father from_heaven* town-chapter-in_turn`

**8**  and there appeared two angels in white clothes,
`and two appear two angel-angel white clothes`

**9**  And then the two angels, angel [and] angel: you [of] Galilee,
`and_said two angel-angel you Galilee`

> Acts 1:9-10, Douay: *he was raised up: and a cloud received him out of their
> sight... behold two men stood by them in white garments.* The white
> garments are here and the sign for the clothes was read from this very
> line.

## 191v — why stand you looking up to heaven?

**1**  men, how? the Lord's joy see [so shall he come]; left on heaven | town
`man how? Lord joy see [so_shall_he_come] leave on-heaven | town`

**2**  before this joy wants the Lord [shall come] on the year of judgment, to judge the living
`before this joy want-Lord [shall_come] on-+judge-year judge the_living`

**3**  and the dead; this word <subject marker> from the Lord, the living Lord; and on this world | went away
`and dead this word SUBJ from Lord living-Lord and on-this world | go_away`

**4**  went into heaven, in turn […] the Lord, with all thy heart, the Lord God, with all thy heart, pleasing and thanks.
`Lord on-heaven in_turn-[?] Lord ?with_all_thy_heart Lord-<divine> ?with_all_thy_heart pleasing and thanks`

**5**  This holy gospel begins,
`begins this holy-gospel`

**6**  written by holy Luke
`write holy-Luke`

**7**  in the second chapter of the writing:
`inside two chapter <of>-write`

**8**  the time, because the time
`time because time`

**9**  the Virgin Mary, on the birth
`Virgin_Mary on-~be_born`

**10**  of the Lord Jesus | […]
`Lord-Jézus | [?]-[?]`

> Acts 1:11: *Ye men of Galilee, why stand you looking up to heaven? This
> Jesus who is taken up from you into heaven, shall so come, as you have seen
> him going into heaven.* The creed's "to judge the living and the dead" is
> on line 2.

## 192r — Simeon in the temple

**1**  year; at that time the wife, the Virgin Mary, carried within [her] bosom into the temple
`year time carry wife Virgin_Mary inside bosom in temple`

**2**  the Lord Jesus; because not this girl [to] destroy, truly the Lord; but wanted the girl
`Lord-Jesus because not this-girl destroy righteous Lord ~but want-girl`

**3**  out [by the Spirit] the salvation of the Jews; and then the girl went to this temple;
`out(ward) [?] from-salvation Jew(ish) and then-exist girl go this temple`

**4**  the time Simeon went into the temple, by the Holy Spirit, in mercy,
`time go Simeon inside temple on-holy-spirit have_mercy`

**5**  and came the Virgin Mary. And then Simeon, the Virgin Mary,
`and come Virgin_Mary and_said Simeon Virgin_Mary`

**6**  Simeon took this son, more than these, this son, Simeon;
`grab-Simeon this son more_than_these* this son Simeon`

**7**  [into his arms] carried the son within Simeon's hands; and knelt
`[into_his_arms] son carry inside of-Simeon hands and kneel`

**8**  before the Lord Jesus, and asked the Lord for mercy;
`Simeon before Lord-Jézus and Lord have_mercy ~ask_(for)`

**9**  And then Simeon: Lord, dismiss the Lord's servant in peace <subject marker>
`and_said Simeon Lord dismiss^ servant of-Lord peace SUBJ`

> Luke 2:27-29, Douay: *And he came by the Spirit into the temple. And when
> his parents brought in the child Jesus... he also took him into his arms,
> and blessed God, and said: Now thou dost dismiss thy servant, O Lord,
> according to thy word in peace.* The Spirit, the taking into the arms and
> the Nunc dimittis are all here in order.

## 192v — mine eyes have seen thy salvation

**1**  Simeon, because see two, Simeon's eyes, saved | of
`Simeon because see two of-Simeon eyes be_saved | of`

**2**  Simeon; and holy Simeon blessed the Lord Jesus; and Simeon's
`Simeon and bless Lord-Jézus holy-Simeon and sin`

**3**  Simeon the Lord had mercy; and the Lord took [him] within [his] bosom
`Simeon have_mercy-Lord and Lord take^ inside bosom`

**4**  and the Lord carried him into the temple at Jerusalem; and then into the temple
`and Lord carry inside Jerusalem temple and then-exist inside temple`

**5**  went the Lord, Simeon and Mary; and Simeon raised the Lord Jesus
`go-Lord-Simeon-Mary and raise Simeon Lord-Jézus`

**6**  within Simeon's hands. And then Simeon: lo, from
`inside of-Simeon hands and_said Simeon ~lo from`

**7**  the Lamb; and the Lord went upon heaven and earth,
`lamb and the_Lord go-Lord on-heaven land`

**8**  on this world the Lord Jesus Christ; and from the Lord, on the cross […]; and on the Lord is
`on-this world Lord-Jesus-Christ and from Lord on_the_cross-[?] and on-Lord exist`

**9**  blessing, all the whole world; and blessing is; left ever
`bless every ~all_the_world world and bless exist leave^ ever`

> Luke 2:30: *Because my eyes have seen thy salvation.* The Lamb on line 6 is
> John 1:29, folded in -- the codex does this constantly, and it is why its
> gospel readings so rarely match one book cleanly.

## 193r — Simeon carries the news to the fathers in hell

**1**  ever, amen. Here ends this holy gospel. The Lord God <subject marker> love this.
`ever amen here_ends this holy_gospel Lord_God SUBJ love this EOL`

**2**  out [of] Moses, truly, within one chapter, who is written, written:
`out Moses righteous inside one chapter who exist write write EOL`

**3**  holy Simeon, three days on this world, Simeon went away, said: Christ, the apostles
`holy-Simeon three_days on-this world go_away-Simeon say Christ apostle EOL`

**4**  of the Lord announce; <subject marker> Simeon within the netherworld, the holy fathers, | on
`of-Lord announce SUBJ Simeon inside netherworld holy-the_father | on-+EOL`

**5**  the coming of the Lord: and see, you are saved, and many
`coming* <of>-Lord and see be_saved you and many`

**6**  judge <subject marker> are within the netherworld, from the forefathers and the holy prophets.
`judge-+SUBJ exist inside netherworld from forefather and prophet-holy. EOL`

**7**  Written; and from the holy gospel, that is, […] down, the Lord; I, the holy gospel:
`write and from holy-gospel that_is [?]-°down Lord I holy-gospel EOL`

**8**  I [the] grape on the water created; I [gave] the blind light through;
`I grape on-water create I blind through light EOL`

**9**  I cast the evil out of the people; I [raised] the dead,
`I evil on-people exorcise I dead EOL`

**10**  rise, resurrect; various lepers the Lord healed; I, the cross, the holy gospel.
`rise* ~resurrect various leper heal-Lord I cross holy-gospel`

> The Gospel of Nicodemus again: Simeon dies, goes down to the fathers in
> limbo, and tells them Christ is coming. It is the same source as the
> harrowing pages earlier in the book.

## 193v — the call of Matthew at the receipt of custom

**1**  This holy gospel begins,
`begins this holy-gospel`

**2**  written by holy Matthew, in the […]
`write holy-Matthew inside and`

**3**  chapter of the writing: the time,
`chapter <of>-write time`

**4**  then the Lord Jesus within
`then Lord-Jesus inside`

**5**  thirtieth year, the time
`thirty years* time`

**6**  he preached in | there was
`preach inside | ~exist`

**7**  afterward, one; and then the Lord Jesus [was] teaching in Capharnaum,
`°afterward-+one and then teaching Lord-Jesus inside Capharnaum`

**8**  and left, down, on preaching; and [many] followed the Lord.
`and leave down on-preach and follow^ to-Lord`

**9**  to him; and then the Lord went into the town, and saw,
`many people and then-exist go-Lord on-town and see`

**10**  the Lord Jesus, at the publican's [place], sat holy Matthew. And then the Lord Jesus
`Lord-Jesus on-publican sit holy-Matthew and_said Lord-Jesus`

> Matthew 9:9, Douay: *Jesus saw a man sitting in the custom house, named
> Matthew; and he saith to him: Follow me.* K&T's dictionary carries the
> tax-collector sign, so the reading of the line is theirs.

## 194r — he sat at meat in the house

**1**  Matthew went to the Lord, to the food, to the place; holy Matthew rose, and
`Matthew go to-Lord on-food to-place rise holy-~Matthew and`

**2**  Matthew went to the Lord Jesus; and the Lord went with Matthew to holy Matthew's house,
`go-Matthew to-Lord-Jézus and go-Lord-Matthew holy-~Matthew house`

**3**  and did, from many, to the table company; how?
`and do from-many-to table company how?`

**4**  Speaks holy Luke: did, from many, to the table.
`speak holy-Luke do from-many-to table.`

**5**  company; and there went to the Lord the Jews, the Pharisees, and
`company and go to-Lord Jew pharisee and`

**6**  the tax collectors, the chief men; and together with the Lord Jesus they drank
`tax_collector exist head and together Lord-Jézus drink`

**7**  and ate, the sinners; and the Jews began,
`and eat sinners* and begin Jew(ish).`

**8**  the Pharisees spoke [to] the Lord's disciples: this you, Master,
`pharisee speak disciple^ of-Lord this you Master`

**9**  save sinners? In turn, then, he is
`sinners* save in_turn then he exist`

> Matthew 9:10-11, Douay: *as he was sitting at meat in the house, behold many
> publicans and sinners came, and sat down with Jesus and his disciples. And
> the Pharisees seeing it, said to his disciples: Why doth your master eat
> with publicans and sinners?*

## 194v — they that are well need not a physician

**1**  and the Lord said: he is a sinner, not from the Lord's salvation; and
`and Lord say he exist sinner^ not from-salvation-Lord and`

**2**  the blind to the Lord Jesus [they that are well] got angry. And then the Lord Jesus [answered]
`~blind-to Lord-Jesus [they_that_are_well] get_angry and_said Lord-Jesus [answered]`

**3**  to the Lord: I go, the Lord, to the just man on this world, but to sin.
`to-Lord I go-Lord to-just_man on-this world but to-sin`

**4**  And then the Lord Jesus: you, just man. And then
`and_said Lord-Jesus you just_man and_said`

**5**  the Lord Jesus: need, the healthy, healing; but rather need.
`Lord-Jesus need the_healthy healing but_rather need.`

**6**  one sin, is this health. Here ends this holy gospel.
`one-sin ~exist-this health here_ends this holy_gospel`

**7**  written by holy Matthew in the […] chapter. Holy Paul speaks and says: | the Lord
`write holy-Matthew inside and chapter holy-Paul speak say | Lord`

**8**  Jesus Christ, from the beginning of the world, from Adam's creation, | to
`Jesus-Christ from* beginning world from* ~Adam create | to`

**9**  [until] the coming of the Lord Jesus Christ into this world [then]
`[until] ~be_born Lord-Jesus-Christ on-this world [then]`

> Matthew 9:12-13, Douay: *They that are in health need not a physician, but
> they that are ill... For I am not come to call the just, but sinners.* Both
> halves, in the gospel's order, and the folio then turns to Paul.

## 195r — from Adam to the coming of Christ

**1**  truly, the man; and one prophet, and one forefather,
`righteous(ly) somebody and one prophet and one forefather`

**2**  and one holy father, holy living; and one | [prophet]
`and one holy-father holy-living and one | [prophet]`

**3**  the father […] in heaven;
`father-[?]-[?]-[?] inside heaven =`

**4**  but rather, then, at the coming of Christ into this world, and then, in his
`but_rather-+one then coming* Christ on-this world* and then-exist inside`

**5**  thirtieth day, the time […] the Lord Jesus upon Carmel,
`thirty day time from-[?]-[?] Lord-Jézus on-Carmel`

**6**  the mount; and then out, thirty-three and a half [years]; at that time
`mount and then out thirty half-three time`

**7**  he was crucified, and on the third day stood up from the dead; and many holy prophets
`crucified and on_the_third_day from die stand_up and many holy-prophet`

**8**  and holy forefathers and holy fathers, holy living, out of the netherworld | to
`and holy-forefather and holy-father holy-living on-netherworld out(ward) | to`

**9**  the Lord went; and then, forty days; at that time to leave
`go-Lord and then forty_days time to-leave`

## 195v — he shall come to judge the quick and the dead

**1**  to the Lord's Father, on the heavenly kingdom; | sat down
`to-of-Lord the_Father on-heaven kingdom^ | sit_down`

**2**  the Lord, the Father, on the right; from there has the Lord [to] go, the Lord, to judge
`Lord the_Father on-right from_there have-Lord go-Lord judge`

**3**  the living and the dead; and before the ascension he blessed all the whole
`the_living and the_dead and before ascension bless every all_the_world`

**4**  world. This holy gospel begins,
`world begins this holy-gospel.`

**5**  written by holy Matthew | [sixteen]
`write holy-Matthew | [sixteen]`

**6**  the fourth chapter of the writing:
`two-two chapter of-write.`

**7**  the time, then, | the Lord
`time then-exist | Lord`

**8**  Jesus, thirty [and a] half, three; at that time said the disciples [to] the Lord Jesus:
`Jesus thirty half-+three time say disciple^ Lord-Jesus.`

**9**  Master, who is to the Lord, he, on Holy, within heaven's
`Master who? exist to-Lord he on_Holy inside heaven`

> The creed, clause by clause: *sitteth at the right hand of the Father, from
> thence he shall come to judge the living and the dead.* Then Matthew 18:1,
> *Who thinkest thou is the greater in the kingdom of heaven?*

## 196r — except you become as little children

**1**  kingdom? because the disciples recognized as the Lord crucified; and
`kingdom^ because recognize disciple^ as Lord crucified and`

**2**  on the third day stood up from the dead; and the Lord to these apostles, to judge
`on_the_third_day from die stand_up and Lord to-this apostle judge`

**3**  who is to the Lord, he, on Holy, within heaven;
`who? exist to-Lord he on_Holy inside heaven =`

**4**  and the Lord Jesus called one little son,
`and call^ Lord-Jesus one little son.`

**5**  and the son the Lord Jesus set upon the head,
`and son <subject> put_on Lord-Jézus on-head.`

**6**  the Lord's hands. And then the Lord Jesus: who [is] not this humble | how
`of-Lord hands and_said Lord-Jesus who-not this humble | how?`

**7**  <subject marker> this little son, one [is] not saved.
`SUBJ this little son one not be_saved`

**8**  The time the Jews brought one | before | the Lord
`time carry Jew(ish) one | before | Lord`

**9**  Jesus, from this emperor, to whom, and he was a pagan.
`Jézus from* this emperor to-+who-to and exist pagan.`

> Matthew 18:2-4, Douay: *And Jesus calling unto him a little child, set him
> in the midst of them, and said... whosoever therefore shall humble himself
> as this little child, he is the greater in the kingdom of heaven.* The sign
> here read as *little* is the one this project first read wrongly as *child*
> and corrected against K&T's own entry.

## 196v — the keys, and whatsoever thou shalt bind

**1**  Because he heard from every man, upon one | before; this was:
`because hear from each,_every somebody on-one | before this exist`

**2**  the Lord Jesus gave the key of salvation [to] holy Peter; said | the Lord
`give^ Lord-Jesus key be_saved holy-Peter say | Lord`

**3**  Jesus: who[m] this Peter binds on this world, from
`Jesus who this-Peter bind on-this world from`

**4**  the man is bound, and from heaven's kingdom;
`man^ exist bind and from_heaven* kingdom^`

**5**  in turn who[m] this Peter absolves on this world, from
`in_turn who this-Peter absolve on-this world from`

**6**  the man is absolved, and from heaven's kingdom.
`man^ exist absolve and from_heaven* kingdom^`

**7**  And then the Lord Jesus: he who [is] on Holy, the Lord, you from
`and_said Lord-Jesus he_who on_Holy Lord you from`

**8**  the Lord, every [one] a servant. And then the Lord Jesus: who [does] not this
`the_Lord every servant and_said Lord-Jesus who-not this`

**9**  apostle, from this little son, does
`apostle this from little son to* do,`

> Matthew 16:19, Douay: *And I will give to thee the keys of the kingdom of
> heaven. And whatsoever thou shalt bind upon earth, it shall be bound also in
> heaven: and whatsoever thou shalt loose on earth, it shall be loosed also in
> heaven.* The codex writes the two halves as a matched pair on lines 3-6,
> which is why the signs in them are among the better attested on the folio.

## 197r — their angels always see the face of my Father

**1**  within the Lord's name, [by] name, and one [is] not saved.
`inside of-Lord ~brother-+name and one not be_saved`

**2**  And then the Lord Jesus, the Lord's apostles, not apostles, and one
`and_said Lord-Jesus apostle of-Lord not apostle and one`

**3**  [despise not] [little ones] do. And then the Lord Jesus [to the] apostles:
`[despise_not] [little_ones] do and_said Lord-Jesus apostle`

**4**  of the Lord: happy are the people, and the angels see the face
`<of>-Lord happy from people and angel see face`

**5**  of the Lord's Father, the will, from the people; and the angels on seeing
`of-Lord the_Father will from-people and angel on-see.`

**6**  the face of the Lord's Father. Here ends this holy gospel.
`face of-Lord the_Father here_ends this holy_gospel`

**7**  This holy gospel begins, written by
`begins this holy-gospel write`

**8**  holy Matthew: the time | the Lord
`holy-Matthew time say | Lord`

**9**  Jesus said to the Lord's apostles, and to the Jewish
`Jézus apostle <of>-Lord and Jew(ish)`

> Matthew 18:10, Douay: *See that you despise not one of these little ones:
> for I say to you, that their angels in heaven always see the face of my
> Father who is in heaven.*

## 197v — take up his cross and follow me

**1**  people; and the apostles, somebody, the Jews: [who] want to go to the Lord | deny
`people and apostle-somebody-Jew want to Lord go | deny`

**2**  the man, our all the world; and take our
`man^ our all_the_world and grab our`

**3**  cross on our shoulder; and go, somebody, to
`~cross on-our shoulder and go-somebody to`

**4**  the Lord. And then the Lord Jesus: who [is] this man, profit, and this world | rich
`Lord and_said Lord-Jesus who this man^ profit and this world | rich`

**5**  [for what] then this man <subject marker> takes our soul | to riches
`[for_what] then this man^ SUBJ grab our soul | to-rich`

**6**  [for what]. And then the Lord Jesus: good <subject marker> this man releases | of
`[for_what] and_said Lord-Jesus good SUBJ this man^ release* | of`

**7**  the man's soul; damned, but saved, because many a man;
`somebody soul be_damned ~a) be_saved because many somebody`

**8**  and the man is [in exchange] [for his soul] [shall render] saved, every
`and somebody exist [?] [?] [?] be_saved-somebody each,_every`

**9**  the man damned [according to] [his works]; the man is judged, the Jews
`man^ be_damned [according_to] [his_works] man^ exist judge Jews`

> Matthew 16:24-26, Douay: *If any man will come after me, let him deny
> himself, and take up his cross, and follow me... For what doth it profit a
> man, if he gain the whole world, and suffer the loss of his own soul?* The
> denying, the cross on the shoulder, the whole world and the soul are all
> here in order.

## 198r — go into all the world

**1**  to damnation; everybody saved. And then the Lord Jesus: you
`on-be_damned everybody = be_saved and_said Lord-Jesus you`

**2**  not, Jews, every until this belief, Jews, who
`not-Jews every until this-believe-Jews who`

**3**  I you, preach the Lord, every until
`I you preach-Lord every until`

**4**  this [look upon]; the Jews see, go on this world, from prayer,
`this [look_upon] see-Jews go on-this world from pray`

**5**  the Son of God within the body, somebody, in the year of judgment, every until
`son God inside body somebody on-judge-year every until`

**6**  this […] believe. And then the Lord Jesus [answered him]
`this-[?] believe and_said Lord-Jesus [answered_him]`

**7**  Peter, one among you; and the apostles | see,
`Peter one among you and apostle | see`

**8**  the apostles, from prayer, the Son of God, within […] the man,
`apostle from pray son God inside ~exist-[?] somebody`

**9**  and the apostles are within the son; the apostles ask. Here ends
`and apostle exist inside son ~ask-apostle end`

**10**  this holy gospel.
`this holy-gospel`

## 198v — write your names in the eternal land

**1**  Said the Lord God to the angel | of
`say <subject> Lord-<divine> on-angel | <of>`

**2**  the Lord, holy […] the prophet, and | holy
`Lord holy-<prophet> prophet and | holy`

**3**  Elijah the prophet [was taken up] | the Jews
`Elijah prophet [was_taken_up] | Jews`

**4**  the apostles, somebody, to the Lord: I.
`apostle-somebody to-Lord I.`

**5**  you […], Lord, have mercy on sin [fruit] this is
`you [...] Lord sin have_mercy [fruit] this exist`

**6**  within the commandment, somebody, that is; and has somebody observing the commandment
`inside commandment somebody that_is and have somebody observe commandment`

**7**  of God, does not commit sin; somebody is saved, many | sufferings
`God not_commit sin somebody be_saved many | suffering`

**8**  not, for ever and ever, amen. Writes <subject marker> the names
`not for_ever_and_ever = amen write SUBJ name`

**9**  ours within heaven, to the house; dies, in turn | on
`our inside heaven = to-house die in_turn | on`

**10**  death, the body and the soul, for ever and ever, amen.
`die body and soul for_ever_and_ever = amen`

> Luke 10:20: *rejoice in this, that your names are written in heaven.* The
> book's frame -- a revelation given to Elijah -- returns on lines 2 and 3,
> which is where it always returns, at the join between two readings.

## 199r — a man had a vineyard and two sons

**1**  This holy gospel begins,
`begins this holy-gospel`

**2**  written by holy Matthew | in the
`write holy-Matthew | one`

**3**  twentieth, in the fifth chapter
`ten-+one-ten inside five chapter`

**4**  of the writing: the time,
`<of>-write time`

**5**  then the Lord Jesus within
`then Lord-Jesus inside`

**6**  thirty-three and a half [years],
`thirty half-three`

**7**  the time the Lord Jesus preached in Jerusalem; and the Lord Jesus said to the apostles
`time preach Lord-Jézus inside Jerusalem and say Lord-Jézus apostle`

**8**  of the Lord, and to the Jewish people: the kingdom of heaven left a man
`<of>-Lord and Jew(ish) people leave king somebody heaven`

**9**  land. And then the Lord Jesus: there was [a vineyard]
`land and_said Lord-Jesus exist [a_vineyard]`

**10**  one rich man, a vineyard; and then he had
`one rich-somebody vineyard and then-exist have`

> Matthew 21:28, Douay: *But what think you? A certain man had two sons.* The
> vineyard and the two sons are both on the page, and the sign read here as
> *man* was got from this very line, out of K&T's own word for it.

## 199v — go work today in my vineyard

**1**  two sons, the pagan [and] the Jew. And then this rich somebody | of
`two son pagan Jew and_said this rich-somebody | of`

**2**  the Lord, somebody, son, on the Jews [go work today], brought the son into | the Lord's, from
`Lord-somebody son on-Jews [go_work_today] brought-son inside | of-Lord-from`

**3**  the man's vineyard to cultivate; said, brought the son to this: go, Jews.
`man vineyard cultivate say brought-son to-this ~go-Jews`

**4**  And then this rich somebody […] […] the second, to the son,
`and_said this rich-somebody [?]-[?] two to-~son`

**5**  […] somebody, into the Lord's somebody's vineyard, vinedresser. And then
`[?]-somebody inside of-Lord-somebody vineyard vinedresser^ and_said`

**6**  the priest, and […] […] the man; and said
`priest* and [?]-[?] [?]-somebody and say`

**7**  the Lord Jesus to the high priest and to the Lord's apostles: judge, Lord,
`Lord-Jesus high_priest = and apostle of-Lord judge-Lord`

**8**  I [ask] you: who <subject marker> this good? Say.
`I you who? SUBJ-this good say.`

**9**  Said the high priest: which <subject marker> good? He who
`say high_priest = who? SUBJ good say he_who`

> Matthew 21:28-31: *Son, go work to day in my vineyard... Which of the two
> did the father's will? They say to him: The first.* The question put back to
> the chief priests is on lines 7-9, exactly where Matthew has it.

## 200r — he let out the vineyard to husbandmen

**1**  said, to the pagan, the priest; and whosoever would be named, in turn went to the pagan;
`say-to-+pagan priest* and name-+who-want in_turn go-to-+pagan`

**2**  And then the Lord Jesus, rightly, the Jews spoke; and the rest said the Lord Jesus
`and_said Lord-Jesus righteous-Jews speak and the_rest^ say Lord-Jesus`

**3**  a parable, and said: there was, taken, one rich lord, on lease
`parable say exist take^ one rich-Lord on-lease`

**4**  the Lord's vinedresser, the vinedresser, the Lord's vineyard; and then
`of-Lord vinedresser vinedresser^ of-Lord vineyard and then`

**5**  the vineyard, the Jews, many years carried, the Jews, to the Jews to take, to release
`vineyard-Jews many year carry-Jews to-Jews take^ release^`

**6**  the vineyard lease. And then this rich Lord | of
`vineyard lease and_said this rich-Lord | of`

**7**  the Lord's servants, prophets and angels, the prophets and angels went, this lease
`Lord servant prophet and angel go-prophet-angel this lease`

**8**  from the Jews to ask, the prophets, the angels; and | the prophets,
`from* Jews ask-prophet-angel and | prophet`

**9**  the angels, the lease to the Jews, the Jews took, than
`angel lease to-Jews grab-Jews than`

> Matthew 21:33-35, Douay: *There was a man an householder, who planted a
> vineyard... and let it out to husbandmen... And he sent his servants to the
> husbandmen, that they might receive the fruits thereof. And the husbandmen
> laying hands on his servants, beat one and killed another.* The codex names
> the servants as the prophets and the angels, which is the standard reading
> of the parable and not Matthew's wording.

## 200v — last of all he sent his son

**1**  they killed all; and the Lord's son went; this rich lord said to this son:
`every kill^ and go-Lord of-Lord son this rich-Lord say this son`

**2**  are, the Jews, having, would say, the lease the Lord takes;
`exist-Jews have would_say* lease Lord take^`

**3**  and then the Lord was, the Jews saw, and went; and the son.
`and then-Lord exist-Jews see and go and son.`

**4**  said. And then the Jews: this is the son from [the heir]
`say* and_said-Jews this_is son from [the_heir]`

**5**  <subject marker> the vineyard, the father's son [cast him out]; and this
`SUBJ vineyard the_father-~son [cast_him_out] and this`

**6**  son is the vineyard; carry. And then the Jews: go, die.
`son exist vineyard carry and_said-Jews go-die`

**7**  the Jews; and [sent] to the Lord; and the son died, the Jews; and
`Jews and [sent] to-Lord and son die-Jews and`

**8**  then was until [killed him]; and the Jews, the head:
`then exist until [killed_him] and Jew ~head`

**9**  how? he said; spoke the Lord Jesus; and thirdly the Lord Jesus said a parable,
`how? he_said* speak Lord-Jézus and three say Lord-Jézus parable`

> Matthew 21:37-39, Douay: *And last of all he sent to them his son, saying:
> They will reverence my son. But the husbandmen seeing the son, said among
> themselves: This is the heir: come, let us kill him... And taking him, they
> cast him forth out of the vineyard, and killed him.* The heir is on line 6.

## 201r — the marriage of the king's son

**1**  and said: there was one king in a land, and then
`say exist one king inside land and then-exist`

**2**  he had one son; and the king would make
`have one son and son want king`

**3**  a wedding; prayed; and then [he] called, this king,
`wedding pray and then call^ this king`

**4**  all the Lord king's, land, to this wedding; and | then,
`every of-Lord king ~land on-this wedding and | then`

**5**  not one went on this wedding. Grew angry this
`not one go on-this wedding grow_angry this`

**6**  king. And then, that is, the people; and excused [themselves], the people,
`king and_said that_is people and excused people`

**7**  of the Lord's table; in turn all the world, to dinner. And then the Lord Jesus: who did
`of-Lord table in_turn all_the_world dinner-to and_said Lord-Jesus who do`

**8**  this king? He said to the Lord's servants: all, from the town,
`this king say <of>-Lord servant each,_every from town.`

**9**  destroy [with] fire and water. And then this king
`destroy fire and* water and_said this king`

> Matthew 22:2-7, Douay: *The kingdom of heaven is likened to a king, who made
> a marriage for his son... But they neglected: and went their ways... But
> when the king had heard of it, he was angry, and sending his armies, he
> destroyed those murderers, and burnt their city.* The anger and the burning
> are both here; the water is the codex's own.

## 201v — go out into the highways

**1**  said to the Lord's servants: go, and speak this word, to the understanding, to the hidden;
`<of>-Lord servant go and this word speak-understand-hide_oneself exist`

**2**  leave; and is called on this wedding. And then
`leave and exist call^ on-this wedding and_said`

**3**  this Lord king's servants went, to the blind, to the hidden, and
`this Lord-king <of>-Lord servant go-?blind-hide_oneself and`

**4**  the way, and to the town; and they found
`way and on-town and find`

**5**  the poor man of God, ninety, blind, and still more […] and
`poor_man_of_God = ninety-~exist blind and still_more-[?]-to and`

**6**  the hungry and the thirsty, and [feeble] the poor of God, and
`be_hungry and thirst and [?] God blind and`

**7**  [go ye] [into the highways] the servants found; all the servants went,
`[?] [?] find servant each,_every go-servant`

**8**  filled within the Lord king's house; and then filled
`filled* inside of-Lord-king house and then fill`

**9**  the house, this king, the various heaven
`house this king various heaven`

> Matthew 22:9-10, Douay: *Go ye therefore into the highways; and as many as
> you shall find, call to the marriage. And his servants going forth into the
> ways, gathered together all that they found, both bad and good.* The blind
> and the hungry are Luke 14:21 folded in, which is the codex's habit.

## 202r — the man without a wedding garment

**1**  Lord; and this king said, this king; and the king went into
`Lord and say this king this-king and go-king inside`

**2**  the Lord king's house; the king would go before, out of
`<of>-Lord-king house want-king to-before on-+out`

**3**  the Lord king's house; and then this king went
`<of>-Lord-king house and then-exist ~go this king`

**4**  into the Lord king's house; and this king saw
`inside <of>-Lord-king house and see this king`

**5**  one man of God in ragged clothes; and
`one God-somebody ragged clothes and`

**6**  thus the king said: this friend, name, sat, to whom, one, which man
`say that_is king this friend name-°sat-to_whom-+one who man^`

**7**  [the king came in] the man went [a wedding garment] the man, friend,
`[?] go-somebody [?] somebody friend`

**8**  the wedding clothes, by name, which this man
`wedding clothes to-+name who this somebody`

> Matthew 22:11-12, Douay: *And the king went in to see the guests: and he saw
> there a man who had not on a wedding garment. And he saith to him: Friend,
> how camest thou in hither not having on a wedding garment?* The friend and
> the wedding garment are both here, and the codex renders the missing garment
> as ragged clothes, which is K&T's own word.

## 202v — bind him hand and foot

**1**  said, within the Lord God's heaven house, found, the year; good, said this king,
`say inside of-Lord_God heaven house find-~year good say this king`

**2**  Gabriel, friend, brother by name, this most high, to, sat, the will;
`Gabriel friend brother-+name this-high to-°sat will`

**3**  Gabriel spoke and said: bind the man's hands and
`speak-+Gabriel say tie_(up) somebody hand and.`

**4**  feet, and cast the man out, the angel, outside, darkness
`foot and somebody cast_out angel on-out darkness`

**5**  there is seen the grinding of teeth, weeping, ever
`there exist see grinding tooth weep ever`

**6**  ever. Here ends this holy gospel. The Lord God, be loved.
`ever here_ends this holy_gospel Lord_God be_loved`

**7**  This holy gospel begins, written by
`begins this holy-gospel write.`

**8**  holy Matthew, [twenty-two] chapter | of
`holy-Matthew [twenty_two] chapter | of.`

**9**  the writing: the time, then, | the Lord
`write time then-exist | Lord`

**10**  Jesus, thirty-three and a half [years]; at that time
`Jesus thirty half-three time`

> Matthew 22:13, Douay: *Then the king said to the waiters: Bind his hands and
> feet, and cast him into the exterior darkness: there shall be weeping and
> gnashing of teeth.* The binding, the casting out, the weeping and the
> gnashing are all here. The codex names the servant who does it **Gabriel**,
> which no gospel does.

## 203r — is it lawful to give tribute to Caesar?

**1**  The Lord Jesus preached in Jerusalem, and the Jews came to him, | to the Lord
`preach Lord-Jézus inside Jerusalem and to-leave Jew(ish) | to-Lord`

**2**  Jesus. And then the Jews: Master, the Jews [Master] [we know] true
`Jesus and_said Jews Master-Jews [Master] [we_know] true^`

**3**  the man; and truly the Lord is a prophet, because truly in God's way
`somebody and righteous(ly)-Lord prophet because righteous(ly) God way`

**4**  the Lord goes; and the Lord has the king and the emperor
`go-Lord and Lord ~have king and emperor`

**5**  [teachest]; go, the Lord's name, learn; how? learn, the Jews, learn | want
`[teachest] go name-Lord learn how? learn-Jews-learn | want`

**6**  the Lord take from what they would do? | […]
`Lord grab from would_say* do, | [?]-[?]`

**7**  the Jews: take from everybody one drachma
`Jews grab from everybody = on-one drachma.`

**8**  [for] the heathen emperor? And said the Jews: how? learn, the Jews, learn.
`emperor heathen and say-Jews how? learn-Jews-learn`

**9**  Would the Lord take from what they would do? Said
`want-Lord grab from would_say* do, say`

> Matthew 22:16-17, Douay: *Master, we know that thou art a true speaker, and
> teachest the way of God in truth... Tell us therefore, is it lawful to give
> tribute to Caesar, or not?* The flattery and the question are both here,
> and K&T's own dictionary carries the drachma.

## 203v — whose image and superscription?

**1**  the Lord Jesus: carry, Jews, [to] the Lord the tax; and the Jews carried
`Lord-Jesus carry-Jews Lord tax and carry-Jews`

**2**  before the Lord Jesus. And then the Lord Jesus: whose <subject marker> this
`before Lord-Jesus and_said Lord-Jesus whose?-+SUBJ this`

**3**  image? Said the Jews: this is the emperor's image.
`image^ say Jew this_is ~emperor image^`

**4**  And then the Lord Jesus: whose <subject marker> this writing? Said
`and_said Lord-Jesus whose?-+SUBJ this write say`

**5**  the Jews: this is the emperor's writing. And then | the Lord
`Jew this_is ~emperor write and_said | Lord`

**6**  Jesus: this is the emperor's image; and the emperor's
`Jesus this_is ~emperor image^ and ~emperor`

**7**  writing; this emperor['s] until leave. And then | the Lord
`write this ~emperor until leave and_said | Lord`

**8**  Jesus: who […] indebted [to the] emperor [whose image]
`Jesus who-[?] indebted ~emperor [whose_image]`

**9**  [to] the emperor, take […]; in turn | love, the Jews, the apostle.
`emperor grab-[?] in_turn | love-Jews-apostle`

> Matthew 22:20-21, Douay: *Whose image and inscription is this? They say to
> him: Caesar's. Then he saith to them: Render therefore to Caesar the things
> that are Caesar's; and to God, the things that are God's.* The codex asks
> the question twice, once of the image and once of the writing, which is its
> own doubling and not Matthew's.

## 204r — render to God the things that are God's

**1**  the man owes God; this, God, take it.
`somebody indebted God this God grab-[?]`

**2**  And then the Lord Jesus: is believing […]
`and_said Lord-Jesus exist ~believe-[?]`

**3**  the emperor, and God; and somebody, from being indebted, pray not
`~emperor and God and somebody from indebted pray not`

**4**  he takes […]; if he owes […]
`grab-[?] ~if indebted-[?]`

**5**  Here ends this holy gospel. Said the Lord Jesus: there is
`end this holy-gospel say Lord-Jézus exist-[?]`

**6**  humble head, the Lord God, the emperor […], this world; and
`humble head Lord_God-~emperor-[?] this world and`

**7**  take […], the Lord God, the emperor […], who
`grab-[?] Lord_God-~emperor-[?] who`

**8**  the Jews […], and indebted […], because this
`Jews-[?] and indebted-[?] because this`

**9**  from the Lord God, the emperor […], you [render]
`from Lord_God-~emperor-[?] you [render]`

## 204v — what a man owes the Church

**1**  from heavenly belief, baptized, somebody remits; the heathen
`from heavenly* believe baptize somebody remit heathen`

**2**  out; believe, baptized, somebody; and | […] the apostles
`out believe baptize somebody and | [?]-apostle`

**3**  somebody; and the Lord God, the emperor, king | humble, the Jews, the apostle.
`somebody and Lord_God-~emperor-king | humble-Jews-apostle.`

**4**  the man; and he owes the Church, this man,
`somebody and indebted-[?] church this somebody`

**5**  [shall be gathered]; in turn, on, on Holy church; and
`[shall_be_gathered] in_turn on on_Holy church and`

**6**  of […] the Lord, the earth; in turn, before, secondly
`<of>-[?] Lord earth in_turn before two`

**7**  the Jews […] indebted [to] the church, this somebody, on
`Jews-[?] indebted church this somebody on`

**8**  [shall stand] before our spirit, the Father; and the Father, this
`[shall_stand] before our spirit the_father and father this`

**9**  somebody makes [his] way before the Lord's | Father
`somebody way do before of-Lord | the_father`

## 205r — fasting, the ten commandments, and thanks

**1**  the divine one; third, the Jews […] indebted, take | of
`DIV third Jews-[?] indebted grab | of`

**2**  somebody['s] fast, and our prayer, and the ten commandments
`somebody-fast and our pray and ten commandment`

**3**  of the Lord's Father; and indebted […] to kneel
`of-Lord the_Father and indebted-[?] kneel`

**4**  before the Lord's Father [shall be gathered] and
`before of-Lord the_Father [shall_be_gathered] and`

**5**  the man owes the Lord prayer, humble, the Lord's pleasing
`indebted-somebody Lord pray ~humble Lord pleasing`

**6**  and gives thanks; and to the Lord all heaven and earth;
`and give_thanks = and to-Lord every heaven land`

**7**  and somebody does not take the head, the Lord, from the emperor, the king,
`and somebody not_take head Lord from emperor king`

**8**  the world, who [is] indebted; somebody is believing, somebody,
`world who indebted somebody exist ~believe-somebody`

**9**  every Lord and every emperor and every king, every believer
`each,_every Lord and each,_every emperor and each,_every king each,_every believe`

## 205v — Jericho

**1**  baptized, the man [unto] the Lord's Father.
`baptize man^ [unto] of-Lord the_Father`

**2**  Here ends this holy gospel; and learning, the holy gospel. The Lord God, be loved.
`here_ends this holy_gospel and learn holy-gospel Lord_God be_loved`

**3**  This holy gospel begins,
`begins this holy-gospel`

**4**  written by holy Luke, in
`write holy-Luke inside`

**5**  the ninth end of numeral chapter of the writing:
`nine [?] chapter <of>-write`

**6**  the time, then,
`time then-exist`

**7**  the Lord Jesus, thirty, in one
`Lord-Jézus thirty inside one`

**8**  day; the time | the Lord
`day time go | Lord`

**9**  Jesus went into another town; and this town's
`Jézus inside one another town and this town`

**10**  name was Jericho; and then
`name exist Jericho and then-exist`

> Luke 19:1: *And entering in, he walked through Jericho.* The next folios are
> Zacchaeus, whose name K&T's dictionary carries in three spellings and which
> this project read a fourth of.

## 206r — Zacchaeus climbs the tree

**1**  the Lord Jesus kept going, the town of Jericho; and then in
`keep_going Lord-Jézus Jericho town and then-exist inside`

**2**  Jericho there was one chief tax collector, and
`Jericho one tax_collector head and.`

**3**  the man's name was Zacchaeus;
`[?]-+name somebody exist Zacchaeus`

**4**  and then the Jews saw the Lord; the Lord Jesus went into Jericho;
`and then Lord see-Jews go Lord-Jesus inside Jericho`

**5**  and Zacchaeus could not see the Lord Jesus,
`and Lord can see Zacchaeus Lord-Jézus`

**6**  but from [chief publican] Zacchaeus, this many people;
`a) from [?] Zacchaeus this many people`

**7**  and [he] climbed one tree, because [little of stature]
`and ascend one tree because [little_of_stature]`

**8**  Zacchaeus […] the Lord Jesus went; and then
`Zacchaeus [?]-go Lord-Jézus and then-exist`

**9**  the Lord Jesus went to this tree, and the Lord Jesus saw
`go Lord-Jesus to-this tree and see Lord-Jesus`

> Luke 19:2-4, Douay: *And behold, there was a man named Zacheus: and he was
> the chief of the publicans, and he was rich. And he sought to see Jesus who
> he was, and he could not for the crowd, because he was low of stature. And
> running before, he climbed up into a sycamore tree, that he might see him.*
> The crowd, the not seeing, and the climbing are all here.

## 206v — make haste and come down

**1**  Zacchaeus abiding on this tree;
`Zacchaeus abide^ on-this tree`

**2**  And then the Lord Jesus: Zacchaeus, go down,
`and_said Lord-Jesus Zacchaeus go down`

**3**  I today [must] be, the Lord, within Zacchaeus's
`I today exist-Lord inside of-Zacchaeus`

**4**  house, table, year, the Lord; and [with] joy left.
`house table-~year-Lord and joy leave.`

**5**  Zacchaeus; and he came down, this
`Zacchaeus and go down this.`

**6**  Zacchaeus; and went the Lord, the apostles, Jesus, into
`Zacchaeus and go-Lord-apostle-Jesus inside`

**7**  Zacchaeus's house; and | from
`Zacchaeus [?]-+who-to house and | from`

**8**  name of the Lord Jesus, […] out, year, the Lord sat; and the Jews began
`name Lord-Jesus [?]-~out-~year sit-Lord and begin-Jews`

**9**  to murmur on the Lord Jesus, the high priest; he said:
`murmur on-Lord-Jesus high_priest = he say`

> Luke 19:5-7, Douay: *Zacheus, make haste and come down; for this day I must
> abide in thy house. And he made haste and came down; and received him with
> joy. And when all saw it, they murmured, saying, that he was gone to be a
> guest with a man that was a sinner.* The murmuring is on line 9 and the sign
> for it is K&T's own.

## 207r — the half of my goods I give to the poor

**1**  the Son of God, in turn, with one sinner, from one
`son God in_turn one sin from-one`

**2**  an extorter, one extorts; and [he] stood up | name, Jerusalem,
`extorter* one extort and stand^ up | name-Jerusalem`

**3**  Zacchaeus. And then Zacchaeus:
`Zacchaeus and_said Zacchaeus`

**4**  Master, this Zacchaeus takes the half,
`Master this-Zacchaeus half grab`

**5**  unrighteously of Zacchaeus's riches, God,
`unrighteously of-Zacchaeus ~rich God`

**6**  the poor in spirit, undeservedly; in turn [he] stood up, one
`poor_in_spirit = undeservedly in_turn stand^ up one`

**7**  among you, in turn, chapter, Jerusalem [half my goods] | take,
`among you in_turn-chapter-Jerusalem [half_my_goods] | grab`

**8**  Zacchaeus, one denarius; on extorting, want, chapter, Jerusalem, the man,
`Zacchaeus one denarius on-extort want-chapter-Jerusalem man^`

**9**  to every [one] four take. And the Lord Jesus saw, as
`to-every two-two grab and see Lord-Jesus as`

> Luke 19:8, Douay: *Behold, Lord, the half of my goods I give to the poor;
> and if I have wronged any man of any thing, I restore him fourfold.* The
> half, the wronging, and the restoring are all here, and the restitution is
> reckoned in denarii, which is the codex's own money.
> Line 6 is Király & Tokai's *spiritual(ly) [poor]*, which they cite here and
> at 208r07. Corrected 2026-09-26: the earlier printing read it *spiritually
> blind*.

## 207v — this day is salvation come to this house

**1**  a righteous son of father Abraham. And then the Lord Jesus: | Zacchaeus,
`righteous son father Abraham and_said Lord-Jesus | Zacchaeus`

**2**  Zacchaeus, have it, because this day, in Zacchaeus's
`Zacchaeus have because this-[?]-+name today inside <of>-+Zacchaeus`

**3**  house is saved, Zacchaeus's; because the Lord, I
`house be_saved of-~Zacchaeus because Lord I`

**4**  [am] truly the Son of the living God. And then the Lord Jesus [to] the high priest:
`righteous son living God and_said Lord-Jesus high_priest =`

**5**  the Jews take the commandment; Zacchaeus not; the Lord to this, I
`grab-Jews commandment Zacchaeus not-Lord to-this I`

**6**  went, the Lord, on this world, who, I, sin, from sat [fourfold] | but
`go-Lord on-this world who I sin from-°sat [fourfold] | but`

**7**  the Lord, I went, the Lord, who, I, sin; the Lord loves; and the Lord, sin
`Lord I go-Lord who I sin love-Lord and Lord sin`

**8**  man; and [this day] of the Lord, the sinful man is saved,
`man* and [?] <of>-Lord be_saved sin-somebody exist`

**9**  and the Lord, godfearing; and the sinful man gives thanks. Here ends this holy gospel. The Lord God,
`and Lord godfearing^ and give_thanks = sin-somebody here_ends this holy_gospel Lord_God`

> Luke 19:9-10, Douay: *This day is salvation come to this house, because he
> also is a son of Abraham. For the Son of man is come to seek and to save
> that which was lost.* Abraham is on line 1 and the coming to save the sinner
> on lines 6-7.

## 208r — what Zacchaeus signifies

**1**  with all thy heart. This Zacchaeus is every chief among sinners,
`with_all_thy_heart* this Zacchaeus exist each,_every sin-somebody head`

**2**  and every tax collector, and every man who takes from the sinner, in mercy,
`and each,_every tax_collector and each,_every somebody from-grab somebody-sin inside have_mercy.`

**3**  the Lord God; and every sinful man, and the sinner in love, the Lord God; and every
`Lord-<divine> and each,_every somebody-sin and somebody-sin inside love Lord-<divine> and each,_every`

**4**  sinful man truly, and the sinner in truth, the Lord God, that is;
`somebody-sin righteous(ly) and somebody-sin inside righteous(ly) Lord-<divine> that_is`

**5**  and somebody, sin, carries the commandment of God; this is the righteous commandment of the Lord God;
`and somebody-sin carry commandment God this_is righteous commandment Lord_God`

**6**  and this Zacchaeus is mercy to God's poor in
`and this Zacchaeus exist have_mercy God spiritually`

**7**  blind; and this Zacchaeus loves the Lord God most high, every creation,
`blind and this Zacchaeus love Lord_God most_high every create`

**8**  and everybody as somebody [his] neighbour; and this.
`and everybody = as somebody neighbour* and this.`

**9**  Zacchaeus is within the righteous commandment of the Lord God, that is, | carrying
`Zacchaeus exist inside righteous commandment Lord_God that_is | carry`

## 208v — the first three commandments

**1**  <subject marker> […] the commandment of God, who is; taken within the word of the Old Testament, | from
`SUBJ-[?] commandment God who exist take^ inside Old_Testament word | from`

**2**  father Abraham. The first commandment of God: believe, man, truly,
`father Abraham first God commandment believe somebody righteous(ly)`

**3**  baptize; one God; somebody saved, many | not
`baptize one God be_saved somebody many | not`

**4**  sufferings; ours <subject marker> heaven land. The rest commandment
`suffering our SUBJ heaven land the_rest^ commandment`

**5**  is taken within the word of the Old Testament, the father Abraham: God's
`exist take^ inside Old_Testament word the_father Abraham God`

**6**  name in vain not take. The third commandment is taken
`name in_vain not_take three commandment exist take^`

**7**  within the word of the Old Testament, the father Abraham: shall somebody
`inside Old_Testament word the_father Abraham shall somebody`

**8**  truly baptize, holy Sunday and feast, holy this somebody, from
`righteous baptize holy-~Sunday and feast holy-this-somebody from*`

**9**  the mother, the temple; let a man hear the preaching, of […]
`mother temple preach hear-somebody <of>-[?].`

> The Decalogue, beginning. Exodus 20:3-8, Douay: *Thou shalt not have strange
> gods before me... Thou shalt not take the name of the Lord thy God in
> vain... Remember that thou keep holy the sabbath day.* The codex attributes
> them to "father Abraham" rather than Moses, which is its own slip and one it
> makes more than once.

## 209r — from Adam to Abraham to Moses

**1**  heaven land; and these three commandments the Lord God confirmed [to] Moses
`heaven land and this three commandment confirm Lord_God Moses`

**2**  by the Lord's angel; the time, then, from Adam, trespass.
`on-angel of-Lord time then from ~Adam ~trespass.`

**3**  until Abraham, one hundred years and […] years; from
`until Abraham one hundred-year and [?]-year from`

**4**  Abraham <subject marker> out until Moses, fifteen hundred
`Abraham SUBJ ~out until Moses half-+three_thousand`

**5**  and fifty; from Abraham until Moses, the time
`and fifty from Abraham until Moses time`

**6**  the Lord God first confirmed to Moses by the Lord's angel; and
`first confirm Lord-<divine> Moses on-angel <of>-Lord and say`

**7**  God's angel said: Moses, because of this, teach, Moses, this
`God angel Moses because-this on-learn this Moses this`

**8**  people the three commandments of the Lord; because this, the people believe one
`people three commandment of-Lord because-this people believe one`

> A chronology of the sort every medieval handbook carries, from Adam to
> Abraham to Moses. The codex's figures are its own and match no standard
> reckoning.

## 209v — the three laws, and what Zacchaeus kept

**1**  God; two, God's name in vain not take; three, God's commandment:
`God two God name in_vain not_take three God commandment`

**2**  [to keep] the holy Sunday and the feast, this holy man, from the mother, the temple;
`[?] holy-~Sunday and feast holy-this-somebody from* mother temple`

**3**  preaching hear, somebody; this [is] God's commandment; and the commandment somebody is
`preach hear-somebody this God commandment and commandment somebody exist`

**4**  bears; every such man is saved. And this Zacchaeus
`carry each,_every somebody exist be_saved and this Zacchaeus`

**5**  [hear the] word, love, and carry these three commandments of the Lord God. End [of] this
`[hear_the] word love and carry this three commandment Lord_God end this`

**6**  apostle's holy gospel. The Lord God, be loved.
`apostle holy-gospel Lord_God be_loved`

## 210r — a man possessed brought before the Lord

**1**  This holy gospel begins,
`begins this holy-gospel`

**2**  written by holy Matthew, in
`write holy-Matthew inside`

**3**  the fourteen-and-one chapter | of
`fourteen-+one end_of_numeral* chapter | of`

**4**  the writing: the time,
`write time`

**5**  then the Lord Jesus
`then Lord-Jesus`

**6**  within thirty-three and a half [years]; at that time preaching | the Lord
`inside thirty half-three time preach | Lord`

**7**  Jesus preached in Jerusalem; and then they brought one man
`Jézus inside Jerusalem and then-exist brought* one somebody`

**8**  before the Lord Jesus, in [the synagogue]; the man was [with] a devil;
`before Lord-Jesus inside [the_synagogue] man^ exist devil =`

**9**  And then the Jews: he [by] the prince of devils, the help
`and_said Jew he prince_of_devils help`

> Matthew 12:22-24, Douay: *Then was offered to him one possessed with a
> devil... But the Pharisees hearing it, said: This man casteth not out
> devils but by Beelzebub the prince of the devils.* The accusation is on
> line 9, and the codex uses its own Lucifer sign for the prince of devils.

## 210v — the unclean spirit walks through dry places

**1**  of the evil within, from the generation, casts out. And then the Lord Jesus: I
`evil inside from generation^ exorcise and_said Lord-Jesus I`

**2**  [by the finger of God], of the Lord's Father; and I, of God the Father, can miracles
`[by_the_finger_of_God] of-Lord the_Father and I of-God_the_Father can miracle`

**3**  do, the Lord. And then the Lord Jesus: this not pious, who
`do-Lord and_said Lord-Jesus this not_pious who`

**4**  from evil is expelled. And then the Lord Jesus: then.
`from evil exist expel and_said Lord-Jesus then.`

**5**  he casts out from a man one unclean
`exorcise inside somebody one unclean`

**6**  spirit, and the evil one goes to a dry place, and
`~spirit and go evil arid,_dry place and`

**7**  [walketh] to the Lord, the place, that is, to the virgin, from the generation, and
`[walketh] to-Lord place that_is on-virgin-from generation^ and`

**8**  to the word, the generation; and there is, therefore not, the evil
`on-word generation^ and exist therefore-°not evil`

**9**  lodging. And then this evil, this evil
`lodging-and_said this evil this-evil`

> Matthew 12:43, Douay: *And when an unclean spirit is gone out of a man he
> walketh through dry places seeking rest, and findeth none.* The dry place
> is on line 6 and K&T gloss the sign as "arid, dry".

## 211r — seven other spirits worse than himself

**1**  and the evil one goes [wicked] because from the evil, love, sin, the sinful man;
`and go-evil [?] because from evil love sin somebody-sin`

**2**  and he takes [taketh with him] seven evil ones, from the evil,
`and exist grab [?] seven evil from evil`

**3**  trespass, mourning; and there are [wicked] seven evil ones; and | they go,
`trespass mourn and exist [wicked] seven evil^ and | go`

**4**  the evil ones, all seven. And then the Lord Jesus: how then this man,
`evil^ every seven and_said Lord-Jesus how? then this man^`

**5**  the first aforesaid [swept]; and everybody, wish, into the house
`first^ aforesaid [swept] and everybody = wish inside house`

**6**  goes, this; and stood up, up, the first woman, the head,
`go-this ~and stand_up-up first^ ~woman head`

**7**  among this people, the Jews. And then: blessed from the womb
`among this people Jew and_said blessed from womb`

**8**  which <subject marker> carried him, and blessed from the breasts which | this
`which-+SUBJ he carry and blessed from breast which | this`

**9**  Lord nursed. And then the Lord Jesus: blessed <subject marker> the Lord's mother,
`Lord nurse and_said Lord-Jesus blessed SUBJ of-Lord mother`

> Matthew 12:45, Douay: *Then he goeth, and taketh with him seven other
> spirits more wicked than himself.* Then Luke 11:27, folded in: *a certain
> woman from the crowd, lifting up her voice, said to him: Blessed is the womb
> that bore thee, and the paps that gave thee suck.*

## 211v — rather, blessed are they that hear the word of God

**1**  the Virgin Mary, which <subject marker> carried the Lord; and blessed from the breasts which
`Virgin_Mary which-+SUBJ to-Lord carry and blessed from breast which`

**2**  did nurse the Lord; and even more blessed are the people, and God said:
`to-Lord nurse even_more and blessed from people and God say.`

**3**  let a man hear, and say, and let a man bear it. Here ends this
`hear-somebody and say <subject> carry-somebody end this`

**4**  holy gospel. The Lord God, with all thy heart.
`holy-gospel Lord-<divine> ?with_all_thy_heart*`

**5**  This holy gospel begins,
`begins this holy-gospel`

**6**  written by holy John
`write holy-John`

> Luke 11:28, Douay: *Yea rather, blessed are they who hear the word of God,
> and keep it.* The "even more" on line 2 is the *quinimmo* of that verse,
> and the hearing and keeping are both on line 3.

## 212r — whence shall we buy bread?

**1**  within the sixth chapter of the writing: at that time, then, the Lord Jesus
`inside six chapter of-write time then Lord-Jesus`

**2**  within thirty-three and a half [years]; at that time sat the Lord Jesus | on
`inside thirty half-three time sit Lord-Jesus | on`

**3**  the Red Sea [of Galilee]; and the Lord went through,
`the_Red_Sea [?] and Lord through`

**4**  the Lord Jesus went through the Red Sea to one
`go-Lord Lord-Jézus through the_Red_Sea to-one`

**5**  mount; and the Lord Jesus sat upon this mount,
`mount and sit Lord-Jézus to-this to-mount`

**6**  and lifted up the Lord's two eyes to heaven [high] and
`and lifted_up of-Lord two eye heaven [high] and`

**7**  the Lord Jesus saw, on all four [sides], [a great multitude] people coming to the Lord; and
`see Lord-Jesus on-every two-two [a_great_multitude] people to-Lord and`

**8**  went. And then the Lord Jesus: Philip, this people | take
`go and_said Lord-Jesus Philip this people | grab`

**9**  the Lord's apostle Philip, to eat. And then holy Philip: Master,
`apostle-Lord-Philip eat and_said holy-Philip Master`

> John 6:3-5, Douay: *Jesus therefore went up into a mountain, and there he
> sat with his disciples... When Jesus therefore had lifted up his eyes, and
> seen that a very great multitude cometh to him, he said to Philip: Whence
> shall we buy bread, that these may eat?* The lifting of the eyes, the
> multitude and Philip by name are all here.

## 212v — five barley loaves and two fishes

**1**  then [we] have two hundred denarii; who, the people,
`then have two_hundred denarius who people`

**2**  buy bread? not enough [for] the people. And then
`bread buy not people enough and_said`

**3**  holy Andrew: Master, <subject marker> this [two hundred pennyworth] one.
`holy-Andrew Master SUBJ this [two_hundred_pennyworth] one.`

**4**  a little boy; and the boy has five
`~little boy^ and have boy^ five.`

**5**  loaves of barley bread, and two fishes.
`loaves barley bread and two fish`

**6**  And the apostles brought these five loaves of barley
`and carry apostle this loaves five barley`

**7**  bread and these two fishes before the Lord Jesus;
`bread and this two fish before Lord-Jézus`

**8**  and the Lord Jesus took this bread and
`and grab Lord-Jézus this bread and`

**9**  these two fishes; and this bread and
`this two fish and this bread and`

> John 6:7-9, Douay: *Two hundred pennyworth of bread is not sufficient for
> them... There is a boy here that hath five barley loaves, and two fishes.*
> Philip, Andrew, the two hundred pence, the five barley loaves and the two
> fishes are every one of them in John and every one of them here.

## 213r — twelve baskets full

**1**  these two fish the Lord Jesus blessed. And then the Lord Jesus [to] the disciples
`this two fish bless* Lord-Jesus and_said Lord-Jesus disciple^`

**2**  of the Lord: apostles, sit this people down upon the grass; and the Lord Jesus divided
`<of>-Lord sit-apostle down this people on-grass and on-divide_into_parts`

**3**  this bread to the apostles, and these two fishes, in turn, the apostles to this
`Lord-Jézus this bread apostle and this two fish in_turn apostle this`

**4**  people; and then the apostles, every apostle took his portion,
`people and then-exist apostle each,_every apostle-[?] portion grab-apostle`

**5**  and then the apostles […] to all the world, on eating. And then | the Lord
`and then apostle-[?] to all_the_world on eat and_said | Lord`

**6**  Jesus to the Lord's apostles: go, apostles, and take this, of the
`Jézus apostle <of>-Lord go-apostle and grab-apostle this from`

**7**  leftovers; and into baskets the apostles, of the leftovers, twelve
`leftovers and on-basket apostle from leftovers six-six`

**8**  filled. And then the Lord Jesus [to] the Lord's disciples: go, this out, among
`fill and_said Lord-Jesus disciple^ of-Lord go this out among`

**9**  this people; and then the apostles carried the twelve baskets filled up out
`people and then-exist apostle carry basket six-six fill_up out(ward)`

> John 6:10-13, Douay: *Now there was much grass in the place. The men
> therefore sat down... Gather up the fragments that remain, lest they be
> lost. They gathered up therefore, and filled twelve baskets.* The grass, the
> sitting, the gathering and the twelve baskets are all here, and K&T's own
> dictionary carries the sign for the leftovers.

## 213v — this is of a truth the prophet

**1**  among this people, many; and saw this many people the power of the Lord Jesus.
`among this people many and see this many people power Lord-Jesus`

**2**  and all the people gave the Lord thanks; and this word they cried out,
`and Lord each,_every people thanks grab and this word who-shout-to`

**3**  thanks: there is God, most high, highest; and the Lord took somebody, by name, one, can,
`thanks exist God most_high highest and the_Lord grab-somebody name-+one can`

**4**  and a man could do this miracle; and he left, among
`and somebody can this miracle do, and leave among`

**5**  this people, the Lord Jesus. Here ends this holy gospel. The Lord God, with all thy heart.
`this people Lord-Jézus end this holy-gospel Lord-<divine> ?with_all_thy_heart.`

**6**  This holy gospel begins,
`begins this holy-gospel`

**7**  written by holy John, in
`write holy-John inside`

**8**  the eighth chapter of the writing:
`six-two chapter <of>-write`

**9**  the time, then,
`time then-exist`

**10**  the Lord Jesus within thirty | [and a] half
`Lord-Jesus inside thirty | half`

**11**  three [years], the time.
`three time.`

## 214r — he that is of God heareth the words of God

**1**  The Lord Jesus preached in Jerusalem, and the Lord Jesus said to the Lord's apostles and to the Jewish
`preach Lord-Jézus inside Jerusalem and say Lord-Jézus apostle <of>-Lord and Jew(ish)`

**2**  people: left one up among you, apostles;
`people leave one up among you-apostle`

**3**  and the Lord admonished on sin. And then the Lord Jesus: verily verily
`and Lord on-sin admonish and_said Lord-Jesus verily verily`

**4**  I speak to you, apostles, the Lord; and […] <subject marker> from
`I you-apostle speak-Lord and [?]-+SUBJ from*`

**5**  God: this somebody […] God's word hears; in turn, and somebody […] not
`God this somebody-[?] God say hear in_turn and somebody-[?] not`

**6**  from God, this somebody […] God's word does not hear. And this
`from* God this somebody-[?] God say not hear and this`

**7**  […] <subject marker> from two [hath a devil]. And then the Jews:
`[?]-+SUBJ from* two [hath_a_devil] and_said Jew`

**8**  he [is] a blasphemer; he [has] Satan, the prince of devils,
`he one blasphemer he Satan prince_of_devils`

**9**  devils has the Lord; he [is] a heretic
`devil^ have-Lord he one heretic`

> John 8:47-48, Douay: *He that is of God, heareth the words of God.
> Therefore you hear them not, because you are not of God. The Jews therefore
> answered, and said to him: Do not we say well that thou art a Samaritan, and
> hast a devil?* The accusation is on line 8 and the codex makes it Lucifer.

## 214v — before Abraham was made, I am

**1**  and he on the holy feast healed the ill. And then the Lord Jesus within
`and he on-holy-feast ill heal-Lord and_said Lord-Jesus inside`

**2**  this [keep my word]: I committed sin, this healing? <subject marker> you [are] sad,
`this [keep_my_word] I commit sin this healing SUBJ you sad`

**3**  love; I [for] you on the holy feast healed the ill.
`love I you on-holy-feast ill heal-Lord`

**4**  And then the Lord Jesus: amen, amen, I [say to] you,
`and_said Lord-Jesus amen amen I you`

**5**  speaks the Lord; and somebody […] not believing the Lord, and one
`speak-Lord and somebody-[?] not Lord believe and one`

**6**  not somebody […] saved, but everybody damned, remains; and | the man,
`not-somebody-[?] be_saved but everybody = be_damned remain* and | man^`

**7**  the apostles, the Jews, is the Lord; believe from somebody […] is | living somebody
`apostle-Jews exist Lord believe from somebody-[?] exist | living-somebody`

**8**  one, the apostles, the Jews: for ever and ever not die. And then
`one-apostle-Jews for_ever_and_ever = not die and_said`

**9**  the Jews: of the Jews Abraham [is] black; <subject marker> believed God;
`Jew of-Jews Abraham black SUBJ God believe`

> John 8:51-52, Douay: *Amen, amen I say to you: If any man keep my word, he
> shall not see death for ever. The Jews therefore said... Abraham is dead,
> and the prophets.* The amen amen, the keeping and the not dying are here,
> and the Jews' answer begins on line 9.

## 215r — Abraham saw my day

**1**  and the black one, God's word he heard, Abraham, and still is dead
`and black <subject> God say hear Abraham and still <subject> [?]`

**2**  in turn he not die. And then the Lord Jesus: I saw
`in_turn he not die and_said Lord-Jesus I see`

**3**  you, the father Abraham. Said the Jews on the head:
`~you the_father Abraham say Jew on-head`

**4**  not he fifty; in turn <subject marker> this | two thousand(?)
`not he fifty in_turn-+SUBJ this | two-?thousand`

**5**  years; if of the Jews the father Abraham is dead; in turn | this
`year ~if of-Jews the_father Abraham is_dead* in_turn | this`

**6**  the Lord spoke, the Lord [rejoiced] Abraham; the Lord saw, the Lord; this [is] not pleasing;
`Lord speak-Lord [rejoiced] Abraham Lord see-Lord this not pleasing`

**7**  he [is] a blasphemer. And then the Lord Jesus: before I leave, than
`he blasphemer and_said Lord-Jesus before I leave than`

**8**  you, the father Abraham, on this world [was made]
`you the_father Abraham on-this world [was_made]`

> John 8:56-58, Douay: *Abraham your father rejoiced that he might see my day:
> he saw it, and was glad... Thou art not yet fifty years old, and hast thou
> seen Abraham? Jesus said to them: Amen, amen I say to you, before Abraham
> was made, I am.* The fifty years are on line 4 and the "before" on line 7.

## 215v — then they took up stones

**1**  And then the Jews: this [is] not pleasing; he [is] a blasphemer;
`and_said Jew this not pleasing he one blasphemer`

**2**  and the Jews carried stones, and would say: stone, stone this
`and carry-Jews stone and would_say* stone-stone-this`

**3**  Lord Jesus; and left among the Jews the Lord Jesus, and out | on
`Lord-Jesus and leave among-Jews Lord-Jesus and out | on`

**4**  the temple the Lord went, and the Lord's apostles. Here ends this holy gospel.
`temple and go-Lord and <of>-Lord apostle end this holy-gospel`

**5**  The Lord God, with all thy heart. Because it is written in Moses, truly, in turn [the law]
`Lord-<divine> ?with_all_thy_heart because-exist inside Moses righteous(ly) write in_turn [?]`

**6**  among you half somebody, how? a blasphemer, and has
`among you half somebody how? blasphemer and have`

**7**  somebody stone, stone this; and among the Jews out [out of the temple] [passing through]
`somebody stone-stone-this and among-Jews out [out_of_the_temple] [passing_through]`

**8**  spoke holy Elijah the prophet and holy Moses; not he said
`speak holy-+Elijah prophet and holy-Moses not he_said*`

**9**  the Jews can, because of […] the Lord created, the Lord God, of the Jews
`can-Jews because* of-[?] Lord create Lord_God of-Jews`

> John 8:59, Douay: *They took up stones therefore to cast at him. But Jesus
> hid himself, and went out of the temple.* The stones and the going out of
> the temple are both here, and the book's frame -- Elijah -- returns on line 8.

## 014r — the Lord went in humility

**1**  the Lord God; because the Lord went in humility, in turn the king, there is heaven and earth,
`Lord-<divine> because go-Lord humble-Lord in_turn king exist heaven and ~earth`

**2**  and many a miracle there was afterward, the Lord; and you, the Lord, | upon
`and many miracle exist afterward-Lord and you Lord | on`

**3**  the cross died, and on the third day stood up from the dead, and appeared to a great nation,
`cross-die and on_the_third_day from die stand_up and appear great^ nation^`

**4**  and the Lord was to you through staying forty years;
`and exist-Lord to-you through stay forty_years`

**5**  and then these forty years [King of kings] see,
`and then this forty_years [King_of_kings] see`

**6**  the Jews […] on every nation see; left within heaven
`Jews-[?] on-every nation^ see leave inside heaven`

**7**  land; and on leaving are the Jews that believe
`land and on-leave exist-Jews that* believe`

**8**  as the true Son of the living God, and king of every king, and
`as righteous son living God and king every king and`

**9**  Lord of all lords, the chief Lord of heaven and earth.
`Lord each,_every Lord head Lord heaven and ~earth`

> Revelation 19:16, Douay: *King of kings, and Lord of lords.* The manuscript's
> page order jumps here, and this project keeps Kiraly and Tokai's order
> rather than renumbering: 215v is followed by 014r, and the Palm Sunday
> reading runs 014r, 014v, 011r, 011v, 012r, 012v, 010r, 010v, 013r, 013v.

## 014v — a new gospel begins

**1**  This holy gospel begins, written by holy Matthew, in
`begins this holy-gospel write holy-Matthew inside`

**2**  the twentieth, in the first chapter of the writing: the time | then
`one-ten-+one-ten inside one chapter <of>-write time | then`

## 011r — go into the village, and you shall find an ass

**1**  was the Lord Jesus thirty-three and a half [years]; at that time went | the Lord
`exist Lord-Jesus thirty half-three time go | Lord`

**2**  Jesus went to Bethany, into Jerusalem, and the twelve apostles; and then | the Lord
`Jézus on-Bethany inside Jerusalem six-six apostle and then-exist | go`

**3**  went to the lodging [Bethphage] there was [mount Olivet] prayer, until, because
`Lord on-+lodging [?] exist [?] as* ~until because`

**4**  the trespassing way of the people, the lodging; and the trespassing, through the night,
`trespass way people lodging and trespass through night`

**5**  the lodging of the Lord Jesus; and then the Lord went, the Lord Jesus, two disciples down
`lodging Lord-Jesus and then-Lord go Lord-Jesus two disciple^ down`

**6**  Bethany, because trespass, the Jews carried every [over against you] way, the people,
`Bethany because trespass carry-Jews every [over_against_you] way people`

**7**  one donkey. And then the Lord Jesus: if you
`one donkey and_said Lord-Jesus if you`

**8**  [immediately] not, the Jews, take, the Jews, said the learners, two learners,
`[immediately] not-Jews grab-Jews say learn-two-learn`

**9**  take, the Jews, the learners, two learners, the donkey [tied]; the apostles <subject marker> [a colt] love
`grab-Jews learn-two-learn donkey [tied] apostle-+SUBJ [a_colt] love`

> Matthew 21:1-2, Douay: *And when they drew nigh to Jerusalem, and were come
> to Bethphage, unto mount Olivet, then Jesus sent two disciples, saying to
> them: Go ye into the village that is over against you, and immediately you
> shall find an ass tied, and a colt with her.* The two disciples, the
> village and the ass are all here.

## 011v — they set him thereon

**1**  [loose them]: Master, on going [bring them] the donkey, in the place, you, the donkey, to
`[loose_them] Master on-go [bring_them] donkey on-place you donkey to`

**2**  the Jews; and then the learners, two learners, were […] […].
`Jews and then learn-two-learn exist [?]-[?].`

**3**  one [laid their garments] the colt, to the donkey, the other donkey,
`one [laid_their_garments] colt^ to-donkey the_rest^ donkey`

**4**  the ass; and then the apostles untied this ass, and
`donkey and then-exist tie_up-apostle this donkey and`

**5**  [they did] this commandment; but [set him] and the Lord Jesus sat down
`[?] this commandment a) [?] and sit down Lord-Jézus`

**6**  on the, he said, donkey; and the Lord loosed, the disciples, this, from
`on-?he_said donkey and Lord loose disciple^ this from`

**7**  the ass, the mother of this ass; and the Lord sat upon this
`donkey mother this donkey and sit-Lord on-this`

**8**  from the donkey; and the Lord went into Jerusalem; and then.
`from donkey and go-Lord inside Jerusalem and then.`

**9**  the Lord was; the Lord went on the tasty to mount, highest, Jerusalem town
`exist-Lord go-Lord on-tasty-to mount highest Jerusalem town`

> Matthew 21:7: *And they brought the ass and the colt, and laid their
> garments upon them, and made him sit thereon.* The mother and the colt are
> distinguished on line 7, as they are in Matthew and nowhere else.

## 012r — the multitude went before him

**1**  and from sought, to the Lord Jesus and the Lord's apostles, because the apostles were [went before]
`and from-°sought-to Lord-Jesus and of-Lord apostle because apostle exist [went_before]`

**2**  And then the Lord Jesus [to] the Lord's apostles: go, you,
`and_said Lord-Jesus apostle of-Lord go you`

**3**  [multitude]; and if you [cried out], is judge,
`[multitude] and if you [cried_out] exist judge`

**4**  who is it; and the apostles went, the apostles said, and the apostles went to the Lord, to
`who_is_(it) and go-apostle say-apostle and go-apostle to Lord to`

**5**  Master; in turn to the Lord went two ways; and then the Lord
`Master in_turn to-Lord go two way and then-Lord`

**6**  was to the Lord [followed] many people, because they preached, this
`exist to-Lord [?] many people because [?]-+preach this`

**7**  people [a great multitude] the Lord Jesus went; and an army went
`people [?] go Lord-Jézus and and go an_army`

**8**  to the Lord Jesus; and then the Lord Jesus kept going to Jerusalem,
`to Lord-Jézus and then-exist keep_going Lord-Jézus to-Jerusalem`

**9**  and then the Lord was; saw on Jerusalem the people; and went the Lord Jesus
`and then-Lord exist see on-Jerusalem people and go Lord-Jesus`

## 012v — hosanna to the son of David

**1**  into Jerusalem; and [with] great joy the Jews shouted: he, and the son goes,
`inside Jerusalem and great^ joy shouted-Jews he and go son`

**2**  David the king; and the Lord, great joy, the Jews,
`David king ~and-Lord great^ joy Jews`

**3**  because one somebody, the Jews, of […] clothes;
`because one somebody-Jews of-[?] clothes^`

**4**  mercy [and] love; spread the Jews, somebody, before the Lord Jesus;
`have_mercy-love spread-Jews-somebody before Lord-Jesus`

**5**  second, the Jews, somebody, the bough <subject marker> | cut off
`second Jews-somebody bough-+SUBJ | cut_off`

**6**  the Jews, somebody; and [spread their garments] | [in the way]
`Jews-somebody and [spread_their_garments] | [in_the_way]`

**7**  somebody before the Lord Jesus; and the Jews shouted | this
`somebody before Lord-Jesus and shouted-Jews | this`

**8**  Lord is the son of David the king; they brought
`Lord <subject> son David king brought-[?].`

**9**  the king's crown, the Jews; and the Jew spoke: he
`king crown-Jews and speak Jew he`

> Matthew 21:8-9, Douay: *And a very great multitude spread their garments in
> the way: and others cut boughs from the trees, and strewed them in the way...
> Hosanna to the son of David.* The spreading, the cutting of branches and
> the cry are all here, in Matthew's order.

## 010r — my house shall be called the house of prayer

**1**  [is] king of the Jews. And this word the Jews shouted: thanks
`king Jew and this word shouted-Jews thanks`

**2**  to the Lord from all the people on earth, and the angels from heaven high; and
`Lord every people on-earth and angel from_heaven* high and`

**3**  the Lord Jesus went into the temple at Jerusalem; and then the Lord found
`go Lord-Jézus inside temple Jerusalem and then-exist exist-Lord find`

**4**  the moneychangers; and the Lord, all the moneychangers, out, the dove sellers | cast out,
`moneychanger and-Lord every moneychanger out dove_seller* | exorcise`

**5**  the Lord. And then the Lord Jesus: this temple <subject marker> [is] a house of prayer,
`Lord and_said Lord-Jesus this temple-+SUBJ prayer^ house`

**6**  one house by name; you Jews did one
`name-+one house you Jews do one`

**7**  den of thieves. And then from one little son
`den_of_thieves and then from one little son`

**8**  and shouted to: he <subject marker> […] the Jews' king.
`and shout-to he SUBJ [?]-Jews king`

**9**  And then one Jew: Master, see, Lord, who this
`and_said one Jew Master see-Lord who this`

> Matthew 21:12-13, Douay: *And Jesus went into the temple of God, and cast
> out all them that sold and bought in the temple... My house shall be called
> the house of prayer; but you have made it a den of thieves.* Both halves,
> and K&T's own dictionary carries the money changers.

## 010v — out of the mouth of infants

**1**  little son speaks, the son [Hosanna]: he [is] the Jews' king. And then
`little son speak-~son [Hosanna] he of-Jews king and_said`

**2**  the Lord Jesus: then this every, this little son not | speak
`Lord-Jesus then this every this little son not | speak`

**3**  the son, then, the earth is, and the rock and stone, all are,
`~son then exist earth and rock-stone each,_every exist.`

**4**  shouted to [son of David]: I [am] your, Jews, king.
`shout-to [son_of_David] I you-Jews king`

**5**  Here ends this holy gospel. The Lord God, with all thy heart. And then
`end this holy-gospel Lord-<divine> ?with_all_thy_heart* and then-[?]`

**6**  the commandment of the Jews; and the Jews, the Lord: take within this town Jerusalem
`commandment Jew and Jews Lord grab inside this town Jerusalem`

**7**  one cup, but rather the Jews, are, the Jews can cup this,
`one cup °but_rather-Jews exist-Jews can-Jews cup* this`

**8**  they would, the chief, take; and then […] the Lord
`would_say* head grab and then [?]-Lord`

**9**  the lodging find, the Creator Lord, heaven and earth, Lord of every lord,
`lodging find Creator_Lord heaven and earth Lord every Lord`

> Matthew 21:15-16, Douay: *and the children crying in the temple, and saying:
> Hosanna to the son of David... Have you never read: Out of the mouth of
> infants and of sucklings thou hast perfected praise?* The children's cry and
> the Lord's answer are both here, and line 3 is Luke 19:40, *the stones will
> cry out* -- folded in, as always.

## 013r — the prophet foretold it

**1**  King of all kings; spoke holy […] the prophet, and holy […]
`king each,_every king speak holy-<prophet> prophet and holy-<prophet>`

**2**  the prophet not can the lodging find, the Creator Lord; and the head
`prophet not can lodging find Creator_Lord and head`

**3**  of heaven and earth, Lord of all lords, King of all kings; and
`heaven and earth Lord each,_every Lord king each,_every king and`

**4**  out, the two, loving, foretold, the prophet, and holy […]
`~out(ward) love-two-exist predict <prophet> prophet and holy-<prophet>`

**5**  the prophet; and the Lord Jesus went [lodged] into Bethany, this [remained there]
`prophet and go Lord-Jézus [?] inside Bethany this [?]`

**6**  went [with him] the two, above, hidden, the earth; and this, many thanks the Lord did;
`go [?] two above-hide_oneself earth and this many thanks Lord do,`

**7**  in turn [morning] the Lord [returning], much sad. And then the Lord Jesus: this
`in_turn [morning] Lord [returning] many sad and_said Lord-Jesus this`

**8**  is [hungry] every one, from a man; and a man is of the Lord's name
`exist [?] each,_every from somebody and somebody exist <of>-Lord name`

**9**  among men; and out of the man, the good man does.
`among somebody and out(ward)-somebody good-somebody do,`

## 013v — the three tables of Moses

**1**  Three tablets Moses gave, and the Lord God wrote by the Lord's angel.
`three tablet Moses give^ and write Lord_God on-angel of-Lord`

> Exodus 31:18, Douay: *he gave to Moses... two tables of stone, written with
> the finger of God.* The codex counts three, as it does elsewhere when it
> is reckoning the Decalogue in three groups, which is how 208v-209v set it out.

## 218r — Gamaliel and Nicodemus, and a servant named Saul

**1**  the second, this holy man remits; the mother, the temple; let a man hear the preaching,
`two holy-this-somebody remit mother temple preach hear-somebody`

**2**  from the seeing; heaven and earth; and the time of prayer, the two
`<of>-from-see <subject> heaven land and time pray two`

**3**  church fathers at Jerusalem; three chiselled on tables of stone, because the Lord God had Moses
`church_father on-Jerusalem three on-stone-tablet chisel because exist Lord-<divine> Moses`

**4**  chisel three tables of stone by the Lord's angel, and wrote three commandments.
`three stone-tablet chisel on-angel <of>-Lord and write three commandment`

**5**  Thanks to the Lord God. The time, then, from Adam, trespass, seven […] and
`to-Lord thanks Lord_God time then from ~Adam ~trespass seven-[?] and`

**6**  fifteen hundred; and the time of these three tablets of Moses, prayer,
`half-+three_thousand and time this three tablet Moses pray`

**7**  two church fathers, two high priests at Jerusalem: Gamaliel the high priest and Nicodemus
`two church_father two high_priest-high_priest on-Jerusalem Gamaliel high_priest and Nicodemus`

**8**  the high priest; and then two servants hired out, learning, these two high priests;
`high_priest and then two servant hire_out learn this two high_priest-high_priest`

**9**  one man there was, and his name was Saul,
`one somebody exist and-~exist-exist-+name Saul`

> The Golden Legend's account of Stephen, which makes Gamaliel and Nicodemus
> his patrons -- Gamaliel is Acts 5:34 and Nicodemus John 3:1, and the legend
> buries Stephen in Gamaliel's field. Kiraly and Tokai's dictionary carries
> both names.

## 218v — Stephen, the first martyr

**1**  The second apostle was Saint Stephen, the first martyr; and | then
`second apostle exist Saint_Stephen the_first_martyr and | then`

**2**  there were two servants, these two, two apostles, these two, two high priests;
`exist two servant two this-two two apostle this-two two high_priest-high_priest`

**3**  in turn these two, two apostles, the two of them from [Damascus] the two, in belief,
`in_turn this-two two apostle exist-two from [?] two on-believe`

**4**  of Christ; this was the time, then, the Lord Christ was crucified,
`[?]-~Christ this exist time then Lord-~Christ crucified`

**5**  and then the Jews wiped out, down, the faith of Christ, the Jews,
`and then Jew wipe_out* down faith ~Christ Jew`

**6**  the head; and was, were, the Jews, found; and there was
`head and exist exist-Jews find* and exist`

**7**  somebody, many [far countries]; somebody, name […] Christ,
`somebody many [far_countries] somebody name [?]-~Christ`

**8**  every man suffering; in turn, a man rather, the chief | take,
`each,_every somebody suffering in_turn somebody-?but_rather head | grab`

**9**  the Jews; and then holy Stephen [cried with a loud voice]: confess the name
`Jews and then holy-Stephen [cried_with_a_loud_voice] confess name`

## 217r — they brought him to suffer

**1**  […] Christ. And then the Jews, the head, followed on this
`[?]-~Christ and then follow Jew ~head on-this`

**2**  Saint Stephen, the first martyr; and then Stephen
`Saint_Stephen the_first_martyr and then Stephen`

**3**  the Jews were brought on suffering within the Jerusalem temple,
`exist-Jews brought* on-suffering inside Jerusalem temple`

**4**  two Jews among the Jews; Stephen went […]; and this Saul
`two-Jews among-Jews Stephen go-[?] and this Saul`

**5**  to the Jews; and Saul went, because not [consenting] many; and this Saul,
`to-Jews and go Saul because not [consenting] many and this Saul`

**6**  and then Stephen was, the Jews, brought within the temple, Jerusalem,
`and then Stephen exist-Jews to-?brought inside temple Jerusalem`

**7**  because they would stone Stephen, because it is written in
`because Stephen would_say* stone-stone-this because-exist write inside`

**8**  Moses, truly, in turn [the law] among you, if a man begin
`righteous(ly) Moses in_turn [?] among you begin somebody`

**9**  to blaspheme, and a man has stones, and | among
`how? blasphemer and have somebody stone-stone-this and | among`

> Acts 6:12-13, Douay: *And they stirred up the people... and running
> together, they took him, and brought him to the council. And they set up
> false witnesses, who said: This man ceaseth not to speak words against the
> holy place and the law.* The law of Moses on blasphemy is Leviticus 24:16
> and the codex has just quoted it at 215v.

## 217v — the heavens opened

**1**  the Jews, out [out of the temple] [passing through] | and then holy Stephen knelt; and | then
`Jews out [out_of_the_temple] [passing_through] | and then kneel holy-Stephen and | then`

**2**  was praying, Stephen, to the Lord, thanks [to] the Lord God, to the Jews; and then
`exist pray-Stephen to-Lord thanks Lord_God to-Jews and then`

**3**  Stephen prayed, redeem, to the Lord, thanks [to] the Lord God; and Stephen raised
`pray ~redeem Stephen to-Lord thanks Lord_God and raise-Stephen`

**4**  Stephen's two eyes [to] heaven land, and to the Lord, thanks.
`of-Stephen two-eyes heaven land and to-Lord thanks.`

**5**  the Lord God; and this word said holy Stephen: to the Lord thanks, the Lord God, through
`Lord_God and this word say holy-Stephen to-Lord thanks Lord_God through`

**6**  offering Stephen, this Stephen, he, Stephen's soul,
`offer Stephen this-Stephen he of-Stephen soul`

**7**  within the Lord's hands. At that time, then, opened
`inside of-Lord hands time then open`

**8**  heaven; and then Stephen saw, Stephen, one king
`heaven and then-Stephen see-Stephen one king`

**9**  sitting on a throne, and [the right hand of God] an army, an army
`inside throne sit and [?] an_army army`

> Acts 7:54-55, Douay: *But he, being full of the Holy Ghost, looking up
> steadfastly to heaven, saw the glory of God, and Jesus standing on the right
> hand of God.* The lifting of the eyes is on line 3 and the sign for the
> seeing on 216r:1 was read from this very passage.

## 216r — they stopped their ears

**1**  of angels; and holy Stephen cried out; Stephen saw [looking up] | see,
`angel and shout-to holy-Stephen see-Stephen [looking_up] | see*`

**2**  the gate of heaven and earth is opened, and Stephen saw one
`gate/open heaven land and see-Stephen one`

**3**  king, crowned, sitting on a throne, and [the right hand of God]
`king crown inside throne sit and [?]`

**4**  an army, an army of angels. And then the Jews
`an_army army angel and_said Jew`

**5**  this Stephen is a blasphemer, Stephen; and
`this-Stephen-+<subject> one blasphemer-Stephen and.`

**6**  took off, the Jews, on the Jews, the Jews' clothes; and.
`take_off-Jews on-Jews of-Jews clothes^ and.`

**7**  left, the Jews, literal, the man, one son; and this son.
`leave-Jews literal man* one son and this son.`

**8**  was this Saul; and the man was [with] these clothes;
`exist this Saul and man* exist this clothes^`

**9**  and from […] want [to] stone, stone this, holy Stephen, | the first martyr
`and from [...] want stone-stone-this holy-Stephen | first_martyr`

> Acts 7:56-58, Douay: *Behold, I see the heavens opened, and the Son of man
> standing on the right hand of God. And they crying out with a loud voice,
> stopped their ears... and the witnesses laid down their garments at the feet
> of a young man, whose name was Saul.* The laying down of the garments at
> Saul's feet is on lines 6-8.

## 216v — Stephen prays for those who stone him

**1**  of the Lord God [lay not this sin]; and […] could stone Stephen, stone this;
`Lord_God [lay_not_this_sin] and [...] can Stephen stone-stone-this`

**2**  and from […] were [fell asleep] in Stephen's death; and this, spoken,
`and from [...] exist [fell_asleep] inside of-Stephen die and this speak`

**3**  written; then not Stephen […] Stephen prayed,
`write then not Stephen [...] pray-Stephen`

**4**  and Stephen, the first martyr, to the Lord, thanks [to] the Lord God;
`and Stephen first_martyr to-Lord thanks Lord_God`

**5**  […] are damned; and then Stephen was, the Jews,
`[...] exist be_damned and then Stephen exist-Jews`

**6**  out on the town, stoned [out of the temple] [passing through]; and | then
`out on-town stone [out_of_the_temple] [passing_through] and | then`

**7**  that day he was; he saw this suffering, this Saul,
`day exist see this suffering this Saul`

**8**  [a great persecution] the Jews did to holy Stephen; | the first, not,
`[a_great_persecution] do Jew on-holy-Stephen | first-not`

**9**  suffering; to the Lord thanks [to] the Lord God; and then | was
`suffering to-Lord thanks Lord_God and then | exist`

**10**  […] through startling, this Saul, and trespassing, to the place
`[...] through startle this Saul and trespass to-place`

> Acts 7:59-8:1, Douay: *And falling on his knees, he cried with a loud voice,
> saying: Lord, lay not this sin to their charge... And Saul was consenting to
> his death.* The praying is here. Saul's consent is not: this page has no
> sign for it, and at 217r:5 the sign before the restored [consenting] is
> "not". An earlier printing of this note said the consent was here; that was
> wrong.

## 219r — Saul takes letters to Damascus

**1**  and by the name of the brethren of the Lord Jesus Christ; and this
`and-brother-+name Lord-Jézus-Christ and go this`

**2**  Saul to the head of the Jews, on the town Jerusalem;
`Saul to-head Jew on-town Jerusalem`

**3**  one from this Saul, the Jews took, the head […];
`one-from this Saul grab-Jews head [...]`

**4**  they could, upon this man that believeth not, and the man who this Jesus, this
`can on-this somebody not_believe and somebody this Jézus this`

**5**  Christ, believes; and [threatenings] […], the mother, […] <subject marker> every
`Christ believe and [threatenings] [...] mother [...] SUBJ every`

**6**  capture; and somebody <subject marker> many [bound] see; and by name brother
`capture and somebody-+SUBJ many [bound] see* and-brother-+name`

**7**  of the Lord, […], every man to you, this going;
`of-Lord [...] everybody = to-you this-go-this`

**8**  and then […] was, the Jews, took a mission, many riches;
`and then [...] exist-Jews grab mission many ~rich`

**9**  and then […] [letters], many servants on the commission.
`and then [...] [letters] many servant on-mission`

> Acts 9:1-2, Douay: *And Saul, as yet breathing out threatenings and slaughter
> against the disciples of the Lord, went to the high priest, and asked of him
> letters to Damascus to the synagogues: that if he found any men and women of
> this way, he might bring them bound to Jerusalem.*

## 219v — a light from heaven

**1**  And then within | within Jerusalem one town
`and then inside | inside Jerusalem one-town`

**2**  a town there was, named Damascus, because, and
`exist-[?] town exist Damascus because and`

**3**  within that [they] believe the Lord Jesus Christ; and then went to
`inside that* believe Lord-Jesus Christ and then go to`

**4**  Saul, upon this town, many an army; and | then
`Saul on-this town many an_army and | then-exist`

**5**  the Jews, Saul, the servants, on half the way, to go, Saul, the servants,
`Jews-Saul-servant on-half way to-go-Saul-servant`

**6**  the time; and this Saul went, before […], servant,
`time and go this Saul ~before [...] servant`

**7**  and […] there was a light [shined round] from heaven and earth,
`and [...] exist light [shined_round] on-heaven land`

**8**  and […] there was a light [fell to the earth] to the heavenly; he bowed,
`and [...] exist light [fell_to_the_earth] on-+heavenly-to bow`

**9**  and the Lord God cried out upon the water: Saul, Saul,
`and shout-to Lord-<divine> on-water Saul Saul`

> Acts 9:3-4, Douay: *And as he went on his journey, it came to pass that he
> drew nigh to Damascus; and suddenly a light from heaven shined round about
> him. And falling on the ground, he heard a voice saying to him: Saul, Saul,
> why persecutest thou me?* The light, the falling and the doubled name are
> all here.

## 220r — I am Jesus of Nazareth

**1**  why? the Lord through […]; and shouted to this | Saul,
`why? Lord through [...] and shout-to this | Saul`

**2**  […] [Saul] lie; in turn the Lord [whom thou persecutest] he; and
`[...] [Saul] lie in_turn Lord [whom_thou_persecutest] he and`

**3**  shouted to the Lord God on the water: I, from Jesus of Nazareth,
`shout-to Lord_God on-water I from Jesus Nazareth`

**4**  the Lord, on the cross executed; and this Saul cried out:
`the_Lord cross execute and shout-to this Saul`

**5**  Lord, who, Saul, the Lord, did; and shouted to
`Lord who Saul Lord ~do and shout-to`

**6**  the Lord God on the water: […] into the town; from […] on learning, the man
`Lord_God on-water [...] inside town from [...] on-learn man^`

**7**  love; […] […], the time, the hour, from
`love [...] [...] time hour from`

**8**  […]; and [led him by the hand]; and […] there were
`[...] and [led_him_by_the_hand] and [...] exist`

**9**  took Saul's servant; and Saul [they] took away,
`grab of-Saul servant and Saul take_away`

> Acts 9:5-8, Douay: *Who said: Who art thou, Lord? And he: I am Jesus whom
> thou persecutest... And Saul arose from the ground; and when his eyes were
> opened, he saw nothing.* The naming and the blindness are both here.

## 220v — the house of Judas, and Ananias

**1**  Saul, servant, into the town; and Saul put, servant,
`Saul servant inside town and Saul put servant`

**2**  one man, Ananias; and a man, Ananias, was born,
`one man* Ananias* and man^ Ananias* exist ~be_born`

**3**  Gamaliel, town; and this Saul, trespass, […]
`Gamaliel town and this Saul trespass [...]`

**4**  at the birth; and […] there was this Saul, this
`on-~be_born and [...] exist this Saul this`

**5**  Ananias put Saul, the servants, into one house;
`Ananias* put <of>-Saul servant inside one house`

**6**  and […] three […], this Saul, within
`and [...] three [...] this Saul inside`

**7**  this house, this Ananias, the man; and this man's name
`this house this Ananias* somebody and this somebody [?]-~exist-+name`

**8**  was Judas; and then one man within this town
`exist Judas and then one man^ inside this town`

**9**  can, the man said, find, understand; in turn, and by name, brother, the man was
`can man^ say find-understand in_turn and-~brother-+name man^ exist`

> Acts 9:9-11, Douay: *And he was there three days, without sight... And there
> was a certain disciple at Damascus, named Ananias... Arise, and go into the
> street that is called Strait, and seek in the house of Judas, one named Saul
> of Tarsus.* The three days, Ananias and the house of Judas are all here --
> and Ananias is the name this project read from this very folio.

## 221r — a vessel to bear my name

**1**  Ananias; and Paul, from Paul; and he bowed down,
`Ananiah and Paul from-[?]-Paul and bow_down`

**2**  [hail] upon Paul [laid his hands]; and Ananias put the Lord's
`[?] on-<of>-Paul [?] and put Ananiah <of>-Lord`

**3**  name upon Paul, because from Paul, Paul is | of
`name on-Paul because from Paul exist-Paul | <of>`

**4**  the Lord's name carries Paul on all the whole world; is Paul | of
`Lord name carry Paul on-all_the_world world exist-Paul | of`

**5**  the Lord's name, confesses Paul. And then holy Ananias:
`Lord name confess Paul and_said holy-Ananiah`

**6**  Lord, how is it, from Saul, of the Lord, the name | bears
`Lord how? exist from Saul <of>-Lord [?]-~exist-+name | carry`

**7**  Saul, and Saul, of the Lord, the name, through
`Saul and Saul <subject> <of>-Lord [?]-~exist-+name through`

**8**  persecuting, Saul? And secondly the Lord God said to holy Ananias:
`persecute-Saul and two say Lord-<divine> holy-Ananiah`

**9**  go, Ananias; the Lord's servant, in truth and love, drink
`go Ananiah <of>-Lord servant inside righteous(ly)-love drink`

> Acts 9:13-15, Douay: *Lord, I have heard by many of this man, how much evil
> he hath done to thy saints in Jerusalem... And the Lord said to him: Go thy
> way; for this man is to me a vessel of election, to carry my name before the
> Gentiles.* Ananias's objection and the Lord's answer are both here, and the
> name borne into the world is on lines 3-5.

## 221v — a table of earthquakes and eclipses

**1**  Before the Spirit, on the Friday, the earth, one
`before spirit inside Friday earth one`

**2**  quake; on the Spirit, on the Wednesday, the moon eclipsed
`quake on-spirit inside Wednesday moon eclipse`

**3**  one hour; and from the year before God,
`one hour and from year before God`

**4**  on the Friday, the earth quaked, from the Spirit;
`inside Friday earth quake from spirit`

**5**  the first year from God, the first year, in turn, on the fast | three
`first year from God first year in_turn on-fast | three`

**6**  day before the Virgin Mary; within Sunday the earth
`day before Virgin_Mary inside ~Sunday earth`

**7**  quaked; and this, and the day [a sign] [shall appear] upon heaven
`quake and this and day [?] [?] on-heaven`

**8**  and earth, living, and confessing, to the letter; and a man
`land living and confess to-literal-to and somebody`

**9**  [a sign] sees [darkened] [the sun] to, within [the holy church]
`[?] see [?] [?] to inside [?]`

**10**  answered, to; in turn, two years [famine] from the Spirit [pestilence]
`°answered-to in_turn two-year [famine] from spirit [pestilence]`

> A table of portents by weekday, of the kind chronicles and almanacs carry.
> These last folios are the most damaged in the book and the least readable.

## 223r — more of the same table

**1**  the day the earth quaked, out, the first
`day <subject> earth quake out(ward) first`

**2**  Spirit, Friday; and the years and three days of God, from the Spirit, four years
`spirit Friday and years* and three_days God from spirit two-two-year`

**3**  [a wind] from the Spirit [shall come] the earth quaked, and the moon
`[?] from spirit [?] earth quake and moon`

**4**  in turn on; and the year <subject marker> half
`in_turn on and year SUBJ half`

**5**  the father, our [heaven] from [render] somebody; and
`the_father our [heaven] from [render] somebody and`

**6**  [within] in truth believing, the Lord bears the man [shall be saved]
`[?] inside righteous(ly) believe carry-Lord somebody [?]`

**7**  believeth not; and this, every one, therefore have mercy, man [shall perish]
`not_believe and this each,_every therefore-have_mercy somebody [?]`

**8**  and the man would, Christ, against, leave; the man, God, learn,
`and somebody want Christ against leave somebody God learn`

**9**  the throne [shall be fulfilled] wants somebody [shall sit], the Lord's throne [shall be saved], righteous
`throne [shall_be_fulfilled] want somebody [shall_sit] Lord-throne [shall_be_saved] righteous`

**10**  of the Lord.
`Lord-<of>`

## 223v — the date, and the age of the world

**1**  From the ascension of the Lord Jesus Christ [to] the Father of the Lord, out,
`from* ascension Lord-Jesus-Christ the_father of-Lord out`

**2**  a thousand years, five hundred and sixty years; and by name, that day,
`thousand-year five_hundred and six-ten-year and from-+name-+day`

**3**  thus, the beginning of the year, written.
`this_is begin-year write`

**4**  Four sons.
`two-two-son`

**5**  From [the beginning] then was forty days; in turn see [and then]
`from* [the_beginning] then exist forty_days in_turn see* [and_then]`

**6**  the son, Moses [five thousand one hundred and ninety nine] by name, the year, the first year,
`son Moses [...] from-+name-year first-~year`

**7**  seven, in turn, from the seeing, two years [a numeral]
`seven in_turn of-from-see two-year [a_numeral]`

**8**  from the earth until the Lord Jesus Christ was born
`from earth until be_born Lord-Jesus-Christ`

**9**  into this world, out, five thousand and a hundred years, and | ninety
`on-this world ~out five_thousand and hundred-~year and | nine-ten`

**10**  years, and nine years; and this symbolizes nine hours from the beginning of this world.
`year and nine-year and this symbolize nine ~hour from begin this world.`

**11**  until the Lord Jesus Christ was born into this world; in turn, and the hour, out,
`until be_born Lord-Jesus-Christ on-this world in_turn and ~hour ~out`

**12**  from the ascension of the Lord Jesus to the Lord's Father, heaven; in turn, brother
`from ascension Lord-Jesus to-the_father of-Lord heaven in_turn-~brother`

**13**  the time the apostles said [to] the Lord Jesus: Master, when is doomsday passing? Said
`time say apostle Lord-Jesus Master when? exist pass doomsday say`

> **Two dates, and both of them matter.** Line 9-10 gives the age of the world
> at the Nativity as five thousand, one hundred and ninety-nine -- the figure
> of the Roman Martyrology's Christmas proclamation, *anno a creatione mundi
> quinquies millesimo centesimo nonagesimo nono*. That is a liturgical
> number, and its presence here is another sign that the compiler worked from
> a missal.
>
> Lines 1-2 give a thousand five hundred and sixty years since the
> Ascension. Read as a date of composition that is the 1560s, which sits
> inside the range the manuscript's paper has always been given and close to
> the Tridentine missal and breviary of 1570 and 1568. This project does not
> claim it as the date of the book; it is what the line says, and the line is
> damaged on both sides.

## 222r — when shall the judgment day be?

**1**  [hallowed be] the name of the Lord, of the Lord's Father.
`[hallowed_be] name of-Lord of-Lord the_Father.`

**2**  In turn, out [after] two thousand years, to this,
`in_turn-[?]-~out(ward) [?] two-thousand-year to-+this_is`

**3**  the brother, of the chapter, one day; and he has
`[?]-+brother <of> chapter one day and have`

**4**  from covered, one, the judgment year; because anew, from the Son of God, judgment;
`from covered-+one judge-~year because new-from son God judge`

**5**  the dead man, the sinful man damned, the sinful man; and saved,
`die somebody sin be_damned somebody sin and be_saved`

**6**  the light, said, said the Lord Jesus; this said the Lord's apostles; there is upon a man
`light say say Lord-Jézus this say apostle <of>-Lord exist on-somebody`

**7**  one, one, girl, earth, water, sun, all [shall be shaken]
`one one girl earth water sun every [shall_be_shaken]`

**8**  the earth, the sun, Christ,
`earth sun Christ`

**9**  [amen] the Lord God.
`[?] Lord-<divine>`

> Matthew 24:3: *Tell us when shall these things be? and what shall be the
> sign of thy coming, and of the consummation of the world?*

## 222v — a calendar, with the writer's own name in it

**1**  [on the holy day] Monday, within Thursday, went somebody [of] the name of the author [I went] to the house,
`[on_the_holy_day] Monday inside Thursday go-+the_name_of_the_author-somebody [I_went] to-house`

**2**  the brother, trespassing, he carried, the writer of this book [to the Lord's house] on the Friday,
`brother-trespass carry-+the_name_of_the_author-somebody [?] inside Friday`

**3**  [and then] the writer of this book [to the Lord's house] on the Sunday he went, the writer of this book, to the seal
`[?] the_name_of_the_author-somebody [?] inside Sunday go-+the_name_of_the_author-somebody seal-to`

**4**  [I went] remitted, half year [to the Lord's house] this, out, one
`[I_went] remit half-year [to_the_Lord's_house] this out one`

**5**  holy Philip's year [on the feast of] Monday, within [a date] he took, the writer of this book,
`holy-Philip-year [on_the_feast_of] Monday inside DATE grab-+the_name_of_the_author-somebody`

**6**  until half year; in turn from half year one, in turn [reckoned]
`until half-year in_turn from* half-year one in_turn [reckoned]`

**7**  [I pray] [my sins] the Lord, have mercy; in turn [my soul] one [reckoned] in turn, in the middle,
`[?] [?] Lord have_mercy in_turn [?] one [?] in_turn in_the_middle`

**8**  the man [to the Lord's house] more than these; this said, gave […], the writer of this book [wrote]
`somebody [to_the_Lord's_house] more_than_these* this say °gave-[?] the_name_of_the_author [wrote]`

**9**  Friday [I fasted] [lunatic] the writer of this book; this, out, two; Sunday, by name,
`Friday [?] [?] the_name_of_the_author-somebody this out(ward) two Sunday name`

**10**  Sunday three, fourth <subject marker> Sunday three, the Lord | Father,
`Sunday three second-two SUBJ Sunday three Lord | father`

**11**  Son and Spirit; on the Monday there was [the Holy Spirit] conceived, to
`son-spirit inside Monday exist [?] get_conceived to`

> **Kiraly and Tokai's dictionary carries a sign they gloss as "the name of the
> author", and it stands six times on this one folio.** Whatever the compiler
> called himself, he signed his book here, in a calendar of his own days --
> where he went, what he carried, what he took. It is the only page in the
> manuscript that is about the man who made it.

## 224r — the last leaf but one

**1**  ninety-six, little, one […]
`nine-ten six little one-[?]`

**2**  Michael, on the Saturday, of the woman [the angel]
`Michael on-Saturday <of>-woman [?]`

**3**  of Mark; you took, and [wrote] and two, from two, the mother,
`of Mark ~you grab and [wrote] and two from two mother`

**4**  on the Saturday [and on] [the same week] on the Saturday,
`on-Saturday [?] [?] on-Saturday`

**5**  upon good [deed] more than these; upon a man there is, then,
`on-good [?] more_than_these* on-somebody exist then-+<subject>`

**6**  upon death, that day, upon the name [one year]
`on-die [?]-+day on-exist-~exist-+name [?]`

**7**  [on the day of] [the feast] Matthew, on the Saturday; and lo,
`[?] [?] Matthew on-Saturday and lo`

**8**  one, this is [likewise] Matthew [and on]
`one this <subject> exist [?] Matthew [?]`

**9**  [the same week] on the Saturday [likewise] [and on] [the same week]
`[?] on-Saturday [?] [?] [?]`

**10**  understanding, who [at the table] the cup by name; and from a man to this rich good [deed]
`understand-who [?] cup-+name and from somebody to this rich good [?]`

**11**  and one [and a half] three, and one [and a half] three,
`and one [?] three and one [?] three`

**12**  believe upon this [a portion] [of wine] [a portion], gave, year
`believe on-this [a_portion] [of_wine] [a_portion] °gave-year`

> The last two folios are the most damaged in the manuscript and the least
> read: 22 of the 29 unread words on 224r have no reading at all. What can be
> made out is a calendar -- Michael, Mark, Matthew, Saturdays -- of the same
> kind as 222v.

## 224v — the end of the book

**1**  the Lord Jesus Christ saved; the Lord, all the world,
`Lord-Jesus-Christ be_saved Lord all_the_world`

**2**  [I pray thee] the son, living, of
`[?] ~son living-exist <of>`

**3**  he said; and this man, upon the food, to, in turn,
`say and this somebody on-food to-on in_turn`

**4**  living, the woman, Matthew [and on] on the Saturday, within
`living woman ~Matthew [?] on-Saturday inside`

**5**  the seal [this book] Lord have mercy, you, have mercy,
`seal-chapter [?] Lord have_mercy you have_mercy`

**6**  of Christ;
`[?]-~Christ`

**7**  and through offering, you, have mercy,
`and through offer you have_mercy`

**8**  have mercy, Lord; in turn, the woman [and on] [the same week]
`have_mercy Lord in_turn woman [?] [?]`

**9**  and of [the saints] and all, from the leaving […] [the same week]
`and <of> [?] and each,_every <of>-from-leave [?] [?]`

**10**  on high; and [into heaven] there is, then, the soul from
`on high and <subject> [?] exist then-+<subject> soul from`

**11**  losing, from riches [at the last] there is [amen] [for ever] from
`lose from-rich [?] exist [?] [?] from`

**12**  the day, this why; and understanding, the man, the woman,
`day this-why? and understand somebody woman`

**13**  this world, truly, two.
`this world righteous(ly) two`

> The book ends in a prayer for mercy, twice repeated, and the last legible
> word of the manuscript is a number. **All 441 folios are now rendered into
> English.**
