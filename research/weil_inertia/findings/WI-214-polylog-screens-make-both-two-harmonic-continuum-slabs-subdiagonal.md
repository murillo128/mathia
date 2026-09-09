# WI-214 — polylogarithmic screens make both two-harmonic continuum slabs subdiagonal

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-BARRIER + CLASSICAL-IDENTITY + LITERATURE-CONTEXT`.

WI-213 proves that the exact two-pair screen of WI-211 cannot flatten the natural `1/M` continuum peak around the second reciprocal harmonic: every bounded-energy phase lift leaves a nonzero limiting profile, whose selected Gallagher energy is `Omega(log T)` above the raw-prime diagonal. That result deliberately left open unequal-depth and genuinely multi-pair continuum screens.

That escape is real. In the full two-harmonic regime `2<d<3`, an equal-depth arithmetic bow of odd population `M` admits a screen with only `4J` additional off-line functional-equation pairs such that:

1. the reciprocal samples `t=1` and `t=2` are cancelled **exactly**;
2. on every fixed natural-scale window `t=1+u/M`, the normalized residual is
   \[
   O_{h,c}(J^{-2}+\log M/M);
   \]
3. on every fixed natural-scale window `t=2+u/M`, the normalized residual is
   \[
   O_{h,c}(J^{-1}+\log M/M);
   \]
4. if `M=T^{\vartheta+o(1)}`, `J=(\log T)^{2/3+o(1)}`, and `d\vartheta<1/2`, every screening pair remains inside the critical strip, its `8J` positive-height zero labels cost `o(M)` of the local Riemann--von Mangoldt budget, and the selected residue energy on **both** corresponding source-fixed Gallagher slabs is `o` of the raw-prime diagonal.

Thus replacing the finite reciprocal packet by the two natural continuum slabs does **not** by itself turn the bow obstruction into a positive-density or defect-to-zero bootstrap. WI-213 remains correct: two pairs cannot flatten the second peak. WI-214 shows that a growing but polylogarithmic family of additional off-line pairs can flatten both reciprocal peaks strongly enough that the selected source residue is already subdiagonal. A successful bootstrap must therefore constrain the growing screen itself -- through source-specific arithmetic, a radial/count tradeoff, a growing family of independent slabs beyond this fixed pair, or another collective invariant -- rather than relying only on fixed-slab continuum coercivity.

This is a matched structural countermodel, not a claim that the constructed zeros occur for `zeta`.

## 1. Bow normalization and the midpoint exponential packet

Use the WI-210--WI-213 unfolded normalization. For odd `M`, put

\[
D_M(t)=\frac{\sin(\pi Mt)}{\sin(\pi t)},
\qquad
B_M(t)=2\cosh(ht)D_M(t),
\tag{1}
\]

with fixed `h>0`. Since `M` is odd,

\[
D_M(1)=D_M(2)=M,
\tag{2}
\]

so

\[
B_M(1)=2M\cosh h,
\qquad
B_M(2)=2M\cosh(2h).
\tag{3}
\]

Let `J=J(M)` satisfy

\[
J\to\infty,
\qquad
J=o(M/\log M).
\tag{4}
\]

Define the centered midpoint frequencies

\[
\kappa_j=\frac{j-(J+1)/2}{J},
\qquad 1\le j\le J.
\tag{5}
\]

Choose integers `n_{j,M}` symmetrically so that

\[
\left|\frac{n_{j,M}}M-\kappa_j\right|\le\frac1M,
\qquad
n_{J+1-j,M}=-n_{j,M}.
\tag{6}
\]

Because the extreme midpoint is `1/2-1/(2J)` and `M/J->infinity`, all these phase lifts fit inside the centered `M`-cell bow with a margin tending to infinity.

The ideal midpoint exponential average is

\[
A_J(u)
:=\frac1J\sum_{j=1}^J e^{2\pi i\kappa_j u}
=\frac{\sin(\pi u)}{J\sin(\pi u/J)}.
\tag{7}
\]

Hence, uniformly for `|u|<=c` with fixed `c`,

\[
A_J(u)
=\frac{\sin(\pi u)}{\pi u}+O_c(J^{-2}).
\tag{8}
\]

Replacing `\kappa_j` by `n_{j,M}/M` costs only `O_c(M^{-1})` in the normalized average. This is the only approximation-theoretic input needed below.

## 2. A first layer cancels the first harmonic and vanishes at the second

Write

\[
H:=\cosh h,
\qquad
C:=\cosh(2h).
\tag{9}
\]

Choose `a_{1,M}>0` by

\[
\boxed{
\cosh a_{1,M}=\frac{MH}{\sqrt2 J}.
}
\tag{10}
\]

For large `M` this is well-defined by (4). Define

\[
\boxed{
S^{(1)}_{M,J}(t)
=2\cosh(a_{1,M}t)
\sum_{j=1}^{J}e^{2\pi i n_{j,M}t}
\left(e^{3\pi it/4}+e^{5\pi it/4}\right).
}
\tag{11}
\]

For each `j`, the two summands in parentheses are two additional right-half-plane zeros, each already paired with its same-ordinate functional-equation mirror through the factor `2 cosh(a t)`. Thus this layer uses `2J` off-line functional-equation pairs.

At `t=1`,

\[
e^{3\pi i/4}+e^{5\pi i/4}=-\sqrt2,
\tag{12}
\]

and all integer lifts disappear. Therefore

\[
S^{(1)}_{M,J}(1)
=-2\sqrt2J\cosh a_{1,M}
=-2MH
=-B_M(1).
\tag{13}
\]

At `t=2`,

\[
e^{3\pi i/2}+e^{5\pi i/2}=0,
\tag{14}
\]

so

\[
\boxed{S^{(1)}_{M,J}(2)=0.}
\tag{15}
\]

This layer therefore cancels the first reciprocal sample exactly while leaving the second sample untouched.

On the first natural window `t=1+u/M`, the ratio

\[
\frac{\cosh(a_{1,M}(1+u/M))}{\cosh a_{1,M}}
=1+O_{h,c}(\log M/M)
\tag{16}
\]

uniformly on compact `u`-intervals. Equations (10)--(12) then give

\[
\frac{S^{(1)}_{M,J}(1+u/M)}M
=-2H A_J(u)
+O_{h,c}(\log M/M).
\tag{17}
\]

Since

\[
\frac{B_M(1+u/M)}M
=2H\frac{\sin(\pi u)}{\pi u}
+O_{h,c}(M^{-1}),
\tag{18}
\]

(8) implies

\[
\boxed{
\sup_{|u|\le c}
\frac{|B_M(1+u/M)+S^{(1)}_{M,J}(1+u/M)|}{M}
\ll_{h,c}J^{-2}+\frac{\log M}{M}.
}
\tag{19}
\]

The price paid at the second continuum window is only `O(1/J)`. Indeed, if

\[
E_1(x):=e^{3\pi i(2+x)/4}+e^{5\pi i(2+x)/4},
\tag{20}
\]

then `E_1(0)=0` and `E_1'(0)=-pi/2`, so `|E_1(x)|<<_c |x|` for `|x|<=c/M`. Also

\[
\cosh(2a_{1,M})
=\frac{M^2H^2}{J^2}-1.
\tag{21}
\]

Using only `|sum_j exp(2 pi i n_j u/M)|<=J` gives

\[
\boxed{
\sup_{|u|\le c}
\frac{|S^{(1)}_{M,J}(2+u/M)|}{M}
\ll_{h,c}J^{-1}.
}
\tag{22}
\]

More precisely the leading leakage is `-(pi H^2 u/J) A_J(u)`, but the coarse `O(J^{-1})` bound is all that is needed.

## 3. A second layer cancels the second harmonic and vanishes at the first

Choose `a_{2,M}>0` by

\[
\boxed{
\cosh(2a_{2,M})=\frac{MC}{2J}.
}
\tag{23}
\]

Define

\[
\boxed{
S^{(2)}_{M,J}(t)
=2\cosh(a_{2,M}t)
\sum_{j=1}^{J}e^{2\pi i n_{j,M}t}
\left(e^{\pi it/2}+e^{3\pi it/2}\right).
}
\tag{24}
\]

This layer uses another `2J` off-line functional-equation pairs. At `t=1`,

\[
e^{\pi i/2}+e^{3\pi i/2}=0,
\tag{25}
\]

so

\[
\boxed{S^{(2)}_{M,J}(1)=0.}
\tag{26}
\]

At `t=2`, both phases equal `-1`, and therefore

\[
S^{(2)}_{M,J}(2)
=-4J\cosh(2a_{2,M})
=-2MC
=-B_M(2).
\tag{27}
\]

Thus, with

\[
R_{M,J}(t)
:=B_M(t)+S^{(1)}_{M,J}(t)+S^{(2)}_{M,J}(t),
\tag{28}
\]

we have the **finite exact identities**

\[
\boxed{
R_{M,J}(1)=R_{M,J}(2)=0.
}
\tag{29}
\]

On the second natural window, (23)--(24) and the same midpoint calculation give

\[
\frac{S^{(2)}_{M,J}(2+u/M)}M
=-2C A_J(u)
+O_{h,c}(\log M/M).
\tag{30}
\]

Combining (8), (18) with `h` replaced by `2h`, and the leakage estimate (22),

\[
\boxed{
\sup_{|u|\le c}
\frac{|R_{M,J}(2+u/M)|}{M}
\ll_{h,c}
J^{-1}+\frac{\log M}{M}.
}
\tag{31}
\]

The second layer barely perturbs the first continuum window. Put

\[
E_2(x):=e^{\pi i(1+x)/2}+e^{3\pi i(1+x)/2}.
\tag{32}
\]

Then `E_2(0)=0` and `E_2(x)=O_c(x)`. Since (23) gives

\[
\cosh a_{2,M}=O_h(\sqrt{M/J}),
\tag{33}
\]

the sum of all `J` second-layer terms on `t=1+u/M`, after division by `M`, is

\[
O_{h,c}\!\left(\frac{\sqrt J}{M^{3/2}}\right).
\tag{34}
\]

Under (4) this is negligible compared with the right side of (19). Hence

\[
\boxed{
\sup_{|u|\le c}
\frac{|R_{M,J}(1+u/M)|}{M}
\ll_{h,c}
J^{-2}+\frac{\log M}{M}.
}
\tag{35}
\]

Equations (31) and (35) are simultaneous: the same `4J` screening pairs flatten both natural reciprocal windows while retaining exact cancellation at their centers.

## 4. Phase geometry, strip depth, and count cost

The midpoint set is symmetric, and the integer lifts in (6) can be chosen symmetrically. The first-layer phase set

\[
3\pi/4+2\pi n_{j,M},
\qquad
5\pi/4+2\pi n_{j,M},
\tag{36}
\]

and the second-layer phase set

\[
\pi/2+2\pi n_{j,M},
\qquad
3\pi/2+2\pi n_{j,M}
\tag{37}
\]

are then closed under complex conjugation after `j` is reflected. Every displayed term already contains its same-ordinate functional-equation mirror. Global negative-height conjugates can be added in the usual way outside the positive-height local interval. Thus the countermodel does not evade the compulsory reciprocal/conjugation symmetry.

The two radial scales are explicit. From (10),

\[
\boxed{
a_{1,M}=\log(M/J)+O_h(1),}
\tag{38}
\]

while (23) gives

\[
\boxed{
a_{2,M}=\frac12\log(M/J)+O_h(1).}
\tag{39}
\]

Return to height `T`, let `L=log T`, and suppose

\[
M=T^{\vartheta+o(1)},
\qquad
J=T^{o(1)}.
\tag{40}
\]

A screen pair with radial parameter `a` has right-half real part

\[
\beta=\frac12+\frac{da}{L}.
\tag{41}
\]

Hence

\[
\beta_1
=\frac12+d\vartheta+o(1),
\qquad
\beta_2
=\frac12+\frac{d\vartheta}{2}+o(1).
\tag{42}
\]

Therefore the same small-bow condition already present in WI-211,

\[
\boxed{d\vartheta<\frac12,}
\tag{43}
\]

puts both layers, and their functional-equation mirrors, strictly inside the critical strip for all sufficiently large `T`.

The screen uses `4J` functional-equation pairs, hence `8J` positive-height zero labels. WI-210--WI-212 record the count-saturating excess

\[
(d-2+o(1))M
\tag{44}
\]

available for fixed `d>2`. Thus

\[
8J=o(M)
\tag{45}
\]

costs zero asymptotic density. Existing audited zero-density bounds also do not forbid a polylogarithmic exceptional population at fixed positive horizontal depth; this construction remains a structural countermodel rather than an existence theorem for zeta zeros.

## 5. Both source-fixed Gallagher slabs become subdiagonal

WI-213 supplies the exact source dictionary term by term. For `k=1,2`, put

\[
X_k=T^{k/d},
\qquad
x_{k,M}(u)=T^{(k+u/M)/d}.
\tag{46}
\]

Then `t=d log x/L=k+u/M`, and `R_{M,J}(t)` is exactly the `x^{1/2}`-normalized selected bow-plus-screen zero-residue integrand, up to the common explicit-formula sign and twist phase.

Let

\[
\epsilon_{1,M}
:=\sup_{|u|\le c}\frac{|R_{M,J}(1+u/M)|}{M},
\qquad
\epsilon_{2,M}
:=\sup_{|u|\le c}\frac{|R_{M,J}(2+u/M)|}{M}.
\tag{47}
\]

For a fixed short natural interval length `lambda`, the same change of variables as WI-213 gives physical short lengths

\[
K_k\asymp \frac{X_kL}{dM}
\tag{48}
\]

and selected residue energies bounded by

\[
\int |Q_{k,M}(x)|^2dx
\ll_{h,c,\lambda}
\epsilon_{k,M}^2
\frac{X_k^2L^3}{d^3M}.
\tag{49}
\]

The raw-prime Gallagher diagonal at that length is

\[
X_kK_k\log X_k
\asymp_{d,k,\lambda}
\frac{X_k^2L^2}{d^2M}.
\tag{50}
\]

Consequently

\[
\boxed{
\frac{\int |Q_{k,M}|^2}
{X_kK_k\log X_k}
\ll L\epsilon_{k,M}^2.
}
\tag{51}
\]

Now take the concrete polylogarithmic screen size

\[
\boxed{J=L^{2/3+o(1)}.}
\tag{52}
\]

Because `M=T^{\vartheta+o(1)}`, the finite-`M` errors in (31) and (35) are negligible. Thus

\[
\epsilon_{1,M}=O(L^{-4/3+o(1)}),
\qquad
\epsilon_{2,M}=O(L^{-2/3+o(1)}).
\tag{53}
\]

Equation (51) yields

\[
\boxed{
\frac{\int |Q_{1,M}|^2}{X_1K_1\log X_1}
=O(L^{-5/3+o(1)})=o(1),
}
\tag{54}
\]

and

\[
\boxed{
\frac{\int |Q_{2,M}|^2}{X_2K_2\log X_2}
=O(L^{-1/3+o(1)})=o(1).
}
\tag{55}
\]

So the selected bow plus its polylogarithmic screen is not merely below the `Omega(L)` superdiagonal residual of WI-213. It is **subdiagonal on both natural reciprocal source slabs simultaneously**.

## 6. What this closes, and what remains live

WI-213 rules out the implication

\[
\text{two-pair discrete screen}
\Longrightarrow
\text{two-pair continuum screen}.
\]

WI-214 now rules out the stronger prospective bootstrap

\[
\begin{aligned}
&\text{dense off-line bow}
+\text{exact cancellation at }t=1,2\\
&\quad+\text{control of fixed natural }1/M\text{ neighborhoods of both samples}\\
&\quad+\text{functional-equation symmetry}
+\text{local zero count}
\Longrightarrow
\text{positive-density fresh defect}.
\end{aligned}
\tag{56}
\]

The conclusion is false for these inputs alone: `4J` extra pairs with `J=(log T)^{2/3+o(1)}` already make both selected source residues subdiagonal while paying `o(M)` count.

This does **not** show that the full source-fixed explicit formula can be screened. The construction is free to place a carefully engineered polylogarithmic set of off-line pairs. Zeta may impose arithmetic restrictions on those pairs that are invisible to symmetry, local counting, and the two fixed source slabs. Nor does the construction address a number of independent frequency/slab constraints growing rapidly enough with `M`, a depth-weighted coercive invariant, or a theorem coupling every deep screen to additional zeros.

The live distinction is therefore sharper than after WI-213. “Use a continuum instead of finitely many samples” is not itself sufficient. A successful defect-to-zero mechanism must make the **complexity or radial cost of the continuum screen quantitatively expensive**, or use source-specific information that prevents these phase-filter layers from being realized.

## 7. Prior-art and novelty audit

The approximation mechanism is classical harmonic analysis. The geometric-sum identity (7) is the Dirichlet-kernel formula, and `sinc(u)` is the Fourier transform of the uniform measure on `[-1/2,1/2]`. Melanie Kircheis, Daniel Potts and Manfred Tasche, *Nonuniform fast Fourier transforms with nonequispaced spatial and frequency data and fast sinc transforms*, Numerical Algorithms 92 (2023), 2307--2339, DOI `10.1007/s11075-022-01389-6`, explicitly write sinc as such a bounded-frequency Fourier integral and in Section 5 prove uniform approximation by finite positive exponential sums. WI-214 uses the simpler midpoint packet (7), whose `O(J^-2)` compact-window error follows directly from `x/sin x=1+O(x^2)`.

The indefinite finite-moment background remains the self-reciprocal/truncated-moment prior art recorded for WI-212. The new step here is not the existence of exponential-sum approximations to sinc. It is the exact coupling of two elementary phase filters to the zeta bow normalization: one `a~log(M/J)` layer cancels the first reciprocal sample and vanishes at the second, while one `a~(1/2)log(M/J)` layer does the reverse; the resulting compact-window bounds are then priced in the source-fixed Gallagher norm.

A targeted search around Alpöge--Furman/Weil-form follow-up, off-line zero screening, reciprocal harmonics, sinc/exponential-sum approximation, and continuum source localization found the classical exponential-approximation literature and the existing Mathia finite-screen context, but no source stating this zeta-specific two-layer countermodel or its subdiagonal Gallagher consequence. Absence from that search is not used as a priority claim, and no novelty claim is made.

## Research consequence

The strongest lesson is negative but useful. Fixed finite reciprocal samples are screenable by WI-212; the specific two-pair screen leaves a continuum defect by WI-213; but **both natural two-harmonic continuum slabs are again screenable once the exceptional population is allowed to grow only polylogarithmically**.

The next RH-facing route should therefore avoid spending effort merely adding denser sampling inside these same two slabs. It must instead seek a theorem that charges one of the quantities this countermodel makes large or structured: the number of independent screen pairs, their first-layer radial depth `log(M/J)`, a growing collection of genuinely independent source observables, or the full source-specific `Lambda-Lambda^sharp` covariance. Any proposed bootstrap that only sees (29), the two fixed natural windows, symmetry, and local count must first explain why the explicit screen (11), (24) is inadmissible.