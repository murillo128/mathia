# MC-319 — Smooth-modulus zero-free rigidity reaches the common source modulus but not the dyadic endpoint resolution

**Status:** `LITERATURE+DERIVED` · `EXACT-DERIVED` · `FRONTIER-NARROWING` · `NEGATIVE/OBSTRUCTION` · `PRIOR-ART-AUDITED` · `NON-RH`.

## Claim

Continue the exact reciprocal-endpoint branch isolated by `MC-305`, `MC-314`, and `MC-317`. Let

\[
\mathcal R_y=\{r:y<r\le 2y,\ r\text{ prime},\ r\equiv1\pmod4\},
\qquad N=|\mathcal R_y|,
\]

let `R` independent quadratic source characters be induced from the common odd squarefree radical `P`, and put

\[
q:=4P.
\]

Assume the balanced critical-rank regime

\[
2^R=(\kappa_0+o(1))\log y
\qquad(0<\kappa_0<\infty),
\tag{1}
\]

together with the exact-natural-scale source package considered in `MC-314`,

\[
n=2R,
\qquad
Z:=\max U\le y^{1/R}.
\tag{2}
\]

Then the already-proved endpoint constraints imply

\[
P\ge \frac{y}{(\log y)^{O(1)}},
\qquad
P\le Z^{2R}\le y^2,
\qquad
P^+(q)\le Z\le y^{1/R}.
\tag{3}
\]

Consequently

\[
\log q\asymp\log y,
\qquad
\frac{\log P^+(q)}{\log q}
=O\!\left(\frac1{\log\log q}\right).
\tag{4}
\]

This is smooth enough to enter the joint smooth-modulus zero-free theorem of Klurman--Mangerel--Teräväinen (KMT), Lemma 12.3 of `MC-S45`, which records Chang's improved zero-free region. More precisely, writing

\[
L:=\log\log q,
\]

there is a fixed constant `A>0` such that, for all sufficiently large `y`, the theorem may be applied with

\[
\vartheta=\frac{A}{L}.
\tag{5}
\]

It follows that the product over **all** Dirichlet characters modulo `q` has the zero-free region

\[
\boxed{
\Re s\ge
1-c_1\frac{\log\log q}{\log q},
\qquad
|\Im s|\le q,
}
\tag{6}
\]

apart from possibly one real simple zero belonging to one real character modulo `q`, for some fixed `c_1>0`.

Thus the smooth common-radical hypothesis really does buy a collective rigidity statement: among the `2R` distinct characters

\[
\chi_i,\qquad \chi_i\chi_4
\qquad(1\le i\le R),
\tag{7}
\]

at most one can be the exceptional character in `(6)`.

However, the prime-sum consequence used by KMT does **not** resolve the endpoint shell. Their Lemma 12.5 converts a zero-free strip of width `\eta^{-2}/\log q` into the Rodosskii-type estimate

\[
\sup_{|t|\le(\log q)^{3/2}}
\left|
\sum_{Y\le p\le Y^{1+\varepsilon}}
\frac{\chi(p)}{p^{1+it}}
\right|
\le C_0\eta,
\tag{8}
\]

provided `Y\ge q^\eta`, for a non-principal character with the required zero-free region. From `(6)`, the smallest scale parameter justified by this route is only

\[
\eta\asymp (\log\log q)^{-1/2}.
\tag{9}
\]

Since `q\le4y^2`, the condition `y\ge q^\eta` is harmless for `(9)`. The resulting analytic resolution is therefore

\[
\boxed{
\left|
\sum_{y\le p\le y^{1+\varepsilon}}
\frac{\chi(p)}p
\right|
\ll (\log\log q)^{-1/2}
}
\tag{10}
\]

for every fixed `\varepsilon>0` and every nonexceptional relevant character, after increasing the implicit constants as needed.

The endpoint signal is far smaller in this harmonic metric. Exact one-defect occupancy gives, for every selected source character,

\[
\#\{r\in\mathcal R_y:\chi_i(r)=+1\}=\frac NR,
\qquad
\#\{r\in\mathcal R_y:\chi_i(r)=-1\}=N\left(1-\frac1R\right).
\tag{11}
\]

Hence, without assuming any independence between sign and prime location,

\[
\boxed{
\left|
\sum_{r\in\mathcal R_y}\frac{\chi_i(r)}r
\right|
\gg \frac1{\log y}.
}
\tag{12}
\]

Indeed, assigning all positive signs the largest possible weight `1/y` and all negative signs the smallest possible weight `1/(2y)` still gives

\[
\sum_{r\in\mathcal R_y}\frac{\chi_i(r)}r
\le
\frac Ny\left(-\frac12+\frac{3}{2R}\right)
\le -\frac{N}{4y}
\tag{13}
\]

for large `R`, while `N\sim y/(2\log y)`.

But

\[
\frac1{\log y}
=o\!\left((\log\log q)^{-1/2}\right).
\tag{14}
\]

Moreover the dyadic shell itself corresponds to the power-window exponent

\[
\varepsilon_y=\frac{\log2}{\log y},
\tag{15}
\]

whereas the KMT Rodosskii proof only gains cancellation after smoothing on logarithmic widths comparable with its parameter `\eta`; with `(9)`, `\varepsilon_y\ll\eta`. Therefore the existing smooth-modulus zero-free-plus-Rodosskii mechanism is intrinsically too coarse to distinguish the endpoint's one-shell harmonic bias from the trivial dyadic mass.

This **does not** show that `(6)` is incapable of yielding the desired dyadic prime-character estimate by some stronger argument. It shows something narrower and durable: the specific KMT conversion supplied by the cited smooth-modulus theory resolves broad power intervals at an `O((\log\log q)^{-1/2})` harmonic scale, while the endpoint contradiction requires control at the much finer `o(1/\log y)` dyadic scale. The proposed smooth-modulus clue therefore survives only as a sharper analytic question: one needs a genuinely dyadic prime-character theorem, or additional collective information beyond the present Rodosskii bound.

No estimate for `M(x)` follows.

## 1. The endpoint parameters satisfy KMT's smooth-modulus hypothesis

From `MC-305` and `(1)`,

\[
P\ge y(\log y)^{-B+o(1)}
\tag{16}
\]

for some fixed `B`, while `(2)` gives `P\le y^2`. Hence

\[
1-o(1)
\le
\frac{\log q}{\log y}
\le
2+o(1).
\tag{17}
\]

Also `(1)` gives

\[
R=\frac{\log\log y}{\log2}+O(1),
\tag{18}
\]

and therefore, using `(2)`,

\[
\frac{\log P^+(q)}{\log q}
\le
\frac{\log y}{R\log q}
=O\!\left(\frac1{\log\log q}\right).
\tag{19}
\]

KMT Lemma 12.3 states that if

\[
P^+(q)\le q^\vartheta,
\qquad
\frac{C}{\log\log(10q)}<\vartheta<0.001,
\tag{20}
\]

then

\[
\prod_{\chi\ ({\rm mod}\ q)}L(s,\chi)
\]

has no zero in

\[
\Re s\ge1-\frac{c\vartheta^{-1}}{\log q},
\qquad |\Im s|\le q,
\tag{21}
\]

apart from possibly one real simple zero corresponding to a unique real character.

Equation `(19)` lets us choose a fixed `A` larger than both the constant required in `(20)` and the bounded coefficient implicit in `(19)`, then set `\vartheta=A/L`. For large `q`, `(20)` holds and `(21)` becomes `(6)` with `c_1=c/A`.

The mod-4 restriction does not create a second exceptional family. Because `P` is odd, characters induced from modulus `P` are trivial on the `(\mathbb Z/4\mathbb Z)^\times` factor, whereas multiplication by `\chi_4` is nontrivial on that factor. Thus the `2R` characters in `(7)` are distinct modulo `4P`, and the one-exception statement applies to the whole set simultaneously.

## 2. The zero-free strip implies only a much coarser Rodosskii resolution

KMT Lemma 12.5 assumes a zero-free region of width

\[
\frac{\eta^{-2}}{\log q}
\tag{22}
\]

and gives `(8)`. To make `(22)` fit inside `(6)`, it is enough to take

\[
\eta=K L^{-1/2}
\tag{23}
\]

with a sufficiently large fixed `K`, because then

\[
\eta^{-2}
=K^{-2}L
\le c_1L.
\]

Conversely, this route cannot use `\eta=o(L^{-1/2})` from `(6)` alone, since the demanded strip `(22)` would then be wider than the strip actually supplied by `(6)`.

For the prime variable `Y=y`, `(17)` gives

\[
\frac{\log y}{\log q}\ge\frac12-o(1),
\]

so `y\ge q^\eta` is automatic for `(23)` once `y` is large. This proves the broad-window estimate `(10)` for every nonexceptional relevant character.

KMT explicitly exploit the harmonic weight `1/p` to make this narrow zero-free region useful; their discussion preceding Lemma 12.5 notes that a direct pointwise `L'/L` estimate costs two logarithms and therefore asks for a stronger zero-free region. The Rodosskii smoothing avoids that cost, but the price is precisely the coarse logarithmic resolution quantified above.

## 3. Exact endpoint occupancy has only dyadic harmonic mass

Equation `(11)` is the exact endpoint average `-1+2/R` rewritten as sign counts. Since every `r` lies in `(y,2y]`,

\[
\frac1{2y}<\frac1r<\frac1y.
\]

The largest possible value of the signed harmonic sum, subject only to the counts `(11)`, occurs if every positive sign receives weight `1/y` and every negative sign receives weight `1/(2y)`. This gives `(13)`. The fixed-modulus prime number theorem for `1 mod 4`, already used in `MC-305`, gives

\[
N=\left(\frac12+o(1)\right)\frac y{\log y},
\]

which proves `(12)`.

The mod-4 projector gives the exact identity

\[
\sum_{r\in\mathcal R_y}\frac{\chi_i(r)}r
=
\frac12
\sum_{y<p\le2y}
\frac{\chi_i(p)+\chi_i\chi_4(p)}p.
\tag{24}
\]

Thus a contradiction from prime-character cancellation would need dyadic control on the pair `\chi_i,\chi_i\chi_4` at a scale strictly smaller than `1/\log y`. Because at most one of all `2R` characters can be exceptional, at least `R-1` pairs are fully nonexceptional under `(6)`. Nevertheless `(10)` is too coarse by `(14)` even for those pairs.

This is not an exceptional-zero problem anymore. It is a **resolution problem**: after the joint zero-free theorem removes all but one possible exceptional character, the available prime-sum conversion still averages on a logarithmic scale much larger than one dyadic shell.

## Prior art and novelty boundary

The external analytic input is entirely established. `MC-S45` is Klurman, Mangerel and Teräväinen, *Multiplicative functions in short arithmetic progressions*, Proc. London Math. Soc. 127 (2023), 366–446, DOI `10.1112/plms.12546`, arXiv `1909.12280`. Its Lemma 12.3 records the smooth-modulus joint zero-free region from Chang's Theorem 10 and its Lemma 12.5 gives the Rodosskii-type prime sum used in `(8)`.

A targeted literature search around smooth-modulus zero-free regions, individual character sums over primes, and primes in progressions to smooth moduli found the KMT/Chang mechanism and broader average-over-moduli distribution results, but no theorem was identified that directly supplies

\[
\sum_{y<p\le2y}\chi(p)\log p=o(y)
\]

uniformly for the present moving-modulus range `q\in[y(\log y)^{-O(1)},4y^2]` for every nonexceptional member of the selected family. This is a bounded audit, not a bibliographic-completeness claim.

No novelty is claimed for the zero-free or Rodosskii theorems. The durable Mathia delta is the parameter bridge `(3)`--`(6)` and the exact scale comparison `(9)`--`(15)`: the arithmetic endpoint is smooth enough to enter the strongest cited collective zero-free mechanism, but the cited prime-sum consequence does not operate at the one-shell resolution the endpoint needs.

## Boundaries and falsification tests

- **Exact natural source scale is load-bearing.** The upper bound `P^+(q)\le y^{1/R}` comes from the `Z\le y^{1/R}` branch of `MC-314`; this finding does not assert that every source package satisfies it.
- **Balanced critical rank is load-bearing for the displayed smoothness coefficient.** The conclusion uses `R\asymp\log\log y`. A materially smaller rank changes `(19)` and must be rechecked.
- **The common-radical lower bound matters.** `MC-305` supplies `P\ge y/(\log y)^{O(1)}` in this endpoint regime, ensuring `\log q\asymp\log y`; without it the scale comparison changes.
- **Only one exceptional zero is allowed, but that alone does not control a dyadic shell.** Equation `(6)` is a genuine family-wide restriction; the negative conclusion concerns the resolution of the available prime-sum conversion, not the zero-free theorem itself.
- **No claim is made that every consequence of `(6)` is exhausted.** A sharper explicit-formula, density, bilinear, or collective-character argument might still prove the required dyadic estimate. Such an argument would be new input relative to the KMT Rodosskii step audited here.
- **The harmonic lower bound is deterministic.** Equation `(12)` uses only the exact endpoint sign counts and the factor-two range of `1/r`; no random-sign or sign/location independence assumption enters.
- **A broad power interval cannot replace the dyadic shell.** Source characters and their endpoint sign pattern are defined at the current shell. Cancellation from primes outside `(y,2y]` may erase its harmonic contribution in `(10)`, so broad-window control cannot be restricted back to the shell without new localization information.
- **No circular zero-free input is used.** The zero-free theorem concerns Dirichlet `L(s,chi)` for the source characters, not `1/zeta(s)` or a zero-free region equivalent to the target Mertens estimate.
- **No RH or Mertens estimate follows.** The result narrows one arithmetic-realizability escape after `MC-317`.

## Consequence for the research line

The smooth-common-modulus clue passes its first gate and fails to close the second with the currently cited machinery. The endpoint modulus is genuinely smooth enough that Chang/KMT leave at most one exceptional character across the entire selected family and its mod-4 twists. What remains is not another generic coding problem and not merely a Siegel-zero bookkeeping problem.

The next theorem surface is now precise: obtain **dyadic** prime-character cancellation, or a collective substitute strong enough to rule out `R-1` simultaneous endpoint biases, for characters whose common modulus satisfies `(3)`. Reusing the existing Rodosskii estimate on `[y,y^{1+\varepsilon}]`, or invoking the one-problem-character statement without a dyadic localization theorem, cannot by itself close the arithmetic endpoint.