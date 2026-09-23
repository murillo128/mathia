# AF-527 — Co-tuned tail multipliers hide anchor scale to all algebraic orders

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `NEGATIVE/OBSTRUCTION` · `ARITHMETIC-FIDELITY` · `DIRICHLET-SOURCE` · `OUTWARD-TRANSPORT` · `MATCHED-COMPOSITE-CONTROL` · `MESOSCOPIC-CURVATURE` · `LOWER-ORDER-FIDELITY` · `NO-NOVELTY-CLAIM`

## Claim

AF-526 showed that, with the same tail multiplier, power-separated anchor cutoffs have asymptotically equal first boundary-layer curvature defects. Allowing the multiplier itself to co-vary creates a stronger obstruction: the **renormalized first curvature defect can be matched to beyond every algebraic order in `1/log log A`** while the retained source supports remain different.

Let

\[
P(s)=\sum_{p\in\mathbb P}p^{-s},
\qquad
\kappa_P(s)=(\log P(s))'',
\]

fix `\theta\in(0,1)`, and for integer `A\to\infty` put

\[
B_A=\lfloor A^\theta\rfloor,
\qquad
L_A=\log A,
\qquad
H_A=\log L_A,
\]

with `L_B=\log B_A` and `H_B=\log L_B`. Let `B_1` denote the Meissel--Mertens constant for prime reciprocals,

\[
\sum_{p\le x}\frac1p
=
\log\log x+B_1+O\!\left(\frac1{\log x}\right).
\tag{1}
\]

Choose

\[
c_A=\left\lfloor e^{\sqrt{H_A}}\right\rfloor,
\qquad
C_A=c_A+1,
\tag{2}
\]

and let `d_A` be a nearest integer to

\[
c_A\frac{H_A+B_1}{H_B+B_1},
\qquad
\widetilde C_A=d_A+1.
\tag{3}
\]

For sufficiently large `A`, both multipliers are integers at least two. Define the two positive unit-weight anchored tail transports

\[
Q_A^{(A)}(s)
=
\sum_{p\le A}p^{-s}
+
C_A^{-s}\sum_{p>A}p^{-s},
\tag{4}
\]

and

\[
Q_A^{(B)}(s)
=
\sum_{p\le B_A}p^{-s}
+
\widetilde C_A^{-s}\sum_{p>B_A}p^{-s}.
\tag{5}
\]

On the common boundary layer

\[
W_A=(0,1/A],
\qquad s=1+t,
\]

write

\[
\Delta_A^{(A)}(t)
=
1-\frac{\kappa_{Q_A^{(A)}}(1+t)}{\kappa_P(1+t)},
\]

\[
\Delta_A^{(B)}(t)
=
1-\frac{\kappa_{Q_A^{(B)}}(1+t)}{\kappa_P(1+t)}.
\tag{6}
\]

Then for every fixed integer `m\ge1`,

\[
\boxed{
\sup_{0<t\le1/A}
H_A^m
\left|
\frac{\Delta_A^{(B)}(t)}{\Delta_A^{(A)}(t)}-1
\right|
\longrightarrow0.
}
\tag{7}
\]

Thus the relative mismatch of the first nonzero curvature defects is **super-algebraically small in `H_A=\log\log A`**. The two controls nevertheless have different source provenance: for all sufficiently large `A` there are primes in `(B_A,A]`; such a prime is retained in `(4)` but transported to an ordinary composite atom in `(5)`.

Equation `(7)` is stronger than AF-526's first-order collision. Once the multiplier is allowed to co-vary with the unknown anchor, every finite algebraic-order observation in `1/H_A` of this renormalized defect collides for the explicit matched-control pair `(4)`--`(5)`. A discriminator for this broader family must therefore use either a beyond-all-orders/nonperturbative distinction, an independently fixed transport scale, or additional source-derived structure.

## Derivation

### 1. The exact AF-525 defect carrier

For a cutoff `X` and integer multiplier `C\ge2`, AF-525 isolates the exact anchor-to-transport carrier

\[
\mathcal D_{X,C}(t)
=
\bigl(C^{1+t}-1\bigr)
\frac{B_0(X,t)}{P(1+t)},
\qquad
B_0(X,t)=\sum_{p\le X}p^{-1-t}.
\tag{8}
\]

The two controls in `(4)`--`(5)` therefore have carriers

\[
\mathcal D_A(t)=\mathcal D_{A,C_A}(t),
\qquad
\widetilde{\mathcal D}_A(t)
=\mathcal D_{B_A,\widetilde C_A}(t).
\]

Their ratio is exactly

\[
\frac{\widetilde{\mathcal D}_A(t)}{\mathcal D_A(t)}
=
\frac{\widetilde C_A^{1+t}-1}{C_A^{1+t}-1}
\frac{B_0(B_A,t)}{B_0(A,t)}.
\tag{9}
\]

Unlike AF-526, the multiplier factor no longer cancels. We tune it against the coarse Mertens mass of the retained anchor.

### 2. Mertens mass is accurate beyond every power of `1/H_A`

The classical reciprocal-prime estimate `(1)` gives

\[
S(X):=\sum_{p\le X}\frac1p
=
\log\log X+B_1+O(1/\log X).
\tag{10}
\]

For `0<t\le1/A`, the elementary bound `0\le1-e^{-u}\le u` gives

\[
\left|B_0(X,t)-S(X)\right|
\le
 t\sum_{p\le X}\frac{\log p}{p}.
\tag{11}
\]

Mertens' weighted prime estimate

\[
\sum_{p\le X}\frac{\log p}{p}=O(\log X)
\tag{12}
\]

therefore yields, uniformly on `W_A`,

\[
B_0(A,t)
=
H_A+B_1+O(L_A^{-1})+O(L_A/A),
\tag{13}
\]

and, since `L_B\sim\theta L_A`,

\[
B_0(B_A,t)
=
H_B+B_1+O(L_A^{-1})+O(L_A/A).
\tag{14}
\]

Because `L_A=e^{H_A}` and `A=e^{L_A}`, both errors in `(13)`--`(14)` are smaller than `H_A^{-m}` for every fixed `m`. More precisely, after division by `H_A+B_1` or `H_B+B_1`,

\[
\frac{B_0(A,t)}{H_A+B_1}=1+o(H_A^{-m}),
\qquad
\frac{B_0(B_A,t)}{H_B+B_1}=1+o(H_A^{-m})
\tag{15}
\]

uniformly on `W_A`, for every fixed `m\ge1`.

### 3. Integer multiplier tuning is also super-algebraically accurate

By nearest-integer choice in `(3)`,

\[
\frac{d_A}{c_A}
=
\frac{H_A+B_1}{H_B+B_1}
+O(c_A^{-1}).
\tag{16}
\]

Since

\[
c_A=e^{\sqrt{H_A}}(1+o(1)),
\]

we have

\[
c_A^{-1}=o(H_A^{-m})
\tag{17}
\]

for every fixed `m`.

For any `C\ge2` and sufficiently small nonnegative `t`,

\[
C^{1+t}-1
=(C-1)\bigl(1+O(t\log C)\bigr),
\tag{18}
\]

uniformly when `t\log C\to0`. Here

\[
\log C_A,\ \log\widetilde C_A=O(\sqrt{H_A}),
\]

so on `W_A`,

\[
t\log C_A+t\log\widetilde C_A
=O\!\left(\frac{\sqrt{H_A}}{A}\right)
=o(H_A^{-m})
\tag{19}
\]

for every fixed `m`. Combining `(16)`--`(19)`,

\[
\frac{\widetilde C_A^{1+t}-1}{C_A^{1+t}-1}
=
\frac{H_A+B_1}{H_B+B_1}
\bigl(1+o(H_A^{-m})\bigr)
\tag{20}
\]

uniformly on `W_A` for every fixed `m`.

Substituting `(15)` and `(20)` into the exact ratio `(9)` gives

\[
\boxed{
\sup_{t\in W_A}
H_A^m
\left|
\frac{\widetilde{\mathcal D}_A(t)}{\mathcal D_A(t)}-1
\right|
\longrightarrow0
}
\tag{21}
\]

for every fixed `m`. The cancellation uses only the coarse anchor statistic `H+B_1` and integer rounding; it does not use the exact prime list below either cutoff.

### 4. Both controls remain in the AF-525 boundary-layer regime

From `(2)`,

\[
C_A\sim e^{\sqrt{H_A}},
\]

and `(3)` gives `\widetilde C_A\asymp C_A` because `H_B=H_A+\log\theta+o(1)`. Hence

\[
\frac{C_AH_A}{L_A}
\ll
H_Ae^{-H_A+\sqrt{H_A}}
\to0,
\tag{22}
\]

while

\[
\frac{\widetilde C_AH_B}{L_B}
\ll
H_Ae^{-H_A+\sqrt{H_A}}
\to0.
\tag{23}
\]

Thus AF-525 applies to both controls. The second control's natural layer `(0,1/B_A]` contains `W_A`, so both may be compared on the same observed window.

For `(7)`, however, the qualitative `o(1)` statement of AF-525 is not enough; its exact moment proof must be retained quantitatively.

### 5. The curvature-to-carrier error is itself beyond all algebraic orders

Use AF-525's notation at a generic admissible cutoff `X`:

\[
\rho_0=\eta(1+\mathcal D),
\qquad
\rho_1=\eta(1+E_1),
\qquad
\rho_2=\eta(1+E_2),
\tag{24}
\]

and

\[
r(t)=
\frac{(M_1^P(1+t))^2}{M_0^P(1+t)M_2^P(1+t)}.
\]

Write

\[
a=E_2/\mathcal D,
\qquad
b=E_1/\mathcal D.
\]

The exact three-moment identity used in AF-525 gives, with

\[
\Delta=1-\kappa_Q/\kappa_P,
\]

the exact formula

\[
\frac{\Delta}{\mathcal D}
=
\frac{
(1-a)(1+\mathcal D)
-r(1-b)\bigl(2+\mathcal D(1+b)\bigr)
}
{(1-r)(1+\mathcal D)^2}.
\tag{25}
\]

AF-525's estimates imply uniformly on the full boundary layer at cutoff `X` that

\[
r=O(1/\log X),
\tag{26}
\]

\[
\mathcal D=O\!\left(\frac{C\log\log X}{\log X}\right),
\tag{27}
\]

\[
\frac{E_1}{\mathcal D}
=O\!\left(\frac{(\log X)^2}{X\log\log X}\right),
\tag{28}
\]

and

\[
\frac{E_2}{\mathcal D}
=O\!\left(
\frac{\log X}{X\log\log X}
+
\frac{(\log X)^3}{X^2\log\log X}
\right).
\tag{29}
\]

For `X=A`, `C=C_A`; for `X=B_A`, `C=\widetilde C_A`. Under `(2)`--`(3)`, every quantity on the right of `(26)`--`(29)`, as well as `(27)`, is `o(H_A^{-m})` for every fixed `m`. Expanding only the elementary rational expression `(25)` around these small quantities therefore gives

\[
\boxed{
\sup_{t\in W_A}
H_A^m
\left|
\frac{\Delta_A^{(A)}(t)}{\mathcal D_A(t)}-1
\right|
\to0,
}
\tag{30}
\]

and

\[
\boxed{
\sup_{t\in W_A}
H_A^m
\left|
\frac{\Delta_A^{(B)}(t)}{\widetilde{\mathcal D}_A(t)}-1
\right|
\to0
}
\tag{31}
\]

for every fixed `m`.

Finally,

\[
\frac{\Delta_A^{(B)}}{\Delta_A^{(A)}}
=
\frac{\Delta_A^{(B)}}{\widetilde{\mathcal D}_A}
\frac{\widetilde{\mathcal D}_A}{\mathcal D_A}
\frac{\mathcal D_A}{\Delta_A^{(A)}}.
\tag{32}
\]

Equations `(21)`, `(30)`, and `(31)` prove `(7)`.

## Fidelity and matched-control audit

The controls are still highly constrained. Both begin from the same rational-prime source, retain an exact initial prime segment, move the remaining source atoms only outward by one integer multiplier, preserve positive unit coefficients, and send every transported prime to an ordinary composite atom. No external marker or arbitrary reweighting is added.

The extra freedom relative to AF-526 is only that the multiplier may depend on the cutoff. That freedom is enough to cancel the retained zeroth-moment anchor mass with super-algebraic precision. The tuning rule uses `H+B_1`, a universal asymptotic statistic of the cutoff, and nearest-integer rounding; it does not inspect which primes are actually present below the cutoff.

This is therefore a stronger representation collision rather than an equality of sources. The common observation is the renormalized first boundary-layer curvature defect, and the collision holds at every finite algebraic order in `1/H_A`. Exact full curvature remains more informative.

## Representation audit

The source provenance parameters are now the pair `(X,C)`: anchor cutoff and rigid outward transport multiplier. The observed representation is the first nonzero normalized curvature defect on the shrinking layer `W_A`.

AF-525 showed that with `X` known, this defect recovers `C` to first order. AF-526 showed that with `C` fixed, changing `X` from `A` to `A^\theta` is invisible at leading relative order because the carrier factors through `\log\log X`. AF-527 closes the next obvious escape: if both provenance parameters are unknown, the multiplier can compensate the entire algebraic asymptotic content of the coarse Mertens anchor mass.

The correct statement is **super-algebraic indistinguishability of the renormalized defect**, not equality of complete profiles and not an assertion that the source itself has only one asymptotic invariant. A beyond-all-orders residual may still distinguish the two controls, and another source-derived observable may expose the cutoff immediately.

## Prior art and novelty assessment

No novelty is claimed for the analytic-number-theory ingredients.

- J. Barkley Rosser and Lowell Schoenfeld, **“Approximate formulas for some functions of prime numbers,”** *Illinois Journal of Mathematics* 6(1), 64–94 (1962), DOI `10.1215/ijm/1255631807`, gives classical explicit estimates for prime sums, including the reciprocal-prime Mertens law used to obtain a quantitative remainder in `(10)`.
- The weighted estimate `(12)` is classical Mertens theory. The prime-zeta singularity and moment estimates used through AF-525 remain those already audited in AF-523--AF-525.
- Generic language about super-algebraic or beyond-all-orders agreement is classical asymptotic-analysis terminology; no new general theorem about asymptotic expansions is claimed here.

A literature search around prime-zeta curvature, Mertens prime sums, matched asymptotics, and beyond-all-orders agreement found the standard ingredients but no established theorem matching this particular tuned anchored-tail transport comparison. The Arithmetic-Fidelity content is the explicit no-go construction obtained by composing those classical estimates with AF-525's exact curvature carrier. It should be treated as a derived obstruction inside this source/representation class, not as a novelty claim about Mertens theory.

## Boundaries

- Equation `(7)` concerns the **relative first curvature defect** on `0<t\le1/A`. It does not assert equality of the exact curvature profiles.
- The result is a deliberately tuned adversarial control. It does not say that naturally chosen multipliers at different cutoffs automatically agree to all algebraic orders.
- The multiplier is allowed to co-vary with the cutoff. If the transport scale is fixed independently or observed separately, this obstruction does not apply.
- The tuning uses the universal constant `B_1`. Replacing it by only the leading term `H` recovers AF-526-type first-order matching but not the super-algebraic statement proved here.
- Super-algebraic agreement in `H_A` does not exclude exponentially or otherwise beyond-all-orders small distinctions, nor does it preclude recovery from a different observable.
- AF-509--AF-510's exact fixed-source curvature recovery results are untouched: this finding concerns a shrinking-window asymptotic representation of a varying source family.
