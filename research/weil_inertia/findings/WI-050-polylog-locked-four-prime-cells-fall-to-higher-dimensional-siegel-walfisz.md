# WI-050 — polylogarithmic locked four-prime cells fall to higher-dimensional Siegel--Walfisz

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + PRIOR-ART-REDIRECTION`. This finding does **not** certify the Yang--Yang one-sided fourth-moment candidate and does not change Mathia's current unconditional simple-critical proportion. It narrows the joint-prime obstruction isolated by WI-043/WI-049: on the asymptotically dominant coprime base family, every fixed polylogarithmic coefficient regime `b1,b2 <= (log X)^B` can be treated directly as a finite-complexity system of four affine-linear prime forms in three variables. Pierre-Yves Bienvenu's higher-dimensional Siegel--Walfisz theorem then gives the expected four-prime asymptotic uniformly on the source convex welding region, including polylogarithmically thin regions. Combined with WI-049's exact local-factor centering, the genuine post-four-form-local-main residual is `o(1)` after source normalization on this whole regime.

Accordingly, the unresolved welding problem is not intrinsically a four-prime/twin-prime obstruction. After the lock is summed rather than frozen, the Yang square is a nondegenerate three-variable linear-forms problem. The remaining analytic difficulty begins when the reduced coefficients leave every fixed polylogarithmic range, exactly where Bienvenu's theorem no longer applies and where WI-039/WI-040 located the power-sized coefficient wall. Any leading post-local-main locked covariance must therefore be carried by that super-polylogarithmic coefficient regime or by separately booked collision/boundary terms.

## 1. Exact unsliced Yang object

The pinned public source remains

`JoshuaHKU/zeta-0.7947-reproduction@d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8`.

Its exact dispersion swap starts from

\[
A(b_2,j)=\sum_m \Lambda(m)\Lambda(n),
\qquad
b_1n-b_2m=j,
\qquad 0<|j|\le J,
\tag{1}
\]

and, after squaring and equating the two locks, writes

\[
m'=m-rk,
\qquad
n'=n-qk,
\qquad
r=\frac{b_1}{(b_1,b_2)},
\qquad
q=\frac{b_2}{(b_1,b_2)}.
\tag{2}
\]

This is not an inferred parametrization: it is the exact `S1` loop in `scripts/t2_swaps.py`, and WI-043 already reconstructed the same identity from the source.

On the dominant coprime prime-power base family identified in WI-045--WI-049, `(b1,b2)=1`, hence `r=b1`, `q=b2`. Summing the lock `j` rather than conditioning on one lock turns the off-diagonal `S1` object into

\[
\sum_{(m,n,k)\in \mathbf Z^3\cap K_{b_1,b_2}(X)}
\Lambda(m)\Lambda(m-b_1k)
\Lambda(n)\Lambda(n-b_2k),
\tag{3}
\]

up to the source's explicitly separated hyperplanes `k=0` and `j=0`. Here `K_{b1,b2}(X)` is cut out by the original `m,n` windows, the translated-window constraints for `m-b1 k` and `n-b2 k`, and

\[
|b_1n-b_2m|\le J.
\tag{4}
\]

Before deleting `k=0` and `j=0`, all these conditions are linear inequalities. Thus `K_{b1,b2}(X)` is a convex body. The paper's own notation has macroscopic windows `Y \asymp X`, lock width `J \asymp X`, and shift range `K \asymp Y/\max(b_1,b_2)` on the coprime family.

## 2. The four prime forms have finite complexity

Define the homogeneous system in variables `(m,n,k)`

\[
\Psi_{b_1,b_2}(m,n,k)
=
\bigl(
 m,
 m-b_1k,
 n,
 n-b_2k
\bigr).
\tag{5}
\]

Its coefficient vectors are

\[
(1,0,0),
\quad (1,0,-b_1),
\quad (0,1,0),
\quad (0,1,-b_2).
\tag{6}
\]

For positive `b1,b2`, no two are rational multiples. Hence no two forms are affinely related and the system has finite complexity in the Green--Tao/Bienvenu sense.

It is also admissible for every prime `p`. Indeed, modulo `p`, choosing

\[
k=0,
\qquad m=n=1
\tag{7}
\]

makes all four forms nonzero. Therefore every local factor `beta_p` is nonzero. This remains true even when `p` divides one of the coefficients.

This is the key structural point: fixing `k` leaves two binary shifted-prime problems, but **averaging over `k` together with `m,n` raises the dimension and makes the full four-form system nondegenerate**. The hard binary character is an artifact of slicing the finite-complexity system along the shift coordinate.

## 3. Bienvenu applies uniformly for polylogarithmic coefficients

Bienvenu, *A higher-dimensional Siegel--Walfisz theorem*, Acta Arith. 179 (2017), Theorem 1.3, proves the following unconditional form. For fixed `d,t,A,B,L`, if an admissible affine-linear system `Psi : Z^d -> Z^t` satisfies

\[
\|\Psi\|_{N,B}\le L,
\tag{8}
\]

so in particular its linear coefficients are `O((log N)^B)`, and if `K subset [-N,N]^d` is convex with

\[
\operatorname{Vol}(K)\gg N^d(\log N)^{-A},
\tag{9}
\]

then

\[
\sum_{x\in\mathbf Z^d\cap K}
\prod_{i=1}^t\Lambda(\psi_i(x))
=
\operatorname{Vol}(K)
\prod_p\beta_p\,(1+o_{d,t,A,B,L}(1)).
\tag{10}
\]

The `o(1)` is uniform over systems and convex bodies satisfying the displayed fixed-parameter hypotheses. Bienvenu's theorem is precisely the extension of the Green--Tao--Ziegler finite-complexity prime-pattern theorem from bounded linear coefficients to coefficients growing as a fixed power of `log N`.

Now fix any constant `B0` and restrict the Yang coprime family to

\[
b_1,b_2\le (\log X)^{B_0}.
\tag{11}
\]

All source coordinates are `O(X)`, so take Bienvenu's ambient parameter `N=CX` for a fixed source-dependent constant `C`. Equations (5)--(6) then give `||Psi||_{N,B}=O(1)` for a fixed `B=O(B0)`.

The exact source geometry is still thick enough after the translated-window constraints are imposed. Write the source `m` window as `I_m=[s_0X/b_2,s_1X/b_2]`, up to harmless integer endpoints, and choose a fixed central subinterval `I_m^*` of length `c_mX/b_2`. For sufficiently small fixed `c_k>0`, restrict

\[
c_k\frac{X}{b_1b_2}\le k\le 2c_k\frac{X}{b_1b_2}.
\]

Then `b_1k=O(X/b_2)`, so both `m` and `m'=m-b_1k` remain in the same interior source window. This one-sided choice also stays away from the deleted hyperplane `k=0`.

Use the lock coordinate

\[
j=b_1n-b_2m.
\]

Choose a fixed one-sided interior slab `c_jX\le j\le2c_jX` with `2c_jX<J` and `c_j` small relative to the fixed source margins. For each admissible `m`, this gives an `n` interval of length `c_jX/b_1`. After shrinking the fixed constants if necessary it lies inside the source `n` range. Moreover

\[
b_1(n-b_2k)-b_2(m-b_1k)=b_1n-b_2m=j,
\]

so the translated lock is preserved exactly; since `b_2k=O(X/b_1)`, the same interior margins keep `n'=n-b_2k` in the translated `n` window. The choice `j>0` avoids the deleted hyperplane `j=0`.

Hence the exact source region contains a convex subbody whose widths, measured directly in `(m,n,k)`, are

\[
\asymp \frac{X}{b_2},\qquad
\asymp \frac{X}{b_1},\qquad
\asymp \frac{X}{b_1b_2}.
\]

Therefore

\[
\operatorname{Vol}(K_{b_1,b_2}(X))
\gg
\frac{X^3}{b_1^2b_2^2}
\ge X^3(\log X)^{-4B_0}.
\tag{12}
\]

Thus Bienvenu's volume hypothesis (9) holds with a fixed exponent `A=4B0+O(1)` uniformly throughout (11).

The source deletions `k=0` and `j=b1 n-b2 m=0` lie on codimension-one lattice hyperplanes. Their von-Mangoldt-weighted contribution is at most `N^2 log^{O(1)}N`, hence is `o(Vol(K) prod_p beta_p)` in the fixed-polylogarithmic regime. Equivalently one may split the sign components into finitely many convex bodies. These deletions therefore do not obstruct (10).

## 4. Bienvenu's local factor is exactly the source `E2` factor

Let

\[
\Lambda_p(a)=\frac{p}{p-1}\,1_{p\nmid a}.
\tag{13}
\]

For (5), Bienvenu's local factor is

\[
\beta_p
=
\mathbb E_{m,n,k\bmod p}
\Lambda_p(m)\Lambda_p(m-b_1k)
\Lambda_p(n)\Lambda_p(n-b_2k).
\tag{14}
\]

Condition on `k`. The `m` and `n` averages factor exactly, so

\[
\beta_p
=
\mathbb E_{k\bmod p}
\tau_p(b_1k)\tau_p(b_2k),
\tag{15}
\]

where

\[
\tau_p(h)
=
\begin{cases}
\dfrac{p}{p-1},&p\mid h,\\[2mm]
\dfrac{p(p-2)}{(p-1)^2},&p\nmid h.
\end{cases}
\tag{16}
\]

Equation (15) is exactly the local second-moment factor used by the Yang `S3` model and derived in WI-045/WI-048. Hence

\[
\boxed{
\prod_p\beta_p=E_2(b_1,b_2)
}
\tag{17}
\]

on the coprime family, with the source's parity and coefficient-prime cases already included in the local average.

Therefore Bienvenu gives, uniformly for (11),

\[
\boxed{
S_1(b_1,b_2)
=
\operatorname{Vol}(K_{b_1,b_2}(X))
E_2(b_1,b_2)\,(1+o(1)).
}
\tag{18}
\]

No twin-prime conjecture, four-prime Hardy--Littlewood conjecture, MRT dispersion estimate, or new large-modulus theorem is needed in this coefficient range.

## 5. The genuine cellwise four-form residual is lower order here

Equation (18) initially identifies the main after summing the lock and shift variables. WI-049 supplies the missing bridge to the **cellwise genuine four-form** model. For each fixed cell lock `j`, WI-049 proved prime by prime that the true four-form local factor is an autocorrelation and that

\[
\frac1p\sum_{k\bmod p}\sigma_{4,p}(k;j)=\kappa_p(j)^2.
\tag{19}
\]

It then proved uniform finite-conductor interval discrepancy `O((log P)^4)` and an `o(1)` normalized passage to the full Euler product over the actual Yang shift/lock aggregation. Consequently the source-weighted sum of the true cellwise four-form mains has the same leading term as the right-hand side of (18):

\[
\sum_{k,j} \mathfrak S_4(k,j)V(k,j)
=
\operatorname{Vol}(K)E_2(b_1,b_2)+o(\operatorname{Vol}(K)E_2).
\tag{20}
\]

Subtracting (20) from (18) yields the durable conclusion

\[
\boxed{
\sum_{k,j}
\bigl(N_4(k,j)-\mathfrak S_4(k,j)V(k,j)\bigr)
=
o\!\left(\operatorname{Vol}(K)E_2(b_1,b_2)\right)
}
\tag{21}
\]

uniformly for every fixed polylogarithmic range (11). Summing over all prime-power pairs in that range preserves the `o(1)` because Bienvenu's error is uniform and the main terms are nonnegative.

Thus the post-four-form-local-main prime residual targeted by `CLUE-yang-locked-covariance-leading-scale` is already asymptotically suppressed on this entire regime.

## 6. What remains genuinely open

This result does **not** close the Yang--Yang one-sided fourth-moment route. The source middle band contains reduced coefficients that are positive powers of the main scale. Bienvenu's norm condition permits

\[
\max(b_1,b_2)\le (\log X)^B
\tag{22}
\]

for an arbitrary but fixed `B`; it does not cover

\[
\max(b_1,b_2)=X^{\delta}
\tag{23}
\]

for fixed `delta>0`, nor does it provide a theorem uniform through the full power-sized coefficient family.

WI-039 and WI-040 had already shown that the public welding geometry genuinely carries such power-sized reduced coefficients and that unimodular reparametrization cannot make all of them bounded. The present finding sharpens the interpretation of that wall:

\[
\boxed{
\text{the missing ingredient is coefficient-uniform finite-complexity prime control,}
\quad
\text{not four-prime complexity itself.}
}
\tag{24}
\]

If a normalized leading post-local-main covariance survives in the full source aggregation, then for every fixed `B` its leading mass must eventually come from cells with `max(r,q)>(log X)^B`, apart from collision/analytic pieces already booked separately. This is a support statement about where the obstruction can live, not a proof that such a leading term exists.

## 7. Prior-art and novelty audit

Primary established source:

- Pierre-Yves Bienvenu, **A higher-dimensional Siegel--Walfisz theorem**, *Acta Arithmetica* 179 (2017), 79--100, DOI `10.4064/aa8600-10-2016`, arXiv:1607.06625. Theorem 1.3 is the load-bearing input: admissible finite-complexity systems with polylogarithmic linear coefficients, convex bodies of volume at least `N^d log^{-A}N`, and a uniform singular-series asymptotic.

Classical lineage:

- Ben Green and Terence Tao, **Linear equations in primes**, *Annals of Mathematics* 171 (2010), 1753--1850, DOI `10.4007/annals.2010.171.1753`, together with the later Green--Tao--Ziegler resolution of the inverse-Gowers inputs. This is the bounded-coefficient finite-complexity framework extended by Bienvenu.

A bounded literature audit also checked recent small-scale linear-pattern work. Pandey--Woo studies small boxes for finite-complexity prime systems but does not supply a general unconditional extension from polylogarithmic to power-sized growing coefficients. No theorem located in the Yang/MRT/Green--Tao chain gives the required uniform asymptotic for the full `X^delta` coefficient family. This absence is **not** a novelty or impossibility claim.

The finite-complexity observation itself is classical once the system (5) is written down. No priority is claimed for applying Bienvenu to this Yang subfamily. The Mathia contribution recorded here is the source-specific audit:

1. undo the fixed-shift slice and identify the exact Yang `S1` square as the three-variable system (5);
2. verify finite complexity, admissibility, polylog-volume thickness, and the exact source local factor (17);
3. combine the established Bienvenu asymptotic with WI-049's full cellwise local-main centering;
4. thereby move the unresolved covariance target from “all four-prime cells” to the super-polylogarithmic coefficient regime.

## 8. Decisive verification / falsification gate

Narrow or retire this finding if any of the following fails under exact source normalization.

1. The off-diagonal `S1` sum for fixed coprime `(b1,b2)` is not representable, after only codimension-one deletions, by the convex three-variable domain (3)--(4).
2. A source window in the fixed-polylog coefficient regime carrying non-negligible normalized mass has convex-body volume smaller than `N^3 log^{-A}N` for every fixed `A`.
3. Bienvenu's Theorem 1.3 has an additional hypothesis not satisfied by (5), despite finite complexity, admissibility, coefficient size and positivity.
4. The local factor (14) does not coincide with the source `E2` local factor after the exact parity/coefficient-prime conventions are restored.
5. WI-049's cellwise-to-aggregate Euler passage is corrected in a way that permits a leading deterministic bias even in the polylogarithmic regime.

Conversely, extending (21) to `b_i <= X^delta` for any fixed `delta>0` by an established theorem or a new exact argument would materially advance the one-sided fourth-moment audit, because it would move the coefficient wall into a smaller source region.

## 9. Consequence for `weil_inertia`

The shortest current question is no longer whether a generic locked four-prime residual can be controlled at all. It can, unconditionally, whenever its source coefficients are polylogarithmic. The open interface is now

\[
\boxed{
\text{finite-complexity four-prime pattern}
+
\text{power-sized moving coefficients}
\longrightarrow ?
}
\tag{25}
\]

This is a materially narrower target than WI-043. It also explains why the source's fixed-shift MRT slicing looked harder than the unsliced object: slicing a finite-complexity three-variable system produces binary shifted-prime correlations and discards exactly the averaging variable that Green--Tao/Bienvenu technology exploits.