# AF-522 — Source extinction allows a continuum of anchored tail-curvature limits

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `DIRICHLET-SOURCE` · `SOURCE-EXTINCTION` · `OUTWARD-TRANSPORT` · `MATCHED-COMPOSITE-CONTROL` · `MESOSCOPIC-CURVATURE` · `NEGATIVE/OBSTRUCTION` · `NO-NOVELTY-CLAIM`

## Claim

Let

\[
P(s)=\sum_{p\in\mathbb P}p^{-s},
\qquad
\kappa_P(s)=(\log P(s))'',
\qquad s>1.
\]

For an integer cutoff `A\to\infty`, put

\[
s_A=1+\frac1A,
\qquad
L_A=\log A,
\qquad
H_A=\log L_A.
\tag{1}
\]

Choose an integer `C_A\ge2` and retain every prime `p\le A`, while moving every prime `p>A` to the ordinary composite atom `C_Ap`. The resulting simple unit-weight source has Dirichlet sum

\[
Q_A(s)
=
\sum_{p\le A}p^{-s}
+
C_A^{-s}\sum_{p>A}p^{-s}.
\tag{2}
\]

Every moved atom is distinct, composite, and strictly larger than its source prime. Thus `(2)` is an anchored outward prime-to-composite transport of exactly the type for which the source-survival hypothesis was load bearing in AF-520.

Then **source extinction by itself imposes no single limiting curvature response**. More precisely, for every

\[
\lambda\in[0,1]
\]

there exists a choice `C_A\to\infty` such that

\[
\boxed{
\frac{Q_A(s_A)}{P(s_A)}\longrightarrow0
}
\tag{3}
\]

while

\[
\boxed{
\frac{\kappa_{Q_A}(s_A)}{\kappa_P(s_A)}
\longrightarrow\lambda.
}
\tag{4}
\]

For every fixed `0<\lambda<1`, one can take

\[
c=\frac{\lambda}{1-\lambda},
\qquad
C_A\sim\frac{L_A}{cH_A},
\tag{5}
\]

with `C_A` rounded to a positive integer. In that case the extinction rate is explicitly

\[
\boxed{
\frac{Q_A(s_A)}{P(s_A)}
\sim
(1+c)\frac{H_A}{L_A},
}
\tag{6}
\]

and nevertheless `(4)` holds with limit `\lambda=c/(1+c)`.

The endpoint `\lambda=0` is obtained, for example, from `C_A=A`; it still has

\[
\frac{Q_A(s_A)}{P(s_A)}
\sim\frac{H_A}{L_A}\to0.
\tag{7}
\]

The endpoint `\lambda=1` is obtained, for example, from

\[
C_A\sim\sqrt{\frac{L_A}{H_A}},
\tag{8}
\]

for which `Q_A/P\sim\sqrt{H_A/L_A}\to0` while the relative curvature tends to one.

Consequently even inside **anchored, simple, unit-weight, ordinary-integer, outward prime-to-composite controls**, the statement

\[
Q_A(s_A)/P(s_A)\to0
\]

is not a curvature regime. For every `\lambda<1`, the controls above even share the same extinction order

\[
Q_A(s_A)/P(s_A)=\Theta(H_A/L_A)
\]

while their curvature limits fill `[0,1)`. The survival lower bound in AF-520 therefore cannot simply be replaced by an assumption that the source is "nearly extinct"; once the denominator collapses, the relative participation of higher logarithmic moments remains independent data.

## Derivation

Write the prime-prefix moments at the moving point `s_A` as

\[
B_j(A)
=
\sum_{p\le A}(\log p)^j p^{-s_A},
\qquad j=0,1,2,
\tag{9}
\]

and the full prime moments as

\[
M_j^P(s_A)
=
\sum_p(\log p)^j p^{-s_A}.
\tag{10}
\]

The classical prime-zeta boundary expansion at `s=1+1/A` gives

\[
M_0^P=L_A+O(1),
\qquad
M_1^P=A+O(1),
\qquad
M_2^P=A^2+O(1).
\tag{11}
\]

Mertens' prime estimates and partial summation give

\[
\sum_{p\le A}\frac1p
=H_A+O(1),
\qquad
\sum_{p\le A}\frac{\log p}{p}
=L_A+O(1),
\tag{12}
\]

and

\[
\sum_{p\le A}\frac{(\log p)^2}{p}
=\frac12L_A^2+O(L_A).
\tag{13}
\]

Since `A^{-1}\log p\le L_A/A=o(1)` uniformly for `p\le A`, replacing `p^{-1}` by `p^{-1-1/A}` does not alter these leading terms. Hence

\[
\boxed{
B_0\sim H_A,
\qquad
B_1\sim L_A,
\qquad
B_2\sim\frac12L_A^2.
}
\tag{14}
\]

Now put

\[
\eta_A=C_A^{-s_A},
\qquad
d_A=\log C_A.
\tag{15}
\]

Because a moved logarithmic support point changes from `\log p` to `\log p+d_A`, the first three moments of `(2)` are exactly

\[
M_0^Q
=B_0+
\eta_A(M_0^P-B_0),
\tag{16}
\]

\[
M_1^Q
=B_1+
\eta_A\bigl[(M_1^P-B_1)+d_A(M_0^P-B_0)\bigr],
\tag{17}
\]

and

\[
\begin{aligned}
M_2^Q
={}&B_2+
\eta_A\bigl[(M_2^P-B_2)
+2d_A(M_1^P-B_1)\\
&\hspace{42mm}+d_A^2(M_0^P-B_0)\bigr].
\end{aligned}
\tag{18}
\]

Define, as in AF-521,

\[
\rho_j(A)=\frac{M_j^Q(s_A)}{M_j^P(s_A)},
\qquad
r_A=
\frac{(M_1^P(s_A))^2}
{M_0^P(s_A)M_2^P(s_A)}.
\tag{19}
\]

Then

\[
r_A=\frac1{L_A}(1+o(1))
\tag{20}
\]

and the exact curvature identity is

\[
\boxed{
\frac{\kappa_{Q_A}(s_A)}{\kappa_P(s_A)}
=
\frac{
\rho_2/\rho_0-r_A(\rho_1/\rho_0)^2
}{1-r_A}.
}
\tag{21}
\]

### Interior limits `0<\lambda<1`

Fix `c>0` and choose

\[
C_A\sim\frac{L_A}{cH_A}.
\tag{22}
\]

Then

\[
\eta_A\sim c\frac{H_A}{L_A},
\qquad
d_A=O(H_A).
\tag{23}
\]

Equations `(11)`, `(14)`, and `(16)` give

\[
M_0^Q
\sim H_A+cH_A=(1+c)H_A,
\]

so

\[
\boxed{
\rho_0
\sim(1+c)\frac{H_A}{L_A}	o0.
}
\tag{24}
\]

For the first moment, the transported tail term `\eta_A M_1^P` is of order

\[
\frac{H_AA}{L_A},
\]

which dominates the prefix `B_1\asymp L_A`. The support-shift correction is negligible because

\[
\frac{d_AM_0^P}{M_1^P}
=O\!\left(\frac{H_AL_A}{A}\right)
=o(1).
\tag{25}
\]

Thus

\[
\rho_1\sim c\frac{H_A}{L_A}.
\tag{26}
\]

Similarly `\eta_AM_2^P` dominates `B_2`, while

\[
\frac{d_AM_1^P}{M_2^P}
=O(H_A/A)=o(1),
\qquad
\frac{d_A^2M_0^P}{M_2^P}
=O(H_A^2L_A/A^2)=o(1).
\tag{27}
\]

Hence

\[
\rho_2\sim c\frac{H_A}{L_A}.
\tag{28}
\]

Therefore

\[
\frac{\rho_2}{\rho_0}\to\frac{c}{1+c},
\qquad
\frac{\rho_1}{\rho_0}\to\frac{c}{1+c}.
\tag{29}
\]

The second ratio remains bounded, so `(20)` kills the first-moment square in `(21)`. Consequently

\[
\boxed{
\frac{\kappa_{Q_A}(s_A)}{\kappa_P(s_A)}
\longrightarrow
\frac{c}{1+c}.
}
\tag{30}
\]

Taking `c=\lambda/(1-\lambda)` proves every interior limit.

### Endpoint `\lambda=0`

Take `C_A=A`. Then

\[
\eta_A\sim A^{-1},
\qquad d_A=L_A.
\tag{31}
\]

Equation `(16)` gives `\rho_0\sim H_A/L_A`. Equation `(17)` gives

\[
\rho_1=O(L_A/A),
\tag{32}
\]

while `(18)` gives

\[
\rho_2=O(1/A).
\tag{33}
\]

Hence

\[
\frac{\rho_2}{\rho_0}
=O\!\left(\frac{L_A}{AH_A}\right)
\to0,
\tag{34}
\]

and

\[
r_A\left(\frac{\rho_1}{\rho_0}\right)^2
=O\!\left(\frac{L_A^3}{A^2H_A^2}\right)
\to0.
\tag{35}
\]

Equation `(21)` therefore yields the zero limit.

### Endpoint `\lambda=1`

Take

\[
C_A\sim\sqrt{\frac{L_A}{H_A}}.
\tag{36}
\]

Then

\[
\eta_A\sim\sqrt{\frac{H_A}{L_A}}
\to0,
\qquad
\frac{H_A/L_A}{\eta_A}
\to0,
\tag{37}
\]

and `d_A=O(H_A)`. Thus the transported tail dominates the prefix in all three moments, while the `d_A` corrections in `(17)`--`(18)` remain lower order exactly as in `(25)`--`(27)`. Therefore

\[
\rho_0\sim\rho_1\sim\rho_2\sim\eta_A,
\tag{38}
\]

so

\[
\frac{\rho_2}{\rho_0}\to1,
\qquad
r_A\left(\frac{\rho_1}{\rho_0}\right)^2\to0.
\tag{39}
\]

Equation `(21)` gives the unit curvature limit even though `(37)` implies source extinction.

## Fidelity and matched-control audit

These examples do not exploit arbitrary weights, nonintegral norms, inward transport, support collisions, or an unanchored global rescaling. For every `A`:

- each prime `p\le A` is retained exactly;
- every prime `p>A` is moved strictly outward;
- every target `C_Ap` is an ordinary composite integer;
- the moved targets are pairwise distinct;
- all source coefficients remain exactly one.

The effect therefore survives the strongest natural control class used in AF-520. The only new regime is the one AF-520 deliberately excluded: `Q_A/P\to0`.

The result also separates two notions that are easy to conflate. `Q_A/P\to0` says that the transformed source contributes a vanishing fraction of the **zeroth Dirichlet moment** at the chosen scale. Curvature depends on a centered second logarithmic moment. Equations `(24)`--`(29)` show that the latter can retain any prescribed fraction below one even while the zeroth moment vanishes at the common order `H_A/L_A`.

Thus "source extinction" is not itself an information-loss theorem. It names the degeneration of one coordinate of the compression. Higher moment participation can die at the same absolute rate while its ratio to that coordinate converges to different constants.

## Representation audit

For a positive Dirichlet source `S`, logarithmic curvature is the variance of `\log x` under the exponentially tilted probability law

\[
\mu_{S,s}(x)=\frac{x^{-s}}{S(s)}.
\]

That classical identity already warns that total unnormalized mass and normalized shape are different objects. AF-509 sharpened the point at the full-profile level by identifying global dilation as an exact curvature gauge for simple unit-weight sources. AF-522 is different: the prime prefix remains fixed, so the present controls are **not** global dilations of the whole source and are not removed by the AF-509 quotient classification.

Instead, the fixed prefix supplies an asymptotically vanishing zeroth-moment anchor while the transported tail controls the dominant second-log-moment scale. The continuum `(30)` is therefore a genuine moving-boundary phenomenon, not the trivial invariance `Q(s)\mapsto C^{-s}Q(s)`.

This distinction matters for the Arithmetic Fidelity program. A coordinate can approach the boundary of its parameter space without forcing the downstream observable to approach a unique boundary value. Any compression theorem that uses a vanishing normalization must identify which **relative** moment or shape coordinates remain controlled after division by that normalization.

## Prior art and novelty assessment

No novelty is claimed for the standard ingredients.

- C.-E. Fröberg, **“On the prime zeta function,”** *BIT* 8 (1968), 187--202, DOI `10.1007/BF01933420`, is the classical reference for the logarithmic singularity of `P(s)` at `s=1`; differentiation yields the moment scales in `(11)`.
- Mertens' prime theorems give `\sum_{p\le x}p^{-1}=\log\log x+O(1)` and `\sum_{p\le x}(\log p)/p=\log x+O(1)`. The second-log-moment estimate `(13)` follows immediately from the latter by partial summation. These estimates are standard; for a modern exposition see Terence Tao, **“Mertens' theorems”** (2013).
- The identity `(21)` is the exact three-moment curvature formula established in AF-521 and is itself ordinary log-partition/cumulant mathematics after normalization.
- AF-509 classifies the full-profile dilation gauge; AF-520 proves the universal two-defect law when `Q_A/P` is bounded below; AF-521 identifies the first-moment gate when that outward domination is removed.

A focused literature search found the standard prime-zeta boundary estimates, Mertens prime sums, and natural-exponential-family variance framework, but no standard theorem formulated as the continuum `(3)`--`(4)` for anchored prime-tail dilations. The durable delta is therefore recorded as an exact internal obstruction with `NO-NOVELTY-CLAIM`, not as a claim of a new theorem in analytic number theory or probability.

## Boundaries and failure modes

1. **The theorem classifies a counterfamily, not all extinct transports.** It proves that extinction does not force a unique curvature limit. It does not claim that `[0,1]` is the complete set of limits achievable by arbitrary outward or mixed transports.
2. **The observation scale is specific.** The construction uses `s_A=1+1/A`. Other couplings between cutoff and boundary distance can have different prefix-versus-tail balances.
3. **The prime prefix is retained exactly.** This is a strength of the matched control, but it also means the proof uses the Mertens-scale contribution of that prefix. Removing or changing the anchoring rule changes the balance.
4. **Only scalar curvature at one moving scale is classified.** The full function `\kappa_{Q_A}(s)`, multi-scale samples, lower-order terms, or richer marked observables can separate these controls more strongly.
5. **The first moment is lower order in this family.** AF-521 remains necessary for inward or mixed transports where `\rho_1/\rho_0` can grow at the critical `\sqrt{L_A}` scale.
6. **Extinction rate beyond order may carry information.** For fixed `0<\lambda<1`, equation `(6)` ties the leading coefficient of `H_A/L_A` to `\lambda` inside this one-parameter family. The theorem rules out extinction status and extinction order as sufficient classifiers, not every possible refined asymptotic of `\rho_0`.
7. **No rational-prime characterization follows.** All controls visibly differ from the prime source on the tail. The result is about what this curvature carrier can retain under a declared perturbation class, not an RH criterion.
8. **No RH consequence follows.** The theorem concerns an information boundary of a positive Dirichlet-source compression and says nothing about Riemann-zero locations.

## Research consequence

AF-520 left `\rho_0\to0` as a separate frontier because its two-defect law divided by a surviving source fraction. AF-521 retained that caveat after showing how inward transport can promote the first moment. AF-522 now resolves the first structural question in the extinct **outward** regime: **vanishing source mass does not select a canonical curvature behavior, even under anchored simple integer controls.**

At the cutoff-adapted scale `(1)`, the same extinction order `\Theta(H_A/L_A)` supports every limiting relative curvature in `[0,1)`, and a slightly slower still-vanishing source share reaches the endpoint `1`. Thus the next useful question is no longer whether `\rho_0\to0` alone creates a new carrier. It is which gauge-invariant or ratio-normalized moment data classify extinct transports, and whether any such classification survives richer multi-scale or arithmetic-provenance tests.