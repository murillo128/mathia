# FD-018 — fixed geometric GCD-duality saturation has a squarefree-dilation dichotomy

**Status:** `EXACT-DERIVED + FIXED-DILATION-DICHOTOMY + NONSQUAREFREE-INTERPOLATION + SQUAREFREE-COLLISION-OBSTRUCTION + MULTIHORIZON-BOUNDARY + NEGATIVE/OBSTRUCTION`.

`FD-015` and `FD-017` leave an apparent gap in the multihorizon picture. A fixed **squarefree** dilation forces a two-horizon saturation deficit through a repeated-prime collision, whereas a dilation ratio tending to infinity eventually exposes a growing fresh equality-ray prefix and allows full asymptotic saturation. The fixed-ratio case is not uniformly coercive. In the unrestricted real-source relaxation, the exact dividing line for a geometric chain is whether the fixed integer dilation is squarefree.

Let

\[
K_H(d,e)=\frac{\gcd(d,e)^2}{de},
\qquad
C_R=(K_R^{-1})_{11}
=\sum_{r\le R}\frac{\mu(r)^2}{J_2(r)},
\qquad
Z:=\zeta(2),
\tag{1}
\]

and, for a real sequence `A(1),A(2),...`, define

\[
m_d^{(H)}:=A\!\left(\left\lfloor\frac Hd\right\rfloor\right),
\qquad
E_H:=(m^{(H)})^TK_Hm^{(H)},
\qquad
R_H:=\frac{A(H)^2}{E_H}
\tag{2}
\]

when the horizon vector is nonzero, with `R_H:=0` for the zero vector.

Fix an integer `q>=2` and an initial horizon `H_0>=1`, and put

\[
H_j=q^jH_0.
\tag{3}
\]

Then the following dichotomy holds for the unrestricted source class:

\[
\boxed{
\begin{array}{ll}
q\ \text{squarefree}
&\Longrightarrow\quad
\text{there is no real source }A\text{ with }R_{H_j}\to Z,\\[2mm]
q\ \text{nonsquarefree}
&\Longrightarrow\quad
\text{there exists one real source }A\text{ with }R_{H_j}\to Z.
\end{array}}
\tag{4}
\]

The constructive half is stronger in a finite-prefix form. After discarding finitely many initial horizons, set `R_j=j+2` with the tail reindexed from `j=0`. For every positive sequence `delta_j -> 0`, one can choose a single source `A` so that

\[
\boxed{
R_{H_j}>C_{R_j}-\delta_j
\qquad(j\ge0),
}
\tag{5}
\]

on that tail. Since `R_j -> infinity` and `C_R -> Z`, equation (5) implies the second half of (4).

The mechanism is exact. When two prefix floor-quotient locations on different members of a fixed `q`-geometric chain coincide, sufficiently shallow growing prefixes force the corresponding divisor indices to differ by an exact power of `q`. If `q` is nonsquarefree, every such later index is itself nonsquarefree, and the finite GCD equality ray is **exactly zero there**. Cross-scale collisions therefore hit only zero coordinates of the new equality ray and cannot prevent the nonzero part of an increasingly long prefix from being planted at each stage.

This result concerns only the arbitrary-real-source relaxation used to test how much information common-source coherence carries. The constructed source has no Möbius increment, divisor-identity, or bounded-jump constraint. It is not a Mertens function and gives no Farey discrepancy counterexample.

## 1. The finite equality ray vanishes exactly on nonsquarefree coordinates

Write, as in `FD-003` and `FD-015`,

\[
u^{(R)}:=K_R^{-1}e_1.
\tag{6}
\]

The inverse-column formula is

\[
u_d^{(R)}
=d\sum_{\substack{r\le R\\d\mid r}}
\frac{\mu(r/d)\mu(r)}{J_2(r)}.
\tag{7}
\]

If `d` is nonsquarefree, every multiple `r` of `d` is nonsquarefree, hence `mu(r)=0` termwise. Therefore

\[
\boxed{u_d^{(R)}=0\qquad(d\le R\text{ nonsquarefree}).}
\tag{8}
\]

Also

\[
u_1^{(R)}=C_R,
\qquad
(u^{(R)})^TK_Ru^{(R)}=C_R.
\tag{9}
\]

Equation (8), rather than mere smallness, is what makes a fixed nonsquarefree dilation behave differently from a fixed squarefree one.

## 2. A collision lemma for shallow prefixes on a geometric chain

It is enough to work on a tail of (3). Reindex that tail so that

\[
H_j=q^jH_*,
\qquad
R_j=j+2,
\tag{10}
\]

where `H_*` is chosen large enough that

\[
H_j>2R_j^2
\qquad(j\ge0).
\tag{11}
\]

For a nonsquarefree integer `q` one has `q>=4`; thus, for example, `H_*>=9` makes (11) persist, because multiplying the left side by at least `4` dominates the successive quadratic growth of `(j+2)^2`.

The same choice also gives, for every `i<j`,

\[
R_j\le q^{j-i}R_i.
\tag{12}
\]

Indeed it is enough to check adjacent indices, where `j+2 <= q(j+1)` for `q>=4`.

Define the visible source set at horizon `H_i` by

\[
S_i:=\left\{\left\lfloor\frac{H_i}{e}\right\rfloor:1\le e\le H_i\right\},
\tag{13}
\]

and the prefix locations at horizon `H_j` by

\[
x_{j,d}:=\left\lfloor\frac{H_j}{d}\right\rfloor,
\qquad1\le d\le R_j.
\tag{14}
\]

The key exact statement is:

\[
\boxed{
 x_{j,d}\in S_i,\ i<j,\ d\le R_j
 \quad\Longrightarrow\quad
 d=q^{j-i}e\text{ for some }e\le R_i.
}
\tag{15}
\]

To prove it, put `lambda=q^(j-i)` and suppose

\[
\left\lfloor\frac{H_j}{d}\right\rfloor
=
\left\lfloor\frac{H_i}{e}\right\rfloor.
\tag{16}
\]

Equality of the floors gives

\[
\left|\frac{H_j}{d}-\frac{H_i}{e}\right|<1,
\]

hence

\[
H_i\,|\lambda e-d|<de.
\tag{17}
\]

The common floor is at least `H_j/d-1`. Therefore

\[
\frac{H_i}{e}
>\frac{H_j}{d}-1
=\frac{\lambda H_i}{d}-1.
\]

Because (11) implies `H_j>2d`, the denominator below is positive and

\[
e
<\frac{dH_i}{\lambda H_i-d}
<\frac{2d}{\lambda}.
\tag{18}
\]

Consequently

\[
de<\frac{2d^2}{\lambda}
\le\frac{2R_j^2}{\lambda}
<\frac{H_j}{\lambda}=H_i.
\tag{19}
\]

If `lambda e-d` were nonzero, its absolute value would be at least `1`, contradicting (17) and (19). Thus `d=lambda e`. Equation (12) then gives `e=d/lambda<=R_i`, proving (15).

There is also no collision between a prefix coordinate and the tail of the **same** horizon. From (11), for `d<=R_j`,

\[
\frac{H_j}{d}-\frac{H_j}{d+1}
=\frac{H_j}{d(d+1)}>1,
\tag{20}
\]

so the first `R_j+1` floor quotients are strictly decreasing. Hence every location (14) is distinct and no coordinate with index greater than `R_j` samples one of them.

## 3. Nonsquarefree dilation makes every inherited prefix collision a zero-coordinate collision

Assume now that `q` is nonsquarefree. If a current prefix location `x_(j,d)` was already visible at an earlier horizon `H_i`, (15) gives

\[
d=q^{j-i}e.
\tag{21}
\]

Thus `q|d`. Since `q` contains a squared prime factor, `d` is nonsquarefree. Equation (8) therefore gives

\[
\boxed{u_d^{(R_j)}=0}
\tag{22}
\]

for **every** prefix coordinate whose source location may already have been assigned by an earlier stage.

This is the exact compatibility that the sparse construction of `FD-017` did not need. The prefix is not literally fresh at fixed multiplicative spacing. Instead, every non-fresh prefix coordinate lies on the square-killed zero stratum of the equality ray. All coordinates carrying nonzero equality-ray data remain free to be planted.

## 4. Sequential interpolation on the fixed geometric chain

Construct one sequence `A` inductively over the tail horizons. At stage `j`, let

\[
u^{(j)}:=K_{R_j}^{-1}e_1.
\tag{23}
\]

For each prefix location `x_(j,d)`, `d<=R_j`, do the following. If that source value has not previously been assigned, set

\[
A(x_{j,d})=t_j u_d^{(j)}.
\tag{24}
\]

If it has already been assigned, leave it unchanged. By (22), the desired coefficient at every such inherited location is zero, so the inherited value contributes only an additive error independent of `t_j`. Set every other still-unassigned source location visible at `H_j` to zero.

At the first retained horizon there is no earlier visibility constraint, so the same prescription starts the induction. At every later stage the entire horizon vector has the form

\[
\boxed{
m^{(H_j)}=t_j\widetilde u^{(j)}+b_j,}
\tag{25}
\]

where `widetilde u^(j)` is `u^(j)` embedded in the first `R_j` coordinates and `b_j` is completely determined before `t_j` is chosen. The within-horizon separation (20) ensures that no tail coordinate duplicates one of the newly assigned nonzero prefix locations.

The endpoint location `H_j=x_(j,1)` is always new, since every earlier visible source location is at most `H_(j-1)<H_j`. Hence

\[
A(H_j)=t_j u_1^{(j)}=t_jC_{R_j}.
\tag{26}
\]

The top-left `R_j x R_j` principal block of `K_(H_j)` is exactly `K_(R_j)`, so

\[
(\widetilde u^{(j)})^TK_{H_j}\widetilde u^{(j)}=C_{R_j}.
\tag{27}
\]

Therefore

\[
E_{H_j}
=t_j^2C_{R_j}
+2t_j(\widetilde u^{(j)})^TK_{H_j}b_j
+b_j^TK_{H_j}b_j,
\tag{28}
\]

and, for fixed inherited data,

\[
R_{H_j}
=\frac{t_j^2C_{R_j}^2}{E_{H_j}}
\longrightarrow C_{R_j}
\qquad(|t_j|\to\infty).
\tag{29}
\]

Choose a finite nonzero `t_j` large enough that (5) holds. Later stages never overwrite an assigned source value, so earlier horizon vectors remain unchanged. The collision lemma ensures that any later prefix location already seen earlier is precisely one of the zero-coordinate cases already absorbed into `b_j`; no hidden consistency condition is being postponed.

Taking `delta_j -> 0` and using the `FD-003` limit

\[
C_{R_j}\longrightarrow Z
\tag{30}
\]

proves

\[
R_{H_j}\longrightarrow Z.
\tag{31}
\]

Because only a tail of the original chain was reindexed, finitely many omitted initial horizons do not affect the limit. Thus the nonsquarefree half of (4) holds for every initial `H_0>=1`.

## 5. Squarefree dilations give the converse obstruction

Assume instead that `q` is squarefree. Choose any prime `p|q`. `FD-015` proves that there is a constant

\[
\kappa_{q,p}<Z
\tag{32}
\]

such that, for every sufficiently large `H`, every real source satisfies

\[
\min\{R_H,R_{qH}\}<\kappa_{q,p}.
\tag{33}
\]

Apply this to consecutive members `H_j,H_(j+1)` of (3). If one source had `R_(H_j)->Z`, then eventually both members of every adjacent pair would exceed the fixed number `kappa_(q,p)`, contradicting (33). Therefore full asymptotic saturation is impossible for squarefree `q`.

Combining this with the construction above proves the dichotomy (4).

## 6. Consequence for the current multihorizon frontier

`FD-016` showed that a fixed `Q`-geometric chain can approach `C_(Q-1)` by keeping a **fixed** fresh prefix. `FD-017` showed that full `Z`-saturation is possible when the multiplicative gaps diverge, because a growing prefix becomes genuinely fresh. The present result inserts a qualitatively different mechanism between them: even with fixed bounded spacing, a growing prefix can be asymptotically planted when every cross-scale collision lands on an exact zero of the GCD equality ray.

Thus bounded multiplicative spacing is not by itself the sought nonreconstructive/coercive regime. At least for pure integer geometric chains in the unrestricted source model, the arithmetic of the **dilation** matters sharply: squarefree dilations preserve a repeated-prime incompatibility, while nonsquarefree dilations make all cross-stage prefix collisions square-killed and therefore harmless to the planted equality ray.

This also clarifies what an overlap-counting theorem would have to measure. The number of shared floor-quotient locations is insufficient; one must weight overlaps by whether they collide **nonzero equality-ray coordinates incompatibly**. A dense overlap graph can be noncoercive if its recurrent collisions live entirely in the kernel pattern generated by nonsquarefree indices.

For the physical source `A=M`, none of this supplies the missing RH estimate. The construction uses arbitrary amplitudes `t_j`, arbitrary inherited values, and no restriction on increments. A successful Farey/Mertens argument may therefore still exploit source-specific Möbius constraints that eliminate this interpolation freedom. The result only closes a natural coherence-only route and sharpens the location of the missing hypothesis.

## 7. Prior art, novelty boundary, and falsification points

The square-GCD matrix, its inverse-column formula, and `C_R -> zeta(2)` are the classical Smith/Jordan GCD-matrix ingredients already audited in `FD-003`. The squarefree repeated-prime obstruction is `FD-015`; the interpolation template is `FD-016`--`FD-017`.

Targeted literature checks also covered Jean-Paul Cardinal, *Symmetric matrices related to the Mertens function* (Linear Algebra Appl. **432** (2010), 161--172; arXiv:0811.3701), and Jeffrey C. Lagarias--David H. Richman, *The floor quotient partial order* (Adv. Appl. Math. **153** (2024), 102615; arXiv:2212.11689), together with their later `a`-floor quotient family (arXiv:2403.04342). Those works establish neighboring Mertens-matrix and floor-quotient structure; the present proof does not import a theorem from them. Searches by the fixed-geometric-horizon, GCD-matrix, Mertens, floor-quotient, and saturation formulations did not locate the dichotomy (4), but search absence is not a broad novelty claim.

The constructive proof has four decisive audit points. First, (15) must force exact divisor-index scaling rather than approximate scaling; this is where (11) is used. Second, (12) must put the recovered earlier index inside the earlier planted prefix. Third, nonsquarefreeness of `q` must force every later collision index `d=q^(j-i)e` into the exact zero set (8). Fourth, the residual vector `b_j` in (25) must be independent of the newly chosen `t_j`. Failure of any one point would break the interpolation.

The squarefree converse is only as broad as `FD-015`: it uses a fixed squarefree integer dilation and the unrestricted common-source GCD-duality ratios. The theorem does not classify non-geometric schedules, variable bounded ratios, mixtures of squarefree and nonsquarefree transitions, or sources with Möbius-specific arithmetic constraints.

The durable conclusion is exact but deliberately limited: **for fixed integer geometric horizon sampling in the unrestricted GCD-duality source relaxation, full asymptotic saturation of the sharp one-horizon constant is possible exactly for nonsquarefree dilations.**