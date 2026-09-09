# WI-220 — remote frequency separation does not localize free fixed-band screens

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-BARRIER + CLASSICAL-IDENTITY + LITERATURE-CONTEXT`.

WI-218 proves that flattening the selected Maynard--Pratt bow throughout a fixed power-scale band costs `Omega(M)` exponential channels. WI-219 shows that this tariff is order-sharp in the free bow-plus-screen interface by an explicit `Theta(M)` companion, but that companion is co-localized with the bow and is rejected by the local Riemann--von Mangoldt count. The remaining hope was that a sufficiently remote screen might become intrinsically unable to reproduce the bow profile on the full fixed band, allowing the linear rank tariff to be converted into a local zero-count charge.

There is an exact obstruction to that hope **if one keeps the arbitrary-coefficient linear screen relaxation used in WI-215--WI-218**. On any proper subinterval of one Fourier period, the cofinite tail of the integer exponential system is dense in `L^2`. Consequently, for every bow size `M`, every prescribed frequency-exclusion radius `R_M`, and every accuracy `epsilon_M>0`, one can approximate the negative bow on the whole fixed band by a finite linear combination of same-depth functional-equation-pair channels whose phase frequencies all satisfy `|n|>R_M`. The coefficients can be chosen conjugate-symmetrically, so the resulting screen is real on the real axis and respects frequency negation at the linear-channel level.

After the exact WI-218 normalization and unit-box operator, choosing even a fixed absolute pre-box error gives total normalized fixed-band energy `O(1/M)`. Since `M=T^{vartheta+o(1)}` with `vartheta>0`, the physical selected Gallagher energy is then `o(1)` of the raw-prime diagonal on every fixed-multiplicative subslab. Thus **mere frequency separation from the bow cannot be the missing localization theorem inside the free linear screen model**.

This does not construct a zeta-zero screen. The approximation may require far more than `O(M)` channels and arbitrarily large complex coefficients. Actual zeros have positive integral multiplicity and functional-equation-coupled amplitudes rather than free complex coefficients. The result therefore identifies the load-bearing information a successful transport theorem must use: a quantitative term-count/coefficient-norm restriction, the positive/unit-multiplicity zero structure, radial/source constraints, or an equivalent arithmetic coercivity. Support separation alone has no coercive content on a proper fixed band.

## 1. Cofinite Fourier tails are complete on every proper interval

Let `I` be any interval of length strictly less than `1`, and fix an integer `R>=0`. Consider

\[
\mathcal E_R
:=\operatorname{span}\{e^{2\pi i n t}: n\in\mathbb Z,\ |n|>R\}
\subset L^2(I),
\tag{1}
\]

where `span` means finite linear combinations. Then

\[
\boxed{\overline{\mathcal E_R}^{\,L^2(I)}=L^2(I).}
\tag{2}
\]

The proof is elementary. Embed `I` in a unit interval `J=[a,a+1]`. Suppose `f in L^2(I)` is orthogonal to every restricted tail exponential in (1), and extend it by zero to `\widetilde f in L^2(J)`. Its Fourier coefficients on `J` vanish for all `|n|>R`, so `\widetilde f` agrees in `L^2(J)` with a trigonometric polynomial of degree at most `R`. But `\widetilde f=0` almost everywhere on the positive-measure set `J\setminus I`. A nonzero trigonometric polynomial cannot vanish on a set with an accumulation point, hence `\widetilde f=0` and therefore `f=0`. The orthogonal complement of `\mathcal E_R` is trivial, proving (2).

Two features are important. First, `R` is arbitrary and may depend on every external parameter: deleting any finite central frequency band does not change completeness on a proper interval. Second, if the target is real-valued, the approximant can be chosen with conjugate-symmetric coefficients. Indeed, from an approximant `q` replace it by

\[
q_{\rm sym}(t):=\frac{q(t)+\overline{q(t)}}2.
\tag{3}
\]

For a real target this does not increase the `L^2` error, preserves the frequency exclusion `|n|>R`, and enforces `c_{-n}=\overline{c_n}`.

This is the simplest cofinite-lattice instance of classical completeness-radius/nonharmonic-Fourier theory. Beurling--Malliavin's 1967 closure theorem, Redheffer's 1977 treatment of completeness of complex exponentials, and the later spectral-gap language of Poltoratski place the phenomenon in a much broader setting. None of those deeper theorems is load-bearing here: (2) follows directly from ordinary Fourier uniqueness.

## 2. The bow can be approximated by arbitrarily remote same-depth channels

Retain the WI-219 equal-depth bow

\[
D_M(t)=\sum_{j=-p}^{p}e^{2\pi ijt},
\qquad
M=2p+1,
\qquad
B_M(t)=2\cosh(ht)D_M(t),
\tag{4}
\]

with fixed `h>0`, and fix an integer reciprocal harmonic `k`. Choose fixed numbers

\[
0<\sigma<\sigma'<\frac12
\tag{5}
\]

small enough that the outer band

\[
I^+:=[k-\sigma',k+\sigma']
\tag{6}
\]

lies in the support-one regime being observed. Its length is `<1`.

Let `R_M` be any finite sequence satisfying, for example,

\[
R_M>p+A_M
\tag{7}
\]

for an arbitrary prescribed separation `A_M>=0`. By (2), for every `epsilon_M>0` there is a finite trigonometric polynomial

\[
Q_M(t)=\sum_{|n|>R_M}c_{n,M}e^{2\pi int},
\qquad
c_{-n,M}=\overline{c_{n,M}},
\tag{8}
\]

such that

\[
\boxed{
\|D_M+Q_M\|_{L^2(I^+)}<\epsilon_M.
}
\tag{9}
\]

Define the same-depth screen

\[
S_M(t):=2\cosh(ht)Q_M(t).
\tag{10}
\]

Every summand in (10) is a scalar multiple of the same functional-equation-pair profile

\[
2\cosh(ht)e^{2\pi int}
=e^{(h+2\pi in)t}+e^{(-h+2\pi in)t}
\tag{11}
\]

used throughout WI-214--WI-219. Thus no radial-depth advantage is being introduced. Since `2 cosh(ht)` is bounded above and below on the fixed compact interval `I^+`, (9) gives

\[
\boxed{
\|B_M+S_M\|_{L^2(I^+)}
\ll_{h,k,\sigma'}\epsilon_M.
}
\tag{12}
\]

The entire phase support of the screen lies outside the prescribed radius `R_M`; in particular it can be separated from the bow frequencies `[-p,p]` by any finite distance `A_M`. There is therefore no qualitative ``far frequencies cannot imitate the bow'' principle for the free linear screen on a proper fixed band.

## 3. The WI-218 Gallagher box does not restore localization

Let

\[
R_M^{\rm tot}(t):=B_M(t)+S_M(t)
\tag{13}
\]

and pass to the natural coordinate around the reciprocal harmonic,

\[
s=M(t-k),
\qquad
r_M(s):=\frac1M R_M^{\rm tot}\!\left(k+\frac{s}{M}\right).
\tag{14}
\]

On the outer natural band `|s|<=sigma' M`, the change of variables gives exactly

\[
\int_{|s|\le\sigma' M}|r_M(s)|^2\,ds
=\frac1M
\int_{I^+}|R_M^{\rm tot}(t)|^2\,dt
\ll\frac{\epsilon_M^2}{M}.
\tag{15}
\]

WI-218 uses

\[
(K_{\eta_M}f)(s)
:=\int_0^1e^{\eta_M v}f(s+v)\,dv,
\qquad
\eta_M=\frac{\log T}{2dM}=o(1).
\tag{16}
\]

For the smaller band `|s|<=sigma M`, `[s,s+1]` lies inside the outer band for all sufficiently large `M`. Cauchy--Schwarz followed by Fubini gives the uniform operator estimate

\[
\int_{|s|\le\sigma M}|K_{\eta_M}r_M(s)|^2\,ds
\le e^{2\eta_M}
\int_{|u|\le\sigma' M}|r_M(u)|^2\,du.
\tag{17}
\]

Therefore

\[
\boxed{
\int_{|s|\le\sigma M}|K_{\eta_M}r_M(s)|^2\,ds
\ll\frac{\epsilon_M^2}{M}.
}
\tag{18}
\]

Take merely `epsilon_M=1`. Every fixed-multiplicative subslab inside the band has nonnegative energy bounded by the total in (18). The WI-217--WI-218 physical dictionary multiplies that normalized subslab energy by `asymp log T` when it is divided by the corresponding raw-prime Gallagher diagonal. Hence

\[
\boxed{
\frac{\text{selected bow+remote-screen Gallagher energy}}
{\text{raw-prime Gallagher diagonal}}
\ll\frac{\log T}{M}=o(1)
}
\tag{19}
\]

on every such subslab because `M=T^{\vartheta+o(1)}` with fixed `\vartheta>0`.

Thus even the exact box/tilt observable that produced the WI-218 fixed-band `Omega(M)` tariff cannot convert *support distance by itself* into a positive residue floor once arbitrary coefficients and unbounded channel count are retained.

## 4. What this does and does not close

There is no conflict with WI-215. That finding fixes the channel count `n` and proves a positive separation from the sinc target. The approximation above may require a channel count tending to infinity very rapidly with `M`, `R_M`, and the requested accuracy. Completeness says only that some finite approximant exists; it supplies no useful quantitative complexity bound.

There is likewise no conflict with WI-218. Its theorem says that uniformly small fixed-band residue requires `n >> M`; (8) is completely free to pay that tariff and much more. Nor does this supersede WI-219: that finding is stronger in a different direction, producing an explicit `Theta(M)` same-depth screen with coefficient `+1` and functional-equation/conjugation symmetry, but at the price of co-localization and an impossible local zero count. WI-220 instead proves that **remoteness itself is not an obstruction in the relaxed linear class**, while deliberately giving up any control on coefficient size or channel count.

Most importantly, (8)--(19) are not a zero configuration. Actual zeta zeros do not carry arbitrary complex scalar coefficients. Their multiplicities are positive integers, their functional-equation partners are coupled, and the available number of labels in a physical ordinate window is constrained by Riemann--von Mangoldt. Large coefficients in a free exponential approximation cannot simply be declared to be zero multiplicities without paying count, and coefficient phases cannot be inserted independently of the zero ordinates. Those are exactly the structures discarded by the WI-215--WI-218 enlargement.

Consequently the surviving transport question is now quantitative rather than qualitative. A useful theorem must control at least one of the following jointly with remote frequency separation:

- the number of remote channels needed for a given fixed-band error;
- an `ell^1`/`ell^2` coefficient cost, preferably in the source-normalized weights actually supplied by zeros;
- positivity/integral multiplicity and functional-equation coupling;
- radial-depth cost or a source-side norm that cannot be compensated by arbitrary coefficients.

A proof that only says ``the screen frequencies lie far from the bow frequencies'' cannot close the bow, because the cofinite Fourier tail remains complete on every proper fixed band.

## 5. Prior-art, novelty, and falsification audit

The exact completeness lemma (2) is classical/elementary Fourier analysis, not a novelty claim. The broader literature audit checked the Beurling--Malliavin completeness-radius theory (A. Beurling and P. Malliavin, *On the closure of characters and the zeros of entire functions*, Acta Math. 118 (1967), 79--93), Redheffer's *Completeness of sets of complex exponentials*, Adv. Math. 24 (1977), 1--62, and Poltoratski's *Spectral gaps for sets and measures*, Acta Math. 208 (2012), 151--209. Those works establish the surrounding density/completeness/spectral-gap framework; no theorem from them is needed for (2).

The nearby Mathia deductions are different. WI-215 is a fixed-rank impossibility theorem, WI-216--WI-218 quantify how rank must grow with observation width, and WI-219 supplies a co-localized positive-coefficient `Theta(M)` upper screen. The new deduction is the combination of the cofinite-tail completeness (2) with the exact WI-218 bow normalization and Gallagher box, yielding (19) for screens placed beyond an arbitrary prescribed phase radius. A targeted search found the classical completeness theory but no zeta-specific statement of this remote-support no-go; absence from that search is not used as a priority claim.

The finding would fail if the interval had full Fourier-period length: on a full unit interval the missing central Fourier modes are orthogonal to the cofinite tail and (2) is false. It would also fail as a statement about actual zero populations if one silently treated the free coefficients `c_{n,M}` as admissible positive multiplicities. Both boundaries are load-bearing and are why the result is a barrier to a *support-only localization proof*, not a counterexample to the desired zeta theorem.

## Research consequence

The fixed-band bow program should not spend further cycles trying to convert WI-218's linear screen tariff into local zero count by a qualitative uncertainty slogan such as ``remote exponentials cannot reproduce a local bow.'' They can in the exact relaxed screen space already used to prove the rank lower bounds, even when every screen frequency is pushed beyond an arbitrarily large finite exclusion radius.

The RH-facing gate is sharper: prove a **quantitative remote-approximation lower bound with the actual zero coefficient/count structure retained**, or prove a source-side coercive norm that charges the coefficient inflation required by remote superposition. This is precisely the information that the co-localized WI-219 companion violates by count and that the free WI-220 approximation is allowed to ignore.