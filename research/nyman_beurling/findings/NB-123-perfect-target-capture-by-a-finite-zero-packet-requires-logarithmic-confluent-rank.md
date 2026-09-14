# NB-123 — perfect target capture by a finite zero packet requires logarithmic confluent rank

**Status:** `EXACT-DERIVED + ZERO-POWER-ANNIHILATING-RECURRENCE + PERFECT-TARGET-RANK-OBSTRUCTION + NB-117/NB-122-SEPARATOR + NEGATIVE/ROUTE-NARROWING + REPRESENTATION-AUDIT`.

`NB-117` identifies the remaining finite-section target problem for an actual finite off-critical zeta-zero packet with weighted interpolation of the harmonic profile `C+D/n` by a confluent zero-power sum. `NB-119`--`NB-122` then show that the broader source class defined only by increasingly many Nyman orthogonality equations still admits perfect visible target capture at the inverse-section scale, even simultaneously across the full nested cutoff prefix.

The actual zero-power representation imposes an additional rigidity that those matched controls do not satisfy. On a geometric subgrid, every finite confluent zero-power primitive is a finite exponential-polynomial sequence and therefore obeys a finite annihilating recurrence. The harmonic target has its own geometric mode `q^{-k}`. Because an actual nontrivial zeta zero never gives the characteristic root `q^{-1}`, the two sequences cannot agree for arbitrarily many consecutive geometric blocks unless the packet rank grows with the cutoff.

Let `F` be a finite multiset of actual nontrivial zeta zeros with `Re rho>1/2`. Write its distinct zeros as `rho_1,...,rho_s` with multiplicities `m_1,...,m_s`, and define the total confluent rank

\[
 d(F):=\sum_{j=1}^{s}m_j=\dim K_F.
\tag{1}
\]

For `f in K_F`, retain the target-tail primitive of `NB-117`,

\[
P_f(n)
=
\sum_{j=1}^{s}\sum_{r=0}^{m_j-1}
 c_{j,r}\,n^{-\overline{\rho_j}}(\log n)^r.
\tag{2}
\]

For every integer `q>=2` and cutoff `R>=2`, if

\[
q_R(f)=1,
\qquad
Q_Rf\ne0,
\tag{3}
\]

then

\[
\boxed{
 d(F)\ge \left\lfloor\log_q R\right\rfloor.
}
\tag{4}
\]

In particular, choosing `q=2` gives the strongest member of this family:

\[
\boxed{
 q_R(f)=1,\ Q_Rf\ne0
 \quad\Longrightarrow\quad
 d(F)\ge \left\lfloor\log_2 R\right\rfloor.
}
\tag{5}
\]

Equivalently, a fixed rank-`d` actual zero packet cannot realize perfect visible target capture once

\[
R\ge 2^{d+1}.
\tag{6}
\]

If `chi_(F,R)` is the packet target-capture fraction of `NB-117`, then

\[
\boxed{
 d(F)<\lfloor\log_2R\rfloor
 \quad\Longrightarrow\quad
 \chi_{F,R}<1.
}
\tag{7}
\]

This is an exact separator between the actual finite zero-power class and the inverse-section matched controls of `NB-119`--`NB-122`. Those controls can satisfy `Q_Rf=e_R` while obeying a growing family of exact Nyman equations; an actual finite zero packet can satisfy the same perfect-target equation only if its confluent rank is at least logarithmic in the cell cutoff.

## 1. Geometric samples of a zero-power primitive have a finite annihilator

Fix an integer `q>=2` and sample `(2)` on the geometric grid `n=q^k`. Put

\[
u_k:=P_f(q^k).
\tag{8}
\]

For each distinct zero define

\[
\lambda_j:=q^{-\overline{\rho_j}}.
\tag{9}
\]

Since `log(q^k)=k log q`, equation `(2)` becomes

\[
\boxed{
 u_k
 =
 \sum_{j=1}^{s}\lambda_j^k p_j(k),
 \qquad
 \deg p_j<m_j,
}
\tag{10}
\]

for suitable polynomials `p_j`. Thus the geometric samples form a confluent exponential-polynomial sequence of total rank at most `d(F)`.

Let `E` denote the forward shift, `(Eu)_k=u_{k+1}`, and define the monic polynomial

\[
A_{F,q}(z)
:=
\prod_{j=1}^{s}(z-\lambda_j)^{m_j}.
\tag{11}
\]

The standard finite-difference identity

\[
(E-\lambda)\bigl(\lambda^k p(k)\bigr)
=
\lambda^{k+1}\bigl(p(k+1)-p(k)\bigr)
\tag{12}
\]

lowers the polynomial degree by one. Repeating it `m_j` times kills every `j`th confluent block. Hence

\[
\boxed{
 A_{F,q}(E)u=0.
}
\tag{13}
\]

Now define the geometric-block increments

\[
v_k:=u_k-u_{k+1}=(I-E)u_k.
\tag{14}
\]

Because `A_(F,q)(E)` commutes with `I-E`, the same recurrence annihilates the increments:

\[
\boxed{
 A_{F,q}(E)v=0.
}
\tag{15}
\]

No generic-position assumption on the ordinates is needed. If two different zeros happen to give the same sampled node `lambda_j`, the polynomial `(11)` merely contains redundant factors; it still annihilates the sequence, so such aliasing can only reduce the true recurrence order and strengthen the obstruction below.

## 2. Perfect target angle fixes every geometric-block increment

`NB-117` proves the exact Pythagorean identity

\[
q_R(f)
=
\frac1{1+L_R\,\mathcal E_R(P_f-H_f)/|A_f|^2},
\qquad
L_R=1-\frac1R,
\tag{16}
\]

where `H_f` is the unique affine function of `1/n` with the same endpoint values as `P_f` on `1,...,R`.

Therefore `(3)` forces equality in the sharp weighted Hardy inequality of `NB-117`. Since `Q_Rf ne 0`, the target coordinate is nonzero, and there are constants `C,D` with `D ne 0` such that

\[
\boxed{
P_f(n)=C+\frac Dn,
\qquad
1\le n\le R.
}
\tag{17}
\]

Equivalently `Q_Rf` is a nonzero scalar multiple of `e_R`.

Set

\[
K:=\left\lfloor\log_q R\right\rfloor.
\tag{18}
\]

For `0<=k<K`, both endpoints `q^k` and `q^(k+1)` lie in the visible grid. Summing the adjacent-cell differences across that block, or simply applying `(17)` at the two endpoints, gives

\[
\begin{aligned}
v_k
&=P_f(q^k)-P_f(q^{k+1})\\
&=D(1-q^{-1})q^{-k}.
\end{aligned}
\tag{19}
\]

Thus perfect target capture forces the first `K` geometric-block increments of the actual zero-power primitive to coincide with a nonzero pure exponential mode whose characteristic root is exactly `q^{-1}`.

## 3. The target root is absent from every actual right-half zero packet

Every actual nontrivial zeta zero in `F` lies in the open critical strip, so

\[
\frac12<\Re\rho_j<1.
\tag{20}
\]

Consequently

\[
|\lambda_j|
=q^{-\Re\rho_j}
>q^{-1},
\tag{21}
\]

and in particular

\[
\boxed{
A_{F,q}(q^{-1})\ne0.
}
\tag{22}
\]

Suppose for contradiction that `K>=d(F)+1`. The recurrence polynomial `(11)` has degree `d(F)`, so evaluating `(15)` at `k=0` uses only

\[
v_0,v_1,\ldots,v_{d(F)}.
\tag{23}
\]

All of these entries lie among the `K` exact target blocks in `(19)`. If

\[
w_k:=D(1-q^{-1})q^{-k},
\tag{24}
\]

then `v_k=w_k` for `0<=k<=d(F)`, and therefore

\[
\begin{aligned}
0
&=A_{F,q}(E)v_0\\
&=A_{F,q}(E)w_0\\
&=A_{F,q}(q^{-1})w_0.
\end{aligned}
\tag{25}
\]

But both factors on the last line are nonzero by `(22)` and `D ne 0`, a contradiction. Hence

\[
K\le d(F),
\tag{26}
\]

which proves `(4)` and `(5)`.

The packet-capture statement `(7)` is immediate. Since `Q_RK_F` is finite-dimensional, `chi_(F,R)=1` means that `e_R` belongs to `Q_RK_F`; therefore some `f in K_F` has `Q_Rf=e_R` and satisfies `(3)`, so `(5)` applies.

## 4. What this removes from the NB-119--NB-122 matched-control class

The generic controls constructed in `NB-119` and `NB-120` are designed only to lie in `V_M^perp` while having `Q_Rf=e_R`. `NB-121` and `NB-122` show that the same maximal repair then captures the target exactly at every smaller nested cutoff as well. Those results deliberately do not impose the source representation `(2)`.

The new obstruction shows that this omission is substantive rather than cosmetic. Nyman orthogonality, even with a growing source depth and full-prefix target coherence, does not encode the finite recurrence forced by an actual zero packet. A matched control may therefore inhabit the exact inverse-section geometry while being impossible to realize by any actual zero packet whose total multiplicity is `o(log R)`.

This closes one precise part of the frontier left by `NB-122`: **bounded-rank and sublogarithmic-rank actual zero packets cannot be hidden inside the perfect-target matched-control class**. The first genuinely source-faithful separator is not another nested projection equation but the transformation law of the zero-power primitive itself.

The result is intentionally about exact target capture. It does not yet show that a low-rank packet has target angle bounded uniformly away from one. A sequence with `q_R(f)=1-o(1)` need only approximate the harmonic block increments, and a quantitative version must control how strongly the annihilator `(11)` amplifies those approximation errors relative to

\[
|A_{F,q}(q^{-1})|.
\tag{27}
\]

That conditioning depends on the actual sampled zero nodes and can deteriorate when nodes cluster or when the packet rank grows. The exact rank obstruction therefore identifies the next quantitative object rather than solving it.

## 5. Prior-art and novelty boundary

The recurrence mechanism itself is classical Prony/annihilating-filter theory. For example, Gerlind Plonka, *Prony methods for recovery of structured functions*, GAMM-Mitteilungen 37 (2014), 239--258, DOI `10.1002/gamm.201410011`, treats exponential and extended-exponential sums through finite annihilating recurrences and related Hankel/Prony structure. No novelty is claimed for `(10)`--`(15)` as general sequence theory.

The line-local content is the splice with the exact Nyman target geometry already derived in `NB-117`: perfect finite target capture forces the geometric block data to be the specific missing root `q^{-1}`, while an actual right-half zeta-zero packet supplies only roots `q^{-\bar\rho}` with `Re rho<1`. A search of the Nyman--Beurling/Báez-Duarte quantitative literature and neighboring Prony formulations did not identify this particular logarithmic packet-rank obstruction. This finding therefore claims only the exact derived consequence `(4)`--`(7)`, not novelty of the underlying recurrence formalism.

No external theorem is load-bearing in the proof: the annihilator identity is proved directly in `(12)`--`(15)`, and the target equality case is the canonical `NB-117` identity. Accordingly this result introduces no new durable source dependency in `SOURCES.md`.

## 6. Boundary conditions and decisive audit tests

The logarithmic bound concerns the **total confluent multiplicity** of a finite actual packet, not merely the number of distinct ordinates. Multiple zeros are already included through the polynomial factors in `(2)` and the powers in `(11)`. Sample-node collisions do not evade the proof because the displayed degree is only an upper bound on the minimal recurrence order.

The nonzero-target hypothesis is essential. If `Q_Rf=0`, the angle `q_R(f)` is not the perfect-target event under study and `D` may vanish. The argument also uses exact equality `q_R(f)=1`; it does not convert a fixed capture fraction `c<1` into a rank lower bound without a stable approximate-recurrence estimate.

The fastest falsification test is algebraic. For any finite confluent packet, form `(11)` and verify `(15)` on the geometric samples of `(2)`. If `(17)` held through a cutoff with `floor(log_q R)>=d(F)+1`, substitution of the forced block data `(19)` into the first recurrence equation would give `(25)`. A counterexample would therefore have to violate either the `NB-117` equality characterization, the elementary annihilator identity, or the strict inequality `Re rho<1` for an actual nontrivial zeta zero.

For the RH program, `(5)` is not an exclusion of off-critical zeros and does not improve a known Nyman approximation-rate exponent. High-rank packets remain completely open. The live quantitative question is now sharper: determine whether actual zero nodes can make the approximate annihilator sufficiently ill-conditioned to permit order-one or near-perfect harmonic-profile capture when `d(F)` grows, or prove a stable lower bound that turns the exact logarithmic rank separator into a nontrivial target-angle gap.