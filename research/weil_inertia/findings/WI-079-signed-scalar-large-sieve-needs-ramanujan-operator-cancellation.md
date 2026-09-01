# WI-079 — signed scalar large-sieve cancellation is a Ramanujan-operator problem, not an ordinary additive-energy input

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECTION`. This finding does **not** certify the Yang--Yang one-sided fourth-moment candidate and does not change Mathia's current unconditional simple-critical proportion. It sharpens the sign-sensitive escape deliberately left open by WI-078. If a scalar reduction of the centered Yang covariance produces real signed outer coefficients on ordinary modulus-level large-sieve blocks, then the published Baker--Munsch--Shparlinski scalar large-sieve interface cannot exploit those signs: its basic object is a sum of nonnegative squared additive-twist norms. Passing such a signed combination through that positive interface majorizes it by the absolute-weight form.

The surviving scalar route is therefore more specific. Sign cancellation can help only if one estimates the **indefinite cross-modulus operator itself**. That operator has the exact Toeplitz kernel

\[
\boxed{
R_\omega(h)=\sum_j\omega_j c_{m_j}(h),
}
\]

where `c_m(h)` is the Ramanujan sum. Consequently any genuine signed scalar gain must force simultaneous cancellation of a family of Ramanujan/divisor marginals. In particular,

\[
\boxed{
\|A_\omega\|_{\mathrm{op}}
\ge
\left|\sum_j\omega_j\varphi(m_j)\right|,
\qquad
\|A_\omega\|_{\mathrm{op}}
\ge
\max_{1\le |h|<N}
\left|\sum_j\omega_j c_{m_j}(h)\right|.
}
\]

For nonzero `h`, the classical divisor formula for Ramanujan sums makes this still more rigid: if

\[
F_\omega(d):=
\sum_{j:d\mid m_j}\omega_j\mu(m_j/d),
\]

then

\[
R_\omega(h)=\sum_{d\mid h}dF_\omega(d),
\]

and Möbius inversion gives, for `1<=d<N`,

\[
\boxed{
 d|F_\omega(d)|
 \le \tau(d)\|A_\omega\|_{\mathrm{op}}.
}
\]

Thus a successful sign-sensitive scalar escape must cancel not only total signed mass but the totient-weighted diagonal and every low-divisor Möbius marginal relevant to the finite operator. Ordinary signed additive energy of the outer coefficient sequence is not an input to the existing Baker--Munsch--Shparlinski theorem and, without a new theorem linking it to this Ramanujan operator, does not bypass WI-077--WI-078.

## 1. The published sparse-moduli large sieve is a positive quadratic form

Let

\[
z=(z_{M+1},\ldots,z_{M+N})\in\mathbf C^N
\]

and let `m_j` be scalar moduli. For each modulus define

\[
(T_jz)_a
:=
\sum_{n=M+1}^{M+N}z_ne(an/m_j),
\qquad
(a,m_j)=1.
\tag{1}
\]

Baker--Munsch--Shparlinski, *Additive energy and a large sieve inequality for sparse sequences*, Mathematika 68 (2022), Theorem 1.1, study exactly the positive functional

\[
\mathcal S(z,\mathbf m;M,N,Q)
=
\sum_{j\le Q}\sum_{a\bmod m_j}^{*}
\left|\sum_nz_ne(an/m_j)\right|^2
=
\sum_{j\le Q}\|T_jz\|_2^2.
\tag{2}
\]

Their theorem bounds (2) in terms of the symmetric and asymmetric additive energies of the scalar modulus sequence. WI-077 already shows that the actual unlabelled effective Yang scalar support has maximal energy exponent, while WI-078 shows that retaining the exact **positive** source weights or pruning while preserving a subpolynomial fraction of positive source mass does not lower that exponent.

The important interface point here is separate from those energy lower bounds: equation (2) is positive before the additive-energy estimate is invoked. The theorem does not take a signed outer coefficient multiplying the modulus-level squared norms and does not contain a signed-energy term that could record cancellation between different moduli.

No novelty is claimed for the positivity of (2). It is the defining large-sieve quadratic form in the primary source. The purpose of making it explicit is to test the remaining sign-sensitive escape from WI-078 against the theorem actually available, rather than against an imagined weighted extension.

## 2. Exact positive-operator majorization erases outer signs

Suppose an exact scalar reorganization of some centered source quantity produces real coefficients `omega_j` and the modulus-level form

\[
Q_\omega(z)
:=
\sum_j\omega_j\|T_jz\|_2^2.
\tag{3}
\]

Define the positive semidefinite Gram blocks

\[
B_j:=T_j^*T_j\succeq0
\]

and the self-adjoint signed and absolute operators

\[
A_\omega:=\sum_j\omega_jB_j,
\qquad
A_{|\omega|}:=\sum_j|\omega_j|B_j.
\tag{4}
\]

Then

\[
A_{|\omega|}+A_\omega
=2\sum_{\omega_j>0}\omega_jB_j\succeq0,
\qquad
A_{|\omega|}-A_\omega
=2\sum_{\omega_j<0}|\omega_j|B_j\succeq0.
\tag{5}
\]

Therefore, in Loewner order,

\[
\boxed{-A_{|\omega|}\preceq A_\omega\preceq A_{|\omega|}.}
\tag{6}
\]

For every `z`,

\[
\boxed{
|Q_\omega(z)|
=|\langle z,A_\omega z\rangle|
\le
\langle z,A_{|\omega|}z\rangle.
}
\tag{7}
\]

Since `A_omega` is self-adjoint, (6) also gives

\[
\boxed{
\|A_\omega\|_{\rm op}
\le
\|A_{|\omega|}\|_{\rm op}.
}
\tag{8}
\]

Thus splitting the signs, applying an ordinary positive large sieve to the two pieces, or taking triangle inequality are all instances of the same information loss: they replace `omega` by `|omega|`. WI-078 then applies at the source-information level whenever those absolute weights retain the positive `(5,7)` mass discussed there.

Equation (8) is only an **upper** majorization. It does not say that signs cannot reduce the true operator norm. They can. It says that any proof which reaches the existing positive large-sieve consumer only after (7) or (8) has already discarded exactly the cancellation it hoped to use. A successful signed route must therefore estimate `A_omega` before this positivity projection.

## 3. The signed modulus operator is exactly a Ramanujan-sum Toeplitz matrix

The matrix kernel of one Gram block is classical. For indices `n,n'` in the source interval,

\[
\begin{aligned}
(B_j)_{n,n'}
&=
\sum_{a\bmod m_j}^{*}
 e(a(n-n')/m_j)\\
&=
c_{m_j}(n-n'),
\end{aligned}
\tag{9}
\]

where

\[
c_m(h):=\sum_{a\bmod m}^{*}e(ah/m)
\tag{10}
\]

is the Ramanujan sum. Hence

\[
\boxed{
(A_\omega)_{n,n'}
=R_\omega(n-n'),
\qquad
R_\omega(h):=\sum_j\omega_jc_{m_j}(h).
}
\tag{11}
\]

So the signed scalar problem is not naturally an additive-energy problem for the coefficient sequence `omega`. It is a finite Toeplitz/operator problem for the signed superposition of Ramanujan kernels attached to the moduli.

This also identifies an exact falsification interface. If a proposed scalar signed reduction claims an operator saving, one can compute or estimate `R_omega(h)` before invoking any large-sieve theorem. Every lag represented inside the `N`-point matrix obeys

\[
|R_\omega(h)|
=|\langle e_n,A_\omega e_{n+h}\rangle|
\le
\|A_\omega\|_{\rm op},
\qquad |h|<N,
\tag{12}
\]

and therefore

\[
\boxed{
\|A_\omega\|_{\rm op}
\ge
\max_{|h|<N}|R_\omega(h)|.
}
\tag{13}
\]

At `h=0`, `c_m(0)=phi(m)`, so (13) contains the particularly cheap diagonal gate

\[
\boxed{
\|A_\omega\|_{\rm op}
\ge
\left|\sum_j\omega_j\varphi(m_j)\right|.
}
\tag{14}
\]

Thus ordinary cancellation of `sum omega_j`, or small signed convolution energy in the scalar index, is not even the first necessary condition. The arithmetic weighting `phi(m_j)` already survives on every diagonal entry.

## 4. Ramanujan's divisor formula turns operator cancellation into simultaneous divisor-marginal cancellation

For nonzero `h`, the classical identity

\[
 c_m(h)
 =
 \sum_{d\mid(m,h)}d\,\mu(m/d)
\tag{15}
\]

gives an exact divisor decomposition of (11). Interchanging the finite sums,

\[
\begin{aligned}
R_\omega(h)
&=
\sum_j\omega_j
\sum_{d\mid(m_j,h)}d\mu(m_j/d)\\
&=
\sum_{d\mid h}d
\sum_{j:d\mid m_j}\omega_j\mu(m_j/d).
\end{aligned}
\tag{16}
\]

Set

\[
F_\omega(d)
:=
\sum_{j:d\mid m_j}\omega_j\mu(m_j/d).
\tag{17}
\]

Then

\[
\boxed{
R_\omega(h)=\sum_{d\mid h}dF_\omega(d).
}
\tag{18}
\]

This is an ordinary divisor convolution with the constant-one function. Möbius inversion therefore yields

\[
\boxed{
 dF_\omega(d)
 =
 \sum_{e\mid d}\mu(d/e)R_\omega(e).
}
\tag{19}
\]

If `1<=d<N`, every divisor `e|d` is an available lag in the finite matrix, so (13) and (19) imply the necessary condition

\[
\boxed{
 d|F_\omega(d)|
 \le
 \tau(d)\|A_\omega\|_{\rm op}.
}
\tag{20}
\]

Thus a genuinely small signed modulus operator forces **all** low-divisor Möbius marginals to be small simultaneously. Examples of the first constraints are

\[
\left|\sum_j\omega_j\mu(m_j)\right|
\le \|A_\omega\|_{\rm op}
\tag{21}
\]

from `d=1`, together with the independent totient-weighted diagonal constraint (14). For general `d`, the condition sees which scalar moduli are divisible by `d` and with what cofactor Möbius sign. This is precisely information discarded by an unlabelled cardinality or ordinary additive-energy description.

The divisor structure is reminiscent of, but distinct from, WI-064. There the exact projective martingale concerns **conditioned prime-pair residue errors across refinement moduli**. Here (18)--(20) arise from the scalar large-sieve Gram kernel itself. The two calculations point in the same methodological direction: if the Yang escape exists, factorization/divisor labels are likely part of the information carrier rather than disposable bookkeeping.

## 5. Why a small signed additive energy is not yet a theorem interface

One can define many sign-sensitive additive energies for coefficients, for example

\[
\sum_s
\left|
\sum_{u+v=s}\omega_u\omega_v
\right|^2,
\tag{22}
\]

and these can indeed be much smaller than the corresponding positive-weight quantities because of cancellation. WI-078 deliberately left this logical possibility open.

But Baker--Munsch--Shparlinski Theorem 1.1 does not take (22), or any signed outer-weight analogue, as an input. Its additive energies belong to the **scalar modulus sequence**, and its left side is the positive form (2). Consequently there is no valid black-box implication

\[
\text{small signed energy of }\omega
\quad\Longrightarrow\quad
\text{small }\|A_\omega\|_{\rm op}
\tag{23}
\]

from that theorem. Establishing (23), with the exact Yang coefficients and source normalization, would itself be a new analytic theorem. Equations (14) and (20) give immediate necessary tests that any such theorem must pass.

This does not claim that a sign-sensitive sparse-moduli large sieve is impossible. It identifies what such a theorem must actually control. A valid result could exploit cancellation in `R_omega(h)`, factorization labels, a two-dimensional incidence transform, a bilinear dispersion identity, or another structure absent from the positive scalar form. What is closed is the cheaper route

\[
\boxed{
\text{centered signed scalar weights}
\longrightarrow
\text{ordinary BMS positive scalar large sieve}
\longrightarrow
\text{power gain from the signs}.
}
\tag{24}
\]

The signs disappear at the first arrow unless a new sign-sensitive operator estimate is inserted before the positive large-sieve consumer.

## 6. Relation to the Yang covariance program

WI-075--WI-078 progressively close scalar reductions that rely only on candidate support, effective support, unweighted additive energy, positive source weights, or positive-mass pruning. The remaining sentence in WI-078 — that **signed centering before energy is taken** could still matter — remains true, but its analytic content is now sharply constrained.

If the exact post-local-main Yang covariance can genuinely be reorganized into signed scalar modulus blocks of the form (3), then a useful cancellation theorem must control

\[
\boxed{
A_\omega
=\sum_j\omega_jT_{m_j}^*T_{m_j}
}
\tag{25}
\]

or an equivalent labelled transform directly. Before any expensive theorem search, the source coefficients should be tested against:

\[
\sum_j\omega_j\varphi(m_j),
\qquad
\sum_j\omega_jc_{m_j}(h),
\qquad
\sum_{j:d\mid m_j}\omega_j\mu(m_j/d).
\tag{26}
\]

Failure of cancellation at even one relevant scale is a direct lower bound on the operator norm. Passing all of these tests does not prove the needed large sieve, because matrix entries can be small while the collective operator norm remains large. It only keeps the sign-sensitive scalar route alive.

There is also an important source-boundary caveat. The current Yang clue is a locked four-prime covariance, and Mathia has not proved that its entire post-local-main complementary region reduces exactly to an outer-signed scalar form (3). The present finding is therefore an **information-interface barrier** for that proposed scalar escape, not a re-expression of the full Yang covariance and not a proof that every labelled/two-dimensional cancellation mechanism is impossible.

## 7. Prior-art and novelty boundary

No novelty is claimed for the large-sieve quadratic form, positivity of `T^*T`, Loewner-order majorization, Ramanujan sums, the identity (15), Möbius inversion, or basic operator-norm bounds on matrix entries. These are classical facts.

The load-bearing established source is:

- Roger C. Baker, Marc Munsch and Igor E. Shparlinski, **Additive energy and a large sieve inequality for sparse sequences**, *Mathematika* 68:2 (2022), 362--399, DOI `10.1112/mtk.12140`, arXiv:2103.12659. Its printed functional is the positive sum (2), and Theorem 1.1 bounds that functional through symmetric and asymmetric additive energies of the scalar modulus sequence.

A targeted prior-art audit around weighted/signed sparse-moduli large sieves and Ramanujan-sum formulations located the established BMS positive scalar-energy framework and related sparse-moduli large-sieve literature, but no theorem was used here that transfers cancellation of arbitrary signed **outer modulus weights** into a bound for (25). This is not an absence or priority claim; a source-specific theorem may exist or may be provable. The durable Mathia deduction is the exact interface test: the surviving signed scalar escape from WI-078 is an indefinite Ramanujan/divisor operator problem, and ordinary use of the currently cited positive scalar large sieve erases the signs before they can help.

No `SOURCES.md` update is needed: BMS is already a durable anchor for this line, and no new external theorem is imported.

## 8. Falsification and remaining gates

1. **Exact scalar reduction first.** Before applying this finding to the whole Yang covariance, derive the actual centered post-local-main scalar coefficients `omega_j` and prove that the relevant quantity has the form (3), or state the additional residue/direction labels that remain. If the source does not reduce to outer scalar weights, the correct object is a richer operator and this barrier applies only to its scalar projection.
2. **Diagonal gate.** Check `sum omega_j phi(m_j)` at the source normalization. If it remains of leading scale, no signed scalar operator saving is possible. If it cancels, continue; this gate is necessary, not sufficient.
3. **Low-lag Ramanujan gates.** Estimate `R_omega(h)` for `1<=|h|<N`. Any leading-scale lag gives an immediate operator lower bound. Equivalently, use (20) to test the low-divisor Möbius marginals.
4. **Do not substitute signed additive energy without a theorem.** A small quantity such as (22) is useful only if a rigorous argument connects it to `||A_omega||_op` with the exact modulus/source ranges. BMS Theorem 1.1 does not provide that bridge.
5. **Labelled and two-dimensional transforms remain live.** Retaining `(r,q)`, physical shifts `(h_1,h_2)`, residue fibers, or the original four-prime lock can expose cancellation absent from the scalar outer-weight projection.
6. **Source-specific dispersion remains live.** The signed Ramanujan profile may itself have a tractable dispersion or spectral estimate. Such a theorem would be genuinely new arithmetic information relative to WI-077--WI-078, not a contradiction of them.
7. **Relation to the accepted covariance clue.** This finding narrows one escape route only. The complementary power-coefficient post-local-main Yang covariance remains unresolved and still requires a source-faithful hybrid, a two-modulus theorem, or an equivalent sign-sensitive operator estimate.