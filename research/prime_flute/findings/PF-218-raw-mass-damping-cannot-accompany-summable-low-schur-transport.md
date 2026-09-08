# PF-218 — raw-mass damping cannot accompany summable low Schur transport

**Status:** `EXACT-DERIVED + OPERATOR-THEORETIC + NEGATIVE/ROUTE-NARROWING`. PF-217 proves that tangential boundary screening destroys every fixed positive fraction of PF-216's raw constant-mode mass after the correct variational shorting. Passing that statement through the exact inverse relation for a positive short gives a direct restriction on the actual Schur factor

\[
D=(I+K)^{-1}.
\]

Let `P` be the PF-217 projection onto the low-symmetric module vectors `\nu_n`, let

\[
W\nu_n=q_n^{-1}\nu_n,
\]

and write `B=PDP|_{P\mathcal B}`. If `E_N` projects onto modules `N\le n\le2N`, then the finite-block weighted inverse norms satisfy

\[
\boxed{
\left\|W_N^{1/2}E_NBE_NW_N^{1/2}\right\|
\ge
\frac{cN}{1+\log N+NP_N^{-\delta}}
\longrightarrow\infty,
}
\]

where `W_N=E_NWE_N` and the same `\delta>0` as in PF-217 may be used after changing constants. Consequently there is no tail-uniform estimate

\[
B\lesssim W^{-1},
\]

and, more pointedly, there is no `\eta\in\ell^1(\mathbb Z)` and finite `C` for which the scalar low blocks obey

\[
\boxed{
|\langle\nu_m,D\nu_n\rangle|
\le
C\sqrt{q_mq_n}\,\eta_{m-n}
}
\]

through the whole tail. Thus one natural scale-sensitive completion of PF-217 is now ruled out: the Schur inverse cannot simultaneously contribute one factor `q_n^{1/2}` of raw PF-216 damping at each endpoint and retain summable module transport.

This does **not** refute PF-213's unweighted sufficient decay criterion, prove that `D` is nonlocal, or rule out a weaker coefficient-weighted transport estimate. The physical seam coefficient satisfies a much smaller `d_n` scale than the raw inverse mass `q_n^{-1}`. The live endpoint question is therefore correctly posed only after the physical `d_n` coefficient has been retained in the recoupling word, or after another effective screened weight has been derived from the shorted form itself.

## Claim

Use PF-214--PF-217 notation. Let

\[
A:=I+K\ge I,
\qquad
D=A^{-1},
\]

where `A` is represented by the closed form

\[
\mathfrak a[f]=\|f\|^2+\mathfrak k[f]
\]

on the normalized simultaneous-boundary space `\mathcal B`. Let `P` be the orthogonal projection onto the closed span of

\[
\nu_n=\frac{\Lambda_{Q,n}^{1/2}\mathbf1_n}{\sqrt{q_n}},
\qquad
q_n=\langle\mathbf1_n,\Lambda_{Q,n}\mathbf1_n\rangle,
\]

and put `Q=I-P`. The PF-217 low short is

\[
\mathfrak s_{\rm low}[x]
=
\inf_{y\in Q\operatorname{Dom}(\mathfrak a)}
\mathfrak a[x+y].
\tag{1}
\]

Let `S` be the positive self-adjoint operator on `P\mathcal B` associated with this closed form. Since `\mathfrak a[f]\ge\|f\|^2`,

\[
\mathfrak s_{\rm low}[x]\ge\|x\|^2,
\qquad
S\ge I.
\tag{2}
\]

Then the inverse of the short is exactly the low compression of the full Schur factor:

\[
\boxed{
S^{-1}=PDP|_{P\mathcal B}=:B.
}
\tag{3}
\]

Define on the algebraic span of the `\nu_n`

\[
W\nu_n=q_n^{-1}\nu_n,
\qquad
\mathfrak m_0[x]=\langle x,Wx\rangle.
\tag{4}
\]

For the tail block projection

\[
E_N=\sum_{N\le n\le2N}|\nu_n\rangle\langle\nu_n|,
\qquad
W_N=E_NWE_N,
\tag{5}
\]

PF-217 supplies vectors `x^{(N)}=E_Nx^{(N)}` and some `\delta>0` such that

\[
\mathfrak m_0[x^{(N)}]\ge cN,
\qquad
\mathfrak s_{\rm low}[x^{(N)}]
\le C\bigl(1+\log N+NP_N^{-\delta}\bigr).
\tag{6}
\]

These vectors force

\[
\boxed{
\left\|W_N^{1/2}E_NBE_NW_N^{1/2}\right\|
\ge
\frac{\mathfrak m_0[x^{(N)}]}
{\mathfrak s_{\rm low}[x^{(N)}]}
\ge
\frac{cN}{1+\log N+NP_N^{-\delta}}.
}
\tag{7}
\]

Because `(1+\log N)/N\to0` and `P_N^{-\delta}\to0`, the right side diverges. Hence the raw-mass-conjugated low inverse is not uniformly bounded on tail blocks.

As a consequence, no tail constants `C<\infty`, `N_0`, and no nonnegative `\eta\in\ell^1(\mathbb Z)` can satisfy

\[
|B_{mn}|
:=|\langle\nu_m,D\nu_n\rangle|
\le C\sqrt{q_mq_n}\,\eta_{m-n}
\qquad(m,n\ge N_0).
\tag{8}
\]

Indeed (8) would make the matrix of `W^{1/2}BW^{1/2}` on the tail entrywise dominated by the convolution kernel `C\eta_{m-n}`. The Schur test would then give a uniform `\ell^2` operator bound `C\|\eta\|_1`, contradicting (7).

## 1. The inverse of the short is the compressed Schur inverse

Identity (3) can be proved directly at the form level, avoiding any bounded-block assumption on `K`. For `h\in P\mathcal B`, the standard quadratic dual formula for `A^{-1}` gives

\[
\langle h,Dh\rangle
=
\sup_{f\in\operatorname{Dom}(\mathfrak a)}
\left(2\operatorname{Re}\langle h,f\rangle-\mathfrak a[f]\right).
\tag{9}
\]

Write `f=x+y` with `x=Pf` and `y=Qf`. Because `h\in P\mathcal B`,

\[
\langle h,f\rangle=\langle h,x\rangle.
\]

Taking the supremum first over `y` is therefore the same as minimizing the energy at fixed `x`:

\[
\begin{aligned}
\langle h,Dh\rangle
&=
\sup_x
\left(
2\operatorname{Re}\langle h,x\rangle
-
\inf_y\mathfrak a[x+y]
\right)\\
&=
\sup_x
\left(
2\operatorname{Re}\langle h,x\rangle
-
\mathfrak s_{\rm low}[x]
\right)\\
&=
\langle h,S^{-1}h\rangle.
\end{aligned}
\tag{10}
\]

Thus `PDP` and `S^{-1}` have the same quadratic form on `P\mathcal B`, proving (3). This is the infinite-dimensional positive-form version of the familiar statement that the inverse of a Schur complement is the corresponding diagonal block of the inverse matrix.

## 2. PF-217 screening becomes a weighted inverse blow-up

For any nonzero finitely supported `x\in P\operatorname{Dom}(\mathfrak s_{\rm low})`, put

\[
m=\mathfrak m_0[x]=\langle x,Wx\rangle,
\qquad
h=Wx.
\tag{11}
\]

Since `S\ge I`, its inverse is bounded. The variational characterization of `S^{-1}` gives

\[
\langle h,S^{-1}h\rangle
=
\sup_{z\ne0}
\frac{|\langle h,z\rangle|^2}{\mathfrak s_{\rm low}[z]}
\ge
\frac{m^2}{\mathfrak s_{\rm low}[x]},
\tag{12}
\]

where the last step chooses `z=x`.

If `x=E_Nx`, then

\[
u=\frac{W_N^{1/2}x}{\sqrt m}
\]

is a unit vector in `E_NP\mathcal B`. Using (3),

\[
\begin{aligned}
\left\langle
u,
W_N^{1/2}E_NBE_NW_N^{1/2}\nu
\right\rangle
&=
\frac{\langle Wx,BWx\rangle}{m}\\
&\ge
\frac{m}{\mathfrak s_{\rm low}[x]}.
\end{aligned}
\tag{13}
\]

Insert the PF-217 vectors (6) to obtain (7). No new prime-gap estimate is needed: the divergence is exactly the dual operator manifestation of the already-established screening ratio.

## 3. A `q`-damped summable transport envelope is impossible

Equation (8) is a natural candidate after PF-216: perhaps shorting destroys raw coercivity but the inverse still gains one square root of the strip constant-mode energy `q_n` at each endpoint, with the remaining propagation controlled by a summable distance kernel. PF-218 rules out that entire class of estimates.

Under (8), the scalar matrix of the conjugated low inverse is

\[
\left|
\left\langle
\nu_m,
W^{1/2}BW^{1/2}\nu_n
\right\rangle
\right|
=
\frac{|B_{mn}|}{\sqrt{q_mq_n}}
\le C\eta_{m-n}.
\tag{14}
\]

Because `\eta\in\ell^1`, convolution by `\eta` is bounded on `\ell^2`, and the Schur test gives a tail-uniform bound for every finite compression. This contradicts (7).

The contradiction is aggregate. PF-218 does **not** prove that every diagonal entry `\langle\nu_n,D\nu_n\rangle` is larger than `Cq_n`, nor does it identify which distances carry the excess weighted norm. The blow-up may arise from diagonal scale, coherent off-diagonal accumulation, or both. Determining the actual screened Green kernel remains open.

## 4. Relation to PF-213 and the physical seam currency

PF-213 asks for enough module transport control to reassemble low-containing recoupling words in weak trace class. Its displayed sufficient hypothesis is an **unweighted** envelope for the full module blocks of `D`; PF-218 does not contradict that hypothesis. The new obstruction concerns a stronger but tempting scale-sensitive refinement in which the raw PF-216 strip weight `q_n` is factored from the inverse itself.

That distinction matters because the actual perturbation word also contains the physical metric coefficient from PF-205. On the prime tail,

\[
d_n\asymp P_n^{-1},
\qquad
q_n\asymp\frac{\log P_n}{P_n},
\tag{15}
\]

so the coefficient entering the resolvent comparison is smaller than the raw constant-mode strip currency by a logarithmic factor. PF-218 therefore says **where not to place the weight**: a successful endpoint proof cannot first demand `q`-damping from `D` and only afterwards multiply by `d_n`.

The live alternatives remain to estimate the coefficient-weighted blocks such as the actual PF-211/PF-213 recoupling words directly, or to derive a weaker screened weight from `\mathfrak s_{\rm low}` whose Green kernel and `d_n` interaction can be controlled. PF-204's unsmoothed mixed critical transport and PF-183's true-short-collar splice remain independent.

## Prior-art and novelty audit

Shorted positive operators and their relation to Schur complements are classical. The foundational references already audited in PF-217 are W. N. Anderson Jr., *Shorted Operators*, SIAM Journal on Applied Mathematics **20** (1971), 520--525, DOI `10.1137/0120053`, and W. N. Anderson Jr. with G. E. Trapp, *Shorted Operators. II*, SIAM Journal on Applied Mathematics **28** (1975), 60--71, DOI `10.1137/0128007`. A fresh structure-directed search again found this classical shorting/Schur-complement literature; no novelty is claimed for (3), the quadratic dual formula, or the Schur test.

The project-specific deduction is (7)--(8): **PF-217's canonical prime-flute screening vectors force the exact low compression of the simultaneous Schur inverse to be unbounded after conjugation by the raw PF-216 mass weight, and therefore exclude every tail-uniform `q`-damped summable transport envelope.** This is a restriction on the exact PF-205/PF-214 boundary operator, not a general theorem about block-Jacobi inverses.

## Falsification and boundary checks

A later adversary should check the following points.

1. Verify that `A=I+K\ge I` is the self-adjoint operator represented by the PF-217 closed form and that `D=A^{-1}` is the PF-214 Schur factor.
2. Reproduce the form-duality calculation (9)--(10), including the domain split `f=x+y`, to confirm `S^{-1}=PDP` without assuming bounded blocks of `K`.
3. Check that `W` is used only on finitely supported low vectors and through finite block compressions, so no unjustified global domain statement about the unbounded diagonal operator is needed.
4. Insert PF-217's exact estimates (6) into (13) and verify that the resulting lower bound diverges even when the `NP_N^{-\delta}` error dominates `\log N`.
5. Check the Schur-test implication from (8) to a uniform bound on the finite weighted compressions.
6. Do not infer from aggregate weighted blow-up that any particular diagonal block violates `O(q_n)`, or that a specific off-diagonal distance is large.
7. Do not infer failure of PF-213's unweighted sufficient envelope, failure of all coefficient-weighted transport, noncompactness of `D`, or failure of the smooth seam architecture.
8. Keep the physical `d_n` coefficient, the unsmoothed PF-204 route, the independent PF-183 true-short-collar splice, scattering/determinants, prime/clone separation, and RH outside the proved claim.

## Consequences for the research line

PF-215--PF-217 show that neither bounded raw hopping nor raw constant-mode coercivity survives as the simple route to Schur locality. PF-218 now moves that negative information through the actual inverse: **the screened low Schur factor cannot recover the lost coercivity by a tail-uniform `q_n^{1/2}` endpoint damping combined with summable index propagation.**

The next smooth-route calculation should therefore keep the physical perturbation scale present from the start. The useful target is a transport estimate for the actual coefficient-weighted recoupling operator, or an explicit screened effective form whose inverse can be analyzed in a weaker weight than the raw PF-216 currency. This is narrower than asking whether `D` is local in the abstract and avoids another completion strategy already excluded by the canonical screening vectors.