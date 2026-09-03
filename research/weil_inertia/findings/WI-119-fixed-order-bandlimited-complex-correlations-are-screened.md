# WI-119 — fixed-order bandlimited complex correlations are screened below the Rudnick--Sarnak boundary

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + CLASSICAL-IDENTITY + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY + PRIOR-ART-REDIRECT`. This finding does **not** improve Mathia's unconditional simple-critical zero proportion. It closes a live higher-correlation escape in `CLUE-higher-zero-correlations-horizontal-rigidity`: after the natural Paley--Wiener complexification that would make a vertical `k`-level test sensitive to horizontal zero displacement, every fixed-order test whose informative Fourier support remains in the currently proved Rudnick--Sarnak region is still asymptotically blind to the WI-005/WI-006 mirror-pair-versus-double screening replacement. The obstruction persists for the standard **distinct-index** correlation sum and for every fixed `k`.

The mechanism is the exact higher-dimensional analogue of WI-007 and WI-115. In the usual unit-density ordinate normalization, the WI critical screening sites lie at the integer lattice. On the translation-invariant frequency hyperplane, the known zeta `k`-level support is

\[
\sum_{r=1}^k |\xi_r|<2,
\qquad
\sum_{r=1}^k\xi_r=0.
\]

After anchoring one coordinate this becomes

\[
\Omega_k
:=\left\{u\in\mathbb R^{k-1}:
\left|\sum_{r=2}^k u_r\right|+
\sum_{r=2}^k|u_r|<2\right\}.
\]

But every nonzero integer `m in Z^(k-1)` has

\[
\left|\sum_{r=2}^k m_r\right|+
\sum_{r=2}^k|m_r|\ge2.
\]

Thus Poisson summation sees only the zero alias throughout the proved support region. At the zero alias every horizontal phase equals one, so a symmetric off-line pair and an on-line double contribute identically. Inclusion--exclusion over coincidence partitions preserves the same support inequality, hence removing repeated indices does not restore a signal. For Schwartz tests the difference on an `M`-site block is actually `O(1)`, not merely `o(M)`.

The consequence is narrower than a no-go for all higher correlations. The classical Montgomery--Hejhal--Rudnick--Sarnak theorems are RH/GRH-conditional and concern ordinates only; they do not themselves define an unconditional horizontal observable. This finding says that **even the most direct Paley--Wiener analytic continuation of that established finite-`k` test class does not defeat the exact WI screening extremizer at density scale**. A successful higher-order horizontal route must therefore import information outside this interface: Fourier support genuinely beyond the `l1=2` boundary, a non-smooth/singular boundary observable with separately justified arithmetic control, a signed weighted statistic not reducible to the standard bandlimited class, or new zeta-specific mixed information.

## 1. The exact literature support region and why it is the relevant comparison

The primary higher-level sources are Dennis Hejhal, **On the triple correlation of zeros of the zeta function**, *International Mathematics Research Notices* 1994:7 (1994), 293--302, DOI `10.1155/S1073792894000334`, and Zeév Rudnick and Peter Sarnak, **Zeros of principal L-functions and random matrix theory**, *Duke Mathematical Journal* 81:2 (1996), 269--322, DOI `10.1215/S0012-7094-96-08115-6`. For zeta, Rudnick--Sarnak's nontrivial Fourier-support restriction is

\[
\boxed{\sum_{r=1}^k|\xi_r|<2.}
\tag{1}
\]

Their theorem assumes RH (and the general `GL_m` version assumes the corresponding GRH), counts zeros with multiplicity, and obtains the `k`-level GUE correlation for admissible symmetric translation-invariant tests. The `k=2` case goes back to Montgomery, `k=3` to Hejhal, and higher `k` to Rudnick--Sarnak.

A convenient modern theorem-level restatement is Felipe Gonçalves, David de Laat and Nando Leijenhorst, **Multiplicity of nontrivial zeros of primitive L-functions via higher-level correlations**, *Mathematics of Computation* 94 (2025), 2041--2058, DOI `10.1090/mcom/4005`, arXiv:2303.01095. Their introduction states the Rudnick--Sarnak sum over **distinct zero indices**, with zeros enumerated according to multiplicity, and for `GL_m` assumes

\[
\overline{\operatorname{supp}}\widehat f
\subset
\left\{\xi:\sum |\xi_r|<\frac2m\right\}.
\tag{2}
\]

For zeta `m=1`, this is (1). They then explicitly pass to the `(k-1)`-dimensional Paley--Wiener formulation used for multiplicity bounds. Their paper is useful here because it makes both the distinct-index convention and the complex evaluation structure of the Paley--Wiener space explicit.

Jeffrey Lagarias and Brad Rodgers, **Higher Correlations and the Alternative Hypothesis**, *Quarterly Journal of Mathematics* 71 (2020), 257--280, DOI `10.1093/qmathj/haz043`, give the strongest prior-art warning against overinterpreting (1). They construct a randomly translated half-lattice point process, and hence a deterministic sequence, whose fixed-order correlations agree with all currently known bandlimited zeta correlations while its spacings remain half-integral. Their proof itself uses Poisson summation and sampling at the critical bandlimit. That result concerns **vertical positions only** and does not model the WI off-line mirror-pair/double ambiguity. The new derived statement below is the corresponding horizontal-complexified screening calculation for that ambiguity; no novelty is claimed for Poisson summation, Paley--Wiener continuation, or the classical support geometry.

## 2. Translation averaging reduces the known test class to one explicit cross-polytope

Let `eta in S(R^k)` be a bandlimited test from the standard correlation theorem. The only arithmetically informative part after averaging the common translation lies on

\[
\xi_1+\cdots+\xi_k=0.
\tag{3}
\]

Equivalently define the relative kernel

\[
g(x_2,\ldots,x_k)
:=\int_{\mathbb R}
\eta(t,t+x_2,\ldots,t+x_k)\,dt.
\tag{4}
\]

With the Fourier convention `e^{2 pi i x.u}`,

\[
\widehat g(u_2,\ldots,u_k)
=
\widehat\eta\!\left(
-\sum_{r=2}^k u_r,
 u_2,\ldots,u_k
\right).
\tag{5}
\]

Therefore (1) gives

\[
\boxed{
\operatorname{supp}\widehat g
\Subset
\Omega_k
:=
\left\{u:
q(u):=
\left|\sum_{r=2}^k u_r\right|
+
\sum_{r=2}^k|u_r|<2
\right\}.
}
\tag{6}
\]

Because `g` is Schwartz and `hat g` is compactly supported, its Paley--Wiener continuation

\[
g(z)=\int_{\Omega_k}\widehat g(u)e^{2\pi i z\cdot u}\,du
\tag{7}
\]

is entire. For every bounded imaginary strip it remains rapidly decreasing in the real directions: for every `N` and every fixed `A`,

\[
|g(x+iy)|\le C_{N,A}(1+|x|)^{-N}
\qquad(|y|\le A).
\tag{8}
\]

This is exactly the regularity needed to ask whether the natural complexified correlation can see horizontal displacement of zeros.

## 3. The screened mirror pair and the on-line double

Use the usual unit-density local ordinate normalization

\[
x=\gamma\frac{\log T}{2\pi}.
\tag{9}
\]

The WI-005/WI-006 critical vertical spacing `2 pi/log T` is therefore the integer lattice. For a fixed normalized horizontal depth `a>=0`, attach two labelled points to every lattice site,

\[
z^{(a)}_{j,\sigma}=j-i\sigma a,
\qquad
j\in\mathbb Z,
\quad
\sigma\in\{+1,-1\}.
\tag{10}
\]

In zeta variables, `a=(beta-1/2) log T/(2 pi)` up to the sign label. For `a>0`, (10) represents a same-height functional-equation mirror pair. For `a=0`, the two labels coincide and represent an on-line double zero. The labels are retained because the zero-correlation literature enumerates zeros according to multiplicity and then imposes distinctness of **indices**, not distinctness of coordinates.

For the moment allow repeated labels. Anchoring the first site, the infinite-volume `k`-tuple density associated with (7) is

\[
A_k(a)
:=
\sum_{\sigma_1,\ldots,\sigma_k\in\{\pm1\}}
\sum_{n\in\mathbb Z^{k-1}}
 g\!\left(
 n_2-i a(\sigma_2-\sigma_1),\ldots,
 n_k-i a(\sigma_k-\sigma_1)
 \right).
\tag{11}
\]

Absolute convergence follows from (8).

## 4. Poisson summation leaves only the zero alias for every fixed `k`

For any integer vector `m=(m_2,...,m_k) != 0`,

\[
q(m)
=
\left|\sum_{r=2}^k m_r\right|
+
\sum_{r=2}^k|m_r|
\tag{12}
\]

is a positive even integer. Indeed modulo two,

\[
\left|\sum m_r\right|
\equiv\sum m_r
\equiv\sum |m_r|\pmod2,
\]

so `q(m)` is even; positivity then gives

\[
\boxed{q(m)\ge2.}
\tag{13}
\]

Applying Poisson summation to the inner sum in (11) gives

\[
\sum_{n\in\mathbb Z^{k-1}}
 g(n-i b)
=
\sum_{m\in\mathbb Z^{k-1}}
 \widehat g(m)\,e^{\pm2\pi m\cdot b},
\tag{14}
\]

where the harmless sign depends on the Fourier convention. By (6) and (13),

\[
\widehat g(m)=0
\qquad(m\ne0).
\tag{15}
\]

At `m=0` the imaginary-shift factor is exactly one. Hence every sign vector in (11) contributes the same `hat g(0)`, independently of `a`, and

\[
\boxed{
A_k(a)=2^k\widehat g(0)=A_k(0)
\qquad\text{for every fixed }k\ge2
\text{ and every fixed }a\ge0.
}
\tag{16}
\]

This is the higher-order screening identity. Horizontal depth has nowhere to enter until a nonzero integer alias is available.

There is also a useful endpoint refinement. If the standard smooth Fourier profile is merely assumed supported in the **closed** region `q(u)<=2`, continuity forces `hat g` to vanish at every boundary point `q=2`, because it vanishes on the open exterior. Thus (16) still holds for ordinary `C_c^infty` test profiles at the closed endpoint. A genuine alias requires support crossing `q=2`, or a non-smooth/singular spectral object with boundary mass whose arithmetic evaluation would need a separate theorem.

## 5. Distinct zero indices do not break the screening identity

The standard `k`-level correlation excludes repeated zero **indices**, so (16) alone is not enough. The distinct-index sum is obtained from the unrestricted sum by Möbius inversion on the lattice of set partitions:

\[
\mathbf 1_{i_1,\ldots,i_k\ \mathrm{distinct}}
=
\sum_{\pi\in\Pi_k}
\mu(\pi)
\mathbf 1_{\text{indices equal within each block of }\pi},
\tag{17}
\]

with

\[
\mu(\pi)=
\prod_{B\in\pi}
(-1)^{|B|-1}(|B|-1)!.
\tag{18}
\]

Fix a partition `pi` with blocks `B`. Collapsing all variables in a block replaces the original full Fourier frequencies `xi_r` by block frequencies

\[
\theta_B:=\sum_{r\in B}\xi_r.
\tag{19}
\]

They still satisfy

\[
\sum_B\theta_B=0,
\qquad
\sum_B|\theta_B|
\le
\sum_{r=1}^k|\xi_r|<2.
\tag{20}
\]

Thus every collapsed test inherits the **same** no-nonzero-integer-alias support property. At its zero alias, each independent labelled site still offers exactly two choices in both models: the two mirror labels for `a>0`, or the two multiplicity labels of the double for `a=0`. Consequently every partition term in (17) has the same infinite-volume density for the mirror-pair and double configurations. Summing the finitely many partition terms gives

\[
\boxed{
A_k^{\mathrm{dist}}(a)=A_k^{\mathrm{dist}}(0).
}
\tag{21}
\]

This is the step needed to match the actual Montgomery--Hejhal--Rudnick--Sarnak convention. It also shows why merely appealing to multiplicity-sensitive higher correlations does not evade the alias obstruction: coincidence subtraction contracts the Fourier `l1` support instead of enlarging it.

## 6. Long finite screening blocks differ only by `O(1)`

Let the sites be `j=0,...,M-1`. For a fixed relative offset vector `n=(n_2,...,n_k)`, the number of allowed anchor positions is

\[
\left(M-R(n)\right)_+,
\qquad
R(n):=
\max(0,n_2,\ldots,n_k)
-
\min(0,n_2,\ldots,n_k).
\tag{22}
\]

By the rapid decay (8), uniformly over the finitely many horizontal sign shifts,

\[
\sum_{n\in\mathbb Z^{k-1}}
R(n)\,|g(n-i b)|<\infty.
\tag{23}
\]

Therefore the unrestricted finite-block sum equals

\[
M A_k(a)+O_{k,a,g}(1).
\tag{24}
\]

The same estimate applies to every collapsed partition test used in (17). Combining (21)--(24), the standard distinct-index complexified statistic obeys

\[
\boxed{
C^{\mathrm{dist}}_{M,k}(a)
-C^{\mathrm{dist}}_{M,k}(0)
=O_{k,a,g}(1),
}
\tag{25}
\]

and hence

\[
\boxed{
\frac{C^{\mathrm{dist}}_{M,k}(a)
-C^{\mathrm{dist}}_{M,k}(0)}{M}
\longrightarrow0.
}
\tag{26}
\]

The finite-block statement is stronger than the `O(log M)` pair estimate in WI-115 because the classical higher-correlation test functions are Schwartz in the relative directions. It is exactly the density-scale obstruction relevant to a proportion theorem.

## 7. Relation to Lagarias--Rodgers and to the WI screening chain

Lagarias--Rodgers prove a stronger **vertical-statistics compatibility** statement than is needed for a generic anti-lattice warning: there is a half-lattice-supported point process whose correlations agree with the sine process against the whole currently known bandlimited test class. Their construction is simple and therefore does not encode the WI ambiguity between a same-height off-line mirror pair and a multiple on-line zero.

WI-005--WI-007 instead construct that horizontal ambiguity for compressed Weil forms. WI-115 shows it again for a complex pair kernel, and WI-117--WI-118 show that universal support-one termwise positivity forces the endpoint taper that screens the pair observable.

The present calculation connects these two themes at **arbitrary fixed correlation order**. It does not import the Lagarias--Rodgers point process as a zeta countermodel. It uses only the same classical sampling geometry to show that, once the WI mirror-pair/double replacement is inserted at the integer critical lattice, the natural complexified Paley--Wiener test has no available nonzero dual-lattice frequency anywhere in the established `l1<2` region. Distinct-index corrections remain inside that region by (20).

Thus increasing `k` does not lower the support threshold. The first possible integer aliases always sit on

\[
\boxed{\sum |\xi_r|=2.}
\tag{27}
\]

For `k=2`, writing `xi=(u,-u)`, equation (27) is `|u|=1`, exactly the support-one boundary in WI-007 and WI-115--WI-118.

## 8. What this closes, and what remains live

This finding decisively closes the route

\[
\boxed{
\text{take the known fixed-}k\text{ bandlimited correlations}
\;\longrightarrow\;
\text{Paley--Wiener complexify them horizontally}
\;\longrightarrow\;
\text{break WI screening at density scale}
}
\tag{28}
\]

without new support or new arithmetic input. The support geometry itself prevents that implication.

It does **not** claim that higher correlations are useless, nor that actual zeta zeros realize the screening lattice. It also does not turn the RH-conditional Rudnick--Sarnak theorem into an unconditional horizontal theorem. The screening configuration is a deterministic falsifier for the information carrier: any proposed universal defect inequality depending only on finitely many such complexified bandlimited correlation functionals must also hold on a configuration where those functionals have the same density-scale value for off-line mirror pairs and on-line doubles.

The live exits from `CLUE-higher-zero-correlations-horizontal-rigidity` are consequently narrower and genuinely arithmetic:

- obtain an unconditional statistic whose effective Fourier support crosses the `l1=2` threshold, which for pairs is the support-`>1` prime-pair barrier already isolated by WI-007;
- control a signed or singular boundary contribution that is not in the smooth Paley--Wiener class;
- estimate the actual BGSTB bad-pair reservoir by cancellation rather than termwise positivity/zero counts; or
- find mixed arithmetic-horizontal information whose Fourier carrier is not exhausted by the standard finite-`k` ordinate-correlation theorem.

Merely increasing the correlation order while remaining inside the established bandlimit is no longer a live anti-screening mechanism.

## 9. Prior-art and novelty audit

No novelty is claimed for the Montgomery, Hejhal or Rudnick--Sarnak correlation theorems, their support restriction, Paley--Wiener analytic continuation, Poisson summation, Möbius inversion on set partitions, or the Lagarias--Rodgers Alternative-Hypothesis construction. Gonçalves--de Laat--Leijenhorst are direct prior art for using the same higher-level correlations and Paley--Wiener spaces to control zero multiplicity under GRH.

A targeted search found no source formulating the specific **horizontal mirror-pair-versus-double** identity (16)/(21) or its distinct-index partition stability. Absence of a located source is not evidence of priority. The durable Mathia contribution is the exact interface theorem joining the established `l1<2` higher-correlation support to the already-persisted WI screening extremizer, together with the finite-block `O(1)` consequence and the sharp identification of the first possible nonzero alias at `l1=2`.

### Decisive falsification boundary

This finding does not obstruct a proposed higher-order route if its horizontal observable has justified Fourier mass beyond `sum |xi_r|=2`, if it uses a non-smooth boundary distribution whose arithmetic evaluation is separately proved, if it controls zeta-specific signed terms not represented by the Paley--Wiener statistic above, or if it exploits information not reducible to any fixed-order correlation functional in this class. Within the stated fixed-`k`, smooth bandlimited complexification, however, equations (13)--(26) give an exact density-scale screening obstruction.