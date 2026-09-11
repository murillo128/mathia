# FD-039 — one-Lipschitz divergent shell profiles can evade nonsquarefree occupation

**Status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + SYNTHETIC-QUOTIENT-SHELL-SOURCE + ONE-LIPSCHITZ + DIVERGENT-CRITICAL-ENERGY + HYPERBOLA-SAMPLING-AMPLIFICATION + JOINT-NONSQUAREFREE-OCCUPATION-BOUNDARY`.

`FD-037` and `FD-038` sharply localize what a failure of joint nonsquarefree occupation would have to do. The former shows that bounded increments force any sequence with `U_(H,D)/E_(H,D) -> 0` into the first `O(H^(1/3))` Jordan rows. The latter shows that every growing terminal quotient range `k<=H^alpha`, `alpha<1/3`, has the expected positive nonsquarefree occupation independently of the shell values. The remaining escape was called **hyperbola-sampling amplification**: a thin set of low rows could in principle sample unusually large long-quotient values and overwhelm the entire terminal bulk.

That escape is real at the level of the generic source properties used so far. For every fixed `D>=1` there exists a nonnegative integer-valued function

\[
F:\mathbb Z_{\ge0}\to\mathbb Z_{\ge0}
\]

with

\[
F(0)=0,\qquad F(1)=1,\qquad |F(n+1)-F(n)|\le1,
\tag{1}
\]

and

\[
F(n)\ll_D n^{2/3},
\tag{2}
\]

such that its critical square sum

\[
Q_F(K):=\sum_{k\le K}\frac{F(k)^2}{k(k+1)}
\tag{3}
\]

diverges, but the exact Jordan-shell energies

\[
E^F_{H,D}:=\sum_{D<r\le H}w(r)F(\lfloor H/r\rfloor)^2,
\qquad
w(r):=\frac{J_2(r)}{r^2},
\tag{4}
\]

\[
U^F_{H,D}:=\sum_{\substack{D<r\le H\\\mu(r)=0}}
w(r)F(\lfloor H/r\rfloor)^2
\tag{5}
\]

satisfy

\[
\boxed{\frac{E^F_{H,D}}H\longrightarrow\infty}
\tag{6}
\]

globally while, along an unbounded sequence `H_j`,

\[
\boxed{\frac{U^F_{H_j,D}}{E^F_{H_j,D}}\longrightarrow0.}
\tag{7}
\]

Moreover the same sequence realizes exactly the amplification left open by `FD-038`: for every fixed `0<alpha<1/3`,

\[
\boxed{
\frac{E^F_{H_j,D}}
{H_jQ_F(\lfloor H_j^\alpha\rfloor)}
\longrightarrow\infty.
}
\tag{8}
\]

Thus **one-Lipschitz shell regularity, the exact hyperbola/Jordan sampling geometry, and divergent critical Mellin energy do not by themselves force a positive nonsquarefree occupation fraction**. The physical clue remains open because the constructed `F` is not the actual Mertens quotient-shell function. Any proof of a constant physical occupation gap must use arithmetic information beyond the generic bound on increments, for example the exact coefficient law

\[
\Delta\mathcal H(n)
=\frac{\mu(\operatorname{rad}n)\varphi(\operatorname{rad}n)}n
\tag{9}
\]

or an equivalent divisibility/multiplicative constraint that the synthetic source below does not satisfy.

## 1. Build sparse triangular shell spikes with exact bounded increments

Fix a prime `r_0>D` and write

\[
w_0:=w(r_0)>0.
\tag{10}
\]

Choose integers

\[
K_1<K_2<\cdots
\]

with `K_1` sufficiently large in terms of `r_0` and, recursively,

\[
K_{j+1}\ge K_j^4.
\tag{11}
\]

Put

\[
A_j:=\lfloor K_j^{2/3}\rfloor
\tag{12}
\]

and define the triangular tent

\[
T_j(k):=(A_j-|k-K_j|)_+.
\tag{13}
\]

After enlarging `K_1` if necessary, (11) makes the positive supports of the tents pairwise disjoint and leaves a zero gap between successive supports. Define

\[
F(0)=0,
\qquad
F(k)=\mathbf 1_{\{k=1\}}+\sum_{j\ge1}T_j(k)
\quad(k\ge1).
\tag{14}
\]

At any fixed `k` at most one large tent is nonzero. Each tent rises and falls with slopes `+1` and `-1`, while the isolated value at `k=1` also changes by at most one. Hence (1) is exact.

If `T_j(k)>0`, then `k=K_j+O(A_j)` and `A_j=o(K_j)`, so `k\asymp K_j` and

\[
F(k)\le A_j\ll k^{2/3}.
\tag{15}
\]

Together with the finite initial pulse this proves (2). In particular, the synthetic source is far below the trivial linear envelope allowed by a one-Lipschitz sequence.

## 2. Every tent contributes constant critical square mass

The contribution of the `j`-th tent to (3) is

\[
q_j
:=\sum_{|m|<A_j}
\frac{(A_j-|m|)^2}{(K_j+m)(K_j+m+1)}.
\tag{16}
\]

Because `A_j/K_j -> 0`, the denominator is `K_j^2(1+o(1))` uniformly on the tent. The exact numerator sum is

\[
\sum_{|m|<A}(A-|m|)^2
=\frac{2A^3+A}{3}.
\tag{17}
\]

Since `A_j^3/K_j^2 -> 1`, equations (16)--(17) give

\[
\boxed{q_j=\frac23+o(1).}
\tag{18}
\]

Therefore

\[
Q_F(K)\longrightarrow\infty,
\tag{19}
\]

and the total critical mass of all tents before the `j`-th one is `O(j)`.

This already forces the global superlinear energy (6), without any special use of the selected horizons. Indeed `w(r)>=1/zeta(2)`. For every fixed `L`, grouping rows with `floor(H/r)=k<=L` yields

\[
\liminf_{H\to\infty}\frac{E^F_{H,D}}H
\ge
\frac1{\zeta(2)}
\sum_{k\le L}\frac{F(k)^2}{k(k+1)}.
\tag{20}
\]

Letting `L->infinity` and using (19) proves (6). At the other end, (2) gives the global polynomial ceiling

\[
E^F_{H,D}
\ll_D
H^{4/3}\sum_{r>D}r^{-4/3}
\ll_D H^{4/3}.
\tag{21}
\]

Thus the countermodel does not obtain its escape from a quadratic-sized energy envelope.

## 3. A selected horizon makes one fixed squarefree row carry the new spike

Set

\[
H_j:=r_0K_j.
\tag{22}
\]

Then

\[
\left\lfloor\frac{H_j}{r_0}\right\rfloor=K_j,
\tag{23}
\]

so the row `r_0` contributes exactly

\[
w_0A_j^2
\tag{24}
\]

to `E^F_(H_j,D)`. Because `r_0` is prime, this contribution is absent from `U^F_(H_j,D)`.

More strongly, for every integer `r>D` with `r\ne r_0`,

\[
\left|\frac{r_0K_j}{r}-K_j\right|
\ge \frac{K_j}{r_0+1}.
\tag{25}
\]

The floor changes this separation by at most one, whereas `A_j=o(K_j)`. Hence, for all sufficiently large `j`, **no row other than `r_0` samples any nonzero point of the current tent**.

Future tents are also invisible at horizon `H_j`. From (11),

\[
K_{j+1}-A_{j+1}>H_j
\tag{26}
\]

for all sufficiently large `j`, and every quotient `floor(H_j/r)` is at most `H_j`. Thus the only remaining contribution at `H_j` comes from the fixed initial pulse and the earlier tents.

## 4. Earlier tents cost only `H_j` times their critical mass

Let

\[
B_{j-1}:=K_{j-1}+A_{j-1}
\]

for `j>=2`. The lacunarity (11) gives

\[
B_{j-1}(B_{j-1}+1)\le H_j
\tag{27}
\]

for all sufficiently large `j`. For every `k<=B_(j-1)`, the number of rows with `floor(H_j/r)=k` is at most

\[
\left\lfloor\frac{H_j}{k}\right\rfloor
-
\left\lfloor\frac{H_j}{k+1}\right\rfloor
\le
\frac{H_j}{k(k+1)}+1
\le
\frac{2H_j}{k(k+1)}.
\tag{28}
\]

Removing the first `D` rows can only decrease that count, and `w(r)<=1`. If `Q_{j-1}` denotes the critical square mass of the initial pulse and the tents preceding `j`, (28) therefore gives

\[
E^F_{\mathrm{old}}(H_j)
\le 2H_jQ_{j-1},
\qquad
Q_{j-1}=O(j).
\tag{29}
\]

Since the current tent contributes only at the squarefree row `r_0`, every nonsquarefree term at `H_j` lies in the old part. Hence

\[
U^F_{H_j,D}\le 2H_jQ_{j-1}.
\tag{30}
\]

On the other hand, (24) gives

\[
E^F_{H_j,D}\ge w_0A_j^2.
\tag{31}
\]

Using `H_j=r_0K_j`, `A_j^2\asymp K_j^{4/3}`, and `Q_(j-1)=O(j)`, we obtain

\[
\frac{U^F_{H_j,D}}{E^F_{H_j,D}}
\ll_{D,r_0}
\frac{j}{K_j^{1/3}}
\longrightarrow0,
\tag{32}
\]

which proves (7). In fact the same estimate shows

\[
\boxed{
E^F_{H_j,D}
=(w_0+o(1))A_j^2
\asymp_D H_j^{4/3}.
}
\tag{33}
\]

The escape is therefore maximally concrete: asymptotically all the selected-horizon energy lies on one fixed squarefree Jordan row.

## 5. The construction realizes the exact escape left by `FD-037` and `FD-038`

Because `r_0` is fixed, eventually

\[
r_0<H_j^{1/3}.
\tag{34}
\]

Equation (33) then shows that the low-row core from `FD-037` contains a `1-o(1)` fraction of the total synthetic energy. Thus the cube-root localization theorem is qualitatively sharp under bounded increments alone.

Now fix `0<alpha<1/3`. Since

\[
H_j^\alpha=o(K_j),
\tag{35}
\]

the cutoff `floor(H_j^alpha)` does not reach the current tent. Every previous tent contributes `O(1)` to the critical square norm, so

\[
Q_F(\lfloor H_j^\alpha\rfloor)=O(j).
\tag{36}
\]

Combining (33), (36), and `H_j\asymp K_j` gives

\[
\frac{E^F_{H_j,D}}
{H_jQ_F(\lfloor H_j^\alpha\rfloor)}
\gg_D
\frac{K_j^{1/3}}j
\longrightarrow\infty,
\tag{37}
\]

which is (8). `FD-038` still applies perfectly to the terminal quotient blocks because its occupation law is uniform over every nonnegative shell profile. The terminal bulk has the expected positive nonsquarefree proportion; it is simply overwhelmed by the single low-row sample in (24).

This is precisely the logical possibility that remained after `FD-037`--`FD-038`, now realized by an explicit fixed source rather than by an abstract horizon-by-horizon energy profile.

## 6. Consequence, prior art, and falsification boundary

`FD-035` showed that the prime-square renormalization inequalities plus coarse energy growth permit sparse cheap-alignment horizons. The present obstruction is stronger in a different direction: it lives directly at the shell-source level, preserves the same hyperbola/Jordan sampling used by the physical energy, satisfies the exact one-Lipschitz regularity exploited by `FD-036` and `FD-037`, and has the divergent critical square norm behind `FD-033` and `FD-038`. Those generic ingredients still permit `U/E -> 0`.

Therefore the accepted joint-occupation problem cannot be closed by combining only bounded increments, critical-norm divergence, terminal weighted nonsquarefree density, and the existing hyperbola block geometry. A successful physical theorem must use structure specific to

\[
\Delta\mathcal H(n)
=\mu(\operatorname{rad}n)\varphi(\operatorname{rad}n)/n,
\]

or another consequence of the actual Mertens source that excludes the triangular concentration mechanism. In particular, merely strengthening the estimate `|Delta mathcal H|<=1` without encoding where the signs and magnitudes can occur is not enough unless the strengthening quantitatively rules out such long coherent tents.

A targeted prior-art audit around Farey--Mertens discrepancy, GCD/Jordan-totient factorization, floor-quotient/hyperbola summation, and summatory-function regularity did not supply an external theorem used by this construction. No novelty is claimed for triangular Lipschitz spikes or sparse countermodels in isolation. The durable Mathia-specific content is the implication separation: the exact generic inputs currently feeding `FD-037`--`FD-038` do not logically imply constant nonsquarefree occupation. No new `SOURCES.md` anchor is therefore required.

The finding is falsified if the tent profile violates (1)--(2), if its critical square mass does not diverge, if another row can sample the current tent at (22), or if the old-energy estimate (29) fails. It must **not** be cited as a counterexample for the actual Mertens quotient-shell source, as evidence that the physical ratio `U_(H,D)/E_(H,D)` ever tends to zero, or as an RH result. Its exact consequence is that the next useful step must exploit arithmetic structure discarded when the physical coefficient law (9) is replaced by the sole bound `|Delta mathcal H|<=1`.