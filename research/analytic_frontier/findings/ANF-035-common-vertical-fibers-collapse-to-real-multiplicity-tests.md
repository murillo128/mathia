# ANF-035 — common vertical fibers collapse to real multiplicity tests

**Status:** `EXACT-DERIVED + STRUCTURAL-REDUCTION + COMPLEX-FALSIFIER-BOUNDARY`. `ANF-012` shows that every continuous compact-band spectrum of a universal affine scalar certificate must satisfy `J>=0`, and `ANF-034` leaves arbitrary conjugation-invariant complex configurations as the next obstruction for its explicit finite-real separator ray. A large complex subclass is nevertheless already redundant: once `J>=0`, attaching the **same conjugation-symmetric vertical fiber** to every point of a real configuration can only increase the spectral energy relative to collapsing that fiber onto the real axis. Hence no Cartesian common-height/common-fiber complex cloud can be a stricter affine falsifier than the corresponding real multiplicity test.

Let

\[
F(z)=\widehat J(z)
=\int_{-B}^{B}J(\alpha)e^{-2\pi i\alpha z}\,d\alpha,
\qquad J\ge0,
\tag{1}
\]

with `J` real and even. Let `X` be a nonempty finite set of distinct real points and let `Y` be a nonempty finite real multiset satisfying `Y=-Y`, with no zero element. Put

\[
Z:=X+iY
=\{x+iy:x\in X,\ y\in Y\},
\tag{2}
\]

with product multiplicities, and write `m:=|Y|`. Then `m>=2`, `Z` is conjugation-invariant and has no real points. If `mX` denotes the real multiset obtained by replacing each `x in X` by `m` coincident copies, then

\[
\boxed{
E_F(Z)\ge E_F(mX)=m^2E_F(X).
}
\tag{3}
\]

Consequently every universal affine inequality

\[
s(W)\ge A|W|-tE_F(W),\qquad t>0,
\tag{4}
\]

that already survives the real multiset `mX` automatically survives its Cartesian complex lift `Z`. In particular, among all common symmetric vertical fibers, the limiting two-point fiber `Y={-y,y}` as `y->0` reproduces the doubled-real constraint used in `ANF-017`; no positive-height version is stronger.

## 1. Exact factorization of the structure factor

For a finite conjugation-invariant multiset `W`, `ANF-012` gives

\[
E_F(W)
=\int_{-B}^{B}J(\alpha)|S_W(\alpha)|^2\,d\alpha,
\qquad
S_W(\alpha)=\sum_{w\in W}e^{-2\pi i\alpha w}.
\tag{5}
\]

For the Cartesian lift (2), the structure factor separates:

\[
S_Z(\alpha)
=
\left(\sum_{x\in X}e^{-2\pi i\alpha x}\right)
\left(\sum_{y\in Y}e^{2\pi\alpha y}\right)
=:S_X(\alpha)P_Y(\alpha).
\tag{6}
\]

Because `Y=-Y` with equal multiplicities and contains no zero,

\[
P_Y(\alpha)
=
2\sum_{y>0}m_y\cosh(2\pi\alpha y),
\tag{7}
\]

where `m_y` is the multiplicity of `y`. Therefore

\[
\boxed{P_Y(\alpha)\ge 2\sum_{y>0}m_y=m}
\qquad(\alpha\in\mathbb R).
\tag{8}
\]

Since `J>=0`, equations (5)--(8) give

\[
\begin{aligned}
E_F(Z)
&=\int J(\alpha)|S_X(\alpha)|^2P_Y(\alpha)^2\,d\alpha\\
&\ge m^2\int J(\alpha)|S_X(\alpha)|^2\,d\alpha\\
&=m^2E_F(X).
\end{aligned}
\tag{9}
\]

The real multiset `mX` has structure factor `mS_X`, hence

\[
E_F(mX)=m^2E_F(X),
\tag{10}
\]

which proves (3).

This is not an asymptotic or a small-height statement. The only inputs are the positive spectral profile forced by `ANF-012`, the Cartesian product geometry, and `cosh u>=1`.

## 2. Common-height conjugate clouds are dominated by double-real collisions

The most important special case is

\[
Y=\{-y,y\},\qquad y>0.
\tag{11}
\]

Then

\[
S_Z(\alpha)
=2\cosh(2\pi\alpha y)S_X(\alpha)
\tag{12}
\]

and therefore

\[
\boxed{
E_F(X+iy\;\cup\;X-iy)
=4\int J(\alpha)\cosh^2(2\pi\alpha y)|S_X(\alpha)|^2d\alpha
\ge4E_F(X).
}
\tag{13}
\]

After division by `|Z|=2|X|`,

\[
\frac{E_F(Z)}{|Z|}
\ge
2e_J(X),
\qquad
e_J(X):=\frac{E_F(X)}{|X|}.
\tag{14}
\]

As `y downarrow0`, the left side converges exactly to the normalized energy of the doubled real multiset `2X`, namely `2e_J(X)`. Thus the vertical displacement is monotone in the only direction relevant to a no-simple affine test: it raises the energy above the real-collision boundary.

For a general symmetric fiber of size `m`, (3) similarly gives

\[
\frac{E_F(Z)}{|Z|}\ge m e_J(X)\ge2e_J(X).
\tag{15}
\]

So among this whole Cartesian class, the smallest no-simple energy is already approached by the doubled-real test. Higher vertical multiplicity cannot create a new lower-energy obstruction.

## 3. Exact consequence for the affine envelope of `ANF-017`

Apply the affine certificate (4) first to the simple real set `X`. Since `s(X)=|X|`,

\[
A\le1+t e_J(X).
\tag{16}
\]

Apply it to the doubled real multiset `2X`. It has no simple elements, so

\[
A\le2t e_J(X).
\tag{17}
\]

These are exactly the two branches of the finite-real envelope

\[
A\le\psi(te_J(X)),
\qquad
\psi(u)=\min(1+u,2u),
\tag{18}
\]

used in `ANF-017`.

Now take any Cartesian complex lift (2). It also has `s(Z)=0`, while (15) gives

\[
\frac{tE_F(Z)}{|Z|}\ge mt e_J(X)\ge2t e_J(X).
\tag{19}
\]

Thus the upper bound on `A` obtained from `Z`,

\[
A\le\frac{tE_F(Z)}{|Z|},
\tag{20}
\]

is never stronger than the already-present doubled-real bound (17). The conclusion holds for every amplitude `t>0`; it is not tied to the amplitude optimizing the Montgomery--Taylor ratio.

This identifies a genuine redundancy in the post-`ANF-034` complex search. Once spectral positivity has been established, taking a dangerous real configuration and moving every site to the same pair of heights `+/-y`, or more generally attaching the same symmetric nonzero vertical fiber to every site, cannot expose any new affine failure.

## 4. Consequence for the explicit central-notch separator

The separator of `ANF-034` has

\[
J_s=J_{\rm MT}-s\phi_\eta\ge0.
\tag{21}
\]

Hence (3)--(20) apply to it without any additional analytic hypothesis. Its elementary isolated conjugate-pair inequality

\[
F_s(iy)\ge F_s(0)
\]

from `ANF-034` is therefore only the one-site member of a much larger statement: **every common-fiber conjugate lift of an arbitrary finite real base is dominated by its collapsed real multiplicity test.**

Accordingly, a complex falsifier capable of killing the central-notch ray after its finite-real tests must break the Cartesian factorization (6). At least one of the following must occur:

- different horizontal sites carry different imaginary heights or different vertical multiplicities;
- real and nonreal points are mixed in a way that changes the simple-point bookkeeping;
- several vertical layers are coupled to different horizontal supports rather than to one common base.

The key structural requirement is **horizontal--vertical coupling**. Merely adding a uniform imaginary displacement profile supplies no new adverse information once `J>=0`.

## 5. Boundary cases and adversarial checks

The sign condition `J>=0` is essential. If `J` changes sign, multiplication by `P_Y(\alpha)^2` can amplify a negative spectral region rather than increase the total energy. Indeed, that is exactly why the vertically growing conjugate binomial combs of `ANF-012` can detect and rule out a negative compact-band profile. The present reduction begins only after that spectral-sign gate has been passed.

The common-fiber hypothesis is also essential. If the available height multiset depends on `x`, then

\[
S_Z(\alpha)
=\sum_x e^{-2\pi i\alpha x}P_x(\alpha)
\tag{22}
\]

with different positive weights `P_x`; no common factor can be removed, and the horizontal phases can cancel differently at different frequencies. Equation (8) then gives no comparison with a single collapsed real configuration. This is precisely the residual complex geometry left open by the theorem.

Allowing `0 in Y` leaves the energy inequality itself intact after adding the corresponding constant term to (7), but it introduces real points into `Z`. Their simple/non-simple contribution can differ from the fully collapsed real multiset, so the clean affine-dominance statement requires the zero-free fiber assumed above. That mixed-real case remains part of the live boundary.

Finally, equality in (3) occurs in the collision limit `Y->0`. For a fixed genuinely nonzero fiber, the inequality is strict whenever `J(\alpha)|S_X(\alpha)|^2` has positive mass away from `alpha=0`, because then `P_Y(\alpha)>m` on that mass. Thus positive vertical separation moves these tests away from, not toward, the dangerous affine boundary.

## 6. Prior-art and evidence boundary

No new external theorem is load-bearing. The Fourier--Laplace representation and positive-definite strip framework are classical and already anchored in `SOURCES.md` through Buescu--Paixão--Symeonides. `ANF-012` supplies the Mathia-specific prerequisite `J>=0` from universal conjugation-invariant affine counting. The new content here is the exact factorization (6), the pointwise symmetric-fiber inequality (8), and their reduction of an infinite complex test family to the real multiplicity envelope of `ANF-017`.

A targeted literature check found the expected classical Fourier--Laplace/positive-definite strip representation, but no separate external theorem is needed for (3). No publication-level novelty claim is made; this finding is retained because it materially narrows the next falsification problem inside the existing Mathia reduction.

The result does **not** prove that the `ANF-034` separator extends to a universal affine zeta-zero certificate. It removes only Cartesian vertical fibers from the list of genuinely new complex obstructions. Heterogeneous-height configurations, mixed real/nonreal configurations, and the full deterministic counting inequality remain unresolved.

## 7. Next decisive test

The cheapest genuinely new complex test is no longer an equal-height conjugate cloud. It should use the smallest conjugation-invariant configuration whose vertical profile depends on horizontal position, for example one real point together with a conjugate pair at a displaced horizontal coordinate, or two conjugate pairs at distinct heights. For such configurations the structure factor has frequency-dependent unequal `cosh` weights, so destructive horizontal interference can no longer be factored away.

A useful next calculation is therefore to derive the exact three-point constraint for

\[
\{0,\ x+iy,\ x-iy\}
\]

and optimize it jointly with the simple/double real envelope and the compulsory slack of `ANF-005`. If that already erases the strict finite-real gain of the central-notch ray, the universal affine scalar branch closes cheaply; if it does not, the first surviving complex geometry will have been isolated much more sharply.