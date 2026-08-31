# WI-059 — fixed-polylog conductor truncation misses a positive fraction of the `W`-local pair energy

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECTION`. This finding does **not** certify the Yang--Yang one-sided fourth-moment candidate, enlarge the Shao--Teräväinen region of WI-054, or change Mathia's current unconditional simple-critical proportion. It sharpens the effective-conductor reduction of WI-058 and closes one tempting repair of the WI-057 conditioning obstruction: projecting the deterministic `W`-local pair main onto characters of any **fixed polylogarithmic conductor** and discarding the rest by its own `L^2` norm cannot be asymptotically lossless. Conversely, the same exact conductor law gives a substantially smaller sufficient super-polylogarithmic cutoff than the crude `w^(3 log log w)` cutoff recorded in WI-058.

The durable conclusion is the scale separation

\[
\boxed{
D=(\log X)^B\text{ with fixed }B
\quad\text{is too small for raw }L^2\text{ truncation,}
}
\tag{1}
\]

while a cutoff with a slowly growing exponent is enough for relative `L^2` capture, and the explicit uniform choice

\[
\boxed{
D_w
=
\exp\!\left(
(2+\eta+o(1))
\frac{\log w\,\log\log w}{\log\log\log w}
\right)
}
\tag{2}
\]

makes the **absolute** discarded `L^2` energy `o(1)` for every fixed `eta>0`. At the Shao--Teräväinen choice `w=(log X)^C`, this is

\[
D_w
=
\exp\!\left(
O_{C,\eta}\!\left(
\frac{\log\log X\,\log\log\log X}
{\log\log\log\log X}
\right)
\right)
=X^{o(1)}.
\tag{3}
\]

Thus WI-058's subpolynomial-conductor redirection survives and becomes quantitatively sharper, but the exponent of `log X` cannot remain fixed if one wants to throw away the complementary local-main spectrum by `L^2` alone.

## 1. Exact input from WI-058

Use the notation and normalization of WI-058. For

\[
W=\prod_{p\le w}p,
\qquad
G_{W,h}=\frac{F_{W,h}}{\mathbb E F_{W,h}},
\qquad
\mathbb E G_{W,h}=1,
\tag{4}
\]

let `nu_{W,h}` be normalized squared Fourier mass and let

\[
d(a)=\frac{W}{(a,W)}
\tag{5}
\]

be the reduced conductor of the character `a mod W`. WI-058 proves exactly that, under `nu_{W,h}`, the indicators

\[
I_p(a):=1_{p\mid d(a)}
\tag{6}
\]

are independent Bernoulli variables with

\[
\boxed{
\theta_p(h):=\Pr(I_p=1)
=
\begin{cases}
1/p,&p\mid h,\\[1mm]
2/p,&p\nmid h.
\end{cases}}
\tag{7}
\]

for every active local prime. In particular

\[
\frac1p\le\theta_p(h)\le\frac2p.
\tag{8}
\]

Also, by Parseval,

\[
\|(1-\Pi_{\le D})G_{W,h}\|_2^2
=
\|G_{W,h}\|_2^2\,
\nu_{W,h}\{d>D\},
\tag{9}
\]

and WI-058 gives the uniform upper bound

\[
\|G_{W,h}\|_2^2\ll(\log w)^2.
\tag{10}
\]

For the full active product there is also the elementary lower bound

\[
\begin{aligned}
\|G_{W,h}\|_2^2
&=
\prod_{p\le w,\ p\mid h}\frac p{p-1}
\prod_{p\le w,\ p\nmid h}\frac p{p-2}\\
&\ge
\prod_{p\le w}\frac p{p-1}
\asymp \log w,
\end{aligned}
\tag{11}
\]

where local admissibility forces `2|h` when `p=2`, and `p/(p-2)>=p/(p-1)` for `p>=3`. Deleting finitely many pinned local primes changes only the implicit constant in (11).

No arithmetic theorem beyond WI-058 and the classical Mertens estimates enters the conductor calculation below.

## 2. A Chernoff bound improves the conductor upper tail to `exp(-K log K + O(K))`

Put

\[
S_w(a):=\frac{\log d(a)}{\log w}
=\sum_{p\le w} I_p(a)\frac{\log p}{\log w}.
\tag{12}
\]

For `t>0`, independence and (8) give

\[
\begin{aligned}
\mathbb E_\nu e^{tS_w}
&=
\prod_{p\le w}
\left(1+\theta_p(h)
\left(e^{t\log p/\log w}-1\right)\right)\\
&\le
\exp\!\left(
2\sum_{p\le w}
\frac{e^{t\log p/\log w}-1}{p}
\right).
\end{aligned}
\tag{13}
\]

For `0<=u<=1`, convexity of `u -> e^(tu)-1` gives the chord bound

\[
e^{tu}-1\le u(e^t-1).
\tag{14}
\]

Hence, with

\[
C_w:=\frac1{\log w}\sum_{p\le w}\frac{\log p}{p}
=1+O\!\left(\frac1{\log w}\right)
\tag{15}
\]

by Mertens,

\[
\boxed{
\mathbb E_\nu e^{tS_w}
\le
\exp\bigl(2C_w(e^t-1)\bigr).
}
\tag{16}
\]

Chernoff therefore yields, for every `K>0`,

\[
\nu_{W,h}\{d>w^K\}
=\Pr(S_w>K)
\le
\exp\bigl(2C_w(e^t-1)-tK\bigr).
\tag{17}
\]

When `K>2C_w`, choose

\[
t=\log\frac{K}{2C_w}.
\tag{18}
\]

Then

\[
\boxed{
\nu_{W,h}\{d>w^K\}
\le
\exp\!\left(
-K\log\frac{K}{2C_w}+K-2C_w
\right).
}
\tag{19}
\]

In particular, uniformly in every locally admissible `h`, for `K>=3` and large `w`,

\[
\boxed{
\nu_{W,h}\{d>w^K\}
\le
\exp(-K\log K+O(K)).
}
\tag{20}
\]

This is materially sharper than WI-058's first-moment/Markov bound `O(e^-K)`. It uses no stronger prime input: the improvement comes solely from exploiting the exact product law rather than only one small positive moment.

## 3. Every fixed exponent leaves a positive relative `L^2` tail

The opposite direction is just as important. Fix any constant `K>0`. Because of the lower inequality in (8), couple the variables `I_p` with independent Bernoulli variables

\[
J_p\sim\operatorname{Bernoulli}(1/p)
\tag{21}
\]

so that `I_p>=J_p` for every active prime.

Choose an integer `m>K`, and then choose `a` with

\[
\frac Km<a<1.
\tag{22}
\]

Fix pairwise disjoint exponent intervals

\[
a<a_1<b_1<a_2<b_2<\cdots<a_m<b_m<1.
\tag{23}
\]

For each `j`, let `E_j` be the event that at least one prime

\[
w^{a_j}<p\le w^{b_j}
\tag{24}
\]

has `J_p=1`. The prime sets are disjoint, so the events are independent. Mertens' product theorem gives

\[
\begin{aligned}
\Pr(E_j)
&=1-
\prod_{w^{a_j}<p\le w^{b_j}}
\left(1-\frac1p\right)\\
&\longrightarrow
1-\frac{a_j}{b_j}
>0.
\end{aligned}
\tag{25}
\]

On the intersection of all the `E_j`, one obtains `m` distinct selected primes and therefore

\[
\log d
\ge
\sum_{j=1}^m a_j\log w
>
ma\log w
>K\log w.
\tag{26}
\]

Consequently there is a constant `c_K>0`, depending only on the chosen fixed intervals, such that

\[
\boxed{
\liminf_{w\to\infty}
\nu_{W,h}\{d>w^K\}
\ge c_K>0
}
\tag{27}
\]

uniformly in the locally admissible shifts for which the local prime ranges in (23) remain active. In the live Yang power-coefficient regime the dominant bases are distinct primes much larger than `w`, so the full small-prime product is active. Removing finitely many pinned local primes also leaves (25)--(27) unchanged asymptotically.

Equation (27) is not a statement that the high-conductor modes dominate. It says something more precise and sufficient for the present gate: **no fixed power `w^K` captures `1-o(1)` of the normalized Fourier energy.**

## 4. Relative `L^2` capture has an exact qualitative threshold

Combining (20) and (27) gives a clean criterion for cutoffs of the form

\[
D_w=w^{K(w)}.
\tag{28}
\]

If

\[
K(w)\to\infty,
\tag{29}
\]

then (20) implies

\[
\frac{\|(1-\Pi_{\le D_w})G_{W,h}\|_2^2}
{\|G_{W,h}\|_2^2}
=
\nu_{W,h}\{d>D_w\}
\to0.
\tag{30}
\]

Conversely, if `K(w)` does not tend to infinity, there is a subsequence on which `K(w)<=K_0` for some fixed `K_0`; monotonicity plus (27) then gives a positive lower bound for the relative discarded energy on that subsequence. Thus, on the full active product,

\[
\boxed{
\nu_{W,h}\{d>w^{K(w)}\}\to0
\quad\Longleftrightarrow\quad
K(w)\to\infty.
}
\tag{31}
\]

The implication relevant to the Yang repair is the necessary half: an asymptotically lossless raw spectral truncation needs a **growing exponent**. Fixed `K` is not enough.

## 5. A much smaller explicit cutoff makes the absolute tail `o(1)`

For the covariance bookkeeping one often wants the discarded local-main norm itself, not just its relative fraction, to vanish. Combining (10) and (20),

\[
\|(1-\Pi_{\le w^K})G_{W,h}\|_2^2
\ll
(\log w)^2
\exp(-K\log K+O(K)).
\tag{32}
\]

Let

\[
L:=\log\log w,
\qquad
L_2:=\log\log\log w,
\tag{33}
\]

and fix `eta>0`. Choose

\[
K(w)=\frac{(2+\eta)L}{L_2}.
\tag{34}
\]

Then

\[
K\log K=(2+\eta+o(1))L,
\tag{35}
\]

while `(log w)^2=e^(2L)`. Therefore (32) gives

\[
\boxed{
\|(1-\Pi_{\le D_w})G_{W,h}\|_2^2=o(1),
}
\tag{36}
\]

with `D_w` as in (2). This replaces WI-058's sufficient choice

\[
K=3\log\log w
\tag{37}
\]

by a value smaller by a factor asymptotic to `log log log w`.

The constant `2` in (34) comes from the **uniform upper bound** `(log w)^2` for the total local-main energy. It is not asserted to be optimal for a fixed shift family. No matching lower theorem for the smallest absolute-`L^2` cutoff is claimed.

## 6. Translation to the Shao--Teräväinen scale kills the fixed-polylog shortcut

Shao--Teräväinen's small-prime approximant uses

\[
w=(\log X)^C
\tag{38}
\]

for a fixed constant `C` determined by the desired fixed-complexity/log-saving parameters. A fixed polylogarithmic Fourier-conductor cutoff

\[
D_X=(\log X)^B
\tag{39}
\]

with fixed `B` is therefore exactly

\[
D_X=w^{B/C}.
\tag{40}
\]

Equation (27) applies with the fixed exponent `K=B/C`, so

\[
\boxed{
\liminf
\frac{\|(1-\Pi_{\le(\log X)^B})G_{W,h}\|_2^2}
{\|G_{W,h}\|_2^2}
>0.
}
\tag{41}
\]

Using (11), in the full active Yang power-coefficient regime one even has

\[
\boxed{
\|(1-\Pi_{\le(\log X)^B})G_{W,h}\|_2^2
\gg_{B,C}\log w,
}
\tag{42}
\]

along a sufficiently large tail. Thus the discarded **absolute** deterministic local-main energy does not merely fail to be `o(1)`; it grows.

This directly rules out the following cheap repair of WI-057:

1. project the `W`-local conditioning weight onto conductors `d<=(log X)^B` for one fixed `B`;
2. prove or import twisted control only for those fixed-polylog modes;
3. discard all remaining modes using the `L^2` norm of the deterministic local main.

Step 3 is false at the required scale, even before any prime-pair error is considered.

The sharpened sufficient cutoff (2) translates through (38) to (3), which remains far below every fixed positive power `X^epsilon`. Hence the negative result does **not** restore a power-modulus obstruction. It identifies a narrower intermediate regime: larger than every fixed polylog, but still subpolynomial by a wide margin.

## 7. Relation to the printed MRT interface

Matomäki--Radziwiłł--Tao, *Correlations of the von Mangoldt and higher divisor functions I. Long shift ranges* (Proc. LMS 118 (2019), arXiv:1707.01315), is the long-shift pair-correlation source used in the Yang route and audited in WI-034/WI-037/WI-041--WI-043.

In its circle-method setup, Section 3 takes the major-arc denominator parameter

\[
Q=\log^B X
\tag{43}
\]

with `B` a sufficiently large **fixed** constant depending on fixed target parameters; Proposition 3.4 and the later Dirichlet-polynomial estimates retain the same fixed-`B` interface. The paper does not state a theorem uniform for an exponent `B=B(X)->infinity`.

Primary source:

- https://arxiv.org/abs/1707.01315

This matters only as an interface audit. Equation (41) says that a proof which first truncates the `W`-local pair main to the printed MRT fixed-polylog denominator range cannot make the complement negligible by raw `L^2`. It does **not** prove that MRT's methods cannot be extended, nor that another dispersion/large-sieve theorem cannot control the needed slowly growing or subpolynomial conductor range.

Likewise there is no contradiction with WI-054. Shao--Teräväinen nilsequence Bombieri--Vinogradov has a much larger modulus range and already controls the complete analytic nonzero-frequency residual in the doubly-small exponent region identified there. The live one-sided obstruction is the **conditioned pair-error covariance** isolated by WI-057, not the mere existence of small-conductor single-prime twists.

## 8. Prior-art and novelty audit

The ingredients used after WI-058 are classical:

- Mertens' estimates `sum_(p<=w) log p/p = log w + O(1)` and `prod_(p<=x)(1-1/p) ~ e^-gamma/log x`;
- Chernoff/Markov exponential-moment bounds;
- independent Bernoulli `1/p` prime-divisor models of Kubilius/Erdos--Kac type;
- the fixed-polylog major-arc decomposition in the cited MRT paper.

A targeted search around Kubilius prime-divisor models, Poisson laws for prime factors, Mertens-product large deviations, and the MRT major-arc denominator range found the expected classical probabilistic-number-theory background. No novelty is claimed for any of those ingredients. Kevin Ford's work on joint Poisson distributions of prime factors, for example, explicitly uses the Kubilius independent-prime-factor paradigm; that literature is conceptual prior art rather than a theorem needed here.

The Mathia contribution recorded by this finding is the **source-specific consequence** of the exact WI-058 Fourier-energy law: apply the classical product-model machinery to the actual normalized `W`-local pair main, derive the two-sided cutoff behavior (20)/(27), and use it to separate a fixed-polylog truncation (provably insufficient in raw `L^2`) from a slowly growing super-polylogarithmic cutoff (sufficient, with the quantitative improvement (2)). Absence of this exact source-specific formulation in the searched literature is not a priority claim.

## 9. What this changes in the live Yang welding problem

WI-057 showed that ordinary marginal MRT control cannot simply be multiplied by the `W`-local all-main pair because the latter retains periodic modes. WI-058 then showed that those modes have exponentially concentrated Fourier **conductor energy**, reducing the frightening full period `W` to an effective subpolynomial spectrum.

The present result makes that reduction nearly scale-exact for relative `L^2`:

\[
\boxed{
\text{fixed }w^K\text{ cutoff: insufficient;}
\qquad
K(w)\to\infty:\text{ sufficient for relative capture.}
}
\tag{44}
\]

For a uniform absolute-`L^2` truncation, (34) gives a concrete target much smaller than WI-058's first cutoff. Therefore the missing theorem interface is no longer well described as either “all `W`-periodic modes” or “only fixed-polylog twists.” A source-faithful repair has three remaining forms:

1. prove the conditioned/twisted shifted-prime estimate, with the required square-function normalization, for conductors extending into the slowly growing super-polylogarithmic regime;
2. prove a covariance-specific estimate showing that the actual companion pair error is negligible on the high-conductor local-main tail, so that the deterministic tail need not be discarded by its own norm;
3. find an exact source identity/cancellation that annihilates the relevant retained modes before a generic twisted theorem is needed.

A proof must still avoid the across-family Cauchy floor of WI-042. Bounding each retained character separately and then summing absolute values is not licensed merely because each individual conductor is small.

## 10. Decisive audit and continuation gate

Narrow or withdraw this finding if any of the following fails.

1. Recheck the exact WI-058 Bernoulli law and the inequalities `1/p <= theta_p <= 2/p` for every active local prime.
2. Verify the exponential-moment identity (13) and the convex chord inequality (14); no independence beyond WI-058's CRT tensorization may be introduced.
3. Reproduce the Chernoff optimizer (18) and exponent (19), including the Mertens normalization `C_w=1+O(1/log w)`.
4. For the lower bound, verify the monotone coupling with Bernoulli `1/p`, disjointness of the prime ranges, the Mertens ratio in (25), and the implication `sum a_j>K`.
5. Keep the active-prime qualification explicit. The fixed-`K` lower bound needs all but finitely many primes in the chosen exponent bands to remain active; this is satisfied in the dominant Yang power-coefficient regime but must not be asserted for an arbitrary conditioning that deletes a growing set of small primes.
6. Do not infer a twisted pair theorem from the conductor cutoff. The local-main spectral statement and the prime-error covariance statement are different interfaces.
7. Do not infer that every fixed-polylog-based argument is impossible. What is decisively closed is **fixed-polylog projection plus raw deterministic-`L^2` disposal of the complement**.

The next substantive step should attack the source-normalized covariance against the retained additive modes at a growing conductor cutoff, preferably preserving an `ell^2`/square-function structure. A theorem barrier showing that even the reduced scale (2)--(3) is inaccessible with current shifted-prime technology would also be a substantive negative result.
