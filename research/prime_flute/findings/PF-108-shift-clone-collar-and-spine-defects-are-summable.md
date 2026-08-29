# PF-108 — shift-clone collar and spine defects are summable

**Status:** `EXACT-DERIVED + BOUNDARY`. This refines PF-107 and the accepted relative-operator clue. Although the all-composite shift clone has a non-`ell^1` additive defect in the long distinguished cuff lengths, the associated **absolute standard-collar widths**, canonical tight-pants seam/spine distances, standard-collar areas, and an explicit unweighted collar metric-distortion integral are summable. No global quasiconformal, resolvent, Schatten, wave, or scattering theorem is claimed.

## Claim

Write

\[
u(x)=\cot\frac{\pi}{x},\qquad F(x)=\log u(x),\qquad \delta(x)=F(x+1)-F(x).
\]

For consecutive odd primes let

\[
h_n=F(p_n)-F(p_{n-1}),\qquad
h_n^+=F(p_n+1)-F(p_{n-1}+1),
\]

where `+` denotes the exact all-composite shift clone `p_n -> p_n+1` of PF-106/PF-107. PF-032 gives the exact standard collar half-width

\[
w_n=\frac{h_n}{2},\qquad w_n^+=\frac{h_n^+}{2},
\]

and PF-026/PF-032 give the canonical common-perpendicular / spine distance across the one-cusp tight pair of pants

\[
d_n=\frac{h_n+h_{n+1}}2,
\qquad
d_n^+=\frac{h_n^++h_{n+1}^+}2.
\]

Then, from any fixed tail index `m`,

\[
\boxed{
\sum_{n=m}^{\infty}|w_n-w_n^+|
=\frac12\,\delta(p_{m-1})<\infty,
}
\tag{1}
\]

and

\[
\boxed{
\sum_{n=m}^{\infty}|d_n-d_n^+|
=\frac12\bigl(\delta(p_{m-1})+\delta(p_m)\bigr)<\infty.
}
\tag{2}
\]

Thus the logarithmic relative collar-width defect found in PF-107 is not an additive divergence of the transverse collar geometry: the actual shrinking widths and the canonical transverse seam distances differ by an exact `ell^1` sequence.

Moreover, if `A_n` and `A_n^+` are the areas of the full standard collars around the matched cuffs, then

\[
\boxed{
\sum_n |A_n-A_n^+|<\infty.
}
\tag{3}
\]

Finally there is an explicit collar-by-collar comparison whose logarithmic metric distortion is integrable with respect to hyperbolic area over the union of the standard collars. This is a genuine partial step toward the metric-deviation question in the accepted operator clue, but it is **unweighted and only on the collars**; it does not verify the Güneysu--Thalmaier criterion on the complete surface.

## 1. Exact telescoping of the collar-width defect

The shift identity is exact:

\[
h_n^+-h_n
=\delta(p_n)-\delta(p_{n-1}),
\]

so

\[
\boxed{
h_n-h_n^+=\delta(p_{n-1})-\delta(p_n).}
\tag{4}
\]

For `x>2`,

\[
F'(x)=\frac{2\pi}{x^2\sin(2\pi/x)}.
\]

Put `y=2*pi/x`. Apart from the positive constant `1/(2*pi)`, this is `y^2/sin y`. Its derivative with respect to `y` has the sign of

\[
2\sin y-y\cos y,
\]

which is positive for `0<y<pi`. Since `y` decreases with `x`, `F'(x)` is strictly decreasing on `x>2`. Therefore

\[
\delta(x)=\int_x^{x+1}F'(t)\,dt
\]

is positive and strictly decreasing to zero.

It follows that every term in (4) is positive and that finite sums telescope:

\[
\sum_{n=m}^{N}(h_n-h_n^+)
=\delta(p_{m-1})-\delta(p_N).
\]

Taking `N -> infinity` and using `w=h/2` proves (1) exactly. No prime-gap estimate is needed for this summability statement.

This resolves a specific ambiguity left by PF-107. That finding proved

\[
\log\frac{w_n^+}{w_n}=-\frac1{p_{n-1}}+o(p_{n-1}^{-1}),
\]

whose absolute sum diverges. Equation (1) shows that the divergence is purely **multiplicative/logarithmic**: because the collars themselves shrink, their absolute transverse displacement has finite total mass.

## 2. The canonical tight-pants seam/spine defect also telescopes

The standard one-cusp tight-pants identity already recorded in PF-032 is

\[
d_n=w_n+w_{n+1}
=\frac12(h_n+h_{n+1})
=\frac12\log\frac{u(p_{n+1})}{u(p_{n-1})}.
\]

It is classical right-angled-hexagon/collar geometry, not a new prime-specific identity. For the shift clone,

\[
d_n^+-d_n
=\frac12\left(\delta(p_{n+1})-\delta(p_{n-1})\right).
\]

Since `delta` is decreasing,

\[
|d_n-d_n^+|
=\frac12\left(\delta(p_{n-1})-\delta(p_{n+1})\right).
\]

Hence

\[
\sum_{n=m}^{N}|d_n-d_n^+|
=\frac12\left(
\delta(p_{m-1})+\delta(p_m)
-\delta(p_N)-\delta(p_{N+1})
\right),
\]

which proves (2).

Using PF-107's asymptotics, or differentiating `delta(x)=x^{-1}+O(x^{-2})`, one also obtains

\[
\boxed{
 d_n-d_n^+
=\frac{p_{n+1}-p_{n-1}}{2p_n^2}(1+o(1))
=\frac{g_{n-1}+g_n}{2p_n^2}(1+o(1)).
}
\tag{5}
\]

The exact telescoping proof is stronger than this asymptotic: summability does not depend on a conjectural prime-gap bound.

## 3. Standard-collar area defects are summable

For a cuff of length `ell` with standard half-width `w`, the full embedded collar has area

\[
A=2\ell\sinh w.
\]

Here `ell=Lambda(h)=2 log coth(h/4)` and `w=h/2`, so define

\[
A(h)=2\Lambda(h)\sinh(h/2).
\]

PF-107 records

\[
\Lambda'(h)=-\frac1{\sinh(h/2)}.
\]

Therefore the derivative simplifies exactly to

\[
\boxed{
A'(h)=\Lambda(h)\cosh(h/2)-2.
}
\tag{6}
\]

As `h -> 0`, this is `O(log(1/h))`. For consecutive primes `a=p_{n-1}`, `b=p_n=a+g`, PF-107 gives

\[
h=\frac ga(1+o(1)),
\qquad
h-h^+=\frac{g}{a^2}(1+o(1)).
\]

Consequently the mean-value theorem and (6) give

\[
|A_n-A_n^+|
=O\left(\frac{g\log a}{a^2}\right).
\tag{7}
\]

The unconditional Baker--Harman--Pintz bound `g=O(a^0.525)` used already in PF-107 makes the right-hand side summable over the prime index (indeed it is `O(a^-1.475 log a)`, and `p_n >= n+1`). This proves (3).

Thus even though the **circumference** defect `ell_n^+-ell_n ~ 2/p_{n-1}` is not in `ell^1`, the area carried by the corresponding standard thin collars changes by an `ell^1` amount.

## 4. An explicit finite unweighted metric-distortion integral on the collars

Use standard collar coordinates with `theta in R/Z`:

\[
g_n=dr^2+\ell_n^2\cosh^2(r)\,d\theta^2,
\qquad |r|<w_n.
\]

Let

\[
q_n=\frac{w_n^+}{w_n}=\frac{h_n^+}{h_n}
\]

and map the prime collar to the clone collar by

\[
T_n(r,\theta)=(q_n r,\theta).
\]

Then

\[
T_n^*g_n^+
=q_n^2dr^2
+(\ell_n^+)^2\cosh^2(q_n r)\,d\theta^2.
\]

Define the collar logarithmic distortion

\[
\kappa_n=
\sup_{|r|\le w_n}
\max\left\{
|2\log q_n|,
\left|2\log\frac{\ell_n^+}{\ell_n}
+2\log\frac{\cosh(q_n r)}{\cosh r}\right|
\right\}.
\]

PF-107 gives

\[
\log q_n=-\frac1a+o(a^{-1}),
\qquad
\log\frac{\ell_n^+}{\ell_n}
=O\left(\frac1{a\log a}\right).
\]

Since `w_n=h_n/2 -> 0`, the `cosh` term is `O(|q_n-1|w_n^2)`. Hence

\[
\boxed{\kappa_n=O(a^{-1}).}
\tag{8}
\]

Also

\[
A_n=2\ell_n\sinh w_n
=O\left(\frac{g\log a}{a}\right).
\]

Combining this with (8) and the same unconditional prime-gap bound yields

\[
\boxed{
\sum_n \kappa_n A_n<\infty.
}
\tag{9}
\]

Equation (9) is a concrete metric statement on a two-dimensional subset of the surface: under the explicit collar maps, the logarithmic distortion is `L^1` with respect to hyperbolic area on the union of all standard distinguished-cuff collars.

It is deliberately **not** identified with a relative-Laplacian theorem. The Güneysu--Thalmaier scattering criterion discussed in the accepted clue uses a global common-manifold comparison and, under its Ricci formulation, a weight involving inverse unit-ball volume. Equation (9) supplies neither the maps on the remaining pants/cusp regions nor the required volume weight.

## 5. Consequence for the operator-class clue

PF-107 exposed a genuine amplification:

\[
\ell^1\text{ endpoint defect}
\not\Rightarrow
\ell^1\text{ additive cuff-circumference defect}.
\]

PF-108 shows that this amplification does **not** propagate uniformly through the thin geometry:

\[
\boxed{
\begin{array}{c}
\text{cuff circumference defect}\in\ell^2\setminus\ell^1,\\[2mm]
\text{absolute collar-width defect}\in\ell^1,\\
\text{canonical seam/spine defect}\in\ell^1,\\
\text{standard-collar area defect}\in\ell^1,\\
\text{unweighted integrated collar log-distortion}<\infty.
\end{array}}
\]

This makes the surviving operator question sharper. A failure of relative compactness/Schatten control cannot be inferred merely from the harmonic additive cuff defect. Any obstruction must survive after the compensating shrinkage of the collars and seams is taken into account. Conversely, the positive collar estimates still do not control the complete pants cores, cusp neighborhoods, unit-ball-volume weights, or the global quotient identification.

## 6. Prior art / novelty audit

The ingredients are standard:

- the tight one-cusp pants identity `d_n=c(alpha_n)+c(alpha_{n+1})` and the standard collar function are established hyperbolic geometry; Basmajian--Hakobyan--Saric use exactly these quantities in their type analysis;
- the standard collar metric `dr^2+ell^2 cosh^2(r)dtheta^2` and its area formula are classical;
- PF-032 already proved that the prime logarithmic mesh is exactly twice the standard collar half-width, so no novelty is claimed for `d_n=(h_n+h_{n+1})/2` itself;
- PF-107 already supplies the needed shift-clone cuff and logarithmic-width asymptotics and the Baker--Harman--Pintz input;
- the accepted clue records Minsky's unbounded-cuff local pants comparison and Güneysu--Thalmaier's weighted metric-deviation scattering criterion.

Directed searches did not locate the specific `p_n -> p_n+1` all-composite comparison or the exact telescoping laws (1)--(2). The durable project contribution is therefore the combination of the shift-clone deformation with the universal collar/seam identities, which proves that several intrinsic **transverse and area-weighted** defects are summable even though the additive cuff-circumference defect is not.

This is not claimed as a new theorem about general infinite-type hyperbolic surfaces, and it is not evidence for RH.

## 7. Audit / falsification core

The reusable checks are:

1. differentiate `F(x)=log cot(pi/x)` and verify that `F'` is decreasing for `x>2`, hence `delta(x)=F(x+1)-F(x)` decreases to zero;
2. verify the exact coboundary identity `h_n-h_n^+=delta(p_{n-1})-delta(p_n)`;
3. combine it with the already-established exact identities `w_n=h_n/2` and `d_n=(h_n+h_{n+1})/2` to obtain the finite telescoping sums (1)--(2);
4. differentiate `A(h)=2 Lambda(h)sinh(h/2)` and verify (6);
5. use the PF-107 asymptotics to obtain the area estimate (7) and collar distortion estimate (8);
6. use only the unconditional gap bound already admitted in PF-107 to justify the convergent series in (3) and (9);
7. do **not** promote (9) to wave equivalence, compact resolvent difference, Schatten class, scattering equivalence, or an RH statement without a global common-manifold map and the hypotheses of the relevant operator theorem.

A refutation would need to break one of the exact identities in steps 1--4 or the asymptotic/summability estimates in steps 5--6. The main remaining research task is outside this finding: control (or obstruct) the complement of the standard collars and the weighted global metric-deviation integral.

## References

- A. Basmajian, H. Hakobyan, D. Saric, *The type problem for Riemann surfaces via Fenchel-Nielsen parameters*, Proc. London Math. Soc. 125 (2022), 568--625.
- H. A. Minsky, *Bounded geometry for Kleinian groups*, Invent. Math. 146 (2001), 143--192, DOI `10.1007/s002220100163`.
- B. Güneysu, A. Thalmaier, *Scattering theory without injectivity radius assumptions, and spectral stability for the Ricci flow*, Ann. Inst. Fourier 70 (2020), 437--456, DOI `10.5802/aif.3316`.
- R. C. Baker, G. Harman, J. Pintz, *The difference between consecutive primes, II*, Proc. London Math. Soc. 83 (2001), 532--562, DOI `10.1112/plms/83.3.532`.
- PF-026, PF-032, PF-106 and PF-107 in this research ledger.
