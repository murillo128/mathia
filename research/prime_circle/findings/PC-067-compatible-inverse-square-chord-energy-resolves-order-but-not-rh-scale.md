# PC-067 — compatible inverse-square chord energy resolves exact order but does not fix an RH scale

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-STRUCTURE` + `PRIOR-ART-REDIRECTION` + `DECISIVE-NEGATIVE` for using the canonical all-level inverse-square chord energy itself, or a regular scalar functional calculus of it, as the missing coercive transverse scale left open by PC-065/PC-066.

## Claim

PC-064 identifies the all-level compatible-circle completion with the arithmetic solenoid and its anchor fiber with `\widehat{\mathbb Z}`. PC-065 shows that the bare leafwise Laplacian is too soft at rational frequencies, while PC-066 shows that abstract transverse translation/unit symmetry fixes exact-order projectors but does not fix their spectral scale. A natural remaining possibility is that the **embedded Euclidean chord geometry** of the finite root sets breaks the abstract unit symmetry and canonically supplies that missing transverse scale.

For the inverse-square chord Laplacian already studied at finite level in PC-032/PC-039, there is indeed a unique refinement-compatible scalar normalization. Let

\[
(\mathcal L_n f)(a)
=\sum_{b\ne a}
\frac{f(a)-f(b)}{|\zeta_n^a-\zeta_n^b|^2},
\qquad a\in\mathbb Z/n\mathbb Z.
\]

If `m\ge1`, let

\[
J_{n,m}:\mathbb C^{\mathbb Z/n\mathbb Z}
\longrightarrow
\mathbb C^{\mathbb Z/mn\mathbb Z},
\qquad
(J_{n,m}f)(x)=f(x\bmod n),
\]

which is the pullback induced by the intrinsic power map `z\mapsto z^m` from the `mn`-th roots to the `n`-th roots. With normalized counting inner products these pullbacks are isometries.

Then

\[
\boxed{
Q_n:=\frac1{n^2}\mathcal L_n
}
\]

satisfies the exact compatibility law

\[
\boxed{
Q_{mn}J_{n,m}=J_{n,m}Q_n.
}
\]

Moreover this normalization is unique up to one global scalar among families `c_n\mathcal L_n` satisfying the same pullback law.

Therefore the embedded inverse-square chord energies define a bounded positive operator `Q_\perp` on the cylinder-function limit

\[
L^2(\widehat{\mathbb Z})
=\overline{\bigcup_n L^2(\mathbb Z/n\mathbb Z)}.
\]

On the character `\chi_\gamma`, `\gamma\in\mathbb Q/\mathbb Z`, choose its standard representative `r\in[0,1)`. The exact multiplier is

\[
\boxed{
Q_\perp\chi_\gamma
=
\sigma(\gamma)\chi_\gamma,
\qquad
\sigma(\gamma)=\frac12r(1-r).
}
\]

This is genuinely more geometric than the unit-invariant class of PC-066: `\sigma(a/n)` is not constant on the primitive residues modulo `n`, so the Euclidean embedding breaks `\widehat{\mathbb Z}^{\times}` symmetry.

But it does **not** supply the desired RH Hamiltonian. Its native spectrum is bounded in `[0,1/8]`, and the exact-order sequence `\gamma_n=1/n` satisfies

\[
\sigma(1/n)=\frac{n-1}{2n^2}\longrightarrow0.
\]

Thus the canonical chord energy makes growing conductor soft rather than coercive. It has no compact resolvent and its heat operator is never trace class.

There is, however, an important information-theoretic correction to a naive no-go: the multiplier does **not lose exact order**. Since

\[
r(1-r)=s(1-s)
\iff
s=r\ \text{or}\ s=1-r,
\]

and reflection preserves the denominator of a reduced rational, the eigenvalue `\sigma(\gamma)` determines `\operatorname{ord}(\gamma)`. Hence every exact-order projector `P_n` from PC-066 is a Borel spectral projector of `Q_\perp`, and the conductor operator itself can be recovered as a discontinuous Borel function:

\[
\boxed{
P_n=\mathbf 1_{S_n}(Q_\perp),
\qquad
C=\sum_{n\ge1}nP_n=F_{\rm ord}(Q_\perp),
}
\]

where

\[
S_n=
\left\{
\frac12\frac an\left(1-\frac an\right):
1\le a<n,\ (a,n)=1
\right\}.
\]

Consequently the embedded chord operator proves that conductor information is present in the transverse geometry, but obtaining a compact conductor Hamiltonian requires a highly discontinuous spectral recoding. That recoding returns exactly to the classical PC-066 trace

\[
\boxed{
\operatorname{Tr}(C^{-s})
=\sum_{n\ge1}\frac{\varphi(n)}{n^s}
=\frac{\zeta(s-1)}{\zeta(s)}.
}
\]

More generally every choice `h(n)` is equally available as the Borel function `h(C)=h(F_{\rm ord}(Q_\perp))`. The embedded chord spectrum therefore restores the **information** missing from abstract unit symmetry, but it still does not select a distinguished spectral scale, a gamma factor, an `s\leftrightarrow1-s` symmetry, or the critical line.

## 1. Exact compatibility fixes the `n^{-2}` normalization

PC-032 records the classical Fourier spectrum

\[
\mathcal L_n e_k
=\lambda_k^{(n)}e_k,
\qquad
\lambda_k^{(n)}=\frac{k(n-k)}2,
\qquad 0\le k<n,
\]

for

\[
e_k(a)=e^{2\pi ika/n}.
\]

Under `J_{n,m}`, the mode `e_k` becomes the frequency-`mk` mode at level `mn`:

\[
J_{n,m}e_k(x)
=e^{2\pi ikx/n}
=e^{2\pi i(mk)x/(mn)}.
\]

Therefore

\[
\lambda_{mk}^{(mn)}
=\frac{mk(mn-mk)}2
=m^2\lambda_k^{(n)}.
\]

Dividing by `(mn)^2` gives

\[
\frac{\lambda_{mk}^{(mn)}}{(mn)^2}
=
\frac{\lambda_k^{(n)}}{n^2},
\]

which proves `Q_{mn}J_{n,m}=J_{n,m}Q_n` on the Fourier basis and hence on the whole finite-level space.

Now suppose instead that `T_n=c_n\mathcal L_n` is any nonzero scalar normalization satisfying

\[
T_{mn}J_{n,m}=J_{n,m}T_n
\]

for all `m,n` with `n\ge2`. On any nonconstant Fourier mode,

\[
c_{mn}m^2\lambda_k^{(n)}=c_n\lambda_k^{(n)},
\]

so

\[
\boxed{c_{mn}=m^{-2}c_n.}
\]

Thus `c_n n^2` is unchanged on passage to a multiple. Given arbitrary `n,r\ge2`, compare both with `\operatorname{lcm}(n,r)` to obtain

\[
c_nn^2=c_rr^2.
\]

Hence

\[
\boxed{c_n=Cn^{-2}}
\]

for one global constant `C`. Compatibility itself fixes the geometric scaling exponent; `n^{-2}` is not chosen because it gives a convenient limit.

## 2. The compatible limit is a bounded embedded transverse multiplier

The inverse system

\[
\widehat{\mathbb Z}=\varprojlim_n\mathbb Z/n\mathbb Z
\]

has normalized Haar measure, and locally constant cylinder functions are the inductive union of the finite quotient spaces under the isometries `J_{n,m}`. The exact compatibility above therefore defines one operator on that dense union.

For the frequency represented by `\gamma=k/n\pmod1`, put `r\in[0,1)` for the corresponding reduced real representative. Then

\[
\frac{\lambda_k^{(n)}}{n^2}
=
\frac12\frac kn\left(1-\frac kn\right)
=
\frac12r(1-r),
\]

with the same value under every refinement representation `k/n=mk/(mn)`.

Since

\[
0\le\frac12r(1-r)\le\frac18,
\]

the cylinder operator is uniformly bounded and extends uniquely to a bounded positive self-adjoint operator

\[
\boxed{
0\le Q_\perp\le\frac18 I
\quad\text{on }L^2(\widehat{\mathbb Z}).
}
\]

The multiplier is not unit-invariant. For example at order five,

\[
\sigma(1/5)=\frac{2}{25},
\qquad
\sigma(2/5)=\frac{3}{25}.
\]

So this construction genuinely uses cyclic placement/chord geometry that PC-066 deliberately discarded when it imposed the full unit symmetry of the abstract profinite fiber.

## 3. Native chord energy is the wrong transverse coercivity

PC-065 left open the possibility that an embedded transverse term might penalize the rational soft modes `1/n` that destroy compactness of the leafwise Laplacian. The compatible inverse-square chord energy does the opposite:

\[
\boxed{
\sigma(1/n)=\frac{n-1}{2n^2}\sim\frac1{2n}.
}
\]

Thus there are infinitely many orthogonal nonconstant characters whose chord energy tends to zero as their exact order tends to infinity.

Because `Q_\perp` is bounded on an infinite-dimensional Hilbert space, no resolvent `(Q_\perp-z)^{-1}` with `z` outside the spectrum can be compact. Equivalently, for `t>0`,

\[
e^{-tQ_\perp}\ge e^{-t/8}I
\]

in the character basis, so

\[
\boxed{
\operatorname{Tr}(e^{-tQ_\perp})=\infty.
}
\]

The same obstruction applies to every continuous functional calculus `f(Q_\perp)`: a continuous function on the compact spectral interval `[0,1/8]` is bounded, so it cannot produce a proper compact-resolvent energy on infinitely many character modes.

More generally, a meromorphic/rational scalar transform with only finitely many singularities also cannot make the rational modes proper. Choose a nonempty subinterval of `(0,1/8)` away from those singularities. The set

\[
\{\sigma(\gamma):\gamma\in\mathbb Q/\mathbb Z\}
\]

is dense in `[0,1/8]`, so infinitely many character modes remain in a region where the transformed energy is bounded. Its resolvent is therefore still noncompact.

The missing conductor penalty cannot be obtained by an ordinary analytic reparametrization of the native chord energy.

## 4. Exact order is nevertheless spectrally recoverable

The previous failure is analytic, not informational.

Suppose

\[
\sigma(r)=\sigma(s),
\qquad r,s\in[0,1).
\]

Then

\[
r-r^2=s-s^2,
\]

hence

\[
(r-s)(1-r-s)=0.
\]

Therefore

\[
\boxed{s=r\quad\text{or}\quad s=1-r.}
\]

If `r=a/n` is reduced, both `r` and `1-r=(n-a)/n` have exact denominator `n`. Thus distinct exact orders have disjoint chord-eigenvalue sets `S_n`.

The exact-order decomposition from PC-066 can consequently be recovered from the spectral measure of `Q_\perp` alone:

\[
P_n=\mathbf1_{S_n}(Q_\perp).
\]

Each projector still has

\[
\operatorname{rank}P_n=\varphi(n).
\]

This is a useful correction to a simplistic "bounded chord energy loses arithmetic" interpretation. The embedded geometry contains the primitive-shell partition extremely faithfully; it just encodes that partition in a bounded dense spectral set rather than as a proper energy scale.

## 5. Discontinuous decoding recovers the classical conductor, not a selected RH Hamiltonian

Define on the pure-point spectrum of `Q_\perp`

\[
F_{\rm ord}(t)=n
\qquad\text{for }t\in S_n.
\]

The sets `S_n` are disjoint, so this is well-defined. It is necessarily very discontinuous because spectral points of arbitrarily large exact order are dense throughout `(0,1/8)`.

Borel functional calculus gives

\[
C=F_{\rm ord}(Q_\perp)
=\sum_{n\ge1}nP_n.
\]

This is exactly the conductor operator of PC-066, with compact resolvent and multiplicity `\varphi(n)` at eigenvalue `n`. Therefore

\[
\operatorname{Tr}(C^{-s})
=\frac{\zeta(s-1)}{\zeta(s)}
\]

in its convergence half-plane, with meromorphic continuation supplied by the classical zeta quotient.

The new embedded geometry does not remove PC-066's scale ambiguity. Once `C` is recoverable, every scalar assignment

\[
h:\mathbb N\to\mathbb R
\]

is equally recoverable as

\[
h(C)=\sum_n h(n)P_n,
\]

and hence as a Borel function of `Q_\perp`. In particular `C^\alpha` remains just as compatible with the recovered order partition as `C`, and its spectral zeta again moves the zeta denominator to `\zeta(\alpha s)`.

So the geometry fixes more than abstract symmetry—indeed it spectrally resolves exact order—but it still does not supply a principle selecting **which discontinuous function of that order** should be the Hamiltonian. Choosing the decoder because its trace contains `\zeta` would reproduce the arbitrary spectral-wrapper failure mode rather than solve it.

## 6. Prior-art and novelty audit

No historical novelty is claimed for the finite inverse-square matrix, Fourier diagonalization, profinite Fourier theory, or Borel functional calculus.

- Calogero and Perelomov, **Some Diophantine relations involving circular functions of rational angles**, *Linear Algebra and its Applications* 25 (1979), 91–94, is already recorded in `research/prime_circle/SOURCES.md` as the classical source boundary for the `\sin^{-2}` regular-polygon spectrum used in PC-032.
- PC-064 records the classical arithmetic-solenoid / `\widehat{\mathbb Z}` completion and its Pontryagin-dual description.
- PC-066 records the exact-order/Ramanujan projectors on `L^2(\widehat{\mathbb Z})` and the classical totient Dirichlet series `\zeta(s-1)/\zeta(s)`.
- The inverse-square chord interaction also lies in the classical long-range `1/\sin^2` family surrounding Calogero-Sutherland/Haldane-Shastry models; this reinforces rather than weakens the prior-art boundary around the finite operator.

Targeted searches for a profinite/solenoidal inverse limit of this exact root-of-unity `\csc^2` Laplacian, and for its use as an RH operator, did not locate a source asserting the project-specific compatibility/decoding conclusion above. That absence is not a novelty proof.

The durable Mathia contribution is therefore the exact **boundary result** obtained by combining already classical pieces in the canonical prime-circle refinement:

\[
\boxed{
\text{embedded inverse-square chord geometry}
\xrightarrow[\text{unique scale}]{\text{refinement compatibility}}
Q_\perp
\xrightarrow{\text{spectral measure}}
\{P_n\}
}
\]

while simultaneously proving

\[
\boxed{
Q_\perp\text{ is bounded/soft, and a compact conductor scale appears only after discontinuous order decoding.}
}
\]

## 7. Consequence for the research frontier

This closes a specific escape left by PC-065/PC-066: the most canonical embedded **inverse-square chord** refinement does not itself provide the transverse coercivity needed to turn the rational solenoid frequencies into a compact-resolvent RH spectrum. Refinement compatibility uniquely normalizes the finite operator into a bounded multiplier, and regular scalar functional calculus cannot reverse that analytic failure.

At the same time, the result says not to discard embedded chord geometry as information-poor. Its eigenvalues already separate exact order up to reflection, so a future mechanism need not invent a new prime label. What remains genuinely open is a construction that uses this embedded order-resolving geometry in a **nonseparable** way—coupled to the leaf coordinate, to old/new blocks, or across several levels—so that the spectral scale is forced by an operator law rather than by a discontinuous post-processing of a diagonal multiplier.

This finding does **not** rule out:

- a noncommuting leaf–fiber operator formed before simultaneous diagonalization;
- an old/new or primitive-shell cross-level operator not reducible to the complete cyclic quotient `\mathbb Z/n\mathbb Z`;
- nonlinear geometry whose energy is not a scalar function of `Q_\perp`;
- a several-level determinant/Gram construction with intrinsically fixed dilation weights;
- or the global uniformization/accessory-parameter branch of PC-017.

The narrowed gate is:

\[
\boxed{
\text{the missing ingredient is not access to conductor information; it is a geometrically forced coercive law for using it.}
}
\]

## 8. Exact audit tests

The result is directly falsifiable.

1. For finite `n`, verify the Fourier eigenvalues `\lambda_k^{(n)}=k(n-k)/2` of `\mathcal L_n`.
2. Pull a mode `k` from level `n` to level `mn` and verify it becomes frequency `mk` and its unnormalized eigenvalue scales by exactly `m^2`.
3. Verify `Q_{mn}J_{n,m}=J_{n,m}Q_n` for `Q_n=n^{-2}\mathcal L_n`.
4. Assume a scalar-compatible family `c_n\mathcal L_n` and derive `c_{mn}=m^{-2}c_n`; compare through least common multiples to prove `c_n=Cn^{-2}`.
5. On `\gamma=a/n`, verify the limit multiplier `\sigma(\gamma)=\tfrac12r(1-r)` and the bound `0\le\sigma\le1/8`.
6. Use `\gamma_n=1/n` to verify `\sigma(\gamma_n)\to0` despite `\operatorname{ord}(\gamma_n)=n\to\infty`.
7. Solve `\sigma(r)=\sigma(s)` and verify the only ambiguity is reflection `s=1-r`, which preserves exact denominator.
8. Check that the finite sets `S_n` are pairwise disjoint and that `\mathbf1_{S_n}(Q_\perp)` has rank `\varphi(n)`.
9. Apply the order decoder and recover exactly the PC-066 conductor trace `\zeta(s-1)/\zeta(s)`.

Failure of items 2–4 would invalidate the claimed canonical refinement scaling. Failure of items 7–8 would invalidate the claim that chord spectrum resolves exact order. A future RH mechanism evades the negative conclusion only by deriving a coercive/nonseparable operator law beyond regular scalar functional calculus of this compatible chord multiplier.