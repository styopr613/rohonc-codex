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

**Numerals that resolved.** Their numbers are written as sums of their parts.
`ten-ten-ten-ten` at 004v:11 and `two-two-ten` at 008r:11 both come to **forty**,
and both sit where forty belongs — forty days and forty nights, and the forty
days of rain. `two-<distributive infix>-two` at 008r:6 and 008r:8 is **two by
two**, of every creature into the ark.

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
