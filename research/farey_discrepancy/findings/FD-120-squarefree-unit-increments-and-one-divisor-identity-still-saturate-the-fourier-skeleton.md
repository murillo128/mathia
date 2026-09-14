# FD-120 — squarefree unit increments and one divisor identity still saturate the Fourier skeleton

**Status:** `EXACT-DERIVED + FLOOR-QUOTIENT-FOURIER-SKELETON + SQUAREFREE-UNIT-INCREMENT-WITNESS + EXACT-DIVISOR-IDENTITY + CRITICAL-SCALE-SATURATION + NEGATIVE/ROUTE-RESTRICTION`.

`FD-119` shows that fixed endpoint truth does not move the `FD-118` Fourier skeleton a positive relative distance away from its Möbius equality ray. The next natural escape is to impose a growing, genuinely discrete source law rather than finitely many Mertens values. Even the full **single-horizon squarefree/unit-amplitude increment law**, together with the exact floor-quotient divisor identity, is still too weak.

Let

\[
\mathcal Q_N
=\left\{\left\lfloor\frac Nm\right\rfloor:1\le m\le N\right\},
\qquad
\tau_N(k)=\left\lfloor\frac Nk\right\rfloor,
\tag{1}
\]

and, for any cumulative source `Y`, define

\[
x_k:=Y(\tau_N(k)),
\qquad
A_Y(k):=\sum_{d\mid k}d\,x_d,
\qquad
\mathcal E_N^{\mathcal Q}(Y)
:=\sum_{k\in\mathcal Q_N}\frac{|A_Y(k)|^2}{k^2}.
\tag{2}
\]

For every sufficiently large `N` there exists a synthetic increment sequence `a_N(1),...,a_N(N)` such that

\[
a_N(1)=1,
\qquad
a_N(n)=0\ \text{if }n\text{ is nonsquarefree},
\qquad
a_N(n)\in\{-1,+1\}\ \text{if }n\text{ is squarefree},
\tag{3}
\]

its cumulative source

\[
Y_N(r):=\sum_{n\le r}a_N(n)
\tag{4}
\]

satisfies the exact physical single-horizon identity

\[
\boxed{
\sum_{d=1}^N Y_N\!\left(\left\lfloor\frac Nd\right\rfloor\right)=1,
}
\tag{5}
\]

and its terminal amplitude obeys

\[
\boxed{Y_N(N)=t_N=\sqrt N+O(1).}
\tag{6}
\]

Nevertheless

\[
\boxed{
\mathcal E_N^{\mathcal Q}(Y_N)
=t_N^2+o(N),
\qquad
\frac{\mathcal E_N^{\mathcal Q}(Y_N)}{t_N^2}\longrightarrow1.
}
\tag{7}
\]

Thus the complete squarefree support pattern, unit amplitudes on every squarefree increment, the physical normalization `a_1=1`, and one exact divisor identity do **not** force a positive critical-scale coercivity gap on the minimal Fourier skeleton. The missing resource is narrower: actual Möbius sign correlation/multiplicativity, a growing family of cross-horizon compatibility identities, horizon-independent coherence of the same sign sequence, or another restriction that distinguishes the true signs from arbitrary squarefree-supported signs.

This is a single-horizon relaxation theorem. The witness depends on `N` and is deliberately nonmultiplicative. It does not claim that the actual Mertens trajectory approaches the equality ray.

## 1. Equality ray and an elementary perturbation bound

`FD-119` reindexes the formal source by `x_k=Y(tau_N(k))` and identifies the exact equality ray

\[
x_k^{(0)}=t\frac{\mu(k)}k,
\qquad k\in\mathcal Q_N,
\tag{8}
\]

for which

\[
A^{(0)}(1)=t,
\qquad
A^{(0)}(k)=0\quad(k>1),
\qquad
\mathcal E_N^{\mathcal Q}(x^{(0)})=t^2.
\tag{9}
\]

We will build a legal squarefree-sign cumulative source whose skeleton coordinates differ from (8) by a perturbation `delta_k`. The following crude but sufficient stability bound keeps the energy accounting self-contained.

If `delta=(delta_k)_(k in Q_N)` has finite support and

\[
B(k):=\sum_{d\mid k}d\,\delta_d,
\tag{10}
\]

then

\[
\boxed{
\sum_{k\in\mathcal Q_N}\frac{|B(k)|^2}{k^2}
\ll (1+\log N)^2
\sum_{k\in\mathcal Q_N}|\delta_k|^2.
}
\tag{11}
\]

Indeed, enlarging the outer sum from `Q_N` to all multiples up to `N`,

\[
\sum_k\frac{|B(k)|^2}{k^2}
\le
\zeta(2)
\sum_{a,b}
|\delta_a\delta_b|
\frac{\gcd(a,b)^2}{ab}.
\tag{12}
\]

Using the Jordan identity

\[
\gcd(a,b)^2=\sum_{d\mid\gcd(a,b)}J_2(d)
\tag{13}
\]

and Cauchy--Schwarz gives, with `u_a=|delta_a|`,

\[
\begin{aligned}
\sum_{a,b}u_au_b\frac{\gcd(a,b)^2}{ab}
&=
\sum_dJ_2(d)
\left(\sum_{d\mid a}\frac{u_a}{a}\right)^2\\
&\le
(1+\log N)
\sum_a\frac{u_a^2}{a}
\sum_{d\mid a}\frac{J_2(d)}d.
\end{aligned}
\tag{14}
\]

For `p^e||a`,

\[
\frac1{p^e}\sum_{j=0}^e\frac{J_2(p^j)}{p^j}
=1+\frac1p-\frac1{p^{e+1}},
\tag{15}
\]

so

\[
\frac1a\sum_{d\mid a}\frac{J_2(d)}d
\le
\prod_{p\mid a}\left(1+\frac1p\right)
=\sum_{d\mid\operatorname{rad}(a)}\frac1d
\le 1+\log N.
\tag{16}
\]

Equations (12)--(16) prove (11). This is intentionally not an optimal GCD-sum estimate; only a polylogarithmic operator loss is needed below.

## 2. Build a legal squarefree-sign source close to the equality ray

Put

\[
s=\lfloor\sqrt N\rfloor,
\qquad
R=\lfloor N^{1/4}\rfloor,
\qquad
q_k=\left\lfloor\frac Nk\right\rfloor,
\qquad
Q=q_{R+1}.
\tag{17}
\]

Choose an integer `t_N` with the same parity as the number of squarefree integers at most `N` and

\[
|t_N-\sqrt N|\le1.
\tag{18}
\]

This parity is necessary for a sum of `+-1` over all squarefree positions and will make the terminal target exact.

On the tail `n<=Q`, reuse the four-dilate squarefree-sign construction of `FD-008`. It gives signs on every squarefree integer, zero on every nonsquarefree integer, `a_1=1`, and simultaneously

\[
\boxed{
|Y_N(x)|\le4\quad(x\le Q),
\qquad
W_{\rm tail}:=
\sum_{n\le Q}a_N(n)\left\lfloor\frac Nn\right\rfloor
=O(R).
}
\tag{19}
\]

The mechanism is elementary: write every squarefree integer uniquely as `dr` with `d in {1,2,3,6}` and `(r,6)=1`, use coefficients `(1,-1,-1,-1)`, and pair the core `r` values with opposite signs. The identity `1-1/2-1/3-1/6=0` kills the real main term in the divisor workload; greedy orientation of the pairs keeps the remaining floor workload `O(R)`.

For `1<=k<=R`, let

\[
I_k=(q_{k+1},q_k]\cap\mathbb Z.
\tag{20}
\]

Choose integers `y_k` with the parity forced by the number of squarefree integers at most `q_k` and

\[
y_1=t_N,
\qquad
\left|y_k-t_N\frac{\mu(k)}k\right|\le1
\quad(2\le k\le R),
\tag{21}
\]

and set `y_(R+1)=Y_N(Q)` from the tail.

These targets are realizable by squarefree signs inside each `I_k`. First,

\[
|I_k|
=\frac{N}{k(k+1)}+O(1)
\gg\frac N{k^2}.
\tag{22}
\]

Uniformly for `k<=R`, the number of nonsquarefree points in `I_k` is at most

\[
|I_k|\sum_{p}\frac1{p^2}+O(\sqrt{q_k})
\le
(\zeta(2)-1)|I_k|+o(|I_k|),
\tag{23}
\]

because `sqrt(q_k)/|I_k| << k^(3/2)/sqrt(N)=o(1)` for `k<=N^(1/4)`. Hence every `I_k` contains `gg |I_k|` squarefree integers. On the other hand the requested interval total satisfies

\[
|y_k-y_{k+1}|
\ll \frac{\sqrt N}{k}+1,
\tag{24}
\]

with the same bound at `k=R` because `y_(R+1)=O(1)`. The ratio of (24) to the squarefree capacity in (22) is `O(k/sqrt(N))=o(1)`. The parity of `y_k-y_(k+1)` is exactly the parity of the number of squarefree positions in `I_k`, so `+-1` signs can be assigned there with that exact total.

After filling the intervals, every position `1<=n<=N` obeys (3), and

\[
Y_N(q_k)=y_k
\quad(1\le k\le R),
\qquad
|Y_N(x)|\le4
\quad(x\le Q).
\tag{25}
\]

In particular the terminal value is already exactly `Y_N(N)=t_N`.

## 3. The one global divisor identity can be repaired without moving the terminal value

Let

\[
W:=\sum_{n\le N}a_N(n)\left\lfloor\frac Nn\right\rfloor.
\tag{26}
\]

Since `floor(N/n)=k` on `I_k`, summation by parts gives

\[
W
=W_{\rm tail}
+\sum_{k=1}^Rk(y_k-y_{k+1})
=W_{\rm tail}
+\sum_{k=1}^Ry_k
-Ry_{R+1}.
\tag{27}
\]

Using (19) and (21),

\[
W
=t_N\sum_{k\le R}\frac{\mu(k)}k+O(R).
\tag{28}
\]

The classical Davenport log-power cancellation already anchored in `SOURCES.md` implies by partial summation that, for every fixed `A>0`,

\[
\sum_{k\le R}\frac{\mu(k)}k
\ll_A(\log R)^{-A}.
\tag{29}
\]

Hence the defect

\[
D:=1-W
\tag{30}
\]

satisfies

\[
\boxed{
|D|
\ll_A
\frac{\sqrt N}{(\log N)^A}+N^{1/4}.
}
\tag{31}
\]

Moreover `D` is even. Modulo two, every legal sequence in (3) equals the squarefree indicator, hence equals `mu(n)` modulo two; the exact Möbius identity `sum_(n<=N) mu(n) floor(N/n)=1` therefore gives `W=1 (mod 2)`.

The defect can now be repaired **without changing `Y_N(N)`**. If `D>0`, flip one `+1` to `-1` in `I_1` and simultaneously one `-1` to `+1` in `I_2`. The terminal cumulative sum changes by `-2+2=0`, while `W` changes by `-2+4=+2`. Reverse the orientations when `D<0`. Repeating `|D|/2` times makes `W=1` exactly.

There are enough signs of both orientations. The first two intervals contain `gg N` squarefree positions, while their prescribed totals are only `O(sqrt(N))`; equation (31) gives `|D|=o(N)`. Thus the paired flips are feasible for all sufficiently large `N`.

After this repair, (3), (5), and (6) all hold exactly. Only the sample at `q_2` changes among `Y_N(q_k)`, `k<=R`, and it changes by exactly `D` up to sign.

## 4. The full discrete law still costs only `o(N)` skeleton energy

Compare the final source with the equality ray of amplitude `t_N`:

\[
x_k^{(0)}=t_N\frac{\mu(k)}k,
\qquad
\delta_k:=Y_N(\tau_N(k))-x_k^{(0)}.
\tag{32}
\]

The terminal repair preserved `Y_N(N)=t_N`, so

\[
\delta_1=0.
\tag{33}
\]

For `k=2`, the paired repair gives

\[
|\delta_2|=O(1+|D|).
\tag{34}
\]

For `3<=k<=R`, (21) gives `|delta_k|<=1`. For `R<k<=s`, one has `tau_N(k)=q_k<=Q`, so (19) gives

\[
|\delta_k|\le4+\frac{t_N}{k}.
\tag{35}
\]

Finally, if `k>s` and `k in Q_N`, then `tau_N(k)<=s<=Q`; again `|Y_N(tau_N(k))|<=4`, while `t_N/k=O(1)`. Since `|Q_N|=2s+O(1)`, equations (31), (34)--(35) imply

\[
\sum_{k\in\mathcal Q_N}|\delta_k|^2
\ll_A
\frac{N}{(\log N)^{2A}}
+N^{3/4}
+N^{1/2}.
\tag{36}
\]

Applying the elementary perturbation estimate (11), and choosing any fixed `A>2`, gives

\[
\sum_{k\in\mathcal Q_N}\frac{|B(k)|^2}{k^2}
=o(N).
\tag{37}
\]

The equality-ray Fourier vector is supported only at `k=1`, while `B(1)=delta_1=0`. There is therefore no cross term:

\[
\mathcal E_N^{\mathcal Q}(Y_N)
=t_N^2+
\sum_{k\in\mathcal Q_N}\frac{|B(k)|^2}{k^2}
=t_N^2+o(N).
\tag{38}
\]

Together with `t_N^2=N+O(sqrt(N))`, this proves (7).

The scale is important. This is not merely another fixed-depth repair: the witness obeys the squarefree/unit-amplitude increment law at **every integer up to the horizon** and the exact global identity. What remains unconstrained is the correlation of those signs.

## 5. Stress tests and representation boundary

The construction was implemented with exact integer squarefree support, parity-compatible block targets, the four-dilate tail, and the paired `I_1/I_2` divisor repair. For `N=1000,3000,10000,30000,100000`, every tested witness satisfied (3), (5), and exact terminal preservation. The observed ratios `E/t_N^2` were approximately `1.489, 1.371, 1.195, 1.101, 1.059`. These finite checks are regression tests only; (38) is the proof.

The representation kill test is also explicit. No extra source has been introduced: the source is still a quotient staircase and the Fourier carrier is still the reversible `FD-118` transform. The result instead falsifies a proposed **coercive restriction** on that carrier. A high-dimensional or fully discrete admissible class does not help if it still contains horizon-dependent near-equality witnesses.

The witness is intentionally synthetic. In particular, its squarefree signs do not obey the actual Möbius multiplicative correlation `mu(mn)=mu(m)mu(n)` for coprime inputs, and witnesses at different horizons need not be restrictions of one infinite sequence. Therefore (7) does not say that the true Mertens staircase saturates the skeleton norm. It says that any proof using only (3), one-horizon identity (5), and the reversible Fourier geometry cannot force a fixed relative gap.

## Prior-art boundary

`FD-008` is the direct internal predecessor: it already constructs horizon-dependent squarefree-supported unit-sign sequences satisfying the same single divisor identity while saturating the older Franel--Mertens GCD-energy constant. `FD-120` does not claim that squarefree-sign repair itself is new; it retunes that mechanism to the distinct `FD-118` floor-quotient Fourier equality ray at the critical terminal scale `sqrt(N)`.

The floor-quotient carrier is classical in its order-theoretic ingredients (Lagarias--Richman and earlier Mertens-matrix work), and GCD-sum/spectral estimates for kernels built from `gcd(a,b)^2/(ab)` are classical. Equation (11) is included only as an elementary self-contained bound; no optimal GCD-sum theorem is imported. The Farey/Mertens formulas underlying the line are already anchored in `SOURCES.md`. A targeted literature audit did not locate an external theorem asserting the single-horizon squarefree-sign saturation statement (7).

The only analytic cancellation used beyond earlier exact line identities is Davenport's classical arbitrary log-power bound for the Möbius summatory function, already anchored in `SOURCES.md`; partial summation yields (29). No new external dependency is therefore added.

## Evidence boundary

This finding proves a negative theorem for a stated relaxation. It does **not** prove an improved Farey discrepancy estimate, an improved Mertens exponent, or anything about truth or falsity of RH. It does not enforce the actual Möbius sign at primes, multiplicativity across coprime factors, compatibility with every smaller horizon, or one horizon-independent infinite sign sequence. Those are now the natural remaining source restrictions if the minimal Fourier skeleton is to yield a critical-scale coercivity gap.