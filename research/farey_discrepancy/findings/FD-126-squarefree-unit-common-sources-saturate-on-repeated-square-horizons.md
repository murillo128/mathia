# FD-126 — squarefree-unit common sources still saturate on repeated-square horizons

**Status:** `EXACT-DERIVED + FLOOR-QUOTIENT-FOURIER-SKELETON + HORIZON-INDEPENDENT-SQUAREFREE-SIGNS + SQUARE-ROOT-ENVELOPE + SUPEREXPONENTIAL-SPARSE-SATURATION + NEGATIVE/ROUTE-RESTRICTION`.

`FD-125` leaves one explicit weakness in its repeated-square common-source countermodel: the cumulative source is coherent across horizons, but its increments need not have the physical Möbius support/amplitude law. That weakness is not enough to close the sparse escape. There exists a **single infinite squarefree-supported unit-sign sequence** whose cumulative source still asymptotically saturates the `FD-118`/`FD-120` floor-quotient Fourier skeleton along a repeated-square chain.

Let

\[
a(1)=1,
\qquad
a(n)=0\quad(n\text{ nonsquarefree}),
\qquad
a(n)\in\{-1,+1\}\quad(n\text{ squarefree}),
\tag{1}
\]

and

\[
Y(x):=\sum_{n\le x}a(n).
\tag{2}
\]

For a horizon `H`, retain

\[
\mathcal Q_H
:=
\left\{\left\lfloor\frac Hm\right\rfloor:1\le m\le H\right\},
\qquad
\tau_H(k):=\left\lfloor\frac Hk\right\rfloor,
\tag{3}
\]

\[
A_H(k):=\sum_{d\mid k}d\,Y(\tau_H(d)),
\qquad
\mathcal E_H^{\mathcal Q}(Y)
:=
\sum_{k\in\mathcal Q_H}\frac{|A_H(k)|^2}{k^2}.
\tag{4}
\]

There are an integer `H_0` and one sequence `a` satisfying (1) such that, for

\[
H_{j+1}=H_j^2,
\tag{5}
\]

one has globally

\[
\boxed{|Y(n)|\ll\sqrt n,}
\tag{6}
\]

and at every retained horizon there is an integer `t_j` with

\[
t_j\equiv \#\{n\le H_j:n\text{ squarefree}\}\pmod2,
\qquad
|t_j-\sqrt{H_j}|\le1,
\qquad
Y(H_j)=t_j,
\tag{7}
\]

such that

\[
\boxed{
\mathcal E_{H_j}^{\mathcal Q}(Y)
=
t_j^2
+O\!\left(H_j^{3/4}(\log H_j)^2\right).
}
\tag{8}
\]

Consequently

\[
\boxed{
\frac{\mathcal E_{H_j}^{\mathcal Q}(Y)}{|Y(H_j)|^2}
=1+O\!\left(H_j^{-1/4}(\log H_j)^2\right)
\longrightarrow1.
}
\tag{9}
\]

Thus the combination

- one horizon-independent source;
- exact squarefree support;
- exact unit amplitudes on every squarefree increment;
- `a(1)=1`;
- a global square-root envelope;

still does **not** force a positive pointwise relative gap on the minimal Fourier skeleton at sufficiently sparse horizons. The remaining arithmetic resource is narrower than `FD-125` left open: it must use the actual correlation of the Möbius signs, a growing family of exact divisor identities, multiplicative compatibility, or another law not implied by support and unit amplitude alone.

## 1. A squarefree supply lemma at square-root length

Write

\[
Q_{\rm sf}(x):=\#\{n\le x:n\text{ squarefree}\}.
\tag{10}
\]

The elementary identity

\[
1_{\rm sf}(n)=\sum_{d^2\mid n}\mu(d)
\tag{11}
\]

gives

\[
Q_{\rm sf}(x)
=
\sum_{d\le\sqrt x}\mu(d)\left\lfloor\frac{x}{d^2}\right\rfloor
=
\frac{x}{\zeta(2)}+O(\sqrt x).
\tag{12}
\]

Indeed the floor errors contribute `O(sqrt(x))`, and extending
`sum_(d<=sqrt(x)) mu(d)/d^2` to infinity also costs `O(x/sqrt(x))`.
Therefore there is an absolute constant `C_0` such that, for all sufficiently large `x`, every interval

\[
[x,x+C_0\sqrt x]
\tag{13}
\]

contains at least `c_0 sqrt(x)` squarefree integers for some absolute `c_0>0`. The same holds for a left window `[x-C_0 sqrt(x),x]` once `x` is large. Only this coarse local supply is needed below.

The point of the `sqrt(x)` window is not sharp squarefree-gap theory. It is exactly long enough for the elementary counting error in (12), while still short enough that the cumulative `L^2` cost of the ramps constructed below is `O(H^(3/2))`.

## 2. Stagewise extension of one permanent sign sequence

Assume the legal signs have been fixed through a retained horizon

\[
L=H_{j-1},
\qquad
Y(L)=t_{j-1}=\sqrt L+O(1),
\tag{14}
\]

and put

\[
H=L^2,
\qquad
R=\lfloor H^{1/4}\rfloor,
\qquad
q_k=\left\lfloor\frac Hk\right\rfloor,
\qquad
Q=q_{R+1}.
\tag{15}
\]

Then

\[
Q\asymp H^{3/4}=L^{3/2}\gg L.
\tag{16}
\]

First extend the signs over `(L,Q]`. Using the squarefree supply lemma in a window of length `O(sqrt(L))`, choose signs opposite to the current cumulative value until `|Y|<=1`; any unused squarefree positions in that window can be paired with opposite signs. Thereafter alternate signs on successive squarefree positions. Hence

\[
|Y(n)|\le1
\quad\text{for all but an initial }O(\sqrt L)\text{-window in }(L,Q],
\tag{17}
\]

while throughout that initial reset window

\[
|Y(n)|\ll\sqrt L.
\tag{18}
\]

Now choose the current terminal amplitude `t=t_j` to be the integer of the forced squarefree parity nearest `sqrt(H)`, so

\[
|t-\sqrt H|\le1.
\tag{19}
\]

For `1<=k<=R`, choose an integer `y_k` satisfying the parity forced at `q_k` and

\[
y_1=t,
\qquad
\left|y_k-t\frac{\mu(k)}k\right|\le1
\quad(2\le k\le R).
\tag{20}
\]

Set

\[
y_{R+1}:=Y(Q).
\tag{21}
\]

Because every legal squarefree sign is congruent to `1 mod 2`, the parity of `Y(x)` is exactly `Q_sf(x) mod 2`. Thus

\[
y_k-y_{k+1}
\equiv
Q_{\rm sf}(q_k)-Q_{\rm sf}(q_{k+1})
\pmod2,
\tag{22}
\]

which is precisely the parity condition for realizing the required net change inside

\[
I_k=(q_{k+1},q_k]\cap\mathbb Z.
\tag{23}
\]

Moreover

\[
|I_k|\asymp\frac{H}{k^2},
\qquad
|y_k-y_{k+1}|\ll\frac{\sqrt H}{k}+1.
\tag{24}
\]

For `k<=R`, the interval therefore contains far more squarefree positions than are needed for the net displacement.

To control the values between endpoints, use two short square-root windows inside each `I_k`. In a lower window of length

\[
O\!\left(\sqrt{q_{k+1}}\right)
=O\!\left(\sqrt{H/k}\right),
\tag{25}
\]

drive the starting value `y_(k+1)` down to absolute value at most `1`; keep `|Y|<=1` through the middle by alternating signs; and in an upper window of the same length realize the exact target `y_k`. The supply lemma provides enough squarefree positions because

\[
|y_k|+|y_{k+1}|+O(1)
\ll
\frac{\sqrt H}{k}
\le
C\sqrt{H/k}.
\tag{26}
\]

The two windows fit disjointly: uniformly for `k<=R`,

\[
\frac{|I_k|}{\sqrt{H/k}}
\asymp
\frac{\sqrt H}{k^{3/2}}
\ge
H^{1/8}
\longrightarrow\infty.
\tag{27}
\]

This fixes every sign through `H` without ever changing the old prefix. Repeating the construction over `H_0,H_1,H_2,...` therefore produces one infinite sequence, not horizon-dependent witnesses.

## 3. The extension preserves a global square-root envelope and a cheap prefix

The construction can be arranged so that at every retained horizon

\[
\boxed{
P(H):=\sum_{n\le H}|Y(n)|^2\ll H^{3/2}.
}
\tag{28}
\]

Assume this at `L`. The old prefix costs `O(L^(3/2))=O(H^(3/4))`. The reset window in `(L,Q]` has length `O(sqrt(L))` and height `O(sqrt(L))`, hence costs `O(L^(3/2))`; after it, (17) contributes only `O(Q)=O(H^(3/4))`. Therefore

\[
P(Q)\ll H^{3/4}.
\tag{29}
\]

On `I_k`, the two ramp windows have total length `O(sqrt(H/k))`, while the path height there is `O(sqrt(H)/k+1)`. Their squared contribution is therefore

\[
O\!\left(
\sqrt{\frac Hk}\,\frac{H}{k^2}
\right)
=
O\!\left(\frac{H^{3/2}}{k^{5/2}}\right).
\tag{30}
\]

The middle parts contribute only their lengths because `|Y|<=1`. Summing (30) over `k<=R` and adding the total middle length gives

\[
P(H)-P(Q)\ll H^{3/2}+H,
\tag{31}
\]

proving (28) inductively after enlarging the constant to absorb the finite initialization.

The same construction gives the pointwise envelope (6). In a ramp inside `I_k`,

\[
|Y(n)|\ll\frac{\sqrt H}{k}+1,
\qquad
n\asymp\frac Hk,
\tag{32}
\]

so `|Y(n)|<<sqrt(n)`; the reset and bounded-middle regions satisfy the same estimate, and the finite base can again be absorbed into the constant.

The useful distinction is that the source is now physically discrete everywhere, but its signs are still free to be chosen nonmultiplicatively.

## 4. Only `O(H^(3/4))` source error reaches the skeleton

Fix a retained horizon `H` and write

\[
x_k:=Y(\tau_H(k)),
\qquad
x_k^{(0)}:=t\frac{\mu(k)}k,
\qquad
\delta_k:=x_k-x_k^{(0)}.
\tag{33}
\]

For `1<=k<=R`, construction of the targets gives

\[
\delta_1=0,
\qquad
|\delta_k|\le1\quad(2\le k\le R).
\tag{34}
\]

For `k>R`, monotonicity of `tau_H` gives

\[
\tau_H(k)\le Q.
\tag{35}
\]

Because `tau_H` is a bijection of `Q_H`, (29) implies

\[
\sum_{\substack{k\in\mathcal Q_H\\k>R}}
|Y(\tau_H(k))|^2
\le
P(Q)
\ll H^{3/4}.
\tag{36}
\]

The equality-ray tail is equally cheap:

\[
\sum_{k>R}\left|t\frac{\mu(k)}k\right|^2
\le
t^2\sum_{k>R}\frac1{k^2}
\ll
\frac{H}{R}
\ll H^{3/4}.
\tag{37}
\]

Hence

\[
\boxed{
\sum_{k\in\mathcal Q_H}|\delta_k|^2
\ll H^{3/4}.
}
\tag{38}
\]

Now apply the elementary divisor-transform stability estimate from `FD-120`. For

\[
B(k):=\sum_{d\mid k}d\,\delta_d,
\tag{39}
\]

it gives

\[
\sum_{k\in\mathcal Q_H}\frac{|B(k)|^2}{k^2}
\ll
(1+\log H)^2
\sum_{k\in\mathcal Q_H}|\delta_k|^2
\ll
H^{3/4}(\log H)^2.
\tag{40}
\]

The equality ray has Fourier image supported only at `k=1`, and `B(1)=delta_1=0`. Thus the cross term vanishes exactly and

\[
\mathcal E_H^{\mathcal Q}(Y)
=
t^2+
\sum_{k\in\mathcal Q_H}\frac{|B(k)|^2}{k^2},
\tag{41}
\]

which proves (8) and (9).

## 5. What arithmetic information is still missing

This result joins the two previously separate negative controls:

- `FD-120` imposed the complete squarefree/unit-amplitude increment law but rebuilt the witness independently for each horizon;
- `FD-125` imposed one permanent common source on repeated-square horizons but allowed nonphysical increments.

The present construction satisfies both restrictions simultaneously. Therefore **horizon-independent coherence plus the complete support/amplitude law is still too weak**. Merely replacing the real-valued `FD-125` source by a genuine cumulative walk on the squarefree integers does not charge a critical relative skeleton cost.

What remains absent is exactly the arithmetic relation among the signs. In particular, this construction does not impose

\[
a(n)=\mu(n),
\tag{42}
\]

nor the coprime multiplicative sign law, nor even the family of exact identities

\[
\sum_{d\le H}Y\!\left(\left\lfloor\frac Hd\right\rfloor\right)=1
\tag{43}
\]

at the retained horizons. `FD-120` can repair (43) at one horizon because its witness is allowed to depend on that horizon; the stagewise common-source construction above does not provide simultaneous repairs. Consequently the next genuine boundary is no longer the physical increment support/amplitude law by itself. A successful coercive theorem must spend **sign correlation or a growing cross-horizon identity family**.

This is still not an RH estimate. It is a matched-control obstruction specifying which source information cannot possibly be sufficient for the current Fourier-skeleton route.

## 6. Stress tests and prior-art boundary

The delicate points are parity, local squarefree capacity, prefix energy, and the final Fourier norm. Parity is exact by (22). The elementary squarefree count (12) supplies the two endpoint windows, and (27) guarantees they do not collide. The worst path cost is the sum of the ramp terms (30), which is `O(H^(3/2))`; this is lower order when inherited by the next repeated-square horizon and yields the sharper `O(H^(3/4))` skeleton-source error in (38). No probabilistic sign model, RH-strength input, short-interval Möbius cancellation, or unproved squarefree-gap estimate is used.

A targeted prior-art audit covered Farey/Franel discrepancy, floor-quotient Mertens compression, signed squarefree sequences, and discrepancy results for squarefree-supported multiplicative functions. The nearby literature studies the floor-quotient carrier or multiplicative squarefree-supported functions, but no matching theorem was located for a single arbitrary squarefree-unit sign source asymptotically realizing the floor-quotient equality ray on repeated-square horizons. Search absence is not a novelty proof; the claim here is the explicit construction and its consequence for this Mathia route.

No new external theorem is load-bearing. Equation (12) is proved directly, and the only nontrivial transform estimate is the already-canonical `FD-120` bound. `SOURCES.md` therefore needs no new dependency.

The decisive falsification tests are concrete: exhibit a parity incompatibility in (20)--(22), show that a required neutralization/final ramp cannot fit inside the windows allowed by (13) and (27), or show that the prefix estimate (29) fails to control the `k>R` quotient coordinates under the `tau_H` involution. Absent such a failure, squarefree support and unit amplitudes have now been removed from the list of candidate mechanisms that can close the superexponential sparse escape by themselves.