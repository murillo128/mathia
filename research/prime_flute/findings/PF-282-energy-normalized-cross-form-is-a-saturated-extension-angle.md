# PF-282 — energy-normalized mixed coupling is a saturated extension-angle operator

**Status:** `EXACT-DERIVED + CLOSED-OPERATOR-BOUNDED-TRANSFORM + EXTENSION-ANGLE-FACTORIZATION + POSITIVE/ROUTE-NARROWING`.

[[research/prime_flute/findings/PF-279-variable-scalar-schur-reservoirs-can-erase-local-corridor-cut-gain|PF-279]] shows that an unprojected cut can lose a favorable local transmission scale because endpoint-normalized extensions accumulate large reservoir mass. [[research/prime_flute/findings/PF-281-energy-normalized-cross-form-removes-bounded-frequency-coupling-gate|PF-281]] then identifies the physically relevant object after the `P/H` split: the diagonal-energy-normalized cross form

\[
T=A^{-1/2}(PKH)_{\rm form}C^{-1/2},
\]

and proves that `T\in\mathcal S_{1,\infty}` is sufficient for the mixed inverse block and reciprocal-prime coefficient commutator to be weak trace class.

There is an exact structural bridge between these two results. Factor the nonnegative precision form through its canonical energy map and restrict that map to the physical low/high sectors. After the same diagonal energy normalization already forced by PF-281, the two restricted extension maps become contractions `Z_P,Z_H`, and

\[
\boxed{T=Z_P^*Z_H.}
\]

Thus `T` is literally a **regularized cross-Gram operator** of the physical low- and high-fed extensions. Writing the polar decompositions of the unnormalized extension maps gives the sharper factorization

\[
\boxed{
T=f(|R_P|)\,\Gamma\,f(|R_H|),
\qquad
f(t)=\frac{t}{\sqrt{1+t^2}},
\qquad
\Gamma=V_P^*V_H.
}
\]

The two outer factors measure extension strength and saturate at one; `\Gamma` measures the relative angle/correlation of the two extension ranges in the common energy space. This is the operator-valued reservoir interface missing after PF-279: large extension mass cannot amplify the PF-281 normalized cross form beyond the contraction scale, but it can remove amplitude damping because `f(t)\to1`. On such reservoir-heavy channels, compactness and every symmetric-ideal property of `T` are equivalent, up to fixed constants, to the same property of the corresponding compression of `\Gamma`.

More precisely, if

\[
E_P^\mu=\mathbf1_{[\mu,\infty)}(|R_P|),
\qquad
E_H^\mu=\mathbf1_{[\mu,\infty)}(|R_H|),
\]

and

\[
\Gamma_\mu=E_P^\mu\Gamma E_H^\mu,
\qquad
T_\mu=E_P^\mu T E_H^\mu,
\]

then for every singular value

\[
\boxed{
f(\mu)^2s_j(\Gamma_\mu)
\le s_j(T_\mu)
\le s_j(\Gamma_\mu).}
\]

Consequently `T` is compact **if and only if** `\Gamma_\mu` is compact for every `\mu>0`. A global estimate `\Gamma\in\mathcal S_{1,\infty}` is a sufficient, reservoir-proof route to PF-281's weak-trace target, although it is stronger than necessary because the outer strength factors may themselves contribute decay on weak-extension channels.

This does not prove the prime-flute weak-trace theorem. It identifies exactly what an actual-PF reservoir can still do after the physically correct normalization: it can push both strength factors into their saturated regime, but then any surviving noncompactness or heavy-sector ideal failure must be carried by **persistent overlap between low-fed and high-fed pant extensions**, not by extension mass alone.

## Claim

Let

\[
\mathcal H=\mathcal H_P\oplus\mathcal H_H
\]

with orthogonal projections `P,H`, and let `k` be a densely defined closed nonnegative form on `\mathcal H`, with associated self-adjoint operator `K\ge0`. Assume, exactly as in PF-281, that `P,H` preserve `\operatorname{Dom}k` and that the two diagonal restrictions of `k` are closed.

Let

\[
R:=K^{1/2}:\operatorname{Dom}k\longrightarrow\mathcal H
\tag{1}
\]

be the canonical energy map and define its closed restrictions

\[
R_P:=R\big|_{P\operatorname{Dom}k},
\qquad
R_H:=R\big|_{H\operatorname{Dom}k}.
\tag{2}
\]

Let the shifted diagonal energy operators be

\[
A:=I+R_P^*R_P\ge I,
\qquad
C:=I+R_H^*R_H\ge I.
\tag{3}
\]

Define the bounded transforms

\[
\boxed{
Z_P:=R_PA^{-1/2},
\qquad
Z_H:=R_HC^{-1/2}.}
\tag{4}
\]

Then:

1. `Z_P,Z_H` are contractions and the PF-281 normalized cross form is exactly
   \[
   \boxed{T=Z_P^*Z_H.}
   \tag{5}
   \]
2. their input Gram operators are
   \[
   \boxed{
   Z_P^*Z_P=I-A^{-1},
   \qquad
   Z_H^*Z_H=I-C^{-1}.}
   \tag{6}
   \]
3. if
   \[
   R_P=V_P|R_P|,
   \qquad
   R_H=V_H|R_H|
   \tag{7}
   \]
   are polar decompositions and
   \[
   \Gamma:=V_P^*V_H,\qquad
   f(t):=\frac{t}{\sqrt{1+t^2}},
   \tag{8}
   \]
   then
   \[
   \boxed{
   Z_P=V_Pf(|R_P|),
   \qquad
   Z_H=V_Hf(|R_H|),}
   \tag{9}
   \]
   and therefore
   \[
   \boxed{
   T=f(|R_P|)\Gamma f(|R_H|).}
   \tag{10}
   \]
4. for every `\mu>0`, with
   \[
   E_P^\mu=\mathbf1_{[\mu,\infty)}(|R_P|),
   \qquad
   E_H^\mu=\mathbf1_{[\mu,\infty)}(|R_H|),
   \tag{11}
   \]
   and
   \[
   T_\mu:=E_P^\mu T E_H^\mu,
   \qquad
   \Gamma_\mu:=E_P^\mu\Gamma E_H^\mu,
   \tag{12}
   \]
   one has
   \[
   \boxed{
   f(\mu)^2s_j(\Gamma_\mu)
   \le s_j(T_\mu)
   \le s_j(\Gamma_\mu)
   \qquad(j\ge1).}
   \tag{13}
   \]
   Hence, on every fixed reservoir-heavy sector, `T_\mu` and `\Gamma_\mu` belong to exactly the same compact two-sided symmetric ideals.
5. the full normalized cross form satisfies the exact compactness criterion
   \[
   \boxed{
   T\text{ is compact}
   \iff
   \Gamma_\mu\text{ is compact for every }\mu>0.}
   \tag{14}
   \]
6. for every compact two-sided symmetric ideal `\mathcal J`,
   \[
   \boxed{
   \Gamma\in\mathcal J
   \Longrightarrow
   T\in\mathcal J.}
   \tag{15}
   \]
   In particular,
   \[
   \boxed{
   \Gamma\in\mathcal S_{1,\infty}
   \Longrightarrow
   T\in\mathcal S_{1,\infty}.}
   \tag{16}
   \]

Statement (16) is a sufficient criterion, not a necessary one. Weak extension-strength channels can make `T` smaller than `\Gamma`; the equivalence becomes exact only after fixing `\mu>0` as in (13).

## 1. The PF-281 cross form is exactly a regularized extension Gram

For `p\in P\operatorname{Dom}k` and `h\in H\operatorname{Dom}k`, the canonical form representation gives

\[
k[p,h]
=\langle Rp,Rh\rangle
=\langle R_Pp,R_Hh\rangle.
\tag{17}
\]

The diagonal restrictions are closed, so their shifted forms have the associated operators (3). The standard closed-operator bounded transform gives

\[
\|R_P(I+R_P^*R_P)^{-1/2}\|\le1,
\qquad
\|R_H(I+R_H^*R_H)^{-1/2}\|\le1,
\tag{18}
\]

which proves that (4) are bounded contractions.

For arbitrary `x\in\mathcal H_P` and `y\in\mathcal H_H`, equation (17) yields

\[
\begin{aligned}
\langle x,Z_P^*Z_Hy\rangle
&=\langle R_PA^{-1/2}x,R_HC^{-1/2}y\rangle\\
&=k[A^{-1/2}x,C^{-1/2}y].
\end{aligned}
\tag{19}
\]

But PF-281 defines `T` as the unique bounded operator representing exactly this energy-normalized cross form. Hence (5) follows by uniqueness.

The Gram identities are equally direct. Since `A=I+R_P^*R_P`, functional calculus gives

\[
\begin{aligned}
Z_P^*Z_P
&=A^{-1/2}R_P^*R_PA^{-1/2}\\
&=A^{-1/2}(A-I)A^{-1/2}\\
&=I-A^{-1},
\end{aligned}
\tag{20}
\]

and the same argument gives the `H` identity in (6).

Thus the diagonal objects in PF-281 have a precise extension interpretation. `A-I` and `C-I` are the unnormalized extension Grams, while `I-A^{-1}` and `I-C^{-1}` are their bounded, shifted energy-normalized versions. The cross object `T` is the corresponding normalized cross Gram.

## 2. Polar decomposition separates strength from range angle

From (7),

\[
R_P=V_P|R_P|,
\qquad
A=I+|R_P|^2.
\tag{21}
\]

Therefore

\[
Z_P
=V_P|R_P|(I+|R_P|^2)^{-1/2}
=V_Pf(|R_P|),
\tag{22}
\]

and similarly for `Z_H`. Substitution into (5) proves (10).

The contraction

\[
\Gamma=V_P^*V_H
\tag{23}
\]

contains no extension-strength factor. It records only how the closures of the two extension ranges sit relative to one another in the common energy space. In the compact/discrete case its nonzero singular values are the usual cosines of principal angles between those ranges; in the general infinite-dimensional case (23) is the corresponding two-subspace correlation operator.

This separates the two effects that PF-279 leaves entangled in a scalar cut norm:

- `f(|R_P|)` and `f(|R_H|)` record how strongly the two physical sectors extend into the reservoir;
- `\Gamma` records whether the resulting extension directions actually overlap.

The scalar function has the exact limits

\[
f(t)=t+O(t^3)\quad(t\downarrow0),
\qquad
f(t)=1-\frac1{2t^2}+O(t^{-4})\quad(t\to\infty).
\tag{24}
\]

Hence weak extension channels are damped, but arbitrarily large reservoir mass does not produce arbitrarily large normalized coupling. It merely drives the corresponding strength factor toward one. Once both sides are saturated, the angle operator is what remains.

This formulation is independent of whether one realizes the nonnegative form through the canonical map `K^{1/2}` or through a minimal geometric energy-extension factorization. Two minimal factorizations of the same form are related by an isometry on the closed energy range; the two polar range maps are transported by the same isometry, so the cross operator `V_P^*V_H` is unchanged up to the canonical identification. For the prime flute one may therefore use the harmonic-extension realization without changing the invariant represented by (10).

## 3. Reservoir-heavy channels are ideal-equivalent to the angle operator

Because `f` is increasing and bounded by one, on the range of `E_P^\mu` one has

\[
f(\mu)E_P^\mu
\le f(|R_P|)E_P^\mu
\le E_P^\mu,
\tag{25}
\]

with the analogous inequality on the `H` side. Since the spectral projections commute with their own strength functions,

\[
T_\mu
=f(|R_P|)\Gamma_\mu f(|R_H|).
\tag{26}
\]

The ordinary two-sided singular-value inequality immediately gives

\[
s_j(T_\mu)\le s_j(\Gamma_\mu).
\tag{27}
\]

On the two heavy spectral subspaces the strength factors are boundedly invertible with inverse norm at most `f(\mu)^{-1}`. Thus

\[
\Gamma_\mu
=f(|R_P|)^{-1}T_\mu f(|R_H|)^{-1}
\tag{28}
\]

on those subspaces, and another singular-value inequality gives

\[
s_j(\Gamma_\mu)
\le f(\mu)^{-2}s_j(T_\mu).
\tag{29}
\]

Equations (27)--(29) are exactly (13).

The point is stronger than an operator-norm comparison. Any compact two-sided symmetric ideal sees `T_\mu` and `\Gamma_\mu` as the same object up to constants depending only on the chosen threshold. A reservoir with enormous diagonal energy cannot hide an ideal failure on a channel where both extension strengths stay above `\mu`; after normalization it can only saturate the outer factors.

## 4. Exact compactness criterion: weak-strength channels can be truncated in norm

Suppose first that `T` is compact. Every compression `T_\mu` is compact, and equation (28) expresses `\Gamma_\mu` as bounded left/right multiplication of `T_\mu`. Therefore every `\Gamma_\mu` is compact.

Conversely suppose that `\Gamma_\mu` is compact for every `\mu>0`. Then (26) shows that every `T_\mu` is compact. Moreover

\[
T-T_\mu
=(I-E_P^\mu)T
+E_P^\mu T(I-E_H^\mu).
\tag{30}
\]

The first term contains the factor

\[
(I-E_P^\mu)f(|R_P|)
\]

whose norm is at most `f(\mu)`, and the second term contains

\[
f(|R_H|)(I-E_H^\mu)
\]

with the same bound. Since `\|\Gamma\|\le1`,

\[
\boxed{
\|T-T_\mu\|
\le2f(\mu)
\longrightarrow0
\qquad(\mu\downarrow0).}
\tag{31}
\]

Thus `T` is a norm limit of compact operators, proving (14).

Equation (31) is an exact boundary on the reservoir problem. **Noncompactness cannot be supported only on channels whose extension strength tends to zero.** If the PF-281 cross form is noncompact, then for at least one fixed positive extension threshold the corresponding low/high extension-angle compression is already noncompact.

The same argument does not by itself give a weak-`S_1` equivalence for the full unthresholded operator. Weak Schatten quasi-norms are sensitive to how the thresholds are populated as `\mu\downarrow0`. For the endpoint problem one still needs either a global ideal estimate on `\Gamma`, or a quantitative decomposition combining heavy-channel angle control with the population/strength distribution of the weak channels.

## 5. PF-281's noncompact falsifier is a pure saturated-angle obstruction

PF-281 uses the direct-sum blocks

\[
K_j=(j-1)
\begin{pmatrix}1&1\\1&1\end{pmatrix},
\qquad j\ge2,
\tag{32}
\]

for which

\[
A_j=C_j=j,
\qquad
T_j=\frac{j-1}{j}\longrightarrow1.
\tag{33}
\]

In the present factorization, the `P` and `H` restrictions of the energy map have the same one-dimensional range and equal strength

\[
|R_{P,j}|=|R_{H,j}|=\sqrt{j-1}.
\tag{34}
\]

Hence

\[
\Gamma_j=1
\tag{35}
\]

and

\[
f(\sqrt{j-1})^2
=\frac{j-1}{j},
\tag{36}
\]

so (10) reproduces (33) exactly. The counterexample is therefore not a mysterious Schur amplification after normalization. It is the limiting regime in which both extension-strength factors saturate and the low/high extension ranges are perfectly aligned.

That calibration matters for the actual PF problem. A negative construction for the physical cross form must preserve a nonvanishing low/high extension angle on channels whose two normalized strengths do not disappear. Merely making the pant reservoir large is insufficient after PF-281 normalization.

## 6. Specialization to the simultaneous prime-flute precision

For the simultaneous seam decomposition of PF-211--PF-214, write

\[
K_{PF}
=\Lambda_Q^{-1/2}\Lambda_E\Lambda_Q^{-1/2}\ge0,
\qquad
D=(I+K_{PF})^{-1}.
\tag{37}
\]

The exterior DtN form can be realized as the energy of the minimizing shifted-harmonic extensions into the disjoint one-cusp pant cores. After the `\Lambda_Q^{-1/2}` normalization, this gives a geometric factorization of the form of `K_{PF}` through the direct sum of pant-core energy spaces. Under the PF-281 form-domain hypotheses for the physical `P/H` split, let

\[
R_P^{PF},\qquad R_H^{PF}
\tag{38}
\]

be the corresponding low-fed and high-fed normalized extension maps.

Then the complete physical cross form appearing in PF-281 is not an additional unknown operator. It is exactly

\[
\boxed{
T_{PF}
=Z_P^{PF*}Z_H^{PF}
=f(|R_P^{PF}|)\Gamma_{PF}f(|R_H^{PF}|),}
\tag{39}
\]

where

\[
\Gamma_{PF}=V_P^{PF*}V_H^{PF}.
\tag{40}
\]

This sharpens the live theorem in two complementary ways.

First, a direct estimate

\[
\Gamma_{PF}\in\mathcal S_{1,\infty}
\tag{41}
\]

would immediately imply PF-281's desired `T_{PF}\in\mathcal S_{1,\infty}` and hence the mixed Schur/commutator endpoint. Such a theorem would be **reservoir-proof**: arbitrary same-sector extension strength has already been absorbed into contraction factors.

Second, (41) may be stronger than necessary. The physically optimal theorem may combine an estimate of the heavy compressions

\[
E_P^\mu\Gamma_{PF}E_H^\mu
\tag{42}
\]

with quantitative control of how many low/high channels have weak extension strength as `\mu\downarrow0`. PF-210's threshold-counting philosophy and PF-212's physical-frequency population estimates are natural currencies for that second part, but no such endpoint summation is asserted here.

This also refines the accepted reservoir clue. PF-279's scalar `\beta'` identifies raw endpoint extension mass as a quantity that a local transmission coefficient alone misses. In the completed physical `P/H` problem, PF-282 shows how that information is reorganized by the normalization actually used in PF-281: the diagonal extension Grams become bounded strength filters, while the decisive cross datum is the angle between the two extension ranges. The remaining question is therefore geometric/spectral: **how much of a physical high-frequency pant extension can lie in the same energy directions as a physical low-frequency extension after all actual pant completion and neighboring-cell coupling are retained?**

## 7. Prior art and novelty audit

No novelty is claimed for the abstract operator-theoretic ingredients.

The bounded transform

\[
R(I+R^*R)^{-1/2}
\]

of a closed operator is standard; see K. Schmüdgen, *Unbounded Self-adjoint Operators on Hilbert Space*, Graduate Texts in Mathematics 265, Springer (2012), Section 7.3, DOI `10.1007/978-94-007-4753-1`.

Z. Tarcsay and Z. Sebestyén, *Canonical Graph Contractions of Linear Relations on Hilbert Spaces*, **Complex Analysis and Operator Theory 15** (2021), article 21, DOI `10.1007/s11785-020-01066-3`, develop the canonical graph contractions and record the standard resolvent/Gram identities underlying (6). The classical two-subspace angle framework goes back at least to P. R. Halmos, *Two Subspaces*, **Transactions of the American Mathematical Society 144** (1969), 381--389, DOI `10.1090/S0002-9947-1969-0251519-5`.

The polar decomposition, singular-value inequalities under bounded two-sided multiplication, and symmetric-ideal stability are standard operator theory. A targeted audit did not identify a need to import any nonstandard theorem into the proof above: (5), (10), (13), and (14) follow directly from those classical tools.

The durable project-specific contribution is therefore not a claim of new general operator theory. It is the exact identification of **PF-281's physical normalized cross form** with the regularized cross Gram of the low/high pant extensions, together with the reservoir-heavy equivalence (13) and compactness criterion (14). These statements convert PF-279's reservoir warning into a falsifiable PF geometry target without reintroducing the raw unbounded cross block that PF-281 removed.

## 8. Falsification and boundary checks

1. The factorization requires the same PF-281 assumptions: the physical `P/H` projections preserve the full form domain and the two diagonal restrictions are closed. PF-282 does not prove those geometric domain facts if they have not already been established in the concrete realization.
2. `\Gamma\in\mathcal S_{1,\infty}` is only a sufficient global criterion. Failure of that criterion does not imply failure of `T\in\mathcal S_{1,\infty}` because weak extension-strength factors may supply additional singular-value decay.
3. Equation (14) is an exact **compactness** criterion, not a weak-trace criterion. One cannot let `\mu\downarrow0` in the fixed-threshold ideal equivalence without controlling the population of the newly admitted channels.
4. The two-subspace interpretation concerns the common energy range after the actual physical extension maps are fixed. A coordinate change that also changes the physical projectors cannot manufacture or remove the relevant angle while pretending `P/H` stayed fixed.
5. PF-279 remains valid as an unprojected scalar matched control. PF-282 explains what survives after PF-281 normalization; it does not retroactively bound the raw scalar cut or its `\beta'` factors.
6. PF-227's raw high--high channel multiplicity remains relevant. A large physical high sector is harmless only if its normalized extension directions become sufficiently transverse to the low-fed range or if the strength/population factors supply the missing ideal decay.
7. Nothing here proves weak trace class of the global first relative resolvent, closes the independent short-collar splice, establishes wave operators/determinants/resonances, separates primes from the all-composite shift clone, or implies RH.

## Consequence for the research line

The next discriminating calculation should no longer ask for an abstract bound on reservoir size alone. Construct the actual simultaneous pant-extension realization of the physical `P/H` split and estimate the cross-range operator

\[
\Gamma_{PF}=V_P^{PF*}V_H^{PF}.
\tag{43}
\]

The strongest clean target is `\Gamma_{PF}\in\mathcal S_{1,\infty}`. If that is too strong, fix a positive extension threshold `\mu`, estimate the heavy compression `\Gamma_{PF,\mu}`, and combine those estimates with the strength/frequency population as `\mu\downarrow0`. A noncompact heavy compression would kill the current sufficient route immediately; a weak-`S_1` heavy-angle estimate with a summable/threshold-controlled weak-strength remainder would close PF-281's remaining mixed-frequency reservoir gate.