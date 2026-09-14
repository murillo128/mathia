# AF-348 — Riesz smoothing erases power-background locality uniformly across moving cutoffs

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `ZERO-SENSITIVE-SOURCE`, `SOURCE-COMPLEXITY-CONSERVATION`, `STRENGTHENING`, `NO-NOVELTY-CLAIM`

## Claim

AF-347 proves on the exact-power subsequence `X=M^k` that a fixed order of classical Riesz smoothing progressively erases the visible locality defect of the weighted perfect-`k`-power background

\[
b_k(n):=
\begin{cases}
 k m^{k-1},&n=m^k\text{ with }m\ge2,\\
 0,&\text{otherwise},
\end{cases}
\qquad k\ge2.
\tag{1}
\]

The exact-power restriction is unnecessary.

Fix integers `k>=2` and `r>=0`. For every real `X>=1`, define

\[
\mathcal R_{k,r}(X)
:=
\sum_{n\le X}b_k(n)
\left(1-\frac nX\right)^r.
\tag{2}
\]

Then, uniformly as `X->infinity`,

\[
\boxed{
\mathcal R_{k,r}(X)
=
\frac{X}{r+1}
+
O_{k,r}\!\left(
X^{\max\{1-(r+1)/k,\,0\}}
\right).
}
\tag{3}
\]

Consequently,

\[
\boxed{
r\ge k-1
\quad\Longrightarrow\quad
\mathcal R_{k,r}(X)
=
\frac{X}{r+1}+O_{k,r}(1)
}
\tag{4}
\]

for **all** large real cutoffs `X`, not merely for `X=M^k`.

The same main term is carried by dense unit mass. Put

\[
\mathcal U_r(X)
:=
\sum_{1\le n\le X}
\left(1-\frac nX\right)^r.
\tag{5}
\]

Then

\[
\mathcal U_r(X)=\frac{X}{r+1}+O_r(1),
\tag{6}
\]

and therefore

\[
\boxed{
\mathcal R_{k,r}(X)-\mathcal U_r(X)
=
O_{k,r}\!\left(
X^{\max\{1-(r+1)/k,\,0\}}
\right).
}
\tag{7}
\]

In particular,

\[
\boxed{
r\ge k-1
\quad\Longrightarrow\quad
\mathcal R_{k,r}(X)-\mathcal U_r(X)=O_{k,r}(1)
}
\tag{8}
\]

uniformly across the entire cutoff axis.

Thus AF-347's locality-loss mechanism is not a favorable-subsequence artifact. Once the smoothing order reaches `k-1`, the polynomially smoothed mass observable has only bounded sensitivity to whether the order-`X` source mass came from a dense unit background or from the sparse, high-amplitude perfect-`k`-power background, even while their raw support geometry remains radically different.

The fidelity conclusion strengthens accordingly:

\[
\boxed{
\text{finite smoothing can destroy a source locality resource uniformly, not merely at aligned cutoffs.}
}
\tag{9}
\]

## Derivation

### 1. Separate the moving terminal cell

Write

\[
y:=X^{1/k},
\qquad
M:=\lfloor y\rfloor,
\qquad
\delta:=y-M\in[0,1),
\qquad
q:=\frac{M}{y}.
\tag{10}
\]

For large `X`, `q` stays uniformly bounded away from zero and

\[
1-q^k
=
1-\left(1-\frac{\delta}{y}\right)^k
=O_k(y^{-1}).
\tag{11}
\]

Temporarily restore the harmless `m=1` term:

\[
\widetilde{\mathcal R}_{k,r}(X)
:=
k\sum_{m=1}^{M}
 m^{k-1}
\left(1-\frac{m^k}{y^k}\right)^r.
\tag{12}
\]

Since

\[
\widetilde{\mathcal R}_{k,r}(X)-\mathcal R_{k,r}(X)
=
k(1-X^{-1})^r
=O_k(1),
\tag{13}
\]

it suffices to prove `(3)` for `(12)`.

Expanding the smoothing polynomial gives

\[
\widetilde{\mathcal R}_{k,r}(X)
=
k\sum_{j=0}^{r}
(-1)^j\binom rj y^{-kj}
\sum_{m=1}^{M}m^{d_j},
\qquad
d_j:=k(j+1)-1.
\tag{14}
\]

### 2. The leading Faulhaber term already contains the terminal-cell error

For each integer `d>=1`, write the exact Faulhaber polynomial as

\[
\sum_{m=1}^{M}m^d
=
\sum_{\ell=0}^{d}c_\ell(d)M^{d+1-\ell},
\tag{15}
\]

where

\[
c_0(d)=\frac1{d+1},
\tag{16}
\]

and, for every fixed `ell>=1`, `c_ell(d)` is a polynomial in `d` of degree at most `ell-1` on the range where that coefficient is present. This is the standard Bernoulli/Faulhaber expansion.

Take first `ell=0`. Its contribution to `(14)` is

\[
\begin{aligned}
E_0
&=
y^k q^k
\sum_{j=0}^{r}
\frac{(-1)^j}{j+1}\binom rj q^{kj}\\
&=
\frac{y^k}{r+1}
\left[1-(1-q^k)^{r+1}\right].
\end{aligned}
\tag{17}
\]

The second identity follows by integrating `(1-z)^r` from `0` to `z=q^k`.

Since `X=y^k`, equations `(11)` and `(17)` give

\[
E_0-rac{X}{r+1}
=
-\frac{y^k}{r+1}(1-q^k)^{r+1}
=
O_{k,r}(y^{k-r-1}).
\tag{18}
\]

This is precisely the moving-terminal-cell contribution. At an exact power, `delta=0`, so it vanishes identically; away from exact powers it has exactly the same scale as the first unsmoothed discrepancy budget in AF-347 after `r` smoothing orders.

### 3. A binomial divisibility lemma replaces exact-cutoff cancellation

The remaining positive-power Faulhaber terms no longer cancel identically when `q!=1`, but they acquire enough vanishing in `1-q^k` to preserve the same bound.

Let `P` be a polynomial of degree at most `m<=r`. Then

\[
F_P(z)
:=
\sum_{j=0}^{r}
(-1)^j\binom rj P(j)z^j
\tag{19}
\]

is divisible by

\[
(1-z)^{r-m}.
\tag{20}
\]

Indeed, expand `P(j)` in the falling-factorial basis `j^{\underline h}`, `0<=h<=m`. Differentiating

\[
(1-z)^r
=
\sum_{j=0}^{r}(-1)^j\binom rj z^j
\tag{21}
\]

`h` times and multiplying by `z^h` gives

\[
\sum_{j=0}^{r}
(-1)^j\binom rj j^{\underline h}z^j
=
(-1)^h r^{\underline h}z^h(1-z)^{r-h}.
\tag{22}
\]

Every basis term therefore contains at least `(1-z)^{r-m}`, proving `(20)`.

This is the moving-cutoff version of AF-347's finite-difference cancellation: at `z=1` the expression vanishes exactly; near `z=1` it vanishes to a controlled order.

### 4. Every positive-power Faulhaber correction obeys the same envelope

Fix `1<=ell<k`. Since

\[
d_j\ge k-1\ge\ell
\tag{23}
\]

for every `j=0,...,r`, the `ell`-th Faulhaber coefficient occurs throughout the binomial sum. Its contribution is

\[
E_\ell
=
k y^{k-\ell}q^{k-\ell}
\sum_{j=0}^{r}
(-1)^j\binom rj
c_\ell(d_j)(q^k)^j.
\tag{24}
\]

Because `d_j` is affine in `j` and `c_ell(d)` has degree at most `ell-1`, the polynomial

\[
P_\ell(j):=c_\ell(d_j)
\tag{25}
\]

has degree at most `ell-1`.

If `ell<=r+1`, the lemma with `m=ell-1` shows that the sum in `(24)` is divisible by

\[
(1-q^k)^{r-\ell+1}.
\tag{26}
\]

Using `(11)`,

\[
E_\ell
=
O_{k,r}\left(
 y^{k-\ell}y^{-(r-\ell+1)}
\right)
=
O_{k,r}(y^{k-r-1}).
\tag{27}
\]

If instead `ell>r+1`, no vanishing is needed: the finite binomial sum is bounded for fixed `k,r`, and

\[
E_\ell
=O_{k,r}(y^{k-\ell})
=O_{k,r}(y^{k-r-2}).
\tag{28}
\]

Therefore, when `r<=k-2`, every positive-power correction is

\[
O_{k,r}(y^{k-r-1}).
\tag{29}
\]

When `r>=k-1`, every `ell<k` lies in the first case and `(27)` is `O_{k,r}(1)` because `k-r-1<=0`.

Finally, every Faulhaber term with `ell>=k` carries the prefactor

\[
y^{k-\ell}=O(1).
\tag{30}
\]

Some such terms are absent for the smallest `d_j`, but only finitely many fixed coefficients occur; with `q` bounded, their total contribution is still `O_{k,r}(1)`.

Combining `(18)` and `(27)`--`(30)` yields

\[
\widetilde{\mathcal R}_{k,r}(X)
=
\frac{X}{r+1}
+
O_{k,r}\!\left(
 y^{\max\{k-r-1,0\}}
\right).
\tag{31}
\]

Since `y=X^{1/k}`, this is exactly `(3)` after restoring `(13)`.

### 5. Dense unit mass remains a bounded-error control for arbitrary cutoffs

Let `N:=floor X`. Expanding `(5)` gives

\[
\mathcal U_r(X)
=
\sum_{j=0}^{r}
(-1)^j\binom rj X^{-j}
\sum_{n=1}^{N}n^j.
\tag{32}
\]

The same Faulhaber argument, now with `N=X+O(1)`, gives

\[
\mathcal U_r(X)=\frac{X}{r+1}+O_r(1).
\tag{33}
\]

Equations `(3)` and `(33)` prove `(7)`--`(8)`.

## Relation to AF-344--AF-347

AF-344 constructs the weighted perfect-power backgrounds and proves that their Dirichlet transforms

\[
B_k(s)=k\bigl(\zeta(ks-k+1)-1\bigr)
\tag{34}
\]

have residue one at `s=1` while remaining holomorphic at nontrivial zeta zeros. Subtracting them from the prime layer therefore preserves the right-half-plane RH pole discriminator even though the source sign/locality geometry changes drastically.

AF-345 identifies prime-gap occupancy and gap-mass concentration as the exact sign currency for nonnegative backgrounds. AF-346 shows that fixed `k>=3` power backgrounds attain the resulting concentration exponent. Those results locate the source complexity that sign count fails to retain.

AF-347 then shows that a later Riesz compression can itself erase the polynomial visibility of that source locality, but states the clean bound only on `X=M^k`. Its explicit boundary section leaves arbitrary cutoffs as a separate quantitative question.

AF-348 closes that question. The terminal fractional cell does not restore fidelity. Exact finite-difference annihilation at aligned cutoffs deforms into **high-order vanishing** in `1-(floor(X^{1/k})/X^{1/k})^k`; that vanishing is exactly strong enough to keep the AF-347 exponent uniformly.

The obstruction is therefore stronger than a subsequence counterexample: for every fixed `k`, smoothing order `k-1` makes the sparse power background and dense unit mass bounded-error indistinguishable under this scalar Riesz observable at every sufficiently large cutoff.

## Exact controls and boundaries

### Uniformity is in the cutoff, not in `k` or `r`

The constants in `(3)`--`(8)` may depend on the fixed integers `k` and `r`. No estimate uniform in a growing smoothing order or a growing power degree is claimed.

### The theorem concerns one scalar smoothing family

Bounded-error Riesz indistinguishability does not imply that the underlying coefficient sequences are close pointwise, in support geometry, in prime-gap occupancy, in an `ell^p` norm, or under a different nonlocal operator. The raw support still has cardinality `asymp X^{1/k}`, amplitudes `asymp X^{1-1/k}`, and gaps `asymp X^{1-1/k}` near height `X`.

The result says only that these distinctions are not automatically available after this declared compression.

### Bounded error is not exact equality

For `r>=k-1`, the dense and sparse observables differ by `O(1)`, not necessarily by a quantity tending to zero and not identically. Any destination theorem sensitive to a bounded residual could still distinguish them. A claim of asymptotic loss must therefore state its normalization or stability modulus explicitly.

### No prime-gap theorem is used

As in AF-347, the argument acts directly on the power-supported background. It does not require primes between consecutive powers, Baker--Harman--Pintz, or Legendre's conjecture. The result applies already at `k=2`.

### RH pole fidelity is inherited

Equation `(34)` and its zero-pole audit belong to AF-344. The present theorem does not strengthen that analytic result; it strengthens only the downstream compression statement applied to the same already-audited source family.

### This does not solve the growing-order observation problem

AF-338 concerns fixed-order sign regularity for a different Euler-log sampling operator. AF-348 does not identify the norm consumed by its determinant constants, prove a growing-order extension, or show that Riesz smoothing is the actual final RH destination. Its role is a sharp transport warning: source complexity that is mathematically real can become quantitatively invisible under a later averaging map.

## Prior art and novelty assessment

No novelty claim is made for the constituent mathematics.

- Classical Riesz means use weights of the form `(1-n/X)^r`; AF-347 already records this as standard summability theory.
- NIST DLMF §24.4(iii), especially Eq. 24.4.7, records finite power sums in Bernoulli-polynomial form, and DLMF §2.10(i) records the Euler--Maclaurin framework for the same class of expansions.
- The divisibility lemma `(19)`--`(22)` is standard finite-difference/binomial calculus: an alternating binomial transform of a degree-`m` polynomial acquires an `(r-m)`-fold zero at `z=1`.

A targeted search around Riesz means, Euler--Maclaurin/Faulhaber expansions, and finite-difference weighted power sums did not identify a standard theorem organized around this exact weighted perfect-power source and the uniform threshold `r=k-1`. Search failure is not evidence of novelty. AF-348 is classified as a strengthening of the Arithmetic Fidelity synthesis in AF-347, not as a new theorem of summability theory.

## Consequence for Arithmetic Fidelity

AF-347 left open a possible escape: perhaps the severe smoothing collapse occurred only because the cutoff was synchronized with the sparse support. AF-348 removes that escape.

The terminal-cell misalignment contributes at the same scale as the already-budgeted post-smoothing discrepancy, and the lower Faulhaber corrections inherit enough binomial vanishing to stay inside that envelope. Therefore no generic choice of cutoff recovers polynomial sensitivity once `r>=k-1`.

For this family, the source/destination accounting is now sharper:

\[
\text{raw sparse locality}
\;\xrightarrow{\text{fixed Riesz order }r\ge k-1}\;
\text{dense-mass observable}+O(1)
\tag{35}
\]

uniformly in the cutoff.

Any proposed arithmetic-fidelity theorem that relies on support sparsity, amplitude concentration, or source-gap geometry must therefore include an explicit **transport statement** through the actual downstream operator. It is not enough that the source possesses the resource, and it is not enough to exclude one aligned subsequence where the resource disappears. The relevant requirement is that the destination retain the discriminator with a quantitative modulus on the full observation regime.