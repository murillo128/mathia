# MC-403 — Source-family lcm energy is exactly signature-discrepancy energy

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-REFINEMENT` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the source-signature and lcm setup of `MC-397`--`MC-402`. Let

\[
W\le \mathbf F_2^R,
\qquad H:=|W|,
\qquad \Omega:=\widehat W,
\]

and let

\[
\Phi:(\mathbf Z/P\mathbf Z)^\times\to\Omega
\]

be the surjective source-signature map of `MC-397`, so that for each source mode `I\in W` and each integer `n` coprime to `P`,

\[
\chi_I(n)=\Phi(n)(I).
\]

Keep the lcm-fiber coefficient

\[
C_g(\ell)
=\sum_{\substack{d,e\le B\\[d,e]=\ell}}g(d)g(e)
\]

from `MC-398`, and for a positive integer `X` define

\[
A_I(X):=\sum_{\ell\le X}C_g(\ell)\chi_I(\ell).
\tag{1}
\]

For each signature `\omega\in\Omega`, define the signed lcm mass

\[
\boxed{
B_\omega(X)
:=
\sum_{\substack{\ell\le X\\(\ell,P)=1\\\Phi(\ell)=\omega}}
C_g(\ell).
}
\tag{2}
\]

Then the whole source family is exactly the finite Fourier transform of the signature-mass vector:

\[
\boxed{
A_I(X)=\sum_{\omega\in\Omega}B_\omega(X)\,\omega(I),
}
\tag{3}
\]

and therefore

\[
\boxed{
\sum_{I\in W}|A_I(X)|^2
=H\sum_{\omega\in\Omega}|B_\omega(X)|^2.
}
\tag{4}
\]

Let `0\in W` denote the trivial source mode and put

\[
\overline B(X):=\frac{A_0(X)}H
=\frac1H\sum_{\omega\in\Omega}B_\omega(X).
\]

Subtracting the trivial Fourier coefficient from `(4)` gives the sharper identity

\[
\boxed{
\sum_{I\in W\setminus\{0\}}|A_I(X)|^2
=
H\sum_{\omega\in\Omega}
|B_\omega(X)-\overline B(X)|^2.
}
\tag{5}
\]

Thus a collective `L^2` saving over the nontrivial source modes is **not an additional averaging resource beyond the source signatures**. It is exactly a signed equidistribution/discrepancy theorem for the lcm coefficient mass across the `H` source-signature classes. Perfect cancellation of every nontrivial source mode occurs if and only if all `B_\omega(X)` are equal.

There is also a quantitative sparsity obstruction. If

\[
S_X:=\#\{\omega\in\Omega:B_\omega(X)\ne0\}\ge1,
\]

then Cauchy--Schwarz and `(4)` imply

\[
\boxed{
\sum_{I\ne0}|A_I(X)|^2
\ge
\left(\frac{H}{S_X}-1\right)|A_0(X)|^2.
}
\tag{6}
\]

Since at most one signature is contributed by each positive integer `\ell\le X`,

\[
S_X\le \min(H,X),
\tag{7}
\]

so whenever `X<H` and `A_0(X)\ne0`,

\[
\boxed{
\sum_{I\ne0}|A_I(X)|^2
\ge
\left(\frac HX-1\right)|A_0(X)|^2.
}
\tag{8}
\]

This does not give an upper bound or a Möbius estimate. It shows instead that **signature sparsity is the opposite of a free source-family gain**: unless the principal signed mass is itself small, concentrating the lcm coefficient on few signatures forces nontrivial source-mode energy.

Finally, combining the same finite Fourier transform with the truncated-incidence identity of `MC-402` gives an exact normal form for the remaining collective branch. Define

\[
J_\omega(n;B)
:=
\sum_{\substack{d,e\le B\\d\mid n,\ e\mid n\\([d,e],P)=1\\\Phi([d,e])=\omega}}
 g(d)g(e),
\tag{9}
\]

and

\[
\overline J(n;B):=\frac1H\sum_{\omega\in\Omega}J_\omega(n;B).
\]

Then

\[
\boxed{
B_\omega(X)
=
\sum_{n\le X}
M\!\left(\left\lfloor\frac Xn\right\rfloor\right)
J_\omega(n;B),
}
\tag{10}
\]

and hence

\[
\boxed{
\sum_{I\ne0}|A_I(X)|^2
=
H\sum_{\omega\in\Omega}
\left|
\sum_{n\le X}
M\!\left(\left\lfloor\frac Xn\right\rfloor\right)
\bigl(J_\omega(n;B)-\overline J(n;B)\bigr)
\right|^2.
}
\tag{11}
\]

Equation `(11)` identifies the exact obligation left by the source-family side of the accepted retained-variable clue: after generic incidence resolution, a collective theorem must control a **Mertens-weighted signed signature-discrepancy vector**. Merely summing or averaging the source modes cannot create a second cancellation dimension; a real gain has to come from special arithmetic of the actual Selberg coefficient/source signatures, or from leaving the lcm-factorable quadratic frame.

No estimate for `M(x)` follows.

## 1. The lcm partial sums are a finite Fourier pair

For `(\ell,P)=1`, `MC-397` gives

\[
\chi_I(\ell)=\Phi(\ell)(I).
\]

For `(\ell,P)>1`, every common-modulus source character vanishes. Therefore `(1)` can be grouped by the signature `\omega=\Phi(\ell)` exactly as

\[
A_I(X)
=
\sum_{\omega\in\Omega}
\left(
\sum_{\substack{\ell\le X\\(\ell,P)=1\\\Phi(\ell)=\omega}}
C_g(\ell)
\right)\omega(I),
\]

which is `(3)`.

Character orthogonality on the finite abelian group `W` gives

\[
\sum_{I\in W}\omega(I)\overline{\omega'(I)}
=H\,\mathbf 1_{\omega=\omega'}.
\tag{12}
\]

Squaring `(3)`, summing over `I`, and applying `(12)` proves `(4)`. Equivalently, Fourier inversion gives

\[
B_\omega(X)
=
\frac1H\sum_{I\in W}A_I(X)\overline{\omega(I)}.
\tag{13}
\]

Because `W` has exponent two, all `\omega(I)` are `\pm1`, but no part of the argument needs that simplification beyond the existing quadratic source construction.

The trivial mode `I=0` satisfies `\omega(0)=1` for every `\omega`, hence

\[
A_0(X)=\sum_\omega B_\omega(X).
\tag{14}
\]

Subtracting `|A_0(X)|^2` from both sides of `(4)` and using the standard variance identity

\[
\sum_\omega|B_\omega-\overline B|^2
=
\sum_\omega|B_\omega|^2-rac1H\left|\sum_\omega B_\omega\right|^2
\]

proves `(5)`.

This is stronger than saying that source modes and signatures are two equivalent labels. For the **scale-truncated lcm coefficient itself**, `(5)` identifies the complete nonprincipal family energy with one concrete discrepancy norm. Any claimed family-level saving can therefore be checked representation-invariantly on the `B_\omega` side.

## 2. Sparse signature occupancy forces source-mode energy

Assume `S_X>0`. Cauchy--Schwarz on the support of `B(X)` gives

\[
|A_0(X)|^2
=
\left|\sum_\omega B_\omega(X)\right|^2
\le
S_X\sum_\omega|B_\omega(X)|^2.
\tag{15}
\]

Insert `(15)` into

\[
\sum_{I\ne0}|A_I|^2
=H\sum_\omega|B_\omega|^2-|A_0|^2
\]

to obtain `(6)`.

The bound `(7)` is purely combinatorial: a nonzero signature mass requires at least one integer `\ell\le X` in that signature class with nonzero `C_g(\ell)`, and there are at most `X` positive integers in the range. This yields `(8)`.

The point is not the numerical strength of `(8)` in isolation. Its role is adversarial. A proposed collective argument cannot treat **few occupied signatures** as though that were automatically a source-family saving. If the signed principal mass remains visible, sparse occupancy forces energy into nontrivial Fourier modes. The favorable regime for small nonprincipal `L^2` energy is instead near-equality of the signed class masses.

The qualification "signed" is essential. `C_g(\ell)` need not be positive. Ordinary equidistribution of the *number* of lcm values among signatures does not imply `(5)` is small; one needs control of their actual Selberg coefficients and their cancellations inside each class.

## 3. Truncation turns the same discrepancy into a Mertens-weighted one

`MC-402` gives, for every source mode `I`,

\[
A_I(X)
=
\sum_{n\le X}
M\!\left(\left\lfloor\frac Xn\right\rfloor\right)
E_I(n;B),
\tag{16}
\]

where

\[
E_I(n;B)
=
\sum_{\substack{d,e\le B\\d\mid n,\ e\mid n}}
 g(d)g(e)\chi_I([d,e]).
\]

Grouping the divisor pairs by `\omega=\Phi([d,e])` gives exactly

\[
E_I(n;B)=\sum_{\omega\in\Omega}J_\omega(n;B)\omega(I).
\tag{17}
\]

Apply Fourier inversion `(13)` to `(16)` and use `(17)`. All sums are finite, so the order may be exchanged; orthogonality leaves precisely `(10)`. Subtracting the class mean and inserting into `(5)` yields `(11)`.

Thus the generic truncated-lcm representation does not merely contain Mertens weights mode by mode, as `MC-402` showed. After the entire source family is kept together, the same weights multiply the **deviation of each signature-incidence energy from the signature mean**. The remaining collective question is consequently sharper than "average over the characters": prove cancellation in this specific signed vector-valued floor sum from actual source/Selberg structure.

A theorem of that kind would be genuinely additional information. Equation `(11)` does not say it is impossible; it says exactly what must be estimated and prevents finite Fourier averaging itself from being credited as the gain.

## 4. Prior art and novelty boundary

Equations `(3)`--`(5)`, `(12)`--`(14)` are standard finite Fourier analysis on a finite abelian group. Kiran Kedlaya's *Notes on Analytic Number Theory*, Theorem 4.10, records the finite-abelian-group character orthogonality used here: https://kskedlaya.org/ant/chap-primes-in-ap.html. Parseval/Plancherel and inversion are immediate consequences. Equation `(6)` is elementary Cauchy--Schwarz, and `(10)`--`(11)` combine that classical Fourier algebra with the classical Möbius-inversion identity already audited in `MC-402`.

A targeted mechanism-level search on 20 September 2026 found no basis for a standalone novelty claim. None is made. The durable contribution is a **Mathia frontier classification**: the lcm/source objects isolated in `MC-397`--`MC-402` admit an exact signature-space Plancherel normal form, which turns the vague possibility of "collective source-family cancellation" into the precise signed-discrepancy obligation `(5)` and, after cutoff inversion, the Mertens-weighted obligation `(11)`.

## Boundaries and falsification tests

- **This is an exact `L^2` identity, not an upper bound.** It does not prove that the signature discrepancy is small.
- **Individual modes may behave differently.** A theorem for one selected `A_I` need not control the full nonprincipal energy in `(5)`; conversely an average `L^2` bound need not give the optimal pointwise bound for every mode without an additional step.
- **The principal mass can cancel.** The lower bounds `(6)`--`(8)` may be weak or vacuous when `A_0(X)` is small. No lower bound for `A_0` is assumed.
- **Signature counts are insufficient.** The relevant quantities `B_\omega` and `J_\omega` are signed Selberg-coefficient masses, not cardinalities.
- **`MC-402` is not bypassed.** Equation `(11)` contains the Mertens staircase explicitly. Bounding it by an unavailable estimate for `M` would be circular relative to the line objective.
- **Actual source/Selberg arithmetic remains open.** A theorem forcing near-uniformity of the signed `B_\omega`, or directly controlling the vector sum in `(11)`, lies outside this obstruction and would be genuine progress.
- **A non-lcm pre-quadratic variable remains open.** Nothing here applies before the divisor-pair information has collapsed through `[d,e]`.
- **No analytic continuation or zero-free region is used.** The derivation is finite Fourier algebra plus the finite cutoff inversion of `MC-402`.
- **No Möbius or RH conclusion.** The finding only identifies the exact collective quantity that a surviving source-family mechanism must control.

## Consequence for the research line

`MC-397` showed that pointwise source-mode averaging is a signature projector; `MC-398`--`MC-402` then removed divisor-pair multiplicity, separable lcm phase, the moving hyperbola coordinate, the complete endpoint, and finally generic truncation as free information carriers.

The present result closes one remaining ambiguity in the accepted retained-variable clue. **"Cancellation across source signatures" is not a separate family dimension after lcm compression: in `L^2` it is exactly signed equidistribution of the lcm coefficient across the source-signature quotient, and under generic cutoff inversion it is exactly a Mertens-weighted signature-discrepancy problem.**

The lcm branch therefore remains alive only through a source-specific theorem that actually proves such discrepancy, or through a genuinely joint estimate that controls `(11)` without first controlling `M` itself. Otherwise the surviving escape is the already-identified pre-quadratic arithmetic variable whose phase or congruence does not factor through the lcm.