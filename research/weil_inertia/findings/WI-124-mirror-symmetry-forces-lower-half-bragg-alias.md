# WI-124 — exact mirror symmetry forces a reciprocal alias at or below half support

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-RIGIDITY + PRIOR-ART-REDIRECT`. WI-123 proves that a finite-period density-one compensated cell with any off-critical horizontal displacement cannot extinguish every reciprocal-lattice harmonic below the support-one edge. The stronger deduction below uses the **full same-ordinate functional-equation mirror symmetry**, rather than only the aggregate balance `sum b_j=0`, and cuts the forced harmonic range in half:

\[
\boxed{
\text{off-line mass in a density-one }P\text{-periodic cell}
\Longrightarrow
C(m/P)\ne0
\text{ for some }1\le m\le\lfloor P/2\rfloor.
}
\]

Thus a genuinely zeta-symmetric finite-period compensator cannot push all of its deterministic Bragg leakage into the `alpha\to1` support-edge layer. At least one nonzero reciprocal alias occurs at `0<alpha<=1/2`. For a fixed cell this produces the same coherent quadratic block mass as WI-123, now safely separated from the support boundary. The result does **not** yet improve the unconditional simple-critical proportion: an embedded selected block can still be canceled by the complementary zeta amplitude before the complete BGSTB square is formed, and for growing periods the theorem is qualitative rather than a period-uniform lower bound on the alias amplitude.

## 1. Exact zeta-symmetric cell and the associated roots

Use the unfolded variables of WI-123,

\[
x=\gamma\frac{L}{2\pi},
\qquad
b=(\beta-\tfrac12)L,
\qquad
L=\log T.
\]

Fix a density-one cell of integer period `P>=2` containing exactly `P` zero labels, counted with multiplicity,

\[
(a_j,b_j),\qquad 1\le j\le P,
\]

with `a_j` understood modulo `P`. Impose the actual upper-half-plane functional-equation symmetry: whenever `(a,b)` with `b\ne0` occurs, `(a,-b)` occurs with the same multiplicity, while critical-line labels have `b=0`. This is the symmetry `rho -> 1-\bar rho`, which preserves the positive ordinate and reverses the horizontal displacement.

Define

\[
z_j:=\exp\!\left(\frac{b_j+2\pi i a_j}{P}\right),
\qquad
C(\alpha):=\sum_{j=1}^P
\exp\!\left(b_j\alpha+2\pi i a_j\alpha\right).
\]

At a reciprocal frequency `alpha=m/P`,

\[
\boxed{C(m/P)=p_m:=\sum_{j=1}^P z_j^m.}
\tag{1}
\]

The same-ordinate mirror map `b -> -b` becomes the involution

\[
\boxed{z\longmapsto\frac1{\bar z}.}
\tag{2}
\]

Hence the multiset `Z={z_1,...,z_P}` is invariant under reciprocal conjugation. In particular `|prod_j z_j|=1`, but (2) is strictly stronger than the aggregate product-modulus condition used in the proof of WI-123.

## 2. Reciprocal conjugation makes the root polynomial self-inversive

Let

\[
Q(z):=\prod_{j=1}^P(z-z_j)
=\sum_{k=0}^P(-1)^k e_k z^{P-k},
\qquad e_0=1,
\tag{3}
\]

where `e_k` is the `k`-th elementary symmetric function of the roots. Since the root multiset is invariant under (2), its elementary symmetric coefficients satisfy the exact reciprocal relation

\[
\boxed{e_{P-k}=e_P\,\overline{e_k}}
\qquad(0\le k\le P).
\tag{4}
\]

Indeed,

\[
\begin{aligned}
e_{P-k}
&=e_P
\sum_{|R|=k}\prod_{j\in R}z_j^{-1}\\
&=e_P\,\overline{
\sum_{|R|=k}\prod_{j\in R}z_j
}
=e_P\overline{e_k},
\end{aligned}
\]

because (2), after conjugation, gives equality of multisets `{z_j^{-1}}={\bar z_j}`. Taking `k=0` also gives `|e_P|=1`, equivalently the product of all root moduli is one.

Relation (4) is the standard coefficient symmetry of a monic self-inversive polynomial. It is classical polynomial theory; the line-specific point is that the **actual horizontal zeta mirror symmetry gives precisely this stronger self-inversive structure** for the reciprocal-cell variables of WI-123.

## 3. Newton--Girard plus self-inversivity halves the required harmonic range

Put

\[
q:=\left\lfloor\frac P2\right\rfloor.
\]

Assume for contradiction that every reciprocal harmonic through half support vanishes:

\[
p_1=p_2=\cdots=p_q=0.
\tag{5}
\]

Newton--Girard gives, for `1<=k<=q`,

\[
k e_k
=\sum_{m=1}^k(-1)^{m-1}e_{k-m}p_m.
\tag{6}
\]

Therefore (5) implies recursively

\[
\boxed{e_1=e_2=\cdots=e_q=0.}
\tag{7}
\]

Now apply the self-inversive relation (4). For every `1<=k<=q`,

\[
e_{P-k}=e_P\overline{e_k}=0.
\tag{8}
\]

If `P=2q+1` is odd, (7) kills `e_1,...,e_q` and (8) kills `e_{q+1},...,e_{P-1}`. If `P=2q` is even, the two ranges meet at `e_q` and again cover every interior coefficient. Thus in either parity

\[
\boxed{e_1=e_2=\cdots=e_{P-1}=0.}
\tag{9}
\]

The root polynomial collapses to

\[
Q(z)=z^P+(-1)^P e_P.
\tag{10}
\]

Since `|e_P|=1`, every root of (10) has modulus one. But from the definition of `z_j`,

\[
|z_j|=e^{b_j/P},
\]

so `|z_j|=1` for every `j` forces

\[
\boxed{b_1=\cdots=b_P=0.}
\tag{11}
\]

This contradicts the presence of off-line mass. Taking the contrapositive proves

\[
\boxed{
\exists j:\ b_j\ne0
\quad\Longrightarrow\quad
\exists m\in\{1,\ldots,\lfloor P/2\rfloor\}:\ C(m/P)\ne0.
}
\tag{12}
\]

The frequency supplied by (12) satisfies

\[
0<\frac mP\le\frac12,
\tag{13}
\]

so the forced alias is separated from the support-one endpoint by at least `1/2`. This is strictly stronger than WI-123's aggregate-balance conclusion `m<P`.

## 4. Exact equality classification

The proof also gives the sharp extinction classification under the true zeta mirror symmetry. A density-one `P`-periodic cell can satisfy

\[
C(m/P)=0
\qquad
(1\le m\le\lfloor P/2\rfloor)
\tag{14}
\]

only if every label is on the critical line. In fact (9)--(10) show more: the variables `z_j` are, with multiplicity, the complete set of `P`-th roots of the unimodular number `(-1)^{P+1}e_P`. Thus their phases are an exact rotated `P`-gon.

Conversely such an on-line rotated `P`-gon has all reciprocal harmonics `1<=m<P` equal to zero. Hence (14) has no hidden off-line equality case.

This classification is useful for near-extremal reasoning: any finite-period compensated screen with genuine horizontal defect must fail at least one of the first `floor(P/2)` power-sum constraints; there is no exact zeta-symmetric construction that stores all of its Bragg leakage arbitrarily close to `alpha=1` while annihilating the entire lower half of the support band.

## 5. Consequence for repeated compensated blocks

Repeat a fixed cell over `N` periods. At the forced reciprocal frequency `alpha=m/P`, translations by `Pn` have phase one, so exactly as in WI-123

\[
A_N(m/P)=N C(m/P)
\]

and therefore

\[
\boxed{|A_N(m/P)|^2=N^2|C(m/P)|^2.}
\tag{15}
\]

For a **fixed** off-line cell, (12) supplies a fixed `m<=P/2` and a fixed positive coefficient `|C(m/P)|^2`, so the selected block carries coherent `Theta(N^2)` spectral mass at a frequency no larger than `1/2`.

The exact Montgomery factor

\[
w(u)=\frac4{4-u^2}
\]

has the same stability on a slowly growing repeated block as in WI-123. If the total unfolded block length `M=PN` satisfies `M=o(L)`, then all pair differences are `O(M/L)`, hence `w=1+O(M^2/L^2)` and the total perturbation is `O(M^4/L^2)=o(M^2)`. For fixed `P`, `N^2\asymp M^2`, so the weighted form retains the coherent quadratic alias.

Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh prove their unconditional form-factor asymptotic uniformly for every `0<=alpha<=1`. Therefore the arithmetic interface already evaluates the whole forced range (13); no support extension or higher prime correlation is required merely to expose this alias. Their positive-square representation still leaves the same load-bearing extraction problem as WI-123: a large selected-block amplitude may be canceled by the complementary zero amplitude before the complete square is taken.

## 6. Why the stronger zeta symmetry matters

WI-123 deliberately used only

\[
\left|\prod_j z_j\right|=1.
\]

That condition alone does **not** prevent a hypothetical root polynomial from concentrating its nonzero coefficients near one end of the Newton hierarchy, so its proof only forced some `m<P`. The actual zeta mirror pairing gives the reciprocal coefficient relation (4): every vanished low-order elementary symmetric coefficient forces the corresponding high-order one to vanish as well. Once the first half of the power sums vanish, the two zero ranges meet and leave only the leading and constant coefficients.

Thus the apparent growing-period escape

\[
\text{push every deterministic alias into }\alpha=1-O(1/P)
\]

is unavailable to an exactly mirror-symmetric finite-period cell **if it also extinguishes the lower-half reciprocal harmonics**. Any proposed compensated motif that claims otherwise must violate the same-ordinate mirror symmetry, fail density one, or leave a detectable `alpha<=1/2` structure factor.

## 7. Stress tests and boundaries

The theorem is exact for multiplicities and repeated ordinates: the `z_j` form a multiset and Newton--Girard/self-inversivity require no simplicity assumption. Critical-line doubles are roots on the unit circle and cause no problem. Off-line pairs may have different depths at different ordinates; only pairwise `b,-b` symmetry at the same ordinate is used.

The result is **not quantitative uniformly in `P`**. For a sequence of growing-period cells the nonzero first-half power sum guaranteed by (12) could in principle tend to zero. Therefore WI-124 does not by itself rule out an aperiodic/growing-period compensator, nor does it prove that a positive density of embedded finite blocks forces a positive amount of complete BGSTB form-factor mass. A useful next step would need either a lower bound for a suitable aggregate of the first-half power sums in terms of horizontal defect, or a localization/coercivity inequality that prevents external cancellation.

The theorem also does not identify a nonzero reciprocal harmonic as uniquely off-line: an irregular all-critical periodic cell can have Bragg peaks too. The implication needed here is one-way. Off-line mass plus exact finite-period zeta symmetry forces a lower-half alias; absence of such aliases forces the cell into the on-line rotated-lattice equality class.

For a period `P=P(T)=o(L)`, even the smallest possible forced frequency `1/P` lies far enough above the `alpha=0` diagonal spike scale that

\[
(\log T)T^{-2/P}
=(\log T)e^{-2L/P}=o(1).
\]

Thus moving the alias toward zero does not create a new support-edge or diagonal-spike loophole in the arithmetic evaluation. What remains missing is amplitude/extraction control, not availability of the unconditional form-factor theorem.

## 8. Prior-art audit and provenance

The polynomial ingredients are classical. A root multiset invariant under `z -> 1/\bar z` defines a self-inversive polynomial, whose coefficients satisfy reciprocal-conjugate relations; see F. F. Bonsall and Morris Marden, **Zeros of self-inversive polynomials**, *Proceedings of the American Mathematical Society* 3 (1952), 471--475, DOI `10.1090/S0002-9939-1952-0047828-8`, and the classical self-inversive-polynomial literature following Cohn. Newton--Girard identities provide the standard recursion from power sums to elementary symmetric coefficients. No novelty is claimed for either ingredient.

The zeta-side arithmetic input is S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya and C. L. Turnage-Butterbaugh, **An unconditional Montgomery theorem for pair correlation of zeros of the Riemann zeta-function**, *Acta Arithmetica* 214 (2024), 357--376, arXiv:2306.04799. Their Theorem 1 states that the normalized complete form factor is real, even and nonnegative and gives its asymptotic uniformly for `0<=alpha<=1`; their Lemma 3 is the positive squared-modulus representation underlying the external-cancellation boundary.

Periodic Bragg amplification and structure-factor extinction are classical diffraction facts already audited in WI-122/WI-123. A targeted search around self-inversive polynomials, power sums, Newton identities and reciprocal-root symmetry did not locate the specific zeta-cell statement (12) or its `alpha<=1/2` consequence. Absence from that search is not evidence of priority, and no priority claim is made. The durable contribution here is the exact use of the **same-ordinate functional-equation pairing** to upgrade WI-123's product-balance Newton argument to a self-inversive one.

## 9. Research implication

WI-122 showed that number-count regularity cannot by itself extract the moving-edge signal. WI-123 then showed that every finite-period off-line compensator must leak somewhere below support one. WI-124 removes the remaining finite-period endpoint loophole: with the actual zeta mirror symmetry, the leak must already occur in the lower half of the available support band.

The two-observable program is therefore sharper. For exact finite-period compensation, no further kernel optimization near `alpha=1` is needed to **locate** a deterministic spectral witness; a forced witness exists at `alpha<=1/2`. The unresolved question is quantitative and global: convert horizontal defect into enough lower-half alias mass, and show that a positive density of such local mass cannot be neutralized by the complementary zeta amplitude while the complete unconditional form factor remains bounded. Conversely, a growing-period/aperiodic construction that makes every first-half forced alias quantitatively negligible while preserving count regularity and moving-edge screening would be a decisive obstruction to this route.