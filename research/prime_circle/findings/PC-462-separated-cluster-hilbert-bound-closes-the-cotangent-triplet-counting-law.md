# PC-462 — A separated-cluster Hilbert bound closes the cotangent triplet counting law

**Status:** LITERATURE+DERIVED + EXACT-DERIVED + CLASSICAL-SIEVE-BOUNDARY. The full conductor-scaled primorial cotangent matrix has an exact triplet-scale counting law at every fixed threshold above the largest pair atom, except at the explicitly identified triplet atoms. A deterministic operator-norm estimate for interactions between separated clusters supplies the missing upper bound in PC-461. The coefficients are classical triplet singular series. No prime-tuple conjecture, individual-eigenvector localization, historical priority, or zeta-zero implication is asserted.

## 1. Full operator and counting theorem

Let
\[
d_y=\prod_{p\le y}p,\qquad N=d_y m,\qquad m\ge1,
\qquad Y=\{a\bmod N:(a,d_y)=1\}.
\]
On the coordinate space of `Y`, keep the full Hermitian matrices
\[
T_{ab}=\begin{cases}
\dfrac{i}{N}\cot\dfrac{\pi(a-b)}N,&a\ne b,\\
0,&a=b,
\end{cases}
\qquad T^+=T+J_{|Y|}/N,
\tag{1}
\]
including the diagonal of the augmentation. Write
`n_+(A,t)=#{lambda(A)>t}` and `n_-(A,t)=#{lambda(A)<-t}`,
with multiplicity. Put
\[
\lambda_2=\frac1{2\pi},\qquad
\mathcal B=\{b\ge4:b\equiv0\text{ or }4\pmod6\},
\]
\[
\lambda_b=\frac1{2\pi}+\frac2{\pi b(b+2)},\qquad
\mathfrak S_b=\frac92\prod_{p\ge5}\frac{p^2(p-3)}{(p-1)^3}
\prod_{\substack{p\ge5\\p\mid b(b+2)}}\frac{p-2}{p-3}.
\tag{2}
\]
Here `lambda_b` and `mathfrak S_b` are indexed by `b in mathcal B`. The second product is finite; the first converges absolutely to a positive number. For every fixed
\[
t>\lambda_2,\qquad t\notin\{\lambda_b:b\in\mathcal B\},
\]
either sign and either matrix convention satisfy
\[
\boxed{\quad
\lim_{y\to\infty}\ \sup_{m\ge1}
\left|
\frac{(\log y)^3}{d_y m}\,n_\pm(T^{(+)},t)
-2e^{-3\gamma}\sum_{\substack{b\in\mathcal B\\\lambda_b>t}}
\mathfrak S_b
\right|=0.
\quad}
\tag{3}
\]
The sum is finite because `lambda_b` decreases to `lambda_2`. The factor two counts the distinct ordered-gap shapes `{0,2,b+2}` and `{0,b,b+2}`; each contributes one eigenvalue of each sign, so signs supply no additional factor.

In particular, if
\[
\frac{13}{24\pi}<t<\frac7{12\pi},
\]
only `b=4` contributes. Thus PC-461's coefficient is exact on this interval:
\[
n_\pm(T^{(+)},t)\sim
2e^{-3\gamma}\mathfrak S_4\frac{N}{(\log y)^3}
\tag{4}
\]
uniformly in refinement. Below `13/(24 pi)`, further admissible triplets contribute. For each fixed `t>7/(12 pi)` the proof also gives
\[
n_\pm(T^{(+)},t)=O_t\!\left(\frac{N}{(\log y)^4}\right).
\tag{5}
\]
This is a population bound, not a spectral edge or a fourth-order asymptotic.

## 2. The deterministic interaction lemma

For real points on a circle of circumference `N`, use circular distance
\[
\delta_N(x,z)=\min_{k\in\mathbb Z}|x-z+kN|.
\]
Suppose a finite support is partitioned into nonempty clusters `C_j`, each of size `r_j<=r`, and points in distinct clusters have distance at least `H>0`. Let `K` be the full kernel (1) on this support, let `D` retain all within-cluster entries, and put `E=K-D`. Then
\[
\boxed{\qquad \|E\|\le\frac rH.\qquad}
\tag{6}
\]
There is no lower bound on distances inside a cluster and no arithmetic assumption.

The classical Montgomery--Vaughan cotangent inequality, Corollary 1, equation (1.4), states that distinct points `x_j mod 1` of minimum circular separation `delta` satisfy
\[
\left|\sum_{j\ne k}u_j\overline{u_k}
\cot\pi(x_j-x_k)\right|
\le\delta^{-1}\sum_j|u_j|^2.
\tag{7}
\]
After dividing by `N`, the Hermitian kernel on any `H`-separated circle support therefore has norm at most `1/H`. This uses the uniform-separation inequality, not a conjectural sharp constant for variable nearest-neighbor weights.

To pass from points to clusters, choose `X_j` independently and uniformly from `C_j`. For a fixed vector `v` on the whole support set
\[
u_j=r_jv_{X_j}.
\]
The selected support is `H`-separated. Independence and the absence of a selected within-cluster pair give the exact finite averaging identity
\[
\mathbb E\left[\sum_{j\ne k}\overline{u_j}
K(X_j,X_k)u_k\right]
=\langle v,Ev\rangle.
\tag{8}
\]
The sum inside the expectation is a Hermitian quadratic form. Hence (7) gives
\[
|\langle v,Ev\rangle|
\le H^{-1}\mathbb E\sum_j|u_j|^2
=H^{-1}\sum_jr_j\sum_{a\in C_j}|v_a|^2
\le(r/H)\|v\|^2.
\tag{9}
\]
Taking the supremum proves (6). Random selection is only a proof of a deterministic finite averaging identity; no probabilistic model of the retained residues is introduced.

This estimate controls the entire off-block cotangent interaction, retaining its cancellation. Summing absolute `1/h` entries would lose that cancellation. It is stronger in this setting than PC-460's Hilbert--Schmidt tail estimate, which alone does not vanish at the triplet count scale for a fixed cutoff.

## 3. Four-point configurations contain every large short-edge component

Fix an integer `H>=2` before taking `y->infinity`. Join two points of `Y` when their circular distance is at most `H`. Delete every vertex in a connected component containing at least four vertices. Call the number deleted `R_(y,H)` and the remaining principal matrix `B_H`.

For every fixed integer offset set `F`, CRT gives
\[
A_y(F):=\#\{a\bmod N:a+F\subset Y\}
=N\prod_{p\le y}\left(1-\frac{\nu_p(F)}p\right),
\quad \nu_p(F)=|F\bmod p|.
\tag{10}
\]
For an admissible pattern of `k` distinct offsets, Mertens's product theorem yields
\[
A_y(F)\sim\frac{Ne^{-k\gamma}\mathfrak S(F)}{(\log y)^k},
\qquad
\mathfrak S(F)=\prod_p\frac{1-\nu_p(F)/p}{(1-1/p)^k}.
\tag{11}
\]
Outside finitely many primes `nu_p(F)=k`, so the normalized factors are `1+O_F(p^-2)`. An inadmissible pattern is eventually absent. The factor `m` in (10) is exact for every refinement, including refinements sharing primes with `d_y`; consequently the limits and bounds for fixed patterns are uniform in `m`.

Every deleted vertex belongs to a connected four-vertex subset: start from that vertex and successively add an adjacent vertex until there are four. Each lies at graph distance at most three from the starting vertex, hence at circular distance at most `3H`. For `N>6H`, lift these vertices to distinct offsets in `[-3H,3H]`, one of which is zero. There are only finitely many such four-point patterns at fixed `H`. Applying (10)--(11) and a union bound gives
\[
R_{y,H}=O_H\!\left(\frac{N}{(\log y)^4}\right).
\tag{12}
\]
This counts all vertices in large components, even when the component itself is long. No bound on its diameter or cardinality is assumed.

The surviving components have sizes one, two or three, with every two different components at distance greater than `H`. Let `D_H` keep their complete principal blocks, including all entries inside a three-point block. Applying (6) gives
\[
\|B_H-D_H\|\le3/H.
\tag{13}
\]
By norm perturbation and principal-submatrix interlacing, for either sign,
\[
n_\pm(D_H,t+3/H)
\le n_\pm(T,t)
\le n_\pm(D_H,t-3/H)+R_{y,H}.
\tag{14}
\]
Thus the full-matrix upper bound costs only the four-point population and a deterministic threshold shift. It does not require operator-norm smallness of an unrestricted long-distance tail on all of `Y`.

## 4. Exactly which triplets cross the pair threshold?

For `N>4H`, a surviving three-point component has a unique cyclic starting point after its long empty arc. It has successive positive gaps `a,b<=H` and offsets `{0,a,a+b}`. Its three eigenvalues are `0,+lambda_N(a,b),-lambda_N(a,b)`, with
\[
\lambda_N(a,b)^2=
\left(\frac1N\cot\frac{\pi a}N\right)^2
+\left(\frac1N\cot\frac{\pi b}N\right)^2
+\left(\frac1N\cot\frac{\pi(a+b)}N\right)^2
\longrightarrow
\lambda(a,b)^2:=\frac1{\pi^2}
\left(\frac1{a^2}+\frac1{b^2}+\frac1{(a+b)^2}\right).
\tag{15}
\]
For fixed `H` convergence is uniform in `m`, and `lambda_N(a,b)<=lambda(a,b)`. A two-point block has magnitude at most `1/(pi h)<=lambda_2`, since retained differences are even once `y>=2`.

Admissible triples also have even `a,b`. If both are at least four, then
\[
\pi\lambda(a,b)\le\sqrt{\frac1{16}+\frac1{16}+\frac1{64}}
=\frac38<\frac12.
\tag{16}
\]
Hence a triplet above `lambda_2` must have one gap equal to two. The case `(2,2)` is obstructed modulo three. For `(2,b)`, all larger primes automatically leave an unused residue class, and the remaining conditions are exactly
\[
b\in\mathcal B.
\]
For these gaps an exact square identity gives
\[
\frac1{\pi}\sqrt{\frac14+\frac1{b^2}+\frac1{(b+2)^2}}
=\frac{b^2+2b+4}{2\pi b(b+2)}=\lambda_b.
\tag{17}
\]
Reflection gives the second ordered-gap shape `(b,2)`, which is distinct because `b>=4`.

For `F_b={0,2,b+2}`, the normalized local factors are `4` at two and `9/8` at three. At `p>=5` there are three distinct residues unless `p|b(b+2)`, when there are two. This proves
\[
\mathfrak S(F_b)=\mathfrak S_b,
\tag{18}
\]
and reflection leaves these factors unchanged.

For any fixed connected three-point pattern, a copy fails to be an entire three-point component only if there is an additional retained point within distance `H` of one of its vertices. These extra points have offsets in a fixed finite interval, and each imposes a distinct four-point union. Equations (10)--(12) show that the number of failed copies is `O_H(N/(log y)^4)`. Consequently each of the two shapes with `b<=H` occurs as a full component
\[
\frac{Ne^{-3\gamma}\mathfrak S_b}{(\log y)^3}
+o_H\!\left(\frac{N}{(\log y)^3}\right)
\tag{19}
\]
times, uniformly in `m`. Components crossing the coordinate cut are included by the cyclic starting-point convention; there is no division by three.

## 5. Closing the fixed-threshold limit

Fix a threshold in (3). The sequence `lambda_b` has its only accumulation point at `lambda_2`. Choose `delta>0` so that `t-delta>lambda_2` and `[t-delta,t+delta]` contains no triplet atom. Then choose one fixed `H` large enough that

- `3/H<delta`;
- every `b` with `lambda_b>t-delta` satisfies `b<=H`.

At both thresholds `t-3/H` and `t+3/H`, the singleton and pair blocks contribute nothing, and (15)--(19) give exactly the finite coefficient on the right of (3). Equation (12) is negligible after multiplication by `(log y)^3/N`. The two sides of (14) therefore squeeze to the same limit. All pattern sets and the cutoff are fixed before `y` varies, so no growing-window sieve estimate or exchange of uncontrolled limits is used.

For `t>lambda_4=7/(12 pi)`, choose fixed `H` with `3/H<t-lambda_4`. Every block of `D_H` is then below `t-3/H`, including at finite `N>4H`. Equations (12)--(14) prove (5) for `T`.

Finally, `T^+-T` has rank one, so either signed threshold count changes by at most one. Both `(log y)^3/N` and `(log y)^4/N` tend to zero uniformly in refinement, proving the augmented assertions. Conjugation sends the raw `T` to `-T`, but exact finite sign symmetry is not needed or asserted for `T^+`.

## 6. Consequences, controls and limits

[[research/prime_circle/findings/PC-460-primorial-cotangent-rare-spectrum-has-a-prime-pair-counting-law]] identifies the first rare population at scale `N/(log y)^2`. [[research/prime_circle/findings/PC-461-admissible-triplets-force-cotangent-populations-above-the-pair-spectrum]] establishes only a lower bound for the smaller population above its top atom. Equation (3) now classifies that population completely at the next scale, for fixed non-atomic thresholds above the pair range. The new load-bearing step is (6), which permits deletion of all larger clusters at their actual smaller frequency while controlling the full remaining interaction in operator norm.

The mechanism is not prime-specific at the operator level. Equation (6) holds on arbitrary clustered circle supports. Any support family with the same triplet frequencies and negligible connected four-point counts gives the same readout. The arithmetic retained by (3) is explicitly the classical local-density product (18), not an additional critical-line selector. The block comparison deliberately preserves those arithmetic frequencies; it is not a second full support with arithmetic information removed.

The theorem does not settle thresholds exactly at `lambda_b`, the accumulating endpoint `lambda_2`, thresholds moving with `y`, individual eigenvalues or eigenvectors, or the complete hierarchy of smaller populations. In particular, (5) does not rule out higher constellations or individual local limits above `lambda_4`. The spectral values and coefficient measure here concern sieved residues modulo a primorial, not actual prime triples. No inference about zeros of zeta or RH follows.

## 7. Prior art and validation

H. L. Montgomery and R. C. Vaughan, *Hilbert's Inequality*, **J. London Math. Soc. (2) 8** (1974), 73--82, [author-hosted original, p. 74, Corollary 1, equation (1.4)](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf), supplies exactly (7). The cluster estimate is a finite averaging consequence derived here; no new general Hilbert inequality is claimed. Preissmann--Lévêque's [*On generalized weighted Hilbert matrices*, §2](https://msp.org/pjm/2013/265-1/pjm-v265-n1-p09-p.pdf) provides neighboring operator-theoretic context. The source constant and its circle normalization were checked against the original displayed equation, including the distinction from variable-gap weighted bounds.

J. C. Lagarias, [*Euler's constant: Euler's work and modern developments*, Theorem 3.3.2](https://arxiv.org/pdf/1303.1856), supplies Mertens's product theorem. K. S. Kedlaya, [*Notes on analytic number theory*, Definition 19.1](https://kskedlaya.org/ant/chap-k-tuples.html), records the singular-series normalization. PC-461 already locates the two shortest shapes in Hardy--Littlewood's original prime-tuple discussion. Only exact CRT counts and the classical product limit are used here; the conjectural prime-tuple asymptotic is unnecessary.

Local duplication checks covered the full pair law, the triplet lower bound and the separation-controlled normalization of PC-457. Directed literature searches covered cotangent and sieved Hilbert spectra, triplet singular-series counting laws, and Hilbert inequalities for separated clusters. These do not establish historical priority. The mathematical delta is the explicit all-radius upper bound and exact triplet-scale population law for this construction, using standard analytic and sieve ingredients.

The proof is analytic, not Lean-verified. Standard-library Python checked **10,000** even-gap classifications with gaps through `200`, **168** exact CRT triple/four-point counts at primorial cutoffs through `11` and refinements `1,2,3`, and **726** exact rational local factors. System LAPACK `zheev`, called through `ctypes`, checked **80** arbitrary nonarithmetic cluster norm bounds (including unequal sizes and wraparound), **45** exhaustive representative-averaging identities, **50** primorial cluster norm bounds, **1,400** threshold/interlacing inequalities, and **140** rank-one count comparisons. Full-matrix checks used **10** cases of dimension at most `480`; **2,646** connected four-point witnesses checked the deletion argument. The maximum averaging residual was below `6.6e-19`, the maximum three-point eigenvalue error below `1.4e-16`, and the largest ratio to the general cluster norm bound below `0.528`. These finite checks audit conventions and inequalities, not the asymptotic theorem. Scratch code and outputs remain outside Git.

The decisive audit points are the uniform circular-separation constant, the `r_j` rather than `sqrt(r_j)` sampling weight, deletion of every vertex in a large component, cyclic uniqueness of triple starts, the two distinct reflected shapes, fixed-cutoff order, and restriction to thresholds strictly separated from the accumulating pair edge and the triplet atoms.
