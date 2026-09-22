# PC-401 — shell-2 indefinite Krein multiplication keeps a universal spectrum

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-NEGATIVE` for the canonical indefinite-metric multiplication/Jacobi continuation of PC-400 as an independent RH mechanism. This does not classify genuinely cross-shell indefinite operators, source-forced generalized eigenvalue pencils, or nonlinear operations on the signed measure.

PC-400 classifies the positive Hankel/Jacobi route attached to the shell-2 Chen moments and explicitly leaves indefinite constructions outside its no-go. The first canonical indefinite continuation can be classified without adding any representation choice. For every non-prime-power shell, keep the signed measure itself rather than replacing it by total variation and place its coordinate multiplication operator in the natural Krein space.

The result is rigid: the indefinite metric remembers the full signed cyclotomic profile, but the multiplication spectrum remains the same interval `[0,log 2]` as in the positive case. Thus changing the metric from positive to indefinite does not move arithmetic into the spectral set; it only moves the already-decoded shell information into the signed spectral measure/fundamental symmetry.

## 1. The shell-2 signed measure has full support

From PC-399 and PC-400, with

\[
X_n(z)=\log\Phi_n(z),\qquad t=X_2(z)=\log(1+z),\qquad L=\log2,
\]

the one-sided Chen ladder is the moment sequence of

\[
\mu_n=(X_2)_*(dX_n),
\qquad
 d\mu_n(t)=w_n(t)\,dt,
\]

where

\[
\boxed{w_n(t)=e^tX_n'(e^t-1).}
\tag{1}
\]

For `n>1`, `Phi_n` has no zero on `[0,1]`, so `w_n` is real analytic on a neighborhood of `[0,L]`. It is not identically zero because `Phi_n` is nonconstant. Hence its zeros are isolated and, on this compact interval, finite. Consequently

\[
\boxed{\operatorname{supp}|\mu_n|=[0,L]}
\tag{2}
\]

for every shell `n>1`.

If `n` is not a prime power, PC-400 gives `mu_n([0,L])=Lambda(n)=0` while PC-399 gives `mu_n != 0`. A continuous nonzero density of zero total mass must take both signs. Therefore `w_n` has a genuine positive/negative decomposition, but that decomposition does not remove any open subinterval from the support of `|mu_n|`.

## 2. The canonical Krein realization has the same spectrum for every shell

Let

\[
\mathcal H_n=L^2(|\mu_n|),
\qquad
(J_nf)(t)=\operatorname{sgn}(w_n(t))f(t).
\tag{3}
\]

Because `w_n` is nonzero almost everywhere, `J_n` is a bounded self-adjoint involution on `H_n`. It defines the natural indefinite inner product

\[
[f,g]_n:=\langle J_nf,g\rangle_{\mathcal H_n}
=\int_0^L f(t)\overline{g(t)}\,d\mu_n(t).
\tag{4}
\]

Now take the coordinate multiplication operator

\[
(M_tf)(t)=t f(t).
\tag{5}
\]

`M_t` is bounded and self-adjoint in the Hilbert space `H_n`, and it commutes with `J_n`. Therefore

\[
[M_tf,g]_n=[f,M_tg]_n,
\tag{6}
\]

so it is also self-adjoint with respect to the Krein metric in the standard `J`-self-adjoint sense.

Its Hilbert-space spectrum is the essential range of the coordinate function with respect to `|mu_n|`. Equation (2) therefore gives the exact shell-independent identity

\[
\boxed{
\sigma(M_t)=[0,\log2]
\qquad\text{for every }n>1.
}
\tag{7}
\]

In particular, allowing the non-prime-power shells to remain indefinite does **not** restore an arithmetic spectral-set motion suppressed by the positive repair in PC-400. The same universal interval persists before any positive scalarization.

## 3. All shell arithmetic sits in the signed spectral measure, not the spectral set

Let `E` be the ordinary projection-valued spectral measure of `M_t` on `H_n`, and let `1` denote the constant cyclic vector. Then for every Borel set `B subset [0,L]`,

\[
\boxed{
[E(B)1,1]_n
=\int_B d\mu_n.
}
\tag{8}
\]

Thus the Krein spectral data seen from the canonical cyclic vector is exactly the original signed measure. Its moments are

\[
[M_t^k1,1]_n
=\int_0^L t^k\,d\mu_n(t)
=k!\,J_{2^k,n}.
\tag{9}
\]

PC-399 already proves that this moment sequence reconstructs `mu_n`, hence `Phi_n` and the shell index itself. The indefinite realization therefore preserves all arithmetic information, but for exactly the same generic compact-moment reason as the Chen decoder. Nothing new is created by calling that information a signed spectral measure.

This separates two notions that are easy to conflate:

\[
\text{operator spectrum}=[0,L]
\quad\text{while}\quad
\text{cyclic signed spectral measure}=\mu_n.
\tag{10}
\]

The first is universal; the second is information-complete but already present before spectralization.

## 4. Multiplying by the metric only exposes the existing sign partition

A natural Hilbert-self-adjoint object associated with the Krein realization is

\[
J_nM_t=M_tJ_n,
\tag{11}
\]

which is simply multiplication by

\[
t\,\operatorname{sgn}(w_n(t)).
\tag{12}
\]

Hence

\[
\boxed{
\sigma(J_nM_t)
=\overline{\operatorname{ess\,ran}\bigl(t\operatorname{sgn}(w_n(t))\bigr)}.
}
\tag{13}
\]

Any shell dependence in (13) is therefore nothing more than the location of the sign intervals of the already-known radial-flux density. No nonlocal interaction, cross-shell coupling, or new spectral parameter has appeared. A matched non-arithmetic analytic signed density on `[0,L]` with the same sign partition produces exactly the same spectral set (13).

Thus even the simplest attempt to turn the fundamental symmetry itself into a Hilbert operator does not manufacture a new arithmetic mechanism; it only re-labels the sign geometry already contained pointwise in `w_n`.

## 5. Why an indefinite Jacobi recurrence is not an automatic escape

For a signed moment functional, ordinary positive Favard theory no longer applies automatically. Hankel minors may vanish, so a scalar orthogonal-polynomial recurrence need not exist globally without a quasi-definiteness/nondegeneracy hypothesis. When such indefinite recurrences do exist, their ambient theory is classical: indefinite Hamburger/Stieltjes moment problems are formulated through generalized Nevanlinna functions, generalized Jacobi matrices, continued fractions, and Hermitian operators in Krein/Pontryagin spaces.

Representative prior art includes Vladimir Derkach and Ivan Kovalyov, **The Schur algorithm for an indefinite Stieltjes moment problem**, *Mathematische Nachrichten* 290 (2017), 1637–1662, DOI `10.1002/mana.201600189`, which develops the nondegenerate truncated indefinite Stieltjes problem and generalized Stieltjes continued fractions, and Jonathan Eckhardt and Aleksey Kostenko, **The Classical Moment Problem and Generalized Indefinite Strings**, *Integral Equations and Operator Theory* 90 (2018), article 23, DOI `10.1007/s00020-018-2446-6`, which places moment sequences in the spectral theory of generalized indefinite strings. Derkach's earlier indefinite moment work and the Krein--Langer program already provide the standard operator-theoretic setting for such extensions.

The line-specific statement here is not novelty of indefinite moment theory. It is the exact Prime-Circle reduction: because the shell-2 coordinate is a homeomorphism and `|mu_n|` has full support, the most direct indefinite multiplication operator has universal spectrum, while its metric spectral measure is precisely the generic decoder of PC-399.

## 6. Consequence and surviving boundary

The canonical continuation

\[
\text{signed shell-2 moments}
\longrightarrow
L^2(|\mu_n|),\ J_n
\longrightarrow
M_t\text{ as a Krein-self-adjoint operator}
\]

therefore does not supply a new route to the zeta zeros or critical line. It preserves the shell exactly, but only in the signed cyclic measure; the operator spectrum is fixed by the coordinate interval.

This closes the most immediate indefinite-metric loophole left by PC-400. It does **not** rule out a source-forced generalized eigenvalue pencil whose two forms come independently from Prime-Circle geometry, an indefinite operator coupling several shells or refinement levels before moment reduction, or a nonlinear operation whose invariant is not determined by one signed measure alone. Those are genuinely additional structures and require separate derivation and matched-control audits.

## Audit / falsification tests

This finding fails if any of the following occurs:

1. the shell-2 Chen measure does not have density (1);
2. a nonzero `w_n` can vanish on an open subinterval of `[0,L]`;
3. `supp |mu_n|` is smaller than `[0,L]`;
4. multiplication by the coordinate on `L^2(|mu_n|)` has spectrum different from its essential range;
5. `J_n` does not commute with coordinate multiplication;
6. the signed cyclic spectral measure in (8) is not exactly `mu_n`.

Items 1--6 are exact consequences of PC-399/PC-400, analyticity of the cyclotomic logarithmic derivative on `[0,1]`, and standard multiplication-operator/Krein-space theory. The finding makes no claim that every indefinite Jacobi pencil is spectrally trivial and no claim about genuinely cross-shell or cross-level indefinite dynamics.