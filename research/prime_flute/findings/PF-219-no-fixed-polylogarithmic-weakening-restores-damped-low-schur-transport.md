# PF-219 — no fixed polylogarithmic weakening restores damped low-Schur transport

**Status:** `EXACT-DERIVED + OPERATOR-THEORETIC + NEGATIVE/ROUTE-NARROWING`. PF-218 passes the PF-217 tangential-screening vectors through the exact identity

\[
B:=P(I+K)^{-1}P=S^{-1}
\]

and rules out a tail-uniform `q_n^{1/2}` damping factor at each low-symmetric endpoint together with summable module transport. That obstruction is substantially stronger than the raw `q_n` scale. For every fixed exponent `a\ge0`, even the weaker endpoint weight

\[
r_n=q_n(1+L_n)^a
\]

fails in the same sense, where `L_n` is the PF physical cuff length and `L_n\asymp\log P_n` on the tail. Equivalently, no fixed polylogarithmic loss in the raw strip currency can restore a summable scalar transport envelope for the exact low Schur inverse.

In particular, PF-216/PF-205 give `q_n\asymp d_nL_n`, so the first logarithmically weakened scale satisfies

\[
q_n(1+L_n)\asymp \frac{q_n^2}{d_n}.
\]

Therefore even allowing the inverse one full logarithmic factor more than PF-218 does **not** produce summable endpoint-damped transport. In coefficient-split form, there is no tail-uniform `\eta\in\ell^1` for which

\[
\sqrt{d_md_n}\,|\langle\nu_m,D\nu_n\rangle|
\le Cq_mq_n\,\eta_{m-n}.
\]

This does not refute PF-213's unweighted block-decay criterion and does not rule out the actual `d_n`-weighted recoupling words. It rules out a broader family of completion arguments that try to repair PF-218 merely by weakening the scalar endpoint damping by any fixed power of the logarithmic cuff scale. A successful smooth-interface proof must use more than a fixed polylogarithmic rescaling of the low Schur Green kernel: it must exploit the actual placement of the physical coefficient, additional low/high operator structure, or a genuinely different screened weight.

## Claim

Use PF-217/PF-218 notation. Let

\[
A=I+K\ge I,
\qquad D=A^{-1},
\qquad B=PDP=S^{-1}
\tag{1}
\]

on the low-symmetric space `P\mathcal B`, with orthonormal module vectors `\nu_n`. Let

\[
q_n=\langle\mathbf1_n,\Lambda_{Q,n}\mathbf1_n\rangle
\asymp \frac{\log P_n}{P_n}
\tag{2}
\]

and let `L_n` denote the physical distinguished-cuff length. PF-217 proves on every dyadic index block `N\le n\le2N` that

\[
L_n\asymp\log P_n\asymp\log P_N
\tag{3}
\]

with constants independent of `N` after a finite head.

For every fixed real `a\ge0`, define on finite low vectors

\[
W_a\nu_n
=\frac{1}{q_n(1+L_n)^a}\nu_n.
\tag{4}
\]

Let `E_N` be the projection onto `\nu_n`, `N\le n\le2N`, and `W_{a,N}=E_NW_aE_N`. Then the PF-217 screening vectors `x^{(N)}` force

\[
\boxed{
\left\|W_{a,N}^{1/2}E_NBE_NW_{a,N}^{1/2}\right\|
\ge
\frac{c_aN/(\log P_N)^a}
{1+\log N+NP_N^{-\delta}}
\longrightarrow\infty,
}
\tag{5}
\]

where `\delta>0` is the same fixed exponent available in PF-217 and constants may depend on the fixed `a` but not on `N`.

Consequently, for no fixed `a\ge0` do there exist tail constants `C,N_0` and a nonnegative `\eta\in\ell^1(\mathbb Z)` such that

\[
\boxed{
|\langle\nu_m,D\nu_n\rangle|
\le
C\sqrt{q_mq_n}
(1+L_m)^{a/2}(1+L_n)^{a/2}
\eta_{m-n}
}
\tag{6}
\]

for all `m,n\ge N_0`.

The case `a=0` is PF-218. The new content is that **every fixed polylogarithmic weakening `a>0` also fails**.

For `a=1`, the PF-205/PF-216 asymptotics

\[
q_n\asymp d_nL_n,
\qquad L_n\to\infty
\tag{7}
\]

give

\[
q_n(1+L_n)\asymp q_nL_n\asymp\frac{q_n^2}{d_n}.
\tag{8}
\]

Thus (6) with `a=1` is, up to uniform constants,

\[
|\langle\nu_m,D\nu_n\rangle|
\le
C\frac{q_m}{\sqrt{d_m}}
\frac{q_n}{\sqrt{d_n}}
\eta_{m-n},
\tag{9}
\]

which is impossible. Multiplying (9) by `\sqrt{d_md_n}` yields the equivalent coefficient-split obstruction

\[
\boxed{
\sqrt{d_md_n}\,|\langle\nu_m,D\nu_n\rangle|
\not\lesssim
q_mq_n\,\eta_{m-n}
\quad\text{for every }\eta\in\ell^1.
}
\tag{10}
\]

Equation (10) is only a scalar low-low compression statement. It is not an assertion about the complete PF recoupling operator, where the coefficient, Poisson factors, low/high projections, and module placement occur in a specific noncommutative order.

## 1. The PF-217 vectors retain macroscopic mass after every fixed polylog weakening

PF-217 constructs finite-support vectors

\[
x^{(N)}=\sum_{N\le n\le2N}x_n^{(N)}\nu_n
\tag{11}
\]

from tangential bumps and a slow discrete sine envelope. In its notation

\[
x_n^{(N)}=t_n\sqrt{q_n},
\qquad |t_n|\asymp|z_n|,
\qquad \sum_{N\le n\le2N}|z_n|^2\asymp N.
\tag{12}
\]

It also proves

\[
\mathfrak s_{\rm low}[x^{(N)}]
\le C\bigl(1+\log N+NP_N^{-\delta}\bigr).
\tag{13}
\]

Using (3), the `W_a` mass of the same vector is

\[
\begin{aligned}
m_a^{(N)}
&:=\langle x^{(N)},W_ax^{(N)}\rangle\\
&=\sum_{N\le n\le2N}
\frac{|t_n|^2}{(1+L_n)^a}\\
&\ge \frac{c_a}{(\log P_N)^a}
\sum_{N\le n\le2N}|z_n|^2\\
&\ge \boxed{\frac{c_aN}{(\log P_N)^a}}.
\end{aligned}
\tag{14}
\]

Thus the screening construction is not a phenomenon tied narrowly to the exact PF-216 mass weight. It beats that weight by enough polynomial-in-index room that any fixed power of the logarithmic cuff scale can be discarded and a divergent inverse test still remains.

## 2. Duality gives the weighted inverse blow-up

PF-218 proves the exact identity `B=S^{-1}` and the quadratic dual estimate

\[
\langle W_ax,BW_ax\rangle
\ge
\frac{\langle x,W_ax\rangle^2}
{\mathfrak s_{\rm low}[x]}
\tag{15}
\]

for every finitely supported low vector `x`; the proof uses only positivity and the variational definition of the short. Normalizing `W_{a,N}^{1/2}x^{(N)}` therefore gives

\[
\left\|W_{a,N}^{1/2}E_NBE_NW_{a,N}^{1/2}\right\|
\ge
\frac{m_a^{(N)}}{\mathfrak s_{\rm low}[x^{(N)}]}.
\tag{16}
\]

Insert (13)--(14) to obtain the displayed lower bound in (5).

It remains only to check divergence. The same classical nth-prime estimates already used in PF-217 give `P_N\asymp N\log N` up to fixed tail constants. Hence, for every fixed `a`,

\[
\frac{(\log P_N)^a(1+\log N)}{N}\longrightarrow0,
\qquad
(\log P_N)^aP_N^{-\delta}\longrightarrow0.
\tag{17}
\]

Both terms in the denominator of (5) are therefore `o(N/(\log P_N)^a)`, proving the divergence.

## 3. Summable transport would contradict the finite-block blow-up

If (6) held, then the scalar matrix of the conjugated operator would satisfy

\[
\left|
\left\langle\nu_m,
W_a^{1/2}BW_a^{1/2}\nu_n
\right\rangle
\right|
\le C\eta_{m-n}.
\tag{18}
\]

The Schur test bounds every finite tail compression by `C\|\eta\|_1`, uniformly in `N`. This contradicts (5). No pointwise lower bound on any particular entry is needed; as in PF-218, the obstruction is aggregate and may be carried by diagonal scale, coherent off-diagonal accumulation, or both.

The `a=1` specialization matters because the physical seam scale is logarithmically smaller than the raw strip constant-mode scale. Equations (7)--(10) show that **merely spending that one logarithm by allowing a larger scalar inverse weight does not repair the transport argument**. In fact (5)--(6) show that no fixed number of such logarithmic losses repairs it.

## Prior-art and novelty audit

Shorted positive operators, Schur complements, inverse-compression identities, quadratic duality, and the Schur test are classical. The same foundational references used in PF-218 apply: W. N. Anderson Jr., *Shorted Operators*, SIAM Journal on Applied Mathematics **20** (1971), 520--525, DOI `10.1137/0120053`, and W. N. Anderson Jr. with G. E. Trapp, *Shorted Operators. II*, SIAM Journal on Applied Mathematics **28** (1975), 60--71, DOI `10.1137/0128007`. A fresh structure-directed search again located the classical shorted-operator/Schur-complement literature and did not supply any theorem that changes the PF-specific calculation above. No novelty is claimed for the general operator-theoretic devices or for elementary domination of powers of logarithms by powers of the index.

The project-specific deduction is (5)--(10): the **canonical PF-217 screening family has enough quantitative room to destroy every fixed polylogarithmic endpoint damping refinement of the exact low Schur inverse**, including the first scale `q_n^2/d_n` suggested by the logarithmic separation between raw strip energy and physical seam coefficient. Search absence is not used as proof of novelty.

## Falsification and boundary checks

A later adversary should check that:

1. PF-217's `x_n=t_n\sqrt{q_n}` relation and dyadic-block comparison `L_n\asymp\log P_N` are used with uniform tail constants.
2. The dual inequality (15) is exactly the PF-218 argument with `W` replaced by the finite-block diagonal `W_a`; no global domain claim for the unbounded weight is needed.
3. Both limits in (17) hold for each **fixed** `a`; PF-219 does not permit `a=a_N` growing with the block.
4. The Schur-test contradiction in (18) requires `\eta\in\ell^1`; no conclusion is drawn about nonsummable kernels.
5. The `a=1` conversion uses only the persisted comparability `q_n\asymp d_nL_n` and `L_n\to\infty`.
6. Aggregate weighted blow-up is not misread as a pointwise lower bound, unweighted nonlocality, or noncompactness of `D`.
7. PF-213's unweighted sufficient envelope, the full `d_n`-weighted low/high recoupling word, PF-204's unsmoothed interface route, PF-183's true-short-collar splice, scattering/determinants, prime/clone separation, and RH remain outside the proved claim.

## Consequences for the research line

PF-218 already says that the low Schur inverse cannot recover the screened PF-216 mass by factoring `q_n^{1/2}` from each endpoint and asking the remaining propagation to be summable. PF-219 shows that this is **not a one-log mismatch**. Any attempt to rescue the same scalar-damping architecture by replacing `q_n` with `q_n(\log P_n)^a` for a fixed `a` still fails.

The smooth decomposition-interface route should therefore stop searching for a merely polylogarithmically weaker diagonal weight on `PDP`. The next useful calculation must keep the physical coefficient and operator placement intact, exploit additional tangential/low-high smoothing that disappears under scalar compression, or derive a genuinely different screened effective variable whose inverse is not just the PF-216 weight with fixed logarithmic slack. PF-204 and the PF-183 true-short-collar splice remain independent alternatives.