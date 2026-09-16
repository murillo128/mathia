# FD-163 — Square-root principal closure forces positive anchor exposure

- **Date:** 2026-09-16
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** exact obstruction / arbitrary prime-avoidance anchors / positive anchor exposure
- **Depends on:** FD-159, FD-160, FD-161, FD-162

## Claim

FD-162 showed that if an arbitrary prime anchor eventually contains every fixed small prime, then any nontrivial active auxiliary core pays growing principal-closure pressure. Its explicit surviving anchor-side escape was a persistent low-prime hole: for example, if `2 notin S`, the first-omitted-prime reservoir from FD-162 is empty.

That escape is not sufficient. A principal divisor closure exposes **all anchor divisors up to a square-root scale**, independently of which small primes are omitted. Under bounded architecture resources, this forces only `O(1)` anchor primes below that scale. The remaining anchor primes are all larger than `sqrt(T)` and therefore behave as one-hit exclusions; they cannot remove more than a fixed fraction of the squarefree vertices. Consequently the prime-avoidance anchor face itself retains positive asymptotic exposure.

Retain the notation of FD-159. Let

\[
V_T:=\{n\le T:\mu^2(n)=1\},
\qquad
D_{S,T}:=\{n\in V_T:(n,P_S)=1\},
\qquad
P_S:=\prod_{p\in S}p,
\tag{1}
\]

for a finite nonempty set of anchor primes `S`, and write `p_*:=min S`. Let `h_(S,T)` be the anchored Cheeger constant, `P_(S,T)` the parent distortion, `f_(S,T)(d)` the occupied primary-fiber count, and `L_(S,C,T)` the outgoing leakage of a finite divisor down-set `C`. For `X>=1`, define the anchor-divisor volume

\[
A_S(X):=\#\{q:q\mid P_S,\ q>1,\ q\le X\}.
\tag{2}
\]

Take a nontrivial active `S`-free auxiliary core

\[
c\in D_{S,T},
\qquad
c>1,
\qquad
p_*c\le T,
\tag{3}
\]

and its principal divisor ideal

\[
D(c):=\{d:d\mid c\}.
\tag{4}
\]

Then

\[
\boxed{
\bar f_{S,D(c)}(T)
\ge
\frac12 A_S\!\left(\frac{T}{\sqrt c}\right)
\ge
\frac12 A_S\!\left(\sqrt{Tp_*}\right).
}
\tag{5}
\]

Hence FD-159 gives the exact square-root closure-pressure law

\[
\boxed{
P_{S,T}
+
\frac{L_{S,D(c),T}}{2^{\omega(c)}}
\ge
\frac{h_{S,T}}2
A_S\!\left(\sqrt{Tp_*}\right).
}
\tag{6}
\]

In particular, if along a family with persistent nontrivial active cores

\[
h_{S,T}\ge h_0>0,
\qquad
P_{S,T}\le P_0,
\qquad
\frac{L_{S,D(c),T}}{2^{\omega(c)}}\le L_0,
\tag{7}
\]

then, for

\[
X_T:=\sqrt{Tp_*},
\tag{8}
\]

the number of anchor primes below `X_T` satisfies

\[
\boxed{
\#\{p\in S:p\le X_T\}
\le
B_0:=\frac{2(P_0+L_0)}{h_0}.
}
\tag{9}
\]

This bounded square-root anchor complexity already forces positive exposure. More precisely, with `B:=ceil(B_0)`,

\[
\boxed{
\frac{|D_{S,T}|}{|V_T|}
\ge
2^{-B}\bigl(1-\log 2-o(1)\bigr).
}
\tag{10}
\]

Thus, under bounded positive anchored expansion, bounded parent distortion, and bounded normalized principal-closure leakage, a nontrivial auxiliary core cannot coexist with a prime-avoidance anchor face whose squarefree exposure tends to zero. A persistent low-prime hole does not rescue that architecture.

## 1. Half of a principal closure sees every anchor divisor below `T/sqrt(c)`

Because `c` is squarefree and `c>1`, it is not a perfect square. Pair each divisor `d|c` with `c/d`. Exactly one member of each pair is smaller than `sqrt(c)`, so exactly half of the `2^(omega(c))` divisors satisfy

\[
d<\sqrt c.
\tag{11}
\]

Fix such a divisor `d`, and take any anchor divisor `q` counted by `A_S(T/sqrt(c))`. Since `q|P_S` while `d|c` and `c` is `S`-free,

\[
(q,d)=1.
\tag{12}
\]

Moreover,

\[
qd
<
q\sqrt c
\le T.
\tag{13}
\]

Hence every such `q` is an occupied primary state above `d`, and therefore

\[
f_{S,T}(d)
\ge
A_S\!\left(\frac{T}{\sqrt c}\right)
\qquad(d\mid c,\ d<\sqrt c).
\tag{14}
\]

The other half of the principal closure contributes nonnegative fiber size. Averaging proves the first inequality in (5).

Activity gives `c<=T/p_*`, whence

\[
\frac{T}{\sqrt c}
\ge
\sqrt{Tp_*}.
\tag{15}
\]

Since `A_S` is monotone, the second inequality in (5) follows. The principal ideal remains an admissible active divisor down-set exactly as in FD-159 and FD-162, so substituting (5) into the average-fiber leakage law proves (6).

Equation (5) is strictly different from the first-omitted-prime reservoir of FD-162. It does not require an initial segment of primes inside `S`: every divisor of the actual anchor product below the square-root scale contributes. In particular, each anchor prime `p<=X_T` is itself counted by `A_S(X_T)`, which yields (9) directly from (6) and (7).

## 2. Bounded square-root anchor complexity leaves a large smooth squarefree reservoir

The remaining anchor primes lie above `X_T`. They cannot jointly erase the squarefree face because the activity assumption itself places `X_T` beyond the square-root threshold.

Indeed `c>1` and squarefree imply `c>=2`; from `p_*c<=T`,

\[
p_*\le T/2.
\tag{16}
\]

Consequently

\[
\sqrt{2T}
\le
X_T
=
\sqrt{Tp_*}
\le
T/\sqrt2
< T.
\tag{17}
\]

Consider the divisor-closed family of `X_T`-smooth squarefree integers

\[
\mathcal F_T(X_T)
:=
\{n\le T:\mu^2(n)=1,\ P^+(n)\le X_T\}.
\tag{18}
\]

where `P^+(1)=1`. Since `X_T>sqrt(T)`, any squarefree integer outside this family contains exactly one prime factor `p>X_T`. Writing it uniquely as `n=pm`, one has `m<=T/p<p`, so `p` does not divide `m` and `m` is any squarefree integer up to `T/p`. Therefore

\[
|V_T\setminus\mathcal F_T(X_T)|
=
\sum_{X_T<p\le T}Q_{\rm sf}(T/p),
\tag{19}
\]

where

\[
Q_{\rm sf}(y)
=
\frac{y}{\zeta(2)}+O(\sqrt y)
\tag{20}
\]

is the elementary squarefree-counting estimate already used in FD-162.

Using (20), the prime number theorem and partial summation,

\[
\sum_{X_T<p\le T}Q_{\rm sf}(T/p)
=
\frac{T}{\zeta(2)}
\sum_{X_T<p\le T}\frac1p
+O\!\left(
\sqrt T\sum_{X_T<p\le T}p^{-1/2}
\right),
\tag{21}
\]

with

\[
\sum_{X_T<p\le T}p^{-1/2}
=O\!\left(\frac{\sqrt T}{\log T}\right),
\tag{22}
\]

and

\[
\sum_{X_T<p\le T}\frac1p
=
\log\log T-\log\log X_T+o(1)
\le
\log2+o(1),
\tag{23}
\]

because `X_T>=sqrt(T)`. Combining (19)--(23) with `|V_T|=T/zeta(2)+O(sqrt(T))` gives

\[
\boxed{
\frac{|\mathcal F_T(X_T)|}{|V_T|}
\ge
1-\log2-o(1).
}
\tag{24}
\]

The constant `1-log 2` is the familiar square-root smooth-number density `rho(2)`; no novelty is claimed for it. Here (24) is kept elementary because the one-large-prime decomposition is exact when `X_T>sqrt(T)`.

## 3. Each low anchor prime costs at most a factor two

Let

\[
S_{\rm low}:=S\cap[2,X_T].
\tag{25}
\]

By (9), `|S_low|<=B`. The family `F_T(X_T)` is divisor-closed. More generally, if a finite squarefree divisor-closed family `A` is already restricted to avoid some set of primes and `p` is another prime, partition it into members divisible and not divisible by `p`. Division by `p` gives an injection

\[
\{n\in\mathcal A:p\mid n\}
\hookrightarrow
\{n\in\mathcal A:p\nmid n\},
\qquad
n\mapsto n/p.
\tag{26}
\]

The image remains in the family by divisor closure, and it avoids all previously excluded primes. Hence imposing avoidance of one additional prime removes at most half the current family. Iterating over `S_low` gives

\[
\#\{n\in\mathcal F_T(X_T):(n,P_{S_{\rm low}})=1\}
\ge
2^{-|S_{\rm low}|}|\mathcal F_T(X_T)|
\ge
2^{-B}|\mathcal F_T(X_T)|.
\tag{27}
\]

Every prime in `S\setminus S_low` is larger than `X_T`, whereas every member of `F_T(X_T)` has all prime factors at most `X_T`. Therefore every integer counted on the left of (27) automatically avoids **all** anchor primes, not just the low ones. It is a subset of `D_(S,T)`. Combining (24) and (27) proves (10).

This is the missing step after FD-162. A bounded first-prime reservoir could be defeated by permanently omitting a low prime, but bounded principal-closure resources force something stronger: only boundedly many anchor primes can occur anywhere below the natural square-root resolution. Once that happens, the infinitely many possible high anchors are too large to remove the smooth squarefree reservoir, while the bounded low set costs only a fixed multiplicative factor.

## 4. Stress tests and sharp boundaries

The conclusion requires a persistent nontrivial active auxiliary core. If no `c>1` satisfies `p_*c<=T`, the principal-closure argument does not start. Likewise, (10) is conditional on the bounded-resource hypotheses (7). A construction can still escape by letting anchored expansion collapse, parent distortion grow, or normalized outer leakage grow.

No claim is made that `2^{-B}(1-log2)` is optimal. The factor `2^{-B}` is the worst-case consequence of the elementary divisor-closure injection; the actual loss from excluding a prime `p` is normally closer to a `p`-dependent density factor. The point needed here is only a uniform positive lower bound when the number of anchors below `X_T` is bounded.

The result is also an architecture theorem, not yet a source-native Farey theorem. It shows that the prime-avoidance anchor face cannot become asymptotically invisible while the FD-159 resources remain bounded and a nontrivial auxiliary closure persists. It does not prove that the Farey discrepancy observable supplies independent information on that positive-density face, does not generate the required Möbius orientations, and does not bridge the remaining information-budget gate to the RH-critical Franel--Landau statement.

## 5. Prior art, representation audit, and consequence for the line

The external ingredients are classical. The squarefree count (20), the prime number theorem, and reciprocal-prime estimates are already covered by the line's existing source anchors. The appearance of `1-log2=rho(2)` is the classical Dickman--de Bruijn square-root smooth-number phenomenon; de Bruijn's 1951 work on integers free of large prime factors is neighboring prior art, not a novelty claim. A targeted search found the expected smooth-number literature but not the coupling of square-root smooth density to FD-159's principal-closure Cheeger pressure. No new external theorem is load-bearing, so `SOURCES.md` requires no update.

The representation audit separates the result cleanly. The half-closure inequality (5), the bounded low-anchor consequence (9), and the divisor-closed factor-two argument are generic squarefree divisibility geometry. The Farey-line-specific content is their use inside the existing anchored positive-divisibility architecture to eliminate the explicit `persistent low-prime hole` escape left by FD-162. No Farey values or Möbius signs enter the proof, so this is still an architecture obstruction rather than source-specific cancellation.

The live anchor-side frontier is therefore narrower. Under bounded FD-159 resources, **vanishing prime-avoidance anchor exposure is no longer available as an auxiliary-migration mechanism**, regardless of whether the anchor omits a fixed small prime. Any surviving construction must pay through architecture deterioration or confront the source-native information-budget problem on a positive-density anchor face.

### Retrieval notes

- Internal inputs: FD-159 through FD-162, the current `farey_discrepancy` synthesis and intuition, current local clue dispositions, and the existing PNT/squarefree-counting anchors in `SOURCES.md`.
- No open local adversarial-review sidecar had owner precedence when this investigation began.
- The square-root closure inequality and positive-exposure argument were derived before the external prior-art audit; the search was used only to identify the classical Dickman--de Bruijn boundary and avoid novelty overclaiming.
- `SOURCES.md`, clues, and `mind/**` are unchanged because no new load-bearing source or clue-state transition is introduced.
- No computational or formalization handoff is needed: the decisive steps are exact divisor pairing, one-large-prime decomposition, and a divisor-closed injection.