# WI-080 — common-period Ramanujan projectors localize signed scalar cancellation to the finite-window boundary

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECTION`. This finding does **not** certify the Yang--Yang one-sided fourth-moment candidate and does not change Mathia's current unconditional simple-critical proportion. It sharpens the sign-sensitive scalar route left open by WI-079.

For every finite family of distinct scalar moduli `m` and real aggregated outer weights `omega_m`, let

\[
A_N=(R_\omega(i-j))_{0\le i,j<N},
\qquad
R_\omega(h)=\sum_m\omega_m c_m(h),
\]

be the signed Ramanujan Toeplitz operator isolated in WI-079. If `L` is any common multiple of all active moduli, define the full `L x L` periodic matrices

\[
C_m^{(L)}=(c_m(i-j))_{i,j\in\mathbf Z/L\mathbf Z}.
\]

Classical Ramanujan-sum orthogonality gives the exact matrix identity

\[
\boxed{
C_m^{(L)}C_n^{(L)}
=L\,\delta_{m,n}C_m^{(L)}.
}
\]

Hence

\[
P_m^{(L)}:=L^{-1}C_m^{(L)}
\]

are pairwise orthogonal projections with

\[
\operatorname{rank}P_m^{(L)}=\varphi(m).
\]

Therefore the complete-period signed operator

\[
A_L:=\sum_m\omega_m C_m^{(L)}
=L\sum_m\omega_mP_m^{(L)}
\]

has the exact spectral decomposition

\[
\boxed{
\operatorname{spec}(A_L)
=
\{L\omega_m\text{ with multiplicity }\varphi(m)\}_m
\cup\{0\}.
}
\]

In particular,

\[
\boxed{
|A_L|=\sum_m|\omega_m|C_m^{(L)},
\qquad
\|A_L\|_{\rm op}=L\max_m|\omega_m|,
}
\]

and more generally for every finite `p>=1`,

\[
\|A_L\|_{S_p}^p
=L^p\sum_m\varphi(m)|\omega_m|^p.
\]

Thus **outer signs give no norm cancellation whatsoever on a complete common period**. They only choose the signs of mutually orthogonal spectral blocks:

\[
n_+(A_L)=\sum_{\omega_m>0}\varphi(m),
\qquad
n_-(A_L)=\sum_{\omega_m<0}\varphi(m).
\]

For arbitrary source-window length `N`, choose a common multiple `L>=N`. Because every `c_m` is `m`-periodic and `m|L`, the WI-079 Toeplitz matrix is exactly a principal compression

\[
\boxed{A_N=R_NA_LR_N^*}
\]

of the complete-period signed projector sum. Consequently **all cross-modulus sign cancellation available to the finite Yang scalar operator is a time-window/compression effect**: it is created only because restriction to `N` consecutive coordinates destroys the orthogonality of the Ramanujan subspaces.

If `r=L-N`, Cauchy interlacing gives the exact inertia stability bounds

\[
\boxed{
n_+(A_N)\ge
\left(\sum_{\omega_m>0}\varphi(m)-r\right)_+,
\qquad
n_-(A_N)\ge
\left(\sum_{\omega_m<0}\varphi(m)-r\right)_+.
}
\]

Thus deleting `r` coordinates from a complete period can erase at most `r` positive and at most `r` negative Ramanujan spectral directions. If `N` itself is a common multiple of the active moduli, `r=0` and the complete-period formula applies exactly: signed scalar cancellation is impossible at the operator-norm, Schatten-norm, rank, and inertia levels. More generally, if a modulus carrying an extremal absolute weight has Ramanujan-subspace multiplicity exceeding the boundary defect, the extremal norm survives the compression unchanged.

The decisive implication for the Yang route is narrow but useful:

\[
\boxed{
\text{signed scalar gain}
\neq
\text{cross-modulus cancellation on complete residue periods};
\qquad
\text{it must be finite-window spectral leakage.}
}
\]

Hence any attempted repair of the Yang covariance by grouping signed scalar modulus blocks over complete common periods, complete residue cycles, or an argument that effectively restores those cycles before estimating the operator cannot exploit the signs. A viable scalar escape must quantify the genuinely nonperiodic time-limiting interaction between Ramanujan subspaces, or retain richer labelled/two-dimensional structure before the scalar projection.

## 1. Classical common-period convolution identity

Noboru Ushiroya proves the following Ramanujan-sum identity (Lemma 1 of *Eigenvalues of Matrices whose Elements are Ramanujan Sums or Kloosterman Sums*, Journal of Integer Sequences 21 (2018), Article 18.2.6; arXiv:1803.02970). If `m|L` and `n|L`, then

\[
\sum_{a=1}^{L}c_m(x-a)c_n(a-y)
=
\begin{cases}
L c_m(x-y),&m=n,\\
0,&m\ne n.
\end{cases}
\tag{1}
\]

In matrix notation, (1) is exactly

\[
C_m^{(L)}C_n^{(L)}
=L\delta_{m,n}C_m^{(L)}.
\tag{2}
\]

Since Ramanujan sums are real and even, every `C_m^(L)` is Hermitian. Equation (2) therefore shows that `P_m^(L)=C_m^(L)/L` is an orthogonal projection and that the projections are mutually orthogonal for distinct moduli.

The rank is classical as well. The diagonal entry is

\[
c_m(0)=\varphi(m),
\]

so

\[
\operatorname{tr}C_m^{(L)}=L\varphi(m).
\]

Because the only eigenvalues allowed by `(C_m^(L))^2=L C_m^(L)` are `0` and `L`, the multiplicity of `L` is

\[
\frac{\operatorname{tr}C_m^{(L)}}L=\varphi(m).
\tag{3}
\]

Ushiroya's Theorem 1 gives the same `0/q` spectrum for the basic `q x q` Ramanujan matrix, and his Theorem 2 treats the unweighted sum over many moduli on a least-common-multiple period. P. P. Vaidyanathan's 2014 Ramanujan-subspace framework independently packages the same harmonic structure as orthogonal exact-period subspaces and their projection operators.

No novelty is claimed for (1)--(3), the Ramanujan subspaces, or their Fourier diagonalization.

## 2. Exact signed spectrum on a complete period

First combine every repeated copy of the same scalar modulus into one coefficient `omega_m`; cancellation between duplicate copies is ordinary coefficient aggregation and is not the cross-modulus question.

Using (2),

\[
A_L=L\sum_m\omega_mP_m^{(L)}
\tag{4}
\]

is already a spectral decomposition into mutually orthogonal invariant subspaces. On `\operatorname{ran}P_m^(L)` it acts as multiplication by `L omega_m`; on the orthogonal complement of all active Ramanujan subspaces it vanishes. Therefore

\[
\operatorname{rank}A_L
=
\sum_{\omega_m\ne0}\varphi(m),
\tag{5}
\]

\[
n_+(A_L)=\sum_{\omega_m>0}\varphi(m),
\qquad
n_-(A_L)=\sum_{\omega_m<0}\varphi(m),
\tag{6}
\]

and

\[
|A_L|
=L\sum_m|\omega_m|P_m^{(L)}
=
\sum_m|\omega_m|C_m^{(L)}.
\tag{7}
\]

Thus the Loewner majorization from WI-079 becomes much sharper on a complete period: not only does replacing `omega_m` by `|omega_m|` provide a positive upper comparator, it is literally the operator absolute value. Every unitarily invariant norm is consequently sign-insensitive. For example,

\[
\|A_L\|_{S_p}^p
=L^p\sum_m\varphi(m)|\omega_m|^p,
\tag{8}
\]

and

\[
\|A_L\|_{\rm op}=L\max_m|\omega_m|.
\tag{9}
\]

This is a decisive negative result for a specific class of signed scalar arguments: signs cannot buy a saving after the modulus blocks have been completed to common residue periods.

## 3. Every finite WI-079 Toeplitz block is a principal compression of the orthogonal decomposition

Let `N` be the length of the source interval in WI-079. Let

\[
L_0=\operatorname{lcm}\{m:\omega_m\ne0\}
\]

and choose any multiple `L` of `L_0` with `L>=N`. Let `R_N` restrict vectors on `\mathbf Z/L\mathbf Z` to `N` consecutive coordinates.

For `0<=i,j<N`, periodicity gives

\[
(C_m^{(L)})_{ij}
=c_m(i-j\bmod L)
=c_m(i-j),
\tag{10}
\]

because `m|L`. Hence

\[
R_NA_LR_N^*
=
\left(\sum_m\omega_m c_m(i-j)\right)_{0\le i,j<N}
=A_N.
\tag{11}
\]

This representation is exact and introduces no asymptotic approximation. A translated consecutive source interval gives the same Toeplitz block because only differences occur.

Equation (11) identifies the only place where different modulus blocks can cease to be orthogonal. Although

\[
P_m^{(L)}P_n^{(L)}=0
\quad(m\ne n),
\]

the compressed positive blocks

\[
R_NP_m^{(L)}R_N^*,
\qquad
R_NP_n^{(L)}R_N^*
\]

need not have orthogonal ranges. The proposed signed cancellation is therefore a **time-frequency leakage phenomenon caused by truncation**, not cancellation between complete Ramanujan residue classes.

This distinction was not visible in WI-079's entrywise Ramanujan/divisor marginals. Those marginals are still necessary tests, but (11) supplies the global spectral geometry behind them.

## 4. Boundary defect controls how much signature compression can erase

Take the smallest convenient complete period above the window,

\[
L=\left\lceil\frac{N}{L_0}\right\rceil L_0,
\qquad
r=L-N,
\qquad
0\le r<L_0.
\tag{12}
\]

The `N x N` matrix `A_N` is obtained by deleting `r` rows and the corresponding columns from the Hermitian `L x L` matrix `A_L`. Cauchy interlacing implies that deletion of one coordinate can lower the positive inertia by at most one and the negative inertia by at most one. Iterating `r` times and inserting (6) gives

\[
\boxed{
n_+(A_N)
\ge
\left(\sum_{\omega_m>0}\varphi(m)-r\right)_+,
}
\tag{13}
\]

\[
\boxed{
n_-(A_N)
\ge
\left(\sum_{\omega_m<0}\varphi(m)-r\right)_+.
}
\tag{14}
\]

This is exactly the type of signature information relevant to the `weil_inertia` mandate: on a nearly complete common period, finite-window mixing cannot destroy a macroscopic signed spectral block unless the boundary defect is itself comparably large.

There is also a sharp extremal-norm corollary. Put

\[
W=\max_m|\omega_m|,
\]

and let

\[
p_W=\sum_{\omega_m=W}\varphi(m),
\qquad
q_W=\sum_{\omega_m=-W}\varphi(m).
\]

The eigenvalues `LW` and `-LW` of `A_L` have multiplicities `p_W` and `q_W`. If

\[
\max(p_W,q_W)>r,
\tag{15}
\]

interlacing forces the corresponding endpoint eigenvalue to survive the principal compression. Since compression cannot increase operator norm,

\[
\boxed{\|A_N\|_{\rm op}=LW}
\tag{16}
\]

under (15).

The important boundary is explicit. When `L_0` is enormous compared with `N`, the smallest common period has `r=L_0-N` enormous and (13)--(16) can become vacuous. That is not a defect in the statement: it says precisely that any successful global signed scalar argument must exploit the **large-common-period, strongly time-limited regime**. Small-lcm/period-complete regroupings cannot provide the hoped-for cancellation.

## 5. Consequence for the current Yang scalar escape

WI-075--WI-078 closed, in turn, power sparsity of the effective scalar support, ordinary unweighted scalar additive-energy savings, and positive/absolute-weight mass-preserving pruning. WI-079 then isolated the only surviving scalar possibility: estimate the signed operator

\[
A_\omega=\sum_m\omega_m T_m^*T_m
\]

directly, rather than pass first through the positive Baker--Munsch--Shparlinski consumer.

The present result narrows that possibility again. The modulus Gram blocks are not merely generic PSD matrices. On a common residue period they are scalar multiples of **mutually orthogonal exact-period projections**. Hence signed cancellation cannot come from combining complete modulus blocks, regardless of how favorable the signs look in the outer coefficient sequence.

The surviving scalar problem is now more specific:

\[
\boxed{
\text{estimate interference between time-limited Ramanujan subspaces}
\quad\text{in the source-faithful large-lcm regime}.
}
\tag{17}
\]

A proof based on completing periods and then taking a norm, trace moment, or inertia estimate will erase the only mechanism that could make the signs useful. Conversely, a theorem for the finite sections may exploit prolate/time-band-limiting geometry, labelled factorization, noncommuting projections, or another structure that genuinely sees the restriction `R_N`.

This does not prove that the exact post-local-main Yang covariance reduces to the scalar operator form of WI-079. That source-interface caveat remains. Nor does it rule out a two-dimensional/direction-labelled dispersion estimate. It only closes the cheaper interpretation that centered scalar signs can cancel complete Ramanujan modulus blocks by themselves.

## 6. Prior-art and novelty boundary

Established prior art used here:

- Noboru Ushiroya, **Eigenvalues of Matrices whose Elements are Ramanujan Sums or Kloosterman Sums**, *Journal of Integer Sequences* 21 (2018), Article 18.2.6; arXiv:1803.02970. Lemma 1 gives the common-multiple convolution orthogonality (1); Theorem 1 gives the `0/q` spectrum of a single Ramanujan matrix; Theorem 2 treats an unweighted sum of Ramanujan kernels on an lcm period.
- P. P. Vaidyanathan, **Ramanujan Sums in the Context of Signal Processing—Part I: Fundamentals**, *IEEE Transactions on Signal Processing* 62:16 (2014), 4145--4157, DOI `10.1109/TSP.2014.2331617`; and **Part II: FIR Representations and Applications**, ibid. 4158--4172, DOI `10.1109/TSP.2014.2331624`. Role: classical Ramanujan-subspace/projection language and orthogonal exact-period decomposition of finite signals.
- Cauchy interlacing / principal-submatrix inertia inequalities are classical Hermitian matrix theory.

No novelty is claimed for Ramanujan-sum orthogonality, circulant Fourier diagonalization, exact-period subspaces, or interlacing. A bounded audit of the current `weil_inertia` corpus found WI-079's Toeplitz/Ramanujan-sum operator and divisor marginals but no stored finding making the common-period orthogonal-projector reduction or the resulting boundary-only interpretation of signed cancellation. The durable Mathia contribution is the **source-interface deduction** from those classical identities: the sign-sensitive scalar escape surviving WI-079 is not a complete-period cancellation problem; it is necessarily a finite-section/time-limiting problem, with the exact inertia loss bounded by the number of deleted coordinates when the common period is close.

No priority claim is made.

## 7. Falsification and remaining gates

1. **Aggregate duplicate moduli first.** Distinct source terms with the same scalar modulus can cancel in their coefficient sum `omega_m`. The no-cancellation statement concerns distinct modulus blocks after this exact aggregation.
2. **Real signed coefficients.** The inertia statements require a Hermitian signed combination, hence real `omega_m`, matching the scalar outer-sign model isolated in WI-079. Complex outer coefficients would require singular-value rather than inertia language.
3. **Complete-period scope is exact.** Equations (4)--(9) require a length divisible by every active modulus. There is no claim that the actual Yang source window has this property.
4. **Finite sections remain genuinely open.** When `L_0>>N`, the boundary `r` in (12) is large and the interlacing lower bounds may be vacuous. A source-faithful signed large-sieve theorem could still obtain cancellation from the overlaps of the compressed Ramanujan subspaces.
5. **The scalar source interface remains unproved.** WI-079 already records that Mathia has not reduced the entire post-local-main locked four-prime covariance to an outer-signed scalar modulus form. This finding is conditional on that proposed scalar reorganization and therefore does not close the accepted Yang locked-covariance clue.
6. **Labelled/two-dimensional routes remain outside the obstruction.** A transform retaining reduced direction `(r,q)`, the two physical shifts, residue fibers, or source phases can carry information absent from the unlabelled scalar Ramanujan operator.
7. **Decisive next test.** If an exact signed scalar reduction is obtained, inspect the active-modulus lcm relative to the source window and compute the compressed cross-Gram blocks `R_NP_mP_nR_N^*` (equivalently the finite-section leakage between `R_NP_m` and `R_NP_n`). A power saving must come from this leakage geometry; any argument whose first step restores complete common periods is already blocked by (7)--(9).
