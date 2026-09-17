# RE-189 — High Euler boundary jets collapse to net multiplicity past log-squared depth

**Status:** `EXACT-DERIVED + CLASSICAL-PARTIAL-FRACTION + BOUNDARY-JET-CONDITIONING + LOG-SQUARED-SATURATION + FINITE-PACKET + SOURCE-INFORMATION-BOUND + PRIOR-ART-IDENTIFIED`.

**Parent findings:** RE-174, RE-178, RE-188.

`RE-188` pushes exact scalar Euler-jet non-rigidity to depths

\[
K=o\!\left((\log p)^{5/3}(\log\log p)^{1/3}\right),
\]

still strictly below `(log p)^2`. The natural temptation is to interpret still higher boundary derivatives as progressively more source-resolving information and hope that enough of them approach the complete Euler fingerprint of `RE-174`.

For a single Euler factor the opposite phenomenon begins at a precise scale. Write

\[
F_q(s):=-\log(1-q^{-s}),
\qquad L:=\log q,
\]

and for integers `j>=1`

\[
U_j(q):=(-1)^jF_q^{(j)}(1)
=L^j\sum_{n\ge1}n^{j-1}e^{-nL}.
\tag{1}
\]

For every `j>=2` there is the exact expansion

\[
\boxed{
\frac{U_j(q)}{(j-1)!}
=
1+2\operatorname{Re}\sum_{k\ge1}
\left(\frac{L}{L+2\pi i k}\right)^j.
}
\tag{2}
\]

Consequently there are absolute constants `C,c>0` such that, for all sufficiently large `L` and every integer `j>=L^2`,

\[
\boxed{
\left|
\frac{U_j(q)}{(j-1)!}-1
\right|
\le
C\exp\!\left(-c\frac{j}{L^2}\right).
}
\tag{3}
\]

Thus, after factorial normalization, sufficiently high boundary jets of **every prime near the same logarithmic scale become almost identical**. The leading coordinate is no longer prime location; it is just multiplicity count. Prime-specific information survives only in exponentially small corrections controlled by the nonzero imaginary singularities of the Euler factor.

For any finite signed prime packet `c_q` supported in a fixed multiplicative selector window

\[
p^a\le q\le p^b,
\qquad 0<a<b<\infty,
\]

put

\[
N:=\sum_q|c_q|,
\qquad
C_0:=\sum_q c_q,
\]

and

\[
D(s):=\sum_q c_qF_q(s).
\]

Then for `j>=C_1(log p)^2`, with constants depending only on `a,b`,

\[
\boxed{
\left|
\frac{(-1)^jD^{(j)}(1)}{(j-1)!}-C_0
\right|
\le
C_2N\exp\!\left(-c_2\frac{j}{(\log p)^2}\right).
}
\tag{4}
\]

In particular, two selector-scale packets with the same net multiplicity become exponentially indistinguishable to normalized high boundary jets. If `C_0=0`, then the entire normalized response itself is exponentially small. This identifies a second scalar crossover, at depth

\[
\boxed{j\asymp(\log p)^2,}
\tag{5}
\]

beyond which simply increasing derivative order does **not** buy increasingly robust prime-location information.

## 1. Exact pole expansion

For `j>=1`, differentiating the absolutely convergent Euler-factor series at `s=1` gives (1). Put

\[
S_j(L):=\sum_{n\ge1}n^{j-1}e^{-nL}.
\]

Since

\[
\sum_{n\ge1}e^{-nL}
=\frac1{e^L-1}
=\frac12\coth\frac L2-\frac12,
\tag{6}
\]

the standard partial-fraction expansion of `coth`, followed by `j-1` differentiations, yields for every `j>=2`

\[
\boxed{
S_j(L)
=(j-1)!\sum_{k\in\mathbb Z}(L+2\pi i k)^{-j}.
}
\tag{7}
\]

Equivalently, (7) is the Poisson-summation identity for the gamma-density lattice sum. Multiplying by `L^j/(j-1)!` gives

\[
\frac{U_j(q)}{(j-1)!}
=
\sum_{k\in\mathbb Z}
\left(\frac{L}{L+2\pi i k}\right)^j,
\tag{8}
\]

and pairing `k` with `-k` proves (2).

The `k=0` term is exactly one. It comes from the common singularity at `s=0` of every Euler factor `F_q(s)`. The next pair `k=+-1` records the first prime-dependent singularities

\[
s=\pm\frac{2\pi i}{\log q}.
\]

Writing

\[
r(L):=\left(1+\frac{4\pi^2}{L^2}\right)^{-1/2},
\qquad
\theta(L):=\arctan\frac{2\pi}{L},
\]

the first location-sensitive correction in (2) is

\[
2r(L)^j\cos(j\theta(L)),
\tag{9}
\]

with

\[
\log r(L)
=-\frac{2\pi^2}{L^2}+O(L^{-4}).
\tag{10}
\]

So the natural attenuation scale of prime-specific boundary-jet information is already visible exactly: `j/L^2`.

## 2. Exponential saturation after `j comparable to L^2`

Taking absolute values in (2),

\[
\left|
\frac{U_j(q)}{(j-1)!}-1
\right|
\le
2\sum_{k\ge1}
\left(1+\frac{4\pi^2k^2}{L^2}\right)^{-j/2}.
\tag{11}
\]

Split the sum into `2pi k<=L`, `L<2pi k<=2pi L`, and `k>L`. In the first range, `log(1+x)>=x/2` for `0<=x<=1`, hence

\[
\left(1+\frac{4\pi^2k^2}{L^2}\right)^{-j/2}
\le
\exp\!\left(-\pi^2\frac{jk^2}{L^2}\right).
\tag{12}
\]

When `j>=L^2`, summing this Gaussian tail is `O(exp(-c j/L^2))`. In the middle range each term is at most `2^{-j/2}` and there are `O(L)` terms. In the final range,

\[
\left(1+\frac{4\pi^2k^2}{L^2}\right)^{-j/2}
\le
\left(\frac{L}{2\pi k}\right)^j,
\tag{13}
\]

whose tail is exponentially smaller still. This proves (3).

There is a useful geometric interpretation. Equation (1) can be written

\[
\frac{U_j(q)}{(j-1)!}
=
L\sum_{n\ge1}
\frac{(nL)^{j-1}e^{-nL}}{(j-1)!}.
\tag{14}
\]

The summand is the density of a Gamma distribution with shape `j`, sampled on a lattice of spacing `L`. Its standard deviation is `sqrt(j)`. Once

\[
\sqrt j\gg L,
\]

the lattice is much finer than the width of the gamma bump and the Riemann sum forgets the lattice spacing, converging to its integral `1`. The exact pole expansion quantifies that loss exponentially.

## 3. Finite selector packets collapse to one count coordinate

Let the packet be supported in `[p^a,p^b]`. Then every `L_q=log q` is at most `b log p`. Applying (3) term by term gives, for `j>=b^2(log p)^2`,

\[
\begin{aligned}
\frac{(-1)^jD^{(j)}(1)}{(j-1)!}
&=
\sum_qc_q
\frac{U_j(q)}{(j-1)!}\\
&=
\sum_qc_q
+O_{a,b}\!\left(
N e^{-c_{a,b}j/(\log p)^2}
\right),
\end{aligned}
\tag{15}
\]

which is (4).

The leading high-jet statistic is therefore the integer `C_0`, the net number of duplicated copies minus deleted copies. All information about **where** those edits occur inside the selector-scale window is pushed into the exponentially small remainder.

This is source-specific in a useful way. The effect is caused by the prime-power completion inside one exact Euler factor, not by replacing primes with a continuous measure or by a poor polynomial basis. If one drops the prime powers and keeps only the `n=1` term, the normalized response would be

\[
\frac{L^je^{-L}}{(j-1)!},
\]

which has completely different large-`j` behavior. The collapse is therefore invisible in the first-prime-mode models that motivated some of the earlier jet conditioning estimates.

## 4. Relation to the current scalar frontier

`RE-178` found a capacity crossover near `log p/log log p`; `RE-184`--`RE-188` then showed constructively that this was not a rigidity threshold. `RE-188` currently reaches

\[
K=o\!\left(L^{5/3}(\log L)^{1/3}\right),
\qquad L=\log p.
\]

But

\[
\frac{L^{5/3}(\log L)^{1/3}}{L^2}
=
\left(\frac{\log L}{L}\right)^{1/3}
\longrightarrow0.
\tag{16}
\]

So all existing exact constructive non-rigidity remains entirely in the **pre-saturation** regime of (5). If a future repair architecture removes the spatial KV ceiling and reaches depths comparable with `L^2`, the scalar system changes character: the new highest rows become increasingly count-like rather than increasingly location-sensitive.

This does not prove that arbitrary depth can be matched. Exact exponentially small corrections in (2) still contain prime-specific information, and a simultaneous solve may become violently ill-conditioned. The conclusion is narrower and more useful: **high derivative order is not itself a robust path from finite jets toward source identification**. Past `L^2`, the source-specific signal is precisely the small remainder after subtracting the universal count mode.

This also clarifies why `RE-174` behaves differently. High-temperature samples `D_Q(sigma)` with `sigma->infinity` isolate the *smallest changed prime*. High boundary derivatives at the fixed point `s=1` instead become dominated by the singularity at `s=0`, which is shared by every Euler factor. These are genuinely different source representations; one should not expect large Taylor order at the Mertens boundary to emulate moving far into the absolutely convergent half-plane.

## 5. Adversarial checks and scope

**The factorial normalization is essential.** Raw derivatives grow like `(j-1)!`; comparing them without removing this universal growth would hide the conditioning statement.

**The result starts at `j=2`.** The first derivative has an additional regularization term in the `coth` partial fraction and is irrelevant to the large-depth claim.

**Finite or localized packets are the proved scope.** Equation (4) assumes finite `N`. An infinite repair tail can have no finite net edit count, and exchanging the `j->infinity` limit with such a tail requires additional summability not asserted here.

**No exact rigidity failure is claimed.** The exponentially small remainder may still encode the support at exact infinite precision. The theorem is about conditioning and effective source information, not equality of two full germs.

**The `L^2` scale is local in logarithmic support.** For packets spanning much larger logarithmic ranges, the slowest saturation scale is set by the largest `log q` present.

**No RH-strength input is used.** The argument is an exact single-Euler-factor calculation and applies independently of any zero-free region or prime-distribution estimate.

## 6. Prior-art and representation audit

The analytic identity is classical. NIST DLMF §4.36 records the standard partial fractions for `coth` and `csch^2`; differentiating the `coth` expansion gives (7). The same formula is a standard negative-order-polylogarithm / Poisson-summation identity. A targeted search found this classical special-function material but no Robin/CA result using the resulting `j/(log q)^2` attenuation as a source-fidelity boundary.

Accordingly, no novelty is claimed for the partial-fraction identity, for Poisson summation, or for the fact that a gamma-density lattice sum converges to its integral. The line-specific contribution is the **representation audit**: exact Euler boundary derivatives are these lattice sums, so the prime-power tower forces a universal multiplicity mode and exponentially suppresses prime-location information after log-squared depth. The derivation above is self-contained at the level needed here, so no new external theorem is imported into `SOURCES.md`.

This is also a warning against representation artifacts. The linear Chebyshev window of `RE-188` describes how its chosen repair frame controls prime-power leakage below the current KV spatial ceiling. Equation (2) describes the exact kernel itself, independent of that frame. The new log-squared crossover therefore survives any change of interpolation basis, although what one can construct beyond it remains open.

## 7. Research consequence

The next scalar question should not be phrased as merely increasing `K`. There are now three distinct regimes:

\[
K\ll (\log p)^2
\quad\text{(location-sensitive boundary jets)},
\]

\[
K\asymp (\log p)^2
\quad\text{(prime-power saturation crossover)},
\]

and

\[
K\gg (\log p)^2
\quad\text{(universal count mode plus exponentially small location residue)}.
\]

A meaningful source-sensitive continuation would have to exploit the **joint structure of the exponentially small residues** in (2), remove the common `s=0` mode before measuring conditioning, or leave scalar boundary jets and return to selector-conditioned occupancy / nonlocal Euler information. Simply appending higher raw derivatives eventually adds almost parallel rows.

**Provenance:** derived against default-branch snapshot `f61aeb47da85be57c28bfe607a93f4eed338109f`; stable finding prefix `RE`; no adversarial sidecar was open; local clues were inspected; no clue-state, `mind/**`, README, graph, or source-registry mutation required.