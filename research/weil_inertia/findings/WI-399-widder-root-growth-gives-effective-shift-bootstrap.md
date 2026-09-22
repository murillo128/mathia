# WI-399 — Widder root growth gives an exact effective-shift defect bootstrap

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + CLASSICAL-IDENTITY + SHARP-STRUCTURAL-BARRIER + PRIOR-ART-REDIRECT + BOOTSTRAP-INTERFACE`.

**Parent findings:** WI-393, WI-395, WI-398.

## Claim

A recent non-peer-reviewed preprint of Zeraoulia Rafik introduces a fixed-height high-order Widder hierarchy for

\[
G(x)=\xi\!\left(\frac12+\sqrt x\right),
\qquad
F_\xi(x)=2\frac{G'(x)}{G(x)},
\]

and proves an RH-equivalent prime-side root-growth criterion. This is materially different from the density-normalized moving-carrier interfaces of WI-393--WI-398: a single off-critical zero already produces an exponentially growing high-order mode at a suitable fixed height.

The load-bearing prime/zero interface of that criterion has now been reconstructed independently from the genus-zero product for `G`, the classical Guinand--Weil explicit formula, elementary beta-kernel estimates, and a Cauchy--Hadamard root-radius argument. This strengthens the evidence for the interface used by WI-399--WI-402 without treating the rest of the recent preprint as independently validated.

For fixed `T>=2`, let

\[
L_{\mathcal P}(T)
:=
\limsup_{m\to\infty}|\mathcal P_m(T)|^{1/m}.
\]

The source's optimized absolute-convergence contour shift gives

\[
L_{\mathcal P}(T)
\le
\mathcal M(T)
:=
\frac{2}{1+\sqrt{1-T^{-2}}}.
\tag{1}
\]

For a hypothetical zero

\[
\rho=\frac12+\delta+i\gamma,
\qquad 0<|\delta|<\frac12,
\]

put

\[
w_\rho=(\gamma-i\delta)^2
\]

and define its one-zero Widder root amplification by

\[
R_{\delta,\gamma}(T)
:=
4T^2\frac{|w_\rho|}{|T^2+w_\rho|^2}.
\tag{2}
\]

Then, for every `T>=2`,

\[
\boxed{
\mathcal M(T)
=
\sup_{|\delta|<1/2}\sup_{\gamma>0}R_{\delta,\gamma}(T).
}
\tag{3}
\]

More strongly, with

\[
M(\sigma)
:=
\frac{2}{1+\sqrt{1-4\sigma^2}},
\qquad 0\le\sigma<\frac12,
\tag{4}
\]

one has

\[
\boxed{
R_{\delta,\gamma}(T)
\le M(|\delta|/T)
< M(1/(2T))=\mathcal M(T).
}
\tag{5}
\]

The first inequality is sharp for every fixed horizontal depth `|delta|`: the maximizing ordinate is explicit. Thus the optimized **absolute** prime-side root bound is exactly the strip-edge envelope of the **single-zero** signal.

There is also an exact conditional effective-width interface. Fix `0<=a<1/2`. If, for all fixed `T` beyond some threshold, one could prove

\[
\boxed{
L_{\mathcal P}(T)\le M(a/T),
}
\tag{6}
\]

then every zero whose corresponding saddle height lies beyond that threshold would satisfy

\[
\boxed{
|\Re\rho-1/2|\le a.
}
\tag{7}
\]

If (6) holds for every fixed `T>=2`, then (7) holds for every nontrivial zero. At `a=1/2` this reduces to the ordinary critical strip; at `a=0` it is the RH root threshold. This is a defect-to-zero *interface*, not a self-starting bootstrap theorem: WI-400 shows that feeding the sharp width-only envelope back through the same scalar profile is idempotent.

No improved simple-critical-zero proportion and no proof of RH is claimed.

## 1. Primary source and exact theorem boundary

The direct source is Zeraoulia Rafik, *Uniform Beta Smoothing of Widder Sums for the Riemann xi-Function and a Schur--Triple Application to Simple Critical Zeros*, Preprints.org manuscript `202609.1018`, version 2, posted 17 September 2026:

<https://www.preprints.org/manuscript/202609.1018>

It is explicitly non-peer-reviewed.

For fixed `T`, Proposition A1 defines

\[
\mathcal R(T)
:=
4T^2\max_{\rho\in\mathcal Z_+}
\left|
\frac{w_\rho}{(T^2+w_\rho)^2}
\right|
\tag{8}
\]

and states

\[
\limsup_{m\to\infty}
|T^2A'_m(T^2)|^{1/m}
=
\mathcal R(T).
\tag{9}
\]

Lemma A1 gives

\[
2T^2A'_m(T^2)
=
\mathcal H_m(T)-\mathcal P_m(T),
\qquad
\mathcal H_m(T)=O_T(1),
\tag{10}
\]

uniformly in `m`. Theorem A2 concludes

\[
\boxed{
\mathrm{RH}
\iff
L_{\mathcal P}(T)\le1
\quad\text{for every fixed }T\ge2.
}
\tag{11}
\]

Proposition A2 gives the absolute-convergence estimate (1). These are the source statements used by this finding. The independent reconstruction below checks their load-bearing normalization and root-rate mechanism directly; it does **not** certify the preprint's separate Schur--triple computation, smoothing theorem in all joint ranges, generating-function refinements, or every later appendix claim.

## 2. Independent reconstruction of the prime/zero interface

### 2.1 Genus-zero product and the Widder zero sum

Set

\[
H(y)=\xi\!\left(\frac12+y\right),
\qquad
H(y)=G(y^2).
\]

The classical functional equation makes `H` even. Since `H` has order one, `G` has order `1/2`, hence genus zero. Its zeros are `-w_rho`, with

\[
w_\rho=(\gamma-i\delta)^2,
\qquad
\rho=\frac12+\delta+i\gamma,
\qquad \gamma>0.
\]

The standard zero count `N(U)=O(U log U)` gives

\[
\sum_{\rho\in\mathcal Z_+}\frac1{|w_\rho|}<\infty,
\]

so the canonical product and logarithmic derivative are locally normally convergent away from the zeros:

\[
G(x)=G(0)
\prod_{\rho\in\mathcal Z_+}
\left(1+\frac{x}{w_\rho}\right),
\qquad
F_\xi(x)
=2\sum_{\rho\in\mathcal Z_+}\frac1{x+w_\rho}.
\tag{12}
\]

Differentiating the Widder expression term by term gives the exact identity

\[
T^2A'_m(T^2)
=
\frac{T^{2m}}{B(m,m)}
\sum_{\rho\in\mathcal Z_+}
\left(
\frac{w_\rho}{(T^2+w_\rho)^2}
\right)^m.
\tag{13}
\]

Write

\[
q_\rho(T)
:=
\frac{w_\rho}{(T^2+w_\rho)^2},
\qquad
S_m(T):=\sum_\rho q_\rho(T)^m.
\]

For fixed `T`, `q_rho(T)=O(gamma^{-2})`, so `sum |q_rho(T)|<infinity` and the maximum

\[
Q(T):=\max_\rho|q_\rho(T)|
\]

is attained. The generating series

\[
\sum_{m\ge1}S_m(T)z^m
=
\sum_\rho\frac{q_\rho(T)z}{1-q_\rho(T)z}
\tag{14}
\]

has radius exactly `Q(T)^{-1}`. Indeed, at `z=1/q_*` for a maximizing value `q_*`, the finitely many identical maximizing terms give a genuine pole; all nonidentical large terms are finite in number and the tail is analytic in a larger disk because `q_rho(T)->0`. Cauchy--Hadamard therefore yields

\[
\limsup_{m\to\infty}|S_m(T)|^{1/m}=Q(T).
\tag{15}
\]

Since `B(m,m)^{-1/m}->4`, (13) gives (9) exactly:

\[
\limsup_{m\to\infty}|T^2A'_m(T^2)|^{1/m}
=4T^2Q(T)=\mathcal R(T).
\tag{16}
\]

This proof avoids any phase-selection or unique-dominant-pair hypothesis.

### 2.2 Guinand--Weil normalization and the prime functional

Put

\[
p_m(y)
:=
\frac{y^{2m}}{B(m,m)(1+y^2)^{2m}},
\qquad
h_{m,T}(r):=p_m(r/T).
\]

For a zero written as

\[
\rho=\frac12+i\Gamma_\rho,
\qquad
\Gamma_\rho=\gamma-i\delta,
\]

one has `Gamma_rho^2=w_rho`; evenness pairs upper and lower zeros, and (13) gives

\[
\sum_{\rho\ \mathrm{all}}h_{m,T}(\Gamma_\rho)
=2T^2A'_m(T^2).
\tag{17}
\]

The beta test is even, holomorphic in the Guinand--Weil strip for `T>=2`, and decays like `|r|^{-2m}` there, so it is admissible in the classical explicit formula.

As an independent normalization check, Chirre--Goncalves, *Bounding the log-derivative of the zeta-function*, Math. Z. 300 (2022), Proposition 5, uses

\[
\widehat h(\xi)=\int_{\mathbb R}h(r)e^{-2\pi ir\xi}\,dr
\]

and states the Guinand--Weil formula with prime term

\[
-\frac1\pi
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\widehat h\!\left(\frac{\log n}{2\pi}\right).
\]

See <https://doi.org/10.1007/s00209-021-02820-9>. Rafik instead writes

\[
g(u)=\frac1{2\pi}\int_{\mathbb R}h(r)e^{-iur}\,dr.
\]

The relation

\[
\widehat h(\xi)=2\pi g(2\pi\xi)
\]

turns the published prime term exactly into

\[
-2\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}g(\log n),
\tag{18}
\]

and likewise converts the `log pi` term with the same normalization. Thus there is no hidden `2`, `pi`, or Fourier-convention mismatch in (10).

For `h=h_{m,T}`, scaling and a residue at the pole `-i` give, for `u>0`,

\[
g_{m,T}(u)
=T e^{-Tu}R_m(Tu),
\tag{19}
\]

with the same residue polynomial `R_m` used in the preprint. Hence (18) is exactly `-mathcal P_m(T)` with the source definition

\[
\mathcal P_m(T)
=2T\sum_{n\ge2}
\frac{\Lambda(n)}{n^{T+1/2}}
R_m(T\log n).
\tag{20}
\]

The remaining explicit-formula terms are exactly `mathcal H_m(T)`.

### 2.3 The nonprime terms are uniformly bounded in the order

For fixed `T>=2`, the three pieces of `mathcal H_m(T)` are harmless at exponential scale. First,

\[
\int_{\mathbb R}p_m(y)\,dy=O(1),
\]

so `g_{m,T}(0)=O_T(1)`. Second, with `u=1/(2T)<=1/4`,

\[
|h_{m,T}(i/2)|
=
\frac1{4^mB(m,m)}
\left(\frac{4u^2}{(1-u^2)^2}\right)^m,
\]

and the factor in parentheses is strictly below one, while `(4^mB(m,m))^{-1}=O(sqrt(m))`; this term is bounded and in fact decays exponentially.

For the gamma-factor integral use the classical bound

\[
\left|\frac{\Gamma'}{\Gamma}
\left(\frac14+\frac{ir}{2}\right)\right|
\ll 1+\log(2+|r|).
\]

After `r=Ty`, the beta mass on `|y|<=1` is uniformly bounded, while for `m>=2`

\[
\int_0^\infty y\,p_m(y)\,dy
=
\frac{m}{2(m-1)}\le1.
\tag{21}
\]

The case `m=1` is one fixed integrable function. Therefore

\[
\boxed{\mathcal H_m(T)=O_T(1)}
\tag{22}
\]

uniformly in `m`, independently recovering the part of Lemma A1 that is relevant to root growth.

### 2.4 Every root threshold above one transfers exactly

Combining the classical explicit formula, (17), and (22) gives (10) independently. A bounded perturbation cannot change an `m`-th-root limsup above the neutral value one. Consequently

\[
\boxed{
\max\{1,L_{\mathcal P}(T)\}
=
\max\{1,\mathcal R(T)\}
}
\qquad(T\ge2).
\tag{23}
\]

This is the threshold transport used explicitly in WI-400.

Under RH every `w_rho` is positive and

\[
\frac{4T^2w_\rho}{(T^2+w_\rho)^2}\le1,
\]

so `mathcal R(T)<=1`. Conversely, if one zero is off the critical line, write `w=re^{i phi}` with `phi` nonzero. Choosing `T^2=r=|w|` gives

\[
R_{\delta,\gamma}(T)
=
\frac{4r^2}{|r+re^{i\phi}|^2}
=
\sec^2(\phi/2)>1.
\tag{24}
\]

For a nontrivial zeta zero this `T` is greater than 14, hence allowed. Equation (23) then forces `L_mathcal P(T)>1`. This gives a short independent proof of the equivalence (11) and needs neither the source's stronger all-orders cosine asymptotic nor a uniqueness-of-dominance choice.

### 2.5 Independent check of the absolute-convergence endpoint

The source's bound (1) can also be recovered at the root-rate level without using its final estimate as a black box. For `u>0`, shift the Fourier line for `g_{m,T}(u)` from the real axis to `y-i sigma`, where

\[
a:=T\sigma>\frac12
\]

and `a` is taken arbitrarily close to `1/2`. No pole is crossed for such `sigma` when `T>=2`. The shift supplies the factor `e^{-au}`. Moreover

\[
|p_m(y-i\sigma)|
=
\frac{1}{4^mB(m,m)}
\mathcal R_\sigma(y)^m,
\]

where

\[
\mathcal R_\sigma(y)
=
\frac{4(y^2+\sigma^2)}
{(1+y^2-\sigma^2)^2+4y^2\sigma^2}.
\tag{25}
\]

For fixed `sigma`, `mathcal R_sigma` is integrable and tends to zero quadratically. Writing `v=y^2+sigma^2`, its denominator becomes `(1+v)^2-4sigma^2`; direct differentiation gives, in the range needed here,

\[
\sup_y\mathcal R_\sigma(y)
=
M(\sigma)
=
\frac{2}{1+\sqrt{1-4\sigma^2}}.
\tag{26}
\]

Thus

\[
\int_{\mathbb R}\mathcal R_\sigma(y)^m\,dy
\le
M(\sigma)^{m-1}
\int_{\mathbb R}\mathcal R_\sigma(y)\,dy,
\]

and `(4^mB(m,m))^{-1/m}->1`. The shifted prime sum is absolutely convergent because

\[
\sum_{n\ge2}\Lambda(n)n^{-1/2-a}<\infty.
\]

Therefore

\[
L_{\mathcal P}(T)\le M(a/T).
\]

Letting `a` decrease to `1/2` proves (1). This independently confirms the exact absolute-convergence width and shows why its constant is the same saddle later seen by one off-line zero.

## 3. Exact kernel identity: the prime saddle is the zero saddle

Set

\[
y=\frac\gamma T,
\qquad
\sigma=\frac{|\delta|}{T}.
\]

Then

\[
|w_\rho|=T^2(y^2+\sigma^2)
\]

and

\[
|T^2+w_\rho|^2
=T^4\left[(1+y^2-\sigma^2)^2+4y^2\sigma^2\right].
\]

Consequently

\[
\boxed{
R_{\delta,\gamma}(T)
=
\mathcal R_\sigma(y),
}
\tag{27}
\]

with exactly the same rational function as the shifted-prime contour calculation (25). Equation (26) proves (5).

The maximum occurs when

\[
y_\sigma^2+\sigma^2
=
\sqrt{1-4\sigma^2}.
\tag{28}
\]

For zeta, `sigma<1/4` when `T>=2`, safely inside the interior-maximizer range. Since `M` is strictly increasing on positive `sigma`, sending `|delta|` upward to the open strip edge `1/2` yields (3):

\[
\sup_{|\delta|<1/2,\gamma>0}R_{\delta,\gamma}(T)
=M(1/(2T))
=\mathcal M(T).
\]

The significance is not that the actual zeta zero set attains this geometric supremum. The point is that the optimized **absolute** prime estimate and the most adverse one-zero geometry are controlled by the same extremal rational function. Absolute shifted-kernel control is therefore saturated at the strip boundary.

As a useful special tuning, choosing

\[
T_\rho=\sqrt{\gamma^2+\delta^2}
\]

gives

\[
R_{\delta,\gamma}(T_\rho)
=1+\frac{\delta^2}{\gamma^2}>1
\tag{29}
\]

for every off-critical zero, reproducing the individual-defect visibility highlighted by the source.

## 4. Effective-width theorem

Suppose `|delta|=d>a` for some zero. Write

\[
r=\gamma^2+d^2.
\]

Choose

\[
\boxed{
T^2
=2d^2+\sqrt{r^2+4d^4}.
}
\tag{30}
\]

This is exactly equivalent to the saddle condition (28), hence

\[
R_{\delta,\gamma}(T)=M(d/T).
\tag{31}
\]

Strict monotonicity gives

\[
M(d/T)>M(a/T)>1.
\]

Therefore `mathcal R(T)>M(a/T)`, and the exact threshold transport (23) forces

\[
L_{\mathcal P}(T)>M(a/T).
\]

This contradicts (6) whenever the selected saddle `T` lies in the range where (6) is known. Hence (7) follows in precisely that range.

This gives `a` a literal interpretation as an **effective horizontal width** purchased by a signed-prime estimate. The existing absolute-convergence proof has width `1/2`; any genuine improvement to `a<1/2` gives the matching stricter horizontal zero strip. Reaching `a=0` is RH.

## 5. Quadratic coefficient and relationship to the preceding barriers

For fixed `a`,

\[
M(a/T)
=1+\frac{a^2}{T^2}+O_a(T^{-4}).
\tag{32}
\]

Thus the absolute endpoint is

\[
\mathcal M(T)
=1+\frac{1}{4T^2}+O(T^{-4}),
\tag{33}
\]

and the coefficient `1/4` is exactly the square of the critical-strip half-width. An estimate

\[
L_{\mathcal P}(T)
\le
1+\frac{c+o(1)}{T^2},
\qquad c<\frac14,
\]

would exclude any fixed-depth family with `|delta|>sqrt(c)+epsilon` at sufficiently large ordinate after saddle tuning. It would **not** by itself exclude zeros with horizontal depth tending to zero.

WI-393--WI-398 found a square-root-prime obstruction for moving-carrier Weil tests: density-normalized horizontal signals can suppress a finite or zero-density exceptional population. The Widder hierarchy escapes that particular population-averaging loss because a single nonreal reflected parameter already changes a fixed-height root rate. The arithmetic obstruction instead becomes the exact contour-width barrier above.

WI-400 sharpens the warning: over the full fixed-`T` profile, converting a known strip width `a` to the sharp envelope `M(a/T)` and back recovers `a` exactly. Therefore the present interface is an RH-sensitive detector, but no contraction follows from width information alone. A successful bootstrap must add signed prime cancellation, height/depth coupling, phase information, population/correlation information, or another independent invariant.

## 6. Prior art, novelty, and evidence boundary

The finite Stieltjes/Widder framework is classical. Bondesson--Simon, *Stieltjes functions of finite order and hyperbolic monotonicity*, Trans. Amer. Math. Soc. 370 (2018), 8279--8314, arXiv:`1604.05267`, develops finite Stieltjes classes and Widder derivative conditions. Recent work of Nicholas G. Polson develops related Thorin/GGC, Stieltjes, reciprocal-xi, and zero-measure formulations. None of that is claimed here as new.

Rafik's 17 September 2026 preprint is the direct prior art for the beta--Widder hierarchy, Proposition A1's zero-side spectral radius, Lemma A1's fixed-height explicit-formula relation, Theorem A2's root-growth RH criterion, and Proposition A2's optimized absolute endpoint. Those source claims remain attributed to the preprint.

The independent check above materially changes their evidential role in this line: the **specific load-bearing interface used by WI-399--WI-402 no longer rests only on accepting the preprint's proof**. Equations (12)--(26) reconstruct it from classical entire-function facts, the published Guinand--Weil formula with matched Fourier normalization, elementary beta moments, contour shifting in an absolute-convergence half-plane, and Cauchy--Hadamard. This is an evidence strengthening of the existing WI-399 claim identity, not a new priority claim and not a validation of the preprint as a whole.

The additional Mathia synthesis remains the exact identification (27) between the shifted-prime saddle and the normalized one-zero amplification, together with the effective-width implication (6)--(7). A fresh prior-art search across Widder/Stieltjes xi criteria, prime-side RH criteria, Guinand--Weil formulations, and recent Thorin work located no earlier explicit statement of this exact width-to-depth theorem. Search absence is not a priority claim.

The source's separate Schur--triple computer-assisted simple-zero value is not imported here. The present finding concerns only the fixed-height Widder/explicit-formula interface and its exact horizontal-defect interpretation.

## Decisive audit tests

The current finding can be falsified by any failure in the following chain:

1. `G` must genuinely have the genus-zero product (12), with `sum 1/|w_rho|<infinity`, and the Widder differentiation must give (13) with the stated beta normalization.
2. The generating function (14) must have radius exactly `Q(T)^{-1}`; in particular a maximizing pole must survive after separating the finite large terms and analytic tail.
3. Chirre--Goncalves Proposition 5 must convert to Rafik's Fourier convention exactly as in (18), with no missing factor in the prime or `log pi` terms, and the beta tests must satisfy its strip hypotheses.
4. The beta moments and digamma bound must give `mathcal H_m(T)=O_T(1)` uniformly in `m`.
5. The shifted contour must remain inside the pole-free strip, the prime Dirichlet series must be absolutely convergent for `a>1/2`, and the calculus maximum (26) must be correct.
6. The substitution `y=gamma/T`, `sigma=|delta|/T` must turn the one-zero factor exactly into the same `mathcal R_sigma(y)`, and (30) must enforce its saddle.

All six checks are exact; no numerical certificate is involved.

## Research consequence

The fixed-height Widder direction survives the first independent source audit at its load-bearing interface. It really does detect an individual off-line zero and really does transport every root threshold above one between zero and prime sides. At the same time, the independently reconstructed contour estimate confirms the sharp obstruction: pure absolute convergence lands exactly at the critical-strip width `1/2` and cannot narrow it.

The next useful question is therefore not another verification of the same root criterion. It is whether established information can make the prime root profile strictly smaller than the width-only envelope by exploiting **height-dependent** zero-free width, signed prime cancellation, or a richer coupled observable. Any proposed improvement should be tested against the exact profile (23)--(33) before being treated as a bootstrap.