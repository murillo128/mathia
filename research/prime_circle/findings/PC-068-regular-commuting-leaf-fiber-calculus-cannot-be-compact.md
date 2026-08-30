# PC-068 — regular commuting leaf–fiber calculus cannot produce compact resolvent

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` for the regular translation-invariant leaf–fiber coupling escape left open by PC-065/PC-067.

## Claim

PC-064 identifies the compatible prime-circle refinement with the arithmetic solenoid

\[
\Sigma_{\mathbb Q}\cong\widehat{\mathbb Q},
\qquad
L^2(\Sigma_{\mathbb Q})=\overline{\operatorname{span}}\{\chi_q:q\in\mathbb Q\}.
\]

PC-065 gives the canonical leaf generator

\[
A\chi_q=2\pi q\,\chi_q,
\]

while PC-067 gives the compatible embedded inverse-square chord operator on the transverse anchor fiber `\widehat{\mathbb Z}` with multiplier

\[
\sigma(\gamma)=\frac12r(1-r),
\qquad
r\in[0,1),\quad \gamma=r\pmod1\in\mathbb Q/\mathbb Z.
\]

The restriction of the solenoid character `q\in\mathbb Q` to the anchor fiber is `q\pmod{\mathbb Z}`. Therefore the canonical translation-invariant lift of the PC-067 transverse chord energy to the full solenoid is

\[
B\chi_q=b(q)\chi_q,
\qquad
b(q)=\frac12\{q\}(1-\{q\}),
\]

where `\{q\}\in[0,1)` is the fractional part.

This apparently supplies two commuting geometric coordinates, leaf frequency and transverse chord energy. In fact it does not create an independent proper spectral direction:

\[
\boxed{
B=b_0(A/2\pi)
}
\]

in bounded Borel functional calculus, where `b_0(t)=\frac12\{t\}(1-\{t\})`. Thus every translation-invariant commuting scalar coupling of these two operators is diagonal on the same rational characters.

More decisively, let `F:\mathbb R\times[0,1/8]\to\mathbb R` be Borel and define the diagonal self-adjoint operator

\[
H_F=F(A,B),
\qquad
H_F\chi_q=E_F(q)\chi_q,
\qquad
E_F(q)=F\!\left(2\pi q,b(q)\right).
\]

If `F` is locally bounded at **even one** point

\[
\Gamma(x)=\left(2\pi x,\frac12\{x\}(1-\{x\})\right),
\qquad x\in\mathbb R\setminus\mathbb Z,
\]

then `H_F` does **not** have compact resolvent. Consequently no continuous, smooth, polynomial, or ordinary meromorphic/rational joint symbol with a regular noninteger point can turn the canonical leaf and chord data into a compact-resolvent Hamiltonian.

A compact-resolvent diagonal coupling must instead be arithmetically singular: its energy must be unbounded in every neighborhood of the dense rational-frequency curve. An exact-order/denominator term supplies this transverse discontinuity, but on the full `\mathbb Q` character set it must also be combined with archimedean growth to control integer translates; for example `|q|+\operatorname{ord}(q\bmod\mathbb Z)` has finite balls. Such order, valuation, or height data are precisely discontinuous/non-archimedean scales not supplied by regular joint functional calculus of `A` and `B`.

Thus the natural commuting repair

\[
\boxed{
\text{leaf generator}+\text{embedded transverse chord energy}
\longrightarrow
\text{regular joint spectral calculus}
\longrightarrow
\text{compact RH operator}
}
\]

is ruled out. A surviving leaf–fiber mechanism must genuinely leave this commuting multiplier class: for example through a non-translation-invariant or noncommuting coupling, old/new cross-level geometry, nonlinear matrix data before Fourier diagonalization, or another intrinsic structure that forces arithmetic properness rather than decoding it afterward.

## 1. The transverse chord multiplier is already a function of leaf frequency

From PC-064, the anchor-fiber exact sequence dualizes to

\[
0\longrightarrow\mathbb Z
\longrightarrow\mathbb Q
\longrightarrow\mathbb Q/\mathbb Z
\longrightarrow0.
\]

Hence restricting `\chi_q` to the fiber remembers exactly the residue class `q\pmod{\mathbb Z}`. Pulling the PC-067 multiplier through this quotient gives

\[
B\chi_q
=\frac12\{q\}(1-\{q\})\chi_q.
\]

But `A/(2\pi)` already has eigenvalue `q` on the same character. Therefore, on the complete Pontryagin basis,

\[
B=b_0(A/2\pi),
\qquad
b_0(t)=\frac12\{t\}(1-\{t\}).
\]

The equality is in Borel functional calculus. The quadratic periodicization `b_0` is bounded, periodic, and continuous, including at the integers where both one-sided limits are zero.

The important point is informational: **the commuting lifted chord coordinate does not enlarge the joint character label beyond `q` itself**. It can still expose exact order through the highly nonuniform rational point set, as PC-067 proves, but only set-theoretically inside a dense real spectrum.

## 2. Compact resolvent for a rational-character multiplier requires finite energy balls

For a real function `E:\mathbb Q\to\mathbb R`, consider

\[
H_E\chi_q=E(q)\chi_q
\]

with its maximal diagonal self-adjoint domain. The resolvent at `i` is

\[
(H_E-i)^{-1}\chi_q
=\frac1{E(q)-i}\chi_q.
\]

A diagonal operator on `\ell^2(\mathbb Q)` is compact exactly when its diagonal coefficients tend to zero off finite subsets. Therefore

\[
\boxed{
H_E\text{ has compact resolvent}
\iff
\forall R<\infty,
\#\{q\in\mathbb Q:|E(q)|\le R\}<\infty.
}
\]

Equivalently, the energy must define a **proper function on the discrete rational character set**. Merely tending to infinity as `|q|\to\infty` is not enough, because infinitely many rational characters lie in every bounded real interval.

This criterion recasts the pathology of PC-065. The leaf energy `(2\pi q)^2` is large at large real frequency but has infinite bounded-energy balls because `\mathbb Q` is dense. PC-067's bounded chord energy is even less proper. The question is whether their regular joint use can repair this; the next section shows it cannot.

## 3. Local boundedness at one irrational accumulation point is fatal

Fix any irrational `x\notin\mathbb Z`. Choose distinct rationals `q_j\to x`. Since fractional part is continuous in a neighborhood of a noninteger point,

\[
\left(2\pi q_j,b(q_j)\right)
\longrightarrow
\Gamma(x)
=
\left(2\pi x,\frac12\{x\}(1-\{x\})\right).
\]

Suppose `F` is locally bounded at `\Gamma(x)`. Then there are a neighborhood `U` of `\Gamma(x)` and `M<\infty` such that

\[
|F(u,v)|\le M
\qquad ((u,v)\in U).
\]

For all sufficiently large `j`,

\[
|E_F(q_j)|
=
\left|F\!\left(2\pi q_j,b(q_j)\right)\right|
\le M.
\]

The distinct orthogonal eigenvectors `\chi_{q_j}` therefore give infinitely many states in one bounded energy window. By the criterion above,

\[
\boxed{
(H_F-i)^{-1}\text{ is not compact}.
}
\]

Nothing special about the chosen irrational point was used. Hence compact resolvent would require `F` to fail local boundedness at **every** point of the noninteger curve `\Gamma(\mathbb R\setminus\mathbb Z)`. That excludes any ordinary continuous or locally regular scalar symbol.

The same argument survives any pole or singularity set that leaves at least one regular noninteger point of `\Gamma`; in particular finitely many isolated poles and ordinary rational/meromorphic symbols regular somewhere on `\Gamma` still fail. A symbol singular along the whole rational-frequency accumulation curve has deliberately left the regular class and is exactly the kind of arithmetic/irregular escape considered below.

## 4. Why obvious combined energies do not help

A tempting response to PC-065 and PC-067 is to combine terms that separately control large and small real frequencies. For example, away from `q=0`, one might try

\[
E(q)=(2\pi q)^2+\frac{b(q)}{(2\pi q)^2}
\]

or a polynomial/rational variant. Such a function can diverge as `q\to0` and as `|q|\to\infty`, but it is still bounded on all rationals sufficiently close to any fixed irrational `x`, say `x=\sqrt2/2`. Hence it still has infinitely many bounded-energy eigenvectors and noncompact resolvent.

The obstruction is therefore not merely the soft sequence `q=1/n` emphasized in PC-065/067. It is the stronger topological fact

\[
\boxed{
\mathbb Q\text{ is dense in the archimedean leaf-frequency axis.}
}
\]

Any finite-valued regular function of the canonical commuting geometric coordinates is locally blind to rational arithmetic complexity.

## 5. Properness can be restored only by a discontinuous arithmetic scale

PC-067 already shows that the chord eigenvalue determines the reduced denominator/exact order up to reflection, so the discontinuous Borel decoder

\[
C\chi_q=\operatorname{ord}(q\bmod\mathbb Z)\chi_q
\]

supplies a transverse arithmetic size. On the full solenoid this decoder alone is **not** proper: every integer `q\in\mathbb Z` has `\operatorname{ord}(q\bmod\mathbb Z)=1`, so its lowest energy ball already contains infinitely many characters.

Combining the transverse size with the archimedean one does give a proper example. Define

\[
L_{\rm ar}(q)=|q|+\operatorname{ord}(q\bmod\mathbb Z).
\]

If `L_{\rm ar}(q)\le R` and `q=a/n` is reduced with `n=\operatorname{ord}(q\bmod\mathbb Z)`, then `n\le R` and `|a|/n\le R`, hence `|a|\le Rn\le R^2`. Only finitely many reduced pairs `(a,n)` satisfy these bounds, so

\[
\boxed{
\#\{q\in\mathbb Q:L_{\rm ar}(q)\le R\}<\infty.
}
\]

Thus arithmetic properness is possible, but only after adding a discontinuous denominator/order scale to ordinary real-frequency growth. The provenance problem is exactly the point: this proper function is not selected by a locally regular joint symbol `F(A,B)`. More generally denominator, projective height, or finite-adic valuation can supply the needed discrete size, but they introduce the additional transverse arithmetic scale that PC-065 identified as missing and PC-066 showed was not fixed by abstract exact-order symmetry.

This does not mean such a scale is illegitimate. It means Prime Circle must **derive** it from an additional exact geometric operation before spectralization; selecting it because properness or a desired Dirichlet series results is an arbitrary spectral wrapper.

## 6. Prior art and novelty audit

The functional-analytic ingredients are classical and no historical novelty is claimed for the compact-resolvent criterion or length-function spectral triples.

A particularly close neighboring boundary is Carla Farsi, Therese Landry, Nadia S. Larsen and Judith A. Packer, **Spectral triples for noncommutative solenoids and a Wiener’s lemma**, *Journal of Noncommutative Geometry* 18:4 (2024), 1415–1452, DOI `10.4171/JNCG/557`, arXiv:2212.07470. They construct finitely summable spectral triples on noncommutative solenoids from length functions of bounded doubling. In their discrete-group formulation bounded doubling includes **properness**, i.e. finite metric balls, and their explicit `\mathbb Z[1/p]` length combines an archimedean absolute-value term with a `p`-adic size term. This is exactly the established neighboring pattern relevant here: solenoidal compact-resolvent geometry is restored by adding a non-archimedean/proper scale, not by a regular function of dense real frequency alone.

The project-specific content of PC-068 is the exact application of that properness boundary to the two canonical Prime-Circle operators already derived in PC-065 and PC-067. Targeted searches for solenoid spectral triples, leaf/transverse Dirac operators, and rational-frequency compactness did not identify this exact Prime-Circle joint-symbol no-go as an RH criterion or theorem. That absence is not a novelty proof.

The durable conclusion is a classification of a natural escape route, not a new spectral construction:

\[
\boxed{
\text{regular commuting leaf–fiber calculus}
\Rightarrow
\text{locally bounded energy on infinitely many rational characters}
\Rightarrow
\text{noncompact resolvent}.
}
\]

## 7. Boundary of the obstruction

PC-068 rules out only **translation-invariant commuting scalar calculus** generated by the canonical leaf operator and the compatible inverse-square transverse chord operator, when the joint symbol has at least one ordinary locally bounded noninteger point.

It does **not** rule out:

- a noncommuting leaf–fiber operator whose matrix entries mix different rational characters before diagonalization;
- a non-translation-invariant operator forced by the distinguished anchor or embedded old/new geometry;
- cross-level primitive/old couplings such as the extensive squarefree sector reopened by PC-047;
- nonlinear matrix or determinant data not reducible to scalar functional calculus of `A` and `B`;
- an independently derived finite-adic/height energy with geometric provenance;
- or the global primitive-root uniformization/accessory branch of PC-017.

The narrowed gate is

\[
\boxed{
\text{the missing ingredient is not another regular scalar combination of the known solenoid coordinates;}
\quad
\text{it must force arithmetic properness before commuting Fourier reduction.}
}
\]

## 8. Exact audit tests

The result has direct falsifiers.

1. Verify from the PC-064 exact sequence that restricting `\chi_q` to the anchor fiber depends only on `q\pmod{\mathbb Z}`.
2. Pull the PC-067 multiplier back along `\mathbb Q\to\mathbb Q/\mathbb Z` and recover `b(q)=\frac12\{q\}(1-\{q\})`.
3. Verify on every character that `B=b_0(A/2\pi)`.
4. For a diagonal real multiplier `E(q)`, prove compact resolvent is equivalent to finiteness of every set `{q:|E(q)|\le R}`.
5. Choose distinct rationals `q_j\to x` for one irrational noninteger `x` and verify that local boundedness of `F` at `\Gamma(x)` gives an infinite bounded-energy subsequence.
6. Test polynomial, continuous and rational examples and confirm the same failure at any regular irrational point.
7. Verify that the exact-order decoder alone is not proper on `\mathbb Q` because all integers have order `1`, while `|q|+\operatorname{ord}(q\bmod\mathbb Z)` has finite balls; confirm that this repair escapes the theorem only through its arithmetic discontinuity.

Failure of items 1–5 would invalidate the exact obstruction. A future leaf–fiber proposal escapes it only by leaving the stated commuting/regular class for a reason derived from Prime-Circle geometry itself.
