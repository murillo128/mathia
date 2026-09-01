# WI-067 — the four-prime rectangle modulus is an AP constraint, not an intrinsic growing coefficient

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + PRIOR-ART-REDIRECTION + CORRECTION`. This finding does **not** certify the Yang--Yang one-sided fourth-moment candidate, change Mathia's current unconditional simple-critical proportion, or prove the centered residue-square estimate needed by the welding argument. It corrects the fixed-polylogarithmic prior-art boundary stated in WI-066 §5 while preserving WI-066's exact and still-valid conclusion that opening the residue square raises the arithmetic correlation order to a four-prime rectangle.

WI-066 parametrized `q|r` by writing `r=qs`, producing the four forms

\[
(n,\ n+h,\ n+qs,\ n+qs+h),
\]

and then treated `q` as a growing coefficient. That representation is exact but not the right one for auditing available prime-pattern theorems. The same condition can instead be left as the congruence

\[
r\equiv0\pmod q
\]

on the **fixed-coefficient** system

\[
\boxed{
\Psi(u,v,w)=(u,\ u+v,\ u+w,\ u+v+w).
}
\tag{1}
\]

Shao--Teräväinen's Theorem 2.7 in *The Bombieri--Vinogradov theorem for nilsequences* is designed precisely for fixed finite-complexity systems evaluated on variable vectors restricted to arithmetic progressions. It therefore supplies the generic four-prime rectangle asymptotic for **almost all** conditioning moduli far beyond every fixed polylogarithmic range. Since the lossless conductor cutoff isolated in WI-058 is `X^{o(1)}`, it lies well inside the power-modulus range of that theorem. The live obstruction is consequently no longer the mere appearance of a super-polylogarithmic coefficient: it is the exact source-weighted treatment of exceptional moduli, centering/local factors, moving regions, and quantitative aggregation.

## 1. Primary theorem: linear prime patterns in progressions to large moduli

The load-bearing source is

Xuancheng Shao and Joni Teräväinen, **The Bombieri--Vinogradov theorem for nilsequences**, *Discrete Analysis* 2021:21, 55 pp., DOI `10.19086/da.29048`, arXiv:2006.05954v2, especially Theorem 2.7.

For fixed `epsilon>0` and fixed `A,t,d,M>=1`, their theorem takes

\[
Q\le x^{1/3-\varepsilon}
\tag{2}
\]

and says that, apart from

\[
\ll_{\varepsilon,A,t,d,M}\frac{Q}{(\log x)^A}
\tag{3}
\]

moduli `1<=q<=Q`, the following statement holds **for every** residue vector

\[
\mathbf a\in(\mathbb Z/q\mathbb Z)^d
\]

and every finite-complexity tuple `Psi=(L_1,...,L_t)` of nonconstant affine-linear forms of bounded size:

\[
\sum_{\mathbf m\in[1,x]^d}
\prod_{i=1}^t\Lambda\!\left(L_i(q\mathbf m+\mathbf a)\right)
=
\beta_\infty\prod_p\beta_{p,\mathbf a,q}
+o_{t,d,M}(x^d).
\tag{4}
\]

The source gives the local factors explicitly as the finite-field averages of the forms `L_i(q n+a)` and defines `beta_infty` by the positive real-volume condition. Theorem 2.7 is stronger here than the Bienvenu interface used in WI-050: the coefficients of the `L_i` remain fixed while the progression modulus `q` is allowed to grow for almost all moduli. The source itself notes that (2) corresponds to a `1/4` level of distribution in the physical prime scale because the primes being counted have size about `Qx`.

This is not an inference from a secondary summary. The exact theorem surface, including the quantifier **for every residue vector** after the exceptional modulus set is removed, is present in the published paper.

## 2. Exact reparametrization of the WI-066 rectangle

Take three variables `(u,v,w)` and the fixed system (1):

\[
L_1=u,\qquad
L_2=u+v,\qquad
L_3=u+w,\qquad
L_4=u+v+w.
\tag{5}
\]

The homogeneous coefficient vectors

\[
(1,0,0),\ (1,1,0),\ (1,0,1),\ (1,1,1)
\]

are pairwise nonproportional, so this is a fixed finite-complexity system. Its size in the sense of Shao--Teräväinen is bounded by an absolute constant, independent of `q`.

For residues `a,b mod q`, choose the variable residue vector

\[
\mathbf a=(a,b,0)\pmod q.
\tag{6}
\]

Then for `\mathbf m=(m_1,m_2,m_3)` one obtains exactly

\[
\begin{aligned}
L_1(q\mathbf m+\mathbf a)&=qm_1+a,\\
L_2(q\mathbf m+\mathbf a)&=q(m_1+m_2)+a+b,\\
L_3(q\mathbf m+\mathbf a)&=q(m_1+m_3)+a,\\
L_4(q\mathbf m+\mathbf a)&=q(m_1+m_2+m_3)+a+b.
\end{aligned}
\tag{7}
\]

If these four quantities are renamed

\[
(n,\ n+h,\ n+r,\ n+h+r),
\]

then (7) enforces

\[
\boxed{r\equiv0\pmod q}
\tag{8}
\]

without putting `q` into any coefficient of the system itself. Conversely, every triple in the corresponding progression box with `q|r` has exactly one pair `(a,b)` of residues in (6). Thus summing (4) over `a,b mod q` reconstructs the raw `q|r` four-prime rectangle aggregate in that box.

The quantifier order in Theorem 2.7 matters: for every good modulus `q`, the theorem holds simultaneously for **every** residue vector. Therefore no additional union bound over the `q^2` choices of `(a,b)` is needed to establish goodness. Summing their asymptotics multiplies both the total main scale and the uniform per-cell `o(x^3)` error by `q^2`, preserving a relative `o(1)` statement for the raw rectangle aggregate at that fixed good modulus.

This is the precise point missed by the coefficient parametrization in WI-066 §5.

## 3. The available modulus range already contains the WI-058 lossless conductor scale

Let `Y` denote the physical prime scale in one dyadic block and write

\[
Y\asymp qx.
\tag{9}
\]

Put

\[
\theta=\frac13-\varepsilon.
\]

The theorem condition `q<=x^theta` implies

\[
q\le (Y/q)^\theta,
\]

hence

\[
\boxed{
q\le Y^{\theta/(1+\theta)}
=Y^{(1-3\varepsilon)/(4-3\varepsilon)}.
}
\tag{10}
\]

As `epsilon` tends to zero this exponent tends to `1/4`. Consequently, for every fixed `eta>0`, choosing a suitable fixed `epsilon>0` gives the theorem throughout

\[
q\le Y^{1/4-\eta}
\tag{11}
\]

apart from the exceptional set (3).

WI-058 gives an asymptotically lossless deterministic `W`-local Fourier cutoff

\[
D_w=w^{3\log\log w},
\qquad
w=(\log Y)^C,
\]

so

\[
D_w
=\exp\!\bigl(O(\log\log Y\,\log\log\log Y)\bigr)
=Y^{o(1)}.
\tag{12}
\]

Therefore

\[
\boxed{D_w<Y^{1/4-\eta}}
\tag{13}
\]

for every fixed `eta>0` once `Y` is large enough. The super-polylogarithmic conductor support identified in WI-059 is thus **not by itself outside known four-prime finite-complexity technology**. It is outside Bienvenu's all-moduli fixed-log coefficient theorem, but it is well inside Shao--Teräväinen's almost-all-moduli progression theorem after the exact reparametrization (6)--(8).

This materially corrects the inference in WI-066 that the lossless conductor tail necessarily demands a new prime-pattern theorem merely because `q` appears as the coefficient in `r=qs`.

## 4. What this does and does not buy for the centered residue square

The exact identity in WI-066 remains unchanged:

\[
\sum_{a\bmod q}|\Psi_q(a;h)|^2
=
\sum_{q\mid r}\sum_n
\Lambda(n)\Lambda(n+h)\Lambda(n+r)\Lambda(n+r+h),
\tag{14}
\]

and centering still gives

\[
\sum_a|\widetilde E_q(a;h)|^2
=
\text{four-prime rectangle}
-2\,\text{conditioned pair main}
+\text{local-main square}.
\tag{15}
\]

Theorem 2.7 addresses the first, genuinely four-prime term for good `q`. It does **not** automatically prove that (15) has the small source-normalized size required by the Yang splice. Four separate gates remain load-bearing.

### 4.1 Exceptional moduli are a weighted, not merely cardinality, problem

The theorem permits the set (3) of bad moduli. The Yang/Mikawa reconstruction does not average moduli with uniform counting measure: exact conductor energies, Mertens factors, and the modulus weights isolated in WI-061--WI-065 enter the contraction. A bound

\[
|\mathcal E_Q|\ll Q(\log x)^{-A}
\]

therefore does **not** by itself imply that the exceptional contribution is negligible. One must insert the actual `W`-local conductor weights and source normalization before concluding this. In particular, the diagonal/Hilbert losses of WI-062--WI-065 cannot be silently reintroduced while discarding the exceptional set.

The positive fact is narrower: there is no longer a theorem-range obstruction on the nonexceptional `X^{o(1)}` conductors.

### 4.2 The local main must match the source centering exactly

The local factors `beta_{p,a,q}` in (4) are explicit, but the Yang route needs the centered pair-in-progression main reconstructed in WI-061/WI-064 and the four-form local model reconstructed in WI-049. An end-to-end splice must sum the residue-cell local factors from (4), separate non-reduced prime-power classes, and verify that parity/collision terms match the deterministic subtraction in (15). The existence of the prime-pattern asymptotic does not perform this bookkeeping automatically.

### 4.3 The source domain is not just one anchored cube

Theorem 2.7 is stated on `[1,x]^d` in normalized progression coordinates. The Yang source has moving intervals, sign conventions, collision hyperplanes, and cell boundaries. Prefix/dyadic decompositions strongly suggest that the bulk boxes are compatible with the theorem, but the exact source error must be written before this is promoted to a welding theorem. The collision values `r=0` and `r=±h` remain separately booked as in WI-066.

### 4.4 Quantitative aggregation still needs an audit

The printed main-term error in Theorem 2.7 is `o_{t,d,M}(x^d)`, while the exceptional-modulus count has arbitrary logarithmic saving through the parameter `A`. The Yang splice sums over several arithmetic ledgers and a growing family of dyadic/source pieces. It is not legitimate to assume that the unspecified `o(1)` rate automatically absorbs every such growing factor. Either the proof must be revisited for the required uniform quantitative rate, or the source decomposition must be organized so that only a bounded amount of asymptotic loss is needed.

These are genuine remaining proof obligations, not reasons to restore the discarded coefficient barrier.

## 5. Relation to WI-054 and the current welding frontier

WI-054 already uses Shao--Teräväinen, but through **Theorem 1.3**: a modulus-averaged nilsequence estimate controls the full Fourier fiber when one prime leg is a residual, yielding the positive-power region

\[
4\alpha+\beta<1,
\qquad
\alpha+4\beta<1.
\]

The present finding uses a different theorem and a different object. Theorem 2.7 acts after the residue square has been opened and controls the resulting **four-prime linear system** in variable-vector progressions. It therefore attacks precisely the vector/residue-summed escape left open by WI-064--WI-066, rather than duplicating WI-054's single-residual fiber estimate.

The updated decision tree is:

1. the desire for a residue `L^2` theorem still raises the correlation order from two primes to four, exactly as WI-066 proves;
2. the super-polylog conductor range is **not** an intrinsic obstacle to the generic four-prime asymptotic, because the modulus can be moved from a linear coefficient into the variable progression and Theorem 2.7 reaches all nonexceptional conductors in the required `Y^{o(1)}` range;
3. the next decisive question is whether the exceptional set and the explicit local-main subtraction can be controlled in the **actual Yang weighted contraction** without paying again the super-polylog Hilbert cost.

Thus “prove a new four-prime theorem through all `X^{o(1)}` conductors” is no longer the first obligation. The sharper target is a source-faithful weighted use of an existing almost-all-modulus four-prime theorem.

## 6. Prior-art and novelty audit

No novelty is claimed for Theorem 2.7, finite-complexity linear forms, passing from a congruence to progression coordinates, or the general principle that a growing coefficient can sometimes be absorbed into a modulus. The primary theorem is established 2021 literature and was already present in Mathia's source corpus for a different role through WI-053/WI-054.

A fresh search around linear equations in primes in large arithmetic progressions, four-prime rectangles, general-sequence BDH, and later linear-pattern work did not locate a stronger all-moduli theorem that directly supplies the centered Yang residue-square estimate with its source weights. Pandey--Woo's 2024 work on small-scale linear patterns explicitly cites Shao--Teräväinen as giving its progression-pattern asymptotic for almost all moduli up to the same `x^{1/3-epsilon}` normalized range, corroborating that Theorem 2.7 is the relevant prior-art interface; their special smooth/dutiful-modulus result is not needed here.

The durable Mathia contribution is only the program-specific correction and exact theorem bridge: WI-066's rectangle can be represented by the fixed system (1) with residue vector (6), which removes the claimed fixed-polylog **range** barrier but leaves the source-weighted centered estimate unresolved. Absence of an end-to-end theorem in the bounded literature search is not used as a novelty or priority claim.

## 7. Falsification and narrowing gates

Narrow or withdraw the program consequence if any of the following occurs.

1. Theorem 2.7 is shown not to be uniform over every residue vector after the exceptional modulus set is chosen. The printed quantifiers currently state exactly that uniformity.
2. The four-form system (5) fails the source's finite-complexity hypothesis. Its four homogeneous coefficient vectors are pairwise nonproportional, so this would require a different convention than the published one.
3. The physical Yang bulk cannot be reduced to a bounded or controllably growing family of progression boxes without an error comparable to the target covariance. Then Theorem 2.7 would remain relevant to the raw rectangle but not to the source splice.
4. The exceptional moduli can carry a non-negligible fraction of the exact weighted Yang contraction despite (3), or controlling them necessarily reintroduces the WI-062--WI-065 super-polylog cost. That would leave a genuine exceptional-set obstruction even though the generic modulus range is open.
5. The local factors from Theorem 2.7 fail to match the WI-049/WI-064 centering after reduced/non-reduced residues, parity, and collisions are fully expanded. Then the raw rectangle asymptotic would not imply the desired centered variance estimate.
6. A later theorem supplies the centered divisor-weighted rectangle directly. In that case the remaining gates should be replaced by that stronger source rather than retained as artificial proof obligations.

## 8. Consequence

The fixed-polylog conclusion of WI-066 §5 is superseded. The exact residue-square identity and the four-prime correlation-order lift in WI-066 remain valid, but the sentence

\[
\text{super-polylog conductor}\Longrightarrow\text{new four-prime arithmetic theorem required}
\]

is too strong. The correct current boundary is

\[
\boxed{
\text{generic }X^{o(1)}\text{ conductors: existing almost-all-modulus four-prime input exists;}
}
\]

\[
\boxed{
\text{remaining gate: exceptional-modulus weighting + exact centering/source splice.}
}
\]

This is a prior-art redirection rather than a new zeta bound, but it materially shortens the live Yang welding proof obligation and removes a barrier that was an artifact of the `r=qs` coordinate choice.