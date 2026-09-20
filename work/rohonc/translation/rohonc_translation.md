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
