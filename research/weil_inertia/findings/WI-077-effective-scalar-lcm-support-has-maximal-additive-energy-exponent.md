# WI-077 — the effective scalar-lcm family has maximal additive-energy exponent

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECTION`. This finding does **not** certify the Yang--Yang one-sided fourth-moment candidate and does not change Mathia's current unconditional simple-critical proportion. It closes the ordinary **unweighted additive-energy** version of the scalar-modulus escape left open by WI-076.

WI-076 proved, using the exact Yang source weights together with Bienvenu's established four-prime asymptotic on the fixed coprime base pair `(b_1,b_2)=(5,7)`, that the source-effective scalar moduli contain a set `A_X` of cardinality

\[
|A_X|\gg \frac{X}{(\log X)^4}
\]

inside one source-scale interval of length `O(X)`. The elementary energy inequalities below then force both Baker--Munsch--Shparlinski energy parameters to have the **maximal possible exponent**:

\[
\boxed{
\mathsf E^+(A_X),\ \mathsf E_*^+(A_X)
\gg \frac{X^3}{(\log X)^{16}}.
}
\]

Consequently, for any unlabelled effective scalar family `B_X` containing this fixed-slope source subfamily and lying in the natural `O(X)` scalar range, with `Q_X=|B_X|`,

\[
\boxed{
Q_X=X^{1+o(1)},\qquad
\mathsf E^+(B_X)=Q_X^{3-o(1)},\qquad
\mathsf E_*^+(B_X)=Q_X^{3-o(1)}.
}
\]

Thus the unlabelled Yang scalar support is not merely non-power-sparse: at exponent level it is also maximally additively structured. In the natural regular-growth exponent `alpha=1`, the general Baker--Munsch--Shparlinski large-sieve theorem therefore supplies no fixed-power improvement over the classical dense-modulus large-sieve scale anywhere in its critical range. This is a theorem-interface obstruction, not a no-go for source-weighted cancellation, a mass-preserving low-energy pruning, or a labelled transform retaining `(r,q)`.

## 1. The fixed source subfamily lies in a macroscopic scalar interval

WI-050 constructed, for every fixed coprime base pair, a one-sided interior convex body on which

\[
c_k\frac{X}{b_1b_2}
\le k\le
2c_k\frac{X}{b_1b_2}
\tag{1}
\]

for one fixed `c_k>0`, while all four von-Mangoldt forms remain inside the source windows and the deleted hyperplanes `k=0` and `j=0` are avoided. WI-076 specialized this body to `(b_1,b_2)=(5,7)` and used the injective scalar projection

\[
L=\operatorname{lcm}(5k,7k)=35k.
\tag{2}
\]

Hence the effective scalar set produced by that fixed-slope subfamily may be taken inside

\[
I_X=[c_kX,2c_kX]
\tag{3}
\]

up to harmless integer endpoints. Write

\[
A_X:=\{35k:\ W_k(X)>0\},
\qquad
M_X:=|A_X|.
\tag{4}
\]

WI-076 gives

\[
\boxed{M_X\gg X(\log X)^{-4}.}
\tag{5}
\]

The only additional information used below is the interval containment (3). No new prime-pattern estimate is introduced.

## 2. Symmetric additive energy is forced to be essentially maximal

For a finite set `A` define

\[
r_A(s):=\#\{(a,b)\in A^2:a+b=s\}.
\tag{6}
\]

Then

\[
\mathsf E^+(A)
=\sum_s r_A(s)^2,
\qquad
\sum_s r_A(s)=|A|^2.
\tag{7}
\]

Because `A_X` lies in an interval of length `O(X)`, its sumset has

\[
|A_X+A_X|\ll X.
\tag{8}
\]

Cauchy--Schwarz therefore gives the classical lower bound

\[
\mathsf E^+(A_X)
\ge
\frac{M_X^4}{|A_X+A_X|}
\gg
\frac{M_X^4}{X}.
\tag{9}
\]

Using (5),

\[
\boxed{
\mathsf E^+(A_X)
\gg
\frac{X^3}{(\log X)^{16}}.
}
\tag{10}
\]

This is already within a polylogarithmic factor of the largest possible energy at this scale. Indeed every `M`-element set satisfies the trivial upper bound

\[
\mathsf E^+(A)\le M^3,
\tag{11}
\]

because three entries of an additive quadruple determine the fourth.

## 3. The asymmetric energy is forced to the same exponent

Baker--Munsch--Shparlinski also use

\[
\mathsf E_h^+(A)
:=
\#\{(a,b,c,d)\in A^4:a+b=c+d+h\},
\qquad
\mathsf E_*^+(A):=\max_{h\ne0}\mathsf E_h^+(A).
\tag{12}
\]

Summing over every integer `h`, each ordered quadruple contributes exactly once, so

\[
\sum_{h\in\mathbf Z}\mathsf E_h^+(A_X)=M_X^4.
\tag{13}
\]

The zero-shift term is the ordinary energy and satisfies

\[
\mathsf E_0^+(A_X)=\mathsf E^+(A_X)\le M_X^3.
\tag{14}
\]

Since all elements of `A_X` lie in an interval of length `O(X)`, only `O(X)` values of `h` can occur in (13). Therefore, for all sufficiently large `X`,

\[
\mathsf E_*^+(A_X)
\gg
\frac{M_X^4-M_X^3}{X}
\gg
\frac{M_X^4}{X}.
\tag{15}
\]

Combining with (5),

\[
\boxed{
\mathsf E_*^+(A_X)
\gg
\frac{X^3}{(\log X)^{16}}.
}
\tag{16}
\]

Thus the asymmetric-energy escape is not available either: the nonzero additive translates carry essentially maximal energy exponent even after the genuine Yang weights have selected the support.

## 4. Passing to the full unlabelled effective scalar support cannot lower either energy

Let `B_X` be any unlabelled effective scalar-modulus set at the same source scale that contains `A_X`. WI-071 gives the global scalar range `L\ll X`, so

\[
Q_X:=|B_X|\ll X.
\tag{17}
\]

Together with `Q_X\ge M_X` and (5),

\[
\boxed{Q_X=X^{1+o(1)}.}
\tag{18}
\]

Set inclusion can only add additive quadruples, so

\[
\mathsf E^+(B_X)\ge\mathsf E^+(A_X).
\tag{19}
\]

For the asymmetric energy, choose a nonzero `h_X` attaining the maximum in (15). Every `A_X` quadruple counted by `\mathsf E_{h_X}^+` remains a `B_X` quadruple, hence

\[
\mathsf E_*^+(B_X)
\ge
\mathsf E_{h_X}^+(B_X)
\ge
\mathsf E_{h_X}^+(A_X)
=
\mathsf E_*^+(A_X).
\tag{20}
\]

Since `Q_X\ll X`, (10), (16), (19), and (20) imply

\[
\mathsf E^+(B_X),\ \mathsf E_*^+(B_X)
\gg
\frac{Q_X^3}{(\log X)^{16}}.
\tag{21}
\]

On the other hand, Baker--Munsch--Shparlinski record `\mathsf E_*^+(B_X)\le\mathsf E^+(B_X)`, while (11) gives `\mathsf E^+(B_X)\le Q_X^3`. Because (18) makes `\log Q_X\sim\log X`,

\[
\boxed{
\mathsf E^+(B_X)=Q_X^{3-o(1)},
\qquad
\mathsf E_*^+(B_X)=Q_X^{3-o(1)}.
}
\tag{22}
\]

The exponent `3` is maximal. In particular no uniform estimate

\[
\mathsf E^+(B_X)\ll Q_X^{3-\delta}
\quad\text{or}\quad
\mathsf E_*^+(B_X)\ll Q_X^{3-\delta}
\tag{23}
\]

can hold for any fixed `delta>0`.

## 5. Consequence for the Baker--Munsch--Shparlinski black-box route

Baker, Munsch and Shparlinski, *Additive energy and a large sieve inequality for sparse sequences*, Mathematika 68 (2022), Theorem 1.1, consider a scalar modulus sequence

\[
m_j=j^{\alpha+o(1)}
\tag{24}
\]

and prove, for `Q^alpha <= N <= Q^(2alpha)`, the bound

\[
\mathfrak S(\mathbf a,\mathbf m;M,N,Q)
\le
\left(
N\mathsf E^+(\mathbf m_Q)^{1/4}
+
N^{3/4}Q^{\alpha/2}\mathsf E_*^+(\mathbf m_Q)^{1/4}
\right)
Q^{o(1)}\|\mathbf a\|^2.
\tag{25}
\]

The theorem is genuinely sensitive to both the symmetric and asymmetric energies; this is why merely proving (10) would not by itself close the obvious low-energy escape.

For the Yang unlabelled scalar family, (18) says that a source-scale block contains `Q=X^{1+o(1)}` distinct moduli of size `X=Q^{1+o(1)}`. Therefore any direct regular-growth realization of these source blocks has the natural exponent

\[
\alpha=1.
\tag{26}
\]

There is a minor interface caveat: Theorem 1.1 is printed for truncations of one regular sequence, whereas the Yang effective support is naturally a source-scale family. If no dyadic/relabelled sequence interface preserving the source weights is proved, the theorem is already not a black-box consumer. Granting such an interface is the **favorable** case considered here.

Under that favorable identification, (22) turns (25), at exponent level, into

\[
\boxed{
NQ^{3/4+o(1)}
+
N^{3/4}Q^{5/4+o(1)}.
}
\tag{27}
\]

Write `N=Q^theta` in the critical range `1<=theta<=2`. The second term in (27) has exponent

\[
\frac34\theta+\frac54\ge2,
\tag{28}
\]

with equality only at the left endpoint `theta=1`. The classical dense-modulus large sieve at this `alpha=1` scale is `Q^2+N=Q^{2+o(1)}` throughout the same range. Hence the general BMS energy theorem, fed with the **actual unweighted Yang scalar energy**, cannot furnish a fixed-power improvement over that classical scale anywhere in its critical range. At the left endpoint a polylogarithmic difference is not excluded; for every `theta>1` the displayed BMS second term is exponent-wise larger than `Q^2`.

This does **not** prove that the underlying Yang covariance is large. It proves only that the particular black-box mechanism “project to unlabelled scalar moduli and win through unusually small ordinary BMS energies” has no power saving available: both required energy inputs are already maximal up to subpolynomial factors.

## 6. What remains live

The obstruction is deliberately narrower than a general no-go for large-sieve or dispersion methods.

1. **Weighted cancellation remains live.** Equations (10)--(22) concern the unweighted support energies in the exact sense used by BMS Theorem 1.1. A transform carrying signed/source coefficients could have cancellation invisible to set cardinality and set energy.
2. **Mass-preserving pruning remains live but needs a theorem.** One could try to retain most of the Yang covariance on a much smaller scalar subset with genuinely lower energy. WI-076 plus the present argument rule out obtaining this merely by deleting the zero-weight moduli; they do not rule out a nontrivial weighted concentration theorem.
3. **Reduced-direction labels remain live.** A scalar organization that keeps `(r,q)` attached to `L` is not the unlabelled family in (22). The polylogarithmic representation multiplicity from WI-075 remains potentially useful.
4. **Two-dimensional source-adapted large sieves remain live.** WI-071's lcm incidence structure can be used before scalar projection; the present energy calculation says nothing about such a theorem.
5. **A Yang-specific dispersion theorem remains live.** The accepted locked-covariance clue still needs control of the post-local-main power-coefficient fibers. This finding only closes one proposed route for acquiring that control.

The practical redirection is therefore sharper than WI-076's boundary:

\[
\boxed{
\text{unlabelled scalar support cardinality: no power sparsity},
\qquad
\text{unweighted scalar additive energy: no power saving}.
}
\tag{29}
\]

Any useful scalar reduction now has to exploit **weights, cancellation, pruning with retained mass, or labels**, not merely the set of scalar `lcm` values.

## 7. Prior-art and novelty boundary

No novelty is claimed for Cauchy--Schwarz in (9), the identities (13)--(15), the trivial upper bound `\mathsf E^+(A)\le|A|^3`, or the general principle that dense subsets of intervals have large additive energy. These are classical additive-combinatorial facts.

The established theorem-level prior art is:

- Roger C. Baker, Marc Munsch and Igor E. Shparlinski, **Additive energy and a large sieve inequality for sparse sequences**, *Mathematika* 68:2 (2022), 362--399, DOI `10.1112/mtk.12140`, arXiv:2103.12659. Theorem 1.1 is the load-bearing large-sieve interface and uses both `\mathsf E^+` and `\mathsf E_*^+` exactly as in (25). The paper's convex-sequence example obtains a genuinely subcubic energy exponent, illustrating the type of input that the Yang scalar family cannot satisfy.
- Pierre-Yves Bienvenu, **A higher-dimensional Siegel--Walfisz theorem**, *Acta Arithmetica* 179 (2017), 79--100, DOI `10.4064/aa8600-10-2016`, arXiv:1607.06625. Its role is inherited through WI-050 and WI-076: it is what certifies the source-effective fixed-slope support lower bound before the elementary energy argument begins.

The durable Mathia deduction is the combination of WI-076's **genuinely weighted source-support lower bound** with the exact finite-set energy identities: the same fixed slope that forbids power sparsity also forces both BMS energy parameters to maximal exponent. A bounded audit of the current `weil_inertia` findings found no prior finding making this energy deduction; WI-076 explicitly left ordinary additive-energy structure as a possible scalar escape. No priority claim is made.

## 8. Falsification and narrowing gates

1. **Source interval geometry.** If WI-050/WI-076's fixed `(5,7)` interior did not place `k` in a macroscopic interval of length `O(X)` while retaining the four von-Mangoldt conditions, then the energy lower bounds would need to be revisited. WI-050 gives the explicit one-sided interval (1), and WI-076 uses that same interior.
2. **Distinct scalar values.** The injection `L=35k` is essential. It is exact for the fixed coprime pair.
3. **Unlabelled support only.** The monotonicity step from `A_X` to `B_X` deliberately forgets which slope generated a scalar value. A labelled energy or matrix-valued transform is outside the claim.
4. **BMS regular-growth interface.** If the Yang source cannot be reorganized into the sequence/truncation interface of BMS Theorem 1.1, then the black-box route fails even earlier. Equation (27) is conditional only on granting the most favorable such interface; the energy obstruction itself, (10)--(22), is unconditional within the already-established source geometry.
5. **No impossibility claim for weighted large sieve.** A theorem using coefficient cancellation rather than unweighted set energy can evade the argument and should be assessed on its own exact norm/weight interface.
