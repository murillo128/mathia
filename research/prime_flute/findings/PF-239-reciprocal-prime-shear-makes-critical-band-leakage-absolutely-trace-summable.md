# PF-239 — reciprocal-prime shear makes critical-band leakage absolutely trace summable

**Status:** `EXACT-DERIVED + RESOLVENT-STABILITY + TRACE-CLASS-ERROR + POSITIVE/ROUTE-NARROWING`. PF-238 closes the complete-lift dressed transfer gate for the exact PF-233 **diagonal** corridor, but leaves PF-232's hypercycle-straightening shear outside the normalized inverse. The first question is therefore whether the shear must preserve the full `sqrt(w_1w_2)/s` mode-by-mode envelope in order for the weak-trace program to survive.

It does not need to do so on the critical transverse band.

PF-232 gives a multiplicative energy-form comparison between the sheared and diagonal corridor with relative error

\[
\beta_n:=\max(\sinh\rho_n,\sinh\rho_{n+1})=O(P_n^{-1}).
\]

After congruence by **any fixed positive boundary seam normalizer**, in particular PF-238's actual complete-lift seam form, operator monotonicity of the resolvent implies that the corresponding normalized Schur factors differ in operator norm by at most `O(beta_n)`. PF-233 simultaneously gives only `O(s_n^{-1})` transverse modes in every fixed scaled band. Hence every part of the shear correction with at least one leg in such a band is finite rank with trace norm

\[
O\!\left(\frac{\beta_n}{s_n}\right).
\]

Multiplying by the reciprocal-prime commutator weight from PF-221/PF-222,

\[
\delta_n=P_n^{-1}-P_{n+1}^{-1},
\]

and using the canonical corridor scale

\[
s_n\asymp \frac{g_n+g_{n+1}}{P_n},
\]

gives

\[
\boxed{
\delta_n\frac{\beta_n}{s_n}
\lesssim \frac1{P_nP_{n+1}}
\lesssim \frac1{P_n^2}.
}
\]

Therefore these critical-band and low/high mode-mixing shear corrections are **absolutely summable in trace norm**. They do not need orthogonal cut supports, weak-ideal counting, or the PF-238 `w/s` gain to be harmless. The only shear-specific piece that still needs a genuine boundary-to-boundary smoothing theorem is the **high-high block**, where neither side meets a fixed PF-233 scaled band.

This is not a full sheared-corridor theorem and does not close the accepted weak-trace clue. It sharply reduces the open gate: failure of the smooth route can no longer come merely from `O(P_n^{-1})` mode mixing involving the critical population. A remaining shear obstruction must survive entirely in the high transverse tail, or appear later in physical `P/H` recoupling, finite-pant completion, neighboring-cell extension, or nested global reassembly.

## Claim

Fix one canonical neighboring-cuff corridor and suppress the index `n`. Let

\[
\Lambda_0
\]

be PF-233's diagonal variable-width energy DtN form and let

\[
\Lambda_1
\]

be PF-232's exact hypercycle-straightened energy DtN form on the same pulled-back two-boundary trace space. Put

\[
\beta=\max(\sinh\rho_1,\sinh\rho_2).
\]

PF-232 proves, for `0<beta<1`,

\[
(1-\beta)\Lambda_0
\le_{\rm form}
\Lambda_1
\le_{\rm form}
(1+\beta+\beta^2)\Lambda_0.
\tag{1}
\]

Let `Q=diag(Q_1,Q_2)>0` be any fixed positive seam form for which the normalized operators are defined, and set

\[
K_j=Q^{-1/2}\Lambda_jQ^{-1/2},
\qquad
D_j=(I+K_j)^{-1},
\qquad j=0,1.
\tag{2}
\]

Then

\[
\boxed{
\|D_1-D_0\|
\le
\varepsilon(\beta)
\le \beta,
}
\tag{3}
\]

where

\[
\varepsilon(\beta)
:=\max\left\{
\frac{\beta}{(1+\sqrt{1-\beta})^2},
\frac{\beta+\beta^2}{(1+\sqrt{1+\beta+\beta^2})^2}
\right\}.
\tag{4}
\]

In particular, for the off-diagonal boundary block

\[
\Delta_{21}:=(D_1-D_0)_{21},
\]

one has

\[
\boxed{\|\Delta_{21}\|\le\beta.}
\tag{5}
\]

Now use PF-233's transverse operator `K_a=T_a^{1/2}` and, for fixed `Z>0`, let

\[
\Pi_Z:=\mathbf 1_{[0,Z]}(K_a).
\tag{6}
\]

PF-233 gives uniform canonical-tail constants `c_0>0` and

\[
\lambda_m(K_a)\ge \sqrt{c_0}\,s(m+\alpha),
\qquad
\alpha=\frac{1+\sqrt5}{2},
\tag{7}
\]

so

\[
\boxed{
N_Z:=\operatorname{rank}\Pi_Z
\le 1+\frac{Z}{\sqrt{c_0}\,s}
=O_Z(s^{-1}).
}
\tag{8}
\]

Define the part of the shear correction that touches this fixed scaled band by

\[
L_Z
:=\Delta_{21}-(I-\Pi_Z)\Delta_{21}(I-\Pi_Z).
\tag{9}
\]

Then `L_Z` is trace class and

\[
\boxed{
\|L_Z\|_1
\le 2N_Z\,\|\Delta_{21}\|
\le C_Z\frac{\beta}{s}.
}
\tag{10}
\]

For the canonical prime-flute family, write `P_n` for the prime-scale parameter, `g_n=P_{n+1}-P_n`, and

\[
\delta_n=P_n^{-1}-P_{n+1}^{-1}
=\frac{g_n}{P_nP_{n+1}}.
\tag{11}
\]

PF-205/PF-232 give `beta_n<=C/P_n` on the tail, while PF-228 gives

\[
s_n\asymp\frac{g_n+g_{n+1}}{P_n}.
\tag{12}
\]

Consequently

\[
\boxed{
\delta_n\|L_{n,Z}\|_1
\le
C_Z\delta_n\frac{\beta_n}{s_n}
\le
\frac{C_Z}{P_nP_{n+1}}
\le
\frac{C_Z}{P_n^2}.
}
\tag{13}
\]

Hence

\[
\boxed{
\sum_n\delta_n\|L_{n,Z}\|_1<\infty.
}
\tag{14}
\]

The conclusion is absolute trace-norm summability. It remains valid if a later exact global identity sandwiches each `L_{n,Z}` between uniformly bounded operators, and therefore does not require orthogonality of the nested PF-222 cuts.

## 1. Multiplicative form control gives a uniform normalized-resolvent bound

Congruence of (1) by `Q^{-1/2}` preserves form order:

\[
(1-\beta)K_0
\le K_1
\le(1+\beta+\beta^2)K_0.
\tag{15}
\]

The function

\[
f(x)=\frac1{1+x}
\]

is operator monotone decreasing on positive self-adjoint operators. Thus

\[
\boxed{
(I+(1+\beta+\beta^2)K_0)^{-1}
\le D_1\le
(I+(1-\beta)K_0)^{-1}.
}
\tag{16}
\]

Since `D_0=(I+K_0)^{-1}`, the upper scalar gap is

\[
\frac1{1+(1-\beta)x}-\frac1{1+x}
=
\frac{\beta x}{(1+(1-\beta)x)(1+x)},
\tag{17}
\]

whose maximum on `x>=0` is

\[
\frac{\beta}{(1+\sqrt{1-\beta})^2}.
\tag{18}
\]

The lower scalar gap is

\[
\frac1{1+x}-\frac1{1+(1+\beta+\beta^2)x}
=
\frac{(\beta+\beta^2)x}
{(1+x)(1+(1+\beta+\beta^2)x)},
\tag{19}
\]

with maximum

\[
\frac{\beta+\beta^2}
{(1+\sqrt{1+\beta+\beta^2})^2}.
\tag{20}
\]

The two operator inequalities in (16) therefore bracket the self-adjoint difference `D_1-D_0` between positive functions of `K_0`, proving (3)--(4). Both scalar maxima are at most `beta` for `0<beta<1`, which gives the simple bound used below.

This step is deliberately independent of the detailed seam spectrum. The same `Q` is used on both corridors, so the PF-232 multiplicative error survives normalization without a factor such as `Q^{-1}` or `w^{-1}`. In particular it applies to PF-238's complete-lift actual seam form after the common exact boundary transport.

## 2. Every correction touching the critical band is finite-rank at cost `O(beta/s)`

Let `P=Pi_Z`. Algebraically,

\[
L_Z
=P\Delta_{21}+(I-P)\Delta_{21}P.
\tag{21}
\]

Each term has rank at most `N_Z`. The elementary finite-rank estimate

\[
\|T\|_1\le \operatorname{rank}(T)\,\|T\|
\tag{22}
\]

and (5) therefore give

\[
\|L_Z\|_1
\le
N_Z\|P\Delta_{21}\|
+N_Z\|(I-P)\Delta_{21}P\|
\le2N_Z\beta.
\tag{23}
\]

Using (8) proves (10).

The decomposition is stronger than a low-low estimate. It includes

\[
P\Delta P,
\qquad
P\Delta(I-P),
\qquad
(I-P)\Delta P.
\]

Thus arbitrary shear-induced mixing between a critical mode and a high mode is already inside the trace-class error. Only

\[
\boxed{
H_Z:=(I-P)\Delta_{21}(I-P)
}
\tag{24}
\]

remains outside the argument.

## 3. Reciprocal-prime smallness upgrades the finite-band error to strong trace class

Using (11)--(12) and `beta_n<=C/P_n`,

\[
\begin{aligned}
\delta_n\frac{\beta_n}{s_n}
&\le
C\frac{g_n}{P_nP_{n+1}}
\frac1{P_n}
\frac{P_n}{g_n+g_{n+1}}\\
&=
C\frac{g_n}{g_n+g_{n+1}}
\frac1{P_nP_{n+1}}\\
&\le
\frac{C}{P_nP_{n+1}}.
\end{aligned}
\tag{25}
\]

No prime number theorem, gap lower bound, or average-gap estimate is needed. Since the primes are a subset of the positive integers,

\[
\sum_n\frac1{P_n^2}<\infty,
\tag{26}
\]

and (14) follows.

This is a different arithmetic currency from PF-238's main diagonal transfer. PF-238 needs the dressed ratio `w/s` because its baseline crossing is the actual signal one hopes to keep at the weak endpoint. The **shear correction** already carries the extra small factor `beta=O(P^{-1})`. Once one leg is confined to the `O(s^{-1})` critical population, that factor is enough to make the reciprocal-prime weighted family strongly trace summable even if the correction loses the entire `w/s` amplitude gain there.

## 4. Prior-art and novelty audit

The functional-analytic ingredients are classical. Variational Dirichlet-to-Neumann operators from closed positive forms and their resolvent relations are standard; Olaf Post, *Boundary pairs associated with quadratic forms*, Math. Nachr. 289 (2016), 1052--1099, DOI `10.1002/mana.201500048`, is already used as background in PF-232. Continuous dependence and resolvent convergence for divergence-form Dirichlet-to-Neumann operators are also part of the established literature; see A. F. M. ter Elst, G. Gordon, and M. Waurick, *The Dirichlet-to-Neumann operator for divergence form problems*, Ann. Mat. Pura Appl. 198 (2019), DOI `10.1007/s10231-018-0768-2`, arXiv `1707.05734`. The finite-rank inequality (22), Schatten ideal property, and operator monotonicity of `(1+x)^{-1}` are standard operator theory.

A structure-directed search for quadratic-form/DtN perturbation estimates and Schatten consequences did not identify a theorem with the PF-specific conclusion (13)--(14). No novelty is claimed for form perturbation or finite-rank compression. The project-specific mathematical delta is the combination of three independently established canonical scales: PF-232's `beta_n=O(P_n^{-1})`, PF-233's `O(s_n^{-1})` fixed-scaled-band rank, and PF-221/PF-222's reciprocal-prime difference `delta_n`. Their product is `O(P_n^{-2})`, which changes what the sheared-corridor gate actually has to prove.

No external theorem is imported as a nontrivial black box in (1)--(14); the proof uses the persisted PF comparisons plus elementary spectral calculus and trace-norm inequalities.

## 5. Falsification and boundary checks

1. **No full shear envelope.** Equation (3) is an operator-norm perturbation bound. It does not imply PF-238's `F(sm)` singular-value envelope for the complete shear correction.
2. **Only low-touch trace class.** The high-high block `H_Z` in (24) can have infinite rank. Form-smallness alone gives only `\|H_Z\|<=beta`; it does not make `H_Z` trace class or weak trace class.
3. **The band is the PF-233 transverse band.** `Pi_Z` is a spectral projection of the diagonal-corridor `K_a`, not the later physical `P/H` split. The result nevertheless covers arbitrary mixing whenever at least one side lies in this canonical fixed scaled band.
4. **Same seam normalizer on both sides of the comparison.** The proof compares diagonal versus sheared corridor while keeping the actual PF-238 complete-lift seam form fixed. It does not compare different seam normalizers.
5. **Common boundary representation is required.** PF-232's DtN comparison is made after the exact graph straightening; PF-235/PF-238's common boundary transport may be applied to both corridor forms, and congruence preserves (1). No claim is made under unrelated boundary identifications.
6. **Finite head is irrelevant.** The canonical estimates `beta_n<1`, uniform `c_0`, and (12) are tail statements. Finitely many initial corridors contribute a finite-rank/trace-class correction and do not affect (14).
7. **No global identity is asserted.** Absolute trace summability means this error would survive arbitrary uniformly bounded left/right factors in a later exact reassembly. PF-239 does not prove that the full prime/shift relative resolvent has already been decomposed into precisely these local blocks.
8. Physical `P/H` recoupling, finite-pant completion, neighboring-cell coupling, PF-222's remaining nested high-tail reassembly, wave operators, determinants/resonances, prime/clone separation, zeta zeros, and RH remain outside the result.

## Consequences for the research line

PF-238 asked whether PF-232's reciprocal-prime-small shear can be inserted without losing the full diagonal `F(sm)` envelope. PF-239 shows that this target was stronger than necessary on the entire critical population. **Any shear damage that touches a fixed PF-233 scaled band is already a strongly trace-summable reciprocal-prime error**, even if it loses the `w/s` gain completely.

The next local shear theorem should therefore isolate only the high-high block (24). A positive route is to prove separated-boundary smoothing or an off-diagonal Poisson/Green estimate for the exact PF-232 sheared form that forces sufficient decay when both transverse legs satisfy `K_a>Z`. A decisive negative route must exhibit a canonical high-high mechanism that defeats such decay. Re-proving low-band `w/s` stability, or treating generic critical-band mode mixing as the obstruction, is now stale.

If the high-high shear tail is controlled, the local frontier moves to the physical `P/H` split and finite-pant completion before the genuinely nested PF-222 global reassembly becomes the remaining smooth-route gate.