# NB-002 — canonical semigroup copies preserve Gram geometry but lose global target mass

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + CANONICAL-INTERNAL-MATCHED-CONTROL + MULTISCALE-TARGET-BUDGET`. `NB-001` shows that complete finite generator Gram data do not determine the distance to the fixed Nyman target: one must retain the target-pairing vector. The standard Nyman semigroup makes this distinction internal to the canonical family rather than only synthetic. Every finite Nyman section has multiplicatively shifted copies, built from canonical generators at indices `m` and `mk`, with **exactly the same Gram matrix** but with every target pairing attenuated by `m^{-1/2}`. Consequently the target projection energy of the copied section is exactly divided by `m`.

More precisely, if

\[
V_N:=\operatorname{span}\{G_2,\ldots,G_N\},
\qquad
q_N:=\|P_{V_N}E\|^2=1-d_N^2,
\]

then for every positive integer `m` the canonical semigroup copy `W_{m,N}` defined below satisfies

\[
\boxed{
\operatorname{dist}(E,W_{m,N})^2
=1-\frac{q_N}{m}
=1-\frac1m+\frac{d_N^2}{m}.
}
\]

At the same time the normalized **local** target at scale `m` is approximated by `W_{m,N}` with exactly the original error `d_N`. Thus the local finite-section geometry is self-similar while its relevance to the fixed global target decays with absolute multiplicative scale. A Gram-compressible or well-conditioned high-scale block is therefore not target-equivalent to the same block near scale one.

This is a classical semigroup consequence, not a new approximation rate. It does not control `d_N` itself and does not improve the known zero-sensitive `1/log N` boundary. Its durable use is to sharpen the target-aware information boundary inside the actual Nyman generator system: absolute scale and target alignment cannot be discarded when reorganizing the family into multiscale Gram blocks.

## 1. The discrete Nyman semigroup reproduces the same finite Gram block at every multiplicative scale

Work in Bagchi's Hardy space

\[
\mathcal H=H^2(\Omega),
\qquad
\Omega=\{s:\operatorname{Re}s>1/2\},
\]

with

\[
G_k(s)=\left(k^{-s}-k^{-1}\right)\frac{\zeta(s)}s,
\qquad
E(s)=\frac1s.
\tag{1}
\]

For a positive integer `m`, define

\[
\Theta_m(s):=m^{1/2-s},
\qquad
S_mF:=\Theta_mF.
\tag{2}
\]

On the boundary `s=1/2+it`, one has `|Theta_m(s)|=1`. Hence `S_m` is an isometry of `H^2(Omega)`. This is the integer specialization of the multiplicative inner semigroup used by Bagchi.

Bagchi's exact covariance identity gives, for every `k>=1`,

\[
\boxed{
S_mG_k
=\sqrt m\left(G_{mk}-\frac1kG_m\right).
}
\tag{3}
\]

For `2<=k<=N` put

\[
D_{m,k}:=\sqrt m\left(G_{mk}-\frac1kG_m\right)=S_mG_k
\tag{4}
\]

and

\[
W_{m,N}:=\operatorname{span}\{D_{m,2},\ldots,D_{m,N}\}=S_mV_N.
\tag{5}
\]

For `m>=2`, every `D_{m,k}` is a linear combination of canonical generators whose indices lie between `m` and `mN`, so

\[
W_{m,N}\subseteq V_{mN}.
\tag{6}
\]

The isometry immediately gives

\[
\boxed{
\langle D_{m,j},D_{m,k}\rangle
=\langle G_j,G_k\rangle
\qquad(2\le j,k\le N).
}
\tag{7}
\]

Thus the entire finite Gram matrix — not merely its spectrum or condition number — is independent of `m` for these canonical semigroup copies.

## 2. The target vector remembers the multiplicative scale exactly

`NB-001` records the reproducing-kernel identity

\[
\langle F,E\rangle=F(1)
\tag{8}
\]

and the canonical target pairings

\[
b_k:=\langle G_k,E\rangle=-\frac{\log k}{k}.
\tag{9}
\]

Since

\[
\Theta_m(1)=m^{-1/2},
\]

we obtain directly from (4) and (8)

\[
\boxed{
\langle D_{m,k},E\rangle
=\frac{b_k}{\sqrt m}.
}
\tag{10}
\]

The same identity can be checked purely arithmetically:

\[
\sqrt m\left(b_{mk}-\frac{b_m}{k}\right)
=\sqrt m\left(
-\frac{\log(mk)}{mk}
+\frac{\log m}{mk}
\right)
=-\frac{\log k}{k\sqrt m}.
\tag{11}
\]

Let `G_N` be the Gram matrix of `G_2,...,G_N`, let `b_N` be their target vector, and use the Moore--Penrose formula of `NB-001`,

\[
q_N=b_N^*G_N^+b_N,
\qquad
d_N^2=1-q_N.
\tag{12}
\]

Equations (7) and (10) say that the synthesis matrix for `W_{m,N}` has the same Gram block `G_N` and target vector `b_N/sqrt(m)`. Therefore

\[
\boxed{
\|P_{W_{m,N}}E\|^2
=\frac1m b_N^*G_N^+b_N
=\frac{q_N}{m},
}
\tag{13}
\]

and hence

\[
\boxed{
\operatorname{dist}(E,W_{m,N})^2
=1-\frac{q_N}{m}
=1-\frac1m+\frac{d_N^2}{m}.
}
\tag{14}
\]

This is an internal matched control stronger than merely changing finite coordinates. The vectors in (4) stay inside the canonical Nyman source family, the complete Gram data stay fixed, and only their absolute multiplicative position changes. As `m` tends to infinity, the target distance tends to one even though the local Gram problem is unchanged byte-for-byte at the level of inner products.

For an individual coefficient vector `c`, the same statement is visible before optimization. If

\[
F_c=\sum_{k=2}^Nc_kG_k,
\qquad
F_{m,c}=S_mF_c=\sum_{k=2}^Nc_kD_{m,k},
\]

then

\[
\|F_{m,c}\|=\|F_c\|,
\qquad
\langle F_{m,c},E\rangle
=\frac1{\sqrt m}\langle F_c,E\rangle.
\tag{15}
\]

Thus every Gram-normalized direction has canonical copies with the same self-geometry and arbitrarily small global target correlation.

## 3. The distance formula is a Pythagorean split between scale exclusion and intrinsic Nyman error

The scaling law has a geometric form that separates the two losses exactly. Let

\[
\mathcal R_m:=S_m\mathcal H.
\tag{16}
\]

For every `F in H`,

\[
\langle F,S_m^*E\rangle
=\langle S_mF,E\rangle
=(S_mF)(1)
=\frac1{\sqrt m}F(1),
\]

so

\[
\boxed{S_m^*E=\frac1{\sqrt m}E.}
\tag{17}
\]

Because `S_m` is an isometry, the orthogonal projection onto its closed range is `P_(R_m)=S_mS_m^*`. Hence

\[
P_{\mathcal R_m}E
=\frac1{\sqrt m}S_mE,
\qquad
\boxed{\|P_{\mathcal R_m}E\|^2=\frac1m.}
\tag{18}
\]

Since `W_{m,N}=S_mV_N subseteq R_m`, projection first onto `R_m` and then onto `W_{m,N}` gives

\[
P_{W_{m,N}}E
=\frac1{\sqrt m}S_mP_{V_N}E.
\tag{19}
\]

The two residual pieces are orthogonal, so

\[
\begin{aligned}
\operatorname{dist}(E,W_{m,N})^2
&=\|E-P_{\mathcal R_m}E\|^2
 +\|P_{\mathcal R_m}E-P_{W_{m,N}}E\|^2\\
&=\boxed{
\left(1-\frac1m\right)
+\frac{d_N^2}{m}.}
\end{aligned}
\tag{20}
\]

The first term is an unavoidable **scale-exclusion tax**: even the whole shifted Hardy range can see only `1/m` of the fixed target energy. The second is the original finite Nyman approximation error, rescaled by the amount of target energy present inside that range.

Equivalently, define the normalized local target

\[
E_m:=S_mE,
\qquad \|E_m\|=1.
\tag{21}
\]

Then

\[
\boxed{
\operatorname{dist}(E_m,W_{m,N})
=\operatorname{dist}(E,V_N)
=d_N.
}
\tag{22}
\]

So the finite approximation problem is exactly self-similar when the target is moved with the semigroup, while the **fixed** global target assigns only `1/m` energy to that copy. This is the target-aware distinction that a Gram-only multiscale analysis cannot see.

## 4. Real-space support gives an independent check and an exact shell budget

Under Bagchi's Mellin isometry from `L^2((0,1])`, the operator `S_m` corresponds to

\[
(T_mf)(x)
=\begin{cases}
\sqrt m\,f(mx),&0<x\le1/m,\\
0,&1/m<x\le1.
\end{cases}
\tag{23}
\]

Its range is exactly the subspace of functions supported on `(0,1/m]`. The Hardy target `E` corresponds to the constant function `1`, while `E_m=S_mE` corresponds to the normalized indicator

\[
\sqrt m\,\mathbf 1_{(0,1/m]}.
\tag{24}
\]

Therefore (18) is also the elementary support identity

\[
\|\mathbf 1_{(0,1/m]}\|_2^2=\frac1m.
\tag{25}
\]

This real-space picture checks that the `m^{-1}` factor is not a normalization accident of the Hardy model.

It also gives a canonical shell budget. If `r>=2`, then

\[
\mathcal R_{mr}\subset\mathcal R_m,
\]

and the amount of global target energy in the orthogonal shell is

\[
\boxed{
\|P_{\mathcal R_m\ominus\mathcal R_{mr}}E\|^2
=\frac1m-\frac1{mr}
=\frac{r-1}{mr}.}
\tag{26}
\]

For the dyadic chain this becomes

\[
\|P_{\mathcal R_{2^j}\ominus\mathcal R_{2^{j+1}}}E\|^2
=2^{-(j+1)},
\qquad j\ge0,
\tag{27}
\]

and these shell masses sum to one. Thus the fixed target has an exact multiscale energy distribution before any arithmetic approximation is attempted.

## 5. Consequence for the target-aware finite-section frontier

The accepted local clue asks whether a source-forced datum beyond universal Gram geometry can remain quantitatively informative through growing sections. Equations (7)--(15) sharpen the negative side of that question. The standard discrete Nyman semigroup itself produces an infinite collection of physically canonical finite blocks with identical Gram geometry and target capture varying by the exact factor `1/m`.

Therefore a multiscale reorganization based on Gram spectra, block condition numbers, block compressibility, or scale-blind normalized eigenvectors cannot treat repeated blocks as equivalent evidence for approximation of the fixed target. It must retain at least one of:

- the absolute multiplicative scale through the target weights in (10);
- explicit cross-scale interactions that recover target information lost by each isolated block;
- a target-relative dual/primal certificate whose norm is evaluated after the multiscale assembly.

This does **not** say that high-index generators are useless. The raw section `V_{mN}` contains many interactions outside the single semigroup copy `W_{m,N}`, and those interactions can combine information across scales. Nor does (14) upper-bound the target capture of `V_{mN}`. The result instead rules out a specific false inference: copying a favorable local Gram block to high multiplicative scale does not copy its usefulness for the fixed target.

A positive continuation must therefore explain how cross-scale assembly beats the scale-local target budget rather than only improving within-block Gram conditioning. The still-open scalar remains

\[
q_N=b_N^*G_N^+b_N=1-d_N^2,
\]

or an equivalent target-aware dual residual. `NB-002` supplies no new asymptotic estimate for it.

## 6. Prior art and evidence boundary

The load-bearing external input is already anchored in `research/nyman_beurling/SOURCES.md`: Bhaskar Bagchi, *On Nyman, Beurling and Baez-Duarte's Hilbert space reformulation of the Riemann hypothesis*, Proc. Indian Acad. Sci. Math. Sci. 116 (2006), 137--146; arXiv:math/0607733. Bagchi explicitly proves the multiplicative semigroup isometries and the covariance identities

\[
M_\mu(F_\lambda)=\mu^{-1/2}(F_{\lambda\mu}-\lambda F_\mu)
\]

in Hardy space and, equivalently,

\[
T_m(g_l)=m^{1/2}(g_{lm}-g_m/l)
\]

in the discrete real-space model. The projection formula and target-vector bookkeeping used here are the finite Hilbert-space identities already canonicalized in `NB-001`.

A targeted literature check also found modern work on Nyman--Beurling Gram structure and multiscale block-compressibility, including Werner Ehm, *On certain Gram matrices and their associated series* (arXiv:2405.06349), and Hugh Carvill, *Beurling Nyman Geometry and Gram Matrix Structure, Ladder Density and Polynomial Decay via Mellin Smoothing* (arXiv:2510.18132). These reinforce that multiscale Gram structure is an active object, but they are not load-bearing for (3)--(27). The search did not identify the exact finite target-mass scaling law above as a named theorem; that absence is **not** a novelty claim, since the law follows directly from Bagchi's classical semigroup together with standard projection geometry.

The result is unconditional and finite-dimensional. It neither assumes nor proves RH. It does not establish decay of `d_N`, a new zero-free region, or a stronger Nyman--Beurling criterion. Its exact contribution is an internal source-generated matched control: local Gram geometry is multiplicatively self-similar, while fixed-target energy is not.