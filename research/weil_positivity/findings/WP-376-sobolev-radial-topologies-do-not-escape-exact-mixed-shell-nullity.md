---
id: WP-376
title: Sobolev radial topologies do not escape exact mixed-shell nullity
branch: weil_positivity
status: supported
kind: cyclotomic-log-radial-sobolev-positive-form-obstruction
claim_strength: exact RH-independent strengthening of WP-375 showing that every finite-order Sobolev, and more generally every absolutely-continuous Fourier-weight Hilbert topology containing the cyclotomic shell profiles, has the same mixed-shell closure obstruction; the simplest trace-topology escape is sharp but reduces exactly to the zero-Mellin Lambda-squared route
created: 2026-09-19
related: [WP-162, WP-374, WP-375]
clues: [CLUE-weil-positivity-noncharacter-finite-archimedean-incidence]
prior_art:
  - classical cyclotomic identity Phi_nq(x)=Phi_n(x^q)/Phi_n(x) for q prime and q not dividing n
  - classical Fourier characterization of Sobolev spaces and unitary translation action
  - classical Riemann-Lebesgue weak escape of far translations
  - classical Mazur lemma and closability criterion for nonnegative quadratic forms
  - classical concentration-compactness/cocompactness viewpoint on translation escape in Sobolev spaces
---

# WP-376 — Sobolev radial topologies do not escape exact mixed-shell nullity

## Claim

`WP-375` shows that exact mixed-shell zero energy is incompatible with retaining any prime-power shell in a closable positive form on the canonical ambient space `L^2(R,du)`. It leaves a precise apparent escape: perhaps the cyclotomic radial geometry carries a different source-native topology in which the far spectator-prime translates no longer disappear weakly.

Changing from `L^2` to any ordinary finite-order Sobolev topology does **not** provide that escape.

For every real `r`, the canonical log-radial shell profile

\[
h_n(u)=e^u\rho_n(e^u),
\qquad
\rho_n(s)=-\frac{d}{ds}\log\Phi_n(e^{-s}),
\tag{1}
\]

belongs to `H^r(R)` for every `n>1`. Let `D subset H^r(R)` be a linear subspace containing all shell profiles, and let `Q` be a nonnegative Hermitian form on `D` that is closable in `H^r`. If

\[
Q(h_m)=0
\qquad
\text{whenever }m\text{ has at least two distinct prime factors},
\tag{2}
\]

then

\[
\boxed{Q(h_{p^a})=0\quad\text{for every prime power }p^a.}
\tag{3}
\]

The same proof works in every translation-invariant Fourier-weight Hilbert space

\[
\|f\|_{H_w}^2
=\int_{\mathbb R}w(\xi)|\widehat f(\xi)|^2\,d\xi,
\tag{4}
\]

with `w>0` measurable, whenever the relevant `h_n` belong to that space. Thus changing derivative order, using a Bessel-potential norm, or inserting any absolutely-continuous Fourier weight does not evade `WP-375`: the spectator-prime translations still escape weakly, Mazur convexification still puts each prime-power profile in the strong closure of the mixed-shell span, and closability still propagates the positive-form radical.

There is a sharp topological control. If one strengthens the topology by adjoining the zero-frequency trace,

\[
\|f\|_*^2=\|f\|_{H^r}^2+c\left|\widehat f(0)\right|^2,
\qquad c>0,
\tag{5}
\]

then the closure argument really does fail: the trace is translation invariant and

\[
\widehat h_n(0)=\int_{\mathbb R}h_n(u)\,du=\Lambda(n).
\tag{6}
\]

The bounded positive form `Q_*(f)=c|\widehat f(0)|^2` annihilates every mixed shell and retains every prime power. But it gives exactly

\[
Q_*(h_n)=c\Lambda(n)^2,
\tag{7}
\]

which is the zero-Mellin survivor already isolated by `WP-374`, not the linear Weil coefficient. Moreover, among single Fourier-trace atoms, zero frequency is forced: a nonzero atom cannot retain a prime-power profile while annihilating all of its spectator-prime mixed shells.

So the `different topology` escape left by `WP-375` is materially narrower. Ordinary Sobolev/Fourier-multiplier Hilbert geometries are closed. The simplest singular trace extension is genuine but classicalizes exactly to the already-known `Lambda^2` zero mode.

**Classification:** `EXACT-DERIVED + RH-INDEPENDENT + CYCLOTOMIC-TRANSLATION-COBOUNDARY + ALL-SOBOLEV-ORDERS + ABSOLUTELY-CONTINUOUS-FOURIER-WEIGHT-NO-GO + MAZUR-CLOSABILITY + SHARP-ZERO-MELLIN-TRACE-CONTROL + SINGLE-ATOM-RIGIDITY + LAMBDA-SQUARED + NO-ZERO-DATA + CLASSICAL-INGREDIENTS + NOT-A-GLOBAL-WEIL-POSITIVITY-PROOF`.

## 1. The canonical shell profiles are Schwartz functions

The cyclotomic product formula gives, for `n>1`,

\[
\log\Phi_n(e^{-s})
=\sum_{d\mid n}\mu(n/d)\log(1-e^{-ds}).
\tag{8}
\]

Hence

\[
\rho_n(s)
=-\sum_{d\mid n}\mu(n/d)\frac{d}{e^{ds}-1},
\tag{9}
\]

and `h_n(u)=s\rho_n(s)` with `s=e^u`.

As `s->0+`,

\[
\frac{d}{e^{ds}-1}
=\frac1s-\frac d2+O(s).
\tag{10}
\]

Because `sum_{d|n} mu(n/d)=0` for `n>1` and

\[
\sum_{d\mid n}\mu(n/d)d=\varphi(n),
\tag{11}
\]

we obtain

\[
\rho_n(s)=\frac{\varphi(n)}2+O(s),
\qquad
h_n(u)=\frac{\varphi(n)}2e^u+O(e^{2u})
\quad(u\to-\infty).
\tag{12}
\]

At the other end, every summand in (9) is exponentially small in `s`; after multiplication by `s=e^u` it is super-exponentially small as `u->+infinity`. Repeated `u`-derivatives are powers of `s d/ds` applied to the same finite sum, so they have the same exponential/super-exponential tail behavior.

Therefore

\[
\boxed{h_n\in\mathcal S(\mathbb R)\quad(n>1).}
\tag{13}
\]

In particular every shell profile lies in `H^r(R)` for every real Sobolev order `r`. Moving to higher or lower finite-order Sobolev regularity is therefore a genuine change of ambient norm, not a domain obstruction that ejects the source profiles.

## 2. Far spectator-prime translations vanish weakly in every Sobolev order

Fix `r in R`. With the standard Fourier realization,

\[
\langle f,g\rangle_{H^r}
=\int_{\mathbb R}(1+\xi^2)^r
\widehat f(\xi)\overline{\widehat g(\xi)}\,d\xi.
\tag{14}
\]

Translations are unitary and satisfy

\[
\widehat{\tau_t f}(\xi)=e^{it\xi}\widehat f(\xi).
\tag{15}
\]

For arbitrary `f,g in H^r`, put

\[
A(\xi)=(1+\xi^2)^{r/2}\widehat f(\xi),
\qquad
B(\xi)=(1+\xi^2)^{r/2}\widehat g(\xi).
\tag{16}
\]

Then `A,B in L^2`, so `A overline B in L^1` by Cauchy--Schwarz. Consequently

\[
\langle\tau_t f,g\rangle_{H^r}
=\int e^{it\xi}A(\xi)\overline{B(\xi)}\,d\xi
\longrightarrow0
\qquad(|t|\to\infty)
\tag{17}
\]

by the Riemann--Lebesgue lemma. Thus

\[
\boxed{\tau_t f\rightharpoonup0\text{ in }H^r
\quad\text{as }|t|\to\infty.}
\tag{18}
\]

Nothing in this argument is specific to `r=0`.

## 3. The WP-375 closure argument therefore survives unchanged

For prime `q` not dividing `n`, the exact cyclotomic identity

\[
\Phi_{nq}(x)=\frac{\Phi_n(x^q)}{\Phi_n(x)}
\tag{19}
\]

implies the source-forced log-radial coboundary relation

\[
h_{nq}=\tau_{\log q}h_n-h_n.
\tag{20}
\]

Fix a prime power `n=p^a` and choose spectator primes `q_j ne p` with `q_j->infinity`. Equation (18) gives

\[
\tau_{\log q_j}h_n\rightharpoonup0
\qquad\text{in }H^r.
\tag{21}
\]

Mazur's lemma supplies finite convex combinations of tails

\[
v_k=\sum_j\alpha_{k,j}\tau_{\log q_j}h_n
\longrightarrow0
\qquad\text{strongly in }H^r.
\tag{22}
\]

Set

\[
y_k=\sum_j\alpha_{k,j}h_{nq_j}=v_k-h_n.
\tag{23}
\]

Every `nq_j` has at least two distinct prime factors, so assumption (2) and positivity make every `h_{nq_j}`, hence every `y_k`, radical for `Q`. Therefore

\[
Q(y_k-y_l)=0,
\qquad
Q(h_n+y_k)=Q(h_n).
\tag{24}
\]

But `z_k=h_n+y_k=v_k->0` strongly in `H^r`. Closability of `Q` gives

\[
Q(z_k)\to0,
\tag{25}
\]

and (24) forces `Q(h_n)=0`. Since `p^a` was arbitrary, (3) follows.

The mechanism is therefore topological but not specifically `L^2`: it uses only weak escape of the source-forced spectator translations plus closability of the positive form in the chosen ambient norm.

## 4. Every absolutely-continuous Fourier-weight Hilbert topology has the same obstruction

The previous calculation does not need the polynomial Sobolev weight. Let `w:R->[0,infinity)` be measurable and positive almost everywhere, and realize a translation-invariant Hilbert space by

\[
\|f\|_{H_w}^2
=\int w(\xi)|\widehat f(\xi)|^2\,d\xi.
\tag{26}
\]

Whenever `f,g in H_w`, Cauchy--Schwarz gives

\[
w(\xi)\widehat f(\xi)\overline{\widehat g(\xi)}\in L^1(d\xi).
\tag{27}
\]

Hence

\[
\langle\tau_t f,g\rangle_{H_w}
=\int e^{it\xi}w(\xi)
\widehat f(\xi)\overline{\widehat g(\xi)}\,d\xi
\to0.
\tag{28}
\]

Thus, provided the canonical `h_n` belong to `H_w`, equations (21)--(25) apply verbatim. In particular, multiplying Fourier modes by a smooth, polynomial, elliptic, or other absolutely-continuous spectral weight cannot turn exact mixed-shell nullity into a surviving closable positive prime-power sector.

This identifies the load-bearing issue more precisely than `different topology`: a successful translation-compatible topology must alter the **spectral type** seen by far translations, not merely reweight Lebesgue-frequency modes.

## 5. Matched control: adjoining the net-flux trace really does evade the closure

The preceding theorem would be too broad if it claimed that every reasonable topology fails. There is a canonical counter-control already latent in the source geometry.

On `S(R)`, define

\[
\|f\|_*^2
=\|f\|_{H^r}^2+c|\widehat f(0)|^2,
\qquad c>0,
\tag{29}
\]

and complete. Equivalently, the completion remembers an ordinary absolutely-continuous Sobolev component together with one extra zero-frequency trace coordinate. Translation acts unitarily because

\[
\widehat{\tau_t f}(0)=\widehat f(0).
\tag{30}
\]

For the cyclotomic profiles,

\[
\widehat h_n(0)
=\int_{\mathbb R}h_n(u)\,du
=\int_0^\infty\rho_n(s)\,ds
=\Lambda(n).
\tag{31}
\]

Therefore the far translates of a prime-power profile do **not** converge weakly to zero in this topology: their zero-frequency coordinate remains `Lambda(p^a)=log p`. The mixed-shell differences (20) have zero trace, so their closed span cannot reach the missing trace coordinate of `h_{p^a}`.

The positive form

\[
Q_*(f)=c|\widehat f(0)|^2
\tag{32}
\]

is bounded in the new topology and satisfies

\[
Q_*(h_m)=0
\quad(\omega(m)\ge2),
\qquad
Q_*(h_{p^a})=c(\log p)^2.
\tag{33}
\]

This is an exact matched control: changing spectral type can defeat the closure theorem. But the survivor is exactly the `WP-374` zero-Mellin form. Under the usual critical half-density scaling of a shell by `n^{-1/4}`, it gives

\[
Q_*(n^{-1/4}h_n)
=c\frac{\Lambda(n)^2}{\sqrt n},
\tag{34}
\]

not the linear finite Weil weight `Lambda(n)/sqrt(n)`.

Thus the most canonical singular/topological escape is real but does not advance the global Weil-positivity objective.

## 6. A single nonzero Fourier atom cannot be the exact selector

The zero trace in the preceding control is not just one convenient atomic choice. It is forced within the simplest atomic class.

Fix `xi_0 in R` and adjoin the Fourier trace `f -> hat f(xi_0)` to any ambient topology in which that trace is defined. Consider the positive atomic form

\[
Q_{\xi_0}(f)=c|\widehat f(\xi_0)|^2.
\tag{35}
\]

Suppose for one prime power `n=p^a` that

\[
Q_{\xi_0}(h_n)>0
\tag{36}
\]

while every spectator-prime mixed shell is null:

\[
Q_{\xi_0}(h_{nq})=0
\qquad(q\ne p\text{ prime}).
\tag{37}
\]

Taking the Fourier transform of (20) gives

\[
\widehat h_{nq}(\xi_0)
=\left(e^{i\xi_0\log q}-1\right)\widehat h_n(\xi_0).
\tag{38}
\]

By (36), `hat h_n(xi_0) ne 0`, so (37) forces

\[
e^{i\xi_0\log q}=1
\qquad\text{for every spectator prime }q.
\tag{39}
\]

Choose any two distinct spectator primes `q_1,q_2`. If `xi_0 ne 0`, then

\[
\xi_0\log q_j=2\pi k_j
\qquad(k_j\in\mathbb Z\setminus\{0\}),
\tag{40}
\]

and hence

\[
\frac{\log q_1}{\log q_2}=\frac{k_1}{k_2}\in\mathbb Q.
\tag{41}
\]

Exponentiating an integer relation implied by (41) contradicts unique factorization. Therefore

\[
\boxed{\xi_0=0.}
\tag{42}
\]

So a one-frequency singular trace cannot hide a more useful oscillatory selector: exact spectator-prime nullity forces it back to the zero Mellin frequency, where positivity squares the Mangoldt mass as in (33).

## 7. Adversarial checks and novelty boundary

The first attempted falsification is changing Sobolev order. It fails because the profiles are Schwartz and translations weakly escape in every `H^r`; no regularity threshold appears. The second is replacing the polynomial Sobolev multiplier by an arbitrary absolutely-continuous Fourier weight. It fails for the same `L^2 x L^2 -> L^1` Riemann--Lebesgue argument. The third is to add singular spectral data. That one succeeds, and the explicit zero-trace topology (29) is retained as the matched control rather than ruled out by definition.

The single-atom test then asks whether the singular escape could sit at a nonzero Mellin frequency and retain genuinely oscillatory information. Equations (38)--(42) rule that out for an atomic positive selector that must kill every spectator-prime mixed shell while retaining a prime-power shell.

The functional-analytic ingredients are classical. Weak escape of translations in `L^2`/Sobolev spaces, Mazur convexification, Fourier multiplier realizations, and concentration-compactness descriptions of mass escaping under translations are standard. A bounded literature search found those general mechanisms but no source applying the all-Sobolev closure plus the cyclotomic identity (20) to this Mangoldt/Weil-positivity question. No novelty is claimed for the general analytic lemmas.

Within Mathia this is not a restatement of `WP-375`: that finding deliberately left a different ambient topology as an escape. The present result closes every finite-order Sobolev topology and the broader absolutely-continuous Fourier-weight class, then exhibits and classifies the simplest source-native singular trace escape. Nor is it classical Weil positivity, Hilbert--Polya, Connes/trace, Sonin/localization, or a zero-defined spectrum: no zeta zero enters the proof.

## Consequence for the research line

A future radial positive-form candidate cannot evade `WP-375` merely by declaring that `L^2` was the wrong regularity scale and replacing it with `H^r`, a derivative energy, a Bessel-potential norm, or another absolutely-continuous Fourier multiplier topology. All of those preserve the same weak spectator-prime escape and therefore the same radical-collapse theorem.

The canonical way to stop weak escape is to retain a translation point mode. But the exact spectator identities force a single surviving point mode to be the zero Mellin frequency, and the associated positive norm returns `Lambda^2`, not `Lambda`. A materially new topological route therefore needs more than ordinary Sobolev regularity or one spectral trace: it must supply a source-forced singular/global sector with genuine finite--archimedean incidence, or keep mixed shells active through an indefinite/global assembly before final positivity.

No global Weil-positive form, Gamma/polar completion, or independent sign theorem is produced here. The result is a decisive negative that narrows the topological escape left open by `WP-375` while preserving a sharp control showing exactly how and where that escape can occur.