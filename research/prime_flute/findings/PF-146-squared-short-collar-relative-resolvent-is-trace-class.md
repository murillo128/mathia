# PF-146 — squared short-collar relative resolvent crosses the trace-class endpoint

**Status:** `EXACT-DERIVED + LITERATURE-BRIDGE + BOUNDARY`. PF-112 and PF-127 show that the first relative resolvent of two genuinely different two-dimensional metrics is not trace class, even though the matched collapsing collar is `S_r`-benign for every `r>1`. The present calculation shows that this local trace obstruction disappears after one further resolvent power: on every fixed central matched collar, the difference of the **squares** of the resolvents is trace class with norm suppressed by the pinching core length. Classical Birman--Kato invariance then identifies global trace class for this squared-resolvent difference as a sufficient alternative route to complete wave operators. The result is local and does not establish that global trace-class statement.

## Claim

Use exactly the fixed-central-collar setup of PF-127. For fixed `R>0`, let

\[
C_{L,R}=(-R,R)\times \mathbb S^1,
\qquad
 ds_L^2=dr^2+L^2\cosh^2r\,d\theta^2,
\]

with Dirichlet boundary at `r=\pm R`, and assume the standard collar width satisfies `w(L)>R`. For `L'=e^tL` with `|t|\le t_0` and `w(L')>R`, put both Dirichlet Laplacians on the common Hilbert space used in PF-127 and write

\[
R_L=(\Delta_L^D+1)^{-1},
\qquad
R_{L'}=(\Delta_{L'}^D+1)^{-1}.
\]

Then

\[
\boxed{
R_{L'}^2-R_L^2\in\mathcal S_1,
\qquad
\|R_{L'}^2-R_L^2\|_{\mathcal S_1}
\le C_{R,t_0}|t|L^3.
}
\tag{1}
\]

For a PF-004 canonical separator in the exact prime flute whose leftmost prime label is at least `P`, let `L_+` be the matched exact shift-clone length. PF-109 gives

\[
\left|\log\frac{L_+}{L}\right|=O(P^{-3})
\]

uniformly even along pinching sequences. Hence

\[
\boxed{
\|R_{L_+}^2-R_L^2\|_{\mathcal S_1}
\le C_R P^{-3}L^3.
}
\tag{2}
\]

In particular the pure central short-collar channel is not an obstruction to a **trace-class resolvent-power** criterion for scattering, despite the sharp failure of trace class for the first relative resolvent.

## 1. The zero Fourier mode still cancels exactly

PF-127 places the collar Laplacian in the Fourier decomposition

\[
H_{m,L}
=H_0+
\frac{(2\pi m)^2}{L^2}\operatorname{sech}^2r,
\]

where `H_0` is independent of `L`. Let

\[
R_{m,L}=(H_{m,L}+1)^{-1},
\qquad
A_m=R_{m,L'}-R_{m,L}.
\]

For `m=0`,

\[
R_{0,L'}=R_{0,L},
\]

so not only the first relative resolvent but every resolvent-power difference vanishes exactly in the only transverse mode surviving at fixed energy as `L\to0`.

## 2. Two Hilbert--Schmidt factors give trace class mode by mode

For `m\ne0`, PF-127 equation (14) with Schatten exponent `2` gives, uniformly for bounded `t`,

\[
\|R_{m,L}\|_{\mathcal S_2}
+
\|R_{m,L'}\|_{\mathcal S_2}
\le
C_{R,t_0}
\left(\frac{L}{|m|}\right)^{3/2}.
\tag{3}
\]

PF-127 equation (18), again with exponent `2`, gives

\[
\boxed{
\|A_m\|_{\mathcal S_2}
\le
C_{R,t_0}|t|
\left(\frac{L}{|m|}\right)^{3/2}.
}
\tag{4}
\]

No new collar asymptotic is needed. The elementary identity

\[
R_{m,L'}^2-R_{m,L}^2
=R_{m,L'}A_m+A_mR_{m,L}
\tag{5}
\]

and Schatten Hölder `\mathcal S_2\mathcal S_2\subset\mathcal S_1` imply

\[
\begin{aligned}
\|R_{m,L'}^2-R_{m,L}^2\|_{\mathcal S_1}
&\le
\bigl(\|R_{m,L'}\|_{\mathcal S_2}
      +\|R_{m,L}\|_{\mathcal S_2}\bigr)
\|A_m\|_{\mathcal S_2}\\
&\le
C_{R,t_0}|t|
\left(\frac{L}{|m|}\right)^3.
\end{aligned}
\tag{6}
\]

The Fourier decomposition is orthogonal. Since the `m=0` block vanishes and

\[
\sum_{m\ne0}|m|^{-3}<\infty,
\]

summing (6) proves (1). Inserting PF-109's `t=O(P^{-3})` proves (2).

## 3. Why the squared resolvent is a different scattering target

The local obstruction in PF-112 is genuinely sharp for the **first** relative resolvent: in two dimensions its nonzero principal symbol has order `-2`, exactly the weak-trace endpoint, so a non-isometric local metric change is not in `\mathcal S_1`. Equation (1) does not contradict that result. Multiplying by one additional resolvent contributes another two derivatives of smoothing; in the separated collar model this appears concretely as the second Hilbert--Schmidt factor in (5)--(6).

This matters because trace class of the first relative resolvent is not the only classical scattering gate. Let `H,H_+\ge0` be two self-adjoint Laplacians after transport to one fixed Hilbert-space identification. If one could prove globally that

\[
\boxed{
(H_++1)^{-2}-(H+1)^{-2}\in\mathcal S_1,
}
\tag{7}
\]

then Kato--Rosenblum applies to the bounded self-adjoint pair

\[
\Phi(H_+),\Phi(H),
\qquad
\Phi(\lambda)=(1+\lambda)^{-2}.
\]

The Birman--Kato invariance principle for strictly monotone `\Phi` then transfers existence and completeness of those wave operators back to the original pair `H_+,H` (with only the conventional interchange of `+/-` for a decreasing `\Phi`). Thus (7) is a sufficient **alternative** to the Güneysu--Thalmaier weighted-metric criterion pursued in PF-128--PF-145.

PF-146 establishes only that the most singular central collar block is compatible with this alternative: its contribution is already trace class and tends to zero at the quantitative rate (2).

## 4. Adversarial controls and limitations

Several stronger conclusions are explicitly excluded.

First, the Dirichlet collar is a localized block. Cutting the surface removes the collar/body transmission terms. Trace class of the direct sum of central collar blocks does not imply (7) for the uncut infinite flute; interface commutators, thick-body contributions, and infinite gluing must still be controlled under one globally coherent identification.

Second, (1) is proved on a **fixed central width** `R`. No uniform claim is made with `R` growing like the full collar width `w(L)\sim\log(1/L)`. The constants in the one-dimensional estimates may depend on `R`.

Third, PF-112 remains intact: `R_{L'}-R_L\notin\mathcal S_1` whenever the two collar metrics genuinely differ. Passing to squared resolvents changes the operator being compared; it does not repair trace class of the first relative resolvent and does not create a first-resolvent Fredholm determinant.

Fourth, a future proof of (7) would imply equivalence of the absolutely continuous scattering class, not equality of scattering matrices, resonances, discrete spectra, relative determinants, Selberg/Ruelle objects, or any RH statement. The comparison surface is the exact all-composite shift clone, so any property forced solely by such an equivalence would in fact be adverse evidence for primality-specific spectral selection.

Finally, the result does not solve the PF-145 geometric trace-welding problem. It identifies a separate operator-theoretic route that may bypass the need to verify the specific Güneysu--Thalmaier weighted metric integral; whether its global interface estimates are easier is an open question.

## 5. Prior art and novelty audit

No novelty is claimed for Schatten Hölder, the algebraic identity (5), Kato--Rosenblum, or the Birman--Kato invariance principle. The classical source is Tosio Kato, *Wave operators and unitary equivalence*, Pacific Journal of Mathematics 15 (1965), 171--180, DOI `10.2140/pjm.1965.15.171`; Birman's 1963 work is the earlier origin of the invariance principle for broad classes of functions. Martin Schechter, *The invariance principle*, Commentarii Mathematici Helvetici 54 (1979), 111--125, DOI `10.1007/BF02566259`, gives a later treatment and explicitly situates the Birman--Kato theorem.

Higher resolvent powers crossing a trace-class threshold are also classical in elliptic spectral theory. For example, J. Behrndt, M. Langer, and V. Lotoreichik, *Trace formulae and singular values of resolvent power differences of self-adjoint elliptic operators*, Journal of the London Mathematical Society 88 (2013), 319--337, DOI `10.1112/jlms/jdt012`, proves trace-class results for sufficiently high resolvent-power differences in a different elliptic boundary-condition setting. That paper does not address degenerating infinite-type hyperbolic collars or the prime/shift comparison here.

Directed searches around degenerating hyperbolic collars, Schatten resolvent differences, and pinching found the standard literature on heat/resolvent convergence and spectral degeneration, but no source supplying the project-specific estimate (1), its `L^3` collapse factor, or the specialization (2). The durable Mathia content is therefore only the exact bridge

\[
\boxed{
\text{PF-127 matched collar }\mathcal S_2\text{ estimates}
\Longrightarrow
\text{squared relative resolvent }\mathcal S_1
\text{ with }O(|t|L^3),
}
\]

plus the observation that the classical invariance principle makes **global** trace class of this resolvent power a sufficient wave-operator target.

## 6. Audit / falsification core

A later adversary can check the finding through a short chain:

1. verify the common-measure Fourier decomposition and exact `m=0` cancellation already audited in PF-127;
2. specialize PF-127 equations (14) and (18) to Schatten exponent `2` to obtain (3)--(4);
3. verify the exact identity (5) without assuming the two resolvents commute;
4. apply `S_2 S_2 subset S_1` and sum `sum_{m!=0}|m|^{-3}`;
5. import PF-109 only for the prime/shift specialization `|t|=O(P^{-3})`;
6. independently check the Birman--Kato invariance principle for the strictly decreasing function `Phi(lambda)=(1+lambda)^{-2}` before using (7) as a global scattering criterion;
7. do not infer (7) from the localized collar estimate: the uncut interface/body/global-summation problem is deliberately left open.

A refutation of PF-146 would have to break the PF-127 `S_2` bounds, the noncommutative algebraic identity (5), the Schatten product estimate, or the classical invariance-principle bridge. Failure of a later global trace-class proof would narrow the new route but would not refute the local claim.

## Consequence for the research line

PF-112's first-resolvent trace obstruction is no longer a reason by itself to expect failure of prime/shift wave equivalence. There are now two logically distinct sufficient programs:

```text
geometric route:
    globally summable Güneysu--Thalmaier weighted metric deviation
    -> complete wave operators

operator route:
    global S1 difference of squared resolvents
    -> Kato--Rosenblum + Birman--Kato invariance
    -> complete wave operators
```

PF-146 proves that the canonical collapsing core is compatible with the second route at a stronger local ideal level than was previously recorded. The remaining question is global: whether body/interface terms and their infinite sum preserve trace class for the squared-resolvent difference under one natural prime/shift identification.