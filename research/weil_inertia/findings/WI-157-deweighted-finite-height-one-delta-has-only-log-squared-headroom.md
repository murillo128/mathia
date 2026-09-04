# WI-157 — the deweighted finite-height one-delta problem has only `O((log T)^-2)` headroom

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY + PRIOR-ART-REDIRECT`.

WI-156 proves that post-hoc choice among any **fixed finite** family of separately valid support-one scalar Lamzouri censuses remains at the Montgomery--Taylor/CCLM barrier. It correctly leaves a growing or `T`-dependent portfolio open because pointwise fixed-test pair-correlation asymptotics do not automatically give uniformity. The first apparent nonuniform mechanism is support-edge concentration: the unconditional form factor contains the finite-height term `T^{-2 alpha} log T`, whose approximate-delta action need not equal evaluation at zero for a test that changes with `T`.

For the **unweighted scalar census actually needed by the Lamzouri inequality**, however, the exact weight-removal step cancels that apparent `O(1/log T)` Poisson relaxation. After deweighting, the finite-height main variational problem is an explicit perturbation of the CCLM one-delta problem by only `1/(2 log^2 T)`. Its sharp infimum can be solved exactly. Consequently, every `T`-dependent support-one scalar family for which the Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh error remains uniformly `o(1)` still has asymptotic ceiling `H_MT`; the deterministic main term offers only `O((log T)^-2)` extra headroom. A fixed positive improvement from a growing scalar portfolio must therefore come from genuinely nonuniform arithmetic error or leave the one-scalar/support-one abstraction.

This finding does **not** bound matrix/Gram-defect methods, joint multi-profile inequalities, higher correlations, or justified wider support. It closes only the regular growing-family loophole left explicitly open in WI-156.

## 1. Start from the unconditional form factor before passing to a fixed test

Let

\[
L:=\log T.
\]

Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh prove unconditionally, uniformly for `0 <= alpha <= 1`,

\[
F_T(\alpha)
=
e^{-2L\alpha}\bigl(L+O(1)\bigr)
+\alpha
+O(L^{-1/2}).
\tag{1}
\]

This is their Theorem 1. Their Lemma 5 obtains the usual fixed-test formula by integrating (1) against a real even profile supported in `[-1,1]`. Lamzouri's Lemma 3.1 quotes that result, and his equation (3.2) performs the exact correction needed to remove the Weil/Montgomery weight

\[
w(u)=\frac4{4-u^2}.
\]

For a desired real even spectral profile `phi` supported in `[-1,1]`, define

\[
r_{L}(\alpha)
:=
\phi(\alpha)-\frac{\phi''(\alpha)}{4L^2}.
\tag{2}
\]

If

\[
H(z)=\widehat\phi(z),
\]

then at the zero difference

\[
z=i(\rho-\rho')\frac{L}{2\pi}
\]

we have

\[
\widehat{r_L}(z)\,w(\rho-\rho')
=H(z).
\tag{3}
\]

Thus the unweighted pair sum entering the scalar census is obtained by integrating the form factor against `r_L`, not against `phi` itself. This distinction is harmless for a fixed test but load-bearing for a `T`-dependent family.

Assume first that `phi` is smooth and compactly supported in `(-1,1)`. Evenness gives `phi'(0)=0`, and two integrations by parts give the exact identity

\[
2L\int_0^1e^{-2L\alpha}r_L(\alpha)\,d\alpha
=\phi(0).
\tag{4}
\]

Similarly,

\[
2\int_0^1\alpha r_L(\alpha)\,d\alpha
=
2\int_0^1\alpha\phi(\alpha)\,d\alpha
-
\frac{\phi(0)}{2L^2}.
\tag{5}
\]

Therefore the deterministic main coefficient of the **deweighted** finite-height scalar census is

\[
\boxed{
C_L(\phi)
=
\phi(0)
+2\int_0^1\alpha\phi(\alpha)\,d\alpha
-
\frac{\phi(0)}{2L^2}.
}
\tag{6}
\]

The tempting Poisson-kernel defect from integrating `phi` directly has disappeared exactly. What survives is only the explicit `-phi(0)/(2L^2)` term.

## 2. Rewrite (6) as a perturbed one-delta problem

Under the scalar universality hypotheses of WI-153, real two-point tests force

\[
H(x)\ge0\quad(x\in\mathbb R),
\qquad
H(0)=1,
\qquad
\operatorname{supp}\widehat H\subset[-1,1],
\tag{7}
\]

with `H in L^1(R)`. As in CCLM, write

\[
H(x)=|S(x)|^2,
\tag{8}
\]

where `S` is an entire function of exponential type `pi` in the Paley--Wiener space. Let `f` be its Fourier transform, supported on

\[
I=[-1/2,1/2].
\]

The normalization `H(0)=1` is

\[
|S(0)|^2=1.
\]

After a harmless phase choice we impose

\[
S(0)=\int_I f(u)\,du=1.
\tag{9}
\]

The triangular Fourier identity gives

\[
\int_{\mathbb R}H(x)
\left(\frac{\sin\pi x}{\pi x}\right)^2dx
=
1-2\int_0^1\alpha\phi(\alpha)\,d\alpha.
\tag{10}
\]

Also

\[
\phi(0)=\int_{\mathbb R}H(x)\,dx
=\int_I|f(u)|^2du.
\tag{11}
\]

Put

\[
c_L:=1-\frac1{2L^2}.
\tag{12}
\]

Then (6) becomes

\[
C_L(\phi)
=
1+Q_{c_L}(f),
\tag{13}
\]

where

\[
Q_c(f)
:=
c\int_I|f(u)|^2du
-
\int_I\int_I
(1-|u-v|)f(u)\overline{f(v)}\,du\,dv.
\tag{14}
\]

For `L>sqrt(2)` this quadratic form is strictly positive. Indeed the integral operator

\[
(Bf)(u)=\int_I(1-|u-v|)f(v)\,dv
\]

satisfies by Schur's test

\[
\|B\|
\le
\sup_{u\in I}\int_I(1-|u-v|)dv
=\frac34,
\tag{15}
\]

while `c_L>3/4` for `L>sqrt(2)`. Hence the finite-height extremal problem is a genuine Hilbert-space minimization.

## 3. The perturbed extremal is solvable in closed form

For any `c>3/4`, minimize `Q_c(f)` subject to (9). The unique minimizer may be chosen real and even and satisfies the Euler--Lagrange equation

\[
(cI-B)f=m_c\,\mathbf 1.
\tag{16}
\]

Let `h=Bf`. On the interior of `I`,

\[
h''(u)=-2f(u).
\tag{17}
\]

Differentiating (16) twice therefore yields

\[
c f''(u)+2f(u)=0.
\tag{18}
\]

Set

\[
\kappa_c:=\sqrt{\frac2c}.
\]

Evenness and the normalization (9) give

\[
\boxed{
f_c(u)
=
\frac{\kappa_c}{2\sin(\kappa_c/2)}
\cos(\kappa_c u).
}
\tag{19}
\]

Conversely, for this `f_c` the left side of (16) has zero second derivative and is even, hence is constant, so (19) really is the minimizer. At `u=1/2`, evenness and total mass one imply

\[
(Bf_c)(1/2)
=
\int_I(1/2+v)f_c(v)dv
=\frac12.
\tag{20}
\]

Thus the exact minimum is

\[
\boxed{
m(c)
=
\frac{c\kappa_c}{2}
\cot\frac{\kappa_c}{2}
-
\frac12
=
\sqrt{\frac c2}
\cot\frac1{\sqrt{2c}}
-
\frac12.
}
\tag{21}
\]

At `c=1` this is precisely the Montgomery--Taylor/CCLM one-delta constant

\[
m_{\rm MT}
=
\frac1{\sqrt2}\cot\frac1{\sqrt2}-\frac12.
\tag{22}
\]

For the actual finite-height deweighting `c=c_L`, equations (13)--(21) prove the sharp main-term bound

\[
\boxed{
C_L(\phi)
\ge
1+m(c_L).
}
\tag{23}
\]

The smooth compactly supported profiles required for the direct integration-by-parts argument are dense in the Paley--Wiener formulation, so (23) is the sharp infimum for that smooth class as well; equality itself may be understood at the Hilbert extremizer before smoothing.

## 4. The entire deterministic headroom is only `O(L^-2)`

Since

\[
c_L=1-\frac1{2L^2},
\]

Taylor expansion of (21) at `c=1` gives

\[
\boxed{
m(c_L)
=
m_{\rm MT}
-
\frac{\kappa_*}{L^2}
+O(L^{-4}),
}
\tag{24}
\]

where, writing `q=1/sqrt(2)`,

\[
\kappa_*
:=
\frac14
\left(
q^2\csc^2q+q\cot q
\right)
=
0.5030635954329\ldots .
\tag{25}
\]

Hence the best lower bound that the finite-height **main term alone** could feed into a scalar Lamzouri census is

\[
2-(1+m(c_L))
=
H_{\rm MT}
+
\frac{0.5030635954\ldots}{(\log T)^2}
+O((\log T)^{-4}).
\tag{26}
\]

In particular there is no fixed positive asymptotic gain hidden in choosing a more and more singular support-one scalar profile. The finite-height relaxation vanishes quadratically in `1/log T` after the mandatory deweighting.

This also corrects a misleading intermediate model. If one integrates the form factor directly against `phi`, before removing `w`, the exponential term is a Poisson/Cauchy approximate identity and a support-edge profile appears to create an `O(1/L)` relaxation. Equations (2)--(5) show that this is not the relevant unweighted census: Lamzouri's exact `phi''/(4L^2)` correction cancels that effect.

## 5. Uniform-error gate for genuinely `T`-dependent portfolios

Theorem 1 of Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh is uniform in `alpha`, so its stated error can be integrated against a `T`-dependent `r_L` with explicit norm dependence. From (1),

\[
\frac{Q_{\phi,T}}{N(T)}
=
C_L(\phi)
+O\!\left(
\frac{\|r_L\|_\infty}{L}
+
\frac{\|r_L\|_1}{\sqrt L}
\right)
+o(1)
\tag{27}
\]

at the same normalization used in the support-one pair-correlation step, with the harmless Riemann--von Mangoldt normalization absorbed into `o(1)`. The first term comes from integrating the uniform `O(1)e^{-2L alpha}` error and the second from the uniform `O(L^{-1/2})` error.

Therefore any growing/adaptive scalar family satisfying

\[
\boxed{
\|r_L\|_\infty=o(L),
\qquad
\|r_L\|_1=o(\sqrt L)
}
\tag{28}
\]

has uniform pair-correlation error `o(1)`. Combining (23), (24), and (27),

\[
\boxed{
\frac{Q_{\phi,T}}{N(T)}
\ge
C_{\rm MT}-o(1),
}
\tag{29}
\]

so post-hoc selection from **any finite, growing, or continuum family satisfying (28) uniformly** still cannot certify an asymptotic proportion above

\[
H_{\rm MT}+o(1).
\tag{30}
\]

Thus WI-156's infinite-family loophole is no longer merely described as “uniformity is needed.” A support-one scalar escape must violate an explicit regularity gate such as (28), exploit the resulting nonuniform arithmetic remainder with a new theorem, or introduce information that does not factor through one scalar pair-sum census.

## 6. Scope and stress tests

### This does not cap the current Weil-inertia record

The Gram-defect/local-geometry improvements already established in this research line exceed `H_MT` because they retain matrix and local configuration information discarded by the scalar cost. Equations (23)--(30) concern only the fully scalarized Lamzouri/one-delta architecture.

### The deweighting correction is load-bearing

Replacing `r_L` by `phi` for a changing profile produces the wrong finite-height variational problem. The exact identity (3) is what turns the weighted unconditional Montgomery formula into the unweighted kernel required by the zero-side census. This is precisely why Lamzouri introduces his `Q-Q''/(4 log^2 T)` test rather than applying Lemma 3.1 to a `T`-dependent desired kernel directly.

### No claim is made for profiles outside the controlled arithmetic regime

A family with `||r_L||_1` or `||r_L||_infty` growing too quickly is not covered by (29). The current BGSTB theorem then supplies no `o(1)` integrated remainder. Such a family is not a free improvement: exploiting it requires genuinely stronger quantitative arithmetic control. This is the surviving boundary, not an omitted proof step.

### The exact finite-height extremal is a perturbation, not a new classical constant

CCLM Corollary 14 proves the `c=1` one-delta theorem and its equality case, tracing it to Montgomery--Taylor. The formula (21) for `c<1` follows by the same Paley--Wiener/RKHS mechanism with the identity coefficient changed from `1` to `c`. The literature audit located variants of the one-delta problem, but no source stating this particular deweighted finite-height perturbation. The novelty claim here is only the derived bridge from the exact BGSTB/Lamzouri deweighting to (21)--(30), not a claim of mathematical priority for the underlying variational technique.

## 7. Prior-art and novelty audit

Primary arithmetic input: Siegfred Alan C. Baluyot, Daniel Alan Goldston, Ade Irma Suriajaya and Caroline L. Turnage-Butterbaugh, *An unconditional Montgomery theorem for pair correlation of zeros of the Riemann zeta-function*, Acta Arith. 214 (2024), 357--376, arXiv:2306.04799. Their Theorem 1 gives (1) uniformly on `[0,1]`; Lemma 5 gives the fixed-test integrated form.

Primary deweighting input: Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882v1 (2 September 2026). Lemma 3.1 quotes the unconditional pair-correlation formula and equations (3.2)--(3.3) use exactly the `Q-Q''/(4 log^2 T)` correction abstracted in (2)--(5).

Primary sharp one-delta input: Emanuel Carneiro, Vorrapan Chandee, Friedrich Littmann and Micah B. Milinovich, *Hilbert spaces and the pair correlation of zeros of the Riemann zeta-function*, J. Reine Angew. Math. 725 (2017), 143--182, arXiv:1406.5462. Corollary 14 gives (22), with the original extremizer attributed to Montgomery--Taylor. Their Paley--Wiener/RKHS factorization is the established framework used in Section 3.

A targeted audit of the current `weil_inertia` chain found WI-153 as the sharp fixed support-one scalar barrier and WI-156 as the immediate predecessor explicitly leaving growing/infinite portfolios conditional on a uniform arithmetic theorem. Neither finding evaluates the mandatory finite-height deweighting for a changing profile or solves the resulting `c_L I-B` one-delta problem. The new substantive content is the exact cancellation (4), the closed-form finite-height infimum (21), its `O(L^-2)` convergence (24), and the explicit regularity gate (28) that extends the scalar barrier to growing adaptive families.

## Consequence for the research program

The obvious next attempt after WI-156 — evade the finite-portfolio theorem by taking more and more support-one scalar kernels as `T` grows — has essentially no deterministic room. Once the Weil weight is removed correctly, even the **best possible** finite-height scalar main term improves the MT ceiling by only `O((log T)^-2)`, while the unconditional arithmetic theorem has a much larger `O((log T)^-1/2)` pointwise remainder before test norms are accounted for. A fixed asymptotic gain cannot come from scalar portfolio size or support-edge concentration alone.

The surviving routes are therefore the ones already structurally distinct in the mandate: a genuinely joint matrix/multi-profile inequality, new horizontal arithmetic information controlling a nonuniform family, higher/mixed correlations, or justified support beyond one. This finding prevents further effort from being spent treating fixed-test nonuniformity as if it were itself an untapped positive constant.
