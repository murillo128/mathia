# PL-439 — Four real signed-residue energies recover the mod-5 oriented defect with exact diagonal cancellation

**Evidence/status:** `EXACT-DERIVED + SOURCE-OBSERVABLE-REDUCTION + LITERATURE-CALIBRATED`.

**Parent findings:** `PL-421`, `PL-428`, `PL-432`, `PL-436`, `PL-437`, `PL-438`.

## Claim

`PL-438` reduces the unresolved arithmetic input in the `p=5` local-factor gate to the two real oriented coordinates

\[
s=\frac{-x_{01}+x_{03}-x_{12}+x_{23}}2,
\qquad
f=\frac{x_{01}-x_{03}-x_{12}+x_{23}}2,
\tag{1}
\]

or equivalently to

\[
g=\frac1{\sqrt2}(s-f,s+f)^T.
\tag{2}
\]

Those coordinates look like genuinely complex character-covariance data in `PL-437`/`PL-438`. On the **source side**, however, they have an exact realization using only four ordinary real scalar energies of fixed signed residue combinations.

Let

\[
R(y)=(R_0(y),R_1(y),R_2(y),R_3(y))^T\in\mathbb R^4
\tag{3}
\]

be the already-centered real residue signal in the established order `(1,2,4,3)`, and let

\[
S=\int R(y)R(y)^T\,d\mu(y)
=(x_{jk})_{0\le j,k\le3},
\tag{4}
\]

with `x_{jj}=D_j`. For every real coefficient vector `w`, define its scalar energy

\[
J(w):=\int (w^TR(y))^2\,d\mu(y)=w^TSw.
\tag{5}
\]

Introduce

\[
P=e_0+e_2,
\qquad
U=e_0-e_2,
\qquad
V=e_3-e_1.
\tag{6}
\]

Then direct expansion gives

\[
P^TSV=2s,
\qquad
U^TSV=-2f.
\tag{7}
\]

The real polarization identity therefore yields the exact formulas

\[
\boxed{
 s=\frac18\Bigl[
 J(1,-1,1,1)-J(1,1,1,-1)
 \Bigr],
}
\tag{8}
\]

and

\[
\boxed{
 f=\frac18\Bigl[
 J(1,1,-1,-1)-J(1,-1,-1,1)
 \Bigr].
}
\tag{9}
\]

Every one of the four probe vectors in (8)--(9) has coordinate squares identically equal to `1`. Consequently each scalar energy contains **the same full diagonal contribution**

\[
D_0+D_1+D_2+D_3,
\tag{10}
\]

and that contribution cancels exactly inside each paired difference. Thus the two oriented coordinates required by the Schur ellipse are not hidden behind four independent diagonal-variance estimates: they are exactly two signed differences of real short-interval energies whose self-energy cancels algebraically.

This is a representation/source-observable refinement, not an arithmetic estimate. Current audited variance results do not yet control the two differences (8)--(9) at the variance scale required by `PL-438` for the actual fixed-mod-5 prime source.

## 1. Exact polarization derivation

From (6),

\[
P^TSV
=(e_0+e_2)^TS(e_3-e_1)
=x_{03}-x_{01}+x_{23}-x_{12}.
\tag{11}
\]

Using the definition of `s` in (1),

\[
x_{03}-x_{01}+x_{23}-x_{12}=2s.
\tag{12}
\]

Similarly,

\[
U^TSV
=(e_0-e_2)^TS(e_3-e_1)
=x_{03}-x_{01}-x_{23}+x_{12}=-2f.
\tag{13}
\]

For arbitrary real vectors `a,b`, symmetry of `S` gives

\[
J(a+b)-J(a-b)=4a^TSb.
\tag{14}
\]

Applying (14) first to `(P,V)` gives

\[
J(P+V)-J(P-V)=8s.
\tag{15}
\]

Since

\[
P+V=(1,-1,1,1),
\qquad
P-V=(1,1,1,-1),
\tag{16}
\]

this proves (8). Applying (14) to `(U,V)` and reversing the order of the two energies gives

\[
J(U-V)-J(U+V)=-4U^TSV=8f,
\tag{17}
\]

with

\[
U-V=(1,1,-1,-1),
\qquad
U+V=(1,-1,-1,1),
\tag{18}
\]

which proves (9).

No positivity, asymptotic, Euler product, analytic continuation, or RH hypothesis enters this derivation. It is a finite covariance identity on exactly the residue signal already used by `PL-421` and `PL-438`.

## 2. Why the diagonal cancellation matters

For a sign vector `w in {+1,-1}^4`, expansion of (5) gives

\[
J(w)
=\sum_{a=0}^3D_a
+2\sum_{0\le a<b\le3}w_aw_bx_{ab}.
\tag{19}
\]

Hence every probe in (8)--(9) has exactly the same self-correlation term. The differences isolate cross-residue information before any analytic estimate is used.

This is stronger than merely saying that arbitrary real polarization can recover a covariance matrix. The live `PL-438` fiber needs only two particular cross-residue asymmetries, and both admit paired `\{\pm1\}` probes for which **all four diagonal terms cancel identically even when the residue variances are unequal**.

For the Schur ellipse, one may therefore regard

\[
\Delta_s
:=J(1,-1,1,1)-J(1,1,1,-1)=8s,
\tag{20}
\]

and

\[
\Delta_f
:=J(1,1,-1,-1)-J(1,-1,-1,1)=8f
\tag{21}
\]

as the two load-bearing source observables. A theorem estimating the four individual energies to high relative precision would suffice, but is stronger than necessary: only the two **paired differences** need the precision required by the ellipse.

This distinction is potentially important because each `J(w)` may live at the natural Selberg variance scale while the desired oriented difference can be smaller through arithmetic cancellation. Estimating the two large terms separately and subtracting them is therefore not automatically well-conditioned. The theorem target should be the signed differences themselves whenever possible.

## 3. Relation to the character-side information obstruction

There is no contradiction with `PL-428`, which proves that real scalar/product probes in the **character basis** do not determine the imaginary coherences of the character covariance.

A real residue vector `w` transforms under the mod-5 Fourier matrix to a generally **complex** coefficient vector on the four character channels. Thus the scalar residue energies in (8)--(9) are real and positive as physical-space quantities, while their character-space polarizations are precisely complex enough to see the orientation that a real character coefficient vector misses.

Equivalently, the DFT conjugate symmetry of a real residue signal does not erase the missing phases; it packages them into relative energies of different real residue sign patterns. The `PL-437` coordinates

\[
\Im(K_{01}+K_{21}),
\qquad
\Im K_{13}
\tag{22}
\]

become the two physical-space covariance asymmetries in (7).

This also clarifies the role of the quarter-turn tomography in `PL-431`--`PL-432`. A shrinking vertical displacement remains a useful way to expose the same oriented information when one insists on standard character-product observables or on the zero/Dirichlet-series side. It is **not intrinsically required to define or measure `g` on the real residue-source side** once arbitrary fixed signed residue combinations are admissible.

## 4. Source interpretation and centering boundary

Equations (8)--(9) apply to the already-centered residue signal `R` of `PL-438`. For the prime source, each `J(w)` is therefore a Selberg-type moving short-interval energy of a fixed bounded `5`-periodic signed residue weight, with the same deterministic centering convention used to construct `R`.

The distinction between centered and raw prime counts is load-bearing. Two of the sign vectors in (8)--(9) have nonzero average over the reduced residue classes, while the other two have zero average. One must therefore transport the principal deterministic subtraction coherently, exactly as `PL-423` and `PL-432` require. The formulas above do not license replacing `R` by raw residue prime counts without adjusting the center.

Once the centering is fixed, however, no new representation issue remains: all four probes are ordinary real scalar energies of explicit fixed linear combinations of the same four residue channels. They introduce neither a new modulus nor an `X`-dependent test vector.

## 5. What theorem would now suffice for the oriented part

On the strict visible branch of `PL-438`, the exact local-factor admission criterion is

\[
(g-\mu)^TE^{-1}(g-\mu)\le\alpha,
\tag{23}
\]

with `E,mu,alpha` determined by the visible real-product sector and the residue diagonal. Equations (8)--(9) give `g` exactly from `Delta_s,Delta_f`.

Therefore the unresolved source theorem can be stated without a full complex covariance asymptotic. It is enough to control the two-dimensional vector

\[
\boxed{
 g=\frac1{8\sqrt2}
 \begin{pmatrix}
 \Delta_s-\Delta_f\\
 \Delta_s+\Delta_f
 \end{pmatrix}
}
\tag{24}
\]

relative to the already-visible ellipse data strongly enough to prove (23).

In an approximately residue-symmetric regime where `mu` is negligible and the visible matrix `E` has a quantitative variance-scale margin, a sufficient route would be variance-scale control of `Delta_s` and `Delta_f`. In the general anisotropic regime the correct target is not separately `Delta_s,Delta_f=o(variance)`, but the source-adapted quadratic combination obtained by substituting (24) into (23).

This is strictly weaker information than the arbitrary-complex-direction lower-frame theorem isolated in `PL-436`, and more source-explicit than the abstract `(s,f)` target in `PL-437`/`PL-438`. It does **not** establish that the needed signed-energy differences satisfy the required bound.

## 6. Prior-art and novelty audit

The algebraic ingredients are classical. The real polarization identity (14), covariance matrices, Fourier change of basis, and cancellation of diagonal terms between equal-modulus sign probes are standard and carry no novelty claim.

The relevant analytic prior art is already audited in `PL-434`--`PL-436`:

- MRSTT (2026) supplies extremely strong almost-all short-interval control for the exact multiplicative quarter-turn twist and fixed arithmetic progressions, but `PL-434` shows that the published estimate is still at the wrong `L^2` scale for covariance transfer.
- MRSTT's almost-all Hardy--Littlewood theorem reaches the two-point correlation itself, but `PL-435` shows that its published leading-order precision does not yield the required triangular Selberg residual.
- de la Bretèche--Fiorilli, Goldston--Yildirim, Harper--Soundararajan and related variance results provide substantial scalar/AP lower-bound technology, but `PL-436` records that the unconditional fixed-modulus oriented covariance needed here is not supplied by those theorems.

A targeted current-literature search for mixed/signed fixed-modulus short-interval prime variances and Dirichlet-character covariance did not locate an unconditional theorem that directly estimates the two fixed signed-residue differences (20)--(21) at the required variance scale. Standard mixed moments of Dirichlet `L`-functions are not the same object, and general polarization does not provide the arithmetic estimate.

The durable line-specific delta is therefore not a new polarization theorem. It is the **minimal source-observable reduction of the accepted `PL-438` Schur-ellipse clue**: the entire remaining oriented vector is exactly encoded by two differences of four explicit real `\{\pm1\}` residue energies, with automatic cancellation of all diagonal self-energy.

## 7. Adversarial audit and boundaries

1. **Exact recovery is not smallness.** Equations (8)--(9) determine `s,f`; they do not bound them. The `PL-428` matched controls still show that the oriented fiber can move the cone verdict while all previously visible data are fixed.

2. **A difference of positive energies need not be easy to estimate.** Each `J(w)` can be large while `Delta_s` or `Delta_f` is a lower-order residual. Proving the paired difference at the required scale may be as delicate as a mixed covariance theorem. The reduction identifies the exact scalar target; it does not claim improved number-theoretic technology.

3. **The four probes are source-real, not character-real.** Their Fourier coefficients are generally complex. This is why they evade the information-theoretic obstruction of `PL-428`; treating them as ordinary real coefficient vectors in the character basis would be incorrect.

4. **Centering must be inherited from the canonical source.** Inserting raw prime counts into (8)--(9) without the principal deterministic subtraction can create additional main terms. All identities here are for the centered `R` used by the parent gate.

5. **Diagonal cancellation does not cancel visible off-diagonal structure.** Equations (20)--(21) isolate particular signed cross-residue combinations, not a pure noise term. Their main terms, if any, have to be computed or bounded arithmetically.

6. **The Schur center may be nonzero.** The actual gate depends on `g-mu`, not simply on `g`. In an asymmetric source, proving `g` small can be the wrong target; the useful theorem may instead show that the signed-energy vector tracks the visible center `mu`.

7. **No full variance asymptotic is required by representation, but one may still be required by available methods.** The finite-dimensional reduction does not guarantee that analytic techniques can prove only the paired differences without first proving stronger individual covariance estimates.

8. **No RH/GRH input is imported.** The derivation is finite-dimensional and unconditional. Conditional fixed-AP variance results remain calibration only and cannot close the prime-lattice RH route non-circularly.

## Consequence for the line

The accepted `PL-438` direction now has a sharper arithmetic surface. The unresolved oriented input should no longer be described merely as two complex character coherences or as a need for quarter-turn tomography. On the actual real residue source it is exactly the pair

\[
\boxed{
\Delta_s
=J(1,-1,1,1)-J(1,1,1,-1),
\qquad
\Delta_f
=J(1,1,-1,-1)-J(1,-1,-1,1).
}
\tag{25}
\]

The next useful arithmetic pass is therefore to search for, derive, or falsify a **fixed-mod-5 signed Selberg-variance-difference estimate** strong enough that (24), together with the visible `PL-438` coefficients, satisfies the exact Schur budget (23). A theorem only for individual residue variances, total trace, or first-order progression sums still misses this target; a theorem for the two paired differences would hit it directly.