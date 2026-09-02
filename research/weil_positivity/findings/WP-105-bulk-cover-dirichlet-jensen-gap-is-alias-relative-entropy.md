# WP-105 — The bulk cover-Dirichlet Jensen gap is alias relative entropy, and exact log degree forces the singular endpoint

**Status:** `EXACT-DERIVED + POSITIVE-SYMBOL + ENTROPY-IDENTITY + DECISIVE-ENDPOINT + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION + NOT-GLOBAL-WEIL`.

`WP-104` leaves open whether a positive **non-trace state** of its cover-Dirichlet logarithmic Jensen defect can do better than the Haar/trace-density scalarization.  On the bulk Bloch symbol this question has an exact answer.

Let

\[
\ell(\theta):=2-2\cos\theta
\]

be the discrete-Laplacian symbol.  For cover degree `n>=2` and coarse Bloch phase `0<phi<2pi`, put

\[
\theta_j=\frac{\phi+2\pi j}{n},
\qquad 0\le j<n.
\]

The normalized constant block vector from `WP-104` decomposes among the `n` fine Bloch aliases with probabilities

\[
\boxed{
w_j^{(n)}(\phi)
=\frac{\ell(\phi)}{n^2\ell(\theta_j)}.
}
\tag{1}
\]

These satisfy

\[
\sum_{j=0}^{n-1}w_j^{(n)}(\phi)=1,
\qquad
\sum_{j=0}^{n-1}w_j^{(n)}(\phi)\ell(\theta_j)
=\frac{\ell(\phi)}n.
\tag{2}
\]

The principal bulk symbol of the positive Jensen defect

\[
J_{n,K}
=\log(nG_K)-W_{n,K}^*(\log G_{nK})W_{n,K}
\succeq0
\]

is therefore

\[
\boxed{
j_n(\phi)
=\log\frac{\ell(\phi)}n
-\sum_{j=0}^{n-1}w_j^{(n)}(\phi)\log\ell(\theta_j).
}
\tag{3}
\]

The special reciprocal relation in (1) makes this Jensen gap much more rigid than a generic positive symbol.  Substituting

\[
\log\ell(\theta_j)
=\log\ell(\phi)-2\log n-\log w_j^{(n)}(\phi)
\]

into (3) gives the exact identity

\[
\boxed{
j_n(\phi)
=\log n-H\!\left(w^{(n)}(\phi)\right)
=D_{\rm KL}\!\left(w^{(n)}(\phi)\middle\|u_n\right),
}
\tag{4}
\]

where

\[
H(w)=-\sum_jw_j\log w_j,
\qquad
u_n=(1/n,\ldots,1/n).
\]

Thus the positive bulk response is exactly the relative entropy of the cover-induced **alias distribution** from the uniform distribution.

This has a decisive consequence for the non-trace-state loophole.  The symbol extends continuously to the singular phase `phi=0 mod 2pi`, because

\[
w^{(n)}(\phi)\longrightarrow(1,0,\ldots,0)
\qquad(\phi\to0).
\]

Hence

\[
\boxed{
0\le j_n(\phi)\le\log n,
\qquad
j_n(0)=\log n,
}
\tag{5}
\]

and, for every regular phase `0<phi<2pi`, all alias weights are strictly positive, so

\[
\boxed{j_n(\phi)<\log n.}
\tag{6}
\]

If a positive state of the commutative bulk-symbol algebra is represented by a probability measure `nu` on the Bloch circle, then

\[
R_n(\nu):=\int j_n(\phi)\,d\nu(\phi)
\le\log n.
\tag{7}
\]

Equality is rigid:

\[
\boxed{
R_n(\nu)=\log n
\iff
\nu=\delta_{\phi=0}.
}
\tag{8}
\]

So a non-trace positive bulk state **can** recover exact logarithmic degree, but only by concentrating completely on the zero-entropy Bloch endpoint.  This is the same boundary character `z=1` whose positive Toeplitz realization was isolated in `WP-094`; there it becomes the endpoint-evaluation form and is nonclosable on `ell^2`.  `WP-095` further shows that adding any member of the full finite-band cover-positive cone does not regularize that endpoint functional.

The ordinary trace density of `WP-104` now has an exact information-theoretic interpretation.  Haar averaging gives

\[
\boxed{
\frac1{2\pi}\int_0^{2\pi}j_n(\phi)\,d\phi
=c_n
=2(H_n-1)-\log n,
}
\tag{9}
\]

so equivalently

\[
\boxed{
\frac1{2\pi}\int_0^{2\pi}
H\!\left(w^{(n)}(\phi)\right)d\phi
=2\log n-2(H_n-1).
}
\tag{10}
\]

The positive harmonic correction in `WP-104` is therefore precisely the average alias-entropy loss from the maximal endpoint response.

This materially narrows the surviving `WP-104` route:

```text
positive cover-Dirichlet log-Jensen defect
    -> bulk Bloch symbol
    -> arbitrary positive state on the symbol algebra
    -> exact log degree
```

forces the singular zero-frequency character.  No Haar-absolutely-continuous, regular Bloch-distributed, or partially delocalized positive state attains the exact `log n` response.

This still does **not** yield global Weil positivity.  The endpoint response exists for every integer cover degree, not just primes; obtaining `Lambda` from `log n` still requires a signed divisor-Mobius primitive or a primitive-generator/Euler-ray decomposition; the endpoint character is the already-known nonclosable boundary anchor rather than a new finite-energy global geometry; and no Gamma/polar/test-function-dependent archimedean term is produced.  Full operator states that see compact or finite-section boundary corrections, singular traces not factoring through the bulk symbol algebra, genuinely nonlinear scalarizations, and nonseparable finite--archimedean couplings remain outside this theorem.

## 1. Exact alias weights in the Bloch fiber

The block symbol used in `WP-104` is the `n x n` Bloch fiber of the discrete circle Laplacian.  Its normalized eigenvectors can be written

\[
v_j(r)=\frac1{\sqrt n}e^{ir\theta_j},
\qquad
0\le r<n,
\]

with eigenvalues

\[
L_n(\phi)v_j=\ell(\theta_j)v_j.
\tag{11}
\]

Let

\[
u_n=\frac1{\sqrt n}(1,\ldots,1)^T
\]

be the block-averaging vector.  Then

\[
\begin{aligned}
w_j^{(n)}(\phi)
&:=|\langle u_n,v_j\rangle|^2\\
&=\frac1{n^2}
\left|\sum_{r=0}^{n-1}e^{ir\theta_j}\right|^2\\
&=\frac{|1-e^{i\phi}|^2}
{n^2|1-e^{i\theta_j}|^2}\\
&=\frac{\ell(\phi)}{n^2\ell(\theta_j)},
\end{aligned}
\tag{12}
\]

which is (1).  Orthonormality of the `v_j` gives `sum_j w_j=1`.

There is also a useful equal-contribution identity:

\[
w_j^{(n)}(\phi)\ell(\theta_j)
=\frac{\ell(\phi)}{n^2}
\qquad\text{for every }j.
\tag{13}
\]

Summing (13) gives the second identity in (2).  Geometrically, the coarse constant block vector distributes its Laplacian expectation equally among the `n` fine alias channels even though the spectral probabilities themselves are highly nonuniform.

Nothing here uses primality or number theory.  It is exact finite-dimensional cover/Laplacian geometry.

## 2. The positive Jensen symbol is exactly an alias KL divergence

In the frozen-position bulk calculation behind `WP-104`, the fine operator has local scale `(nK)^2x^2 L_n(phi)`, whereas the coarse term `nG_K` has local scale `nK^2x^2 ell(phi)`.  The common position and cutoff factors cancel in the logarithmic difference.  Compressing the fine logarithm against `u_n` therefore gives exactly (3):

\[
j_n(\phi)
=-\log n+\log\ell(\phi)
-\sum_jw_j\log\ell(\theta_j).
\tag{14}
\]

Equation (2) already identifies (14) as the scalar logarithmic Jensen gap

\[
\log\left(\sum_jw_j\ell(\theta_j)\right)
-\sum_jw_j\log\ell(\theta_j),
\]

so `j_n(phi)>=0` follows independently from concavity of `log`, matching the operator positivity of `J_{n,K}`.

The stronger identity follows from (1).  Since

\[
\ell(\theta_j)
=\frac{\ell(\phi)}{n^2w_j},
\]

substitution into (14) yields

\[
\begin{aligned}
j_n(\phi)
&=-\log n+\log\ell(\phi)\\
&\quad-\sum_jw_j
\bigl(\log\ell(\phi)-2\log n-\log w_j\bigr)\\
&=\log n+\sum_jw_j\log w_j\\
&=\sum_jw_j\log(nw_j).
\end{aligned}
\tag{15}
\]

The last expression is exactly `D_KL(w || u_n)`.  Positivity is therefore visible both as logarithmic Jensen concavity and as nonnegativity of relative entropy.

The identity is special to the cover alias relation (13).  A generic Jensen gap is not automatically `log n-H(w)`; here the fine eigenvalues are reciprocally locked to the spectral weights.

## 3. Exact logarithmic degree is maximal entropy-defect saturation

For any probability vector on `n` points,

\[
0\le H(w)\le\log n.
\]

Equation (4) therefore gives (5).  More importantly, `j_n=log n` is not a typical positive value: it is the **maximum possible** value of this Jensen gap and requires

\[
H(w)=0.
\tag{16}
\]

For `0<phi<2pi`, equation (1) has strictly positive numerator and denominator for every alias, hence every `w_j(phi)>0`.  At least two weights are therefore nonzero and

\[
H(w^{(n)}(\phi))>0.
\tag{17}
\]

This proves the strict inequality (6).

At the endpoint,

\[
\frac{\ell(\phi)}{n^2\ell(\phi/n)}\longrightarrow1,
\]

whereas for `j>=1`,

\[
\frac{\ell(\phi)}{n^2\ell((\phi+2\pi j)/n)}\longrightarrow0.
\]

Thus

\[
w^{(n)}(\phi)\to\delta_0,
\qquad
H(w^{(n)}(\phi))\to0,
\tag{18}
\]

and (4) extends continuously with `j_n(0)=log n`.

The logarithmic cover response is therefore produced by **complete alias-channel collapse**, not by a regular average over the positive bulk geometry.

## 4. Positive-state classification on the bulk symbol algebra

The continuous extension `j_n in C(T)` can be scalarized by any positive normalized state on the commutative Bloch-symbol algebra.  By the Riesz representation theorem such a state is integration against a probability measure `nu`.

Equation (4) gives

\[
\log n-R_n(\nu)
=\int H(w^{(n)}(\phi))\,d\nu(\phi).
\tag{19}
\]

The integrand is nonnegative everywhere and strictly positive away from the single circle point `phi=0 mod 2pi`.  Therefore (8) follows immediately.

In particular, if `nu` is absolutely continuous with respect to Haar measure, then

\[
R_n(\nu)<\log n.
\tag{20}
\]

The same is true for every positive state placing any nonzero mass away from the endpoint.  Measures concentrating increasingly near `phi=0` can approximate `log n`, but exact equality is rigidly singular.

This is the precise answer to the bulk non-trace-state loophole in `WP-104`: changing the state can remove the harmonic trace-density defect only by collapsing the state to the endpoint character.

## 5. Haar trace density is average alias relative entropy

`WP-104` already computes the normalized bulk trace as Haar integration of the symbol and proves

\[
\frac1{2\pi}\int j_n(\phi)d\phi
=2(H_n-1)-\log n.
\tag{21}
\]

Combining (21) with (4) gives (9)--(10).  Thus

\[
c_n
=\frac1{2\pi}\int
D_{\rm KL}(w^{(n)}(\phi)\|u_n)d\phi.
\tag{22}
\]

The quantity that looked in `WP-104` like an unavoidable harmonic/UV correction is exactly the average Shannon entropy of alias splitting:

\[
\log n-c_n
=\frac1{2\pi}\int H(w^{(n)}(\phi))d\phi.
\tag{23}
\]

As `n->infinity`, `c_n=log n+2gamma-2+o(1)`, so the average alias entropy tends to the finite constant

\[
2-2\gamma.
\tag{24}
\]

This asymptotic is only a diagnostic; the exact identities (4), (10), and (22) are the durable content.

## 6. The exact-log state lands on the already-known singular boundary character

Under `z=e^{i phi}`, the unique state in (8) is evaluation at

\[
z=1.
\]

This is the same character selected independently by `WP-094`.  There, positivity plus exact cover covariance for an arbitrary finite-dimensional block-Toeplitz form forces its Herglotz measure to

\[
R\delta_1,
\]

and the resulting quadratic form is

\[
q_\partial(x)
=\left\langle R\sum_jx_j,\sum_jx_j\right\rangle.
\]

Every nonzero such form is nonclosable on the ambient `ell^2` space.  `WP-095` then proves that adding the entire fixed-finite-band cover-positive cone of `WP-093` cannot make this endpoint functional bounded in the corresponding energy norm or restore closability.

The present result does not assert that `J_{n,K}` itself is the Toeplitz form of `WP-094`.  The exact identification is at the **state/character** level: the only bulk symbol state that attains `log n` is precisely the boundary character that produces the previously classified singular endpoint geometry when realized as a positive Toeplitz quadratic form.

So the non-trace-state escape does not uncover a new regular carrier.  It redirects back to a known singular boundary object.

## 7. Arithmetic and global falsification controls

The endpoint survivor fails the research mandate in several independent ways.

### 7.1 All-integer matched control

Equations (1)--(24) hold for every integer `n>=2`.  Primes, Euler products, zero data, and the zeta functional equation never enter.  Therefore the exact endpoint response

\[
R_n(\delta_0)=\log n
\]

survives unchanged in the all-integer cover control.

### 7.2 Prime-power support still requires a signed/external selector

The divisor-Mobius primitive of `log n` is indeed `Lambda(n)`, but the Mobius signs are not consequences of the positive state in (8).  Equivalently, one can retain primitive prime generators as in `WP-074`/`WP-083`, but then prime-power support is supplied by the Euler-ray decomposition rather than by the Jensen sign theorem.

Thus

\[
\text{positive endpoint state}
\Longrightarrow \log n
\]

is exact, while

\[
\log n\Longrightarrow\Lambda(n)
\]

still uses a separate signed/arithmetic operation.

### 7.3 No archimedean/global completion is generated

The rich continuous-dual-Hahn spectral measure of the critical `WP-093` Jacobi operator contains Gamma functions and the threshold `1/4+t^2`.  The state `delta_0` does not turn that spectral family into the Riemann Gamma term.  It collapses the Bloch alias variable to one boundary character and returns only `log n`.

There is no test-function-dependent digamma functional, `-1/2 log pi` normalization, polar term, or local-to-global Weil quadratic form in (1)--(24).  None can be inserted without an additional construction whose sign must be proved independently.

### 7.4 Singularity is structural, not evidence for RH

The fact that exact log degree sits at a singular endpoint is mathematically sharp but arithmetically universal.  The same entropy saturation occurs for every integer refinement system with this discrete-Laplacian block geometry.  It cannot by itself distinguish the rational primes from matched generalized or all-degree controls.

## 8. Scope boundary

The theorem closes only positive scalarizations that factor through the **principal bulk Bloch symbol** of the `WP-104` Jensen defect.  It does not classify:

- states of a larger Toeplitz/operator algebra that retain compact or finite-section boundary information beyond the principal symbol;
- singular traces or finite-part functionals that do not factor through a probability measure on `C(T)`;
- subleading cutoff anomalies after removal of the extensive bulk term;
- nonlinear scalarizations not given by a positive state;
- arbitrary position-dependent infinite-range cover forms outside `WP-093`--`WP-095`;
- a genuinely nonseparable finite--archimedean object formed before scalarization.

Those routes remain open, but they cannot cite a regular bulk state of the cover-Dirichlet logarithmic Jensen defect as a source of exact `log degree`: the exact bulk state is uniquely the singular endpoint character.

## 9. Prior art and novelty audit

The ingredients surrounding the identity are classical.  `WP-104` already anchors the Davis/Hansen--Pedersen operator-Jensen inequality, GLT/local-Toeplitz bulk calculus, Fejer weights, and the Fourier analysis of the discrete Laplacian.  Shannon entropy and Kullback--Leibler divergence are standard information-theoretic quantities; `research/weil_positivity/SOURCES.md` already contains information-geometry anchors used elsewhere in this line.  `WP-094` supplies the classical Herglotz/Riesz boundary interpretation of the endpoint character, and `WP-095` supplies the Mathia-specific nonclosability obstruction for its natural hybrid with the finite-band positive cone.

No novelty is claimed for Jensen's inequality, Fejer/polyphase aliasing, entropy bounds, relative entropy, the Riesz representation theorem, Herglotz theory, or endpoint evaluation itself.  A targeted literature audit did not identify a reason to promote the elementary entropy algebra to a standalone general theorem.

The durable Mathia-specific result is the exact specialization

\[
\boxed{
\text{WP-093 cover Laplacian alias weights}
\Longrightarrow
j_n(\phi)=D_{\rm KL}(w^{(n)}(\phi)\|u_n)
\Longrightarrow
\text{exact }\log n\text{ only at }z=1,
}
\]

which closes an explicit `WP-104` positive-state escape and connects it rigorously to the previously isolated singular endpoint obstruction.

## Consequence for the Weil-positivity search

The non-diagonal positive survivor of `WP-093` now exhibits the same boundary pattern as several earlier routes, but for a stronger reason than mere divergence: its canonical logarithmic Jensen response has an **exact information budget**.  Regular Bloch aliasing spends part of the maximal `log n` response as Shannon entropy.  Recovering the exact arithmetic primitive forces zero alias entropy, which means collapse to the singular `z=1` character.

A genuinely new positive Weil mechanism therefore cannot obtain exact finite arithmetic merely by choosing a better positive bulk state of this cover-Dirichlet Jensen geometry.  It must retain additional non-bulk information or introduce a new coupled object before positivity/scalarization, and that object must still generate the archimedean and polar sectors with an independent sign theorem.