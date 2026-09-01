# AF-044 — Closed-secant modulus is the exact distance to fidelity loss

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `STRUCTURAL-CLASSIFICATION`, `NEGATIVE/OBSTRUCTION`

## Claim

Let `S\subset\mathbb R^n` contain at least two points, and let

\[
K_S
=
\widehat{\operatorname{Sec}}(S)
=
\overline{\left\{
\frac{x-y}{\|x-y\|}:x,y\in S,\ x\neq y
\right\}}
\subset S^{n-1}
\]

be the closed unit-secant carrier from AF-043. For a linear map

\[
B:\mathbb R^n\to\mathbb R^q
\]

write

\[
\kappa_S(B)
=
\min_{u\in K_S}\|Bu\|.
\]

In the operator space `\mathcal L(\mathbb R^n,\mathbb R^q)` equipped with the Euclidean operator norm, define

\[
\Sigma_S
=
\{A:\kappa_S(A)=0\}
\]

for the **stable-fidelity failure set**, and

\[
\mathcal C_S
=
\{A:A|_S\text{ is not injective}\}
\]

for the **exact-collision set**. Then:

1. **The fidelity modulus is 1-Lipschitz in the compression operator.** For all linear `A,B`,
   \[
   \boxed{
   |\kappa_S(A)-\kappa_S(B)|
   \le
   \|A-B\|.
   }
   \]

2. **The closed-secant modulus is exactly the operator-norm distance to stable fidelity loss.**
   \[
   \boxed{
   \operatorname{dist}(B,\Sigma_S)
   =
   \kappa_S(B).
   }
   \]
   A nearest unstable operator always exists. If `u_*\in K_S` minimizes `\|Bu\|`, the rank-one perturbation
   \[
   \Delta_*(v)
   =
   -\langle v,u_*\rangle Bu_*
   \]
   satisfies
   \[
   \|\Delta_*\|=\kappa_S(B),
   \qquad
   (B+\Delta_*)u_*=0,
   \]
   so `B+\Delta_*\in\Sigma_S`.

3. **The same number is the distance to an actual collision, even though the collision set need not be closed.**
   \[
   \boxed{
   \operatorname{dist}(B,\mathcal C_S)
   =
   \kappa_S(B).
   }
   \]
   Consequently
   \[
   \boxed{
   \Sigma_S
   =
   \overline{\mathcal C_S}.
   }
   \]
   Stable fidelity failure is therefore precisely the closure, in operator space, of exact pairwise collapse.

4. **Attainment distinguishes actual from limiting secants.** A nearest operator in `\mathcal C_S` exists at distance `\kappa_S(B)` if and only if the infimum
   \[
   \inf_{u\in\operatorname{Sec}(S)}\|Bu\|
   \]
   is attained by an actual unit secant. By contrast, a nearest point of `\Sigma_S` always exists because the closed secant carrier is compact. Thus AF-043's distinction between actual and limiting secants becomes an exact distinction between **attained collision radius** and **stable-loss radius**.

5. **`\kappa_S` is the sharp perturbation radius.** If
   \[
   \|\Delta\|<\kappa_S(B),
   \]
   then
   \[
   \boxed{
   \kappa_S(B+\Delta)
   \ge
   \kappa_S(B)-\|\Delta\|>0.
   }
   \]
   No operator perturbation below that radius can destroy stable fidelity, while at radius exactly `\kappa_S(B)` a rank-one perturbation always does.

6. **This gives a carrier-relative condition number.** Whenever `B\neq0` and `\kappa_S(B)>0`, define
   \[
   \operatorname{cond}_S(B)
   =
   \frac{\|B\|}{\kappa_S(B)}.
   \]
   Then
   \[
   \boxed{
   \operatorname{cond}_S(B)
   =
   \frac{\|B\|}{\operatorname{dist}(B,\Sigma_S)}.
   }
   \]
   The stable recoverability of a linear compression is therefore controlled by its **relative distance to the nearest operator that kills an actual or limiting secant direction**.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\text{the closed-secant fidelity modulus is not merely a lower Lipschitz constant; it is the exact perturbation radius to loss of recoverability.}
}
\]

This turns AF-043's geometric transversality condition into a condition-number statement and makes the actual-secant / closed-secant distinction visible directly in operator space.

## Derivation

### The modulus is 1-Lipschitz

For every unit vector `u`, the reverse triangle inequality gives

\[
\bigl|\|Au\|-\|Bu\|\bigr|
\le
\|(A-B)u\|
\le
\|A-B\|.
\]

Taking minima over the same compact set `K_S` yields

\[
\kappa_S(A)
\ge
\kappa_S(B)-\|A-B\|.
\]

Interchanging `A` and `B` gives

\[
|\kappa_S(A)-\kappa_S(B)|
\le
\|A-B\|.
\]

In particular `\Sigma_S=\kappa_S^{-1}(\{0\})` is closed.

### Exact distance to stable failure

Let `A\in\Sigma_S`. Since `\kappa_S(A)=0`, the Lipschitz estimate gives

\[
\kappa_S(B)
\le
\|B-A\|.
\]

Taking the infimum over `A\in\Sigma_S` gives

\[
\kappa_S(B)
\le
\operatorname{dist}(B,\Sigma_S).
\]

For the reverse inequality, choose `u_*\in K_S` with

\[
\|Bu_*\|=\kappa_S(B),
\]

which exists because `K_S` is compact. Define

\[
\Delta_*
=
-(Bu_*)\otimes u_*^{\!*},
\qquad
\Delta_*(v)
=
-\langle v,u_*\rangle Bu_*.
\]

Since `\|u_*\|=1`,

\[
\|\Delta_*\|=\|Bu_*\|=\kappa_S(B),
\]

and

\[
(B+\Delta_*)u_*=0.
\]

Because `u_*\in K_S`, AF-043 gives

\[
\kappa_S(B+\Delta_*)=0.
\]

Thus `B+\Delta_*\in\Sigma_S` and

\[
\operatorname{dist}(B,\Sigma_S)
\le
\kappa_S(B).
\]

Both inequalities give equality, with a rank-one nearest perturbation.

### Exact collisions have the same distance

Every exact collision is a stable-fidelity failure:

\[
\mathcal C_S\subseteq\Sigma_S.
\]

Therefore

\[
\operatorname{dist}(B,\mathcal C_S)
\ge
\operatorname{dist}(B,\Sigma_S)
=
\kappa_S(B).
\]

Conversely, by AF-043,

\[
\kappa_S(B)
=
\inf_{u\in\operatorname{Sec}(S)}\|Bu\|.
\]

Given `\varepsilon>0`, choose an actual unit secant

\[
u=\frac{x-y}{\|x-y\|}
\]

with

\[
\|Bu\|<\kappa_S(B)+\varepsilon.
\]

Set

\[
\Delta(v)=-\langle v,u\rangle Bu.
\]

Then

\[
\|\Delta\|=\|Bu\|<\kappa_S(B)+\varepsilon,
\]

while `(B+\Delta)u=0`. Since `u` comes from the actual pair `x\neq y`,

\[
(B+\Delta)x=(B+\Delta)y,
\]

so `B+\Delta\in\mathcal C_S`. Letting `\varepsilon\downarrow0` proves

\[
\operatorname{dist}(B,\mathcal C_S)
\le
\kappa_S(B).
\]

Hence

\[
\boxed{
\operatorname{dist}(B,\mathcal C_S)
=
\operatorname{dist}(B,\Sigma_S)
=
\kappa_S(B).
}
\]

Since a point has zero distance to a set exactly when it lies in that set's closure,

\[
\Sigma_S
=
\overline{\mathcal C_S}.
\]

### When is the nearest collision attained?

Suppose an actual secant `u\in\operatorname{Sec}(S)` attains

\[
\|Bu\|=\kappa_S(B).
\]

The rank-one perturbation above has norm exactly `\kappa_S(B)` and creates an actual collision, so the distance to `\mathcal C_S` is attained.

Conversely, suppose `A\in\mathcal C_S` satisfies

\[
\|A-B\|=\kappa_S(B).
\]

Choose an actual unit secant `u` killed by `A`. Then

\[
\|Bu\|
=
\|(B-A)u\|
\le
\|B-A\|
=
\kappa_S(B).
\]

But `\kappa_S(B)` is the infimum over actual secants, so equality holds. Thus that actual secant attains the infimum.

Therefore the collision-distance infimum is attained **exactly** when the minimizing closed-secant direction can be realized by an actual secant with the same value.

## Boundary control: exact injectivity need not be open

Take the compact parabola

\[
S
=
\{(t,t^2):-1\le t\le1\}
\subset\mathbb R^2
\]

and the row operator

\[
B(x,y)=2x-y.
\]

On the parabola,

\[
B(t,t^2)=2t-t^2.
\]

This function is strictly increasing on `[-1,1]`: for `s<t`,

\[
(2t-t^2)-(2s-s^2)
=(t-s)(2-t-s)>0,
\]

because distinct `s,t\le1` imply `t+s<2`. Hence `B|_S` is injective and

\[
B\notin\mathcal C_S.
\]

But the secant between `(s,s^2)` and `(t,t^2)` is proportional to

\[
(1,s+t).
\]

As distinct `s,t\to1`, the normalized secants converge to

\[
\frac{(1,2)}{\sqrt5},
\]

which is killed by `B` because

\[
B(1,2)=0.
\]

Therefore

\[
\kappa_S(B)=0,
\qquad
B\in\Sigma_S\setminus\mathcal C_S.
\]

The distinction is visible under arbitrarily small operator perturbations. For `0<\varepsilon<1`, let

\[
B_\varepsilon(x,y)
=
2x-(1+\varepsilon)y.
\]

Then

\[
\|B_\varepsilon-B\|=\varepsilon.
\]

Choose

\[
t=1,
\qquad
s=\frac{2}{1+\varepsilon}-1.
\]

For `0<\varepsilon<1`, one has `0<s<1=t`, and

\[
s+t=\frac{2}{1+\varepsilon}.
\]

Thus `B_\varepsilon` kills the actual secant direction `(1,s+t)` and

\[
B_\varepsilon\in\mathcal C_S.
\]

Hence

\[
B_\varepsilon\to B,
\qquad
B\notin\mathcal C_S,
\]

showing concretely that `\mathcal C_S` need not be closed. Exact injectivity can survive at a map that is arbitrarily close to noninjective maps, while stable fidelity correctly records zero robustness.

This is the operator-space version of AF-043's geometric distinction:

\[
\text{actual secant avoidance}
\quad\not\Rightarrow\quad
\text{uniform closed-secant separation}.
\]

## Condition-number interpretation

The equality

\[
\kappa_S(B)
=
\operatorname{dist}(B,\Sigma_S)
\]

makes the scale-invariant ratio

\[
\operatorname{cond}_S(B)
=
\frac{\|B\|}{\kappa_S(B)}
\]

a direct distance-to-ill-posedness condition number.

This interpretation is stronger than merely saying that `\kappa_S(B)` lower-bounds perturbation tolerance. The radius is sharp:

- every perturbation of norm strictly less than `\kappa_S(B)` preserves stable fidelity;
- some rank-one perturbation of norm exactly `\kappa_S(B)` destroys it;
- an exact collision can be approached at the same radius;
- a nearest exact collision exists precisely when an actual secant attains the restricted minimum.

For a linear carrier `S=M` that is itself a subspace, AF-043 reduces `K_S` to the unit sphere of `M`; the formula then becomes the familiar smallest restricted singular value / distance-to-singularity geometry. For a nonlinear carrier, the closed secant set replaces the whole unit sphere and identifies exactly which directions matter for recoverability of that carrier.

## Prior art and novelty assessment

The distance-to-instability mechanism is classical, and this finding does **not** claim novelty for the rank-one perturbation argument or the condition-number principle.

- Vincent Roulet, Nicolas Boumal, and Alexandre d'Aspremont, **“Computational complexity versus statistical performance on sparse recovery problems,”** *Information and Inference: A Journal of the IMA* 9(1) (2020), 1–32, DOI `10.1093/imaiai/iay020`, especially Definition 3.1 and Lemma 3.1. Role: direct prior art. For a closed cone `C`, they identify distance to feasibility with the minimal conically restricted singular value `min_{x\in C,\|x\|=1}\|Ax\|` and prove the upper bound with the same rank-one perturbation `-Azz^T`. Taking the closed cone generated by `K_S` places the stable-distance identity above directly inside this classical conic framework.
- James Renegar, **“Incorporating Condition Measures into the Complexity Theory of Linear Programming,”** *SIAM Journal on Optimization* 5(3) (1995), 506–524, DOI `10.1137/0805026`. Role: foundational distance-to-ill-posedness condition-measure framework; the ratio `\|B\|/\operatorname{dist}(B,\Sigma_S)` is explicitly Renegar-style rather than a new concept of conditioning.
- Carl Eckart and Gale Young, **“The Approximation of One Matrix by Another of Lower Rank,”** *Psychometrika* 1(3) (1936), 211–218, DOI `10.1007/BF02288367`. Role: classical matrix-nearness background underlying the ordinary smallest-singular-value specialization of the distance-to-rank-loss principle.
- D. S. Broomhead and M. Kirby, **“A New Approach to Dimensionality Reduction: Theory and Algorithms,”** *SIAM Journal on Applied Mathematics* 60(6) (2000), 2114–2142, DOI `10.1137/S0036139998338583`, together with Gilles Puy, Michael Davies, and Rémi Gribonval, **“Linear embeddings of low-dimensional subsets of a Hilbert space to R^m,”** EUSIPCO 2015, 469–473, DOI `10.1109/EUSIPCO.2015.7362427`. Role: direct prior art for judging linear embeddings by their action on secant directions and for restricted-isometry control on a carrier's secant set.

The exact stable-distance theorem is therefore best regarded as a **classical conic condition theorem specialized to AF-043's closed secant carrier**. The durable Arithmetic Fidelity content is the resulting three-way identification

\[
\boxed{
\text{closed-secant modulus}
=
\text{distance to stable fidelity loss}
=
\text{distance to the closure of exact collisions},
}
\]

plus the attainment criterion that distinguishes actual from limiting secants. This is useful because it turns the line's qualitative compression vocabulary into a sharp perturbation geometry without overstating novelty.

## Boundaries and downstream implication

- The exact rank-one formula uses finite-dimensional Euclidean source/target spaces and their induced operator norm. Other Banach norms require the corresponding dual functional geometry and need not retain this exact formula unchanged.
- `\kappa_S(B)` measures metric stability of the representation of the declared carrier `S`; it does not by itself show that the surviving information is the discriminator relevant to a later arithmetic or RH claim.
- Nonlinear downstream transformations are not covered merely by linearizing them. AF-007 and AF-042 show that local differential fidelity and global collision fidelity remain distinct unless additional global hypotheses close the gap.
- For noncompact or scale-growing carriers, AF-043's far-field secants remain essential. A positive finite-stage condition number does not imply a uniform asymptotic condition number.
- The theorem supplies a practical stopping rule for linear compression proposals: if the relevant closed secant carrier approaches the downstream kernel, the condition number diverges and arbitrarily small operator perturbations can destroy stable recovery even when exact collisions have not yet occurred.

No RH consequence follows from this classification alone. Its role is to make the robustness of a proposed information-preserving compression quantitatively falsifiable before a later analytic, spectral, positivity, or asymptotic step is trusted.
