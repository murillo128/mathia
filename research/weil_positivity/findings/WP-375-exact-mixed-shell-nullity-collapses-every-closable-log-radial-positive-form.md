---
id: WP-375
title: Exact mixed-shell nullity collapses every closable log-radial positive form
branch: weil_positivity
status: supported
kind: cyclotomic-log-radial-closable-positive-form-obstruction
claim_strength: exact RH-independent no-go showing that on the canonical log-radial L2 space, any closable positive form that assigns zero energy to every mixed-prime shell must also assign zero energy to every prime-power shell; this removes stationarity from the main escape left by WP-374
created: 2026-09-19
related: [WP-162, WP-374]
clues: [CLUE-weil-positivity-noncharacter-finite-archimedean-incidence]
prior_art:
  - classical cyclotomic identity Phi_nq(x)=Phi_n(x^q)/Phi_n(x) for q prime and q not dividing n
  - classical weak convergence to zero of far translations in L2(R), via Plancherel and the Riemann-Lebesgue lemma
  - classical Mazur lemma converting weak convergence into norm-convergent convex combinations
  - standard sequential criterion for closability of nonnegative quadratic forms
---

# WP-375 — Exact mixed-shell nullity collapses every closable log-radial positive form

## Claim

`WP-374` proved that a **translation-stationary** positive geometry on the canonical log-radial cyclotomic fluxes cannot make all mixed-prime shells null while retaining nontrivial radial information on prime powers. Its explicit escape was to abandon translation stationarity and try a source-forced nonstationary positive form.

That escape is much smaller than it appeared. Stationarity is not needed for the obstruction once the positive form is required to be closable in the canonical ambient radial topology.

Let

\[
H=L^2(\mathbb R,du),
\]

let `D subset H` be a linear subspace containing every canonical shell profile

\[
h_n(u)=e^u\rho_n(e^u),
\]

and let `Q` be a nonnegative Hermitian form on `D`. Assume only that `Q` is **closable in `H`**. No translation invariance, convolution representation, locality, boundedness, or commutation with dilations is assumed.

If

\[
Q(h_m)=0
\qquad
\text{for every }m\text{ having at least two distinct prime factors},
\tag{1}
\]

then necessarily

\[
\boxed{Q(h_{p^a})=0\quad\text{for every prime power }p^a.}
\tag{2}
\]

Hence a closable positive form on the canonical log-radial `L^2` space cannot use exact zero energy as the Mangoldt selector at all: exact mixed-shell nullity forces **every nontrivial cyclotomic shell** into the form radical.

This is stronger than `WP-374`. There the collapse followed from positivity plus translation covariance. Here the only global analytic requirement is the standard one needed for a positive quadratic form to define a closed/closable energy on the ambient Hilbert space.

**Classification:** `EXACT-DERIVED + RH-INDEPENDENT + CYCLOTOMIC-TRANSLATION-COBOUNDARY + L2-WEAK-ESCAPE + MAZUR-CONVEXIFICATION + POSITIVE-RADICAL-RIGIDITY + CLOSABILITY-NO-GO + NONSTATIONARY-INCLUDED + FINITE-PANEL-SHARP-CONTROL + NO-ZERO-DATA + CLASSICAL-INGREDIENTS + NOT-A-GLOBAL-WEIL-POSITIVITY-PROOF`.

## 1. Spectator primes generate mixed shells as far translation differences

The canonical identity from `WP-374` is

\[
h_{nq}=\tau_{\log q}h_n-h_n,
\qquad
(\tau_t f)(u)=f(u+t),
\tag{3}
\]

whenever `q` is prime and `q` does not divide `n`. Also

\[
h_n\in L^1(\mathbb R)\cap L^2(\mathbb R),
\qquad
\int_{\mathbb R}h_n(u)\,du=\Lambda(n).
\tag{4}
\]

Fix a prime power `n=p^a` and choose distinct spectator primes `q_j ne p` with `q_j to infinity`. Then `t_j=log q_j to infinity`.

For every `g in L^2(R)`, Plancherel gives

\[
\langle \tau_{t_j}h_n,g\rangle
=
\int_{\mathbb R}e^{i\xi t_j}\widehat h_n(\xi)\overline{\widehat g(\xi)}\,d\xi
\tag{5}
\]

up to the fixed Fourier normalization. The product in (5) lies in `L^1` by Cauchy--Schwarz. The Riemann--Lebesgue lemma therefore implies

\[
\tau_{t_j}h_n\rightharpoonup0
\qquad\text{weakly in }L^2(\mathbb R).
\tag{6}
\]

By Mazur's lemma, there are finite convex combinations of tails

\[
v_k=\sum_j\alpha_{k,j}\tau_{\log q_j}h_n,
\qquad
\alpha_{k,j}\ge0,
\qquad
\sum_j\alpha_{k,j}=1,
\tag{7}
\]

such that

\[
v_k\longrightarrow0
\qquad\text{strongly in }L^2(\mathbb R).
\tag{8}
\]

Using (3), define

\[
y_k:=\sum_j\alpha_{k,j}h_{nq_j}.
\tag{9}
\]

Because the coefficients sum to one,

\[
y_k=v_k-h_n,
\qquad
y_k\longrightarrow-h_n
\quad\text{in }L^2.
\tag{10}
\]

Thus every prime-power shell profile lies in the ambient `L^2` closure of the linear span of mixed-prime shell profiles. This closure statement is purely a consequence of the source-forced cyclotomic dilation identity; no candidate positive form has yet been chosen.

## 2. Positivity turns each exact zero into a radical vector

For a nonnegative Hermitian form, Cauchy--Schwarz gives

\[
|Q(x,z)|^2\le Q(x)Q(z).
\tag{11}
\]

Therefore

\[
Q(x)=0\quad\Longrightarrow\quad Q(x,z)=0
\quad\text{for all }z\in D.
\tag{12}
\]

Under assumption (1), every `h_{nq_j}` in (9) is a mixed-prime shell and hence is in the radical of `Q`. Every finite linear combination `y_k` is therefore also radical:

\[
Q(y_k,z)=0
\qquad\text{for all }z\in D.
\tag{13}
\]

In particular,

\[
Q(y_k-y_l)=0.
\tag{14}
\]

## 3. Closability transfers the radical through the ambient L2 limit

Set

\[
z_k:=y_k+h_n=v_k.
\tag{15}
\]

By (8), `z_k to 0` in the ambient Hilbert norm. Because the `h_n` term cancels in differences and the `y_k` are radical,

\[
Q(z_k-z_l)=Q(y_k-y_l)=0.
\tag{16}
\]

Also, by (13),

\[
Q(z_k)=Q(h_n+y_k)=Q(h_n).
\tag{17}
\]

The standard sequential criterion for closability of a nonnegative form says that whenever

\[
z_k\to0\text{ in }H
\quad\text{and}\quad
Q(z_k-z_l)\to0,
\]

one must have `Q(z_k) to 0`. Applying it to (15)--(17) yields

\[
Q(h_n)=0.
\tag{18}
\]

Since the prime power `n=p^a` was arbitrary, (2) follows.

The result can be stated geometrically as

\[
\boxed{
\overline{\operatorname{span}}^{L^2}
\{h_m:\omega(m)\ge2\}
\supset
\{h_{p^a}:p\text{ prime},a\ge1\},
}
\tag{19}
\]

and a closable positive form cannot keep a vector energetic while an approximating sequence from its radical converges to it in the ambient topology.

## 4. Matched control: the zero-Mellin survivor is exactly nonclosable

`WP-374` identified the scalar stationary survivor

\[
Q_0(f)=c\left|\int_{\mathbb R}f(u)\,du\right|^2,
\qquad c>0,
\tag{20}
\]

on a domain such as `L^1 cap L^2`. It does exactly what (2) says a closable `L^2` form cannot do:

\[
Q_0(h_m)=c\Lambda(m)^2,
\tag{21}
\]

so all mixed-prime shells vanish while prime powers survive.

The apparent counterexample is sharp because `Q_0` is not closable in `L^2`. Let

\[
f_j(u)=j^{-1}{\bf 1}_{[0,j]}(u).
\tag{22}
\]

Then

\[
\|f_j\|_2=j^{-1/2}\to0,
\qquad
\int f_j=1,
\qquad
Q_0(f_j)=c.
\tag{23}
\]

Moreover `int(f_j-f_k)=0`, hence

\[
Q_0(f_j-f_k)=0
\tag{24}
\]

for every `j,k`. Equations (23)--(24) violate the closability criterion exactly. The exceptional zero-Mellin functional is therefore not an omitted closable nonstationary solution; it lives outside the canonical `L^2` energy topology.

## 5. Matched control: finite spectator panels can fake the separation

The obstruction is genuinely global. Fix a prime power `n=p^a` and only finitely many spectator primes `q_1,...,q_r`. Let

\[
M=\operatorname{span}\{h_{nq_1},\ldots,h_{nq_r}\}\subset L^2.
\tag{25}
\]

Every element of `M` is in `L^1` and has integral zero, while

\[
\int h_n=\Lambda(n)>0.
\tag{26}
\]

Hence `h_n notin M`. Since `M` is finite-dimensional, it is closed. If `w=P_{M^\perp}h_n`, then `w ne 0` and the bounded rank-one form

\[
Q_M(f)=|\langle f,w\rangle_{L^2}|^2
\tag{27}
\]

is positive and closable, annihilates each tested mixed shell `h_{nq_j}`, yet satisfies

\[
Q_M(h_n)=\|w\|_2^4>0.
\tag{28}
\]

Thus no finite-prime numerical panel can establish the infinite obstruction. The theorem begins only when arbitrarily far spectator-prime translations are admitted, exactly where weak escape plus convexification makes the mixed-shell span ambiently dense along each prime-power direction.

## 6. Consequence for the Weil-positivity search

This closes the most direct nonstationary continuation left by `WP-374`. A candidate cannot evade the stationary theorem merely by replacing convolution or translation covariance with an arbitrary position-dependent positive kernel if that kernel still defines a closable quadratic form on the canonical log-radial `L^2` space and uses exact mixed-shell zero energy as its arithmetic selector.

A surviving route must violate at least one premise for a source-justified reason. In particular it must do one of the following: use a different intrinsic topology in which the far-translated shell profiles do not have the closure behavior above; use a singular/nonclosable boundary functional and independently justify why that is the native geometric object rather than a regularization artifact; avoid exact mixed-shell nullity on the positive diagonal; or create the required finite-prime incidence **before** radial projection so that the arithmetic information is not represented only by the vectors `h_n` in one common `L^2` space.

The last option is the cleanest continuation of the accepted noncharacter-incidence clue. The theorem does not exclude an indefinite intermediate finite--archimedean coupling whose mixed shells remain active until after assembly, nor a different cohomological/intersection topology forced by the source geometry. It says that ordinary Hilbert-form positivity on the canonical radial profiles is now exhausted more broadly than the stationary analysis alone showed.

## 7. Adversarial novelty audit

The proof ingredients are classical and are not claimed as new: weak vanishing of translations in `L^2`, the Riemann--Lebesgue lemma, Mazur's lemma, the positive-form Cauchy--Schwarz inequality, and the standard closability criterion. A bounded literature search also finds classical work characterizing closable semibounded Toeplitz/Wiener--Hopf forms, reinforcing that closability is standard operator-form structure rather than a Mathia-specific theorem.

The repository search found no existing Mathia result combining those facts with the exact cyclotomic spectator identity (3) to prove the closure statement (19) and its consequence (2). `WP-374` required strong translation covariance of the candidate positive form; the present argument explicitly removes that assumption. The novelty here is therefore only the **application-level obstruction for this Mathia construction**, not any of the functional-analytic lemmas.

This is also not a reformulation of classical Weil positivity, Hilbert--Polya, Connes/trace, Sonin/localization, or a zero-defined spectrum: no zeta zeros enter the construction or proof. Conversely, it supplies no global Weil-positive form and proves no statement equivalent to RH. It is a decisive negative that narrows which intrinsic Mathia geometries can still plausibly support such a form.

## Status

Supported exact no-go under the stated canonical `L^2`-closability hypothesis. The stationary escape left open in `WP-374` is closed for every closable nonnegative form on the same ambient radial Hilbert space. The remaining research burden is to justify a genuinely different source-native topology/coupling or to move the finite--archimedean incidence upstream of radial positive scalarization.