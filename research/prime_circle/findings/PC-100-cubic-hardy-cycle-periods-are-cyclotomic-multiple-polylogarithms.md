# PC-100 — cubic Hardy cycle periods are cyclotomic multiple polylogarithms

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the first genuinely higher cyclic Hardy trace isolated in PC-082. For three cyclically adjacent distinct primitive-shell orders greater than one, every separated root-channel trace — and hence the completed shell trace — lies exactly in the weight-three cyclotomic multiple-polylogarithm span at level dividing the least common multiple of the three shell orders and `2`. Thus the triangle-cone period of PC-082 really contains information beyond pairwise cyclotomic resultants, but at cubic order it does **not** define a new period algebra outside the classical cyclotomic multiple-polylogarithm / multiple-`L`-value world.

This resolves the specific novelty boundary left open in PC-082 and sharpened by PC-086. It does **not** prove an analogous reduction for all higher cycle lengths, repeated-shell root words that fail cyclic root separation, infinite-shell generating constructions, or global Hardy determinants with a genuinely new geometry-forced parameter.

## 1. Starting point: the PC-082 triangle cone is an ordinary trace

Let `a,b,c` be roots of unity with

\[
a,b,c\neq1,
\qquad
ab\neq1,\quad bc\neq1,\quad ca\neq1.
\]

These hypotheses hold rootwise when `a,b,c` are chosen from three cyclically adjacent distinct primitive shells of orders `n_1,n_2,n_3>1`. PC-082 and the correction PC-086 give the ordinary trace

\[
\mathcal P(a,b,c)
:=\operatorname{Tr}(\mathcal H_a\mathcal H_b\mathcal H_c)
\]

as the conditionally convergent triangle-cone sum

\[
\boxed{
\mathcal P(a,b,c)
=
\sum_{\substack{r,s,t\ge1\\
r+s>t,\ s+t>r,\ t+r>s\\
r+s+t\ \mathrm{odd}}}
\frac{a^r b^s c^t}{rst},
}
\]

where PC-086 justifies the natural rectangular finite-section limit without requiring Abel regularization. Absolute convergence still fails at the critical homogeneity, so the prior-art question in PC-082 was whether this conditional value lives outside the standard cyclotomic multiple-zeta/polylogarithm algebra.

It does not at length three.

## 2. Remove the parity constraint exactly

Define the unprojected triangle sum, with the same natural finite-section/Abel boundary value,

\[
T_\triangle(a,b,c)
=
\sum_{\substack{r,s,t\ge1\\
r+s>t,\ s+t>r,\ t+r>s}}
\frac{a^r b^s c^t}{rst}.
\]

The odd-total projector is elementary:

\[
\mathbf 1_{r+s+t\ \mathrm{odd}}
=\frac{1-(-1)^{r+s+t}}2.
\]

Hence

\[
\boxed{
\mathcal P(a,b,c)
=\frac12\Bigl(
T_\triangle(a,b,c)-T_\triangle(-a,-b,-c)
\Bigr).
}
\]

The sign twist only enlarges the cyclotomic level by at most a factor of two. It therefore suffices to classify `T_triangle`.

## 3. The triangle is the full octant minus three explicit horns

For positive integers `r,s,t`, failure of the strict triangle inequalities means exactly one of

\[
r\ge s+t,
\qquad
s\ge t+r,
\qquad
t\ge r+s.
\]

These three regions are disjoint. Since `Li_1(z)=-Log(1-z)` in the radial branch, the full positive octant factorizes as

\[
\sum_{r,s,t\ge1}\frac{a^r b^s c^t}{rst}
=\operatorname{Li}_1(a)\operatorname{Li}_1(b)\operatorname{Li}_1(c).
\]

For the horn `t>=r+s`, define

\[
C(c;a,b)
:=
\sum_{r,s\ge1}\sum_{t\ge r+s}
\frac{a^r b^s c^t}{rst}.
\]

At radial parameter `0<rho<1`, the tail identity

\[
\sum_{t\ge r+s}\frac{(\rho c)^t}{t}
=
\int_0^{\rho c}\frac{u^{r+s-1}}{1-u}\,du
\]

is absolutely justified. Summing first over `r,s` and then taking `rho -> 1^-` gives

\[
\boxed{
C(c;a,b)
=
\int_0^c
\frac{\operatorname{Li}_1(au)\operatorname{Li}_1(bu)}{u(1-u)}\,du.
}
\]

The path from `0` to `c` encounters no singularity: `c!=1`, and `ca!=1`, `cb!=1` exclude the two other possible endpoint collisions. Therefore

\[
\boxed{
T_\triangle(a,b,c)
=
\operatorname{Li}_1(a)\operatorname{Li}_1(b)\operatorname{Li}_1(c)
-C(a;b,c)-C(b;c,a)-C(c;a,b).
}
\]

This is already a finite reduction of the critical three-dimensional cone to ordinary one-dimensional iterated integrals.

## 4. Each horn is a weight-three cyclotomic hyperlogarithm

Use the standard hyperlogarithm convention

\[
G(q_1,\ldots,q_k;z)
=
\int_0^z\frac{du}{u-q_1}G(q_2,\ldots,q_k;u),
\qquad G(;z)=1.
\]

Then

\[
\operatorname{Li}_1(au)=-G(a^{-1};u).
\]

The shuffle product for two weight-one iterated integrals and

\[
\frac1{u(1-u)}=\frac1u-\frac1{u-1}
\]

give the exact identity

\[
\boxed{
\begin{aligned}
C(c;a,b)
={}&G(0,a^{-1},b^{-1};c)
   +G(0,b^{-1},a^{-1};c)\\
 &-G(1,a^{-1},b^{-1};c)
   -G(1,b^{-1},a^{-1};c).
\end{aligned}
}
\]

Scaling the endpoint to one gives

\[
G(q_1,q_2,q_3;c)
=G(q_1/c,q_2/c,q_3/c;1).
\]

Every nonzero letter on the right is a root of unity, while zero stays zero. Consequently each horn is a weight-three multiple-polylogarithm value at roots of unity. The product of the three `Li_1` values is in the same weight-three span by the shuffle relations.

If

\[
N=\operatorname{lcm}(2,n_1,n_2,n_3),
\]

then all letters occurring for roots from the three shells, including the parity-twisted roots `-a,-b,-c`, belong to `mu_N`. Therefore

\[
\boxed{
\mathcal P(a,b,c)\in \operatorname{MPV}_3(N),
}
\]

where `MPV_3(N)` denotes the `Q`-span of weight-three multiple polylogarithm values at `N`th roots of unity (equivalently, the standard cyclotomic multiple-`L`-value period space at this weight).

## 5. Completed primitive shells inherit the same classicalization

For primitive-shell Hardy operators

\[
\Gamma_n=-\sum_{\alpha\in P_n^*}\mathcal H_\alpha,
\]

let `n_1,n_2,n_3>1` be cyclically adjacent and pairwise distinct. Rootwise separation is automatic: if `alpha_i alpha_{i+1}=1`, the two roots have the same exact order, contrary to `n_i!=n_{i+1}`.

Thus every term in the finite root expansion lies in `MPV_3(N)`, and so

\[
\boxed{
\operatorname{Tr}(\Gamma_{n_1}\Gamma_{n_2}\Gamma_{n_3})
\in \operatorname{MPV}_3(N),
\qquad
N=\operatorname{lcm}(2,n_1,n_2,n_3).
}
\]

This does **not** undo the exact PC-082 control

\[
\operatorname{Tr}(\Gamma_3\Gamma_2)=0,
\qquad
\operatorname{Tr}(\Gamma_3\Gamma_2\Gamma_3)>0.
\]

Higher Hardy traces can still contain more information than pairwise resultants. The correction is about the **period class** of the first separated cubic trace, not about whether that trace is determined by pairwise shell data.

## 6. Prior-art and novelty audit

The classification lands squarely in established cyclotomic multiple-polylogarithm theory.

- A. B. Goncharov, **Multiple polylogarithms, cyclotomy and modular complexes**, *Mathematical Research Letters* 5 (1998), 497–516, DOI `10.4310/MRL.1998.v5.n4.a7`, develops multiple polylogarithms at roots of unity and their iterated-integral continuation, identifying them with the cyclotomic/multiple-Dirichlet-`L` period setting used above.
- Jianqiang Zhao, **A Note on Colored Tornheim's Double Series**, *Integers* 10 (2010), 879–882, DOI `10.1515/integ.2010.059`, gives a directly neighboring reduction of colored Mordell–Tornheim series to multiple polylogarithm values at roots of unity.
- Terasoma's rational-cone theorem and the Guo–Paycha–Zhang conical-zeta papers already recorded in `research/prime_circle/SOURCES.md` were the prior-art boundary in PC-082. Their general absolutely-convergent cone theorem did not by itself cover the critical conditional triangle sum. The finite horn decomposition above removes that gap specifically at cycle length three.

No historical novelty is claimed for hyperlogarithms, shuffle reduction, or colored Tornheim/MPL theory. The Prime-Circle-specific durable result is the exact identification of the PC-082 cubic Hardy invariant with that classical period space.

## 7. RH consequence and remaining boundary

The first genuinely higher separated Hardy trace therefore follows the chain

\[
\boxed{
\text{Prime-Circle cubic Hardy trace}
\longrightarrow
\text{triangle cone}
\longrightarrow
\text{finite horn decomposition}
\longrightarrow
\text{weight-3 cyclotomic MPVs}.
}
\]

So the fact that cubic traces escape pairwise cyclotomic resultants is **not by itself** a new bridge to the Riemann zeros. At this order there is still no geometry-forced free complex parameter, gamma factor, `s <-> 1-s` symmetry, positivity criterion, or zero divisor; the arithmetic periods are classical cyclotomic special values.

The surviving Hardy question is narrower and explicit: determine whether cycle lengths `k>=4`, repeated-shell mixed words outside rootwise separation, or an intrinsically generated infinite-shell organization force period/function classes beyond finite cyclotomic multiple-polylogarithm data. Merely pointing to the criticality of the cubic cone no longer counts as an escape.

## Falsification surface

1. Expand the PC-082 cubic trace and verify the bijection from `(i,j,k)>=0` to strict triangle triples with odd `r+s+t`; a mismatch invalidates the starting formula.
2. Under radial damping, partition the positive octant into the strict triangle plus the three disjoint horns and verify the displayed tail integral for each horn.
3. Differentiate the proposed formula for `C(c;a,b)` with respect to its endpoint; it must give `Li_1(ac)Li_1(bc)/(c(1-c))` with zero value at the origin.
4. Verify the hyperlog shuffle identity and the sign in `1/[u(1-u)]=1/u-1/(u-1)`.
5. Check that cyclic root separation excludes every endpoint singularity used in the passage `rho -> 1^-`.
6. Scale each endpoint to one and verify that every nonzero letter remains in `mu_N`, with `N=lcm(2,n_1,n_2,n_3)`.
7. This finding must **not** be generalized to arbitrary `k` without a separate linear-reducibility/iterated-integral proof; such an extrapolation would exceed the evidence here.
