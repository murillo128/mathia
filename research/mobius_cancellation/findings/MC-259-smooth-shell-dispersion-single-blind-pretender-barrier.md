# MC-259 — Smooth-shell dispersion isolates at most one blind pretender but does not improve the support frontier

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `FRONTIER-REFINEMENT`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the squarefree-conductor descent of `MC-257`--`MC-258`. Let

\[
y=c\log X,
\qquad 0<c<\frac12,
\qquad
P=\prod_{p\le y}p,
\qquad
T=X-P,
\]

and let

\[
R=\prod_{y<r\le2y\atop r\ {m prime}}r,
\qquad
G=(\mathbb Z/R\mathbb Z)^\times,
\qquad
H=\langle p\bmod R:p\le y\text{ prime}\rangle.
\tag{1}
\]

Write

\[
A=H^\perp\le\widehat G,
\qquad
I=[G:H]=|A|,
\tag{2}
\]

and keep the logarithmically rough Möbius coefficient

\[
g_y(n)=\mu(n)\mathbf 1_{P^-(n)>y}.
\tag{3}
\]

`MC-258` gives the exact descended blind-source projector

\[
B^{(A)}_S(X)
=
\frac1{R|H|}
\sum_{\substack{n\le T\\-n\bmod R\in H}}g_y(n).
\tag{4}
\]

The smooth-modulus variance theorem of Klurman--Mangerel--Teräväinen (`MC-S45`, Theorem 1.3) applies unconditionally to the **shell radical `R` itself** and to the multiplicative function `g_y`. Its rank-one pretentious main term has an exact interaction with `(4)`: after summing over the target coset `-H`, the main term either vanishes identically or is carried by a **single character in the blind annihilator `A`**.

More precisely, let `chi_1 (mod R)` be a character minimizing the pretentious distance in Theorem 1.3, and put

\[
C_{\chi_1}(T)
:=
\sum_{n\le T}g_y(n)\overline{\chi_1(n)}.
\tag{5}
\]

Then for every admissible theorem parameter `epsilon`,

\[
\boxed{
B^{(A)}_S(X)
=
\mathbf 1_{\chi_1\in A}
\frac{\chi_1(-1)}{R\varphi(R)}C_{\chi_1}(T)
+
O\!\left(
\sqrt\varepsilon\,
\frac{T}{R^2}\sqrt{I}
\right).
}
\tag{6}
\]

Thus smooth-modulus dispersion compresses the structured part of the entire blind family to at most one best-pretending blind mode. If `chi_1 notin A`, the rank-one main term cancels exactly on `-H`; if `chi_1 in A`, the remaining structured obstruction is precisely one rough Möbius twist whose Dirichlet series is the reciprocal-`L` object already isolated in `MC-246`.

However, **the quantitative remainder in `(6)` cannot improve the elementary support frontier of `MC-258`**. The smoothness hypothesis in Theorem 1.3 forces

\[
\varepsilon
\ge
(\log y)^{-1/3+o(1)},
\tag{7}
\]

while `I>=1`. Consequently even the smallest theorem-scale remainder available from `(6)` is only

\[
\frac{T}{R^2}(\log y)^{-1/6+o(1)},
\tag{8}
\]

before any possible index cost `I^{1/2}`. By contrast, `MC-258` already gives the absolute support estimate

\[
|B^{(A)}_S(X)|
\ll
\frac{T}{R^2\log y}+X^{-c+o(1)}.
\tag{9}
\]

Hence the KMT variance remainder is weaker by at least a factor `(log y)^{5/6-o(1)}` even in the best case `I=1`, and it can lose a fixed power when the blind index `I` does. In particular, this prior art does not move the `R=X^{\alpha+o(1)}` support threshold `alpha=1/4` exposed in `MC-258`.

The durable frontier refinement is therefore structural rather than numerical: **after conductor descent, existing smooth-modulus dispersion says that any pretentious rank-one obstruction visible to all residue classes can intersect the exact source coset through at most one blind character, but its residual variance is too coarse to buy the missing fixed power.** A successful continuation must control that single blind pretender and/or prove a source-coset estimate whose remainder scales with the much thinner rough support, rather than merely improve generic all-residue dispersion by logarithms.

No improved estimate for `B^{(A)}_S(X)`, `M(X)`, or any zeta zero is proved here.

## 1. The shell radical satisfies the smooth-modulus hypotheses

The prime number theorem gives

\[
\log R
=
\vartheta(2y)-\vartheta(y)
=y+o(y),
\tag{10}
\]

so

\[
R=X^{c+o(1)},
\qquad
T=X(1+o(1)).
\tag{11}
\]

Every prime factor of `R` lies in `(y,2y]`, hence

\[
P^+(R)\le2y.
\tag{12}
\]

Klurman--Mangerel--Teräväinen Theorem 1.3 takes

\[
\varepsilon'=\exp(-\varepsilon^{-3})
\tag{13}
\]

and requires `R` to be `R^{epsilon'}`-smooth and `(T/R)^{epsilon^2}`-typical, with

\[
(\log(T/R))^{-1/200}\le\varepsilon\le1.
\tag{14}
\]

For a concrete admissible choice take

\[
\varepsilon_X=(\tfrac12\log y)^{-1/3}.
\tag{15}
\]

Then

\[
\varepsilon'_X=y^{-1/2},
\qquad
R^{\varepsilon'_X}
=
\exp(y^{1/2+o(1)})
\gg2y,
\tag{16}
\]

so the smoothness condition holds. Also

\[
Y:=(T/R)^{\varepsilon_X^2}
=
\exp\!\left(
\frac{(1-c+o(1))\log X}{(\tfrac12\log y)^{2/3}}
\right)
\gg y.
\tag{17}
\]

For every `z>=Y`, all prime factors of `R` are already below `z`, while

\[
\omega(R)=\pi(2y)-\pi(y)\asymp\frac y{\log y}=o(\pi(z)).
\tag{18}
\]

Thus the `Y`-typicality condition holds for sufficiently large `X`. The lower bound `(14)` is also weaker than `(15)` asymptotically. Therefore Theorem 1.3 applies to this exact deterministic shell modulus; no exceptional-modulus set is involved.

The function `g_y` is multiplicative and `1`-bounded, so it is an admissible input even though its definition depends on the current cutoff `y`.

## 2. KMT variance and annihilator orthogonality give the dichotomy

For each reduced residue `a mod R`, define

\[
F_a(T)
:=
\sum_{\substack{n\le T\\n\equiv a\pmod R}}g_y(n).
\tag{19}
\]

Theorem 1.3 gives

\[
\boxed{
\sum_{a\bmod R}^{*}
\left|
F_a(T)
-
\frac{\chi_1(a)}{\varphi(R)}C_{\chi_1}(T)
\right|^2
\ll
\varepsilon\varphi(R)\left(\frac TR\right)^2.
}
\tag{20}
\]

Write the bracketed residual as `E_a`. Equation `(4)` is exactly

\[
B^{(A)}_S(X)
=
\frac1{R|H|}
\sum_{a\in-H}F_a(T).
\tag{21}
\]

Summing the rank-one term in `(20)` over the coset gives

\[
\sum_{a\in-H}\chi_1(a)
=
\chi_1(-1)\sum_{h\in H}\chi_1(h).
\tag{22}
\]

Finite-group orthogonality on `H` yields

\[
\sum_{h\in H}\chi_1(h)
=
\begin{cases}
|H|,&\chi_1\in H^\perp=A,\\
0,&\chi_1\notin A.
\end{cases}
\tag{23}
\]

For the residual, Cauchy--Schwarz and `(20)` give

\[
\left|
\sum_{a\in-H}E_a
\right|
\le
|H|^{1/2}
\left(\sum_a^*|E_a|^2\right)^{1/2}
\ll
\sqrt{\varepsilon|H|\varphi(R)}\frac TR.
\tag{24}
\]

Dividing `(22)`--`(24)` by `R|H|` and using

\[
\frac{\varphi(R)}{|H|}=[G:H]=I
\tag{25}
\]

proves `(6)` exactly.

This is not a statement that every blind character except `chi_1` is small individually. The theorem controls their combined residue-class variance after removal of one pretentious profile. The exact point is that **only one rank-one profile can survive the coset summation as a structured main term**, and it survives only when that character is itself blind to the small-prime subgroup.

## 3. The surviving pretender is the reciprocal-`L` obstruction, not a new object

If `chi_1 in A`, then by definition

\[
\chi_1(p)=1
\qquad(p\le y\text{ prime}).
\tag{26}
\]

For `Re(s)>1`, complete multiplicativity and `(3)` give

\[
\sum_{n\ge1}
\frac{g_y(n)\overline{\chi_1(n)}}{n^s}
=
\prod_{p>y}
\left(1-\frac{\overline{\chi_1(p)}}{p^s}\right)
=
\frac1{L(s,\overline{\chi_1})}
\prod_{p\le y}(1-p^{-s})^{-1}.
\tag{27}
\]

This is exactly the single-character specialization of the full reciprocal-`L` aggregate in `MC-246`. Equation `(6)` therefore does not manufacture a new analytic route around the zero problem. It says that the all-residue pretentious structure, when projected onto the exact source coset, can leave at most one member of the already-known reciprocal-`L` obstruction.

No continuation of `(27)` to the critical strip is used here. Doing so without an independently available zero-free region would be circular under the line mandate.

## 4. The theorem parameter cannot hide a fixed-power gain

The smoothness requirement itself supplies a lower envelope for `epsilon`. Since `P^+(R) asymp y`, applicability requires

\[
2y
\le
R^{\exp(-\varepsilon^{-3})}.
\tag{28}
\]

Using `log R=y+o(y)` and taking logarithms gives

\[
\exp(-\varepsilon^{-3})
\ge
\frac{\log y+O(1)}{y+o(y)}.
\tag{29}
\]

Therefore

\[
\varepsilon^{-3}
\le
\log y-\log\log y+O(1),
\tag{30}
\]

which proves `(7)`. The explicit admissible choice `(15)` shows the same scale from the other side up to constants.

Substituting `(7)` into the error term of `(6)` shows that its best theorem-level scale is no smaller than the expression in `(8)` when `I=1`; if `I>1`, the displayed certificate only becomes weaker.

By Mertens' product theorem,

\[
\frac{\varphi(P)}P
\asymp\frac1{\log y},
\tag{31}
\]

so the direct support term of `MC-258` is `(9)`. Thus the KMT residual has a weaker logarithmic factor even before paying for blind index. In the power notation

\[
R=X^{\alpha+o(1)},
\qquad
I=X^{\delta+o(1)},
\tag{32}
\]

its displayed exponent is

\[
1-2\alpha+\frac\delta2,
\tag{33}
\]

whereas support alone has exponent `1-2alpha`. If `delta=0`, the fixed-power threshold remains `alpha=1/4`; if `delta>0`, this variance route moves the threshold in the wrong direction.

The comparison concerns the **certificate supplied by this theorem**, not the true size of the KMT residual. The actual residual may be much smaller. What is ruled out is extracting the missing fixed power merely by feeding `(20)` through Cauchy--Schwarz and the exact source coset.

## 5. Relation to `MC-188`, `MC-246`, and `MC-258`

`MC-188` applied the same KMT theorem to the small-prime primorial modulus and showed that smooth-modulus dispersion is transverse to the rough global zero mode. The present application is different in geometry but reaches a parallel obstruction. The modulus is now the **shell radical** produced by the exact prime-square conductor descent, and the quantity being projected is not the global mean over all reduced classes but one multiplicative coset determined by the small-prime subgroup.

`MC-246` identified the full blind family as the annihilator of that subgroup and exposed its reciprocal-`L` aggregate. `MC-258` then proved that the wild prime-square directions collapse, leaving the squarefree projector `(4)` but no support-exponent gain. Equation `(6)` is the natural smooth-modulus dispersion audit of this new squarefree frontier: it shows exactly how an established all-residue theorem decomposes the source coset after descent.

The result closes one obvious next move. **It is not enough to observe that `R` is an exceptionally smooth modulus and invoke the strongest available smooth-modulus variance theorem.** That theorem isolates at most one pretentious blind direction but its transverse error does not beat the already-known support estimate.

## 6. Prior art and novelty audit

The analytic theorem is established prior art: Oleksiy Klurman, Alexander P. Mangerel and Joni Teräväinen, *Multiplicative functions in short arithmetic progressions*, Proc. London Math. Soc. 127 (2023), 366--446, DOI `10.1112/plms.12546`, arXiv:`1909.12280`. Their Theorem 1.3 is precisely the smooth-modulus variance estimate `(20)`, with no exceptional moduli under the stated smoothness and typicality hypotheses. The source is already anchored as `MC-S45`.

The paper also makes clear that its smooth-modulus theorem removes one best-pretending character profile rather than controlling that profile itself. Character orthogonality on `H`, the prime-number-theorem estimate `(10)`, and Mertens' product `(31)` are classical. No novelty is claimed for any of these ingredients.

A targeted literature search around smooth-modulus multiplicative-function variance, Möbius sums in arithmetic progressions, and character/subgroup cosets found KMT as the directly applicable all-residue theorem, together with the established character-sum/subgroup literature. It did not identify a theorem giving the stronger **source-coset-scaled** remainder needed here. Absence from that search is not evidence of novelty.

The durable Mathia delta is the exact composition of KMT Theorem 1.3 with the newly descended shell projector from `MC-258`: subgroup orthogonality forces the KMT rank-one profile either to disappear on the source coset or to be one blind reciprocal-`L` mode, while the theorem's permitted parameter range proves that its residual cannot improve the existing `alpha=1/4` support frontier through the naive variance-to-coset step.

## 7. Boundaries and decisive audit

- The KMT character `chi_1` is not asserted to be principal, nonprincipal, unique, real, or blind. Equation `(6)` is a dichotomy conditional only on whether the chosen minimizing character lies in `A`.
- If several characters tie for the minimum pretentious distance, choosing a different minimizer may change which rank-one decomposition is displayed. The theorem still removes only one profile, and `(6)` remains valid for the selected minimizer.
- The remainder comparison is method-specific. It does not lower-bound the true residual and does not rule out a stronger theorem, an `L^p` refinement, a coset-targeted estimate, or source-specific cancellation inside the residual.
- The factor `I^{1/2}` is genuine in the Cauchy--Schwarz passage from all reduced classes to one `H`-coset. A theorem controlling the target coset directly could avoid it.
- The direct support bound `(9)` remains valid independently of the KMT decomposition. The fact that the KMT remainder is numerically weaker is not a contradiction; the two estimates retain different information.
- Equation `(27)` is used only in `Re(s)>1`. No zero-free continuation is imported.
- The proof assumes the shell scaling and `c<1/2` used by the current square-defect construction. Other modulus scales require a fresh applicability and rate audit.

The claim is falsified if the shell radical fails either smoothness or typicality for the stated admissible `epsilon`, if the KMT theorem does not allow the multiplicative input `g_y`, if subgroup orthogonality does not produce `(23)`, or if the normalization inherited from `MC-258` differs from `1/(R|H|)`. Each dependency is explicit.

## Consequence for the live frontier

After `MC-257`--`MC-259`, prime-square conductor complexity is no longer the immediate analytic bottleneck. The exact blind projector descends to a very smooth squarefree modulus, and the strongest directly applicable smooth-modulus variance prior art can be inserted there without an exceptional-modulus loophole. What survives is sharper:

1. at most one best-pretending blind character can carry the KMT structured main term on the source coset;
2. that character, when present, is exactly a reciprocal-`L` rough Möbius twist already known to be zero-sensitive;
3. the transverse KMT remainder is still too expensive at fixed-power scale and does not beat absolute support.

The next useful theorem surface is therefore not generic smooth-modulus equidistribution. It is either a source-coset estimate with a remainder normalized to the rough support density, a theorem excluding or controlling the distinguished blind pretender, or a signed coupling that uses the common source relation before residue-class variance is taken.