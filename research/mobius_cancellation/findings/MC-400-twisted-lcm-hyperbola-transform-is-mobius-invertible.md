# MC-400 — Twisted lcm hyperbola transform is an exact Möbius-inversion pair

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-REFINEMENT` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the exact Selberg/source setup of `MC-398` and `MC-399`. Write

\[
f(n)=\left(\sum_{d\mid n}g(d)\right)^2
=\sum_{\ell\mid n}C_g(\ell),
\qquad C_g(\ell)=0\quad(\ell>B^2),
\tag{1}
\]

and fix one source-mode Dirichlet character `\chi=\chi_I`. Define

\[
c_\chi(\ell):=C_g(\ell)\chi(\ell),
\qquad
f_\chi(n):=f(n)\chi(n),
\tag{2}
\]

with partial sums

\[
A_\chi(X):=\sum_{\ell\le X}c_\chi(\ell),
\qquad
F_\chi(X):=\sum_{n\le X}f_\chi(n),
\qquad
M_\chi(X):=\sum_{m\le X}\chi(m).
\tag{3}
\]

Then complete multiplicativity gives the coefficient-level Dirichlet-convolution identities

\[
\boxed{f_\chi=\chi*c_\chi},
\qquad
\boxed{c_\chi=(\mu\chi)*f_\chi},
\tag{4}
\]

where `(\mu\chi)(n)=\mu(n)\chi(n)` is the Dirichlet-convolution inverse of `\chi`.

Consequently the lcm/end-point transform isolated in `MC-399` has the exact summatory forms

\[
\boxed{
F_\chi(N)
=\sum_{\ell\le N}c_\chi(\ell)M_\chi(N/\ell)
=\sum_{m\le N}\chi(m)A_\chi(N/m),
}
\tag{5}
\]

and the exact inverse

\[
\boxed{
A_\chi(N)
=\sum_{d\le N}\mu(d)\chi(d)F_\chi(N/d).
}
\tag{6}
\]

As usual, the arguments of summatory functions in `(5)`--`(6)` mean integer floors.

Thus the moving boundary `N/\ell` left open by `MC-399` is not, by itself, an additional arithmetic sample or independent averaging coordinate. It is the standard hyperbola presentation of the convolution `(4)`, and the scale-indexed families `F_\chi` and `A_\chi` determine each other exactly by Möbius inversion.

This does **not** say that hyperbola or bilinear methods are useless. A real gain may still come from an independent theorem about the special lcm coefficients `C_g`, cancellation of the twisted partial sums `A_\chi`, concentration by source-signature class, or a genuinely joint bilinear estimate that exploits structure not contained in the formal inversion. What is ruled out is treating the moving boundary itself as new arithmetic information after `MC-399` has already reduced the object to `(5)`.

No estimate for `M(x)` follows.

## 1. Coefficient-level inversion

Equation `(1)` is the exact lcm-fiber identity of `MC-398`, namely

\[
f=\mathbf 1*C_g
\tag{7}
\]

under Dirichlet convolution. Multiplying by the completely multiplicative character `\chi` gives

\[
\begin{aligned}
(\chi*c_\chi)(n)
&=\sum_{d\mid n}\chi(d)C_g(n/d)\chi(n/d)\\
&=\chi(n)\sum_{d\mid n}C_g(n/d)\\
&=f(n)\chi(n)=f_\chi(n),
\end{aligned}
\tag{8}
\]

which proves the first identity in `(4)`.

For every completely multiplicative `\chi`, including a Dirichlet character that vanishes on non-units of its modulus,

\[
\chi*(\mu\chi)=\varepsilon,
\tag{9}
\]

because

\[
\sum_{d\mid n}\chi(d)\mu(n/d)\chi(n/d)
=\chi(n)\sum_{d\mid n}\mu(n/d)
=\varepsilon(n).
\]

Convolving `(8)` with `\mu\chi` therefore gives the second identity in `(4)`.

The point is structural: the twisted lcm coefficient sequence `c_\chi` and the twisted Selberg sequence `f_\chi` are not two independent arithmetic objects. At coefficient level they are related by an exactly invertible classical transform.

## 2. The moving hyperbola boundary is the summatory convolution

Summing `(8)` up to `N` and writing `n=\ell m` gives

\[
\begin{aligned}
F_\chi(N)
&=\sum_{\ell m\le N}c_\chi(\ell)\chi(m)\\
&=\sum_{\ell\le N}c_\chi(\ell)M_\chi(N/\ell),
\end{aligned}
\tag{10}
\]

which is exactly the fixed-mode transform already present in equation `(2)` of `MC-399`.

Reversing the order instead yields

\[
F_\chi(N)
=\sum_{m\le N}\chi(m)
\sum_{\ell\le N/m}c_\chi(\ell)
=\sum_{m\le N}\chi(m)A_\chi(N/m),
\tag{11}
\]

proving the second form in `(5)`.

Now sum the inverse coefficient identity in `(4)`:

\[
\begin{aligned}
A_\chi(N)
&=\sum_{dm\le N}\mu(d)\chi(d)f_\chi(m)\\
&=\sum_{d\le N}\mu(d)\chi(d)F_\chi(N/d),
\end{aligned}
\tag{12}
\]

which is `(6)`.

Equations `(5)` and `(6)` sharpen the open boundary left by `MC-399`. The hyperbola `\ell m\le N` is genuine coupling in the summation region, but **its mere presence does not create a new source of arithmetic information**: over all scales, the lcm-side cumulative data and the original twisted Selberg partial sums are exact inversion partners.

## 3. What kind of lcm-side estimate could still matter

The inversion only blocks a representation-level shortcut. It does not prevent additional information about `C_g` from being useful.

A substantive lcm-side gain would need an estimate such as

\[
A_\chi(X)=\sum_{\ell\le X}C_g(\ell)\chi(\ell)
\tag{13}
\]

that is proved from **independent structure of the Selberg weight and the lcm fibers**: for example cancellation across lcm coefficients, concentration across source signatures, a special multiplicative decomposition of `C_g`, or a joint bilinear theorem whose hypotheses are not automatic consequences of `(4)`--`(6)`.

Such a theorem could then be inserted into `(11)` and might genuinely alter the source-depth or common-radical cost. Conversely, deriving a bound for `A_\chi` only from `(6)` using a bound for `F_\chi`, and then feeding it through `(11)` to claim an improved bound for the same `F_\chi`, is formally circular unless a strict independent gain enters between the two transforms.

The same distinction applies to a direct source-signature incidence estimate. If it controls signature-class sums of `C_g` by a theorem about their arithmetic distribution, it lies outside this obstruction. If it merely Fourier-expands the same convolution and renames the hyperbola boundary as an extra average, it does not.

## 4. Prior art and novelty boundary

The mathematics in `(4)`--`(12)` is classical Dirichlet convolution, Möbius inversion, and summatory hyperbola rearrangement. NIST DLMF §27.6, already recorded as `MC-S9` in `SOURCES.md`, is an authoritative classical anchor for the divisor-sum/Möbius-inversion mechanism and cites Apostol's *Introduction to Analytic Number Theory*, Chapter 2. Standard Dirichlet-hyperbola arguments use the same summatory convolution rearrangement.

No novelty is claimed for these identities. The Mathia-specific contribution is a **frontier classification** obtained by applying that classical inverse structure to the exact post-`MC-399` object: once the source phase has separated, the remaining moving lcm boundary is a reversible convolution representation and cannot be credited, by itself, as the missing Stadlmann-style retained arithmetic variable.

This is deliberately narrower than a no-go theorem for all hyperbola methods. Hyperbola decompositions are often powerful precisely when one factor carries independently controlled partial sums or when a bilinear decomposition exposes additional structure. Those possibilities remain live here.

## Boundaries and falsification tests

- **No claim that `C_g` is generic is made.** Special algebraic or sign structure of the actual Selberg coefficients may support a new theorem for `(13)`.
- **No positivity of `C_g` is assumed.** `MC-398` already warned that the lcm-fiber coefficient is signed in general.
- **No single-scale bijection is claimed.** The exact statement concerns the coefficient sequences and their scale-indexed partial sums; one value `F_\chi(N)` alone does not determine one value `A_\chi(N)`.
- **The hyperbola boundary is not erased.** It remains useful bookkeeping and may be analytically exploitable together with independent factor estimates; it is only ruled out as independent arithmetic data by itself.
- **A genuinely joint bilinear estimate remains open.** A method need not first prove a standalone bound for `A_\chi` if it exploits structure of `c_\chi(\ell)\chi(m)` that is not a tautological consequence of convolution.
- **The pre-quadratic route remains open.** A variable that does not factor through the lcm before the quadratic Selberg compression is outside `(4)`--`(12)`.
- **Dirichlet-character zeros cause no exception.** Complete multiplicativity and `(9)` remain exact when primes dividing the modulus receive character value zero.
- **No analytic continuation, zero-free region, or RH input is used.** The result is finite arithmetic algebra.
- **No Möbius cancellation bound follows.** The finding only removes one representation-level interpretation of the current endpoint branch.

A proposed counterexample must show that the moving boundary in the exact standard transform `(5)`, without importing independent information about `C_g`, its signature distribution, or a new bilinear structure, supplies arithmetic information not already related to `F_\chi` by `(6)`. A theorem exploiting such independent lcm-side structure is not a counterexample; it is the surviving branch identified here.

## Consequence for the research line

`MC-397` removed source-mode averaging as a free arithmetic dimension. `MC-398` compressed the squared Selberg divisor pair to the single lcm coefficient. `MC-399` showed that this lcm coordinate separates from the source-character phase before the first additive q-vdC correlation. `MC-400` now classifies the remaining moving-boundary escape: **the standard twisted lcm/end-point transform and its lcm-coefficient partial sums form an exact Möbius-inversion pair, so the hyperbola boundary alone is not a new averaging variable.**

The accepted retained-variable clue therefore narrows once more. Its standard-lcm branch now requires an independent theorem about `C_g(\ell)\chi_I(\ell)`, its source-signature class sums, or a genuinely collective bilinear estimate that changes the source-cost scaling without merely cycling through `(5)`--`(6)`. The alternative branch remains a pre-quadratic representation containing an arithmetic variable that does not collapse through the lcm and stays nonseparable through the relevant correlation.