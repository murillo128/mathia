# NB-033 — a polylogarithmic moving-tail skeleton preserves relative distance and the Möbius coefficient core

**Status:** `EXACT-DERIVED + SOURCE-FAITHFUL-TAIL-QUOTIENT + RELATIVE-DISTANCE-COMPRESSION + MOBIUS-CORE-PRESERVATION + METHOD-BOUNDARY`. `NB-031` proves that moving high-index adjacent differences form a Gram-whitened target-poor sector, and `NB-032` shows that projecting that sector away leaves a target-bearing skeleton of rank at most the lower cutoff minus one while preserving the limiting Nyman distance. The remaining concern was that this skeleton might be only an abstract Gram compression: its basis can depend on the full tail, and it was not known whether the source-locked Möbius coordinates survive the quotient or whether the additive `NB-032` distance error is small relative to the actual finite-section distance.

Both points admit exact answers. Let

\[
V_N:=\operatorname{span}(g_2,\ldots,g_N),
\qquad
h_n:=g_n-g_{n+1},
\]

and, for `2<=M<N`, set

\[
W_{M,N}^{\rm tail}:=\operatorname{span}(h_M,\ldots,h_{N-1}),
\qquad
Q_{M,N}:=I-P_{W_{M,N}^{\rm tail}},
\]

\[
K_{M,N}:=V_N\cap(W_{M,N}^{\rm tail})^\perp,
\qquad
k_j^{(M,N)}:=Q_{M,N}g_j\quad(2\le j\le M).
\tag{1}
\]

Then the canonical generators `g_2,...,g_N` are linearly independent, and therefore

\[
\boxed{
\dim V_N=N-1,
\qquad
\dim W_{M,N}^{\rm tail}=N-M,
\qquad
\dim K_{M,N}=M-1.
}
\tag{2}
\]

Moreover

\[
\boxed{
\{k_2^{(M,N)},\ldots,k_M^{(M,N)}\}
\text{ is a basis of }K_{M,N},
}
\tag{3}
\]

and all canonical tail generators have the **same quotient image**,

\[
\boxed{
Q_{M,N}g_n=k_M^{(M,N)}
\qquad(M\le n\le N).
}
\tag{4}
\]

Consequently, if the full best approximant has its unique canonical expansion

\[
P_{V_N}e=\sum_{n=2}^N a_{N,n}g_n,
\tag{5}
\]

then its projection to the target-bearing skeleton is exactly

\[
\boxed{
P_{K_{M,N}}e
=
\sum_{n=2}^{M-1}a_{N,n}k_n^{(M,N)}
+
\left(\sum_{n=M}^N a_{N,n}\right)k_M^{(M,N)}.
}
\tag{6}
\]

Thus the moving-tail quotient does not scramble the low source coordinates: **every coefficient below `M` survives unchanged**, while the entire block `M,...,N` collapses to one endpoint quotient scalar. This is the source-faithful description that remained missing after `NB-032`.

There is also a deterministic polylogarithmic cutoff that preserves the finite-section distance multiplicatively, not merely in the limit. Let

\[
M_N:=\left\lceil
\log N\,(\log\log N)^3
\right\rceil
\tag{7}
\]

for sufficiently large `N`, and write

\[
d_N:=\operatorname{dist}(e,V_N),
\qquad
\kappa_N:=\operatorname{dist}(e,K_{M_N,N}).
\]

Then

\[
\boxed{
\frac{\kappa_N}{d_N}
=1+O\!\left(\frac1{\log\log N}\right),
}
\tag{8}
\]

unconditionally. Hence a predeclared skeleton of exact dimension

\[
\boxed{
M_N-1
=O\!\left(\log N(\log\log N)^3\right)
}
\tag{9}
\]

retains the full canonical section distance to relative error `o(1)`, regardless of whether that distance tends to zero.

Finally, the entire inverse-distance Möbius core from `NB-020` lies inside this skeleton for all sufficiently large `N`. Along any subsequence with `d_N->0`, if

\[
x_N:=\left\lfloor\frac{c_*}{d_N}\right\rfloor
\tag{10}
\]

uses the same sufficiently small absolute constant `c_*` as the local locking argument of `NB-020`, then `x_N<M_N` eventually and the skeleton coefficients in (6) satisfy, for every `2<=n<=x_N`,

\[
\boxed{
|a_{N,n}+\mu(n)|\le2d_N\sigma(n).
}
\tag{11}
\]

In particular the positive weighted-density subset used in `NB-020` survives the quotient unchanged, so

\[
\boxed{
\sum_{n\le x_N}n\,|a_{N,n}|
\gg d_N^{-2}
}
\tag{12}
\]

along every closure subsequence. The rank collapse of `NB-032` therefore does **not** discard the finite Möbius-sized source core that is forced when the target distance becomes small.

## 1. The canonical finite dictionary is linearly independent

The independence needed for the exact rank statement can be proved directly in the harmonic-shell coordinates, without a determinant or zeta estimate. On

\[
I_t=\left(\frac1{t+1},\frac1t\right]
\]

one has the exact canonical formula

\[
g_j|_{I_t}=\left\{\frac tj\right\}.
\tag{13}
\]

Suppose

\[
v=\sum_{j=2}^Nc_jg_j=0
\]

in `L^2`. Since `v` is constant on every shell, all shell values `v_t` vanish. Put

\[
A:=\sum_{j=2}^N\frac{c_j}{j}.
\]

The first shell gives `v_1=A=0`. The discrete fractional-part identity already used in `NB-020`,

\[
\left\{\frac nj\right\}
-
\left\{\frac{n-1}{j}\right\}
=
\frac1j-\mathbf1_{j\mid n},
\tag{14}
\]

then yields, for `2<=n<=N`,

\[
0=v_n-v_{n-1}
=A-
\sum_{\substack{j\mid n\\j\ge2}}c_j
=-
\sum_{\substack{j\mid n\\j\ge2}}c_j.
\tag{15}
\]

At `n=2` this forces `c_2=0`; induction on `n` forces `c_n=0` for every `n<=N`. Thus the dictionary is independent and `dim V_N=N-1`.

The coefficient vectors of `h_M,...,h_(N-1)` are the ordinary path differences in the tail block. They are independent, so `dim W_(M,N)^tail=N-M`. Since `NB-032` gives the orthogonal decomposition

\[
V_N=W_{M,N}^{\rm tail}\oplus K_{M,N},
\]

equation (2) follows. This strengthens the previous rank upper bound to an exact rank.

## 2. The quotient basis preserves every head coefficient exactly

Restricted to `V_N`, the operator `Q_(M,N)` has kernel exactly `W_(M,N)^tail` and range exactly `K_(M,N)`. For every `n>=M`, telescoping gives

\[
g_M-g_n=\sum_{r=M}^{n-1}h_r\in W_{M,N}^{\rm tail}.
\tag{16}
\]

Applying `Q_(M,N)` proves (4). Since `NB-032` already shows that the images of `g_2,...,g_M` span `K_(M,N)`, and (2) shows that both the number of these vectors and the dimension of the skeleton are `M-1`, they form the basis (3).

Now let `v_N=P_(V_N)e`. Because the full space splits orthogonally as tail plus skeleton,

\[
Q_{M,N}v_N=P_{K_{M,N}}e.
\tag{17}
\]

Applying `Q_(M,N)` termwise to the unique expansion (5), using (4), gives (6). The head coefficients are therefore not reconstructed approximately or inferred from a Gram eigenvector: they are literally unchanged by the quotient map in the canonical quotient basis. Only the tail block is identified modulo the path-difference relation, leaving its total coefficient sum as the final scalar coordinate.

This statement is basis-specific in the correct source-faithful sense. It does not claim that arbitrary coordinates on `K_(M,N)` preserve Möbius structure. The canonical basis (3) is singled out by quotienting the original arithmetic generators by the certified nuisance sector.

## 3. The shell Möbius inversion also survives intrinsically inside the skeleton

The preservation can be seen without referring back to the full coefficient vector. Let

\[
\rho_{M,N}:=e-P_{K_{M,N}}e
\]

and write `rho_(M,N;t)` for its value on `I_t`, with the usual convention `rho_(M,N;0)=1`. Since

\[
P_{K_{M,N}}e
=Q_{M,N}P_{V_N}e,
\]

we have

\[
\rho_{M,N}=r_N+P_{W_{M,N}^{\rm tail}}e.
\tag{18}
\]

`NB-031` proves that every vector in the moving tail has the rank-one early-shell profile `At` for `1<=t<M`. Hence there is a scalar `A_(M,N)` such that

\[
\rho_{M,N;t}-\rho_{M,N;t-1}
=
(r_{N,t}-r_{N,t-1})+A_{M,N}
\qquad(1\le t<M).
\tag{19}
\]

For every `2<=n<M`, Möbius inversion annihilates that added constant because

\[
\sum_{d\mid n}\mu(n/d)=0.
\]

Combining (19) with the exact `NB-020` shell inversion gives

\[
\boxed{
a_{N,n}
=
\sum_{d\mid n}
\mu\!\left(\frac nd\right)
\bigl(\rho_{M,N;d}-\rho_{M,N;d-1}\bigr),
\qquad 2\le n<M.
}
\tag{20}
\]

Thus the head Möbius coordinates are recoverable from the **compressed skeleton residual itself**. If

\[
\kappa_{M,N}:=\|\rho_{M,N}\|,
\]

the same shell-norm argument as in `NB-020` yields the intrinsic bound

\[
\boxed{
|a_{N,n}+\mu(n)|
\le2\kappa_{M,N}\sigma(n)
\qquad(2\le n<M).
}
\tag{21}
\]

Equation (21) is weaker than (11) when `kappa_(M,N)>d_N`; its role is structural. It shows that Möbius inversion is native to the compressed target-bearing skeleton rather than an artifact of retaining the discarded tail coordinates.

## 4. Burnol's floor upgrades additive compression to relative compression at polylog rank

`NB-032` gives the exact distance identity

\[
\kappa_{M,N}^2
=d_N^2+
\|P_{W_{M,N}^{\rm tail}}e\|^2,
\tag{22}
\]

while `NB-031` gives

\[
\|P_{W_{M,N}^{\rm tail}}e\|^2
\le
\varepsilon_M,
\qquad
\varepsilon_M
=
\frac1M+
\frac{(H_M-1)^2}{M-H_M}
=O\!\left(\frac{(\log M)^2}{M}\right).
\tag{23}
\]

For the deterministic choice (7),

\[
\varepsilon_{M_N}
=O\!\left(
\frac1{\log N\,\log\log N}
\right).
\tag{24}
\]

The unconditional Burnol lower bound already anchored and used in this line gives, for some absolute `c_B>0` and all sufficiently large `N`,

\[
d_N^2\ge\frac{c_B}{\log N}.
\tag{25}
\]

Therefore

\[
0\le
\frac{\kappa_N^2}{d_N^2}-1
\le
\frac{\varepsilon_{M_N}}{d_N^2}
=O\!\left(\frac1{\log\log N}\right),
\tag{26}
\]

which proves (8). More generally, any predeclared `M_N<N` satisfying

\[
\frac{M_N}
{\log N\,(\log M_N)^2}
\longrightarrow\infty
\tag{27}
\]

gives `kappa_(M_N,N)/d_N->1` by the same argument. The choice (7) is only a simple explicit near-logarithmic scale.

This sharpens the interpretation of `NB-032`. Arbitrarily slowly growing rank is enough to preserve the **limiting** distance, but preserving the finite-section distance on its own scale requires the removed target mass to be `o(d_N^2)`. Burnol's universal floor shows that this stronger requirement still costs only a polylogarithmic rank.

## 5. The whole forced Möbius core fits below the deterministic cutoff

`NB-020` proves that the canonical best coefficients obey

\[
|a_{N,n}+\mu(n)|\le2d_N\sigma(n)
\tag{28}
\]

and, using a positive weighted density of squarefree indices with controlled divisor sum, that the forced Möbius core extends to an absolute multiple of `d_N^(-1)` whenever the distance is small. Burnol's bound (25) also gives

\[
d_N^{-1}\ll\sqrt{\log N}.
\tag{29}
\]

Hence

\[
x_N\asymp d_N^{-1}
\ll\sqrt{\log N}
=o(M_N).
\tag{30}
\]

All of those coefficients therefore lie in the unchanged head part of (6). Along a closure subsequence `d_N->0`, the local weighted-density argument of `NB-020` gives

\[
\sum_{\substack{n\le x_N\\
\mu(n)^2=1\\
\sigma(n)\le C_0n}}
n|a_{N,n}|
\gg x_N^2
\asymp d_N^{-2},
\tag{31}
\]

which implies (12). The same coefficients occur, without any transfer error, in the canonical quotient basis of `K_(M_N,N)`.

This is stronger than saying that the quotient preserves the target distance. The skeleton simultaneously preserves, at relative `1+o(1)` distance accuracy, the complete low-index coefficient region that the target itself forces toward the Möbius pattern. The discarded high-index adjacent sector is therefore a genuine nuisance sector not only target-geometrically but also with respect to the already-established source lock.

## 6. Adversarial controls, prior art, and research consequence

Several limitations remain decisive. First, low rank is not low computational cost. Constructing `Q_(M,N)` still requires the full tail Gram geometry, and the quotient basis (3) may be severely ill-conditioned. Nothing here supplies a stable `O(M)` algorithm or a uniformly bounded skeleton Gram inverse.

Second, the coefficient preservation in (6) is exact but coordinate-specific. `NB-030` already shows that large raw coefficient loading is not a substitute for Gram-whitened target occupation. Equation (12) therefore does not by itself force a new low-eigenvalue target mass theorem. The next useful estimate must control the Gram geometry of the quotient basis or an invariant Hilbert quantity built from the preserved Möbius block.

Third, the tail is not arithmetically empty. It collapses to the single scalar `sum_(n=M)^N a_(N,n)`, and `NB-028` shows that related partial coefficient sums are tied to Mertens cancellation plus residual error. This scalar, or the way it couples to `k_M^(M,N)`, may still carry genuinely global information. The theorem says that the other `N-M` tail degrees of freedom are unnecessary for the target distance at the stated precision; it does not control the surviving endpoint channel.

Fourth, (8) does not improve `d_N`; it says that the compressed problem reproduces whatever the full finite section does. Burnol's theorem is used only as a lower floor to compare `NB-031`'s discarded target mass with the existing error. No RH-strength Möbius estimate is imported.

The finite independence argument, quotient algebra, and rank calculation are elementary. A targeted prior-art check covered Báez-Duarte/Bagchi finite Nyman sections, Jousse's work on continuity of projections onto varying Nyman subspaces, recent Gram-compressibility work of Hugh Carvill, Jongho Yang's Friedrichs-angle study, and searches for successive/adjacent-difference tail quotients. The accessible statements did not identify the exact pushforward (6), the intrinsic compressed Möbius inversion (20), or the predeclared polylog-rank relative-distance consequence (8). Search absence is not a priority claim. No new external theorem is load-bearing beyond Burnol and the classical Nyman sources already anchored in `SOURCES.md`, so the source list is unchanged.

The live question after `NB-032` is therefore narrower. The moving-tail quotient already gives a **source-faithful, polylogarithmic-rank representation** of the finite problem: it preserves the target distance relatively and retains the whole forced Möbius head. What remains is not to find the arithmetic signal after compression — that signal is explicitly present — but to control the Gram/conditioning geometry of this quotient signal, or to show that the surviving endpoint scalar and globally conditioned quotient basis can still reproduce all of the hard behavior of the original section. Until such a bound is obtained, `NB-033` is a structural compression theorem rather than an approximation-rate improvement and gives no independent evidence for RH.