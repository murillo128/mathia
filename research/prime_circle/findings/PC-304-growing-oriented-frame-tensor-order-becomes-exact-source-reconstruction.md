# PC-304 — growing oriented-frame tensor order becomes exact source reconstruction

**Status:** `EXACT-DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the growing-tensor-order escape left open by PC-303.

PC-303 classifies every **fixed finite** tensor contraction of the oriented Prime-Circle frames as joint additive Fourier/polyspectral source data, but deliberately leaves tensor degree growing with the modulus open. That escape can now be bounded sharply. At prime modulus `q`, powers of a single oriented frame coordinate already expose the complete additive DFT of the source once the tensor degree reaches `q-1`; inverse DFT then reconstructs the source exactly. For the canonical prime source there is an additional exact simplification: none of its Fourier coefficients vanish, so its full cyclic bispectrum is a complete translation-invariant descriptor up to the unavoidable cyclic shift.

Thus growing tensor order can certainly recover more information than any fixed order, but the endpoint is not a new Prime-Circle carrier: it is exact reconstruction of the input source itself. Higher translation-invariant polyspectra likewise do not add orbit information once the full bispectrum is available. This does **not** rule out a load-bearing intermediate scaling regime, a geometry-forced operator acting before reconstruction, or genuinely cross-level/mixed-conductor interactions.

Let `q >= 5` be prime, let

\[
\zeta_q=e^{2\pi i/q},
\qquad
P_q=\{\ell:2<\ell<q,\ \ell\text{ prime}\},
\qquad
L_q=|P_q|,
\]

and let `nu_q` be the uniform probability law on `P_q`. Write its additive Fourier transform as

\[
F_q(a)
:=\widehat\nu_q(a)
=\frac1{L_q}\sum_{\ell\in P_q}\zeta_q^{a\ell},
\qquad a\in\mathbb Z/q\mathbb Z.
\tag{1}
\]

The argument below in fact starts for an arbitrary probability law on `Z/qZ`; primality of the source residues is used only in identifying the canonical Prime-Circle source as a nonempty proper subset.

## 1. One oriented coordinate generates the complete source DFT

Retain the PC-296--303 oriented frame coordinates

\[
x_{m,s}(h)=N^{-1/2}\zeta_q^{msh}.
\tag{2}
\]

As soon as the frame contains `m=1` and `h=1`, one coordinate is

\[
y_s:=x_{1,s}(1)=N^{-1/2}\zeta_q^s.
\tag{3}
\]

For any probability law `mu` on `Z/qZ` and any integer `d>=1`, its degree-`d` tensor moment is exactly

\[
\boxed{
\mathbb E_{s\sim\mu}[y_s^d]
=N^{-d/2}\widehat\mu(d\bmod q).
}
\tag{4}
\]

Therefore the moments of degrees

\[
1,2,\ldots,q-1
\]

recover every nonzero Fourier mode of `mu`; the zero mode is already known from normalization, `widehat mu(0)=1`. Hence tensor degree growing only linearly with `q` exposes the **entire** additive DFT. Fourier inversion then gives

\[
\boxed{
\mu(s)=\frac1q\sum_{a\bmod q}
\widehat\mu(a)\zeta_q^{-as}.
}
\tag{5}
\]

No joint source law, Gram matrix, or large frame packet is needed for this completeness statement. A single oriented coordinate and its powers suffice. Consequently, the limiting endpoint of the growing-degree hierarchy is exact source reconstruction rather than an additional hidden invariant.

This is an information statement, not an RH mechanism. For the canonical source, (5) merely reconstructs which residues below `q` were prime; it does not create a spectral parameter, gamma factor, functional-equation symmetry, explicit-formula kernel, or critical-line constraint.

## 2. The canonical prime source has no Fourier zeros

The canonical source enjoys a useful exact property that removes the usual nonvanishing caveat in cyclic bispectrum inversion.

Let `A` be any nonempty proper subset of `Z/qZ`, with `q` prime, and define

\[
S_A(a):=\sum_{r\in A}\zeta_q^{ar}.
\]

For every `a != 0 mod q`, multiplication by `a` permutes `Z/qZ`, so `aA` is again a nonempty proper subset. Suppose for contradiction that `S_A(a)=0`. Choose representatives `0,...,q-1` for `aA` and form

\[
Q_A(X):=\sum_{r\in aA}X^r\in\mathbb Z[X].
\tag{6}
\]

Then `Q_A(zeta_q)=0`. Since the minimal polynomial of `zeta_q` over `Q` is

\[
\Phi_q(X)=1+X+\cdots+X^{q-1},
\tag{7}
\]

of degree `q-1`, `Phi_q` must divide `Q_A` in `Q[X]`. But `deg Q_A <= q-1`. If `deg Q_A<q-1`, this is impossible because `Q_A` is nonzero. If `deg Q_A=q-1`, divisibility forces `Q_A=c Phi_q`; its `0/1` coefficients then force `c=1` and `A=Z/qZ`, again a contradiction. Therefore

\[
\boxed{
S_A(a)\ne0
\quad\text{for every nonempty proper }A\subset\mathbb Z/q\mathbb Z
\text{ and every }a\ne0.
}
\tag{8}
\]

For `q>=5`, `P_q` is nonempty and proper, so

\[
\boxed{F_q(a)\ne0\quad\text{for every }a\bmod q.}
\tag{9}
\]

The zero mode is `F_q(0)=1`. Thus the native Prime-Circle prime source has a nowhere-vanishing additive Fourier transform at every prime modulus in scope.

Equation (8) is a prime-modulus special case of the classical theory of vanishing sums of roots of unity. Lam and Leung, **On Vanishing Sums of Roots of Unity**, *Journal of Algebra* 224 (2000), 91--109, DOI `10.1006/jabr.1999.8089`, gives a much broader classification. Here the elementary cyclotomic-minimal-polynomial proof is enough and keeps the project-local dependency explicit.

## 3. The full bispectrum is exactly complete up to translation

For any probability law `mu` on `Z/qZ` with Fourier transform `F`, define the cyclic bispectrum

\[
B_F(a,b)
:=F(a)F(b)\overline{F(a+b)}.
\tag{10}
\]

For the canonical source all `F_q(a)` are nonzero by (9). Suppose another probability law has Fourier transform `G` and the same full bispectrum,

\[
B_G(a,b)=B_F(a,b)
\qquad\text{for all }a,b\bmod q.
\tag{11}
\]

Because `F(0)=G(0)=1`, setting `b=0` gives

\[
|G(a)|^2=|F(a)|^2.
\tag{12}
\]

Hence `G(a)` is also nonzero and the ratio

\[
r(a):=\frac{G(a)}{F(a)}
\tag{13}
\]

has modulus one. Dividing (11) by the nonzero bispectrum factors yields

\[
r(a)r(b)\overline{r(a+b)}=1,
\]

so

\[
\boxed{r(a+b)=r(a)r(b).}
\tag{14}
\]

Thus `r` is a character of the cyclic group. There is some `c mod q` such that

\[
r(a)=\zeta_q^{ca},
\qquad
G(a)=\zeta_q^{ca}F(a).
\tag{15}
\]

With the translation convention

\[
(\tau_c\mu)(s)=\mu(s-c),
\]

(15) is exactly the Fourier transform of a cyclic translate. Therefore

\[
\boxed{
B_G=B_F
\quad\Longrightarrow\quad
G=\widehat{\tau_c\mu}
\text{ for a unique cyclic shift }c
\text{ modulo any stabilizer.}
}
\tag{16}
\]

For the canonical source there is no genericity assumption: the nonvanishing needed by the standard cyclic-bispectrum inversion is guaranteed exactly by prime modulus and proper support.

This does **not** declare cyclic translation to be a physical gauge of Prime-Circle geometry. The common anchor can make absolute phase/origin meaningful. Equation (16) only says that if one chooses the translation-invariant polyspectral route identified in PC-303, the cubic invariant already determines the entire translation orbit. Higher translation-invariant orders cannot supply additional orbit-discriminating information.

## 4. What growing tensor order actually buys

PC-303 left growing tensor order open because a fixed degree sees only a fixed finite Fourier/polyspectral packet. Equations (4)--(5) identify the endpoint of that escape exactly:

\[
\boxed{
\text{oriented tensor moments through degree }q-1
\Longleftrightarrow
\text{complete additive DFT}
\Longleftrightarrow
\text{exact source law}.
}
\tag{17}
\]

The first equivalence is constructive via (4); the second is ordinary finite Fourier inversion. This means that increasing tensor order can pass every fixed-order information bottleneck, but only by approaching a lossless encoding of the original source data.

Once all frequencies are exposed, (9)--(16) sharpen the translation-invariant side:

\[
\boxed{
\text{full source bispectrum}
\Longleftrightarrow
\text{source up to cyclic translation}
}
\tag{18}
\]

for the canonical prime source. Thus there is no unbounded hierarchy of progressively new translation-invariant source information waiting beyond the bispectrum. The hierarchy saturates informationally.

The distinction from PC-303 is important. PC-303 says **fixed finite order is classical polyspectral data**. PC-304 says **allowing the order to grow far enough does not reveal a new carrier either; it becomes complete source reconstruction, and the full invariant orbit is already bispectrally complete**.

## 5. Prior-art and novelty audit

Both abstract ingredients are classical. The vanishing-sum statement belongs to cyclotomic theory; Lam--Leung gives the broad roots-of-unity context. Bispectral completeness on finite groups is standard higher-order harmonic analysis. Ramakrishna Kakarala, **Bispectrum on finite groups**, ICASSP 2009, DOI `10.1109/ICASSP.2009.4960328`, develops finite-group bispectra and inversion under nonvanishing Fourier hypotheses. Tamir Bendory, Dan Edidin and Shay Kreymer, **Signal recovery from a few linear measurements of its high-order spectra**, arXiv:`2103.01551`, places bispectrum/higher-order spectra explicitly in cyclic-shift orbit recovery and proves strong completeness/compression results.

Accordingly, neither roots-of-unity nonvanishing nor bispectral inversion is claimed as new mathematics. The project-local exact delta is their synthesis with the Prime-Circle oriented-frame hierarchy: **the specific growing-order escape left open by PC-303 reaches the complete DFT using powers of one native frame coordinate, while the canonical prime support automatically removes Fourier-zero obstructions to exact bispectral orbit recovery.**

This is a negative/classification result for the research program, not a positive bridge to zeta. It survives the novelty audit precisely because it does not rebrand the classical ingredients as a new spectral construction.

The derivation is self-contained and the literature is novelty context rather than a load-bearing dependency, so no new `SOURCES.md` anchor is required.

## 6. Falsification and reproducibility controls

Equation (4) is directly checkable for any finite law `mu`: enumerate the source residues, average `y_s^d`, and compare with the DFT coefficient at frequency `d mod q`. Degrees `1,...,q-1` followed by the inverse transform (5) must reproduce every source weight exactly up to floating-point error.

Equation (8) has an exact algebraic falsification criterion: a counterexample would be a nonempty proper `0/1` polynomial of degree at most `q-1` divisible by `Phi_q`, contradicting the minimal-polynomial argument. Direct enumeration for the native prime sets at `q=5,7,11,13,17,19,23,29,31` also gives nonzero magnitude at every Fourier mode, as predicted.

Equation (16) can be tested by computing the full bispectrum of any nowhere-zero cyclic signal, translating it by each residue, and confirming that the bispectrum is unchanged. Conversely, reconstruct phase ratios from equal bispectra: (14) must hold for every pair and hence force the ratio vector to one of the `q` cyclic characters. Any equal-bispectrum pair with a non-character ratio would refute the completeness claim.

## 7. Consequence for the research frontier

The straightforward “escape PC-303 by increasing tensor order with `q`” is therefore not by itself a new Prime-Circle mechanism. At sufficient order the construction simply stores the source exactly. Any proposed RH relevance must come from an additional structure that does something mathematically nontrivial with that information rather than from the amount of recoverable source information itself.

Three possibilities remain outside this boundary. First, an intermediate joint limit such as `d=d(q)<<q` could have a nontrivial asymptotic transition before full reconstruction; PC-304 does not classify such scaling laws. Second, a geometry-forced nonlinear/operator evolution could act on the oriented fields before they are reduced to their Fourier source coordinates. Third, genuinely cross-level or mixed-conductor interactions can couple several moduli in a way that is not equivalent to reconstructing each source separately and then post-processing it.

Those are materially different targets. Merely increasing tensor degree, or invoking still higher translation-invariant polyspectra after the complete Fourier packet is available, is now exhausted as an information-gain argument.