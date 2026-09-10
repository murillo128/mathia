# FD-020 — Cesàro GCD-duality saturation is classified by density of bounded squarefree transitions

**Status:** `EXACT-DERIVED + CESARO-SATURATION-DICHOTOMY + TRANSITION-DENSITY-CLASSIFICATION + MIXED-SCHEDULE-INTERPOLATION + MULTIHORIZON-BOUNDARY + NEGATIVE/OBSTRUCTION`.

`FD-019` classifies **pointwise** saturation on integer-ratio horizon chains: one unrestricted real source can satisfy `R_(H_j) -> zeta(2)` exactly when bounded squarefree transition ratios eventually disappear. The natural next question is whether recurrent squarefree collisions accumulate when one weakens pointwise saturation to an average over horizons. They do, but the correct threshold is not recurrence itself. It is **positive transition density**.

Retain

\[
K_H(d,e)=\frac{\gcd(d,e)^2}{de},
\qquad
C_L=(K_L^{-1})_{11}
=\sum_{r\le L}\frac{\mu(r)^2}{J_2(r)},
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

when the horizon vector is nonzero, with `R_H:=0` for the zero vector. As in `FD-003`,

\[
0\le R_H\le C_H\le Z,
\qquad
C_L\longrightarrow Z.
\tag{3}
\]

Let

\[
H_0<H_1<H_2<\cdots,
\qquad
H_j=q_jH_{j-1},
\qquad
q_j\in\mathbb Z_{\ge2}\quad(j\ge1).
\tag{4}
\]

For a fixed finite `B>=2`, write

\[
S_B(n):=
\#\{1\le j\le n:
q_j\le B\ \text{and}\ q_j\ \text{is squarefree}\}.
\tag{5}
\]

Then the unrestricted common-source relaxation has the exact Cesàro classification

\[
\boxed{
\begin{aligned}
&\text{there exists one real source }A\text{ such that}
\quad
\frac1{n+1}\sum_{j=0}^{n}R_{H_j}\longrightarrow Z\\[1mm]
&\qquad\Longleftrightarrow\\[1mm]
&S_B(n)=o(n)\quad\text{for every fixed }B<\infty.
\end{aligned}}
\tag{6}
\]

Equivalently, bounded squarefree transition ratios may recur infinitely often, but every bounded family of them must have asymptotic density zero. This is strictly weaker than the `FD-019` pointwise criterion. For example, a fixed squarefree transition such as `q_j=2` may occur infinitely often on a zero-density set of indices while the Cesàro mean still saturates `Z` for a suitably constructed unrestricted source.

Conversely, if some bounded squarefree family occurs with positive upper density, the average deficit from `Z` is bounded away from zero along a subsequence. More precisely, for every fixed `B` there are constants `delta_B>0` and `J_B` such that every source satisfies

\[
\boxed{
2\sum_{i=0}^{n}(Z-R_{H_i})
\;>\;
delta_B\bigl(S_B(n)-J_B\bigr)
\qquad(n\ge J_B).
}
\tag{7}
\]

Thus a positive density of bounded squarefree transitions produces a genuine additive multihorizon gap. What it does **not** produce is an RH-scale estimate: the constants inherited from the two-horizon obstruction deteriorate with the transition bound, and the theorem remains inside the arbitrary-real-source relaxation.

## 1. Bounded squarefree transitions force an additive average deficit

Fix `B>=2`. Only finitely many squarefree integers `q` lie in `[2,B]`. For each such `q`, choose a prime `p|q` and use the `FD-015` two-horizon theorem

\[
\min\{R_H,R_{qH}\}<\kappa_{q,p}<Z
\qquad(H\ge400q^2).
\tag{8}
\]

Set

\[
\kappa_B:=
\max_{\substack{2\le q\le B\\q\ \mathrm{squarefree}}}
\kappa_{q,p(q)},
\qquad
\delta_B:=Z-\kappa_B>0,
\tag{9}
\]

where any fixed prime divisor `p(q)` may be used. Since `H_j` grows at least geometrically, there is an index `J_B` after which every base horizon `H_(j-1)` exceeds all finitely many thresholds `400q^2` with squarefree `q<=B`.

Define the nonnegative horizon deficit

\[
d_i:=Z-R_{H_i}\ge0.
\tag{10}
\]

For every marked transition `j>J_B` counted by `S_B`, equation (8) implies

\[
\min\{R_{H_{j-1}},R_{H_j}\}<\kappa_B,
\]

and hence

\[
d_{j-1}+d_j>\delta_B.
\tag{11}
\]

Sum (11) over all marked transition edges up to `n`. Each vertex `i` belongs to at most two adjacent transition edges, so

\[
\delta_B\bigl(S_B(n)-J_B\bigr)
<
\sum_{\substack{J_B<j\le n\\q_j\le B\ \mathrm{squarefree}}}
(d_{j-1}+d_j)
\le
2\sum_{i=0}^{n}d_i.
\tag{12}
\]

This proves (7). In particular, if one source has Cesàro saturation,

\[
\frac1{n+1}\sum_{i=0}^{n}R_{H_i}\to Z,
\tag{13}
\]

then the average nonnegative deficit tends to zero. Equation (12) therefore forces

\[
\frac{S_B(n)}n\longrightarrow0
\tag{14}
\]

for every fixed `B`. This proves the necessity direction of (6).

The estimate also prices the obstruction directly. If for some `B`

\[
\limsup_{n\to\infty}\frac{S_B(n)}n=\rho_B>0,
\tag{15}
\]

choose a subsequence `n_k` on which `S_B(n_k)/n_k -> rho_B`. Then (12) gives

\[
\boxed{
\limsup_{k\to\infty}
\frac1{n_k+1}\sum_{i=0}^{n_k}R_{H_i}
\le
Z-\frac{\delta_B\rho_B}{2}.
}
\tag{16}
\]

No independence between the local pair obstructions is needed; the factor `2` is only the maximal edge incidence of a horizon in the transition chain.

## 2. Zero density permits a slowly growing equality-ray depth

Assume now that

\[
S_B(n)=o(n)
\qquad\text{for every fixed }B.
\tag{17}
\]

We construct one source that saturates in Cesàro mean while sacrificing a density-zero set of difficult horizons.

Choose integers

\[
1\le N_1<N_2<N_3<\cdots
\tag{18}
\]

recursively so large that for every `k>=1` and every `n>=N_k`,

\[
S_{2k}(n)\le\frac nk,
\tag{19}
\]

and, for every `j>=N_k`,

\[
H_j>2k^2.
\tag{20}
\]

This is possible because (17) holds for each fixed `2k` and `H_j -> infinity`.

Define the nondecreasing prefix depth

\[
L_j:=k
\qquad(N_k\le j<N_{k+1}).
\tag{21}
\]

Then

\[
L_j\to\infty,
\qquad
H_j>2L_j^2
\tag{22}
\]

for all sufficiently large `j`. Call a retained transition `j` **bad** when

\[
q_j\ \text{is squarefree and}\ q_j\le2L_j,
\tag{23}
\]

and **good** otherwise. Let `B(n)` denote the number of bad indices up to `n`. If `N_k<=n<N_(k+1)`, then every bad index after the finite initial prefix has squarefree transition ratio at most `2k`. Therefore

\[
B(n)\le S_{2k}(n)+O(1)\le\frac nk+O(1).
\tag{24}
\]

As `k->infinity` with `n`, this gives

\[
\boxed{B(n)=o(n).}
\tag{25}
\]

Thus the hypothesis yields exactly what the interpolation argument needs: a density-one set of stages on which a prefix of increasing depth can be planted compatibly.

## 3. Every good stage is either fresh or square-killed

Write

\[
u^{(L)}:=K_L^{-1}e_1.
\tag{26}
\]

The exact inverse-column formula used in `FD-018`--`FD-019` gives

\[
u_d^{(L)}
=d\sum_{\substack{r\le L\\d\mid r}}
\frac{\mu(r/d)\mu(r)}{J_2(r)},
\tag{27}
\]

so

\[
\boxed{u_d^{(L)}=0
\quad\text{whenever }d\text{ is nonsquarefree}.}
\tag{28}
\]

Consider a sufficiently large good stage `j`.

If `q_j` is squarefree, goodness means `q_j>2L_j`. Hence, for every `d<=L_j`,

\[
\left\lfloor\frac{H_j}{d}\right\rfloor
\ge
\left\lfloor\frac{H_j}{L_j}\right\rfloor
=
\left\lfloor\frac{q_jH_{j-1}}{L_j}\right\rfloor
\ge2H_{j-1}>H_{j-1}.
\tag{29}
\]

All first `L_j` source locations are therefore above every earlier horizon and are completely fresh.

Suppose instead that `q_j` is nonsquarefree and that one current prefix location had already been assigned while processing an earlier good horizon `H_i`, `i<j`. Then, for some integer `e>=1`,

\[
\left\lfloor\frac{H_j}{d}\right\rfloor
=
\left\lfloor\frac{H_i}{e}\right\rfloor,
\qquad d\le L_j.
\tag{30}
\]

Since all transition ratios are integers,

\[
\lambda:=\frac{H_j}{H_i}\in\mathbb Z_{\ge2}
\tag{31}
\]

and equality of the floors implies

\[
H_i|\lambda e-d|<de.
\tag{32}
\]

As in the collision lemma of `FD-019`, equation (22) gives `H_j>2d`; comparing the common floor yields

\[
e<\frac{2d}{\lambda},
\qquad
 de<\frac{2d^2}{\lambda}
\le\frac{2L_j^2}{\lambda}
<\frac{H_j}{\lambda}=H_i.
\tag{33}
\]

Thus the integer `lambda e-d` must vanish:

\[
\boxed{d=\lambda e.}
\tag{34}
\]

The product `lambda=H_j/H_i` contains the current transition factor `q_j`. Since `q_j` is nonsquarefree, `d` is nonsquarefree, and (28) gives

\[
\boxed{u_d^{(L_j)}=0.}
\tag{35}
\]

Therefore every inherited prefix collision at a good nonsquarefree stage occurs exactly on a zero coordinate of the current equality ray.

Finally, the first `L_j+1` floor quotients at the same horizon are strictly decreasing, because for `d<=L_j`,

\[
\frac{H_j}{d}-\frac{H_j}{d+1}
=\frac{H_j}{d(d+1)}>1
\tag{36}
\]

by (22). No tail coordinate can duplicate a newly planted prefix location.

## 4. Sequential interpolation on the density-one good set

Ignore the finite initial segment before (22), which cannot affect a Cesàro limit. Process the remaining horizon indices in increasing order, but assign source values only at **good** stages. Bad stages impose no constraint in the construction.

At a good stage `j`, let

\[
u^{(j)}:=K_{L_j}^{-1}e_1.
\tag{37}
\]

For each prefix source location

\[
x_{j,d}:=\left\lfloor\frac{H_j}{d}\right\rfloor,
\qquad1\le d\le L_j,
\tag{38}
\]

set

\[
A(x_{j,d})=t_j u_d^{(j)}
\tag{39}
\]

when that source value is still unassigned, and leave it unchanged when it was assigned earlier. By Section 3, an already assigned prefix coordinate can occur only at a nonsquarefree `d`, where `u_d^(j)=0`. Set every other still-unassigned source location visible at the current good horizon to zero. Do not assign source values that the current horizon does not sample.

Consequently the complete vector at this good horizon has the form

\[
\boxed{
m^{(H_j)}=t_j\widetilde u^{(j)}+b_j,}
\tag{40}
\]

where `widetilde u^(j)` embeds `u^(j)` into the first `L_j` coordinates and `b_j` is completely fixed before `t_j` is chosen. The endpoint `H_j` is always fresh, so

\[
A(H_j)=t_jC_{L_j}.
\tag{41}
\]

The top-left `L_j x L_j` principal block of `K_(H_j)` is `K_(L_j)`, hence

\[
(\widetilde u^{(j)})^TK_{H_j}\widetilde u^{(j)}=C_{L_j}.
\tag{42}
\]

For fixed inherited data,

\[
R_{H_j}
=
\frac{t_j^2C_{L_j}^2}
{t_j^2C_{L_j}
+2t_j(\widetilde u^{(j)})^TK_{H_j}b_j
+b_j^TK_{H_j}b_j}
\longrightarrow C_{L_j}
\quad(|t_j|\to\infty).
\tag{43}
\]

Choose a finite nonzero `t_j` so large that

\[
R_{H_j}>C_{L_j}-\frac1{L_j}.
\tag{44}
\]

Every source location visible at a processed good horizon is now assigned, and later stages never overwrite assigned values. Therefore later interpolation cannot change any earlier good horizon vector. After all good stages have been processed, assign every untouched source value arbitrarily, say zero. This may determine or alter the ratios at skipped bad horizons, but by (3) they always remain in `[0,Z]`.

Along good indices tending to infinity, equations (3), (21), and (44) give

\[
Z-R_{H_j}\longrightarrow0.
\tag{45}
\]

The bad set has density zero by (25), and every deficit is bounded by `Z`. Hence

\[
\frac1{n+1}\sum_{j=0}^{n}(Z-R_{H_j})\longrightarrow0,
\tag{46}
\]

which is exactly the Cesàro saturation in (6). This proves sufficiency.

## 5. What this changes in the multihorizon frontier

`FD-019` showed that infinitely many occurrences of one bounded squarefree transition already prevent **pointwise** saturation. The present theorem shows that this obstruction does not automatically accumulate strongly enough to prevent **average** saturation. A sparse exceptional set of incompatible transitions can simply be sacrificed: the unrestricted source interpolates increasingly accurate equality-ray prefixes on the complementary density-one set.

On the other hand, recurrent squarefree collisions with positive density cannot be ignored. Equation (7) converts their frequency directly into an additive mean deficit without assuming statistical independence, mixing, or disjointness of the pair obstructions. In this sense transition density is the first genuinely accumulating overlap statistic obtained from the current GCD-duality mechanism.

The result sharpens the line's search target. An intermediate nonreconstructive horizon family cannot be justified merely by having infinitely many bounded squarefree collisions; for average coercivity they must occupy nonvanishing density, or else carry a stronger weight than the unweighted horizon count. Even positive density yields only a fixed average constant gap for fixed `B`. Turning such overlap into a **scale-sensitive** Franel/Mertens estimate would require a quantitative scheme in which the density and the local deficits survive while the relevant transition breadth grows, without approaching the all-horizon source reconstruction of `FD-009`.

For the physical source `A=M`, the theorem remains only a relaxation boundary. The constructed source uses arbitrary amplitudes and unrestricted increments. Möbius sign, divisor, or other arithmetic constraints could obstruct Cesàro saturation even when condition (17) holds. No bound for the actual Mertens function, no improved Franel exponent, and no progress toward excluding off-critical zeros follows from (6) alone.

## 6. Prior art, novelty boundary, and falsification points

The one-horizon GCD duality and equality ray are the Smith/Jordan matrix ingredients already audited in `FD-003`; the squarefree two-horizon deficit is `FD-015`; and the exact collision/zero-coordinate interpolation mechanism is `FD-018`--`FD-019`. The proof above adds no external theorem beyond those established ingredients and elementary counting on a path graph.

A targeted literature check against the existing Farey-discrepancy source domains, including GCD matrices, Mertens/floor-quotient formulations, and Farey discrepancy, did not locate this exact Cesàro transition-density classification. That search absence is not a broad novelty claim. No new bibliographic dependency is needed in `SOURCES.md` because the theorem is derived from already audited local ingredients rather than importing a new external estimate.

The necessity direction would fail if the `FD-015` pair gap could not be made uniform over the finite set of bounded squarefree ratios, or if summing marked adjacent edges could amplify a horizon deficit more than twice; neither occurs. The sufficiency direction would fail if a good squarefree stage had a nonfresh planted prefix, if an inherited prefix coordinate at a good nonsquarefree stage could be squarefree, or if later assignments could modify an earlier good horizon. Equations (29), (34)--(35), and the rule that every visible location at a processed good stage is frozen exclude those three failure modes.

The durable conclusion is exact but limited: **for integer-ratio horizon chains in the unrestricted common-source GCD-duality relaxation, Cesàro saturation of the sharp one-horizon constant occurs exactly when every bounded family of squarefree transition ratios has density zero.** Positive-density bounded squarefree overlap therefore gives a real accumulating constant-level obstruction, while zero-density recurrence is still interpolable. The remaining RH-facing problem is to obtain a scale-dependent accumulation mechanism from the actual Farey/Möbius source before the horizon data become reconstructive.