# FD-085 — power-window linear blocks can have only superexponential integer-ratio chains

**Status:** `EXACT-DERIVED + MATCHED-GEOMETRIC-CONTROL + FULL-COUNTING-POWER-WINDOWS + LINEAR-ADDITIVE-BLOCKS + DIVERGING-DILATION-CHAIN + DECISIVE-NEGATIVE`.

`FD-083` and `FD-084` leave one geometric arrow open. The physical constant-occupation set has full counting exponent inside every fixed-power future window, and every such window contains a consecutive occupied block of polynomial length. A tempting next step is to extract from those two facts an integer-ratio chain with bounded, or at least finite-entropy, transition ratios and then feed that chain into the multihorizon GCD-duality obstructions of `FD-022`--`FD-023`.

That implication is false at the level of the set geometry currently proved. There is an explicit subset of the positive integers that satisfies a stronger version of both `FD-083` and `FD-084` while **every infinite integer-ratio chain inside it has transition ratios tending to infinity**. Consequently its logarithmic horizon growth per retained scale diverges, exactly the superexponential escape left open by `FD-023`.

Fix

\[
a:=\frac12\log 2
\]

and define the logarithmically accelerating band set

\[
\boxed{
\mathcal S
:=
\bigcup_{k\ge1}
\left([e^{k^2},e^{k^2+a}]\cap\mathbb N\right).
}
\tag{1}
\]

Then the following three statements hold.

First, for every fixed `epsilon>0`,

\[
\boxed{
\lim_{X\to\infty}
\frac{
\log\!\left(1+\#(\mathcal S\cap(X,X^{1+\varepsilon}])\right)
}{\log X}
=1+\varepsilon.
}
\tag{2}
\]

Second, for every fixed `epsilon>0` and every fixed `alpha<1`, every sufficiently large `X` admits an integer `H` such that

\[
\boxed{
[H,H+\lfloor H^\alpha\rfloor]
\subset
\mathcal S\cap(X,X^{1+\varepsilon}].
}
\tag{3}
\]

In fact the available block has length comparable with `H`, so (3) is much stronger than the `H^(Theta-delta)` additive blocks supplied by `FD-084`.

Third, for every fixed integer `B>=2` there exists `N_B` such that

\[
\boxed{
n\in\mathcal S,\ n\ge N_B,\ 2\le q\le B
\quad\Longrightarrow\quad
qn\notin\mathcal S.
}
\tag{4}
\]

Hence if

\[
n_0<n_1<n_2<\cdots,
\qquad
n_{j+1}=q_jn_j,
\qquad
q_j\in\mathbb Z_{\ge2},
\qquad
n_j\in\mathcal S,
\tag{5}
\]

is any infinite integer-ratio chain, then

\[
\boxed{q_j\longrightarrow\infty}
\tag{6}
\]

and therefore

\[
\boxed{
\frac1j\log\frac{n_j}{n_0}
=
\frac1j\sum_{i<j}\log q_i
\longrightarrow\infty.
}
\tag{7}
\]

Thus full-counting power-window abundance plus polynomial, even linear, additive blocks do not by themselves produce the finite-logarithmic-entropy multiplicative transport needed to activate the existing multihorizon obstruction.

## 1. Every fixed-power window contains a near-upper-end logarithmic band

Put

\[
x:=\log X,
\qquad
y:=(1+\varepsilon)x.
\]

Choose `k` maximal with

\[
k^2+a\le y.
\tag{8}
\]

Maximality gives

\[
y-k^2<(k+1)^2-k^2+a=2k+1+a=O(\sqrt y).
\tag{9}
\]

Since `y-x=epsilon*x` while the right side of (9) is `O(sqrt(x))`, for all sufficiently large `X` one has

\[
x<k^2<k^2+a\le y.
\tag{10}
\]

Therefore the entire band

\[
I_k:=[e^{k^2},e^{k^2+a}]
\]

lies inside `(X,X^(1+epsilon)]`.

Moreover (9) gives

\[
e^{k^2}
=
\exp\bigl((1+\varepsilon)x-O(\sqrt x)\bigr)
=
X^{1+\varepsilon-o(1)}.
\tag{11}
\]

The number of integers in the band is

\[
\#(I_k\cap\mathbb N)
=(e^a-1)e^{k^2}+O(1)
=X^{1+\varepsilon-o(1)}.
\tag{12}
\]

Since the whole future window contains at most `X^(1+epsilon)` integers, (12) proves (2). Notice that this is the same full-counting exponent as `FD-083`, and it holds in every sufficiently large fixed-power future window rather than only on a selected subsequence.

## 2. The same bands contain linear consecutive blocks

Let

\[
H_k:=\lceil e^{k^2}\rceil.
\]

Because the right endpoint of `I_k` is `e^a e^(k^2)` and `e^a=sqrt(2)>1`, there is a fixed constant `c>0`, for example any

\[
0<c<\frac{e^a-1}{3},
\tag{13}
\]

such that for all sufficiently large `k`,

\[
[H_k,H_k+\lfloor cH_k\rfloor]
\subset I_k\cap\mathbb N.
\tag{14}
\]

For every fixed `alpha<1`, one also has `H_k^alpha<cH_k` eventually. Combining this with the band placement in Section 1 proves (3).

This matches the exact geometric information presently available from the physical occupation argument and strengthens its local block length. In particular, because `Theta<=1`, every exponent `Theta-delta` occurring in `FD-084` is strictly below one and is therefore represented by the control (3).

## 3. Every bounded integer dilation eventually lands in a gap

The gap between consecutive bands grows on the logarithmic scale:

\[
(k+1)^2-k^2=2k+1\longrightarrow\infty.
\tag{15}
\]

Fix `B>=2`. Choose `k_B` so large that

\[
2k+1>a+\log B
\qquad(k\ge k_B).
\tag{16}
\]

If `n` lies in the `k`-th band and `2<=q<=B`, then the lower bound `q>=2` and the choice `a<log 2` give

\[
qn
\ge2e^{k^2}
>e^{k^2+a},
\tag{17}
\]

so `qn` lies beyond the current band. On the other hand,

\[
qn
\le Be^{k^2+a}
<e^{k^2+a+2k+1-a}
=e^{(k+1)^2},
\tag{18}
\]

where (16) was used in the strict inequality. Thus `qn` lies strictly before the next band. It belongs to no later band either, proving (4).

Now take an infinite chain (5). Since every transition ratio is at least two, `n_j` tends to infinity and the band index containing `n_j` tends to infinity. Given an arbitrary fixed `B`, equation (4) therefore forces `q_j>B` for every sufficiently large `j`. Since `B` was arbitrary, (6) follows. The sequence `log q_j` tends to infinity, so its Cesàro means also tend to infinity, proving (7).

## 4. Exact consequence for the current Farey route

`FD-022` obtains a uniform Cesàro GCD-duality gap on integer-ratio chains with a fixed transition ceiling. `FD-023` weakens that hypothesis substantially: for a polynomial-growth source, Cesàro saturation can survive only if

\[
\frac1j\log\frac{H_j}{H_0}\longrightarrow\infty,
\tag{19}
\]

that is, only on a superexponential horizon schedule in the chain index.

The set `S` shows that the coarse geometry established in `FD-083`--`FD-084` is fully compatible with exactly that escape. It has the same fixed-power-window counting exponent, stronger additive blocks, and yet **every** infinite integer-ratio chain satisfies (19). Therefore no argument using only those set-theoretic abundance and block-placement conclusions can manufacture the finite-entropy chain required to close the GCD-duality accumulation route.

This is stronger than merely observing that one particular prescribed dilation can miss a long interval. A single set simultaneously evades every fixed bounded dilation alphabet eventually: for each finite ceiling `B`, all sufficiently large sources in the set have no outgoing integer-ratio edge with multiplier at most `B`.

The conclusion is negative but useful. The remaining compatibility theorem must exploit information absent from this control, for example the exact quotient-shell/Jordan energy attached to the physical occupation values, a transport inequality across nearby horizons, or a source-specific restriction on where successive occupied blocks can occur. Pure counting abundance plus additive thickness has reached its logical limit.

## 5. Stress tests and evidence boundary

The control is deliberately synthetic. It is **not** asserted to arise as

\[
\{H:\nu_{H,D}>\eta\}
\]

for the physical Farey/Mertens source, and it does not satisfy or imitate the exact divisor-supported energy increment identities of `FD-084`. Accordingly it does not refute a source-specific multiplicative-compatibility theorem. It refutes only an implication whose hypotheses are the coarse geometric consequences already extracted from those identities.

The conclusion is also about fixed integer-ratio chains. It does not exclude useful transport with nonintegral ratios, floor-quotient correspondences, or inequalities that accumulate directly under additive horizon motion. Nor does it say that the physical occupied set actually realizes the superexponential escape. Those are precisely the remaining mathematical questions.

A targeted prior-art audit covered additive thickness versus multiplicative configurations, geometric-progression-free large sets, and multiplicatively syndetic sets. Beiglböck--Bergelson--Hindman--Strauss, *Multiplicative structures in additively large sets* (J. Combin. Theory Ser. A **113** (2006), 1219--1242), already shows that additively thick sets can have sharply restricted multiplicative structure, including thick sets with no three-term geometric progression. Chapman, *Partition regularity and multiplicatively syndetic sets* (Acta Arith. **196** (2020), 109--138), develops multiplicative syndeticity precisely as a stronger largeness notion for dilation-invariant configurations. Thus no novelty is claimed for the qualitative separation between additive and multiplicative largeness. The contribution persisted here is the exact matched control for the `FD-083`--`FD-084` power-window geometry and its direct identification with the superexponential escape of `FD-023`.

No external theorem is load-bearing in the derivation: (1)--(7) are elementary and proved above. The literature is used only to delimit novelty, so `SOURCES.md` requires no new dependency anchor.

## 6. Consequence for the frontier

The live hierarchy can now be sharpened from

\[
\text{recurrence}
\to
\text{full-counting occupation}
\to
\text{additive blocks}
\to
\text{multiplicative compatibility}
\]

to a strict separation at the last arrow: **multiplicative compatibility cannot mean extracting a finite-entropy integer-ratio chain from the set geometry alone.** Any successful theorem must use additional physical arithmetic or replace integer-ratio chaining by an additive/nonlocal transport mechanism that composes the already-proved blocks.

This is a route restriction, not an RH estimate and not a contradiction to the positive occupation results. It closes a natural but invalid combinatorial shortcut after `FD-084` while leaving the genuinely source-specific transport problem open.