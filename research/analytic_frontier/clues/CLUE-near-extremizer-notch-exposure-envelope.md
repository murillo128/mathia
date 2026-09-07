---
id: CLUE-analytic-frontier-near-extremizer-notch-exposure-envelope
type: research-clue
status: accepted
origin: research-watch
target_line: analytic_frontier
based_on:
  - research/analytic_frontier/findings/ANF-086-affine-slack-opens-a-uniform-hilbert-tube-around-all-separable-fibers.md
  - research/analytic_frontier/findings/ANF-087-montgomery-taylor-equality-is-a-two-site-real-zero-set-packing.md
  - research/analytic_frontier/findings/ANF-088-montgomery-taylor-excess-is-an-exact-projection-tax.md
  - research/analytic_frontier/findings/ANF-097-fatal-near-extremizers-require-macroscopic-source-anti-alignment.md
  - research/analytic_frontier/findings/ANF-098-convexifying-separable-carriers-erases-all-center-height-nonseparability.md
---

# Can near-extremizer notch exposure decide the whole fixed notch ray without selecting a separable carrier?

## Observation

ANF-097 isolates destructive source interference with every compatible separable comparator, and ANF-098 shows that convexifying that comparison class destroys the question. However, the affine certificate does not require reconstructing the entire configuration or finding a product comparator: it only needs an upper bound on the energy removed by the fixed central notch.

There are two unused opportunities. First, the globally optimal affine constant along a fixed notch direction is an infimum of affine functions, so its initial slope should be governed by the notch exposure of **all nearly active configurations**, not only the exact equality cases in ANF-087. Second, ANF-088 already approximates the actual source tensor by its adapted equality-signature tensor with a norm error bounded by the square root of the source excess. Applying only the notch observable to those tensors is a weaker objective than reconstructing a nearby physical separable multiset.

## Research question

Freeze one notch width `eta` and its complete shape before varying its amplitude. Write

\[
J_0=J_{\rm MT},\qquad
\phi_\eta(\alpha)=b_\eta(1-|\alpha|/\eta)_+,
\qquad 0\le\phi_\eta\le J_0,
\]

with the ANF-086 conventions. For every nonempty finite conjugation-invariant multiset `W`, let

\[
L(W)=2|W|-\sigma(W),\qquad
S_W(\alpha)=\sum_{z\in W}e^{-2\pi i\alpha z},
\]

where `sigma` counts simple **real** sites, and define

\[
r(W)=\frac{\int J_0|S_W|^2}{L(W)},\qquad
e(W)=r(W)-1,\qquad
h_\eta(W)=\frac{\int\phi_\eta|S_W|^2}{L(W)}.
\tag{1}
\]

Lamzouri's inequality and spectral domination give `r>=1` and `0<=h_eta<=r`. Put

\[
A_\eta(\varepsilon)=\sup_{e(W)\le\varepsilon}h_\eta(W),
\qquad
\beta_\eta=\lim_{\varepsilon\downarrow0}A_\eta(\varepsilon),
\tag{2}
\]

where the supremum includes **every finite cardinality**, every multiplicity, and unbounded geometry. The sets are nonempty because real singleton equality configurations exist; monotonicity and `A_eta(epsilon)<=1+epsilon` give `0<=beta_eta<=1`.

Let `C_0=C_MT` and

\[
B_\eta=\frac{C(\phi_\eta)}{C_0}
=\frac{b_\eta(1+\eta^2/3)}{C_0}.
\tag{3}
\]

For `J_t=J_0-t phi_eta`, define the optimal global affine floor

\[
q_\eta(t)=\inf_W\{r(W)-t h_\eta(W)\},
\qquad \rho_\eta(t)=\frac{C(J_t)}{C_0}=1-tB_\eta.
\tag{4}
\]

Audit the proposed exact criterion

\[
\boxed{q_\eta'(0+)=-\beta_\eta,\qquad
\exists\,0<t<\min(1,1/B_\eta):\ q_\eta(t)>\rho_\eta(t)
\iff \beta_\eta<B_\eta.}
\tag{5}
\]

Then attack `beta_eta<B_eta` through the **source-generated tensor concentration test** below, rather than through a full nonconvex separable-selection theorem. A physical near-extremizing sequence with notch exposure at least `B_eta` would instead rule out strict improvement at every positive admissible amplitude along this one frozen direction.

## Why it may matter

This would replace a stronger geometric sufficient condition by an exact scalar decision for the fixed notch ray. It also changes the quantifier burden: qualitative, all-cardinality near-extremizer control can be sufficient for the existence of a smaller improving amplitude, even when no rate is strong enough to close the original fixed amplitude in ANF-086.

The proposed contribution is not a bound on `beta_eta`. It is a derivation of the precise observable that needs bounding, a direct way to read it from the existing projection-tax identity, and explicit controls against two invalid relaxations. This could support either a complete auxiliary certificate or a decisive negative result for the entire frozen ray without solving a harder configuration-reconstruction problem first.

## Decisive test

**Reconstruct the envelope without assuming compactness or an attained minimizer.** For each `epsilon>0`, split configurations into `e<=epsilon` and `e>epsilon`. In the first part, `r-t h>=1-t A_eta(epsilon)`. In the second, `h<=r` gives `r-t h>=(1-t)(1+epsilon)` for `0<t<1`. Therefore

\[
q_\eta(t)\ge
\min\{1-tA_\eta(\varepsilon),(1-t)(1+\varepsilon)\}.
\tag{6}
\]

Choose approximate maximizers in (2) along `epsilon_n downarrow 0`. They have `r(W_n)->1` and `h_eta(W_n)->beta_eta`; no bounded-cardinality subsequence is assumed. For every fixed positive `t`, their affine values imply

\[
q_\eta(t)\le1-t\beta_\eta.
\tag{7}
\]

When `t<=epsilon/(1+epsilon)`, the second term in (6) is at least one. Dividing (6)--(7) by `t` after subtracting one and then sending `t downarrow0`, followed by `epsilon downarrow0`, proves the derivative assertion in (5).

More importantly, (6)--(7) decide existence on the whole admissible ray. If `beta_eta>=B_eta`, (7) excludes strict improvement for every such `t`, **including the equality case**. If `A_eta(epsilon)<=a<B_eta` for one positive `epsilon`, choose any

\[
0<t\le
\min\left\{\frac{\varepsilon}{2(1+\varepsilon)},
\frac1{2(1+B_\eta)}\right\}.
\tag{8}
\]

Then (6) gives the single global certificate

\[
E_{J_t}(W)\ge (1-ta)L(W),\qquad
1-ta>1-tB_\eta>0,\qquad
\frac{C(J_t)}{1-ta}<C_0.
\tag{9}
\]

The existence of `epsilon,a` follows from `beta_eta<B_eta`. Conversely (7) proves necessity, not merely failure of a sufficient bound. This is not convexifying the class of physical configurations: each affine function in (4) still comes from an actual multiset. The proof only studies their scalar lower envelope.

**Transfer the observable to the existing equality-signature tensor.** Use ANF-087's `g`, with `eta_MT=sqrt(g)` and `J_0=g*g`, and work on `[-1/2,1/2]^2`. The actual tensor is

\[
\mathcal F_W(u,v)=\eta_{\rm MT}(u)\eta_{\rm MT}(v)S_W(u+v).
\]

Let `mathcal T_W` be exactly the ANF-088 adapted `2/1/0` tensor, not a freely chosen projection. That finding gives

\[
\|\mathcal F_W-\mathcal T_W\|_2^2\le e(W)L(W),
\qquad
\|\mathcal T_W\|_2^2=4D_U+(D_V-D_U)\le L(W).
\tag{10}
\]

The second bound follows directly from `D_U=r+k`, `D_V-D_U=n`, and the true real/nonreal multiplicities; the counts `r,k,n` here are the ANF-088 dimension counts, not the energy ratio in (1).

Define the contraction `M_eta` as multiplication by

\[
m_\eta(u,v)=\sqrt{\frac{\phi_\eta(u+v)}{J_0(u+v)}}.
\tag{11}
\]

Set it to zero where both numerator and denominator vanish. The only endpoint ambiguity is null for the integral, and `0<=m_eta<=1`. The convolution identity gives exactly

\[
h_\eta(W)=\frac{\|M_\eta\mathcal F_W\|_2^2}{L(W)}.
\tag{12}
\]

Put `Theta_eta(W)=||M_eta mathcal T_W||_2^2/L(W)`. From (10)--(12), the reverse triangle inequality and contraction give

\[
\boxed{
|\sqrt{h_\eta(W)}-\sqrt{\Theta_\eta(W)}|\le\sqrt{e(W)},
\qquad
|h_\eta(W)-\Theta_\eta(W)|\le2\sqrt{e(W)}+e(W).
}
\tag{13}
\]

For the second estimate, expand the squared norm around `mathcal T_W` and use `||M_eta mathcal T_W||<=sqrt(L(W))`. Consequently

\[
\boxed{\beta_\eta=
\lim_{\varepsilon\downarrow0}
\sup_{e(W)\le\varepsilon}\Theta_\eta(W).}
\tag{14}
\]

A decisive positive target is now explicit: find one `epsilon>0` and a **uniform physical** bound

\[
\sup_{e(W)\le\varepsilon}\Theta_\eta(W)
+2\sqrt\varepsilon+\varepsilon < B_\eta.
\tag{15}
\]

It supplies `a` in (8)--(9). A decisive negative target is an actual sequence `e(W_n)->0` with `liminf Theta_eta(W_n)>=B_eta`; by (13) and (7), that kills this fixed ray. This is concentration of a source-generated tensor near `u+v=0`, not reconstruction of all center-height data, and no inverse Gram matrix or condition number enters the transfer.

**Check what qualitative separable stability would already buy.** Freeze the original certified amplitude `s_0` and constant `q_0` from ANF-086, with `q_0>1-s_0 B_eta`. If the all-sequence implication

\[
e(W_n)\to0\ \Longrightarrow\
d_{\rm sep}^{(s_0)}(W_n)\to0
\tag{16}
\]

were proved, ANF-086 would give `liminf E_(J_(s_0))(W_n)/L(W_n)>=q_0`. Since this ratio is `r(W_n)-s_0 h_eta(W_n)`, applying it to approximate maximizers in (2) yields

\[
\beta_\eta\le\frac{1-q_0}{s_0}<B_\eta.
\tag{17}
\]

Thus **no quantitative convergence rate in (16) is needed to prove existence of an improving smaller amplitude**. This does not certify the original `s_0`, does not replace uniformity over growing cardinalities by fixed-cardinality compactness, and does not prove (16). The direct tensor test (15) is potentially weaker still: it need not reconstruct any physical separable comparator.

**Retain two falsification controls.** Testing only exact equality cases cannot determine the envelope. As an abstract scalar control, take admissible pairs `(r,h)=(1,1/4)` and `(1+1/n^2,3/4)` for all positive integers `n`. They satisfy `r>=1` and `0<=h<=r`. The exact minimizer has exposure `1/4`, but the nearly active envelope has `beta=3/4` and `q(t)=1-3t/4`. With objective slope `B=1/2`, there is no improvement. This is not a physical counterexample; it demonstrates why the finite equality classification in ANF-087 alone cannot settle (5).

Nor may the source-generated tensors in (14)--(15) be replaced by arbitrary tensors with the same signature. Let `psi_j(u)=exp(2 pi i j u)`, `1<=j<=m`, be orthonormal on `[-1/2,1/2]`, and form the abstract tensor `T_m=2 sum_j psi_j(u)psi_j(v)` with normalization `L_m=4m`. Its notch exposure is

\[
\frac{\|M_\eta T_m\|_2^2}{4m}
=\frac1m\int_{-1}^{1}(1-|\alpha|)
\frac{\phi_\eta(\alpha)}{J_0(\alpha)}
\left|\sum_{j=1}^{m}e^{2\pi i j\alpha}\right|^2d\alpha
\longrightarrow \frac{b_\eta}{J_0(0)}.
\tag{18}
\]

The limit is the elementary Fejer approximate identity: the multiplier is continuous near zero and supported inside `(-1,1)`, and the other period-edge peaks do not contribute. For sufficiently small fixed `eta`, this limit exceeds `B_eta`, since

\[
\frac{b_\eta/J_0(0)}{B_\eta}
=\frac{C_0}{J_0(0)(1+\eta^2/3)}>1,
\qquad
C_0=J_0(0)+\int |\alpha|J_0(\alpha)\,d\alpha>J_0(0).
\tag{19}
\]

These abstract orthonormal tensors have the right coefficient pattern and mass, but are **not asserted to arise from actual configurations with small source excess**. Their control says that (10)'s rank/signature data alone cannot prove the wanted concentration bound. The relation between the adapted subspaces and the actual exponential source must survive. This blocks a specific false shortcut without refuting (15) on its physical class.

## Evidence boundary

This is a proposed analytical handoff for independent Research Watch validation. The envelope and tensor-transfer arguments are supplied for checking, but no upper bound `beta_eta<B_eta`, no counterexample sequence in the physical class, and no new all-configuration affine certificate is established here. In particular, moving `eta` with `t`, optimizing the notch after inspecting the configurations, or proving only fixed-cardinality stability changes the question.

The envelope mechanism is classical optimization/sensitivity mathematics, not a theorem-level novelty claim. Paul Milgrom and Ilya Segal, *Envelope Theorems for Arbitrary Choice Sets*, Econometrica 70(2) (2002), 583--601, DOI `10.1111/1468-0262.00296`, is an appropriate prior-art boundary for value-function derivatives on unrestricted choice sets. No theorem from it is imported without hypotheses: (6)--(7) give the complete elementary proof needed here, including nonattainment and nearly active configurations. The multiplication-operator estimate and Fejer control are likewise classical; their proposed Mathia use is the exact observable-level splice into ANF-088.

A finite numerical search can produce witnesses and stress-test identities, but cannot upper-bound the all-cardinality supremum in (2) or (15). Even a successful positive answer would first establish an auxiliary affine certificate requiring the full analytic zero-counting assembly; it is not by itself an improved unconditional zero proportion or a proof of RH. A negative answer would exclude only the frozen notch direction, not all analytic methods, other spectra, or RH.

## Research disposition

Accepted. The unrestricted lower-envelope argument and the `ANF-088` tensor-transfer identities have been independently reconstructed and canonicalized in [[research/analytic_frontier/findings/ANF-099-fixed-notch-ray-is-controlled-by-near-extremizer-exposure.md]]. The remaining live question is physical: prove `beta_eta<B_eta`, equivalently a uniform near-extremizer bound on the canonical tensor exposure, or construct an actual Montgomery--Taylor near-extremizing sequence whose limiting exposure is at least `B_eta`. Exact equality cases and arbitrary tensors carrying only the abstract `2/1/0` signature do not decide that question.