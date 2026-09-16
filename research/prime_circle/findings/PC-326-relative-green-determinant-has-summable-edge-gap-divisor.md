# PC-326 — relative Green determinant has a summable edge-gap divisor

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE` + `PRIOR-ART-CLASSICALIZATION` for the direct Riemann-zero spectral-divisor interpretation of the PC-323 relative Green/Hilbert determinant.

PC-323 leaves the trace-class relative determinant of the canonical cross-level Green operator as the first determinant-like object that can still retain detailed Prime-Circle source information after the universal Hilbert channel is removed. PC-325 then shows that the complete relative pair is phase-gauge and can depend only on the two source autocorrelations. A more basic spectral obstruction applies before any attempt to extract a source-specific zero pattern.

Let

\[
G=G_{a,b},\qquad G_0=G_0(a,b),\qquad V:=G-G_0\in\mathcal S_1,
\]

with the notation of PC-323. If

\[
E:=\pi c_{a,b}>0,
\]

then

\[
\sigma(G_0)=[-E,E].
\]

The zeros of the relative perturbation determinant

\[
\Delta_{a,b}(z)
=
\det\!\left(I+V(G_0-z)^{-1}\right),
\qquad z\in\mathbb C\setminus[-E,E],
\]

are exactly the discrete eigenvalues of the self-adjoint operator `G` outside the Hilbert band. Those eigenvalues can accumulate only at the two band edges, and trace class forces a stronger exact restriction:

\[
\boxed{
\sum_{\lambda_j>E}(\lambda_j-E)
+
\sum_{\lambda_j<-E}(-E-\lambda_j)
\le \|V\|_1.
}
\]

Thus the zero divisor of the relative determinant has **summable distance to the essential band**. This immediately rules out not only a direct unbounded Riemann-ordinate spectral identification, but also every edge compactification whose distance to the band is comparable to `gamma^{-alpha}` with `alpha<=1`. In particular the usual reciprocal/Cayley scale `1/gamma` is still too dense because the Riemann ordinates satisfy `sum 1/gamma = infinity`.

The surviving relative Green determinant can therefore carry source-dependent bound states, but at fixed conductors it cannot be a direct Hilbert--Polya realization of the full Riemann-zero divisor unless one inserts a substantially faster, geometry-forced compactification, takes a singular conductor/cross-level limit in which the trace-class control breaks down, or changes the operator. An arbitrary nonlinear reparameterization of the spectral variable would be exactly the kind of spectral wrapper excluded by the Prime-Circle mandate.

## 1. Relative determinant zeros are the bound states outside the Hilbert band

PC-323 proves the exact decomposition

\[
G=G_0+V,
\qquad V=V^*\in\mathcal S_1,
\tag{1}
\]

where the comparison operator has one positive and one negative Hilbert channel and

\[
\sigma(G_0)=[-E,E],
\qquad E=\pi c_{a,b}.
\tag{2}
\]

For `z` in the resolvent set of `G_0`, factorization gives

\[
G-z
=
\left(I+V(G_0-z)^{-1}\right)(G_0-z).
\tag{3}
\]

The first factor is identity plus trace class. Hence the analytic Fredholm theorem and the ordinary trace-class determinant imply

\[
\boxed{
\Delta_{a,b}(z)=0
\iff
z\in\sigma_p(G)\cap(\mathbb C\setminus[-E,E]).
}
\tag{4}
\]

Because `G` is self-adjoint, every such zero is real. Its order agrees with the finite eigenvalue multiplicity. Thus the relative determinant does not produce an independent complex zero cloud: its zeros are precisely the discrete bound states created outside the universal Hilbert band.

Since `G` is bounded, there is already a coarse obstruction: these zeros lie in the compact interval `[-||G||,||G||]`. Hence no direct affine identification with the unbounded Riemann ordinates, and no direct `lambda=s(1-s)` identification whose RH values grow like `gamma^2`, is possible. The trace-class structure gives a much sharper obstruction near the only places where infinitely many relative zeros may accumulate, namely `+E` and `-E`.

## 2. Trace class forces summable band-edge gaps

Let the eigenvalues of `G` above `E`, repeated with multiplicity, be

\[
\lambda_1^+\ge\lambda_2^+\ge\cdots>E,
\]

and those below `-E` be

\[
\lambda_1^-\le\lambda_2^-\le\cdots<-E.
\]

The upper gaps are the positive eigenvalues of `G-EI`. Since `G_0-EI<=0`, equation (1) gives the quadratic-form inequality

\[
G-EI=(G_0-EI)+V\le V.
\tag{5}
\]

Applying the Ky Fan/min--max inequality to the positive eigenvalues and then the trace-class variational formula yields

\[
\sum_j(\lambda_j^+-E)
\le \operatorname{Tr}V_+.
\tag{6}
\]

For the lower edge apply the same argument to `-G`. Since `-G_0-EI<=0`,

\[
-G-EI=(-G_0-EI)-V\le -V,
\tag{7}
\]

and therefore

\[
\sum_j(-E-\lambda_j^-)
\le \operatorname{Tr}V_-.
\tag{8}
\]

Adding (6) and (8) gives the exact fixed-source bound

\[
\boxed{
\sum_{\lambda_j\notin[-E,E]}
\operatorname{dist}(\lambda_j,[-E,E])
\le
\operatorname{Tr}V_++\operatorname{Tr}V_-
=
\|V\|_1.
}
\tag{9}
\]

No asymptotic estimate of the generalized Hilbert blocks is needed: PC-323 already supplies `V in S_1`, and (9) is a direct self-adjoint trace-ideal consequence. In particular an infinite zero sequence of `Delta` can exist only by approaching the Hilbert band with an `ell^1` sequence of edge gaps.

## 3. Riemann-zero density is incompatible with reciprocal or slower edge compactification

Let

\[
0<\gamma_1\le\gamma_2\le\cdots
\]

be the positive ordinates of the nontrivial Riemann zeros, repeated with multiplicity. The Riemann--von Mangoldt formula gives

\[
N_\zeta(T)
\sim \frac{T}{2\pi}\log T.
\tag{10}
\]

As already used independently in PC-107, partial summation gives

\[
\boxed{
\sum_j\frac1{\gamma_j}=\infty.
}
\tag{11}
\]

More generally, for every `0<alpha<=1`,

\[
\boxed{
\sum_j\gamma_j^{-\alpha}=\infty.
}
\tag{12}
\]

For `alpha<1` this follows from (10) with growth of order `T^{1-alpha} log T`; `alpha=1` is the logarithmic-square divergence in PC-107.

Suppose one attempts to identify all sufficiently high Riemann zeros with relative-determinant zeros `lambda_j` approaching either Hilbert edge and the proposed spectral compactification has the natural asymptotic scale

\[
\operatorname{dist}(\lambda_j,[-E,E])
\ge c\,\gamma_j^{-\alpha}
\tag{13}
\]

for some `c>0` and `alpha<=1`. Equations (12)--(13) force

\[
\sum_j\operatorname{dist}(\lambda_j,[-E,E])=\infty,
\]

contradicting (9). Therefore

\[
\boxed{
\text{no direct, affine, polynomial, reciprocal, or slower-than-reciprocal edge map can identify }
\Delta_{a,b}\text{ with the Riemann-zero divisor.}
}
\tag{14}
\]

The affine and polynomial cases are already excluded by boundedness; (9) adds the nontrivial statement that a standard compactification toward a band edge at `1/gamma` is also impossible. A power-law compactification compatible with (9) would have to satisfy `alpha>1`. Trace class does not prohibit such a super-reciprocal map, but no such map is forced by the Green construction of PC-322/323. Choosing one only to fit the zero density would be external interpolation rather than source-derived spectral structure.

## 4. This is not the PC-107 trace-class determinant obstruction

PC-107 studies a different operator situation. There the canonical object itself is a compact trace-class remainder `T_n`, and

\[
D_n(z)=\det(I-zT_n)
\]

has zeros at reciprocal eigenvalues `1/lambda_j(T_n)`. Trace class therefore forces reciprocal-zero summability and `N_D(R)=o(R)` in an **unbounded determinant variable**.

Here `G` is noncompact and has the universal Hilbert absolutely-continuous band. The determinant is relative to that band, and its zeros are bounded eigenvalues of `G` itself. The correct trace-class invariant is consequently not reciprocal-zero summability but **summability of distance from the continuum** in (9). The two obstructions are mathematically analogous but apply to different surviving branches and different spectral variables.

This distinction matters because PC-323 explicitly survives PC-107 by abandoning the absolute determinant of a trace-class remainder in favor of a relative determinant for a noncompact Hilbert-channel operator. Equation (9) closes the most direct zero-divisor interpretation of that new relative object rather than recycling the earlier fixed-shell theorem.

## 5. Prior-art and novelty audit

The abstract ingredients are classical perturbation theory. The factorization (3) and the zero/eigenvalue correspondence for trace-class perturbation determinants are standard Fredholm theory. The edge estimate (9) is the elementary self-adjoint `S_1` eigenvalue-variation/Ky Fan bound; it is also a special case of the classical trace-ideal spectral-variation theory of Birman, Krein, Solomyak, Kato, and later treatments. The Riemann--von Mangoldt comparison is classical and was already audited in PC-107.

A fresh directed search around trace-class self-adjoint perturbations, perturbation determinants, and eigenvalue-distance/Lieb--Thirring bounds returned the expected standard perturbation-theoretic literature rather than a Prime-Circle-specific theorem. In particular, the general principle that trace-class perturbations constrain discrete eigenvalues outside an essential spectral interval is established operator theory; no novelty is claimed for it.

No external theorem is load-bearing beyond these standard facts because (5)--(9) give the needed inequality directly from the exact PC-323 decomposition. No new durable literature dependency is introduced, so `SOURCES.md` is unchanged.

The Mathia-specific delta is the application to the **canonical PC-323 Green relative pair**: the determinant that remained after removing the universal Hilbert channel has an `ell^1` edge-gap divisor, and that divisor is too sparse in its intrinsic relative spectral coordinate even after the first natural compactification of the Riemann ordinates.

## 6. Consequence for the Prime-Circle frontier

At fixed source conductors the chain

\[
\text{cross-level Green kernel}
\longrightarrow
\text{relative Hilbert pair}
\longrightarrow
\Delta_{a,b}(z)
\longrightarrow
\text{Riemann-zero spectral divisor}
\]

is therefore closed in its direct spectral meaning. PC-325 still leaves the source autocorrelations as genuine relative spectral data, but any discrete eigenvalues they create outside the universal Hilbert band must satisfy (9). Source specificity cannot change that trace-ideal law.

A continuation of the Green branch would need at least one genuinely new ingredient: a geometry-forced conductor/cross-level limit in which the relevant trace norm diverges and the edge-gap class changes; a different nonseparable operator whose comparison defect is not trace class; or an independently derived spectral coordinate approaching the Hilbert edge faster than `1/gamma` and tied to an actual zeta-zero theorem. None of these is supplied by the present construction.

In particular, simply declaring a nonlinear map from Riemann ordinates into a bounded band does not count as an escape. Without a derivation from the roots-of-unity geometry it is an arbitrary spectral wrapper, which the canonical research mandate explicitly excludes.

## Audit tests

The result can be falsified locally at four points. First, PC-323 must indeed give `V=G-G_0 in S_1` with `sigma(G_0)=[-E,E]`. Second, factorization (3) must identify zeros of `Delta` off the band with discrete eigenvalues of `G`. Third, the form inequalities (5) and (7), together with the self-adjoint min--max principle, must give the edge-gap estimate (9). Fourth, Riemann--von Mangoldt must imply (12), so any proposed map satisfying (13) contradicts (9).

Passing these tests proves only the fixed-conductor relative-determinant obstruction above. It does not rule out a singular growing-conductor limit, a non-trace-class comparison defect, or a different geometry-forced operator/spectral coordinate.