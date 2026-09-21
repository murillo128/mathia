# FD-258 — The first switched row imposes a zero-frontier polynomial depth ceiling

- **Date:** 2026-09-21
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** exact first-row capacity obstruction / dyadic Mertens increment / zeta-zero power frontier / scale-adapted reservoir depth ceiling
- **Depends on:** FD-257, FD-226, FD-225, FD-046, FD-005
- **Classification:** `EXACT-DERIVED + LITERATURE-CALIBRATED + SOURCE-SIDE-OBSTRUCTION + FIRST-ROW-CAPACITY + DYADIC-MERTENS-INCREMENT + ZERO-FRONTIER + POLYNOMIAL-DEPTH-CEILING`

## Claim

The source-side positivity problem has an obstruction that appears before the deep-band capacity depletion of FD-257. In the exact scale-adapted divisor-reservoir architecture of FD-226, the **first switched row alone** forces the first two reservoir counts to absorb the dyadic Mertens increment

\[
B_{\mathbf M}(N):=\mathbf M(2N)-\mathbf M(N)
=\sum_{N<n\le 2N}\mu(n).
\]

Let

\[
I_d^*=\left(dN\left(1-\frac1{4D}\right),dN\right],
\qquad 1\le d\le D,
\]

be the FD-226 exact floor cells, let `K_d(N)` be the number of available reservoir primes in `I_d^*`, and choose physical occupancies

\[
0\le a_d\le K_d(N).
\]

Let `X_N` be the selected-Euler source obtained from the physical Möbius baseline by flipping those primes, exactly as in FD-225--FD-226. If the first switched row is bounded by `B_N`,

\[
\left|X_N(2N)-X_N(N)\right|\le B_N,
\tag{1}
\]

then, without using any prime-number-theorem estimate,

\[
\boxed{
|B_{\mathbf M}(N)|
\le B_N+\frac ND+2.
}
\tag{2}
\]

Equivalently, whenever `|B_M(N)|>B_N+2`,

\[
\boxed{
D\le
\frac{N}{|B_{\mathbf M}(N)|-B_N-2}.
}
\tag{3}
\]

The arithmetic forcing term in (2) has exactly the full zeta-zero polynomial exponent. With

\[
\Theta
:=
\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\},
\]

one has

\[
\boxed{
\limsup_{N\to\infty}
\frac{\log(1+|\mathbf M(2N)-\mathbf M(N)|)}{\log N}
=\Theta.
}
\tag{4}
\]

Consequently, if `B_N=N^{o(1)}` (in particular if the switched target is `O(1)` as in FD-225), there are infinitely many horizons along which every realization inside the FD-226 cells obeys

\[
\boxed{
D\le N^{1-\Theta+o(1)}.
}
\tag{5}
\]

Thus an all-sufficiently-large-`N` reservoir construction with a uniform polynomial lower depth

\[
D_N\ge N^{\alpha+o(1)}
\]

cannot have `alpha>1-Theta`. Since Hardy's theorem gives `Theta>=1/2`, an unconditional consequence is that no such construction can maintain a bounded first switched row with uniform depth exponent strictly larger than `1/2`. If RH is false, `Theta>1/2` and the ceiling is strictly below the square-root exponent.

This is a genuine capacity obstruction, but it lies far beyond the presently certified Vinogradov--Korobov block `D=N^{o(1)}`. It therefore does **not** invalidate FD-225--FD-226. Its role is to pin a polynomial-depth ceiling for this exact reservoir architecture and to show that the physical Mertens baseline eventually re-enters through the very first row, even if all later conditioning and positivity issues were solved.

## 1. The first two reservoir columns decouple exactly

The exact source response of FD-226 is

\[
X_N(mN)
=
\mathbf M(mN)
+2\sum_{d\le m}
 a_d\,
\mathbf M\!\left(\left\lfloor\frac md\right\rfloor\right),
\qquad 1\le m\le D.
\tag{6}
\]

At `m=1`, only the first reservoir appears and `M(1)=1`, so

\[
X_N(N)=\mathbf M(N)+2a_1.
\tag{7}
\]

At `m=2`, the first reservoir is multiplied by `M(2)=0`, while the second is multiplied by `M(1)=1`. Therefore

\[
X_N(2N)=\mathbf M(2N)+2a_2.
\tag{8}
\]

Subtracting gives the exact identity

\[
\boxed{
X_N(2N)-X_N(N)
=
B_{\mathbf M}(N)+2(a_2-a_1).
}
\tag{9}
\]

This is stronger than a statement about the canonical full-grid correction. It does not assume a common occupancy, a constant response target, the exact divisor inverse, or any behavior of rows after the first one. Every physical source that stays inside the first two FD-226 reservoirs and makes the first switched row small must satisfy (9).

The identity is also immune to the usual reservoir-interaction concern. For large `N`, selected reservoir primes are `>(1-o(1))N`, so the product of two selected primes exceeds `2N`; at these first two samples their source effects add exactly. The selected-Euler extension through small locked primes is already what produces the Mertens factors in (6).

## 2. Trivial cell cardinality already gives the capacity bound

The first two scale-adapted cells have lengths

\[
|I_1^*|=\frac{N}{4D},
\qquad
|I_2^*|=\frac{N}{2D}.
\tag{10}
\]

No prime-distribution theorem is needed for an upper bound on their occupancy capacities. Simply counting possible integers gives

\[
K_1(N)\le \frac{N}{4D}+1,
\qquad
K_2(N)\le \frac{N}{2D}+1.
\tag{11}
\]

Since `0<=a_d<=K_d`,

\[
|a_2-a_1|
\le \max(K_1,K_2)
\le \frac{N}{2D}+1.
\tag{12}
\]

Combining (1), (9), and (12) yields

\[
|B_{\mathbf M}(N)|
\le B_N+2|a_2-a_1|
\le B_N+\frac ND+2,
\]

which proves (2)--(3).

The use of the trivial cardinality bound is deliberate. FD-226's asymptotic prime-capacity law `K_d asymp dN/(D log N)` is certified only in its current Vinogradov--Korobov prime-resolution range. Equation (2), by contrast, remains a valid necessary condition even when `D` is polynomial and that asymptotic is no longer available. Any sharper upper bound for primes in these short cells would only strengthen (2); none is required for the exponent conclusion below.

## 3. Dyadic Mertens increments carry the full zero-frontier exponent

The general arithmetic statement behind the obstruction is elementary once the classical power frontier of the Mertens function is fixed. FD-046 records that

\[
\inf\{\sigma>0:\mathbf M(x)=O(x^{\sigma+\varepsilon})
\text{ for every }\varepsilon>0\}
=\Theta.
\tag{13}
\]

We now show that passing from `M(N)` to one multiplicative block loses no polynomial exponent.

The upper bound in (4) is immediate. For every `sigma>Theta`, (13) gives

\[
|B_{\mathbf M}(N)|
\le |\mathbf M(2N)|+|\mathbf M(N)|
=O_\sigma(N^\sigma).
\tag{14}
\]

For the reverse inequality, suppose instead that the limsup exponent of `B_M` were strictly below `Theta`. Choose

\[
0<\sigma<\Theta
\]

above that limsup. Then for all sufficiently large integers `n`,

\[
|B_{\mathbf M}(n)|\le n^\sigma.
\tag{15}
\]

Fix an integer `N` and form the binary descent

\[
n_j=\left\lfloor\frac{N}{2^j}\right\rfloor.
\]

Whenever `n_{j+1}=m>=1`, one has either `n_j=2m` or `n_j=2m+1`, and hence

\[
\mathbf M(n_j)-\mathbf M(n_{j+1})
=
B_{\mathbf M}(m)
+\epsilon_j\mu(2m+1),
\qquad
\epsilon_j\in\{0,1\}.
\tag{16}
\]

Telescoping until the descent reaches one and using (15),

\[
\begin{aligned}
|\mathbf M(N)|
&\ll
1+
\sum_{j\ge0}
\left(n_{j+1}^\sigma+1\right)\\
&\ll
N^\sigma+\log N\\
&\ll N^\sigma.
\end{aligned}
\tag{17}
\]

This contradicts (13) because `sigma<Theta`. Therefore the lower limsup in (4) is at least `Theta`, and (14) proves equality.

No claim of general novelty is made for this dyadic-block corollary of the classical Mertens power criterion. The research-specific point is that this exact block is precisely the forcing term that the first two physical reservoir cells must cancel.

## 4. The zero frontier becomes a polynomial depth ceiling

Equation (4) says that for every fixed `epsilon>0` there are infinitely many `N` with

\[
|B_{\mathbf M}(N)|
\ge N^{\Theta-\epsilon}.
\tag{18}
\]

Assume `B_N=N^{o(1)}`. Since `Theta>=1/2`, the switched tolerance and the additive constant in (2) are negligible on the subsequence (18). Equation (3) gives

\[
D
\le
N^{1-\Theta+\epsilon+o(1)}.
\tag{19}
\]

Letting `epsilon` tend to zero along a diagonal subsequence proves (5).

A useful formulation is therefore

\[
\boxed{
\liminf_{N\to\infty}
\frac{\log D_N}{\log N}
\le 1-\Theta
}
\tag{20}
\]

for every all-large-`N` family in this reservoir architecture whose first switched row is `N^{o(1)}`. In particular, if one asks for a uniform lower depth exponent `alpha`, then necessarily

\[
\boxed{
\alpha\le1-\Theta\le\frac12.
}
\tag{21}
\]

The dependence on `Theta` is structurally natural. Under RH, `Theta=1/2` and the first-row capacity ceiling is square-root scale. If RH is false, the rightmost zero moves to `Theta>1/2` and the admissible depth exponent decreases to `1-Theta`.

This should not be confused with an RH-equivalent construction theorem. Equation (21) is only a **necessary** condition for the selected-reservoir countermodel. Nothing here constructs bounded switched rows up to `N^(1-Theta)`, and nothing rules out a different source representation with more degrees of freedom in the first row.

## 5. Relation to FD-257 and the current physical frontier

FD-257 proves a different source-side fact: under a linear coefficient envelope, a nonnegative cushion whose entire switched schedule remains bounded must lose dyadic capacity at a fixed polynomial rate. That is a deep-band one-sided constraint. It explicitly leaves open whether the canonical block-Mertens repair actually demands enough positive slack on those bands to create a contradiction.

The present obstruction bypasses that missing lower bound. It uses neither aggregate negative capacity nor late-band positivity. Before any deep row is considered, the first switched row asks the two smallest exact floor cells to compensate the actual arithmetic block

\[
\sum_{N<n\le2N}\mu(n).
\]

At the current FD-225--FD-226 depth

\[
D=\exp(O(\Phi(N)))=N^{o(1)},
\]

the available first-cell width `N/D=N^{1-o(1)}` is vastly larger than the zero-frontier forcing `N^{Theta+o(1)}` whenever `Theta<1`; thus (2) creates no new obstruction in the certified regime. This is consistent with FD-225's successful common-cushion construction.

The result becomes decisive only for a future attempt to push the exact same reservoir geometry to polynomial depth. It says that improving prime resolution, divisor-response conditioning, rounding, or late-band positive-lift estimates cannot by themselves yield a uniform exponent above `1-Theta`: the first row would already run out of physical slots on an infinite arithmetic subsequence.

## 6. Prior-art boundary, failure modes, and next test

The literature input is exactly the standard Mertens/zeta-zero power frontier already anchored in `SOURCES.md` through Titchmarsh and used in FD-046. The identity `M(2N)-M(N)=sum_(N<n<=2N) mu(n)` and the binary telescoping argument are elementary. The prior-art search did not identify a separate external theorem needed for (4), so no new source anchor is required.

The repository-specific statement is the coupling of that classical dyadic block to the first two exact reservoir columns. The key cancellation `M(2)=0` makes the geometry unusually rigid: reservoir `1` disappears completely from the `2N` sample, reservoir `2` is the only active new column, and the first switched row can change the baseline block only through the bounded difference `a_2-a_1`.

The boundary is correspondingly precise. The theorem applies to the FD-226 selected-prime reservoir architecture and its exact floor-response representation. A construction that introduces additional source variables affecting `N` or `2N`, changes the reservoir geometry, or abandons this selected-Euler realization may evade (2). The theorem also gives no obstruction to the present subpolynomial depth and no matching sufficiency result below `1-Theta`.

**Verdict.** The first switched row already contains a source-side polynomial barrier that is invisible in the current Vinogradov--Korobov regime. Its forcing term has the full zeta-zero exponent `Theta`, while the first two physical cells contain only `O(N/D)` possible flips. Therefore the exact FD-226 reservoir architecture cannot support a uniformly bounded first switched row at all sufficiently large horizons with polynomial depth exponent above `1-Theta`; unconditionally, any such uniform exponent is at most `1/2`. A future polynomial-depth countermodel must change the first-row source geometry, not merely improve later-row conditioning or positivity estimates.