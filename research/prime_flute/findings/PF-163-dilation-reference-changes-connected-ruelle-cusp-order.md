# PF-163 — dilation reference changes the connected Ruelle cusp from `log` to `log^2`

**Status:** `EXACT-DERIVED + CLASSICAL-INPUT + LITERATURE-AUDITED + DECISIVE-NEGATIVE/REFERENCE-DEPENDENCE`. PF-161 shows that, after the PF-159 one-ended subtraction, the canonical bottom-Ruelle product against the exact `p -> p+1` all-composite shift reference has a finite nonzero value at `s=0` and logarithmic derivative `~ C_* log(1/s)`. PF-162 then shows that the coefficient is reference-dependent across all fixed positive odd shifts. The present finding tests a stronger possible escape: perhaps the *type* of the boundary singularity is nevertheless intrinsic to the selected canonical separator sector.

It is not. For every fixed integer dilation `K>=2`, PF-105 supplies an equally exact all-composite control from the labels `Kp`, normalized by the hyperbolic isometry `z -> z/K`. Repeating the connected canonical bottom-Ruelle construction with that reference gives a finite positive value at `s=0`, but

\[
\boxed{
\frac d{ds}\log \mathcal R_{0,K}(s)
\sim
\alpha_K\left(\log\frac1s\right)^2,
\qquad
\alpha_K:=\frac{\pi^2}{3}\left(1-K^{-2}\right)>0.
}
\tag{1}
\]

Equivalently,

\[
\boxed{
\log \mathcal R_{0,K}(s)-\log \mathcal R_{0,K}(0)
\sim
\alpha_K s\left(\log\frac1s\right)^2.
}
\tag{2}
\]

Thus changing between two natural exact all-composite matched-reference families changes not merely the amplitude but the **logarithmic order** of the selected connected Ruelle cusp: fixed shifts give `log(1/s)`, whereas exact dilations give `log^2(1/s)`. The singularity type of this selected relative sector is therefore not an intrinsic invariant of the prime flute and cannot be promoted to a prime-gap/RH selector.

This is not a comparison of full Ruelle or Selberg zeta functions, scattering matrices, resonances, or Laplace spectra for the dilation clone.

## 1. Exact dilation reference and its slower endpoint defect

Keep the exact endpoint law

\[
V(x)=\pi\cot\frac{\pi}{x}.
\tag{3}
\]

For a fixed integer `K>=2`, the labels `Kp` are all composite. PF-105 observes that the exact flute built from `V(Kp)` is isometric, after `z -> z/K`, to the flute with normalized endpoints

\[
\boxed{W_K(x):=\frac1K V(Kx).}
\tag{4}
\]

Write

\[
\varepsilon_K(x):=W_K(x)-V(x).
\tag{5}
\]

Since `V'` is strictly decreasing to `1`,

\[
\varepsilon_K'(x)=V'(Kx)-V'(x)<0.
\tag{6}
\]

The cotangent expansion gives

\[
V(x)
=x-\frac{\pi^2}{3x}-\frac{\pi^4}{45x^3}+O(x^{-5}),
\]

hence

\[
\boxed{
\varepsilon_K(x)
=\frac{\alpha_K}{x}+O_K(x^{-3}),
\qquad
\varepsilon_K'(x)=O_K(x^{-2}),
}
\tag{7}
\]

with `alpha_K` as in (1). In particular `\varepsilon_K(x)>0` and decreases to zero.

This is the structural difference from PF-162's fixed shifts: their sampled endpoint defect is `O_m(x^-2)` and summable over primes, whereas the dilation reference has a positive `alpha_K/x` tail and therefore carries reciprocal-prime mass. PF-105 nevertheless proves that its complete marked tail cross-ratio defect still tends uniformly to zero and that the canonical fan-shear defect is `ell^1`.

## 2. The PF-159 one-ended factorization survives exactly

Take a PF-004 canonical separator with consecutive exterior prime pairs

\[
a<b<c<d.
\]

As in PF-159, put

\[
X=V(b)-V(a),\quad
Y=V(c)-V(b),\quad
Z=V(d)-V(c),\quad
S=X+Y+Z,
\]

\[
\chi=\frac{YS}{XZ},
\qquad
L=4\operatorname{arsinh}\sqrt\chi.
\tag{8}
\]

Use superscript `(K)` for the corresponding increments, cross-ratio and length formed from `W_K`. Since `\varepsilon_K` is decreasing,

\[
X^{(K)}=X+\varepsilon_K(b)-\varepsilon_K(a)<X.
\]

Define the exact left-edge response

\[
R_{a,K}:=\frac{X}{X^{(K)}}>1,
\tag{9}
\]

and the one-ended model

\[
\widehat\chi_K:=R_{a,K}\chi,
\qquad
\widehat L_K:=4\operatorname{arsinh}\sqrt{\widehat\chi_K}.
\tag{10}
\]

The same algebra as PF-159 gives the exact factorization

\[
\boxed{
\frac{\chi^{(K)}}{\widehat\chi_K}
=
\frac{Y^{(K)}}Y
\frac{S^{(K)}}S
\frac Z{Z^{(K)}}.
}
\tag{11}
\]

Fix the left pair `a<b` and send `c<d` through consecutive primes to infinity. Since `V(x)=x+O(x^-1)`, the Baker--Harman--Pintz envelope already audited in S6 gives `d-c=o(c)`. Equations (7) and (11) then imply

\[
\boxed{
 c\log\frac{\chi^{(K)}}{\widehat\chi_K}
 \longrightarrow
 -A_{a,K},
\qquad
A_{a,K}:=\varepsilon_K(a)+\varepsilon_K(b)>0.
}
\tag{12}
\]

Indeed the `Y` and `S` factors contribute `-\varepsilon_K(b)` and `-\varepsilon_K(a)` respectively, while

\[
\frac{\varepsilon_K(d)-\varepsilon_K(c)}{Z}=O_K(c^{-2})
\tag{13}
\]

because `Z>=d-c`. The far separator has `\chi -> infinity`, so

\[
\frac{d}{d\log\chi}
4\operatorname{arsinh}\sqrt\chi
\longrightarrow2.
\]

Consequently

\[
\boxed{
 c\bigl(L^{(K)}-\widehat L_K\bigr)
 \longrightarrow
 -2A_{a,K}.
}
\tag{14}
\]

For later uniform summation, (11) also yields in the far-span region `c>=4a`

\[
\boxed{
\left|L^{(K)}-\widehat L_K\right|
\le C_K\left(\frac1{ac}+\frac1{c^2}\right).
}
\tag{15}
\]

The first term comes from `|\varepsilon_K|=O_K(1/x)` divided by `Y,S\asymp c`; the second comes from the right exterior interval through (13).

## 3. The connected bottom product still has a finite nonzero value at zero

Define, for real `s>0`,

\[
\boxed{
\mathcal R_{0,K}(s)
:=
\prod_{\eta\in\mathcal C}
\frac{1-e^{-sL_\eta^{(K)}}}
     {1-e^{-s\widehat L_{K,\eta}}}.
}
\tag{16}
\]

As in PF-161,

\[
\left|
\log\frac{1-e^{-sL^{(K)}}}{1-e^{-s\widehat L_K}}
\right|
\le
\left|\log\frac{L^{(K)}}{\widehat L_K}\right|
\qquad(s\ge0),
\tag{17}
\]

where the local factor at zero is interpreted as `L^(K)/Lhat_K`. We claim

\[
\boxed{
\sum_{\eta\in\mathcal C}
\left|\log\frac{L_\eta^{(K)}}{\widehat L_{K,\eta}}\right|<\infty.
}
\tag{18}
\]

For `c<4a`, PF-105 gives `|log(chi^(K)/chi)|=O_K(a^-2)`. Equation (9) also has `log R_{a,K}=O_K(a^-2)`, hence

\[
\left|\log\frac{L^{(K)}}{\widehat L_K}\right|=O_K(a^{-2}).
\tag{19}
\]

The classical Chebyshev bound `pi(x)=O(x/log x)` gives only `O(a/log a)` possible right prime labels in this region. Therefore its total contribution is bounded by

\[
\sum_{a\ \mathrm{prime}}
O_K\!\left(\frac1{a\log a}\right)<\infty.
\tag{20}
\]

For `c>=4a`, PF-158's BHP lower bound gives

\[
\min(L^{(K)},\widehat L_K)\ge \kappa\log c-C_K
\tag{21}
\]

apart from finitely many pairs. Combining (15) and (21),

\[
\left|\log\frac{L^{(K)}}{\widehat L_K}\right|
\ll_K
\frac1{ac\log c}+
\frac1{c^2\log c}.
\tag{22}
\]

Now

\[
\sum_{c\ge4a\atop c\ \mathrm{prime}}
\frac1{c\log c}
\ll\frac1{\log a},
\tag{23}
\]

while the second term stays summable after counting at most `O(c/log c)` possible left prime labels below `c/4`. Thus (18) follows from the classical convergence of `sum_p 1/(p log p)`.

Equations (17)--(18) give uniform absolute convergence in logarithm on every real compact interval `0<=s<=S`. Hence

\[
\boxed{
0<\mathcal R_{0,K}(0)
:=
\prod_{\eta\in\mathcal C}
\frac{L_\eta^{(K)}}{\widehat L_{K,\eta}}
<\infty.
}
\tag{24}
\]

So the dilation reference, like the shift reference, produces neither a zero nor a pole at the selected bottom-Ruelle boundary.

## 4. The left-edge response now has divergent reciprocal-prime mass

Let `b` denote the prime immediately after `a`. Equation (7) and the BHP gap envelope give

\[
\boxed{
A_{a,K}
=\frac{2\alpha_K}{a}+O_K(a^{-2+0.525}).
}
\tag{25}
\]

The error is absolutely summable even over all integers. Mertens' theorem therefore yields

\[
\boxed{
\sum_{a\le x\atop a\ \mathrm{prime}} A_{a,K}
=2\alpha_K\log\log x+O_K(1).
}
\tag{26}
\]

This is exactly the extra logarithm absent from PF-161/PF-162. For any fixed shift `m`, the analogous left coefficients are `O_m(a^-2)` and have finite total mass. For a dilation clone, the exact one-ended response itself has a prime-harmonic left tail.

## 5. A second Mertens summation produces the `log^2` cusp

Put

\[
q_s(L):=\frac{L}{e^{sL}-1}.
\]

PF-161 records

\[
\frac{\partial q_s}{\partial L}
=-\frac12 h(sL),
\qquad
h(x):=2\frac{(x-1)e^x+1}{(e^x-1)^2}.
\tag{27}
\]

Here `h(0)=1`, `0<h(x)<=1`, and `h(x)=O((1+x)e^-x)`. In fact `h` is decreasing on `(0,infinity)`, since

\[
h'(x)
=-2\frac{e^x\bigl((x-2)e^x+x+2\bigr)}{(e^x-1)^3}<0.
\tag{28}
\]

For one separator the logarithmic-derivative summand is

\[
T_{a,c,K}(s)
:=q_s(L_{a,c}^{(K)})-q_s(\widehat L_{K,a,c}).
\tag{29}
\]

To isolate the leading term, fix any `M>1` and first restrict to the power-separated sector

\[
c\ge a^M.
\tag{30}
\]

In this sector the proof of (12) is uniform as `a->infinity`: `Y/c ->1`, `S/c ->1`, the terms involving `\varepsilon_K(c)` are negligible relative to `A_{a,K}`, and the `Z` term in (13) is smaller by a factor `a/c`. Moreover the far cross-ratio tends uniformly to infinity. Thus

\[
\boxed{
L_{a,c}^{(K)}-\widehat L_{K,a,c}
=-\frac{2A_{a,K}}c\,(1+o_M(1))
}
\tag{31}
\]

uniformly for `c>=a^M` after `a->infinity`. The mean-value theorem applied to (27) gives

\[
T_{a,c,K}(s)
=\frac{A_{a,K}}c\,(1+o_M(1))
 h(s\xi_{a,c}),
\tag{32}
\]

where `xi_{a,c}` lies between the two matched lengths. PF-158's far-span bounds imply constants `0<kappa_M<C_M<infinity` such that

\[
\kappa_M\log c-C_M
\le \xi_{a,c}\le
C_M\log c+C_M.
\tag{33}
\]

The classical Mertens asymptotic implies the Abelian estimate, for every fixed `beta>0`,

\[
\boxed{
\sum_{c\ \mathrm{prime}}
\frac{\log\log c}{c}
 h(\beta s\log c)
\sim
\frac12\left(\log\frac1s\right)^2.
}
\tag{34}
\]

A short proof is enough here. For `c<=exp(delta/s)`, `h(beta s log c)` tends uniformly to `1` as `delta downarrow0`, while partial summation of

\[
\sum_{p\le x}\frac1p=\log\log x+B+o(1)
\]

gives

\[
\sum_{p\le x}\frac{\log\log p}{p}
\sim\frac12(\log\log x)^2.
\]

For the upper tail, (27) gives exponential damping once `log c >>1/s`. Replacing the cutoff constant changes `log log(exp(C/s))` only by an additive constant, so the leading coefficient `1/2` is independent of the precise soft cutoff.

For each right prime `c`, (26) applied up to `c^(1/M)` gives

\[
\sum_{a\le c^{1/M}\atop a\ \mathrm{prime}}A_{a,K}
=2\alpha_K\log\log c+O_{K,M}(1).
\tag{35}
\]

Equations (32)--(35) therefore give the main contribution

\[
\alpha_K\left(\log\frac1s\right)^2
+o\!\left(\left(\log\frac1s\right)^2\right).
\tag{36}
\]

The omitted sectors are lower order. The near sector `c<4a` is uniformly summable by (19)--(20). In the transition strip

\[
4a\le c<a^M,
\]

(15) and `|partial_L q_s|<=1/2` reduce the first term to `O_K(a^-1)` after summing the bounded Mertens mass of `1/c` across that strip. The far-length lower bound then supplies the `h(s log a)` cutoff, so the total transition contribution is only

\[
O_{K,M}\!\left(\log\frac1s\right).
\tag{37}
\]

The `c^-2` error in (15) is summable, and finitely many left labels also contribute only `O(log(1/s))`. Hence

\[
\boxed{
\frac d{ds}\log\mathcal R_{0,K}(s)
=\sum_{a,c}T_{a,c,K}(s)
\sim
\alpha_K\left(\log\frac1s\right)^2,
}
\tag{38}
\]

which is (1). Integrating from zero, using the continuity in (24), gives (2).

## 6. Adversarial interpretation

PF-162 already rules out the coefficient of the PF-161 `s log(1/s)` cusp as an intrinsic quantity: it varies without bound across exact odd-shift all-composite references. The dilation family closes the stronger escape that the **singularity class itself** might survive reference changes.

The mechanism is transparent:

\[
\boxed{
\varepsilon_{\rm shift}(p)=O(p^{-2})
\Rightarrow
\sum_a A_a<\infty
\Rightarrow
G_0(s)\asymp\log(1/s),
}
\]

whereas

\[
\boxed{
\varepsilon_{\rm dilation}(p)\sim\alpha_K/p
\Rightarrow
\sum_{a\le x}A_a\sim2\alpha_K\log\log x
\Rightarrow
G_0(s)\sim\alpha_K\log^2(1/s).
}
\tag{39}
\]

Both controls are exact surfaces produced by the same sampled cotangent endpoint law from all-composite labels and normalized only by hyperbolic Möbius isometries. The difference is therefore a property of the chosen relative reference tail, not a new prime-flute spectral divisor.

Several overclaims are excluded.

- PF-105 does not prove that a dilation clone lies in the same compact-relative-resolvent or wave-operator class as the prime flute; those stronger operator results were proved only for the shift clone in later findings.
- The product (16) uses only the PF-004 canonical separator family after an explicit one-ended subtraction. It is not the full Ruelle zeta function of either surface.
- Equation (38) concerns the right-half-plane germ and its real `s downarrow0` boundary behavior. It does not prohibit a separately defined regularization, but any such renormalization would be a different object and would need an intrinsic spectral justification.
- The double logarithm comes from two classical reciprocal-prime summations acting on a reference defect. It does not encode prime-gap fluctuations or a critical-line divisor.

Any future relative Selberg/Ruelle proposal that claims arithmetic significance must therefore specify why its comparison surface is intrinsic and prove stability not only of coefficients but of the boundary singularity class under the exact matched controls allowed by the prime-flute mandate.

## 7. Prior art and novelty audit

No novelty is claimed for Mertens' reciprocal-prime theorem, Chebyshev prime counting, the local Ruelle factor, or the general fact that relative zeta/determinant constructions depend on a comparison object. Franz Mertens' original theorem is *Ein Beitrag zur analytischen Zahlentheorie*, J. reine angew. Math. 78 (1874), 46--62, DOI `10.1515/crll.1874.78.46`. Werner Müller's relative determinant framework (*Relative zeta functions, relative determinants and scattering theory*, Comm. Math. Phys. 192 (1998), 309--347, DOI `10.1007/s002200050301`) explicitly starts from an operator pair `(A,A_0)` and trace-class relative heat data. Borthwick--Judge--Perry relate Selberg zeta, scattering and determinants for geometrically finite / hyperbolic-near-infinity surfaces under finite-geometry hypotheses; those results do not supply a zeta theory for this zero-systole infinite-type flute. Dyatlov--Zworski's theorem on the Ruelle zeta at zero (Invent. Math. 210 (2017), 211--229, DOI `10.1007/s00222-017-0727-3`) concerns the genuine full Ruelle zeta of compact negatively curved surfaces and a topological zero order, not selected relative canonical separators.

Directed searches across relative determinants, Selberg/Ruelle theory, tight flutes and infinite-type hyperbolic surfaces did not locate a theorem treating the PF-004 separator family, the exact cotangent dilation clone, or the project-specific double-Mertens boundary law (38). The durable Mathia content is therefore the exact specialization

\[
\boxed{
W_K(x)=V(Kx)/K
\to
\varepsilon_K(x)\sim\alpha_K/x
\to
A_{a,K}\sim2\alpha_K/a
\to
\text{connected separator response }A_{a,K}/c
\to
\alpha_K\log^2(1/s),
}
\tag{40}
\]

and its adversarial consequence for the previously isolated selected Ruelle cusp. The warranted novelty classification is **prime-flute-specific reference-dependence/boundary refinement**, not a new general theorem about Ruelle zeta functions.

## Consequence for the research line

PF-158--PF-163 now remove the complete explicit canonical-separator Selberg/Ruelle branch as an intrinsic RH mechanism in progressively stronger form: the unrenormalized `1/4` boundary is one-ended propagation; the connected `0` boundary is the standard bottom layer; the corresponding product has no zero or pole; its cusp coefficient varies across exact shifts; and even its logarithmic singularity order changes under an exact dilation all-composite reference.

A surviving Selberg/Ruelle route must therefore come from a genuinely intrinsic full-surface dynamical object, or from a relative construction whose comparison object is itself canonically selected by the prime-flute geometry and survives both the shift and dilation matched-control audits.