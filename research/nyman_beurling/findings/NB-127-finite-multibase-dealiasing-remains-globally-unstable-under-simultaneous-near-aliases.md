# NB-127 — finite multibase de-aliasing remains globally unstable under simultaneous near-aliases

**Status:** `EXACT-DERIVED + SIMULTANEOUS-NEAR-ALIAS + FINITE-MULTIBASE-INSTABILITY + BURNOL-MASS-DECOUPLING + NB-126-STRENGTHENING + NEGATIVE/ROUTE-NARROWING + REPRESENTATION-AUDIT`.

`NB-126` identifies an exact one-base obstruction: shifting an ordinate by `2pi/log q` preserves the complete `q`-geometric zero-power trace and the `NB-124` annihilator margin while the Burnol target mass decays like the inverse square of the absolute height. It therefore redirects the bridge toward two multiplicatively independent bases, such as `q=2,3`, because they have no common nonzero **exact** alias period.

That exact de-aliasing is real but is not quantitatively coercive by itself. For every finite collection of geometric bases, there are arbitrarily large common vertical shifts whose phase at every base returns arbitrarily close to the identity. Along those shifts, the full cross-base characteristic-root data, every annihilator coefficient vector, every normalized annihilator margin, and every fixed finite window of geometric primitive samples return arbitrarily close to their original values, while the elementary Burnol target mass tends to zero like `T^-2`.

Thus **finitely many geometric bases remove exact alias symmetry but do not provide a globally stable inverse from recurrence phase to absolute height.** Any successful multibase bridge from `NB-124`--`NB-125` to the absolute-height budget of `NB-116` must retain a quantitative phase modulus whose required resolution tightens with the height/cutoff, or use additional actual-zero structure. Merely replacing one fixed-base margin by finitely many continuously combined margins does not close the representation-level gap.

## 1. Every finite family of geometric bases has arbitrarily high simultaneous near-aliases

Let

\[
\mathcal Q=\{q_1,\ldots,q_m\},\qquad q_j\ge2,
\]

be a finite set of integer bases. For a vertical shift `T`, put

\[
u_q(T):=e^{iT\log q}.
\tag{1}
\]

For `m=1`, `NB-126` gives the exact period `2pi/log q_1`. Assume `m>=2`. Set

\[
\alpha_j:=\frac{\log q_j}{\log q_1},\qquad 2\le j\le m.
\tag{2}
\]

For every integer `N>=2`, consider the `N^(m-1)+1` points

\[
\bigl(\{k\alpha_2\},\ldots,\{k\alpha_m\}\bigr),
\qquad 0\le k\le N^{m-1},
\]

in the `(m-1)`-dimensional unit cube, partitioned into `N^(m-1)` boxes of side `1/N`. Two points lie in the same box. Taking their difference gives an integer

\[
1\le n\le N^{m-1}
\]

and integers `p_2,...,p_m` such that

\[
|n\alpha_j-p_j|\le\frac1N,
\qquad 2\le j\le m.
\tag{3}
\]

Now choose

\[
T=\frac{2\pi n}{\log q_1}.
\tag{4}
\]

Then

\[
u_{q_1}(T)=1
\]

exactly, while `(3)` gives

\[
|u_{q_j}(T)-1|
\le \frac{2\pi}{N},
\qquad 2\le j\le m.
\tag{5}
\]

As `N` tends to infinity, either the resulting integers `n` are unbounded, in which case `(4)--(5)` give a sequence `T_k->infinity` with

\[
\boxed{
\max_{q\in\mathcal Q}|u_q(T_k)-1|\longrightarrow0,
}
\tag{6}
\]

or some nonzero `n` recurs for arbitrarily large `N`. In the latter case `(3)` forces `n alpha_j` to be integral for every `j`, so `(4)` is an **exact** common period; its integer multiples give arbitrarily large exact aliases. Hence `(6)` holds for every finite base family, with exact equality along a subsequence in the commensurable case.

When no exact common period exists, `(3)` also gives the coarse quantitative recurrence

\[
\max_{q\in\mathcal Q}|u_q(T)-1|
\ll_{\mathcal Q}T^{-1/(m-1)}
\tag{7}
\]

along an unbounded sequence of shifts. Indeed `n<=N^(m-1)` and `T\asymp_(q_1)n`.

For the important pair `\mathcal Q={2,3}`, exact common aliasing is impossible: an exact nonzero common period would imply

\[
\frac{\log3}{\log2}\in\mathbb Q,
\]

hence `3^a=2^b` for positive integers `a,b`. Nevertheless convergents `p/n` to `log3/log2` give shifts

\[
T_n=\frac{2\pi n}{\log2}
\]

for which

\[
\boxed{
u_2(T_n)=1,
\qquad
|u_3(T_n)-1|\ll T_n^{-1}.
}
\tag{8}
\]

Thus the two-base phase map is injective with infinite precision but has arbitrarily high returns to every neighborhood of its starting point.

## 2. Near-aliases preserve the complete finite-base recurrence representation to arbitrary accuracy

Let

\[
F=\{(\rho_j,m_j):1\le j\le s\},
\qquad
\rho_j=\beta_j+i\gamma_j,
\qquad
\frac12<\beta_j<1,
\]

be a finite formal zero-power packet, with total confluent rank

\[
d=d(F):=\sum_jm_j.
\]

As in `NB-126`, *formal* means that the points need not be actual zeros of `zeta`; this is a matched control for the source representation isolated in `NB-117`. Translate the whole packet by a common ordinate `T`:

\[
F_T:=\{(\rho_j+iT,m_j):1\le j\le s\}.
\tag{9}
\]

At base `q`, each characteristic root transforms as

\[
q^{-\overline{\rho_j+iT}}
=u_q(T)\,q^{-\bar\rho_j}.
\tag{10}
\]

Hence the **cross-base root signature** of every labelled packet point returns to its original value whenever `(6)` holds. This already includes information that separate scalar margins discard: the same root is matched across all bases before any product or norm is taken.

The corresponding annihilator satisfies an exact covariance law. Write

\[
A_{F,q}(z)
=\prod_j\bigl(z-q^{-\bar\rho_j}\bigr)^{m_j}
=\sum_{r=0}^{d}a_{r,q}z^r.
\tag{11}
\]

Then `(10)` gives

\[
\boxed{
A_{F_T,q}(z)
=u_q(T)^d A_{F,q}\!\left(\frac{z}{u_q(T)}\right)
=\sum_{r=0}^{d}a_{r,q}u_q(T)^{d-r}z^r.
}
\tag{12}
\]

Consequently

\[
\boxed{
|a_{r,q}(F_T)|=|a_{r,q}(F)|
}
\tag{13}
\]

for every coefficient and every shift. The weighted coefficient norm appearing in `NB-124` is therefore **exactly invariant** under an arbitrary common vertical translation, not merely under an exact alias.

Put `r_q=q^-1`. The normalized missing-root margin becomes

\[
\mathfrak s_{F_T,q}
=(1-r_q)
\frac{|A_{F,q}(r_q\overline{u_q(T)})|^2}
{\sum_{r=0}^{d}|a_{r,q}|^2r_q^r}.
\tag{14}
\]

Along any simultaneous near-alias sequence `(6)`, polynomial continuity therefore gives

\[
\boxed{
\mathfrak s_{F_{T_k},q}
\longrightarrow
\mathfrak s_{F,q}
\qquad(q\in\mathcal Q).
}
\tag{15}
\]

The same statement holds before annihilation. If

\[
P(n)=\sum_{j}\sum_{r<m_j}
c_{j,r}n^{-\bar\rho_j}(\log n)^r
\tag{16}
\]

is a primitive in the packet space and `P_T` is obtained by keeping the same coefficients in the translated packet, then

\[
\boxed{
P_T(q^k)=u_q(T)^kP(q^k).
}
\tag{17}
\]

Since `|u^k-1|<=k|u-1|` on the unit circle, every fixed finite geometric sample window returns uniformly to its original trace. More quantitatively, if

\[
K_k\max_{q\in\mathcal Q}|u_q(T_k)-1|\longrightarrow0,
\]

then the modulation defect in `(17)` is uniformly `o(1)` for all bases and all `0<=k<=K_k`. For the pair `2,3`, the continued-fraction sequence `(8)` therefore preserves windows of any depth `K_k=o(T_k)` to vanishing relative modulation.

Thus adding finitely many bases does more than merely fail after separate scalarization: **even the labelled joint root phases and finite sampled primitive traces have arbitrarily high near-returns.**

## 3. Absolute-height Burnol mass still vanishes along the same sequence

The elementary Burnol defect of one right-half point is, from `NB-114`--`NB-116` and `NB-126`,

\[
\delta_\rho
=\frac{2\beta-1}{\beta^2+\gamma^2}.
\tag{18}
\]

For the common translate `(9)`,

\[
\delta_{\rho_j+iT}
=\frac{2\beta_j-1}{\beta_j^2+(\gamma_j+T)^2}
=O_F(T^{-2}).
\tag{19}
\]

The finite-packet Blaschke target mass satisfies

\[
\tau(F_T)
:=1-|B_{F_T}(1)|^2
\le
\sum_jm_j\delta_{\rho_j+iT},
\]

so

\[
\boxed{
\tau(F_T)=O_F(T^{-2})\longrightarrow0.
}
\tag{20}
\]

Combining `(6)`, `(15)`, `(17)` and `(20)` gives the multibase matched control:

\[
\boxed{
T_k\to\infty,
\qquad
\mathcal D_{\mathcal Q}(F_{T_k})\to
\mathcal D_{\mathcal Q}(F),
\qquad
\tau(F_{T_k})\to0,
}
\tag{21}
\]

where `mathcal D_Q` may retain the labelled cross-base characteristic roots, all annihilator coefficient vectors, all normalized margins, or any fixed finite collection of geometric primitive samples. The first convergence is in the ordinary finite-dimensional topology appropriate to the chosen descriptor.

A useful precise no-go follows. Let `Phi` be any continuous nonnegative functional of such finite-base recurrence data, and suppose

\[
\Phi(\mathcal D_{\mathcal Q}(F))>0.
\]

There cannot be a universal representation-level inequality

\[
\tau(G)\ge
\Phi(\mathcal D_{\mathcal Q}(G))
\tag{22}
\]

for all finite formal strip packets `G`: applying `(22)` to `F_(T_k)` would leave its right side bounded away from zero while `(20)` sends the left side to zero. The same obstruction applies to any lower-semicontinuous positive coupling at `mathcal D_Q(F)`.

In particular, replacing the single `NB-124` margin by a finite vector

\[
(\mathfrak s_{F,q_1},\ldots,\mathfrak s_{F,q_m})
\]

and then applying a stable continuous combination cannot by itself force positive absolute-height Burnol mass throughout the formal zero-power representation class.

## 4. What two bases do and do not buy

The distinction with `NB-126` is now exact.

For multiplicatively independent bases such as `2` and `3`, the joint phase signature has **no exact nonzero alias**. With exact infinite-precision labelled root data, the ordinate is therefore identifiable. But the inverse is globally unstable: arbitrarily large ordinates return arbitrarily close to the same finite-base phase signature. Exact injectivity is not a quantitative height estimate.

This does not refute a theorem restricted to **actual zeta zeros**. The translated packets `(9)` are generally not zero packets, and the actual zero set may obey additional arithmetic/global constraints that forbid the matched recurrence. Nor does `(21)` exclude a deliberately singular or height-sensitive multibase certificate. A successful bridge could exploit, for example, an explicit quantitative anti-recurrence modulus, phase resolution that shrinks with the cutoff, a number of independent sampling scales that grows with the problem, the full natural-grid primitive, or an actual-zero relation coupling phase to zero density/zero-free information.

What `(21)` rules out is the simpler redirect suggested immediately after `NB-126`: **a fixed finite family of geometric bases is not, merely by removing exact aliases, a stable source of absolute ordinate information.** The missing theorem must quantify how close a high ordinate can return to the joint phase data at the accuracy demanded by near-perfect target capture, and then combine that quantitative phase defect with source-faithful information about actual zeros. For `q=2,3`, `(8)` shows that near-returns already occur at phase error `O(1/T)`, so any useful two-base argument must genuinely use the scale of the mismatch rather than only the fact that exact equality is impossible.

## 5. Adversarial and prior-art audit

Several possible overclaims were checked.

First, simultaneous near-aliasing does **not** restore the exact symmetry of `NB-126` for multiplicatively independent bases; the result is convergence, not equality. Second, the common shift preserves cross-base root correspondence rather than comparing two unrelated packets after forgetting which root is which. Third, confluent logarithmic powers cause no extra phase: `(17)` holds because the `(log q^k)^r` factor is unchanged by vertical translation. Fourth, the weighted annihilator coefficient norm is exactly invariant by `(12)--(13)`, while only the missing-root evaluation moves; no hidden Prony inversion is being assumed. Fifth, conjugation symmetry of a formal packet can be retained by translating `beta+i gamma` and `beta-i gamma` to `beta+i(gamma+T)` and `beta-i(gamma+T)` respectively; the same simultaneous recurrence controls the conjugate phases and both Burnol defects vanish. Sixth, the finding makes no assertion that arbitrary translated packets satisfy the global counting laws of actual zeta zeros.

The simultaneous-recurrence step is classical simultaneous Diophantine approximation, but the proof needed here is the elementary pigeonhole argument in Section 1, so no external approximation theorem is imported. A targeted prior-art search found neighboring multiscale Nyman--Beurling work, including a `2^{-j}3^{-k}` ladder formulation, and the classical signal-processing theme that multiple sampling rates remove exact aliases. No source located in that search supplies the specific zero-power conclusion `(21)`: finite multibase annihilator data can de-alias exactly while remaining globally unstable against Burnol absolute-height mass. No external theorem is load-bearing, so `SOURCES.md` needs no new anchor.

## Consequence

The frontier after `NB-126` is narrower than “use two independent bases.” Finite multibase recurrence geometry can identify an ordinate exactly but cannot stably coerce its absolute height through a fixed continuous certificate. The next source-faithful bridge must retain **quantitative joint phase mismatch at a resolution tied to the target-capture scale**, or use richer information whose complexity grows with the cutoff, before the `NB-125` annihilator budget can be coupled to the `NB-116` inverse-height Burnol mass.