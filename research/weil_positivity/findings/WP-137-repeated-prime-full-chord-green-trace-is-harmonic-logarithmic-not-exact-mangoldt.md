# WP-137 — Repeated-prime full-chord Green trace is harmonic-logarithmic, not exact Mangoldt

**Status:** `EXACT-DERIVED + SHARP-RESTRICTION + PRIME-CIRCLE + POSITIVE-GREEN + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION` for the canonical singular inverse readout of the repeated-prime full-chord fiber pencil of `PC-156`.

`WP-136` proves that every fixed continuous nonnegative trace over the complete repeated-prime fiber spectrum is either zero or extensive in the deck multiplicity. It deliberately leaves singular endpoint-sensitive positive spectral readouts open. The most canonical such readout is the Green trace

\[
h_d(t):=\operatorname{Tr}\mathcal P_d(t)^{-1},
\qquad 0<t<1,
\]

for the exact Hermitian pencil

\[
\mathcal P_d(t)
=
\frac1{d^2}
\left(
L_d^{\rm int}+\frac t2 C_d-\frac{t^2}{2}I
\right)
\]

of `PC-156`.

This singular route does evade the extensivity theorem, but only in a universal cover-theoretic way. The pencil has canonically conjugate simple zero modes at the two endpoints. Their Green poles turn the uniform deck sum into harmonic numbers, so a residue-normalized deck-Haar Green mean grows as `log m`. Consequently refinement `m -> a m` has asymptotic increment `log a` for every integer degree multiplier `a`, not specifically for primes. In the exact matched case `d=2` the normalized Green mean is **exactly** `H_{m-1}`, hence the repeated-prime shell increment is never the finite Mangoldt weight `log 2`; it only converges to it.

Thus the endpoint singularity left open by `WP-136` does contain logarithmic scale, but the canonical Green readout does **not** produce the exact finite prime-power coefficient required by the Weil explicit formula. It produces the generic logarithm of cover degree. Recovering exact finite weights would require an additional endpoint counterterm, nonlinear limiting prescription, or arithmetic selector whose positivity and global finite--archimedean compatibility would have to be proved independently.

## 1. The two endpoints are exactly gauge-equivalent

Let

\[
q:=\varphi(d),
\qquad
D_d:=\operatorname{diag}\left(e^{2\pi i a/d}\right)_{a\in U(d)}.
\]

Although `PC-156` samples only `0<=t<1`, its quadratic formula extends canonically to `t=1`. Put

\[
\mathcal P_d(0)=d^{-2}L_d^{\rm int}.
\]

For distinct `a,b in U(d)`, set

\[
\theta=\frac{\pi(a-b)}d,
\qquad
w_{ab}=\frac1{4\sin^2\theta}.
\]

The off-diagonal entry of `L_d^{int}` is `-w_ab`. Directly,

\[
\begin{aligned}
\left(D_d^*L_d^{\rm int}D_d-L_d^{\rm int}\right)_{ab}
&=w_{ab}\left(1-e^{-2i\theta}\right)\\
&=\frac12\left(1+i\cot\theta\right)\\
&=\frac12(C_d)_{ab}.
\end{aligned}
\]

The diagonal of the left side vanishes, whereas `(C_d)_{aa}=1`. Hence the exact matrix identity is

\[
\boxed{
D_d^*L_d^{\rm int}D_d
=
L_d^{\rm int}+\frac12C_d-\frac12I.
}
\tag{1}
\]

Therefore

\[
\boxed{
\mathcal P_d(1)=D_d^*\mathcal P_d(0)D_d.
}
\tag{2}
\]

Substituting (2) back into the quadratic pencil gives the stronger interpolation identity

\[
\boxed{
\mathcal P_d(t)
=(1-t)\mathcal P_d(0)
+t\mathcal P_d(1)
+\frac{t(1-t)}{2d^2}I.
}
\tag{3}
\]

Both endpoint matrices are positive semidefinite because they are Laplacians up to unitary conjugacy. Thus

\[
\boxed{
\mathcal P_d(t)\succeq \frac{t(1-t)}{2d^2}I>0,
\qquad 0<t<1.
}
\tag{4}
\]

The Green operator is therefore an ordinary positive inverse throughout the interior. No zeta regularization, analytic continuation, or inserted zero data is involved.

## 2. The endpoint Green residues are equal and explicit

The complete positive weighted graph underlying `L_d^{int}` is connected whenever `q>1`; for `q=1` the same formulas below are immediate. Thus the endpoint kernel is one-dimensional. Let

\[
u_0=\frac1{\sqrt q}(1,\ldots,1)^T.
\]

Since

\[
\mathcal P_d'(0)=\frac{C_d}{2d^2},
\]

and the ordered cotangent terms cancel in the total sum,

\[
\langle u_0,H_du_0\rangle=0,
\qquad
\langle u_0,J_du_0\rangle=q.
\]

Hence the simple eigenvalue leaving zero at `t=0` has slope

\[
\boxed{
c_d:=\langle u_0,\mathcal P_d'(0)u_0\rangle
=\frac{q}{2d^2}.
}
\tag{5}
\]

At the other endpoint the kernel vector is

\[
u_1=D_d^*u_0.
\]

Differentiate (3) at `t=1`:

\[
\mathcal P_d'(1)
=
\mathcal P_d(1)-\mathcal P_d(0)-\frac1{2d^2}I.
\]

Because `P_d(1)u_1=0`, it remains to compute the coarse Laplacian energy. For every unordered pair `a<b`,

\[
w_{ab}|u_1(a)-u_1(b)|^2=\frac1q,
\]

so

\[
\langle u_1,L_d^{\rm int}u_1\rangle
=\frac{q-1}{2}.
\]

Therefore

\[
\boxed{
\langle u_1,\mathcal P_d'(1)u_1\rangle
=-\frac{q}{2d^2}=-c_d.
}
\tag{6}
\]

Finite-dimensional analytic perturbation at a simple zero eigenvalue now gives

\[
\boxed{
h_d(t)=\frac1{c_dt}+O(1),\qquad t\downarrow0,}
\tag{7}
\]

and

\[
\boxed{
h_d(t)=\frac1{c_d(1-t)}+O(1),\qquad t\uparrow1.}
\tag{8}
\]

More precisely,

\[
r_d(t)
:=
h_d(t)-\frac1{c_dt}-\frac1{c_d(1-t)}
\tag{9}
\]

extends continuously to `[0,1]`.

## 3. Uniform deck sampling is a harmonic-number law

The full repeated-prime fiber samples `t=k/m`. Since the endpoint blocks themselves are singular, use the nonzero deck sectors `1<=k<=m-1`. Define the residue-normalized deck-Haar Green mean

\[
\boxed{
G_d(m)
:=
\frac{c_d}{2m}
\sum_{k=1}^{m-1}
\operatorname{Tr}\mathcal P_d(k/m)^{-1}.
}
\tag{10}
\]

The factor `1/m` is the uniform deck average. The remaining factor `c_d/2` is the normalization forced by the two equal endpoint residues if their combined harmonic singularity is to have unit leading coefficient.

Substituting (9) into (10) gives the exact decomposition

\[
\begin{aligned}
G_d(m)
&=
\frac1{2m}
\sum_{k=1}^{m-1}
\left(
\frac{m}{k}+\frac{m}{m-k}
\right)
+
\frac{c_d}{2m}
\sum_{k=1}^{m-1}r_d(k/m)\\
&=
\boxed{
H_{m-1}
+
\frac{c_d}{2m}
\sum_{k=1}^{m-1}r_d(k/m).
}
\tag{11}
\end{aligned}
\]

Because `r_d` is continuous, the second term converges to a finite constant. Hence

\[
\boxed{
G_d(m)=\log m+C_d^{G}+o(1)
}
\tag{12}
\]

for a base-level constant `C_d^G`, and for every fixed integer `a>=2`,

\[
\boxed{
G_d(am)-G_d(m)\longrightarrow\log a.
}
\tag{13}
\]

The singular Green readout therefore escapes the linear-in-`m` behavior of `WP-136`, but it does so by a completely generic endpoint harmonic law.

## 4. Exact matched falsifier: `d=2`

The smallest repeated-prime fiber makes the mismatch exact. For `d=2`, `q=1` and

\[
L_2^{\rm int}=H_2=0,
\qquad
J_2=1.
\]

Therefore

\[
\boxed{
\mathcal P_2(t)=\frac{t(1-t)}8,
\qquad
c_2=\frac18.
}
\tag{14}
\]

Equation (10) can then be summed exactly:

\[
\begin{aligned}
G_2(m)
&=\frac1{16m}
\sum_{k=1}^{m-1}
\frac{8m^2}{k(m-k)}\\
&=\boxed{H_{m-1}}.
\tag{15}
\end{aligned}
\]

Now take the actual repeated-prime tower `m=2^r`. The arithmetic coefficient is exactly

\[
\Lambda(2^{a+r})=\log2
\]

at every depth, whereas the geometric shell defect is

\[
\boxed{
G_2(2m)-G_2(m)
=H_{2m-1}-H_{m-1}.
}
\tag{16}
\]

For every finite `m` the right side is rational, while `log 2` is irrational, so (16) is never the exact Mangoldt coefficient. It only satisfies

\[
H_{2m-1}-H_{m-1}\longrightarrow\log2.
\tag{17}
\]

This kills the strongest possible interpretation that the canonical singular Green trace itself supplies the exact repeated-prime finite-place weight at finite refinement depth.

## 5. Matched controls and what the logarithm really knows

Equation (13) holds for **every** integer deck multiplier `a`, whether or not `a` is prime. The logarithm comes from the universal identity

\[
\sum_{k=1}^{m-1}\frac1k=H_{m-1},
\]

forced by a simple zero mode at each boundary of a uniformly sampled band. It does not inspect prime support, unique factorization, the von Mangoldt selector, or any specifically arithmetic datum of `Q`.

The same mechanism therefore survives the natural generalized-cover control: any cyclic refinement family with the same two simple endpoint Green poles has the same `log a` asymptotic after residue normalization. In this sense (13) is a cover-degree law, not an arithmetic selection theorem.

There are several legitimate escapes, but each is extra structure beyond the present Green trace:

- one may subtract the finite remainder in (11) or prescribe an endpoint counterterm so that the defect becomes exactly `log a`; that is a renormalization and needs an intrinsic geometric theorem fixing the counterterm rather than the desired arithmetic answer;
- one may define `log a` through the limit in (13); the limit is exact as a scalar identity, but it is a **difference of positive Green quantities**, not itself a positive quadratic-form theorem, and it remains universal for arbitrary degree multipliers;
- one may introduce a distinguished arithmetic deck sector, a new-prime interaction, a nonlinear cross-sector observable, or finite--archimedean coupling before scalarization; none of those mechanisms is present in (10).

Most importantly for this branch, even a successful extraction of the scalar `log p` from (13) would only recover a finite coefficient. It supplies neither the Gamma/polar counterterms of the global explicit formula nor an independent theorem that the resulting Weil quadratic form is nonnegative. Feeding `log p` back into the ordinary prime-translation/autocorrelation lift returns to the sign obstruction already exposed in earlier `WP` findings.

## 6. Prior-art and novelty audit

No novelty is claimed for the analytic ingredients. A resolvent has a simple pole when a simple eigenvalue crosses zero; endpoint `1/t` singularities sampled on a uniform grid produce harmonic numbers and logarithmic Riemann-sum asymptotics; and Green traces are logarithmic derivatives of determinants wherever both are defined. These are classical finite-dimensional spectral facts.

The logarithm itself is also not new inside this research line. `WP-074` derives an exact positive log-degree trace from a pointed-cover inverse-scale defect, and `WP-075` shows how positive shifted resolvent defects mix that log degree with digamma corrections. `WP-083` already identifies singular endpoints as the only place where a homogeneous positive cover bulk can retain a Mangoldt-like signal. `WP-104` gives another extensive/harmonic cover-trace comparison.

The branch-specific advance is narrower and exact: `PC-156` supplies the newest complete repeated-prime full-chord pencil, `WP-136` leaves singular endpoint readouts as an explicit survivor, and equations (1)--(17) classify its canonical Green choice. The exact endpoint gauge identity (1), positive interpolation (3), equal Green residues (5)--(8), and the `d=2` identity (15) show that this survivor yields generic harmonic cover-degree logarithms rather than an exact finite Mangoldt shell law.

## 7. Consequence for the Weil-positivity search

The repeated-prime full-chord route now has a sharper boundary. Fixed continuous positive whole-spectrum traces are extensive by `WP-136`; the canonical singular inverse trace avoids extensivity but degenerates to universal endpoint harmonic behavior. Thus **singularity alone is not the missing arithmetic ingredient**.

A viable continuation must add structure that is absent from a uniformly sampled one-parameter cover pencil: an intrinsic arithmetic selector, genuinely nonseparable cross-prime coupling, a canonical finite--archimedean completion before positivity, or another construction whose sign theorem survives matched generalized-cover controls. Any such proposal must still reproduce the exact finite prime-power coefficients at finite arithmetic scale and derive the Gamma/polar terms and global nonnegativity independently of RH or inserted zero data.

### Internal evidence

- [WP-136](WP-136-repeated-prime-full-chord-continuous-positive-spectral-traces-are-extensive.md)
- [WP-104](WP-104-cover-dirichlet-log-jensen-positivity-has-extensive-harmonic-trace-density.md)
- [WP-083](WP-083-homogeneous-cover-jensen-positivity-is-flat-and-mangoldt-support-is-singular-endpoint.md)
- [WP-075](WP-075-positive-shifted-resolvent-cover-defects-mix-log-degree-with-digamma-but-exact-finite-weights-force-zero-shift.md)
- [WP-074](WP-074-pointed-cover-inverse-scale-defect-has-positive-log-degree-trace-but-poisson-weil-lift-is-indefinite.md)
- [PC-156](../../prime_circle/findings/PC-156-repeated-prime-full-chord-fibers-collapse-to-a-fixed-quadratic-pencil.md)
