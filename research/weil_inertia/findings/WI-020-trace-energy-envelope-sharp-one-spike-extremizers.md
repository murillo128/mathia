# WI-020 — the trace--energy envelope is sharp and high-energy extremizers have a one-spike spectrum

**Status:** `EXACT-DERIVED`. This finding resolves the local compression question exposed by the WI-011 adversarial review. It strengthens the repaired inequality `D >= Phi_m(E)` into an exact fixed-energy minimization theorem, characterizes every high-energy equality spectrum, and gives quantitative slack away from that spectrum. The proof is finite-dimensional and elementary once the WI-011 defect profile is fixed; no new zeta or prime-side input is used.

## 1. Exact fixed-energy theorem

Let `G` be an `m x m` positive-semidefinite Hermitian matrix with unit diagonal, `m>=2`. Write its eigenvalues as `lambda_i>=0`, so

\[
\sum_{i=1}^m\lambda_i=m.
\]

Set

\[
x_i=\lambda_i-1,\qquad x_i\ge-1,\qquad \sum_i x_i=0,
\]

and define

\[
E=\operatorname{tr}(G-I)^2=\sum_i x_i^2,
\]

\[
D=\operatorname{tr}\Psi(G)=\sum_i\psi(x_i),
\qquad
\psi(x)=
\begin{cases}
x^2,&-1\le x\le1,\\
2x-1,&x\ge1.
\end{cases}
\]

The feasible energy range is

\[
0\le E\le m(m-1).
\]

For every feasible `E`, the exact minimum of `D` over all such Gram matrices is

\[
\boxed{
\min D=\Phi_m(E),
}
\tag{1}
\]

where

\[
\Phi_m(E)=
\begin{cases}
E,&0\le E\le \dfrac{m}{m-1},\\[2mm]
2\sqrt{\dfrac{m-1}{m}E}-1+\dfrac Em,
&\dfrac{m}{m-1}\le E\le m(m-1).
\end{cases}
\tag{2}
\]

Thus the envelope repaired and used in WI-011 is not merely a lower bound: it is the **sharp spectral envelope at fixed Frobenius energy**.

For

\[
E>\frac{m}{m-1},
\qquad
r_*:=\sqrt{\frac{m-1}{m}E}>1,
\]

equality in (1) holds if and only if, up to permutation, the shifted eigenvalues are

\[
\boxed{
\left(r_*,-\frac{r_*}{m-1},\ldots,-\frac{r_*}{m-1}\right).
}
\tag{3}
\]

Equivalently the eigenvalue multiset is

\[
\boxed{
\left\{1+r_*,\left(1-\frac{r_*}{m-1}\right)^{[m-1]}\right\}.
}
\tag{4}
\]

An explicit unit-diagonal PSD realization is the equicorrelation matrix

\[
G_*=(1-c)I+c\mathbf1\mathbf1^*,
\qquad
c=\frac{r_*}{m-1}.
\tag{5}
\]

Since `E<=m(m-1)`, one has `0<=c<=1`, so (5) is feasible and has exactly the spectrum (4).

For `E<=m/(m-1)`, every feasible spectrum has `lambda_i<=2`; hence `D=E` identically and the low-energy branch has many equality configurations rather than a unique spectrum.

## 2. Why the low-energy branch is forced

Suppose some shifted eigenvalue satisfies `x_1=r>1`. The remaining coordinates sum to `-r`, so Cauchy--Schwarz gives

\[
\sum_{i=2}^m x_i^2\ge\frac{r^2}{m-1}.
\]

Therefore

\[
E\ge r^2+\frac{r^2}{m-1}
=\frac{m}{m-1}r^2
>\frac{m}{m-1}.
\tag{6}
\]

Consequently no coordinate can cross the affine branch when `E<=m/(m-1)`. In that whole range `psi(x_i)=x_i^2` for every `i`, proving

\[
D=E=\Phi_m(E).
\]

The threshold `m/(m-1)` is therefore intrinsic: it is the least energy at which an eigenvalue can exceed `2` under the trace constraint.

## 3. Compression reduces every high-energy minimizer to one spike

Assume at least two shifted eigenvalues lie above the threshold. Write the `k>=2` large coordinates as

\[
x_i=1+z_i,\qquad z_i>0,
\]

and put `Z=sum z_i`. Replace them by

\[
1+Z,\underbrace{1,\ldots,1}_{k-1},
\]

leaving the other coordinates unchanged. As persisted in the repaired WI-011 argument, this operation preserves the total sum and preserves `D` exactly, while its energy changes by

\[
\boxed{
E'-E
=Z^2-\sum_i z_i^2
=2\sum_{i<j}z_i z_j>0.
}
\tag{7}
\]

The transformed vector has at most one coordinate strictly above `1`. Thus any lower bound for the one-large-coordinate case at energy `E'` transfers back to the original vector; because `Phi_m` is strictly increasing, (7) also shows that a configuration with two or more genuinely super-threshold coordinates can never attain equality in (1).

Now suppose there is exactly one large coordinate `r>1`. The remaining coordinates sum to `-r`, so again

\[
E\ge\frac{m}{m-1}r^2,
\qquad
r\le r_*:=\sqrt{\frac{m-1}{m}E}.
\tag{8}
\]

For this spectrum

\[
D=E+2r-1-r^2.
\tag{9}
\]

At fixed `E`, the right side of (9) is strictly decreasing for `r>1`. Hence it is minimized at the largest permitted `r`, namely `r=r_*`. Substitution gives

\[
D\ge E+2r_*-1-r_*^2
=2r_*-1+\frac Em
=\Phi_m(E).
\tag{10}
\]

Equality in Cauchy--Schwarz in (8) forces every remaining coordinate to equal `-r_*/(m-1)`, proving (3)--(4). If instead no coordinate exceeds `1` while `E>m/(m-1)`, then `D=E`, and

\[
E-\Phi_m(E)=(r_*-1)^2>0,
\]

so equality is impossible there as well.

## 4. Quantitative near-equality rigidity

The same proof gives explicit stability information.

### Several super-threshold eigenvalues

For `k>=2`, let `z_i=x_i-1>0` on the large coordinates. Across the full feasible energy interval,

\[
\Phi_m'(E)\ge\frac2m
\]

(with the derivative interpreted one-sided at the kink). Combining this with (7) and the compressed-vector envelope gives

\[
\boxed{
D-\Phi_m(E)
\ge
\frac4m\sum_{i<j}z_i z_j.
}
\tag{11}
\]

Thus near saturation quantitatively forbids two substantial eigenvalue excesses above `2`: their pairwise excess products must be small.

### Exactly one super-threshold eigenvalue

Let `r>1` be the unique large shifted eigenvalue and define the variance of the remaining coordinates around their forced mean by

\[
V:=\sum_{i\ne1}
\left(x_i+\frac{r}{m-1}\right)^2.
\]

Then

\[
E=\frac{m}{m-1}r^2+V,
\qquad
r_*^2-r^2=\frac{m-1}{m}V.
\tag{12}
\]

A direct subtraction from (10) gives the exact identity

\[
\boxed{
D-\Phi_m(E)
=(r_*-r)(r_*+r-2)
=
\frac{m-1}{m}V\,
\frac{r_*+r-2}{r_*+r}.
}
\tag{13}
\]

In particular, if the large coordinate stays a fixed amount above the kink, `r>=1+eta`, then

\[
\boxed{
D-\Phi_m(E)
\ge
\frac{m-1}{m}\frac{\eta}{1+\eta}\,V.
}
\tag{14}
\]

Away from the threshold, near equality therefore forces the other `m-1` eigenvalues to become nearly equal, not merely to remain below `2`.

These two estimates give a useful spectral picture of a high-energy near-extremizer:

\[
\boxed{
\text{one eigenvalue justifies the affine tail; the remaining spectrum is nearly flat.}
}
\]

## 5. Relation to WI-011

WI-011 only needed the inequality `D>=Phi_m(E)` at

\[
m=438,
\qquad
E=A=\frac{20097}{20000}=1.00485.
\]

At this point

\[
\frac{m}{m-1}=1.0022883295\ldots,
\qquad
r_*=1.0012770954\ldots,
\]

so the sharp equality spectrum would have

\[
\lambda_{\max}=2.0012770954\ldots,
\qquad
\lambda_2=\cdots=\lambda_m
=0.9977087481\ldots.
\]

The operating point is only slightly beyond the kink. Indeed

\[
E-\Phi_{438}(E)=1.63097\ldots\times10^{-6}.
\]

This explains why the nonlinear envelope improves the four-point assembly only slightly: its extremizer is already extremely close to the branch point where `D=E` becomes exact. The rigidity theorem is therefore structural information, not a hidden large numerical gain for WI-011.

If a future argument comes close to saturating the WI-011 trace--energy conversion on blocks whose energy is bounded away from the kink, (11)--(14) give exact conditions that its Gram spectrum must satisfy. Such conditions can be compared against additional Gram geometry or arithmetic information rather than treating the envelope slack as an opaque scalar loss.

## 6. A reusable tangent-affine generalization

The compression mechanism is not special to the numerical threshold `1`. For `a>0`, define on the real line

\[
\psi_a(x)=
\begin{cases}
x^2,&x\le a,\\
2ax-a^2,&x\ge a.
\end{cases}
\]

For arbitrary real `x_1,...,x_m` with zero sum and fixed energy `E=sum x_i^2`, the same proof gives

\[
\boxed{
\min\sum_i\psi_a(x_i)
=
\begin{cases}
E,&E\le \dfrac{ma^2}{m-1},\\[2mm]
2a\sqrt{\dfrac{m-1}{m}E}-a^2+\dfrac Em,
&E\ge \dfrac{ma^2}{m-1}.
\end{cases}
}
\tag{15}
\]

On the high branch the equality vector is, up to permutation,

\[
\left(
\sqrt{\frac{m-1}{m}E},
-\frac1{m-1}\sqrt{\frac{m-1}{m}E},\ldots
\right).
\]

The exact excess-compression identity becomes

\[
E'-E=2\sum_{i<j}z_i z_j
\]

when the super-threshold coordinates are written `a+z_i`.

This establishes a reusable principle for **quadratic penalties continued by their tangent affine branch**. It does not establish an analogous theorem for arbitrary convex profiles that merely happen to become affine; their curved branch would need a separate analysis.

## 7. Prior-art and novelty audit

The quadratic-to-linear shape is classical in robust statistics: Peter J. Huber, *Robust Estimation of a Location Parameter*, Ann. Math. Statist. 35 (1964), 73--101, DOI `10.1214/aoms/1177703732`, introduced the familiar symmetric Huber loss. The profile here is a one-sided tangent-affine analogue arising from spectral clipping, and WI-012 already places the associated spectral convex function inside classical Fenchel analysis.

Majorization and convex-order theory provide broad classical language for concentrating coordinates under symmetric constraints. Targeted searches around Huber losses, fixed first/second moments, fixed trace/Frobenius norm, and one-large-eigenvalue extremizers did not locate a source stating the exact finite equal-weight problem (1)--(4) or the stability identities (11)--(14). That absence is not evidence of priority. No novelty claim is made beyond recording the exact deduction for this Mathia spectral functional.

The important provenance distinction is therefore:

- the **shape** of a quadratic-to-affine loss is classical;
- the WI-011 compression step was already exposed by the adversarial/qwen-lean audit;
- equations (1)--(4) and (11)--(15) are exact consequences derived here from that compression and the trace constraint.

## 8. Boundaries and falsification tests

This theorem optimizes only the spectral conversion from `E` to `D`. It does not say that actual Montgomery--Taylor Gram blocks can realize the equicorrelation extremizer while also satisfying their ordered-gap kernel geometry. Proving that they cannot is precisely a possible source of additional support-one gain.

It also does not constrain the exceptional block `Q'` directly and therefore does not distinguish multiple critical-line zeros from screened off-line pairs. The WI-005--WI-007 obstruction remains untouched.

The high-energy stability degenerates as `r` approaches `1`; equation (13) makes that loss explicit. Since the WI-011 numerical operating point lies very close to the kink, one should not infer a large quantitative improvement from the equality classification alone.

A finite falsification test is straightforward: for any proposed counterexample spectrum with fixed trace `m` and energy `E`, compute `D`; (1) predicts `D>=Phi_m(E)`, with high-energy equality only for the multiset (4). For the generalized profile (15), the same test applies after replacing the threshold by `a`.

## 9. Consequence for `weil_inertia`

The trace--energy conversion now has a complete extremal description. There is no remaining algebraic slack to recover by sharpening `D>=Phi_m(E)` as a function of `E` alone:

\[
\boxed{
\text{any further gain must use information beyond the scalar energy }E.
}
\]

At high energy, the only exact equality spectrum is one-spike plus a flat complement, and (11)--(14) quantify departures from it. This supplies a concrete target for future Gram-geometry or arithmetic constraints: rule out, or charge positive defect to, Montgomery--Taylor blocks whose spectra approach that pattern.