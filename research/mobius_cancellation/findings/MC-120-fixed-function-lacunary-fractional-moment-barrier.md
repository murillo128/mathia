# MC-120 — One fixed multiplicative comparator defeats sub-L1 transfer on infinitely many lacunary windows

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `DECISIVE-NEGATIVE`, `MATCHED-CONTROL`, `NO-NOVELTY-CLAIM`.

## Claim

Fix `0<p<1`. Choose

\[
\frac34<a<\min\!\left(\frac{p+2}{2(p+1)},0.99\right)
\tag{1}
\]

and

\[
1<\theta<
\theta_*(a,p)
:=
\frac{2-a(p+1)}{1-p/2}.
\tag{2}
\]

Let `epsilon_j>0` be any sequence with `epsilon_j -> 0`. Then there exist a strictly increasing sequence `Q_j -> infinity` and a **single** multiplicative function

\[
f:\mathbb N\to\{-1,0,1\},
\qquad |f(n)|=\mu(n)^2,
\tag{3}
\]

such that, writing

\[
S_f(N)=\sum_{n\le N}f(n),
\qquad
P_{p,f}(X)=
\left(\frac1X\sum_{N<X}|S_f(N)|^p\right)^{1/p},
\qquad
D_{1,f}(X)=\frac1X\sum_{N<X}|S_f(N)|,
\tag{4}
\]

one has for every sufficiently large `j`

\[
\boxed{
P_{p,f}(X)
\ll_{p,a,\theta}
X^{1/2+\epsilon_j}
\qquad
(Q_j\le X\le Q_j^\theta),
}
\tag{5}
\]

uniformly throughout the whole `j`-th polynomial window, while simultaneously

\[
\boxed{
D_{1,f}(Q_j)
\gg_{p,a}
\frac{Q_j^{2a-1}}{\log Q_j}.
}
\tag{6}
\]

Because `a>3/4`, the exponent in `(6)` is strictly larger than `1/2`. Thus the moving-comparator limitation of `MC-119` can be removed on an **infinite sequence of windows**: exact square-free support, exact multiplicativity, one-function consistency, and asymptotically RH-scale fractional `p`-moment control on every cutoff of each window still do not generically recover the RH-complete first absolute mean.

The price is essential in the present construction. The scales `Q_j` are chosen recursively very far apart, in particular so that the next engineered prime block lies above the preceding polynomial window. No bound of the form

\[
\frac{\log Q_{j+1}}{\log Q_j}\to1
\tag{7}
\]

is proved or expected from this argument. Hence this finding does **not** defeat the subpower-dense checkpoint requirement isolated by `MC-116`; rather, it narrows the surviving information to dense/overlapping-scale coherence or to genuinely Möbius-specific arithmetic structure.

## 1. Deterministic recursive prime blocks

Let

\[
H_j=\lfloor Q_j^a\rfloor.
\tag{8}
\]

At scale `Q_j`, use the same balanced terminal-block geometry as `MC-118`--`MC-119`. Inside `(Q_j-H_j,Q_j]`, choose equal-sized prime sets `P_{j,+}` and `P_{j,-}` in separated thirds and prescribe signs `+1` and `-1`, respectively. By the short-interval prime theorem `MC-S32`, for sufficiently large `Q_j` one can arrange

\[
|P_{j,+}|=|P_{j,-}|=:L_j
\asymp\frac{H_j}{\log Q_j}.
\tag{9}
\]

Define the cumulative signed block

\[
B_j(y)=
\sum_{\substack{q\in P_{j,+}\cup P_{j,-}\\q\le y}}b_q,
\qquad
b_q\in\{+1,-1\}.
\tag{10}
\]

It has a plateau of height `L_j` and width comparable with `H_j`, but the block is exactly balanced:

\[
\sum_{q\in P_{j,+}\cup P_{j,-}}b_q=0.
\tag{11}
\]

The scales are chosen recursively and **before** any random prime signs are sampled. Besides the analytic conditions imposed below, require

\[
Q_{j+1}-Q_{j+1}^a>Q_j^\theta.
\tag{12}
\]

Thus every future engineered prime block lies completely above every earlier controlled window.

Let

\[
A_j=\bigcup_{i\le j}(P_{i,+}\cup P_{i,-}),
\qquad
r_j=|A_j|,
\qquad
C_j=2^{r_{j-1}}.
\tag{13}
\]

At stage `j`, `C_j` is finite and depends only on already chosen deterministic blocks. We are free to take `Q_j` large enough to absorb it.

## 2. One global multiplicative function

After the entire deterministic block sequence has been fixed, assign independent Rademacher signs `epsilon_q in {+1,-1}` to every prime outside

\[
A_\infty=\bigcup_{j\ge1}(P_{j,+}\cup P_{j,-}).
\tag{14}
\]

Define `f` on primes by the prescribed block sign on `A_infinity` and by `epsilon_q` elsewhere, set

\[
f(q^k)=0\qquad(k\ge2),
\tag{15}
\]

and extend multiplicatively. Then `(3)` holds identically.

For a fixed stage `j`, define an auxiliary background `g_j` by zeroing the current block `P_{j,+} union P_{j,-}` while retaining all older prescribed prime signs and all random signs. Future prescribed primes do not occur below `Q_j^theta` by `(12)`. Write

\[
G_j(N)=\sum_{n\le N}g_j(n).
\tag{16}
\]

Since every admissible `theta` in `(2)` is `<2`, the window lies below `(Q_j-H_j)^2` for large `j`. Hence an integer in the window contains at most one current-block prime, and the exact transport identity from `MC-118` remains valid:

\[
\boxed{
S_f(N)=G_j(N)+R_j(N),
\qquad
R_j(N)=\sum_{m\ge1}g_j(m)B_j(N/m).
}
\tag{17}
\]

Older engineered primes may divide `m`; this does not change the identity and the transport estimate below uses only `|g_j(m)|<=1`.

## 3. The current block remains subcritical throughout its window

For `0<p<1`, subadditivity and the exact balance `(11)` give exactly the same counting bound as `MC-119`:

\[
\sum_{N<X}|R_j(N)|^p
\ll
L_j^p\left(
H_j\left(\frac X{Q_j}\right)^2+rac X{Q_j}
\right)
\tag{18}
\]

uniformly for `X<(Q_j-H_j)^2`.

The exponent audit in `MC-119` depends only on `(1)`--`(2)`. Therefore there is a fixed `delta=delta(p,a,theta)>0` such that

\[
\sum_{N<X}|R_j(N)|^p
\ll
Q_j^{-\delta}X^{1+p/2}
\qquad
(Q_j\le X\le Q_j^\theta).
\tag{19}
\]

Thus all accumulation from previous stages is confined to the background `G_j`; the new balanced block itself continues to cost strictly less than the square-root `p`-moment budget.

## 4. Old deterministic prime signs cost only a finite stage constant

The random signs in `g_j` are no longer independent at **all** primes because the finitely many old engineered primes are fixed. Nevertheless their effect can be bounded by the crude finite constant `C_j`.

Every square-free `n` can be written uniquely as

\[
n=d m,
\tag{20}
\]

where all prime factors of `d` lie in `A_{j-1}` and all prime factors of `m` lie outside `A_{j-1}` and outside the current zeroed block. Grouping the sum `(16)` by the random part `m` gives

\[
G_j(N)=\sum_m \epsilon(m) A_{j,N}(m),
\tag{21}
\]

where distinct square-free `m` carry orthogonal Rademacher monomials and

\[
|A_{j,N}(m)|\le 2^{r_{j-1}}=C_j.
\tag{22}
\]

Consequently

\[
\mathbb E|G_j(N)|^2
=
\sum_m |A_{j,N}(m)|^2
\le C_j^2N,
\tag{23}
\]

and, since `0<p<2`,

\[
\mathbb E|G_j(N)|^p
\le C_j^p N^{p/2}.
\tag{24}
\]

Hence

\[
\mathbb E\sum_{N<X}|G_j(N)|^p
\ll_p C_j^pX^{1+p/2}.
\tag{25}
\]

This bound is intentionally crude. Its only role is to show that previously prescribed prime blocks create a **finite** loss at each stage, which can be swallowed by moving the next scale far enough out.

## 5. A single random realization works on all infinitely many windows

Choose positive numbers `eta_j` with

\[
\sum_{j\ge1}2\eta_j<1;
\tag{26}
\]

for example `eta_j=2^{-j-4}`. On the `j`-th window use a dyadic mesh of size

\[
K_j=O_\theta(\log Q_j).
\tag{27}
\]

Markov's inequality applied to `(25)`, followed by a union bound over the mesh, shows that with failure probability at most `eta_j`,

\[
\sum_{N<X}|G_j(N)|^p
\ll_p
C_j^p\frac{K_j}{\eta_j}X^{1+p/2}
\tag{28}
\]

at every mesh point. Monotonicity of the cumulative `p`-mass fills the intervening cutoffs at a fixed constant cost.

Because `C_j`, `eta_j`, and the previously chosen blocks are all fixed before `Q_j` is chosen, enlarge `Q_j` until

\[
C_j\left(\frac{K_j}{\eta_j}\right)^{1/p}
\le Q_j^{\epsilon_j}/10.
\tag{29}
\]

Combining `(19)` and `(28)` then gives `(5)` on the whole window whenever this stage event holds.

The same realization must preserve the deterministic plateau excursion. On the plateau of `B_j`, the term `m=1` is the only possible current-block multiplier at `N<Q_j`, so

\[
R_j(N)=L_j.
\tag{30}
\]

By `(23)`, the expected absolute background mass across a plateau of length `asymp H_j` satisfies

\[
\mathbb E\sum_{N\in\mathrm{plateau}}|G_j(N)|
\ll H_jC_j\sqrt{Q_j}.
\tag{31}
\]

The deterministic signal mass is

\[
\asymp H_jL_j
\asymp\frac{H_j^2}{\log Q_j}.
\tag{32}
\]

Since `a>1/2`, we may enlarge `Q_j` again so that

\[
C_jQ_j^{1/2-a}\log Q_j
\ll\eta_j.
\tag{33}
\]

A final Markov bound then makes the probability that the background erases more than half of the plateau signal at most `eta_j`.

Thus the total stage-`j` failure probability is at most `2 eta_j`. No independence between different stage events is required. By `(26)` and the countable union bound, the probability that **any** stage fails is strictly less than one. Therefore at least one global assignment of all unprescribed prime signs satisfies every stage simultaneously. Fix such an assignment. The resulting deterministic multiplicative function is the single `f` in `(3)`.

On every source plateau for this fixed realization,

\[
\sum_{N<Q_j}|S_f(N)|
\gg H_jL_j,
\tag{34}
\]

and division by `Q_j` proves `(6)`.

## Prior-art and novelty assessment

The comparator class and its ingredients are established territory. `MC-S16` studies square-free-supported multiplicative sign functions and proves unbounded discrepancy for the full class. Random multiplicative functions obtained from independent prime signs have a large literature, while conditioning or prescribing prime values is also a standard probabilistic operation. `MC-S32` supplies the only non-elementary arithmetic input used here: enough primes in each short terminal slab.

A targeted literature check around random multiplicative partial sums, conditioned/prescribed prime values, and square-free-supported multiplicative discrepancy found adjacent results on random-model fluctuations, sign changes, conditional prime assignments, and discrepancy, but no theorem is needed for `(21)`--`(34)`: the argument uses only Rademacher orthogonality, Markov's inequality, a countable union bound, and the balanced-block transport already derived in `MC-118`--`MC-119`.

Accordingly **no external novelty claim is made**. The durable value is narrower: it closes a specific internal escape left open by `MC-119`, namely that its comparator changed with the source scale.

## Boundaries and failure modes

The construction is deliberately **lacunary**. The crude old-block cost `C_j=2^{r_{j-1}}` is absorbed by choosing `Q_j` arbitrarily large. This proves existence of one fixed comparator but gives no useful upper bound on consecutive scale ratios and certainly does not establish the subpower-dense condition `(7)`.

The result therefore does not obstruct a theorem that uses one-function consistency at a dense logarithmic sequence of scales, overlapping windows, or another quantitative cross-scale relation that prevents old coherent blocks from being hidden by moving far enough into the future.

The fixed comparator also does not reproduce Möbius's exact prime law `mu(q)=-1`. Exact square-free support, multiplicativity, and exact agreement at every prime would identify Möbius tautologically, so the relevant open target remains an **intermediate quantitative** condition rather than exact source specification.

Nor does this construction preserve the known quantitative Chowla information of Möbius. It therefore leaves open a genuinely joint correlation-plus-multiplicativity transfer in which correlations constrain how coherent prime blocks can recur across scales.

Finally, the obstruction remains specific to `0<p<1`. At `p=1`, the source statistic is already the first absolute mean and there is no fractional-moment information-loss gap.

## Consequence for the active mean-absolute transfer route

`MC-117` showed that sub-`L^1` moments lose rare coherent amplitude. `MC-118` showed that generic multiplicativity can transport such an excursion. `MC-119` showed that the weak statistic may remain controlled at every cutoff throughout a polynomial future window.

The present finding removes the next obvious repair: **requiring the same multiplicative function to exhibit this behavior at infinitely many source scales is still insufficient when those scales may be very far apart.** The source-specific frontier is therefore sharper. A viable transfer must exploit at least one feature absent here: subpower-dense/overlapping-scale coherence, a quantitatively strong joint multiplicativity-correlation law, or another Möbius-specific arithmetic constraint that forbids coherent balanced blocks without merely specifying Möbius itself.