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

**13**  […] […] and […] from Abraham until
`[?] [?] and [?] from Abraham until`

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

**1**  […] from […] […] until the Virgin Mary | was born
`[?] from [?] [?] ~out(ward) until virgin-Mary | be_born`

**2**  […] […] and one […] and […]
`[?] [?] and one [?] and [?]`

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

**12**  […] from […] […] until the Virgin Mary was conceived; and […]
`~out(ward) from [?] [?] until virgin-Mary get_conceived and [?]`

**13**  […] and one hundred, and […] and
`[?] and one hundred and [?] and`

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

**3**  […] from […] […] until the birth […]
`out(ward) from [?] [?] until be_born [?]`

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
