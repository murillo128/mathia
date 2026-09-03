# ANF-013 — duplicated lattice tests expose a scale-free periodization barrier

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + EXTREMAL-REDUCTION + STRUCTURAL-BOUNDARY`. After `ANF-012`, every continuous compact-band spectral profile in the universal affine scalar branch is nonnegative. Long equally spaced real configurations then impose a stronger thermodynamic family of necessary constraints than the one- and two-point tests of `ANF-005`. For a profile `J>=0` supported in `[-1,1]`, these constraints are governed by one periodization floor

\[
p(J):=\inf_{h>0}\frac1h\sum_{k\in\mathbb Z}J(k/h).
\]

If `C(J)` denotes the BGSST pair-correlation cost, then optimizing only the scalar amplitude of a fixed profile can never produce a simple-critical-zero lower bound larger than

\[
\max\left\{0,\ 2-\frac{C(J)}{p(J)}\right\}.
\]

Consequently **any universal affine scalar improvement over Montgomery--Taylor must satisfy the scale-free necessary condition `C(J)/p(J)<C_MT`.** The familiar nonnegative-spatial-kernel problem is the special case `p(J)=F(0)`, where the ratio reduces to the classical Montgomery--Taylor functional. A formal profile that saturates every duplicated-lattice constraint admits an exact Möbius-inversion formula, exposing an unexpected arithmetic boundary inside the remaining scalar extremal problem.

## 1. The residual universal affine branch

Use the universal affine counting setup of `ANF-005`:

\[
s(Z)\ge A|Z|-E_F(Z),
\qquad
E_F(Z)=\sum_{z,w\in Z}F(z-w),
\tag{1}
\]

for every finite conjugation-invariant multiset `Z`, where `s(Z)` counts simple real elements. By `ANF-012`, in the continuous compact support-one branch we may write

\[
F(x)=\widehat J(x)
=\int_{-1}^{1}J(\alpha)e^{-2\pi i\alpha x}\,d\alpha,
\qquad
J\ge0,
\tag{2}
\]

with `J` continuous, real and even. Continuity together with support in `[-1,1]` gives `J(1)=J(-1)=0`.

The unconditional BGSST evaluation used in `ANF-005` assigns to this profile the cost

\[
C(J):=J(0)+2\int_0^1\alpha J(\alpha)\,d\alpha.
\tag{3}
\]

A certificate with intercept `A` would therefore yield asymptotically the lower bound

\[
B=A-C(J)
\tag{4}
\]

for the simple critical-zero proportion. The question is how large `A` can be once (1) is required for all finite configurations.

## 2. Long real lattices give an exact periodization constraint

Fix a spacing `h>0`, an integer `n>=1`, and a multiplicity `r>=1`. Let `Z_{n,h}^{(r)}` consist of the `n` real sites

\[
0,h,2h,\ldots,(n-1)h,
\]

each repeated `r` times. These configurations are admissible in (1). For `r=1` every point is simple, so `s=n`; for `r>=2` no point is simple, so `s=0`.

Put

\[
S_{n,h}(\alpha)=\sum_{j=0}^{n-1}e^{-2\pi i\alpha hj}.
\]

Fourier inversion gives

\[
E_F\!\left(Z_{n,h}^{(r)}\right)
=r^2\int_{-1}^{1}J(\alpha)|S_{n,h}(\alpha)|^2\,d\alpha.
\tag{5}
\]

The normalized factor `n^{-1}|S_{n,h}|^2` is the Fejér kernel in the variable `h alpha`. Its standard approximate-identity limit is the Dirac comb of period `1/h`. Since `J` is continuous and compactly supported,

\[
\boxed{
\lim_{n\to\infty}\frac1n
\int_{-1}^{1}J(\alpha)|S_{n,h}(\alpha)|^2\,d\alpha
=P_J(h)
:=\frac1h\sum_{k\in\mathbb Z}J(k/h).
}
\tag{6}
\]

The sum is finite. Applying (1), dividing by `n`, and taking `n->infinity` gives for the simple lattice `r=1`

\[
\boxed{A\le1+P_J(h),}
\tag{7}
\]

while for multiplicity `r>=2`

\[
\boxed{A\le rP_J(h).}
\tag{8}
\]

Because `J>=0`, the strongest duplicated-lattice member of (8) is `r=2`. Hence, for every `h>0`,

\[
\boxed{
A\le \psi(P_J(h)),
\qquad
\psi(x):=\min(1+x,2x).
}
\tag{9}
\]

This family contains the small-configuration constraints as limits. As `h->infinity`, the Riemann sum in (6) tends `int_{-1}^1 J=F(0)`, recovering the singleton/double-point normalization constraints. As `h->1^-`, only the `k=0` sample remains and `P_J(h)->J(0)`. At intermediate spacings, (9) tests cancellation and periodic packing information invisible to either endpoint alone.

## 3. The lattice family has a scale-free extremal ratio

Define

\[
p(J):=\inf_{h>0}P_J(h).
\tag{10}
\]

Since `psi` is increasing, (9) yields

\[
A\le\psi(p(J)).
\tag{11}
\]

Moreover

\[
p(J)\le J(0)\le C(J).
\tag{12}
\]

If `p(J)=0`, (11) already gives `A<=0`, so this shape cannot produce a positive bound through a universal affine certificate. Assume henceforth `p(J)>0`.

Now fix the **shape** of `J` and scale its amplitude by `t>0`. Both quantities scale linearly:

\[
p(tJ)=tp(J),
\qquad
C(tJ)=tC(J).
\tag{13}
\]

Therefore the lattice tests alone cap the best possible lower bound from that scaled shape by

\[
B_t\le \psi(tp)-tC,
\tag{14}
\]

where `p=p(J)` and `C=C(J)`. Put `r=C/p`. By (12), `r>=1`. Writing `x=tp`, the right side becomes

\[
\psi(x)-rx
=
\begin{cases}
(2-r)x,&0<x\le1,\\
1-(r-1)x,&x\ge1.
\end{cases}
\tag{15}
\]

Thus the amplitude optimization is exact:

\[
\boxed{
\sup_{t>0}\bigl(\psi(tp)-tC\bigr)
=
\max\left\{0,\ 2-\frac{C(J)}{p(J)}\right\}.
}
\tag{16}
\]

When `1<=C/p<2`, the unique junction scale is `tp=1`: the simple and duplicated lattice constraints meet at `A<=2`. If `C/p>=2`, the thermodynamic lattice family already prevents any positive lower bound regardless of amplitude.

Let

\[
C_{\rm MT}
=\frac12+\frac1{\sqrt2}\cot\frac1{\sqrt2}
=1.3274992963\ldots
\]

be the Montgomery--Taylor pair cost, so the benchmark proportion is `2-C_MT`. Equation (16) gives the following necessary condition for every residual universal affine scalar improvement:

\[
\boxed{
B>2-C_{\rm MT}
\quad\Longrightarrow\quad
\frac{C(J)}{p(J)}<C_{\rm MT}.
}
\tag{17}
\]

This is strictly a **survival test**. A profile passing (17) has not proved (1); it has only survived the entire long-lattice subfamily of universal configurations.

## 4. Montgomery--Taylor is the nonnegative-spatial special case

The ratio in (17) clarifies exactly what spatial sign changes would have to buy. By Poisson summation, with the conventions of (2),

\[
P_J(h)=\sum_{m\in\mathbb Z}F(mh).
\tag{18}
\]

For the classical admissible class with `F(x)>=0` on the real axis and normalization `F(0)=1`, equation (18) gives `P_J(h)>=1` for every `h`, while the Riemann-sum limit of (6) as `h->infinity` gives `P_J(h)->1`. Hence

\[
p(J)=1.
\tag{19}
\]

The scale-free ratio is then simply `C(J)`. Carneiro--Chandee--Littmann--Milinovich prove that this nonnegative-spatial support-one class satisfies

\[
C(J)\ge C_{\rm MT}.
\tag{20}
\]

So (17) reproduces the established Montgomery--Taylor ceiling on that subspace. The only remaining scalar possibility is therefore very specific: `J` stays nonnegative by `ANF-012`, but `F=widehat J` uses spatial sign changes in such a way that the BGSST cost `C(J)` drops **more rapidly** than the worst periodized lattice energy `p(J)`.

This is more informative than saying merely that `F` may be signed. It identifies the exact scale-free quantity that those signs must improve.

## 5. Perfect lattice saturation has an exact Möbius inverse

There is a useful exact boundary model for (17). Normalize the junction scale so that `p(J)=1`, and consider the deliberately stronger **perfect-saturation ansatz**

\[
J(0)=1,
\qquad
P_J(h)=1
\quad\text{for every }h\ge1.
\tag{21}
\]

This is not required by an extremizer; it asks what profile would make every duplicated-lattice thermodynamic inequality tight simultaneously.

For real `t>=1`, compact support and evenness turn (21) into

\[
1+2\sum_{1\le k\le t}J(k/t)=t,
\tag{22}
\]

where the endpoint contribution is harmless because `J(1)=0`. Define

\[
G(t):=J(1/t),
\qquad t\ge1.
\tag{23}
\]

Then

\[
\sum_{k\le t}G(t/k)=\frac{t-1}{2}.
\tag{24}
\]

Ordinary Möbius inversion on the dilation semigroup gives, exactly,

\[
\boxed{
G(t)
=\frac12\sum_{n\le t}\mu(n)\left(\frac{t}{n}-1\right)
=\frac12\left(
t\sum_{n\le t}\frac{\mu(n)}n-M(t)
\right),
}
\tag{25}
\]

where `mu` is the Möbius function and `M(t)=sum_{n<=t}mu(n)` is the Mertens summatory function. Indeed, applying `sum_{n<=t} mu(n)` to the left side of (24) collapses the double sum by `sum_{d|m}mu(d)=1_{m=1}`.

Thus a profile that saturated **all** real-lattice constraints would not be a free smooth extremizer: its values on `(0,1]` would be arithmetically forced by (25). Nonnegativity, continuity and the remaining complex-configuration inequalities then become concrete tests on this Möbius-generated boundary profile.

No assertion is made that (25) defines an admissible extremizer. The significance is the exact bridge: the thermodynamic boundary of the residual positive-spectral pair-correlation problem already contains Möbius cancellation when every lattice scale is forced to equality.

## 6. Prior-art and novelty boundary

The Fejér approximate identity, Poisson summation and Möbius inversion used in (6), (18) and (25) are classical. The Montgomery--Taylor extremal value and its full nonnegative-spatial admissible class are the Carneiro--Chandee--Littmann--Milinovich result already anchored in `SOURCES.md`. Positive-definite bandlimited functions with spatial sign constraints also have a substantial classical extremal literature; spatial sign change by itself is not new structure.

A targeted search across pair-correlation extremal problems, positive-definite bandlimited optimization, lattice/periodization tests and Möbius inversion did not locate the exact reduction (9)--(17) from a universal simple-real counting inequality, nor the perfect-saturation identity (25) in this zeta-zero certificate setting. No publication-level novelty claim is made. The durable Mathia contribution is the **information-boundary reduction**: long duplicated lattices turn the residual affine problem into the scale-free ratio `C(J)/p(J)`, and complete saturation of those constraints has an explicit arithmetic inverse.

## 7. Decisive audit boundary and next test

The result uses only configurations already quantified over by (1), the positive spectral profile forced by `ANF-012`, and standard Fourier limits. It would fail only if the Fejér limit (6) were normalized incorrectly, if multiplicity scaling in (7)--(8) miscounted simple points, or if the amplitude optimization (15) were wrong. Each step is explicit and independent of zeta-specific asymptotics once `C(J)` has been supplied by BGSST.

The constraints are necessary, not sufficient. In particular, (17) does not test non-lattice real configurations, vertically displaced conjugate configurations, or the complete universal inequality (1). The perfect-saturation ansatz (21) is stronger still and must not be confused with a necessary equality condition for an optimizer.

The cheapest next scalar test is now sharper than the generic finite-configuration search left by `ANF-012`: first decide whether any continuous even `J>=0`, supported in `[-1,1]` and compatible with the remaining universal constraints, can satisfy

\[
\boxed{\frac{C(J)}{p(J)}<C_{\rm MT}.}
\tag{26}
\]

A rigorous lower bound `C(J)/p(J)>=C_MT` would close the residual universal affine scalar route immediately. A strict sub-Montgomery--Taylor profile would only justify the harder second stage: proving that its affine counting inequality survives **all** conjugation-invariant complex multisets. The configuration-level and genuinely non-affine escape routes from `ANF-006` remain outside this obstruction.