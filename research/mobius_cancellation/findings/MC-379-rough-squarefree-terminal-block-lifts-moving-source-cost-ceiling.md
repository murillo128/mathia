# MC-379 — Rough squarefree terminal block lifts the moving source-cost ceiling

**Status:** `LITERATURE+DERIVED` · `EXACT-DERIVED` · `FRONTIER-ADVANCE` · `SOURCE-COST` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the exact endpoint source-package setup of `MC-296`, `MC-374`, `MC-377`, and `MC-378`. Write

\[
\mathcal R_y=D_1\sqcup\cdots\sqcup D_R,
\qquad R\to\infty,
\]

for the nonempty endpoint defect cells, choose fixed lower-prime product representatives `V_i` for their independent quadratic endpoint generators, and put

\[
U=\bigcup_{i=1}^R V_i,
\qquad
P=\prod_{p\in U}p.
\tag{1}
\]

There is an absolute constant `C>0` such that the following moving-exponent statement holds. If `A=A(y)>=2` satisfies

\[
2^{CA}=o(R)
\tag{2}
\]

and

\[
2^{CA}\log\log y=o(\log y),
\tag{3}
\]

then an exact endpoint realization cannot satisfy

\[
P\le y^A
\tag{4}
\]

for all sufficiently large `y`.

Consequently there is an absolute `c>0` such that every exact endpoint source package obeys the unconditional architecture-level rate

\[
\boxed{
\frac{\log P}{\log y}
\ge
c\min\{\log(R+2),\,\log\log y\}
}
\tag{5}
\]

for all sufficiently large `y`.

The new point relative to `MC-378` is analytic but source-specific. `MC-378` inserted the full moving-parameter Cochrane--Granville--Zheng theorem and therefore inherited its generic condition

\[
k2^k\ll\log\log Q,
\]

which produced the `log log log y` ceiling in its explicit source-cost rate. Here the source-incidence code first removes very small source primes at codimension `2^{O(A)}`. Every remaining canonical quadratic conductor is then **squarefree and rough from below**. For such a conductor, the prime local estimate in Cochrane--Granville--Zheng Proposition 6 can be multiplied directly over the final squarefree block. Lemma 7 then averages the displacement collisions with only a factor

\[
\prod_{p\mid Q}\left(1+\frac{k}{\sqrt p}\right).
\]

Once every `p|Q` exceeds `2^{O(k)}`, this gives a fixed negative power of `Q` without the generic `k2^k<<log log Q` absorption step. The remaining `2^{-k}` loss is unavoidable in Proposition 7, but with `k=O(A)` it costs only `2^{O(A)}` and therefore permits `A` up to a small constant multiple of `log log y`.

No bound for `M(x)`, no RH consequence, and no statement about arbitrary character families follows.

## 1. Remove both rough-above and tiny source coordinates

Assume `(4)` toward contradiction. Put

\[
\theta:=\frac1{32A}.
\tag{6}
\]

As in `MC-377`--`MC-378`, a source prime `p>y^\theta` contributes more than `\theta\log y` to `\log P`, so

\[
\#\{p\in U:p>y^\theta\}
\le \frac A\theta
=32A^2.
\tag{7}
\]

For every source prime define its incidence column

\[
c_p=(\mathbf 1_{p\in V_1},\ldots,\mathbf 1_{p\in V_R})\in\mathbb F_2^R.
\tag{8}
\]

For `I\in\mathbb F_2^R`, let

\[
V_I:=\mathop\triangle_{i:I_i=1}V_i,
\qquad
\chi_I:=\prod_{p\in V_I}\left(\frac{\cdot}{p}\right).
\tag{9}
\]

The source-incidence identity is

\[
p\in V_I\iff\langle I,c_p\rangle=1.
\tag{10}
\]

We now impose a lower cutoff as well. The explicit prime estimate in Cochrane--Granville--Zheng Proposition 6, specialized to `f(x)=x`, `g(x)=0` after `k` differencing steps, has local constant

\[
C_k=2^{k+2}.
\tag{11}
\]

The algebraic exceptional-prime audit already carried out in `MC-242` shows that for this specialization the additional bad primes at depth `k` are confined to fixed algebraic factors and primes of size `O(k)`; no exponentially large exceptional prime is hidden there.

Choose an absolute constant `K` large enough that, simultaneously for every

\[
k\le 33A,
\]

the cutoff

\[
T_A:=2^{KA}
\tag{12}
\]

contains all those exceptional primes and satisfies

\[
T_A\ge C_k^{16}
\tag{13}
\]

and the elementary inequality

\[
1+\frac{k}{\sqrt p}\le p^{1/16}
\qquad(p>T_A).
\tag{14}
\]

Let `E_y` contain every source prime either above `y^theta` or at most `T_A`, and define

\[
W:=\{I\in\mathbb F_2^R:\langle I,c_p\rangle=0\text{ for every }p\in E_y\}.
\tag{15}
\]

By `(7)` and the trivial bound `pi(T_A)<=T_A`,

\[
\operatorname{codim}W
\le 32A^2+2^{KA}.
\tag{16}
\]

After increasing the absolute constant in `(2)`, that hypothesis makes `(16)` `o(R)`. Hence, with

\[
H:=|W|,
\]

we have

\[
\boxed{
\dim W=R-o(R),
\qquad
H=2^{R-o(R)}.
}
\tag{17}
\]

Every nonzero source character indexed by `W` is therefore supported only on primes in

\[
T_A<p\le y^{1/(32A)}.
\tag{18}
\]

The endpoint generators are independent, so distinct indices in `W` give distinct endpoint modes and every nonzero pair difference gives a nonprincipal source character.

Condition `(3)` implies `A=O(log log y)` and hence `A^2=o(log y)`. Therefore, after enlarging `C` if necessary,

\[
T_A<y^{1/(32A)}
\tag{19}
\]

for all sufficiently large `y`; the interval in `(18)` is not vacuous merely because of the two cutoffs.

## 2. A rough squarefree terminal block has fixed power cancellation

We isolate the analytic lemma that removes the generic moving-depth tariff.

Let `q` be the primitive squarefree conductor of one of the nonprincipal characters arising from `(9)`, and let an interval `J` have length `N`. Factor

\[
q=q_1\cdots q_kQ
\tag{20}
\]

into pairwise coprime factors and apply Cochrane--Granville--Zheng Proposition 7 to

\[
a_q(n)=\chi_q(n).
\]

After `k` differencing steps their Proposition 6, specialized to `f(x)=x`, `g(x)=0`, gives at each prime `p|Q`, after capping by the trivial bound when a displacement collision occurs,

\[
\max_{b\bmod p}
\left|
\frac1p\sum_{n\bmod p}
\chi_p(f^*_{\mathbf h}(n))e(bn/p)
\right|
\le
C_k p^{-\frac12\max\{0,1-v_p(\mathbf h)\}}.
\tag{21}
\]

Write

\[
\Pi(\mathbf h)=\prod_{j=1}^k(h_{j,1}-h_{j,0}).
\]

Because `Q` is squarefree, multiplication of `(21)` over `p|Q` gives

\[
C_k^{\omega(Q)}Q^{-1/2}(Q,\Pi(\mathbf h))^{1/2}.
\tag{22}
\]

This is the squarefree specialization that is deliberately not used in the generic prime-power branch of the published Theorem 3 proof.

Average `(22)` over the displacement tuples. For every `u|Q`, Lemma 7 gives

\[
\Pr(u\mid\Pi(\mathbf h))
<\frac{\tau_k(u)}u,
\tag{23}
\]

where `tau_k` is the ordered `k`-fold divisor function. Since `Q` is squarefree, `tau_k(p)=k`; consequently

\[
\begin{aligned}
\mathbb E (Q,\Pi(\mathbf h))^{1/2}
&\le
\sum_{u\mid Q}u^{1/2}\Pr(u\mid\Pi(\mathbf h))\\
&<
\sum_{u\mid Q}\frac{\tau_k(u)}{\sqrt u}\\
&=
\prod_{p\mid Q}\left(1+\frac{k}{\sqrt p}\right).
\end{aligned}
\tag{24}
\]

Combining `(22)`--`(24)` with their Lemma 5 therefore gives the explicit terminal estimate

\[
\boxed{
\mathbf E_Q
\ll
\left(1+\frac{Q\log Q}{N}\right)
C_k^{\omega(Q)}Q^{-1/2}
\prod_{p\mid Q}\left(1+\frac{k}{\sqrt p}\right).
}
\tag{25}
\]

Suppose now that every prime factor of `Q` exceeds `T_A`, that `k<=33A`, and that `Q<N`. By `(13)`,

\[
C_k^{\omega(Q)}\le Q^{1/16},
\tag{26}
\]

and by `(14)`,

\[
\prod_{p\mid Q}\left(1+\frac{k}{\sqrt p}\right)
\le Q^{1/16}.
\tag{27}
\]

As `Q->infinity`, also

\[
1+\frac{Q\log Q}{N}
\le1+\log Q
\le Q^{1/16}.
\tag{28}
\]

Thus, conservatively,

\[
\boxed{
\mathbf E_Q\ll Q^{-1/4}.
}
\tag{29}
\]

No condition of the shape `k2^k<<log log Q` occurs. In the generic proof that condition is used to absorb a factor `(3^kD)^{omega(Q^*)}` after the weaker prime-power complete-sum exponent has been applied. Here the exact squarefree source conductor and the lower roughness cutoff permit the prime estimate to be multiplied before the final `2^{-k}` root.

This is a composite rough-squarefree extension of the prime-terminal calculation in `MC-242`; the underlying differencing and complete-sum estimates are entirely from `MC-S46`.

## 3. Good endpoint modes get a moving power saving without the `log log Q` gate

We next separate the low-conductor pair modes before applying the preceding lemma.

`MC-374`, specialized at fixed `delta=1`, shows that among all nonzero endpoint modes only `O(R)` can have minimum primitive lower-prime source conductor at most `y`, provided

\[
R y^{-c_0}\log y=o(1)
\tag{30}
\]

for an absolute `c_0>0`. Under `(4)`, source-incidence independence gives

\[
R\le |U|\le\log_2P\ll A\log y.
\tag{31}
\]

Condition `(3)` forces `A=O(log log y)`, so `(30)` follows. Call those `O(R)` endpoint differences **bad** and every other nonzero difference **good**.

Fix a good difference in `W`, and let `q` be the conductor of its canonical source character `(9)`. Its minimum source conductor exceeds `y`, hence

\[
q>y.
\tag{32}
\]

On the other hand `q|P`, so

\[
q\le y^A,
\tag{33}
\]

and every prime factor of `q` lies in `(18)`.

Put

\[
\delta:=\frac1{16A}.
\tag{34}
\]

Then `(18)`, `(32)` give

\[
P^+(q)\le y^{1/(32A)}\le q^{\delta/2}.
\tag{35}
\]

An elementary greedy factorization of the squarefree prime factors of `q` now yields `(20)` with

\[
k\le\frac2\delta+1\le33A,
\tag{36}
\]

\[
q_i\le q^\delta\le y^{1/16},
\tag{37}
\]

and a terminal factor satisfying

\[
q^{\delta/2}<Q\le q^\delta.
\tag{38}
\]

This is the same arithmetic factorization pattern used in the proof of Cochrane--Granville--Zheng Theorem 4, but no moving-parameter theorem is invoked here.

For the shell-scale intervals needed below, take any

\[
N\ge y^{1-o(1)}.
\]

Then `(37)` makes every `q_i` a fixed power smaller than `N`, while `(38)` and `(32)` give

\[
Q\ge y^{1/(32A)}
\tag{39}
\]

and `Q<N`. Proposition 7, `(29)`, and `(36)` therefore yield

\[
\left|\frac1N\sum_{n\in J}\chi_q(n)\right|
\ll
kN^{-c_1/2^k}+Q^{-1/(4\,2^k)}
\tag{40}
\]

for an absolute `c_1>0`. After increasing the absolute constant once more, `(39)`--`(40)` imply a uniform saving

\[
\boxed{
\left|\sum_{n\in J}\chi_q(n)\right|
\ll N y^{-\sigma_A},
\qquad
\sigma_A\ge2^{-CA}.
}
\tag{41}
\]

The harmless prefactor `k=O(A)` is absorbed because `(3)` implies `2^{-CA}\log y\gg\log A` after choosing the displayed `C` sufficiently large.

The important distinction from `MC-378` is that `(41)` uses neither the imprimitive-character inclusion-exclusion loss nor the published Theorem 3 condition `k2^k<<log log Q`: every pair is represented by its canonical primitive squarefree source character, and the rough terminal estimate `(29)` supplies the required complete-sum decay directly.

## 4. Sparse low-conductor exceptions do not defeat the prime frame

Transfer `(41)` through the same Selberg-sieve/Bombieri prime-frame argument already audited in `MC-377`--`MC-378`.

Choose

\[
b:=\sigma_A/100,
\qquad
B:=y^b.
\tag{42}
\]

In the Selberg expansion of the weighted inner product for a good pair, every inner interval has length

\[
N'\gg y/B^2=y^{1-2b}.
\tag{43}
\]

The derivation of `(41)` is uniform for all such `N'`: the factors `q_i<=y^{1/16}` remain a fixed power smaller than `N'`, while `Q<=y^{1/16}<<N'`, so the terminal factor in `(25)` only improves. After the `B^2` Selberg expansion cost, there is therefore an absolute `c_2>0` such that every good off-diagonal weighted inner product is

\[
\ll y^{1-c_2\sigma_A}.
\tag{44}
\]

For a bad pair we use only the trivial diagonal-scale bound. There are `O(R)` bad endpoint differences in total by `MC-374`, and for any fixed row `I\in W` the map `J\mapsto I+J` is injective. Hence every row has only `O(R)` bad neighbours.

Let `V` be the `H x |\mathcal R_y|` shell-character matrix and

\[
G:=|\mathcal R_y|^{-1}VV^*.
\]

Exactly as in `MC-377`, every row is constant on the `R` endpoint cells, so

\[
\operatorname{rank}V\le R,
\qquad
\operatorname{tr}G=H,
\]

and therefore

\[
\lambda_{\max}(G)\ge\frac HR.
\tag{45}
\]

Bombieri's frame inequality with the Selberg weight has diagonal scale

\[
\ll \frac y{\log B}+B^2,
\]

which becomes `O(sigma_A^{-1})` after normalization by `|mathcal R_y| asymp y/log y`. The `O(R)` bad neighbours cost at most the same diagonal scale each, while `(44)` controls every good neighbour. Consequently

\[
\boxed{
\lambda_{\max}(G)
\ll
R\sigma_A^{-1}
+H y^{-c_3\sigma_A}\log y
}
\tag{46}
\]

for an absolute `c_3>0`.

Combine `(45)` and `(46)` and divide by `H`:

\[
\frac1R
\ll
\frac{R\sigma_A^{-1}}H
+y^{-c_3\sigma_A}\log y.
\tag{47}
\]

By `(17)` and `(2)`, the first term is `o(1/R)`. For the second, `(31)` and `(41)` show that it is also `o(1/R)` as soon as

\[
2^{CA}\log\log y=o(\log y),
\]

which is exactly `(3)` after enlarging `C` one final time. This contradicts `(47)` and proves the moving-exponent claim `(2)`--`(4)`.

## 5. Explicit rate and comparison with MC-378

Choose a sufficiently small absolute `c>0` and put

\[
A_*(y):=
 c\min\{\log(R+2),\log\log y\}.
\tag{48}
\]

If an exact endpoint had `log P/log y < A_*`, then `P<=y^{A_*}`. For `c` small relative to the absolute constant in `(2)`--`(3)`, we have

\[
2^{CA_*}=o(R)
\]

and

\[
2^{CA_*}\log\log y=o(\log y).
\]

The just-proved moving theorem gives a contradiction. This proves `(5)`.

The result is complementary to `MC-378`, not a pointwise replacement for it. `MC-378` gives

\[
\frac{\log P}{\log y}
\gg
\min\left\{
\sqrt{\frac{R}{\log(R+2)}},
\log\log\log y
\right\}.
\]

Its rank-side term can be much stronger than `log R`. The present argument instead improves the **analytic moving-depth ceiling** from `log log log y` to `log log y` whenever the endpoint rank is large enough to pay the `2^{O(A)}` small-prime pruning cost. Both lower bounds remain valid and may be combined by taking their maximum.

## Prior art and novelty boundary

The analytic machinery is classical/recent literature rather than a claimed new character-sum theorem. `MC-S46`, Todd Cochrane, Andrew Granville and Junren Zheng, *Mixed incomplete character sums of rational functions with smooth moduli*, arXiv:`2601.10927v1` (16 January 2026), supplies Proposition 7, Proposition 6, Lemma 5, and Lemma 7. Their proof of Theorem 3 explicitly bounds the generic terminal average by a factor of the form `(3^kD)^{omega(Q^*)}(Q^*)^{-1/(4D)}` and then invokes `k2^k<<log log Q^*` to absorb the positive factor. Equations `(22)`--`(29)` instead retain the stronger prime-local exponent available when the terminal conductor is squarefree and use the source-imposed lower bound on every prime factor before taking the final root.

`MC-242` already established the essential proof discipline: it returned to Propositions 6--7 rather than substituting a growing differencing depth into a fixed-parameter theorem, and it obtained a `log log y` support floor when the terminal block was one shell prime. The present result extends that same explicit audit to a **composite rough squarefree terminal block** and then couples it to the later endpoint source-incidence and prime-frame architecture. No novelty is claimed for `q`-van der Corput differencing, the prime complete-sum estimate, the displacement-divisor calculation, or the Selberg/Bombieri transfer.

A targeted literature search on 18 September 2026 found the Cochrane--Granville--Zheng manuscript, Graham--Ringrose/smooth-modulus character-sum literature, and later uses of `q`-van der Corput methods, but no source was found stating the endpoint/source-cost consequence `(2)` or the exact rough-terminal specialization `(25)` in this form. Absence from that search is not evidence of novelty.

As in `MC-377`--`MC-378`, `MC-S46` remains manuscript-level evidence, so any material revision of its Propositions 6--7 or Lemma 7 requires re-audit.

## Decisive audit and boundaries

- **Squarefree primitive source conductors are load-bearing.** The improvement from the generic `(3^kD)^{omega(Q^*)}` treatment comes from multiplying the prime-local `p^{-1/2}` estimate over a squarefree terminal block. It does not automatically extend to arbitrary prime-power moduli.
- **Lower roughness is load-bearing.** Without removing source primes `p<=2^{O(A)}`, the factor `C_k^{omega(Q)}` in `(25)` can again overwhelm the negative power before the final `2^{-k}` root.
- **The `O(R)` low-conductor family is not ignored.** `MC-374` is used before the frame estimate, and those pair differences are paid for trivially as sparse bad neighbours. No character-sum saving is asserted for them.
- **The endpoint/source-incidence code is load-bearing.** It creates the codimension-`2^{O(A)}` subspace while retaining `2^{R-o(R)}` modes. A generic unrelated character family need not survive this pruning.
- **The exponent `log log y` is not claimed optimal.** It is the scale at which the remaining `2^{O(A)}` differencing and small-prime costs can still be beaten by `log y`. A stronger terminal estimate or a way to avoid pruning all small source coordinates could move it further.
- **The conclusion concerns common source cost, not minimum conductor of every mode.** A sparse `O(R)` family of low-minimum-conductor endpoint modes explicitly remains.
- **No RH, GRH, zero-density, or Möbius square-root cancellation input is used.** The result narrows one exact endpoint representation branch only.
- **No estimate for `M(x)` follows.** The new rate is a source-realizability obstruction, not a global Möbius cancellation theorem.