# AF-214 — Prouhet simple-integer clusters have arbitrary-order Euler flatness

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-CONTROL`, `QUANTITATIVE-RECOVERY`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-182 showed that positive generalized-prime clusters with binomial multiplicities can annihilate arbitrarily many low-order source moments, producing arbitrarily high fixed-band Euler flatness. That leaves a natural arithmetic escape: rational primes are simple generators, so perhaps the instability depends on repeated generalized-prime multiplicity or non-unit cluster weights.

It does not. The classical Prouhet–Thue–Morse partition produces the same arbitrary-order cancellation using **two sets of distinct consecutive integers with unit multiplicity**.

Fix an integer cancellation order

\[
m\ge 1,
\tag{1}
\]

and write

\[
\varepsilon_j:=(-1)^{s_2(j)},
\qquad
0\le j<2^m,
\tag{2}
\]

where `s_2(j)` is the binary digit sum. Define the two Prouhet classes

\[
A_m:=\{0\le j<2^m:\varepsilon_j=+1\},
\qquad
B_m:=\{0\le j<2^m:\varepsilon_j=-1\}.
\tag{3}
\]

They are disjoint, contain exactly `2^{m-1}` elements each, and Prouhet's theorem gives

\[
\boxed{
\sum_{a\in A_m}a^r
=
\sum_{b\in B_m}b^r,
\qquad r=0,1,\ldots,m-1.
}
\tag{4}
\]

Consequently, after translation by any integer `N\ge2`, the simple integer generator clusters

\[
\mathcal A_{m,N}:=\{N+a:a\in A_m\},
\qquad
\mathcal B_{m,N}:=\{N+b:b\in B_m\}
\tag{5}
\]

still match every norm-coordinate polynomial moment below order `m`.

Let

\[
G_s(q):=-\log(1-q^{-s})
=
\sum_{k\ge1}\frac{q^{-ks}}k,
\qquad \Re s>0,
\tag{6}
\]

be the analytic logarithm of one Euler factor. For fixed `sigma>0` and finite vertical bandwidth `T`, define the exact cluster Euler discrepancy

\[
D_{m,N}(\sigma,T)
:=
\sup_{|t|\le T}
\left|
\sum_{a\in A_m}G_{\sigma+it}(N+a)
-
\sum_{b\in B_m}G_{\sigma+it}(N+b)
\right|.
\tag{7}
\]

Put

\[
H_m:=\prod_{r=0}^{m-1}2^r
=2^{m(m-1)/2}.
\tag{8}
\]

Then there are finite constants `0<c_{m,\sigma}\le C_{m,\sigma,T}<\infty`, independent of `N`, such that

\[
\boxed{
 c_{m,\sigma}N^{-(\sigma+m)}
\le
D_{m,N}(\sigma,T)
\le
C_{m,\sigma,T}N^{-(\sigma+m)}.
}
\tag{9}
\]

More explicitly,

\[
\boxed{
H_m\,\sigma^{\overline m}(N+2^m-1)^{-(\sigma+m)}
\le D_{m,N}(\sigma,T),
}
\tag{10}
\]

where

\[
\sigma^{\overline m}
=\sigma(\sigma+1)\cdots(\sigma+m-1),
\tag{11}
\]

while, with `S_T=(\sigma^2+T^2)^{1/2}`,

\[
\boxed{
D_{m,N}(\sigma,T)
\le
H_m(m-1)!
\frac{\prod_{r=0}^{m-1}(S_T+r)}{(1-2^{-\sigma})^m}
N^{-(\sigma+m)}.
}
\tag{12}
\]

Thus the order `m` is sharp on this family: at any fixed band the Euler discrepancy is `Theta(N^{-\sigma-m})`, not merely `O(N^{-\sigma-m})`.

The source geometry remains nondegenerate. In absolute norm coordinate, the sorted points of the two clusters pair across adjacent integers, so both the bottleneck distance and the probability-normalized one-dimensional Wasserstein distance equal

\[
\boxed{d_{\rm abs}=W_{1,\rm abs}=1.}
\tag{13}
\]

In logarithmic norm coordinate, the bottleneck distance is exactly

\[
\boxed{
 d_{\log}
 =\log\!\left(1+\frac1N\right)
 \asymp N^{-1},
}
\tag{14}
\]

and the corresponding probability-normalized `W_1` distance is also `Theta(N^{-1})`.

Combining `(9)` and `(14)` gives the sharp family-level scaling

\[
\boxed{
D_{m,N}(\sigma,T)
\asymp
d_{\log}^{\,\sigma+m}
\qquad(N\to\infty)
}
\tag{15}
\]

for every fixed `m,\sigma,T`.

Therefore a source class containing these simple integer clusters for arbitrarily large Prouhet order cannot admit any uniform positive inverse Hölder exponent. If

\[
d_{\log}\le C D^\alpha
\tag{16}
\]

held uniformly for some `\alpha>0`, choose a fixed integer `m` with

\[
\alpha(\sigma+m)>1.
\tag{17}
\]

Then `(9)` and `(14)` contradict `(16)` as `N\to\infty`.

Hence

\[
\boxed{
\text{integrality + distinctness + unit generator multiplicity do not restore any uniform positive inverse Hölder modulus.}
}
\tag{18}
\]

This closes the multiplicity escape left by AF-182. The source obstruction can be realized by two ordinary sets, not weighted multisets.

## Derivation

### 1. Prouhet–Thue–Morse gives unit-weight moment cancellation

The finite Thue–Morse generating polynomial factors as

\[
\boxed{
\sum_{j=0}^{2^m-1}\varepsilon_j z^j
=
\prod_{r=0}^{m-1}(1-z^{2^r}).
}
\tag{19}
\]

The right side has a zero of order `m` at `z=1`. Equivalently, the signed power sums vanish through order `m-1`, which is the binary Prouhet construction `(4)`.

Translation preserves this matching: for `r<m`, `(N+j)^r` is a polynomial in `j` of degree below `m`, so

\[
\sum_{a\in A_m}(N+a)^r
=
\sum_{b\in B_m}(N+b)^r.
\tag{20}
\]

Unlike the binomial finite-difference cluster of AF-182, every point occurs exactly once. Both sides are simple subsets of the same consecutive-integer block.

### 2. The Prouhet sum is an exact mixed finite difference

Let `E_hf(q)=f(q+h)`. Expanding `(19)` with `z` replaced by the shift operator gives

\[
\sum_{j=0}^{2^m-1}\varepsilon_j f(N+j)
=
\prod_{r=0}^{m-1}(1-E_{2^r})f(N).
\tag{21}
\]

Since `1-E_h=-\Delta_h`, iterating the fundamental theorem of calculus yields

\[
\boxed{
\sum_{j=0}^{2^m-1}\varepsilon_j f(N+j)
=(-1)^m
\int_0^1\int_0^2\cdots\int_0^{2^{m-1}}
 f^{(m)}(N+u_0+\cdots+u_{m-1})
\,du_{m-1}\cdots du_0.
}
\tag{22}
\]

The integration volume is exactly `H_m`. Thus arbitrary-order Prouhet cancellation is an anisotropic mixed finite difference with dyadic step sizes, not a multiplicity-weighted ordinary finite difference.

### 3. Euler derivatives give the uniform upper bound

Termwise differentiation of `(6)` gives

\[
G_s^{(m)}(q)
=(-1)^m
\sum_{k\ge1}
\frac{(ks)^{\overline m}}k
q^{-ks-m},
\tag{23}
\]

where

\[
(ks)^{\overline m}=ks(ks+1)\cdots(ks+m-1).
\tag{24}
\]

For `|t|\le T` and `k\ge1`,

\[
|(ks)^{\overline m}|
\le
k^m\prod_{r=0}^{m-1}(S_T+r).
\tag{25}
\]

Hence, for `q\ge N\ge2`,

\[
|G_s^{(m)}(q)|
\le
q^{-m}
\prod_{r=0}^{m-1}(S_T+r)
\sum_{k\ge1}k^{m-1}q^{-k\sigma}.
\tag{26}
\]

Using the Eulerian-polynomial bound

\[
\sum_{k\ge1}k^{m-1}r^k
\le
(m-1)!\frac{r}{(1-r)^m},
\qquad 0<r<1,
\tag{27}
\]

with `r=q^{-\sigma}` gives

\[
|G_s^{(m)}(q)|
\le
(m-1)!
\frac{\prod_{r=0}^{m-1}(S_T+r)}{(1-2^{-\sigma})^m}
N^{-(\sigma+m)}.
\tag{28}
\]

Substituting `(28)` into `(22)` proves `(12)`.

### 4. The real axis proves sharp order

At `s=\sigma>0`, every term in

\[
(-1)^mG_\sigma^{(m)}(q)
=
\sum_{k\ge1}
\frac{(k\sigma)^{\overline m}}k
q^{-k\sigma-m}
\tag{29}
\]

is positive. In particular,

\[
(-1)^mG_\sigma^{(m)}(q)
\ge
\sigma^{\overline m}q^{-(\sigma+m)}.
\tag{30}
\]

The point `t=0` lies in every declared vertical band. Applying `(22)` to `G_\sigma`, all integrand contributions have one sign and every integration point lies in `[N,N+2^m-1]`. Therefore

\[
\left|
\sum_j\varepsilon_jG_\sigma(N+j)
\right|
\ge
H_m\sigma^{\overline m}(N+2^m-1)^{-(\sigma+m)},
\tag{31}
\]

which proves `(10)` and the lower side of `(9)`. No complex-phase estimate is needed for sharpness.

### 5. The two source sets remain one integer apart

Thue–Morse signs satisfy

\[
\varepsilon_{2r}=\varepsilon_r,
\qquad
\varepsilon_{2r+1}=-\varepsilon_r.
\tag{32}
\]

Thus each adjacent pair

\[
\{N+2r,N+2r+1\},
\qquad 0\le r<2^{m-1},
\tag{33}
\]

contains exactly one point from `\mathcal A_{m,N}` and one from `\mathcal B_{m,N}`. Since different adjacent pairs are already ordered and disjoint, the monotone one-dimensional matching pairs the two points inside each pair. This proves `(13)`.

After taking logarithms, the paired distances are

\[
\log\frac{N+2r+1}{N+2r}.
\tag{34}
\]

The largest is the first one, proving `(14)` for bottleneck distance. For the normalized Wasserstein distance,

\[
\frac1{N+2^m-1}
\le
W_{1,\log}
\le
\frac1N,
\tag{35}
\]

so the same `N^{-1}` scale holds.

## Bandwidth consequence

The same derivative estimate remains informative for a growing band `T_N`. For fixed `m`,

\[
D_{m,N}(\sigma,T_N)
\le
C_{m,\sigma}
N^{-\sigma}
\left(\frac{\sqrt{\sigma^2+T_N^2}+m}{N}\right)^m.
\tag{36}
\]

In particular, if

\[
T_N=O(N^\theta),
\qquad 0\le\theta<1,
\tag{37}
\]

then

\[
\boxed{
D_{m,N}(\sigma,T_N)
=O\!\left(N^{-\sigma-m(1-\theta)}\right).
}
\tag{38}
\]

For every fixed sublinear power-law bandwidth exponent `theta<1`, arbitrary Prouhet order again destroys every uniform positive inverse Hölder exponent: choose `m` so that

\[
\alpha[\sigma+m(1-\theta)]>1.
\tag{39}
\]

This is consistent with AF-187's reciprocal-separation phenomenon. Here adjacent log-generators are separated by `Theta(N^{-1})`, so their reciprocal phase-resolution scale is `Theta(N)`. The present theorem proves only the negative side: every power-law sublinear bandwidth still permits arbitrary-order simple-integer flatness. It does not claim that linear bandwidth is sufficient for stable inversion of the whole source class.

## Arithmetic Fidelity consequence

AF-182's binomial multiplicities were not the essential source of high-order Euler cancellation. Prouhet's classical partition removes three plausible rescue assumptions simultaneously:

- every local generator norm is an integer;
- every generator is distinct;
- every generator occurs with multiplicity one.

Even under those restrictions, two equal-cardinality positive generator sets can match arbitrarily many norm-coordinate moments and become arbitrarily high-order close under fixed-band Euler observation while remaining exactly one unit apart in absolute generator geometry.

The line's source-side frontier therefore narrows. **Simplicity and integrality are not enough arithmetic provenance.** Any source restriction intended to block AF-182-style cancellation must use stronger structure: actual primality, a positivity/order condition such as the AF-206 Peano cone, a complexity condition that excludes high Prouhet order, or another arithmetic relation not shared by arbitrary simple integer generalized-prime sets.

For rational-prime applications this is still a control theorem, not a claim about the prime set itself. The construction deliberately uses integer generator norms that need not be prime. Its role is to show that replacing weighted generalized primes by simple integral controls does not yet reach the information layer where rational primality is distinguished.

## Prior art and novelty assessment

The cancellation engine is classical and no novelty is claimed for the Prouhet partition, Thue–Morse signs, equal sums of like powers, or the generating-product identity.

- Eugène Prouhet, **“Mémoire sur quelques relations entre les puissances des nombres,”** *Comptes Rendus de l'Académie des Sciences de Paris*, Série I 33 (1851), 225. Prouhet's construction partitions consecutive integers into classes with equal sums of powers through a prescribed degree.
- E. M. Wright, **“Prouhet's 1851 Solution of the Tarry-Escott Problem of 1910,”** *American Mathematical Monthly* 66(3) (1959), 199–201, DOI `10.1080/00029890.1959.11989269`. Historical reconstruction of Prouhet's solution and its equal-power-sum content.
- Jean-Paul Allouche and Jeffrey Shallit, **“The Ubiquitous Prouhet–Thue–Morse Sequence,”** in *Sequences and Their Applications*, Springer (1999), 1–16. Their Proposition 2 records the generating product behind `(19)`, and their Theorem 6 states exactly the binary Prouhet equal-power partition used in `(4)`.
- Jean-Paul Allouche and Michel Mendès France, **“Euler, Pisot, Prouhet–Thue–Morse, Wallis and the duplication of sines,”** *Monatshefte für Mathematik* 155 (2008), 301–315, DOI `10.1007/s00605-008-0012-z`. Modern source linking the Thue–Morse product formula with multigrade/Prouhet–Tarry–Escott identities.

The new content recorded here is the Arithmetic Fidelity specialization: translate the classical unit-weight Prouhet sets to escaping integer Euler-generator scale, derive the exact mixed-difference representation of their Euler-factor log contrast, prove the sharp `Theta(N^{-\sigma-m})` fixed-band profile, and convert it into a no-Hölder conditioning theorem for **simple integer generalized-prime controls**. This combination should be treated as a derived control theorem, not as a novelty claim.

## Boundaries and failure modes

1. The sets in `(5)` are simple integer generalized-prime generators, not sets of rational primes. The theorem rules out integrality and unit multiplicity as sufficient fidelity constraints; it does not rule out a stronger rescue that uses actual primality.
2. Cancellation order `m` costs `2^{m-1}` generators per side and a cluster diameter `2^m-1`. The no-uniform-Hölder conclusion allows arbitrary source complexity. A class with a hard cardinality, cancellation-order, or combinatorial-complexity budget may retain a positive modulus.
3. Equation `(9)` is for fixed finite bandwidth. Equation `(38)` extends the obstruction to power-law sublinear bandwidth, but no claim is made for `T_N` of linear or superlinear order.
4. The source moment matching in `(20)` is in **integer norm coordinate**, unlike AF-182's log-coordinate finite differences. This strengthens the integrality control but means the exact matched statistics differ. After logarithmic reparameterization the source distance is only asymptotically `N^{-1}`; the theorem does not claim exact matching of low log moments.
5. The theorem concerns Euler-factor logarithms in their local analytic half-plane `Re(s)>0`. For an actual infinite generalized-prime zeta product one may work in `Re(s)>1` and append the same sufficiently sparse simple integer tail to both systems; the common tail cancels exactly and does not change the local discrepancy.
6. No statement about zeta zeros, the critical strip, or RH follows from this conditioning obstruction.

## Consequence for the next research step

Do not treat “simple primes rather than weighted generalized primes” as a sufficient answer to the source-complexity problem. The next useful arithmetic gate is stricter: determine which properties genuinely specific to the rational-prime source class prevent high-order Prouhet-type matched cancellation, or prove that natural prime-like control classes still admit it. Candidate restrictions must be stated at the same information layer as the Euler compression — for example actual primality/counting constraints, order/positivity of the induced Peano carrier, or a quantified source-complexity bound — and must be tested against simple integer Prouhet controls before being credited as discriminator-preserving structure.
