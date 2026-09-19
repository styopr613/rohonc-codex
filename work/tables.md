<!-- RANKING -->
| process | what it is | fp42 APE | fp42 floor | line floor | median floor |
|---|---|---:|---:|---:|---:|
| `noise_floor` | manuscript, other half | 2.0% | 0.16x | 0.35x | 0.12x |
| `fivecomp` | five-component model (fingerprint) | 3.3% | 0.29x | 2.96x | 0.25x |
| `manual` | hand-executable manual (fingerprint) | 9.0% | 1.15x | 2.99x | 0.61x |
| `naibbe_latin` | Naibbe verbose cipher over latin | 15.6% | 1.24x | 3.24x | 1.07x |
| `naibbe_italian` | Naibbe verbose cipher over italian | 15.4% | 1.19x | 3.30x | 0.87x |
| `grille` | table-and-grille (Rugg) | 34.8% | 3.34x | 2.48x | 1.47x |
| `grille_bigtable` | table-and-grille, large table | 23.0% | 2.68x | 2.83x | 1.58x |
| `selfcite` | self-citation (Timm & Schinner) | 18.6% | 2.38x | 2.93x | 1.64x |
| `llull` | Llull combinatoric disks | 51.6% | 5.18x | 4.04x | 3.24x |
| `abbrev` | Latin scribal abbreviation | 50.1% | 5.66x | 3.22x | 4.61x |
| `gibberish` | human gibberish (42 volunteers) | 65.7% | 7.79x | 2.75x | 5.06x |
| `natlang_italian` | plain italian, invented alphabet | 45.3% | 5.56x | 3.75x | 3.64x |
| `natlang_latin` | plain latin, invented alphabet | 51.1% | 4.78x | 3.17x | 4.13x |
| `natlang_hebrew` | plain hebrew, invented alphabet | 52.4% | 6.60x | 3.93x | 4.23x |
| `subst` | substitution cipher over Latin | 49.3% | 4.71x | 3.15x | 3.96x |
| `subst_homophonic` | homophonic cipher over Latin (k=3) | 97.7% | 12.87x | 3.24x | 6.05x |

<!-- HEADLINE -->
| process | h2 | h1 | TTR | word len | Zipf | cross-word MI |
|---|---|---|---|---|---|---|
| **the manuscript** | **1.84** | **3.86** | **0.275** | **5.17** | **-0.904** | **0.068** |
| `noise_floor` | 1.85 | 3.86 | 0.273 | 5.20 | -0.919 | 0.068 |
| `fivecomp` | 1.86 | 3.85 | 0.251 | 5.16 | -0.918 | 0.065 |
| `manual` | 1.91 | 3.79 | 0.232 | 5.20 | -0.728 | 0.049 |
| `naibbe_latin` | 1.78 | 3.87 | 0.271 | 5.23 | -0.954 | 0.005 |
| `naibbe_italian` | 1.79 | 3.86 | 0.262 | 5.20 | -0.973 | 0.004 |
| `grille` | 2.02 | 3.84 | 0.079 | 4.60 | -0.642 | 0.017 |
| `grille_bigtable` | 2.10 | 3.84 | 0.269 | 4.59 | -0.799 | 0.005 |
| `selfcite` | 2.31 | 3.84 | 0.335 | 5.21 | -0.706 | 0.010 |
| `llull` | 2.33 | 3.57 | 0.181 | 7.13 | -0.420 | 0.001 |
| `abbrev` | 3.22 | 4.22 | 0.368 | 5.04 | -0.928 | 0.024 |
| `gibberish` | 3.94 | 4.40 | 0.680 | 4.94 | -0.650 | 0.021 |
| `natlang_italian` | 3.12 | 4.12 | 0.239 | 3.95 | -0.994 | 0.056 |
| `natlang_latin` | 3.19 | 3.97 | 0.351 | 5.33 | -0.934 | 0.016 |
| `natlang_hebrew` | 3.80 | 4.27 | 0.349 | 3.74 | -0.833 | 0.024 |
| `subst` | 3.19 | 3.97 | 0.351 | 5.33 | -0.934 | 0.016 |
| `subst_homophonic` | 4.74 | 5.56 | 0.746 | 5.33 | -0.762 | 0.037 |

<!-- LINE -->
| process | m line-final | gallows lift | cross-line rep | para coherence | section MI | len autocorr |
|---|---|---|---|---|---|---|
| **the manuscript** | **66.97** | **73.34** | **0.12** | **2.61** | **0.23** | **0.11** |
| `noise_floor` | 67.18 | 74.63 | 0.36 | 1.86 | 0.27 | 0.13 |
| `fivecomp` | 10.51 | 2.40 | 0.45 | 1.06 | -0.01 | 0.06 |
| `manual` | 6.75 | 0.35 | 0.80 | 1.75 | 0.02 | 0.03 |
| `naibbe_latin` | 15.93 | 0.20 | 0.18 | 1.27 | 0.05 | -0.03 |
| `naibbe_italian` | 17.27 | 0.49 | 0.06 | 1.15 | 0.05 | -0.04 |
| `grille` | 13.87 | -0.65 | 0.42 | 1.39 | 0.22 | 0.07 |
| `grille_bigtable` | 16.09 | 0.00 | 0.24 | 1.39 | 0.07 | 0.03 |
| `selfcite` | 14.57 | -5.81 | 0.42 | 1.02 | 0.08 | 0.06 |
| `llull` | 3.18 | 1.30 | 0.00 | 0.68 | 0.03 | -0.06 |
| `abbrev` | 0.00 | -1.68 | 0.00 | 1.16 | 0.08 | -0.05 |
| `gibberish` | 0.00 | 0.23 | 0.74 | 0.98 | 0.19 | 0.11 |
| `natlang_italian` | 0.00 | 0.00 | 0.00 | 1.16 | 0.03 | -0.15 |
| `natlang_latin` | 0.00 | 0.00 | 0.12 | 1.08 | 0.06 | -0.03 |
| `natlang_hebrew` | 0.00 | 0.00 | 0.18 | 1.33 | 0.06 | -0.24 |
| `subst` | 8.70 | -2.54 | 0.12 | 1.08 | 0.06 | -0.03 |
| `subst_homophonic` | 0.00 | -0.22 | 0.00 | 0.86 | 0.12 | -0.03 |

<!-- WORST -->

**`fivecomp` — five-component model (fingerprint)**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| line | gallows para-start lift | 2.395 | 73.336 | 10.0x |
| line | m line-final % | 10.511 | 66.966 | 4.7x |
| line | para vocab coherence | 1.063 | 2.610 | 1.9x |
| line | word-section MI (bits) | -0.008 | 0.232 | 1.8x |
| line | word-len autocorr | 0.059 | 0.113 | 1.6x |

**`naibbe_latin` — Naibbe verbose cipher over latin**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| line | gallows para-start lift | 0.204 | 73.336 | 10.2x |
| struct | hapax share of types % | 54.661 | 71.586 | 7.2x |
| struct | adjacent identical words % | 0.160 | 0.870 | 5.3x |
| line | m line-final % | 15.933 | 66.966 | 4.3x |
| line | word-len autocorr | -0.033 | 0.113 | 4.1x |

**`grille_bigtable` — table-and-grille, large table**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| struct | len<=2 % | 16.980 | 7.240 | 14.7x |
| text | top-5 finals % | 72.404 | 91.640 | 10.1x |
| line | gallows para-start lift | 0.003 | 73.336 | 10.0x |
| struct | hapax share of types % | 52.037 | 71.586 | 8.4x |
| text | mean word len | 4.588 | 5.173 | 6.4x |

**`abbrev` — Latin scribal abbreviation**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| text | top-5 finals % | 58.070 | 91.640 | 17.5x |
| struct | len<=2 % | 18.195 | 7.240 | 16.3x |
| struct | H pos4 from end | 4.062 | 3.364 | 14.8x |
| text | h1 (char) | 4.221 | 3.863 | 13.1x |
| text | top-5 onsets % | 46.630 | 70.175 | 10.8x |

**`gibberish` — human gibberish (42 volunteers)**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| text | top-5 finals % | 44.093 | 91.640 | 24.9x |
| struct | H pos4 from end | 4.380 | 3.364 | 21.4x |
| text | h1 (char) | 4.399 | 3.863 | 19.7x |
| struct | H pos2 from end | 4.369 | 2.893 | 19.4x |
| text | top-5 onsets % | 32.665 | 70.175 | 17.3x |
