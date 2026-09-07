# MC-132 — Polynomial timestamp moments remain excursion-blind under exact product-state matching

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `MATCHED-CONTROL`, `CLASSICAL-MECHANISMS`, `NO-NOVELTY-CLAIM`.

## Claim

The occurrence-order obstruction of `MC-129`--`MC-131` survives a substantially richer time summary than coarse bins or periodic clocks. For every fixed polynomial degree, one can match **all polynomial timestamp moments of every clocked product-state transition exactly** while placing two bounded-increment paths on opposite sides of square-root first-absolute excursion scale.

Fix integers

\[
k,q,m\ge 2,
\qquad D\ge 0,
\qquad M>D,
\]

put

\[
B=2^M,
\qquad
L=2^{M-D},
\]

and choose a block length `T` such that

\[
4\operatorname{lcm}(q,m)\mid T,
\qquad
T\ge 4(k-1).
\tag{1}
\]

Let

\[
v=+^{k-1},
\]

and define two equal-length macro-cycles

\[
P=-^{T/4}+^{3T/4},
\qquad
Q=-^{3T/4}+^{T/4}.
\tag{2}
\]

They both return the local suffix to `v`, have length `T`, and have integer displacements

\[
\Delta(P)=+T/2,
\qquad
\Delta(Q)=-T/2.
\tag{3}
\]

Because `q | T/2` and `m | T`, both are closed walks at the same vertex after adjoining height modulo `q` and clock phase modulo `m`.

For `0<=n<B`, let

\[
\sigma_n=(-1)^{s_2(n)},
\tag{4}
\]

where `s_2(n)` is the binary digit sum. This is the length-`B` Prouhet--Thue--Morse sign word. Define a second sign word by first setting

\[
h_r=
\begin{cases}
+1,&0\le r<L/2,\\
-1,&L/2\le r<L,
\end{cases}
\tag{5}
\]

and then

\[
\theta_b=(-1)^{s_2(b)},
\qquad
0\le b<2^D,
\]

\[
\tau_{bL+r}=\theta_b h_r.
\tag{6}
\]

Both sign words have the same power moments through degree `D`:

\[
\boxed{
\sum_{n=0}^{B-1}n^a\sigma_n
=
\sum_{n=0}^{B-1}n^a\tau_n
=0
\quad(0\le a\le D).
}
\tag{7}
\]

Form two increment words by starting with the common prefix `v` and then substituting `P` for sign `+1` and `Q` for sign `-1` along `sigma` and `tau`. Call the resulting words `U` and `W`. Their common length is

\[
N=k-1+BT.
\tag{8}
\]

For a tail step `j`, let

\[
E_Z(j)=
\left(
C_Z(j-1),
S_Z(j-1)\bmod q,
(j-1)\bmod m,
z_j
\right)
\tag{9}
\]

be the complete one-step state used by the `MC-131` clocked product graph: preceding `k-1` increments, modular lifted height, periodic clock phase, and next increment. For every state `e` and every polynomial timestamp degree `0<=a<=D`, define

\[
K_Z^{(a)}(e)
=
\sum_{\substack{j>k-1\\E_Z(j)=e}}(j-1)^a.
\tag{10}
\]

Then

\[
\boxed{
K_U^{(a)}(e)=K_W^{(a)}(e)
\quad
\text{for every }e\text{ and }0\le a\le D.
}
\tag{11}
\]

Consequently `U` and `W` agree on every scalar observable obtained by weighting the full local/modular/clock transition state with a polynomial in the absolute timestamp of degree at most `D`. Because the periodic phase is already a state coordinate, the same conclusion holds for every **quasi-polynomial** time weight whose restriction to each residue class modulo `m` is a polynomial of degree at most `D`.

Despite this exact match, their first-absolute excursions separate strongly. If

\[
D_1(Z)=\frac1N\sum_{j=1}^N |S_Z(j)|,
\]

then

\[
D_1(U)=O(k+T),
\tag{12}
\]

while

\[
D_1(W)
\ge
\frac{BT}{N}
\left(
\frac{TL}{8}-\frac{3T}{4}-(k-1)
\right).
\tag{13}
\]

In particular, keep `D,k,q,m` fixed, let `B=2^M -> infinity`, and choose an admissible

\[
T=B^{\eta+o(1)},
\qquad 0<\eta<1.
\tag{14}
\]

Then

\[
N=B^{1+\eta+o(1)},
\]

\[
D_1(U)=N^{\eta/(1+\eta)+o(1)}
      =N^{1/2-\Omega(1)},
\tag{15}
\]

whereas

\[
D_1(W)\ge \left(2^{-D-3}+o(1)\right)N.
\tag{16}
\]

Thus finitely many polynomial timestamp moments do not recover the macro-order information carrying excursion amplitude. The obstruction also permits a logarithmically growing degree range: if `D=delta log_2 B+o(log B)` with

\[
\delta<\frac{1+\eta}{2},
\tag{17}
\]

then the same construction still has

\[
D_1(W)=N^{1-\delta/(1+\eta)+o(1)}
      =N^{1/2+\Omega(1)},
\tag{18}
\]

while `(15)` remains below square-root scale.

This is a representation-level matched-control obstruction. The words are not claimed to satisfy Möbius multiplicativity, the square-free support pattern, prime values, divisor relations, or any zeta-specific analytic constraint.

## 1. The macro-cycles close in the full periodic product state

Both cycles in `(2)` end with at least `k-1` plus signs, so they return the local context to `v`. Their displacements are `+T/2` and `-T/2`; condition `(1)` makes both zero modulo `q`. Their common length `T` is zero modulo `m`. Therefore every macro-block begins at the same local/modular/periodic state independently of the preceding macro-order.

This is the key separation between the **integer lift**, which stores excursion height, and the finite product state retained by the statistic. The latter resets after each block even though the former moves by `+T/2` or `-T/2`.

Within either cycle, the integer displacement relative to the block boundary has absolute value at most `3T/4`. That uniform bound will later isolate the macro-boundary contribution to `D_1`.

## 2. Prouhet moment matching with radically different prefix geometry

For the low-excursion word `sigma`, the generating polynomial is

\[
F_M(z)
=
\sum_{n=0}^{2^M-1}\sigma_n z^n
=
\prod_{j=0}^{M-1}(1-z^{2^j}).
\tag{19}
\]

Hence `F_M` has a zero of order `M` at `z=1`. Since `M>D`, its derivatives through order `D` vanish there. Derivatives give falling-factorial moments, and ordinary powers are linear combinations of falling factorials, proving the first equality in `(7)`.

For the high-excursion word, the inner block in `(5)` has generating polynomial

\[
H_L(z)
=
\sum_{r=0}^{L-1}h_rz^r
=
\frac{(1-z^{L/2})^2}{1-z},
\tag{20}
\]

which has a simple zero at `z=1`. The outer Thue--Morse signs contribute

\[
F_D(z^L)
=
\prod_{j=0}^{D-1}(1-z^{L2^j}),
\tag{21}
\]

with the empty product interpreted as `1` when `D=0`. Therefore

\[
\sum_{n=0}^{B-1}\tau_nz^n
=
H_L(z)F_D(z^L)
\tag{22}
\]

has a zero of order `D+1` at `z=1`. This proves the second equality in `(7)`.

The two moment-matched words have very different prefix geometry. For the Thue--Morse signs,

\[
\left|\sum_{i<n}\sigma_i\right|\le 1
\quad\text{for every }n.
\tag{23}
\]

For `tau`, each length-`L` inner block resets to zero, but before its `L` entries the absolute prefix sums have total

\[
0+1+\cdots+(L/2-1)+L/2+(L/2-1)+\cdots+1
=\frac{L^2}{4}.
\tag{24}
\]

The outer sign `theta_b` only reverses those excursions. Hence, over all `B` macro-boundaries,

\[
\frac1B\sum_{n=0}^{B-1}
\left|\sum_{i<n}\tau_i\right|
=\frac{L}{4}.
\tag{25}
\]

This is the exact source of the macroscopic separation.

## 3. Polynomial timestamp moments of every state transition match exactly

Fix a state `e` from `(9)` and a degree `a<=D`. Because every macro-block starts at the same product-state vertex, the set of within-block offsets at which `P` realizes `e` is fixed; call it `I_P(e)`. Define `I_Q(e)` analogously.

If the first tail step has absolute timestamp offset `s`, then the contribution of a `P` block in macro-position `n` is

\[
A_{P,e,a}(n)
=
\sum_{u\in I_P(e)}(s+nT+u)^a,
\tag{26}
\]

and similarly for `Q`. Each is a polynomial in `n` of degree at most `a`. For a sign word `x=(x_n)`, the total tensor coordinate can therefore be written as

\[
K_x^{(a)}(e)
=
\frac12\sum_{n=0}^{B-1}
\left(A_{P,e,a}(n)+A_{Q,e,a}(n)\right)
+
\frac12\sum_{n=0}^{B-1}x_n
\left(A_{P,e,a}(n)-A_{Q,e,a}(n)\right).
\tag{27}
\]

The first term depends only on the common number `B` of macro-blocks. The bracket in the second term is a polynomial in `n` of degree at most `a<=D`. Equation `(7)` therefore makes the second term identical for `x=sigma` and `x=tau`, proving `(11)`.

This argument matches the tensor **state by state**, not merely after a final scalar summation. Any finite family of periodic weights is already absorbed by enlarging the clock to the joint least-common-multiple period exactly as in `MC-131`; multiplying each periodic state by a polynomial timestamp of degree at most `D` still factors through `(11)`.

The same construction also survives the finite-horizon repair closed by `MC-130`: first fold an `h`-step empirical path with starting memory `k_0-1` into effective context `K=k_0+h-1`, then choose `T>=4(K-1)`. Polynomial timestamp moments of every such finite-horizon path type remain matched through degree `D`.

## 4. Excursion separation and the square-root regime

Let

\[
A_n(x)=\sum_{i<n}x_i
\]

be the macro-sign prefix sum. At the start of macro-block `n`, the integer lifted height is

\[
k-1+\frac{T}{2}A_n(x).
\tag{28}
\]

For `x=sigma`, `(23)` and the within-cycle `3T/4` bound imply

\[
|S_U(j)|\le k-1+\frac{5T}{4}
\]

throughout the tail, giving `(12)`.

For `x=tau`, reverse triangle inequality at every step in a macro-block gives a block-average lower bound

\[
\frac{T}{2}|A_n(\tau)|-(k-1)-\frac{3T}{4}.
\]

Averaging this over the `B` blocks and using `(25)` yields `(13)`.

For fixed `D`, `L=B/2^D`, so the leading term in `(13)` is `N/2^{D+3}`. Choosing `T=B^{eta+o(1)}` with `eta<1` simultaneously makes the low path sub-square-root by `(15)`. This gives an arbitrarily large exact separation while preserving every tensor in `(11)`.

If `D` grows, `L=B/2^D` simply records the information cost of the Prouhet moment constraints. Taking `D=delta log_2 B+o(log B)` gives `(18)`. Thus the obstruction is not confined to a literally fixed number of moments: a controlled logarithmic moment family can still be blind below its explicit information threshold.

## 5. Prior art and novelty assessment

The equal-power-sum mechanism is classical Prouhet--Thue--Morse theory. Jean-Paul Allouche and Jeffrey O. Shallit, *The Ubiquitous Prouhet-Thue-Morse Sequence*, in *Sequences and Their Applications* (SETA'98), Springer (1999), pp. 1--16, DOI `10.1007/978-1-4471-0551-0_1`, surveys the Prouhet construction and the Thue--Morse sequence. The standard generating product `(19)` and the resulting equal sums of like powers are therefore prior art, not a Mathia discovery.

Likewise, empirical Markov/path types and periodic state augmentation are classical mechanisms already audited in `MC-S41`, `MC-130`, and `MC-131`. A targeted literature search found no basis for claiming novelty for polynomially weighted type counts as an abstract construction, so none is claimed.

The durable line-specific result is the exact combination: Prouhet moment matching can be imposed on the **macro-order of common based product-state cycles**, preserving all transition-level polynomial/quasi-polynomial timestamp moments through the declared degree while the integer lift retains radically different excursion geometry. The proof is self-contained and the novelty classification remains conservative.

## Boundaries and falsification tests

- Equality holds for polynomial timestamp moments through degree `D`, state by state. It does **not** match the raw ordered list of occurrence times, the full empirical measure on absolute timestamps, arbitrary non-polynomial weights, adaptive weights chosen from the path, or the complete ordered trajectory.
- Because the periodic clock is part of the state, the result covers quasi-polynomial weights with fixed period `m`; several periodic phases reduce to their joint least-common-multiple period as in `MC-131`.
- The logarithmically growing-degree extension spends an explicit factor `2^D` in the high excursion. It is not a claim that arbitrarily many moments remain free.
- Exact timestamps can of course reconstruct occurrence order when retained at full resolution. The result says only that compressing those timestamps to finitely or moderately many polynomial moments still loses decisive order information.
- The matched controls are generic `+/-1` words. They do not preserve Möbius multiplicativity, square-free zeros, prime values, divisor relations, or an arithmetic source law. A theorem showing that such arithmetic constraints force excursion control from a polynomial-time summary would evade this obstruction.
- No `1/zeta` identity, zero-free region, contour shift, probabilistic independence assumption, or numerical evidence enters the proof.

## Consequence for the line

`MC-130` closed finite-horizon empirical path types and `MC-131` closed periodic timing. The immediate next repair -- attach a finite family of absolute-time moments to every local/modular/periodic transition type -- is also insufficient. **Moment information about occurrence times is not occurrence order.**

The accepted mean-absolute transfer frontier should therefore no longer list generic timestamp moments as an unexplored carrier. A surviving timing-based source mechanism must retain substantially finer occurrence-order information: a non-polynomial/adaptive or essentially full-resolution temporal measure, a genuinely nested multiscale relation not reducible to a bounded moment family, a critical information budget beyond the present construction, or Möbius-specific arithmetic structure that forbids these Prouhet macro-cycle reorderings.