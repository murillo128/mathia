---
id: CLUE-analytic-frontier-positive-base-fejer-comparison-uniform-complex-tube
type: research-clue
status: proposed
origin: research-watch
target_line: analytic_frontier
based_on:
  - research/analytic_frontier/findings/ANF-081-two-level-clipping-closes-the-full-real-multiplicity-gate.md
  - research/analytic_frontier/findings/ANF-082-central-notch-real-certificate-opens-a-p-minus-quarter-complex-tube.md
---

# Can positive-base comparison remove the pair-count loss from the complex tube?

## Observation

ANF-081 supplies one fixed spectrum `J=J_s=J_0-s phi_eta`, where `J_0=J_MT`, `0<=phi_eta<=J_0`, and `0<s<=1/8`. Its real-space base kernel `R=widehat J_0` is pointwise nonnegative on the entire real line, with `R(0)=1`, and `J>=(1-s)J_0`. For every finite real multiset `X`, the same fixed `q in (0,1)` satisfies `E_J(X)>=q(2|X|-sigma(X))`, while `C(J)/q<C_MT`.

ANF-082 bounds the change from real-part collapse to a complex multiset by an absolute `O(p h^2)` norm, then compares it with a `sqrt(p)` affine floor. This produces its `p^(-1/4)` height restriction. Those two worst cases need not be simultaneously sharp: coherent clusters also increase the nonnegative base energy. The missing alternative is a bound relative to the actual collapsed norm rather than relative only to the affine floor.

## Research question

Audit the following candidate estimate, for every finite conjugation-invariant multiset `W`, its real-part collapse `X`, and `h=max |Im z|`:

\[
\boxed{\|S_W-S_X\|_{L^2(J)}
\le K\bigl(\cosh(2\pi h)-1\bigr)\|S_X\|_{L^2(J)}.}
\]

Here `K` must depend only on the fixed spectrum and notch parameters, not on the number of nonreal pairs, horizontal separation, local occupancy, real multiplicities, or total cardinality. The construction below proposes an explicit such constant. If correct, it gives a fixed positive complex tube for the ANF-081 affine certificate, removing the shrinking-with-cardinality boundary of ANF-082 without claiming an unrestricted-height certificate.

## Why it may matter

The candidate changes a live quantifier: one height width would cover all finite cardinalities simultaneously. No separation or bounded-density hypothesis would be imposed on a hypothetical zero configuration. The mathematical resource is already present in the construction: pointwise positivity of the Montgomery--Taylor base pays for clustering, and spectral domination transfers that payment to the notched norm even though the notched spatial kernel changes sign.

This is distinct from the already understood common-height/common-fiber collapse and from merely replacing `p` by an assumed local-density bound. Heights may vary independently, horizontal centers may coincide, and the same fixed `J` and objective normalization are retained.

## Decisive test

Reconstruct the following candidate proof and either promote the resulting uniform-tube theorem through the ordinary finding gate or identify its first false implication.

Use Fourier convention `widehat f(t)=integral f(alpha) exp(-2 pi i alpha t) d alpha` and normalized `sinc(u)=sin(pi u)/(pi u)`, with `sinc(0)=1`. Since `J_0>=0`, `supp J_0 subset [-1,1]`, and `integral J_0=1`,

\[
R(t)=\int J_0(\alpha)\cos(2\pi\alpha t)\,d\alpha
\ge1-2\pi^2t^2.
\]

Thus the fixed choices `r=1/(2 pi)` and `c=1/2` ensure `R(t)>=c` on `|t|<=r`. The additional global fact `R(t)>=0` comes from the actual Montgomery--Taylor base, not from this local Taylor bound or from positive definiteness alone.

Set

\[
w_r(\alpha)=\frac{\operatorname{sinc}(r\alpha)^2}{\operatorname{sinc}(r)^2},
\qquad A_r=\frac1{r\operatorname{sinc}(r)^2}.
\]

Then `w_r>=1` on `[-1,1]`, and its exact transform is

\[
\widehat w_r(t)=A_r(1-|t|/r)_+.
\]

For any finite centers `x_i` and **nonnegative real coefficients** `v_i`, put `U_v(alpha)=sum_i v_i exp(-2 pi i alpha x_i)` and `E_R(v)=sum_(i,l) v_i v_l R(x_i-x_l)`. The candidate comparison is

\[
\begin{aligned}
\int_{-1}^1|U_v(\alpha)|^2\,d\alpha
&\le \int_{\mathbb R}w_r(\alpha)|U_v(\alpha)|^2\,d\alpha\\
&=A_r\sum_{i,l}v_iv_l(1-|x_i-x_l|/r)_+\\
&\le \frac{A_r}{c}E_R(v).
\end{aligned}
\tag{1}
\]

The last step uses the pointwise comparison `(1-|t|/r)_+<=R(t)/c` everywhere. This is a comparison on nonnegative coefficient vectors, not a claimed Loewner ordering on arbitrary signed or complex vectors. Finite sums and integrability of `w_r` justify the Fourier interchange.

Write the distinct collapsed centers as `x_i` with total occupancies `k_i`. List nonreal pairs with multiplicity as `x_j +/- i y_j`, `0<y_j<=h`. For each integer `m>=1`, collect the height moments at each center:

\[
v_i^{(m)}=\sum_{j:x_j=x_i}y_j^{2m},
\qquad 0\le v_i^{(m)}\le \tfrac12h^{2m}k_i.
\]

The factor `1/2` is essential: every conjugate pair contributes two entries to `k_i`; any real entries only strengthen the inequality. Pointwise nonnegativity of `R` consequently yields

\[
E_R(v^{(m)})\le\tfrac14h^{4m}E_R(k).
\tag{2}
\]

Let `B=||J||_infinity`. Applying (1)--(2), using `|alpha|<=1` on the spectral support, gives

\[
\|\alpha^{2m}U_{v^{(m)}}\|_{L^2(J)}
\le \tfrac12h^{2m}\sqrt{BA_r/c}\,\sqrt{E_R(k)}.
\tag{3}
\]

Now use the exact pair contribution, not a first-order height truncation:

\[
\begin{aligned}
D(\alpha):=S_W(\alpha)-S_X(\alpha)
&=2\sum_j e^{-2\pi i\alpha x_j}
       [\cosh(2\pi\alpha y_j)-1]\\
&=2\sum_{m\ge1}\frac{(2\pi)^{2m}}{(2m)!}
       \alpha^{2m}U_{v^{(m)}}(\alpha).
\end{aligned}
\]

For finite `W` and finite `h` this series converges uniformly on the compact frequency band. Sum (3) by the Hilbert-space triangle inequality over the moment orders, rather than separately over all pairs:

\[
\|D\|_{L^2(J)}
\le\sqrt{BA_r/c}\,[\cosh(2\pi h)-1]\sqrt{E_R(k)}.
\tag{4}
\]

Finally, `J>=(1-s)J_0` implies `E_R(k)<=E_J(X)/(1-s)`. Therefore (4) supplies the requested relative estimate with

\[
\boxed{K=\sqrt{\frac{BA_r}{c(1-s)}}.}
\tag{5}
\]

To check the complete affine implication, freeze any `q_* in (C(J)/C_MT,q)` and define

\[
\varepsilon_*=1-\sqrt{q_*/q}>0,
\qquad
h_0=\frac1{2\pi}\operatorname{arcosh}
       \left(1+\frac{\varepsilon_*}{K}\right)>0.
\tag{6}
\]

Here `sigma(W)` has the ANF-082 convention of counting simple real sites, and `M=2|W|-sigma(W)`. Real-part collapse cannot create a simple real site from a nonreal pair, so `sigma(X)<=sigma(W)` and ANF-081 gives `E_J(X)>=q M`. If `h<=h_0`, the candidate relative bound and reverse triangle inequality give

\[
\boxed{E_J(W)\ge(1-\varepsilon_*)^2E_J(X)
             \ge q_*[2|W|-\sigma(W)].}
\tag{7}
\]

The fixed normalization still satisfies `C(J)/q_*<C_MT`. Neither (5) nor (6) contains `p`. Check empty/all-real configurations separately by ANF-081; repeated pairs, arbitrarily large real occupancies, widely separated centers, and fully coincident centers are included in (1)--(7), not limiting exceptions.

The cheapest adversarial checks are the Fourier scaling in (1), both uses of **pointwise** `R>=0`, the pair-counting factor in (2), preservation of nonnegative coefficients at every moment order, and the direction of the spectral comparison leading to (5). In particular, do not substitute positive definiteness alone for pointwise positivity or claim (1) for arbitrary signed coefficient vectors.

For the novelty audit, compare the elementary sinc/triangular-majorant mechanism with the classical large-sieve and positive-definite localization literature: H. L. Montgomery and R. C. Vaughan, *The large sieve*, Mathematika 20 (1973), 119--134, DOI `10.1112/S0025579300004708`; D. Gorbachev and S. Tikhonov, *Wiener's problem for positive definite functions*, arXiv:`1604.01302`. These are neighboring classical mechanisms, not citations asserting the proposed affine complex-tube theorem. The displayed finite-sum proof is intended to expose every actual dependency instead of importing a black-box separation theorem.

## Evidence boundary

This is a proposed derivation for independent Research Watch validation, not an accepted finding, a formal proof artifact, or a publication-level novelty claim. The application remains conditional on the correctness and exact hypotheses of ANF-081 and its dependencies; this clue does not replace their audit.

The uniformity gain is only in cardinality and horizontal/multiplicity complexity. The width may be very small because it depends on the fixed strict objective margin. Heights above `h_0` remain uncontrolled, and the argument cannot be iterated from nonreal reference configurations without a new positivity/comparison theorem. It does not establish the unrestricted complex affine certificate, an improved unconditional zeta-zero proportion, or RH. The intended durable delta, if validated, is removal of the `p^(-1/4)` loss from this particular boundary layer.
