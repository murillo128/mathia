# WI-432 — adiabatic height localization kills the safe-line prime Hardy leakage

Status: `CLASSICAL-IDENTITY + EXACT-DERIVED + DECISIVE-BARRIER + PRIOR-ART-AUDITED + NO-NOVELTY-CLAIM`

Parents: `WI-429`, `WI-430`, `WI-431`

## Claim

`WI-431` shows that height localization is the first place where the negative-frequency prime source can mix into the positive Hardy half-space. That statement is necessary but not sufficient: for the most natural *adiabatic* localizations, the prime leakage actually disappears as the height window is widened.

Fix a safe line \(\sigma>1\) and write

\[
F_\sigma(t)
:=\frac{\zeta'(\sigma+it)}{\zeta(\sigma+it)}
 +\frac1{\sigma-1+it}
=D_\sigma(t)+h_{\sigma-1}(t),
\]

where

\[
D_\sigma(t)=-\sum_{n\ge2}\Lambda(n)n^{-\sigma}e^{-it\log n},
\qquad
h_c(t)=\frac1{c+it}.
\]

Under the Fourier convention \(\widehat f(\xi)=\int_\mathbb R f(t)e^{-it\xi}\,dt\), let \(P_+\) be the multiplier \(1_{\xi>0}\). For a fixed Schwartz window \(\chi\), put

\[
\chi_T(t)=\chi(t/T),\qquad T>0.
\]

Then

\[
\boxed{
\|P_+(\chi_TD_\sigma)\|_2
\le
A_\sigma
\left(
\frac{T}{2\pi}
\int_{T\log2}^{\infty}|\widehat\chi(v)|^2\,dv
\right)^{1/2},
}
\tag{1}
\]

where

\[
A_\sigma:=\sum_{n\ge2}\Lambda(n)n^{-\sigma}
=-\frac{\zeta'(\sigma)}{\zeta(\sigma)}<\infty.
\]

Consequently the **prime contribution decays faster than every power of \(T\)** for every fixed Schwartz window.

The elementary pole-cancelling Cauchy term has no spectral gap at frequency zero, but its leakage still satisfies

\[
\boxed{
\|P_+(\chi_Th_c)\|_2^2
\le \frac{C_\chi}{T},
\qquad
C_\chi:=\frac1{2\pi}
\int_0^\infty
\left(\int_x^\infty|\widehat\chi(v)|\,dv\right)^2dx<\infty.
}
\tag{2}
\]

Hence, on every fixed safe line,

\[
\boxed{
\|P_+(\chi_TF_\sigma)\|_2=O_\chi(T^{-1/2}),
}
\tag{3}
\]

and the arithmetic prime part is smaller than any power of \(T^{-1}\). Thus a smooth cutoff widened by dilation does **not** produce a bulk positive-frequency prime signal on the safe line. Any nonzero interior signal capable of paying the `WI-430` first-defect quantum must enter through horizontal continuation/residue terms, through non-adiabatic window structure with Fourier mass reaching the prime frequencies, or through genuinely additional arithmetic information.

There is an exact bandlimited version. If

\[
\operatorname{supp}\widehat\chi\subset[-\Omega,\Omega],
\]

then

\[
\boxed{
P_+(\chi_TD_\sigma)=0
\quad\text{for every }T>\Omega/\log2.
}
\tag{4}
\]

For the explicit Fejér-type window

\[
\chi(t)=\left(\frac{\sin t}{t}\right)^2,
\qquad
\widehat\chi(v)=\pi\left(1-\frac{|v|}{2}\right)_+,
\]

all prime leakage is therefore exactly zero once \(T>2/\log2\), while

\[
\boxed{
\|P_+(\chi_TF_\sigma)\|_2^2
\le \frac{\pi}{5T}.
}
\tag{5}
\]

The suppression in (1)--(5) is **input-specific**, not an operator-norm smallness of the localization commutator. If \(M_{\chi_T}\) denotes multiplication by \(\chi_T\), then with the unitary dilation

\[
(U_Tf)(t)=T^{-1/2}f(t/T)
\]

one has exactly

\[
\boxed{
[P_+,M_{\chi_T}]
=U_T[P_+,M_\chi]U_T^{-1}.
}
\tag{6}
\]

Thus every unitarily invariant norm and every singular value of the commutator is unchanged by widening the window. The prime leakage vanishes because the Euler source has a genuine frequency gap \(( -\log2,0)\), while an adiabatic window concentrates its Fourier mass near zero.

This sharpens the source-side target left by `WI-431`: **localization by itself is not the missing arithmetic resource.** The live object is the horizontal transport of the localized Hardy component from a safe line to \(\Re s=1/2+a\), including all residues and boundary/commutator terms, or else a deliberately non-adiabatic localization whose fixed-frequency tails are quantitatively controlled. A proof that merely makes a smooth height window wider and expects the safe-line commutator to reveal more prime information runs in the wrong direction.

## 1. Exact prime spectral-gap estimate

For one frequency \(\lambda>0\),

\[
\widehat{\chi_T(t)e^{-it\lambda}}(\xi)
=T\widehat\chi\bigl(T(\xi+\lambda)\bigr).
\]

Therefore Plancherel gives

\[
\begin{aligned}
\|P_+(\chi_Te^{-it\lambda})\|_2^2
&=\frac1{2\pi}\int_0^\infty
T^2|\widehat\chi(T(\xi+\lambda))|^2d\xi\\
&=\frac{T}{2\pi}
\int_{T\lambda}^\infty|\widehat\chi(v)|^2dv.
\end{aligned}
\tag{7}
\]

On \(\sigma>1\), the Dirichlet series for \(\zeta'/\zeta\) converges absolutely and uniformly, and

\[
\sum_{n\ge2}\Lambda(n)n^{-\sigma}=A_\sigma<\infty.
\]

Multiplication by \(\chi_T\in L^2\) therefore turns the uniformly convergent series into an \(L^2\)-convergent series, so the Riesz projection may be passed through the sum. Since every \(\lambda_n=\log n\ge\log2\), the triangle inequality and (7) give (1).

If \(\chi\) is Schwartz, the tail of \(|\widehat\chi|^2\) decreases faster than any polynomial. The extra prefactor \(T^{1/2}\) in (1) does not change that conclusion: for every \(N>0\),

\[
\|P_+(\chi_TD_\sigma)\|_2=O_{\chi,\sigma,N}(T^{-N}).
\tag{8}
\]

If instead \(\widehat\chi\) is supported in \([-\Omega,\Omega]\), then for \(\xi>0\)

\[
T(\xi+\log n)>T\log2>\Omega,
\]

so every term vanishes identically. This proves (4) without cancellation between primes.

The point is structural: the first prime frequency lies a fixed distance \(\log2\) from the Hardy boundary at \(\xi=0\). A window whose Fourier width shrinks like \(T^{-1}\) cannot bridge that gap in the bulk.

## 2. The zero-frequency Cauchy tail is explicit and only costs \(T^{-1/2}\)

For \(c>0\), `WI-429` uses the classical transform

\[
\widehat{h_c}(\eta)=2\pi e^{c\eta}1_{\eta<0}.
\tag{9}
\]

The product-convolution identity yields, for \(\xi>0\),

\[
\begin{aligned}
\widehat{\chi_Th_c}(\xi)
&=T\int_{-\infty}^0
\widehat\chi(T(\xi-\eta))e^{c\eta}\,d\eta\\
&=\int_{T\xi}^\infty
\widehat\chi(v)e^{-c(v-T\xi)/T}\,dv.
\end{aligned}
\tag{10}
\]

Since the exponential factor has modulus at most one on \(v\ge T\xi\), Plancherel and \(x=T\xi\) give

\[
\begin{aligned}
\|P_+(\chi_Th_c)\|_2^2
&\le
\frac1{2\pi T}
\int_0^\infty
\left(\int_x^\infty|\widehat\chi(v)|\,dv\right)^2dx,
\end{aligned}
\]

which is (2). The constant is finite for every Schwartz window.

For \(\chi(t)=(\sin t/t)^2\),

\[
\widehat\chi(v)=\pi(1-|v|/2)_+.
\]

On \(0\le x\le2\),

\[
\int_x^2\widehat\chi(v)\,dv
=\pi(1-x/2)^2.
\]

Thus

\[
C_\chi
=\frac1{2\pi}
\int_0^2\pi^2(1-x/2)^4dx
=\frac\pi5,
\]

proving (5).

This term is elementary rather than arithmetic. Its spectrum reaches \(0^-\), so no \(\log2\)-type exact gap is available; nevertheless broad localization makes its positive-frequency leakage tend to zero.

## 3. Why the commutator itself does not get small

The Riesz projection commutes with positive dilations because dilating a function rescales its Fourier variable without changing its sign. Also

\[
M_{\chi_T}=U_TM_\chi U_T^{-1}.
\]

Therefore

\[
[P_+,M_{\chi_T}]
=U_T[P_+,M_\chi]U_T^{-1},
\]

which is (6). In particular

\[
\|[P_+,M_{\chi_T}]\|_{2\to2}
=\|[P_+,M_\chi]\|_{2\to2}
\]

for every \(T\). Whenever the commutator is in a Schatten class, all of its Schatten norms are likewise exactly scale invariant.

This is the standard Hankel-operator structure behind Hardy commutators. For example, if the symbol is regular enough that the off-diagonal block \(H_\chi=P_+M_\chi P_-\) is Hilbert--Schmidt, a direct Fourier-kernel calculation gives

\[
\boxed{
\|H_\chi\|_{\mathrm{HS}}^2
=\frac1{4\pi^2}
\int_0^\infty u|\widehat\chi(u)|^2du.
}
\tag{11}
\]

The right side is the homogeneous \(H^{1/2}\)-type seminorm and is exactly invariant under \(\chi(t)\mapsto\chi(t/T)\). Equation (11) is included only to expose the mechanism; no Schatten estimate is needed for (1)--(5).

Thus there are two distinct facts which must not be conflated:

- the localization commutator does not become a small operator under dilation;
- its action on the particular safe-line zeta source becomes small because that source has no prime spectrum near the Hardy boundary.

Any future bridge has to exploit the second fact without incorrectly assuming the first.

## 4. Consequence for the localized defect program

The exact interior identity from `WI-431` is

\[
\chi P_+\frac{B'}B
=P_+(\chi F)-[P_+,\chi]F.
\tag{12}
\]

The present finding shows that evaluating the first positive-frequency source term on a fixed safe line with a broad smooth cutoff gives asymptotically no prime signal at all. Therefore one cannot hope to obtain the `WI-430` defect-energy upper bound merely by proving that this safe-line leakage is small and then informally carrying that smallness into the critical strip.

If a hypothetical off-line zero survives on an interior line, the Hardy projection acquires the reciprocal-distance energy from `WI-429`/`WI-430`. A correct horizontal continuation of a localized quantity must therefore account for the discrepancy between the vanishing safe-line leakage and that interior defect signal. In contour language this is where pole crossings/residues and horizontal-boundary terms must appear. Dropping them would erase exactly the object the method is trying to detect.

There are two clean escape categories.

First, use a non-adiabatic height window with Fourier mass at frequencies at least \(\log2\). A sharp interval cutoff is the elementary example: its Fourier tail does not contract away at prime frequencies. Such leakage is an edge effect and must be estimated with its full boundary cost; it is not generated by the bulk width \(T\).

Second, keep a smooth adiabatic window but derive an exact horizontal transport/explicit-formula identity in which the residues and boundary terms are visible and independently bounded. That is now the most direct continuation of the `WI-429`--`WI-431` branch.

## Prior art and novelty audit

No novelty or priority claim is made for the harmonic-analysis ingredients.

- The one-sided prime spectrum on \(\sigma>1\) is the classical absolutely convergent Euler/Dirichlet-series identity already used in `WI-431`.
- Riesz projections, the identity of Hardy commutators with off-diagonal Hankel operators, and the relation between Schatten membership and Besov/Sobolev regularity are classical. Relevant primary prior art includes V. V. Peller, *Hankel operators of class* \(\mathfrak S_p\) *and their applications*, Sbornik Mathematics 41 (1982), 443--479, and Peller's later monograph *Hankel Operators and Their Applications* (Springer, 2003). Modern commutator/Schatten formulations include M. Lacey, J. Li and B. D. Wick, *Schatten Classes and Commutator in the Two Weight Setting, I. Hilbert Transform*, Potential Analysis 60 (2024), 875--894.
- The scale invariance (6) and the constants in (1)--(5), (11) are derived here directly under the repository's Fourier normalization; they do not depend on importing a sharp theorem from those sources.
- A targeted repository and literature audit did not locate this exact application of the prime spectral gap \(\log2\) to the `WI-431` localized Hardy bridge. Absence from that audit is not evidence of priority. The durable delta is the barrier: **smooth dilation-localization suppresses rather than exposes the independent safe-line prime Hardy signal**, so the missing arithmetic mechanism has to live in non-adiabatic edge frequencies or in the horizontal transport/residue identity.

## Boundary, stress tests, and falsification

1. **This does not rule out localization.** It rules out expecting a fixed smooth profile \(\chi(t/T)\) on a fixed safe line to generate a growing or even persistent positive-frequency prime source. Sharp, modulated, multiscale, or otherwise non-adiabatic windows remain outside the barrier.

2. **The conclusion is safe-line only.** No claim is made that the corresponding interior localized projection is small. Indeed, under non-RH it cannot remain small across every line without residue/boundary compensation; that discrepancy is the next object to quantify.

3. **The pole-cancelling term is retained exactly.** Unlike an argument that silently discards \(1/(s-1)\), equations (2), (5), and (10) show its zero-frequency leakage explicitly.

4. **Bandlimited windows are not compactly supported in height.** Equation (4) is an exact spectral test, while the Schwartz estimate (1)--(3) covers ordinary smooth compactly supported height cutoffs as well.

5. **The commutator operator does not shrink.** Equation (6) prevents a false interpretation of (3) as a generic small-commutator theorem. The gain is specific to the zeta source spectrum.

6. **No RH implication is asserted.** The missing theorem remains a non-oracular horizontal transport estimate strong enough to compare the interior localized defect with `WI-430`'s first-defect quantum.

## Research consequence

The immediate next test should no longer be a generic `L^2` bound for `[P_+,\chi_T]` with a wider and wider smooth window: dilation cannot improve that operator, while the safe-line prime input itself is driven to zero. The load-bearing question is instead to derive the exact horizontally transported localized identity from \(\sigma>1\) to \(1/2+a\), with prime source, pole term, zero residues, and top/bottom boundary terms all kept. A useful theorem must then show that some independently controlled arithmetic part of that identity cannot supply the `WI-430` first-defect quantum.