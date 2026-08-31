# WI-051 — complexity-one Fourier control does not remove the Yang coefficient wall

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECTION`. This finding does **not** certify the Yang--Yang one-sided fourth-moment candidate and does not change Mathia's current unconditional simple-critical proportion. It closes a tempting shortcut left open by WI-039/WI-050: the unsliced Yang four-prime system is in fact Cauchy--Schwarz complexity exactly one, so on a single finite field its multilinear average is controlled by ordinary Fourier/`U^2` uniformity with no dependence on the sizes of `r,q`. However, that coefficient-free statement does not survive the localization needed at the Yang physical scales. On the natural anisotropic groups, the maps `k -> r k` and `k -> q k` land in proper subgroups of indices `r,q`; quotient modes then remain perfectly coherent under every allowed shift. An explicit bounded mean-zero quadratic-phase example forces any `U^2`-only localized estimate to lose at least a positive power of the coefficient index.

Thus the super-polylogarithmic obstruction isolated in WI-039/WI-050 is **not a higher-Gowers-order obstruction**. It is a localization/modulus obstruction: globally the system is Fourier-complexity one but the relevant cells are polynomially sparse, while at natural local scale the missing density reappears as large-index sublattice aliasing. Any successful repair must control those quotient modes arithmetically after the genuine local main is removed, or bypass them with a direct joint four-prime estimate.

## 1. Exact Yang system and its Cauchy--Schwarz complexity

The pinned public Yang source remains

`JoshuaHKU/zeta-0.7947-reproduction@d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8`.

WI-039, WI-043 and WI-050 reconstruct its off-diagonal equal-lock system as

\[
L_1=m,
\qquad
L_2=m-rk,
\qquad
L_3=n,
\qquad
L_4=n-qk,
\tag{1}
\]

where

\[
r=\frac{b_1}{(b_1,b_2)},
\qquad
q=\frac{b_2}{(b_1,b_2)}.
\tag{2}
\]

On the asymptotically dominant coprime prime-power family, `(r,q)=(b1,b2)`.

The coefficient rows in variables `(m,n,k)` are

\[
a_1=(1,0,0),
\quad
a_2=(1,0,-r),
\quad
a_3=(0,1,0),
\quad
a_4=(0,1,-q).
\tag{3}
\]

For every `r,q != 0`, this system has Cauchy--Schwarz complexity at most one. For example, for `a1` partition the other forms as

\[
\{a_2,a_3\}\sqcup\{a_4\}.
\]

The span of `a2,a3` consists of `(x,y,-rx)` and therefore cannot contain `a1`; `a4` is not a scalar multiple of `a1`. Cyclically, valid two-class partitions are

\[
\begin{array}{c|c}
\text{target} & \text{classes}\\ \hline
 a_1 & \{a_2,a_3\},\{a_4\}\\
 a_2 & \{a_1,a_4\},\{a_3\}\\
 a_3 & \{a_1,a_4\},\{a_2\}\\
 a_4 & \{a_2,a_3\},\{a_1\}.
\end{array}
\tag{4}
\]

The complexity is not zero, because

\[
q(a_1-a_2)=r(a_3-a_4),
\tag{5}
\]

and every coefficient in this unique four-form dependence is nonzero. Hence every `a_i` lies in the span of the other three:

\[
\boxed{s_{\rm CS}(L_1,L_2,L_3,L_4)=1.}
\tag{6}
\]

This is a specialization of the classical Green--Tao/Gowers complexity-one framework, not a new notion.

## 2. On one prime cyclic group the coefficients disappear exactly

Let `P` be prime with `P` not dividing `rq`, put `G=Z/PZ`, and use normalized Fourier transform

\[
\widehat f(\xi)
=\mathbb E_{x\in G}f(x)e_P(-\xi x).
\tag{7}
\]

For arbitrary functions `f_i:G->C`, define

\[
\Lambda_{r,q}^{(P)}
:=
\mathbb E_{m,n,k\in G}
 f_1(m)f_2(m-rk)f_3(n)f_4(n-qk).
\tag{8}
\]

Expanding all four factors into characters, the averages over `m,n,k` impose

\[
\xi_1+\xi_2=0,
\qquad
\xi_3+\xi_4=0,
\qquad
r\xi_2+q\xi_4=0.
\tag{9}
\]

Because `r,q` are units modulo `P`, every solution is uniquely parameterized by `t in G` as

\[
(\xi_1,\xi_2,\xi_3,\xi_4)
=(-qt,qt,rt,-rt).
\tag{10}
\]

Therefore

\[
\boxed{
\Lambda_{r,q}^{(P)}
=
\sum_{t\in G}
\widehat f_1(-qt)
\widehat f_2(qt)
\widehat f_3(rt)
\widehat f_4(-rt).
}
\tag{11}
\]

Hölder and the fact that multiplication by `r` or `q` permutes `G` give the coefficient-free bound

\[
\boxed{
|\Lambda_{r,q}^{(P)}|
\le
\prod_{i=1}^4\|f_i\|_{U^2(G)}.
}
\tag{12}
\]

This is the exact Fourier form of the ordinary Cauchy--Schwarz-complexity-one phenomenon. Large integer representatives for `r,q` are harmless as long as all variables live in the same finite field and those coefficients remain nonzero.

This observation materially changes the interpretation of WI-039. The Yang system does **not** intrinsically require a `U^3` or higher-order uniformity theorem merely because it contains four prime forms. A Fourier-level route is structurally sufficient in a dense common ambient group.

## 3. The common-group formulation loses the Yang cell volume

The source, however, is highly anisotropic. WI-046/WI-050 identify the dominant coprime physical scales

\[
M_m\asymp \frac{X}{b_2},
\qquad
M_n\asymp \frac{X}{b_1},
\qquad
K\asymp \frac{X}{b_1b_2},
\tag{13}
\]

so that

\[
rK\asymp M_m,
\qquad
qK\asymp M_n.
\tag{14}
\]

If one embeds the whole source cell into a common prime cyclic group of size `P asy X` so that (11)--(12) apply literally, the three-variable cell occupies only

\[
\rho_{b_1,b_2}
\asymp
\frac{M_mM_nK}{X^3}
\asymp
\boxed{\frac1{b_1^2b_2^2}}
\tag{15}
\]

of the ambient volume.

Consequently an ambient estimate `error=o(P^3)` is not a relative asymptotic for the source cell. A black-box normalized Fourier error `delta(X)` must satisfy at least

\[
\delta(X)=o\!\left(\frac1{b_1^2b_2^2}\right)
\tag{16}
\]

before geometry/Fourier-algebra losses are even charged. On any fixed positive-mass continuum box with

\[
b_1\ge X^{\alpha_0},
\qquad
b_2\ge X^{\beta_0},
\qquad
\alpha_0,\beta_0>0,
\tag{17}
\]

this demands a polynomial saving

\[
\delta(X)=o\!\left(X^{-2(\alpha_0+\beta_0)}\right).
\tag{18}
\]

WI-039 already proves that fixed/polylogarithmic coefficients occupy only `o(1)` of the relevant Mertens mass and that positive-power coefficient regions are genuine. Thus a qualitative or merely logarithmically saving common-group `U^2` theorem cannot by itself be inserted cellwise into the Yang continuum. Equation (18) is a scaling requirement, not a claim that no stronger prime estimate could ever supply it.

## 4. Localizing to the physical scales restores density but creates quotient aliasing

The natural attempt to avoid (15) is to localize each variable at its own physical scale. The exact finite-group model of (14) is

\[
G_m=\mathbb Z/(rL)\mathbb Z,
\qquad
G_n=\mathbb Z/(qL)\mathbb Z,
\qquad
G_k=\mathbb Z/L\mathbb Z,
\tag{19}
\]

with multilinear form

\[
\Lambda_{r,q,L}^{\rm loc}
=
\mathbb E_{m\in G_m}
\mathbb E_{n\in G_n}
\mathbb E_{k\in G_k}
 f_1(m)f_2(m-rk)f_3(n)f_4(n-qk).
\tag{20}
\]

Now `k -> rk` maps `G_k` injectively onto the index-`r` subgroup `r Z/(rL)`, and similarly for `q`. Fourier expansion gives

\[
\boxed{
\Lambda_{r,q,L}^{\rm loc}
=
\sum_{t\bmod L} A_r(t)A_q(-t),
}
\tag{21}
\]

where

\[
A_r(t)
=
\sum_{\substack{a\bmod rL\\a\equiv t\;({\rm mod}\;L)}}
\widehat f_1(-a)\widehat f_2(a),
\tag{22}
\]

and

\[
A_q(t)
=
\sum_{\substack{c\bmod qL\\c\equiv t\;({\rm mod}\;L)}}
\widehat f_3(-c)\widehat f_4(c).
\tag{23}
\]

The single Fourier line (11) has become fibers of cardinalities `r` and `q`. This is not a proof artifact: the fibers are precisely the dual characters of the quotient groups left unchanged by the sublattice shifts.

## 5. A centered quadratic-phase witness forces coefficient loss

The aliasing in (21)--(23) cannot be removed by an abstract `U^2` inequality.

Let `r>=3` be an odd prime and take any positive integer `L`. On the quotient `Z/rZ`, set

\[
\phi(c)=e_r(c^2),
\qquad
\mu=\mathbb E_{c\bmod r}\phi(c).
\tag{24}
\]

The classical quadratic Gauss-sum identity gives

\[
|\mu|=r^{-1/2}
\tag{25}
\]

and every normalized Fourier coefficient of `phi` has modulus `r^{-1/2}`. Lift the centered quotient mode to `G_m=Z/(rL)` by

\[
g_r(m)=\frac{\phi(m\bmod r)-\mu}{2}.
\tag{26}
\]

Then

\[
\mathbb E_{m\in G_m}g_r(m)=0,
\qquad
\|g_r\|_\infty<1.
\tag{27}
\]

Because every allowed displacement `rk` is divisible by `r`,

\[
\boxed{g_r(m-rk)=g_r(m)}
\tag{28}
\]

for every `m,k`. Hence, taking

\[
f_1=g_r,
\qquad
f_2=\overline{g_r},
\qquad
f_3=f_4=1,
\tag{29}
\]

gives the exact localized correlation

\[
\boxed{
\Lambda_{r,q,L}^{\rm loc}
=
\mathbb E_m|g_r(m)|^2
=
\frac{1-r^{-1}}4.
}
\tag{30}
\]

On the other hand the Fourier support of `g_r` consists of the `r-1` nonzero quotient frequencies `a=L u`, each with modulus `1/(2\sqrt r)`. Therefore

\[
\boxed{
\|g_r\|_{U^2(G_m)}^4
=
\frac{r-1}{16r^2},
\qquad
\|g_r\|_{U^2(G_m)}
=
\frac{(r-1)^{1/4}}{2r^{1/2}}.
}
\tag{31}
\]

Combining (30)--(31), any inequality of the form

\[
|\Lambda_{r,q,L}^{\rm loc}|
\le C(r,q)\,
\|f_1\|_{U^2}
\prod_{i=2}^4\|f_i\|_\infty
\tag{32}
\]

valid for all bounded functions must satisfy

\[
\boxed{
C(r,q)
\ge
\frac{(r-1)^{3/4}}{2r^{1/2}}
\asymp r^{1/4}.
}
\tag{33}
\]

By symmetry the same construction with the `n` quotient forces `C(r,q) gg q^{1/4}`. Thus no coefficient-uniform localized `U^2` consumer exists at these natural subgroup scales using only ordinary one-variable `U^2` information.

The witness is deliberately **mean zero**. The obstruction is therefore not merely the constant mode that one would remove by subtracting the global mean. It is a coherent quotient mode supported on the residue classes preserved by the large-index dilation.

## 6. Why this does not contradict the classical complexity-one theorem

Green--Tao's finite-complexity framework and the standard Cauchy--Schwarz-complexity-one generalized von Neumann inequality work on a common finite ambient group. Freddie Manners later emphasized explicitly that the Cauchy--Schwarz complexity bound is uniform in the coefficients when its hypotheses are satisfied on that common group; his coefficient-dependence obstruction concerns the harder case where true complexity is smaller than Cauchy--Schwarz complexity.

There is no contradiction here. Equation (12) is exactly that uniform common-group phenomenon. The failure in (33) occurs only after replacing the common group by the source-faithful anisotropic groups (19), where multiplication by `r` is no longer an automorphism: it lands in a subgroup of index `r`. The quotient characters in (26) are invisible to the `k`-motion.

Relevant established prior art:

- Ben Green and Terence Tao, **Linear equations in primes**, *Annals of Mathematics* 171 (2010), 1753--1850, DOI `10.4007/annals.2010.171.1753`. Role: classical finite-complexity/Cauchy--Schwarz framework; complexity-one prime patterns are governed by Fourier/`U^2` information for fixed systems.
- Freddie Manners, **Good Bounds in Certain Systems of True Complexity One**, *Discrete Analysis* 2018/2019-era publication from arXiv:1705.06801. In the introduction, especially Question 1.4 and the discussion around Proposition 1.1, he distinguishes the coefficient-uniform Cauchy--Schwarz-complexity bound from coefficient-dependent true-complexity reductions. Role here: confirms that common-group CS-complexity-one uniformity is classical rather than a new Yang mechanism.
- Xuancheng Shao and Joni Teräväinen, **The Bombieri--Vinogradov theorem for nilsequences**, *Discrete Analysis* 2021:21, DOI `10.19086/da.29048`. Role: established example of how large-modulus arithmetic progression structure requires its own averaged distribution input; it does not by itself cover the full power-sized Yang coefficient support. WI-047 already quantifies the corresponding fixed-level support obstruction.

The quadratic Gauss sum and the Fourier calculations (11), (21)--(33) are classical identities. No novelty is claimed for them. The Mathia-specific deduction is their application to the exact Yang scale geometry: **the apparent complexity-one escape and the coefficient wall are compatible because global density and local quotient aliasing trade off against one another.**

## 7. Relation to WI-039, WI-047, WI-049 and WI-050

This finding narrows rather than supersedes those results.

- WI-039 showed that published generic higher-uniformity transference does not cover the dominant power-sized coefficients.
- WI-047 showed that converting the coefficients into AP moduli and applying any black-box fixed level `theta<1` leaves positive Yang support mass uncovered.
- WI-049 showed that the **deterministic** genuine four-form local singular-series main centers correctly; a missing local Euler main is not the explanation for a persistent covariance.
- WI-050 used Bienvenu to prove that the post-local-main residual is lower order throughout every fixed polylogarithmic coefficient range.

The present result explains why simply noticing that (1) is a complexity-one system does not close the remaining super-polylogarithmic regime. A valid Fourier repair has to prove that, **after the genuine local model is removed**, the actual prime residual has negligible mass on the quotient/aliasing fibers visible in (22)--(23), uniformly over the power-sized `r,q` family. Ordinary global `U^2=o(1)` does not state that.

This is also why the quadratic witness is not a counterexample to the primes. It is an information-theoretic control showing that no theorem whose only hypothesis is one-variable `U^2` smallness can rule out coherent quotient modes at natural scale. The von Mangoldt residual may possess additional arithmetic cancellation that the witness lacks; proving exactly that cancellation is now the target.

## 8. Decisive audit and falsification tests

Narrow or reject this finding if any of the following fails.

1. Reconstruct (1)--(2) directly from the pinned `t2_swaps.py` equal-lock relation and verify the dominant coprime identification `(r,q)=(b1,b2)`.
2. Check the four partitions in (4) and the nonzero dependence (5), establishing `s_CS=1` rather than merely finite complexity.
3. Recompute the common-group Fourier constraints (9) and parameterization (10); `P` must not divide `rq`.
4. Verify the source scale relations (13)--(14) and the ambient-volume ratio (15). Do not infer a relative cell asymptotic from a merely ambient `o(1)` estimate.
5. Recompute the anisotropic Fourier condition: the `k` average imposes `a+c=0 mod L`, not equality modulo `rL` or `qL`; this is what produces the fibers (22)--(23).
6. For odd prime `r`, verify the normalized quadratic Gauss transform, the centering in (26), shift invariance (28), and exact formulas (30)--(31). The lower bound (33) must grow like `r^(1/4)`.
7. Do **not** promote the toy quotient phase to a model of primes. A source-specific theorem proving that genuine locally centered prime residuals are uniformly orthogonal to these fibers would bypass the obstruction and materially narrow this finding.
8. Do **not** infer that all Fourier approaches fail. The obstruction is specifically to a coefficient-free black-box consumer based only on ordinary one-variable `U^2` control after natural anisotropic localization.

## 9. Consequence for `weil_inertia`

The active super-polylogarithmic welding question is more precise. The remaining target is not generically “higher Gowers uniformity for four primes.” The exact system already has Fourier complexity one. What is missing is one of the following genuinely coefficient-aware inputs:

\[
\boxed{
\begin{array}{c}
\text{quotient/AP-uniform control of the post-local-main Fourier fibers},\\
\text{an anisotropic relative-}U^2\text{ theorem with the sublattice modes removed},\\
\text{or a direct joint four-prime/covariance estimate on the Yang weighted family.}
\end{array}}
\tag{34}
\]

This closes the cheap route

\[
\boxed{
\text{“the Yang system has complexity one”}
\;\Longrightarrow\;
\text{“ordinary Fourier uniformity removes the power-coefficient wall.”}
}
\tag{35}
\]

The first statement is true; the implication is false for exact, source-relevant localization reasons. Future work on `CLUE-yang-locked-covariance-leading-scale` should therefore test quotient-aware arithmetic cancellation rather than spend cycles replacing `U^3` machinery by an unlocalized `U^2` estimate.