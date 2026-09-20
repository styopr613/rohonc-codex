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

---

## What the book turns out to be

The opening is not a gospel. Folios 004v through 001v tell the **Life of Adam
and Eve**: the fall of Lucifer, the creation of Adam, the breath of life,
Paradise, the rib, Eve, the serpent, the fruit, the shame, and God walking in
the garden asking where Adam is. That is the apocryphal *Vita Adae et Evae*,
not Genesis, because the distinguishing episode is there — God commands the
angels to bow to Adam and Lucifer refuses, which is in the *Vita* and not in
Genesis.

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

**2**  […] […] and the earth.
`[?] [?] and ~earth`

**3**  The sun and the moon, [as] the scripture(?) [says].
`sun and moon write`

**4**  Elijah the prophet. The angel of God said:
`Elijah prophet say angel God`

**5**  […] before […] of man.
`[?] before [?] <of>-somebody`

**6**  The Father […]; man bowed down(?) before the Lord.
`from-father ~Adam bow_down Lord`

**7**  God in heaven […] and the brethren.
`God on-on-sky [?] in_turn-brother`

**8**  Many angels […]; and God the Father had many angels about him.
`many ~angel [?] and exist to-from-father God on-many angel`

**9**  Among the angels, two hundred and fifty(?) years […] before […] of man.
`on-angel two-half-hundred-year [?] before [?] <of>-somebody`

**10**  The Father, Adam, and the angels […]; there was Lucifer, and the other angels.
`from-father ~Adam and angel [?] exist hide_oneself-angel and two ~angel`

**11**  And the angels prayed, and for forty [days?] and forty nights
`and angel hide_oneself-angel pray and ten-ten-ten-ten [?day] ten-ten-ten-ten night`

**12**  […] Lucifer […] to Lucifer […] among the brethren, in hell.
`which hide_oneself-angel to hide_oneself-angel [?] on-in_turn-brother on-hell`

**13**  And again the angel said to Elijah: Elijah, when there is […]
`and two say angel to-Elijah Elijah and then-exist [?]`

**14**  Lucifer, who did [this] — Lucifer, when he was
`hide_oneself-angel who do, hide_oneself-angel then-exist`

**15**  […] seated on the throne of God the Father. God the Father went […]
`[?] sit on throne from-father God go from-father God`

> Lucifer's name is a compound: their code for "hide oneself" followed by
> their sign for angel, Satan, Lucifer. It is the code this project spent ten
> failed attempts trying to guess as a single word.

## 004r — the cup

A formula repeats six times in thirteen lines. I have kept the repetition
rather than smoothing it, because it is the shape of the page.

**1**  The angel of the Father said; God the Father; the angel said to Lucifer: because the cup was hidden away.
`angel <of>-father say from-father God angel say hide_oneself-angel because cup-to hide_oneself`

**2**  […] of the Father, on the throne […] God; the angel; Lucifer; the cup was hidden away.
`[?] <of>-father on throne [?] God angel hide_oneself-angel cup-to hide_oneself`

**3**  […] the Lord on the throne; and when the cup […] […] the cup was hidden away […]
`[?] Lord on throne and then-exist cup [?] [?] cup-to hide_oneself [?]`

**4**  And when Lucifer […], the angel returned to the Father.
`and then-exist from hide_oneself-angel return angel to-father`

**5**  […] the angel, the Lord, the cup, Lucifer […] the cup was hidden away […] and the other went.
`[?] angel Lord cup hide_oneself-angel [?] cup-to hide_oneself [?] and two go`

**6**  God the Father; the angel of the Father [spoke] to Lucifer; Lucifer said: because the cup was hidden away.
`father-<divine> <of>-father angel to-hide_oneself-angel say hide_oneself-angel because cup-to hide_oneself`

**7**  […] with the Father, on the throne; and when Lucifer went to God
`[?] on-<of>-father on throne and then-exist to-hide_oneself-angel go God`

**8**  the angel said: God; the angel; the cup was hidden away […] the Lord on the throne; and when
`angel say God angel cup-to hide_oneself [?] Lord on throne and then-exist`

**9**  the cup of Lucifer […] the cup was hidden away […] and then […] | was hidden.
`cup hide_oneself-angel [?] cup-to hide_oneself [?] and then-exist from | hide_oneself`

**10**  The angel returned, the angel, to God the Father, because there was
`angel return angel to-father God because-exist`

**11**  said Lucifer; to the Lord; hidden; the Lord God; the mother […] […] to the Lord, to the Lord, this | hidden.
`say hide_oneself-angel to-Lord hide_oneself Lord-<divine> mother [?] [?] to-Lord to-Lord this | hide_oneself`

**12**  The angel […] Lucifer, he on the throne […] God, the angel, the Lord.
`angel [?] hide_oneself-angel this on throne [?] God angel Lord`

**13**  The cup of Lucifer […] the cup was hidden away […] said Lucifer to the Lord: hidden.
`cup hide_oneself-angel [?] cup-to hide_oneself [?] say hide_oneself-angel to-Lord hide_oneself`

## 002r — Michael, the command to bow, and Lucifer's fall

**1**  The mother of the Lord God was born; and Lucifer […] to the Lord, to the Lord; Lucifer […]
`Lord-<divine> mother be_born and hide_oneself-angel to-Lord to-Lord hide_oneself-angel [?]`

**2**  Lucifer, he upon the throne […] of the Lord God […]
`hide_oneself-angel this on throne [?] Lord-<divine> <of>-Lord [?]`

**3**  There was the earth […] God the Father […] Michael.
`exist earth [?] from-father God [?] Michael`

**4**  The angels, faithful servants, rose up; and when they had risen,
`angel believe servant stand_up up and then-exist stand_up`

**5**  the heavenly ones spoke. God the Father […] went to Lucifer, and
`heavenly say from-father-<divine> [?] go to-hide_oneself-angel and`

**6**  Lucifer fell from the throne of the Lord; and when, within […]
`hide_oneself-angel bow_down on throne <of>-Lord and then-exist inside [?]`

**7**  they bowed down — and of the angels every one — to whom Lucifer [would not] bow.
`bow_down and from angel each,_every to-which hide_oneself-angel bow_down`

**8**  And then […] God the Father […], and cried out.
`and then-exist [?] from-father God [?] and shout`

**9**  God the Father […]: Lucifer departed by commandment, because all were angels
`from-father God [?] leave hide_oneself-angel commandment because each,_every exist angel`

**10**  to whom Lucifer bowed. And […] […] said God the Father, from
`to-which hide_oneself-angel bow_down and [?] [?] say from-father-<divine> from`

**11**  he departed. This was the angel. He left food(?) […], and […] said the angel
`leave this exist angel leave food [?] and [?] say angel`

**12**  to Elijah the prophet: Elijah, say(?) […] God the Father is.
`to-Elijah prophet Elijah say [?] from-father-<divine> exist`

**13**  To the Son came the Holy Spirit. Father, Son […] man […]
`to-son go holy-spirit father son [?] somebody [?]`

**14**  God the Father, the Holy Spirit — how man knows the image of the Father.
`from-father-<divine> holy-spirit on-how? somebody shape,_form know father`

> The distinguishing episode of the *Life of Adam and Eve* is on this page:
> the angels are commanded to bow, all of them do, and Lucifer will not. It is
> not in Genesis.

## 002v — the Trinity, and the making of Adam

**1**  The Son, the Spirit […] […]; the Son, in the image of the Lord.
`son spirit [?] [?] son on-<of> shape,_form on-Lord`

**2**  […] […] man is; all one; to the Father, the Son,
`[?] [?] exist somebody each,_every one to-father son`

**3**  the Spirit. Father, Son and Spirit took man, and every living thing […]
`spirit grab father son spirit somebody each,_every living [?]`

**4**  The soul heard. Adam saw the living, truly, not many |
`soul hear Adam see living righteous(ly) not many | from`

**5**  Father and Son — not many; the Holy Spirit; but this Lord is all,
`father from son not many holy-spirit a) this Lord each,_every`

**6**  one God. […] God, the angel, Elijah the prophet.
`one God [?] God angel Elijah prophet`

**7**  Elijah the prophet, when there were Father, Son and Spirit, going forth
`prophet Elijah then-exist father son spirit to-go`

**8**  […] […] and the brethren, in this world, and […] |
`table [?] in_turn-brother on-this world and [?] | to`

**9**  […] the Lord God, Adam […] […]; and then
`[?] Lord-<divine> Adam [?] [?] and then-exist`

**10**  Adam was […] as was said before […] and […] […]
`Adam ~exist [?] earlier_mentioned [?] and [?] [?]`

**11**  […] breathed into Adam, and he became living, and
`[?] breathe on-Adam and living leave and`

**12**  the Lord God took Adam, and Adam went into
`Adam grab Lord-<divine> and Adam go inside`

**13**  Paradise; and all […]. End of chapter. Adam
`Garden_of_Eden and each,_every [?] exist-chapter Adam`

> Line 11 is Genesis 2:7 — the breath, and the man becoming a living being.
> Line 5 is a Trinity formula: Father and Son, not many, one God.

## 003r — the commandment, and the sleep

**1**  […] the Lord God [and] Adam. The Lord [spoke] to Adam; he took
`[?] Lord-<divine> Adam this-Lord this-Adam grab`

**2**  every truly […] hunger, and thirst […] upon Adam; and
`each,_every righteous(ly) [?] be_hungry and thirsty [?] this-Adam and`

**3**  one living [thing] dies. There shall be sin, hunger, thirst, to him who
`one living die sin have be_hungry thirsty to-to-this-who`

**4**  […] the Lord took. To Adam, all truly one.
`[?] grab-Lord this-Adam each,_every righteous(ly) one`

**5**  […] this yoke upon Adam, by commandment: not […]
`[?] this yoke this-Adam through commandment not [?]`

**6**  this […] […] […] […] Adam is […]
`this [?] [?] [?] [?] Adam exist [?]`

**7**  […] Adam would die. And then Adam slept within |
`[?] die-Adam and then-exist Adam sleep inside | to`

**8**  […] and then upon him […] first, from […] and | when
`[?] and then-exist on-this [?] ~first from [?] and | then`

**9**  the Holy Spirit came within […] […] this
`exist go holy-spirit inside [?] [?] this`

**10**  […] this […] and the Lord God took Adam
`[?] this [?] and grab Lord-<divine> Adam`

**11**  […] and […] […] said the angel to you:
`[?] and [?] [?] say angel you`

**12**  mother. And then Adam, from […] […] this |
`mother and then-exist Adam from [?] [?] this | to`

## 003v — the rib, Eve, and the serpent

**1**  Bone of bone; and the two souls are one. | Before
`bone bone in_turn two soul one | before`

**2**  […] and […] said the angel. The Lord God departed […] | Chapter.
`[?] and [?] say angel leave Lord-<divine> [?] | in_turn-chapter`

**3**  […] and Eve went into Paradise; and | when
`[?] and go Eve on-Garden_of_Eden and | then`

**4**  Eve came to that tree which […]
`exist Eve go to-this tree what [?]`

**5**  the Lord God had by commandment [forbidden]; and she saw a
`exist Lord-<divine> through commandment and see one`

**6**  serpent in that tree, which […] was
`serpent on-this tree what [?] exist`

**7**  the Lord God's by commandment […] this serpent […]
`Lord-<divine> through commandment [?] this serpent [?]`

**8**  […] this fruit […] Eve […] ate,
`[?] this fruit [?] Eve [?] eat`

**9**  because […] Adam, the Master, by commandment […]
`because [?] Adam Master through commandment [?]`

**10**  this serpent. Eve ate […] Adam
`this serpent Eve eat [?] Adam`

**11**  […] this fruit; and the fruit […] was […]
`[?] this fruit in_turn fruit [?] exist [?]`

**12**  […] Adam ate; and […] Adam knew
`[?] Adam eat exist [?] Adam know`

## 001r — good and evil, shame, and back to Elijah

**1**  evil and good, as the Lord God knows. And then they plucked,
`evil and good how?-to Lord-God know and then-exist pluck`

**2**  the serpent, this fruit, this serpent; and | Chapter.
`serpent this fruit this serpent and | then-chapter`

**3**  […] took […] and […] took the fruit.
`[?] grab [?] in_turn [?] fruit grab`

**4**  Adam. And then […] the two of them, Adam, [were] naked.
`Adam and then-exist [?] on-two Adam naked`

**5**  […] saw Adam; and then […] Adam
`see [?] Adam and then-exist [?] Adam`

**6**  was ashamed. And [chapter] six: the angel of God said to Elijah […]
`be_ashamed_of_sg and six say God angel to-Elijah [?]`

**7**  Elijah; and this […] […] Lucifer,
`Elijah and this [?] [?] hide_oneself-angel`

**8**  the Father […] […] Lucifer had fallen | Father
`from-father [?] [?] hide_oneself-angel exist bow_down | father`

**9**  God […] and the brethren […] and […] said
`<divine> [?] in_turn-brother [?] and [?] say`

**10**  the angel of God to Elijah the prophet: Elijah, the Lord God departed
`God angel to-Elijah prophet Elijah leave Lord-<divine>`

**11**  […] […] within Paradise, saying
`[?] [?] inside Garden_of_Eden say`

## 001v — where art thou

**1**  The Lord God, with the angels, came out(?) […] and then departed.
`Lord-<divine> on-angel this ~out(ward) two from [?] and then-exist leave`

**2**  The Lord God […] within […] […] the Lord God.
`Lord-<divine> [?] inside [?] [?] Lord-<divine> <divine>`

**3**  […] Where [art thou]? […] Adam […] the Lord God.
`[?] why? [?] ~Adam [?] Lord-<divine>`

**4**  […] The Lord God [spoke] with his own mouth. Adam hid himself […] Adam,
`[?] Lord-<divine> who-mouth ~Adam hide_oneself [?] ~Adam`

**5**  who […] […]. Said the Lord God: Where art thou, Adam?
`who [?] [?] say Lord-<divine> why? ~Adam`

**6**  […] […] Eve [gave?] […] ate […]
`[?] [?] Eve [?] food [?]`

**7**  The Lord God […] heavenly […] […] Eve, to the Lord,
`Lord-<divine> [?] heavenly [?] [?] Eve this-Lord-to`

**8**  […] the Lord God: Why, Eve? […] Eve […]
`[?] Lord-<divine> why? Eve [?] who Eve [?]`

**9**  […] the Lord God: Why, Eve? […] […] […]
`[?] Lord-<divine> why? Eve [?] [?] [?]`

**10**  The serpent […] ate […] the Lord God, Adam
`serpent [?] food [?] Lord-<divine> ~Adam`

**11**  one commandment: this Adam […] did not keep(?) the commandment.
`to-one commandment this ~Adam [?] commandment ~carry`

> Genesis 3:9, "Where art thou?", and 3:13, "What is this that thou hast
> done?" — here as a repeated *Why, Eve?*

## 137v — a prayer to the Virgin, with the author's colophon

This is the page Király and Tokai published a reading of, so it is the one
place the work can be scored against theirs. Their published line is line 3,
and it matches.

**1**  Hail, O Virgin. Through holy Mary, mother of God, […] […]
`healing-girl through holy-Mary mother God [?] [?]`

**2**  Queen Mary, […] Lady […] […] | thou
`king-Mary [?] wife [?] [?] | this`

**3**  Mary, the one and only virgin maiden — thou, Mary, didst conceive Jesus without [sin].
`Mary one only_one virgin-girl this-Mary ~get_conceived Jézus without [?sin]`

**4**  Born of Mary […]; and from the Lord the Redeemer, in the Lord | I, [author],
`be_born-Mary [?] and from Lord-redeemer inside Lord | this-<author>`

**5**  we do not doubt, [author]; we […] | I, [author],
`somebody do_not_doubt-<author>-somebody [?] | this-<author>`

**6**  we pray to thee, Mary, […] | of [author],
`somebody this-Mary pray [?] | <of>-<author>`

**7**  that when there is […], our soul may be forgiven | of [author],
`somebody then-exist [?] soul remit | <of>-<author>`

**8**  we […]. End of chapter. Amen. This prayer must be [said].
`somebody exist-exist-chapter amen this pray have`

**9**  […] have mercy. Hail Mary. […] have mercy […] | Lord
`[?] have_mercy healing Mary [?] have_mercy [?] | Lord`

> Király and Tokai's published reading of line 3 is *sin, without, Jesus,
> conceive, you-Mary*. That is the same line, in their order.
>
> The right-hand margin is a colophon: the author's own name sign repeated
> down the side of the page, once with "I" and twice with the genitive. The
> codex does not inflect, so a name sign standing where a pronoun would stand
> is how it says "I".

---

## 007r — the curse, and the sword at the gate

**1**  Adam was, to him who […] and why […]
`exist ~Adam to-to-this-who [?] in_turn why?-in_turn`

**2**  […] Adam was of the earth […]
`[?] exist ~Adam earth [?]`

**3**  he would […] eat, and take, and […] […]
`want [?] food ~grab in_turn [?] [?]`

**4**  it was through […]; and […] was painful.
`exist through [?] and [?] exist painful`

**5**  […] shall be; and this evil — this evil is
`[?] have in_turn this evil this-evil exist`

**6**  […] the earth […] and […]
`[?] earth [?] ~and [?]`

**7**  evil. Man was made, all of this. The serpent dies; and
`evil this somebody create each,_every this serpent die and`

**8**  he departed from among […] the Lord God; and there went
`leave among [?] Lord-<divine> and go`

**9**  the Lord God, the angel […] fire,
`Lord-<divine> angel [?] fire`

**10**  a sword; and […] out | within
`sword and [?] out(ward) | on-inside`

**11**  Paradise. He drove them out, and set an angel […]
`Garden_of_Eden exorcise and put angel [?]`

> Genesis 3:24 — the angel and the flaming sword set at the gate.

## 007v — outside the garden: Cain, Abel, Seth, and Adam goes blind

**1**  […] […] Paradise; and one created
`[?] [?] Garden_of_Eden and one create`

**2**  […] within Paradise; but the angel […] the Lord God
`[?] inside Garden_of_Eden a) angel [?] Lord-<divine>`

**3**  with the angel […] from […] and from eight(?) said |
`on-angel this table [?] from [?] and from two-two-two-two say | to`

**4**  Elijah. The angel of God: Elijah, when the Lord God [drove] Adam
`Elijah God angel Elijah then-exist Lord-<divine> ~Adam`

**5**  out […] from Paradise; and then |
`out(ward) [?] on-Garden_of_Eden and then-exist | [?]`

**6**  […] he dwelt in the field many years; and Adam had […]
`[?] leave inside ~field many year and ~have ~Adam [?]`

**7**  offspring, these two sons. And the firstborn was Cain, and the second […] was
`descendant this-two to-son and firstborn exist Cain and two [?] exist`

**8**  Abel. […] […] was Seth. And then
`Abel [?] [?] exist Seth and then-exist`

**9**  Adam was blind in both eyes; and then Adam went into […]
`~Adam from eye-eye blind and then-exist go ~Adam inside [?]`

**10**  the son […]; and this son was […] the son […]
`son [?] and this son exist [?] son [?]`

**11**  Adam. And then Adam said: bring Adam from […]
`~Adam and then-exist say ~Adam carry ~Adam from [?]`

## 006r — Seth goes to Paradise for the branch

**1**  a branch. And then the branch […] carry […] through
`one ~branch and then-exist branch [?] carry [?] through`

**2**  the light; and then by that light […], through the eye, blind Adam sees;
`~light and then-exist through ~light [?] through eye see blind ~Adam`

**3**  and Adam was made whole […]. And then Seth went |
`and healing leave ~Adam [?] and then-exist Seth go | [?]`

**4**  […] to Paradise; and […] to Seth appeared God's
`[?] Garden_of_Eden and [?] Seth appear God`

**5**  angel […] the angel of God [to] Seth […]; and he went […] Seth said:
`angel [?] God angel Seth [?] and go [?] say Seth`

**6**  Adam my father. Seth […] went into Paradise | when
`from-father ~Adam Seth [?] go inside Garden_of_Eden | then`

**7**  it was Adam his father. Seth brought from […] a branch.
`exist father ~Adam carry Seth from [?] branch`

**8**  […] […] Adam his father was, through sin; and Adam said,
`[?] [?] exist father ~Adam through sin and say ~Adam`

**9**  Adam, when […] Seth brought […] through
`~Adam then-exist [?] carry Seth [?] through`

**10**  the light; and then by that light […], through the eye, the blind man sees;
`~light and then-exist through ~light [?] through eye see blind ~and`

**11**  and Adam was made whole […]. The angel truly […] spoke; and then
`healing leave ~Adam [?] angel righteous(ly) [?] speak and then-exist`

**12**  the angel went into Paradise, and Seth carried the branch
`go angel inside Garden_of_Eden and Seth carry branch`

> This is the Legend of the Rood, in the *Life of Adam and Eve*: blind, dying
> Adam sends Seth back to Paradise, and Seth returns with a branch. The codex
> tells it twice over, lines 1–3 and 9–12, in nearly the same words.

## 006v — the branch brought home, and a city

**1**  out of Paradise, from […] […] Adam was, through
`on-Garden_of_Eden from [?] [?] exist ~Adam through`

**2**  sin. And then […] the angel gave(?) this branch;
`sin and then-exist [?] ~exist ~grab angel this branch`

**3**  and then the branch […] he carried […] to his father
`and then-exist branch [?] carry [?] father`

**4**  Adam. And then […] he went into a city,
`~Adam and then-exist [?] go inside one town`

**5**  and […] the city was […] where Adam was,
`and [?] town exist [?] who exist ~Adam`

**6**  a house. And then he came […] […]; and within, all from
`house and then-exist arrive can [?] [?] and inside each,_every from`

**7**  the city […] […]; and […] out of the city
`town can [?] [?] and [?] out(ward) town`

**8**  one […]; and then Seth went, this […]
`one [?] and then-exist Seth exist go this [?]`

**9**  and within […] […]; and then Seth said, one
`and inside can [?] [?] and then-exist Seth say one`

**10**  […] […] […] the Father, the Spirit, the Father […] […]
`[?] [?] [?] from-father spirit father [?] [?]`

**11**  Adam. And Adam was blind in both eyes — Adam, who was the Lord
`~Adam and ~Adam exist eye-eye blind who ~Adam exist Lord`

**12**  God's, [driven] out of Paradise by the angel; and then […]
`God out(ward) [?] on-Garden_of_Eden on-angel and then-exist [?]`

**13**  […] the gospel, and they found […] years(?); and
`from-see gospel and find [?] ten-two-two-ten-year and`

## 008r — Noah and the ark

**1**  […] And then […] at that time the Lord God appeared to Noah;
`[?] and then-exist [?] time appear Lord-<divine> Noah`

**2**  and then […] the Lord God. Noah. The Lord grieved […] man […]
`and then-exist [?] Lord-<divine> Noah sad(ly)-Lord year [?] somebody on-<of> [?]`

**3**  that he had made them, because […] he who keeps his commandment. The Lord God would have all
`create because [?] this who carry <of> commandment ~exist Lord-<divine> want each,_every`

**4**  destroyed. […] The Lord God [said to] Noah: make one […] the Lord |
`destroy [?] Lord-<divine> Noah do, one exist Lord | [?]`

**5**  […] the Lord. It was forty(?) cubits long, and […]
`~exist Lord exist on-two-two-ten cubit long in_turn [?]`

**6**  broad; and […] lift up […] take […] of every creature two by two; and
`broad in_turn [?] lift_up [?] grab [?] each,_every create two-<distributive>-two and`

**7**  […] of the ark. And then this […] the Lord […] the Lord went;
`[?] <of>-ark and then-exist this [?] this-Lord [?] go-Lord`

**8**  and then […] he took of every creature two by two, and went before the Lord God;
`and then-exist [?] grab each,_every create two-<distributive>-two and go before Lord-<divine>`

**9**  and […] the Lord God, to the cup, and to the Lord […] and […]
`and [?] Lord-<divine> to-cup and to-Lord [?] and [?]`

**10**  the Lord God; all, two by two, [in every] direction […]
`Lord-<divine> each,_every two-two direction [?] [?] [?] [?] [?]`

**11**  and the rain came for forty days; and […] the cities were destroyed.
`and go rain two-two-ten-year and [?] town destroy`

**12**  The Lord God […]. The angel of God said [to] Elijah: the Lord God was [with] Noah;
`Lord-<divine> [?] God angel Elijah say exist Lord-<divine> Noah`

**13**  […] […] all this […] was; and the other […] departed; and this
`[?] [?] each,_every this [?] exist and two [?] leave and this`

## 008v — from Noah to Abraham

**1**  the people were, until Abraham the forefather […] believed.
`people exist until Abraham forefather [?] believe`

**2**  From Noah it was, until Abraham […] […]
`from Noah exist until Abraham [?] [?]`

**3**  The angel of God to Elijah the prophet: Elijah, within this and that
`God angel to-Elijah prophet Elijah inside this-and-this`

**4**  believe. One man was saved in that time.
`believe one somebody ~be_saved inside time`

**5**  The angel departed from before Elijah the prophet; and this and that he said.
`leave angel before Elijah prophet and this-and-this say`

**6**  […] Elijah the prophet wrote; and […] […]
`[?] write Elijah prophet and [?] [?]`

**7**  within […] chapter […] of the writing.
`inside [?] chapter [?] <of>-write`

## 005r — Abraham and Isaac

**1**  […] and the son went [with] the father |
`[?] and go-son-father | [?]`

**2**  the father; and a sheep, and a lamb.
`father and one sheep and one lamb`

**3**  […] the son; the father sacrificed […]; the father Abraham,
`[?] son father sacrifice [?] father Abraham`

**4**  for love of the Lord, […] the Lord God, the offering. Chapter. And then Isaac
`from love Lord to-hide_oneself-Lord Lord-<divine> offering-chapter and then-exist Isaac`

**5**  was […] […] who was […] Isaac […]
`exist [?] [?] who exist [?] Isaac [?]`

**6**  […] Abraham sacrificed, and drew out […]
`[?] Abraham sacrifice and take_out [?]`

**7**  […] […] […] Isaac he would slay;
`understand-girl-chapter [?] [?] Isaac want slay`

**8**  and the Lord God cried out from the cloud, by the angel of the Lord God,
`and shout Lord-<divine> on-cloud on-angel <of>-Lord-<divine>`

**9**  […] to Abraham […] […] who […]
`leave-leave Abraham-to [?] [?] who [?]`

**10**  Abraham. The Lord God. Love the Lord.
`Abraham Lord-<divine> love Lord`

**11**  […] peace to the Lord.
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

**1**  And then he sacrificed the lamb […]; the Lord God from the cloud,
`and then-exist from lamb sacrifice [?] Lord-<divine> on-cloud`

**2**  by the angel of the Lord, said to Abraham […] within […]
`on-angel <of>-Lord Abraham say [?] inside <of> understand-girl-chapter`

**3**  A holy [Virgin]; of a virgin shall be born a son […]
`one holy-<Virgin_Mary> from virgin-<Virgin_Mary> on-be_born son [?]`

**4**  The son shall be […] Jesus; and the Lord went […]
`son exist [?] Jézus and go Lord [?]`

**5**  He preached the gospel, [did] many miracles […]
`exist gospel preach many who-and-this-and miracle [?]`

**6**  and the Lord suffered […]; and […] rose from the dead.
`and suffer Lord [?] and [?] from die stand_up-Lord`

**7**  […] the Lord God, by the angel, [to] Abraham; and […] the Lord's chapter is
`[?] Lord-<divine> on-angel Abraham and from-and-see chapter-Lord exist`

**8**  believe truly [in] the Son of the living God; every man is saved […]
`believe righteous(ly) son living God each,_every somebody be_saved [?]`

**9**  One man […]; but every man is saved [from] the yoke; and
`one somebody [?] a) each,_every somebody be_saved yoke and`

**10**  man […] the Lord […] believes; and one […] […]
`somebody Lord [?] believe and one [?] [?]`

**11**  but every man was damned, from Adam […] until Abraham,
`a) each,_every somebody be_damned from ~Adam [?] table until Abraham`

**12**  a hundred years and twenty years; from Abraham […] […]
`one hundred-year and ten-ten-year from Abraham [?] table [?]`

**13**  Moses began: three thousand and fifty from Abraham until
`+Moses ~begin-+three_thousand and +fifty from Abraham until`

> Line 13 first read as three blanks. The numerals are five strokes and a
> thousand sign, five strokes and a ten sign, read by Király & Tokai's rule
> that the sign after a group of strokes multiplies it (2026-09-20).

> The angel gives Abraham the whole gospel in advance: a virgin's son named
> Jesus, who preaches, works miracles, suffers, and rises. Then the book
> starts counting years between the patriarchs, which is what a world
> chronicle does.

---

## 015r — David the king

**1**  […] David the king humbled himself before […]
`[?] David king humble against [?]`

**2**  The king began his repentance […] […] the king […]
`repentance begin king [?] [?] king [?]`

**3**  have mercy; and the king's sin — have mercy. At that time there appeared to the king
`have_mercy and sin king have_mercy time appear king`

**4**  the angel of God […]; the angel of God [to] David the king: the Lord God.
`God angel [?] God angel David king Lord-<divine>`

**5**  The king […] sin, have mercy. The king keeps the Lord's commandment; and
`king [?] sin have_mercy carry-king <of>-Lord commandment and`

**6**  the Lord confirmed the king […] upon the king's throne; and the king proclaimed [it to] the people. Chapter.
`confirm-Lord king [?] on-<of>-king throne and announce king people-chapter`

**7**  […] there shall be born […] a son […]; the son shall be the Son
`[?] on-be_born host [?] son [?] son exist son`

**8**  of God. And the angel departed from before David […]
`God and leave angel before David [?]`

**9**  From David the king until the Virgin Mary […]
`from David king until virgin-Mary [?]`

**10**  […] and […] and one […]
`[?] and [?] and one [?]`

**11**  […] […] and one […] | six(?)
`~out(ward) [?] and one [?] | two-two-two`

**12**  […] and […] from David the king until the Virgin Mary
`[?] and [?] from David king until virgin-Mary`

## 015v — the count of years

**1**  the birthday: from Adam onward until the Virgin Mary | was born,
`be_born-+day from +Adam ?onward ~out(ward) until virgin-Mary | be_born`

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

**1**  Saint Luke writes; the sixth(?) […] of his writing; from […] […]
`write holy-Luke six-throne <of>-write from [?] [?]`

**2**  […] […] they gave thanks, and prayed to the Lord God.
`[?] [?] thanks grab and pray to-Lord-<divine>`

## 016v — Joachim's offering is refused

**1**  And Saint Anne […]; of the two of them, all their rich substance […] […]
`and holy-Anne [?] from-two from_the_two_of_them each,_every <of>-rich soul [?] [?]`

**2**  one portion they took […]; and a second portion
`one division grab [?] on-exist-chapter in_turn-two division`

**3**  to the Lord […] to the people. […] a portion […] […]
`from-Lord [?] people-chapter [?] division [?] [?]`

**4**  And all Joachim's household gave thanks to the Lord God; and […] |
`and each,_every Saint_Joachim_and_his_houseful thanks to-thanks Lord-<divine> in_turn [?] | [?]`

**5**  […] […] thirty years; and he prepared the offering.
`[?] [?] thirty year and prepare offering-chapter`

**6**  […] all […] […]; and then, and from Joachim
`exist-chapter each,_every [?] [?] and then-exist and from Joachim`

**7**  he brought his offering; and at Joachim looked the chief
`carry <of> offering and to-Joachim see from head`

**8**  of the Jews. […] This chief of the Jews [said to] Saint Joachim,
`Jew(ish) [?] this head Jew(ish) holy-Joachim`

**9**  […] to this Joachim […] who was […] go
`food this-Joachim [?] who-exist [?] go`

**10**  among the […] […] of the offering […] one […]
`among <of> [?] food <of> offering [?] one [?]`

**11**  and […] […] […] at this. And sorrowfully
`and [?] [?] [?] on-this exist-chapter and sad(ly)`

**12**  Joachim departed, and went into the field, into the wilderness […]
`Joachim leave and go inside field inside forest chapter-<of> from love-exist-to`

**13**  and from […] […] and at one […] one
`and from [?] love-exist-to and on-one [?] one`

> The Protevangelium and the Golden Legend: Joachim divides his substance in
> portions, the high priest refuses his offering because he is childless, and
> he goes off into the wilderness.

## 017r — the angel comes to Joachim

**1**  a lamb […]; and then the lamb […] […]
`lamb [?] and then-exist lamb [?] [?]`

**2**  At that time, when Joachim was […] God […]
`time then-exist Joachim exist [?] God [?]`

**3**  […] the angel of God [to] Joachim […] hear […]
`[?] God angel Joachim [?] hear [?]`

**4**  […] […] the angel of God [to] Joachim, this […]
`[?] [?] God angel Joachim this [?]`

**5**  The Lord God has had mercy. Go home, Joachim; and at the golden
`Lord-<divine> have_mercy go Joachim to-home and on-golden`

**6**  gate — this Joachim departed — Joachim's wife Anne, and […]
`gate this Joachim leave <of>-Joachim wife Anne and [?]`

**7**  a virgin maiden. And then […] and […]
`one virgin-girl and then-exist [?] and [?]`

**8**  The virgin maiden shall be Mary; and Mary shall bear a son […]
`virgin-girl exist Mary and remit Mary on-be_born son [?]`

**9**  The son shall be […] Jesus; and the Lord went […]
`son exist [?] Jézus and go-Lord [?]`

**10**  He preached the gospel, did many miracles, and suffered,
`exist gospel preach many who-and-this-and miracle do, and suffer`

**11**  the Lord […]; and […] rose from the dead; and […] shall be saved,
`Lord [?] and [?] from die stand_up-Lord and [?] be_saved`

**12**  every […] […]; and the man who believes in the Lord. And the angel departed
`each,_every [?] [?] and somebody Lord exist believe and leave angel`

**13**  from before Saint Joachim; and at that time the angel […]
`before holy-Joachim and time then-exist angel [?]`

## 017v — the golden gate, and Mary carried nine months

**1**  the angel of God [to] Saint Anne: […] this Anne, […] the Lord God has had mercy, has heard
`God angel holy-Anne have this Anne [?] Lord-<divine> have_mercy hear`

**2**  the Lord God, Anne's […]. Go home, Anne; and
`Lord-<divine> <of>-Anne [?] go Anne to home and`

**3**  at the golden gate Anne came to(?) the Lord's Joachim; and there was conceived a
`on-golden gate leave Anne <of>-Lord Joachim and from-get_conceived one`

**4**  virgin maiden. And then was born in the body the virgin maiden — she is Mary;
`virgin-girl and then-exist be_born body virgin-girl exist Mary`

**5**  and Mary shall bear a son […]; the son shall be, in the body,
`and remit Mary be_born son [?] son exist and-body`

**6**  Jesus; and the Lord went […]; he preached the gospel, [did] many
`Jézus and go Lord [?] exist gospel preach many who-and-this-and`

**7**  miracles; and the Lord suffered […]; and […] from death
`miracle do, and suffer Lord [?] and [?] from die`

**8**  the Lord rose; and […] is saved, every […] […]; and the man who is the Lord's
`stand_up-Lord and [?] be_saved each,_every [?] [?] and somebody Lord exist`

**9**  […]. And the angel departed from before Saint Anne; and there was conceived the blessed
`[?] and leave ~angel before holy-Anne and from-get_conceived happy`

**10**  Virgin Mary. And Mary carried the child nine months, and in the tenth the child was born; and this
`virgin-Mary and from Mary foetus carry nine moon in_turn ten foetus be_born and this`

**11**  […] two months; and […] […]; and at six years
`out(ward) two moon and on-out(ward) [?] and on-six-year-to`

**12**  from Adam onward until the Virgin Mary was conceived and born:
`~out(ward) from +Adam ?onward until virgin-Mary get_conceived and on-be_born.`

**13**  five thousand and one hundred and fifty and
`+five_thousand and one hundred and +fifty and`

> Lines 12 and 13 first read as blanks; the same Adam-to-Mary count as 015v
> (2026-09-20).

> The meeting at the Golden Gate, and the conception of Mary. Line 10 is the
> kind of detail no paraphrase invents: nine months carried, born in the tenth.

## 018r — Gabriel: Hail, full of grace

**1**  […] months, until the offering […] the blessed Virgin Mary.
`[?] moon until offering inside chapter-year-chapter happy virgin-Mary`

**2**  And then Mary was within […]; from the beginning she withdrew(?) into […]
`and then-exist Mary exist inside [?] from begin go-hide_oneself-this inside exist-chapter`

**3**  […] and said […] that Mary would keep her virginity |
`[?] and say [?] this-Mary want virgin-carry | <of>`

**4**  Mary […]. O! O! Amen. And then Mary
`Mary [?] chapter-oh chapter-oh amen and then-exist Mary`

**5**  was […] […] and […]; and at that time
`exist six-six [?] and [?] and time from-gate`

**6**  God the Father in heaven, because he saw […] all […] darkness […]
`from-father-<divine> heaven because see hide_oneself each,_every [?] darkness [?]`

**7**  and at that time God the Father in heaven, and […]
`and time from-gate from-father-<divine> heaven and [?]`

**8**  the Lord's angel Gabriel […] to the blessed […]
`<of>-Lord angel Gabriel inside exist-chapter to-happy [?]`

**9**  Saint Luke writes […] in his writing: at that time the angel said,
`write holy-Luke [?] <of>-write time say angel`

**10**  Gabriel: Hail, thou virgin, maiden full of grace! The Lord God is with Mary […]
`Gabriel healing this-virgin-girl have_mercy-girl out(ward) Lord-<divine>-Mary [?]`

**11**  This virgin maiden: How shall this be? […] this maiden […] this maiden
`this virgin-girl how? this [?] can this-girl [?] this-girl`

**12**  […] this maiden would keep her virginity […]
`[?] this-girl want virgin-girl carry <of>-girl [?]`

**13**  O! O! Amen. […] the angel Gabriel [to] Mary:
`chapter-oh chapter-oh amen [?] angel Gabriel Mary`

> Luke 1:28 and 1:34, in order, and the codex names Luke as its source two
> lines earlier.

## 018v — the Holy Spirit, and Elizabeth six months gone

**1**  […] the Holy Spirit shall come upon thee, and grace to all […]
`have want to-girl this go holy-spirit to-each,_every have_mercy [?]`

**2**  This maiden shall conceive a son; and the son […] shall be […]
`this-girl get_conceived son and ~son [?] exist [?]`

**3**  […] the Virgin Mary […] […] said this; and […] would from […]
`[?] virgin-Mary [?] [?] this say and [?] want from [?]`

**4**  this […] […] the Lord, this […]; and then the maiden […]
`this [?] [?] Lord this [?] ~and then-exist girl [?]`

**5**  the Virgin Mary; the word of command to the Lord; Mary […] this […] which maiden
`virgin-Mary commandment word to-Lord-hide_oneself Mary hide_oneself this [?] who girl`

**6**  the angel said; at this he said […] God the Father, the Virgin Mary | the Holy
`exist angel say on-this say [?] father-<divine> virgin-Mary | holy`

**7**  Spirit; and to the Lord […] […] the Lord Jesus Christ came; the Lord was conceived,
`spirit in_turn to-Lord [?] [?] go Lord-Jézus-Christ from-get_conceived Lord`

**8**  Christ. And then […] the Virgin Mary […] the angel Gabriel
`Christ and then-exist [?] virgin-Mary [?] angel Gabriel`

**9**  [to] Mary: Behold, thy kinswoman is six months gone |
`Mary have lo out(ward) six moon <of>-girl relative | [?]`

**10**  […] who conceived […] Mary; the son, Saint John […] within the chapter […]
`[?] who get_conceived Mary son holy-John [?] inside chapter [?]`

**11**  […] chapter; the Lord God's mercy to this […]; from John shall be the way
`go chapter Lord-<divine> <of> have_mercy to-this have from John exist way`

**12**  made [for] the Lord Jesus Christ, that is the Lord […] this
`do, Lord-Jézus-Christ that_is Lord [?] this`

**13**  Mary bore; and the Lord went forth […]; he preached the gospel
`Mary be_born and from Lord go Lord [?] exist gospel preach`

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

**1**  […] many miracles […]; and the Lord suffered [under] the Jews
`who-and-this-and miracle [?] and suffer Lord Jew(ish)`

**2**  […]; and the man who is the Lord's […] truly
`[?] and somebody to-Lord exist [?] to righteous(ly)`

**3**  the Son of the living God — every man […]; and one man
`son living God each,_every somebody [?] and one somebody`

**4**  is damned; and the Lord […] […]; and one
`be_damned to and Lord [?] [?] and one to`

**5**  […] but […] a man is damned. Here ends this holy gospel.
`[?] a) [?] somebody be_damned end this holy-gospel`

**6**  And at that time the angel was […]; the angel of God
`and time then-exist angel exist [?] God angel`

**7**  the aged […] […] the angel of God […]
`very_old [?] [?] God angel [?]`

**8**  Joseph. Go, aged one […]
`Joseph go very_old [?]`

**9**  within […] […] to Mary; and this […]
`inside exist-chapter [?] to-to Mary and this [?]`

**10**  Joseph was […] aged […]
`Joseph exist [?] very_old [?]`

**11**  of the son, well-pleasing, from Mary […]; and then the son shall be born
`from son to-pleasing from Mary [?] and then-exist ~son on-be_born`

**12**  […]; the son shall be Jesus; and the Lord went forth […]; he
`[?] ~son exist Jézus and from Lord go [?] exist`

**13**  preached the gospel […], did many miracles, and the Lord suffered […]
`gospel [?] who-and-this-and miracle do, and suffer Lord [?]`

> "The aged" is Joseph's standing epithet all through these pages, which is
> how medieval art paints him.

## 019v — the census of Augustus

**1**  [under] the Jews […]; and the man who believes in the Lord […]
`Jew(ish) [?] and somebody to-Lord exist ~believe [?]`

**2**  truly the Son of the living God — every man is saved; and one
`righteous(ly) son living God each,_every somebody be_saved and one`

**3**  man is damned; and the Lord […] believes; and one
`somebody be_damned to and Lord [?] believe and one`

**4**  […] but […] a man is damned. Here ends this holy gospel.
`to [?] a) [?] somebody be_damned end this holy-gospel`

**5**  And then the blessed Virgin Mary was sixteen years old […]
`and then-exist out(ward) happy virgin-Mary ten-six-year [?]`

**6**  There was a decree, before […] the Lord Jesus Christ, twenty and | two
`exist commandment before [?] Lord-Jézus-Christ ten-ten and | two`

**7**  years; and […] one year [before] the Lord Jesus Christ […]
`two-year and [?] one year Lord-Jézus-Christ [?]`

**8**  At that time Augustus the emperor commanded that
`time command Augustus emperor because`

**9**  all […] should be counted. And then […] Augustus
`each,_every [?] exist make_census and then-exist [?] Augustus`

**10**  […] all […] went back […] and | when
`[?] each,_every [?] back go [?] in_turn-chapter-in_turn and | then`

**11**  it was, the two of them, Mary and aged Joseph, went |
`exist and from two Mary very_old Joseph go | to`

**12**  […] And then the two, Mary and aged Joseph,
`[?] and then-exist two Mary very_old Joseph`

**13**  took one ox and one
`exist grab one ox and one`

> Luke 2:1, the decree that all the world should be taxed.

## 020r — no room, and a manger

**1**  donkey; because this they took, aged Joseph
`donkey because this exist grab very_old Joseph`

**2**  the ox, the two of them — aged Joseph and Mary
`from ox who two very_old Joseph Mary`

**3**  […] […] […] the two of them, the aged […]
`[?] [?] [?] who two very_old [?]`

**4**  […] and the donkey was aged Joseph's;
`[?] exist in_turn donkey exist very_old Joseph`

**5**  he took her who would bear this son | Mary and aged
`grab who this son on-be_born want | very_old-Mary`

**6**  Joseph carried her on the donkey; and then […]
`Joseph on-donkey from-carry and then-exist [?]`

**7**  aged Joseph, when he arrived | the aged
`very_old Joseph exist from arrive | very_old`

**8**  Mary and Joseph, [at] Bethlehem town; and […]
`Mary-Joseph Bethlehem town and [?]`

**9**  […] Mary and aged Joseph […] found
`can very_old-Mary-Joseph [?] find`

**10**  none; but the two of them, Mary and aged Joseph, lodged in a
`a) leave two very_old-Mary-Joseph inside one`

**11**  barn; and […] […]
`barn and [?] [?]`

**12**  a manger; and then bought […]
`one manger and then-exist buy [?]`

**13**  Joseph hay; and then the ox
`Joseph hay and then two ox`

> Luke 2:7 — no room, and the manger. The ox and the ass are not in Luke.
> They come from Isaiah by way of the Nativity plays.

## 020v — the birth, the star, and the angel's news

**1**  and the donkey; he laid the hay; and then the aged |
`donkey exist hay put and then-exist very_old | [?]`

**2**  […] a fire began to give light; and then, over his shoulder […]
`[?] ~fire begin-light ~and then-exist shoulder-to [?]`

**3**  in the night the son was born; and the son was
`night time on-be_born son and son exist`

**4**  […] Jesus. At that time […] […]
`[?] Jézus time then-exist [?] [?]`

**5**  light through Bethlehem town; and then a star
`through light Bethlehem town and then-exist star`

**6**  was seen […]; and from […] […]; and then
`see [?] and from [?] love-exist-to and then-exist`

**7**  at the star, a miracle. At that time the angel said […] […]
`on-star miracle time say angel understand-chapter [?]`

**8**  joy! A king is born, a king […] born in
`joy be_born king king [?] be_born inside`

**9**  Bethlehem town, within […], in a donkey's manger.
`~Bethlehem town inside [?] inside donkey manger`

**10**  […] the donkey […] hay within […] […]
`[?] donkey love hay inside [?] [?]`

**11**  Christ, Mary's son. And then […] went [to] Bethlehem;
`Christ Mary son and then-exist [?] go Bethlehem`

**12**  and then […] knelt down, and every one of them knelt
`and then-exist [?] kneel_(down) and each,_every this exist kneel_(down)`

**13**  before […] […] to go […] and […]
`before from [?] [?] to go [?] and [?]`

> Luke 2:10–11, the angel's "tidings of great joy" and the child born in the
> city of David.

## 021r — the reckoning of years

**1**  gave thanks, and gave thanks. Here ends this holy gospel […]
`thanks and thanks grab end this holy-gospel [?]`

**2**  Saint Luke writes, in […] […] of his writing, chapter […] […]
`write holy-Luke inside [?] [?] <of>-write chapter [?] [?]`

**3**  from Adam onward until the birth of the Lord Jesus Christ.
`out(ward) from +Adam ?onward until be_born Lord-Jézus-Christ.`

> Line 3 first read as blanks; the same Adam-to-Christ formula as 015v and
> 017v, now that the Adam sign is read (2026-09-20).

**4**  […] and […] hundred years and sixty years
`[?] and [?] hundred-year and two-two-two-ten-year`

**5**  and six years, until the birth of the Lord Jesus Christ.
`and six-year until be_born Lord-Jézus-Christ`

## 021v — the flight into Egypt, and the eighth day

**1**  At that time, in the year the Lord Jesus Christ was born […]
`time then-exist to-to-year on-be_born Lord-Jézus-Christ [?]`

**2**  at that time the angel said […] to the aged […]
`time say angel understand-chapter very_old [?]`

**3**  Rise up, and take this son and his mother(?), this son […]
`stand_up up and grab this son and <of> this son [?]`

**4**  and flee into Egypt. And they went, all of them, beginning […]
`and escape inside Egypt-to and go each,_every this begin [?]`

**5**  out of Egypt […] this; the angel […] said […] […] Here ends
`out(ward)-out(ward) Egypt [?] this this angel [?] say [?] [?] end`

**6**  this holy gospel. At that time he rose up […] |
`this holy-gospel time stand_up up [?] | [?]`

**7**  […] and took the Lord Jesus Christ and his mother, and […]
`[?] ~and grab Lord-Jézus-Christ and <of> mother and [?]`

**8**  the year […] when […] |
`year out(ward) then-exist | [?]`

**9**  […] they went into Jerusalem […], that is, when was born
`[?] go inside Jerusalem [?] that_is on-be_born`

**10**  the Lord Jesus Christ. On the eighth day the son was circumcised,
`Lord-Jézus-Christ on-six-two-year time circumcise son`

**11**  and the son was named Jesus. And this Lord Jesus first
`and son exist [?] Jézus and this Lord-Jézus first`

**12**  […] shed his blood; and then […]
`[?] <of>-Lord blood shed and then-exist [?]`

**13**  the Lord Jesus was circumcised in Jerusalem. Chapter. And they fled
`circumcise Lord-Jézus inside Jerusalem exist-chapter and escape`

**14**  […]
`[?]`

> Matthew 2:13 and Luke 2:21. Line 10 dates the circumcision to the eighth
> day, which is what Luke says, and lines 11–12 call it the first shedding of
> Christ's blood — a medieval devotional idea, not a gospel one.

---

## 022r — Egypt, and the twelve

**1**  into the land of Egypt; and […]; and the Lord went […]
`inside Egypt earth and [?] and go Lord [?]`

**2**  in the land of Egypt, into every city […] […]
`on-Egypt earth inside each,_every town [?] [?]`

**3**  […] the evil ones pierced and pierced; and | […]
`[?] evil pierce-pierce and | [?]`

**4**  […] died. From […] they remained in Egypt twelve years,
`[?] die from [?] leave-leave inside Egypt six-six-year`

**5**  at that time the angel Gabriel said […]
`time say ~Gabriel angel [?]`

**6**  Flee into the land of Egypt, into […] city.
`escape on-Egypt earth inside [?] town`

**7**  And […] they remained […]
`and [?] leave-leave [?]`

**8**  [in that] city twelve years; and […]; and this […]
`town six-six-year and [?] and this [?] table`

**9**  […] years. Here ends this holy gospel. One
`ten-ten-two-nine-year end this holy-gospel one`

**10**  […] He called twelve apostles; and […] […] and |
`[?] call six-six apostle and [?] [?] and | who-this`

**11**  many miracles […]: the blind eye […] the Lord, through
`and-this miracle [?] eye blind [?] Lord through`

**12**  light; the dead […] the Lord […] the evil among the people […]
`light die [?] Lord [?] evil inside people [?]`

## 022v — the signs, numbered

**1**  First, that is, […] the Lord made wine […] that is […] the Lord
`before that_is [?] Lord wine create-Lord [?] on-that_is [?] Lord`

**2**  broke […] […] […] […] the people.
`break [?] [?] [?] [?] people`

**3**  The fourth sign the Lord Jesus showed, when |
`in_turn-two-two can show Lord-Jézus then-exist | [?]`

**4**  […] he raised up from […] a son […]
`before in_turn-to-in_turn resurrect from [?] son [?]`

**5**  the sign the Lord Jesus showed, when he raised up […]
`can show Lord-Jézus then-exist resurrect to-to [?]`

**6**  in Jerusalem. The sixth sign the Lord Jesus showed in […]
`inside Jerusalem in_turn-six can show Lord-Jézus inside [?]`

**7**  […] when the Jews brought a sick man
`in_turn-chapter-in_turn then-exist Jew(ish) carry one ill`

**8**  before the Lord Jesus: a sick man, and a sick man, and a sick man, and a paralytic;
`before Lord-Jézus <sick_man> and <sick_man> and <sick_man> and paralytic`

**9**  and the sick, the sick, the sick, the paralytic — the Lord Jesus healed […]
`and <sick_man> <sick_man> <sick_man> paralytic from-healing Lord-Jézus [?]`

**10**  The sign the Lord Jesus showed in Capernaum, when he healed alive
`can show Lord-Jézus inside Capharnaum because from-healing living`

**11**  the servant of a soldier; and […] […]
`two servant one soldier and [?] [?]`

**12**  […] The eighth sign the Lord Jesus showed
`exist [?] in_turn-six-two can show Lord-Jézus`

**13**  in Tyre […] to a woman […]
`inside Tyrus in_turn-chapter-in_turn to-to one ~woman head`

> First the water into wine at Cana, John 2:11, which the gospel itself calls
> the first of the signs. Then the centurion's servant at Capernaum, Matthew
> 8:5, and the Syro-Phoenician woman at Tyre, Mark 7:24 — both named by the
> right place.

## 023r — the ninth, tenth and eleventh signs

**1**  a […]; and within her was a devil; and […]
`one [?] and inside to-to exist hell evil and [?]`

**2**  he cast it out […]. The ninth sign the Lord Jesus showed in |
`out(ward) [?] in_turn-nine can show Lord-Jézus inside | [?]`

**3**  a proud man […] because the man […]
`proud on-one [?] somebody because somebody [?]`

**4**  did. The tenth sign the Lord Jesus showed in […]
`do, in_turn-ten can show Lord-Jézus inside apostle-oh-<divine>-chapter`

**5**  a king's son, because he was at the point of death; and the son […]
`one king son because exist on-die and son [?]`

**6**  […] The eleventh sign the Lord Jesus showed in Jerusalem: the evil
`[?] in_turn-and can show Lord-Jézus inside Jerusalem evil`

**7**  spirit, when the Lord [cast] out of a man a devil […]
`then-exist Lord inside one somebody hell evil [?]`

**8**  First, before the birth of the Lord Jesus Christ, the Son of God […]
`first before be_born Lord-Jézus-Christ son God [?]`

**9**  a prophet, a forefather, this […]
`one prophet one forefather this [?]`

**10**  […] […] Christ […]; and by miracle they confessed
`[?] [?] Christ [?] and miracle confess`

**11**  […] the Lord Jesus is truly the Son of God. […] confessed […]
`[?] Lord-Jézus righteous(ly) son God [?] confess [?]`

**12**  the Lord Jesus […] the Lord Jesus is truly the Son of God. First confessed
`Lord-Jézus [?] Lord-Jézus righteous(ly) son God first confess`

**13**  […] the Lord Jesus […] and Elijah. Secondly confessed
`~have Lord-Jézus [?] and Elijah in_turn-two confess`

> The king's son at the point of death is John 4:46–54, and "at the point of
> death" is the gospel's own phrase.

## 023v — who confessed him, and the Transfiguration

**1**  […] the Lord Jesus; God the Father, the Lord's […]. Confessed the evil ones,
`~have Lord-Jézus from-father-<divine> <of>-Lord [?] confess ~evil evil`

**2**  […] the Lord Jesus is truly the Son of God. Fourthly confessed
`[?] Lord-Jézus righteous(ly) son God in_turn-two-two confess ~have`

**3**  the Lord Jesus — the angels […] the Lord Jesus is truly the Son of God.
`Lord-Jézus angel [?] Lord-Jézus righteous(ly) son God [?]`

**4**  They confessed […]; and the earth, the sun,
`confess [?] and earth sun [?]`

**5**  the moon […] the Lord Jesus is truly the Son of God; and all this […]
`moon [?] Lord-Jézus righteous(ly) son God and this each,_every [?]`

**6**  […] the Lord Jesus is truly the Son of God. First confessed it Saint Peter,
`[?] Lord-Jézus righteous(ly) son God first confess holy-Peter`

**7**  […] and Elijah. Saint Luke writes that when
`[?] and Elijah write holy-Luke then-exist`

**8**  the Lord Jesus was thirty […], at that time the Lord Jesus went […]
`Lord-Jézus inside thirty [?] time go Lord-Jézus [?]`

**9**  [to] Mount Tabor with his apostles; and he was transfigured; and
`Mount_Tabor and <of> apostle and be_glorified ~and`

**10**  the apostles saw […] and Elijah […] […]
`see apostle [?] and Elijah [?] [?]`

**11**  and they saw the light […]; and then there stood | the Lord
`and see light [?] and then-exist from-leave-leave | Lord`

**12**  Jesus, and […] and Elijah; and then the apostles, through
`Jézus and [?] and Elijah and then-exist apostle through`

**13**  fear, fell down […]; and then the apostles […]
`get_frightened and down [?] bow_down and then-exist apostle [?]`

> Peter's confession, Matthew 16:16, "Thou art the Christ, the Son of the
> living God" — and the codex names him. Then the Transfiguration on Tabor
> with Elias, and Matthew 17:6, "they fell on their face, and were sore
> afraid."

## 024r — Tabor and Carmel, and the baptism

**1**  heard this word spoken […] of the Son; and the Father […] […] […]
`hear this word say [?] <of> son and father [?] [?] [?]`

**2**  and then home […] not the apostles, and not every […]
`and then-exist home [?] not apostle and not each,_every [?]`

**3**  but to the Lord Jesus. Here ends this holy gospel. Secondly confessed
`a) to-Lord-Jézus end this holy-gospel in_turn-two confess`

**4**  […] the Lord Jesus, God the Father: first on Mount Tabor,
`~have Lord-Jézus from-father <of>-Lord first on-Mount_Tabor`

**5**  secondly on Mount Carmel. Because when the Lord Jesus was thirty
`in_turn-two on-Carmel to-mount because then-exist Lord-Jézus inside thirty`

**6**  […], at that time the Lord Jesus went […] Saint John
`[?] time go Lord-Jézus understand [?] holy-John`

**7**  […] to Mount Carmel; and then the Lord went |
`[?] on-Carmel to-mount and then-exist Lord go | to`

**8**  [to] Saint John. The Lord Jesus said: John […]. The Lord said | Saint
`holy-John say Lord-Jézus John [?] Lord say | holy`

**9**  John: Master, and […] […] […]. And the Lord Jesus said,
`John Master and [?] [?] [?] and say Lord-Jézus`

**10**  John […] the Lord; and […] is […]
`John [?] Lord and [?] exist [?]`

**11**  Saint John […] baptized the Lord Jesus, when
`holy-John [?] see-baptize Lord-Jézus then-exist`

**12**  the Lord was thirty years old; and […] the Holy Spirit
`to-Lord inside thirty year and [?] holy-spirit`

## 024v — the dove

**1**  in the form of a dove […]: This is the Lord's Son.
`inside ~shape,_form dove [?] this-Lord <of> son`

**2**  […] the Spirit came to rest; and the Lord took
`[?] spirit calm_down and Lord grab`

**3**  the Holy Spirit; and the Lord went into […]
`holy-spirit and Lord go inside [?]`

**4**  […] the Lord Jesus […] years […] confessed
`[?] Lord-Jézus ten-two-two-year [?] confess`

> Matthew 3:16–17 — the Spirit descending like a dove, and the voice naming
> the Son.

## 025r — the devils confess him

**1**  the devils […] the Lord Jesus is truly the Son of God. Because when
`hell evil [?] Lord-Jézus righteous(ly) son God because exist`

**2**  the Lord Jesus was thirty years old, at that time the Lord Jesus went into |
`Lord-Jézus inside thirty year time go Lord-Jézus inside | exist`

**3**  […] […]; and then he went into […]. At that time
`[?] in_turn-chapter-in_turn and then-exist go inside [?] time`

**4**  a man knelt down before the Lord Jesus,
`then-exist kneel_(down) one somebody before Lord-Jézus`

**5**  […] the Lord; the man […] one son; and […]
`[?] Lord mouth somebody [?] one son and [?]`

**6**  a devil […]. The man's son — his apostles […] could not
`hell evil [?] somebody son <of> apostle to-hide_oneself-to [?] can`

**7**  heal him. […] He begged the Lord to heal this man's son. Said
`from-healing [?] ask_(for) from-healing this Lord <of>-somebody son say`

**8**  the Lord Jesus: have mercy […] the son […] […]
`Lord-Jézus have_mercy gain [?] son can [?] [?]`

**9**  And then the son came before the Lord Jesus; and […]
`and then-exist son go before Lord-Jézus and [?]`

**10**  he was made whole; and this […] confessed — the devils […]
`healing leave-to-leave and this [?] confess hell evil [?]`

**11**  the Lord Jesus is truly the Son of God, because by miracle they confessed. Fourthly
`Lord-Jézus righteous(ly) son God because miracle confess in_turn-two-two`

**12**  confessed […] the Lord Jesus — the angels, at the birth of the Lord Jesus
`confess have Lord-Jézus angel on-be_born Lord-Jézus`

**13**  Christ. Because when the Lord Jesus was born [in] Bethlehem
`Christ because then-exist Lord-Jézus be_born Bethlehem`

> Matthew 17:14–18: the father kneels, the disciples could not cure the boy,
> and Jesus does.

## 025v — the Nativity told again

This page repeats 020v almost word for word, as the proof that the angels
confessed him.

**1**  town; and first, before the birth, one […] was
`town and first before be_born one [?] exist`

**2**  […] a star, light through Bethlehem town; and | then
`[?] star through light Bethlehem town and | then`

**3**  the star was seen […]; and from […] […]
`exist star see [?] and from [?] [?]`

**4**  and then at the star, a miracle. At that time the angel said […]
`and then-exist on-star miracle time say angel [?]`

**5**  […] joy! A king is born, a king […]
`[?] joy be_born king king [?]`

**6**  born in Bethlehem town, in a barn, in a donkey's
`be_born inside ~Bethlehem town inside barn inside donkey`

**7**  manger […] the donkey, in the hay, in
`manger [?] donkey inside hay inside`

**8**  […] […] Christ, Mary's son. And | then
`[?] [?] Christ Mary son and | then`

**9**  […] […] they went [to] Bethlehem; and […]
`[?] [?] go Bethlehem and [?]`

**10**  […] knelt down, and every one of them knelt | and
`[?] kneel_(down) and each,_every this ~exist kneel_(down) | ~exist`

**11**  […] from […] […] to go […] and
`[?] from [?] [?] to go [?] and`

**12**  […] gave thanks, and gave thanks. Here ends this holy gospel.
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

**2**  because when the Lord Christ […]
`because then-exist Lord-Christ [?]`

**3**  the earth quaked, the rocks and the stones split.
`earth quake-rock stone split`

> Matthew 27:51, "the earth did quake, and the rocks rent".

## 026v — the sun darkened, and Abraham's confession

**1**  The sun and the moon were darkened; and all […] […] humbled themselves; and all
`sun and moon this eclipse and each,_every [?] [?] this humble and each,_every`

**2**  creation […] when Christ […]; and all this […] confessed,
`create [?] then-exist Christ [?] and this each,_every [?] confess`

**3**  in sorrow […], that the Lord Jesus is truly the Son of God; and by miracle they confessed
`inside-to-sad(ly) [?] Lord-Jézus righteous(ly) son God and miracle confess`

**4**  […] the Lord Jesus is truly the Son of God, because […]
`[?] Lord-Jézus righteous(ly) son God because [?]`

**5**  miracle […]; and the Lord suffered [under] the Jews […]
`miracle [?] and suffer Lord Jew(ish) [?]`

**6**  and […] […] the Lord God […] Abraham |
`and [?] [?] Lord-<divine> [?] Abraham | [?]`

**7**  […] came […] said. The Lord God said to Abraham by the angel; and this
`[?] arrive [?] say exist say Lord-<divine> Abraham on-angel and this`

**8**  the Lord God said to the blessed Virgin Mary by the angel; and | Saint
`say say Lord-<divine> happy virgin-Mary on-understand-chapter angel and | holy`

**9**  […] […]; and the man who believes in the Lord,
`[?] [?] and somebody to-Lord exist believe`

**10**  that he is truly the Son of the living God — every man is saved; and […]
`what righteous(ly) son living God each,_every somebody be_saved and [?]`

**11**  a man is damned; and the Lord […] believes; and […]
`somebody be_damned to and Lord [?] believe and [?]`

**12**  one is saved, but […] a man is damned; and | this
`one to be_saved a) [?] somebody be_damned and | this`

**13**  thus he said. First confessed it Abraham the forefather |
`and-this say confess first Abraham forefather | on-this`

**14**  This one confessed […]; secondly confessed […]
`this confess [?] on-that_is confess [?]`

## 027r — Mary's confession

**1**  the mother, the blessed Virgin Mary. Thirdly confessed the blessed | Virgin
`mother happy virgin-Mary on-that_is confess happy | virgin`

**2**  Mary. The angel of God said: at that time the Lord was; the Lord God went; the Lord's
`Mary say angel God time exist Lord go Lord-<divine> <of>-Lord`

**3**  angel [to] the blessed Virgin Mary, when […] from […] to the house
`angel happy virgin-Mary then-exist ~out(ward) from want-year to-house`

**4**  of the Virgin Mary […]; and she bore; and […] […]
`virgin-Mary [?] and be_born and [?] [?]`

**5**  and one hundred and sixteen(?) years and […] and and […]
`and one hundred and six-ten-year and [?] and and [?]`

**6**  at that time God the Father in heaven, because he saw […] all
`time from-gate from-father-<divine> heaven because see hide_oneself each,_every`

**7**  […] darkness […]. At that time God the Father
`[?] darkness [?] time from-gate from-father-<divine>`

**8**  in heaven; and the Lord's angel Gabriel went […]
`heaven and go <of>-Lord angel Gabriel inside exist-chapter`

**9**  to the blessed Virgin Mary, and said this and that. Saint Luke writes
`to-happy virgin-Mary and this-and-this say write holy-Luke`

**10**  […] in his writing; and the man who believes in the Lord,
`[?] <of>-write and somebody to-Lord exist believe`

**11**  that he is truly the Son of the living God — every man is saved; and
`to righteous(ly) son living God each,_every somebody be_saved and`

**12**  one man is damned; and the Lord […]
`one somebody be_damned to and Lord [?]`

**13**  believes; and one is saved; but every man
`believe and one to be_saved a) each,_every somebody`

## 027v — Joseph's confession, and "there are not many gods"

**1**  is damned; and thus he said. Confessed it Saint Joseph the aged |
`be_damned and this-and-this say confess holy-very_old | [?]`

**2**  […] the angel of God said, because the Lord God spoke by the angel
`[?] say angel God because exist say Lord-<divine> on-angel`

**3**  Gabriel; and […] who is the Lord's […] truly
`Gabriel and [?] to-Lord exist [?] to righteous(ly)`

**4**  the Son of the living God — every man is saved; and one
`son living God each,_every somebody be_saved and one`

**5**  man is damned; and the Lord […] […]; and | […]
`somebody be_damned to and Lord [?] [?] and | [?]`

**6**  […] is saved, but every […] is damned; and | thus
`chapter to be_saved a) each,_every [?] be_damned and | this-and`

**7**  he said. The Lord Jesus spoke of his many wounds, when the Lord went |
`this say say Lord-Jézus on-many wound then-exist Lord go | on`

**8**  to his death; and then the Lord […] the apostles in Jerusalem. At that time knelt
`die and then-exist-Lord [?] apostle inside Jerusalem time kneel_(down)`

**9**  the Lord Jesus before the blessed Virgin Mary; and the Lord Jesus said: there are not
`Lord-Jézus before happy virgin-Mary and say Lord-Jézus is_not`

**10**  many gods […] one God […] the Lord Jesus
`many God [?] one God [?] Lord-Jézus`

**11**  […] and the Lord […] […] in the Lord Jesus Christ; and
`to and Lord [?] [?] inside Lord-Jézus-Christ and`

**12**  one is saved, but every man is damned;
`one to be_saved a) each,_every somebody be_damned`

**13**  and Mary blessed the Lord Jesus, with all the apostles — the blessed Virgin Mary.
`and Mary bless Lord-Jézus on-each,_every apostle happy virgin-Mary`

## 028r — the Passover lamb, and the twelfth sign

**1**  And then Mary […] the Lord Jesus, the Lord's mother,
`and then-exist-Mary exist-Lord [?] Lord-Jézus <of>-Lord mother`

**2**  the blessed Virgin Mary; and then Mary was, and from […]
`happy virgin-Mary and then-exist-Mary exist and from [?]`

**3**  […] Mary's son the Lord Jesus Christ; and from Mary went
`[?] <of>-Mary son Lord-Jézus-Christ and from Mary from-go`

**4**  the Lord Jesus […] the apostles in Jerusalem, because […] the apostles […]
`Lord-Jézus [?] apostle inside Jerusalem because [?] apostle [?]`

**5**  Before the Lord went into Jerusalem, where the apostles [were] at supper […]
`before Lord go inside Jerusalem who-exist apostle to-dinner-to-to [?]`

**6**  the apostles prepared a lamb, because at that time
`prepare-apostle one lamb because time`

**7**  was the feast of the Jews, the Passover. […] There began the suffering
`holiday exist Jew(ish) Easter [?] begin suffering`

**8**  of the Lord Jesus Christ, Son of God; because […] the Lord is truly the Son of God.
`Lord-Jézus-Christ son God because [?] Lord righteous(ly) son God`

**9**  And then the Lord, the Jews […]; and then the Lord, the apostles,
`and then-exist Lord Jew(ish) [?] and then-exist Lord apostle`

**10**  the mother; he was laid in the tomb, and […] rose from the dead. And the | twelfth
`mother inside burial_chamber put and [?] from die stand_up-Lord and from | six`

**11**  sign the Lord Jesus showed, when […]
`six can show Lord-Jézus then-exist [?]`

**12**  from […] the Lord and the apostles […] in Jerusalem; and […] the sign the Lord Jesus showed
`from [?] Lord and apostle [?] inside Jerusalem and [?] can show Lord-Jézus`

## 028v — the Ascension

**1**  when […] […] on a mountain, two men and two men
`then-exist [?] [?] one mount two somebody and two somebody`

**2**  […] […] and […] and sixteen(?) and six devils
`[?] [?] and [?] and six-ten and six hell evil`

**3**  and the two men were healed […] […] the sign showed
`and two somebody healing [?] [?] can show`

**4**  the Lord Jesus; then […] when he went to God his Father |
`Lord-Jézus then [?] then-exist leave to-<of>-Lord father-<divine> | on`

**5**  in heaven […]; the Lord sat at the right hand of God the Father.
`heaven [?] from-sit-Lord from-father-<divine> God on-right_side`

> The last line is the creed: he ascended into heaven, and sitteth at the
> right hand of God the Father.

## 029r — the Passion begins: "Here begins"

**1**  Here begins […]
`begins this begin [?]`

**2**  […] of a man […]
`[?] <of>-somebody [?]`

**3**  the writing […] […]
`write [?] cup-not [?]`

**4**  [of] Saint Matthew and Saint John,
`holy-Matthew and holy-John`

**5**  of the Passion |
`from suffering | [?]`

**6**  a man […] […]
`somebody [?] [?]`

**7**  The Lord Jesus went […]
`go Lord-Jézus [?]`

**8**  to Jerusalem, because […] the Lord […] to the supper […] because […]
`Jerusalem because from far-to-Lord to-dinner-chapter [?] because exist [?]`

**9**  Before the Lord went, the apostles [went] into Jerusalem […] the Lord Jesus […]
`before Lord go apostle inside Jerusalem [?] Lord-Jézus exist [?]`

**10**  to prepare the Passover lamb, where the Lord and the apostles […]
`prepare from Easter lamb who-exist Lord apostle [?]`

**11**  should eat. And the Lord [said]: go, you. And then the Lord […]
`eat and this-Lord to you go and then-exist Lord [?]`

**12**  to the apostles in Jerusalem; and the Lord sat down at the table […] the apostles. At that time
`to-apostle inside Jerusalem and sit to-throne Lord [?] this-apostle time`

**13**  the apostles prepared the Passover lamb; and the lamb
`exist apostle prepare from Easter lamb and lamb`

> The codex names its own sources for the Passion: Saint Matthew and Saint
> John. Line 1 is a rubric, "Here begins", of the kind a scribe writes.

## 029v — the supper, and the washing of feet

**1**  the apostles brought to the table […] the Lord Jesus […] the Lord's […]
`carry apostle on throne [?] Lord-Jézus [?] <of>-Lord from`

**2**  […] the Lord would eat this with you […]
`[?] want Lord to you eat this [?]`

**3**  lamb. Therefore the Lord asks you: do not, apostles,
`lamb that_is_why ask_(for)-Lord you do_not apostle`

**4**  be offended in the Lord, because the Lord goes to his death — the Lord dies; and the Lord |
`inside Lord stumble because this-Lord go on-die Lord die and this-Lord | on`

**5**  […] […] […] and the Lord […] you […]
`[?] [?] [?] and this-Lord you [?]`

**6**  and […] the Lord Jesus [rose] from the table, and laid aside |
`and [?] to-throne Lord-Jézus and take_off-Lord | on`

**7**  the Lord, his […] […]. The Lord Jesus, one apostle
`Lord <of>-Lord [?] [?] Lord-Jézus one apostle`

**8**  among […] the apostles, and among […] the apostles, and […]
`among [?] apostle and among [?] apostle and [?]`

**9**  an apostle [named …] brought a bucket […]
`apostle exist <name>-in_turn carry one bucket [?]`

**10**  and a washing-dish; and then water into the dish
`and one washdish and then-exist water inside washdish`

**11**  he poured; and the Lord Jesus came to Saint Peter, and […]
`pour and go Lord-Jézus to holy-Peter in_turn <name>-in_turn`

**12**  brought the water in the dish, which the Lord Jesus […] Saint Peter.
`carry inside washdish water this-who Lord-Jézus [?] holy-Peter`

> John 13:4–6, in order: he rose from supper, laid aside his garments, poured
> water into a basin, and came to Simon Peter. Luke 22:15 is at line 2, and
> Matthew 26:31, "all ye shall be offended", at line 4.

---

## 030r — Peter objects

**1**  Master […] Peter […] the Lord […] washes my feet?
`Master [?] this-Peter [?] this-Lord [?] foot wash`

**2**  […] the Lord Jesus […] […] the Lord […] the feet
`[?] Lord-Jézus [?] [?] this-Lord [?] foot`

**3**  washed […] […] […] within […] […]
`wash [?] [?] [?] inside [?] [?]`

**4**  […] […] Master […] Peter, this
`[?] [?] Master [?] this-Peter this`

**5**  […] trespass; the Lord, the sufferer […]
`[?] trespass this-Lord sufferer [?]`

**6**  […] […] […] the Lord in heaven […] |
`[?] [?] [?] this-Lord inside heaven [?] | [?]`

**7**  […] the Lord took […] […]
`[?] this-Lord grab-cut_off-to [?] [?]`

**8**  washed; and all […] […] he washed; and | then
`wash and each,_every [?] [?] wash and | then`

**9**  […] […] the Lord washed their feet; and the feet
`exist [?] [?] foot exist-Lord wash and foot`

**10**  […] […] […] and the two of them from […] among the apostles, every one
`[?] [?] [?] and two from [?] apostle middle each,_every`

**11**  he washed; and the feet […] […] […] and
`wash and foot [?] [?] [?] and`

**12**  the Lord Jesus took […] his […] and
`grab Lord-Jézus on-Lord <of>-Lord [?] and`

> John 13:8, Peter's "thou shalt never wash my feet".

## 030v — the bread, and the cup with water and wine

**1**  The Lord Jesus sat at table with the apostles […]; the Lord Jesus looked […] the apostles
`sit Lord-Jézus to-throne to-apostle [?] Lord-Jézus see [?] apostle`

**2**  […] see how the Lord […] you […] from […]
`to-Lord see how? this-Lord you [?] from [?]`

**3**  and you shall eat […] […]; and took
`and you understand-eat two [?] and grab`

**4**  the Lord Jesus […] one baked loaf,
`Lord-Jézus inside why?-in_turn one baked „cake”`

**5**  and […] the Lord Jesus this […] and […]
`and [?] Lord-Jézus this [?] and [?]`

**6**  the Lord set it before them; and the Lord Jesus took
`before Lord put Lord-Jézus and grab Lord-Jézus`

**7**  wine in a cup, and poured water into the cup; and […]
`wine one cup and water inside cup pour and [?]`

**8**  the Lord Jesus, the wine and the water; and the wine and water
`Lord-Jézus wine and water and wine water`

**9**  the Lord Jesus set before them […] the Lord Jesus; and […]
`before Lord put Lord-Jézus [?] Lord-Jézus and [?]`

**10**  whoever eats of this […], that man shall be | the
`exist this [?] eat this somebody exist | <of>`

**11**  Lord's […] […]; and the man who […] this […]
`Lord [?] [?] and somebody [?] this [?]`

> Water poured into the wine is not in the gospels. It is the mixed chalice
> of the Mass, so the page is describing the rite as much as the supper.

## 031r — one of you shall betray me

**1**  eats and believes in the Lord […]; every man is damned […]
`eat and Lord believe each,_every somebody be_damned [?]`

**2**  and the man who believes in the Lord […] is from
`and somebody exist Lord believe [?] exist from`

**3**  […] they ate the holy Host […] drank […]
`thirty holy-host eat [?] drink [?]`

**4**  that man shall live. O! O! Amen. […]
`somebody exist living chapter-oh chapter-oh amen [?]`

**5**  The Lord Jesus […] […]: one among you
`Lord-Jézus [?] [?] one among you`

**6**  and […] the Lord […] one of the apostles shall betray him. And the apostles looked among
`and [?] Lord [?] from apostle betray and see-apostle among`

**7**  the apostles, saying […] Master […] and […]
`apostle say [?] Master [?] and [?]`

**8**  the Lord Jesus said; and […] […] the Lord Jesus
`say Lord-Jézus and [?] [?] Lord-Jézus`

**9**  […] and John, and said: O […] […]
`[?] and ~John and say oh [?] [?]`

**10**  […] Master, who is it? And then he leaned
`from-judge Master Who_is_it? and then-exist lean_on`

**11**  […] upon the Lord Jesus […] Master |
`[?] on-end Lord-Jézus [?] Master | [?]`

**12**  thus said the Lord Jesus […]; the Lord took a morsel
`this-and-this say Lord-Jézus [?] this-Lord grab bite`

> John 13:25, "Lord, who is it?", with John leaning on him, and 13:26, the
> sop. The dictionary has a word for "Who is it?" as a single code.

## 031v — Satan enters into Judas

**1**  […] It is he. And then […] […]
`[?] That_is_it. and then-exist sleep [?]`

**2**  upon the Lord Jesus; and he took this […]
`on-end Lord-Jézus and grab this [?]`

**3**  […] and […] the Lord Jesus […] this
`[?] and [?] Lord-Jézus [?] this`

**4**  […] And then […] Judas
`[?] and then-exist [?] exist-Lord Judas`

**5**  […] took; and then […] Judas
`[?] grab and then-exist [?] Judas`

**6**  […] In that place the devil entered into Judas.
`[?] on-to-place hell evil inside Judas go-this`

**7**  […] the Lord Jesus; the apostles weeping […]; and he took this
`[?] Lord-Jézus apostle crying from somebody and grab this`

**8**  […] the Son of God […] the Lord Jesus. Judas did
`from son God [?] Lord-Jézus Judas do,`

**9**  […] did; and then […] the apostles, how
`[?] do, and then-exist [?] apostle how?`

**10**  he said: Master, speak. But the apostles did not understand what Judas said.
`say Master speak a) understand apostle how? say Judas`

**11**  […] bought […] shepherd […] because
`[?] buy [?] shepherd [?] because`

**12**  […] the apostles […] because this was the Jews' Passover.
`food apostle ~exist judge because this exist Jew(ish) Easter`

> John 13:27, "Satan entered into him", and 13:28, "no man at the table knew
> for what intent he spake this unto him."

## 032r — Wednesday, and the silver

**1**  and […] Judas; and he went [to] the Jews'
`and [?] Judas and go Jew(ish)`

**2**  chief in Jerusalem; because the Lord was […]. On Wednesday one of the apostles
`head inside Jerusalem because Lord exist inside Wednesday from apostle`

**3**  betrayed him — Judas — because he took for the Lord […]
`betray Judas because exist to-Lord grab [?]`

**4**  silver […] the Lord Jesus; the Lord's brethren; the Lord
`silver [?] Lord-Jézus brother <of>-Lord this-Lord`

**5**  goes to God his Father; and the Lord […] to you
`go <of>-Lord father-<divine> and this-Lord you`

**6**  the Holy Spirit shall come; and you shall […]
`go holy-spirit and you exist see-two`

**7**  […] that is, the Lord goes to his death; the Lord dies, because
`judge that_is this-Lord go on-die Lord die because`

**8**  the Lord, the Jews […]; and the Lord […]
`Lord Jew(ish) [?] and this-Lord [?]`

**9**  […] the Lord shall rise. Therefore the Lord asks you:
`[?] stand_up-Lord that_is_why ask_(for) Lord you`

**10**  do not, apostles, be offended in the Lord, because […]
`do_not apostle inside Lord stumble because what-go [?]`

**11**  [to] God his Father […] […] […] the Lord […] […]
`<of>-Lord father-<divine> [?] [?] [?] Lord [?] [?]`

> The codex dates the betrayal to a Wednesday, which is the traditional day
> and not stated in any gospel.

## 032v — Peter will deny him

**1**  Peter: Master — Peter would […] the Lord; the Lord dies.
`Peter Master this-Peter want food Lord this-Lord die`

**2**  […] the Lord Jesus [to] Peter: first, but before […]
`[?] Lord-Jézus Peter first a) before [?]`

**3**  […] thou shalt deny the Lord. And Peter said […]
`[?] Lord-to [?] exist deny and Peter say [?]`

**4**  […] […] the Lord Jesus, Peter, this […] this
`emperor [?] Lord-Jézus Peter this [?] this`

**5**  […] Therefore the Lord asks you: do not […]
`~out(ward) that_is_why ask_(for) Lord you do_not [?]`

**6**  be offended in the Lord; because the apostles were very sorrowful for the Lord;
`inside Lord stumble because exist apostle many sad(ly) on-Lord have`

**7**  and one of the Jews was a judge; and the mouth
`in_turn one Jew(ish) exist judge and mouth`

**8**  […] the Lord Jesus said: but […]; and the Lord went
`can Lord say Lord-Jézus a) [?] and go Lord`

**9**  on the way, because the Lord Jesus […] when the Lord […]
`on-way because have Lord-Jézus then-exist Lord [?]`

**10**  Judas, in the house of the high priest; and many miracles
`Judas inside house ~high_priest and many miracle`

**11**  and much preaching […] the Lord Jesus, on the way.
`and many ~preach [?] Lord-Jézus on-way`

---

## 033r — over the brook Cedron, into the garden

**1**  And Saint John tells of many miracles and much preaching
`and speak holy-John many miracle and many ~preach`

**2**  […] of the Lord Jesus […], but it is not written
`[?] Lord-Jézus [?] but inside write not`

**3**  down. And then the Lord and the twelve apostles […] […]
`write and then-exist Lord six-six apostle [?] [?]`

**4**  There was a brook […]; and of the apostles
`exist one brook [?] and from apostle`

**5**  the rest of the apostles […]. The Lord took Peter,
`rest apostle [?] apostle Lord grab Peter [?]`

**6**  John, and […], and […]
`John and [?] and [?]`

**7**  across the Cedron; and […] into […]
`over-exist Cedron and [?] inside [?]`

**8**  and […], because there was a garden there […]
`and [?] because-exist garden on-this [?]`

**9**  […] Jerusalem […]; and […] the Lord went to Jerusalem; and in
`trespass Jerusalem in_turn-to-in_turn and [?] go-Lord on-Jerusalem and inside`

**10**  Jerusalem, behold, the Lord […] to the Lord Jesus and his apostles,
`Jerusalem lo Lord [?] to Lord-Jézus and <of>-Lord apostle`

**11**  because they would seize the Lord Jesus and take him in the garden.
`because want-Lord grab Lord-Jézus inside-garden capture`

**12**  […] of the man, the father Adam […] […]
`[?] <of>-somebody father ~Adam [?] [?]`

> Line 2 is John 21:25, the many other things Jesus did that are not written.
> Lines 4–8 are John 18:1: over the brook Cedron, where there was a garden.
> The codex has the brook by name.

## 033v — a stone's cast, and the prayer

**1**  through […] this the Lord Jesus would, to a man […]
`through [?] this want Lord-Jézus to-somebody [?]`

**2**  […] suffering, not […]; and then from the Lord
`[?] suffering not-to and then-exist from-to Lord`

**3**  the apostles in the garden; and the Lord went […] tells
`apostle inside garden in_turn to-Lord go [?] speak`

**4**  Saint John. The Lord went […] from the apostles […]
`holy-John from-go-Lord trespass from apostle [?] then-chapter`

**5**  about a stone's throw […]; his Father; and he knelt down,
`stone to-throw [?] father <of>-Lord and kneel_(down)`

**6**  the Lord Jesus […] Father, his God […]
`Lord-Jézus [?] father <of>-Lord God [?]`

**7**  […] take from the Lord this suffering; nevertheless
`from [?] from Lord this suffering in_turn`

**8**  […] as it pleases thee. And […] the Lord Jesus; and the Lord went
`[?] pleasing and [?] Lord-Jézus and go-Lord`

**9**  to the apostles […]; the apostles were asleep […] the Lord Jesus […]
`to apostle [?] apostle to-sleep [?] Lord-Jézus [?]`

**10**  and […] woke them; and the Lord Jesus went […] Peter
`and [?] awake and go Lord-Jézus Peter`

**11**  [to] the hilltop […] to see this […], because all the people were
`mountain_peak [?] to see this [?] because exist each,_every people`

> Luke 22:41, "withdrawn from them about a stone's cast, and kneeled down,
> and prayed". The codex has the stone's cast.

## 034r — the second prayer, and the sweat

**1**  And a second time the Lord went […], and the Lord Jesus knelt […]
`and two go Lord [?] and kneel_(down) Lord-Jézus [?]`

**2**  God the Father […] take from […] from the Lord this suffering;
`father-<divine> [?] from [?] from Lord this suffering`

**3**  nevertheless […] as it pleases thee. And then the sweat ran down
`in_turn [?] pleasing and then-exist to-to-to sweat through`

**4**  the Lord Jesus, because […] the Lord Jesus […] the Lord's suffering
`Lord-Jézus because [?] Lord-Jézus [?] Lord suffering`

**5**  […]. And the Lord went to the apostles […]; the apostles were asleep
`not-chapter and go Lord to-apostle [?] apostle to-sleep`

**6**  […] the Lord Jesus […]; and […] woke them.
`[?] Lord-Jézus [?] and [?] awake`

**7**  At that time Saint Peter went […] […] sat
`time go holy-Peter [?] [?] army-to sit`

**8**  and […] the Lord went […] to God his Father, and knelt | the Lord
`and [?] go Lord [?] father-<divine> <of>-Lord and kneel_(down) | Lord`

**9**  Jesus […] God his Father […] from |
`Jézus [?] father-<divine> <of>-Lord [?] from | [?]`

**10**  Father, take from the Lord this suffering; nevertheless […] as it pleases thee; nevertheless
`father from Lord this suffering in_turn [?] pleasing in_turn`

**11**  […] as it pleases thee; because God the Father […] for the Lord, the whole wide world |
`[?] pleasing because this-father-<divine> [?] on-Lord ~the_whole_wide_world | <of>`

> Luke 22:44, the sweat. Three prayers in the garden, as in Matthew 26, and
> the second and third are worded almost identically here.

## 034v — the angel from heaven

**1**  the Father. And an angel came […] from on high, from God the Father […]
`father and go angel [?] high from-father-<divine> [?]`

**2**  the Lord, this […] this […] this suffering […]
`Lord this ~have this [?] this suffering [?]`

**3**  […] the angel […] offered the Lord […]
`[?] angel [?] this-Lord offer [?]`

**4**  the Lord's lot, of God the Father; the Son Jesus […]
`<of>-Lord fate <of>-father-<divine> son Jézus [?]`

**5**  all […] redeemed. And the angel departed from before
`each,_every [?] from-buy and leave-to-leave angel before`

**6**  the Lord Jesus; because every night the angel came from on high, from God the Father,
`Lord-Jézus because each,_every night this-go angel high from-father-<divine>`

**7**  to the Lord Jesus; because the angel bore for the Lord all his suffering,
`to-Lord-Jézus because Lord carry angel each,_every <of>-Lord suffering`

**8**  it is written; and […] truly […] […] […]
`write and [?] righteous(ly) [?] [?] [?]`

**9**  written. And the Lord went to the apostles […] the Lord Jesus
`write and go-Lord to-apostle [?] Lord-Jézus`

**10**  […] his […]; and the Lord and the apostles had one […]
`[?] <of>-Lord and have-Lord-apostle one [?]`

**11**  […]; and then […] […]; and then the apostles |
`[?] and then-exist [?] [?] and then-exist apostle | to`

> Luke 22:43, the angel from heaven strengthening him.

## 035r — the sign, and the kiss

**1**  slept. And the Lord Jesus could not sleep; but the Lord laid a stone
`sleep and can sleep Lord-Jézus a) Lord-put one stone`

**2**  at his head; and the Lord Jesus could not sleep; but […]
`to-head and can sleep Lord-Jézus a) [?]`

**3**  […] the Lord, the apostles […] the apostles […] […] […]
`[?] Lord apostle [?] apostle [?] [?] [?]`

**4**  […] because from […] came the Jews […]
`[?] because from [?] go Jew(ish) [?]`

**5**  […] the Son of God […] to take him. And then
`somebody-<divine> son [?] capture and then-exist`

**6**  the Lord and the apostles went on the way, and saw | the Lord
`Lord apostle and apostle go-Lord-and-apostle on-way and see | Lord`

**7**  Jesus a great crowd coming; and among the Jews was Judas.
`Jézus many people-chapter go and among Jew(ish) exist Judas`

**8**  […] the father died, and the mother […] […] Judas and the Jews.
`[?] from-father die and mother [?] sleep [?] Judas and Jew(ish)`

**9**  He gave a sign, to tell the Lord apart from James and John — a kiss —
`ask_for_sign distinguish Lord James John [?] kiss`

**10**  so that Judas […] the Jews might take the Lord. And then
`Judas from Lord capture Jew(ish) and then-exist`

**11**  Judas went up to the Lord Jesus; and […]
`go Judas against Lord-Jézus and [?]`

**12**  Judas […] the Lord's hand; because he had given the Jews the sign,
`~Judas <of>-Lord hand because to-Jew(ish) ask_for_sign`

> Matthew 26:48, "he gave them a sign". The codex adds the reason the sign
> was needed, on the next page.

## 035v — "Whom seek ye?" and they fell backward

**1**  because John was like the Lord Jesus. And he cried out, | the Lord
`because exist similar John to-Lord-Jézus ~and shout | Lord`

**2**  Jesus: Whom seek ye? The people, the Lord's — the Jews. And they cried,
`Jézus who(m)? search people <of>-Lord Jew(ish) and shout`

**3**  the Jews […] […] Jesus […]; and cried
`Jew(ish) [?] [?] Jézus [?] and shout`

**4**  the Lord Jesus: I am he, if ye seek the Lord — the Jews. And all
`Lord-Jézus from this-Lord if Lord search Jew(ish) and each,_every`

**5**  the Jews fell backward […] the Lord Jesus […] […]
`Jew(ish) back bow_down [?] Lord-Jézus [?] [?]`

**6**  […] […] hidden […] staves; and […] […]; and the Jews'
`[?] [?] hide_oneself <of>-club and [?] [?] and <of>-Jew(ish)`

**7**  staves […] because the Lord Jesus […]
`club [?] inside why?-in_turn because Lord-Jézus [?]`

**8**  did; God his Father, to the Jewish people; and
`do, father-<divine> <of>-Lord to-Jew(ish) people and`

**9**  […] […]; and a second time the Lord Jesus cried: […] seek ye,
`[?] [?] and two shout Lord-Jézus [?] search`

**10**  the people, the Lord's — the Jews. And they cried […]
`people <of>-Lord Jew(ish) and shout [?]`

**11**  […] […] Jesus […]; and cried
`[?] [?] Jézus [?] and shout`

**12**  the Lord Jesus: I am he, if ye seek the Lord — the Jews; and
`Lord-Jézus from this-Lord if Lord search Jew(ish) and`

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

**1**  A king, and the Lord God begins […] […] […]
`king and Lord-<divine> begin [?] [?] [?]`

**2**  […] […] […] would a man, the Lord God […]
`have [?] to [?] want somebody this Lord-<divine> [?]`

**3**  forgive the debt. And behold, the Lord God the king […]
`remit indebted ~and see this Lord-<divine>-king [?]`

**4**  The servant of the Lord God the king humbled himself — the man-servant — and
`~humble this servant <of>-Lord-<divine>-king somebody-servant and`

**5**  the man had mercy, the Lord God the king; and the man forgave all […]
`somebody have_mercy this Lord-<divine>-king and somebody have_mercy each,_every [?]`

**6**  of the man's sin. And the man went […] to his
`<of>-somebody sin and somebody go-angel <of>-somebody`

**7**  home. And then, as the man went on, the fellow-servant
`home and then-exist keep_going-somebody this heavenly servant`

**8**  of his household — and then he met one | God
`<of>-somebody home and then-exist appear one | God`

**9**  the man, this man, the fellow-servant; and the man was
`somebody this somebody heavenly servant and somebody exist`

**10**  in debt […] pence; and the man of God began to demand it.
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

**1**  […] […] and the scribes murmured at the Lord Jesus, that the Lord spoke
`[?] [?] and church_father murmur on-Lord-Jézus this-Lord speak`

**2**  [as] the Son of God; and when the Lord was the Son of God | this
`son God in_turn then-exist this-Lord exist son God | this`

**3**  Lord […] went, this […] […] the Lord Jesus | when
`Lord [?] go this [?] [?] Lord-Jézus | then`

**4**  What man is there among you | who has one
`exist one have among you | one`

**5**  hundred sheep in the wilderness, and if he lose one
`hundred sheep inside field and then-exist lose one`

**6**  of them […] […] […] the man is […] the lost one […]
`among [?] [?] [?] somebody exist [?lost] [?]`

**7**  and does he not leave the ninety sheep and nine
`and exist from-food-somebody from nine-ten sheep and nine`

**8**  in the wilderness, and go, the man […] nine, [after] the lost one
`inside field and go-somebody [?] nine [?lost]`

**9**  to find it; and when he finds the lost one,
`find and then-exist [?lost] find-somebody`

**10**  and the man takes it up […] | upon
`and [?lost] grab-somebody [?] | on`

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

**1**  All the Jews fell backward […] the Lord Jesus […] […]
`each,_every Jew(ish) back bow_down [?] Lord-Jézus [?] [?]`

**2**  […] hidden […] staves; and […] […] and the
`[?] hide_oneself <of>-club and [?] [?] and <of>`

**3**  Jews' staves […] because | the Lord
`Jew(ish) club [?] inside why?-in_turn because | Lord`

**4**  Jesus […] […] God his Father, to the Jewish
`Jézus [?] [?] father-<divine> <of>-Lord to Jew(ish)`

**5**  people; and […] […]; and a third time he cried | the Lord
`people ~and [?] [?] and +three shout | Lord`

**6**  Jesus: Whom seek ye? The Lord's […] the Jews;
`Jézus [?] search <of>-Lord Jew(ish)`

**7**  and the Jews cried, they answered:
`and shout Jew(ish) +say +answered`

**8**  Jesus of Nazareth. And the Lord Jesus cried: I am he.
`Jézus +Nazareth and shout Lord-Jézus from this-Lord`

**9**  If ye seek the Lord — the Jews. And then the Lord Jesus cried:
`if Lord search Jew(ish) +and_then shout Lord-Jézus`

**10**  Take me, ye Jews, for I go […] to God my Father.
`grab Jew(ish) Lord because go [?] <of>-Lord father-<divine>`

**11**  And then the Jews […] the Jews, the Lord Jesus […]
`and then-exist ~Jew(ish) from-leave-leave Jew(ish) Lord-Jézus [?]`

> The exchange runs three times here, and John 18 gives it twice with the
> third cry implied. "Jesus of Nazareth" is the answer, and it is the sign
> this project read as Nazareth on its six occurrences.

## 036v — Malchus, and the ear put back

**1**  He cut off […] […] the ear of one of the Jews,
`cut_off [?] [?] ear one Jew(ish)`

**2**  and that Jew was Malchus. And then
`and [?] Jew(ish) exist Malchus +and_then`

**3**  the Lord Jesus [said]: Peter, Peter, […] thou hast cut off […] because
`Lord-Jézus Peter Peter [?] cut_off [?] because and`

**4**  the man Peter […] cut off from […]
`somebody Peter [?] cut_off from [?]`

**5**  […] […] die. And the Lord Jesus took the ear
`[?] [?] die and grab Lord-Jézus this ear`

**6**  and put it back in its place, and the ear was made
`and [?] put on-place and healing ear`

**7**  whole. And the Lord Jesus [did] that miracle before the heathen […]
`leave-to-leave and from Lord-Jézus on-pagan miracle [?]`

**8**  and […] said, and believed in the Lord; but his […] |
`and [?] +say inside Lord believe a) <of>-Lord [?] | on`

**9**  the Lord […]; and one of the Jews fled,
`Lord [?] and escape one Jew(ish)`

**10**  and believed in the Lord Jesus; and from […] the Lord Jesus
`to-Lord believe Lord-Jézus and from [?] to-Lord [?] Lord-Jézus`

**11**  all said […] these Jews went; and […] from […]
`each,_every +say [?] this-who Jew(ish) go and [?] from [?]`

**12**  […] And then the Lord could have fled — the Lord did not flee,
`[?] and then-exist Lord want escape exist Lord not escape`

**13**  but […] […] the apostles, the Jews […] […]
`a) good [?] [?] apostle Jew(ish) [?] [?]`

> John 18:10 names the servant Malchus, and Luke 22:51 has Jesus touch the
> ear and heal it. The codex has both, and adds that the bystanders believed
> because of it.

## 037r — bound, and struck

**1**  […] and […] led the Lord […]
`[?] and [?] carry to-Lord [?]`

**2**  the Lord Jesus; and then […] the hands of the Lord Jesus Christ
`Lord-Jézus and then-exist [?] hand Lord-Jézus-Christ`

**3**  […] all […] […] […]; and then […]
`[?] each,_every to-<of>-Lord to-year-to [?] [?] and then-exist [?]`

**4**  they went to the chief of the Jews […]; and then the Lord
`go to-Jew(ish) head [?] and then-exist Lord`

**5**  went down from the mountain; and many […] […]
`go down on-to-mount and many [?] [?]`

**6**  Jews upon the Lord Jesus, because one struck the Lord
`Jew(ish) on-Lord-Jézus because Lord one [?] beat`

**7**  […] […] secondly, to the Lord's house […] thirdly
`[?] [?] in_turn-two to-Lord to-house [?] +third`

**8**  […] no man at all had mercy on the Lord Jesus.
`to-Lord [?] from not-not <of>-somebody have_mercy Lord-Jézus`

**9**  And then through […] through […] […]
`and then-exist through [?] through [?] [?]`

**10**  and the Lord […] went over the bridge […]
`and Lord [?] on-bridge go [?]`

**11**  but the Lord on the bridge […]; and […] […]
`a) Lord on-bridge [?] and to-Lord [?] [?]`

**12**  no man had mercy on the Lord Jesus, because […] the Jews went
`<of>-somebody have_mercy Lord-Jézus because Lord two [?] go Jew(ish)`

## 038r — bound before Caiaphas

**1**  […] they bound the Lord Jesus Christ; and then the Lord
`[?] who-chain-to Lord-Jézus-Christ and then-exist Lord`

**2**  […] and dragged him out […]; no man had mercy
`exist and out(ward)-out(ward) draw [?] <of>-somebody have_mercy`

**3**  on the Lord Jesus Christ. And then the Jews […] the Lord would
`Lord-Jézus-Christ +and_then Jew(ish) [?] Lord want`

**4**  the Jews went […] one […] the Lord |
`Jew(ish) go [?] one [?] Lord | to`

**5**  Pilate; secondly […] to Caiaphas; and | when
`Pilate in_turn-two say [?] to-Caiaphas and | then`

**6**  the Lord […] to Caiaphas the high priest. And then
`exist Lord [?] to-Caiaphas high_priest +and_then`

**7**  the Jews […] accused the Lord; and then
`Jew(ish) [?] Lord [?] accuse and then-exist`

**8**  the Lord […] before the high priest's house; and | when
`Lord [?] before <priest> high_priest house and | then`

**9**  the Lord […] […] the Lord this […]
`exist Lord [?] [?] Lord this [?]`

**10**  and then the Lord […] into a house; and | when
`and then-exist Lord [?] inside one house and | then`

**11**  the Lord […] one […] […] | not at all
`exist Lord from-to-each,_every one [?] [?] | not-not`

**12**  the Lord Jesus Christ said. And then Peter, one
`+say Lord-Jézus-Christ +and_then Peter one`

## 038v — the first denial, and Caiaphas's counsel

**1**  of the Jews, this Malchus whose ear was cut off […]
`Jew(ish) this Malchus ear cut_off [?]`

**2**  Peter […] this Peter […] and this was
`Peter [?] this-Peter and-to-Lord-to-Peter and this from`

**3**  the first denial of the Lord Jesus, because Peter said […] the Lord, and denied him.
`first denial Lord-Jézus because say Peter [?] Lord and-to-Lord-to`

**4**  And […] the Lord Jesus [was brought] to Caiaphas the high priest; and | when
`and [?] Lord-Jézus to-Caiaphas high_priest and | then-exist`

**5**  he said, the Lord went before Caiaphas; and there cried
`+say to-Lord go before Caiaphas and shout`

**6**  the Jews […] […] this went […]
`Jew(ish) [?] [?] go this [?]`

**7**  this […] the Lord; and to the Lord […] of the apostles
`this [?] Lord and to-Lord +<subject_marker> from apostle-exist-exist`

**8**  […] […] all the people against the Lord […] | and
`food [?] each,_every people on-Lord [?] | in_turn`

**9**  the second said: the Son of God; the third said: the king.
`two [?] say son God +third [?] king`

**10**  Caiaphas said: it is written, it is good that one man
`say say Caiaphas write +<subject_marker> good one Lord-somebody`

**11**  should die rather than all […] […]; and […] […]
`die [?] rather each,_every [?] [?] and [?] [?]`

**12**  the high priest […] in the house, among the apostles Christ […]
`apostle-high [?] inside house among apostle Christ look_up leave [?]`

> Line 10 is John 11:50 and 18:14 — Caiaphas's counsel that it was expedient
> that one man should die for the people. The denials are numbered as the
> signs of Christ were: first, second, third.

## 039r — the second denial

**1**  Saint Peter before the gate; and then Peter was
`holy-Peter before ~gate and then-exist Peter exist`

**2**  seen by the maid at the Jews' gate. And then the maid [said] to Peter:
`see from-handmaid ~gate Jew(ish) +and_then handmaid this-Peter`

**3**  art thou an apostle of this Jesus? Peter said […] and denied him.
`apostle this Jézus say Peter [?] and-to-Lord-to [?]`

**4**  This was the second denial of the Lord Jesus, because Peter said […] the Lord |
`this two denial Lord-Jézus because say Peter [?] Lord | [?]`

**5**  and denied him. And John […] […]
`to-Lord-to in_turn John [?] [?]`

**6**  was known to the high priest. Caiaphas said to Jesus: sayest thou
`acquaintance this high_priest say Caiaphas to-Jézus this-Lord say`

**7**  the Son of God? And how dost thou truly preach? Jesus said
`son God in_turn how? this righteous(ly) preach say Jézus`

**8**  to Caiaphas […] Caiaphas […] answered […]
`to-Caiaphas from-judge-Caiaphas from +say [?]`

**9**  hear my preaching […] truly […]
`hear preach [?] ~righteous(ly) [?]`

**10**  And then Caiaphas, this Caiaphas, and […] in the Lord […]
`+and_then Caiaphas this-Caiaphas and [?] inside Lord [?]`

**11**  Caiaphas […] the Lord […] the man; Caiaphas said
`Caiaphas-year [?] this-Lord [?] somebody say Caiaphas`

**12**  […] the Lord […] […] to Caiaphas […]
`[?] Lord [?] [?] to-<of>-Caiaphas exist-exist`

> John 18:15–17: the maid at the door, the other disciple known to the high
> priest, and Peter's denial. The codex names the disciple John.

## 039v — before Pilate

**1**  And this […] the two […]; and the Lord […] |
`and this ~out(ward) two [?] and Lord [?] | to`

**2**  Pilate; and they accused the Lord […]
`Pilate and from Lord [?] accuse [?]`

**3**  […] Pilate; the Lord went […] and | when
`[?] Pilate go this-Lord half-believe and | then`

**4**  he said: they have done nothing at all against the Lord.
`exist +say many not-not on-Lord do,`

**5**  The Lord went before Pilate, because all his […] |
`go Lord before Pilate because each,_every <of>-Lord [?] | on`

**6**  the Lord […] and his holy face […] and | when
`Lord from [?] and <of>-Lord holy-face each,_every [?] and | then`

**7**  the Lord […] said […] […] […]; no man
`exist Lord exist +say [?] [?] [?] <of>-somebody`

**8**  had mercy on the Lord Jesus. And then the Lord said, and went
`have_mercy Lord-Jézus and then-exist Lord exist +say go`

**9**  to Pilate. And then the Jews [said] to Pilate: the Lord
`to-Pilate +and_then Jew(ish) this Pilate +say Lord`

**10**  went […]; and the Lord […] | of the apostles
`go this-Lord half-believe and Lord +<subject_marker> from | apostle-exist`

**11**  […] […] all the people against the Lord […]
`exist food [?] each,_every people on-Lord [?]`

**12**  The second said: he saith he is the Son of God. The third said:
`in_turn-two say +say say son God +third say +say`

## 040r — the third denial, and the cock

**1**  he saith he is king. And then Peter went to a
`king say and then-exist Peter go to-one`

**2**  […] […] because […] […] […]
`[?] [?] because exist virgin-cut_off [?] [?]`

**3**  […] […] […] said one of the Jews to him:
`want [?] [?] say one Jew(ish) to`

**4**  […] art thou an apostle of this Jesus?
`[?] this apostle [?] this Jézus`

**5**  Peter said […] and denied him,
`say Peter grab God this-Peter [?]`

**6**  and this was the third denial of the Lord Jesus; and at that moment the cock crew.
`and this +three denial Lord-Jézus and time crow cock`

**7**  And Peter said […] Peter went out: Master,
`and say Peter this +<subject_marker> out(ward) [?] Peter Master`

**8**  he spoke, and sorrowfully […] went out. And then Pilate
`speak and sad(ly) [?] leave-to-leave +and_then Pilate`

**9**  [said] to Jesus: sayest thou that thou art the Son of God? And how dost thou
`to-Jézus this Lord say son God in_turn how? this [?]`

**10**  preach? The Lord Jesus said to Pilate; Pilate
`preach say Lord-Jézus to-Pilate from-judge-Pilate`

**11**  answered […]: hear my preaching […]
`from +say [?] Lord-to hear preach [?]`

**12**  […] preach. And Pilate […]; the Lord Jesus spoke
`[?] preach and Pilate [?] from speak Lord-Jézus`

## 040v — two lines

**1**  but the Lord said […] with his own mouth, that he is
`a) say Lord [?] +<subject_marker> mouth [?] this-Lord`

**2**  truly the Son of the living God.
`righteous(ly) son living God`

## 041r — art thou the king of the Jews

**1**  And then Pilate [said] to the Lord: speakest thou, Lord, king of the Jews?
`+and_then Pilate this Lord speak Lord king Jew(ish)`

**2**  The Lord Jesus said to Pilate […] Pilate's mouth
`say Lord-Jézus this Pilate +<subject_marker> [?] Pilate mouth`

**3**  […] that he is truly the Son of the living God […]
`[?] this-Lord righteous(ly) son living God [?]`

**4**  Pilate […] truly this man; Pilate
`Pilate this-Lord +<subject_marker> righteous(ly) somebody this Pilate`

**5**  how […] in the Lord […]; and there cried
`how? [?] inside Lord [?] and shout`

**6**  the Jews […] the Lord. Pilate: the cross! The Lord [is] accursed, this
`Jew(ish) [?] Lord Pilate +cross Lord cursed this`

**7**  Pilate […] would say the Lord, say […]
`Pilate this-hide_oneself want +say Lord +say [?]`

**8**  […] truly […]. And then […]
`[?] righteous(ly) [?] +and_then [?]`

**9**  […] they took the Lord, saying; and the Lord […]
`[?] grab Lord +say and Lord [?]`

**10**  Herod, Pilate's […]; and then […] […]
`~Herod <of>-Pilate [?] and then-exist ~out(ward) [?]`

**11**  the hour; and then the Lord […] […]
`hour and then-exist Lord [?] [?]`

**12**  king; and then, and […] upon one
`king and then-exist and [?] on-one`

## 041v — sent to Herod, because he is of Galilee

**1**  […] […]; and then all cried out, the four […]
`love [?] and then-exist from shout each,_every two-two [?]`

**2**  the Lord […] this […] the Lord […]
`Lord [?] this [?] this-Lord [?]`

**3**  this Jesus blasphemeth; and the Lord is out of Galilee,
`this blasphemer-Lord this Jézus and +<subject_marker> Lord from Galilee`

**4**  he cometh […]; all the people against the Lord […]
`protrude [?] each,_every people on-Lord [?]`

**5**  And then the Lord […] many judged […]
`and then-exist Lord [?] many judge [?]`

**6**  Herod the king, because […] the Jews would […] the Lord
`Herod king because [?] Jew(ish) to-Lord want`

**7**  to Herod […]; and the Lord […]
`Herod [?] and Lord [?]`

**8**  Herod […]; but […] shone […]
`Herod [?] a) [?] shine [?]`

**9**  Herod, the Lord Jesus Christ; and then the Lord […] before
`Herod Lord-Jézus-Christ and then-exist Lord [?] before`

**10**  Herod the king; and the Jews cried […]
`Herod king and shout Jew(ish) [?]`

**11**  Herod said: the Lord went […]; and the Lord
`Herod +say Lord go this-Lord begin-believe and Lord +<subject_marker>`

**12**  is out of Galilee, he cometh […] all
`from Galilee protrude [?] each,_every`

> Luke 23:6–7 — Pilate hears Galilee and sends him to Herod.

## 042r — four lines

**1**  the people against the Lord […]; and the Lord said, the Son
`people on-Lord [?] and Lord say son`

**2**  of God. And then the false […] said of the Lord, and
`God +and_then ~false [?] say Lord and`

**3**  […] this […] destroy | he would
`[?] this exist-chapter destroy | want`

**4**  the Lord, that he […] all […]
`Lord this-Lord food [?] each,_every [?]`

## 042v — Herod questions him

**1**  and […] confessed it […] Herod; but […]
`and [?] to-this confess [?] Herod a) [?]`

**2**  Herod said: Lord — Herod […] God, that the Lord is the Son; and
`Herod say Lord Herod [?] God this Lord son and`

**3**  one said, spoke of the Lord Jesus against Herod; and
`one say speak Lord-Jézus ~against Herod and`

**4**  Herod […] Herod […] Herod the king […]
`Herod [?] Herod [?] this-Herod king [?]`

**5**  the Lord […] Herod […] this death […] […]
`this-Lord can Herod [?] this die [?] [?]`

**6**  the Lord […] Herod said to him, Herod said […]
`this-Lord [?] Herod to say say Herod [?]`

**7**  to Herod: the Lord of the living God […]; Herod said […]
`to-Herod this Lord-to living God [?] say Herod [?]`

**8**  God — that he is the Son; and […] the Lord […]
`God this-Lord son and [?] Lord [?]`

**9**  his Father […]. And then the Lord Jesus to Herod | that
`<of>-Lord father [?] +and_then Lord-Jézus to-Herod | this`

**10**  the Lord is truly the Son of the living God. The Lord Jesus said: the Lord goeth
`Lord righteous(ly) son living God say Lord-Jézus this-Lord go`

**11**  to his Father […] to judge the living and the dead;
`<of>-Lord father [?] judge living and die`

**12**  and Herod did so: he brought a stone and […]
`and do, Herod carry stone and [?]`

> Line 11 is the creed again: he shall come to judge the quick and the dead.

## 043r — Herod hoped to see a miracle

**1**  a vessel of water, and […] various
`one vessel water and [?] various`

**2**  […] before the Lord Jesus; and the Lord was asked
`[?] before Lord-Jézus and Lord ~ask_(for)`

**3**  by Herod, when the Lord [stood] before him, to do a miracle;
`Herod then-exist-Lord before miracle do,`

**4**  and they set a yoke before the Lord Jesus, and […]
`and yoke Lord-Jézus before and understand-eat`

**5**  to do a miracle, because when […] before
`miracle do, because then-exist [?] before`

**6**  Herod he did no miracle, though the Lord took […]
`miracle do, why?-Lord grab [?]`

**7**  […] but Herod said […] the Lord […]
`[?] a) say Herod [?] this Lord [?]`

**8**  Pilate became Herod's brother […] who
`Pilate to-<of>-Herod brother [?] who`

**9**  […] the Lord, because […] upon the Lord, Pilate did.
`[?] this-Lord because on-Lord do, Pilate`

**10**  And the Lord […] before Pilate, many […]
`and Lord [?] before Pilate many [?]`

**11**  And this was […] the sixth hour; and the Lord […] before
`and this ~out(ward) six hour and Lord [?] before`

**12**  Pilate. And then the Jews [said to] Pilate; Pilate said
`Pilate +and_then Jew(ish) Pilate say this-Lord Pilate +<subject_marker>`

> Luke 23:8, Herod hoped to see a miracle, and 23:12, Pilate and Herod were
> made friends that same day — here "Pilate became Herod's brother". John
> 19:14 puts the judgment at the sixth hour, and line 11 has it.

## 043v — the scourging

**1**  Herod […]; and Pilate […] the Jews would
`Herod [?] in_turn-who-Lord this Pilate [?] want Jew(ish)`

**2**  the Lord. He said […] […] truly […]
`Lord +say [?] [?] righteous(ly) [?]`

**3**  And then Pilate […] the soldiers; the soldiers brought him [to] Pilate,
`+and_then Pilate understand-eat soldier carry-soldier Pilate`

**4**  the two […] […]; and then Pilate said, bring
`two [?] [?] and then-exist Pilate +say carry`

**5**  the two […] […]; and the Lord […] the gate
`two [?] [?] and Lord gate [?]`

**6**  […] […]; and Pilate took | two
`understand-eat ~until and grab Pilate | two`

**7**  two soldiers to the Lord Jesus, and the Lord was scourged; and then
`two soldier to Lord-Jézus and Lord exist whip and then-exist`

**8**  the two […] flogged the Lord Jesus; and a second time the Lord
`two from [?] flog Lord-Jézus in_turn-two Lord`

**9**  the second began, saying, to flog; and then the second, and the second said,
`begin two +say flog and then-exist two and from two +say`

**10**  […] flogged the Lord Jesus Christ; and | there came
`from [?] flog Lord-Jézus-Christ and | leave`

**11**  one soldier to the Lord Jesus; and then
`to-leave one soldier to Lord-Jézus and then-exist`

**12**  […] the Lord Jesus, because the Lord had many […]
`from [?] Lord-Jézus because exist Lord many [?]`

## 044v — the purple robe and the crown of thorns

**1**  And then the Lord […]; they bowed before the Lord Jesus; and
`and then-exist Lord [?] bow_down Lord-Jézus and`

**2**  the Lord […] […] […]; and the Lord […]
`Lord [?] [?] [?] and Lord [?]`

**3**  […] a purple robe; and the Lord,
`[?] understand-eat purple_robe and Lord`

**4**  thorns […] upon his head […]
`thorn [?] on-head [?]`

**5**  and they set the Lord upon a seat; and
`and Lord sit on-understand-eat chair and`

**6**  […] knelt before the Lord Jesus, and
`[?] kneel_(down) before Lord-Jézus and`

**7**  spoke: Hail, Jesus, this day! And […] […]
`speak healing Jézus today-this and leave-to-leave [?]`

**8**  […] the soldiers […] […] […] the Lord Jesus; and
`understand-eat soldier [?] [?] [?] Lord-Jézus and`

**9**  […] […] […] the Lord Jesus; and then
`[?] from [?] [?] Lord-Jézus and then-exist`

**10**  the Lord […] bowed; and the Jews took the Lord,
`Lord [?] bow_down and Lord grab Jew(ish)`

**11**  and the Jews led the Lord to Pilate, into the house.
`and Lord go Jew(ish) to Pilate inside house`

> John 19:2–3: the purple robe, the crown of thorns, and Hail, King of the
> Jews, with the kneeling. The codex keeps the mockery of the kneeling.

## 045v — twelve legions of angels

**1**  And the Lord sat […] in a judgment seat |
`and Lord sit +say inside one throne | on`

**2**  in the midst […]; and then Pilate knelt
`middle ~until and then-exist kneel_(down) Pilate`

**3**  before the Lord Jesus, and Pilate said: Hail, Lord, King
`before Lord-Jézus and say Pilate healing Lord king`

**4**  of the Jews! And the Lord Jesus said to Pilate […]
`Jew(ish) and say Lord-Jézus to-Pilate [?]`

**5**  speakest thou that the Lord is King of the Jews? Because | when
`speak because this-Lord king Jew(ish) because | then`

**6**  […] his Father God, ye
`exist [?] <of>-Lord father-<divine> you`

**7**  took the Lord prisoner; for if the Lord would,
`Lord take_prisoner because then-exist this-Lord want Lord`

**8**  the Lord would ask of God his Father | twelve
`this-Lord ask_(for) from <of>-Lord from-father God | six`

**9**  legions of angels […] the Lord,
`six [?] in_turn angel [?] this-Lord`

**10**  that ye took him prisoner; because
`you grab take_prisoner because then-chapter`

**11**  if the Lord would, the Lord could […] you all
`this-Lord want this-Lord you each,_every can`

> Matthew 26:53 — "more than twelve legions of angels". The twelve is
> written six and six across the margin break, the same way the twelve
> apostles are written at 022r:10.

## 046r — Barabbas, and Behold the man

**1**  the Lord die […]; and ye took
`Lord die [?] and you grab`

**2**  the Lord prisoner. And Pilate said to Jesus:
`Lord take_prisoner and say Pilate to-Jézus this`

**3**  sayest thou, Lord, the Son of God? And one said
`Lord say son God and one say`

**4**  […] the Lord Jesus said to Pilate; and he released
`[?] say Lord-Jézus to-Pilate and leave-chapter-leave`

**5**  Barabbas […] Jesus; and they beat the Lord,
`Barabbas to-Jézus and Lord beat [?]`

**6**  […] […] […] all his […]
`[?] [?] [?] each,_every <of>-Lord [?]`

**7**  quaked; and Jesus said […] the soldier, Barabbas, truly
`quake and say Jézus this soldier Barabbas this righteous(ly)`

**8**  the Lord spoke […] they beat him; the scribes spoke,
`speak-Lord to-inside-Lord beat speak church_father`

**9**  it is written […]; and […] […] they beat him.
`write [?] exist and [?] [?] beat`

**10**  O! O! And so they did to the Lord.
`chapter-oh chapter-oh and Lord do,`

**11**  Pilate went out of the house, and cried,
`Pilate out(ward) go on-house and shout-to`

**12**  Pilate: Behold Jesus, […] the King of the Jews!
`Pilate lo Jézus [?] king Jew(ish)`

> John 19:14, "Behold your King!", and Barabbas from all four gospels.

## 046v — crucify him, the second time

**1**  […] and the angel […] Bethlehem […]
`[?] in_turn angel Bethlehem [?]`

**2**  And the Jews cried: the cross for the Lord! Pilate: the Lord is accursed,
`and shout Jew(ish) +cross Lord Pilate cursed Lord`

**3**  […] if ye will the Lord. He said […] […]
`[?] if want Lord +say [?] [?]`

**4**  truly […]; and Pilate said to the soldiers, lead the Lord
`righteous(ly) [?] and say Pilate to soldier go Lord`

**5**  into the house. And a second time the Lord […] went into the house,
`inside house and two Lord [?] go on-house`

**6**  and Pilate cried: Behold Jesus […]
`and shout Pilate lo Jézus [?]`

**7**  the King of the Jews! […] and the angel |
`king Jew(ish) [?] in_turn angel | to`

**8**  [to] Bethlehem […] and […]
`Bethlehem [?] and [?]`

**9**  the Jews: the cross for the Lord! Pilate: the Lord is accursed, this
`Jew(ish) +cross Lord Pilate cursed Lord this`

**10**  Pilate, if ye will the Lord. He said […] […]
`Pilate if want Lord +say [?] [?]`

**11**  truly […]; and Pilate said to the soldiers, lead the Lord
`righteous(ly) [?] and say Pilate to soldier go Lord`

## 047r — the third time, and Caesar

**1**  into the house. And a third time the Lord […] went into the house,
`inside-house and +three Lord [?] go on-house`

**2**  and Pilate cried: Behold Jesus […]
`and shout Pilate lo Jézus [?]`

**3**  the King of the Jews! […] and the angel
`king Jew(ish) [?] in_turn angel`

**4**  [to] Bethlehem […]; and there cried
`to-Bethlehem [?] and shout`

**5**  the Jews: the cross for the Lord! Pilate: the Lord is accursed […]
`Jew(ish) +cross Lord Pilate cursed Lord [?]`

**6**  Pilate, if ye will the Lord. He said […] |
`Pilate if want Lord +say [?] | [?]`

**7**  Caesar truly […]. And then the Jews
`emperor righteous(ly) [?] +and_then Jew(ish)`

**8**  […] that the Lord is King of the Jews […]
`[?] this-Lord king Jew(ish) [?]`

**9**  half […] the Lord, half […] one
`half one Lord half-believe one`

**10**  the Lord blasphemeth. And Pilate cried, Pilate,
`blasphemer-Lord and shout Pilate this Pilate`

**11**  and how […] in the Lord […] Pilate, that he is
`and how? [?] inside Lord [?] Pilate this-Lord +<subject_marker>`

> John 19:12, Caesar. The Ecce Homo is put three times, first second third,
> the way the codex numbers everything.

## 047v — Pilate washes his hands

**1**  truly this man. And then Pilate […] water
`righteous(ly) somebody +and_then Pilate [?] water`

**2**  in a basin, and […] […]
`inside one washdish and [?] [?]`

**3**  brought it, and […] the two […]. And then
`carry and [?] <of> two why?-in_turn +and_then`

**4**  Pilate […]: I am innocent of this Lord's blood. And then
`Pilate [?] innocent from <of>-Lord [?] +and_then`

**5**  the Jews, because this was […] and […] the son;
`Jew(ish) because this exist [?] and [?] son`

**6**  and Pilate cried: whom will ye |
`and shout Pilate who want | [?]`

**7**  that I release, Barabbas or Jesus? And
`to +say release Barabbas in_turn Jézus and`

**8**  the Jews cried: release […] Barabbas,
`shout Jew(ish) release [?] Barabbas`

**9**  and Jesus to the cross! And then Pilate […]
`in_turn Jézus +cross [?] +and_then Pilate understand-eat`

**10**  the soldiers led the Lord […] into the house; and then Pilate,
`soldier go Lord [?] on-house and then-exist Pilate this-who`

**11**  the Lord went […] […] into the house; and Pilate cried |
`Lord go [?] [?] on-house and shout Pilate | from`

> Matthew 27:24, the basin and "I am innocent of the blood of this just
> person", with the choice of Barabbas right after it.

## 048r — the Reproaches: O my people, what have I done to thee

**1**  […] this man truly took […] because
`+<subject_marker> somebody righteous(ly) grab [?] because +<subject_marker>`

**2**  […] the Lord […]; and the Lord […]
`[?] Lord-to [?] and Lord [?]`

**3**  Pilate went out of the house […] among […]
`Pilate out(ward) go on-house [?] among from [?]`

**4**  […] and the Lord Jesus cried: O my people,
`[?] and shout Lord-Jézus people-chapter`

**5**  the Lord's people, the Jews, who […] […]
`<of>-Lord Jew(ish) who this-Lord [?] [?]`

**6**  I loved this people […] […] the people,
`to-love this-people-chapter [?] [?] people-chapter`

**7**  the Lord's, the Jews, who […] this people, through sin
`<of>-Lord Jew(ish) who this-Lord this-people-chapter through sin`

**8**  […] I did good to this people […] the Lord
`[?] this-people-to good [?] then-exist-Lord this-Lord`

**9**  among this people did miracles. First, |
`among this-people-to miracle do, first | this`

**10**  this people went into Egypt […] as servants;
`people-chapter go on-Egypt [?] living-servant this`

**11**  over […] […] I divided
`over [?] [?] divide`

## 048v — forty years in the wilderness, and a cross for their Saviour

**1**  in two parts, this people, over the sea;
`on-two direction this-people-chapter over sea`

**2**  through […] the Lord led them by day, and from the beginning
`through [?] go-Lord +day in_turn from head`

**3**  all […] to this people, the whole wide world |
`each,_every [?] to-<of>-people-chapter ~the_whole_wide_world | this`

**4**  I kept this people alive forty years in the wilderness,
`people [?] living-Lord two-two-ten-year inside field`

**5**  and the angel […] to this people;
`in_turn angel [?] to-this-people-chapter`

**6**  […] […] I did for the Lord's people,
`[?] [?] do, people <of>-Lord`

**7**  the Jews […]; they lifted up the Lord on Palm Sunday |
`Jew(ish) [?] to-Lord-to lift_up on-Palm_Sunday | then`

**8**  they would make the Lord king, a crown, and […]
`chapter-Lord want king crown in_turn [?]`

**9**  […] his […] lifted up upon the cross;
`[?] <of>-Lord [?] +cross lift_up-to`

**10**  and Pilate cried […] the Lord […]
`and shout Pilate [?] Lord [?]`

**11**  and the Lord […] the Jews; and then he said
`and Lord [?] Jew(ish) and then-exist +say`

> This is the Improperia, the Reproaches sung on Good Friday: *O my people,
> what have I done unto thee? I brought thee out of Egypt, I divided the
> sea, I led thee forty years through the wilderness, and thou hast
> prepared a cross for thy Saviour.* It is liturgy, not gospel, and the
> codex has it in order, with forty written the way it is written of the
> flood.

## 049r — the two thieves, and Mary Magdalene told

**1**  They brought two thieves to the Lord Jesus, and set
`to-go +say two ~thief to Lord-Jézus and put`

**2**  […] upon the Lord Jesus; and of the two thieves |
`+say [?] on-Lord-Jézus in_turn from two ~thief | carry`

**3**  […] […] the good one […] […] the Lord Jesus.
`+say [?] good from [?] [?] Lord-Jézus`

**4**  And Saint John went up into Bethany, to
`and to-go up holy-John inside Bethany to`

**5**  Mary Magdalene: […] Master, the Lord liveth […]
`two-Mary Magdalene good [?] Master living Lord [?]`

**6**  to Mary Magdalene […]; and he said
`to-Mary Magdalene [?] and +say +<subject_marker>`

**7**  […]; Mary Magdalene went with John […] at that time
`understand-go Mary Magdalene John [?] time`

## 049v — over the Cedron, and Simon carries it

**1**  The Lord went, he said, to the Cedron; and then the Lord went
`go this-Lord +say exist Cedron and then-exist go Lord`

**2**  over the Cedron; and then
`+say over-exist Cedron and then-exist`

**3**  down […] […] the Lord Jesus; and […] |
`to-down [?] [?] Lord-Jézus and [?] | from`

**4**  […] the Lord Jesus […]; and the Jews knelt
`[?] Lord-Jézus [?] and kneel_(down) Jew(ish)`

**5**  before the Lord Jesus, and […] Hail,
`before Lord-Jézus and [?] healing`

**6**  Jesus! […] And there came to the Lord | the Virgin
`Jézus [?] and leave-to-leave to-Lord | virgin`

**7**  Mary; and Simon carried it for the Lord; and | when
`Mary and Lord Simon [?] carry and | then`

**8**  the Jews […] within […]
`exist Jew(ish) [?] inside [?]`

**9**  and […] […] upon the earth, and
`and [?] [?] on-earth and`

**10**  […] believed in the Lord Jesus […] […]
`[?] believe on-Lord-Jézus food [?]`

**11**  […] the Lord […] the Lord Jesus, and
`[?] Lord [?] Lord-Jézus and`

> Simon of Cyrene, Matthew 27:32.

## 050r — laid upon the cross

**1**  the Virgin Mary came to the Lord Jesus; and |
`leave-to-leave virgin-Mary to-Lord-Jézus and | from`

**2**  […] […] his bonds. And then
`[?] [?] <of>-Lord handcuffs +and_then`

**3**  the Lord Jesus […] his […] said,
`Lord-Jézus [?] <of>-Lord [?] +say`

**4**  […] […] this, in the commandment […] his apostles;
`trespass [?] this inside commandment this [?] <of>-Lord apostle`

**5**  and the Jews saw […] the whole wide world
`and see Jew(ish) [?] good the_whole_wide_world`

**6**  To his passion the Lord went; and […] said, in
`on-suffering-year go Lord and [?] +say inside`

**7**  the Lord believed; and they laid the Lord upon the cross,
`Lord believe and to-Lord place_onto +cross`

**8**  and the Lord […] one […]
`and Lord [?] one why?-in_turn`

**9**  and the two […] the cross, and could
`and two [?] +cross and can`

**10**  […] and […] […]
`[?] and why?-in_turn [?]`

**11**  and […] […]; and his feet could
`and why?-in_turn [?] and <of>-Lord foot can`

## 050v — the title, and the ninth hour

**1**  […] and the feet […]
`[?] ~and foot [?]`

**2**  and they pierced the feet; and all his […]; and | the
`and foot pierce and each,_every <of>-Lord [?] and | <of>`

**3**  Lord […] in the Lord […] in the Lord Jesus Christ.
`Lord [?] inside Lord [?] inside Lord-Jézus-Christ`

**4**  And Pilate wrote upon a tablet: Jesus
`and write Pilate on-one tablet Jézus`

**5**  […] King of the Jews. And then the Jews:
`[?] king Jew(ish) +and_then Jew(ish)`

**6**  write that the Lord said he is King of the Jews. But the Lord's writing,
`write Lord king Jew(ish) a) Lord write`

**7**  Jesus […]. And then Pilate: what I have written
`Jézus [?] +and_then Pilate write +<subject_marker>`

**8**  Pilate has written. And the two thieves; with the Lord they nailed them
`[?] ~Pilate write and two ~thief to-Lord pierce`

**9**  to the cross, and the Lord among the two thieves […]
`+cross and Lord among two ~thief [?]`

**10**  […]. And this was at the ninth hour. And then the Lord Jesus
`+say and this out(ward) nine hour +and_then Lord-Jézus`

**11**  on the cross prayed to God his Father […]
`+cross from-father <of>-Lord God [?] ask_(for)-Lord`

> John 19:19–22, the title and "what I have written I have written", and
> Matthew 27:46, the ninth hour.

## 051v — three nails, and the sponge on a stick

**1**  […] Mary's […]; but his three nails, long, with which
`[?] <of>-Mary [?] a) <of>-Lord three_nails long this-who`

**2**  they nailed the Lord to the cross. And then the Lord Jesus […] the Lord; and | the
`this-Lord pierce to-cross +and_then Lord-Jézus [?] Lord and | <of>`

**3**  Lord's apostles, when they bought […] sweet, and
`Lord apostle then-exist buy exist-nine sweet and`

**4**  wine; the apostles took […] the Jews' chief; and
`wine grab apostle Jew(ish) head and`

**5**  the Lord […]; but […] […] and the Lord | took
`Lord [?] a) [?] [?] in_turn Lord | grab`

**6**  […] vinegar; and […]; and the Lord,
`+say vinegar and [?] and Lord`

**7**  they took wine upon a sponge on a stick, and
`wine grab +say on-one sponge_(hyssop?)_on_a_stick and`

**8**  held the sponge to the Lord's face […]; and the wine
`then-exist-Lord sponge face [?] and wine`

**9**  […] his mouth […] […]. And then | the Lord
`grab mouth [?] [?] +and_then | Lord`

**10**  Jesus upon the cross [prayed to] God his Father in heaven […]
`Jézus +cross from-father <of>-Lord God heaven [?]`

**11**  […] his Father […] into his Father's hands.
`this-Lord this-father <of>-Lord [?] inside <of>-father-<divine>`

> John 19:29, the sponge on hyssop, and Luke 23:46, "Father, into thy hands".

## 052r — two lines

**1**  […] and […] to the Lord Jesus, his […] […]
`why?-in_turn and from to-Lord-Jézus <of>-Lord [?] [?]`

**2**  Here ends […] […] […] the Passion of the Lord Jesus.
`end this [?] [?] [?] suffering Lord-Jézus`

## 052v — the earthquake, and Longinus

**1**  And then the Lord Jesus, his […] […] upon the cross; the earth
`and then-exist Lord-Jézus <of>-Lord [?] [?] +cross earth`

**2**  quaked, the rocks and the stones […]; the sun and the moon
`quake rock stone [?] sun and moon`

**3**  were darkened; and all […] […] humbled themselves; and all
`this eclipse and each,_every [?] [?] this humble ~and each,_every`

**4**  creation mourned, when Christ the Lord was crucified. And there came
`create mourn then-exist Christ +crucified Lord and go [?]`

**5**  one soldier from Jerusalem, blind; and that soldier
`one soldier on-Jerusalem blind and [?] soldier`

**6**  was Longinus; and the Jews' spear pierced
`exist Longinus and pierce Jew(ish) spear [?]`

**7**  the Lord Jesus Christ; and […] the spear
`Lord-Jézus-Christ and can [?] spear on`

**8**  […] the Lord Jesus Christ; and the soldier, the blood splashed
`[?] Lord-Jézus-Christ how? soldier [?] splash`

**9**  from the Lord Jesus upon his eyes, and through it he saw, and the soldier was healed;
`to-to-to Lord-Jézus on-place through see and healing soldier`

**10**  and the soldier believed in the Lord Jesus Christ,
`leave and grab soldier believe Lord-Jézus-Christ`

**11**  and the soldier was baptized, and saw […]
`and soldier see-baptize and see [?]`

> Longinus, the blind soldier whose sight is restored by the blood from the
> spear wound, is not in any gospel. He is the Golden Legend, and Király and
> Tokai's dictionary has a code glossed for him by name.

## 053r — after the ninth hour

**1**  […] the Lord Jesus Christ; and […] believed in the Lord,
`can Lord-Jézus-Christ and [?] inside Lord believe`

**2**  but many judged […] […] home.
`a) many judge [?] [?] home`

**3**  And the second said sorrowfully, accusing, because […] […]
`in_turn-two +say sad(ly) accuse because [?] [?]`

**4**  he said […] they crucified, saying, the Son of God; and
`+say [?] ~execute +say son God and`

**5**  sorrowfully they went, saying […] home; and this
`sad(ly) go +say [?] home and this`

**6**  […] was the ninth hour, and four hours from that hour
`[?] out(ward) nine ~hour and two-two from ~hour`

**7**  the Lord Jesus suffered upon the cross […] […]
`+cross suffer Lord-Jézus [?] [?]`

**8**  all […] home from […] […]
`each,_every [?] home from [?] [?]`

**9**  and the apostles […] went, every one of the apostles […] |
`in_turn apostle exist [?] go-go each,_every to-apostle [?] | on`

**10**  […] and one, and […]
`[?] and one and understand-eat`

## 053v — Joseph and Nicodemus ask for the body

**1**  the apostles […]; and then two […] Jerusalem,
`apostle cut_off and then-exist two somebody-have_mercy Jerusalem [?]`

**2**  and […] was […]; and the second
`and [?] exist [?] in_turn-two`

**3**  Nicodemus; and then the two asked of Pilate
`~Nicodemus and then-exist two ask_(for) from Pilate`

**4**  […] the Lord Jesus; and […] the two, the sufferer
`[?] Lord-Jézus and [?] two sufferer`

**5**  […] the Lord Jesus; and then the two went […]
`[?] Lord-Jézus and then-exist two go [?]`

**6**  Christ was […]; and the two went […]
`exist Christ [?] and go [?] two`

**7**  many Jews; and the two were, that is, good and merciful men;
`many Jew(ish) and two people that_is good people have_mercy`

**8**  and then the two saw the Virgin Mary, and […]
`and then-exist two see virgin-Mary and [?]`

**9**  Magdalene. Many people went out of Jerusalem, and
`Magdalene go many people on-Jerusalem and ~through`

**10**  were afraid, because the Jews would […] the Lord, all […] because
`startle because to Lord want Jew(ish) each,_every Lord [?] because`

## 054r — taken down, and the tomb sealed

**1**  this was […] | and […] went […] […]
`this exist from | and [?] go [?] [?]`

**2**  because Mary was […] fled […]
`because exist-Mary [?] escape [?]`

**3**  the Jews; and in that place were these people, when
`Jew(ish) and on-place exist this people then-exist`

**4**  the two Marys went to the people, and took
`from two-Mary to-people go-two-Mary and grab`

**5**  Nicodemus the Lord Jesus from the cross, and the three nails,
`~Nicodemus +cross [?] Lord-Jézus in_turn +three three_nails`

**6**  […] Saint John took […] saw | the Virgin
`[?] grab holy-John [?] see | virgin`

**7**  Mary […] took the Virgin Mary into […]
`Mary [?] grab virgin-Mary inside [?]`

**8**  and […] Nicodemus, with his servants'
`~and [?] Nicodemus <of>-living-servant`

**9**  […]; and the two covered the body, and […] […]; and
`[?] and cover two body and [?] [?] and`

**10**  Nicodemus laid the Lord Jesus within, and
`inside-put Nicodemus [?] Lord-Jézus and`

**11**  they closed the Lord within the tomb; and there stood, he said, four soldiers by the Lord […]
`Lord inside burial_chamber close and leave [?] +say to-Lord two-two soldier [?]`

**12**  […] the chief of Jerusalem; and […] went […]. Here ends this
`[?] Jerusalem head ~and [?] go [?] end this`

**13**  holy gospel.
`holy-gospel`

## 054v — a rubric, naming Mark

**1**  Here begins this holy gospel, written by Saint Mark.
`begins this holy-gospel write holy-Mark`

> The fourth evangelist the codex names for itself, after Luke, Matthew and
> John. What follows is Mark 16, and it follows it closely.

## 055r — the three women at the tomb

**1**  in the […] chapter of his writing: at that time, when
`inside [?] chapter-leave <of>-write time then-exist`

**2**  they went […] […] to the tomb of Christ, because they had prepared
`go [?] [?] burial_chamber Christ because-exist prepare`

**3**  […] […] […] […] Jesus:
`[?] [?] this-cut_off [?] [?] Jézus`

**4**  Mary Salome, and Mary the mother of James, and
`Mary Salome and Mary James mother and`

**5**  Mary Magdalene. And then these Marys […] these Marys
`Mary Magdalene and then-exist this-two-Mary [?] this-two-Mary`

**6**  among […] […]
`among [?] [?]`

**7**  […] the stone from the tomb; and then |
`[?] from stone on-burial_chamber and then-exist | [?]`

**8**  Mary came to the tomb of Christ, and saw […] […]
`Mary to-burial_chamber Christ and see [?] [?]`

**9**  the tomb […]; and then […] within this
`+<subject_marker> burial_chamber from [?] and then-exist [?] inside this`

**10**  […] and they went in […] and
`[?] and inside-to-go [?] and`

**11**  […] saw […] Jesus; but they saw one
`[?] see [?] Jézus a) see one`

> Mark 16:1 names exactly these three: Mary Magdalene, Mary the mother of
> James, and Salome. The codex has all three, and the stone rolled away.

## 055v — be not afraid, he is risen

**1**  angel, sitting on the left side, from […] within
`angel sit on-left_(side) direction from [?] inside exist`

**2**  […] […] Jesus. And then Mary, through
`[?] [?] Jézus and then-exist Mary through`

**3**  was afraid, because Mary […] as a ghost.
`startle because rather-Mary [?] +<subject_marker> how? ghost`

**4**  And then the angel: be not […] […]
`+and_then angel do_not [?] [?]`

**5**  […] be not afraid. He is risen, whom ye mourn — the Lord Jesus,
`[?] through startle +rise mourn to-Lord from Jézus`

**6**  whom they crucified, is risen […]; but […]
`execute +rise [?] a) [?]`

**7**  within […] and […]
`inside [?] and [?]`

**8**  his apostles, and Peter […]. Here ends this
`<of>-Lord apostle and Peter [?] end this`

**9**  holy gospel. And […] these women went
`holy-gospel and [?] go this woman`

**10**  […] from the tomb of Christ; and |
`head from this burial_chamber Christ and | [?]`

**11**  Mary Magdalene went back to the tomb of Christ. At that time
`[?] back Mary Magdalene to-burial_chamber Christ time`

> Mark 16:5–7, including "tell his disciples and Peter", which is Mark's
> detail and no one else's. The codex puts the angel on the left; Mark says
> the right.

## 056r — Mary Magdalene takes him for the gardener

**1**  the Lord Jesus appeared to Mary Magdalene in the form of a
`appear Lord-Jézus Mary Magdalene inside shape,_form from one`

**2**  gardener. And then this gardener, the Lord Jesus Christ, | [said to] this
`gardener +and_then this gardener-Lord-Jézus-Christ | this`

**3**  woman: why […] woman, weepest thou for the Lord? He,
`woman who-shore [?] woman mourn to-Lord this from`

**4**  Jesus, whom they crucified, is risen, because
`Jézus execute +rise [?] because`

**5**  […] said […] […] […] light […]
`say [?] [?] [?] light [?]`

**6**  […] […] the tomb pierced, and the tomb
`town-chapter-in_turn [?] burial_chamber pierce and burial_chamber +<subject_marker>`

**7**  light […]; and […] […] is risen.
`light from-gate and [?] can [?] +rise`

**8**  And the Lord Jesus stood before Mary Magdalene
`and leave Lord-Jézus before Mary Magdalene`

**9**  in that place; Mary […] […]
`on-to-place Mary [?] on-reason [?]`

**10**  […] Master! And the Lord […] to Mary: go to the apostles.
`this-Lord Master and Lord +<subject_marker> to-Mary-apostle go-Lord-apostle`

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

**4**  of Jerusalem. And then the Lord Jesus [gave] the commandment of God among
`Jerusalem +and_then Lord-Jézus commandment God among`

**5**  you: his mercy to whoever believes
`you <of>-Lord have_mercy somebody to and believe`

**6**  in the Lord, and in his Father God […]
`inside Lord and inside <of>-Lord from father-<divine> [?]`

**7**  O! Amen. And then the Lord Jesus
`chapter-oh amen +and_then Lord-Jézus +<subject_marker>`

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
`six chapter-leave <of>-write`

**4**  and Saint Mark […]
`in_turn holy-Mark [?]`

**5**  it is written. Said Saint […] the prophet:
`write say holy-<prophet>`

**6**  because he saith […] it is found,
`because say +<subject_marker> exist find`

**7**  in the Old Testament is truly written this word: the Lord shall rise from the dead.
`inside <Old_Testament> righteous(ly) write this word stand_up-Lord on-die-Lord`

**8**  The King — thanks to the Lord […]; and the Lord Christ destroyed the evil one; and
`king to-Lord thanks [?] and destroy Lord ~evil Christ and from`

**9**  […] […] the evil one […] Lucifer. This is written |
`[?] [?] ~evil can hide_oneself-angel +this_is write | to`

**10**  Saint Mark, in the […] chapter of his writing: when the Lord
`holy-Mark inside [?] chapter-leave <of>-write then-exist Lord`

**11**  Christ upon the cross breathed out his soul, the earth quaked,
`Christ +cross <of>-Lord soul breathe_out earth quake`

**12**  the rocks and stones […]; the sun and the moon
`rock stone this [?] sun and moon this`

## 058r — the harrowing of hell

**1**  were darkened; and all […] […] humbled themselves; and all creation mourned
`eclipse and each,_every [?] [?] this humble and each,_every create mourn`

**2**  when Christ was crucified. And four hours
`then-exist Christ +crucified and two-two hour`

**3**  the Lord Jesus suffered upon the cross; and the Lord within the tomb | the apostles laid him,
`+cross suffer Lord-Jézus and Lord inside burial_chamber | put-apostle`

**4**  […] and then they laid the Lord within the tomb; and
`Mary-angel and then-exist-Lord inside burial_chamber lay Lord and`

**5**  at that hour there came from God the Father in heaven,
`hour time go from-father God heaven`

**6**  from the Father, an angel into […] the Lord Jesus; and
`on-<of>-father angel inside [?] Lord-Jézus and`

**7**  […] […] and the angel within the tomb […]
`[?] from [?] in_turn angel inside burial_chamber [?]`

**8**  and the Lord went […], and destroyed the evil one; and […]
`in_turn to-Lord go-Lord [?] and ~evil destroy and [?]`

**9**  the people who died within a hundred years, and within | five
`people die inside one hundred-year and inside | +five`

**10**  […] and within […] and […] all the prophets
`[?] and inside [?] and [?] each,_every prophet`

**11**  went into hell; and […] three souls, all […] the Lord went,
`go on-netherworld and [?] +three soul each,_every [?] go Lord`

**12**  and the three souls within the evil one's […] the Lord |
`in_turn +three soul inside ~evil [?] Lord | [?]`

## 058v — Adam's soul kneels to the Virgin

**1**  Saint Augustine the doctor: within many years, and one soul […]
`holy-Augustine-church_father inside many-to-year and one soul [?]`

**2**  went into the […] land; but when the Lord
`~go inside [?] land a) then-exist to-Lord`

**3**  went to the souls, the Lord, and […] three souls
`to-soul-soul-soul-soul-soul go Lord and [?] +three soul`

**4**  […] […] the Lord went to the souls; and the Lord appeared
`[?] [?] to-go Lord soul and Lord appear Lord`

**5**  to the blessed Virgin Mary; and Adam's soul knelt
`to-happy virgin-Mary and kneel_(down) ~Adam soul`

**6**  before the blessed Virgin Mary; and the maiden […]
`before to-happy virgin-Mary and girl [?]`

**7**  prayed; and blessed the blessed Virgin Mary;
`ask_(for) and bless-year to-happy virgin-Mary`

**8**  and all the souls stood before the blessed
`and to-soul-soul-soul each,_every leave before to-happy`

**9**  Virgin Mary; and within […] the souls, the Lord, the souls;
`virgin-Mary and inside [?] soul Lord soul`

**10**  and the Lord went to the souls; and then twenty-five(?)
`and go Lord soul and then-exist two-ten-ten +five`

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

**6**  […] and |
`in_turn-chapter-in_turn and | exist-chapter`

**7**  […] was Emmaus; and then the two apostles […] of the living
`[?] exist Emmaus and then-exist to-high-two-apostle from living`

**8**  Lord Jesus; and then the two spoke of how the Lord
`Lord-Jézus and then-exist two speak how?-Lord this-Lord`

**9**  was truly a man, truly the Lord, preaching, and many
`exist righteous(ly) somebody righteous(ly) Lord ~preach who-and-this-and`

**10**  miracles he did […]; the two apostles; the Jews'
`miracle do, [?] <of>-two-apostle Jew(ish)`

**11**  chief crucified him. At that time there appeared
`head execute time appear`

**12**  to the two apostles the Lord Jesus, in the form of a traveller; and then
`two-apostle Lord-Jézus shape,_form traveller and then-exist`

> Luke 24:13–21, and the codex names Emmaus. As with the gardener, it
> explains why they did not know him: he appeared in the form of a traveller.

## 060r — the Lord asks the two what they are speaking of

**1**  The two apostles […] Lord Jesus, and the two apostles began to talk, and
`two-apostle [?] Lord-Jézus and two-apostle (begin_to)_talk and`

**2**  the Lord spoke from among them; and then Lord Jesus: O my
`Lord from-speak +and_then Lord-Jézus oh <preposition_of_genitive>-Lord`

**3**  two apostles, are you not saying, two apostles, Lord, how, saying among
`two-apostle exist-~exist say two-apostle Lord how? say ~among`

**4**  […] have, two apostles, because they said the Lord Jesus Christ
`[?] have two-apostle because say exist Lord-Jézus-Christ`

**5**  apostle […] the two men spoke of the Lord, this Lord, the two
`apostle [?] two somebody from-Lord speak this-Lord two`

**6**  Lord's apostles; the third Lord; and then Luke this […]
`Lord apostle +three Lord +and_then Luke this [?]`

**7**  the way, the man, this Lord, this good […] […]
`way somebody this Lord this good [?] [?]`

**8**  how […] the miracles in Jerusalem afterwards, and how
`how? [?] +<subject_marker> miracle Jerusalem ?afterward how?-to`

**9**  the man […] said, the chief truly
`somebody [?]-+say head righteous(ly)`

**10**  crucified this Jesus; and the Lord came into the world, went
`execute this Jézus and +the_Lord ?into_the_world go-Lord`

**11**  went preaching, and this and that miracle he did
`go-+<subject_marker> ~preach-Lord who-and-this-and miracle do,`

> Luke 24:17–20. The codex keeps the two apostles' complaint that the chief
> priests crucified him, and names Luke as one of the two, which the gospel
> does not.

## 060v — the miracles, and the women's news they did not believe

**1**  the blind, through him light; the dead, through him […] […]
`eye-eye ~blind +<subject_marker> through light die +<subject_marker> [?] | [?]`

**2**  […] the body, and the evil, those possessed by the evil one, healed
`[?] body and evil obsessed_by_the_evil from-healing`

**3**  and the Lord […] was from […] […]
`and Lord +<subject_marker> exist from [?] [?]`

**4**  he rose, and one said, the one baptized, the Baptist, the chief
`stand_up-Lord and say one +one-+baptize-+the_Baptist ~head`

**5**  the news was of the Lord […] he rose; the news the two
`news exist-Lord [?] stand_up-Lord news two`

**6**  apostles […] believed, who from the Lord, from the dead
`apostle [?] believe who from Lord from die`

**7**  rose; because he is the Lord's, to the brethren
`stand_up-Lord because ?he_is <preposition_of_genitive>-Lord brother-to`

**8**  […] this pleasing, and who from the Lord, from the
`[?] this pleasing who from Lord from`

**9**  dead rose; and then Lord Jesus […] the two
`die stand_up +and_then Lord-Jézus [?] two`

**10**  […] the man, to hide, the two believing
`[?] somebody to-hide_oneself believe-two`

> Luke 24:21–24, the report of the women at the tomb that the two did not
> believe.

## 061r — O fools and slow of heart, and Cleopas is named

**1**  Is it that these, to him, rise from the […]
`?is_he-two this to-+<subject_marker> ?rise from ?as`

**2**  And then Lord Jesus left; the Son of God died
`+and_then Lord-Jézus leave exist die son God`

**3**  more than these, rise from the, from the
`?more_than_these ?rise from ?as from ?as`

**4**  the Lord, from the eternal Father, and began, through
`+the_Lord from father-<suffix_of_divine_name> ?eternal and begin through`

**5**  Lord Jesus expounded from Adam, the trespass, written
`explain Lord-Jézus from ~Adam ~trespass write`

**6**  said; and then Cleopas, Luke, this Lord, to the two […]
`say +and_then Cleopas Luke this Lord to-two [?]`

**7**  the Lord wished good, said; and then Lord Jesus from […]
`want-Lord good say +and_then Lord-Jézus from [?]`

**8**  […] signified this Jesus crucified, how, in turn
`[?] symbolize this Jézus execute how? | in_turn`

**9**  […] died, the brother's […] and this Jesus
`[?] die <preposition_of_genitive>-brother [?] and this Jézus`

**10**  died, the Lord's brother; and then Lord Jesus, the trespass […]
`die <preposition_of_genitive>-Lord brother +and_then Lord-Jézus trespass [?]`

> Luke 24:25–27, *beginning at Moses and all the prophets, he expounded unto
> them.* The codex begins further back, at Adam's trespass. **Cleopas is
> named on line 6**, which is Luke 24:18, and the codex makes Luke the other
> of the two.

## 061v — Abraham as the figure of the crucifixion

**1**  […] signified this Jesus crucified, he is […]
`go_up-+day-why? symbolize this Jézus execute ?he_is go_up-~gate-who`

**2**  redeemed every people in […] this […] and on this Jesus
`redeem each,_every ~people inside [?] this [?] and on-this Jézus`

**3**  crucified, saved every one, Adam gained; and then
`execute be_saved each,_every ~Adam gain +and_then`

**4**  Lord Jesus, above; Abraham — Abraham's [deed] signified this
`Lord-Jézus up Abraham Abraham symbolize so`

**5**  Jesus crucified, and Lord Jesus said, said the Lord.
`Jézus execute and say Lord-Jézus say exist Lord-<suffix_of_divine_name>.`

**6**  Abraham, to the Lord's angel — Abraham gave
`Abraham on-~Satan <preposition_of_genitive>-Lord-<suffix_of_divine_name> Abraham give`

**7**  his son […] and the Lord […]
`<preposition_of_genitive>-son [?] and Lord [?].`

**8**  […] who did, Abraham on
`[?] who do, Abraham on`

**9**  […] the faggots […] in turn Abraham
`[?] faggot [?] in_turn Abraham`

**10**  took […] who […] wished to slay
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

**2**  wished […] and then […] O
`want [?] +and_then [?] oh`

**3**  my father […] and went far
`<preposition_of_genitive>-father [?] and go far`

**4**  […] and a, and the ram, and a
`[?] and a and sheep and a`

**5**  […] the young men […] father […] and said
`[?] ?brethren [?] father [?] and say`

**6**  from father Abraham, from the brethren, the Lord […]
`from-father Abraham from ?brethren Lord-<suffix_of_divine_name> [?].`

**7**  […] and then […] […]
`[?] and then-exist [?] [?]`

**8**  of […] living, the Lord wished to slay, and
`<preposition_of_genitive> [?] [?]-living want Lord slay and`

**9**  the Lord cried […] to the angel […]
`shout Lord-<suffix_of_divine_name> [?] on-angel [?]`

**10**  Abraham, to the whole wide world, the Lord's love, this is
`Abraham to-the_whole_wide_world +<subject_marker> Lord <preposition_of_genitive> love +this_is`

> Genesis 22. *My father* on line 3 is Isaac's question, the ram caught for
> the sacrifice is on line 4, the young men left behind with the ass on
> line 5, and the angel stops the hand on line 9.

## 062v — he made as though he would go further, and they constrained him

**1**  Lord […] and then Lord Jesus, he is, was […]
`Lord [?] +and_then Lord-Jézus ?he_is exist [?]`

**2**  as he gave his father's [son], so this Jesus was crucified
`to-give <preposition_of_genitive> father so and so Jézus execute exist`

**3**  the Lord gave, his divine Father, and he rose
`to-give-Lord <preposition_of_genitive>-Lord father-<suffix_of_divine_name> and +<subject_marker> ?rise`

**4**  the Lord from the […] because the Lord from the […] from the Father,
`Lord from ?as-[?] because-+the_Lord from ?as-[?] from-father`

**5**  eternal God; and then the Lord's apostles went, this in turn
`God ?eternal and then-exist go-apostle-Lord this in_turn-chapter-in_turn`

**6**  and then Lord Jesus went, the two apostles, you, because this Lord
`+and_then Lord-Jézus go-two-apostle you because this-Lord`

**7**  the Lord had a long way; and the Lord began, the two apostles
`have-Lord long way and Lord begin two apostle`

**8**  persuaded; and then the Lord was, the two apostles persuaded, and the two
`persuade and then-exist-Lord exist two-apostle persuade and | two`

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

**1**  the two apostles carried […] water and wine.
`carry apostle two [?] ~water and wine and.`

**2**  Lord Jesus took one […] and […]
`grab Lord-Jézus one [?] and [?]`

**3**  […] this, how, then […] […]
`[?] this how? then-exist [?] [?]`

**4**  and from […] today's, and wine, and the cloud
`and from [?]-today’s and wine and cloud`

**5**  Lord Jesus blessed; and then the two apostles ate, the two
`bless Lord-Jézus and then-exist two apostle | eat-two`

**6**  apostles, and the two apostles drank, in the place, to the two apostles
`apostle and drink-two-apostle on-place to-two-apostle`

**7**  in the Holy Spirit, the farm, truly the Son of God
`on-spirit holy-farm +<subject_marker> righteous(ly) son God`

**8**  to Lord Jesus; the two apostles, he left them, and
`to Lord-Jézus two apostle <preposition_of_genitive>-to-leave-this and`

**9**  […] among the two apostles, Lord Jesus Christ, the chapter answered
`[?] among two apostle Lord-Jézus-Christ chapter-?answered`

**10**  to the Lord […] the two apostles saw. Here ends this holy gospel.
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

**3**  in the twentieth chapter
`inside two-ten-ten chapter-leave`

**4**  of his writing. At that time
`<preposition_of_genitive>-write time`

**5**  the apostles were found in Jerusalem
`~find apostle inside Jerusalem`

**6**  in […] house, six
`inside [?] house six`

**7**  in the Lord's house, where the Lord
`inside Lord house where Lord-<suffix_of_divine_name>`

**8**  Lord Jesus, after supper; and then holy Thomas went […]
`Lord-Jézus dinner ?afterward and then-exist go holy-Thomas [?]`

**9**  one Saturday evening, to the apostles; and the apostles said, Thomas, apostle,
`one Saturday evening to-apostle and say-apostle Thomas apostle`

**10**  we have seen the Lord. And holy Thomas said, I do not believe this
`see Lord and say holy-Thomas this-Thomas this not believe`

**11**  at all; unless I hide this, unless Thomas believes […] not, unless he sees
`each,_every this this-hide_oneself this-Thomas this believe [?] not | see`

**12**  Thomas the Lord's end, and unless Thomas puts his finger in […]
`Thomas <preposition_of_genitive>-Lord end and <preposition_of_genitive>-Thomas finger not put inside | <preposition_of_genitive>`

> John 20:24–25. *Except I shall see in his hands the print of the nails, and
> put my finger into the print of the nails, I will not believe.*

## 009r — reach hither thy finger, and my Lord and my God

**1**  the Lord's end, who from the Lord, rose from the dead; at that time Lord Jesus Christ left
`Lord end who from Lord from die stand_up time leave Lord-Jézus-Christ`

**2**  into the midst of the apostles […] and said, you have the commandment, and judge; he left
`middle apostle [?] and say commandment you exist and judge leave`

**3**  the apostles in turn; Thomas began […] and Lord Jesus said, Thomas,
`apostle in_turn Thomas begin [?] and say Lord-Jézus Thomas`

**4**  thou shalt go to put thy finger, Thomas, into the Lord's wound
`go-?shall to put <preposition_of_genitive>-Thomas finger inside <preposition_of_genitive>-Lord wound`

**5**  […] see and believe; and […] Lord Jesus, the Lord's wound
`[?] see believe and [?] Lord-Jézus <preposition_of_genitive>-Lord wound`

**6**  and Lord Jesus said, Thomas, blessed are they, and the man who sees
`and say Lord-Jézus Thomas happy-to from and somebody see`

**7**  and believes […] and blessed are they, and the food he sees
`and believe [?] and happy-to from and food see`

**8**  […] believe. Here ends this holy gospel. And he kneeled,
`[?] believe end this holy-gospel and kneel_(down)`

**9**  holy Thomas, before Lord Jesus, and holy Thomas said, Lord,
`holy-Thomas before Lord-Jézus and say holy-Thomas Lord`

**10**  Thomas's God; Thomas asked this of the Lord,
`<preposition_of_genitive>-Thomas God <preposition_of_genitive>-Thomas ask_(for)-Thomas this-Lord-<suffix_of_divine_name>`

**11**  have mercy on Thomas, who through sin against this Lord
`have_mercy Thomas who this-Thomas through +sin against this-Lord-<suffix_of_divine_name>`

> John 20:26–29. Line 4 is *reach hither thy finger*, line 6 is *blessed are
> they that have not seen, and yet have believed*, and lines 9–10 are *My Lord
> and my God*, which the codex renders as Thomas's Lord and Thomas's God
> because of the rule that a name sign stands in for the pronoun.

## 009v — Thomas blesses him, and the Good Shepherd begins

**1**  Thomas, this Lord, Thomas believed […] this Lord truly
`this-Thomas this-Lord believe-Thomas [?] this-Lord righteous(ly)`

**2**  the Son of the living God. And then Thomas blessed Lord Jesus Christ.
`son living God and then-exist Thomas exist bless Lord-Jézus-Christ.`

**3**  And have mercy on Thomas's sin. And Lord Jesus said, every […] and […] […] from
`and +sin Thomas have_mercy and say Lord-Jézus each,_every [?] and [?] [?] from`

**4**  […] believing in Lord Jesus Christ, every gentile man and Jew
`[?] on-believe to-Lord-Jézus-Christ each,_every of_an_alien_nation,_pagan somebody Jew(ish)`

**5**  […] have mercy on sin. Here ends this apostle's holy gospel; blessed be the Lord.
`[?] +sin have_mercy end this apostle holy-gospel on-Lord-<suffix_of_divine_name> bless`

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

**11**  to his Lord, this good Lord, before the son, in turn, you, from the apostles
`<preposition_of_genitive>-Lord this-Lord good ?son-before in_turn you from apostle`

> Thomas's confession, *my Lord and my God*, John 20:28, then the book turns
> to John 10, the Good Shepherd.

## 064r — the good shepherd and the hireling

**1**  his sheep, and the Lord knows his sheep, and
`<preposition_of_genitive>-Lord sheep and Lord ~know <preposition_of_genitive>-Lord sheep and`

**2**  this Lord knows his sheep. And then Lord Jesus: then
`this-Lord ~know <preposition_of_genitive>-Lord sheep +and_then Lord-Jézus | then`

**3**  there was a king, and then he had two shepherds,
`exist one king and then-exist ~have two ?sons`

**4**  one who kept the house well, a shepherd; the other in turn a hired
`one ~who home good ?sons in_turn-two farm_hand`

**5**  shepherd. And then, of the two shepherds […] from one
`?sons and then-exist from two ?sons chapter-[?] from one`

**6**  herd of sheep of this king; and then came the wolf
`herd sheep this king and then-exist go wolf`

**7**  to this sheep, and would carry this sheep away
`this sheep and want this sheep from-~carry`

**8**  and this hired shepherd, of the shepherds […]
`and this farm_hand ?sons from ?sons [?]`

**9**  this sheep; in turn the good shepherd, of the house, of the shepherds
`this +sheep in_turn-this good ?sons home from ?sons`

**10**  redeemed this sheep, and made the sheep ready in the herd
`redeem this +sheep and +sheep prepare inside herd`

**11**  and took it into the good keeping, and one carried away, and
`and inside-good-exist-to grab and one from-~carry and`

> John 10:11–13, told as a parable of a king with two shepherds, one his own
> and one hired. The wolf comes, the hireling flees, the good shepherd
> redeems the sheep.

## 064v — the good shepherd giveth his life, and other sheep I have

**1**  in turn who […] […] this herd, and went.
`in_turn-who [?] [?] this herd and go.`

**2**  The wolf, and the sheep carried away; and then
`wolf and sheep from-~carry +and_then`

**3**  Lord Jesus: he who is the good shepherd, of the shepherds, lays
`Lord-Jézus to-+he_who good ?sons from ?sons put`

**4**  down his […] for his sheep; and the Lord takes
`down <preposition_of_genitive>-Lord [?] to-<preposition_of_genitive>-Lord +sheep and grab-Lord`

**5**  and one […] he who is the good shepherd, of the shepherds,
`and one [?] +he_who good ?sons from ?sons`

**6**  is the gate of his sheep; and then they hear
`+<subject_marker> ~gate <preposition_of_genitive>-Lord sheep and then-exist hear`

**7**  the voice of the Lord; the sheep […] the shepherd go; and then
`voice,_sound <preposition_of_genitive>-Lord-<suffix_of_divine_name> sheep [?] ?sons go +and_then`

**8**  Lord Jesus, his apostles, one creature […] one sheep
`Lord-Jézus apostle <preposition_of_genitive>-Lord ?creature-+one [?] one +sheep`

**9**  and these sheep I will bring to you […] and go
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

**4**  At that time, then the chapter
`time | then-chapter`

**5**  of the day of Lord Jesus Christ,
`+day Lord-Jézus-Christ`

**6**  thirty, three days.
`thirty +three_days`

**7**  At that time Lord Jesus said
`time say Lord-Jézus`

**8**  to his apostles, go, and to you […] believe
`apostle <preposition_of_genitive>-Lord go to-you [?] believe-chapter`

**9**  false prophets, pagan, evil […] they are pagan
`false prophet pagan evil [?] exist pagan`

**10**  evil, the Lord's trespass […] […] the apostles, men,
`evil trespass Lord [?] [?] apostle somebody`

**11**  and the pagan evil believe, because they are false
`and pagan evil believe because exist false`

> Matthew 7:15, *beware of false prophets, which come to you in sheep's
> clothing.* The codex has put it straight after the Good Shepherd, which is
> where the sheep's clothing belongs.

## 065v — by their fruits ye shall know them

**1**  the Lord's name […]; and then Lord Jesus, to his apostles,
`Lord +name [?] +and_then Lord-Jézus apostle <preposition_of_genitive>-Lord`

**2**  […] […] this Lord spoke to you; and then
`[?] [?] this-Lord you speak +and_then`

**3**  Lord Jesus: do not pick figs from thistles, but rather from the fig, and […]
`Lord-Jézus do_not_pick fig on-thistle ?but_rather-to on-fig and | [?]`

**4**  food, grapes […] not from the grapevine,
`food grape [?] ~a) on-grapevine`

**5**  because he who is a good tree brings this good fruit; in turn
`because ?he_who good tree this +good_fruit grab | in_turn`

**6**  likewise the evil tree brings this evil of hell.
`?likewise die-evil tree this die-evil-hell grab`

**7**  Because a good tree cannot bring forth the evil of hell,
`because good tree can die-evil-hell grab ~a)`

**8**  every good fruit it brings; in turn likewise the evil tree
`each,_every +good_fruit grab in_turn-?likewise die-evil tree`

**9**  cannot bring good fruit, but every evil of hell
`can +good_fruit grab ~a) each,_every die-evil-hell`

**10**  it brings. And then Lord Jesus, many people were crying out against the judgment
`grab +and_then Lord-Jézus many people exist shout | on-judge`

**11**  the Lord's year, to the Lord; this man's trespass; this the Lord preached, and Lord Jesus said
`year Lord to-Lord this somebody trespass this Lord preach and say Lord-Jézus`

> Matthew 7:16–20. *Do men gather grapes of thorns, or figs of thistles?* on
> lines 3–4, and the good tree and the corrupt tree on lines 5–9, in the same
> order as the gospel.

## 066r — the weeping and gnashing of teeth

**1**  and […] the man who can speak of the Lord, go to the Lord, the Lord's heart
`and [?] somebody can-say-Lord go Lord-<suffix_of_divine_name> Lord +heart`

**2**  the man, and the Lord saved every one, Adam gained, this man
`somebody and +be_saved Lord each,_every ~Adam gain this somebody`

**3**  […] the year out, the man […] of his Father, and this man
`[?] out(ward)-year somebody [?] <preposition_of_genitive>-Lord father-<suffix_of_divine_name> and this somebody`

**4**  every man […] into […] the heavenly home of his
`each,_every somebody [?] inside [?] heavenly home <preposition_of_genitive>-Lord`

**5**  Father; but every one goes, the man, to hell
`father-<suffix_of_divine_name> a) each,_every go somebody on-chapter-oh chapter-oh hell`

**6**  fire; there is seen the gnashing of teeth and crying
`fire there exist see grinding tooth crying`

**7**  for ever; in turn, and the man is […] the man
`chapter-oh chapter-oh in_turn and somebody exist [?] somebody`

**8**  says, three, Lord upon Lord upon Lord, saved by the Lord, every people, this man
`say +three Lord-chapter-Lord-chapter-Lord +be_saved Lord each,_every ?people this somebody`

**9**  every one goes into […] the heavenly home of his Father; there
`each,_every go inside [?] heavenly home <preposition_of_genitive>-Lord father-<suffix_of_divine_name> there`

**10**  is the man's judgment, to the Lord, and the angels, and his Lord Father
`exist somebody judge to-Lord and angel and <preposition_of_genitive>-Lord-father`

**11**  God, for ever, amen. Here ends this holy gospel.
`God chapter-oh chapter-oh amen end this holy-gospel`

> Matthew 8:12, *there shall be weeping and gnashing of teeth*, set against
> *in my Father's house are many mansions*, John 14:2, which is where the
> next folio begins.

## 066v — whatsoever ye shall ask the Father in my name

**1**  Here begins this holy gospel
`begins this holy-gospel`

**2**  written by holy John
`write holy-John`

**3**  in the fourteenth chapter of his writing.
`14-+one chapter <preposition_of_genitive>-write`

**4**  At that time Lord Jesus said
`time say Lord-Jézus`

**5**  to his apostles, at the last supper,
`apostle <preposition_of_genitive>-Lord on-last dinner`

**6**  […] […] this the Lord spoke to you: love.
`[?] [?] this-Lord you speak love`

**7**  Whatsoever ye shall ask of the Lord's Father
`whatever you exist ~ask_(for) from <preposition_of_genitive>-Lord-from father-<suffix_of_divine_name>`

**8**  in the Lord's name, ye shall all receive it saved
`inside <preposition_of_genitive>-Lord +name each,_every you +be_saved grab`

**9**  from heaven, from this Lord Christ. And this Lord Jesus spoke, saying,
`from heavenly from this-Lord Christ and this say speak Lord-Jézus`

**10**  on the way, to his apostles, and said, O the Lord's son.
`on-way apostle <preposition_of_genitive>-Lord and say oh <preposition_of_genitive>-Lord son.`

> John 14:13–14, *whatsoever ye shall ask in my name, that will I do*, placed
> at the last supper as the gospel places it.

## 067r — whose son is he, and thou art the Son of the living God

**1**  Judge this: whose son is he?
`judge this-Lord you whose? son | ?is_he`

**2**  […] the apostles spoke to the Lord, and the apostles said, the apostles answered, this Lord
`[?] to-Lord speak apostle and say apostle +answered apostle this Lord`

**3**  believe […] this Lord […] truly the Son of the living God. And
`believe [?] this Lord [?] righteous(ly) son living God and say`

**4**  Lord Jesus said, O the Lord's son, this Lord casts this out;
`Lord-Jézus oh <preposition_of_genitive>-Lord son this-Lord this exorcise`

**5**  if you believe this, it is to the Lord
`if-to you this believe exist to-Lord`

**6**  that this Lord is truly the Son of the living God […] and […]
`this-Lord righteous(ly) son living God [?] and [?] | ?is_he`

**7**  […] believe, believing, because this Lord who goes
`[?] believe believe-+day because this-Lord who-go`

**8**  to the death, to the Lord's death […] ask this of you […]
`on-die to-Lord-die [?] ~ask_(for) this-Lord you [?]`

**9**  in the Lord […] the apostles, because you are apostles, many sorrowing
`inside Lord [?] apostle because you exist apostle many sad(ly)`

**10**  on the Lord you have, because you apostles, all the apostles
`on-Lord have because you apostle each,_every apostle`

**11**  […] […] go and go […] and to and one and
`[?] [?] go-go [?] and to-and one and`

> Matthew 22:42, *what think ye of Christ? whose son is he?*, answered with
> Peter's confession from Matthew 16:16, *thou art the Christ, the Son of the
> living God*.

## 067v — he that believeth and is baptized shall be saved

**1**  one […] and this Lord, on the third day, rose again.
`one [?] and this-Lord +on_the_third_day +one-?again.`

**2**  He stood up, and this Lord, believing in you, within
`stand_up-to and this-Lord you believe-+day inside`

**3**  belief, afterwards […] there is
`believe ?afterward [?] exist`

**4**  a leaving; for ever, amen. And the two
`leave-chapter-leave chapter-oh chapter-oh amen and two`

**5**  men […] you, and the apostles are one
`somebody [?] you and exist apostle one`

**6**  God; the apostles believe, and the man who is outside this […]
`God believe apostle and somebody exist out(ward) this [?]`

**7**  and one man is saved, but every man is damned
`and one somebody be_saved a) each,_every somebody be_damned`

**8**  and the man who believes in […] Christ, this
`~to and somebody exist believe inside [?]-~Christ this`

**9**  whosoever shall be saved, because this is to the Lord, one God.
`?whosoever exist +be_saved because this to-Lord one God`

**10**  Here ends this holy gospel. […] the man has, he asks
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

**3**  the brethren, Paul the man would be saved first; he asks, the man,
`?brethren want-somebody-Paul +be_saved first | ask_(for)-somebody`

**4**  Paul: love the Lord most high with all the heart, and every man as his neighbour
`Paul love Lord-<suffix_of_divine_name> most_high each,_every +heart and each,_every somebody how?-to +neighbour`

**5**  as the neighbour; and the man shall be saved. In turn the second he has,
`to-+neighbour and exist somebody be_saved in_turn-two have`

**6**  Paul the man asks, in Jesus' name […]
`somebody-Paul ask_(for) inside Jézus +name [?]`

**7**  believe; Paul the man asks of Lord Jesus, in his
`believe ask_(for) somebody-Paul from Lord-Jézus inside <preposition_of_genitive>-Lord`

**8**  name. The third Paul the man has, he asks, in
`and-to-end-+name +third have somebody-Paul ask_(for) | inside`

**9**  Jesus' name, saved by Lord Jesus, in his
`Jézus and-to-end-+name be_saved from Lord-Jézus inside <preposition_of_genitive>-Lord`

**10**  […] name, and the man shall be saved. Here ends
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

**6**  supper: this Lord goes to his Father; you learn,
`dinner this-Lord go-Lord <preposition_of_genitive>-Lord father-<suffix_of_divine_name> you learn`

**7**  he does, heaven and earth, that is, this Lord […]
`do, heavenly land that_is this-Lord [?]`

**8**  to the death; the Lord dies, and this Lord goes from you […]
`on-die Lord die and this-Lord you go | [?]`

**9**  the day; in turn he who, this Lord, this dies for you […]
`+day in_turn-who this-Lord this die to you [?]`

**10**  the Holy Spirit; the Lord dies, and this Lord, to you
`holy-spirit Lord die and this-Lord you`

**11**  the Holy Spirit goes, and you shall see two
`go holy-spirit and you exist see-two`

**12**  judgments: first of sin; in turn the second of righteousness; the third, judgment
`judge first from +sin in_turn-two from righteous(ly) +third judge`

> John 16:7–8, *it is expedient for you that I go away... and when he is
> come, he will reprove the world of sin, and of righteousness, and of
> judgment.* Line 12 has the three in the gospel's order, counted with the
> codex's own ordinals.

## 069r — the Spirit, the tongues, and the signs

**1**  And then this Holy Spirit goes to you, from the Spirit
`and then-exist you go this holy-spirit from-spirit`

**2**  through it you receive […] every good thing, and there are
`through grab you [?] each,_every good and exist`

**3**  apostles […] who lift up tongues […] […] you shall have many
`apostle [?] who-go_up language [?] [?] you exist many`

**4**  miracles […] which the mouth speaks in the Old Testament word, and it lives
`miracle [?] which-mouth exist inside <pertaining_to_the_Old_Testament> word and living exist`

**5**  goes before […] […] […] the day of judgment
`go before [?] [?]-[?] [?] judge-+day`

**6**  because there are many miracles afterwards. Here ends this holy gospel.
`because-exist many miracle ?afterward end this holy-gospel`

**7**  Here begins this holy gospel
`begins this holy-gospel`

**8**  written by holy Luke, in the tenth
`write holy-Luke inside | ten`

**9**  the last chapter of his writing. Said
`?the_last chapter <preposition_of_genitive>-write say`

**10**  Lord Jesus to his apostles, at
`Lord-Jézus apostle <preposition_of_genitive>-Lord | on`

**11**  the last supper, this Lord […] his Father
`last dinner this-Lord [?] father-<suffix_of_divine_name> <preposition_of_genitive>-Lord +<subject_marker>`

> Acts 2, the tongues and the signs, joined to the promise of the Spirit at
> the supper.

## 069v — I am the vine, ye are the branches

**1**  the vineyard; in turn you are the branches, and
`farm in_turn you vine_branch and go`

**2**  the Father, the Lord's vineyard, the angel […] this […]
`father-<suffix_of_divine_name> <preposition_of_genitive>-Lord farm angel [?] this | [?]`

**3**  […] and without a name […] […]
`[?] and without-+name [?] | [?]`

**4**  […] he takes this and cuts it off, and […] out
`[?] grab this cut_off and [?] out(ward)`

**5**  onto the way […] and then Lord Jesus, and the man who is
`on-~way [?] +and_then Lord-Jézus and somebody exist`

**6**  within the Lord, carried by the Lord, stays; and this Lord is
`inside Lord-[?]-~carry-Lord stay and this-Lord exist`

**7**  within […]. And then Lord Jesus, to his apostles, O
`inside [?] +and_then Lord-Jézus apostle <preposition_of_genitive>-Lord oh`

**8**  the Lord's son, this law and love the Lord carries; can the apostles […]
`Lord son this +law-love-~carry-Lord can apostle [?]`

**9**  understand what this Lord […] to you, speaking
`understand who this-Lord you [?] | speak`

**10**  Lord; and the man who is in the Lord's commandment of love, the man carries, from
`Lord and somebody exist <preposition_of_genitive>-Lord commandment-love carry-somebody from`

**11**  the man who is within the Lord's law […] stays, and this Lord
`somebody exist inside Lord-+law-[?] stay and this-Lord`

> John 15:1–5. *I am the true vine, and my Father is the husbandman... ye are
> the branches... abide in me.* The vineyard is the codex's word for the
> husbandman's ground, and the cutting off on line 4 is John 15:2.

## 070r — the branch that beareth not is cast into the fire

**1**  the Lord is within […]; Lord Jesus said, who afterwards
`exist-Lord inside [?] say Lord-Jézus who ?afterward`

**2**  to his Father, this […] […] is good
`to-father-<suffix_of_divine_name> <preposition_of_genitive>-Lord this [?] [?] exist | good`

**3**  […] takes this and that […] […] from the Father
`[?] grab this-and-this [?] [?] from-father-<suffix_of_divine_name>`

**4**  of the Lord, upon whom every […] carries; and the Lord's Father goes
`<preposition_of_genitive>-Lord who-chapter each,_every [?] carry and go father <preposition_of_genitive>-Lord`

**5**  two evil vineyards, and this in turn what […]
`two evil farm and this in_turn-what [?]`

**6**  takes the evil vineyard, and […] to the evil
`grab evil farm and +<subject_marker> [?] on-~evil`

**7**  […] there is seen the gnashing of teeth and crying, for
`[?] there exist see grinding tooth crying chapter-oh`

**8**  ever. And then Lord Jesus, he is from his Father
`chapter-oh +and_then Lord-Jézus ?he_is from-father-<suffix_of_divine_name> <preposition_of_genitive>-Lord`

**9**  the Lord loves, and this Lord loves you; and Lord Jesus said, O
`Lord love and this-Lord you love and say Lord-Jézus oh`

**10**  the Lord's son, and you love, because the apostles are in love
`<preposition_of_genitive>-Lord son and you love because-exist apostle inside-love`

> John 15:6, *if a man abide not in me, he is cast forth as a branch... and
> men gather them, and cast them into the fire*, with the codex's own
> gnashing of teeth attached, then John 15:9, *as the Father hath loved me,
> so have I loved you.*

## 070v — ask in my name, and Paul's three askings again

**1**  in the commandment you are, the Lord's ten laws of love the apostles carry
`inside commandment you exist <preposition_of_genitive>-Lord +law-love-ten carry-apostle`

**2**  Lord Jesus said, and the man who carries […] […]
`say Lord-Jézus and somebody exist carry [?] [?]`

**3**  […] you first […] love the Lord, whatsoever it is
`[?] you first [?] Lord love whatever | ?is_he`

**4**  ye shall ask of the Father, of the Lord's Father, in
`exist ~ask_(for) from-father-<suffix_of_divine_name> from <preposition_of_genitive>-Lord from-father-<suffix_of_divine_name> inside`

**5**  the Lord's name, ye shall all receive it saved.
`<preposition_of_genitive>-Lord +name each,_every you be_saved grab`

**6**  Here ends this holy gospel. […] the man has, he asks
`end this holy-gospel [?] have somebody ask_(for)`

**7**  in Jesus' name he is saved, speaks holy Paul the apostle
`inside-Jézus +name +be_saved speak holy-Paul apostle`

**8**  this word; Paul's own; whosoever Paul
`this word exist-exist <preposition_of_genitive>-Paul have ?whosoever-Paul`

**9**  asks in Jesus' name; three things Paul the man asks
`ask_(for) inside-Jézus +name +three ask_(for) somebody-Paul`

**10**  if Paul the man would be saved, first he asks
`if want somebody-Paul +be_saved first ask_(for)`

> The ten commandments of love on line 1, then John 14:13 again, then the
> **same Paul passage as 068r, repeated almost word for word**. The codex
> reuses whole pericopes, which is what a preaching or lectionary collection
> does rather than a continuous narrative.

## 071r — the great commandment, repeated

**1**  Paul the man: love the Lord most high, literally with all the heart, and every man as
`somebody Paul love Lord-<suffix_of_divine_name> from literal each,_every +heart and each,_every somebody | how?`

**2**  the neighbour […] and the man shall be saved.
`to +neighbour [?] and exist somebody +be_saved`

**3**  In turn the second Paul the man has, he asks, in his […] and
`in_turn-two have somebody Paul ask_(for) inside <preposition_of_genitive>-Lord | and`

**4**  was named […] believe; Paul the man asks
`?was_named [?] believe ask_(for) somebody Paul`

**5**  of Lord Jesus, in the Lord's name. The third he has,
`from Lord-Jézus inside <preposition_of_genitive>-Lord +name +third have`

**6**  Paul the man asks in the Lord's name, saved
`somebody Paul ask_(for) inside <preposition_of_genitive>-Lord +name +be_saved`

**7**  by Lord Jesus, in the Lord's name; and
`from Lord-Jézus inside <preposition_of_genitive>-Lord +name and exist`

**8**  the man shall be saved. Here ends this apostle's holy gospel […]
`somebody +be_saved end this apostle holy-gospel [?]`

**9**  Here begins this holy gospel, written by
`begins this holy-gospel write`

**10**  holy Luke, in […] of
`holy-Luke inside [?] | <preposition_of_genitive>`

**11**  his writing. Lord Jesus said to his apostles
`write say Lord-Jézus apostle <preposition_of_genitive>-Lord`

**12**  at the last supper: you shall be driven out
`on-last dinner you | chase`

> The second copy of the great commandment, running straight on from 070v.

## 071v — a woman when she is in travail hath sorrow

**1**  cast out, for hearing; how one […] every
`+say out(ward) on-hear how? one [?] each,_every`

**2**  for the Lord's name. And then you
`to-<preposition_of_genitive>-Lord +name and then-exist you`

**3**  they will drive out, the apostles say; this is it: out, he who, apostle by apostle,
`chase want apostle say +this_is ~out(ward) ?he_who apostle-apostle`

**4**  Master […] and the Lord, the Jews put to death; and you
`Master [?] and Lord Jew(ish) die and you`

**5**  shall have much sorrow upon the Lord; in turn, one word,
`exist many sad(ly) on-Lord have in_turn one +say-exist`

**6**  joy […] your sorrow is […] until
`joy [?] you sad(ly) exist [?] ~until`

**7**  […] how; then one woman, the chief,
`[?] how? then-exist one baptize head`

**8**  a son is born […] she has no more; in turn, then
`son be_born [?] many not-not have in_turn | then`

**9**  the son is born, and of that comes joy over the son
`exist be_born from-~exist on-son joy this-Peter`

**10**  and your sorrow, in turn, joy; much sorrow
`and ~you sad(ly) in_turn-+say joy want many sad(ly)`

**11**  cast out, and […] in the year of judgment; in turn your sorrow, much
`~out(ward) and [?] on-judge-year in_turn you sad(ly) many`

**12**  joy cast out, and […] in the year of judgment. Here ends this holy gospel.
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

**3**  […] in the twenty-
`[?] inside | two`

**4**  fifth chapter
`ten-ten +five chapter`

**5**  of his writing. At that time,
`<preposition_of_genitive>-write time`

**6**  then, after the crucifixion
`then-exist on-execute`

**7**  of Lord Christ […] at that time then
`Lord-Christ [?]-+day time then-exist`

**8**  the apostles sat […] in Jerusalem, in the Lord's house, where the Lord
`sit apostle [?] inside Jerusalem inside Lord house where Lord-<suffix_of_divine_name>`

**9**  Lord Jesus made the supper; at that time he appeared, the Lord
`Lord-Jézus dinner do, time appear | Lord`

**10**  Jesus, to his apostles, in […] name, the man; and
`Jézus apostle <preposition_of_genitive>-Lord inside [?]-+name somebody and.`

**11**  he sat with the apostles […] and began to rebuke their unbelief
`sit to-apostle [?] and begin-admonish on-believe`

> Mark 16:14, *afterward he appeared unto the eleven as they sat at meat, and
> upbraided them with their unbelief.*

## 072v — go ye into all the world, he that believeth and is baptized

**1**  and Lord Jesus said, go ye, apostles, among the people, and
`and say Lord-Jézus you go apostle ?among_the_people and`

**2**  baptize in the Lord's name; and the man
`exist baptize inside <preposition_of_genitive>-Lord ?was_named and somebody`

**3**  who is baptized in the name of the Father and the Son
`exist baptize inside +name father-<suffix_of_divine_name> and son`

**4**  and the Holy Spirit, and believes in the Lord,
`and holy-spirit and exist Lord-to believe`

**5**  every such man shall be saved; and one is damned […]
`each,_every somebody +be_saved and one be_damned [?]`

**6**  […] and the man […] baptized, and believes in the Lord
`[?] and somebody [?] baptize and exist Lord-to`

**7**  and one […] but every man
`believe and one [?] a) each,_every somebody`

**8**  is damned […] […] and the man who believes in the Lord
`be_damned [?] [?] and somebody exist Lord-to believe`

**9**  shall do many miracles, all in the Lord's
`from exist many miracle do, each,_every inside <preposition_of_genitive>-Lord`

**10**  name; the man in the Lord's […]
`+name exist somebody inside <preposition_of_genitive>-Lord | and-exist`

**11**  […] name: the blind through light, the dead see and rise up.
`[?]-+name ~blind through light die from-see resurrect stand_up.`

> Mark 16:15–16, *go ye into all the world... he that believeth and is
> baptized shall be saved; but he that believeth not shall be damned*, with
> the baptismal formula of Matthew 28:19 folded into it.

## 073r — and these signs shall follow them that believe

**1**  the man in the Lord's name, the evil in
`exist somebody inside <preposition_of_genitive>-Lord +name evil inside`

**2**  the man casts out; he carries serpents in
`somebody exorcise exist serpent carry inside`

**3**  the hand, and the man cannot be bitten; the man, in
`hand ~exist somebody can bite exist somebody inside`

**4**  the Lord's name […] […] and whatever
`<preposition_of_genitive>-Lord +name [?] [?] and what-to`

**5**  the man […] the man, in the Lord's
`who somebody ~exist [?] exist somebody inside <preposition_of_genitive>-Lord`

**6**  name, at the cup […] of the man, why in turn he puts
`+name on-cup-[?]-+day <preposition_of_genitive>-somebody why?-in_turn put`

**7**  […] the man is healed, all in the Lord's
`[?] exist somebody from-healing each,_every inside <preposition_of_genitive>-Lord`

**8**  name; the man does many miracles, and
`+day-+name exist somebody many miracle do, and`

**9**  Lord Jesus said, this Lord goes to his Father, to you
`say Lord-Jézus this-Lord go to-<preposition_of_genitive>-Lord from-father-<suffix_of_divine_name> to-you`

**10**  the Lord, and the Lord goes, and this Lord, to you goes
`Lord and Lord-<suffix_of_divine_name> +<subject_marker> Lord go and this-Lord you go-Lord`

**11**  the Holy Spirit, and the apostles […] lift up tongues
`holy-spirit and exist apostle [?] who-go_up language`

> Mark 16:17–18, sign for sign and in order: *in my name shall they cast out
> devils; they shall speak with new tongues; they shall take up serpents; and
> if they drink any deadly thing, it shall not hurt them; they shall lay
> hands on the sick, and they shall recover.* The cup on line 6 is the deadly
> draught.

## 073v — he went on the way, and each time he said the same

**1**  […] and Lord Jesus said to his apostles, go, apostles […]
`[?] and say Lord-Jézus apostle <preposition_of_genitive>-Lord go-apostle [?]`

**2**  the mount; this Lord would go out truly, and the whole wide world; from his
`mount this-Lord want-Lord ~out(ward) righteous(ly) and the_whole_wide_world <preposition_of_genitive>-Lord | from`

**3**  Father; and he passed on, from the apostles; in turn the apostles knew the Lord went
`father-<suffix_of_divine_name> and trespass go-Lord from apostle in_turn apostle know Lord go apostle`

**4**  and then the Lord looked on the apostles and said, peace be unto you
`and then-exist from-see-Lord on-apostle and say-Lord +law you`

**5**  and then the Lord passed on the way; and a second time he looked on the apostles
`and then-exist trespass go-Lord on-~way and two from-see-Lord on-apostle`

**6**  and said, peace be unto you; and then the Lord passed on
`and say-Lord +law you and then-exist trespass go-Lord | on`

**7**  the way; in turn the apostles knew the Lord; on the Monday; and a third time he looked on the apostles
`~way in_turn apostle know Lord Monday-apostle and +three from-see-Lord on-apostle`

**8**  and said, peace be unto you; and then the Lord passed on
`and say-Lord +law you and then-exist trespass go-Lord`

**9**  the way; and a fourth time he looked on the apostles and said, peace be unto you
`on-~way and two-two from-see-Lord on-apostle and say-Lord +law | ?is_he`

**10**  […] and then the Lord passed on the way; and a fifth time
`[?] and then-exist trespass go-Lord on-~way and +five | from`

**11**  the Lord looked on the apostles and said, this Lord, to you, the eye
`see-Lord on-apostle and say-Lord this-Lord you +law eye`

> A numbered sequence of five, each ending in the same formula, counted with
> the codex's own ordinals: second, third, fourth, fifth. This is the shape of
> a devotional list rather than a gospel passage, and the repeated greeting
> reads as *peace be unto you*.

## 074r — he was received up into glory

**1**  to his sufferer, and to his Father, for ever
`to-sufferer <preposition_of_genitive>-Lord and <preposition_of_genitive>-Lord from-father-<suffix_of_divine_name> chapter-oh chapter-oh`

**2**  amen; because Lord Jesus would have him confess
`amen because want Lord-Jézus to-Lord confess have`

**3**  before his Father, in the year of judgment; then
`before from-father-<suffix_of_divine_name> <preposition_of_genitive>-Lord on-judge-year then-exist`

**4**  the Father goes to judge the living and the dead, the man; and the Lord said to the apostles,
`go father-<suffix_of_divine_name> judge living and die somebody and say-Lord apostle`

**5**  ye shall hear; his mother, and
`you exist hear <preposition_of_genitive>-Lord mother and`

**6**  Mary blessed upon all the apostles, and among this […]
`Mary bless on-each,_every apostle and among this [?]`

**7**  […] knew Lord Jesus, and […] Lord Jesus […]
`[?] know Lord-Jézus and [?] Lord-Jézus | [?]`

**8**  […] went […] and blessed all the whole wide world
`[?] go [?] and bless each,_every the_whole_wide_world ?world`

**9**  and the Lord was taken into eternal glory. At that time said holy
`and Lord grab to-?eternal ?glory time say | holy`

**10**  Peter: Master, how does this Lord have apostles, as it were, saying
`Peter Master how? this-Lord have apostle ?as say`

> Mark 16:19, *he was received up into heaven*, with the creed's *judge the
> quick and the dead* on line 4.

## 074v — the Lord's Prayer

**1**  Lord Jesus, this his son, as the Father of the man
`Lord-Jézus this <preposition_of_genitive>-Lord son ?as father-<suffix_of_divine_name> <preposition_of_genitive>-somebody`

**2**  and the Lord, in the eternal holy name of the Father; the man goes
`and-Lord inside ?eternal holy +name <preposition_of_genitive>-father-<suffix_of_divine_name> go somebody`

**3**  into the Father's kingdom; the whole wide world is the Lord's, as in heaven
`inside king <preposition_of_genitive>-father-<suffix_of_divine_name> exist the_whole_wide_world <preposition_of_genitive>-Lord how? +heaven`

**4**  so on earth […] of the man, every year
`this and ~earth [?] <preposition_of_genitive>-somebody each,_every year`

**5**  the Lord gives the man this day's bread; this man's trespass
`grab-Lord somebody today’s year this-somebody trespass`

**6**  forgive, as the man forgives his own; joy
`remit how?-to somebody remit <preposition_of_genitive>-somebody joy`

**7**  the man goes into pleasing […] from evil. Amen.
`go somebody inside pleasing-chapter [?] from evil amen`

**8**  Written by holy Matthew in his gospel. And the second time said
`write holy-Matthew inside <preposition_of_genitive> gospel and two say`

**9**  holy Peter: Master, Lord, when shall be […]
`holy-Peter Master Lord when? exist [?]`

**10**  the year of judgment? Lord Jesus Christ said […] out and out
`judge-year say Lord-Jézus-Christ [?] out(ward)-out(ward)`

> **The Lord's Prayer**, Matthew 6:9–13, and the codex says so on line 8.
> Hallowed be thy name, thy kingdom come, thy will be done in earth as it is
> in heaven, give us this day our daily bread, and forgive us our trespasses
> as we forgive them that trespass against us, and deliver us from evil.
> Amen. The word rendered *year* on lines 4–5 is the same root the dictionary
> gives as day or year, so *this day's bread* is the daily bread.

## 075r — two men in white apparel

**1**  In turn, out and out, two thousand years. And the third time said holy Peter:
`in_turn out(ward)-to-out(ward) two-to-?thousand-year and +three say holy-Peter`

**2**  Master, how shall the apostles […] write of the Lord? Lord Jesus said, one
`Master how? apostle [?] Lord write say Lord-Jézus one`

**3**  year write, apostles, literally; in turn the second, figuratively. And then
`year write apostle literal in_turn two metaphoric and then-exist`

**4**  the eternal […] was to Lord Jesus; and then
`?eternal [?] exist-to Lord-Jézus and then-exist`

**5**  Lord Jesus went into heaven, into glory; and the Lord's light
`go Lord-Jézus heaven ?glory and Lord light from`

**6**  departed, because Lord Jesus would have it so; then the Lord
`~leave because want Lord-Jézus then-exist Lord`

**7**  shone on the apostles of God, upon this world; and then the two
`apostle God shine on-this ?world and then-exist-two`

**8**  appeared, two angels, white […]
`appear two angel-angel white | [?]`

**9**  […] and then the two angels, to you
`[?] +and_then two angel-angel you`

**10**  apostles, O men, how see ye the Lord's joy? Jairus
`apostle-oh-<suffix_of_divine_name>-chapter man how? Lord joy see Jairus`

> Acts 1:10, *behold, two men stood by them in white apparel.* Lines 2–3 are
> a note on how the apostles are to write: one literally, the other
> figuratively, which is a commentator's remark, not a gospel verse.

## 075v — he shall so come, to judge the quick and the dead

**1**  he departed, from the eternal; in turn, to the end, this joy
`~leave ?from_the_eternal in_turn-chapter-end-chapter this joy`

**2**  the Lord would go to […] judge the living and the dead,
`want Lord go on-[?] judge living and die`

**3**  the man. And the two said, these two angels, go, apostles, into
`somebody and say-two this two angel-angel go-apostle inside`

**4**  the apostles, O; and the Lord […] the apostle-man.
`apostle-oh-<suffix_of_divine_name>-chapter and Lord [?] apostle-somebody.`

**5**  And […] they saw; the word was done by the two
`and [?] see word do, two | angel`

**6**  angels. Here ends this holy gospel. Love the Lord with all thy heart.
`angel end this holy-gospel +the_Lord love Lord-<suffix_of_divine_name> ?with_all_thy_heart`

**7**  The Lord spoke, the apostles, Lord Jesus Christ;
`speak-Lord apostle Lord-Jézus-Christ`

**8**  then the apostles prayed,
`then-exist apostle pray`

**9**  his son,
`<preposition_of_genitive>-Lord son`

**10**  this Father of the man
`this father-<suffix_of_divine_name>-<preposition_of_genitive>-somebody`

> Acts 1:11, *this same Jesus... shall so come in like manner*, with the
> creed's *judge the quick and the dead* on line 2.

## 076r — how oft shall my brother sin against me

**1**  […] to the apostles many said […] written […] […]
`[?] to-apostle many say [?] write [?] [?]`

**2**  in the first chapter of his writing. At that time, then, Lord Jesus Christ
`inside +one chapter <preposition_of_genitive>-write time then-exist Lord-Jézus-Christ`

**3**  in the thirtieth year, and three days, and five months, and three days, at
`inside thirty year and +three_days and +five moon and +three_days inside`

**4**  that time left the apostles, to Lord Jesus; and then holy Peter
`time leave-to-leave apostle ~to Lord-Jézus +and_then holy-Peter`

**5**  answered, would the most high, this Peter, have mercy […] Peter is
`+answered want-high this-Peter have_mercy [?] exist Peter`

**6**  […] and then Lord Jesus Christ: Peter, Peter, in turn
`[?] +and_then Lord-Jézus-Christ Peter Peter | in_turn`

**7**  the brethren, one […] […] one year, through the sin of a man
`?brethren +one-[?] [?] one year through sin somebody`

**8**  against this Peter; have mercy, the man, if the man goes to mercy,
`against this-Peter have_mercy somebody +<subject_marker> if go somebody-have_mercy`

**9**  asks mercy, the man receives […] goes
`ask_(for)-have_mercy-somebody +<subject_marker> grab [?] go`

**10**  […] the man of mercy; and cried to Lord Jesus Christ
`[?] somebody-have_mercy and shout-to Lord-Jézus-Christ`

> Matthew 18:21, *Lord, how oft shall my brother sin against me, and I
> forgive him?* The dating on line 3 is the codex's own, not the gospel's.

## 076v — the catalogue of sins

**1**  he departed on the water of heaven […] Peter, Peter, if rather
`~leave on-water heaven [?] Peter Peter if-?but_rather`

**2**  a man among the apostles sins against you […] from
`+<subject_marker> somebody among apostle you sin [?] from`

**3**  […] the man, the apostle, the sin […] […] the man, of
`[?] somebody apostle +sin [?] [?] somebody | <preposition_of_genitive>`

**4**  the man's sin, leave it; but if a man's sins are many, in turn
`somebody-+sin leave a) if-exist many somebody-+sin in_turn`

**5**  he who is a thief; in turn […]; in turn a shedder of blood, that is
`thief-who in_turn [?] in_turn blood blood_shedder that_is`

**6**  a killer of men; the man in turn […]; the man in turn from […]
`people-die somebody in_turn [?] somebody in_turn from [?]`

**7**  the man in turn proud; the man in turn a drinker; the man in turn many
`somebody in_turn proud somebody in_turn drink somebody in_turn many`

**8**  […]; the man in turn under many yokes; this Peter
`[?] somebody in_turn many yoke-chapter somebody this-on-Peter`

**9**  said Lord Jesus Christ, because Peter is […] in turn in […]
`say Lord-Jézus-Christ because exist Peter [?] in_turn inside [?]`

**10**  the man, this […] how then the man dies in turn
`somebody this [?] how? then-exist somebody die in_turn`

> A list of sins built on the repeated *in turn*: thief, shedder of blood,
> manslayer, proud, drunkard. Catalogues like this belong to the confessional
> handbook rather than to the gospel.

## 077r — one sin, and whosoever sins is damned

**1**  […] the man […] have mercy; the man in turn from riches […]
`[?] somebody [?] have_mercy somebody in_turn from-rich-from [?]`

**2**  the man in turn […] truly; the man, or the man judges
`somebody in_turn [?] righteous(ly) somebody or ~judge somebody`

**3**  of whom holy Paul speaks […] said Lord Jesus Christ, this […]
`who speak holy-Paul [?] say Lord-Jézus-Christ this [?]`

**4**  the man sins one sin […] he is saved; and he who hides
`somebody sin one +sin [?] be_saved and who-hide_oneself`

**5**  the man […] […] in sin, to Lord Jesus Christ
`somebody [?] [?] on-sin to Lord-Jézus-Christ`

**6**  one sin […] is saved; but every one, whosoever sins, is damned
`one +sin [?] be_saved a) each,_every ?whosoever-+sin be_damned`

**7**  said Lord Jesus Christ: Peter, Peter […] that is […]
`say Lord-Jézus-Christ Peter Peter [?] that_is [?]`

**8**  whosoever sins […] the apostle, this whosoever sins, from […] […]
`?whosoever-+sin [?] apostle-this-?whosoever-+sin from [?] [?]`

**9**  […] the man, of […] leaves […]
`[?] somebody <preposition_of_genitive>-[?] leave [?]`

**10**  the man […] the voice […] the brethren, the man says, this man
`somebody [?] voice,_sound [?] ?brethren-exist somebody say somebody this`

> Still Matthew 18, the sin of a brother and the forgiving of it.

## 077v — go to him alone, then take two, then three

**1**  he loves Lord Jesus Christ more than these. Lord Jesus Christ said to Peter:
`+<subject_marker> love Lord-Jézus-Christ ?more_than_these say Lord-Jézus-Christ to-Peter`

**2**  in turn […] the apostle-man among […]; the man who sins, go to
`in_turn [?] apostle-somebody among [?] somebody-+sin go | to`

**3**  Peter, […] the sin, to the house; and the man upon his sin
`Peter [?]-+sin to-home and somebody-on-+sin`

**4**  rebuke, because this man who sins suffers; in turn, to whom this man
`admonish because this somebody-+sin sufferer in_turn to-which this-somebody`

**5**  suffers […] the apostle, this whosoever sins, from […] […]
`sufferer [?] apostle this ?whosoever-+sin from [?] [?]`

**6**  he looks; of […] he leaves; but Peter goes, to Peter, two
`from-see <preposition_of_genitive>-[?] leave a) go-Peter to-Peter two`

**7**  […] the sin; and the man upon his sin rebuke, because this whosoever sins
`[?]-+sin and somebody-on-+sin admonish because this ?whosoever-+sin`

**8**  suffers; in turn, to whom this man suffers […] the apostle, this whosoever sins
`sufferer in_turn to-which this-somebody sufferer [?] apostle this ?whosoever-+sin`

**9**  from […] […] the man, of […] leaves; but
`from [?] [?] somebody <preposition_of_genitive>-[?] leave a)`

**10**  Peter goes, to Peter, a third time […] the sin, and the man
`go Peter to-Peter +three [?]-+sin and somebody`

> Matthew 18:15–17, and the codex counts the three steps with its own
> ordinals: go alone first, then take two, then a third time. Line 1 is
> *lovest thou me more than these*, John 21:15, put in front of it.

## 078r — judge righteous judgment

**1**  upon his sin rebuke, because this whosoever sins suffers; in turn, to whom this man
`on-sin admonish because this ?whosoever-+sin sufferer in_turn to-which this-somebody`

**2**  suffers, take him, whosoever sins […] from […] within
`sufferer grab ?whosoever-+sin [?] from [?] inside`

**3**  why in turn? because this is truly, truly, to whosoever sins; because
`why?-in_turn because this exist righteous(ly) righteous(ly) to-?whosoever-+sin because`

**4**  a false judge […] judges whosoever, truly judge
`false ~judge-somebody [?] chapter-judge-?whosoever righteous(ly) judge`

**5**  but rather every […] false judgment; in turn the false judge
`?but_rather-each,_every [?] false judge in_turn false ~judge-somebody`

**6**  the true man falsely judged is damned, in the evil
`righteous(ly) somebody false from-judge be_damned +<subject_marker> inside ~evil`

**7**  for ever; in turn the true judge, every one
`+<subject_marker> chapter-oh chapter-oh in_turn righteous(ly) ~judge-somebody each,_every`

**8**  to whom he judges truly […] the judge falsely
`to-which-chapter righteous(ly) judge [?] judge-somebody false`

**9**  judging, but rather to whom he judges truly; the Lord speaks, every writing
`from-judge ?but_rather-each,_every to-which-chapter righteous(ly) judge Lord-<suffix_of_divine_name> speak each,_every write`

**10**  and every prophet and every church father and every forefather and […]
`and each,_every prophet and each,_every church_father and each,_every forefather and [?]`

> John 7:24, *judge not according to the appearance, but judge righteous
> judgment*, worked out at length against the false judge.

## 079r — the orders of angels, and one word

**1**  among all peoples, to eternal glory, most high, all the angels, the orders of angels
`inside each,_every ?people to-?eternal ?glory most_high each,_every angel angel angel order`

**2**  […] eat literally, from the one Lord, truly […] speaks holy Paul
`[?] eat literal from one Lord righteous(ly) [?] speak holy-Paul`

**3**  […] Paul's own, this Lord truly […] Lord Jesus Christ
`[?] exist-exist <preposition_of_genitive>-Paul this-Lord righteous(ly) [?] Lord-Jézus-Christ`

**4**  this Lord judges all peoples by one word […] the word, every
`this-Lord exist judge each,_every ?people one word [?] word each,_every`

**5**  man […] of the man, truly, good, mercy, saying, love, doing; and
`somebody [?] <preposition_of_genitive>-somebody righteous(ly)-good-have_mercy-say-love-do, and`

**6**  the Lord takes; this Lord truly […] and the Lord, every
`grab Lord-<suffix_of_divine_name> +<subject_marker> this-Lord righteous(ly) [?] and Lord-<suffix_of_divine_name> each,_every`

**7**  man receives […] from the Lord […] the man
`somebody exist grab [?] exist from Lord-<suffix_of_divine_name> [?] somebody`

**8**  the firstborn is damned, to be […] […] […]
`firstborn exist be_damned to-exist-~exist [?] [?] [?]`

**9**  damned […] […] […] and nine […]
`be_damned [?] [?] [?] and nine [?]`

> The nine orders of angels on line 1, which is Pseudo-Dionysius by way of
> every medieval preaching book, and the judgment of all peoples by one word.

## 080r — the Comforter, and the threefold reproof

**1**  Before the gospel: written by holy John, in the sixteenth chapter of his writing.
`before gospel write holy-John inside ten-six chapter <of>-write`

**2**  Then said the Lord Jesus to his apostles at the last supper: this Lord
`time say Lord-Jézus apostle <of>-Lord on-last dinner this-Lord`

**3**  goes to his Father. You know that
`go-Lord <of>-Lord father-<divine> you learn do,`

**4**  the heavenly kingdom, that is: this Lord goes away, to die; the Lord
`heavenly land that_is this-Lord ?go_away on-die Lord`

**5**  dies, and this Lord sends you the Holy Spirit. In turn,
`die and this-Lord you go holy-spirit | in_turn`

**6**  if this Lord did not die, did not go away, to you the Holy Spirit
`who this-Lord this die to you +go_not_away holy-spirit`

**7**  [would not come]. The Lord dies, and this Lord sends you the Holy Spirit,
`Lord-die and this-Lord you go holy-spirit`

**8**  and you shall see two judgments: the first, of sin;
`and you exist see-two judge first from +sin`

**9**  the second, of righteousness; the third, judgment. And then you
`in_turn-two from righteous(ly) +third judge and then-exist you`

**10**  receive this Holy Spirit; from the Spirit, through him, he takes you.
`go this holy-spirit from-spirit through grab you`

> John 16:7-13: "if I go not away, the Comforter will not come unto you; but
> if I depart, I will send him unto you. And when he is come, he will reprove
> the world of sin, and of righteousness, and of judgment ... he will guide
> you into all truth." The citation on line 1 is right. The two readings
> marked here, *go away* and *go not away*, sit where Király & Tokai's own
> apparatus puts a negated *go* on these very lines.

## 080v — the apostles wait in prayer with Mary

**1**  […] every good thing; and the apostles […] lift up […] […]
`[?] each,_every good and exist apostle [?] who-go_up [?] [?]`

**2**  […] ye shall have many miracles, says the mouth
`[?] you exist many miracle say which-mouth-chapter-year`

**3**  in the Old Testament word, and it lives; go before […] […]
`inside <pertaining_to_the_Old_Testament> word and living-exist go before [?] [?]-[?]`

**4**  […] the day of judgment. Here ends this teaching gospel. Here begins
`[?] judge-+day end this +<subject_marker> learn holy-gospel begins`

**5**  this holy gospel, written by holy Luke, in the second chapter of his writing. At that time,
`this holy-gospel write holy-Luke inside two chapter <preposition_of_genitive>-write time`

**6**  then, after the crucifixion of Lord Christ […] year; and then
`then-exist on-execute Lord-~Christ [?]-year and | then`

**7**  the Lord was […] year; at that time the apostles remained in prayer
`Lord-exist [?]-year time leave apostle pray`

**8**  in the Lord's, until where the Lord, Lord Jesus, made the supper; out
`inside Lord ~until where Lord-<suffix_of_divine_name> Lord-Jézus dinner do, on-~out(ward)`

**9**  ten years; and then this went on ten years; at that time the apostles remained in
`ten-year and then-exist keep_going this ten-year time leave apostle on`

**10**  prayer; and holy Peter left, to the Virgin Mary. And then
`pray and leave-to-leave holy-Peter to virgin-Mary +and_then`

> Acts 1:14, *these all continued with one accord in prayer and supplication,
> with Mary the mother of Jesus.* The upper room is named as the place where
> the supper was made.

## 081r — the Spirit comes upon them

**1**  holy Peter, the wife, to the apostles answered, speaking; understand, apostles, the Lord is
`holy-Peter wife apostle-to +answered speak understand apostle exist-Lord`

**2**  from […] the Holy Spirit goes, to Peter the rock […] this
`from [?] go holy-spirit rock-to Peter [?]-+day this`

**3**  is. And then the Virgin Mary, then the Father, from […]
`exist +and_then virgin-Mary then-exist father-<suffix_of_divine_name> from [?]`

**4**  the Holy Spirit goes; father Abraham, and Abraham
`go holy-spirit father Abraham and Abraham`

**5**  the spirit goes upon the eleven […] understand the spirit
`spirit go on-ten-+one-[?] understand spirit`

**6**  and the apostles, Mary, on high; go, upon this; said Lord Jesus, his Father,
`and apostle-Mary to-high go on-this say say Lord-Jézus father-<suffix_of_divine_name> <preposition_of_genitive>-Lord`

**7**  this Lord from […] goes, his own Holy Spirit
`this-Lord from [?] go <preposition_of_genitive>-Lord exist-exist holy-spirit`

**8**  and his mother. And then the Father, how, in what form would he go
`and <preposition_of_genitive>-Lord mother +and_then father-<suffix_of_divine_name> how? shape,_form want go`

**9**  if he goes into God, the Son, the Spirit; the Lord, Father, Son, Holy Spirit
`if go inside God-son-spirit-Lord father son holy-spirit`

**10**  […] this people crucified; and then the Father, holy
`[?] this ?people +cross execute +and_then father-<suffix_of_divine_name> | holy`

> Pentecost, Acts 2, with the eleven named on line 5 and the Trinity set out
> on line 9.

## 081v — cloven tongues like as of fire

**1**  the Spirit took, upon the spirit, the form of fire
`spirit grab on-spirit fire shape,_form`

**2**  and the Spirit went out from the apostles, Mary, the Jews, and the man
`and go spirit from somebody-apostle-Mary-Jew(ish) and somebody`

**3**  this Spirit […] the apostles, the Jews; and it took, upon the spirit,
`this spirit [?] apostle-Jew(ish) and grab on-spirit`

**4**  the Spirit, the form of holy fire, and the Spirit went
`spirit holy-fire shape,_form and go-spirit`

**5**  out from the apostles, Mary, the Jews; and the man, the Spirit […]
`from somebody-apostle-Mary-Jew(ish) and somebody spirit [?]`

**6**  the apostles, Mary, the Jews, many […] […]
`somebody-apostle-Mary-Jew(ish) many [?] [?]`

**7**  many a wind, in that form […] in fire
`many sough inside shape,_form [?] inside fire`

**8**  in that form; and the Jews saw this fire,
`inside shape,_form and see Jew(ish) this fire.`

**9**  that form, and it came down upon this house where the apostles and Mary
`shape,_form and bow_down on-this house where apostle-Mary`

**10**  were at prayer. And then the Jews said, the chief, that is
`on-pray +and_then-+say Jew(ish) ~head-chapter that_is`

> Acts 2:2–3, *a rushing mighty wind... and there appeared unto them cloven
> tongues like as of fire, and it sat upon each of them.* The wind is on line
> 7 and the descent on the house on line 9.

## 082r — the Jews see it, and three thousand are added

**1**  the Lord; the apostles began to believe, every wind, and […] the Jews
`Lord ~begin-believe apostle each,_every sough and [?] Jew(ish)`

**2**  saw it, because […] the Jews […] every wind; and then
`on-see because [?] Jew(ish) [?] each,_every sough and | then`

**3**  the Jews were […] in the house where the apostles and Mary were at
`exist Jew(ish) [?] inside house where apostle-Mary | on`

**4**  prayer, to […] from the apostles and Mary at prayer, they left
`pray to [?] from apostle-Mary on-pray leave`

**5**  the heavenly word; thanks, apostles and Mary, to the Lord; thanks to the Lord God; and
`heavenly word thanks apostle-Mary to-Lord thanks Lord God and`

**6**  various […] […] and then the Jews […]
`various [?] [?] +and_then Jew(ish) [?].`

**7**  these apostles; the sons of Jerusalem saw how […] […] and then the apostles
`this-apostle Jerusalem son see how? [?] [?] +and_then apostle`

**8**  are apostles, Master, from […] the Holy Spirit goes […]
`+<subject_marker> exist apostle Master from [?] go holy-spirit [?]`

**9**  the apostles, the one who […] went from the people, the Jews, one […]
`apostle +one-who food go from people-+day Jew(ish) +one-[?]`

**10**  the people received belief in Lord Jesus Christ, and every
`people-+day grab believe Lord-Jézus-Christ and each,_every`

> Acts 2:6–12, the crowd hearing them, and then Acts 2:41, *and the same day
> there were added unto them about three thousand souls*, which the next
> folio counts.

## 082v — three thousand added, and the Trinity begins

**1**  man, Jew, apostle, Mary, received the Holy Spirit; and two years, three baptisms, from
`somebody-Jew(ish)-apostle-Mary grab holy-spirit and two-year +three-+baptize from`

**2**  the Jews […] and […] baptism […] three thousand, and
`Jew(ish) [?] and [?] ?baptism-[?] +three-thousand-+day and`

**3**  one […] son, seven sons; and from the son received holy
`+one-[?]-[?] ~son +seven ~son and from ~son grab | holy`

**4**  Spirit […] upon the spirit, the Holy Spirit, every man, Jew,
`spirit [?] on-spirit holy-spirit each,_every | somebody-Jew(ish)`

**5**  son […] received the Holy Spirit and believed in the Lord
`~son-[?] grab holy-spirit and believe | Lord`

**6**  Jesus Christ […] believing, the man would […]
`Jézus-Christ [?] on-believe somebody want +one-can [?]`

**7**  in turn […] Here ends this holy gospel, this Holy Spirit.
`in_turn-[?] end this holy-gospel this holy-spirit.`

**8**  […] from the Father, out and out, the Spirit proceeds; in turn the Son,
`[?] on-father out(ward)-out(ward) go_out-spirit in_turn son`

**9**  this Son, from the Father, sitteth; see, he is this […]
`this-son from to-father-<suffix_of_divine_name> sit see ?he_is this | [?]`

**10**  […] the Sun; this sun has three good things; first
`[?] Sun this sun +<subject_marker> +three good first`

> The three thousand of Acts 2:41 on line 2, then the folio turns to the
> procession of the Spirit and sets up the sun analogy for the Trinity.

## 083v — the sun, its light and its warmth

**1**  is good […] he who is light; in turn the second is good, warmth; the third is good
`+<subject_marker> good [?] ?he_who light in_turn-two +<subject_marker> good warmth +third +<subject_marker> good`

**2**  from the Sun; the sun's light signifies the Son of God; in turn the warmth
`from-Sun sun Sun light symbolize son God in_turn warmth`

**3**  signifies the Holy Spirit; in turn the Sun itself signifies the Father; upon this Lord, from the Sun
`symbolize holy-spirit in_turn from-Sun symbolize from-father-<suffix_of_divine_name> on-this-Lord from-Sun`

**4**  proceeds the light, proceeds the warmth, proceeds the Son from the Father,
`on-go_out light on-go_out warmth on-go_out son on-from-father-<suffix_of_divine_name>`

**5**  proceeds the Holy Spirit from the Father; he is the sun,
`on-go_out holy-spirit on-from-father-<suffix_of_divine_name> ?he_is sun`

**6**  one form; this
`one shape,_form | this`

**7**  is one God; in turn who
`+<subject_marker> one God in_turn-who`

**8**  is, this can have, how
`+<subject_marker> this can have how?`

**9**  can heaven and earth
`can heaven earth`

**10**  quake, and in his […] prepare
`quake and inside <preposition_of_genitive>-Lord [?] prepare`

**11**  heaven, in turn, and the earth
`heaven in_turn-chapter-in_turn-from-in_turn and earth`

> The sun analogy for the Trinity: the sun itself is the Father, its light
> the Son, its warmth the Spirit, and all three are one sun. Standard
> patristic teaching, set out here as a numbered list.

## 084r — Augustine and the child on the seashore

**1**  At that time, then,
`time then-exist`

**2**  after the condemning of Lord Jesus
`on-?condemned Lord-Jézus`

**3**  Christ, in the sixtieth year, at that time
`Christ six-ten-year time`

**4**  holy Augustine went to the shore
`go holy-Augustine shore`

**5**  of the sea, because he would
`sea because want`

**6**  understand how it is
`understand ?likewise`

**7**  that three, Lord, Lord, Lord, Father,
`+three Lord-Lord-Lord father`

**8**  Son, Spirit, are one God; and this is one
`son spirit one God and this exist one`

**9**  […] in the evening […] at the going down of the sun; and then
`[?] evening [?] sun on-go_out and then-exist`

**10**  he found one little child on the shore; this
`find one little son-Lord-<suffix_of_divine_name> on-shore this`

**11**  […] that day the little child sat […] and
`[?]-daily,_of_that_day sit son-Lord-<suffix_of_divine_name> little [?] and | <preposition_of_genitive>`

**12**  the child […] one pit […] and
`son-Lord-<suffix_of_divine_name> [?] one pit [?] and | <preposition_of_genitive>`

**13**  the child carried in his hand one spoon, and this
`son-Lord-<suffix_of_divine_name> hand one spoon carry-son-Lord-<suffix_of_divine_name> and this`

**14**  that day the child scooped with this spoon into this pit, this child
`[?]-daily,_of_that_day this spoon inside this pit scoop-son-Lord-<suffix_of_divine_name> this son`

> **The legend of Saint Augustine and the child on the seashore**, who is
> emptying the sea into a hole with a spoon, and tells Augustine that he will
> sooner do that than understand the Trinity. It is in the Golden Legend,
> which is in this project's reference corpus, and it follows directly from
> the sun analogy on the folio before.

## 084v — thou shalt sooner empty the sea

**1**  And then holy Augustine, this […] child,
`+and_then holy-Augustine this [?] son-Lord-<suffix_of_divine_name>`

**2**  what does this child want? Said the child, this:
`who this want-son-Lord-<suffix_of_divine_name> say want-son-Lord-<suffix_of_divine_name> this.`

**3**  that day into this pit I scoop. Said holy Augustine, this
`[?]-daily,_of_that_day inside this pit scoop say holy-Augustine | this`

**4**  child, can this child do it? What
`son-Lord-<suffix_of_divine_name> this can-son-Lord-<suffix_of_divine_name> do, who | this`

**5**  child, this, that day, into this pit the child scoops
`son-Lord-<suffix_of_divine_name> this [?]-daily,_of_that_day inside this pit scoop-son-Lord-<suffix_of_divine_name>`

**6**  said this […] child; first this child, can
`say this [?] son-Lord-<suffix_of_divine_name> first this-son this | can`

**7**  the child do it, and this Augustine, upon leaving
`son-Lord-<suffix_of_divine_name> do, a)-who this-Augustine on-chapter-leave-this`

**8**  and the child […] saw the word afterwards, before
`and son-Lord-<suffix_of_divine_name> [?] see word ?afterward before`

**9**  holy Augustine; and he could tell many this […] in writing […]
`holy-Augustine and can to-many this [?] on-write [?]`

**10**  but believe truly, this woman, one God, of
`a) +believe righteous(ly) this-woman one God | <preposition_of_genitive>`

**11**  the man, heaven and earth, that is, he has
`somebody-+<subject_marker> heaven land that_is have`

**12**  carries the law of God […] sin, the man is saved
`carry +law God [?] +sin somebody be_saved`

**13**  the man answered, to many, he shall never die, for
`somebody ?answered to-many not-not-die chapter-oh chapter-oh`

**14**  ever, amen; speaks […] […] his own
`amen speak [?] [?] exist-exist <preposition_of_genitive>`

> The child tells Augustine he will sooner empty the sea into the pit than
> understand the Trinity, and Augustine goes away and writes of it.

## 085r — one commandment broken is all of them broken

**1**  and among you, through transgressing one
`and among you through transgress one`

**2**  of God's laws, the commandment, every man […] receives before
`+law God to-commandment each,_every somebody-+<subject_marker> [?] grab before`

**3**  […] thanks to the Lord, because if a man one
`[?] to-Lord thanks Lord-<suffix_of_divine_name> because and somebody one`

**4**  transgresses, how then is he a transgressor of every law? because
`transgress how? then-exist each,_every +law ~transgress somebody | because`

**5**  it is the Lord's; he received it from his angel, in the Old
`+<subject_marker> exist Lord-<suffix_of_divine_name> grab on-angel <preposition_of_genitive>-Lord inside <pertaining_to_the_Old_Testament>`

**6**  Testament word, father Abraham […] ten and one commandment
`word father Abraham [?]-ten and +one-[?] commandment`

**7**  […] this, more than these, go and be saved among men; the Lord
`[?] this ?more_than_these go be_saved among somebody Lord`

**8**  of the Jews, Jesus, apostle to the gentiles, most high […] the Son of the living God
`Jew(ish) Jézus apostle-pagan ?above-high [?] son living God`

**9**  Lord Jesus Christ; and to the man from […] and to the man the soul
`Lord-Jézus-Christ and to-somebody from [?] and to-somebody soul`

**10**  upon the cross […] and for the man his blood was shed, and the man
`~on-+cross-[?] and to-somebody +<subject_marker> <preposition_of_genitive> blood shed and somebody +<subject_marker>`

**11**  the Lord redeemed from hell fire […] the man, to many, until
`redeem-Lord from hell fire [?] somebody to-many from-until`

**12**  the ten laws; believe truly, be baptized […] one God
`ten-+law +believe righteous(ly) ?baptism-[?] one God`

> James 2:10, *whosoever shall keep the whole law, and yet offend in one
> point, he is guilty of all*, set against the ten commandments.

## 085v — Elijah calls down fire

**1**  of the man, heaven and earth, that is, he has
`<preposition_of_genitive>-somebody +<subject_marker> heaven land that_is have`

**2**  carries the law of God […] sin, the man is saved
`carry +law God [?] +sin somebody be_saved`

**3**  the man answered, to many, he shall never die, for
`somebody ?answered to-many not-not-die chapter-oh chapter-oh`

**4**  ever, amen. Speaks holy Augustine, to many: believe, the man, in
`amen speak holy-Augustine to-many +believe somebody inside`

**5**  God for ever […] God can, for ever.
`God exist-exist-chapter [?] God can inside exist-exist-chapter.`

**6**  […] this day, in the place, the man receives
`to-from [?] exist-today’s on-place grab somebody`

**7**  in his mouth; speaks holy Elijah the prophet, it is written.
`inside <preposition_of_genitive>-somebody mouth speak holy-Elijah prophet write.`

**8**  Holy the prophet, holy Moses, there was […] fire upon all peoples
`holy-<name_of_a_prophet> holy-Moses exist [?] fire on-each,_every ?people`

**9**  to heaven on high, because all peoples were destroyed; kneeled one
`to-heaven high because-exist each,_every ?people destroy kneel_(down) one`

**10**  holy Elijah the prophet. At that time, then, the Lord destroyed
`holy-Elijah prophet time then-exist Lord-<suffix_of_divine_name> destroy-Lord`

**11**  the earth; there was fire in one place, and […] from
`earth exist fire inside one place and [?] | from`

**12**  piercing […] to the Lord, in water; upon this the destroying was three
`pierce [?] to-to Lord-<suffix_of_divine_name> inside water on-this destroy exist +three`

> 1 Kings 18:36–38, Elijah at Carmel, the water poured over the altar and the
> fire of the Lord falling.

## 086r — the torch lit from heaven

**1**  twenty years and six years; at that time holy Elijah kneeled
`two-two-ten-year and six-year time kneel_(down) holy-Elijah`

**2**  and prayed; thanks to the Lord; and fire
`and pray to-Lord thanks Lord-<suffix_of_divine_name> to fire`

**3**  from the gate of God, the angel of heaven; and rather
`from-gate God angel heaven and from ?but_rather`

**4**  fire […] one […] […] said
`fire [?] one [?] [?] say`

**5**  the angel of God: Elijah, this signifies the Lord, the Lord of
`God angel Elijah this exist symbolize Lord-<suffix_of_divine_name> Lord | <preposition_of_genitive>`

**6**  angels. And then holy Elijah took a torch, and the torch
`angel and then-exist grab holy-Elijah torch ~and torch`

**7**  gave light; in turn this […] […] went to Elijah, from twenty
`light in_turn this [?] [?] go to-Elijah from | two-two`

**8**  twenty peoples, and every one […] the torch gave light; in turn
`two-two people-+day and each,_every from-[?] torch light in_turn`

**9**  holy Elijah […] […] and in Elijah, until
`holy-Elijah [?] [?] and inside Elijah from-until`

**10**  until; and then holy Elijah, then, forty
`from-until +and_then holy-Elijah then-exist | two-two-two-two`

**11**  days. This is written by holy Moses in the Old Testament word.
`ten-+day +this_is write holy-Moses inside <pertaining_to_the_Old_Testament> word`

> The fire from heaven becomes a torch, and the torch a figure, which the
> next folio applies to the Virgin.

## 086v — the torch signifies the Virgin

**1**  it signifies […] […] the angel from the Father, for ever
`symbolize [?] [?] exist angel from-father inside exist-exist-chapter`

**2**  to the blessed Virgin Mary, one son, the Lord […] signifies
`to-happy virgin-Mary son one Lord-<suffix_of_divine_name> [?] symbolize`

**3**  the man, for ever […] received, upon the Lord
`somebody exist-exist-chapter [?] exist grab | on-Lord`

**4**  Jesus Christ; it signifies the torch, for ever, to the blessed Virgin
`Jézus-Christ symbolize torch exist-exist-chapter to-happy | virgin`

**5**  Mary; then Mary conceived the Lord, and Jesus saved the whole wide
`Mary then-exist-Mary get_conceived Lord-<suffix_of_divine_name> and Jézus be_saved each,_every the_whole_wide_world`

**6**  world; and Christ […] of the man, and the Lord, the head […]
`?world and Christ [?]-to-[?] <preposition_of_genitive>-somebody and Lord ~head-[?]-~son`

**7**  heaven and earth […] signifies, for ever, Lord Jesus
`heaven and earth [?] symbolize exist-exist-chapter Lord-Jézus`

**8**  Christ […] the fire signifies the Lord, and every one can […] God the Father
`Christ [?] symbolize fire Lord-<suffix_of_divine_name> and can each,_every | father-God`

**9**  Lord Jesus Christ, the angel, the Holy Spirit, Mary, the apostles, one […]
`Lord-Jézus-Christ-angel-holy-spirit-Mary-apostle one [?]`

**10**  God […] and this […] is, until the crucifying
`God [?] and this [?] exist from-until on-execute`

**11**  of Lord Jesus Christ, at thirty, in […] the Lord's year, upon the whole wide world
`Lord-Jézus-Christ on-thirty inside [?] Lord-year on-each,_every the_whole_wide_world ?world`

> The torch lit but not consumed is read as the Virgin, which is the same
> figure the burning bush usually carries. Typology of this kind is why the
> book keeps saying *signifies*.

## 087r — the torch and the light

**1**  and the man who eats this day […] the Son
`and somebody exist this exist-today’s eat [?] son`

**2**  of God […] every man shall be saved; and one
`God [?] each,_every somebody +be_saved and one`

**3**  man […] Elijah signifies, for ever, the blessed
`somebody [?] Elijah symbolize exist-exist-chapter to-happy`

**4**  Virgin Mary, how from Mary the torch gave light at his coming
`virgin-Mary how? from-Mary torch light then-?coming`

**5**  the Lord created of the man, and the cross could, to one
`create-Lord <preposition_of_genitive>-somebody and can +cross to-one`

**6**  man's death, but all peoples die; this one, one man
`somebody die a) each,_every ?people die this-+one one somebody`

**7**  could, God, everything, in his mouth receives, because the Lord
`can God each,_every inside <preposition_of_genitive>-somebody mouth grab because Lord-<suffix_of_divine_name>`

**8**  […] for ever, but rather […] God is
`[?] exist-exist-chapter +but_rather [?] God-+<subject_marker>`

**9**  many […] and […] and from […] […]
`many [?] and [?] and from [?] [?]`

**10**  the earth […] and heaven on high, and God is
`earth [?] and heaven high and God-+<subject_marker>`

**11**  this can; then the Lord would have heaven and earth quake
`this can then-exist want-Lord heaven earth quake`

> The torch figure carried through to the Nativity and the cross.

## 087v — the blind of God

**1**  […] the gospel written
`~exist-chapter gospel write`

**2**  by holy Matthew […]
`holy-Matthew [?]`

**3**  of his writing, who is
`<preposition_of_genitive>-write who-exist-to`

**4**  whosoever is an apostle, this from this
`?whosoever-apostle this from this`

**5**  […] the son […]
`[?] son [?]`

**6**  afterwards, in Jesus'
`?afterward inside <preposition_of_genitive>-Jézus`

**7**  name, one
`and-~exist-exist-from-+name one`

**8**  man is saved, one […] in heaven; in turn
`somebody +be_saved one [?] inside heaven | in_turn-chapter`

**9**  the day is not so; every man is damned, judged, the man, by Christ. Holy
`+day-exist ~a) each,_every somebody be_damned judge somebody Christ | holy`

**10**  Matthew speaks […] this man says, this […]
`Matthew speak [?] this somebody say this [?]`

**11**  the son, this […] the man trespasses, blind to God, and
`son this [?] somebody trespass blind God and`

**12**  blind to God is the man, and […] […] the man in turn, this
`blind God somebody and [?] [?] somebody in_turn this`

> A sermon on the man who is blind to God, leading into the rich man of the
> next folio.

## 088r — the rich man, and the soul in purgatory

**1**  the man is rich, he has wealth, he sees, blind
`somebody rich have-somebody wealth see blind`

**2**  he goes […] or sits, and […] asks of this
`go [?] or sit and [?] exist ask_(for) from this`

**3**  man alms, in Jesus' name […]
`somebody alms inside Jézus and-~exist-exist-from-+name [?]`

**4**  the blind, the high receives; the man is damned, the man, for
`blind high-grab somebody be_damned exist somebody chapter-oh`

**5**  ever […] […] judged and damned, the man
`chapter-oh [?] [?] from-judge be_damned somebody`

**6**  upon the blind; in turn damned, whosoever is damned, the man, for
`on-blind in_turn be_damned ?whosoever be_damned exist somebody chapter-oh`

**7**  ever […] saved; the man is damned, the man […]
`chapter-oh [?] +be_saved somebody be_damned exist somebody [?]`

**8**  whosoever, in the evil […] […] it is written, the man
`?whosoever inside ~evil [?] [?] write somebody`

**9**  in the evil until the death of the man […] in turn upon
`inside ~evil until to-die <preposition_of_genitive>-somebody and-[?]-from-+name in_turn | on`

**10**  death the soul is in purification […] until the day of judgment; in turn upon
`die soul inside purification [?] until judge-+day in_turn | on`

**11**  the day of judgment, and the soul, and for ever in the evil, for ever
`judge-+day and soul and exist-exist-chapter inside ~evil chapter-oh chapter-oh`

> Purgatory is named outright on line 10, which is a doctrine of the Latin
> church and not a gospel text.

## 088v — there was a certain rich man, clothed in purple

**1**  Here begins this holy gospel
`begins this holy-gospel`

**2**  written by holy Luke in
`write holy-Luke inside`

**3**  the sixth […] of his writing.
`six [?] <preposition_of_genitive>-write`

**4**  At that time Lord Jesus said
`time say Lord-Jézus`

**5**  to his apostles, and the Jewish
`apostle <preposition_of_genitive>-Lord and Jew(ish)`

**6**  people, there was a rich man,
`people-chapter exist-rich`

**7**  one rich man,
`one rich-somebody`

**8**  and the rich man, every […] and purple the rich man wore, and
`and somebody-rich each,_every [?] and purple go-somebody-rich | and`

**9**  the rich man from day to day made merry; and then […] came
`rich from +day until +day joy-rich and then-exist [?] go`

**10**  one Lazarus to the rich man's house; and Lazarus was all over
`one ~Lazarus to-house this-rich and ~Lazarus exist each,_every from`

**11**  […] until […] […] wounds, Lazarus; at that time this rich man
`[?] until [?] [?] wound ~Lazarus time this rich`

**12**  to […] the rich man sat, the man, the Lord […] the Lord king […]
`to [?] sit-rich somebody Lord [?] king-Lord [?]`

**13**  this and that, the Lord; and then the rich man, this poor man asked
`who-and-this-and Lord and then-exist rich exist this ?the_poor_man ask_(for)`

> Luke 16:19–20, *there was a certain rich man, which was clothed in purple
> and fine linen, and fared sumptuously every day: and there was a certain
> beggar named Lazarus, which was laid at his gate, full of sores.*

## 089r — the dogs licked his sores, and angels carried him

**1**  alms; and the poor man, alms […] the rich man […]
`alms and ?the_poor_man alms [?] rich [?]`

**2**  but the poor man he drove out; and then this poor man lay
`a) ?the_poor_man out(ward) chase and then-exist lie this`

**3**  outside the gate of the rich man, alone, because the poor man was […]
`?the_poor_man out(ward) ~gate to-<preposition_of_genitive>-rich exist-+one because exist ?the_poor_man [?]`

**4**  was […]; and then the poor man desired the crumbs that fell […]
`exist [?] and then-exist want ?the_poor_man trespass from crumbs [?]`

**5**  from the rich man's table […] the poor man […]; and then
`on-<preposition_of_genitive>-rich throne [?] ?the_poor_man [?] and then-exist | have`

**6**  the rich man had many dogs, and the dogs came, this […] and
`rich many dog and go-dog this [?] ~and`

**7**  the dogs licked Lazarus […] and Lazarus more
`lick-dog <preposition_of_genitive>-Lazarus [?] and Lazarus more`

**8**  was of the dogs […] mercy, this Lazarus; in turn from the rich man
`exist from dog [?] have_mercy this Lazarus in_turn from-rich`

**9**  mercy […] […] mercy; and then this Lazarus
`have_mercy [?] [?] have_mercy and then-exist this Lazarus`

**10**  died, went with angels to heaven, to glory, literally, from God the Father […] this Lazarus, and Lazarus
`die go angel heaven ?glory literal from-father God [?] this Lazarus and Lazarus`

**11**  the angels took, and carried Lazarus into the bosom of Abraham
`grab-angel and Lazarus carry inside öl Abraham`

**12**  the forefather. And then this rich man saw this miracle, of this Lazarus
`forefather and then-exist see this miracle this rich from this Lazarus`

> Luke 16:21–22, *the dogs came and licked his sores... the beggar died, and
> was carried by the angels into Abraham's bosom.* The word for bosom is
> Kiraly and Tokai's own Hungarian gloss, *öl*, left as they give it.

## 089v — in hell he lifted up his eyes

**1**  […] Lazarus did, the angels, the Father, heaven; and then this
`[?] do, Lazarus angel father heaven and then-exist this`

**2**  rich man died, and this rich man […] in the evil was buried; and then
`rich die and this-~rich [?] inside ~evil bury and then-exist`

**3**  he suffered in the evil, this rich man; he looked up and saw Lazarus
`suffer inside ~evil this ~rich see ~trespass-~rich and see Lazarus`

**4**  in the bosom of father Abraham, and this rich man cried
`inside öl father Abraham and shout this rich`

**5**  father Abraham, said the father, Lazarus, because this […] the poor man, of
`father Abraham say-father Lazarus because-this from-understand ?the_poor_man | <preposition_of_genitive>`

**6**  Lazarus, a little […] dip in water, and cool it
`Lazarus little [?] immerge water and cool`

**7**  on the rich man's tongue […] […] the soul of the rich man; and from
`on-<preposition_of_genitive>-rich tongue [?] [?] soul <preposition_of_genitive>-rich and from`

**8**  […] for ever, of the rich man. And then father Abraham: this
`[?] exist-exist-chapter <preposition_of_genitive>-rich +and_then father Abraham | this`

**9**  rich man, son of the Father, this rich man had good things […] he is
`~rich son <preposition_of_genitive>-father-<suffix_of_divine_name> this-~rich good [?] ?he_is`

**10**  Lazarus was […] […] the people; in turn this rich man was
`Lazarus exist [?] [?] ?people in_turn this-~rich exist`

**11**  rich […] […] this rich man, Lazarus took the crumbs that fell
`rich [?] [?] this-~rich grab-Lazarus trespass from crumbs`

**12**  […] the rich man's table; the rich man took […] the rich man, Lazarus […]
`[?] [?]-~rich throne ~rich grab [?] ~rich Lazarus [?]`

> Luke 16:23–25, *in hell he lift up his eyes... send Lazarus, that he may
> dip the tip of his finger in water, and cool my tongue... Son, remember
> that thou in thy lifetime receivedst thy good things.*

## 090r — a great gulf fixed, and they have Moses and the prophets

**1**  said father Abraham, take Lazarus […] […] the people. And then
`say father Abraham grab-Lazarus [?] [?] ?people +and_then`

**2**  father Abraham: a great chasm between the rich man […] or […]
`father Abraham many chasm among-~rich-[?] or [?]`

**3**  this is the netherworld, most high, evil upon evil; who cries, this […]
`+this_is netherworld most_high ~evil on-~evil who-shout this-[?]`

**4**  father Abraham; and Lazarus […] in the bosom of father
`father Abraham and Lazarus [?] inside öl father`

**5**  Abraham; and a second time this rich man cried, father Abraham,
`Abraham and two who-shout this-~rich father-<suffix_of_divine_name> Abraham`

**6**  send Lazarus […] […] […] the rich man has, the trespass, these two, of the rich man
`go Lazarus [?] [?] [?] have-~rich trespass this-two-two <preposition_of_genitive>-rich`

**7**  brethren, because the brethren […] of the rich man, how in this rich man's suffering
`~exist-exist because ~exist-exist [?] from-~rich how? inside this-rich suffer`

**8**  because these brethren, the man sins, from […] then is damned
`because this ~exist-exist somebody sin from [?] then-exist be_damned`

**9**  the man, as the rich man, this rich man is damned. Said father Abraham, they have
`somebody how?-rich this-rich be_damned say father-<suffix_of_divine_name> Abraham have`

**10**  the brethren, the trespass, this prophet, and preaching, because this prophet preaches
`exist-exist trespass this prophet and preach because this prophet preach`

**11**  evil; the man, the brethren […] and a third time he cried, this
`evil somebody brother [?] and +three who-shout this`

> Luke 16:26–29, *between us and you there is a great gulf fixed... I have
> five brethren... they have Moses and the prophets.* The codex counts the
> rich man's three cries with its own ordinals, second on line 5 and third on
> line 11.

## 090v — neither will they be persuaded, though one rose from the dead

**1**  the rich man; father Abraham […] the prophet preaches, believe […]
`rich father-<suffix_of_divine_name> Abraham [?] prophet preach believe [?]`

**2**  […] good, the man Lazarus, believing
`[?] good somebody-Lazarus believe-exist-exist`

**3**  and the body rose from the dead, the poor man. Said father Abraham, in turn who […]
`and body from die stand_up-somebody-?the_poor_man say father-<suffix_of_divine_name> Abraham in_turn-who [?]`

**4**  the brethren, the prophet, let the brethren believe, and the preaching
`brother prophet believe-brother-somebody and preach`

**5**  and good, from the man […] […] the brethren believe; and the body
`and good from somebody-+the_Baptist-[?] [?] exist-exist believe and body`

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

**12**  […] to the Lord he came
`[?] to-Lord go-this`

> Luke 16:31, *neither will they be persuaded, though one rose from the
> dead*, which the codex reads back onto Lazarus. Then Nicodemus. **The
> citation on line 8 says John chapter two and the passage is John 3; it is
> the one miss in the citation test.**

## 091r — except a man be born again

**1**  but by night to the Lord came Nicodemus. And then Nicodemus: O.
`a) inside night to-Lord go-Nicodemus +and_then Nicodemus oh.`

**2**  Nicodemus answered, this Nicodemus, this Lord Nicodemus believes.
`<preposition_of_genitive>-Nicodemus +answered this-Nicodemus this-Lord believe-Nicodemus.`

**3**  […] this Lord is truly the Son of the living God, because this Lord goes to heaven.
`[?] this-Lord righteous(ly) son living God because this-Lord go on-heaven.`

**4**  In turn […] and the Lord, this Lord truly the Son of the living God. And then
`in_turn-[?] and-Lord this-Lord righteous(ly) son living God +and_then.`

**5**  Lord Jesus, Nicodemus […] […] this Lord to you
`Lord-Jézus Nicodemus [?] [?] this-Lord you.`

**6**  speaks: and the man […] who believes in the Lord […] a second time
`speak and somebody [?] exist to-Lord believe [?] two.`

**7**  is born into this world, that one man is saved; but every man
`be_born on-this ?world one somebody be_saved a) each,_every-somebody`

**8**  is damned. Said Nicodemus, answering, how can this be, who a second time
`be_damned say Nicodemus +answered how?-this can exist who to-two-before`

**9**  a second time from his mother goes, Nicodemus, and a second time is born into this world?
`two from <preposition_of_genitive> mother go-Nicodemus and two be_born-Nicodemus on-this ?world.`

**10**  For this, thanks. Said Lord Jesus, Nicodemus […] this Lord, this
`this thanks say Lord-Jézus Nicodemus [?] this-Lord this-donkey-to`

> John 3:3–4, *except a man be born again, he cannot see the kingdom of God.
> How can a man be born when he is old? can he enter the second time into his
> mother's womb, and be born?*

## 091v — born of water and of the Spirit, and God so loved the world

**1**  this host, this Nicodemus, a second time born of his mother; but
`this host this-Nicodemus two be_born from <preposition_of_genitive>-Nicodemus mother a)`

**2**  this Lord speaks: then, born a second time, the man Nicodemus, of water and
`this-Lord speak then two be_born-somebody-Nicodemus from water and`

**3**  of the Holy Spirit, that one man Nicodemus is saved; but
`from holy-spirit one somebody-Nicodemus be_saved a)`

**4**  every man Nicodemus is damned. Said Lord Jesus, Nicodemus, in turn then
`each,_every-somebody-Nicodemus be_damned say Lord-Jézus Nicodemus in_turn | then`

**5**  this Lord to you began, the Lord, to preach of heaven
`exist this-Lord you begin-Lord preach from-heaven`

**6**  and earth, how you from […] left, Nicodemus
`land how? you from [?] | leave-Nicodemus`

**7**  the man; then can this world, Nicodemus, the man […]
`somebody then-exist this ?world can Nicodemus-somebody [?]`

**8**  he left, the brethren; this Lord to you preached, said the Lord
`leave-to-leave ?brethren this-Lord you preach-Lord say | Lord`

**9**  Jesus, Nicodemus: so did you love the Father, his God of heaven
`Jézus Nicodemus [?]-+one you love father <preposition_of_genitive>-Lord God heaven`

**10**  but the Father's only begotten Son, Jesus, that is, to the Lord, so
`a) <preposition_of_genitive>-father-<suffix_of_divine_name> only_one son Jézus that_is to-Lord [?]-+one`

**11**  did you love the Father, said Lord Jesus; and […] and the man, the Lord
`you love father-<suffix_of_divine_name> say Lord-Jézus and [?] and somebody Lord`

> John 3:5, *except a man be born of water and of the Spirit*, then John
> 3:16, *God so loved the world, that he gave his only begotten Son*, which
> line 10 gives with the word *only begotten* intact.

## 092r — that whosoever believeth should not perish

**1**  believes in the Son of the Father, the only begotten, Lord Jesus Christ, and one
`believe son <preposition_of_genitive>-father-<suffix_of_divine_name> only_one Lord-Jézus-Christ and one`

**2**  man Nicodemus is saved; but every man Nicodemus is damned. Said
`somebody-Nicodemus be_saved a) each,_every-somebody-Nicodemus be_damned say`

**3**  Lord Jesus, Nicodemus […] to the Lord goes the Father, his God of heaven;
`Lord-Jézus Nicodemus [?] to-Lord go father <preposition_of_genitive>-Lord God heaven`

**4**  he loved this Lord; this people he judges, but rather to the Lord goes the Father, the brethren, this Lord
`love this-Lord this ?people judge ?but_rather to-Lord go father-<suffix_of_divine_name> ?brethren this-Lord`

**5**  saved this world by his death; and […] is, to the Lord
`this ?world be_saved on-<preposition_of_genitive>-Lord die and [?] exist to-Lord`

**6**  believes, this man Nicodemus, and his Father
`believe this somebody-Nicodemus exist and <preposition_of_genitive>-Lord father-<suffix_of_divine_name>`

**7**  believes more than these; this one, one God. Said Lord Jesus […]
`believe ?more_than_these this +one one God say Lord-Jézus [?]`

**8**  one […] among you […] from
`one ~exist-[?] among you [?] from`

**9**  the dog and […] […] […] not; and said
`dog and [?] [?] [?] not and say`

**10**  Lord Jesus, and the man Nicodemus who does evil among you
`Lord-Jézus and +<subject_marker> do_evil-somebody-Nicodemus among you`

> John 3:16–18, *that whosoever believeth in him should not perish... he that
> believeth not is condemned already.*

## 092v — men loved darkness rather than light

**1**  from the man Nicodemus who will not come to the light, but loves the darkness,
`from somebody-Nicodemus not_want on-light go a) darkness love`

**2**  the man Nicodemus; said Lord Jesus, and the true man Nicodemus, from
`somebody-Nicodemus say Lord-Jézus and +<subject_marker> righteous(ly)-somebody-Nicodemus from`

**3**  the man Nicodemus, the light, the man Nicodemus loves, and all come to the light
`somebody-Nicodemus light love-somebody-Nicodemus and each,_every on-light | go`

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

**11**  people: then
`people-chapter | then-exist`

**12**  a rich lord made, one rich man, many […]
`rich-Lord-<suffix_of_divine_name> do, one rich somebody many [?]`

> John 3:19–21, *men loved darkness rather than light.* Then the citation on
> line 7 says **Luke chapter fourteen**, and what follows is the Great
> Supper, Luke 14:16. That citation checks out.

## 093r — a certain man made a great supper, and bade many

**1**  And then the rich lord, among the rich lord's, the redeemer's day, three […]
`and then-exist-rich-Lord-<suffix_of_divine_name> among-rich-Lord-<suffix_of_divine_name> redeemer-+day +three [?].`

**2**  upon this […] said this rich lord to his living servant, go […]
`on-this [?] say this-rich-Lord-<suffix_of_divine_name> <preposition_of_genitive>-Lord living-servant go-[?].`

**3**  speak this word, go, the man; at that time all is finished, say.
`this word speak-angel go-somebody time +<subject_marker> each,_every finished say.`

**4**  This living servant, this […] […] lo, the living servant.
`this-living-servant this [?] [?] lo living-servant.`

**5**  Go to the rich lord's living man […] then the lord […]
`go <preposition_of_genitive>-living-somebody-Lord-<suffix_of_divine_name> [?] then-chapter-Lord-<suffix_of_divine_name> [?]`

**6**  of the lord […] said this first: not.
`<preposition_of_genitive>-Lord-<suffix_of_divine_name> [?] say this first [?] not.`

**7**  […] because […] a piece of ploughland; I must
`[?] because [?] plough_land | want`

**8**  […] go and see it, and I must, the ploughland […]
`[?] +<subject_marker> [?] see and want plough_land [?].`

**9**  he asks […] to speak […] he is to
`ask_(for) [?] to-speak [?] exist-to`

**10**  […] the lord; and said this second, lo.
`[?] Lord-<suffix_of_divine_name> and say this two sense lo.`

**11**  The living servant goes, the lord's living servant, this man
`living-servant go <preposition_of_genitive>-living-servant Lord-<suffix_of_divine_name> this-somebody-sense`

> Luke 14:16–19, *a certain man made a great supper, and bade many... and
> they all with one consent began to make excuse. The first said unto him, I
> have bought a piece of ground, and I must needs go and see it.* The codex
> counts the excuses first, second, as the gospel does.

## 093v — I have bought five yoke of oxen

**1**  then the lord; the man goes, of the lord […] said this
`then-chapter-Lord-<suffix_of_divine_name> go-somebody-sense <preposition_of_genitive>-Lord-<suffix_of_divine_name> [?] say this`

**2**  second man, this man cannot
`two somebody-sense this-somebody-sense not`

**3**  the man cannot, because the man has bought
`can-somebody-sense because buy-somebody-sense`

**4**  five yoke of oxen […] the man must
`+five yoke sense [?] want-somebody-sense`

**5**  the man goes […] the man must
`go-somebody-sense [?] want-somebody-sense`

**6**  […] thanks; he can […] […]
`+<subject_marker> [?] thanks exist can [?] | [?]`

**7**  […] […] believe; this living servant, to speak
`[?] [?] +believe this-living-~servant to-speak`

**8**  the man, before […] the lord said
`somebody-sense before [?] Lord-<suffix_of_divine_name> say`

**9**  this third man, lo, the living servant goes, the lord's living servant
`this +three somebody-thief lo living-servant go <preposition_of_genitive>-living-servant`

**10**  the lord; this third man, then the lord, the man goes
`Lord-<suffix_of_divine_name> this-somebody-thief then-chapter-Lord-<suffix_of_divine_name> go-somebody-thief`

**11**  of the lord […] said this third, this man
`<preposition_of_genitive>-Lord-<suffix_of_divine_name> [?] say this +three thief this-somebody-thief`

> Luke 14:19, *I have bought five yoke of oxen, and I go to prove them.* The
> codex counts the three excuse-makers with its own ordinals.

## 094r — go out into the highways and hedges

**1**  the man cannot, and the man must go
`not can-somebody-thief and to-go-somebody-thief`

**2**  because the man must go, he has married; this man cannot
`because to-go-somebody-thief marry this-somebody-thief not`

**3**  the man cannot, and the man must go, and this and that
`can somebody-thief and to-go-somebody-thief and this-and-this`

**4**  the man […] said, to speak, the man is to
`somebody-thief [?] say to-speak somebody-thief exist-to`

**5**  of […] the lord; and then, and one goes, the man
`<preposition_of_genitive>-[?] Lord-<suffix_of_divine_name> and then-exist and one | go-somebody`

**6**  […] upon this, to the supper, said this
`[?] on-this to-dinner-to say this`

**7**  lord, that is, the people; and the people spoke of the lord […]
`Lord-<suffix_of_divine_name> that_is people-chapter and people-chapter from-speak <preposition_of_genitive>-Lord-<suffix_of_divine_name> [?]`

**8**  and the lord said to the living servant, go out into the roadside and the way
`and say <preposition_of_genitive>-Lord-<suffix_of_divine_name> living-servant go on-(on_the)_roadside and on-way`

**9**  and into the town, and to the town gate, and.
`and on-town and on-gate town and.`

**10**  […] within, the one-eyed, the blind, to be
`[?] inside only_one-+day-~exist blind-eye | to-exist-chapter`

**11**  […] the body hungry, and […] within the one-eyed, and […]
`[?] body be_hungry and [?] inside only_one-+day-~exist and [?].`

> Luke 14:21–23, *go out quickly into the streets and lanes of the city, and
> bring in hither the poor, and the maimed, and the halt, and the blind...
> go out into the highways and hedges.*

## 094v — blessed is he that shall eat bread in the kingdom of God

**1**  […] he found; every man went, the angel, into the lord's house
`[?] find each,_every somebody go-angel inside <preposition_of_genitive>-Lord-<suffix_of_divine_name> house`

**2**  said this living servant, the angel, Lord, it is done; and the mountain top, which the Lord
`say this living-servant-angel Lord do, and mountain_peak who-Lord`

**3**  said […] said this living servant, the angel […]
`say [?] say this living-servant-angel [?]`

**4**  one to the place, and to the place the living servant would go out
`one to-place and to-place want living-servant-angel on-out(ward)`

**5**  and then there rose at the table one Jew, and
`and then-exist +rise to-throne one Jew(ish) and`

**6**  cried out: blessed is he, from within the one-eyed, the blind, because
`shout-to happy from inside only_one-+day-~exist blind-eye because`

**7**  the one-eyed, of the blind, heaven and earth; and said Lord
`only_one-+day-~exist <preposition_of_genitive>-blind-eye heaven land and say | Lord`

**8**  Jesus truly, speaking to the Jew, more than these, within the one-eyed, heaven
`Jézus righteous(ly) speak-Jew(ish) ?more_than_these inside only_one-+day-~exist heaven`

**9**  and earth. And then this rich man, the lord […] […]
`land +and_then this-rich somebody-Lord-<suffix_of_divine_name> [?] [?]`

**10**  many, to go, the mouth […]
`many to-go-mouth | [?]`

**11**  the thief upon the rich lord's […] Here ends this holy gospel.
`thief on-<preposition_of_genitive>-somebody-rich-Lord-<suffix_of_divine_name> [?] end this holy-gospel`

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

**6**  people: ye
`people-chapter you`

**7**  shall eat of his, for ever,
`exist <preposition_of_genitive>-Lord exist-exist-chapter`

**8**  and of his shall ye
`eat and <preposition_of_genitive>-Lord to-to-this`

**9**  drink. And then Lord Jesus, with his apostles, at the last supper, this
`drink +and_then Lord-Jézus apostle <preposition_of_genitive>-Lord last dinner-to this`

**10**  at the last supper; and Lord Jesus took, in turn, one baked
`on-last dinner and grab Lord-Jézus inside why?-in_turn one baked`

**11**  cake, and Lord Jesus blessed this bread
`„cake” and +blessed Lord-Jézus this +bread.`

**12**  and […] before the Lord, Lord Jesus put it. And
`and [?] before Lord put Lord-Jézus and.`

> **John chapter six is what the page says, and John 6 is the Bread of Life.
> That citation checks out.** The word for the loaf is Kiraly and Tokai's
> own, left in their quotation marks.

## 095v — except ye eat my flesh and drink my blood

**1**  Lord Jesus took wine, one cup, and water into the cup
`grab Lord-Jézus wine one cup and water inside cup`

**2**  poured, and Lord Jesus blessed the wine and the water; and
`pour and +blessed Lord-Jézus wine and water and`

**3**  the wine and water before the Lord, Lord Jesus put. And then Lord
`wine water before Lord put Lord-Jézus +and_then | Lord`

**4**  Jesus: and the man who eats this bread, this man
`Jézus and somebody exist this +bread eat this somebody`

**5**  is called his own […] and the man […]
`exist <preposition_of_genitive>-Lord ?shall_be_called [?] and somebody [?]`

**6**  who eats this bread […] believes in the Lord
`this +bread eat [?] Lord believe`

**7**  every man is damned […] and the man who believes in the Lord
`each,_every somebody be_damned cut_off-[?] and somebody exist Lord believe`

**8**  […] from the altar, from the thirty, the holy host
`[?] from altar(table) exist from thirty holy-host`

**9**  eats […] […] every man shall be
`eat [?] [?] each,_every somebody exist`

**10**  living, for ever, amen. And then the Jews:
`living chapter-oh chapter-oh amen +and_then Jew(ish)`

**11**  how can this be, his own, to be eaten, and his
`how? exist-+say <preposition_of_genitive>-Lord ?shall_be_called eat and <preposition_of_genitive>-Lord`

> John 6:52–54, *how can this man give us his flesh to eat?... except ye eat
> the flesh of the Son of man, and drink his blood, ye have no life in you.*
> The wine mixed with water on line 1 is the liturgy, not the gospel.

## 096r — whoso eateth my flesh hath eternal life

**1**  drink of this? This pleasing, which this Lord speaks, because food
`to-to-this drink this pleasing who this-Lord speak because food`

**2**  the Jews, who […] […] and his body to eat
`Jew(ish) who-[?] [?] and <preposition_of_genitive>-Lord body eat`

**3**  and to drink of it; which is hidden, said this Lord Jesus, who is the Lord
`and to-to-this drink which-hide_oneself say this Lord-Jézus who-Lord-exist`

**4**  […] but said Lord Jesus, believe; then
`[?] a) say Lord-Jézus to-believe then-exist`

**5**  the man believes in the Lord, to the Lord, he who is truly the Son
`believe-somebody inside Lord to-Lord this-?he_who righteous(ly) son`

**6**  of the living God. And then Lord Jesus: his own, this is
`living God +and_then Lord-Jézus <preposition_of_genitive>-Lord ?shall_be_called +this_is`

**7**  truly to eat, and of his, this is truly to drink
`righteous(ly) eat and <preposition_of_genitive>-Lord to-to-this +this_is righteous(ly) drink`

**8**  And then Lord Jesus: then the man who eats this bread
`+and_then Lord-Jézus then-exist somebody this +bread eat`

**9**  is a man, an apostle […] upon his, never […]
`exist somebody apostle [?] on-<preposition_of_genitive>-Lord not-not [?]`

**10**  is from eating, how the bread of […]
`exist from eat how? +bread <preposition_of_genitive>-[?]`

> John 6:55, *my flesh is meat indeed, and my blood is drink indeed*, which
> line 7 gives in both halves.

## 096v — I am the living bread which came down from heaven

**1**  your fathers did eat in […] because that is the bread
`you father eat inside [?] because that_is +bread`

**2**  of life; he who goes, the Lord, the Lord's bread; in turn he left the eternal town
`living +he_who go-Lord +bread-Lord in_turn leave ?from_the_eternal | town`

**3**  from that day, upon this world; and the man who eats this bread
`from-+day on-this ?world and somebody exist this +bread eat`

**4**  from him, the man shall live for ever, amen
`from somebody exist living chapter-oh chapter-oh amen`

**5**  and this Lord, this […] because the Lord, this Lord goes
`and this-Lord this [?] because-Lord this-Lord | go`

**6**  the Lord from his Father, upon this world; and this Lord
`Lord from <preposition_of_genitive>-Lord from-father-<suffix_of_divine_name> on-this ?world and this-Lord`

**7**  to his Father, the living Lord; and the man who in the Lord
`to-<preposition_of_genitive>-Lord from-father living-Lord and somebody exist Lord.`

**8**  believes, from him the man lives to the Lord, for
`believe from somebody exist to-Lord living chapter-oh`

**9**  ever […] and the man who is
`chapter-oh [?] and somebody exist`

**10**  within the Lord's law of love, carried by the Lord, stays; and this Lord is
`inside Lord-+law-love-~carry-Lord stay and this-Lord exist`

> John 6:49–51, *your fathers did eat manna in the wilderness, and are dead.
> This is the bread which cometh down from heaven... I am the living bread.*

## 097r — he that dwelleth in me, and I in him

**1**  within […] and the man who carries his commandment, from the man
`inside [?] and somebody exist <preposition_of_genitive>-Lord commandment carry from somebody`

**2**  who is in the Lord, from the Lord's law of love, carried by the Lord, stays; and this Lord is
`exist inside Lord from Lord-+law-love-~carry-Lord stay and this-Lord exist`

**3**  within […] And then Lord Jesus […] the man, and the man who is
`inside [?] +and_then Lord-Jézus [?] somebody and somebody exist`

**4**  within the Lord, the Father, the Son, God, Jesus, the Holy Spirit, Mary, Christ, the apostles, the angels
`inside Lord-father-<suffix_of_divine_name>-son-God-Jézus-holy-spirit-Mary-Christ-apostle-angel`

**5**  […] stays; the Lord, the Father, the Son, God would have
`[?]-stay | want-Lord-father-<suffix_of_divine_name>-son-God`

**6**  Jesus, the Holy Spirit, Mary, Christ, the apostles, the angels go; and the man
`Jézus-holy-spirit-Mary-Christ-apostle-angel go and somebody`

**7**  goes, the Lord, the Father, the Son, God, Jesus, the Holy Spirit, Mary, Christ, the apostles, the angels
`go-Lord-father-<suffix_of_divine_name>-son-God-Jézus-holy-spirit-Mary-Christ-apostle-angel`

**8**  into the heavenly land. And then Lord Jesus, and this man
`inside heavenly land +and_then Lord-Jézus and this somebody`

**9**  would have the Lord, the Father, the Son, God, Jesus, the Holy Spirit, Mary, Christ, the apostles, the angels
`want-Lord-father-<suffix_of_divine_name>-son-God-Jézus-holy-spirit-Mary-Christ-apostle-angel`

**10**  take his house, at the Lord's, the Father's, the Son's, God's, Jesus', the Holy Spirit's
`house grab at | <preposition_of_genitive>-Lord-father-<suffix_of_divine_name>-son-God-Jézus-holy-spirit`

> John 6:56, *he that eateth my flesh, and drinketh my blood, dwelleth in me,
> and I in him.* The long chains on lines 4, 7 and 9 are one sign written as
> a single compound naming the whole of heaven at once, which is how the
> codex does a litany.

## 097v — the whole company of heaven, and the host

**1**  Mary, Christ, the apostles, the angels; from God the Father, hidden, through staying
`Mary-Christ-apostle-angel from-father-God to-hide_oneself-exist through stay`

**2**  the man, for ever, amen. And then Lord Jesus, and
`somebody chapter-oh chapter-oh amen +and_then Lord-Jézus and`

**3**  the man who from the altar, from the thirty, the holy host
`somebody exist from altar(table) from thirty holy-host`

**4**  eats […] from him the man lives, for
`eat [?] from somebody exist living-somebody chapter-oh`

**5**  ever, amen. Here ends this holy gospel. The Lord, with all thy heart.
`chapter-oh amen end this holy-gospel Lord-?with_all_thy_heart`

**6**  Here begins this holy gospel
`begins this holy-gospel`

**7**  written by holy Luke, in
`write holy-Luke inside`

**8**  the […] chapter of his writing.
`and chapter <preposition_of_genitive>-write`

**9**  Then Lord Jesus, in
`then-exist Lord-Jézus inside`

**10**  the thirtieth day and in the first
`thirty +day and inside +one`

**11**  year; at that time he left
`year time leave-to-leave`

> The altar, the thirty and the holy host on line 3 are the mass, not the
> gospel.

## 098r — the light of the body is the eye

**1**  Lord Jesus […] among the chief of the Jews, and his apostles
`Lord-Jézus [?] among Jew(ish) head and <preposition_of_genitive>-Lord apostle`

**2**  And then Lord Jesus, to his apostles and the Jewish people […]
`+and_then Lord-Jézus apostle <preposition_of_genitive>-Lord and Jew(ish) people-+day [?]`

**3**  have mercy […] the eye […] […] of the apostles
`have_mercy-+<subject_marker> <preposition_of_genitive>-[?] eye-from [?] [?] | <preposition_of_genitive>-apostle`

**4**  the man said, the eye. And then Lord Jesus, the eye of […]
`+say-somebody eye-from +and_then Lord-Jézus eye-from | <preposition_of_genitive>-[?]`

**5**  the man, this is the lamp of […] and the lamp of the apostles
`somebody +this_is lamp <preposition_of_genitive>-[?] and lamp | <preposition_of_genitive>-apostle`

**6**  the man said, this is for ever, of […] and
`+say-somebody +this_is exist-exist-chapter <preposition_of_genitive>-[?] and`

**7**  in turn, it is within […] for ever […] one
`in_turn exist inside <preposition_of_genitive>-[?] exist-exist-chapter [?] one`

**8**  the heart, sin protruding, is all of […] for ever
`heart +sin protrude exist each,_every <preposition_of_genitive>-[?] exist-exist-chapter`

**9**  darkness. And then Lord Jesus, in turn who […] […]
`darkness +and_then Lord-Jézus in_turn-who [?] [?]`

**10**  sins against the Lord, from God the Father, from the heart; he would, from the Father
`sin against <preposition_of_genitive>-Lord from-father God from heart want from-father`

> Luke 11:34, *the light of the body is the eye: therefore when thine eye is
> single, thy whole body also is full of light; but when thine eye is evil,
> thy body also is full of darkness.*

## 098v — a candle set on a candlestick

**1**  his scourges, various, of the ass. And then Lord Jesus, this hidden
`<preposition_of_genitive>-Lord whip-whip various from-donkey +and_then Lord-Jézus this-hide_oneself`

**2**  is within […] for ever; every […] is clean
`exist inside <preposition_of_genitive>-[?] exist-exist-chapter each,_every [?] clean exist`

**3**  all of […] for ever, light. And then Lord Jesus,
`each,_every <preposition_of_genitive>-[?] exist-exist-chapter light +and_then Lord-Jézus`

**4**  how then […] the lamp gives light, to
`how? then-exist [?]-[?] lamp light to-+<subject_marker>`

**5**  the light; the lamp, a hundred, gives light, of […] for ever.
`light lamp hundred exist light <preposition_of_genitive>-[?] exist-exist-chapter`

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

**12**  man upon this world, and healing
`somebody on-this ?world and healing`

> Luke 11:33, *no man, when he hath lighted a candle, putteth it in a secret
> place... but on a candlestick, that they which come in may see the light.*

## 099r — he that dwelleth in love dwelleth in God

**1**  the man receives, and God receives the man […] the man, God. To
`somebody grab and God somebody grab [?] somebody God | to`

**2**  this the man has: the Lord God, Jesus Christ, the Son of God;
`this have somebody Lord-<divine> Jézus Christ son <of>-God`

**3**  and the Lord, the Lord's head, heaven and earth;
`and Lord ~head-Lord +heaven and earth`

**4**  and love his brother as thy neighbour.
`and love <of>-somebody father son how?-to somebody +neighbour`

**5**  In turn […] the holy man; the man has wealth, he sees;
`in_turn [?] ~rich somebody have somebody wealth see`

**6**  trespass; the unseen God; and the man […] has God, the man
`trespass blind God and somebody [?] have God somebody`

**7**  loves the holy man as thy neighbour. Of
`+<subj> love-rich-somebody how?-to somebody +neighbour exist | <of>`

**8**  whosoever is holy, one, the kingdom of heaven, speaks holy Matthew; and
`?whosoever-rich-+one heaven land speak holy-~Matthew and`

**9**  the man […] says: this man loves God. In turn, of the holy
`somebody [?] say this-somebody God love in_turn | <of>-rich.`

**10**  man, his brother […] loves the holy man, from […]
`somebody father son [?] love-rich-somebody from [?]`

> 1 John 4:15-21: "Whosoever shall confess that Jesus is the Son of God, God
> dwelleth in him ... he that loveth not his brother whom he hath seen, how
> can he love God whom he hath not seen? ... he who loveth God love his
> brother also." *Father son* is the book's word for brother, "my father's
> son", by Király & Tokai's own entry, which cites lines 4 and 10 here.

## 099v — if a man say, I love God, and hateth his brother, he is a liar

> Corrected 2026-09-20: lines 2, 3 and 6 first read "the father, the son".
> Király & Tokai's entry for *son* says the pair *father son* is the book's
> word for brother, "my father's son", and cites these very lines. So
> 1 John 4:20-21 stands here word for word: he that loveth God love his
> brother also.

**1**  he is a liar; how does this man love God, in turn, of
`one liar exist how? this somebody God love in_turn | <preposition_of_genitive>`

**2**  his brother […] loves God […] the Most High, this he sees.
`somebody father son [?] love God [?] high-this see.`

**3**  the man, in turn, his brother he sees; whosoever […]
`somebody in_turn <preposition_of_genitive>-somebody father son see ?whosoever [?]`

**4**  the son […] the man loves; how does this man love God, this
`son [?] love-somebody how? this-somebody God love this`

**5**  pleasing; in turn the rich man would love God; first love, of the rich
`pleasing in_turn want-rich-somebody God love first love | <preposition_of_genitive>-rich`

**6**  man, his brother, as the holy man, the holy man's neighbour, God
`somebody father son how?-to rich-somebody rich-+neighbour God`

**7**  and good; the rich man is loved […] […] the eternal
`and good exist somebody-~rich love [?]-[?] ?eternal`

**8**  land, the evil […] the rich man sees, saved
`land ~evil [?] see-rich-somebody | +be_saved`

**9**  the rich man is, for ever, amen.
`rich-somebody exist chapter-oh chapter-oh amen.`

**10**  In turn who is the rich man; the Lord, the apostles, love every man as the rich man
`in_turn-who-exist rich-somebody Lord apostle love each,_every somebody how?-to rich-somebody`

> **1 John 4:20**, *if a man say, I love God, and hateth his brother, he is a
> liar: for he that loveth not his brother whom he hath seen, how can he love
> God whom he hath not seen?* Lines 1–4 have both halves of it, and the
> answer on line 6 is the great commandment again.

## 100r — Elijah taken up by fire, and the list of miracles

**1**  the neighbour is of the holy man; the eternal kingdom […]
`+neighbour exist <of>-rich-somebody ?eternal land [?]`

**2**  the holy man, from […] the Lord, from the Father and the Son and the Holy Spirit.
`rich somebody from [?] Lord from father-<divine> and son and holy-spirit`

**3**  Elijah the prophet was taken,
`+Elijah prophet grab`

**4**  by fire, into heaven.
`fire on-+heaven`

**5**  Various miracles:
`various miracle`

**6**  afterward the blind eyes,
`?afterward blind eye`

**7**  through light [saw]; the dead
`+<subj> through light die +<subj>`

**8**  were raised up; the lame [walked];
`?raised_up +lame`

**9**  the body, and the possessed of the evil one, were healed. Elijah? Who? and this,
`body and evil obsessed_by_the_evil +<subj> from-healing +Elijah | who-and-this`

**10**  and this miracle: did Elijah do it? writes the church father, the scholar […]
`and-this miracle do, +Elijah write church_father scholar [?]`

**11**  First writes the scholar […]; the church father […] Elijah.
`first write scholar [?] church_father [?] +Elijah`

> 2 Kings 2:11 on lines 3-4, then the Matthew 11:5 list: the blind receive
> their sight, the dead are raised up, the lame walk, the sick are healed.
> The sign read Elijah here was read *Enoch* until today; it is Király &
> Tokai's own Elijah with one glyph swapped, and the Horeb pages at 133r
> settle it. *Lame* and *raised up* stand where their apparatus cites their
> own lame and resurrect signs on these lines. Lines 9-11 are a scholastic
> question, whether Elijah did these, answered from the fathers.

## 100v — the fathers on the sepulchre, a chronology, and the temple of forty-six years

**1**  the sepulchre; to heaven; on earth; on that, writes […]
`burial_chamber to-+heaven on-earth on-that_is write [?]`

**2**  […] the church father, on that, writes: the Most High hid himself, and from […] the scholar.
`[?] church_father on-that_is write high-hide_oneself-and-from scholar.`

**3**  […] the church father, on that, writes the scholar […] the Pharisees.
`[?] church_father on-that_is write scholar [?] ?Pharisees`

**4**  And the church father writes this three; and Saint Augustine the church father: Elijah
`and church_father this +three write and +Saint_Augustine_the_church_father +Elijah`

**5**  the Lord God [heart-Lord] first, but rather [heart-Lord] the sun and the moon,
`Lord-<divine> +heart-Lord first +but_rather +heart-Lord sun and moon`

**6**  and there is living Elijah; to Elijah, two; then, from
`and exist living +Elijah to +Elijah two then-exist from`

**7**  Adam [heart-Lord] fifty; and on this man […] seven
`+Adam +heart-Lord +fifty and on-this somebody [?] +seven`

**8**  people. Then is this man five hundred and
`people-chapter time exist this somebody +five_hundred and`

**9**  thirty. In the thirtieth year, then: "destroy", the Lord; five
`thirty thirty-+day time destroy Lord-<divine> +five`

**10**  towns; and then on this: "destroy", forty years and six years.
`town and then-exist on-this destroy two-two-ten-year and six-year`

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

**4**  And Elijah, the man, from […] […] […] and
`and +Elijah-somebody from-leave-to-leave [?] [?] and`

**5**  Elijah, the man, was taken up into heaven […] and […]. Elijah,
`+Elijah-somebody get_raptured heaven [?] and [?] | +Elijah`

**6**  the man […] from the day; Noah and Elijah shall bear the sword;
`somebody [?] from-+day Noah +Elijah +sword carry`

**7**  the evil one […] and […] […] Noah and Elijah on the earth.
`~evil [?] and [?] leave-to-leave Noah +Elijah on-earth`

**8**  […] […] shall be born; two; the chief evil, the evil one,
`[?] [?] through be_born two ~head-evil ~evil`

**9**  and the son of the devil; and there is […] evil, who is Antichrist.
`and son hide_oneself-angel and exist-[?] evil exist Antichrist`

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

**1**  Before the gospel, says
`before gospel speak`

**2**  holy Luke: thanks to the Lord,
`holy-Luke to-Lord thanks`

**3**  the Lord God, thanks be;
`Lord God thanks exist`

**4**  of the Lord, holy mercy, Lord;
`<of>-Lord holy-have_mercy Lord`

**5**  this Lord, the gate, Lord;
`this Lord gate Lord`

**6**  of the Lord, many homes.
`<of>-Lord many home`

**7**  Before, many holy fathers before, many, writes […] the church father:
`before many holy-father-before many write [?] church_father`

**8**  heaven; the Lord's Son […] the Lord taken; to see one […]
`+heaven Lord son +<subj> grab-Lord see one [?]`

**9**  because many holy fathers wanted to see the Lord Jesus Christ […]
`because because many holy-father want see Lord-Jézus-Christ [?]`

**10**  The Lord's chapter: many; how shall we see? In turn, Simeon; one, Simeon.
`Lord-chapter many ?how_shall_we see a) Simeon one-Simeon`

> Luke 2:25-32, Simeon, who was promised he should not see death before he
> had seen the Lord's Christ, and Luke 10:24, "many prophets and kings have
> desired to see those things which ye see". The reading continues on 102r.

## 102r — Simeon's arms, and the thirtieth year

**1**  and shall be called; it is Simeon; for Simeon carried him in his bosom:
`and ?shall_be_called exist Simeon because from Simeon carry +bosom`

**2**  the Lord Jesus Christ […]. The Lord saw the apostles and the Jewish people, and
`Lord-Jézus-Christ [?] Lord see apostle and Jew(ish) people-chapter and`

**3**  these apostles, the Jews, the Lord; all saw within […] of the name of the man.
`this apostle Jew(ish) Lord each,_every see inside [?]-from-+name somebody`

**4**  Then was the Lord Jesus within his thirtieth year. Then,
`time then-exist Lord-Jézus inside thirty year time`

**5**  from the woman, the Lord Jesus; and the Lord went from town
`from-woman-woman Lord-Jézus and go-Lord from town`

**6**  to town, from temple to temple, from
`+until town from temple +until temple from`

**7**  field to field; and the Lord's apostles went into the world; the gospel
`plough_land +until plough_land and <of>-Lord apostle go-Lord ?into_the_world gospel`

**8**  the Lord preached; various miracles the Lord did afterward: […]
`preach-Lord various miracle ?afterward-Lord | [?]`

**9**  […] the Lord: through light [the blind saw]; the dead the Lord raised up; the lame [walked];
`[?] +<subj>-Lord through light-Lord die ?raised_up_(by_the_Lord) ?lame`

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

**3**  of the Lord; to the thief, who […]; and the Lord redeemed man from hell
`+<subj> <of>-Lord to-to-thief-who and somebody redeem-Lord from hell`

**4**  fire. And then the Lord, the cross […] […]
`fire and then-exist-Lord +cross-[?] | [?]`

**5**  […] and the moon, this darkened, before the sun darkened;
`[?] and moon this eclipse before sun eclipse`

**6**  and before the moon darkened, the face of the earth quaked; the rock,
`and before moon eclipse face-~Adam quake rock`

**7**  the stone rent; and at the sun's darkening every
`stone +rent and on-sun eclipse each,_every`

**8**  creature […] this humbled itself, and every creature mourned.
`?creatures [?] this humble and each,_every create mourn`

**9**  Then Christ, the cross […]; and the Lord was put in the sepulchre.
`then-exist Christ +cross-[?] ~and Lord inside burial_chamber | put`

> Matthew 27:45 and 27:51, the darkness and the rocks rent, with Luke 23:43
> for the thief. *Rent* is Király & Tokai's split-the-rock sign in a second
> spelling their entry cites at this line and at 052v:2, where the same
> sentence stands in the long Passion. Their quake, rock, stone, humble and
> mourn are all cited by them on these lines.

## 103r — the three days: where was the soul?

**1**  said; and then the Lord lay in the sepulchre, the Lord; and the hour, then,
`+say and then-exist-Lord inside burial_chamber lay-Lord and hour time`

**2**  went to the Father, God, heaven; to the Father's; the angel; the soul within
`go from-father God heaven on-<of>-father angel soul inside`

**3**  […] the Lord Jesus, and rose from prayer(?).
`[?]-chapter Lord-Jézus and ?rise from pray`

**4**  In turn: the devil in the sepulchre stayed; in turn, the Lord went to hell,
`in_turn angel inside burial_chamber +stayed in_turn to-Lord go-Lord on-hell`

**5**  and destroyed hell, and redeemed man; hell fire, because | he carried,
`and hell destroy and somebody redeem-Lord fire hell because | carry`

**6**  the Lord, his cross on his shoulder; and man's soul […]
`Lord <of>-Lord +cross on-<of>-Lord shoulder and somebody soul-[?]`

**7**  of the Lord the Father, all the world, the people. And then the Lord Jesus, from
`<of>-Lord father-<divine> each,_every the_whole_wide_world ?people +and_then Lord-Jézus | from`

**8**  the Father, the Lord God eternal; the soul […] of this Father, this soul
`father <of>-Lord God ?eternal soul-[?] this-father-<divine> this soul`

> The question the fathers asked of the three days: did the soul stay in the
> sepulchre, or go down to hell? Line 4 puts both, with *stayed*, which is
> Király & Tokai's stay sign in a spelling they cite at this line. The word
> rendered angel on lines 2 and 4 is their angel/Satan/Lucifer sign; on line
> 4 the devil is meant.

## 103v — the lost sheep, a doxology, and the names in one sign

**1**  of the Lord; from the lost sheep this Lord's soul the Lord redeemed; the wolf; the face of the earth;
`<of>-Lord from-+the_lost_sheep this-Lord soul redeem-Lord wolf face-~Adam`

**2**  this Father's soul; the lost sheep […] the Lord took; this Father's soul.
`this-father-<divine> soul +the_lost_sheep [?] grab-Lord this-father-<divine> soul`

**3**  […] […] until the ages of ages,
`[?] [?] +until chapter-oh chapter-oh`

**4**  amen. From every ghost, and from […] the Lord, from the heavenly, on this
`amen from each,_every ghost and from [?] Lord from ?heavenly on-this`

**5**  the people believe; woman, woman; and […] the Lord […] the angel. On
`?people believe woman woman and [?] Lord [?] angel | on`

**6**  […]-[…]-Mary-Jesus-God-Christ-angel-the-lost-sheep
`[?]-[?]-Mary-Jézus-God-Christ-angel-+the_lost_sheep`

**7**  speaks Saint […], the church father. Holy
`speak +Saint_[a_church_father] church_father | holy`

**8**  Anne, this Anne, gave birth:
`Anne this Anne be_born`

**9**  […] […] […]
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

**2**  Mary; from Mary the coming of the Lord Jesus Christ; and the Lord went
`Mary from Mary ?coming Lord-Jézus-Christ and from Lord go`

**3**  into the world, preached the gospel, various miracles; afterward
`?into_the_world gospel preach various miracle ?afterward`

**4**  the Lord suffered for man's sin, for the whole world; the Lord was crucified, and
`Lord and suffer to somebody +sin the_whole_wide_world +crucified Lord and`

**5**  for man the Lord shed his blood, and the Lord redeemed man
`to somebody +<subj> <of>-Lord +shed_his_blood and somebody +<subj> redeem-Lord`

**6**  from hell fire; and man, the Lord; there is the faith
`from hell fire and somebody Lord exist believe-chapter`

**7**  in the true Son of the living God: every man shall be saved; and one
`to righteous(ly) son living God each,_every somebody be_saved and one`

**8**  man shall be damned; and the Lord: he that believeth not, and […]
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

**6**  and the Jewish people:
`and Jew(ish) people-chapter`

**7**  blessed the two
`to-happy two from`

**8**  eyes, the two eyes that see the Lord; and you [see] those things which | the apostles see.
`eye-from to-two eye-from this Lord see who you ?those_things_which | see-apostle`

**9**  He said: for many holy fathers, many, writes the church father, many prophets, many
`+say because many holy-father many write church_father many prophet many`

**10**  kings, many emperors | would have liked, the fathers, church fathers, prophets, kings, emperors,
`king many emperor | would_like_to-father-church_father-prophet-king-emperor`

**11**  to see this which you […] from […]; and
`this see who you [?] from-[?] and`

**12**  there rose among these Jews one; another church father wanted
`+rise among this Jew(ish) one +another church_father want`

> Luke 10:23-24: "Blessed are the eyes which see the things that ye see: for
> I tell you, that many prophets and kings have desired to see those things
> which ye see, and have not seen them." The citation, Luke chapter ten, is
> right. Line 10 packs father, church father, prophet, king and emperor into
> one compound sign after listing them one by one on lines 9-10.
