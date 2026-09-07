# ANF-105 — endpoint-decoupled profile splitting cannot raise fixed-notch exposure

**Status:** `EXACT-DERIVED + MULTIPROFILE-POLARIZATION + EXPOSURE-LOCALIZATION + ENDPOINT-DECOUPLING + SUPERLINEAR-BULK-NARROWING`. `ANF-101` leaves genuinely superlinear horizontal escape as a separate noncompact regime for the fixed-notch envelope, while `ANF-103`--`ANF-104` show that a sparse remote tail matters only if it remains source-heavy and keeps an endpoint-amplified interaction channel open to its core. The same mechanism extends beyond a one-core/one-tail split. For an arbitrary partition into conjugation-invariant physical profiles, if the **aggregate** cross interaction is small in both the Montgomery--Taylor source norm and the fixed-notch observable, then a globally near-extremal high-exposure configuration contains one component that is itself near-extremal and carries essentially the full normalized notch exposure.

Consequently, horizontal superlinearity created only by asymptotically decoupled fragmentation cannot enlarge the envelope `beta_eta` of `ANF-099`. A sequence relevant to the obstruction can always be localized to one of its profiles. The surviving superlinear branch is therefore narrower: it must be genuinely **interaction-bearing**, in the sense that no useful physical profile decomposition has vanishing aggregate cross budget. Using the explicit Montgomery--Taylor kernel from `ANF-104` and the exact Fourier--Laplace transform of the triangular notch, one sufficient condition for decoupling is a single inverse-square endpoint coupling sum.

## 1. Exact multiprofile bookkeeping

Fix the notch width `0<eta<1` and notation of `ANF-099`,

\[
J_0=J_{\rm MT},\qquad
\phi_\eta(\alpha)=b_\eta(1-|\alpha|/\eta)_+,
\]

and for every nonempty finite conjugation-invariant multiset `X` write

\[
S_X(\alpha)=\sum_{z\in X}e^{-2\pi i\alpha z},
\qquad
L(X)=2|X|-\sigma(X),
\]

\[
r(X)=\frac{\int J_0|S_X|^2}{L(X)},
\qquad
e(X)=r(X)-1\ge0,
\qquad
h_\eta(X)=\frac{\int\phi_\eta|S_X|^2}{L(X)}.
\tag{1}
\]

The pointwise domination `0<=phi_eta<=J_0` gives

\[
0\le h_\eta(X)\le1+e(X).
\tag{2}
\]

Let

\[
W=\bigsqcup_{j=1}^m X_j
\tag{3}
\]

be any finite partition into nonempty conjugation-invariant pieces that is complete on every real-part fiber. Thus no real support site is divided between components, and the affine denominator is exactly additive:

\[
L(W)=\sum_{j=1}^mL(X_j)=:L.
\tag{4}
\]

For `psi=J_0` or `phi_eta`, put

\[
\mathcal C_\psi(X_i,X_j)
:=\operatorname{Re}\int\psi(\alpha)
S_{X_i}(\alpha)\overline{S_{X_j}(\alpha)}\,d\alpha,
\tag{5}
\]

and define the normalized absolute cross budgets

\[
\delta_0
:=\frac2L\sum_{i<j}|\mathcal C_{J_0}(X_i,X_j)|,
\qquad
\delta_\eta
:=\frac2L\sum_{i<j}|\mathcal C_{\phi_\eta}(X_i,X_j)|.
\tag{6}
\]

Set `w_j=L(X_j)/L`. Polarization gives the exact identities

\[
\sum_jw_je(X_j)
=e(W)-\frac2L\sum_{i<j}\mathcal C_{J_0}(X_i,X_j),
\tag{7}
\]

and

\[
h_\eta(W)
=\sum_jw_jh_\eta(X_j)
+\frac2L\sum_{i<j}\mathcal C_{\phi_\eta}(X_i,X_j).
\tag{8}
\]

Since every component separately satisfies the Montgomery--Taylor floor, the left side of (7) is nonnegative. Therefore, with

\[
E:=\sum_jw_je(X_j),
\qquad q:=e(W)+\delta_0,
\tag{9}
\]

one has the finite bounds

\[
0\le E\le q,
\qquad
\left|h_\eta(W)-\sum_jw_jh_\eta(X_j)\right|\le\delta_\eta.
\tag{10}
\]

These statements allow arbitrarily many profiles and make no assumption about their relative cardinalities.

## 2. A near-extremal high-exposure component survives every decoupled split

Assume first `0<q<=1` and call a component good when

\[
e(X_j)\le\sqrt q.
\tag{11}
\]

By Markov's inequality applied to the nonnegative numbers `e(X_j)`, the total affine weight of the bad components is at most

\[
\sum_{j\,\mathrm{bad}}w_j\le\frac{E}{\sqrt q}\le\sqrt q.
\tag{12}
\]

Using (2), their total notch contribution obeys

\[
\sum_{j\,\mathrm{bad}}w_jh_\eta(X_j)
\le
\sum_{j\,\mathrm{bad}}w_j
+
\sum_{j\,\mathrm{bad}}w_je(X_j)
\le\sqrt q+q.
\tag{13}
\]

Equations (8), (10), and (13) then imply

\[
\sum_{j\,\mathrm{good}}w_jh_\eta(X_j)
\ge
h_\eta(W)-\delta_\eta-\sqrt q-q.
\tag{14}
\]

Because the good weights sum to at most one, at least one good component satisfies

\[
\boxed{
 e(X_j)\le\sqrt{e(W)+\delta_0},
}
\tag{15}
\]

and

\[
\boxed{
 h_\eta(X_j)
\ge
h_\eta(W)-\delta_\eta
-\sqrt{e(W)+\delta_0}
-e(W)-\delta_0.
}
\tag{16}
\]

If `q=0`, (7) forces every positive-weight component to have zero excess and the same conclusion follows directly from (8), so (15)--(16) remain valid by continuity.

This is the key localization lemma. It does **not** say that every component is near-extremal, nor that the selected component has a positive fraction of the original cardinality. Neither is needed for the envelope problem. It says something sharper for `ANF-099`: whenever a physical decomposition is asymptotically orthogonal in the two relevant quadratic forms, one component retains essentially all of the normalized exposure while its own Montgomery--Taylor excess vanishes.

In particular, for any sequence of partitions

\[
W_n=\bigsqcup_jX_{n,j}
\tag{17}
\]

with

\[
e(W_n)\to0,
\qquad
\delta_{0,n}+\delta_{\eta,n}\to0,
\tag{18}
\]

there are components `Y_n=X_{n,j(n)}` such that

\[
\boxed{
e(Y_n)\to0,}
\qquad
\boxed{
\liminf_n h_\eta(Y_n)
\ge
\liminf_n h_\eta(W_n).
}
\tag{19}
\]

Thus an envelope-achieving sequence for `beta_eta` cannot gain exposure merely by splitting into asymptotically decoupled physical profiles. The split can be discarded by passing to one component.

## 3. The triangular notch has the same inverse-square remote-decoupling scale

`ANF-104` already gives the source-side estimate. With

\[
\mathfrak M_1(X)
:=\sum_{z\in X}e^{2\pi|\operatorname{Im}z|}
\tag{20}
\]

and horizontal gap

\[
R(A,B)
:=\min_{a\in A,b\in B}
|\operatorname{Re}a-\operatorname{Re}b|,
\tag{21}
\]

that finding proves, for `R(A,B)>=1`,

\[
|\mathcal C_{J_0}(A,B)|
\le
\frac{\kappa^2}{R(A,B)^2}
\mathfrak M_1(A)\mathfrak M_1(B),
\tag{22}
\]

where `kappa` is the explicit Montgomery--Taylor constant of `ANF-104`.

The fixed triangular notch admits a parallel estimate with no additional analysis input. With the Fourier convention used by the exponential sums,

\[
\widehat{\phi_\eta}(z)
=
 b_\eta\eta
\left(
\frac{\sin(\pi\eta z)}{\pi\eta z}
\right)^2,
\tag{23}
\]

with the removable value at `z=0`. Since

\[
|\sin(\pi\eta z)|
\le e^{\pi\eta|\operatorname{Im}z|},
\tag{24}
\]

for `|\operatorname{Re}z|>=R>0`,

\[
|\widehat{\phi_\eta}(z)|
\le
\frac{b_\eta}{\pi^2\eta R^2}
 e^{2\pi\eta|\operatorname{Im}z|}.
\tag{25}
\]

Therefore, defining

\[
\mathfrak M_\eta(X)
:=\sum_{z\in X}e^{2\pi\eta|\operatorname{Im}z|},
\tag{26}
\]

direct expansion of the cross term gives

\[
\boxed{
|\mathcal C_{\phi_\eta}(A,B)|
\le
\frac{b_\eta}{\pi^2\eta R(A,B)^2}
\mathfrak M_\eta(A)\mathfrak M_\eta(B).
}
\tag{27}
\]

Because `0<eta<1`, `mathfrak M_eta(X)<=mathfrak M_1(X)`. Hence the **same endpoint exponential mass** used by `ANF-104` controls both quadratic forms relevant to the fixed-notch envelope.

For a partition (3) whose distinct components satisfy `R_{ij}:=R(X_i,X_j)>=1`, define the aggregate endpoint interaction budget

\[
\mathcal Q(W;\{X_j\})
:=
\frac2L
\sum_{i<j}
\frac{\mathfrak M_1(X_i)\mathfrak M_1(X_j)}{R_{ij}^2}.
\tag{28}
\]

Then (22) and (27) imply

\[
\boxed{
\delta_0\le\kappa^2\mathcal Q,
\qquad
\delta_\eta
\le
\frac{b_\eta}{\pi^2\eta}\mathcal Q.
}
\tag{29}
\]

Combining (15)--(16) with (29) gives a fully geometric sufficient condition: if a near-extremal sequence admits any physical profile partition with

\[
\mathcal Q_n\to0,
\tag{30}
\]

then one component is itself a near-extremizer and retains the limiting fixed-notch exposure.

## 4. Superlinear diameter caused by profile fragmentation is not a new obstruction

There is a simple control showing why this distinction matters. If `A` and `B` are two fixed finite physical configurations and `B+T` denotes horizontal translation by a real number `T`, then

\[
S_{B+T}(\alpha)=e^{-2\pi i\alpha T}S_B(\alpha).
\tag{31}
\]

Both cross terms are Fourier transforms of compactly supported `L^1` functions evaluated at `T`, so the Riemann--Lebesgue lemma gives

\[
\mathcal C_{J_0}(A,B+T)\to0,
\qquad
\mathcal C_{\phi_\eta}(A,B+T)\to0
\qquad(|T|\to\infty).
\tag{32}
\]

Thus one can inflate horizontal diameter arbitrarily by translating already-existing near-extremal components far apart while asymptotically preserving both the source ratio and the notch exposure as affine-weighted mixtures. Repeating the operation produces configurations with very large or superlinear span without creating a new exposure mechanism. Equations (15)--(19) formalize the converse statement needed for the envelope: any such decoupled fragmentation can be localized back to a component with no loss in the limiting obstruction.

This prevents the `D_n/N_n->infinity` branch left by `ANF-101` from being treated as a single phenomenon. A large diameter can arise from mere translation dichotomy, which is harmless for `beta_eta`, or from a genuinely interacting diffuse geometry, which is not. The correct discriminator is the aggregate interaction budget, not the diameter itself.

## 5. Adversarial controls

The absolute values in (6) and the aggregate sum in (28) are essential. Small **signed total** source interaction is not enough: different profile pairs can cancel in the source form while retaining a large notch interaction, and with a growing number of profiles individually small pair interactions can accumulate to a macroscopic total. Likewise, pairwise gaps tending to infinity do not by themselves imply (30) when endpoint masses or the number of interacting pairs grow. The theorem deliberately asks for the norm-matched aggregate budget.

The fiber-complete partition condition is also load-bearing. Splitting copies of one real support site can destroy the additivity of `L=2|W|-sigma(W)` and hence invalidate (7). There is no such issue for an honest spatial cluster decomposition that keeps each real-part fiber intact.

Finally, the localization conclusion does not assert geometric compactness of the selected component. The component may still have growing cardinality, a source-heavy high tail, or its own superlinear internal span. The theorem is recursive rather than terminal: if the selected component itself admits a decoupled profile split, apply the same localization again. What cannot survive indefinitely as an explanation is exposure generated only by orthogonal juxtaposition.

A direct falsification test for the finite lemma is therefore clear. One would need a fiber-complete partition with small `e(W)`, `delta_0`, and `delta_eta` but with every component either having source excess larger than the right side of (15) or notch exposure below (16). Equations (7)--(13) rule this out algebraically, independently of any geometric kernel estimate.

## 6. Prior-art boundary and research consequence

A targeted literature audit against concentration--compactness dichotomy and translation-profile decompositions confirms that loss of compactness by widely separated pieces is a classical general phenomenon. Those frameworks motivate the language of profiles, but no external compactness theorem is load-bearing here: (7)--(19) are a finite exact consequence of the Montgomery--Taylor affine floor and the domination `phi_eta<=J_0`, while (23)--(29) use the explicit line-specific kernels already fixed in this program. No `SOURCES.md` update is required.

The frontier after `ANF-103`--`ANF-105` is therefore sharper. A sparse remote component must be source-heavy and endpoint-coupled to the core; an arbitrary many-profile superlinear configuration that is endpoint-decoupled can be collapsed to one equally dangerous near-extremal profile; and only a **genuinely coupled superlinear bulk**, a coupled source-heavy tail, or a nonconvex tight linear-span component can still control `beta_eta`.

This does not prove `beta_eta<B_eta`, improve the simple-critical-zero proportion, or establish RH. It removes a fake source of noncompactness from the decisive test of `ANF-099`. A positive continuation would now show that every superlinear near-extremizer either admits a partition with `mathcal Q=o(1)` or pays an endpoint-coupling cost incompatible with near-extremality. A negative continuation would construct a physical sequence with `e->0`, exposure reaching `B_eta`, and no profile partition whose aggregate source/notch interaction vanishes.