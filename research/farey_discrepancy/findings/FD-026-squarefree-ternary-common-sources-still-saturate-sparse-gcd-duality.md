# FD-026 — squarefree-ternary common sources still saturate sparse GCD duality

**Status:** `EXACT-DERIVED + COMMON-SOURCE-CONSTRUCTION + EXACT-SQUAREFREE-TERNARY-INCREMENTS + POWER-ENVELOPE-CONTROL + RH-SCALE-DIAGONAL-CONTROL + SPARSE-HORIZON-SATURATION + NEGATIVE/OBSTRUCTION`.

`FD-007` shows that at one horizon the exact Möbius support/amplitude restrictions

\[
a_1=1,\qquad
a_n=0\ \text{if }n\text{ is nonsquarefree},\qquad
a_n\in\{-1,+1\}\ \text{if }n\text{ is squarefree}
\tag{1}
\]

do not improve the leading GCD-duality constant when the squarefree signs are otherwise free. `FD-024` shows that one unrestricted **common** real source can still saturate on every supermultiplicatively separated horizon sequence under any fixed power envelope strictly above `1/2`. `FD-025` then proves that the half-power threshold is genuine: every sublinear common source that saturates at any horizons must have endpoint size `omega(sqrt H)` there.

The two negative controls can be imposed simultaneously. Let

\[
A(x):=\sum_{n\le x}a_n,
\qquad
m_d^{(H)}:=A\!\left(\left\lfloor\frac Hd\right\rfloor\right),
\qquad
K_H(d,e):=\frac{\gcd(d,e)^2}{de},
\tag{2}
\]

and

\[
E_H:=(m^{(H)})^TK_Hm^{(H)},
\qquad
R_H:=\frac{A(H)^2}{E_H},
\tag{3}
\]

with `R_H:=0` when the horizon vector vanishes. Put

\[
Z:=\zeta(2).
\]

Then:

\[
\boxed{
\begin{minipage}{0.88\linewidth}
For every fixed `alpha>1/2` and every increasing integer horizon sequence
`H_0<H_1<...` with `H_j/H_(j-1)->infinity`, there is one infinite sequence
`a` satisfying (1) and
\[
|A(n)|\ll_\alpha n^\alpha
\]
such that
\[
R_{H_j}\longrightarrow Z.
\]
\end{minipage}}
\tag{4}
\]

There is also a diagonal endpoint strengthening. One can choose a single sequence satisfying (1) and a sufficiently sparse horizon sequence such that

\[
\boxed{
A(n)=O_\varepsilon\!\left(n^{1/2+\varepsilon}\right)
\quad\text{for every }\varepsilon>0,
\qquad
R_{H_j}\longrightarrow Z.
}
\tag{5}
\]

Thus the exact squarefree zero set, exact unit amplitude on every squarefree increment, one common infinite source, and even an RH-scale **family of growth envelopes** still do not force a persistent deficit from the sharp GCD coordinate constant on sufficiently sparse horizons if the squarefree signs themselves remain freely selectable. The residual cumulative rigidity must use information not present in (1) and (5): in particular the actual correlated law `mu(n)=(-1)^{omega(n)}` on squarefree integers, multiplicative ancestry, exact divisor consistency across the relevant horizons, or another source relation coupling those signs.

This is a negative classification of the free source model. It is not a bound for the physical Mertens function and does not improve the Franel--Landau exponent.

## 1. Equality prefixes need only long squarefree hyperbola intervals

For `R>=1`, write

\[
C_R:=(K_R^{-1})_{11},
\qquad
u^{(R)}:=K_R^{-1}e_1.
\tag{6}
\]

`FD-003` gives

\[
C_R\uparrow Z,
\qquad
(\nu^{(R)})^TK_R\nu^{(R)}=C_R,
\qquad
\nu_1^{(R)}=C_R,
\tag{7}
\]

and `FD-007`/`FD-024` give the uniform inverse-column estimate

\[
\boxed{
|\nu_d^{(R)}|\le\frac{Z^2}{d}
\qquad(1\le d\le R).
}
\tag{8}
\]

Fix a large horizon `H` and let

\[
q_d:=\left\lfloor\frac Hd\right\rfloor,
\qquad
I_d:=(q_{d+1},q_d]\cap\mathbb Z.
\tag{9}
\]

Write `L_d=|I_d|`. Then

\[
L_d\ge\frac{H}{d(d+1)}-1.
\tag{10}
\]

The elementary square-divisibility count used in `FD-007` can be localized to the upper endpoint of an interval. If `S_d` is the number of squarefree integers in `I_d`, then every nonsquarefree integer there is divisible by `k^2` for some `2<=k<=sqrt(q_d)`, so

\[
\begin{aligned}
L_d-S_d
&\le\sum_{2\le k\le\sqrt{q_d}}
\left(\frac{L_d}{k^2}+1\right)\\
&\le (Z-1)L_d+\sqrt{q_d}.
\end{aligned}
\tag{11}
\]

Hence

\[
\boxed{
S_d\ge(2-Z)L_d-\sqrt{q_d}.
}
\tag{12}
\]

If `R=R(H)` satisfies

\[
R\longrightarrow\infty,
\qquad
\frac{R^3}{H}\longrightarrow0,
\tag{13}
\]

then (10)--(12) imply a uniform positive-density estimate

\[
\boxed{
S_d\ge c_0L_d
\qquad(1\le d\le R)
}
\tag{14}
\]

for all sufficiently large `H`, with any fixed `c_0<(2-Z)`. Indeed

\[
\frac{\sqrt{q_d}}{L_d}
\ll\frac{d^{3/2}}{\sqrt H}
\le\frac{R^{3/2}}{\sqrt H}
=o(1).
\]

This is the only density input required below. No distribution theorem for the actual Möbius signs is used.

There is a second elementary ingredient. Let

\[
\mathsf Q(x):=\#\{n\le x:n\text{ is squarefree}\}.
\]

Every sequence satisfying (1) obeys

\[
A(x)\equiv\mathsf Q(x)\pmod2.
\tag{15}
\]

Conversely, on an interval containing `S` squarefree integers, any integer increment `Delta` with

\[
|\Delta|\le S,
\qquad
\Delta\equiv S\pmod2
\tag{16}
\]

is realized exactly by assigning `+1` to `(S+Delta)/2` of those squarefree points and `-1` to the rest. The signs can be ordered so that the intermediate cumulative sums never leave the interval between the two prescribed endpoint values by more than one. Thus endpoint interpolation and pointwise growth control can be handled simultaneously.

## 2. One exact squarefree-sign source saturates every prescribed supermultiplicative schedule under a fixed power envelope

Fix `alpha>1/2`. Choose

\[
\frac12<\gamma<\min\{\alpha,1\}
\tag{17}
\]

when `alpha<=1`, and any `gamma in (1/2,1)` when `alpha>1`; equivalently choose once and for all

\[
\frac12<\gamma<\min\{\alpha,1\}
\]

with the evident interpretation that the right endpoint is `1` for `alpha>=1`. Also choose

\[
0<\beta<\min\left\{1-\gamma,\frac13\right\}.
\tag{18}
\]

Let

\[
\rho_j:=\frac{H_j}{H_{j-1}},
\qquad
R_j:=\left\lfloor
\min\left\{H_j^\beta,\frac{\rho_j}{16}\right\}
\right\rfloor.
\tag{19}
\]

On a sufficiently late tail,

\[
R_j\to\infty,
\qquad
R_j^3/H_j\to0,
\qquad
H_j^{\gamma-1}R_j\to0,
\tag{20}
\]

and

\[
q_{R_j+1}^{(j)}
:=\left\lfloor\frac{H_j}{R_j+1}\right\rfloor
>H_{j-1}.
\tag{21}
\]

A finite initial segment of the squarefree signs can therefore be assigned arbitrarily, for example by alternating signs in increasing squarefree order, and every later stage works only with fresh source positions above the preceding horizon.

At stage `j`, abbreviate `H=H_j`, `R=R_j`, and set

\[
t:=\frac{H^\gamma}{32Z^2}.
\tag{22}
\]

For `1<=d<=R`, choose an integer `y_d` with the forced parity

\[
y_d\equiv\mathsf Q(q_d)\pmod2
\tag{23}
\]

and

\[
\boxed{|y_d-t\nu_d^{(R)}|\le1.}
\tag{24}
\]

Also choose

\[
y_{R+1}\in\{0,1\},
\qquad
y_{R+1}\equiv\mathsf Q(q_{R+1})\pmod2.
\tag{25}
\]

The bridge interval `(H_(j-1),q_(R+1)]` contains a positive proportion of squarefree integers and has length comparable to `q_(R+1)`, while the induction below keeps `A(H_(j-1))=O(H_(j-1)^gamma)`. Since `q_(R+1)` is a fixed multiple larger than `H_(j-1)` and `gamma<1`, eventually there are more than enough fresh squarefree signs to move the old endpoint exactly to (25), with the required parity.

For a hyperbola interval `I_d`, (8) and (24) give

\[
|y_d-y_{d+1}|
\le
\frac{2Z^2t}{d}+2
\ll\frac{H^\gamma}{d}+1.
\tag{26}
\]

On the other hand (10), (14), and (20) give

\[
S_d\gg\frac{H}{d^2},
\qquad
\frac{H^\gamma/d}{H/d^2}
=H^{\gamma-1}d
\le H^{\gamma-1}R=o(1).
\tag{27}
\]

Thus (16) applies in every `I_d`: all squarefree integers are assigned signs `+-1`, all nonsquarefree increments remain zero, and telescoping gives

\[
\boxed{A(q_d)=y_d\qquad(1\le d\le R).}
\tag{28}
\]

Repeating this stage inductively defines **one infinite sequence** satisfying the exact support/amplitude law (1), rather than a different finite witness at each horizon.

The same sign ordering gives a polynomial envelope. On `I_d`, every `n` satisfies `n>H/(d+1)`, while (8), (22), and (24) give

\[
|y_d|\le\frac{H^\gamma}{32d}+1.
\tag{29}
\]

Since `gamma<1`, the right side is a fixed small multiple of `n^gamma` uniformly for `d<=R`, apart from an eventually negligible additive constant. Ordering the signs as in Section 1 keeps all intermediate partial sums between the endpoint magnitudes up to one. On the fresh bridge, order the signs first to move monotonically toward the parity-compatible value in `{0,1}` and then in canceling pairs; this never creates a new large excursion. Induction therefore yields

\[
\boxed{|A(n)|\ll_\gamma n^\gamma.}
\tag{30}
\]

Because `gamma<alpha`, (30) implies the announced `O_alpha(n^alpha)` envelope.

## 3. The squarefree rounding error and inherited tail are negligible in GCD energy

At a stage horizon `H`, pad `nu^(R)` by zero coordinates through `H` and denote the result by `\widetilde\nu`. Equations (24) and (28) give

\[
m^{(H)}=t\widetilde\nu+z,
\tag{31}
\]

where

\[
|z_d|\le1\quad(d\le R),
\qquad
|z_d|=|A(\lfloor H/d\rfloor)|\ll_\gamma(H/d)^\gamma
\quad(d>R).
\tag{32}
\]

The bounded prefix rounding has small GCD norm. `FD-007` proves

\[
\mathbf1^TK_R\mathbf1\ll R,
\]

so

\[
\|z_{\le R}\|_{K_H}=O(\sqrt R).
\tag{33}
\]

For the tail, the weighted GCD estimate of `FD-024` gives, for every `gamma>1/2`,

\[
\|z_{>R}\|_{K_H}^2
\ll_\gamma
H^{2\gamma}R^{1-2\gamma}.
\tag{34}
\]

The triangle inequality in the positive-definite `K_H` norm, (22), and `R->infinity` therefore imply

\[
\boxed{
\frac{\|z\|_{K_H}}{t}
\ll_\gamma
\frac{\sqrt R}{H^\gamma}
+R^{1/2-\gamma}
\longrightarrow0.
}
\tag{35}
\]

The top-left `R x R` block of `K_H` is exactly `K_R`, hence

\[
\|\widetilde\nu\|_{K_H}^2=C_R.
\tag{36}
\]

Also

\[
A(H)=m_1=tC_R+O(1).
\tag{37}
\]

Cauchy--Schwarz now gives

\[
E_H=t^2(C_R+o(1)),
\]

and therefore

\[
\boxed{R_H=C_R+o(1).}
\tag{38}
\]

Since `R=R_j->infinity` and `C_R->Z`, equation (4) follows.

The conclusion is stronger than either input control separately. `FD-007` used a different finite sign sequence for each horizon; `FD-024` used one common source but allowed arbitrary real increments. Here the same infinite source has the exact squarefree-supported ternary increment law at every integer and still asymptotically realizes the unrestricted coordinate constant on every prescribed schedule with diverging multiplicative gaps.

## 4. A diagonal construction also survives all `1/2+epsilon` growth envelopes

The fixed-power theorem still chooses a different source when `alpha` changes. One can diagonalize the construction if the horizon schedule itself may be chosen sufficiently sparse.

Suppose the source has already been assigned through a horizon `H_*`, and put

\[
B_*:=\max_{n\le H_*}|A(n)|.
\tag{39}
\]

Choose the next horizon `H` so large that, with

\[
L(H):=\exp(\!\sqrt{\log H}),
\qquad
R:=\lfloor H^{1/5}\rfloor,
\tag{40}
\]

one has

\[
q_{R+1}>H_*,
\qquad
L(H)\ge j(B_*+2),
\tag{41}
\]

at stage `j`. Such an `H` always exists. Set

\[
t:=\frac{\sqrt H\,L(H)}{32Z^2}.
\tag{42}
\]

The same parity construction as in Section 2 is feasible. Indeed every hyperbola interval with `d<=R` contains `gg H^{3/5}` squarefree integers by (10)--(14), while the required endpoint change is at most

\[
O(t)=H^{1/2+o(1)}=o(H^{3/5}).
\tag{43}
\]

The fresh bridge can again reset the old endpoint to a parity-compatible value in `{0,1}` because its length tends to infinity much faster than the fixed previous amplitude.

At the new horizon, every tail coordinate `d>R` samples an index at most `q_(R+1)`. On the fresh bridge the cumulative sums can be kept bounded by `max{|A(H_*)|,2}`, and below `H_*` they are bounded by `B_*`. Hence

\[
|z_d|\le B_*+2
\qquad(d>R).
\tag{44}
\]

Using again `\mathbf1^TK_H\mathbf1\ll H`, now on the full tail rather than a power-weighted estimate,

\[
\|z_{>R}\|_{K_H}\ll(B_*+2)\sqrt H.
\tag{45}
\]

Together with the `O(sqrt R)` rounding norm,

\[
\frac{\|z\|_{K_H}}{t}
\ll
\frac{B_*+2}{L(H)}
+\frac{\sqrt R}{\sqrt H\,L(H)}
\le O(1/j)+o(1).
\tag{46}
\]

Thus the same argument as (36)--(38) gives

\[
R_H=C_R+o(1)\to Z
\tag{47}
\]

along the recursively chosen horizons.

It remains to verify that the resulting source has the promised RH-scale growth. At the planted hyperbola endpoints,

\[
|A(q_d)|
\le\frac{\sqrt H\,L(H)}{32d}+1.
\tag{48}
\]

For `d<=H^(1/5)`, every integer in `I_d` is at least of order `H^(4/5)`, so

\[
L(H)=e^{\sqrt{\log H}}
\le e^{2\sqrt{\log n}}
\tag{49}
\]

for all sufficiently large `H` and every such `n`. The interval sign ordering introduces only a unit overshoot beyond the endpoint range. On the bridge, the source never exceeds the already-controlled preceding endpoint scale. Induction therefore gives a global bound of the form

\[
\boxed{
|A(n)|\ll\sqrt n\,e^{2\sqrt{\log n}}.
}
\tag{50}
\]

Since

\[
e^{2\sqrt{\log n}}=O_\varepsilon(n^\varepsilon)
\qquad(\varepsilon>0),
\tag{51}
\]

this proves (5).

The diagonal source necessarily has super-square-root values at the saturating horizons:

\[
|A(H_j)|\asymp\sqrt{H_j}\,e^{\sqrt{\log H_j}},
\tag{52}
\]

up to the bounded `C_R/Z` factor and rounding. This is exactly consistent with the horizon-free necessity in `FD-025`; the construction approaches the half-power boundary from above without crossing it.

## 5. What arithmetic information is still missing

The construction now survives four restrictions simultaneously:

1. there is one common source across all retained horizons;
2. every nonsquarefree increment is exactly zero;
3. every squarefree increment has exactly unit modulus and `a_1=1`;
4. the cumulative source can obey either any prescribed fixed `1/2+delta` power envelope on every supermultiplicative schedule, or all `1/2+epsilon` envelopes simultaneously on a sufficiently sparse schedule.

The freedom that remains is the **choice of signs at squarefree integers**. For the actual Möbius function those signs are not free:

\[
\mu(n)=(-1)^{\omega(n)}
\qquad(n\text{ squarefree}),
\tag{53}
\]

and they participate in exact divisor identities at every horizon. The present source generally violates that multiplicative/sign-correlation law and does not claim to satisfy the fixed-horizon divisor identity of `FD-008` at the retained horizons.

This identifies a sharper boundary for the current cumulative program. A future theorem cannot obtain a GCD-duality deficit merely from common-source coherence, sparsity restrictions, pointwise squarefree support, ternary amplitude, or RH-scale endpoint growth. It must fail on the sources constructed here for a reason traceable to **correlated arithmetic signs or exact cross-horizon divisor compatibility**. Equivalently, replacing the true Möbius signs by independent squarefree signs remains too large a relaxation even after the strongest growth control normally associated with the RH exponent is restored.

This does not close ordered Farey routes before the `FD-002`/`FD-003` cumulative compression. It only tightens the source-side boundary after that compression has already occurred.

## 6. Prior-art and novelty boundary

The load-bearing ingredients are already canonical in this line: Smith/Jordan factorization and the sharp coordinate ray (`FD-003`), exact squarefree-sign interpolation on long hyperbola intervals (`FD-007`), the weighted GCD tail estimate above exponent `1/2` (`FD-024`), and the half-power obstruction (`FD-025`). The local squarefree count (11)--(14) is elementary and is proved here rather than imported from a distribution theorem.

A targeted literature audit checked Farey/Mertens discrepancy, GCD-matrix extremality, arbitrary signs supported on squarefree integers, and multiplicative squarefree-supported discrepancy. The closest neighboring result remains Marco Aymone, *The Erdős discrepancy problem over the squarefree and cubefree integers*, Mathematika **68** (2022), 51--73, DOI `10.1112/mtk.12117`, which studies squarefree-supported signs under **complete multiplicativity** and proves unboundedness phenomena. That hypothesis is precisely absent here: the construction needs independent sign choice on fresh squarefree intervals. No directly matching theorem about a single squarefree-ternary source saturating the Farey--Mertens GCD coordinate constant across sparse horizons was located. Search absence is not used as a novelty proof, and no new external theorem is needed for the derivation, so `SOURCES.md` does not require a new load-bearing anchor.

The Mathia-specific delta is the simultaneous intersection of the previous relaxations: `FD-007` was finite-horizon, while `FD-024`/`FD-025` treated common real sources without exact Möbius support/amplitude. Equations (4)--(5) show that putting those restrictions together still leaves the leading GCD-duality obstruction intact.

## 7. Stress tests, falsification controls, and consequences

Several conditions are essential. The arbitrary-schedule theorem (4) gives one fixed exponent above `1/2`; it does **not** say that the same source satisfies all `1/2+epsilon` envelopes on every prescribed supermultiplicative schedule. The simultaneous family (5) uses a horizon sequence chosen recursively sparse enough to dominate the inherited finite source. Conflating these two quantifier orders would materially strengthen the theorem without proof.

The squarefree signs are exact, not a real-valued relaxation. Parity (15)--(16) is what makes every prescribed integer endpoint realizable. The condition `R^3/H->0` is what makes the elementary squarefree count uniform across all planted hyperbola intervals, while `H^(gamma-1)R->0` makes their sign capacity dominate the required equality-ray jumps. The bridge freshness condition prevents later stages from altering earlier source values.

The energy argument includes the whole inherited tail. In the fixed-power construction it is controlled by the `FD-024` weighted tail estimate; in the diagonal construction it is bounded by the actual previous maximum and `1^TK_H1<<H`. No unassigned squarefree integer is silently set to zero.

A decisive falsification would be one of the following: failure of the parity/capacity inequalities in some planted interval, a hidden collision `q_(R+1)<=H_(j-1)` on the chosen tail, a source value violating the claimed global envelope, or a non-negligible `K_H` perturbation contradicting (35) or (46). Each point is explicit in the construction and uses only finite sign assignment plus the already-proved GCD estimates.

No RH improvement follows. The durable conclusion is a stronger **no-free-gain boundary**: even one infinite source with the exact squarefree zero pattern, exact ternary amplitudes, and RH-scale cumulative growth can asymptotically saturate the unrestricted Franel--Mertens GCD coordinate geometry on sufficiently sparse horizons. What remains genuinely arithmetic is the correlated Möbius sign law and the divisor/multiplicative compatibility tying those signs together.