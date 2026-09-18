# PC-350 — full inversion defect is faithful via a two-by-two Fourier decoder

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `NUMERICAL-SANITY` + `DECISIVE-NEGATIVE` for raw all-depth inversion-signature depth as an RH selector; `DECISIVE-BOUNDARY` for strict source-forced quotients/invariants of that signature.

PC-349 closes the Prime-Circle radial path by the reciprocity-forced totient ray and shows that the resulting regularized inversion defect has trivial abelianization while its first nonzero Lie level is only a rank-two area form. It deliberately leaves open whether **unbounded** noncommutative depth can retain genuinely more information than that low-rank first correction.

For finite shell sets containing shell `2`, there is an exact answer. The complete regularized inversion defect is injective on the reciprocal Prime-Circle radial profiles once the canonical shell labels/reciprocity vector are fixed. In fact, one does not need arbitrary matrix representations or the whole free Lie algebra: a family of source-native `2 x 2` solvable evaluations, using shell `2` as the canonical calibration coordinate, already recovers every centered shell profile. Their upper-right entries are Fourier transforms of finite signed measures whose two pieces live on disjoint intervals, so Fourier uniqueness reconstructs the original radial differential exactly.

Thus the rank-two collapse in PC-349 is only the **first derivative at zero** of an all-depth decoder. Higher repeated-shell-`2` words restore the information lost at first Lie order. This is mathematically substantive, but negative for the RH objective: the same decoder works for arbitrary non-arithmetic reciprocal paths with one calibration coordinate. Raw unbounded signature depth is therefore another lossless source encoding, not a zeta-zero selector. A surviving mechanism must pass to a strict, geometry-forced quotient or invariant with an independently zero-sensitive destination.

## 1. Centering by the canonical shell `2` removes the asymptotic ray exactly

Retain the notation of PC-349. For a finite shell set `S` with `2 in S`, let

\[
X_n(r):=\log\Phi_n(r),\qquad r\ge0,
\tag{1}
\]

and

\[
H:=\sum_{m\in S}\varphi(m)e_m.
\tag{2}
\]

Cyclotomic reciprocity gives, for every `n>1`,

\[
X_n(r)=\varphi(n)\log r+X_n(r^{-1}).
\tag{3}
\]

Shell `2` is special only in the useful sense that it supplies an exact canonical clock:

\[
\Phi_2(r)=1+r,
\qquad
X_2(r)=\log(1+r),
\qquad
\varphi(2)=1.
\tag{4}
\]

For every target shell `n != 2`, define the transverse centered profile

\[
\boxed{
W_n(r):=X_n(r)-\varphi(n)X_2(r).
}
\tag{5}
\]

Subtracting the two reciprocity laws gives the exact inversion symmetry

\[
\boxed{
W_n(r)=W_n(r^{-1}).
}
\tag{6}
\]

Moreover `W_n(0)=0`, `W_n` is real analytic on `[0,1]`, and differentiating (6) gives

\[
W_n'(r)=-r^{-2}W_n'(r^{-1})=O(r^{-2})
\qquad(r\to\infty).
\tag{7}
\]

Hence `dW_n` has finite total variation on `(0,infinity)`. The asymptotic logarithmic direction has disappeared completely from the transverse coordinate.

This centering is not fitted to a desired zeta formula. The coefficient `varphi(n)` is exactly the reciprocity residue already present in PC-349, and shell `2` is an intrinsic member of the primitive-layer family.

## 2. A `2 x 2` solvable evaluation isolates one transverse shell at all depths

Let

\[
D=\begin{pmatrix}1&0\\0&0\end{pmatrix},
\qquad
E=\begin{pmatrix}0&1\\0&0\end{pmatrix},
\tag{8}
\]

so that

\[
D^2=D,\qquad DE=E,\qquad ED=E^2=0.
\tag{9}
\]

For a complex parameter `lambda` and a target shell `n != 2`, define a linear substitution on the shell letters by

\[
\boxed{
\rho_{\lambda,n}(e_m)
=
\lambda\,\delta_{m2}D
+
\bigl(\delta_{mn}-\varphi(n)\delta_{m2}\bigr)E.
}
\tag{10}
\]

The reciprocity vector is sent to

\[
\rho_{\lambda,n}(H)=\lambda D,
\tag{11}
\]

because `varphi(2)=1`. Along the radial connection

\[
\Omega=\sum_{m\in S}e_m\,dX_m,
\tag{12}
\]

we obtain

\[
\boxed{
\rho_{\lambda,n}(\Omega)
=
\lambda D\,dX_2+E\,dW_n.
}
\tag{13}
\]

Use the right-ordered convention of PC-348/PC-349. If

\[
U(r)=\begin{pmatrix}a(r)&b(r)\\0&1\end{pmatrix},
\qquad U(0)=I,
\tag{14}
\]

then `U'=U rho(Omega)` gives

\[
a'=\lambda X_2' a,
\qquad
b'=aW_n'.
\tag{15}
\]

Therefore at cutoff `R`,

\[
a(R)=(1+R)^\lambda,
\qquad
b(R)=\int_0^R(1+r)^\lambda\,dW_n(r).
\tag{16}
\]

The reciprocity-forced closing factor of PC-349 evaluates to

\[
\exp[-(\log R)\rho(H)]
=
\begin{pmatrix}R^{-\lambda}&0\\0&1\end{pmatrix}.
\tag{17}
\]

Right multiplication by (17) changes only the first column. Hence the regularized diagonal tends to `1`, while the upper-right entry tends to

\[
\boxed{
V_n(\lambda)
:=
\int_0^\infty(1+r)^\lambda\,dW_n(r),
\qquad \Re\lambda<1.
}
\tag{18}
\]

The convergence domain follows from (7). In particular the entire imaginary axis is available.

The key point is that this is an **all-depth subsector of the universal defect**, not an extra operator inserted after the fact. Because `E^2=ED=0`, the evaluation selects words containing one transverse insertion together with arbitrarily many shell-`2` insertions. Expanding around `lambda=0` reads those coefficients degree by degree. Thus equality of two formal regularized defects forces equality of every derivative of `V_n` at zero; since (18) is holomorphic on the connected half-plane `Re lambda<1`, the identity theorem forces equality of `V_n(lambda)` throughout that half-plane.

## 3. Inversion turns the decoder into a support-separated Fourier transform

Split (18) at `r=1` and put `r=1/t` in the exterior half. Equation (6) reverses the orientation of `dW_n`, giving

\[
\boxed{
V_n(\lambda)
=
\int_0^1
\left[
(1+t)^\lambda-
\left(1+\frac1t\right)^\lambda
\right]dW_n(t).
}
\tag{19}
\]

Now restrict to `lambda=i tau`, `tau in R`, and define

\[
a(t):=\log(1+t),
\qquad
b(t):=\log\left(1+\frac1t\right).
\tag{20}
\]

On `0<t<=1`, these maps have complementary ranges

\[
a((0,1])=(0,\log2],
\qquad
b((0,1])=[\log2,\infty).
\tag{21}
\]

Let `mu_n=dW_n` on `(0,1]`. Since `W_n` is analytic, `mu_n` is a finite signed measure with no atoms. Equation (19) becomes

\[
\boxed{
V_n(i\tau)
=
\int_{\mathbb R}e^{i\tau y}\,d\nu_n(y),
\qquad
\nu_n:=a_\#\mu_n-b_\#\mu_n.
}
\tag{22}
\]

Thus `V_n(i tau)` is the Fourier--Stieltjes transform of a finite signed measure. Fourier uniqueness determines `nu_n` exactly from all real `tau`.

The two summands in `nu_n` occupy disjoint open supports: `a_# mu_n` lies below `log 2`, while `b_# mu_n` lies above `log 2`. They meet only at `log 2`, and neither has an atom there. Consequently `nu_n` itself separates the two pieces:

\[
\nu_n\!\restriction_{(0,\log2)}
=
a_\#\mu_n\!\restriction_{(0,\log2)}.
\tag{23}
\]

Because `a(t)=log(1+t)` is a bijection from `(0,1)` to `(0,log2)`, (23) recovers `mu_n=dW_n`. The normalization `W_n(0)=0` then recovers `W_n` itself, and finally

\[
\boxed{
X_n(t)=W_n(t)+\varphi(n)\log(1+t),
\qquad 0\le t\le1.
}
\tag{24}
\]

Reciprocity (3) recovers the exterior profile as well.

Therefore, for fixed shell labels and their canonical reciprocity weights,

\[
\boxed{
\mathcal D_S
\text{ determines every }X_n|_{[0,1]}
\text{ whenever }2\in S.
}
\tag{25}
\]

More precisely, the repeated-shell-`2`/one-transverse word sector already suffices. The entire free noncommutative signature contains strictly more information than is needed for this injectivity statement.

## 4. PC-349's rank-two area is exactly the first linear-response coefficient

Equation (19) also identifies precisely what PC-349 measured. Since the bracket vanishes at `lambda=0`,

\[
V_n(0)=0.
\tag{26}
\]

Differentiating once,

\[
\begin{aligned}
V_n'(0)
&=
\int_0^1
\left[
\log(1+t)-\log\left(1+\frac1t\right)
\right]dW_n(t)\\
&=
\int_0^1\log t\,dW_n(t)\\
&=
-\int_0^1W_n(t)\frac{dt}{t}.
\end{aligned}
\tag{27}
\]

The boundary term in the integration by parts vanishes because `W_n(t)=O(t)` at zero. If

\[
I_m:=\int_0^1X_m(t)\frac{dt}{t},
\tag{28}
\]

then (5) gives

\[
V_n'(0)=\varphi(n)I_2-I_n.
\tag{29}
\]

But PC-349 proves

\[
A_{mn}=\varphi(n)I_m-\varphi(m)I_n.
\tag{30}
\]

Since `varphi(2)=1`,

\[
\boxed{
V_n'(0)=A_{2n}.
}
\tag{31}
\]

So the rank-two first Lie layer is not the end of the inversion information. It is simply the first derivative at the origin of a faithful all-depth transform. More generally,

\[
\boxed{
V_n^{(k)}(0)
=
\int_0^1
\left[
\log^k(1+t)-
\log^k\left(1+\frac1t\right)
\right]dW_n(t),
\qquad k\ge1.
}
\tag{32}
\]

The full sequence of repeated-calibration moments, equivalently the analytic germ of `V_n`, restores the transverse shell profile even though its first coefficient has the universal rank-two collapse found in PC-349.

This resolves an important interpretive ambiguity: low rank at the first Lie level does **not** imply that the regularized inversion defect is information-poor at unbounded depth.

## 5. Faithfulness is kinematic under a matched non-arithmetic control

The decoder above does not use cyclotomic factorization after the reciprocity law is supplied. Let `Y_j(r)` be any sufficiently regular family satisfying

\[
Y_j(r)=a_j\log r+Y_j(r^{-1}),
\tag{33}
\]

and assume it contains a calibration coordinate

\[
Y_0(r)=\log(1+r),
\qquad a_0=1.
\tag{34}
\]

Set

\[
Z_j(r)=Y_j(r)-a_jY_0(r).
\tag{35}
\]

Then `Z_j(r)=Z_j(1/r)`. Replacing `X_2,W_n,varphi(n)` by `Y_0,Z_j,a_j` in (10)--(24) reproduces the same support-separated Fourier decoder verbatim. Therefore the complete reciprocal inversion defect is injective on this broad non-arithmetic control class as well.

This control is decisive for interpretation. Prime Circle contributes a canonical calibration shell and exact integer reciprocity residues, but **the recovery mechanism itself is reciprocity plus one calibration direction**, not cyclotomic arithmetic. Hence faithfulness cannot by itself be evidence for a Riemann-zero mechanism.

## 6. Novelty and prior-art audit

The abstract ingredients are classical and must not be counted as novelty. Hambly and Lyons, *Uniqueness for the signature of a path of bounded variation and the reduced path group*, Annals of Mathematics 171 (2010), 109--167, DOI `10.4007/annals.2010.171.109`, prove that ordinary bounded-variation path signatures determine paths modulo tree-like equivalence. PC-348 already applies that theorem to the **interior** Prime-Circle radial signature. Lyons and Xu, *Inverting the signature of a path*, J. Eur. Math. Soc. 20 (2018), 1655--1687, DOI `10.4171/JEMS/796`, gives explicit reconstruction methods for ordinary path signatures. Fourier--Stieltjes uniqueness for finite signed measures, triangular/solvable matrix developments, and Mellin/Fourier changes of variables are standard harmonic-analysis tools.

Those theorems do not by themselves settle the present object: PC-349's inversion defect is a **regularized limit of an unbounded reciprocal path plus an asymptotic closing ray**, with trivial abelianization. The ordinary bounded-variation uniqueness theorem therefore does not immediately say whether the regularized defect still remembers the original source profile. The exact line-local delta here is the explicit centering (5), solvable evaluation (10), transform (19), support separation (21)--(23), and the identification (31) of PC-349's low-rank area as only the first Taylor coefficient.

A targeted prior-art search over path-signature inversion, triangular matrix developments, regularized root-of-unity holonomy, and Mellin/Fourier reconstruction did not locate this specific Prime-Circle reciprocal decoder. No broad historical novelty is claimed: the construction is an exact application of classical ingredients to this source-native regularized defect. The cyclotomic regularized-holonomy/associator boundary remains exactly the one already audited in PC-349.

## 7. Consequence for the RH-facing frontier

PC-349 left **unbounded noncommutative depth** as a surviving possibility after the abelian and first-Lie channels collapsed. Equation (25) now shows that raw unbounded depth, without any further quotient or destination theorem, is not a new selector. It is again a source reconstruction device.

This is analogous to PC-348 but stronger in the inversion-closed setting. PC-348 says the full interior signature is faithful when a monotone prime-power coordinate is available. Here the regularized inversion defect has zero displacement and a rank-two first Lie level, yet a much smaller repeated-calibration subsector still recovers every centered profile. Closing by inversion has hidden the information from low-degree summaries, not destroyed it.

The surviving branch is consequently narrower. A future all-depth proposal must specify **before** looking for zeta zeros:

1. a strict quotient, representation, scalar invariant, or conductor-coupled limit forced by the original root/refinement geometry rather than chosen as an arbitrary spectral wrapper;
2. a reason that this operation discards ordinary source-reconstruction information instead of merely repackaging it;
3. an independently established destination related to the zeta functional equation, explicit formula, zero set, or critical line; and
4. a matched non-arithmetic reciprocal control on which the claimed arithmetic selectivity fails.

Merely showing that an infinite-depth holonomy is nontrivial, high-rank after representation, or able to reconstruct the cyclotomic profiles is no longer progress toward RH under the line mandate.

## Numerical sanity checks

The exact argument above is primary. Direct finite-cutoff quadrature provides a check on the inversion and regularization signs. For example, with cutoff `R=10^4`:

- for `n=3`, `tau=0.5`, (19) gives approximately `-0.4257538966 + 0.0437557791 i`, while the direct integral in (18) to `R` gives `-0.4257515380 + 0.0437601899 i`, an error about `5.0e-6`;
- for `n=3`, `tau=2`, the two values differ by about `4.0e-6`;
- for `n=6` and `n=10`, the corresponding discrepancies are of order `5e-5`, consistent with the omitted `O(R^{-1})` tail.

These tests probe both a prime shell and composite shells and agree with the exact transformation (19).

## Audit / falsification tests

This finding must be revised if any of the following fails:

1. shell `2` does not obey `X_2(r)=log(1+r)` and the same reciprocal law with residue one;
2. subtraction (5) does not give exact inversion invariance (6);
3. `dW_n` fails to have finite variation on `(0,infinity)`, invalidating (18) on the imaginary axis;
4. the substitution (10) fails to send `H` to `lambda D` or fails to produce the triangular evolution (15);
5. the reciprocity change of variables does not yield the minus sign and transform (19);
6. the pushforward measures in (22) overlap on a set of positive measure, so that `nu_n` cannot be separated into its two source pieces;
7. equality of the all-depth formal defects does not determine the analytic germ of `V_n` at zero, or that germ fails to determine `V_n` on `Re lambda<1`;
8. Fourier--Stieltjes uniqueness fails for the finite signed measures in (22);
9. the first derivative (31) disagrees with the area formula of PC-349;
10. a matched reciprocal control satisfying (33)--(34) fails under the same decoder, which would invalidate the claim that faithfulness is kinematic rather than arithmetic.

## Bottom line

The canonical inversion-closed Prime-Circle signature does **not** remain low-information at unbounded depth. For shell sets containing `2`, an explicit family of `2 x 2` solvable evaluations turns a repeated-shell-`2` subsector into a support-separated Fourier transform and reconstructs every centered radial shell profile exactly. PC-349's rank-two area is merely the first derivative of this faithful transform.

That is a decisive boundary rather than an RH mechanism. The same reconstruction works for non-arithmetic reciprocal controls, so **raw all-depth inversion signature is source recovery, not zero selection**. Any surviving Prime-Circle route through noncommutative depth must now identify a strict source-forced quotient/invariant or growing-conductor law whose arithmetic destination is independently tied to zeta zeros and cannot be reproduced by the reciprocal control class.