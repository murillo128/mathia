---
id: WP-290
title: A source-native Mangoldt dilation coboundary cancels the pole but is tempered if and only if RH
branch: weil_positivity
status: supported
kind: signed-source-cancellation-obstruction
claim_strength: exact integer-dilation pole annihilation with RH-equivalent temperedness and non-tempered Jordan channels
created: 2026-09-13
related: [WP-269, WP-270, WP-273, WP-278, WP-289]
prior_art:
  - classical identity -zeta'/zeta(s)=sum Lambda(n)n^-s
  - von Koch/Schoenfeld RH bounds for Chebyshev psi
  - Fourier--Laplace theory of tempered distributions supported in a half-line
  - classical pole-killing Euler factors such as 1-q^(1-s)
  - Arias de Reyna, Explicit formula and quasicrystal definition, arXiv:2402.10604
---

# WP-290 — A source-native Mangoldt dilation coboundary cancels the pole but is tempered if and only if RH

## Claim

`WP-270` shows that the obvious additive completion of the critical Mangoldt half-density by the zeta-pole continuum is tempered exactly under RH. That leaves a narrower possible escape: perhaps the pole continuum need not be inserted as a separate global sector at all. The arithmetic source itself has an intrinsic multiplicative semigroup, so an integer dilation difference could cancel its leading pole growth before any positivity theorem is attempted.

This cancellation exists, is exact, and is source-native. It nevertheless does **not** make the critical source unconditionally admissible.

On the positive logarithmic half-line define

\[
\mu:=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\,\delta_{\log n}.
\tag{1}
\]

For an integer `q>=2`, let `S_a` denote right translation by `a`,

\[
S_a\delta_x:=\delta_{x+a},
\tag{2}
\]

and define the multiplicative dilation coboundary

\[
\boxed{
\Delta_q\mu
:=\mu-\sqrt q\,S_{\log q}\mu.
}
\tag{3}
\]

Then

\[
\boxed{
\Delta_q\mu\in\mathcal S'(\mathbb R)
\quad\Longleftrightarrow\quad
\mathrm{RH}.
}
\tag{4}
\]

The mechanism is exact. For `Re s>1/2`,

\[
\mathcal L\mu(s)
=-\frac{\zeta'}{\zeta}(s+1/2),
\tag{5}
\]

so

\[
\boxed{
\mathcal L(\Delta_q\mu)(s)
=\bigl(1-q^{1/2-s}\bigr)
\left(-\frac{\zeta'}{\zeta}(s+1/2)\right).
}
\tag{6}
\]

The factor `1-q^(1/2-s)` vanishes at the pole location `s=1/2`, hence cancels the zeta pole without inserting the continuum `e^(x/2)dx` of `WP-270`. But at a pole arising from a nontrivial zero `rho`, namely `s=rho-1/2`, the multiplier is

\[
1-q^{1-\rho}\neq0,
\tag{7}
\]

because `0<Re rho<1` gives `|q^(1-rho)|>1`. Thus no off-critical zero pole is removed.

The more important positivity consequence is stronger. Writing the Jordan decomposition

\[
\Delta_q\mu=(\Delta_q\mu)_+-(\Delta_q\mu)_-,
\tag{8}
\]

**both positive measures `(Delta_q mu)_+` and `(Delta_q mu)_-` are individually non-tempered.** The category descent in (4), when it occurs, is therefore irreducibly signed: taking positive and negative channels separately, total variation, an absolute value, or any positive completion that preserves those channels independently destroys the cancellation.

A matched nonarithmetic control separates pole cancellation from arithmetic content. For

\[
\mu_{\mathbb N}:=\sum_{n\ge1}n^{-1/2}\delta_{\log n},
\tag{9}
\]

the identical dilation coboundary

\[
\Delta_q\mu_{\mathbb N}
=\mu_{\mathbb N}-\sqrt qS_{\log q}\mu_{\mathbb N}
\tag{10}
\]

is tempered **unconditionally**. Hence the finite difference itself is only a generic pole-removal mechanism. What is arithmetic and target-strength is whether the post-cancellation Mangoldt remainder descends to the tempered category.

**Classification:** `EXACT-DERIVED + SOURCE-NATIVE-INTEGER-DILATION + ZERO-INDEPENDENT-POLE-ANNIHILATION + RH-EQUIVALENT-TEMPEREDNESS + SIGNED-COBOUNDARY + BOTH-JORDAN-PARTS-NONTEMPERED + POSITIVE-CHANNEL-SEPARATION-FAILS + MATCHED-CONTROL + NOT-A-WEIL-POSITIVITY-PROOF`.

## 1. The integer dilation is intrinsic to the arithmetic source

The translation in (3) is not a fitted displacement. In the logarithmic energy coordinate, multiplication by the integer `q` is exactly translation by `log q`. Acting on an atom from `n` gives

\[
\log n\longmapsto\log(qn)=\log n+\log q.
\tag{11}
\]

The coefficient `sqrt(q)` is likewise forced by the critical half-density scaling. If the leading continuous tangent is

\[
\lambda:=e^{x/2}\mathbf 1_{x\ge0}\,dx,
\tag{12}
\]

then

\[
\sqrt q\,S_{\log q}\lambda
=e^{x/2}\mathbf 1_{x\ge\log q}\,dx,
\tag{13}
\]

and therefore

\[
\boxed{
\lambda-\sqrt qS_{\log q}\lambda
=e^{x/2}\mathbf 1_{[0,\log q)}(x)\,dx.
}
\tag{14}
\]

The exponentially growing pole tangent is converted into a compactly supported boundary layer. This is the real-space version of the zero of the multiplier in (6) at `s=1/2`.

Thus the pole cancellation exposed by `WP-278` can be performed by a finite source self-difference, without first adjoining a continuous archimedean/pole background. The question is whether this source-native cancellation leaves an ordinary distribution with controlled growth. Equation (4) answers that question exactly: only under RH.

## 2. RH implies temperedness

Let

\[
M(X):=\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}.
\tag{15}
\]

Under RH, the standard von-Koch/Schoenfeld bound

\[
\psi(X)=X+O(\sqrt X\log^2X)
\tag{16}
\]

and partial summation give

\[
\begin{aligned}
M(X)
&=\frac{\psi(X)}{\sqrt X}
+\frac12\int_1^X\psi(t)t^{-3/2}\,dt\\
&=2\sqrt X+O(\log^3X).
\end{aligned}
\tag{17}
\]

The cumulative function of the signed measure (3) is, for `X>=q`,

\[
D_q(X)
:=M(X)-\sqrt q\,M(X/q).
\tag{18}
\]

The two leading square-root terms cancel exactly:

\[
2\sqrt X-\sqrt q\,2\sqrt{X/q}=0,
\tag{19}
\]

hence

\[
D_q(X)=O(\log^3X).
\tag{20}
\]

With `X=e^x`, the cumulative function of `Delta_q mu` therefore has polynomial growth `O(x^3)`. A locally finite signed measure whose cumulative function has polynomial growth defines the distributional derivative of a polynomially growing locally integrable function, hence a tempered distribution. This proves

\[
\mathrm{RH}\Longrightarrow\Delta_q\mu\in\mathcal S'(\mathbb R).
\tag{21}
\]

Notice what has happened: the same critical source that was exponentially non-tempered in `WP-269` becomes polynomial after a **finite signed arithmetic self-coupling**. No zeta zeros were used to choose the coupling, and no continuum counterterm was inserted by hand.

## 3. Temperedness forces RH

Conversely, suppose `Delta_q mu` is tempered. Its support lies in `[log 2,infinity)`, so the Fourier--Laplace transform of this half-line-supported tempered distribution is holomorphic for

\[
\operatorname{Re}s>0.
\tag{22}
\]

On the initial half-plane `Re s>1/2`, direct summation gives (6). Holomorphic uniqueness therefore requires the meromorphic continuation of the right-hand side of (6) to have no poles in `Re s>0`.

The pole of `-zeta'/zeta(s+1/2)` at `s=1/2`, corresponding to the pole of zeta at `1`, is canceled because

\[
1-q^{1/2-(1/2)}=0.
\tag{23}
\]

Now let `rho` be a nontrivial zero with `Re rho>1/2`. The logarithmic derivative has a pole at

\[
s_\rho=\rho-1/2,
\qquad \operatorname{Re}s_\rho>0.
\tag{24}
\]

At that point the finite-difference multiplier is

\[
1-q^{1-\rho}.
\tag{25}
\]

It cannot vanish. Indeed `Re rho<1` for every nontrivial zero, so

\[
|q^{1-\rho}|=q^{1-\operatorname{Re}\rho}>1.
\tag{26}
\]

Thus the pole at `s_rho` survives, contradicting the holomorphy forced by temperedness. Consequently zeta has no nontrivial zero to the right of the critical line. The functional equation and symmetry `rho -> 1-rho` then exclude zeros to the left as well, proving RH.

This establishes (4).

The argument also explains why the criterion is not a positivity theorem in disguise. Temperedness is already detecting the full zero-free half-plane after the source-native pole cancellation. The hard arithmetic content has not been transferred into an independent geometric sign theorem; it remains exactly target-strength analytic cancellation.

## 4. Both Jordan channels remain outside the tempered category

The signed difference (3) has coefficient at the atom `log m`

\[
c_q(m)
=\frac{\Lambda(m)-q\,\mathbf 1_{q\mid m}\Lambda(m/q)}{\sqrt m}.
\tag{27}
\]

Every prime atom remains positive. For a prime `p`, the second term is absent unless `q|p`; in the only possible case `q=p`, it contains `Lambda(1)=0`. Hence

\[
c_q(p)=\frac{\log p}{\sqrt p}>0.
\tag{28}
\]

By the prime number theorem and partial summation,

\[
\sum_{p\le X}\frac{\log p}{\sqrt p}
\sim2\sqrt X.
\tag{29}
\]

Therefore the positive Jordan part has exponential mass growth in logarithmic coordinate:

\[
(\Delta_q\mu)_+([0,x])\ge (2+o(1))e^{x/2}.
\tag{30}
\]

A positive tempered measure has at most polynomial mass growth, so `(Delta_q mu)_+` is not tempered.

The negative channel is equally large. For every prime `p` with `p\nmid q`, the integer `qp` has at least two distinct prime factors, hence

\[
\Lambda(qp)=0,
\tag{31}
\]

while the translated contribution gives

\[
c_q(qp)
=-\sqrt q\frac{\log p}{\sqrt p}<0.
\tag{32}
\]

Thus

\[
(\Delta_q\mu)_-([0,x])
\ge
\sqrt q\sum_{\substack{p\le e^x/q\\p\nmid q}}
\frac{\log p}{\sqrt p}
=(2+o(1))e^{x/2}.
\tag{33}
\]

The negative Jordan measure is also non-tempered. It follows immediately that the total variation `|Delta_q mu|` is non-tempered as well.

This is a decisive sign-order obstruction. The source-native operation can enter the ordinary distribution category only by allowing two individually inadmissible positive channels to cancel. Any architecture that forms their positive direct sum, takes absolute values, keeps them as separately positive sectors, or asks a positive majorant to dominate both recreates the exponential-growth obstruction of `WP-289`.

## 5. Matched control: generic pole removal is not arithmetic specificity

Consider the nonarithmetic counting half-density

\[
\mu_{\mathbb N}
:=\sum_{n\ge1}n^{-1/2}\delta_{\log n}.
\tag{34}
\]

Its Laplace transform is

\[
\mathcal L\mu_{\mathbb N}(s)=\zeta(s+1/2),
\qquad \operatorname{Re}s>1/2.
\tag{35}
\]

Applying the same integer dilation coboundary gives

\[
\mathcal L(\Delta_q\mu_{\mathbb N})(s)
=(1-q^{1/2-s})\zeta(s+1/2).
\tag{36}
\]

Again the multiplier cancels the pole at `s=1/2`. But there are no zero-generated poles because zeta itself, rather than its logarithmic derivative, appears.

The real-space estimate makes the difference even clearer. Euler--Maclaurin gives

\[
A(X):=\sum_{n\le X}n^{-1/2}
=2\sqrt X+\zeta(1/2)+O(X^{-1/2}).
\tag{37}
\]

Therefore

\[
A(X)-\sqrt qA(X/q)
=(1-\sqrt q)\zeta(1/2)+O_q(X^{-1/2}),
\tag{38}
\]

so `Delta_q mu_N` is tempered unconditionally.

This control rejects the interpretation that the mere existence of a finite pole-killing dilation difference is evidence for arithmetic Weil geometry. Such differences are generic consequences of matching a leading homogeneous growth law. The Riemann-specific content begins only after that generic cancellation, where the logarithmic derivative remembers the nontrivial zeros.

## 6. Aggressive falsification and relation to the current frontier

**This does not improve the RH-equivalent category descent of `WP-270`.** It changes *where* the pole subtraction comes from: a source-native finite semigroup difference replaces the inserted pole continuum. But the statement that the resulting object is tempered is still equivalent to RH. Hence this is not an unconditional preprocessing trick for a later positivity theorem.

**It does evade one narrower objection from `WP-289`, but only by becoming signed first.** The operation in (3) does not preserve the critical arithmetic covariance as a positive summand. It subtracts a translated copy of the same source before any scalar positivity is read. This is exactly the type of upstream signed interference left open by the positive-majorant no-go. Equations (30)--(33) then show that the sign is essential rather than cosmetic.

**It does not produce the archimedean Gamma term.** The coboundary cancels the pole tangent and leaves zero-sensitive arithmetic remainder. Nothing in (3) intrinsically generates the Riemann Gamma/digamma contribution or the full Weil explicit-formula quadratic form. A global candidate would still need a canonical finite--archimedean coupling and an independent sign theorem.

**Symmetrization does not change the conclusion.** Adding the reflected copy of (3) produces an even signed carrier on the full logarithmic line. Its two Jordan channels still have exponential growth, while its temperedness remains equivalent to the one-sided criterion and therefore to RH.

**Moving away from the critical half-density changes the problem.** The cancellation coefficient is tied to the homogeneity `e^(x/2)`. Replacing the critical source by another weight gives the corresponding homogeneous finite difference, but it no longer targets the Weil critical normalization.

The surviving search is therefore more specific than after `WP-289`. Source-native semigroup operations can indeed supply the required *pre-positive signed interference* and can eliminate the largest pole continuum without importing zero locations. What they have not supplied is an independently positive global geometry. The first exact example already shows the danger: the point at which the signed carrier becomes an ordinary tempered object is itself RH-equivalent.

## 7. Prior-art and novelty audit

No novelty is claimed for the individual analytic ingredients. The identity `-zeta'/zeta=sum Lambda(n)n^-s`, finite Euler-factor/pole-killing multipliers, von-Koch type RH error estimates, and Fourier--Laplace theory for half-line-supported tempered distributions are classical. The transform (6) is an elementary consequence of those ingredients.

A bounded literature search was made for the exact critical object `sum Lambda(n)/sqrt(n) delta_(log n)`, integer dilation/translation differences, formulas equivalent to `psi(x)-q psi(x/q)`, and the multiplier `1-q^(1/2-s)` used as a temperedness criterion for RH. No direct named theorem or paper matching the exact statement (4), together with the Jordan-channel obstruction (30)--(33), was located. That absence is not evidence that the criterion is historically new.

The closest exact prior-art anchor remains `WP-270`: Arias de Reyna identifies the pole-completed critical Mangoldt measure whose temperedness is equivalent to RH. The present result should therefore be read as a **Mathia-native structural refinement of that boundary**, not as a new RH criterion. It shows that the pole continuum can be annihilated internally by an integer semigroup coboundary, and then proves that the resulting category descent remains target-strength and cannot be factorized into admissible positive channels.

## Consequence for `weil_positivity`

A viable route may still use an upstream signed, nonlocal, or quotient operation before final positivity; `WP-289` already makes such a step necessary. `WP-290` now supplies a concrete source-native example and a sharper rejection test.

If an arithmetic self-coupling merely kills the homogeneous pole mode while leaving the nontrivial-zero poles untouched, then proving that its output lies in the ordinary tempered/continuous category can already be equivalent to RH. And if the coupling decomposes into positive channels whose individual critical masses retain exponential growth, no independent positive-energy theorem may be applied channelwise before the cancellation.

The desired geometry must therefore do more than renormalize the source into an admissible distribution. It must produce a canonical finite--archimedean pairing in which the required signed cancellation is built into the geometry **before** positivity, while nonnegativity itself follows from an independent geometric theorem and not from the RH-equivalent success of that cancellation.