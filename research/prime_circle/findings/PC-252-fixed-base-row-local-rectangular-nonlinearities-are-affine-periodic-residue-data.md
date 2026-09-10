# PC-252 — fixed-base row-local rectangular nonlinearities are affine-periodic residue data

**Status:** `EXACT-DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the higher-order/common-row rectangular escape left open by PC-249 and PC-251. Fix distinct lower primes

\[
p_1,\ldots,p_m,
\qquad
M:=\prod_{i=1}^m p_i,
\tag{1}
\]

and let `q` be a prime larger than every lower prime and every pairwise Frobenius threshold

\[
Q_0:=\max_{i<j}(p_ip_j-p_i-p_j).
\tag{2}
\]

Write the complete `q`-row data of the native rectangular prime-transfer packets as

\[
R_q(u):=
\bigl(K_{p_1,q}(u,\cdot),\ldots,K_{p_m,q}(u,\cdot)\bigr),
\qquad 0\le u<q.
\tag{3}
\]

For **any fixed, `q`-independent row-local readout** `F` from this fixed finite-dimensional row space to a finite-dimensional complex vector space, define

\[
A_F(q):=\sum_{u=0}^{q-1}F(R_q(u)).
\tag{4}
\]

Then there are a fixed vector `A_F^bulk` and a function

\[
B_F:(\mathbb Z/M\mathbb Z)^\times\to V
\tag{5}
\]

such that, for every admissible prime `q>Q_0`, exactly

\[
\boxed{
A_F(q)=qA_F^{\rm bulk}+B_F(q\bmod M).
}
\tag{6}
\]

No regularity, linearity, polynomiality, commutativity, or spectral hypothesis on `F` is required. After the elementary linear bulk term is removed, the complete upper-prime dependence of every fixed row-local nonlinear contraction is only finite residue data modulo the fixed product `M`.

There is an especially sharp multilinear corollary. If each distinct lower packet occurs once and all upper rows are contracted before any pairwise Gram compression, then even the residue term disappears. With

\[
\mathcal T_q(t_1,\ldots,t_m)
:=\sum_{u=0}^{q-1}
\prod_{i=1}^m K_{p_i,q}(u,t_i),
\tag{7}
\]

one has

\[
\boxed{
\mathcal T_q(t_1,\ldots,t_m)
=q\Bigl(\prod_{i=1}^m p_i\Bigr)
\left|\bigcap_{i=1}^m
\left[\frac{t_i}{p_i},\frac{t_i+1}{p_i}\right)
\right|.
}
\tag{8}
\]

Thus the most direct genuinely higher-order shared-upper relation proposed after PC-251 stabilizes exactly to a fixed lower-grid intersection tensor. It carries no upper-prime residue at all once the lower boundary meshes are pairwise separated.

## 1. Native rectangular packets as one moving integer grid

PC-246 and PC-249 give the exact interval representation, for `p<q`,

\[
K_{p,q}(u,t)
=p\left|
[u,u+1)\cap
\left[\frac{qt}{p},\frac{q(t+1)}p\right)
\right|.
\tag{9}
\]

Equivalently, scale back to `[0,1]`. The lower `p_i`-partition consists of the cells

\[
I_t^{(p_i)}=
\left[\frac{t}{p_i},\frac{t+1}{p_i}\right),
\tag{10}
\]

while the upper `q`-grid samples them with cells of length `1/q`.

Let `\mathcal B` be the union of all interior lower-grid boundaries

\[
\mathcal B
=
\bigcup_{i=1}^m
\left\{\frac{k}{p_i}:1\le k<p_i\right\}.
\tag{11}
\]

Together with `0,1`, these points partition `[0,1]` into finitely many joint atoms `J`. On the interior of each atom every lower label is fixed. If `t_i(J)` denotes that label, define the corresponding pure row state

\[
r_J:=
\bigl(p_1e_{t_1(J)},\ldots,p_me_{t_m(J)}\bigr).
\tag{12}
\]

The natural bulk value associated with an arbitrary fixed row readout is therefore

\[
\boxed{
A_F^{\rm bulk}
:=\sum_J |J|F(r_J).
}
\tag{13}
\]

All endpoints of the joint atoms have denominator dividing `M`.

## 2. Beyond the pairwise Frobenius thresholds, every exceptional upper cell contains one lower boundary at most

For two distinct lower primes `p_i,p_j`, PC-249 proves that an upper unit cell can contain an interior boundary from both lower meshes only if

\[
q\le p_ip_j-p_i-p_j.
\tag{14}
\]

Hence `q>Q_0` excludes every cross-mesh double boundary. Since also `q>p_i`, consecutive boundaries of the same `p_i`-mesh are separated by `q/p_i>1` in the scaled `[0,q]` coordinate. Therefore

\[
\boxed{
q>Q_0,\ q>\max_i p_i
\quad\Longrightarrow\quad
\text{every upper cell contains at most one point of }q\mathcal B.
}
\tag{15}
\]

This elementary separation is the entire load-bearing mechanism. A non-boundary upper cell lies wholly inside one joint atom and has exactly the pure row state `r_J`. A boundary cell contains one point

\[
\beta=\frac{k}{p_i}.
\tag{16}
\]

Its fractional cut position is

\[
\theta_q(\beta)
=\left\{\frac{qk}{p_i}\right\}
=\frac{qk\bmod p_i}{p_i}.
\tag{17}
\]

The `p_i` packet row is split between the two adjacent columns according to this fraction. Every other lower packet is constant across that same upper cell, because no second lower boundary occurs there. Its column label is determined solely by the position `k/p_i` among the fixed lower partitions. Consequently the **entire exceptional row state** at `\beta` depends on `q` only through `q mod p_i`, hence only through `q mod M`.

This is stronger than saying that an invariant of the row state is periodic: the full vector `R_q(u)` at every boundary cell is repeated when the upper scale is changed within one residue class modulo `M`.

## 3. Exact affine periodicity of every fixed row-local nonlinear readout

Take two admissible upper integers `q,q'>Q_0` with

\[
q'\equiv q\pmod M.
\tag{18}
\]

The statement is algebraic for any such coprime upper integers; primality merely selects the source-forced Prime-Circle subsequence. Write

\[
q'-q=\ell M.
\tag{19}
\]

For a joint atom `J=[a,b)` all numbers `Ma` and `Mb` are integers. Therefore scaling from `qJ` to `q'J` translates its two endpoints by the integers `\ell Ma` and `\ell Mb`. The fractional endpoint configurations are unchanged, while the number of complete unit cells contained in that atom increases by exactly

\[
\ell M(b-a)=(q'-q)|J|.
\tag{20}
\]

Every one of those added cells contributes the same pure value `F(r_J)`. By (17)--(18), meanwhile, each boundary cell has exactly the same row state for `q` and `q'`, so all boundary contributions cancel in the difference. Hence

\[
\begin{aligned}
A_F(q')-A_F(q)
&=(q'-q)\sum_J|J|F(r_J)\\
&=(q'-q)A_F^{\rm bulk}.
\end{aligned}
\tag{21}
\]

Thus

\[
A_F(q)-qA_F^{\rm bulk}
\tag{22}
\]

is constant on each admissible residue class modulo `M`, proving (6). This proof does not use a Taylor expansion or polynomial approximation to `F`: once the lower bases are fixed, exact boundary separation reduces the problem to a finite set of repeated row states.

As a concrete nonlinear control, take lower primes `3,5` and

\[
F(R)=\|R_3\|_2^2\,\|R_5\|_2^2.
\tag{23}
\]

Here `M=15`, `Q_0=7`, and direct exact overlap arithmetic gives

\[
A_F^{\rm bulk}=225.
\tag{24}
\]

For the three primes `31,61,151`, all congruent to `1 mod 15`, one obtains respectively

\[
6415,\quad 13165,\quad 33415,
\tag{25}
\]

and in every case

\[
A_F(q)-225q=-560.
\tag{26}
\]

The example is only a finite falsification check; equation (21) is the exact proof.

## 4. Higher-order shared-upper contraction collapses more strongly than the general theorem

The principal escape left after PC-249/PC-251 was to retain several rectangles in their common upper orientation and form a genuinely higher-order relation **before** pairwise Gram contraction. Equation (7) is the canonical row-contracted multilinear tensor for that proposal.

On an upper cell `C_u=[u,u+1)`, equation (15) says that at most one of the lower indicator functions can change value. Every other lower indicator is constant, equal to `0` or `1`, on the whole cell. Therefore, for every column tuple `(t_1,...,t_m)`,

\[
\prod_{i=1}^m
|C_u\cap qI_{t_i}^{(p_i)}|
=
\left|C_u\cap
\bigcap_{i=1}^m qI_{t_i}^{(p_i)}
\right|.
\tag{27}
\]

Multiplying by `\prod_i p_i`, summing over the unit partition, and scaling back by `q` proves (8).

For example, with lower primes `(3,5,7)` the largest pairwise threshold is `5\cdot7-5-7=23`. At `q=29`,

\[
\mathcal T_{29}(0,0,0)
=29\cdot3\cdot5\cdot7\cdot\frac17
=435,
\tag{28}
\]

and the same identity holds entrywise for the full `3 x 5 x 7` tensor. No trace, determinant, singular-value ordering, or pairwise Gram has been taken: the complete higher-order tensor itself has already lost all non-scalar upper-level information.

If one repeats a lower packet inside the same row-local nonlinearity, powers of the fractional boundary split need not cancel as in (27). Equation (6) classifies exactly what remains: a finite correction depending only on `q mod M`. Thus repeated factors do not reopen a growing upper-scale carrier either.

## 5. Finite character classicalization and the RH boundary

Because `B_F` is a function on the finite unit group `(Z/MZ)^x`, finite Fourier inversion gives

\[
\boxed{
B_F(q)
=\sum_{\chi\bmod M} b_\chi\chi(q),
}
\tag{29}
\]

with vector coefficients `b_chi`; characters that do not occur simply have zero coefficient. Unlike the centered Gram packets in PC-248, a raw oriented rectangle need not identify `q` with `-q`, so the full character group can occur. That distinction does not change the information ceiling: it remains one finite Dirichlet-character packet at fixed `M`.

Consequently a prime-only Dirichlet aggregation of (6) contains only two established pieces. In a half-plane of absolute convergence,

\[
\sum_{q\ {m prime}}
\frac{A_F(q)}{q^s}
=
A_F^{\rm bulk}
\sum_{q\ {m prime}}q^{1-s}
+
\sum_{\chi\bmod M}b_\chi
\sum_{q\ {m prime}}\frac{\chi(q)}{q^s},
\tag{30}
\]

up to the finite initial levels excluded by the threshold. The first term is the shifted ordinary prime-zeta series; the second is the same finite Dirichlet prime-character package already classicalized in PC-247/PC-248 through Euler products and Möbius inversion. Any zeta or Dirichlet-`L` singularities obtained after this aggregation are therefore inherited from the standard prime/Dirichlet transform, not produced by a new Prime-Circle operator, functional equation, or critical-line symmetry.

The exact result is actually stronger than what is needed for that analytic conclusion: the finite residue quotient is present before any Mellin/Dirichlet transform is introduced.

## 6. Prior-art and novelty audit

No novelty is claimed for rational interval partitions, floor/lattice counting, finite residue periodicity, the two-generator Frobenius threshold, finite Fourier analysis on `(Z/MZ)^x`, or Dirichlet-character expansions. The affine-plus-periodic form in (6) is the one-dimensional rational-lattice/quasi-polynomial behavior one should expect once the finite lower boundary arrangement is fixed. PC-249 already identified the pairwise threshold as the classical Frobenius number, and PC-248 already supplies the relevant finite-character ceiling after a finite residue quotient has been established.

A targeted literature audit over rational lattice-point/quasi-polynomial counting, uniform partition overlaps, conditional-expectation products, multiway partition tables, and Frobenius boundary separation found only these classical ambient structures. The present negative conclusion does not rely on failure to locate an identical formula in the literature: equations (15)--(21) explicitly prove the finite residue quotient, and (27) proves the stronger multilinear collapse.

The project-local mathematical delta is therefore precise but negative. PC-249 closed pairwise shared-upper Grams at fixed lower bases, while PC-251 left higher-order rectangular relations before pairwise contraction as a possible escape. PC-252 shows that **every fixed row-local nonlinear contraction** is eventually only affine bulk plus finite residue data, and that the canonical distinct-base higher-order contraction is exactly upper-prime blind after its scalar factor `q` is removed.

## 7. Matched controls and strict surviving boundary

The proof after (9) uses only commensurable uniform partitions and coprimality. Replace the lower primes by any fixed finite family of pairwise-coprime integers and artificially assign the same all-one uniform transfer masks. Once the corresponding pairwise boundary meshes are separated, the same affine-periodic theorem and multilinear collapse hold, with `M` replaced by their common multiple. Therefore the mechanism responsible for (6) and (8) is source-blind partition geometry. Prime cyclotomy supplies these packets canonically; primality is not what makes the fixed-base nonlinear carrier stabilize.

This closes the chain

\[
\boxed{
\text{fixed finitely many lower prime packets}
\to
\text{common upper row orientation}
\to
\text{arbitrary fixed row-local nonlinear contraction}
\to
\text{new growing RH carrier}.
}
\tag{31}
\]

The theorem does **not** cover a readout whose lower bases grow with `q`, a rule whose interaction range or state dimension itself grows with `q`, dependence on absolute upper-row labels not reconstructible from the packet rows, nonlocal couplings between separated upper rows, several independent upper scales retained simultaneously, native composite cyclotomic masks, or an infinite-dimensional limit taken before the fixed-base quotient. Those are materially different inputs rather than more elaborate choices of the fixed row-local `F` in (4).

In particular, the comparable-scale regime isolated by PC-251 remains outside this theorem because then `M` and the boundary arrangement grow with the upper scale rather than staying fixed. The same is true of genuinely nonlocal row-to-row operators. What no longer survives as a distinct escape is **fixed-base higher arity or fixed-base row-local nonlinearity before Gram compression**.