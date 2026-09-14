# FD-119 — fixed Mertens endpoint data cost only bounded energy on the floor-quotient Fourier skeleton

**Status:** `EXACT-DERIVED + FLOOR-QUOTIENT-FOURIER-SKELETON + FIXED-ENDPOINT-REPAIR + BOUNDED-ENERGY-COUNTERMODEL + NEGATIVE/ROUTE-RESTRICTION`.

`FD-118` leaves a precise quantitative question after the information-equivalence collapse of `FD-117`: perhaps the minimal divisor-closed Fourier skeleton, although carrying no new source information, has a coercive geometry that forces the physical quotient-Mertens vector away from first-mode saturation at the RH-critical scale.

The most immediate physical endpoint constraints do not do this. On the `FD-118` skeleton there is an exact formal Möbius equality ray that kills every mode except the first. Imposing any **fixed** initial segment of the true Mertens values, and also imposing the exact floor-quotient identity

\[
\sum_{d\le N}M\!\left(\left\lfloor\frac Nd\right\rfloor\right)=1,
\tag{1}
\]

can be repaired from that equality ray by changing only finitely many source coordinates at indices of size `Theta(N)`. Those repairs cost only `O_R(1)` in the normalized skeleton energy.

More precisely, fix `R>=1`. Let

\[
\mathcal Q_N
=
\left\{\left\lfloor\frac Nm\right\rfloor:1\le m\le N\right\},
\qquad
\tau_N(k)=\left\lfloor\frac Nk\right\rfloor,
\tag{2}
\]

and let `m_N` be any real target amplitude satisfying

\[
|m_N|\log N=o(N).
\tag{3}
\]

For every sufficiently large `N` there exists a real formal quotient source

\[
y^{(N)}=(y_r)_{r\in\mathcal Q_N}
\tag{4}
\]

such that

\[
y_N=m_N,
\qquad
y_r=M(r)\quad(1\le r\le R),
\tag{5}
\]

and the exact physical divisor identity is also satisfied:

\[
\boxed{
\sum_{d=1}^N y_{\lfloor N/d\rfloor}=1.
}
\tag{6}
\]

Define the skeleton Fourier coordinates by the same finite transform as `FD-118`,

\[
A_y(k)
:=
\sum_{d\mid k}
 d\,y_{\tau_N(d)},
\qquad k\in\mathcal Q_N,
\tag{7}
\]

and its native normalized quadratic energy

\[
\mathcal E_N^{\mathcal Q}(y)
:=
\sum_{k\in\mathcal Q_N}
\frac{|A_y(k)|^2}{k^2}.
\tag{8}
\]

Then the source can be chosen so that

\[
\boxed{
\mathcal E_N^{\mathcal Q}(y)
=
m_N^2+O_R(1).
}
\tag{9}
\]

The implicit constant is uniform in `N` and in target families satisfying (3). In particular, choosing `m_N=floor(sqrt(N))` gives

\[
\boxed{
\frac{\mathcal E_N^{\mathcal Q}(y)}{m_N^2}
=1+O_R(N^{-1})
\longrightarrow1.
}
\tag{10}
\]

Thus the minimal `2 sqrt(N)+O(1)` Fourier carrier cannot acquire a fixed relative coercivity gap at the RH-critical amplitude merely from `M(1),...,M(R)` for fixed `R` plus the exact identity (1). Any such gap must use arithmetic information whose depth grows with the horizon, or another restriction not captured by fixed endpoint data and one global floor-quotient compatibility.

## 1. The skeleton has an exact Möbius equality ray

Reindex a formal quotient source by

\[
x_k:=y_{\tau_N(k)},
\qquad k\in\mathcal Q_N.
\tag{11}
\]

`FD-118` proves that `\mathcal Q_N` is divisor-closed and that `\tau_N` is an involution. Equation (7) becomes

\[
A_y(k)=\sum_{d\mid k}d\,x_d.
\tag{12}
\]

Ordinary divisor Möbius inversion stays inside `\mathcal Q_N`:

\[
kx_k
=
\sum_{d\mid k}\mu(k/d)A_y(d).
\tag{13}
\]

For any real `m`, set

\[
\boxed{
x_k^{(0)}=m\frac{\mu(k)}k.}
\tag{14}
\]

Then

\[
A^{(0)}(1)=m,
\qquad
A^{(0)}(k)
=m\sum_{d\mid k}\mu(d)=0
\quad(k>1).
\tag{15}
\]

Hence

\[
\boxed{\mathcal E_N^{\mathcal Q}(y^{(0)})=m^2.}
\tag{16}
\]

This is not itself the new obstruction: it is the expected equality ray of the invertible divisor transform in `FD-118`. The issue is whether simple physical constraints destroy it at a power-relevant cost. Sections 2--3 show that fixed endpoint information does not.

For completeness, if `Z_{\mathcal Q}` is the divisor-zeta matrix on `\mathcal Q_N`, `Delta=diag(k)` and `W=diag(k^{-2})`, the Gram matrix of (8) in the `x` coordinates is

\[
G_{\mathcal Q}
=\Delta Z_{\mathcal Q}^{T}WZ_{\mathcal Q}\Delta.
\tag{17}
\]

Because `Z_{\mathcal Q}` is unit triangular,

\[
\boxed{\det G_{\mathcal Q}=1,}
\tag{18}
\]

and (14) is exactly `G_{\mathcal Q}^{-1}e_1` up to scale. Thus the sharp unrestricted inequality is only

\[
x_1^2\le\mathcal E_N^{\mathcal Q}(x),
\tag{19}
\]

with equality on (14).

## 2. A fixed true Mertens prefix is a bounded-energy perturbation

Fix `r`. For sufficiently large `N`, `r<=sqrt(N)`, so `r\in\mathcal Q_N`. Let

\[
k_r:=\tau_N(r)=\left\lfloor\frac Nr\right\rfloor.
\tag{20}
\]

By involutivity, changing `y_r` by `delta` is exactly the same as changing `x_{k_r}` by `delta`. Starting from (14) with `m=m_N`, the baseline endpoint value is

\[
y_r^{(0)}
=
x_{k_r}^{(0)}
=
m_N\frac{\mu(k_r)}{k_r}.
\tag{21}
\]

For fixed `r`, condition (3) implies in particular `m_N/k_r=o(1)`, because `k_r~N/r`. Therefore the correction required to impose the true fixed value `M(r)` is

\[
\delta_r
:=
M(r)-y_r^{(0)}
=O_R(1)
\qquad(1\le r\le R).
\tag{22}
\]

A correction at `x_{k_r}` changes `A_y(k)` only when `k_r|k`. If `k=jk_r<=N`, then

\[
j\le\left\lfloor\frac N{k_r}\right\rfloor=r,
\tag{23}
\]

again by `tau_N(k_r)=r`. Hence its normalized Fourier-energy norm is bounded by

\[
\sum_{\substack{k\in\mathcal Q_N\\k_r\mid k}}
\left|\frac{k_r\delta_r}{k}\right|^2
\le
|\delta_r|^2\sum_{j\le r}\frac1{j^2}
\le
\zeta(2)|\delta_r|^2.
\tag{24}
\]

Only `R` such corrections are made. By the triangle inequality in the weighted Fourier `l^2` norm, their combined cost is `O_R(1)`. They do not alter `A_y(1)=m_N`, because every `k_r>1` for fixed `r` and sufficiently large `N`.

Thus the complete exact Mertens prefix

\[
M(1),M(2),\ldots,M(R)
\tag{25}
\]

can be grafted onto the formal equality ray at bounded energy cost. In particular this includes the terminal physical condition `M(1)=1`, which by itself cannot create a critical-scale gap.

## 3. The exact divisor identity is also repairable at bounded cost

For `r\in\mathcal Q_N`, let

\[
c_N(r)
:=
\#\left\{d\le N:\left\lfloor\frac Nd\right\rfloor=r\right\}
=
\left\lfloor\frac Nr\right\rfloor
-
\left\lfloor\frac N{r+1}\right\rfloor.
\tag{26}
\]

Then the left side of (6) is

\[
\sum_{r\in\mathcal Q_N}c_N(r)y_r.
\tag{27}
\]

First bound this functional on the unperturbed equality ray. Since `tau_N(r)=floor(N/r)>=N/(2r)`, one has

\[
\begin{aligned}
\left|
\sum_{r\in\mathcal Q_N}
 c_N(r)y_r^{(0)}
\right|
&\le
|m_N|
\sum_{r\in\mathcal Q_N}
\frac{c_N(r)}{\tau_N(r)}\\
&\le
\frac{2|m_N|}{N}
\sum_{r\in\mathcal Q_N}r c_N(r).
\end{aligned}
\tag{28}
\]

But grouping integers `d<=N` by `floor(N/d)` gives

\[
\sum_{r\in\mathcal Q_N}r c_N(r)
=
\sum_{d\le N}\left\lfloor\frac Nd\right\rfloor
\le
N(1+\log N).
\tag{29}
\]

Therefore the baseline value in (27) is

\[
O\!\left(|m_N|\log N\right)=o(N)
\tag{30}
\]

by (3). The fixed-prefix corrections from Section 2 contribute at most `O_R(N)`, since each fixed `c_N(r)=O_R(N)` and each `delta_r=O_R(1)`.

Now reserve the next endpoint `r_0=R+1`, which also belongs to `\mathcal Q_N` for all sufficiently large `N`. Its block weight satisfies

\[
c_N(r_0)
=
\frac{N}{r_0(r_0+1)}+O_R(1)
=
\Theta_R(N).
\tag{31}
\]

After the prefix corrections, choose one additional correction `delta_{r_0}` so that (27) becomes exactly `1`. Equations (30)--(31) give

\[
\boxed{\delta_{r_0}=O_R(1).}
\tag{32}
\]

The same support calculation (23)--(24), now with `r=r_0`, shows that this final exact repair also costs only `O_R(1)` in the skeleton energy. This proves (5)--(9).

The construction is intentionally a relaxation. Except at the fixed endpoints (5) and in the global identity (6), the resulting `y_r` are not claimed to be actual Mertens values. That is precisely the falsification role: any proposed coercivity proof using only those constraints must also hold for this synthetic source, and therefore cannot force a fixed relative gap at `m_N~sqrt(N)`.

## 4. A sharp one-endpoint calculation shows the same scale

There is also an exact finite calculation behind the bounded-cost phenomenon. Keep only the physical condition `y_1=M(1)=1` and fix the target `y_N=m`. In the `x` coordinates these are

\[
x_N=1,
\qquad x_1=m.
\tag{33}
\]

Applying (13) at `k=N` gives the linear constraint

\[
\sum_{\substack{d\mid N\\d>1}}
\mu(N/d)A_y(d)
=
N-\mu(N)m.
\tag{34}
\]

Weighted Cauchy--Schwarz is sharp here. Among all real formal sources satisfying (33), the exact minimum skeleton energy is

\[
\boxed{
\min \mathcal E_N^{\mathcal Q}
=
m^2+
\frac{(N-\mu(N)m)^2}{T_N},
}
\tag{35}
\]

where

\[
T_N
:=
\sum_{\substack{d\mid N\\d>1}}
\mu(N/d)^2d^2
=
N^2\prod_{p\mid N}(1+p^{-2})-\mu(N)^2.
\tag{36}
\]

Equality is attained by taking all nondivisor skeleton modes zero and the divisor modes proportional to `mu(N/d)d^2`, so (35) is a true sharp relaxation, not merely a lower bound.

For the actual target `m=M(N)`, the numerator in (35) cannot vanish at large scale for a trivial physical reason. If `mu(N)=0`, it equals `N`. If `mu(N)=\pm1`, then

\[
N-\mu(N)M(N)
=
\sum_{n\le N}\left(1-\mu(N)\mu(n)\right)
\ge
\left\lfloor\frac N4\right\rfloor,
\tag{37}
\]

because every multiple of `4` has `mu(n)=0`. Also

\[
N^2\le T_N
<
N^2\prod_p(1+p^{-2})
=
\frac{15}{\pi^2}N^2.
\tag{38}
\]

Thus the terminal endpoint alone forces a strict **additive** energy gap, but only of constant size:

\[
\frac{\pi^2}{15}
\left(\frac{\lfloor N/4\rfloor}{N}\right)^2
\le
\frac{(N-\mu(N)M(N))^2}{T_N}
\le 4.
\tag{39}
\]

The lower bound tends `pi^2/240`, while the sharp endpoint-only excess is uniformly `O(1)`. This makes the scale failure explicit: the endpoint normalization genuinely breaks exact equality, but it breaks it far below the `Theta(N)` energy scale corresponding to a square-root-sized target.

## 5. Consequence for the current Farey frontier

`FD-117`--`FD-118` separate information from proof geometry: the complete cumulative discrepancy field is Mertens-equivalent, and a divisor-closed `2 sqrt(N)+O(1)` Fourier skeleton already carries that source exactly. The present result tests the first natural hope for extra proof geometry on that skeleton.

The answer is negative at fixed arithmetic depth. The native positive Fourier norm has an exact Möbius equality ray. The physical endpoint `M(1)=1` breaks the ray only by `O(1)` energy, and any fixed number of further exact Mertens endpoint values can be imposed with the same bounded cost. Even adding the exact global floor-quotient identity (1) still leaves synthetic critical-scale sources with

\[
\mathcal E_N^{\mathcal Q}
=
m_N^2+O_R(1)
=
N+o(N)
\tag{40}
\]

whenever `m_N~sqrt(N)`.

Therefore a useful coercivity theorem for the minimal skeleton must consume a **growing-depth** feature of the physical Mertens trajectory: bounded increments over a growing range, the squarefree/multiplicative sign law, growing divisor compatibility, cross-horizon coherence, or another arithmetic restriction strong enough to make departure from the Möbius equality ray cost a positive fraction of the critical energy. Fixed endpoint normalization and one global identity are not enough.

This also clarifies the role of redundant Fourier measurements. `FD-003` obtains a finite generic improvement from the complete infinite Fourier/Franel energy, while the minimal divisor-closed carrier has the exact equality ray above. Redundant modes can therefore add coercivity without adding source information. What remains to be shown is whether that coercivity can become power-relevant on the **physical** arithmetic source; `FD-003`--`FD-008` already show that several broad relaxations still leave its leading scalar constant sharp.

## 6. Checks, prior art, and evidence boundary

The divisor-closure/involution statements and the Farey Fourier transform are inherited from `FD-118`. The identity (1) is the classical Möbius floor-quotient relation already used in `FD-004`--`FD-005` and anchored in `SOURCES.md`. Divisor Möbius inversion, incidence matrices and their triangularity are classical. A targeted literature audit across divisor-incidence/Möbius matrices, Farey Fourier transforms, and Mertens floor-quotient formulas found neighboring matrix and inversion literature but no reason to claim novelty for any of these ingredients. No external theorem is load-bearing for the bounded-repair argument, so no new source anchor is required.

As finite regression checks, exact arithmetic verified `det(G_Q)=1` and `G_Q^{-1}e_1=(mu(k)/k)_(k in Q_N)` for representative horizons through `N=1000`. These checks are not part of the proof.

Several boundaries are essential. The construction is a **formal source countermodel**, not an alternative Möbius function. It preserves a fixed true Mertens prefix and one exact global identity, but not integrality of every quotient value, the bounded-increment law, squarefree support, multiplicativity, or all cross-horizon identities. The depth `R` is fixed; allowing `R=R(N)` to grow may accumulate non-negligible energy and is precisely one remaining route. Finally, (9) does not say the actual Farey skeleton energy is close to `M(N)^2`; it says that such closeness cannot be excluded from the stated fixed-depth constraints alone.

The durable conclusion is a quantitative no-free-gain boundary for the current minimal carrier: **fixed endpoint arithmetic can break the formal Möbius equality ray, but only at bounded energy cost. Any RH-critical coercivity must come from arithmetic structure whose effective depth grows with the horizon.**
