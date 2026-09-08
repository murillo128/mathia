# ANF-127 — exponential digit clouds evacuate one saddle and regenerate source in another

**Status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + EXPONENTIAL-TRANSLATION-CLOUD + SAME-SADDLE-COHERENT-TAIL-RESURRECTION + NEW-SPECTRAL-CHAMBER + SUBEXPONENTIAL-BUDGET-SHARPNESS`. `ANF-122` shows that same-saddle translation mirrors collapse to global excision in its controlled growth regime, and `ANF-126` extends that conclusion to arbitrary growing translated `ANF-115` aggregates provided their unsigned Hilbert budget is subexponential in the height parameter `A`. The remaining exponential-budget boundary is real, not a technical artifact of the moderate-deviation estimate.

For every fixed `ANF-115` packet family and for **every prescribed positive exponential budget rate** `rho>0`, there is an explicit positive physical cloud of translated copies, all with exactly the same individual saddle, whose unsigned budget satisfies

\[
\frac1A\log \mathcal U_A\longrightarrow \rho,
\]

while the aggregate source norm on every shrinking macroscopic chamber around the original saddle is superexponentially small relative to one packet. Nevertheless the same aggregate has exponentially *larger* Montgomery--Taylor source mass in a second fixed spectral chamber. Thus exponentially many coherent copies can resurrect the exponentially small tail of each constituent and turn it into the dominant source reservoir after cancelling the original saddle.

The construction uses only a finite root-of-unity digit product. It shows that the hypothesis `log \mathcal U_A=o(A)` in `ANF-126` is sharp at the level of scale: it cannot be replaced by `log \mathcal U_A=O(A)` with any universal positive rate, however small. What remains open is no longer whether a same-saddle exponential cloud can escape excision; it can. The unresolved near-extremizer problem is whether the newly created chamber can itself be cancelled and transported again while the complete affine/source bookkeeping stays at bounded mass.

## 1. A distinct positive q-ary cloud with an exact modulation product

Fix `gamma>0` and let

\[
P_A:=P_{A,\lfloor\gamma A\rfloor}
\]

be the `ANF-115` packet. Write

\[
E_A:=E_0(P_A),
\qquad
m_A:=|P_A|,
\qquad
 a:=a_\gamma,
\qquad
f:=f_\gamma=F_\gamma(a),
\]

where

\[
F_\gamma(\alpha)
=\alpha+2\gamma\log\cos\frac{\pi\alpha}{2},
\qquad
F_\gamma'(a)=0,
\qquad
F_\gamma''(a)<0.
\tag{1}
\]

Thus

\[
\frac1A\log\frac{E_A}{m_A^2}\longrightarrow f.
\tag{2}
\]

Fix any target budget rate `rho>0`. Choose an integer `q>=2`, to be made large below, and define the one-sided root-of-unity sum

\[
D_q(x):=\sum_{v=0}^{q-1}e^{-2\pi i v x}.
\tag{3}
\]

Set

\[
d_q:=\frac{q-1}{qa},
\qquad
\beta_q:=\frac1{d_q}=\frac{qa}{q-1}.
\tag{4}
\]

For all sufficiently large fixed `q`, `beta_q<1`. The two distinguished phases satisfy

\[
 a d_q=\frac{q-1}{q},
\qquad
\beta_qd_q=1,
\]

and therefore

\[
\boxed{D_q(ad_q)=0,\qquad |D_q(\beta_qd_q)|=q.}
\tag{5}
\]

Let

\[
r_A:=\left\lfloor\frac{\rho A}{\log q}\right\rfloor.
\tag{6}
\]

For each `A`, choose positive real numbers `d_{1,A},\ldots,d_{r_A,A}` satisfying

\[
|d_{\ell,A}-d_q|\le A^{-4}
\tag{7}
\]

and such that all numbers

\[
x+\sum_{\ell=1}^{r_A}v_\ell d_{\ell,A},
\qquad
x\in X_A,\quad
v_\ell\in\{0,\ldots,q-1\},
\tag{8}
\]

are distinct, where `X_A` is the finite set of horizontal centers of `P_A`. Such a choice exists inductively: once the first `ell-1` steps have been chosen, each collision involving the new digit with different `v_ell` excludes only one value of `d_{ell,A}`, and there are only finitely many collisions to avoid. Every interval in (7) therefore contains an admissible choice.

For a digit vector `v=(v_1,...,v_{r_A})`, put

\[
\tau_v:=\sum_{\ell=1}^{r_A}v_\ell d_{\ell,A}
\]

and form the physical multiset

\[
T_A:=\bigsqcup_{v\in\{0,\ldots,q-1\}^{r_A}}(P_A+\tau_v).
\tag{9}
\]

By (8) the translated packets are disjoint. Their number is

\[
R_A=q^{r_A},
\qquad
\boxed{\frac1A\log R_A\longrightarrow\rho.}
\tag{10}
\]

Every constituent has the same source energy `E_A` and the same saddle `a`. Hence the unsigned Hilbert budget in the normalization of `ANF-126` is exactly

\[
\boxed{\mathcal U_A=R_A.}
\tag{11}
\]

The entire cloud still has only linear horizontal span:

\[
D_x(T_A)
\le D_x(P_A)+(q-1)\sum_{\ell=1}^{r_A}d_{\ell,A}
=O_{\gamma,\rho,q}(A).
\tag{12}
\]

Most importantly, translation gives the exact factorization

\[
S_{T_A}(\alpha)
=p_A(\alpha)S_{P_A}(\alpha),
\qquad
\boxed{
p_A(\alpha)
=\prod_{\ell=1}^{r_A}D_q(\alpha d_{\ell,A}).
}
\tag{13}
\]

Thus the exponential cloud is controlled by one finite digit product, with no signed coefficients and no nonphysical weighting.

## 2. The original saddle is evacuated on every shrinking macroscopic chamber

Let `S_A` be any positive sequence with

\[
\frac{S_A}{\sqrt A}\longrightarrow0
\]

and define the two-sided chamber

\[
B_A(S_A)
:=
\left\{
\alpha\in[-1,1]:
\bigl||\alpha|-a\bigr|
\le\frac{S_A}{\sqrt A}
\right\}.
\tag{14}
\]

The zero of `D_q` at `(q-1)/q` is simple. Since `q` is fixed, (5) and (7) imply uniformly on `B_A(S_A)`

\[
|D_q(\alpha d_{\ell,A})|
\le
C_q\left(\frac{S_A}{\sqrt A}+A^{-4}\right).
\tag{15}
\]

The same estimate holds at the negative saddle by conjugation. Using (13),

\[
\sup_{\alpha\in B_A(S_A)}|p_A(\alpha)|^2
\le
\left[
C_q^2\left(\frac{S_A}{\sqrt A}+A^{-4}\right)^2
\right]^{r_A}.
\tag{16}
\]

Since `r_A/A -> rho/log q>0` while the bracket tends to zero,

\[
\boxed{
\frac1A
\log
\sup_{\alpha\in B_A(S_A)}|p_A(\alpha)|^2
\longrightarrow-\infty.
}
\tag{17}
\]

Consequently, without using any asymptotic description of the base packet inside the chamber,

\[
\frac{E_{B_A(S_A)}(T_A)}{E_A}
\le
\sup_{B_A(S_A)}|p_A|^2
\frac{E_{B_A(S_A)}(P_A)}{E_A}
\le
\sup_{B_A(S_A)}|p_A|^2,
\]

so

\[
\boxed{
\frac1A\log
\frac{E_{B_A(S_A)}(T_A)}{E_A}
\longrightarrow-\infty.
}
\tag{18}
\]

This is much stronger than the local mirror condition used in `ANF-126`: the entire same-saddle aggregate becomes superexponentially small on every chamber whose physical width tends to zero, even though its unsigned source budget has the positive exponential rate `rho`.

## 3. Coherent tails regenerate an exponentially larger source chamber

The cancellation in (18) does **not** make the aggregate source-negligible. The cloud factors are maximally aligned at the second frequency `beta_q` from (4). Define the large-deviation gap of the base packet there by

\[
\boxed{
I_q:=f-F_\gamma(\beta_q)>0.
}
\tag{19}
\]

Because `beta_q -> a` as `q->infinity`, Taylor expansion at the strict saddle gives

\[
I_q
=
\frac{c_\gamma}{2}
\left(\frac{a}{q-1}\right)^2
+O_\gamma(q^{-3}),
\qquad
c_\gamma:=-F_\gamma''(a)>0.
\tag{20}
\]

In particular `I_q->0`. We may therefore choose the fixed integer `q` above so large that

\[
\boxed{I_q<\rho}
\tag{21}
\]

while still having `beta_q<1`.

Take a fixed `c>0` small enough that

\[
C_A
:=
\left\{
\alpha:
\bigl||\alpha|-\beta_q\bigr|
\le\frac cA
\right\}
\subset(-1,1).
\tag{22}
\]

For `alpha` in this window, (7) gives

\[
\alpha d_{\ell,A}=\pm1+O_{q,c}(A^{-1}).
\]

The geometric sum has a nondegenerate maximum at each integer, hence

\[
|D_q(\alpha d_{\ell,A})|
\ge q\exp(-C_qA^{-2})
\]

for all large `A`. Multiplying `r_A=O(A)` factors yields

\[
\boxed{
|p_A(\alpha)|^2
\ge R_A^2e^{-o(A)}
\qquad(\alpha\in C_A).
}
\tag{23}
\]

On the same fixed interior frequency, the exact `ANF-115` product formula gives uniformly on the `A^{-1}` window

\[
J_0(\alpha)|S_{P_A}(\alpha)|^2
=
m_A^2\exp\left(A F_\gamma(\beta_q)+o(A)\right),
\tag{24}
\]

with a positive prefactor because `J_0(\beta_q)>0`. Integrating (23)--(24) over (22) and comparing with (2) gives

\[
\boxed{
\liminf_{A\to\infty}
\frac1A\log
\frac{E_{C_A}(T_A)}{E_A}
\ge
2\rho-I_q
>
\rho>0.
}
\tag{25}
\]

Therefore

\[
\boxed{
\frac{E_0(T_A)}{E_A}
\ge
\exp((\rho+o(1))A)
\longrightarrow\infty,
}
\tag{26}
\]

while (18) says the same aggregate is invisible on the original saddle chamber. Each constituent has exponentially little source at `beta_q`; `R_A` coherent copies align there with amplitude `R_A`, paying the individual large-deviation cost `I_q` with the quadratic gain `2\log R_A`. This is the exact mechanism by which an exponential same-saddle cloud manufactures a new spectral reservoir.

The rate comparison is also the natural continuation of `ANF-123`. The new chamber lies at the fixed distance

\[
\beta_q-a=rac{a}{q-1},
\]

and its individual-packet penalty is

\[
I_q
=
\frac{c_\gamma}{2}(\beta_q-a)^2+O((\beta_q-a)^3).
\tag{27}
\]

Thus source transfer becomes possible once the unsigned **norm** budget rate exceeds approximately one half of the relevant quadratic large-deviation rate. The exponential cost predicted there is therefore not only necessary in scale; a coherent positive translation cloud can actually spend that budget to resurrect the tail.

## 4. Consequence for the analytic-frontier gate

For this construction every constituent packet has exactly the same `gamma`, so the constituent saddle-displacement quantity `r_A` in `ANF-126` is identically zero. The only hypothesis of its chamber theorem that fails is

\[
\log\mathcal U_A=o(A).
\]

Yet the local mirror conclusion (18) holds in a form stronger than required while the global-excision conclusion fails maximally by (26). Since `rho>0` was arbitrary and `q` can be chosen after `rho`, there is no positive universal constant `rho_0` for which the theorem could be extended to all clouds satisfying

\[
\log\mathcal U_A\le \rho_0A+o(A).
\]

The **little-o boundary is sharp at exponential scale**.

This does not construct a fatal fixed-notch near-extremizer and does not settle `ANF-099`. In fact (26) makes the missing step explicit: the regenerated chamber is exponentially oversized relative to the original packet scale. A bounded-mass completion would need a second cancellation layer that removes this new reservoir without making the whole block excisable, possibly transferring the source again. The next concrete gate is therefore an exponential **cancellation cascade across spectral chambers**, not a refinement of same-chamber Gaussian conditioning.

The prior-art audit checked the classical finite geometric/root-of-unity sum underlying (3)--(5) and the neighboring language of finite/generalized Riesz products. Those literatures explain the elementary trigonometric product pattern but do not supply the Montgomery--Taylor source-budget statement, the physical translated-packet realization, or the sharp `log \mathcal U_A=o(A)` boundary above. No external theorem is load-bearing: the proof uses only the exact geometric-sum identity and the already internal `ANF-115` Laplace exponent. `SOURCES.md` therefore requires no update.

No clue disposition changes. In particular the accepted fixed-notch exposure-envelope clue remains an exact reduction; this finding only identifies a genuinely surviving exponential completion mechanism on the obstruction side.