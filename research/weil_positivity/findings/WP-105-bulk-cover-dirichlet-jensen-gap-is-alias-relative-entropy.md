# WP-105 — The bulk cover-Dirichlet Jensen gap is alias relative entropy, and exact log degree forces the singular endpoint

**Status:** `EXACT-DERIVED + POSITIVE-SYMBOL + ENTROPY-IDENTITY + DECISIVE-ENDPOINT + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION + NOT-GLOBAL-WEIL`.

`WP-104` leaves open whether a positive **non-trace state** of its cover-Dirichlet logarithmic Jensen defect can do better than the Haar/trace-density scalarization. On the principal bulk Bloch symbol this question has an exact answer.

For cover degree `n>=2`, let

\[
\ell(\theta)=2-2\cos\theta,
\qquad
\theta_j=\frac{\phi+2\pi j}{n},
\quad 0\le j<n,
\]

with `0<phi<2pi`. The normalized constant block vector decomposes among the `n` fine Bloch aliases with probabilities

\[
\boxed{
w_j^{(n)}(\phi)
=\frac{\ell(\phi)}{n^2\ell(\theta_j)}.
}
\tag{1}
\]

They satisfy

\[
\sum_jw_j^{(n)}(\phi)=1,
\qquad
\sum_jw_j^{(n)}(\phi)\ell(\theta_j)
=\frac{\ell(\phi)}n.
\tag{2}
\]

The principal bulk symbol of the positive Jensen defect from `WP-104`,

\[
J_{n,K}
=\log(nG_K)-W_{n,K}^*(\log G_{nK})W_{n,K}
\succeq0,
\]

is

\[
\boxed{
j_n(\phi)
=\log\frac{\ell(\phi)}n
-\sum_jw_j^{(n)}(\phi)\log\ell(\theta_j).
}
\tag{3}
\]

The reciprocal relation in (1) makes this Jensen gap rigid. If

\[
H(w)=-\sum_jw_j\log w_j
\]

and

\[
\upsilon_n=(1/n,\ldots,1/n)
\]

is the uniform probability vector, then exactly

\[
\boxed{
j_n(\phi)
=\log n-H\!\left(w^{(n)}(\phi)\right)
=D_{\rm KL}\!\left(w^{(n)}(\phi)\middle\|\upsilon_n\right).
}
\tag{4}
\]

Thus the positive bulk response is the relative entropy of the cover-induced **alias distribution** from uniformity.

The symbol extends continuously to the singular phase `phi=0 mod 2pi`. There

\[
w^{(n)}(\phi)\longrightarrow(1,0,\ldots,0),
\]

so

\[
\boxed{
0\le j_n(\phi)\le\log n,
\qquad
j_n(0)=\log n.
}
\tag{5}
\]

For every regular phase `0<phi<2pi`, all alias weights are strictly positive, hence

\[
\boxed{j_n(\phi)<\log n.}
\tag{6}
\]

Consequently, if a positive normalized state of the commutative bulk-symbol algebra is represented by a probability measure `nu` on the Bloch circle,

\[
R_n(\nu):=\int j_n(\phi)\,d\nu(\phi),
\]

then

\[
\boxed{
R_n(\nu)=\log n
\iff
\nu=\delta_{\phi=0}.
}
\tag{7}
\]

A non-trace positive bulk state therefore **can** recover exact logarithmic degree, but only by concentrating completely on the zero-entropy Bloch endpoint. Under `z=e^{i\phi}`, this is the boundary character `z=1` already isolated independently in `WP-094`; its natural positive Toeplitz realization is nonclosable on `ell^2`, and `WP-095` proves that adding the entire finite-band cover-positive cone does not regularize that endpoint functional.

The Haar trace density of `WP-104` now has an exact information-theoretic interpretation:

\[
\boxed{
\frac1{2\pi}\int_0^{2\pi}j_n(\phi)\,d\phi
=c_n
=2(H_n-1)-\log n,
}
\tag{8}
\]

hence

\[
\boxed{
\frac1{2\pi}\int_0^{2\pi}
H\!\left(w^{(n)}(\phi)\right)d\phi
=2\log n-2(H_n-1).
}
\tag{9}
\]

So the deficit of the regular Haar response from the maximal `log n` endpoint response is exactly the mean alias entropy.

This materially narrows the explicit `WP-104` escape

```text
positive cover-Dirichlet log-Jensen defect
    -> principal bulk Bloch symbol
    -> arbitrary positive state on the symbol algebra
    -> exact log degree
```

because exact `log degree` forces the already-known singular zero-frequency character. No Haar-absolutely-continuous, regular Bloch-distributed, or partially delocalized positive state attains it.

This still does **not** yield global Weil positivity. The endpoint response exists for every integer cover degree; obtaining `Lambda` from `log n` still requires a signed divisor-Mobius primitive or a primitive-generator/Euler-ray decomposition; and the endpoint state supplies neither the Riemann Gamma term nor the polar/global terms of the Weil explicit formula. Full operator states retaining compact or finite-section boundary information, singular traces not factoring through the principal symbol, nonlinear scalarizations, and genuinely nonseparable finite--archimedean constructions remain outside the theorem.

## 1. Exact Bloch alias probabilities

Let `L_n(phi)` be the `n x n` Bloch fiber of the discrete circle Laplacian used in `WP-104`. Its normalized eigenvectors are

\[
v_j(r)=\frac1{\sqrt n}e^{ir\theta_j},
\qquad 0\le r<n,
\]

with

\[
L_n(\phi)v_j=\ell(\theta_j)v_j.
\tag{10}
\]

Let

\[
a_n=\frac1{\sqrt n}(1,\ldots,1)^T
\]

be the block-averaging vector. Then

\[
\begin{aligned}
w_j^{(n)}(\phi)
&:=|\langle a_n,v_j\rangle|^2\\
&=\frac1{n^2}
\left|\sum_{r=0}^{n-1}e^{ir\theta_j}\right|^2\\
&=\frac{|1-e^{i\phi}|^2}
{n^2|1-e^{i\theta_j}|^2}\\
&=\frac{\ell(\phi)}{n^2\ell(\theta_j)}.
\end{aligned}
\tag{11}
\]

Orthonormality gives `sum_j w_j=1`. Moreover

\[
\boxed{
w_j^{(n)}(\phi)\ell(\theta_j)
=\frac{\ell(\phi)}{n^2}
}
\tag{12}
\]

for every `j`, so summing yields the second identity in (2). The coarse constant block vector distributes its Laplacian expectation equally among the fine alias channels even though the spectral probabilities are nonuniform.

Nothing in (10)--(12) uses primality or number theory.

## 2. The Jensen symbol is exactly KL divergence

In the frozen-position bulk calculation behind `WP-104`, the fine operator has local scale `(nK)^2x^2L_n(phi)`, while the coarse term `nG_K` has local scale `nK^2x^2ell(phi)`. The common position and cutoff factors cancel in the logarithmic difference, giving (3), equivalently

\[
j_n(\phi)
=-\log n+\log\ell(\phi)
-\sum_jw_j\log\ell(\theta_j).
\tag{13}
\]

By (2), this is the scalar concave-log Jensen gap

\[
\log\left(\sum_jw_j\ell(\theta_j)\right)
-\sum_jw_j\log\ell(\theta_j),
\]

so its positivity is independently forced by Jensen concavity, in agreement with `J_{n,K}>=0`.

The stronger identity follows from (1):

\[
\ell(\theta_j)
=\frac{\ell(\phi)}{n^2w_j}.
\]

Therefore

\[
\begin{aligned}
j_n(\phi)
&=-\log n+\log\ell(\phi)\\
&\quad-\sum_jw_j
\bigl(\log\ell(\phi)-2\log n-\log w_j\bigr)\\
&=\log n+\sum_jw_j\log w_j\\
&=\sum_jw_j\log(nw_j)\\
&=D_{\rm KL}(w\|\upsilon_n),
\end{aligned}
\tag{14}
\]

which proves (4). A generic Jensen gap need not have this form; here it is forced by the reciprocal alias relation (12).

## 3. Exact log degree is maximal entropy-defect saturation

For any probability vector on `n` points,

\[
0\le H(w)\le\log n.
\]

Thus `j_n=log n` is the **maximum possible** value of the bulk Jensen gap and requires `H(w)=0`.

For `0<phi<2pi`, every numerator and denominator in (1) is strictly positive, hence all `n` weights are nonzero and `H(w)>0`. At the endpoint,

\[
\frac{\ell(\phi)}{n^2\ell(\phi/n)}\to1,
\]

while, for `j>=1`,

\[
\frac{\ell(\phi)}{n^2\ell((\phi+2\pi j)/n)}\to0.
\]

Therefore

\[
w^{(n)}(\phi)\to(1,0,\ldots,0),
\qquad
H(w^{(n)}(\phi))\to0,
\tag{15}
\]

and `j_n` extends continuously with value `log n` there.

For a state `nu`, equation (4) gives

\[
\log n-R_n(\nu)
=\int H(w^{(n)}(\phi))\,d\nu(\phi).
\tag{16}
\]

The integrand is nonnegative and is zero only at the circle point `phi=0 mod 2pi`, proving the rigidity statement (7). Measures concentrated increasingly near the endpoint can approximate `log n`, but exact equality is singular.

## 4. The WP-104 harmonic density is mean alias entropy

`WP-104` proves that Haar averaging of the principal bulk symbol gives

\[
\frac1{2\pi}\int j_n(\phi)d\phi
=2(H_n-1)-\log n.
\tag{17}
\]

Combining (17) with (4) yields

\[
\boxed{
c_n
=\frac1{2\pi}\int
D_{\rm KL}(w^{(n)}(\phi)\|\upsilon_n)d\phi.
}
\tag{18}
\]

Equivalently, the loss from the maximal endpoint response is

\[
\log n-c_n
=\frac1{2\pi}\int H(w^{(n)}(\phi))d\phi
=2\log n-2(H_n-1).
\tag{19}
\]

Since `c_n=log n+2gamma-2+o(1)`, the mean alias entropy tends to `2-2gamma`. The asymptotic is only diagnostic; (4), (18), and (19) are exact.

## 5. Exact log degree redirects to the WP-094 endpoint anchor

Under `z=e^{i phi}`, the unique state in (7) is evaluation at `z=1`. `WP-094` independently proves that positivity plus exact cover covariance for any finite-dimensional block-Toeplitz quadratic form forces its Herglotz measure to `R delta_1`; the resulting endpoint-evaluation quadratic form is nonclosable on the ambient `ell^2` space. `WP-095` then proves that adding any member of the complete fixed-finite-band cover-positive cone from `WP-093` cannot regularize that endpoint functional.

The present result does **not** identify `J_{n,K}` itself with the Toeplitz form of `WP-094`. The exact connection is at the state/character level: the only bulk symbol state attaining `log n` is precisely the boundary character whose natural Toeplitz positive realization is the previously classified singular endpoint geometry.

So choosing a better positive state does not uncover a new regular bulk carrier; it redirects to a known singular boundary object.

## 6. Arithmetic and global falsification controls

### 6.1 All-integer control

Equations (1)--(19) hold for every integer `n>=2`. Replacing prime-labelled covers by arbitrary integer-degree covers leaves the positivity, entropy identity, and endpoint response unchanged.

### 6.2 Prime-power support remains external to the sign theorem

The divisor-Mobius primitive of `log n` is `Lambda(n)`, but the Mobius signs are not consequences of the positive state. Equivalently, retaining primitive prime generators as in `WP-074`/`WP-083` supplies prime-power support through an Euler-ray decomposition rather than through the Jensen positivity theorem.

Thus the exact implication here is

\[
\text{positive singular endpoint state}
\Longrightarrow\log n,
\]

not

\[
\text{positive geometry}
\Longrightarrow\Lambda(n)
\]

without an additional signed/arithmetic selector.

### 6.3 No archimedean completion

The continuous-dual-Hahn spectral measure of `WP-093` contains Gamma functions and the threshold `1/4+t^2`, but the endpoint Bloch state does not turn that spectral family into the Riemann Gamma term. It collapses the alias variable to one boundary character and returns only `log n`. No test-function-dependent digamma functional, `-1/2 log pi` normalization, polar term, or assembled Weil quadratic form follows from the entropy identity.

### 6.4 Singularity is universal, not RH evidence

The zero-entropy saturation at `z=1` is structural for this cover/Laplacian refinement geometry. It persists under all-integer matched controls and therefore cannot by itself distinguish Riemann arithmetic or imply RH.

## 7. Scope boundary

This finding closes only positive scalarizations that factor through the **principal bulk Bloch symbol** of the `WP-104` Jensen defect. It does not classify:

- states of a larger operator algebra retaining compact or finite-section boundary information beyond the principal symbol;
- singular traces or finite-part functionals not represented by probability measures on `C(T)`;
- subleading cutoff anomalies after removal of the extensive bulk term;
- nonlinear scalarizations not given by a positive state;
- arbitrary position-dependent infinite-range cover forms outside `WP-093`--`WP-095`;
- genuinely nonseparable finite--archimedean objects formed before scalarization.

Those routes remain open, but they cannot cite a regular positive bulk state of the cover-Dirichlet logarithmic Jensen geometry as a source of exact `log degree`.

## 8. Prior art and novelty audit

The surrounding ingredients are classical. `WP-104` already anchors the Davis/Hansen--Pedersen operator-Jensen inequality, GLT/local-Toeplitz bulk calculus, Fejer weights, and Fourier analysis of the discrete Laplacian. Shannon entropy and Kullback--Leibler divergence are standard information-theoretic quantities; the line's `SOURCES.md` already contains information-geometry anchors. `WP-094` supplies the classical Herglotz/Riesz boundary interpretation, while `WP-095` supplies the Mathia-specific nonclosability obstruction for the natural hybrid with the finite-band positive cone.

No novelty is claimed for Jensen's inequality, aliasing/Fejer weights, entropy bounds, relative entropy, Riesz representation, Herglotz theory, or endpoint evaluation. A targeted literature audit found only standard Jensen-gap/information-theory and filter-bank/aliasing contexts, not a reason to promote the elementary identity (14) as a new general theorem.

The durable Mathia-specific result is the exact specialization

\[
\boxed{
\text{WP-093 cover-Laplacian aliases}
\Longrightarrow
j_n(\phi)=D_{\rm KL}(w^{(n)}(\phi)\|\upsilon_n)
\Longrightarrow
\text{exact }\log n\text{ only at }z=1.
}
\]

It closes an explicit `WP-104` positive-state escape and connects it rigorously to the singular endpoint obstruction already isolated by `WP-094`--`WP-095`.

## Consequence for the Weil-positivity search

The critical non-diagonal positive geometry of `WP-093` has an exact information budget: regular Bloch aliasing spends part of the maximal `log n` response as Shannon entropy. Recovering the exact arithmetic primitive forces zero alias entropy, hence collapse to the singular `z=1` character.

A genuinely new positive Weil mechanism therefore cannot obtain exact finite arithmetic merely by choosing a better positive bulk state of this cover-Dirichlet Jensen geometry. It must retain additional non-bulk information or introduce a new coupled object before positivity/scalarization, and that object must still generate the archimedean and polar sectors with an independent sign theorem.