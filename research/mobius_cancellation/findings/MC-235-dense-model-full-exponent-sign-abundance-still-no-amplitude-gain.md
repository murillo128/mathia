# MC-235 — Dense-model Linnik transference gives full-exponent sign abundance but still no amplitude gain

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `FRONTIER-REFINEMENT`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-234` used the 2026 Matomäki--Teräväinen Linnik theorem only through its published least-representative conclusion. After CRT amplification this gave, for a hard source-selected progression

\[
q=X^{2\alpha+o(1)},\qquad
Z=X^{1-\beta+o(1)},\qquad
2\alpha+\beta<\frac12,
\]

and every fixed `eta>0`, the lower bound

\[
N_\Delta(Z;q,a)
\ge \frac{Z^{1/2-\eta}}q
\qquad(\Delta\in\{+1,-1\}).
\tag{1}
\]

Reading the proof rather than only the theorem statement gives substantially more. The sparse convolution used to prove Matomäki--Teräväinen's general Theorem 1.2 carries a quantitative lower bound before the final non-emptiness step. After removing its harmless sieve weight and factorization multiplicity, their proof implies the following derived counting statement.

Let

\[
L_1(m)=\max\{C,L(m)^{100},B(m)\}
\]

be the parameter used in their proof of Corollary 1.3, with `C` sufficiently large. For every sufficiently large modulus `m`, every reduced class `A mod m`, and each sign `Delta`, there are at least

\[
\boxed{
\#\{n\le m^2L_1(m):n\equiv A\pmod m,\ \mu(n)=\Delta\}
\gg
\frac{\varphi(m)L_1(m)^{99/100}}
     {L_1(m)^{o(1)}\log^2 L_1(m)}
}
\tag{2}
\]

where the `L_1(m)^{o(1)}` notation may harmlessly be absorbed into `m^{o(1)}`. In particular, since the same corollary proves

\[
L_1(m)=m^{o(1)},
\tag{3}
\]

one gets the simpler full-exponent consequence

\[
N_\Delta(m^2L_1(m);m,A)\ge m^{1-o(1)}.
\tag{4}
\]

Combining `(4)` with the same auxiliary-modulus CRT idea as `MC-234` upgrades `(1)` throughout every fixed interior hard scaling pair to

\[
\boxed{
N_\Delta(Z;q,a)
\ge
\frac Zq X^{-\eta}
}
\tag{5}
\]

for **every fixed `eta>0`** and all sufficiently large `X` (the threshold may depend on `eta,alpha,beta`). Thus neither Möbius sign can occupy only a fixed negative-power fraction of the square-free support in the source-selected hard progression. At exponent resolution, both signs already have full progression occupancy.

This closes the remaining **sign-abundance exponent gap** left by `MC-234`, but it still does not improve the exponent of the signed amplitude. The square-free support satisfies

\[
N_{\rm sf}(Z;q,a)
=\left(\frac6{\pi^2}+o(1)\right)\frac Zq,
\tag{6}
\]

whereas the sufficient componentwise target remains

\[
|M_\mu(Z;q,a)|\le X^{1/2+o(1)}.
\tag{7}
\]

Even `(5)` allows one sign to occupy only an `X^{-o(1)}` fraction of `(6)`, leaving

\[
|N_+-N_-|=X^{1-\beta-2\alpha+o(1)}
\]

at the same leading power as the unsigned support. To reach `(7)` one needs actual **near-balance**,

\[
\min(N_+,N_-)
=rac12N_{\rm sf}+O(X^{1/2+o(1)}),
\tag{8}
\]

or an aggregate cancellation mechanism across the smooth dilations of `MC-233`.

The current first-shell frontier can therefore be narrowed further: extracting merely *more representatives* from the Linnik dense-model proof cannot solve the amplitude problem. The proof already supplies each sign with full exponent. Any useful strengthening must control the **difference of the two sign masses**, not just give lower bounds for each mass separately.

No bound `(7)`, no estimate for `B_S`, no improvement of `M(X)`, and no consequence for the zeta zero set is proved here.

## 1. The quantitative mass is already present in the proof of Theorem 1.2

Kaisa Matomäki and Joni Teräväinen, *Linnik's problem for multiplicative functions*, arXiv:2605.27833v1 (27 May 2026), prove Theorem 1.2 by introducing a sparse convolution

\[
S^{\overline\Delta,\mathcal K}_{B_4,B_5,B_6}(A)
\]

whose factors have the shape

\[
n=r_1r_2r_3\,p_1\,u\,v
\le m^2Q_1.
\]

Here the three `r_i` factors carry the normalized rough-sign weights, while `p_1,u,v` provide the prime, square-free sign, and Matomäki--Radziwiłł ladder variables. Their equation (7.3) normalizes each `k`-cell by

\[
S_{\bar k}\asymp m^2Q_1.
\tag{9}
\]

Lemma 7.2 says that it is enough to obtain

\[
S^{\overline\Delta,\mathcal K}_{B_4,B_5,B_6}(A)
\gg
\frac{\varphi(m)}m
\frac{(\log m)^3}{mQ_1^{1/100}\log^2Q_1}.
\tag{10}
\]

The final case analysis proves exactly this lower bound, as equation (10.1), whenever the real-character obstruction of Theorem 1.2 is absent. The proof of their Möbius Corollary 1.3 applies Theorem 1.2 to the Liouville function with

\[
Q_1=L_1(m)=\max\{C,L(m)^{100},B(m)\}
\tag{11}
\]

and proves that the character obstruction is then impossible. Because every surviving integer in Lemma 7.2 is square-free, `lambda(n)=mu(n)` on the objects being counted, so the quantitative mass transfers from Liouville to either Möbius sign exactly as the least-representative conclusion does.

Multiplying `(10)` by the normalization `(9)` shows that the square-free part of the sparse convolution has weighted representation mass

\[
\gg
\frac{\varphi(m)Q_1^{99/100}(\log m)^3}
     {\log^2Q_1}.
\tag{12}
\]

Lemma 7.2 explicitly proves that the non-square-free contribution is little-oh of the normalized lower bound, so it does not consume `(12)`.

## 2. The convolution weight and multiplicity cost only subpower factors

The only non-unit weights in the three rough factors are

\[
w_m
=
\prod_{\substack{p<z\\p\nmid m}}
\left(1-\frac1p\right)^{-1}.
\]

By Mertens' theorem,

\[
w_m\ll\log m,
\tag{13}
\]

so one square-free factor tuple contributes at most `O((log m)^3)` to `(12)`. Removing this weight leaves at least

\[
\gg
\frac{\varphi(m)Q_1^{99/100}}{\log^2Q_1}
\tag{14}
\]

ordered square-free factor tuples.

A fixed square-free integer `n` has at most

\[
\tau_6(n)=6^{\omega(n)}=m^{o(1)}
\tag{15}
\]

ordered decompositions into the six factors used in the convolution, uniformly for `n<=m^2Q_1` because `Q_1<=m^{o(1)}` in the Möbius specialization. The `e`-adic interval indices introduce no additional fixed-power multiplicity: once a factor `r_i` is fixed, its interval index is fixed up to harmless endpoint conventions.

Dividing `(14)` by `(15)` gives `(2)`. This is an extraction from the published proof, not an additional dense-model theorem.

The distinction from the headline statement is substantial. Corollary 1.3 says that each sign occurs at least once by `m^{2+o(1)}`. Equations `(10)`--`(15)` show that the proof actually constructs `m^{1-o(1)}` distinct integers of each sign in each reduced class by that scale.

## 3. CRT amplification upgrades full exponent from the auxiliary modulus to the source progression

Return to a fixed hard source component `(q,a,Z)` and fix `eta>0`. Since `L_1(m)=m^{o(1)}`, for every fixed `rho>0` and all sufficiently large `m`,

\[
L_1(m)\ll_\rho m^\rho.
\tag{16}
\]

Choose `rho>0` sufficiently small that

\[
\frac{1-\beta}{2+\rho}-2\alpha>0
\tag{17}
\]

and

\[
(1-\beta)\frac{\rho}{2+\rho}<\frac\eta2.
\tag{18}
\]

Set

\[
R=c_\rho\frac{Z^{1/(2+\rho)}}q
\tag{19}
\]

with `c_rho>0` small enough to absorb the constant in `(16)`, and choose a prime `ell` with `R<ell<2R`. Equation `(17)` makes `ell` grow polynomially in `X`; hence for large `X` it is coprime to the logarithmic shell modulus `q`.

Put `m=q ell`. For every reduced `b mod ell`, CRT supplies a reduced class `A_b mod m` with

\[
A_b\equiv a\pmod q,
\qquad
A_b\equiv b\pmod\ell.
\tag{20}
\]

By `(16)` and the choice of `c_rho`,

\[
m^2L_1(m)\le Z.
\tag{21}
\]

Applying `(4)` to each `A_b` gives at least `m^{1-o(1)}` distinct integers of either chosen sign below `Z` in that sub-class. Different `b` give disjoint sets modulo `ell`. Therefore

\[
N_\Delta(Z;q,a)
\ge
(\ell-1)m^{1-o(1)}
=
\frac{m^{2-o(1)}}q.
\tag{22}
\]

Using `m=X^{(1-\beta)/(2+\rho)+o(1)}` gives

\[
N_\Delta(Z;q,a)
\ge
\frac{Z^{2/(2+\rho)}}q X^{-o(1)}
=
\frac Zq
X^{-(1-\beta)\rho/(2+\rho)-o(1)}.
\tag{23}
\]

Equations `(18)` and `(23)` prove `(5)` after absorbing the remaining `o(1)` into `eta/2`.

This argument uses only the strict interior hard condition. If `1/2-2alpha-beta` tends to zero with `X`, the fixed-parameter choice of `rho` and the uniformity thresholds of the Linnik theorem must be re-audited.

## 4. Full-exponent sign abundance still leaves the signed amplitude at the trivial power

Combining `(5)` with `(6)` yields, for every fixed `eta>0`,

\[
\frac{N_\Delta(Z;q,a)}{N_{\rm sf}(Z;q,a)}
\ge X^{-\eta+o(1)}.
\tag{24}
\]

Thus neither sign can be polynomially rarer than the square-free support. This is much stronger than the black-box consequence `(1)`, whose relative density was only `Z^{-1/2+o(1)}`.

But lower bounds on the two masses do not control their difference. Even if

\[
\min(N_+,N_-)=N_{\rm sf}X^{-o(1)},
\]

one may still have

\[
|N_+-N_-|
=N_{\rm sf}\bigl(1-X^{-o(1)}\bigr)
=X^{1-\beta-2\alpha+o(1)}.
\tag{25}
\]

That is the same leading power as the trivial unsigned bound. The target `(7)` instead asks for relative discrepancy

\[
\frac{|N_+-N_-|}{N_{\rm sf}}
\le
X^{-(1/2-2\alpha-\beta)+o(1)},
\tag{26}
\]

which is a fundamentally different output.

Consequently, the useful information still hidden in the dense-model architecture, if any, cannot merely be a stronger lower bound for the number of positive and negative representatives. It must preserve enough **signed comparison** between the two dense models to control `(26)`, or it must reveal cancellation when the `X^{o(1)}` smooth-dilation components of `MC-233` are recombined before triangle inequality.

## 5. Prior-art and novelty boundary

The dense-model theorem, the sparse convolution, the normalization `(9)`, the threshold `(10)`, and the Möbius choice `(11)` are all from Matomäki--Teräväinen, arXiv:2605.27833v1. Their stated result is a least-sign representative theorem, not the count `(2)`. The count here is obtained by retaining the quantitative lower bound already present in their proof and dividing only by the explicit sieve weight and the elementary divisor-function representation multiplicity.

A targeted literature check found no stated all-modulus theorem in this sign-change line giving the near-balanced Möbius counts required by `(26)`. Klurman--Mangerel--Teräväinen's earlier *Multiplicative functions in short arithmetic progressions* gives variance/average-distribution results for almost all moduli, which is a different quantifier surface from the source-selected individual progression here. No literature-absence or novelty claim is made for `(2)` or `(5)`; they are recorded as proof-level consequences useful for locating Mathia's remaining information barrier.

## 6. Boundaries and falsification tests

- The extraction `(2)` depends on the quantitative lower bound actually proved inside Theorem 1.2, not merely on Corollary 1.3 as a black box. If a later revision changes the normalization or the non-square-free error, the count must be rechecked.
- The `m^{o(1)}` representation loss uses only the elementary maximum-order bound for fixed divisor functions and the fact that the construction has six multiplicative factors. It does not assume random or unique factorization of the tuple.
- The passage from Liouville to Möbius is valid because Lemma 7.2 discards non-square-free outputs and `lambda(n)=mu(n)` for square-free `n`; it is not a statement that the two functions agree on all integers.
- The CRT amplification is fixed-parameter and interior. It makes no uniform claim at the moving support boundary `2alpha+beta=1/2`.
- Equation `(5)` is a lower bound on each unsigned sign population, not a discrepancy estimate. It cannot be inserted into `(N_+-N_-)` with a favorable sign without additional structure.
- The result concerns the sufficient componentwise progression surface exposed by `MC-233`. Aggregate cancellation across smooth dilations remains a separate possible escape and is not ruled out.

## Consequence for the live frontier

The recent Linnik dense-model machinery is stronger than `MC-234` could see from its theorem statement: throughout the fixed interior hard CRT region it already forces **both Möbius signs at essentially the full occupancy exponent**. The obstruction is therefore not lack of representatives, not parity existence, and not even polynomial sparsity of one sign.

The unresolved object is now sharply the **signed discrepancy**. Any continuation of this route should ask whether the proof contains a relation between the positive and negative dense models that survives transference strongly enough to bound `N_+-N_-`, rather than trying to improve separate lower bounds for `N_+` and `N_-`. If no such comparative invariant survives, the only remaining first-shell escape visible here is cancellation across the smooth-dilation family before the componentwise triangle inequality.